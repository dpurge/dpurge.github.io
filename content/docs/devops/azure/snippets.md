# Snippets

```sh
az group create -g $group -l northeurope

az vm create \
  -n vm1 \
  -g $group \
  -l northeurope \
  --image Win2019Datacenter \
  --admin-username $username \
  --admin-password $password \
  --nsg-rule rdp

az appservice plan create \
  -n web-plan \
  -g $group \
  -l northeurope \
  --sku S1

az webapp create \
  -n $appname \
  -g $group \
  -p web-plan

az webapp list -g $group --query "[].enabledHostNames" -o jsonc

az group delete -g $group
```
