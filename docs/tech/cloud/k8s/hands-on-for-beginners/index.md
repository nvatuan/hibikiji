# Hands-on Kubernetes actions for Beginners
This will contains source code and walkthrough to interact with kubernetes and learning its behaviors.

## Summary
### Goals:
- Deploying a service onto Kubernetes environment

### Walkthrough:
- Setup a local k8s environment with Minikube
- Inspect the service and the container image
- Create a Namespace
- Create a Deployment
- Create a Service

## Steps
- Operating System: MacOS

### Setup a local Kubernetes environment with Minikube
#### 0. Check if homebrew is installed
- Homebrew is a tool similar to `apt-get`, is used to install packages on your machines.
- Runs this command to check if it was installed.
```bash
brew -v
```

- If not, following this to install: https://brew.sh/
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Relauch terminal and Re-run `brew -v` to check if it was installed successfully.

#### 1. Install Docker container or similar environment:
We will install OrbStack to our Mac machine. Following https://docs.orbstack.dev/quick-start
```bash
brew install orbstack
```

#### 2. Install `minikube`
Following this to install `minikube` on your machine: https://minikube.sigs.k8s.io/docs/start/
- Runs this command
```
brew install minikube
```

- Runs this to check for `minikube` command:
```
brew unlink minikube
brew link minikube
```

#### 3. Start your clusters
- Start your cluster with this command to launch a kubernetes cluster with 3 nodes:
- You can use this command to delete previously created kubernetes.
```bash
minikube delete
```
- You can ignore `--nodes=3` to lauch it with only 1 node.
```bash
minikube start --nodes=3
```




