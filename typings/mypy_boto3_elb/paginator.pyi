"""
Type annotations for elb service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_elb.client import ElasticLoadBalancingClient
    from mypy_boto3_elb.paginator import (
        DescribeAccountLimitsPaginator,
        DescribeLoadBalancersPaginator,
    )

    session = Session()
    client: ElasticLoadBalancingClient = session.client("elb")

    describe_account_limits_paginator: DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
    describe_load_balancers_paginator: DescribeLoadBalancersPaginator = client.get_paginator("describe_load_balancers")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeAccessPointsInputPaginateTypeDef,
    DescribeAccessPointsOutputTypeDef,
    DescribeAccountLimitsInputPaginateTypeDef,
    DescribeAccountLimitsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("DescribeAccountLimitsPaginator", "DescribeLoadBalancersPaginator")

if TYPE_CHECKING:
    _DescribeAccountLimitsPaginatorBase = Paginator[DescribeAccountLimitsOutputTypeDef]
else:
    _DescribeAccountLimitsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAccountLimitsPaginator(_DescribeAccountLimitsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/paginator/DescribeAccountLimits.html#ElasticLoadBalancing.Paginator.DescribeAccountLimits)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/paginators/#describeaccountlimitspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAccountLimitsInputPaginateTypeDef]
    ) -> PageIterator[DescribeAccountLimitsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/paginator/DescribeAccountLimits.html#ElasticLoadBalancing.Paginator.DescribeAccountLimits.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/paginators/#describeaccountlimitspaginator)
        """

if TYPE_CHECKING:
    _DescribeLoadBalancersPaginatorBase = Paginator[DescribeAccessPointsOutputTypeDef]
else:
    _DescribeLoadBalancersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLoadBalancersPaginator(_DescribeLoadBalancersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/paginator/DescribeLoadBalancers.html#ElasticLoadBalancing.Paginator.DescribeLoadBalancers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/paginators/#describeloadbalancerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAccessPointsInputPaginateTypeDef]
    ) -> PageIterator[DescribeAccessPointsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/elb/paginator/DescribeLoadBalancers.html#ElasticLoadBalancing.Paginator.DescribeLoadBalancers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elb/paginators/#describeloadbalancerspaginator)
        """
