# Installation

## NodeJS

{{< tabs "install-bodejs" >}}

{{< tab "Linux" >}}

```sh
git clone https://github.com/nvm-sh/nvm.git /opt/nvm
cd /opt/nvm
git checkout v0.40.3
```

Add to `~/.profile`:

```sh
export NVM_DIR="$HOME/.nvm"

if [ -s "/opt/nvm/nvm.sh" ]; then
  . "/opt/nvm/nvm.sh"
fi

if [ -s "/opt/nvm/bash_completion" ]; then
  . "/opt/nvm/bash_completion"
fi
```

Install NodeJS:

```sh
nvm install node
nvm install-latest-npm
npm install -g yarn
```

{{< /tab >}}

{{< tab "Windows" >}}

Install [NVM for Windows](https://github.com/coreybutler/nvm-windows)

Settings:

```txt
root: D:\pgm\nvm
path: D:\pgm\nodejs
```

Install NodeJS:

```cmd
nvm list available
nvm install latest
nvm use newest
```

{{< /tab >}}

{{< tab "MacOS" >}}
{{< /tab >}}

{{< /tabs >}}

## Basic tools

Install `yarn`:

```sh
npm install -g yarn
```
