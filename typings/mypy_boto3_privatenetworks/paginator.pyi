"""
Type annotations for privatenetworks service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_privatenetworks import Private5GClient
    from mypy_boto3_privatenetworks.paginator import (
        ListDeviceIdentifiersPaginator,
        ListNetworkResourcesPaginator,
        ListNetworkSitesPaginator,
        ListNetworksPaginator,
        ListOrdersPaginator,
    )

    client: Private5GClient = boto3.client("privatenetworks")

    list_device_identifiers_paginator: ListDeviceIdentifiersPaginator = client.get_paginator("list_device_identifiers")
    list_network_resources_paginator: ListNetworkResourcesPaginator = client.get_paginator("list_network_resources")
    list_network_sites_paginator: ListNetworkSitesPaginator = client.get_paginator("list_network_sites")
    list_networks_paginator: ListNetworksPaginator = client.get_paginator("list_networks")
    list_orders_paginator: ListOrdersPaginator = client.get_paginator("list_orders")
    ```
"""
import sys
from typing import Dict, Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    DeviceIdentifierFilterKeysType,
    NetworkResourceFilterKeysType,
    OrderFilterKeysType,
)
from .type_defs import (
    ListDeviceIdentifiersResponseTypeDef,
    ListNetworkResourcesResponseTypeDef,
    ListNetworkSitesResponseTypeDef,
    ListNetworksResponseTypeDef,
    ListOrdersResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListDeviceIdentifiersPaginator",
    "ListNetworkResourcesPaginator",
    "ListNetworkSitesPaginator",
    "ListNetworksPaginator",
    "ListOrdersPaginator",
)

class ListDeviceIdentifiersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/privatenetworks.html#Private5G.Paginator.ListDeviceIdentifiers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html#listdeviceidentifierspaginator)
    """

    def paginate(
        self,
        *,
        networkArn: str,
        filters: Dict[DeviceIdentifierFilterKeysType, List[str]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeviceIdentifiersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/privatenetworks.html#Private5G.Paginator.ListDeviceIdentifiers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html#listdeviceidentifierspaginator)
        """

class ListNetworkResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/privatenetworks.html#Private5G.Paginator.ListNetworkResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html#listnetworkresourcespaginator)
    """

    def paginate(
        self,
        *,
        networkArn: str,
        filters: Dict[NetworkResourceFilterKeysType, List[str]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNetworkResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/privatenetworks.html#Private5G.Paginator.ListNetworkResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html#listnetworkresourcespaginator)
        """

class ListNetworkSitesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/privatenetworks.html#Private5G.Paginator.ListNetworkSites)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html#listnetworksitespaginator)
    """

    def paginate(
        self,
        *,
        networkArn: str,
        filters: Dict[Literal["STATUS"], List[str]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNetworkSitesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/privatenetworks.html#Private5G.Paginator.ListNetworkSites.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html#listnetworksitespaginator)
        """

class ListNetworksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/privatenetworks.html#Private5G.Paginator.ListNetworks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html#listnetworkspaginator)
    """

    def paginate(
        self,
        *,
        filters: Dict[Literal["STATUS"], List[str]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNetworksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/privatenetworks.html#Private5G.Paginator.ListNetworks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html#listnetworkspaginator)
        """

class ListOrdersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/privatenetworks.html#Private5G.Paginator.ListOrders)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html#listorderspaginator)
    """

    def paginate(
        self,
        *,
        networkArn: str,
        filters: Dict[OrderFilterKeysType, List[str]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOrdersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/privatenetworks.html#Private5G.Paginator.ListOrders.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html#listorderspaginator)
        """
