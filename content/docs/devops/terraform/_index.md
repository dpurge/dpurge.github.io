---
title: Terraform
bookCollapseSection: true
---

Terraform can provision infratsructure on public and private clouds.

Example provider configuration:

```terraform
provider "aws" {
    region = "us-east-2"
}
```

Generic formats:

```terraform
data "{provider}_{type}" "{name}" {
    {config}
}

resource "{provider}_{type}" "{name}" {
    {config}
}
```

Reference formats:

```terraform
data.{provider}_{type}.{name}.{attribute}
```

Example:

```terraform
provider "aws" {
    region = "us-east-2"
}

variable "server_port" {
    description = "The port on which the HTTP server will run"
    default = 8080
    type  = number

    validation {
        condition  = var.server_port} > 0 && var.server_port < 65536
        error_message  = "Port must be between 1 and 65535"
    }

    sensitive = true
}

data "aws_vpc" "this" {
    default = true
}

data "aws_subnets" "this" {
    filter {
        name = "vpc-id"
        values = [data.aws_vpc.this.id]
    }
}

resource "aws_security_group" "this" {
    name   = "allow-web"

    ingress {
        from_port   = var.server_port
        to_port      = var.server_port
        protocol    = "tcp"
        cidr_blocks  = ["0.0.0.0/0"]
    }
}

resource "aws_security_group" "alb" {
    name = "web-alb"

    ingress {
        from_port   = 80
        to_port = 80
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port  = 0
        to_port    = 0
        protocol   = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_launch_configuration" "this" {
    image_id = "ami-0c94855ba95c574c8"
    instance_type = "t3.micro"
    security_groups = [aws_security_group.this.id]

    user_data = <<-EOF
        #!/bin/bash
        echo "Hello, World!" > index.html
        nohup busybox httpd -f -p ${var.server_port} &
        EOF

    lifecycle {
        create_before_destroy  = true
    }
}

resource "aws_autoscaling_group" "this" {
    launch_configuration = aws_launch_configuration.this.name
    vpc_zone_identifier = data.aws_subnets.this.ids

    target_group_arns = [aws_lb_target_group.this.arn]
    health_check_type  = "ELB"

    min_size  = 2
    max_size  = 4

    tag {
        key    = "Name"
        value  = "web"
        propagate_at_launch  =  true
    }
}

resource "aws_lb" "this" {
    name = "web"
    load_balancer_type = "application"
    subnets = data.aws_subnets.this.ids
    security_groups = [aws_security_group.alb.id]
}

resource "aws_lb_listener" "http" {
    load_balancer_arn = aws_lb.this.arn
    port = 80
    protocol = "HTTP"

    default_action {
        type = "fixed-response"

        fixed_response {
            content_type = "text/plain"
            message_body = "404: page not found"
            status_code  = 404
        }
    }
}

resource "aws_lb_target_group" "this" {
    name = "web-example"
    port = var.server_port
    protocol = "HTTP"
    vpc_id = data.aws_vpc.this.id

    health_check {
        path = "/"
        protocol = "HTTP"
        matcher = "200"
        interval = 15
        timeout = 3
        healthy_threshold  = 2
        unhealthy_threshold  = 2
    }
}

resource "aws_lb_listener_rule" "this" {
    listener_arn = aws_lb_listener.http.arn
    priority = 100

    condition {
        path_pattern {
            values = ["*"]
        }
    }

    action {
        type = "forward"
        target_group_arn = aws_lb_target_group.this.arn
    }
}

output "alb_dns_name" {
    description = "DNS name of the application load balancer"
    value = aws_lb.this.dns_name
    sensitive = false
}
```

```sh
#!/bin/bash
set -o xtrace

terraform apply --auto-approve
ALB=$(terraform output alb_dns_name | tr -d '"')
curl http://${ALB}/
```
