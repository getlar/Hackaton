## RBAC

Role-based access control (RBAC) is a method of regulating access to computer or network resources based on the roles of individual users within your organization. RBAC authorization allowings to dynamically configure policies through the Kubernetes API.

2.

Your company provides Chicken and Egg custom resources. You want to provide a ClusterRole that allows managing these resources, with the exception of deletion. Which of these would be sufficient?

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: chicken-egg-role
rules:
- apiGroups: ['example.com']
  resources: ['chickens','eggs']
  verbs: ['create', 'get', 'list', 'patch', 'update', 'watch']
```

3.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: clusterrole-reader
rules:
- apiGroups: ["rbac.authorization.k8s.io"]
  resources: ["clusterroles"]
  verbs: ["get","read","list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: clusterrole-reader-binding
  namespace: default
subjects:
- kind: ServiceAccount
  name: ithon-test
roleRef:
  kind: Role 
  name: clusterrole-reader 
  apiGroup: rbac.authorization.k8s.io
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: role-reader
rules:
- apiGroups: ["rbac.authorization.k8s.io"]
  resources: ["roles"]
  verbs: ["get","read","list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: role-reader-binding
  namespace: default
subjects:
- kind: ServiceAccount
  name: ithon-test
roleRef:
  kind: Role 
  name: role-reader 
  apiGroup: rbac.authorization.k8s.io
```