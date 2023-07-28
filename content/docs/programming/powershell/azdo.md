# Azure DevOps

## URIs and authentication header

```pwsh
$AccessToken = $env:AZDO_ADMIN_TOKEN
$Organization = "MyOrganization"

$AuthenicationHeader = @{
    Authorization = 'Basic ' + [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(":${AccessToken}"))
}

$OrganizationUri = "https://dev.azure.com/${Organization}/" 
$ProjectsUri = "${OrganizationUri}_apis/projects?api-version=5.1"
$RepositoriesUri = "${OrganizationUri}_apis/git/repositories?api-version=7.0"
```

## AzDO projects

```pwsh
$Projects = Invoke-RestMethod -Uri $ProjectsUri -Method get -Headers $AuthenicationHeader

foreach ($Project in $Projects.Value) {
    $ProjectName = $Project.name
    $ProjectUri  = $Project.url
    Write-Host "${ProjectName}: ${ProjectUri}"
}
```

## AzDO repositories

```pwsh
$Repositories = Invoke-RestMethod -Uri $RepositoriesUri -Method get -Headers $AuthenicationHeader

foreach ($Repository in $Repositories.value) {
    $ProjectName = $Repository.Project.name
    $RepositoryName = $Repository.name
    $RepositoryWebUri = $Repository.webUrl
    $RepositoryIsActive = -not $Repository.IsDisabled
    if ($RepositoryIsActive) {
        $Folder = Join-Path -Path $PWD -ChildPath $ProjectName
        if (-not (Test-Path $Folder)) {
            New-Item $Folder -ItemType Directory | Out-Null
        }
        Push-Location -Path $Folder
        Write-Host "${ProjectName}/${RepositoryName} ..."
        git clone --depth 1 $RepositoryWebUri
        Pop-Location
    }
}
```