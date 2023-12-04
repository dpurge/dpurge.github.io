# DPurge personal notebook

To work locally: `hugo server -D`

To build: `hugo --minify`

## Diagrams

- [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/downloads/) are a prerequisite to install some packages
- [GraphViz](https://graphviz.org/download/) is required for diagrams

```sh
python -m venv .venv
source ./.venv/Scripts/activate
pip install -r requirements.txt
```

Compilation:

```sh
cd ./content/docs/devops/blueprints/
python aws-static-webapp.py
```
