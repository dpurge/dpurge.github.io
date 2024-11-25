# Firewall

Firewall rules apply to a given project and VPC.
It is also possible to apply firewall rules across an organization.

Firewall rules apply either to incoming or outgoing connections, never both at the same timne.

Every VPC network functions as a distributed firewall.
Firewall rules are defined on a network level, connections are allowed or denied on a per instance basis.
You can imagine the acting not only on a perimeter of the network, but also between instances within the network.

Rules can act on:

- protocol
- ports
- source
- destination

Implied/pre-populated rules:

- forbidden egress traffic on port 25
- allow traffic to the *metadata server* on `169.254.169.254` (DHCP, DNS, instance metadata, NTP)
- allow egress
- deny ingress (lowest priority)

Firewall rule characteristics:

- applies either to incoming or outgoing connections (not both)
- only support IPv4 connections
- apply to a VPC level
- stateful - return traffic (same source IP, destination IP, source port, destination port, protocol) is also allowed

