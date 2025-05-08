"""
Type annotations for account service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_account.client import AccountClient
    from mypy_boto3_account.paginator import (
        ListRegionsPaginator,
    )

    session = Session()
    client: AccountClient = session.client("account")

    list_regions_paginator: ListRegionsPaginator = client.get_paginator("list_regions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListRegionsRequestPaginateTypeDef, ListRegionsResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListRegionsPaginator",)

if TYPE_CHECKING:
    _ListRegionsPaginatorBase = Paginator[ListRegionsResponseTypeDef]
else:
    _ListRegionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRegionsPaginator(_ListRegionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account/paginator/ListRegions.html#Account.Paginator.ListRegions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/paginators/#listregionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRegionsRequestPaginateTypeDef]
    ) -> PageIterator[ListRegionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/account/paginator/ListRegions.html#Account.Paginator.ListRegions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/paginators/#listregionspaginator)
        """
