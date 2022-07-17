import aws_cdk as core
import aws_cdk.assertions as assertions

from cloud_formation.cloud_formation_stack import CloudFormationStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cloud_formation/cloud_formation_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CloudFormationStack(app, "cloud-formation")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
