"""
Main interface for application-autoscaling service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_application_autoscaling import (
        ApplicationAutoScalingClient,
        Client,
        DescribeScalableTargetsPaginator,
        DescribeScalingActivitiesPaginator,
        DescribeScalingPoliciesPaginator,
        DescribeScheduledActionsPaginator,
    )

    session = Session()
    client: ApplicationAutoScalingClient = session.client("application-autoscaling")

    describe_scalable_targets_paginator: DescribeScalableTargetsPaginator = client.get_paginator("describe_scalable_targets")
    describe_scaling_activities_paginator: DescribeScalingActivitiesPaginator = client.get_paginator("describe_scaling_activities")
    describe_scaling_policies_paginator: DescribeScalingPoliciesPaginator = client.get_paginator("describe_scaling_policies")
    describe_scheduled_actions_paginator: DescribeScheduledActionsPaginator = client.get_paginator("describe_scheduled_actions")
    ```
"""

from .client import ApplicationAutoScalingClient
from .paginator import (
    DescribeScalableTargetsPaginator,
    DescribeScalingActivitiesPaginator,
    DescribeScalingPoliciesPaginator,
    DescribeScheduledActionsPaginator,
)

Client = ApplicationAutoScalingClient

__all__ = (
    "ApplicationAutoScalingClient",
    "Client",
    "DescribeScalableTargetsPaginator",
    "DescribeScalingActivitiesPaginator",
    "DescribeScalingPoliciesPaginator",
    "DescribeScheduledActionsPaginator",
)
