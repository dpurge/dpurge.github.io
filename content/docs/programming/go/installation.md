# Installation


{{< tabs "go-setup" >}}

    {{< tab "Linux" >}}
        ```sh
        sudo apt update
        sudo apt upgrade -y
        sudo apt install golang -y
        ```
    {{< /tab >}}

    {{< tab "Windows" >}}
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
    {{< /tab >}}

{{< /tabs >}}

Check version: `go version`
