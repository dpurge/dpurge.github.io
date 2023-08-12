# Learn architecture

<!--
See:
    - [Gherkin](https://cucumber.io/docs/gherkin/reference/)
    - [Markdown with Gherkin](https://github.com/cucumber/gherkin/blob/main/MARKDOWN_WITH_GHERKIN.md)

VSCode tip: `Ctr-K V` for preview
-->

Exercises in simple application architecture design.

Tutorial: [AWS Prescriptive Guidance](https://aws.amazon.com/prescriptive-guidance/)

## Static website

```ascii
Browser
    <--> Route53
        <--  CloudFront
            <-- S3
```

## Web application with relational database

```ascii
Browser
    <--> Load Balancer
        <--> (VPC + ECS + ECR)
            <--> RDS
```

## Data processing

```ascii
Data stream
--> App?
    --> Kinesis Firehose
        (save 5min/5MB chunks of data)
        --> S3
            (put notification: location and name of the file)
            --> Lambda function
                (get file content and parse)
                (send data structure to be indexed)
                --> ElasticSearch
                    <--> Kibana
                         (display dashboards from ElasticSerach)
```

## Serverless data source monitoring

Problems:

- Monitoring
- Statistics
- Secrets management
- Configuration for Lambda functions

![image info](https://raw.githubusercontent.com/dpurge/dpurge.github.io/gh-pages/docs/devops/aws/architecture_rest_data_monitoring.drawio.svg)

```gherkin
Feature: process changes in the data source

  Scenario: data source has changes
    Given for each $currentValue in $batchOfChanges
      And $previousValue of $currentValue
    When $currenValue != $previousValue
    Then save $currentValue in the data index
    
  Scenario: data source has no changes
    Given new batch of changes
    When current value equals previous value

Feature: notify users about interesting changes
  Scenario: the change is interesting
    Given data source has changed
    When the change is small
    Then do nothing
  Scenario: the change is not interesting
    Given data source has changed
    When the change is big
    Then send email to the user

Feature: show monitoring dashboard
  Scenario: new event saved to data index
```
