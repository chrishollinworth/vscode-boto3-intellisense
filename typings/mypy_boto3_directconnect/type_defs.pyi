"""
Type annotations for directconnect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_directconnect.type_defs import AcceptDirectConnectGatewayAssociationProposalRequestRequestTypeDef

    data: AcceptDirectConnectGatewayAssociationProposalRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AddressFamilyType,
    BGPPeerStateType,
    BGPStatusType,
    ConnectionStateType,
    DirectConnectGatewayAssociationProposalStateType,
    DirectConnectGatewayAssociationStateType,
    DirectConnectGatewayAttachmentStateType,
    DirectConnectGatewayAttachmentTypeType,
    DirectConnectGatewayStateType,
    GatewayTypeType,
    HasLogicalRedundancyType,
    InterconnectStateType,
    LagStateType,
    VirtualInterfaceStateType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptDirectConnectGatewayAssociationProposalRequestRequestTypeDef",
    "AcceptDirectConnectGatewayAssociationProposalResultTypeDef",
    "AllocateConnectionOnInterconnectRequestRequestTypeDef",
    "AllocateHostedConnectionRequestRequestTypeDef",
    "AllocatePrivateVirtualInterfaceRequestRequestTypeDef",
    "AllocatePublicVirtualInterfaceRequestRequestTypeDef",
    "AllocateTransitVirtualInterfaceRequestRequestTypeDef",
    "AllocateTransitVirtualInterfaceResultTypeDef",
    "AssociateConnectionWithLagRequestRequestTypeDef",
    "AssociateHostedConnectionRequestRequestTypeDef",
    "AssociateMacSecKeyRequestRequestTypeDef",
    "AssociateMacSecKeyResponseTypeDef",
    "AssociateVirtualInterfaceRequestRequestTypeDef",
    "AssociatedGatewayTypeDef",
    "BGPPeerTypeDef",
    "ConfirmConnectionRequestRequestTypeDef",
    "ConfirmConnectionResponseTypeDef",
    "ConfirmPrivateVirtualInterfaceRequestRequestTypeDef",
    "ConfirmPrivateVirtualInterfaceResponseTypeDef",
    "ConfirmPublicVirtualInterfaceRequestRequestTypeDef",
    "ConfirmPublicVirtualInterfaceResponseTypeDef",
    "ConfirmTransitVirtualInterfaceRequestRequestTypeDef",
    "ConfirmTransitVirtualInterfaceResponseTypeDef",
    "ConnectionResponseMetadataTypeDef",
    "ConnectionTypeDef",
    "ConnectionsTypeDef",
    "CreateBGPPeerRequestRequestTypeDef",
    "CreateBGPPeerResponseTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "CreateDirectConnectGatewayAssociationProposalRequestRequestTypeDef",
    "CreateDirectConnectGatewayAssociationProposalResultTypeDef",
    "CreateDirectConnectGatewayAssociationRequestRequestTypeDef",
    "CreateDirectConnectGatewayAssociationResultTypeDef",
    "CreateDirectConnectGatewayRequestRequestTypeDef",
    "CreateDirectConnectGatewayResultTypeDef",
    "CreateInterconnectRequestRequestTypeDef",
    "CreateLagRequestRequestTypeDef",
    "CreatePrivateVirtualInterfaceRequestRequestTypeDef",
    "CreatePublicVirtualInterfaceRequestRequestTypeDef",
    "CreateTransitVirtualInterfaceRequestRequestTypeDef",
    "CreateTransitVirtualInterfaceResultTypeDef",
    "DeleteBGPPeerRequestRequestTypeDef",
    "DeleteBGPPeerResponseTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteDirectConnectGatewayAssociationProposalRequestRequestTypeDef",
    "DeleteDirectConnectGatewayAssociationProposalResultTypeDef",
    "DeleteDirectConnectGatewayAssociationRequestRequestTypeDef",
    "DeleteDirectConnectGatewayAssociationResultTypeDef",
    "DeleteDirectConnectGatewayRequestRequestTypeDef",
    "DeleteDirectConnectGatewayResultTypeDef",
    "DeleteInterconnectRequestRequestTypeDef",
    "DeleteInterconnectResponseTypeDef",
    "DeleteLagRequestRequestTypeDef",
    "DeleteVirtualInterfaceRequestRequestTypeDef",
    "DeleteVirtualInterfaceResponseTypeDef",
    "DescribeConnectionLoaRequestRequestTypeDef",
    "DescribeConnectionLoaResponseTypeDef",
    "DescribeConnectionsOnInterconnectRequestRequestTypeDef",
    "DescribeConnectionsRequestRequestTypeDef",
    "DescribeDirectConnectGatewayAssociationProposalsRequestRequestTypeDef",
    "DescribeDirectConnectGatewayAssociationProposalsResultTypeDef",
    "DescribeDirectConnectGatewayAssociationsRequestRequestTypeDef",
    "DescribeDirectConnectGatewayAssociationsResultTypeDef",
    "DescribeDirectConnectGatewayAttachmentsRequestRequestTypeDef",
    "DescribeDirectConnectGatewayAttachmentsResultTypeDef",
    "DescribeDirectConnectGatewaysRequestRequestTypeDef",
    "DescribeDirectConnectGatewaysResultTypeDef",
    "DescribeHostedConnectionsRequestRequestTypeDef",
    "DescribeInterconnectLoaRequestRequestTypeDef",
    "DescribeInterconnectLoaResponseTypeDef",
    "DescribeInterconnectsRequestRequestTypeDef",
    "DescribeLagsRequestRequestTypeDef",
    "DescribeLoaRequestRequestTypeDef",
    "DescribeTagsRequestRequestTypeDef",
    "DescribeTagsResponseTypeDef",
    "DescribeVirtualInterfacesRequestRequestTypeDef",
    "DirectConnectGatewayAssociationProposalTypeDef",
    "DirectConnectGatewayAssociationTypeDef",
    "DirectConnectGatewayAttachmentTypeDef",
    "DirectConnectGatewayTypeDef",
    "DisassociateConnectionFromLagRequestRequestTypeDef",
    "DisassociateMacSecKeyRequestRequestTypeDef",
    "DisassociateMacSecKeyResponseTypeDef",
    "InterconnectResponseMetadataTypeDef",
    "InterconnectTypeDef",
    "InterconnectsTypeDef",
    "LagResponseMetadataTypeDef",
    "LagTypeDef",
    "LagsTypeDef",
    "ListVirtualInterfaceTestHistoryRequestRequestTypeDef",
    "ListVirtualInterfaceTestHistoryResponseTypeDef",
    "LoaResponseMetadataTypeDef",
    "LoaTypeDef",
    "LocationTypeDef",
    "LocationsTypeDef",
    "MacSecKeyTypeDef",
    "NewBGPPeerTypeDef",
    "NewPrivateVirtualInterfaceAllocationTypeDef",
    "NewPrivateVirtualInterfaceTypeDef",
    "NewPublicVirtualInterfaceAllocationTypeDef",
    "NewPublicVirtualInterfaceTypeDef",
    "NewTransitVirtualInterfaceAllocationTypeDef",
    "NewTransitVirtualInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "RouteFilterPrefixTypeDef",
    "StartBgpFailoverTestRequestRequestTypeDef",
    "StartBgpFailoverTestResponseTypeDef",
    "StopBgpFailoverTestRequestRequestTypeDef",
    "StopBgpFailoverTestResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConnectionRequestRequestTypeDef",
    "UpdateDirectConnectGatewayAssociationRequestRequestTypeDef",
    "UpdateDirectConnectGatewayAssociationResultTypeDef",
    "UpdateLagRequestRequestTypeDef",
    "UpdateVirtualInterfaceAttributesRequestRequestTypeDef",
    "VirtualGatewayTypeDef",
    "VirtualGatewaysTypeDef",
    "VirtualInterfaceResponseMetadataTypeDef",
    "VirtualInterfaceTestHistoryTypeDef",
    "VirtualInterfaceTypeDef",
    "VirtualInterfacesTypeDef",
)

_RequiredAcceptDirectConnectGatewayAssociationProposalRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptDirectConnectGatewayAssociationProposalRequestRequestTypeDef",
    {
        "directConnectGatewayId": str,
        "proposalId": str,
        "associatedGatewayOwnerAccount": str,
    },
)
_OptionalAcceptDirectConnectGatewayAssociationProposalRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptDirectConnectGatewayAssociationProposalRequestRequestTypeDef",
    {
        "overrideAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
    },
    total=False,
)

class AcceptDirectConnectGatewayAssociationProposalRequestRequestTypeDef(
    _RequiredAcceptDirectConnectGatewayAssociationProposalRequestRequestTypeDef,
    _OptionalAcceptDirectConnectGatewayAssociationProposalRequestRequestTypeDef,
):
    pass

AcceptDirectConnectGatewayAssociationProposalResultTypeDef = TypedDict(
    "AcceptDirectConnectGatewayAssociationProposalResultTypeDef",
    {
        "directConnectGatewayAssociation": "DirectConnectGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AllocateConnectionOnInterconnectRequestRequestTypeDef = TypedDict(
    "AllocateConnectionOnInterconnectRequestRequestTypeDef",
    {
        "bandwidth": str,
        "connectionName": str,
        "ownerAccount": str,
        "interconnectId": str,
        "vlan": int,
    },
)

_RequiredAllocateHostedConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredAllocateHostedConnectionRequestRequestTypeDef",
    {
        "connectionId": str,
        "ownerAccount": str,
        "bandwidth": str,
        "connectionName": str,
        "vlan": int,
    },
)
_OptionalAllocateHostedConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalAllocateHostedConnectionRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class AllocateHostedConnectionRequestRequestTypeDef(
    _RequiredAllocateHostedConnectionRequestRequestTypeDef,
    _OptionalAllocateHostedConnectionRequestRequestTypeDef,
):
    pass

AllocatePrivateVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "AllocatePrivateVirtualInterfaceRequestRequestTypeDef",
    {
        "connectionId": str,
        "ownerAccount": str,
        "newPrivateVirtualInterfaceAllocation": "NewPrivateVirtualInterfaceAllocationTypeDef",
    },
)

AllocatePublicVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "AllocatePublicVirtualInterfaceRequestRequestTypeDef",
    {
        "connectionId": str,
        "ownerAccount": str,
        "newPublicVirtualInterfaceAllocation": "NewPublicVirtualInterfaceAllocationTypeDef",
    },
)

AllocateTransitVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "AllocateTransitVirtualInterfaceRequestRequestTypeDef",
    {
        "connectionId": str,
        "ownerAccount": str,
        "newTransitVirtualInterfaceAllocation": "NewTransitVirtualInterfaceAllocationTypeDef",
    },
)

AllocateTransitVirtualInterfaceResultTypeDef = TypedDict(
    "AllocateTransitVirtualInterfaceResultTypeDef",
    {
        "virtualInterface": "VirtualInterfaceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateConnectionWithLagRequestRequestTypeDef = TypedDict(
    "AssociateConnectionWithLagRequestRequestTypeDef",
    {
        "connectionId": str,
        "lagId": str,
    },
)

AssociateHostedConnectionRequestRequestTypeDef = TypedDict(
    "AssociateHostedConnectionRequestRequestTypeDef",
    {
        "connectionId": str,
        "parentConnectionId": str,
    },
)

_RequiredAssociateMacSecKeyRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateMacSecKeyRequestRequestTypeDef",
    {
        "connectionId": str,
    },
)
_OptionalAssociateMacSecKeyRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateMacSecKeyRequestRequestTypeDef",
    {
        "secretARN": str,
        "ckn": str,
        "cak": str,
    },
    total=False,
)

class AssociateMacSecKeyRequestRequestTypeDef(
    _RequiredAssociateMacSecKeyRequestRequestTypeDef,
    _OptionalAssociateMacSecKeyRequestRequestTypeDef,
):
    pass

AssociateMacSecKeyResponseTypeDef = TypedDict(
    "AssociateMacSecKeyResponseTypeDef",
    {
        "connectionId": str,
        "macSecKeys": List["MacSecKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "AssociateVirtualInterfaceRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
        "connectionId": str,
    },
)

AssociatedGatewayTypeDef = TypedDict(
    "AssociatedGatewayTypeDef",
    {
        "id": str,
        "type": GatewayTypeType,
        "ownerAccount": str,
        "region": str,
    },
    total=False,
)

BGPPeerTypeDef = TypedDict(
    "BGPPeerTypeDef",
    {
        "bgpPeerId": str,
        "asn": int,
        "authKey": str,
        "addressFamily": AddressFamilyType,
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": BGPPeerStateType,
        "bgpStatus": BGPStatusType,
        "awsDeviceV2": str,
        "awsLogicalDeviceId": str,
    },
    total=False,
)

ConfirmConnectionRequestRequestTypeDef = TypedDict(
    "ConfirmConnectionRequestRequestTypeDef",
    {
        "connectionId": str,
    },
)

ConfirmConnectionResponseTypeDef = TypedDict(
    "ConfirmConnectionResponseTypeDef",
    {
        "connectionState": ConnectionStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredConfirmPrivateVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "_RequiredConfirmPrivateVirtualInterfaceRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
    },
)
_OptionalConfirmPrivateVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "_OptionalConfirmPrivateVirtualInterfaceRequestRequestTypeDef",
    {
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
    },
    total=False,
)

class ConfirmPrivateVirtualInterfaceRequestRequestTypeDef(
    _RequiredConfirmPrivateVirtualInterfaceRequestRequestTypeDef,
    _OptionalConfirmPrivateVirtualInterfaceRequestRequestTypeDef,
):
    pass

ConfirmPrivateVirtualInterfaceResponseTypeDef = TypedDict(
    "ConfirmPrivateVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": VirtualInterfaceStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfirmPublicVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "ConfirmPublicVirtualInterfaceRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
    },
)

ConfirmPublicVirtualInterfaceResponseTypeDef = TypedDict(
    "ConfirmPublicVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": VirtualInterfaceStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfirmTransitVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "ConfirmTransitVirtualInterfaceRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
        "directConnectGatewayId": str,
    },
)

ConfirmTransitVirtualInterfaceResponseTypeDef = TypedDict(
    "ConfirmTransitVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": VirtualInterfaceStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConnectionResponseMetadataTypeDef = TypedDict(
    "ConnectionResponseMetadataTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": ConnectionStateType,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "awsLogicalDeviceId": str,
        "hasLogicalRedundancy": HasLogicalRedundancyType,
        "tags": List["TagTypeDef"],
        "providerName": str,
        "macSecCapable": bool,
        "portEncryptionStatus": str,
        "encryptionMode": str,
        "macSecKeys": List["MacSecKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": ConnectionStateType,
        "region": str,
        "location": str,
        "bandwidth": str,
        "vlan": int,
        "partnerName": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "awsLogicalDeviceId": str,
        "hasLogicalRedundancy": HasLogicalRedundancyType,
        "tags": List["TagTypeDef"],
        "providerName": str,
        "macSecCapable": bool,
        "portEncryptionStatus": str,
        "encryptionMode": str,
        "macSecKeys": List["MacSecKeyTypeDef"],
    },
    total=False,
)

ConnectionsTypeDef = TypedDict(
    "ConnectionsTypeDef",
    {
        "connections": List["ConnectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBGPPeerRequestRequestTypeDef = TypedDict(
    "CreateBGPPeerRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
        "newBGPPeer": "NewBGPPeerTypeDef",
    },
    total=False,
)

CreateBGPPeerResponseTypeDef = TypedDict(
    "CreateBGPPeerResponseTypeDef",
    {
        "virtualInterface": "VirtualInterfaceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionRequestRequestTypeDef",
    {
        "location": str,
        "bandwidth": str,
        "connectionName": str,
    },
)
_OptionalCreateConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionRequestRequestTypeDef",
    {
        "lagId": str,
        "tags": List["TagTypeDef"],
        "providerName": str,
        "requestMACSec": bool,
    },
    total=False,
)

class CreateConnectionRequestRequestTypeDef(
    _RequiredCreateConnectionRequestRequestTypeDef, _OptionalCreateConnectionRequestRequestTypeDef
):
    pass

_RequiredCreateDirectConnectGatewayAssociationProposalRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDirectConnectGatewayAssociationProposalRequestRequestTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "gatewayId": str,
    },
)
_OptionalCreateDirectConnectGatewayAssociationProposalRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDirectConnectGatewayAssociationProposalRequestRequestTypeDef",
    {
        "addAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
        "removeAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
    },
    total=False,
)

class CreateDirectConnectGatewayAssociationProposalRequestRequestTypeDef(
    _RequiredCreateDirectConnectGatewayAssociationProposalRequestRequestTypeDef,
    _OptionalCreateDirectConnectGatewayAssociationProposalRequestRequestTypeDef,
):
    pass

CreateDirectConnectGatewayAssociationProposalResultTypeDef = TypedDict(
    "CreateDirectConnectGatewayAssociationProposalResultTypeDef",
    {
        "directConnectGatewayAssociationProposal": "DirectConnectGatewayAssociationProposalTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDirectConnectGatewayAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDirectConnectGatewayAssociationRequestRequestTypeDef",
    {
        "directConnectGatewayId": str,
    },
)
_OptionalCreateDirectConnectGatewayAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDirectConnectGatewayAssociationRequestRequestTypeDef",
    {
        "gatewayId": str,
        "addAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
        "virtualGatewayId": str,
    },
    total=False,
)

class CreateDirectConnectGatewayAssociationRequestRequestTypeDef(
    _RequiredCreateDirectConnectGatewayAssociationRequestRequestTypeDef,
    _OptionalCreateDirectConnectGatewayAssociationRequestRequestTypeDef,
):
    pass

CreateDirectConnectGatewayAssociationResultTypeDef = TypedDict(
    "CreateDirectConnectGatewayAssociationResultTypeDef",
    {
        "directConnectGatewayAssociation": "DirectConnectGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDirectConnectGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDirectConnectGatewayRequestRequestTypeDef",
    {
        "directConnectGatewayName": str,
    },
)
_OptionalCreateDirectConnectGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDirectConnectGatewayRequestRequestTypeDef",
    {
        "amazonSideAsn": int,
    },
    total=False,
)

class CreateDirectConnectGatewayRequestRequestTypeDef(
    _RequiredCreateDirectConnectGatewayRequestRequestTypeDef,
    _OptionalCreateDirectConnectGatewayRequestRequestTypeDef,
):
    pass

CreateDirectConnectGatewayResultTypeDef = TypedDict(
    "CreateDirectConnectGatewayResultTypeDef",
    {
        "directConnectGateway": "DirectConnectGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInterconnectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInterconnectRequestRequestTypeDef",
    {
        "interconnectName": str,
        "bandwidth": str,
        "location": str,
    },
)
_OptionalCreateInterconnectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInterconnectRequestRequestTypeDef",
    {
        "lagId": str,
        "tags": List["TagTypeDef"],
        "providerName": str,
    },
    total=False,
)

class CreateInterconnectRequestRequestTypeDef(
    _RequiredCreateInterconnectRequestRequestTypeDef,
    _OptionalCreateInterconnectRequestRequestTypeDef,
):
    pass

_RequiredCreateLagRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLagRequestRequestTypeDef",
    {
        "numberOfConnections": int,
        "location": str,
        "connectionsBandwidth": str,
        "lagName": str,
    },
)
_OptionalCreateLagRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLagRequestRequestTypeDef",
    {
        "connectionId": str,
        "tags": List["TagTypeDef"],
        "childConnectionTags": List["TagTypeDef"],
        "providerName": str,
        "requestMACSec": bool,
    },
    total=False,
)

class CreateLagRequestRequestTypeDef(
    _RequiredCreateLagRequestRequestTypeDef, _OptionalCreateLagRequestRequestTypeDef
):
    pass

CreatePrivateVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "CreatePrivateVirtualInterfaceRequestRequestTypeDef",
    {
        "connectionId": str,
        "newPrivateVirtualInterface": "NewPrivateVirtualInterfaceTypeDef",
    },
)

CreatePublicVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "CreatePublicVirtualInterfaceRequestRequestTypeDef",
    {
        "connectionId": str,
        "newPublicVirtualInterface": "NewPublicVirtualInterfaceTypeDef",
    },
)

CreateTransitVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "CreateTransitVirtualInterfaceRequestRequestTypeDef",
    {
        "connectionId": str,
        "newTransitVirtualInterface": "NewTransitVirtualInterfaceTypeDef",
    },
)

CreateTransitVirtualInterfaceResultTypeDef = TypedDict(
    "CreateTransitVirtualInterfaceResultTypeDef",
    {
        "virtualInterface": "VirtualInterfaceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBGPPeerRequestRequestTypeDef = TypedDict(
    "DeleteBGPPeerRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
        "asn": int,
        "customerAddress": str,
        "bgpPeerId": str,
    },
    total=False,
)

DeleteBGPPeerResponseTypeDef = TypedDict(
    "DeleteBGPPeerResponseTypeDef",
    {
        "virtualInterface": "VirtualInterfaceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "connectionId": str,
    },
)

DeleteDirectConnectGatewayAssociationProposalRequestRequestTypeDef = TypedDict(
    "DeleteDirectConnectGatewayAssociationProposalRequestRequestTypeDef",
    {
        "proposalId": str,
    },
)

DeleteDirectConnectGatewayAssociationProposalResultTypeDef = TypedDict(
    "DeleteDirectConnectGatewayAssociationProposalResultTypeDef",
    {
        "directConnectGatewayAssociationProposal": "DirectConnectGatewayAssociationProposalTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDirectConnectGatewayAssociationRequestRequestTypeDef = TypedDict(
    "DeleteDirectConnectGatewayAssociationRequestRequestTypeDef",
    {
        "associationId": str,
        "directConnectGatewayId": str,
        "virtualGatewayId": str,
    },
    total=False,
)

DeleteDirectConnectGatewayAssociationResultTypeDef = TypedDict(
    "DeleteDirectConnectGatewayAssociationResultTypeDef",
    {
        "directConnectGatewayAssociation": "DirectConnectGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDirectConnectGatewayRequestRequestTypeDef = TypedDict(
    "DeleteDirectConnectGatewayRequestRequestTypeDef",
    {
        "directConnectGatewayId": str,
    },
)

DeleteDirectConnectGatewayResultTypeDef = TypedDict(
    "DeleteDirectConnectGatewayResultTypeDef",
    {
        "directConnectGateway": "DirectConnectGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInterconnectRequestRequestTypeDef = TypedDict(
    "DeleteInterconnectRequestRequestTypeDef",
    {
        "interconnectId": str,
    },
)

DeleteInterconnectResponseTypeDef = TypedDict(
    "DeleteInterconnectResponseTypeDef",
    {
        "interconnectState": InterconnectStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLagRequestRequestTypeDef = TypedDict(
    "DeleteLagRequestRequestTypeDef",
    {
        "lagId": str,
    },
)

DeleteVirtualInterfaceRequestRequestTypeDef = TypedDict(
    "DeleteVirtualInterfaceRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
    },
)

DeleteVirtualInterfaceResponseTypeDef = TypedDict(
    "DeleteVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": VirtualInterfaceStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeConnectionLoaRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeConnectionLoaRequestRequestTypeDef",
    {
        "connectionId": str,
    },
)
_OptionalDescribeConnectionLoaRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeConnectionLoaRequestRequestTypeDef",
    {
        "providerName": str,
        "loaContentType": Literal["application/pdf"],
    },
    total=False,
)

class DescribeConnectionLoaRequestRequestTypeDef(
    _RequiredDescribeConnectionLoaRequestRequestTypeDef,
    _OptionalDescribeConnectionLoaRequestRequestTypeDef,
):
    pass

DescribeConnectionLoaResponseTypeDef = TypedDict(
    "DescribeConnectionLoaResponseTypeDef",
    {
        "loa": "LoaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectionsOnInterconnectRequestRequestTypeDef = TypedDict(
    "DescribeConnectionsOnInterconnectRequestRequestTypeDef",
    {
        "interconnectId": str,
    },
)

DescribeConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeConnectionsRequestRequestTypeDef",
    {
        "connectionId": str,
    },
    total=False,
)

DescribeDirectConnectGatewayAssociationProposalsRequestRequestTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationProposalsRequestRequestTypeDef",
    {
        "directConnectGatewayId": str,
        "proposalId": str,
        "associatedGatewayId": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeDirectConnectGatewayAssociationProposalsResultTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationProposalsResultTypeDef",
    {
        "directConnectGatewayAssociationProposals": List[
            "DirectConnectGatewayAssociationProposalTypeDef"
        ],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDirectConnectGatewayAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationsRequestRequestTypeDef",
    {
        "associationId": str,
        "associatedGatewayId": str,
        "directConnectGatewayId": str,
        "maxResults": int,
        "nextToken": str,
        "virtualGatewayId": str,
    },
    total=False,
)

DescribeDirectConnectGatewayAssociationsResultTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationsResultTypeDef",
    {
        "directConnectGatewayAssociations": List["DirectConnectGatewayAssociationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDirectConnectGatewayAttachmentsRequestRequestTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAttachmentsRequestRequestTypeDef",
    {
        "directConnectGatewayId": str,
        "virtualInterfaceId": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeDirectConnectGatewayAttachmentsResultTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAttachmentsResultTypeDef",
    {
        "directConnectGatewayAttachments": List["DirectConnectGatewayAttachmentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDirectConnectGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeDirectConnectGatewaysRequestRequestTypeDef",
    {
        "directConnectGatewayId": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeDirectConnectGatewaysResultTypeDef = TypedDict(
    "DescribeDirectConnectGatewaysResultTypeDef",
    {
        "directConnectGateways": List["DirectConnectGatewayTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHostedConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeHostedConnectionsRequestRequestTypeDef",
    {
        "connectionId": str,
    },
)

_RequiredDescribeInterconnectLoaRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeInterconnectLoaRequestRequestTypeDef",
    {
        "interconnectId": str,
    },
)
_OptionalDescribeInterconnectLoaRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeInterconnectLoaRequestRequestTypeDef",
    {
        "providerName": str,
        "loaContentType": Literal["application/pdf"],
    },
    total=False,
)

class DescribeInterconnectLoaRequestRequestTypeDef(
    _RequiredDescribeInterconnectLoaRequestRequestTypeDef,
    _OptionalDescribeInterconnectLoaRequestRequestTypeDef,
):
    pass

DescribeInterconnectLoaResponseTypeDef = TypedDict(
    "DescribeInterconnectLoaResponseTypeDef",
    {
        "loa": "LoaTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInterconnectsRequestRequestTypeDef = TypedDict(
    "DescribeInterconnectsRequestRequestTypeDef",
    {
        "interconnectId": str,
    },
    total=False,
)

DescribeLagsRequestRequestTypeDef = TypedDict(
    "DescribeLagsRequestRequestTypeDef",
    {
        "lagId": str,
    },
    total=False,
)

_RequiredDescribeLoaRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeLoaRequestRequestTypeDef",
    {
        "connectionId": str,
    },
)
_OptionalDescribeLoaRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeLoaRequestRequestTypeDef",
    {
        "providerName": str,
        "loaContentType": Literal["application/pdf"],
    },
    total=False,
)

class DescribeLoaRequestRequestTypeDef(
    _RequiredDescribeLoaRequestRequestTypeDef, _OptionalDescribeLoaRequestRequestTypeDef
):
    pass

DescribeTagsRequestRequestTypeDef = TypedDict(
    "DescribeTagsRequestRequestTypeDef",
    {
        "resourceArns": List[str],
    },
)

DescribeTagsResponseTypeDef = TypedDict(
    "DescribeTagsResponseTypeDef",
    {
        "resourceTags": List["ResourceTagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVirtualInterfacesRequestRequestTypeDef = TypedDict(
    "DescribeVirtualInterfacesRequestRequestTypeDef",
    {
        "connectionId": str,
        "virtualInterfaceId": str,
    },
    total=False,
)

DirectConnectGatewayAssociationProposalTypeDef = TypedDict(
    "DirectConnectGatewayAssociationProposalTypeDef",
    {
        "proposalId": str,
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "proposalState": DirectConnectGatewayAssociationProposalStateType,
        "associatedGateway": "AssociatedGatewayTypeDef",
        "existingAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
        "requestedAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
    },
    total=False,
)

DirectConnectGatewayAssociationTypeDef = TypedDict(
    "DirectConnectGatewayAssociationTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "associationState": DirectConnectGatewayAssociationStateType,
        "stateChangeError": str,
        "associatedGateway": "AssociatedGatewayTypeDef",
        "associationId": str,
        "allowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
        "virtualGatewayId": str,
        "virtualGatewayRegion": str,
        "virtualGatewayOwnerAccount": str,
    },
    total=False,
)

DirectConnectGatewayAttachmentTypeDef = TypedDict(
    "DirectConnectGatewayAttachmentTypeDef",
    {
        "directConnectGatewayId": str,
        "virtualInterfaceId": str,
        "virtualInterfaceRegion": str,
        "virtualInterfaceOwnerAccount": str,
        "attachmentState": DirectConnectGatewayAttachmentStateType,
        "attachmentType": DirectConnectGatewayAttachmentTypeType,
        "stateChangeError": str,
    },
    total=False,
)

DirectConnectGatewayTypeDef = TypedDict(
    "DirectConnectGatewayTypeDef",
    {
        "directConnectGatewayId": str,
        "directConnectGatewayName": str,
        "amazonSideAsn": int,
        "ownerAccount": str,
        "directConnectGatewayState": DirectConnectGatewayStateType,
        "stateChangeError": str,
    },
    total=False,
)

DisassociateConnectionFromLagRequestRequestTypeDef = TypedDict(
    "DisassociateConnectionFromLagRequestRequestTypeDef",
    {
        "connectionId": str,
        "lagId": str,
    },
)

DisassociateMacSecKeyRequestRequestTypeDef = TypedDict(
    "DisassociateMacSecKeyRequestRequestTypeDef",
    {
        "connectionId": str,
        "secretARN": str,
    },
)

DisassociateMacSecKeyResponseTypeDef = TypedDict(
    "DisassociateMacSecKeyResponseTypeDef",
    {
        "connectionId": str,
        "macSecKeys": List["MacSecKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InterconnectResponseMetadataTypeDef = TypedDict(
    "InterconnectResponseMetadataTypeDef",
    {
        "interconnectId": str,
        "interconnectName": str,
        "interconnectState": InterconnectStateType,
        "region": str,
        "location": str,
        "bandwidth": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "awsLogicalDeviceId": str,
        "hasLogicalRedundancy": HasLogicalRedundancyType,
        "tags": List["TagTypeDef"],
        "providerName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InterconnectTypeDef = TypedDict(
    "InterconnectTypeDef",
    {
        "interconnectId": str,
        "interconnectName": str,
        "interconnectState": InterconnectStateType,
        "region": str,
        "location": str,
        "bandwidth": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "awsLogicalDeviceId": str,
        "hasLogicalRedundancy": HasLogicalRedundancyType,
        "tags": List["TagTypeDef"],
        "providerName": str,
    },
    total=False,
)

InterconnectsTypeDef = TypedDict(
    "InterconnectsTypeDef",
    {
        "interconnects": List["InterconnectTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LagResponseMetadataTypeDef = TypedDict(
    "LagResponseMetadataTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": LagStateType,
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "awsLogicalDeviceId": str,
        "connections": List["ConnectionTypeDef"],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": HasLogicalRedundancyType,
        "tags": List["TagTypeDef"],
        "providerName": str,
        "macSecCapable": bool,
        "encryptionMode": str,
        "macSecKeys": List["MacSecKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LagTypeDef = TypedDict(
    "LagTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": LagStateType,
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "awsLogicalDeviceId": str,
        "connections": List["ConnectionTypeDef"],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": HasLogicalRedundancyType,
        "tags": List["TagTypeDef"],
        "providerName": str,
        "macSecCapable": bool,
        "encryptionMode": str,
        "macSecKeys": List["MacSecKeyTypeDef"],
    },
    total=False,
)

LagsTypeDef = TypedDict(
    "LagsTypeDef",
    {
        "lags": List["LagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVirtualInterfaceTestHistoryRequestRequestTypeDef = TypedDict(
    "ListVirtualInterfaceTestHistoryRequestRequestTypeDef",
    {
        "testId": str,
        "virtualInterfaceId": str,
        "bgpPeers": List[str],
        "status": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListVirtualInterfaceTestHistoryResponseTypeDef = TypedDict(
    "ListVirtualInterfaceTestHistoryResponseTypeDef",
    {
        "virtualInterfaceTestHistory": List["VirtualInterfaceTestHistoryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoaResponseMetadataTypeDef = TypedDict(
    "LoaResponseMetadataTypeDef",
    {
        "loaContent": bytes,
        "loaContentType": Literal["application/pdf"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoaTypeDef = TypedDict(
    "LoaTypeDef",
    {
        "loaContent": bytes,
        "loaContentType": Literal["application/pdf"],
    },
    total=False,
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "locationCode": str,
        "locationName": str,
        "region": str,
        "availablePortSpeeds": List[str],
        "availableProviders": List[str],
        "availableMacSecPortSpeeds": List[str],
    },
    total=False,
)

LocationsTypeDef = TypedDict(
    "LocationsTypeDef",
    {
        "locations": List["LocationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MacSecKeyTypeDef = TypedDict(
    "MacSecKeyTypeDef",
    {
        "secretARN": str,
        "ckn": str,
        "state": str,
        "startOn": str,
    },
    total=False,
)

NewBGPPeerTypeDef = TypedDict(
    "NewBGPPeerTypeDef",
    {
        "asn": int,
        "authKey": str,
        "addressFamily": AddressFamilyType,
        "amazonAddress": str,
        "customerAddress": str,
    },
    total=False,
)

_RequiredNewPrivateVirtualInterfaceAllocationTypeDef = TypedDict(
    "_RequiredNewPrivateVirtualInterfaceAllocationTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
    },
)
_OptionalNewPrivateVirtualInterfaceAllocationTypeDef = TypedDict(
    "_OptionalNewPrivateVirtualInterfaceAllocationTypeDef",
    {
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "addressFamily": AddressFamilyType,
        "customerAddress": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class NewPrivateVirtualInterfaceAllocationTypeDef(
    _RequiredNewPrivateVirtualInterfaceAllocationTypeDef,
    _OptionalNewPrivateVirtualInterfaceAllocationTypeDef,
):
    pass

_RequiredNewPrivateVirtualInterfaceTypeDef = TypedDict(
    "_RequiredNewPrivateVirtualInterfaceTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
    },
)
_OptionalNewPrivateVirtualInterfaceTypeDef = TypedDict(
    "_OptionalNewPrivateVirtualInterfaceTypeDef",
    {
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": AddressFamilyType,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class NewPrivateVirtualInterfaceTypeDef(
    _RequiredNewPrivateVirtualInterfaceTypeDef, _OptionalNewPrivateVirtualInterfaceTypeDef
):
    pass

_RequiredNewPublicVirtualInterfaceAllocationTypeDef = TypedDict(
    "_RequiredNewPublicVirtualInterfaceAllocationTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
    },
)
_OptionalNewPublicVirtualInterfaceAllocationTypeDef = TypedDict(
    "_OptionalNewPublicVirtualInterfaceAllocationTypeDef",
    {
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": AddressFamilyType,
        "routeFilterPrefixes": List["RouteFilterPrefixTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class NewPublicVirtualInterfaceAllocationTypeDef(
    _RequiredNewPublicVirtualInterfaceAllocationTypeDef,
    _OptionalNewPublicVirtualInterfaceAllocationTypeDef,
):
    pass

_RequiredNewPublicVirtualInterfaceTypeDef = TypedDict(
    "_RequiredNewPublicVirtualInterfaceTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
    },
)
_OptionalNewPublicVirtualInterfaceTypeDef = TypedDict(
    "_OptionalNewPublicVirtualInterfaceTypeDef",
    {
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": AddressFamilyType,
        "routeFilterPrefixes": List["RouteFilterPrefixTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class NewPublicVirtualInterfaceTypeDef(
    _RequiredNewPublicVirtualInterfaceTypeDef, _OptionalNewPublicVirtualInterfaceTypeDef
):
    pass

NewTransitVirtualInterfaceAllocationTypeDef = TypedDict(
    "NewTransitVirtualInterfaceAllocationTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": AddressFamilyType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

NewTransitVirtualInterfaceTypeDef = TypedDict(
    "NewTransitVirtualInterfaceTypeDef",
    {
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": AddressFamilyType,
        "directConnectGatewayId": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RouteFilterPrefixTypeDef = TypedDict(
    "RouteFilterPrefixTypeDef",
    {
        "cidr": str,
    },
    total=False,
)

_RequiredStartBgpFailoverTestRequestRequestTypeDef = TypedDict(
    "_RequiredStartBgpFailoverTestRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
    },
)
_OptionalStartBgpFailoverTestRequestRequestTypeDef = TypedDict(
    "_OptionalStartBgpFailoverTestRequestRequestTypeDef",
    {
        "bgpPeers": List[str],
        "testDurationInMinutes": int,
    },
    total=False,
)

class StartBgpFailoverTestRequestRequestTypeDef(
    _RequiredStartBgpFailoverTestRequestRequestTypeDef,
    _OptionalStartBgpFailoverTestRequestRequestTypeDef,
):
    pass

StartBgpFailoverTestResponseTypeDef = TypedDict(
    "StartBgpFailoverTestResponseTypeDef",
    {
        "virtualInterfaceTest": "VirtualInterfaceTestHistoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBgpFailoverTestRequestRequestTypeDef = TypedDict(
    "StopBgpFailoverTestRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
    },
)

StopBgpFailoverTestResponseTypeDef = TypedDict(
    "StopBgpFailoverTestResponseTypeDef",
    {
        "virtualInterfaceTest": "VirtualInterfaceTestHistoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectionRequestRequestTypeDef",
    {
        "connectionId": str,
    },
)
_OptionalUpdateConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectionRequestRequestTypeDef",
    {
        "connectionName": str,
        "encryptionMode": str,
    },
    total=False,
)

class UpdateConnectionRequestRequestTypeDef(
    _RequiredUpdateConnectionRequestRequestTypeDef, _OptionalUpdateConnectionRequestRequestTypeDef
):
    pass

UpdateDirectConnectGatewayAssociationRequestRequestTypeDef = TypedDict(
    "UpdateDirectConnectGatewayAssociationRequestRequestTypeDef",
    {
        "associationId": str,
        "addAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
        "removeAllowedPrefixesToDirectConnectGateway": List["RouteFilterPrefixTypeDef"],
    },
    total=False,
)

UpdateDirectConnectGatewayAssociationResultTypeDef = TypedDict(
    "UpdateDirectConnectGatewayAssociationResultTypeDef",
    {
        "directConnectGatewayAssociation": "DirectConnectGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateLagRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLagRequestRequestTypeDef",
    {
        "lagId": str,
    },
)
_OptionalUpdateLagRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLagRequestRequestTypeDef",
    {
        "lagName": str,
        "minimumLinks": int,
        "encryptionMode": str,
    },
    total=False,
)

class UpdateLagRequestRequestTypeDef(
    _RequiredUpdateLagRequestRequestTypeDef, _OptionalUpdateLagRequestRequestTypeDef
):
    pass

_RequiredUpdateVirtualInterfaceAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVirtualInterfaceAttributesRequestRequestTypeDef",
    {
        "virtualInterfaceId": str,
    },
)
_OptionalUpdateVirtualInterfaceAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVirtualInterfaceAttributesRequestRequestTypeDef",
    {
        "mtu": int,
    },
    total=False,
)

class UpdateVirtualInterfaceAttributesRequestRequestTypeDef(
    _RequiredUpdateVirtualInterfaceAttributesRequestRequestTypeDef,
    _OptionalUpdateVirtualInterfaceAttributesRequestRequestTypeDef,
):
    pass

VirtualGatewayTypeDef = TypedDict(
    "VirtualGatewayTypeDef",
    {
        "virtualGatewayId": str,
        "virtualGatewayState": str,
    },
    total=False,
)

VirtualGatewaysTypeDef = TypedDict(
    "VirtualGatewaysTypeDef",
    {
        "virtualGateways": List["VirtualGatewayTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VirtualInterfaceResponseMetadataTypeDef = TypedDict(
    "VirtualInterfaceResponseMetadataTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": AddressFamilyType,
        "virtualInterfaceState": VirtualInterfaceStateType,
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List["RouteFilterPrefixTypeDef"],
        "bgpPeers": List["BGPPeerTypeDef"],
        "region": str,
        "awsDeviceV2": str,
        "awsLogicalDeviceId": str,
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VirtualInterfaceTestHistoryTypeDef = TypedDict(
    "VirtualInterfaceTestHistoryTypeDef",
    {
        "testId": str,
        "virtualInterfaceId": str,
        "bgpPeers": List[str],
        "status": str,
        "ownerAccount": str,
        "testDurationInMinutes": int,
        "startTime": datetime,
        "endTime": datetime,
    },
    total=False,
)

VirtualInterfaceTypeDef = TypedDict(
    "VirtualInterfaceTypeDef",
    {
        "ownerAccount": str,
        "virtualInterfaceId": str,
        "location": str,
        "connectionId": str,
        "virtualInterfaceType": str,
        "virtualInterfaceName": str,
        "vlan": int,
        "asn": int,
        "amazonSideAsn": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": AddressFamilyType,
        "virtualInterfaceState": VirtualInterfaceStateType,
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List["RouteFilterPrefixTypeDef"],
        "bgpPeers": List["BGPPeerTypeDef"],
        "region": str,
        "awsDeviceV2": str,
        "awsLogicalDeviceId": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

VirtualInterfacesTypeDef = TypedDict(
    "VirtualInterfacesTypeDef",
    {
        "virtualInterfaces": List["VirtualInterfaceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
