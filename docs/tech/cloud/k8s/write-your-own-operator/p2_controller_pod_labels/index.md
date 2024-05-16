# K8s controller | Pod Labels
[source](https://kubernetes.io/blog/2021/06/21/writing-a-controller-for-pod-labels/)

1. `operator-sdk init

> Next, we need a create a new controller. This controller will handle pods and not a custom resource, so no need to generate the resource code. Let's run this command to scaffold the code we need

- We will need to generate resource code if our controller interact with custom resources.

