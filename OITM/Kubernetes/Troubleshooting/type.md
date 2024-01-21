## Troubleshooting

Kubernetes environments can be complex, involving multiple components and wide range of configurations, dependencies between the micro-services. When something goes wrong, troubleshooting skills are essential to be able to quickly identify the root cause of the problem, whether it's a misconfiguration, resource constraint, or application-related issue.

2.
Deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nokia-deployment
  namespace: nokia
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nokia-app
  template:
    metadata:
      labels:
        app: nokia-app
    spec:
      containers:
        - name: nokia-app
          image: nokia-registry:5000/nokia-app:1.0.0
          ports:
            - containerPort: 80
          volumeMounts:
            - name: secret-volume
              mountPath: /secrets
            - name: configmap-volume
              mountPath: /config
      volumes:
        - name: secret-volume
          secret:
            secretName: nokia-login-secret
        - name: configmap-volume
          configMap:
            name: nokia-app-configmap
```

After applying to cluster, its stuck on ContainerCreating:

```sh
kubectl get po -n nokia
NAME                                READY   STATUS              RESTARTS   AGE
nokia-deployment-77dfdf667c-dm559   0/1     ContainerCreating   0          50s
```

Pod Details:

```sh
Events:
  Type     Reason       Age                From               Message
  ----     ------       ----               ----               -------
  Normal   Scheduled    86s                default-scheduler  Successfully assigned nokia/nokia-deployment-77dfdf667c-5pwb5 to Nokia-k8s-node
  Warning  FailedMount  21s (x8 over 85s)  kubelet            MountVolume.SetUp failed for volume "configmap-volume" : configmap "nokia-app-configmap" not found
  Warning  FailedMount  21s (x8 over 85s)  kubelet            MountVolume.SetUp failed for volume "secret-volume" : secret "nokia-login-secret" not found
```

What's the reason? Select corrective answer.

Apply the configmap.yaml named yaml file to the cluster

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nokia-app-configmap
  namespace: nokia
data:
  config.ini: |
    database.url=jdbc:mysql://db.nokia.com:3306/mydb
    logging.level=INFO
```

With the following command:

```sh
kubectl apply -f configmap.yaml
```

Apply secret.yaml

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: nokia-login-secret
  namespace: nokia
type: Opaque
data:
  username: aGVsbG8=
  password: d29ybGQ=

```

With the following command:

```sh
kubectl apply -f secret.yaml
```