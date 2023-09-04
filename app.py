#!/usr/bin/env python3
import os

import aws_cdk as cdk

from app_project.app_project_stack import EC2InstanceStack


app = cdk.App()
EC2InstanceStack(app, "EC2InstanceStack")

app.synth()
