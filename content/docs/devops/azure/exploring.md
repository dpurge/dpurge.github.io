# Exploring Azure resources

## List subscription and tenant

```sh
az account show --query "{subscriptionId:id, tenantId:tenantId}" -o table
```

```sh
az login
az account subscription list
```

## Create service principal for RBAC

```sh
az ad sp create-for-rbac --role Contributor --name my-name-001 --scope /subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

```sh
az cloud set -n AzureCloud
az login --service-principal -u *** --password=*** --tenant xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx --allow-no-subscriptions
az account set --subscription xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
az aks get-credentials --resource-group $(ResourceGroup) --name $(KubernetesService)
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

Examples:

```sh
az vmss show --resource-group ResGrp-xxx --name DEV-VMSS001 --query [sku] --output table
az acr login --name dockercr001
```

```pwsh
Invoke-RestMethod -Headers @{"Metadata"="true"} -Method GET -NoProxy -Uri "http://x.x.x.x/metadata/instance?api-version=2021-02-01" | ConvertTo-Json -Depth 64
$env:ARM_ACCESS_KEY = $(az storage account keys list --resource-group ResGrp-Terraform --account-name xxxx --query '[0].value' -o tsv)
if ((kubectl get ns -o jsonpath='{.items[*].metadata.name}').split(' ') -contains 'keda') {"Keda is installed"}
```

```pwsh
$ctx = (Get-AzStorageAccount -ResourceGroupName ResGrp-xxx -Name xxx).Context
$StgTable = Get-AzStorageTable -Name xxx -Context $Ctx
foreach ($Row in (Get-AzTableRow -table $StgTable.CloudTable)) {
 $VMSize = $Row.VMSize
 $BuildTime = $Row.FinishTime - $Row.StartTime
 Write-Host ('{0}: {1:hh} hr {1:mm} min {1:ss} sec' -f $VMSize,$BuildTime)
}
```
