# Definitions

What is cloud computing?
: The delivery of a *shared pool* of *on-demand computing services* over the *public internet*, that can be *rapidly provisioned and released* with *minimal* management effort or service provider interaction.

- provision resources automatically without requiring human interaction
- available over the network
- pooled resources to support a multi-tenant model allowing multiple customers to share the same applications or the same physical infrastructure
- rapidly provision and de-provision any of the cloud computing resources
- resource usage can be monitored, controlled and reported using metering capabilities

Zone
: a deployment area within a region; the smallest entity of global infrastructure

Region
: an indepenedent geographic area holding a collection of zones

Multi-Region
: large geographic area holding two or more regions

## Compute

Compute Engine
: (IaaS) virtual machines called *instances* deployed from public or private images in a specific region and zone; pre-configured images on Google Cloud Marketplace; multiple instances managed with *instance groups* and *autoscaling*; attach/detach additional *disks*; can use *Google Cloud Storage*; accessed with *ssh*

GKE (Google Kubernetes Engine)
: (CaaS) container orchestrating system; built on open source Kubernetes; can integrate with on-premise Kubernetes; uses Compute Engine instances as nodes in a cluster

App Engine
: (PaaS) managed serverless platform for hosting web applications at scale; provisions and patches servers and scales the application instances based on demand; build your app in Go, Java, .NET, NodeJS, PHP, Python, Ruby; seamlessly connects with Google services (storage, databases, ...); can connect to other cloud providers or external databases; integrates with *Web Security Scanner* to identify vulnerabilities

Cloud Functions
: (FaaS) serverless execution environment; simple, single-purpose functions triggered when a watched event is fired, executing in a fully managed environment; written in Java Script, Python 3, Go, Java; good for ETL, webhooks, APIs, mobile backend functions

Cloud Run
: (FaaS) serverless for containers; managed compute platform for deploying and scaling containerized applications; built upon an open standard *Knative*; abstracts away all infrastructure management; any language, library or binary

## Storage

Cloud Storage
: consistent, scalable, large capacity, highly durable object storage; unlimited storage with no minimum object size; eleven nines durability (99.999999999%); excellent for content delivery, data lakes, backups; comes in different *storage classes* (standard, nearline, coldline, archive) and *availability* (region, dual-region, multi-region)

Filestore
: fully managed NFS file server compliant with NFSv3; stores data for running applications in VM instances or Kubernetes clusters

Persistent Disks
: durable block storage for instances; comes in two options (standard, solid state); available in zonal and regional option

## Databases

### SQL/relational

Cloud SQL
: managed PostgreSQL, MySQL or SQL Server; high availability across zones

Cloud Spanner
: scalable relational database service; supports transactions, strong consistency, synchronous replication; high availability across regions and globally

### NoSQL

Bigtable
: fully managed, scalable NoSQL DB; high throughput with low latency; cluster resizing without downtime

Datastore
: fast, fully managed, serverless, NoSQL document database; for mobile, web and IoT apps; multi-region replication; ACID transactions

Firestore
: NoSQL realtime database optimized for offline us; cluster resizing without downtime

Memorystore
: fully managed, highly available in-memory service for Redis and Memcached

## Networking

VPC (Virtual Private Cloud)
: core networking service, virtualized network within Google Cloud; global resource; each VPC contains a default network; additional networks can be created in your project, but networks cannot be shared between projects

Firewall Rules
: a global distributed firewall that governs traffic comming into instances on a network; default network has a default set of firewall rules; custom rules can be created

Routes
: advanced networking functions for instances; specifies how packets leaving an instance should be directed

## Load Balancing

Distribution of workloads across multiple instances.

HTTP(S) Load Balancing
: distribute traffic across regions to ensure that requests are routed to the closest region or a healthy instance in the next closest region; distribute traffic based on content type

Network Load Balancing
: distribute traffic among server instances in the same region based on incomming IP protocol data (address, port, protocol)

## Cloud DNS

Google Cloud DNS
: publish and maintain DNS records

## Advanced Connectivity

Cloud VPN
: connect your existing network to your VPC through an IPsec connection

Direct Interconnect
: connect your existing network to your VPC using a highly available, low latency, enterprise grade connection; does not go over public internet, connects to the nearest Google backbone

Direct Peering
: exchange internet traffic between your network and Google at Google edge network location

Carrier Peering
: connect your infratsructure to Google network edge through highly available, lower latency connection from a service provider

## Resource hierarchy

Google Cloud resources are organized hierarchically using a parent/child relationship designed to map organizational structure to Google Cloud, so that it can be used to manage permissions and access control.

Policies are controlled by *IAM*. Access control policies and configuration settings on a parent resource are inherited by the child. Each child object has exactly one parent.

- cloud level
  - Payments Profile
  - Billing Account
  - Domain (organizations, users, policies)
- account level
  - Organization (root node, closely integrated with the domain)
  - Folders (grouping mechanism and isolation boundary, eg. departments, teams, products)
  - Projects (core organizational component; required to use resources; parents resources)
  - Project Labels
- service level
  - Resources (any service-level resource, eg. VM, storage bucket, databases, ...)
  - Resource Labels

Labels:

- categorize resurces by using a key/value pair

[https://console.cloud.google.com/freetrial]
