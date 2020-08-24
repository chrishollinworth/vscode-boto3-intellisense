# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for elb service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_elb import ElasticLoadBalancingClient
    from mypy_boto3_elb.paginator import (
        DescribeAccountLimitsPaginator,
        DescribeLoadBalancersPaginator,
    )

    client: ElasticLoadBalancingClient = boto3.client("elb")

    describe_account_limits_paginator: DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
    describe_load_balancers_paginator: DescribeLoadBalancersPaginator = client.get_paginator("describe_load_balancers")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_elb.type_defs import (
    DescribeAccessPointsOutputTypeDef,
    DescribeAccountLimitsOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("DescribeAccountLimitsPaginator", "DescribeLoadBalancersPaginator")


class DescribeAccountLimitsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAccountLimits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeAccountLimits)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAccountLimitsOutputTypeDef]:
        """
        [DescribeAccountLimits.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeAccountLimits.paginate)
        """


class DescribeLoadBalancersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeLoadBalancers)
    """

    def paginate(
        self, LoadBalancerNames: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAccessPointsOutputTypeDef]:
        """
        [DescribeLoadBalancers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/elb.html#ElasticLoadBalancing.Paginator.DescribeLoadBalancers.paginate)
        """
