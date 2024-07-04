"""
Type annotations for freetier service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_freetier/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_freetier import FreeTierClient
    from mypy_boto3_freetier.paginator import (
        GetFreeTierUsagePaginator,
    )

    client: FreeTierClient = boto3.client("freetier")

    get_free_tier_usage_paginator: GetFreeTierUsagePaginator = client.get_paginator("get_free_tier_usage")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ExpressionTypeDef, GetFreeTierUsageResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("GetFreeTierUsagePaginator",)

class GetFreeTierUsagePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/freetier.html#FreeTier.Paginator.GetFreeTierUsage)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_freetier/paginators.html#getfreetierusagepaginator)
    """

    def paginate(
        self, *, filter: "ExpressionTypeDef" = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetFreeTierUsageResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/freetier.html#FreeTier.Paginator.GetFreeTierUsage.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_freetier/paginators.html#getfreetierusagepaginator)
        """
