# SearXNG

```sh
sudo apt update -y
sudo apt upgrade -y
sudo apt-get install -y python3-dev python3-babel python3-venv uwsgi uwsgi-plugin-python3 git build-essential libxslt-dev zlib1g-dev libffi-dev libssl-dev
```

## Install

Create user:

```sh
sudo groupadd --system searxng
sudo useradd --system --gid searxng --create-home --home-dir /var/lib/searxng --shell /bin/bash --comment "Privacy-respecting metasearch engine" searxng
sudo -u searxng -i
(searxng)$ git clone "https://github.com/searxng/searxng" "/var/lib/searxng/searxng-src"
(searxng)$ python3 -m venv "/var/lib/searxng/searxng-pyenv"
```

Autoload virtual enviroment in `/var/lib/searxng/.profile`:

```sh
# Automatically load virtual environment
if [ -f "$HOME/searxng-pyenv/bin/activate" ] ; then
    . "$HOME/searxng-pyenv/bin/activate"
fi
```

Exit and start in a new session.
Make sure that pyenv was activated automatically:

```sh
(searxng-pyenv)$ command -v python
(searxng-pyenv)$ python --version
```

Install dependencies in pyenv:

```sh
cd $HOME/searxng-src
pip install -U pip
pip install -U setuptools
pip install -U wheel
pip install -U pyyaml
pip install -e .
```

## Configure

```sh
sudo mkdir -p "/etc/searxng"
sudo cp "/var/lib/searxng/searxng-src/utils/templates/etc/searxng/settings.yml" "/etc/searxng/settings.yml"
```

Generate secret key:

```sh
openssl rand -hex 16
```

Update `secret_key` in the settings.
Remove connection to Redis.
Set `port` to `8001`.
Set `bind_address` to `127.0.0.1`.

```yml
use_default_settings: true
server:
  base_url: http://jdplxd01.home.arpa  # change this!
  port: 8001
  bind_address: "127.0.0.1"
  secret_key: "ultrasecretkey"  # change this!
  limiter: false  # can be disabled for a private instance
  image_proxy: true
ui:
  static_use_hash: true
redis:
  #url: redis://redis:6379/0
  url: false
```

Test interactively:

```sh
sudo -u searxng -i
cd /var/lib/searxng/searxng-src
export SEARXNG_SETTINGS_PATH="/etc/searxng/settings.yml"
python searx/webapp.py
```

```sh
curl --location --verbose --head --insecure 127.0.0.1:8001
```

## uWSGI

```sh
sudo touch /etc/uwsgi/apps-available/searxng.ini
sudo ln -s /etc/uwsgi/apps-available/searxng.ini /etc/uwsgi/apps-enabled/
```

Set configuration in `/etc/uwsgi/apps-available/searxng.ini`:

```ini
[uwsgi]

uid = searxng
gid = searxng

env = LANG=C.UTF-8
env = LANGUAGE=C.UTF-8
env = LC_ALL=C.UTF-8

chdir = /var/lib/searxng/searxng-src/searx
env = SEARXNG_SETTINGS_PATH=/etc/searxng/settings.yml
disable-logging = true
chmod-socket = 666
single-interpreter = true
master = true
lazy-apps = true
plugin = python3,http
enable-threads = true
module = searx.webapp
virtualenv = /var/lib/searxng/searxng-pyenv
pythonpath = /var/lib/searxng/searxng-src
socket = /var/lib/searxng/run/socket
buffer-size = 8192
static-map = /static=/usr/local/searxng/searxng-src/searx/static
static-expires = /* 31557600
static-gzip-all = True
offload-threads = %k

cache2 = name=searxngcache,items=2000,blocks=2000,blocksize=4096,bitmap=1
```

Management of the service:

```sh
create     /etc/uwsgi/apps-available/searxng.ini
enable:    sudo -H ln -s /etc/uwsgi/apps-available/searxng.ini /etc/uwsgi/apps-enabled/
start:     sudo -H service uwsgi start   searxng
restart:   sudo -H service uwsgi restart searxng
stop:      sudo -H service uwsgi stop    searxng
disable:   sudo -H rm /etc/uwsgi/apps-enabled/searxng.ini
```
uwsgi --socket 0.0.0.0:8001 --protocol=http -w wsgi:searx.webapp
sudo usermod -a -G www-data caddy

```ini
[Unit]
Description=SearXNG
After=network.target

[Service]
User=searxng
Group=www-data
WorkingDirectory=/var/lib/searxng/searxng-src
Environment="SEARXNG_SETTINGS_PATH=/etc/searxng/settings.yml"
ExecStart=python searx/webapp.py

[Install]
WantedBy=multi-user.target
```
