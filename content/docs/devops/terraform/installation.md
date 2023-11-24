# Installation

{{< tabs "tf-setup" >}}

{{< tab "Linux" >}}

Install `tfswitch`:

```sh
export TFSWITCH_VERSION=0.13.1300
curl \
    -sSL https://github.com/warrensbox/terraform-switcher/releases/download/${TFSWITCH_VERSION}/terraform-switcher_${TFSWITCH_VERSION}_linux_amd64.tar.gz \
    -o /tmp/tfswitch_linux_amd64.tar.gz
tar --directory=/usr/local/bin -xf /tmp/tfswitch_linux_amd64.tar.gz tfswitch
rm /tmp/tfswitch_linux_amd64.tar.gz
```

Install `terraform`:

```sh
tfswitch 1.3.7
```

Install `tflint`:

```sh
export TFLINT_VERSION=0.38.1
curl \
    -sSL https://github.com/terraform-linters/tflint/releases/download/v${TFLINT_VERSION}/tflint_linux_amd64.zip \
    -o /tmp/tflint_linux_amd64.zip
cd /usr/local/bin
unzip /tmp/tflint_linux_amd64.zip
rm /tmp/tflint_linux_amd64.zip
```

{{< /tab >}}

{{< tab "MacOS" >}}
```sh
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```
{{< /tab >}}

{{< tab "Windows" >}}
$tf_version = "1.6.4"
$tf_archive = "https://releases.hashicorp.com/terraform/${tf_version}/terraform_${tf_version}_windows_amd64.zip"
Invoke-WebRequest -Uri $tf_archive -OutFile "${pwd}/terraform_${tf_version}_windows_amd64.zip"

Add-Type -Assembly System.IO.Compression.FileSystem
$zip = [IO.Compression.ZipFile]::OpenRead("${pwd}/terraform_${tf_version}_windows_amd64.zip")
$Executables = $zip.Entries | Where-Object {$_.Name -like '*.exe'}
foreach ($Executable in $Executables) {
    [System.IO.Compression.ZipFileExtensions]::ExtractToFile($Executable, "${pwd}/$($Executable.Name)", $True)
}
$zip.Dispose()
Remove-Item -Path "${pwd}/terraform_${tf_version}_windows_amd64.zip"
{{< /tab >}}

{{< /tabs >}}