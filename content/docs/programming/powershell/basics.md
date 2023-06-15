# Powershell basics

## Get unix timestamp

```pwsh
[int](Get-Date -UFormat %s -Millisecond 0)
```
