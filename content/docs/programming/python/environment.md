# Virtual environment

TODO

## Venv

Create and activate virtual environment:

{{< tabs "venv-setup" >}}

{{< tab "Bash" >}}

```bash
echo Hello
```

{{< /tab >}}

{{< tab "Powershell" >}}

```pwsh
python -m venv .venv
.venv\Scripts\activate.ps1
```

{{< /tab >}}

{{< tab "Cmd" >}}

```cmd
echo Hello
```

{{< /tab >}}

{{< /tabs >}}

Upgrade `pip` and install `requirements.txt`:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Deactivate virtual environment:

```bash
deactivate
```

## Pipenv

TODO
