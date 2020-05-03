## Website on AWS

```
aws s3 mb s3://kbase-app-ajs-aws --profile Administrator
aws s3 website s3://kbase-app-ajs-aws --index-document index.html --profile Administrator
aws s3api put-bucket-policy --bucket kbase-app-ajs-aws --policy file://~/Code/kbase/aws-cli/app-bucket-policy.json
```