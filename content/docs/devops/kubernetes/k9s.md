# K9s

- [Home page](https://k9scli.io/)
- [GitHub repository](https://github.com/derailed/k9s)
- [Releases](https://github.com/derailed/k9s/releases)

## Installation

{{< tabs "k9s-setup" >}}

{{< tab "Windows" >}}

```pwsh
$K9s_Version = "0.27.4"

$K2s_Archive = "https://github.com/derailed/k9s/releases/download/v${K9s_Version}/k9s_Windows_amd64.zip"
Invoke-WebRequest -Uri $K2s_Archive -OutFile "${pwd}/k9s_Windows_amd64_${K9s_Version}.zip"

Add-Type -Assembly System.IO.Compression.FileSystem
$zip = [IO.Compression.ZipFile]::OpenRead("${pwd}/k9s_Windows_amd64_${K9s_Version}.zip")
$Executables = $zip.Entries | Where-Object {$_.Name -like '*.exe'}
foreach ($Executable in $Executables) {
    [System.IO.Compression.ZipFileExtensions]::ExtractToFile($Executable, "${pwd}/$($Executable.Name)", $True)
}
$zip.Dispose()
Remove-Item -Path "${pwd}/k9s_Windows_amd64_${K9s_Version}.zip"
```

{{< /tab >}}

{{< tab "Linux" >}}
TODO
{{< /tab >}}

{{< /tabs >}}
