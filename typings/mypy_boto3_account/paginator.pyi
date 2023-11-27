"""
Type annotations for account service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_account import AccountClient
    from mypy_boto3_account.paginator import (
        ListRegionsPaginator,
    )

    client: AccountClient = boto3.client("account")

    list_regions_paginator: ListRegionsPaginator = client.get_paginator("list_regions")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import RegionOptStatusType
from .type_defs import ListRegionsResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListRegionsPaginator",)

class ListRegionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Paginator.ListRegions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/paginators.html#listregionspaginator)
    """

    def paginate(
        self,
        *,
        AccountId: str = None,
        RegionOptStatusContains: List[RegionOptStatusType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRegionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/account.html#Account.Paginator.ListRegions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/paginators.html#listregionspaginator)
        """
