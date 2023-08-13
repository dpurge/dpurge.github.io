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

- [`Pod`](https://kubernetes.io/docs/concepts/workloads/pods/) (abstraction of container runtime for a container)
- `Service` (a permanent IP address and load balancer for Pods)
- `Ingress` (forwards requests using domain name to a specific Service)
- `ConfigMap` (external configuration for application)
- `Secret` (stores secret configuration data encoded in base64)
- [`Deployment`](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) (an abstraction of a set of Pod replicas that can be scaled)
- `Volume` (external disk storage - local or remote - connected to the cluster)
- [`Job`](https://kubernetes.io/docs/concepts/workloads/controllers/job/) (???)
- [`CronJob`](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) (???)
- [`StatefulSet`](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) (an abstraction of a set of Pods that have a shared state, eg. data)
- [`DaemonSet`](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) (ensures that all matching Nodes run a copy of a Pod)
- [`ReplicaSet`](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) (???)
- [`ReplicationController`](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/) (???)
