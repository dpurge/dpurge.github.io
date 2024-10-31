# Cloud shell

Customize in `~/.customize_environment` (`edit .customize_environment`):

```sh
#!/bin/sh
TERRAFORM_VERSION="0.12.0"
curl https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip > terraform_${TERRAFORM_VERSION}_linux_amd64.zip
unzip -o terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/local/bin
```

Editor is based on Eclipse Theia.
