from diagrams import Diagram, Cluster, Edge

from diagrams.aws.general import Users
from diagrams.aws.network import Route53
from diagrams.aws.network import Route53HostedZone
from diagrams.aws.security import Shield
from diagrams.aws.network import CloudFront
from diagrams.aws.storage import SimpleStorageServiceS3

from diagrams.onprem.gitops import ArgoCD

with Diagram("AWS static WebApp", filename="aws-static-webapp", show=False, direction="LR"):

    users = Users("Users")

    with Cluster("AWS Cloud"):
        shield = Shield()
        dns = Route53("DNS")
        hosted_zone = Route53HostedZone("Hosted Zone")
        cdn = CloudFront("CDN")
        storage = SimpleStorageServiceS3("Storage")

    with Cluster("On-prem"):
        workflow = ArgoCD("Workflow")

    users >> Edge(forward=True, reverse=True) >> dns
    dns >> Edge(forward=True, reverse=True) >> hosted_zone

    hosted_zone >> Edge(forward=True, reverse=True) >> cdn
    cdn >> Edge(style="dashed", forward=True, reverse=True) >> storage

    storage << workflow