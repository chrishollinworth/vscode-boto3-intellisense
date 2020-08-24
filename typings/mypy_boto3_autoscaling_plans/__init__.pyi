"""
Main interface for autoscaling-plans service.

Usage::

    ```python
    import boto3
    from mypy_boto3_autoscaling_plans import (
        AutoScalingPlansClient,
        Client,
        DescribeScalingPlanResourcesPaginator,
        DescribeScalingPlansPaginator,
    )

    session = boto3.Session()

    client: AutoScalingPlansClient = boto3.client("autoscaling-plans")
    session_client: AutoScalingPlansClient = session.client("autoscaling-plans")

    describe_scaling_plan_resources_paginator: DescribeScalingPlanResourcesPaginator = client.get_paginator("describe_scaling_plan_resources")
    describe_scaling_plans_paginator: DescribeScalingPlansPaginator = client.get_paginator("describe_scaling_plans")
    ```
"""
from mypy_boto3_autoscaling_plans.client import AutoScalingPlansClient
from mypy_boto3_autoscaling_plans.paginator import (
    DescribeScalingPlanResourcesPaginator,
    DescribeScalingPlansPaginator,
)

Client = AutoScalingPlansClient


__all__ = (
    "AutoScalingPlansClient",
    "Client",
    "DescribeScalingPlanResourcesPaginator",
    "DescribeScalingPlansPaginator",
)
