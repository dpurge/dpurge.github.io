# IAM

IAM = Identity Access Management

Manages: *Identity* (who?) has *role* (what access) for which *resource* (or organization, project, folder).

Use the principle of least access.

Permissions not granted directly to the user.
Permissions are grouped into roles which are granted to the authenticated members.

IAM policy defines and enforces what roles are granted to which members.
This policy is attached to a resource.

## Policy architecture

```yaml
Policy:
  Metadata:
    etags: concurrency control
    version: specifies schema version
  Audit-Config: configures audit logging
  Binding:
    Condition: constrains binding
    Member: []
    Role:
      Permissions: []
```

Member is an identity that can access a resource.
Identity is an e-mail account associated with a user, service account or a Google group, a domain name associated with a GSuite or cloud identity domains.

Google Account
: any email address that is associated with a Google Account, either gmail.com or other domains

Service Account
: an account for an application instead of an individual end user

Google Group
: a named collection of Google Accounts and service accounts

G Suite Domain
: Google Accounts created in an organization's G Suite account

Cloud Identity Domain
: Google Accounts in an organization that are not tied to any G Suite applications or features

AllAUthenticatedUsers
: a special identifier that represents all service accounts and all users on the internet who have authenticated with a Google Account

AllUsers
: a special identifier that represents anyone, including authenticated and unauthenticated users

Permissions determine what operations are allowed on a resource.
They correspond one-to-one with REST API methods.
Permissions are not granted to users directly.
You grant roles which contain one or more permissions.
Permissions are represented as *{service}.{resource}.{verb}*, eg. `compute.instances.list`

Roles are collections of permissions.
You cannot grant a permission to the user directly.
You grant a role to a user and all the permissions that the role contains.

There are three types of roles:

Primitive roles
: `Owner`, `Editor`, `Viewer`; historically available prior to IAM; avoid using these roles; can only be grated from a Google console

Predefined roles
: finer-grained access control than the primitive roles; created and maintained by Google

Custom roles
: tailor permissions to the needs of your organization; not maintained by Google; cannot be created at folder level; by default only project owner can create new roles

Custom role *launch stages*:

- alpha = in testing
- beta = tested and awaiting approval
- ga = generally available

Condition is a logic expression used to define and enforce attribute-based access control for Google Cloud resources.
Conditions allow you to choose granting resource access to identities only if configured conditions are met.
When a contition exists, the access request is only granted if the condition expression evaluates to `true`.

Metadata etags prevent a race condition when updating the policy.

Metadata version is used to avoid breaking existing integrations that rely on consistency in the policy structure when new policy schema versions are introduced.

Audit config configures audit logging; determines which permission types are logged and what identities are exempted from logging.

Resource inherit the policies of all their parent resources.
The policy is a union of a resource direct policy and the policies of all its parents in the resource hierarchy (organization, folders, project, resource).

Example policy statement (can be expressed in JSON or YAML):

```json
{
    "bindings": [
        {
            "role": "roles/storage.admin",
            "members": [
                "user:example@gmail.com"
            ]
        },
        {
            "role": "roles/storage.objectViewer",
            "members": [
                "user:other@gmail.com"
            ],
            "condition": {
                "title": "Expires_January_1_2021",
                "description": "Do not grant access after Jan 2021",
                "expression": "request.time < timestamp('2021-01-01T00:00:00.000Z')"
            }
        }
    ],
    "etag": "BeEEja0YfWJ=",
    "version": 3
}
```

Querying for policies:

```sh
gcloud projects get-iam-policy {project-id}
gcloud resource-manager folders get-iam-policy {folder-id}
gcloud organizations get-iam-policy {organization-id}
```

Policy versions:

version 1
: default; supports binding one role to one or more members; does not support conditional role bindings

version 2
: for Google's internal use

version 3
: introduces condition statement

## Policy limitations

- each resource can only have one policy (including organizations, projects, folders)
- max 1500 members or 250 Google groups per policy
- up to 7 minutes for a policy change to fully propagate across GCP
- max 100 conditional role bindings per policy

## Policy conditions

Condition attributes are either based on resource or based on details of the request, eg. timestamp or originating/destination IP address

```yaml
bindings:
- members:
  - user:me@gmail.com
  role: roles/owner
- members:
  - user:example@gmail.com
  role: roles/storage.objectViewer
  condition:
    title: Business_hours_access
    description: Business hours access Monday-Friday
    expression: request.time.getHours("America/Toronto") >= 9 &&
                request.time.getHours("America/Toronto") <= 17 &&
                // 0 = Sunday, 6 = Saturday
                request.time.getDayOfWeek("America/Toronto") >= 1 &&
                request.time.getDayOfWeek("America/Toronto") <= 5
etag: xxx
version: 3
```

```yaml
bindings:
- members:
  - user:me@gmail.com
  role: roles/owner
- members:
  - group:developer@mydomain.com
  role: roles/compute.instanceAdmin
  condition:
    title: Dev_only_access
    description: Only access to development* VMs
    expression: (resource.type == 'compute.googleapis.com/Disk' &&
                resource.name.startsWith('projects/project-my-example/regions/us-central1/disks/development')) ||
                (resource.type == 'compute.googleapis.com/Instance' &&
                resource.name.startsWith('projects/project-my-example/zones/us-central1-a/instances/development')) ||
                (resource.type != 'compute.googleapis.com/Instance' &&
                resource.type != 'compute.googleapis.com/Disk')
etag: xxx
version: 3
```

Condition limitations:

- limited to specific services
- primitive roles are not supported
- members cannot be `allUsers` or `allAuthenticatedUsers`
- max 100 conditional role bindings per policy
- max 20 role bindings for the same role and the same member

## Audit config logs

```yaml
auditConfigs:
- auditLogConfigs:
  - logType: DATA_READ
  - logType: ADMIN_READ
  - logType: DATA_WRITE
  service: allServices
- auditLogConfigs:
  - exmptedMembers:
    - me@gmail.com
    logType: ADMIN_READ
  service: storage.googleapis.com
```

## Edit policy

```sh
gcloud projects get-iam-policy {project-id} > new-policy.yaml
gcloud projects set-iam-policy {project-id} new-policy.yaml
```

Make sure that etag is correct, or you will not be able to set the new policy.

Granting access from the command line:

```sh
gcloud projects add-iam-policy-binding {project-id} --member user:somebody@gmail.com --role roles/storage.admin
```

## Service accounts

A service account is both an identity and a resource.

Service account is a special kind of account used by an application or a virtual machine instance and not a person.
It represents a non-human user.
A service account is identified by an email address which is unique.

There are three service account types:

User-managed
: user created; you choose the name; default quota 100 user accounts per project

Default
: some services automatically create user-managed service account with *Editor* role for the project; Google recommends revoking Editor role manually

Google-managed
: created and managed by Google; used by Google services; some visible, some hidden; name ends with "Service Agent" or "Service Account"; do not change or revoke roles for these accounts

Email format for user mananaged service accounts: `{service-name}@{project-id}.iam.gserviceaccount.com`

Email formats for the default service accounts:

- `{project-id}@appspot.gserviceaccount.com`
- `{project-number}-compute@developer.gserviceaccount.com`

Service accounts authenticate using keys.
Each service has two sets of private and public RSA keypairs.

There are Google managed and user managed keys.

```sh
gcloud iam service-accounts list
gcloud iam service-accounts create sa-example --display-name='sa-example'
gcloud projects add-iam-policy-binding {project-name} --member 'serviceAccount:{account-name}@{project-name}.iam.gserviceaccount.com' --role 'roles/storage.objectViewer'
gcloud compute instances stop instance-1 --zone us-central1-a
gcloud compute instances set-service-account instance-1 --zone us-central1-a --service-account sa-example@{project-name}.iam.gserviceaccount.com
gcloud compute instances start instance-1 --zone us-central1
```
