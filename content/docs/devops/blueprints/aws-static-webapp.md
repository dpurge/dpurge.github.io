# AWS static web application

![AWS static web application](https://raw.githubusercontent.com/dpurge/dpurge.github.io/gh-pages/docs/devops/blueprints/aws-static-webapp.png)

Components:

- *AWS Shield Standard* - free protection against common DDoS attacks,
  applied automatically to CloudFront and Route 53.
- *Route 53* - Domain Name System web service, performs domain registration,
  DNS routing and health checking.
- *Hosted Zone* - container for records specifying how to route traffic for a
  specific domain.
- *CloudFront* - content delivery network for distributing static content from
  edge locations.
- *S3 bucket* - cloud storage for web content
- *Argo Workflows* - pipelines producing web content and publishing it to the
  cloud storage