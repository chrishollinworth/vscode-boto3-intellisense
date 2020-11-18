# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for autoscaling-plans service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_autoscaling_plans import AutoScalingPlansClient
    from mypy_boto3_autoscaling_plans.paginator import (
        DescribeScalingPlanResourcesPaginator,
        DescribeScalingPlansPaginator,
    )

    client: AutoScalingPlansClient = boto3.client("autoscaling-plans")

    describe_scaling_plan_resources_paginator: DescribeScalingPlanResourcesPaginator = client.get_paginator("describe_scaling_plan_resources")
    describe_scaling_plans_paginator: DescribeScalingPlansPaginator = client.get_paginator("describe_scaling_plans")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_autoscaling_plans.type_defs import (
    ApplicationSourceTypeDef,
    DescribeScalingPlanResourcesResponseTypeDef,
    DescribeScalingPlansResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("DescribeScalingPlanResourcesPaginator", "DescribeScalingPlansPaginator")


class DescribeScalingPlanResourcesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScalingPlanResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlanResources)
    """

    def paginate(
        self,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeScalingPlanResourcesResponseTypeDef]:
        """
        [DescribeScalingPlanResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlanResources.paginate)
        """


class DescribeScalingPlansPaginator(Boto3Paginator):
    """
    [Paginator.DescribeScalingPlans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlans)
    """

    def paginate(
        self,
        ScalingPlanNames: List[str] = None,
        ScalingPlanVersion: int = None,
        ApplicationSources: List["ApplicationSourceTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeScalingPlansResponseTypeDef]:
        """
        [DescribeScalingPlans.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlans.paginate)
        """
