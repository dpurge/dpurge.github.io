# VPC

Create regional network with custom subnets.

Public subnet will have a default internet gateway.

Private subnet will have NAT gateway as its route.

```sh
gcloud compute networks create main --bgp-routing-mode=regional --subnet-mode=custom
```

Add public subnet:

```sh
gcloud compute networks subnets create public --range=10.0.0.0/24 --network=main --region=us-west2
```

Create private subnet:

```sh
gcloud compute networks subnets create private --range=10.0.1.0/24 --network=main --region=us-west2 --enable-private-ip-google-access
```

Create cloud router:

```sh
gcloud compute routers create router --network=main --region=us-west2
```

Create cloud NAT gateway and select IP ranges:

```sh
gcloud compute routers nats create nat --router=router --region=us-west2 --nat-custom-subnet-ip-ranges=private --auto-allocate-nat-external-ips
```

## Create VPC with terraform

First create a service account to be used with terraform and download credentials.

```tf
provider "google" {
    credentials = file("~/google-credentials.json")
    project = "my-project"
    region = "us-west2"
}

# main VPC
resource "google_compute_network" "this" {
    name = "main"
    auto_create_subnetworks = false
}

# public subnet
resource "google_compute_subnetwork" "public" {
    name = "public"
    ip_cidr_range = "10.0.0.0/24"
    region = "us-west2"
    network = google_compute_network.this.id
}

# private subnet
resource "google_compute_subnetwork" "public" {
    name = "private"
    ip_cidr_range = "10.0.1.0/24"
    region = "us-west2"
    network = google_compute_network.this.id
}

# cloud router
resource "google_compute_router" "this" {
    name = "router"
    network = google_compute_network.this.id
    bgp {
        asn = 64514
        advertise_mode = "CUSTOM"
    }
}

# NAT gateway
resource "google_compute_router_nat" "this" {
    name = "nat"
    router = google_compute_router.this.name
    region = google_compute_router.this.region
    nat_ip_allocate_option = "AUTO_ONLY"
    source_subnetwork_ip_ranges_to_nat = "LIST_OF_SUBNETWORKS"

    subnetwork {
        name = "private"
        source_ip_ranges_to_nat = ["ALL_IP_RAGES"]
    }
}
```
