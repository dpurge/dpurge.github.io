# NodeJS

## Installation on Linux

```sh
git clone https://github.com/nvm-sh/nvm.git /opt/nvm
cd /opt/nvm
git checkout v0.39.3
```

Add to `~/.profile`:

```sh
export NVM_DIR="$HOME/.nvm"

if [ -s "$NVM_DIR/nvm.sh" ]; then
  . "$NVM_DIR/nvm.sh"
fi

if [ -s "$NVM_DIR/bash_completion" ]; then
  . "$NVM_DIR/bash_completion"
fi
```

Install NodeJS:

```sh
nvm install node
nvm install-latest-npm
npm install -g yarn
```

## Installation on Windows

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

Install `yarn`:

```sh
npm install -g yarn
```

