## Workloads

In Kubernetes, a "workload" is a term used to describe the type of application or task that you want to run on the cluster. Kubernetes provides several types of workloads to including various application deployment scenarios. These workloads define how applications are scheduled, scaled, and managed.

1.

Extend the valid deployment skeleton with the following requirements:

- Deployment target namespace: ithon
- Create 3 replicas
- Add an environment variable with name ingress_port and value 30100.

deployment_skeleton.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nokia-app-deployment
  labels:
    app: nokia-web-app
spec:
  selector:
    matchLabels:
      app: nokia-web-app
  template:
    metadata:
      labels:
        app: nokia-web-app
    spec:
      containers:
        - name: nokia-container
          image: nokia-registry:5000/nokia-container-image:1.0.0
          ports:
            - containerPort: 80
```
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nokia-app-deployment
  namespace: ithon
  labels:
    app: nokia-web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nokia-web-app
  template:
    metadata:
      labels:
        app: nokia-web-app
    spec:
      containers:
        - name: nokia-container
          image: nokia-registry:5000/nokia-container-image:1.0.0
          ports:
            - containerPort: 80
          env:
            - name: ingress_port
              value: "30100"
```

3.

Extend the valid deployment skeleton with the following requirements:
Add liveness probe with HTTP request and set the failureThreshold to 3
Perform a liveness probe every 10 seconds but wait 15 seconds before performing the first probe

Add Readiness probe HTTP request and set the failureThreshold to 3
Perform a readiness probe every 15 seconds but wait 30 seconds before performing the first probe

Add resource Reqs
CPU: 100 millicore
MEMORY: 128 Mebibyte
Add resouce limits:
CPU: 500 millicore
MEMORY: 512 Mebibyte

deployment_skeleton.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nokia-app-deployment
  labels:
    app: nokia-web-app
spec:
  selector:
    matchLabels:
      app: nokia-web-app
  template:
    metadata:
      labels:
        app: nokia-web-app
    spec:
      containers:
        - name: nokia-container
          image: nokia-registry:5000/nokia-container-image:1.0.0
```

```yaml
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 15
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 30
            periodSeconds: 15
          resources:
            requests:
              cpu: "100m"
              memory: "128Mi"
            limits:
              cpu: "500m"
              memory: "512Mi"
```