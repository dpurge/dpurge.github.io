# Installation

{{< tabs "go-setup" >}}

{{< tab "Linux" >}}

On Ubuntu, remove system packages:

```sh
sudo apt purge golang*
```

Install Go:

```sh
wget https://go.dev/dl/go1.24.4.linux-amd64.tar.gz
tar -C /opt/ -xzf go1.24.4.linux-amd64.tar.gz
mkdir ~/.go
```

Setup `~/.profile`:

```sh
if [ -d "/opt/go" ] ; then
    export GOROOT=/opt/go
    PATH="$GOROOT/bin:$PATH"
fi

if [ -d "$HOME/.go" ] ; then
    export GOPATH="$HOME/.go"
    PATH="$GOPATH/bin:$PATH"
fi
```

On Ubuntu, you may install as alternative:

```sh
sudo update-alternatives --install "/usr/bin/go" "go" "/usr/local/go/bin/go" 0
sudo update-alternatives --set go /usr/local/go/bin/go
```

{{< /tab >}}

{{< tab "Windows" >}}

```pwsh
$go_version = "1.21.4"
$go_archive = "https://dl.google.com/go/go${go_version}.windows-amd64.zip"
Invoke-WebRequest -Uri $go_archive -OutFile "${pwd}/go${go_version}.windows-amd64.zip"

Add-Type -Assembly System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::ExtractToDirectory("${pwd}/go${go_version}.windows-amd64.zip", "${pwd}")
Remove-Item -Path "${pwd}/go${go_version}.windows-amd64.zip"

$path_list = [System.Environment]::GetEnvironmentVariable('PATH', 'Machine') -split ';'
if ($path_list -notcontains "${pwd}\go\bin") {
    $path_string = ($path_list + "${pwd}\go\bin") -join ';'
    [System.Environment]::SetEnvironmentVariable('PATH', $path_string, 'Machine')
}
```

{{< /tab >}}

{{< tab "MacOS" >}}
{{< /tab >}}

{{< /tabs >}}

Check version: `go version`
