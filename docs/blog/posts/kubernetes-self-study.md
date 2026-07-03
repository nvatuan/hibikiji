---
date: 2026-07-03
categories:
  - Platform Engineering
tags:
  - kubernetes
  - infra
---

# Notes from my Kubernetes self-study

Working through k8s from first principles instead of copy-pasting `kubectl apply`
until something turns green.

<!-- more -->

Starting points I keep coming back to:

- **Pods aren't the unit you deploy** — Deployments/ReplicaSets are.
- **Services are just stable virtual IPs** with a label selector in front of pods.
- **etcd is the source of truth**; everything else is a controller reconciling
  desired vs. actual state.

Full hands-on lab notes will live under [Tech → Kubernetes](../../tech/cloud/k8s/index.md).
