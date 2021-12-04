# MongoDB Atlas AWS CDK Sample

This is a first start example of how you can use CDN Level 1 constructs with the MongoDB Atlas AWS CloudFormation resources.

It was generated from `cdk init app --language python`.

There is 1 example stack which creates an Atlas Project.

You need to pass in your MongoDB Atlas APIKEY via context:

```bash
ATLAS_DEPLOYMENT_NAME="butter-betty-bought" && cdk deploy --context atlas_public_key=${ATLAS_PUBLIC_KEY} --context atlas_private_key=${ATLAS_PRIVATE_KEY} --context project_name=butter-betty-bought            
Atlas project_name=butter-betty-bought
project_name=butter-betty-bought-- 
mongodb-cdk-butter-betty-bought: deploying...
mongodb-cdk-butter-betty-bought: creating CloudFormation changeset...

 ✅  mongodb-cdk-butter-betty-bought

Stack ARN:
arn:aws:cloudformation:us-east-1:XXXXXXXXXX:stack/mongodb-cdk-butter-betty-bought/XXXXXXXXXXX```

It's still not clear how to pass the stack name into the cdk to make it the same as the Atlas project name.
