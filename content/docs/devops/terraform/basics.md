# Basic commands

## Resource management

```sh
terraform init
terraform plan
terraform apply
terraform destroy
```

## Work with code

```sh
terraform validate
terraform fmt
```

## Work with state

```sh
terraform state list
terraform state mv
terraform state show
terraform state rm \<type\>.\<resource\>
```

Examples:

```pwsh
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String((kubectl get secret api-secret -o jsonpath='{.data.db-connectionstring}')))
terragrunt plan -var-file secrets.tfvars --terragrunt-log-level debug
az ad group show --group xxx-Contributors --query id --output tsv
```
