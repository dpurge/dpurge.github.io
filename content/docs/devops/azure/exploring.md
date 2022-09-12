# Exploring Azure resources

## List subscription and tenant

```sh
az account show --query "{subscriptionId:id, tenantId:tenantId}" -o table
```

## Create service principal for RBAC

```sh
az ad sp create-for-rbac --role Contributor --name my-name-001 --scope /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

## Find VM images

```sh
az vm image list-offers --publisher Canonical --location westeurope -o table

az vm image list-skus --publisher Canonical --offer 0001-com-ubuntu-server-jammy --location westeurope -o table

az vm image list --all --publisher Canonical --offer 0001-com-ubuntu-server-jammy --sku 22_04-lts --location westeurope -o table
```

Refer to this image: `Canonical:0001-com-ubuntu-server-jammy:22_04-lts`

## List public and private IP

For current subscription:

```sh
az vm list -d --query "[].{Name:name, PublicIPs:publicIps, PrivateIPs:privateIps}" -o table
```

For all subscriptions:

```sh
for i in `az account list --query "[].{id:id}" --output tsv`; do az account set --subscription $i; az vm list -d --query "[].{Name:name, PublicIPs:publicIps, PrivateIPs:privateIps}" --output tsv; done
```