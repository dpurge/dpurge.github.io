# Python on MacOS

```sh
brew update
brew install pyenv
```

Check:

```sh
pyenv root
```

Install python:

```sh
pyenv install -l
pyenv install 3.12.0
pyenv global 3.12.0
pyenv version
```

Add to `~/.zshenv`: `eval "$(pyenv init -)"`

Install packages:

```sh
pip install --upgrade pip
pip install awscli
```