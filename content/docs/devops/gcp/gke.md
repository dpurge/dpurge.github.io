# GKE

[source: Anton Putra GitHub repo](https://github.com/antonputra/tutorials/blob/main/lessons/069/)

```tf
# 0-provider.tf

provider "google" {
    region     = "us-west2"
}

resource "random_integer" "this" {
    min = 100
    max = 1000000
}

terraform {
    required_providers {
        google = {
            source = "hashicorp/google"
            version = "~> 3.66"
        }

        random = {
            source = "hashicorp/random"
            version = "~> 3.1"
        }
    }
}
```

```tf
# 1-locals.tf

locals {
    region = "us-west2"
    org_id = "..."
    billing_account = "..."
    host_project_name = "host-staging"
    service_project_name = "k8s-staging"
    host_project_id = "${local.host_project_name}-${random_integer.this.result}"
    service_project_id = "${local.service_project_name}-${random_integer.this.result}"
    projects_api = "container.googleapis.com"
    secondary_ip_ranges = {
        "pod-ip-range" = "10.0.0.0/14",
        "services-ip-range" = "10.4.0.0/19"
    }
}
```

```tf
# 2-projects.tf

resource "google_project" "host-staging" {
    name = local.host_project_name
    project_id = local.host_project_id
    billing_account = local.billing_account
    org_id = local.org_id
    auto_create_network = false
}

resource "google_project" "k8s-staging" {
    name = local.service_project_name
    project_id = local.service_project_id
    billing_account = local.billing_account
    org_id = local.org-id
    auto_create_network = false
}

resource "google_project_service" "host" {
    project = google_project.host-staging.number
    service = local.projects_api
}

resource "google_project_service" "service" {
    project = google_project.k8s-staging.number
    service = local.projects_api
}
```

```tf
# 3-vpc.tf

resource "google_compute_network" "main" {
    name  = "main"
    project = google_compute_shared_vpc_hosts_project.host.project
    auto_create_subnetworks = false
    routing_mode = "REGIONAL"
    mtu = 1500
}

resource "google_compute_subnetwork" "private" {
    name = "private"
    project = google_compute_shared_vpc_hosts_project.host.project
    ip_cidr_range = "10.5.0.0/20"
    region = local.region
    network = google_compute_network.main.self_link
    private_ip_google_access = true

    dynamic "secondary_ip_range" {
        for_each = local.secondary_ip_ranges

        content {
            range_name = secondary_ip_range.key
            ip_cidr_range = secondary_ip_range.value
        }
    }
}
```

```tf
# 4-router.tf

resource "google_compute_router" "router" {
    name = "router"
    region = local.region
    project = local.hosts_project_id
    network = google_compute_network.main.self_link
}
```

```tf
# 5-nat.tf

resource "google_compute_router_nat" "mist_nat" {
    name = "nat"
    project = local.hosts_project_id
    router = google_compute_router.router.name
    region = local.region
    nat_ip_allocate_option = "AUTO_ONLY"
    source_subnetwork_ip_ranges_to_nat = "ALL_SUBNETWORKS_ALL_IP_RANGES"

    depends_on = [google_compute_subnetwork.private]
}
```

```tf
# 6-shared-vpc.tf

resource "google_compute_shared_vpc_host_project" "host" {
    project = google_project.host-staging.number
}

resource "google_compute_shared_vpc_service_project" "service" {
    host_project = local.host_project_id
    service_project = local.service_project_id

    depends_on = [google_compute_shared_vpc_host_project.host]
}

resource "google_compute_subnetwork_iam_binding" "binding" {
    project = google_compute_shared_vpc_host_project.host.project
    region = google_compute_subnetwork.private.region
    subnetwork = google_compute_subnetwork.private.name

    role = "roles/compute.networkUser"
    members = [
        "serviceAccount:${google_service_account.k8s-staging.email}",
        "serviceAccount:${google_project.k8s-staging.number}@cloudservices.gserviceaccount.com",
        "serviceAccount:service-${google_project.k8s-staging.number}@container-engine-robot.iam.gserviceaccount.com"
    ]
}

resource "google_project_iam_binding" "container-engine" {
    project = google_compute_shared_vpc_host_project.host.project
    role    = "roles/container.hostServiceAgentUser"

    members = [
        "serviceAccount:service-${google_project.k8s-staging.number}@container-engine-robot.iam.gserviceaccount.com",
    ]
    depends_on = [google_project_service.service]
}
```

```tf
# 7-kubernetes.tf

resource "google_service_account" "k8s-staging" {
  project    = local.service_project_id
  account_id = "k8s-staging"

  depends_on = [google_project.k8s-staging]
}

resource "google_container_cluster" "gke" {
  name     = "gke"
  location = local.region
  project  = local.service_project_id

  networking_mode = "VPC_NATIVE"
  network         = google_compute_network.main.self_link
  subnetwork      = google_compute_subnetwork.private.self_link

  remove_default_node_pool = true
  initial_node_count       = 1

  release_channel {
    channel = "REGULAR"
  }

  ip_allocation_policy {
    cluster_secondary_range_name  = "pod-ip-range"
    services_secondary_range_name = "services-ip-range"
  }

  network_policy {
    provider = "PROVIDER_UNSPECIFIED"
    enabled  = true
  }

  private_cluster_config {
    enable_private_endpoint = false
    enable_private_nodes    = true
    master_ipv4_cidr_block  = "172.16.0.0/28"
  }

  workload_identity_config {
    identity_namespace = "${google_project.k8s-staging.project_id}.svc.id.goog"
  }

}

resource "google_container_node_pool" "general" {
  name       = "general"
  location   = local.region
  cluster    = google_container_cluster.gke.name
  project    = local.service_project_id
  node_count = 1

  management {
    auto_repair  = true
    auto_upgrade = true
  }

  node_config {
    labels = {
      role = "general"
    }
    machine_type = "e2-medium"

    service_account = google_service_account.k8s-staging.email
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}
```

```sh
gcloud auth application-default login
terraform fmt
terraform init
terraform validate
terraform plan
terraform apply

gcloud container clusters get-credentials gke --region us-west2 --project k8s-staging-000000
kubectl get svc
kubectl get nodes
```

Example load balacer in Kubernetes:

```yaml
# 0-deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

```yaml
# 1-service.yaml
---
apiVersion: v1
kind: Service
metadata:
  name: nginx
  namespace: default
spec:
  type: LoadBalancer  
  ports:
  - protocol: TCP
    port: 80
  selector:
    app: nginx
```

```sh
kubectl apply -f .
kubectl get pods
kubectl get svc
```

Public IP address of the LoadBalancer is not accessible on the public internet.

Create firewall rules go open access:

```sh
kubectl describe svc nginx
```

You can copy `gcloud` command to create firewall rules, or create them with terraform.

```tf
# 8-firewall.tf

resource "google_compute_firewall" "lb" {
  name        = "k8s-fw-...."
  network     = google_compute_network.main.name
  project     = local.host_project_id
  description = "{\"kubernetes.io/service-name\":\"default/nginx\", \"kubernetes.io/service-ip\":\"....\"}"

  allow {
    protocol = "tcp"
    ports    = ["80"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["gke-gke-...-node"]
}

resource "google_compute_firewall" "health" {
  name        = "k8s-...-node-http-hc"
  network     = google_compute_network.main.name
  project     = local.host_project_id
  description = "{\"kubernetes.io/cluster-id\":\"...\"}"

  allow {
    protocol = "tcp"
    ports    = ["10256"]
  }

  source_ranges = ["130.211.0.0/22", "209.85.152.0/22", "209.85.204.0/22", "35.191.0.0/16"]
  target_tags   = ["gke-gke-...-node"]
}
```

```sh
terraform apply

kubectl get svc
# EXTERNAL-IP should be now accessible
```
