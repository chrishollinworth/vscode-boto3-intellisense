"""
Main interface for autoscaling service.

Usage::

    ```python
    import boto3
    from mypy_boto3_autoscaling import (
        AutoScalingClient,
        Client,
        DescribeAutoScalingGroupsPaginator,
        DescribeAutoScalingInstancesPaginator,
        DescribeLaunchConfigurationsPaginator,
        DescribeLoadBalancerTargetGroupsPaginator,
        DescribeLoadBalancersPaginator,
        DescribeNotificationConfigurationsPaginator,
        DescribePoliciesPaginator,
        DescribeScalingActivitiesPaginator,
        DescribeScheduledActionsPaginator,
        DescribeTagsPaginator,
    )

    session = boto3.Session()

    client: AutoScalingClient = boto3.client("autoscaling")
    session_client: AutoScalingClient = session.client("autoscaling")

    describe_auto_scaling_groups_paginator: DescribeAutoScalingGroupsPaginator = client.get_paginator("describe_auto_scaling_groups")
    describe_auto_scaling_instances_paginator: DescribeAutoScalingInstancesPaginator = client.get_paginator("describe_auto_scaling_instances")
    describe_launch_configurations_paginator: DescribeLaunchConfigurationsPaginator = client.get_paginator("describe_launch_configurations")
    describe_load_balancer_target_groups_paginator: DescribeLoadBalancerTargetGroupsPaginator = client.get_paginator("describe_load_balancer_target_groups")
    describe_load_balancers_paginator: DescribeLoadBalancersPaginator = client.get_paginator("describe_load_balancers")
    describe_notification_configurations_paginator: DescribeNotificationConfigurationsPaginator = client.get_paginator("describe_notification_configurations")
    describe_policies_paginator: DescribePoliciesPaginator = client.get_paginator("describe_policies")
    describe_scaling_activities_paginator: DescribeScalingActivitiesPaginator = client.get_paginator("describe_scaling_activities")
    describe_scheduled_actions_paginator: DescribeScheduledActionsPaginator = client.get_paginator("describe_scheduled_actions")
    describe_tags_paginator: DescribeTagsPaginator = client.get_paginator("describe_tags")
    ```
"""
from mypy_boto3_autoscaling.client import AutoScalingClient
from mypy_boto3_autoscaling.paginator import (
    DescribeAutoScalingGroupsPaginator,
    DescribeAutoScalingInstancesPaginator,
    DescribeLaunchConfigurationsPaginator,
    DescribeLoadBalancersPaginator,
    DescribeLoadBalancerTargetGroupsPaginator,
    DescribeNotificationConfigurationsPaginator,
    DescribePoliciesPaginator,
    DescribeScalingActivitiesPaginator,
    DescribeScheduledActionsPaginator,
    DescribeTagsPaginator,
)

Client = AutoScalingClient


__all__ = (
    "AutoScalingClient",
    "Client",
    "DescribeAutoScalingGroupsPaginator",
    "DescribeAutoScalingInstancesPaginator",
    "DescribeLaunchConfigurationsPaginator",
    "DescribeLoadBalancerTargetGroupsPaginator",
    "DescribeLoadBalancersPaginator",
    "DescribeNotificationConfigurationsPaginator",
    "DescribePoliciesPaginator",
    "DescribeScalingActivitiesPaginator",
    "DescribeScheduledActionsPaginator",
    "DescribeTagsPaginator",
)
