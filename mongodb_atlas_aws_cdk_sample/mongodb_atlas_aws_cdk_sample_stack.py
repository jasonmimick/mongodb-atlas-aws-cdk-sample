from aws_cdk import (
    core as cdk
    # aws_sqs as sqs,
)

import requests
from requests.auth import HTTPDigestAuth

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class MongodbAtlasAwsCdkSampleStack(cdk.Stack):

    def first_org_id(self,public,private):
        print(f"-- first_org_id public={public}")
        #print(f"-- first_org_id private={private}")
        url = "https://cloud.mongodb.com/api/atlas/v1.0/orgs"
        response= requests.get(url,
                               auth=HTTPDigestAuth(public,private))
        #print(f"fetch_orgs response={response}")
        response.raise_for_status()
        orgs = response.json()
        #print(f"orgs={orgs}")
        org_id = orgs['results'][0]['id']
        return org_id

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "MongodbAtlasAwsCdkSampleQueue",
        #     visibility_timeout=cdk.Duration.seconds(300),
        # )
        #project_name = str(cdk.Stack.stack_name)
        project_name = self.node.try_get_context("project_name")
        print(f"project_name={project_name}")

        public_key = self.node.try_get_context("atlas_public_key")
        private_key = self.node.try_get_context("atlas_private_key")

        #print(f"public_key={public_key}")
        # Look up the org_id from the with the key; pick first one.
        org_id=self.first_org_id(public_key, private_key)
        #print(f"org_id={org_id}")
        project = cdk.CfnResource(self, project_name,
                type="MongoDB::Atlas::Project",
                properties={
                  "ApiKeys": {
                    "PublicKey": public_key,
                    "PrivateKey": private_key
                  },
                  "OrgId": org_id,
                  "Name": project_name 
                }
        )
        #print(f"project={project}")


