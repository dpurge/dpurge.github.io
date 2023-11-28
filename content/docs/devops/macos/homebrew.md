# Homebrew

## Install

Download package from `https://github.com/Homebrew/brew/releases/`.

It installs in `/opt/homebrew`.

## Configuration

Add line to `~/.zprofile`:

```sh
eval "$(/opt/homebrew/bin/brew shellenv)"
```

## Usage

```sh
brew help
brew analytics off
brew doctor
brew update
brew shellenv
brew cleanup
brew search xxx
brew info xxx
brew install xxx
brew reinstall xxx
brew uninstall xxx
brew bundle dump
brew bundle install --file ./Brewfile
```
## Hashicorp tools

Install:

```sh
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

Upgrade:

```sh
brew update
brew upgrade hashicorp/tap/terraform
```