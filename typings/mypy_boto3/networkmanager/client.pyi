"""
Type annotations for networkmanager service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_networkmanager import NetworkManagerClient

    client: NetworkManagerClient = boto3.client("networkmanager")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    DescribeGlobalNetworksPaginator,
    GetConnectionsPaginator,
    GetCustomerGatewayAssociationsPaginator,
    GetDevicesPaginator,
    GetLinkAssociationsPaginator,
    GetLinksPaginator,
    GetSitesPaginator,
    GetTransitGatewayConnectPeerAssociationsPaginator,
    GetTransitGatewayRegistrationsPaginator,
)
from .type_defs import (
    AssociateCustomerGatewayResponseTypeDef,
    AssociateLinkResponseTypeDef,
    AssociateTransitGatewayConnectPeerResponseTypeDef,
    AWSLocationTypeDef,
    BandwidthTypeDef,
    CreateConnectionResponseTypeDef,
    CreateDeviceResponseTypeDef,
    CreateGlobalNetworkResponseTypeDef,
    CreateLinkResponseTypeDef,
    CreateSiteResponseTypeDef,
    DeleteConnectionResponseTypeDef,
    DeleteDeviceResponseTypeDef,
    DeleteGlobalNetworkResponseTypeDef,
    DeleteLinkResponseTypeDef,
    DeleteSiteResponseTypeDef,
    DeregisterTransitGatewayResponseTypeDef,
    DescribeGlobalNetworksResponseTypeDef,
    DisassociateCustomerGatewayResponseTypeDef,
    DisassociateLinkResponseTypeDef,
    DisassociateTransitGatewayConnectPeerResponseTypeDef,
    GetConnectionsResponseTypeDef,
    GetCustomerGatewayAssociationsResponseTypeDef,
    GetDevicesResponseTypeDef,
    GetLinkAssociationsResponseTypeDef,
    GetLinksResponseTypeDef,
    GetSitesResponseTypeDef,
    GetTransitGatewayConnectPeerAssociationsResponseTypeDef,
    GetTransitGatewayRegistrationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LocationTypeDef,
    RegisterTransitGatewayResponseTypeDef,
    TagTypeDef,
    UpdateConnectionResponseTypeDef,
    UpdateDeviceResponseTypeDef,
    UpdateGlobalNetworkResponseTypeDef,
    UpdateLinkResponseTypeDef,
    UpdateSiteResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("NetworkManagerClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class NetworkManagerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        NetworkManagerClient exceptions.
        """
    def associate_customer_gateway(
        self, *, CustomerGatewayArn: str, GlobalNetworkId: str, DeviceId: str, LinkId: str = None
    ) -> AssociateCustomerGatewayResponseTypeDef:
        """
        Associates a customer gateway with a device and optionally, with a link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.associate_customer_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#associate_customer_gateway)
        """
    def associate_link(
        self, *, GlobalNetworkId: str, DeviceId: str, LinkId: str
    ) -> AssociateLinkResponseTypeDef:
        """
        Associates a link to a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.associate_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#associate_link)
        """
    def associate_transit_gateway_connect_peer(
        self,
        *,
        GlobalNetworkId: str,
        TransitGatewayConnectPeerArn: str,
        DeviceId: str,
        LinkId: str = None
    ) -> AssociateTransitGatewayConnectPeerResponseTypeDef:
        """
        Associates a transit gateway Connect peer with a device, and optionally, with a
        link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.associate_transit_gateway_connect_peer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#associate_transit_gateway_connect_peer)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#can_paginate)
        """
    def create_connection(
        self,
        *,
        GlobalNetworkId: str,
        DeviceId: str,
        ConnectedDeviceId: str,
        LinkId: str = None,
        ConnectedLinkId: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateConnectionResponseTypeDef:
        """
        Creates a connection between two devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.create_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#create_connection)
        """
    def create_device(
        self,
        *,
        GlobalNetworkId: str,
        AWSLocation: "AWSLocationTypeDef" = None,
        Description: str = None,
        Type: str = None,
        Vendor: str = None,
        Model: str = None,
        SerialNumber: str = None,
        Location: "LocationTypeDef" = None,
        SiteId: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDeviceResponseTypeDef:
        """
        Creates a new device in a global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.create_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#create_device)
        """
    def create_global_network(
        self, *, Description: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateGlobalNetworkResponseTypeDef:
        """
        Creates a new, empty global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.create_global_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#create_global_network)
        """
    def create_link(
        self,
        *,
        GlobalNetworkId: str,
        Bandwidth: "BandwidthTypeDef",
        SiteId: str,
        Description: str = None,
        Type: str = None,
        Provider: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateLinkResponseTypeDef:
        """
        Creates a new link for a specified site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.create_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#create_link)
        """
    def create_site(
        self,
        *,
        GlobalNetworkId: str,
        Description: str = None,
        Location: "LocationTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateSiteResponseTypeDef:
        """
        Creates a new site in a global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.create_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#create_site)
        """
    def delete_connection(
        self, *, GlobalNetworkId: str, ConnectionId: str
    ) -> DeleteConnectionResponseTypeDef:
        """
        Deletes the specified connection in your global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.delete_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_connection)
        """
    def delete_device(self, *, GlobalNetworkId: str, DeviceId: str) -> DeleteDeviceResponseTypeDef:
        """
        Deletes an existing device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.delete_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_device)
        """
    def delete_global_network(self, *, GlobalNetworkId: str) -> DeleteGlobalNetworkResponseTypeDef:
        """
        Deletes an existing global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.delete_global_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_global_network)
        """
    def delete_link(self, *, GlobalNetworkId: str, LinkId: str) -> DeleteLinkResponseTypeDef:
        """
        Deletes an existing link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.delete_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_link)
        """
    def delete_site(self, *, GlobalNetworkId: str, SiteId: str) -> DeleteSiteResponseTypeDef:
        """
        Deletes an existing site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.delete_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_site)
        """
    def deregister_transit_gateway(
        self, *, GlobalNetworkId: str, TransitGatewayArn: str
    ) -> DeregisterTransitGatewayResponseTypeDef:
        """
        Deregisters a transit gateway from your global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.deregister_transit_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#deregister_transit_gateway)
        """
    def describe_global_networks(
        self, *, GlobalNetworkIds: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeGlobalNetworksResponseTypeDef:
        """
        Describes one or more global networks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.describe_global_networks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#describe_global_networks)
        """
    def disassociate_customer_gateway(
        self, *, GlobalNetworkId: str, CustomerGatewayArn: str
    ) -> DisassociateCustomerGatewayResponseTypeDef:
        """
        Disassociates a customer gateway from a device and a link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.disassociate_customer_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#disassociate_customer_gateway)
        """
    def disassociate_link(
        self, *, GlobalNetworkId: str, DeviceId: str, LinkId: str
    ) -> DisassociateLinkResponseTypeDef:
        """
        Disassociates an existing device from a link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.disassociate_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#disassociate_link)
        """
    def disassociate_transit_gateway_connect_peer(
        self, *, GlobalNetworkId: str, TransitGatewayConnectPeerArn: str
    ) -> DisassociateTransitGatewayConnectPeerResponseTypeDef:
        """
        Disassociates a transit gateway Connect peer from a device and link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.disassociate_transit_gateway_connect_peer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#disassociate_transit_gateway_connect_peer)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#generate_presigned_url)
        """
    def get_connections(
        self,
        *,
        GlobalNetworkId: str,
        ConnectionIds: List[str] = None,
        DeviceId: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetConnectionsResponseTypeDef:
        """
        Gets information about one or more of your connections in a global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.get_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_connections)
        """
    def get_customer_gateway_associations(
        self,
        *,
        GlobalNetworkId: str,
        CustomerGatewayArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetCustomerGatewayAssociationsResponseTypeDef:
        """
        Gets the association information for customer gateways that are associated with
        devices and links in your global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.get_customer_gateway_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_customer_gateway_associations)
        """
    def get_devices(
        self,
        *,
        GlobalNetworkId: str,
        DeviceIds: List[str] = None,
        SiteId: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetDevicesResponseTypeDef:
        """
        Gets information about one or more of your devices in a global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.get_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_devices)
        """
    def get_link_associations(
        self,
        *,
        GlobalNetworkId: str,
        DeviceId: str = None,
        LinkId: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetLinkAssociationsResponseTypeDef:
        """
        Gets the link associations for a device or a link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.get_link_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_link_associations)
        """
    def get_links(
        self,
        *,
        GlobalNetworkId: str,
        LinkIds: List[str] = None,
        SiteId: str = None,
        Type: str = None,
        Provider: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetLinksResponseTypeDef:
        """
        Gets information about one or more links in a specified global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.get_links)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_links)
        """
    def get_sites(
        self,
        *,
        GlobalNetworkId: str,
        SiteIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetSitesResponseTypeDef:
        """
        Gets information about one or more of your sites in a global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.get_sites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_sites)
        """
    def get_transit_gateway_connect_peer_associations(
        self,
        *,
        GlobalNetworkId: str,
        TransitGatewayConnectPeerArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetTransitGatewayConnectPeerAssociationsResponseTypeDef:
        """
        Gets information about one or more of your transit gateway Connect peer
        associations in a global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.get_transit_gateway_connect_peer_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_transit_gateway_connect_peer_associations)
        """
    def get_transit_gateway_registrations(
        self,
        *,
        GlobalNetworkId: str,
        TransitGatewayArns: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetTransitGatewayRegistrationsResponseTypeDef:
        """
        Gets information about the transit gateway registrations in a specified global
        network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.get_transit_gateway_registrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_transit_gateway_registrations)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#list_tags_for_resource)
        """
    def register_transit_gateway(
        self, *, GlobalNetworkId: str, TransitGatewayArn: str
    ) -> RegisterTransitGatewayResponseTypeDef:
        """
        Registers a transit gateway in your global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.register_transit_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#register_transit_gateway)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Tags a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#untag_resource)
        """
    def update_connection(
        self,
        *,
        GlobalNetworkId: str,
        ConnectionId: str,
        LinkId: str = None,
        ConnectedLinkId: str = None,
        Description: str = None
    ) -> UpdateConnectionResponseTypeDef:
        """
        Updates the information for an existing connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.update_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#update_connection)
        """
    def update_device(
        self,
        *,
        GlobalNetworkId: str,
        DeviceId: str,
        AWSLocation: "AWSLocationTypeDef" = None,
        Description: str = None,
        Type: str = None,
        Vendor: str = None,
        Model: str = None,
        SerialNumber: str = None,
        Location: "LocationTypeDef" = None,
        SiteId: str = None
    ) -> UpdateDeviceResponseTypeDef:
        """
        Updates the details for an existing device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.update_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#update_device)
        """
    def update_global_network(
        self, *, GlobalNetworkId: str, Description: str = None
    ) -> UpdateGlobalNetworkResponseTypeDef:
        """
        Updates an existing global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.update_global_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#update_global_network)
        """
    def update_link(
        self,
        *,
        GlobalNetworkId: str,
        LinkId: str,
        Description: str = None,
        Type: str = None,
        Bandwidth: "BandwidthTypeDef" = None,
        Provider: str = None
    ) -> UpdateLinkResponseTypeDef:
        """
        Updates the details for an existing link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.update_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#update_link)
        """
    def update_site(
        self,
        *,
        GlobalNetworkId: str,
        SiteId: str,
        Description: str = None,
        Location: "LocationTypeDef" = None
    ) -> UpdateSiteResponseTypeDef:
        """
        Updates the information for an existing site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Client.update_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#update_site)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_global_networks"]
    ) -> DescribeGlobalNetworksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#describeglobalnetworkspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_connections"]) -> GetConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Paginator.GetConnections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getconnectionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_customer_gateway_associations"]
    ) -> GetCustomerGatewayAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getcustomergatewayassociationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_devices"]) -> GetDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getdevicespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_link_associations"]
    ) -> GetLinkAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getlinkassociationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_links"]) -> GetLinksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getlinkspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_sites"]) -> GetSitesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getsitespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_connect_peer_associations"]
    ) -> GetTransitGatewayConnectPeerAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayConnectPeerAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#gettransitgatewayconnectpeerassociationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_registrations"]
    ) -> GetTransitGatewayRegistrationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#gettransitgatewayregistrationspaginator)
        """
