# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for autoscaling service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_autoscaling import AutoScalingClient
    from mypy_boto3_autoscaling.paginator import (
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

    client: AutoScalingClient = boto3.client("autoscaling")

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
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_autoscaling.type_defs import (
    ActivitiesTypeTypeDef,
    AutoScalingGroupsTypeTypeDef,
    AutoScalingInstancesTypeTypeDef,
    DescribeLoadBalancersResponseTypeDef,
    DescribeLoadBalancerTargetGroupsResponseTypeDef,
    DescribeNotificationConfigurationsAnswerTypeDef,
    FilterTypeDef,
    LaunchConfigurationsTypeTypeDef,
    PaginatorConfigTypeDef,
    PoliciesTypeTypeDef,
    ScheduledActionsTypeTypeDef,
    TagsTypeTypeDef,
)

__all__ = (
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


class DescribeAutoScalingGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAutoScalingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingGroups)
    """

    def paginate(
        self,
        AutoScalingGroupNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[AutoScalingGroupsTypeTypeDef]:
        """
        [DescribeAutoScalingGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingGroups.paginate)
        """


class DescribeAutoScalingInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAutoScalingInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingInstances)
    """

    def paginate(
        self, InstanceIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[AutoScalingInstancesTypeTypeDef]:
        """
        [DescribeAutoScalingInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeAutoScalingInstances.paginate)
        """


class DescribeLaunchConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLaunchConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLaunchConfigurations)
    """

    def paginate(
        self,
        LaunchConfigurationNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[LaunchConfigurationsTypeTypeDef]:
        """
        [DescribeLaunchConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLaunchConfigurations.paginate)
        """


class DescribeLoadBalancerTargetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLoadBalancerTargetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancerTargetGroups)
    """

    def paginate(
        self, AutoScalingGroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLoadBalancerTargetGroupsResponseTypeDef]:
        """
        [DescribeLoadBalancerTargetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancerTargetGroups.paginate)
        """


class DescribeLoadBalancersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancers)
    """

    def paginate(
        self, AutoScalingGroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLoadBalancersResponseTypeDef]:
        """
        [DescribeLoadBalancers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeLoadBalancers.paginate)
        """


class DescribeNotificationConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeNotificationConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeNotificationConfigurations)
    """

    def paginate(
        self,
        AutoScalingGroupNames: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeNotificationConfigurationsAnswerTypeDef]:
        """
        [DescribeNotificationConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeNotificationConfigurations.paginate)
        """


class DescribePoliciesPaginator(Boto3Paginator):
    """
    [Paginator.DescribePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribePolicies)
    """

    def paginate(
        self,
        AutoScalingGroupName: str = None,
        PolicyNames: List[str] = None,
        PolicyTypes: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[PoliciesTypeTypeDef]:
        """
        [DescribePolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribePolicies.paginate)
        """


class DescribeScalingActivitiesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScalingActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScalingActivities)
    """

    def paginate(
        self,
        ActivityIds: List[str] = None,
        AutoScalingGroupName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ActivitiesTypeTypeDef]:
        """
        [DescribeScalingActivities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScalingActivities.paginate)
        """


class DescribeScheduledActionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScheduledActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScheduledActions)
    """

    def paginate(
        self,
        AutoScalingGroupName: str = None,
        ScheduledActionNames: List[str] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ScheduledActionsTypeTypeDef]:
        """
        [DescribeScheduledActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeScheduledActions.paginate)
        """


class DescribeTagsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeTags)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[TagsTypeTypeDef]:
        """
        [DescribeTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling.html#AutoScaling.Paginator.DescribeTags.paginate)
        """
