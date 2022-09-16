# Installation

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

Install chosen version: `pyenv install 3.10.7`

Set global Python version: `pyenv global 3.10.7`

Set local Python version: `pyenv local 3.10.7`

## Install basic packages

```cmd
pip install invoke
pip install pipenv
```

Create environment variable `PIPENV_VENV_IN_PROJECT=1`.
