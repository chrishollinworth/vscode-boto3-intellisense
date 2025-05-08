"""
Type annotations for privatenetworks service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_privatenetworks.client import Private5GClient
    from mypy_boto3_privatenetworks.paginator import (
        ListDeviceIdentifiersPaginator,
        ListNetworkResourcesPaginator,
        ListNetworkSitesPaginator,
        ListNetworksPaginator,
        ListOrdersPaginator,
    )

    session = Session()
    client: Private5GClient = session.client("privatenetworks")

    list_device_identifiers_paginator: ListDeviceIdentifiersPaginator = client.get_paginator("list_device_identifiers")
    list_network_resources_paginator: ListNetworkResourcesPaginator = client.get_paginator("list_network_resources")
    list_network_sites_paginator: ListNetworkSitesPaginator = client.get_paginator("list_network_sites")
    list_networks_paginator: ListNetworksPaginator = client.get_paginator("list_networks")
    list_orders_paginator: ListOrdersPaginator = client.get_paginator("list_orders")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDeviceIdentifiersRequestPaginateTypeDef,
    ListDeviceIdentifiersResponseTypeDef,
    ListNetworkResourcesRequestPaginateTypeDef,
    ListNetworkResourcesResponseTypeDef,
    ListNetworkSitesRequestPaginateTypeDef,
    ListNetworkSitesResponseTypeDef,
    ListNetworksRequestPaginateTypeDef,
    ListNetworksResponseTypeDef,
    ListOrdersRequestPaginateTypeDef,
    ListOrdersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListDeviceIdentifiersPaginator",
    "ListNetworkResourcesPaginator",
    "ListNetworkSitesPaginator",
    "ListNetworksPaginator",
    "ListOrdersPaginator",
)

if TYPE_CHECKING:
    _ListDeviceIdentifiersPaginatorBase = Paginator[ListDeviceIdentifiersResponseTypeDef]
else:
    _ListDeviceIdentifiersPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeviceIdentifiersPaginator(_ListDeviceIdentifiersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/paginator/ListDeviceIdentifiers.html#Private5G.Paginator.ListDeviceIdentifiers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators/#listdeviceidentifierspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeviceIdentifiersRequestPaginateTypeDef]
    ) -> PageIterator[ListDeviceIdentifiersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/paginator/ListDeviceIdentifiers.html#Private5G.Paginator.ListDeviceIdentifiers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators/#listdeviceidentifierspaginator)
        """

if TYPE_CHECKING:
    _ListNetworkResourcesPaginatorBase = Paginator[ListNetworkResourcesResponseTypeDef]
else:
    _ListNetworkResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListNetworkResourcesPaginator(_ListNetworkResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/paginator/ListNetworkResources.html#Private5G.Paginator.ListNetworkResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators/#listnetworkresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNetworkResourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListNetworkResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/paginator/ListNetworkResources.html#Private5G.Paginator.ListNetworkResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators/#listnetworkresourcespaginator)
        """

if TYPE_CHECKING:
    _ListNetworkSitesPaginatorBase = Paginator[ListNetworkSitesResponseTypeDef]
else:
    _ListNetworkSitesPaginatorBase = Paginator  # type: ignore[assignment]

class ListNetworkSitesPaginator(_ListNetworkSitesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/paginator/ListNetworkSites.html#Private5G.Paginator.ListNetworkSites)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators/#listnetworksitespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNetworkSitesRequestPaginateTypeDef]
    ) -> PageIterator[ListNetworkSitesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/paginator/ListNetworkSites.html#Private5G.Paginator.ListNetworkSites.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators/#listnetworksitespaginator)
        """

if TYPE_CHECKING:
    _ListNetworksPaginatorBase = Paginator[ListNetworksResponseTypeDef]
else:
    _ListNetworksPaginatorBase = Paginator  # type: ignore[assignment]

class ListNetworksPaginator(_ListNetworksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/paginator/ListNetworks.html#Private5G.Paginator.ListNetworks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators/#listnetworkspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNetworksRequestPaginateTypeDef]
    ) -> PageIterator[ListNetworksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/paginator/ListNetworks.html#Private5G.Paginator.ListNetworks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators/#listnetworkspaginator)
        """

if TYPE_CHECKING:
    _ListOrdersPaginatorBase = Paginator[ListOrdersResponseTypeDef]
else:
    _ListOrdersPaginatorBase = Paginator  # type: ignore[assignment]

class ListOrdersPaginator(_ListOrdersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/paginator/ListOrders.html#Private5G.Paginator.ListOrders)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators/#listorderspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOrdersRequestPaginateTypeDef]
    ) -> PageIterator[ListOrdersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/paginator/ListOrders.html#Private5G.Paginator.ListOrders.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators/#listorderspaginator)
        """
