# Caddy

## Install `xcaddy`

```sh
wget -q https://github.com/caddyserver/xcaddy/releases/download/v0.3.4/xcaddy_0.3.4_linux_amd64.tar.gz
tar xf xcaddy_0.3.4_linux_amd64.tar.gz
sudo mv xcaddy /usr/local/bin/
```

## Build `caddy`

```sh
xcaddy build \
    --with github.com/wxh06/caddy-uwsgi-transport
sudo mv caddy /usr/local/bin/
sudo setcap cap_net_bind_service+eip /usr/local/bin/caddy
```

## Install `caddy`

```sh
sudo groupadd --system caddy
sudo useradd --system --gid caddy --create-home --home-dir /var/lib/caddy --shell /usr/sbin/nologin --comment "Caddy web server" caddy
```

Create files and directories:

```sh
sudo mkdir /etc/caddy
sudo touch /etc/caddy/Caddyfile
sudo chown -R root:caddy /etc/caddy
sudo mkdir /etc/ssl/caddy
sudo chown -R root:caddy /etc/ssl/caddy
sudo chmod 0770 /etc/ssl/caddy
sudo mkdir -p /var/www/public_html
sudo chown caddy:caddy /var/www/public_html
sudo touch /etc/systemd/system/caddy.service
sudo chmod 644 /etc/systemd/system/caddy.service
sudo touch /var/www/public_html/index.html
```

Service file `/etc/systemd/system/caddy.service`:

```ini
[Unit]
Description=Caddy web server
Documentation=https://caddyserver.com/docs/
After=network.target network-online.target
Requires=network-online.target

[Service]
Type=notify
User=caddy
Group=caddy
ExecStart=/usr/local/bin/caddy run --environ --config /etc/caddy/Caddyfile
ExecReload=/usr/local/bin/caddy reload --config /etc/caddy/Caddyfile --force
TimeoutStopSec=5s
LimitNOFILE=1048576
LimitNPROC=512
PrivateTmp=true
ProtectSystem=full
AmbientCapabilities=CAP_NET_ADMIN CAP_NET_BIND_SERVICE

[Install]
WantedBy=multi-user.target
```

Caddy configuration file `/etc/caddy/Caddyfile`:

```json
{
    auto_https off
}

http://hide.example.home.arpa {

    root * /var/www/public_html
    encode gzip
    file_server

    header / {
        Content-Security-Policy = "upgrade-insecure-requests; default-src 'self'; style-src 'self'; script-src 'self'; img-src 'self'; object-src 'self'; worker-src 'self'; manifest-src 'self';"
        Strict-Transport-Security = "max-age=63072000; includeSubDomains; preload"
        X-Xss-Protection = "1; mode=block"
        X-Frame-Options = "DENY"
        X-Content-Type-Options = "nosniff"
        Referrer-Policy = "strict-origin-when-cross-origin"
        Permissions-Policy = "fullscreen=(self)"
        Cache-Control = "max-age=0,no-cache,no-store,must-revalidate"
    }
}
```


Index file `/var/www/public_html/index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta name="viewport"content="width=device-width,initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
        rel="stylesheet"
        integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM"
        crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz"
        crossorigin="anonymous"></script>
    <title>Static page example</title>
</head>
<body class="text-center">
    <div class="jumbotron text-center">
        <h1>Welcome to Caddy</h1>
        <h2 class="h2 card-title">Welcome to Caddy</h2>
        <h6 class="h6 card-text">Your installation of Caddy is working.</h6>
    </div>
</body>
</html>
```

Run service:

```sh
sudo systemctl daemon-reload
sudo systemctl enable caddy
sudo systemctl start caddy
sudo systemctl stop caddy

systemctl status caddy.service
sudo journalctl -xeu caddy.service
sudo journalctl -u caddy --no-pager | less
```

```json
http://example.home.arpa {

  @api {
    path /config
    path /healthz
    path /stats/errors
    path /stats/checker
  }

  @static {
    path /static/*
  }

  @notstatic {
    not path /static/*
  }

  @imageproxy {
    path /image_proxy
  }

  @notimageproxy {
    not path /image_proxy
  }

  header {
    X-XSS-Protection "1; mode=block"
    X-Content-Type-Options "nosniff"
    X-Robots-Tag "noindex, noarchive, nofollow"
    -Server
  }

  header @api {
    Access-Control-Allow-Methods "GET, OPTIONS"
    Access-Control-Allow-Origin  "*"
  }

  handle {
    encode zstd gzip
    reverse_proxy localhost:8001 {
      header_up X-Forwarded-Port {http.request.port}
      header_up X-Forwarded-Proto {http.request.scheme}
    }
  }
}
```