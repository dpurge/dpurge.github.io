# Python on MacOS

```sh
brew update
brew install pyenv
brew install pyenv-virtualenv
```

Add to `~/.zshenv`:

```sh
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
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

Prepare virtual environment for LLM:

```sh
pyenv virtualenv 3.12.0 llm
pyenv global llm
pip install langchain
```

Install packages:

```sh
pip install --upgrade pip
pip install awscli
```