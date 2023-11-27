"""
Type annotations for autoscaling-plans service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/paginators.html)

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

from .type_defs import (
    ApplicationSourceTypeDef,
    DescribeScalingPlanResourcesResponseTypeDef,
    DescribeScalingPlansResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("DescribeScalingPlanResourcesPaginator", "DescribeScalingPlansPaginator")

class DescribeScalingPlanResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlanResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/paginators.html#describescalingplanresourcespaginator)
    """

    def paginate(
        self,
        *,
        ScalingPlanName: str,
        ScalingPlanVersion: int,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeScalingPlanResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlanResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/paginators.html#describescalingplanresourcespaginator)
        """

class DescribeScalingPlansPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlans)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/paginators.html#describescalingplanspaginator)
    """

    def paginate(
        self,
        *,
        ScalingPlanNames: List[str] = None,
        ScalingPlanVersion: int = None,
        ApplicationSources: List["ApplicationSourceTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeScalingPlansResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/autoscaling-plans.html#AutoScalingPlans.Paginator.DescribeScalingPlans.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/paginators.html#describescalingplanspaginator)
        """
