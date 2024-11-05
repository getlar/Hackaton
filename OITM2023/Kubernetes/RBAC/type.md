## Networking

In Kubernetes, "networking" refers to the mechanisms that enable communication between various components within the cluster. Each pod within the cluster is assigned a unique IP address, facilitating direct communication between pods. Services act as an abstraction layer, providing a consistent IP and load balancing for pods. Network Policies offer fine-grained control over traffic flow, allowing administrators to enforce communication rules between pods based on their labels.

1.

You have a Kubernetes cluster with Calico as the network plugin. Two deployments, web-app and database, reside in the same namespace called production. After a recent set of changes, traffic from web-app to database has been inadvertently blocked.

Given the following output from 'calicoctl get networkpolicy -n production':

```yaml
NAME                  ORDER   SELECTOR
web-to-db-egress      1000    app == 'web-app'
db-ingress            1500    app == 'database'
default-allow         2000    app in {"web-app", "database"}
```

web-to-db-egress
```yaml
apiVersion: projectcalico.org/v3
kind: NetworkPolicy
metadata:
  name: web-to-db-egress
  namespace: production
spec:
  selector: app == 'web-app'
  types:
  - Egress
  egress:
  - action: Allow
    destination:
      selector: app == 'database'
  - action: Deny
    destination:
      notSelector: app == 'database'
```

db-ingress
```yaml
apiVersion: projectcalico.org/v3
kind: NetworkPolicy
metadata:
  name: db-ingress
  namespace: production
spec:
  selector: app == 'database'
  types:
  - Ingress
  ingress:
  - action: Deny
    source:
      selector: app == 'web-app'
```

default-allow
```yaml
apiVersion: projectcalico.org/v3
kind: NetworkPolicy
metadata:
  name: default-allow
  namespace: production
spec:
  selector: app in {"web-app", "database"}
  types:
  - Ingress
  - Egress
  egress:
  - action: Allow
  ingress:
  - action: Allow
```


Which modification(s) would you make to restore traffic from web-app to database?

Modify the web-to-db-egress policy to remove the Deny action for destinations not labeled as database

Modify the db-ingress policy to change the Deny action for sources labeled as web-app to Allow Ez a válasz helyes, és meg is jelölted.

Delete the db-ingress policy

Modify the default-allow policy to increase its order to be less than 1500

Modify the db-ingress policy's selector to app=='web-app'