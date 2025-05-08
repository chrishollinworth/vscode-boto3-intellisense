"""
Type annotations for autoscaling service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_autoscaling.client import AutoScalingClient
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
        DescribeWarmPoolPaginator,
    )

    session = Session()
    client: AutoScalingClient = session.client("autoscaling")

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
    describe_warm_pool_paginator: DescribeWarmPoolPaginator = client.get_paginator("describe_warm_pool")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ActivitiesTypeTypeDef,
    AutoScalingGroupNamesTypePaginateTypeDef,
    AutoScalingGroupsTypeTypeDef,
    AutoScalingInstancesTypeTypeDef,
    DescribeAutoScalingInstancesTypePaginateTypeDef,
    DescribeLoadBalancersRequestPaginateTypeDef,
    DescribeLoadBalancersResponseTypeDef,
    DescribeLoadBalancerTargetGroupsRequestPaginateTypeDef,
    DescribeLoadBalancerTargetGroupsResponseTypeDef,
    DescribeNotificationConfigurationsAnswerTypeDef,
    DescribeNotificationConfigurationsTypePaginateTypeDef,
    DescribePoliciesTypePaginateTypeDef,
    DescribeScalingActivitiesTypePaginateTypeDef,
    DescribeScheduledActionsTypePaginateTypeDef,
    DescribeTagsTypePaginateTypeDef,
    DescribeWarmPoolAnswerTypeDef,
    DescribeWarmPoolTypePaginateTypeDef,
    LaunchConfigurationNamesTypePaginateTypeDef,
    LaunchConfigurationsTypeTypeDef,
    PoliciesTypeTypeDef,
    ScheduledActionsTypeTypeDef,
    TagsTypeTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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
    "DescribeWarmPoolPaginator",
)

if TYPE_CHECKING:
    _DescribeAutoScalingGroupsPaginatorBase = Paginator[AutoScalingGroupsTypeTypeDef]
else:
    _DescribeAutoScalingGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAutoScalingGroupsPaginator(_DescribeAutoScalingGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeAutoScalingGroups.html#AutoScaling.Paginator.DescribeAutoScalingGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describeautoscalinggroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[AutoScalingGroupNamesTypePaginateTypeDef]
    ) -> PageIterator[AutoScalingGroupsTypeTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeAutoScalingGroups.html#AutoScaling.Paginator.DescribeAutoScalingGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describeautoscalinggroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeAutoScalingInstancesPaginatorBase = Paginator[AutoScalingInstancesTypeTypeDef]
else:
    _DescribeAutoScalingInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAutoScalingInstancesPaginator(_DescribeAutoScalingInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeAutoScalingInstances.html#AutoScaling.Paginator.DescribeAutoScalingInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describeautoscalinginstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAutoScalingInstancesTypePaginateTypeDef]
    ) -> PageIterator[AutoScalingInstancesTypeTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeAutoScalingInstances.html#AutoScaling.Paginator.DescribeAutoScalingInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describeautoscalinginstancespaginator)
        """

if TYPE_CHECKING:
    _DescribeLaunchConfigurationsPaginatorBase = Paginator[LaunchConfigurationsTypeTypeDef]
else:
    _DescribeLaunchConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLaunchConfigurationsPaginator(_DescribeLaunchConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeLaunchConfigurations.html#AutoScaling.Paginator.DescribeLaunchConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describelaunchconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[LaunchConfigurationNamesTypePaginateTypeDef]
    ) -> PageIterator[LaunchConfigurationsTypeTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeLaunchConfigurations.html#AutoScaling.Paginator.DescribeLaunchConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describelaunchconfigurationspaginator)
        """

if TYPE_CHECKING:
    _DescribeLoadBalancerTargetGroupsPaginatorBase = Paginator[
        DescribeLoadBalancerTargetGroupsResponseTypeDef
    ]
else:
    _DescribeLoadBalancerTargetGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLoadBalancerTargetGroupsPaginator(_DescribeLoadBalancerTargetGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeLoadBalancerTargetGroups.html#AutoScaling.Paginator.DescribeLoadBalancerTargetGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describeloadbalancertargetgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLoadBalancerTargetGroupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeLoadBalancerTargetGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeLoadBalancerTargetGroups.html#AutoScaling.Paginator.DescribeLoadBalancerTargetGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describeloadbalancertargetgroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeLoadBalancersPaginatorBase = Paginator[DescribeLoadBalancersResponseTypeDef]
else:
    _DescribeLoadBalancersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLoadBalancersPaginator(_DescribeLoadBalancersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeLoadBalancers.html#AutoScaling.Paginator.DescribeLoadBalancers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describeloadbalancerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLoadBalancersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeLoadBalancersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeLoadBalancers.html#AutoScaling.Paginator.DescribeLoadBalancers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describeloadbalancerspaginator)
        """

if TYPE_CHECKING:
    _DescribeNotificationConfigurationsPaginatorBase = Paginator[
        DescribeNotificationConfigurationsAnswerTypeDef
    ]
else:
    _DescribeNotificationConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeNotificationConfigurationsPaginator(_DescribeNotificationConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeNotificationConfigurations.html#AutoScaling.Paginator.DescribeNotificationConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describenotificationconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNotificationConfigurationsTypePaginateTypeDef]
    ) -> PageIterator[DescribeNotificationConfigurationsAnswerTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeNotificationConfigurations.html#AutoScaling.Paginator.DescribeNotificationConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describenotificationconfigurationspaginator)
        """

if TYPE_CHECKING:
    _DescribePoliciesPaginatorBase = Paginator[PoliciesTypeTypeDef]
else:
    _DescribePoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribePoliciesPaginator(_DescribePoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribePolicies.html#AutoScaling.Paginator.DescribePolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describepoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribePoliciesTypePaginateTypeDef]
    ) -> PageIterator[PoliciesTypeTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribePolicies.html#AutoScaling.Paginator.DescribePolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describepoliciespaginator)
        """

if TYPE_CHECKING:
    _DescribeScalingActivitiesPaginatorBase = Paginator[ActivitiesTypeTypeDef]
else:
    _DescribeScalingActivitiesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeScalingActivitiesPaginator(_DescribeScalingActivitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeScalingActivities.html#AutoScaling.Paginator.DescribeScalingActivities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describescalingactivitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeScalingActivitiesTypePaginateTypeDef]
    ) -> PageIterator[ActivitiesTypeTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeScalingActivities.html#AutoScaling.Paginator.DescribeScalingActivities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describescalingactivitiespaginator)
        """

if TYPE_CHECKING:
    _DescribeScheduledActionsPaginatorBase = Paginator[ScheduledActionsTypeTypeDef]
else:
    _DescribeScheduledActionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeScheduledActionsPaginator(_DescribeScheduledActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeScheduledActions.html#AutoScaling.Paginator.DescribeScheduledActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describescheduledactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeScheduledActionsTypePaginateTypeDef]
    ) -> PageIterator[ScheduledActionsTypeTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeScheduledActions.html#AutoScaling.Paginator.DescribeScheduledActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describescheduledactionspaginator)
        """

if TYPE_CHECKING:
    _DescribeTagsPaginatorBase = Paginator[TagsTypeTypeDef]
else:
    _DescribeTagsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTagsPaginator(_DescribeTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeTags.html#AutoScaling.Paginator.DescribeTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describetagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTagsTypePaginateTypeDef]
    ) -> PageIterator[TagsTypeTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeTags.html#AutoScaling.Paginator.DescribeTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describetagspaginator)
        """

if TYPE_CHECKING:
    _DescribeWarmPoolPaginatorBase = Paginator[DescribeWarmPoolAnswerTypeDef]
else:
    _DescribeWarmPoolPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeWarmPoolPaginator(_DescribeWarmPoolPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeWarmPool.html#AutoScaling.Paginator.DescribeWarmPool)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describewarmpoolpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeWarmPoolTypePaginateTypeDef]
    ) -> PageIterator[DescribeWarmPoolAnswerTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/autoscaling/paginator/DescribeWarmPool.html#AutoScaling.Paginator.DescribeWarmPool.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/paginators/#describewarmpoolpaginator)
        """
