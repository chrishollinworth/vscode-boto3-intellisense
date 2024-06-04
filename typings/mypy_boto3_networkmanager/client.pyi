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

from .literals import (
    AttachmentStateType,
    AttachmentTypeType,
    CoreNetworkPolicyAliasType,
    PeeringStateType,
    RouteStateType,
    RouteTypeType,
)
from .paginator import (
    DescribeGlobalNetworksPaginator,
    GetConnectionsPaginator,
    GetConnectPeerAssociationsPaginator,
    GetCoreNetworkChangeEventsPaginator,
    GetCoreNetworkChangeSetPaginator,
    GetCustomerGatewayAssociationsPaginator,
    GetDevicesPaginator,
    GetLinkAssociationsPaginator,
    GetLinksPaginator,
    GetNetworkResourceCountsPaginator,
    GetNetworkResourceRelationshipsPaginator,
    GetNetworkResourcesPaginator,
    GetNetworkTelemetryPaginator,
    GetSitesPaginator,
    GetTransitGatewayConnectPeerAssociationsPaginator,
    GetTransitGatewayRegistrationsPaginator,
    ListAttachmentsPaginator,
    ListConnectPeersPaginator,
    ListCoreNetworkPolicyVersionsPaginator,
    ListCoreNetworksPaginator,
    ListPeeringsPaginator,
)
from .type_defs import (
    AcceptAttachmentResponseTypeDef,
    AssociateConnectPeerResponseTypeDef,
    AssociateCustomerGatewayResponseTypeDef,
    AssociateLinkResponseTypeDef,
    AssociateTransitGatewayConnectPeerResponseTypeDef,
    AWSLocationTypeDef,
    BandwidthTypeDef,
    BgpOptionsTypeDef,
    ConnectAttachmentOptionsTypeDef,
    CreateConnectAttachmentResponseTypeDef,
    CreateConnectionResponseTypeDef,
    CreateConnectPeerResponseTypeDef,
    CreateCoreNetworkResponseTypeDef,
    CreateDeviceResponseTypeDef,
    CreateGlobalNetworkResponseTypeDef,
    CreateLinkResponseTypeDef,
    CreateSiteResponseTypeDef,
    CreateSiteToSiteVpnAttachmentResponseTypeDef,
    CreateTransitGatewayPeeringResponseTypeDef,
    CreateTransitGatewayRouteTableAttachmentResponseTypeDef,
    CreateVpcAttachmentResponseTypeDef,
    DeleteAttachmentResponseTypeDef,
    DeleteConnectionResponseTypeDef,
    DeleteConnectPeerResponseTypeDef,
    DeleteCoreNetworkPolicyVersionResponseTypeDef,
    DeleteCoreNetworkResponseTypeDef,
    DeleteDeviceResponseTypeDef,
    DeleteGlobalNetworkResponseTypeDef,
    DeleteLinkResponseTypeDef,
    DeletePeeringResponseTypeDef,
    DeleteSiteResponseTypeDef,
    DeregisterTransitGatewayResponseTypeDef,
    DescribeGlobalNetworksResponseTypeDef,
    DisassociateConnectPeerResponseTypeDef,
    DisassociateCustomerGatewayResponseTypeDef,
    DisassociateLinkResponseTypeDef,
    DisassociateTransitGatewayConnectPeerResponseTypeDef,
    GetConnectAttachmentResponseTypeDef,
    GetConnectionsResponseTypeDef,
    GetConnectPeerAssociationsResponseTypeDef,
    GetConnectPeerResponseTypeDef,
    GetCoreNetworkChangeEventsResponseTypeDef,
    GetCoreNetworkChangeSetResponseTypeDef,
    GetCoreNetworkPolicyResponseTypeDef,
    GetCoreNetworkResponseTypeDef,
    GetCustomerGatewayAssociationsResponseTypeDef,
    GetDevicesResponseTypeDef,
    GetLinkAssociationsResponseTypeDef,
    GetLinksResponseTypeDef,
    GetNetworkResourceCountsResponseTypeDef,
    GetNetworkResourceRelationshipsResponseTypeDef,
    GetNetworkResourcesResponseTypeDef,
    GetNetworkRoutesResponseTypeDef,
    GetNetworkTelemetryResponseTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetRouteAnalysisResponseTypeDef,
    GetSitesResponseTypeDef,
    GetSiteToSiteVpnAttachmentResponseTypeDef,
    GetTransitGatewayConnectPeerAssociationsResponseTypeDef,
    GetTransitGatewayPeeringResponseTypeDef,
    GetTransitGatewayRegistrationsResponseTypeDef,
    GetTransitGatewayRouteTableAttachmentResponseTypeDef,
    GetVpcAttachmentResponseTypeDef,
    ListAttachmentsResponseTypeDef,
    ListConnectPeersResponseTypeDef,
    ListCoreNetworkPolicyVersionsResponseTypeDef,
    ListCoreNetworksResponseTypeDef,
    ListOrganizationServiceAccessStatusResponseTypeDef,
    ListPeeringsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LocationTypeDef,
    PutCoreNetworkPolicyResponseTypeDef,
    RegisterTransitGatewayResponseTypeDef,
    RejectAttachmentResponseTypeDef,
    RestoreCoreNetworkPolicyVersionResponseTypeDef,
    RouteAnalysisEndpointOptionsSpecificationTypeDef,
    RouteTableIdentifierTypeDef,
    StartOrganizationServiceAccessUpdateResponseTypeDef,
    StartRouteAnalysisResponseTypeDef,
    TagTypeDef,
    UpdateConnectionResponseTypeDef,
    UpdateCoreNetworkResponseTypeDef,
    UpdateDeviceResponseTypeDef,
    UpdateGlobalNetworkResponseTypeDef,
    UpdateLinkResponseTypeDef,
    UpdateNetworkResourceMetadataResponseTypeDef,
    UpdateSiteResponseTypeDef,
    UpdateVpcAttachmentResponseTypeDef,
    VpcOptionsTypeDef,
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
    CoreNetworkPolicyException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class NetworkManagerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NetworkManagerClient exceptions.
        """

    def accept_attachment(self, *, AttachmentId: str) -> AcceptAttachmentResponseTypeDef:
        """
        Accepts a core network attachment request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.accept_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#accept_attachment)
        """

    def associate_connect_peer(
        self, *, GlobalNetworkId: str, ConnectPeerId: str, DeviceId: str, LinkId: str = None
    ) -> AssociateConnectPeerResponseTypeDef:
        """
        Associates a core network Connect peer with a device and optionally, with a
        link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.associate_connect_peer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#associate_connect_peer)
        """

    def associate_customer_gateway(
        self, *, CustomerGatewayArn: str, GlobalNetworkId: str, DeviceId: str, LinkId: str = None
    ) -> AssociateCustomerGatewayResponseTypeDef:
        """
        Associates a customer gateway with a device and optionally, with a link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.associate_customer_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#associate_customer_gateway)
        """

    def associate_link(
        self, *, GlobalNetworkId: str, DeviceId: str, LinkId: str
    ) -> AssociateLinkResponseTypeDef:
        """
        Associates a link to a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.associate_link)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.associate_transit_gateway_connect_peer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#associate_transit_gateway_connect_peer)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#close)
        """

    def create_connect_attachment(
        self,
        *,
        CoreNetworkId: str,
        EdgeLocation: str,
        TransportAttachmentId: str,
        Options: "ConnectAttachmentOptionsTypeDef",
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None
    ) -> CreateConnectAttachmentResponseTypeDef:
        """
        Creates a core network Connect attachment from a specified core network
        attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.create_connect_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#create_connect_attachment)
        """

    def create_connect_peer(
        self,
        *,
        ConnectAttachmentId: str,
        PeerAddress: str,
        CoreNetworkAddress: str = None,
        BgpOptions: "BgpOptionsTypeDef" = None,
        InsideCidrBlocks: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None,
        SubnetArn: str = None
    ) -> CreateConnectPeerResponseTypeDef:
        """
        Creates a core network Connect peer for a specified core network connect
        attachment between a core network and an appliance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.create_connect_peer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#create_connect_peer)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.create_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#create_connection)
        """

    def create_core_network(
        self,
        *,
        GlobalNetworkId: str,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        PolicyDocument: str = None,
        ClientToken: str = None
    ) -> CreateCoreNetworkResponseTypeDef:
        """
        Creates a core network as part of your global network, and optionally, with a
        core network policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.create_core_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#create_core_network)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.create_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#create_device)
        """

    def create_global_network(
        self, *, Description: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateGlobalNetworkResponseTypeDef:
        """
        Creates a new, empty global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.create_global_network)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.create_link)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.create_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#create_site)
        """

    def create_site_to_site_vpn_attachment(
        self,
        *,
        CoreNetworkId: str,
        VpnConnectionArn: str,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None
    ) -> CreateSiteToSiteVpnAttachmentResponseTypeDef:
        """
        Creates an Amazon Web Services site-to-site VPN attachment on an edge location
        of a core network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.create_site_to_site_vpn_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#create_site_to_site_vpn_attachment)
        """

    def create_transit_gateway_peering(
        self,
        *,
        CoreNetworkId: str,
        TransitGatewayArn: str,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None
    ) -> CreateTransitGatewayPeeringResponseTypeDef:
        """
        Creates a transit gateway peering connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.create_transit_gateway_peering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#create_transit_gateway_peering)
        """

    def create_transit_gateway_route_table_attachment(
        self,
        *,
        PeeringId: str,
        TransitGatewayRouteTableArn: str,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None
    ) -> CreateTransitGatewayRouteTableAttachmentResponseTypeDef:
        """
        Creates a transit gateway route table attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.create_transit_gateway_route_table_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#create_transit_gateway_route_table_attachment)
        """

    def create_vpc_attachment(
        self,
        *,
        CoreNetworkId: str,
        VpcArn: str,
        SubnetArns: List[str],
        Options: "VpcOptionsTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None
    ) -> CreateVpcAttachmentResponseTypeDef:
        """
        Creates a VPC attachment on an edge location of a core network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.create_vpc_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#create_vpc_attachment)
        """

    def delete_attachment(self, *, AttachmentId: str) -> DeleteAttachmentResponseTypeDef:
        """
        Deletes an attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.delete_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_attachment)
        """

    def delete_connect_peer(self, *, ConnectPeerId: str) -> DeleteConnectPeerResponseTypeDef:
        """
        Deletes a Connect peer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.delete_connect_peer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_connect_peer)
        """

    def delete_connection(
        self, *, GlobalNetworkId: str, ConnectionId: str
    ) -> DeleteConnectionResponseTypeDef:
        """
        Deletes the specified connection in your global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.delete_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_connection)
        """

    def delete_core_network(self, *, CoreNetworkId: str) -> DeleteCoreNetworkResponseTypeDef:
        """
        Deletes a core network along with all core network policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.delete_core_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_core_network)
        """

    def delete_core_network_policy_version(
        self, *, CoreNetworkId: str, PolicyVersionId: int
    ) -> DeleteCoreNetworkPolicyVersionResponseTypeDef:
        """
        Deletes a policy version from a core network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.delete_core_network_policy_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_core_network_policy_version)
        """

    def delete_device(self, *, GlobalNetworkId: str, DeviceId: str) -> DeleteDeviceResponseTypeDef:
        """
        Deletes an existing device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.delete_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_device)
        """

    def delete_global_network(self, *, GlobalNetworkId: str) -> DeleteGlobalNetworkResponseTypeDef:
        """
        Deletes an existing global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.delete_global_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_global_network)
        """

    def delete_link(self, *, GlobalNetworkId: str, LinkId: str) -> DeleteLinkResponseTypeDef:
        """
        Deletes an existing link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.delete_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_link)
        """

    def delete_peering(self, *, PeeringId: str) -> DeletePeeringResponseTypeDef:
        """
        Deletes an existing peering connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.delete_peering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_peering)
        """

    def delete_resource_policy(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        Deletes a resource policy for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_resource_policy)
        """

    def delete_site(self, *, GlobalNetworkId: str, SiteId: str) -> DeleteSiteResponseTypeDef:
        """
        Deletes an existing site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.delete_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#delete_site)
        """

    def deregister_transit_gateway(
        self, *, GlobalNetworkId: str, TransitGatewayArn: str
    ) -> DeregisterTransitGatewayResponseTypeDef:
        """
        Deregisters a transit gateway from your global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.deregister_transit_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#deregister_transit_gateway)
        """

    def describe_global_networks(
        self, *, GlobalNetworkIds: List[str] = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeGlobalNetworksResponseTypeDef:
        """
        Describes one or more global networks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.describe_global_networks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#describe_global_networks)
        """

    def disassociate_connect_peer(
        self, *, GlobalNetworkId: str, ConnectPeerId: str
    ) -> DisassociateConnectPeerResponseTypeDef:
        """
        Disassociates a core network Connect peer from a device and a link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.disassociate_connect_peer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#disassociate_connect_peer)
        """

    def disassociate_customer_gateway(
        self, *, GlobalNetworkId: str, CustomerGatewayArn: str
    ) -> DisassociateCustomerGatewayResponseTypeDef:
        """
        Disassociates a customer gateway from a device and a link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.disassociate_customer_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#disassociate_customer_gateway)
        """

    def disassociate_link(
        self, *, GlobalNetworkId: str, DeviceId: str, LinkId: str
    ) -> DisassociateLinkResponseTypeDef:
        """
        Disassociates an existing device from a link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.disassociate_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#disassociate_link)
        """

    def disassociate_transit_gateway_connect_peer(
        self, *, GlobalNetworkId: str, TransitGatewayConnectPeerArn: str
    ) -> DisassociateTransitGatewayConnectPeerResponseTypeDef:
        """
        Disassociates a transit gateway Connect peer from a device and link.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.disassociate_transit_gateway_connect_peer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#disassociate_transit_gateway_connect_peer)
        """

    def execute_core_network_change_set(
        self, *, CoreNetworkId: str, PolicyVersionId: int
    ) -> Dict[str, Any]:
        """
        Executes a change set on your core network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.execute_core_network_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#execute_core_network_change_set)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#generate_presigned_url)
        """

    def get_connect_attachment(self, *, AttachmentId: str) -> GetConnectAttachmentResponseTypeDef:
        """
        Returns information about a core network Connect attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_connect_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_connect_attachment)
        """

    def get_connect_peer(self, *, ConnectPeerId: str) -> GetConnectPeerResponseTypeDef:
        """
        Returns information about a core network Connect peer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_connect_peer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_connect_peer)
        """

    def get_connect_peer_associations(
        self,
        *,
        GlobalNetworkId: str,
        ConnectPeerIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetConnectPeerAssociationsResponseTypeDef:
        """
        Returns information about a core network Connect peer associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_connect_peer_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_connect_peer_associations)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_connections)
        """

    def get_core_network(self, *, CoreNetworkId: str) -> GetCoreNetworkResponseTypeDef:
        """
        Returns information about the LIVE policy for a core network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_core_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_core_network)
        """

    def get_core_network_change_events(
        self,
        *,
        CoreNetworkId: str,
        PolicyVersionId: int,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetCoreNetworkChangeEventsResponseTypeDef:
        """
        Returns information about a core network change event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_core_network_change_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_core_network_change_events)
        """

    def get_core_network_change_set(
        self,
        *,
        CoreNetworkId: str,
        PolicyVersionId: int,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetCoreNetworkChangeSetResponseTypeDef:
        """
        Returns a change set between the LIVE core network policy and a submitted
        policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_core_network_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_core_network_change_set)
        """

    def get_core_network_policy(
        self,
        *,
        CoreNetworkId: str,
        PolicyVersionId: int = None,
        Alias: CoreNetworkPolicyAliasType = None
    ) -> GetCoreNetworkPolicyResponseTypeDef:
        """
        Returns details about a core network policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_core_network_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_core_network_policy)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_customer_gateway_associations)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_devices)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_link_associations)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_links)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_links)
        """

    def get_network_resource_counts(
        self,
        *,
        GlobalNetworkId: str,
        ResourceType: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetNetworkResourceCountsResponseTypeDef:
        """
        Gets the count of network resources, by resource type, for the specified global
        network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_network_resource_counts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_network_resource_counts)
        """

    def get_network_resource_relationships(
        self,
        *,
        GlobalNetworkId: str,
        CoreNetworkId: str = None,
        RegisteredGatewayArn: str = None,
        AwsRegion: str = None,
        AccountId: str = None,
        ResourceType: str = None,
        ResourceArn: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetNetworkResourceRelationshipsResponseTypeDef:
        """
        Gets the network resource relationships for the specified global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_network_resource_relationships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_network_resource_relationships)
        """

    def get_network_resources(
        self,
        *,
        GlobalNetworkId: str,
        CoreNetworkId: str = None,
        RegisteredGatewayArn: str = None,
        AwsRegion: str = None,
        AccountId: str = None,
        ResourceType: str = None,
        ResourceArn: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetNetworkResourcesResponseTypeDef:
        """
        Describes the network resources for the specified global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_network_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_network_resources)
        """

    def get_network_routes(
        self,
        *,
        GlobalNetworkId: str,
        RouteTableIdentifier: "RouteTableIdentifierTypeDef",
        ExactCidrMatches: List[str] = None,
        LongestPrefixMatches: List[str] = None,
        SubnetOfMatches: List[str] = None,
        SupernetOfMatches: List[str] = None,
        PrefixListIds: List[str] = None,
        States: List[RouteStateType] = None,
        Types: List[RouteTypeType] = None,
        DestinationFilters: Dict[str, List[str]] = None
    ) -> GetNetworkRoutesResponseTypeDef:
        """
        Gets the network routes of the specified global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_network_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_network_routes)
        """

    def get_network_telemetry(
        self,
        *,
        GlobalNetworkId: str,
        CoreNetworkId: str = None,
        RegisteredGatewayArn: str = None,
        AwsRegion: str = None,
        AccountId: str = None,
        ResourceType: str = None,
        ResourceArn: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetNetworkTelemetryResponseTypeDef:
        """
        Gets the network telemetry of the specified global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_network_telemetry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_network_telemetry)
        """

    def get_resource_policy(self, *, ResourceArn: str) -> GetResourcePolicyResponseTypeDef:
        """
        Returns information about a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_resource_policy)
        """

    def get_route_analysis(
        self, *, GlobalNetworkId: str, RouteAnalysisId: str
    ) -> GetRouteAnalysisResponseTypeDef:
        """
        Gets information about the specified route analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_route_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_route_analysis)
        """

    def get_site_to_site_vpn_attachment(
        self, *, AttachmentId: str
    ) -> GetSiteToSiteVpnAttachmentResponseTypeDef:
        """
        Returns information about a site-to-site VPN attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_site_to_site_vpn_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_site_to_site_vpn_attachment)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_sites)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_transit_gateway_connect_peer_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_transit_gateway_connect_peer_associations)
        """

    def get_transit_gateway_peering(
        self, *, PeeringId: str
    ) -> GetTransitGatewayPeeringResponseTypeDef:
        """
        Returns information about a transit gateway peer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_transit_gateway_peering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_transit_gateway_peering)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_transit_gateway_registrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_transit_gateway_registrations)
        """

    def get_transit_gateway_route_table_attachment(
        self, *, AttachmentId: str
    ) -> GetTransitGatewayRouteTableAttachmentResponseTypeDef:
        """
        Returns information about a transit gateway route table attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_transit_gateway_route_table_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_transit_gateway_route_table_attachment)
        """

    def get_vpc_attachment(self, *, AttachmentId: str) -> GetVpcAttachmentResponseTypeDef:
        """
        Returns information about a VPC attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.get_vpc_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#get_vpc_attachment)
        """

    def list_attachments(
        self,
        *,
        CoreNetworkId: str = None,
        AttachmentType: AttachmentTypeType = None,
        EdgeLocation: str = None,
        State: AttachmentStateType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListAttachmentsResponseTypeDef:
        """
        Returns a list of core network attachments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.list_attachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#list_attachments)
        """

    def list_connect_peers(
        self,
        *,
        CoreNetworkId: str = None,
        ConnectAttachmentId: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListConnectPeersResponseTypeDef:
        """
        Returns a list of core network Connect peers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.list_connect_peers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#list_connect_peers)
        """

    def list_core_network_policy_versions(
        self, *, CoreNetworkId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListCoreNetworkPolicyVersionsResponseTypeDef:
        """
        Returns a list of core network policy versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.list_core_network_policy_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#list_core_network_policy_versions)
        """

    def list_core_networks(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListCoreNetworksResponseTypeDef:
        """
        Returns a list of owned and shared core networks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.list_core_networks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#list_core_networks)
        """

    def list_organization_service_access_status(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListOrganizationServiceAccessStatusResponseTypeDef:
        """
        Gets the status of the Service Linked Role (SLR) deployment for the accounts in
        a given Amazon Web Services Organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.list_organization_service_access_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#list_organization_service_access_status)
        """

    def list_peerings(
        self,
        *,
        CoreNetworkId: str = None,
        PeeringType: Literal["TRANSIT_GATEWAY"] = None,
        EdgeLocation: str = None,
        State: PeeringStateType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListPeeringsResponseTypeDef:
        """
        Lists the peerings for a core network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.list_peerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#list_peerings)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#list_tags_for_resource)
        """

    def put_core_network_policy(
        self,
        *,
        CoreNetworkId: str,
        PolicyDocument: str,
        Description: str = None,
        LatestVersionId: int = None,
        ClientToken: str = None
    ) -> PutCoreNetworkPolicyResponseTypeDef:
        """
        Creates a new, immutable version of a core network policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.put_core_network_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#put_core_network_policy)
        """

    def put_resource_policy(self, *, PolicyDocument: str, ResourceArn: str) -> Dict[str, Any]:
        """
        Creates or updates a resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#put_resource_policy)
        """

    def register_transit_gateway(
        self, *, GlobalNetworkId: str, TransitGatewayArn: str
    ) -> RegisterTransitGatewayResponseTypeDef:
        """
        Registers a transit gateway in your global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.register_transit_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#register_transit_gateway)
        """

    def reject_attachment(self, *, AttachmentId: str) -> RejectAttachmentResponseTypeDef:
        """
        Rejects a core network attachment request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.reject_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#reject_attachment)
        """

    def restore_core_network_policy_version(
        self, *, CoreNetworkId: str, PolicyVersionId: int
    ) -> RestoreCoreNetworkPolicyVersionResponseTypeDef:
        """
        Restores a previous policy version as a new, immutable version of a core network
        policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.restore_core_network_policy_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#restore_core_network_policy_version)
        """

    def start_organization_service_access_update(
        self, *, Action: str
    ) -> StartOrganizationServiceAccessUpdateResponseTypeDef:
        """
        Enables the Network Manager service for an Amazon Web Services Organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.start_organization_service_access_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#start_organization_service_access_update)
        """

    def start_route_analysis(
        self,
        *,
        GlobalNetworkId: str,
        Source: "RouteAnalysisEndpointOptionsSpecificationTypeDef",
        Destination: "RouteAnalysisEndpointOptionsSpecificationTypeDef",
        IncludeReturnPath: bool = None,
        UseMiddleboxes: bool = None
    ) -> StartRouteAnalysisResponseTypeDef:
        """
        Starts analyzing the routing path between the specified source and destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.start_route_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#start_route_analysis)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Tags a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.untag_resource)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.update_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#update_connection)
        """

    def update_core_network(
        self, *, CoreNetworkId: str, Description: str = None
    ) -> UpdateCoreNetworkResponseTypeDef:
        """
        Updates the description of a core network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.update_core_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#update_core_network)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.update_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#update_device)
        """

    def update_global_network(
        self, *, GlobalNetworkId: str, Description: str = None
    ) -> UpdateGlobalNetworkResponseTypeDef:
        """
        Updates an existing global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.update_global_network)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.update_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#update_link)
        """

    def update_network_resource_metadata(
        self, *, GlobalNetworkId: str, ResourceArn: str, Metadata: Dict[str, str]
    ) -> UpdateNetworkResourceMetadataResponseTypeDef:
        """
        Updates the resource metadata for the specified global network.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.update_network_resource_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#update_network_resource_metadata)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.update_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#update_site)
        """

    def update_vpc_attachment(
        self,
        *,
        AttachmentId: str,
        AddSubnetArns: List[str] = None,
        RemoveSubnetArns: List[str] = None,
        Options: "VpcOptionsTypeDef" = None
    ) -> UpdateVpcAttachmentResponseTypeDef:
        """
        Updates a VPC attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Client.update_vpc_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/client.html#update_vpc_attachment)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_global_networks"]
    ) -> DescribeGlobalNetworksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.DescribeGlobalNetworks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#describeglobalnetworkspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_connect_peer_associations"]
    ) -> GetConnectPeerAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.GetConnectPeerAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getconnectpeerassociationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_connections"]) -> GetConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.GetConnections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getconnectionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_core_network_change_events"]
    ) -> GetCoreNetworkChangeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.GetCoreNetworkChangeEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getcorenetworkchangeeventspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_core_network_change_set"]
    ) -> GetCoreNetworkChangeSetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.GetCoreNetworkChangeSet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getcorenetworkchangesetpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_customer_gateway_associations"]
    ) -> GetCustomerGatewayAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.GetCustomerGatewayAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getcustomergatewayassociationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_devices"]) -> GetDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.GetDevices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getdevicespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_link_associations"]
    ) -> GetLinkAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinkAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getlinkassociationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_links"]) -> GetLinksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.GetLinks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getlinkspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_network_resource_counts"]
    ) -> GetNetworkResourceCountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.GetNetworkResourceCounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getnetworkresourcecountspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_network_resource_relationships"]
    ) -> GetNetworkResourceRelationshipsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.GetNetworkResourceRelationships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getnetworkresourcerelationshipspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_network_resources"]
    ) -> GetNetworkResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.GetNetworkResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getnetworkresourcespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_network_telemetry"]
    ) -> GetNetworkTelemetryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.GetNetworkTelemetry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getnetworktelemetrypaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_sites"]) -> GetSitesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.GetSites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#getsitespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_connect_peer_associations"]
    ) -> GetTransitGatewayConnectPeerAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayConnectPeerAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#gettransitgatewayconnectpeerassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_registrations"]
    ) -> GetTransitGatewayRegistrationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.GetTransitGatewayRegistrations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#gettransitgatewayregistrationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_attachments"]
    ) -> ListAttachmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.ListAttachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#listattachmentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_connect_peers"]
    ) -> ListConnectPeersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.ListConnectPeers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#listconnectpeerspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_core_network_policy_versions"]
    ) -> ListCoreNetworkPolicyVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.ListCoreNetworkPolicyVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#listcorenetworkpolicyversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_core_networks"]
    ) -> ListCoreNetworksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.ListCoreNetworks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#listcorenetworkspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_peerings"]) -> ListPeeringsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmanager.html#NetworkManager.Paginator.ListPeerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/paginators.html#listpeeringspaginator)
        """
