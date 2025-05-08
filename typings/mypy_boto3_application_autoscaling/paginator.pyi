"""
Type annotations for application-autoscaling service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_application_autoscaling.client import ApplicationAutoScalingClient
    from mypy_boto3_application_autoscaling.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeScalableTargetsRequestPaginateTypeDef,
    DescribeScalableTargetsResponseTypeDef,
    DescribeScalingActivitiesRequestPaginateTypeDef,
    DescribeScalingActivitiesResponseTypeDef,
    DescribeScalingPoliciesRequestPaginateTypeDef,
    DescribeScalingPoliciesResponseTypeDef,
    DescribeScheduledActionsRequestPaginateTypeDef,
    DescribeScheduledActionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeScalableTargetsPaginator",
    "DescribeScalingActivitiesPaginator",
    "DescribeScalingPoliciesPaginator",
    "DescribeScheduledActionsPaginator",
)

if TYPE_CHECKING:
    _DescribeScalableTargetsPaginatorBase = Paginator[DescribeScalableTargetsResponseTypeDef]
else:
    _DescribeScalableTargetsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeScalableTargetsPaginator(_DescribeScalableTargetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/paginator/DescribeScalableTargets.html#ApplicationAutoScaling.Paginator.DescribeScalableTargets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators/#describescalabletargetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeScalableTargetsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeScalableTargetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/paginator/DescribeScalableTargets.html#ApplicationAutoScaling.Paginator.DescribeScalableTargets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators/#describescalabletargetspaginator)
        """

if TYPE_CHECKING:
    _DescribeScalingActivitiesPaginatorBase = Paginator[DescribeScalingActivitiesResponseTypeDef]
else:
    _DescribeScalingActivitiesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeScalingActivitiesPaginator(_DescribeScalingActivitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/paginator/DescribeScalingActivities.html#ApplicationAutoScaling.Paginator.DescribeScalingActivities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators/#describescalingactivitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeScalingActivitiesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeScalingActivitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/paginator/DescribeScalingActivities.html#ApplicationAutoScaling.Paginator.DescribeScalingActivities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators/#describescalingactivitiespaginator)
        """

if TYPE_CHECKING:
    _DescribeScalingPoliciesPaginatorBase = Paginator[DescribeScalingPoliciesResponseTypeDef]
else:
    _DescribeScalingPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeScalingPoliciesPaginator(_DescribeScalingPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/paginator/DescribeScalingPolicies.html#ApplicationAutoScaling.Paginator.DescribeScalingPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators/#describescalingpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeScalingPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeScalingPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/paginator/DescribeScalingPolicies.html#ApplicationAutoScaling.Paginator.DescribeScalingPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators/#describescalingpoliciespaginator)
        """

if TYPE_CHECKING:
    _DescribeScheduledActionsPaginatorBase = Paginator[DescribeScheduledActionsResponseTypeDef]
else:
    _DescribeScheduledActionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeScheduledActionsPaginator(_DescribeScheduledActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/paginator/DescribeScheduledActions.html#ApplicationAutoScaling.Paginator.DescribeScheduledActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators/#describescheduledactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeScheduledActionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeScheduledActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-autoscaling/paginator/DescribeScheduledActions.html#ApplicationAutoScaling.Paginator.DescribeScheduledActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/paginators/#describescheduledactionspaginator)
        """
