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
brew install xxx
brew reinstall xxx
brew uninstall xxx
brew bundle dump
brew bundle install --file ./Brewfile
```
