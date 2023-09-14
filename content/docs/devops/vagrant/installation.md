# Installation

# Windows

- Install Hyper-V
- Check Samba configuration
- Configure Hyper-V as default Vagrant provider
- Install Vagrant's `reload` plugin
- Create NAT switch for Hyper-V

```pwsh
Get-SmbServerConfiguration

[Environment]::SetEnvironmentVariable("VAGRANT_DEFAULT_PROVIDER", "hyperv", "User")

vagrant plugin install vagrant-reload

# Get-NetAdapter | Format-Table -AutoSize

Get-VMSwitch | Select-Object -ExpandProperty Name
# if NatSwitch not listed
New-VMSwitch -SwitchName "NATSwitch" -SwitchType Internal

Get-NetIPAddress | Select-Object -ExpandProperty IPAddress
# if 192.168.200.1 not listed
New-NetIPAddress -IPAddress 192.168.200.1 -PrefixLength 24 -InterfaceAlias "vEthernet (NATSwitch)"

Get-NetNAT | Select-Object -ExpandProperty InternalIPInterfaceAddressPrefix
# if 192.168.200.0/24 not listed
New-NetNAT -Name "NATNetwork" -InternalIPInterfaceAddressPrefix 192.168.200.0/24
```

## Vagrantfile

This template is ready to create several VMs on Hyper-V
and set static address to all of them.

```ruby
# Groovy Gorilla
Vagrant.configure("2") do |config|

  servers=[
    {
      :hostname => "srv01",
      :box => "generic/ubuntu2010",
      :ip => "192.168.200.101",
      :ssh_port => '2201',
      :memory => 512,
      :cpus => 1
    }
  ]
  
  gateway="192.168.200.1"

  servers.each do |srv|
    config.vm.define srv[:hostname] do |node|
      node.vm.box = srv[:box]
      node.vm.hostname = srv[:hostname]

      node.vm.provider :hyperv
      node.vm.network :public_network, auto_config: false
      node.vm.network "forwarded_port", guest: 22, host: srv[:ssh_port], id: "ssh"
      node.vm.synced_folder ".", "/vagrant", disabled: true

      node.vm.provision "shell", path: "./scripts/configure-static-ip.sh", :args => "#{srv[:ip]} #{gateway}"
      servers.each do |host|
        node.vm.provision "shell", path: "./scripts/add-hosts-entry.sh", :args => "#{host[:ip]} #{host[:hostname]}"
      end
      node.vm.provision :reload

      node.vm.provider :hyperv do |h|
        h.vmname = srv[:hostname]
        h.enable_virtualization_extensions = true
        h.linked_clone = true
        h.maxmemory = 2048
        h.memory = srv[:memory]
        h.cpus = srv[:cpus]
      end
    end
  end
end
```

Script to update `/etc/hosts` file in `scripts/add-hosts-entry.sh`:

```sh
#!/bin/sh

echo -n 'Adding IP to hosts file: '
echo $1
echo -n 'Host name is: '
echo $2

echo "$1 $2" >> /etc/hosts
```

## Ubuntu `scripts/configure-static-ip.sh`

```sh
#!/bin/sh

echo -n 'Setting static IP address: '
echo $1
echo -n 'Setting gateway address: '
echo $2

cat << EOF > /etc/netplan/01-netcfg.yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses: [$1/24]
      gateway4: $2
      nameservers:
        addresses: [8.8.8.8,8.8.4.4]
EOF
```

## CentOS `scripts/configure-static-ip.sh`

```sh
#!/bin/sh

echo -n 'Setting static IP address: '
echo $1
echo -n 'Setting gateway address: '
echo $2

cat << EOF > /etc/sysconfig/network-scripts/ifcfg-eth0
DEVICE=eth0
BOOTPROTO=none
ONBOOT=yes
PREFIX=24
IPADDR=$1
GATEWAY=$2
DNS1=8.8.8.8
EOF
```

## Commands

The Hyper-V provider requires that Vagrant be run with administrative privileges.
This is a limitation of Hyper-V itself.

```sh
vagrant up
vagrant ssh srv01
vagrant halt
vagrant destroy
```

Username is `vagrant`, password is `vagrant`.
