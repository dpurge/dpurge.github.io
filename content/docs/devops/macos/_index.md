---
title: MacOS
bookCollapseSection: true
---

Quick start:

## XCode

```sh
xcode-select --install
ssh-keygen -t ed25519 -C "username@example.com"
git config --global user.email "username@example.com"
git config --global user.name "username"
```

Run software updates.

Setup profile for Terminal in `Settings/Profiles`. Copy from `Pro`.

Add to `~/.zshenv`:

```sh
plugins=(git ssh-agent)
```

Configure GitHub:

```sh
ssh-keygen -t rsa -C "dpurge@example.com"
ssh-add ~/.ssh/id_rsa_dpurge
```

Add to `~/.ssh/config`:

```txt
# username account
Host github.com-username
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_ed25519

# dpurge account
Host github.com-dpurge
	HostName github.com
	User git
	IdentityFile ~/.ssh/id_rsa_dpurge
```

Create workspace:

```sh
mkdir -p ~/src/github.com/dpurge
cd ~/src/github.com/dpurge
git clone git@github.com:dpurge/dpurge.github.io.git
cd dpurge.github.io
git config user.email "dpurge@example.com"
git config user.name "D. Purge"
```

## VPN certificate request

```sh
openssl ecparam -out ~/Documents/${USER}.key -name secp384r1 -genkey
openssl req -new -key ~/Documents/${USER}.key -out ~/Documents/${USER}.csr -subj "/CN=${USER}/SN=$(system_profiler SPHardwareDataType | awk '/Serial Number \(system\)/{print $NF}')"
```

## Homebrew

Use installer from [GitHub releases](https://github.com/Homebrew/brew/releases/).

```sh
brew update
brew install openssl readline sqlite3 xz zlib
brew instll mc
brew install pyenv
brew install pyenv-virtualenv
pyenv install 3.12.7
pyenv global 3.12.7
brew install deno
brew install warrensbox/tap/tgswitch
brew install warrensbox/tap/tfswitch
tfswitch -u
tgswitch
pip install jupyterlab
deno jupyter --install
pip install ansible
brew install go-task/tap/go-task
brew install k3d
brew install podman-compose
```

Add to `~/.zshenv`:

```sh
PATH="${HOME}/bin:/usr/local/bin:${PATH}"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
export PATH
```

## VS Code

Use installer from [download page](https://code.visualstudio.com/download).

## Podman

Use installer from [GitHub releases](https://github.com/containers/podman/releases).

```sh
podman machine init --cpus 4 --memory 2048 --disk-size 100 
podman machine set --rootful
```

## Go

Use installer from [install page](https://go.dev/doc/install).

## Jupyter
