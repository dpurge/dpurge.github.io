# Configuration of git

## Username and email

```sh
git config --global user.name "D. Purge"
git config --global user.email "my@email.com"
git config --global core.autocrlf false
```

## SSH checkouts from Azure DevOps

Generate SSH keypair:

```sh
ssh-keygen -t rsa
```

Full parameters:

```sh
ssh-keygen \
    -m PEM \
    -t rsa \
    -b 4096 \
    -C "user@server.example.com" \
    -f ~/.ssh/mykeys/privatekey \
    -N passphrase
```

Parameters:

- *-m PEM* = format key as PEM
- *-t RSA* = type of the key, RSA format
- *-b 4096* = number of bits in the key, 4096 bits
- *-C "user@server.example.com"* = a comment appended at the end of the public key, to identify it
- *-f ~/.ssh/mykeys/privatekey* = the filename of the private key filet,
  a corresponding public key file appended with `.pub` is generated in the same directory which must exist
- *-N passphrase* = a passphrase used to access the private key file

Add configuration in `~/.ssh/config`:

```
Host ssh.dev.azure.com
  IdentityFile ~/.ssh/id_rsa
  IdentitiesOnly yes
  User git
  PubkeyAcceptedAlgorithms +ssh-rsa
  HostkeyAlgorithms +ssh-rsa
```