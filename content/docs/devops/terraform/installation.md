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

{{< /tabs >}}