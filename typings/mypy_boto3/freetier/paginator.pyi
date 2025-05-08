"""
Type annotations for freetier service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_freetier.client import FreeTierClient
    from mypy_boto3_freetier.paginator import (
        GetFreeTierUsagePaginator,
    )

    session = Session()
    client: FreeTierClient = session.client("freetier")

    get_free_tier_usage_paginator: GetFreeTierUsagePaginator = client.get_paginator("get_free_tier_usage")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import GetFreeTierUsageRequestPaginateTypeDef, GetFreeTierUsageResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("GetFreeTierUsagePaginator",)

if TYPE_CHECKING:
    _GetFreeTierUsagePaginatorBase = Paginator[GetFreeTierUsageResponseTypeDef]
else:
    _GetFreeTierUsagePaginatorBase = Paginator  # type: ignore[assignment]

class GetFreeTierUsagePaginator(_GetFreeTierUsagePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier/paginator/GetFreeTierUsage.html#FreeTier.Paginator.GetFreeTierUsage)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/paginators/#getfreetierusagepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetFreeTierUsageRequestPaginateTypeDef]
    ) -> PageIterator[GetFreeTierUsageResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier/paginator/GetFreeTierUsage.html#FreeTier.Paginator.GetFreeTierUsage.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/paginators/#getfreetierusagepaginator)
        """
