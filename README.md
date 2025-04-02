# Todo

### Install SAM CLI

https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html

AWS: Detect SAM CLI

In case of problems with docker do this: https://stackoverflow.com/a/77926411/1816687

### Install AWS Toolkit VSCode extension

Edit AWS CLI credentials and configuration

Edit files:
- `~/.aws/config` - for configuration
- `~/.aws/credentials` - for credentials

Add new profile if needed e.g. localstack:

Config
```
[localstack]
region = eu-central-1
output = json
s3 =
    endpoint_url = http://localhost:4566
lambda =
    endpoint_url = http://localhost:4566
iam =
    endpoint_url = http://localhost:4566
```

