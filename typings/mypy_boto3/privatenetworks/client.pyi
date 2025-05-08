"""
Type annotations for privatenetworks service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_privatenetworks.client import Private5GClient

    session = Session()
    client: Private5GClient = session.client("privatenetworks")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListDeviceIdentifiersPaginator,
    ListNetworkResourcesPaginator,
    ListNetworkSitesPaginator,
    ListNetworksPaginator,
    ListOrdersPaginator,
)
from .type_defs import (
    AcknowledgeOrderReceiptRequestTypeDef,
    AcknowledgeOrderReceiptResponseTypeDef,
    ActivateDeviceIdentifierRequestTypeDef,
    ActivateDeviceIdentifierResponseTypeDef,
    ActivateNetworkSiteRequestTypeDef,
    ActivateNetworkSiteResponseTypeDef,
    ConfigureAccessPointRequestTypeDef,
    ConfigureAccessPointResponseTypeDef,
    CreateNetworkRequestTypeDef,
    CreateNetworkResponseTypeDef,
    CreateNetworkSiteRequestTypeDef,
    CreateNetworkSiteResponseTypeDef,
    DeactivateDeviceIdentifierRequestTypeDef,
    DeactivateDeviceIdentifierResponseTypeDef,
    DeleteNetworkRequestTypeDef,
    DeleteNetworkResponseTypeDef,
    DeleteNetworkSiteRequestTypeDef,
    DeleteNetworkSiteResponseTypeDef,
    GetDeviceIdentifierRequestTypeDef,
    GetDeviceIdentifierResponseTypeDef,
    GetNetworkRequestTypeDef,
    GetNetworkResourceRequestTypeDef,
    GetNetworkResourceResponseTypeDef,
    GetNetworkResponseTypeDef,
    GetNetworkSiteRequestTypeDef,
    GetNetworkSiteResponseTypeDef,
    GetOrderRequestTypeDef,
    GetOrderResponseTypeDef,
    ListDeviceIdentifiersRequestTypeDef,
    ListDeviceIdentifiersResponseTypeDef,
    ListNetworkResourcesRequestTypeDef,
    ListNetworkResourcesResponseTypeDef,
    ListNetworkSitesRequestTypeDef,
    ListNetworkSitesResponseTypeDef,
    ListNetworksRequestTypeDef,
    ListNetworksResponseTypeDef,
    ListOrdersRequestTypeDef,
    ListOrdersResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PingResponseTypeDef,
    StartNetworkResourceUpdateRequestTypeDef,
    StartNetworkResourceUpdateResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateNetworkSitePlanRequestTypeDef,
    UpdateNetworkSiteRequestTypeDef,
    UpdateNetworkSiteResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("Private5GClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class Private5GClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks.html#Private5G.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Private5GClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks.html#Private5G.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#generate_presigned_url)
        """

    def acknowledge_order_receipt(
        self, **kwargs: Unpack[AcknowledgeOrderReceiptRequestTypeDef]
    ) -> AcknowledgeOrderReceiptResponseTypeDef:
        """
        Acknowledges that the specified network order was received.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/acknowledge_order_receipt.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#acknowledge_order_receipt)
        """

    def activate_device_identifier(
        self, **kwargs: Unpack[ActivateDeviceIdentifierRequestTypeDef]
    ) -> ActivateDeviceIdentifierResponseTypeDef:
        """
        Activates the specified device identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/activate_device_identifier.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#activate_device_identifier)
        """

    def activate_network_site(
        self, **kwargs: Unpack[ActivateNetworkSiteRequestTypeDef]
    ) -> ActivateNetworkSiteResponseTypeDef:
        """
        Activates the specified network site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/activate_network_site.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#activate_network_site)
        """

    def configure_access_point(
        self, **kwargs: Unpack[ConfigureAccessPointRequestTypeDef]
    ) -> ConfigureAccessPointResponseTypeDef:
        """
        Configures the specified network resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/configure_access_point.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#configure_access_point)
        """

    def create_network(
        self, **kwargs: Unpack[CreateNetworkRequestTypeDef]
    ) -> CreateNetworkResponseTypeDef:
        """
        Creates a network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/create_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#create_network)
        """

    def create_network_site(
        self, **kwargs: Unpack[CreateNetworkSiteRequestTypeDef]
    ) -> CreateNetworkSiteResponseTypeDef:
        """
        Creates a network site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/create_network_site.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#create_network_site)
        """

    def deactivate_device_identifier(
        self, **kwargs: Unpack[DeactivateDeviceIdentifierRequestTypeDef]
    ) -> DeactivateDeviceIdentifierResponseTypeDef:
        """
        Deactivates the specified device identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/deactivate_device_identifier.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#deactivate_device_identifier)
        """

    def delete_network(
        self, **kwargs: Unpack[DeleteNetworkRequestTypeDef]
    ) -> DeleteNetworkResponseTypeDef:
        """
        Deletes the specified network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/delete_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#delete_network)
        """

    def delete_network_site(
        self, **kwargs: Unpack[DeleteNetworkSiteRequestTypeDef]
    ) -> DeleteNetworkSiteResponseTypeDef:
        """
        Deletes the specified network site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/delete_network_site.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#delete_network_site)
        """

    def get_device_identifier(
        self, **kwargs: Unpack[GetDeviceIdentifierRequestTypeDef]
    ) -> GetDeviceIdentifierResponseTypeDef:
        """
        Gets the specified device identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/get_device_identifier.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#get_device_identifier)
        """

    def get_network(self, **kwargs: Unpack[GetNetworkRequestTypeDef]) -> GetNetworkResponseTypeDef:
        """
        Gets the specified network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/get_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#get_network)
        """

    def get_network_resource(
        self, **kwargs: Unpack[GetNetworkResourceRequestTypeDef]
    ) -> GetNetworkResourceResponseTypeDef:
        """
        Gets the specified network resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/get_network_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#get_network_resource)
        """

    def get_network_site(
        self, **kwargs: Unpack[GetNetworkSiteRequestTypeDef]
    ) -> GetNetworkSiteResponseTypeDef:
        """
        Gets the specified network site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/get_network_site.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#get_network_site)
        """

    def get_order(self, **kwargs: Unpack[GetOrderRequestTypeDef]) -> GetOrderResponseTypeDef:
        """
        Gets the specified order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/get_order.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#get_order)
        """

    def list_device_identifiers(
        self, **kwargs: Unpack[ListDeviceIdentifiersRequestTypeDef]
    ) -> ListDeviceIdentifiersResponseTypeDef:
        """
        Lists device identifiers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/list_device_identifiers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#list_device_identifiers)
        """

    def list_network_resources(
        self, **kwargs: Unpack[ListNetworkResourcesRequestTypeDef]
    ) -> ListNetworkResourcesResponseTypeDef:
        """
        Lists network resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/list_network_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#list_network_resources)
        """

    def list_network_sites(
        self, **kwargs: Unpack[ListNetworkSitesRequestTypeDef]
    ) -> ListNetworkSitesResponseTypeDef:
        """
        Lists network sites.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/list_network_sites.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#list_network_sites)
        """

    def list_networks(
        self, **kwargs: Unpack[ListNetworksRequestTypeDef]
    ) -> ListNetworksResponseTypeDef:
        """
        Lists networks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/list_networks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#list_networks)
        """

    def list_orders(self, **kwargs: Unpack[ListOrdersRequestTypeDef]) -> ListOrdersResponseTypeDef:
        """
        Lists orders.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/list_orders.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#list_orders)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#list_tags_for_resource)
        """

    def ping(self) -> PingResponseTypeDef:
        """
        Checks the health of the service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/ping.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#ping)
        """

    def start_network_resource_update(
        self, **kwargs: Unpack[StartNetworkResourceUpdateRequestTypeDef]
    ) -> StartNetworkResourceUpdateResponseTypeDef:
        """
        Use this action to do the following tasks:.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/start_network_resource_update.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#start_network_resource_update)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#untag_resource)
        """

    def update_network_site(
        self, **kwargs: Unpack[UpdateNetworkSiteRequestTypeDef]
    ) -> UpdateNetworkSiteResponseTypeDef:
        """
        Updates the specified network site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/update_network_site.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#update_network_site)
        """

    def update_network_site_plan(
        self, **kwargs: Unpack[UpdateNetworkSitePlanRequestTypeDef]
    ) -> UpdateNetworkSiteResponseTypeDef:
        """
        Updates the specified network site plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/update_network_site_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#update_network_site_plan)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_device_identifiers"]
    ) -> ListDeviceIdentifiersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_network_resources"]
    ) -> ListNetworkResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_network_sites"]
    ) -> ListNetworkSitesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_networks"]
    ) -> ListNetworksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_orders"]
    ) -> ListOrdersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/privatenetworks/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client/#get_paginator)
        """
