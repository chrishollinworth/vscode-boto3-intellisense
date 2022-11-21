"""
Type annotations for privatenetworks service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_privatenetworks import Private5GClient

    client: Private5GClient = boto3.client("privatenetworks")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    DeviceIdentifierFilterKeysType,
    NetworkResourceFilterKeysType,
    OrderFilterKeysType,
)
from .paginator import (
    ListDeviceIdentifiersPaginator,
    ListNetworkResourcesPaginator,
    ListNetworkSitesPaginator,
    ListNetworksPaginator,
    ListOrdersPaginator,
)
from .type_defs import (
    AcknowledgeOrderReceiptResponseTypeDef,
    ActivateDeviceIdentifierResponseTypeDef,
    ActivateNetworkSiteResponseTypeDef,
    AddressTypeDef,
    ConfigureAccessPointResponseTypeDef,
    CreateNetworkResponseTypeDef,
    CreateNetworkSiteResponseTypeDef,
    DeactivateDeviceIdentifierResponseTypeDef,
    DeleteNetworkResponseTypeDef,
    DeleteNetworkSiteResponseTypeDef,
    GetDeviceIdentifierResponseTypeDef,
    GetNetworkResourceResponseTypeDef,
    GetNetworkResponseTypeDef,
    GetNetworkSiteResponseTypeDef,
    GetOrderResponseTypeDef,
    ListDeviceIdentifiersResponseTypeDef,
    ListNetworkResourcesResponseTypeDef,
    ListNetworkSitesResponseTypeDef,
    ListNetworksResponseTypeDef,
    ListOrdersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PingResponseTypeDef,
    PositionTypeDef,
    SitePlanTypeDef,
    UpdateNetworkSiteResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("Private5GClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class Private5GClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Private5GClient exceptions.
        """
    def acknowledge_order_receipt(self, *, orderArn: str) -> AcknowledgeOrderReceiptResponseTypeDef:
        """
        Acknowledges that the specified network order was received.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.acknowledge_order_receipt)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#acknowledge_order_receipt)
        """
    def activate_device_identifier(
        self, *, deviceIdentifierArn: str, clientToken: str = None
    ) -> ActivateDeviceIdentifierResponseTypeDef:
        """
        Activates the specified device identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.activate_device_identifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#activate_device_identifier)
        """
    def activate_network_site(
        self, *, networkSiteArn: str, shippingAddress: "AddressTypeDef", clientToken: str = None
    ) -> ActivateNetworkSiteResponseTypeDef:
        """
        Activates the specified network site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.activate_network_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#activate_network_site)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#close)
        """
    def configure_access_point(
        self,
        *,
        accessPointArn: str,
        cpiSecretKey: str = None,
        cpiUserId: str = None,
        cpiUserPassword: str = None,
        cpiUsername: str = None,
        position: "PositionTypeDef" = None
    ) -> ConfigureAccessPointResponseTypeDef:
        """
        Configures the specified network resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.configure_access_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#configure_access_point)
        """
    def create_network(
        self,
        *,
        networkName: str,
        clientToken: str = None,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateNetworkResponseTypeDef:
        """
        Creates a network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.create_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#create_network)
        """
    def create_network_site(
        self,
        *,
        networkArn: str,
        networkSiteName: str,
        availabilityZone: str = None,
        availabilityZoneId: str = None,
        clientToken: str = None,
        description: str = None,
        pendingPlan: "SitePlanTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateNetworkSiteResponseTypeDef:
        """
        Creates a network site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.create_network_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#create_network_site)
        """
    def deactivate_device_identifier(
        self, *, deviceIdentifierArn: str, clientToken: str = None
    ) -> DeactivateDeviceIdentifierResponseTypeDef:
        """
        Deactivates the specified device identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.deactivate_device_identifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#deactivate_device_identifier)
        """
    def delete_network(
        self, *, networkArn: str, clientToken: str = None
    ) -> DeleteNetworkResponseTypeDef:
        """
        Deletes the specified network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.delete_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#delete_network)
        """
    def delete_network_site(
        self, *, networkSiteArn: str, clientToken: str = None
    ) -> DeleteNetworkSiteResponseTypeDef:
        """
        Deletes the specified network site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.delete_network_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#delete_network_site)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#generate_presigned_url)
        """
    def get_device_identifier(
        self, *, deviceIdentifierArn: str
    ) -> GetDeviceIdentifierResponseTypeDef:
        """
        Gets the specified device identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.get_device_identifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#get_device_identifier)
        """
    def get_network(self, *, networkArn: str) -> GetNetworkResponseTypeDef:
        """
        Gets the specified network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.get_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#get_network)
        """
    def get_network_resource(self, *, networkResourceArn: str) -> GetNetworkResourceResponseTypeDef:
        """
        Gets the specified network resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.get_network_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#get_network_resource)
        """
    def get_network_site(self, *, networkSiteArn: str) -> GetNetworkSiteResponseTypeDef:
        """
        Gets the specified network site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.get_network_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#get_network_site)
        """
    def get_order(self, *, orderArn: str) -> GetOrderResponseTypeDef:
        """
        Gets the specified order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.get_order)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#get_order)
        """
    def list_device_identifiers(
        self,
        *,
        networkArn: str,
        filters: Dict[DeviceIdentifierFilterKeysType, List[str]] = None,
        maxResults: int = None,
        startToken: str = None
    ) -> ListDeviceIdentifiersResponseTypeDef:
        """
        Lists device identifiers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.list_device_identifiers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#list_device_identifiers)
        """
    def list_network_resources(
        self,
        *,
        networkArn: str,
        filters: Dict[NetworkResourceFilterKeysType, List[str]] = None,
        maxResults: int = None,
        startToken: str = None
    ) -> ListNetworkResourcesResponseTypeDef:
        """
        Lists network resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.list_network_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#list_network_resources)
        """
    def list_network_sites(
        self,
        *,
        networkArn: str,
        filters: Dict[Literal["STATUS"], List[str]] = None,
        maxResults: int = None,
        startToken: str = None
    ) -> ListNetworkSitesResponseTypeDef:
        """
        Lists network sites.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.list_network_sites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#list_network_sites)
        """
    def list_networks(
        self,
        *,
        filters: Dict[Literal["STATUS"], List[str]] = None,
        maxResults: int = None,
        startToken: str = None
    ) -> ListNetworksResponseTypeDef:
        """
        Lists networks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.list_networks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#list_networks)
        """
    def list_orders(
        self,
        *,
        networkArn: str,
        filters: Dict[OrderFilterKeysType, List[str]] = None,
        maxResults: int = None,
        startToken: str = None
    ) -> ListOrdersResponseTypeDef:
        """
        Lists orders.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.list_orders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#list_orders)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#list_tags_for_resource)
        """
    def ping(self) -> PingResponseTypeDef:
        """
        Checks the health of the service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.ping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#ping)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#untag_resource)
        """
    def update_network_site(
        self, *, networkSiteArn: str, clientToken: str = None, description: str = None
    ) -> UpdateNetworkSiteResponseTypeDef:
        """
        Updates the specified network site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.update_network_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#update_network_site)
        """
    def update_network_site_plan(
        self, *, networkSiteArn: str, pendingPlan: "SitePlanTypeDef", clientToken: str = None
    ) -> UpdateNetworkSiteResponseTypeDef:
        """
        Updates the specified network site plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Client.update_network_site_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/client.html#update_network_site_plan)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_identifiers"]
    ) -> ListDeviceIdentifiersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Paginator.ListDeviceIdentifiers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html#listdeviceidentifierspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_network_resources"]
    ) -> ListNetworkResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Paginator.ListNetworkResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html#listnetworkresourcespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_network_sites"]
    ) -> ListNetworkSitesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Paginator.ListNetworkSites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html#listnetworksitespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_networks"]) -> ListNetworksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Paginator.ListNetworks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html#listnetworkspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_orders"]) -> ListOrdersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/privatenetworks.html#Private5G.Paginator.ListOrders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/paginators.html#listorderspaginator)
        """
