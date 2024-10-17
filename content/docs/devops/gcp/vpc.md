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
