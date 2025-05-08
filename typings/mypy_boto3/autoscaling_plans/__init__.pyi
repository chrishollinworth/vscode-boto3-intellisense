"""
Main interface for autoscaling-plans service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_autoscaling_plans import (
        AutoScalingPlansClient,
        Client,
        DescribeScalingPlanResourcesPaginator,
        DescribeScalingPlansPaginator,
    )

    session = Session()
    client: AutoScalingPlansClient = session.client("autoscaling-plans")

    describe_scaling_plan_resources_paginator: DescribeScalingPlanResourcesPaginator = client.get_paginator("describe_scaling_plan_resources")
    describe_scaling_plans_paginator: DescribeScalingPlansPaginator = client.get_paginator("describe_scaling_plans")
    ```
"""

from .client import AutoScalingPlansClient
from .paginator import DescribeScalingPlanResourcesPaginator, DescribeScalingPlansPaginator

Client = AutoScalingPlansClient

__all__ = (
    "AutoScalingPlansClient",
    "Client",
    "DescribeScalingPlanResourcesPaginator",
    "DescribeScalingPlansPaginator",
)
