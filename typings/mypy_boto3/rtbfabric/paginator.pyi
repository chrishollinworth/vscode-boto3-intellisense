"""
Type annotations for rtbfabric service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_rtbfabric.client import RTBFabricClient
    from mypy_boto3_rtbfabric.paginator import (
        ListLinksPaginator,
        ListRequesterGatewaysPaginator,
        ListResponderGatewaysPaginator,
    )

    session = Session()
    client: RTBFabricClient = session.client("rtbfabric")

    list_links_paginator: ListLinksPaginator = client.get_paginator("list_links")
    list_requester_gateways_paginator: ListRequesterGatewaysPaginator = client.get_paginator("list_requester_gateways")
    list_responder_gateways_paginator: ListResponderGatewaysPaginator = client.get_paginator("list_responder_gateways")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListLinksRequestPaginateTypeDef,
    ListLinksResponseTypeDef,
    ListRequesterGatewaysRequestPaginateTypeDef,
    ListRequesterGatewaysResponseTypeDef,
    ListResponderGatewaysRequestPaginateTypeDef,
    ListResponderGatewaysResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListLinksPaginator", "ListRequesterGatewaysPaginator", "ListResponderGatewaysPaginator")

if TYPE_CHECKING:
    _ListLinksPaginatorBase = Paginator[ListLinksResponseTypeDef]
else:
    _ListLinksPaginatorBase = Paginator  # type: ignore[assignment]

class ListLinksPaginator(_ListLinksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/paginator/ListLinks.html#RTBFabric.Paginator.ListLinks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/paginators/#listlinkspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLinksRequestPaginateTypeDef]
    ) -> PageIterator[ListLinksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/paginator/ListLinks.html#RTBFabric.Paginator.ListLinks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/paginators/#listlinkspaginator)
        """

if TYPE_CHECKING:
    _ListRequesterGatewaysPaginatorBase = Paginator[ListRequesterGatewaysResponseTypeDef]
else:
    _ListRequesterGatewaysPaginatorBase = Paginator  # type: ignore[assignment]

class ListRequesterGatewaysPaginator(_ListRequesterGatewaysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/paginator/ListRequesterGateways.html#RTBFabric.Paginator.ListRequesterGateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/paginators/#listrequestergatewayspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRequesterGatewaysRequestPaginateTypeDef]
    ) -> PageIterator[ListRequesterGatewaysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/paginator/ListRequesterGateways.html#RTBFabric.Paginator.ListRequesterGateways.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/paginators/#listrequestergatewayspaginator)
        """

if TYPE_CHECKING:
    _ListResponderGatewaysPaginatorBase = Paginator[ListResponderGatewaysResponseTypeDef]
else:
    _ListResponderGatewaysPaginatorBase = Paginator  # type: ignore[assignment]

class ListResponderGatewaysPaginator(_ListResponderGatewaysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/paginator/ListResponderGateways.html#RTBFabric.Paginator.ListResponderGateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/paginators/#listrespondergatewayspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResponderGatewaysRequestPaginateTypeDef]
    ) -> PageIterator[ListResponderGatewaysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rtbfabric/paginator/ListResponderGateways.html#RTBFabric.Paginator.ListResponderGateways.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/paginators/#listrespondergatewayspaginator)
        """
