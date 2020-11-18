# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for directconnect service client

Usage::

    ```python
    import boto3
    from mypy_boto3_directconnect import DirectConnectClient

    client: DirectConnectClient = boto3.client("directconnect")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_directconnect.paginator import (
    DescribeDirectConnectGatewayAssociationsPaginator,
    DescribeDirectConnectGatewayAttachmentsPaginator,
    DescribeDirectConnectGatewaysPaginator,
)
from mypy_boto3_directconnect.type_defs import (
    AcceptDirectConnectGatewayAssociationProposalResultTypeDef,
    AllocateTransitVirtualInterfaceResultTypeDef,
    ConfirmConnectionResponseTypeDef,
    ConfirmPrivateVirtualInterfaceResponseTypeDef,
    ConfirmPublicVirtualInterfaceResponseTypeDef,
    ConfirmTransitVirtualInterfaceResponseTypeDef,
    ConnectionsTypeDef,
    ConnectionTypeDef,
    CreateBGPPeerResponseTypeDef,
    CreateDirectConnectGatewayAssociationProposalResultTypeDef,
    CreateDirectConnectGatewayAssociationResultTypeDef,
    CreateDirectConnectGatewayResultTypeDef,
    CreateTransitVirtualInterfaceResultTypeDef,
    DeleteBGPPeerResponseTypeDef,
    DeleteDirectConnectGatewayAssociationProposalResultTypeDef,
    DeleteDirectConnectGatewayAssociationResultTypeDef,
    DeleteDirectConnectGatewayResultTypeDef,
    DeleteInterconnectResponseTypeDef,
    DeleteVirtualInterfaceResponseTypeDef,
    DescribeConnectionLoaResponseTypeDef,
    DescribeDirectConnectGatewayAssociationProposalsResultTypeDef,
    DescribeDirectConnectGatewayAssociationsResultTypeDef,
    DescribeDirectConnectGatewayAttachmentsResultTypeDef,
    DescribeDirectConnectGatewaysResultTypeDef,
    DescribeInterconnectLoaResponseTypeDef,
    DescribeTagsResponseTypeDef,
    InterconnectsTypeDef,
    InterconnectTypeDef,
    LagsTypeDef,
    LagTypeDef,
    ListVirtualInterfaceTestHistoryResponseTypeDef,
    LoaTypeDef,
    LocationsTypeDef,
    NewBGPPeerTypeDef,
    NewPrivateVirtualInterfaceAllocationTypeDef,
    NewPrivateVirtualInterfaceTypeDef,
    NewPublicVirtualInterfaceAllocationTypeDef,
    NewPublicVirtualInterfaceTypeDef,
    NewTransitVirtualInterfaceAllocationTypeDef,
    NewTransitVirtualInterfaceTypeDef,
    RouteFilterPrefixTypeDef,
    StartBgpFailoverTestResponseTypeDef,
    StopBgpFailoverTestResponseTypeDef,
    TagTypeDef,
    UpdateDirectConnectGatewayAssociationResultTypeDef,
    VirtualGatewaysTypeDef,
    VirtualInterfacesTypeDef,
    VirtualInterfaceTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DirectConnectClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    DirectConnectClientException: Type[BotocoreClientError]
    DirectConnectServerException: Type[BotocoreClientError]
    DuplicateTagKeysException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]


class DirectConnectClient:
    """
    [DirectConnect.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_direct_connect_gateway_association_proposal(
        self,
        directConnectGatewayId: str,
        proposalId: str,
        associatedGatewayOwnerAccount: str,
        overrideAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None,
    ) -> AcceptDirectConnectGatewayAssociationProposalResultTypeDef:
        """
        [Client.accept_direct_connect_gateway_association_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.accept_direct_connect_gateway_association_proposal)
        """

    def allocate_connection_on_interconnect(
        self, bandwidth: str, connectionName: str, ownerAccount: str, interconnectId: str, vlan: int
    ) -> "ConnectionTypeDef":
        """
        [Client.allocate_connection_on_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.allocate_connection_on_interconnect)
        """

    def allocate_hosted_connection(
        self,
        connectionId: str,
        ownerAccount: str,
        bandwidth: str,
        connectionName: str,
        vlan: int,
        tags: List["TagTypeDef"] = None,
    ) -> "ConnectionTypeDef":
        """
        [Client.allocate_hosted_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.allocate_hosted_connection)
        """

    def allocate_private_virtual_interface(
        self,
        connectionId: str,
        ownerAccount: str,
        newPrivateVirtualInterfaceAllocation: NewPrivateVirtualInterfaceAllocationTypeDef,
    ) -> "VirtualInterfaceTypeDef":
        """
        [Client.allocate_private_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.allocate_private_virtual_interface)
        """

    def allocate_public_virtual_interface(
        self,
        connectionId: str,
        ownerAccount: str,
        newPublicVirtualInterfaceAllocation: NewPublicVirtualInterfaceAllocationTypeDef,
    ) -> "VirtualInterfaceTypeDef":
        """
        [Client.allocate_public_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.allocate_public_virtual_interface)
        """

    def allocate_transit_virtual_interface(
        self,
        connectionId: str,
        ownerAccount: str,
        newTransitVirtualInterfaceAllocation: NewTransitVirtualInterfaceAllocationTypeDef,
    ) -> AllocateTransitVirtualInterfaceResultTypeDef:
        """
        [Client.allocate_transit_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.allocate_transit_virtual_interface)
        """

    def associate_connection_with_lag(self, connectionId: str, lagId: str) -> "ConnectionTypeDef":
        """
        [Client.associate_connection_with_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.associate_connection_with_lag)
        """

    def associate_hosted_connection(
        self, connectionId: str, parentConnectionId: str
    ) -> "ConnectionTypeDef":
        """
        [Client.associate_hosted_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.associate_hosted_connection)
        """

    def associate_virtual_interface(
        self, virtualInterfaceId: str, connectionId: str
    ) -> "VirtualInterfaceTypeDef":
        """
        [Client.associate_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.associate_virtual_interface)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.can_paginate)
        """

    def confirm_connection(self, connectionId: str) -> ConfirmConnectionResponseTypeDef:
        """
        [Client.confirm_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.confirm_connection)
        """

    def confirm_private_virtual_interface(
        self,
        virtualInterfaceId: str,
        virtualGatewayId: str = None,
        directConnectGatewayId: str = None,
    ) -> ConfirmPrivateVirtualInterfaceResponseTypeDef:
        """
        [Client.confirm_private_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.confirm_private_virtual_interface)
        """

    def confirm_public_virtual_interface(
        self, virtualInterfaceId: str
    ) -> ConfirmPublicVirtualInterfaceResponseTypeDef:
        """
        [Client.confirm_public_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.confirm_public_virtual_interface)
        """

    def confirm_transit_virtual_interface(
        self, virtualInterfaceId: str, directConnectGatewayId: str
    ) -> ConfirmTransitVirtualInterfaceResponseTypeDef:
        """
        [Client.confirm_transit_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.confirm_transit_virtual_interface)
        """

    def create_bgp_peer(
        self, virtualInterfaceId: str = None, newBGPPeer: NewBGPPeerTypeDef = None
    ) -> CreateBGPPeerResponseTypeDef:
        """
        [Client.create_bgp_peer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.create_bgp_peer)
        """

    def create_connection(
        self,
        location: str,
        bandwidth: str,
        connectionName: str,
        lagId: str = None,
        tags: List["TagTypeDef"] = None,
        providerName: str = None,
    ) -> "ConnectionTypeDef":
        """
        [Client.create_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.create_connection)
        """

    def create_direct_connect_gateway(
        self, directConnectGatewayName: str, amazonSideAsn: int = None
    ) -> CreateDirectConnectGatewayResultTypeDef:
        """
        [Client.create_direct_connect_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.create_direct_connect_gateway)
        """

    def create_direct_connect_gateway_association(
        self,
        directConnectGatewayId: str,
        gatewayId: str = None,
        addAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None,
        virtualGatewayId: str = None,
    ) -> CreateDirectConnectGatewayAssociationResultTypeDef:
        """
        [Client.create_direct_connect_gateway_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.create_direct_connect_gateway_association)
        """

    def create_direct_connect_gateway_association_proposal(
        self,
        directConnectGatewayId: str,
        directConnectGatewayOwnerAccount: str,
        gatewayId: str,
        addAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None,
        removeAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None,
    ) -> CreateDirectConnectGatewayAssociationProposalResultTypeDef:
        """
        [Client.create_direct_connect_gateway_association_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.create_direct_connect_gateway_association_proposal)
        """

    def create_interconnect(
        self,
        interconnectName: str,
        bandwidth: str,
        location: str,
        lagId: str = None,
        tags: List["TagTypeDef"] = None,
        providerName: str = None,
    ) -> "InterconnectTypeDef":
        """
        [Client.create_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.create_interconnect)
        """

    def create_lag(
        self,
        numberOfConnections: int,
        location: str,
        connectionsBandwidth: str,
        lagName: str,
        connectionId: str = None,
        tags: List["TagTypeDef"] = None,
        childConnectionTags: List["TagTypeDef"] = None,
        providerName: str = None,
    ) -> "LagTypeDef":
        """
        [Client.create_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.create_lag)
        """

    def create_private_virtual_interface(
        self, connectionId: str, newPrivateVirtualInterface: NewPrivateVirtualInterfaceTypeDef
    ) -> "VirtualInterfaceTypeDef":
        """
        [Client.create_private_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.create_private_virtual_interface)
        """

    def create_public_virtual_interface(
        self, connectionId: str, newPublicVirtualInterface: NewPublicVirtualInterfaceTypeDef
    ) -> "VirtualInterfaceTypeDef":
        """
        [Client.create_public_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.create_public_virtual_interface)
        """

    def create_transit_virtual_interface(
        self, connectionId: str, newTransitVirtualInterface: NewTransitVirtualInterfaceTypeDef
    ) -> CreateTransitVirtualInterfaceResultTypeDef:
        """
        [Client.create_transit_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.create_transit_virtual_interface)
        """

    def delete_bgp_peer(
        self,
        virtualInterfaceId: str = None,
        asn: int = None,
        customerAddress: str = None,
        bgpPeerId: str = None,
    ) -> DeleteBGPPeerResponseTypeDef:
        """
        [Client.delete_bgp_peer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.delete_bgp_peer)
        """

    def delete_connection(self, connectionId: str) -> "ConnectionTypeDef":
        """
        [Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.delete_connection)
        """

    def delete_direct_connect_gateway(
        self, directConnectGatewayId: str
    ) -> DeleteDirectConnectGatewayResultTypeDef:
        """
        [Client.delete_direct_connect_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.delete_direct_connect_gateway)
        """

    def delete_direct_connect_gateway_association(
        self,
        associationId: str = None,
        directConnectGatewayId: str = None,
        virtualGatewayId: str = None,
    ) -> DeleteDirectConnectGatewayAssociationResultTypeDef:
        """
        [Client.delete_direct_connect_gateway_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.delete_direct_connect_gateway_association)
        """

    def delete_direct_connect_gateway_association_proposal(
        self, proposalId: str
    ) -> DeleteDirectConnectGatewayAssociationProposalResultTypeDef:
        """
        [Client.delete_direct_connect_gateway_association_proposal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.delete_direct_connect_gateway_association_proposal)
        """

    def delete_interconnect(self, interconnectId: str) -> DeleteInterconnectResponseTypeDef:
        """
        [Client.delete_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.delete_interconnect)
        """

    def delete_lag(self, lagId: str) -> "LagTypeDef":
        """
        [Client.delete_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.delete_lag)
        """

    def delete_virtual_interface(
        self, virtualInterfaceId: str
    ) -> DeleteVirtualInterfaceResponseTypeDef:
        """
        [Client.delete_virtual_interface documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.delete_virtual_interface)
        """

    def describe_connection_loa(
        self,
        connectionId: str,
        providerName: str = None,
        loaContentType: Literal["application/pdf"] = None,
    ) -> DescribeConnectionLoaResponseTypeDef:
        """
        [Client.describe_connection_loa documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_connection_loa)
        """

    def describe_connections(self, connectionId: str = None) -> ConnectionsTypeDef:
        """
        [Client.describe_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_connections)
        """

    def describe_connections_on_interconnect(self, interconnectId: str) -> ConnectionsTypeDef:
        """
        [Client.describe_connections_on_interconnect documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_connections_on_interconnect)
        """

    def describe_direct_connect_gateway_association_proposals(
        self,
        directConnectGatewayId: str = None,
        proposalId: str = None,
        associatedGatewayId: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeDirectConnectGatewayAssociationProposalsResultTypeDef:
        """
        [Client.describe_direct_connect_gateway_association_proposals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateway_association_proposals)
        """

    def describe_direct_connect_gateway_associations(
        self,
        associationId: str = None,
        associatedGatewayId: str = None,
        directConnectGatewayId: str = None,
        maxResults: int = None,
        nextToken: str = None,
        virtualGatewayId: str = None,
    ) -> DescribeDirectConnectGatewayAssociationsResultTypeDef:
        """
        [Client.describe_direct_connect_gateway_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateway_associations)
        """

    def describe_direct_connect_gateway_attachments(
        self,
        directConnectGatewayId: str = None,
        virtualInterfaceId: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeDirectConnectGatewayAttachmentsResultTypeDef:
        """
        [Client.describe_direct_connect_gateway_attachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateway_attachments)
        """

    def describe_direct_connect_gateways(
        self, directConnectGatewayId: str = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeDirectConnectGatewaysResultTypeDef:
        """
        [Client.describe_direct_connect_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_direct_connect_gateways)
        """

    def describe_hosted_connections(self, connectionId: str) -> ConnectionsTypeDef:
        """
        [Client.describe_hosted_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_hosted_connections)
        """

    def describe_interconnect_loa(
        self,
        interconnectId: str,
        providerName: str = None,
        loaContentType: Literal["application/pdf"] = None,
    ) -> DescribeInterconnectLoaResponseTypeDef:
        """
        [Client.describe_interconnect_loa documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_interconnect_loa)
        """

    def describe_interconnects(self, interconnectId: str = None) -> InterconnectsTypeDef:
        """
        [Client.describe_interconnects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_interconnects)
        """

    def describe_lags(self, lagId: str = None) -> LagsTypeDef:
        """
        [Client.describe_lags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_lags)
        """

    def describe_loa(
        self,
        connectionId: str,
        providerName: str = None,
        loaContentType: Literal["application/pdf"] = None,
    ) -> "LoaTypeDef":
        """
        [Client.describe_loa documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_loa)
        """

    def describe_locations(self) -> LocationsTypeDef:
        """
        [Client.describe_locations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_locations)
        """

    def describe_tags(self, resourceArns: List[str]) -> DescribeTagsResponseTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_tags)
        """

    def describe_virtual_gateways(self) -> VirtualGatewaysTypeDef:
        """
        [Client.describe_virtual_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_virtual_gateways)
        """

    def describe_virtual_interfaces(
        self, connectionId: str = None, virtualInterfaceId: str = None
    ) -> VirtualInterfacesTypeDef:
        """
        [Client.describe_virtual_interfaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.describe_virtual_interfaces)
        """

    def disassociate_connection_from_lag(
        self, connectionId: str, lagId: str
    ) -> "ConnectionTypeDef":
        """
        [Client.disassociate_connection_from_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.disassociate_connection_from_lag)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.generate_presigned_url)
        """

    def list_virtual_interface_test_history(
        self,
        testId: str = None,
        virtualInterfaceId: str = None,
        bgpPeers: List[str] = None,
        status: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListVirtualInterfaceTestHistoryResponseTypeDef:
        """
        [Client.list_virtual_interface_test_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.list_virtual_interface_test_history)
        """

    def start_bgp_failover_test(
        self, virtualInterfaceId: str, bgpPeers: List[str] = None, testDurationInMinutes: int = None
    ) -> StartBgpFailoverTestResponseTypeDef:
        """
        [Client.start_bgp_failover_test documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.start_bgp_failover_test)
        """

    def stop_bgp_failover_test(self, virtualInterfaceId: str) -> StopBgpFailoverTestResponseTypeDef:
        """
        [Client.stop_bgp_failover_test documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.stop_bgp_failover_test)
        """

    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.untag_resource)
        """

    def update_direct_connect_gateway_association(
        self,
        associationId: str = None,
        addAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None,
        removeAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"] = None,
    ) -> UpdateDirectConnectGatewayAssociationResultTypeDef:
        """
        [Client.update_direct_connect_gateway_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.update_direct_connect_gateway_association)
        """

    def update_lag(self, lagId: str, lagName: str = None, minimumLinks: int = None) -> "LagTypeDef":
        """
        [Client.update_lag documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.update_lag)
        """

    def update_virtual_interface_attributes(
        self, virtualInterfaceId: str, mtu: int = None
    ) -> "VirtualInterfaceTypeDef":
        """
        [Client.update_virtual_interface_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Client.update_virtual_interface_attributes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_direct_connect_gateway_associations"]
    ) -> DescribeDirectConnectGatewayAssociationsPaginator:
        """
        [Paginator.DescribeDirectConnectGatewayAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_direct_connect_gateway_attachments"]
    ) -> DescribeDirectConnectGatewayAttachmentsPaginator:
        """
        [Paginator.DescribeDirectConnectGatewayAttachments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGatewayAttachments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_direct_connect_gateways"]
    ) -> DescribeDirectConnectGatewaysPaginator:
        """
        [Paginator.DescribeDirectConnectGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/directconnect.html#DirectConnect.Paginator.DescribeDirectConnectGateways)
        """
