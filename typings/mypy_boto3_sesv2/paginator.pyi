"""
Type annotations for sesv2 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_sesv2.client import SESV2Client
    from mypy_boto3_sesv2.paginator import (
        ListMultiRegionEndpointsPaginator,
    )

    session = Session()
    client: SESV2Client = session.client("sesv2")

    list_multi_region_endpoints_paginator: ListMultiRegionEndpointsPaginator = client.get_paginator("list_multi_region_endpoints")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListMultiRegionEndpointsRequestPaginateTypeDef,
    ListMultiRegionEndpointsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListMultiRegionEndpointsPaginator",)

if TYPE_CHECKING:
    _ListMultiRegionEndpointsPaginatorBase = Paginator[ListMultiRegionEndpointsResponseTypeDef]
else:
    _ListMultiRegionEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMultiRegionEndpointsPaginator(_ListMultiRegionEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2/paginator/ListMultiRegionEndpoints.html#SESV2.Paginator.ListMultiRegionEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/paginators/#listmultiregionendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMultiRegionEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[ListMultiRegionEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sesv2/paginator/ListMultiRegionEndpoints.html#SESV2.Paginator.ListMultiRegionEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sesv2/paginators/#listmultiregionendpointspaginator)
        """
