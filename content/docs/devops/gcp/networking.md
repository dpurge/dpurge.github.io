# Networking

OSI model:

1. Physical
2. Data link
3. Network (IPv4, IPv6, ICMP)
4. Transport (TCP, UDP)
5. Session
6. Presentation
7. Application (telnet, SSH, DNS, DHCP, HTTP, HTTPS)

## IP v4

Classful addressing:

4,294,967,296 addresses

Class A
: `0.0.0.0` - `127.255.255.255`; 2,147,483,648 addresses; 128 networks

Class B
: `128.0.0.0` - `191.255.255.255`; 1,073,741,824 addresses; 16,384 networks

Class C
: `192.0.0.0` - `223.255.255.255`; 536,870,912 addresses; 2,097,152 networks

Private IP addresses (RFC1918):

- class A: `10.0.0.0` - `10.255.255.255`; 16,777,216 addresses
- class B: `172.16.0.0` - `172.31.255.255`; 1,048,576 addresses
- class C: `192.168.0.0` - `192.168.255.255`; 65,536 addresses

### Classless Inter-Domain Routing

CIDR = Classless Inter-Domain Routing

Allows creating a network in any range using pattern `{network-address}/{prefix}`, eg: `192.168.0.0/16` which can be split in two halves with 32,768 addresses each: `192.168.0.0/17` (`192.168.0.0` - `192.168.127.255`) and `192.168.128.0/17` (`192.168.128.0` - `192.168.255.255`).

Each of these halves can be halved again, each part with 16,384 addresses:

- `192.160.0.0/18` (`192.168.0.0` - `192.168.63.255`)
- `192.160.64.0/18` (`192.168.64.0` - `192.168.127.255`)
- `192.160.128.0/18` (`192.168.128.0` - `192.168.191.255`)
- `192.160.192.0/18` (`192.168.192.0` - `192.168.255.255`)

This subnetting process can be continued.

Common networks:

- `192.168.0.0/8`; 16+ million addresses
- `192.168.0.0/16`; 65,536 addresses
- `192.168.0.0/24`; 256 addresses
- `192.168.1.2/32`; 1 address
- `0.0.0.0/0`; all IP addresses

## IP v6

Uses hexadecimal notation in which two octets are combined into *hextets*.
Address consists of 8 hextets; it is 128 bits long.
Redundand zeroes in a hextet can be removed.
Double colon `::` stands for a slew of zeroes.

Example: `2001:de3::/64` (`2001:de3:0000:0000:0000:0000:0000:0000` - `2001:de3:0000:0000:ffff:ffff:ffff:ffff`)

All addresses: `::/0`

## IP packet

TCP = Transmission Control Protocol

UDP = User Datagram Protocol

IP packet:

1. Source IP address
2. Destination IP address
3. Protocol port number (source/destination)
4. Data

## Snippets

Increase subnet range:

```sh
gcloud compute networks subnets expand-ip-range default --region=us-west1 --prefix-length=16
gcloud compute networks subnets describe default --region=us-west1
```

Create regional IP address:

```sh
gcloud compute addresses create {address-name} --region {region}
```

Create global IP address:

```sh
gcloud compute addresses create {address-name} --global --ip-version [IPV4|IPV6]
```

List available IP addresses:

```sh
gcloud compute addresses list
```

Promote external IP address from ephemeral to static:

```sh
gcloud compute addresses create {address-name} --addresses 104.196.219.42 --region us-east1
```

Delete static internal IP address:

```sh
gcloud compute addresses delete {address-name}  --region us-east1
```
