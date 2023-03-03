# Charts

## Download

```sh
mkdir cluster-config
cd cluster-config

helm pull --help
helm pull bitnami/mysql --untar=true
helm install mysql ./mysql/
helm upgrade mysql --values=./mysql/custom-values.yaml ./mysql/
```

## Convert to k8s configuration

```sh
helm template mysql ./mysql/ --values=./mysql/custom-values.yaml > mysql-installation.yaml
```

## Create charts

```sh
helm create example-helm-chart
cd example-helm-chart/
helm template . # to test the output
```

Reference values in the template: `{{ .Values.MyKey }}`

Call function in the template with space-separated list of parameters: `{{ lower .Values.MyKey }}`

Pass values to a function through a pipeline: `{{ .Values.MyKey | upper }}`

Example of flow control:

```yml
image:
  version: v0.1.0{{ if eq .Values.environment "dev" }}-dev{{ end }}
```

Files containing named templates have names starting with underscore.

Example of named template in `_shared.tpl`:

```
{{ define "example" }}
- name: xxx
  value: yyy
{{ end }}
```

Using named template:

```
mylist:
{{- include "example" . | indent 2}}
```

Prefix k8s object names with release name:

```
metadata:
  name: {{ .Release.Name }}-webapp
```