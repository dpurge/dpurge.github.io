# GCloud

## Console

[Cloud console](https://console.cloud.google.com/)

## Install

[Google documentation](https://cloud.google.com/sdk/docs/install-sdk)

```sh
# using snapcraft
sudo systemctl status snapd
snap search google-cloud-sdk
sudo snap install google-cloud-sdk --classic
sudo snap remove google-cloud-sdk
rm -rf ~/.config/gcloud

# check
which gcloud
which gsutil
which bq

gcloud version
gcloud help
```

## Initialize environment

```sh
gcloud init 
# or: gcloud init --console-only
```

To switch active account:

```sh
gcloud auth list
gcloud config set account dpurge@example.com
```

## Get information

```sh
gcloud info
gcloud config list
gcloud config configurations list
```

## Modify installation

```sh
gcloud components list
gcloud components install COMPONENT
gcloud components remove COMPONENT
gcloud components update
```

## Beta commands interactive shell

```sh
gcloud components install beta
gcloud beta interactive
```

## Switch project

```sh
gcloud projects list
gcloud config get-value project
gcloud config set project PROJECT_ID
```

## Switch account

```sh
gcloud config configurations list
gcloud config configurations activate ACCOUNT
ls ~/.config/gcloud/configurations
gcloud config configurations describe ACCOUNT
# you can delete non-active configuration
gcloud config configurations delete ACCOUNT
```

## Connect to Cloud Shell

```sh
# create key-pair and connect
gcloud alpha cloud-shell ssh
```

## Create a VPC

In Google Cloud VPC is global, it spans multiple regions.
Subnets are regional and span multiple zones within a region.
This is different from AWS.

Subnets have unique names across all VPCs.
You need to allow access to the subnet by creating firewall rules.

```sh
gcloud compute networks create vpc-1 --description "Testing" --subnet-mode custom
gcloud compute firewall-rules create vpc1-fw-allow-ssh --network vpc-1 --allow tcp:22
gcloud compute networks subnets create vpc1-euw2-1 --network vpc-1 --region europe-west2 --range 10.0.1.0/24

gcloud compute networks list
gcloud compute networks subnets list
gcloud compute networks subnets list --network vpc-1
```

Subnets and networks can be deleted if there are no resources running in them.

```sh
gcloud compute networks subnets delete vpc1-euw2-1 --region europe-west2
gcloud compute firewall-rules delete vpc1-fw-allow-ssh
gcloud compute networks delete vpc-1
```

## Virtual machines

Connect to the VM:

```sh
gcloud compute instances list
gcloud compute ssh vm-1
```

Stop the VM before creating a disk snapshot.

```sh
# todo
```

## Managed instance groups

- create instance template
- create instance groups and add instances to it

```sh
# todo
# gcloud compute instance-templates create my-template --image-family centos-7 --machine-type f2-micro
# gcloud compute target-pools create MY_POOL --target-http-proxies PROXY
# gcloud compute instance-groups managed create my-ig --zone us-central1-a —target-size TARGET_SIZE
```

## Instance group autoscaling

```sh
# todo
```
