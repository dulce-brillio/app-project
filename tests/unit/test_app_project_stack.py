import aws_cdk as core
import aws_cdk.assertions as assertions

from app_project.app_project_stack import AppProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in app_project/app_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AppProjectStack(app, "app-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
