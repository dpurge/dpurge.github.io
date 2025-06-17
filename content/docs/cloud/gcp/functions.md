# Cloud functions

## Manual depoyment

```sh
gcloud functions deploy my-function \
  --source https://source.developers.google.com/projects/test1/repos/github_example_functions/moveable-aliases/main/paths/my-function \
  --runtime nodejs16 \
  --trigger-http \
  --entry-point helloWorld
```

When redeploying, do not specify runtime or trigger.

## Cloud Build deployment

Get project ID and project number and grant permissions:

```sh
gcloud projects describe test1

gcloud iam service-accounts add-iam-policy-binding PROJECT_ID@appspot.gserviceaccount.com --member PROJECT_NUMBER@cloudbuild.gserviceaccount.com --role roles/iam.serviceAccountUser

gcloud projects add-iam-policy-binding PROJRCT_ID --member serviceAccount:PROJECT_NUMBER@cloudbuild.gserviceaccount.com --role roles/cloudfunctions.developer
```

Create `cloudbuild.yaml`:

```yaml
- steps:
  - name: 'gcr.io/cloud-builders/npm'
    args: ['install']
    dir: 'my-function'
  - name: 'gcr.io/cloud-builders/npm'
    args: ['test']
    dir: 'my-function'
  - name: 'gcr.io/cloud-bulders/gcloud'
    args: ['functions', 'deploy', 'my-function', '--trigger-http', '--runtime', 'nodejs16', '--entry-point', 'helloWorld']
    dir: 'my-function'
```

## Terraform deployment

```tf
locals {
    project_id = "test1"
    timestamp = formatdate("YYMMDDhhmmss", timestamp())
}

provider "google" {
    project = local.project_id
    region = "us-central1"
}

data "archive_file" "this" {
    type = "zip"
    source_dir = "my-function"
    output_path = "/tmp/functions-${local.timestamp}.zip"
}

resource "google_storage_bucket" "this" {
    name = "${local.project_id}-functions"
    location = "US"
}

resource "google_storage_bucket_object" "this" {
    name = "functions.zip#${data.archive_file.this.output_md5}"
    bucket = google_storage_bucket.this.name
    source = data.archive_file.this.output_path
}

resource "google_cloudfunctions_function" "this" {
    name = "my-function"
    runtime = "nodejs16"

    available_memory_mb = 128
    source_archive_bucket = google_storage_bucket.this.name
    source_archive_object = google_storage_bucket_object.this.name
    trigger_http = true
    entry_point = "helloWorld"
}

resource "google_cloudfunctions_function_iam_member" "invoker" {
    project = google_cloudfunctions_function.this.project
    region = google_cloudfunctions_function.this.region
    cloud_function = google_cloudfunctions_function.this.name

    role = "roles/cloudfunctions.invoker"
    member = "allUsers"
}

output "function_url" {
    value = google_cloudfunctions_function.this.https_trigger_url
}
```

## NodeJS setup

```sh
npm install --save-dev @google-cloud/functions-framework
```

Specify entry point in `package.json`:

```json
{
    "name": "my-function",
    "version": "0.0.1",
    "devDependencies": {
        "@google-cloud/functions-framework": "^2.1.0"
    },
    "script": {
        "start": "npx functions-framework --target=helloWorld --signature-type=http --port=8080"
    }
}
```

Body of the function in `index.js`:

```js
exports.helloWorld = (req, res) => {
    res.send('Hello World!');
}
```

Run:

```sh
npm start
curl localhost:8080
```

## API Gateway

For API Gateway create service accounts.

Write API description in `openapi2-functions.yaml` to upload:

```yaml
---
swagger: '2.0'
info:
  title: test-name-spec
  description: Sample API on API Gateway
  version: 1.0.0
schemes:
  - https
produces:
  - application/json
paths:
  /helloWorld:
    get:
      summary: Greet a user
      operationId: hello
      x-google-backend:
        address: https://us-central1-....cloudfunctions.net/my-function
      responses:
        '200':
          description: A successful response
          schema:
            type: string
```
