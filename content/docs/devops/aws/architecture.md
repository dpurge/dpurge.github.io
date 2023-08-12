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

![static web application](https://raw.githubusercontent.com/dpurge/dpurge.github.io/gh-pages/docs/devops/aws/architecture_static_website.drawio.svg)

## Web application with relational database

Use Fargate for ECS.

![web application with relational database](https://raw.githubusercontent.com/dpurge/dpurge.github.io/gh-pages/docs/devops/aws/architecture_webapp_with_database.drawio.svg)

## Data processing

![data processing application](https://raw.githubusercontent.com/dpurge/dpurge.github.io/gh-pages/docs/devops/aws/architecture_data_processing.drawio.svg)

## Serverless data source monitoring

Problems:

- Monitoring
- Statistics
- Secrets management
- Configuration for Lambda functions

![serverless application for monitoring rest data over time](https://raw.githubusercontent.com/dpurge/dpurge.github.io/gh-pages/docs/devops/aws/architecture_rest_data_monitoring.drawio.svg)

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
