# GCloud

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
gcloud auth list
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
gcloud components install COMPONENT  # COMPONENT: compute, appengine or kubernetes etc..
gcloud components remove COMPONENT  # remove a component from the installation, e.g., gcloud compute
gcloud components update
```

## Switch project

```sh
gcloud projects list
gcloud config get-value project
gcloud config set project PROJECT_ID  # replace with your Project ID.
```
