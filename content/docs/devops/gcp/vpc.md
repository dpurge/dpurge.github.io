# VPC

VPC = Virtual Private Cloud

VPC is a virtualized, software defined network within Google Cloud.

VPC network, its routes and firewall rules are global resources, not associated with any particular region or zone.

VPC is encapsulated within a project.

VPCs do not have any IP address ranges associated with them.
IP adress ranges are defined within subnetworks associated with VPC.
Subnetworks are regional.

Network firewall rules control traffic flowing in and out of the VPC.

Resources within a VPC can communicate with one another by using their internal (priovate) IPv4 addresses.

VPCs only support IPv4 addresses (nodes can only send and receive IPv4 traffic).
It is possible to create IPv6 address for a global load balancer.

Each project comes with a default VPC network `10.128.0.0/9` that has a route to the default internet gateway and by default is in *auto mode*.
There are two network types: subnet creation *auto mode* or *custom mode*.

*Auto mode* networks automatically create a `/20` subnet in each region.
As new regions become available, new subnets are automatically added.
Conversion from *auto mode* to *custom mode* is one-way.
You cannot convert back; *custom mode* networks cannot be changed back to *auto mode* mentworks.

Traffic cannot pass between separate networks unless you set up VPC peering or use a VPN connection.

## VPC network subnets

A VPC network consists of one or more subnets; each subnet is associated with a region.

The name or region of a subnet cannot be changed after you have created it.
You have to delete a subnet (no resources may be using it) and create it again.

Primary and secondary ranges for subnets cannot overlap with any allocated range in other subnets or peered networks.

Subnet address range can be increased: it must not overlap with other subnets, must stay inside the RFC 1918 adress-space, must be larger than the original.
You cannot undo the expansion.
`/20` range can be expanded to the `/16` range, but not larger.
You have to convert to a *custom mode* to increase the range any further.

### IP addresses reserved for Google

There are 4 reserved IP addresses (first two and last two in the CIDR range) in its primary IP range:

1. network (first)
2. default gateway (second)
3. future use (second-to-last)
4. broadcast (last)

There are no reserved IP addresses in the secondary IP range.

## Routing and Private Google Access

Routes define the network traffic path from one destination to the other.

In a VPC route consists of a single CIDR destination and a single next hop.

All routes are stored in the routing table for the VPC.

Each packet leaving a VM is delivered to the next hop of an applicable route based on a routing order.

There are two routing types:

System generated
: default, subnet route

Custom routes
: static route (created manually), dynamic route (maintained automatically by cloud routers)

### Default route

- path to the internet
- path for *Private Google Access*
- can be deleted only by replacing with custom route
- it has the lowest priority

### Subnet route

- define paths to each subnet in the VPC
- each subnet has at least one subnet route whose destination matches the primary IP range of the subnet
- when a subnet is created, a corresponding subnet route is created for both primary and secondary IP range
- you cannot delete a subnet route unless you modify or delete the subnet; when you delete a subnet, all its subnet routes are deleted automatically

### Static route

- can use the next hop feature
- can be created manually
- static routes for the remote traffic selectors are created automatically when creating Cloud VPN tunnels

Every route in the project must have a unique name.
Priorities are from `0` to `1000`, lower number have higher priority.

### Dynamic route

- managed by one or more Cloud Routers
- dynamically exchange routes between a VPC and on-premises networks
- destination IP ranges outside the VPC network
- used with dynamically routed VPNs and Interconnect

## Create VPC with gcloud

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

## VPC with Private Google Access

Private access = access to a VM without a public IP access.

Create VPC:

```sh
gcloud compute networks create mynetwork --project=myproject --description=... --subnet-mode=custom --bgp-routing-mode=regional

gcloud compute networks subnets create public --project=myproject --range=10.0.0.0/24 --network=mynetwork --region=us-east1

gcloud compute networks subnets create private --project=myproject --range=10.0.5.0/24 --network=mynetwork --region=us-east4
```

Set up cloud storage:

```sh
# todo
```

Set up VM instances:

```sh
gcloud beta compute --project=myproject instances create public-instance --zone=us-east1-b --machine-type=e2-micro --subnet=public --network-tier=PREMIUM --maintenance-policy=MIGRATE --service-account=... --scopes=https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/trace.append,https://www.googleapis.com/auth/devstorage.read_write --tags=public --image=debian-10-buster-v20200910 --image-project=debian-cloud --boot-disk-size=10GB --boot-disk-type=pd-standard --boot-disk-device-name=public-instance --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --labels=env=public --reservation-affinity=any

# add another machine private-instance in the private subnet without public IP
```

Add firewall rules allowing ssh and icmp access:

```sh
# todo
```

On the public machine, check access to the storage:

```sh
gsutil ls gs://mybucket-test-access
```

Check ssh from public to the private instance:

```sh
gcloud compute ssh --project myproject --zone us-east4-c private-instance --internal-ip
```

Enable private gGoogle accees on the private network:

```sh
# todo
```

## VPC network peering

VPC peering is a service allowing two VPC networks to communicate privately without passing the traffic through the public Internet. (RFC 1918)

All the traffic stays within Google's network.

Peering can be established between the same or different projects and organizations.

As compared to VPN:

- reduces network latency
- increases network security
- reduces network costs

Characteristics:

- peered networks remain administratively separate (routes, firewalls, vpn are applied separately)
- connection established for each VPC separately, configuration on both sides has to match, each side can break the peering at any time
- VPC peers always exchange all subnet routes
- a VPC can peer with many networks, but quotas apply
- CIDR range in one network cannot overlap with a static route in another network.
- to allow ingress traffic from VM instances in a peer network, you must create ingress allow firewall rules (by default ingress traffic to VMs is blocked by the implied deny ingress rule)
- transitive peering is not supported (networks must be peered directly to allow traffic)
- you cannot use a tag or a service account in one peered network in another peered network
- internal DNS is not accessible for compute engine in peered networks
