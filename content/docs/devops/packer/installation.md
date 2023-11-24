# Installation


{{< tabs "packer-setup" >}}

{{< tab "Windows" >}}
$pkr_version = "1.9.4"
$pkr_archive = "https://releases.hashicorp.com/packer/${pkr_version}/packer_${pkr_version}_windows_amd64.zip"
Invoke-WebRequest -Uri $pkr_archive -OutFile "${pwd}/packer_${pkr_version}_windows_amd64.zip"

Add-Type -Assembly System.IO.Compression.FileSystem
$zip = [IO.Compression.ZipFile]::OpenRead("${pwd}/packer_${pkr_version}_windows_amd64.zip")
$Executables = $zip.Entries | Where-Object {$_.Name -like '*.exe'}
foreach ($Executable in $Executables) {
    [System.IO.Compression.ZipFileExtensions]::ExtractToFile($Executable, "${pwd}/$($Executable.Name)", $True)
}
$zip.Dispose()
Remove-Item -Path "${pwd}/packer_${pkr_version}_windows_amd64.zip"
{{< /tab >}}

{{< tab "Linux" >}}
```sh
export PACKER_VERSION=1.7.10
curl \
    -sSL https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip \
    -o /tmp/packer_linux_amd64.zip
cd /usr/local/bin
unzip /tmp/packer_linux_amd64.zip
rm /tmp/packer_linux_amd64.zip
```
{{< /tab >}}

{{< /tabs >}}



Example:

```sh
packer validate src/build-agent-ubuntu.pkr.hcl
packer build src/build-agent-ubuntu.pkr.hcl
```