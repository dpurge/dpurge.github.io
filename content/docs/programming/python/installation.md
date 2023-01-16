# Installation

## PyEnv on Linux

Install build dependencies:

```sh
sudo apt update
sudo apt install \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    curl \
    llvm \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libffi-dev \
    liblzma-dev
```

Install PyEnv scripts:

```sh
curl https://pyenv.run | bash
```

Add to `~/.profile`:

```sh
export PATH="$HOME/.pyenv/bin:$PATH"

if command -v pyenv 1>/dev/null 2>&1; then
 eval "$(pyenv init -)"
fi
```


## PyEnv on Windows

Copy `pyenv-win` from https://github.com/pyenv-win/pyenv-win/archive/master.zip to `E:\pgm\pyenv-win`.

Environment variables:

| Name       | Value            |
|------------|------------------|
| PYENV_HOME | E:\pgm\pyenv-win |
| PYENV_ROOT | E:\pgm\pyenv-win |
| PYENV      | E:\pgm\pyenv-win |

Add to PATH: 

- `E:\pgm\pyenv-win\bin`
- `E:\pgm\pyenv-win\shims`

List available versions: `pyenv install -l`

Install chosen version: `pyenv install 3.11.1`

Set global Python version: `pyenv global 3.11.1`

Set local Python version: `pyenv local 3.11.1`

## Install basic packages

```sh
pip install invoke
pip install pipenv
```

Create environment variable `PIPENV_VENV_IN_PROJECT=1`.
