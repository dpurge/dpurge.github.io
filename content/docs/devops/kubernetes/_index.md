---
title: Kubernetes
bookCollapseSection: true
---

# Kubernetes

Container orchestration:

- High availability
- Scalability
- Disaster recovery

## Architecture

A `node` is a virtual or physical machine.

A [Kubernetes](https://kubernetes.io/) cluster is made from at least one `master node` and connected to it `worker nodes`.
All nodes are connected by cluster's Virtual Network. All of these components create one unified machine.

Kubernetes does not manage data persistence.
It is easier to host databases outside of Kubernetes cluster.

Each worker node has a `kubelet` process running. Kubelet is a node agent that allows cluster to communicate with nodes and execute tasks on them. Worker nodes have application containers deployed on them. Applications run on worker nodes.

Master node runs `Control Plane` processes necessary for managing the cluster:

- `API Server` (entry point to the cluster for kubernetes clients)
- `Controller Manager` (keeps track of what is happening in the cluster)
- `Scheduler` (decides on which worker node to schedule new Pod)
- `etcd` key-value store (keeps current configuration and state of the cluster)

## Components

- [`Pod`](https://kubernetes.io/docs/concepts/workloads/pods/)
  Abstraction of container runtime for one or more containers.
  Smallest unit of computing that is assigned an individual IP address and can be deployed and managed.
- `Service`
  A permanent IP address and load balancer for Pods.
  Publishes its own virtual address either as an environment variable in every Pod or, if cluster is using CoreDNS, as a DNS entry.
  Services can abstract access not only to Pods, but also to databases, external host or other services.
- `Ingress` (forwards requests using domain name to a specific Service)
- `ConfigMap` (external configuration for application)
- `Secret` (stores secret configuration data encoded in base64)
- [`Deployment`](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
  An abstraction allowing to manage the state of a set of Pods or Replica Sets.
  It allows to run a group of identical Pods with a common configuration.
- `Volume` (external disk storage - local or remote - connected to the cluster)
- [`Job`](https://kubernetes.io/docs/concepts/workloads/controllers/job/) (???)
- [`CronJob`](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) (???)
- [`StatefulSet`](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/)
  Provides unique network identifiers, persistent storage, ordered deployment and scaling.
- [`DaemonSet`](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)
  Ensures that all matching Nodes run a copy of a Pod.
- [`ReplicaSet`](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
  A group of duplicated identical pods.
- [`ReplicationController`](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/) (???)
