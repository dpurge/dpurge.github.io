# Blocky

Blocky is a DNS proxy and ad-blocker.

```sh
wget -q "https://github.com/0xERR0R/blocky/releases/download/v0.21/blocky_v0.21_Linux_x86_64.tar.gz"
tar xf blocky_v0.21_Linux_x86_64.tar.gz
sudo mv blocky /usr/local/bin/
sudo setcap cap_net_bind_service=ep /usr/local/bin/blocky
```

Create user:

```sh
sudo groupadd --system blocky
sudo useradd --system --gid blocky --create-home --home-dir /var/lib/blocky --shell /usr/sbin/nologin --comment "Blocky DNS proxy" blocky
```

Configuration file `/etc/blocky/config.yml`:

```yml
upstream:
  default:
    - 8.8.8.8
    - 1.1.1.1
blocking:
  blackLists:
    ads:
      - https://raw.githubusercontent.com/dpurge/dns-hole/main/blacklist/dpurge.txt
      - https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
  whiteLists:
    ads:
      - https://raw.githubusercontent.com/dpurge/dns-hole/main/whitelist/dpurge.txt
  clientGroupsBlock:
    default:
      - ads
  downloadTimeout: 4m
  downloadAttempts: 5
  downloadCooldown: 10s
customDNS:
  mapping:
    example.home.arpa: 127.0.0.1
ports:
  dns: 53
bootstrapDns:
  - 8.8.8.8
  - 1.1.1.1
log:
  level: warn
```

Service file `/etc/systemd/system/blocky.service`:

```ini
[Unit]
Description=Blocky DNS resolver
ConditionPathExists=/usr/local/bin/blocky
After=local-fs.target

[Service]
User=blocky
Group=blocky
Type=simple
WorkingDirectory=/var/lib/blocky
ExecStart=/usr/local/bin/blocky --config /etc/blocky/config.yml
Restart=on-failure
RestartSec=10
SyslogIdentifier=blocky

[Install]
WantedBy=multi-user.target
```

Install:

```sh
systemctl is-active systemd-resolved
sudo systemctl disable --now systemd-resolved.service
sudo systemctl daemon-reload
sudo systemctl enable blocky
sudo systemctl start blocky
systemctl is-active blocky
sudo less /var/log/syslog
```

Manage:

```sh
sudo systemctl status blocky
sudo systemctl stop blocky
sudo systemctl start blocky
sudo systemctl restart blocky
```

Configure:

```sh
sudo vim /etc/blocky/config.yml
sudo vim /etc/systemd/system/blocky.service
```

Uninstall:

```sh
systemctl stop blocky
systemctl disable --now blocky.service
systemctl enable --now systemd-resolved.service
rm -rf /etc/systemd/system/blocky.service
rm -rf /usr/local/bin/blocky
userdel -r -f blocky
```