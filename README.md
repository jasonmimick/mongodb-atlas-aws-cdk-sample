# MongoDB Atlas AWS CDK Sample

This is a first start example of how you can use CDN Level 1 constructs with the MongoDB Atlas AWS CloudFormation resources.

It was generated from `cdk init app --language python`.

There is 1 example stack which creates an Atlas Project.

You need to pass in your MongoDB Atlas APIKEY via context:

```bash
cdk deploy --context atlas_public_key=${ATLAS_PUBLIC_KEY} --context atlas_private_key=${ATLAS_PRIVATE_KEY} --context project_name=${YOUR_PROJECT_NAME}
mongodb-cdk-cdk1: deploying...
mongodb-cdk-cdk1: creating CloudFormation changeset...

 ✅  mongodb-cdk-cdk1

Stack ARN:
arn:aws:cloudformation:us-east-1:466197078724:stack/mongodb-cdk-cdk1/771ec470-5498-11ec-8373-0a596eda02f3
```

It's still not clear how to pass the stack name into the cdk to make it the same as the Atlas project name.
