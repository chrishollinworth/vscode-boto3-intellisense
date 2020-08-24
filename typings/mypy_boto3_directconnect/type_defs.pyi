"""
Main interface for directconnect service type definitions.

Usage::

    ```python
    from mypy_boto3_directconnect.type_defs import AssociatedGatewayTypeDef

    data: AssociatedGatewayTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociatedGatewayTypeDef",
    "BGPPeerTypeDef",
    "ConnectionTypeDef",
    "DirectConnectGatewayAssociationProposalTypeDef",
    "DirectConnectGatewayAssociationTypeDef",
    "DirectConnectGatewayAttachmentTypeDef",
    "DirectConnectGatewayTypeDef",
    "InterconnectTypeDef",
    "LagTypeDef",
    "LoaTypeDef",
    "LocationTypeDef",
    "ResourceTagTypeDef",
    "RouteFilterPrefixTypeDef",
    "TagTypeDef",
    "VirtualGatewayTypeDef",
    "VirtualInterfaceTestHistoryTypeDef",
    "VirtualInterfaceTypeDef",
    "AcceptDirectConnectGatewayAssociationProposalResultTypeDef",
    "AllocateTransitVirtualInterfaceResultTypeDef",
    "ConfirmConnectionResponseTypeDef",
    "ConfirmPrivateVirtualInterfaceResponseTypeDef",
    "ConfirmPublicVirtualInterfaceResponseTypeDef",
    "ConfirmTransitVirtualInterfaceResponseTypeDef",
    "ConnectionsTypeDef",
    "CreateBGPPeerResponseTypeDef",
    "CreateDirectConnectGatewayAssociationProposalResultTypeDef",
    "CreateDirectConnectGatewayAssociationResultTypeDef",
    "CreateDirectConnectGatewayResultTypeDef",
    "CreateTransitVirtualInterfaceResultTypeDef",
    "DeleteBGPPeerResponseTypeDef",
    "DeleteDirectConnectGatewayAssociationProposalResultTypeDef",
    "DeleteDirectConnectGatewayAssociationResultTypeDef",
    "DeleteDirectConnectGatewayResultTypeDef",
    "DeleteInterconnectResponseTypeDef",
    "DeleteVirtualInterfaceResponseTypeDef",
    "DescribeConnectionLoaResponseTypeDef",
    "DescribeDirectConnectGatewayAssociationProposalsResultTypeDef",
    "DescribeDirectConnectGatewayAssociationsResultTypeDef",
    "DescribeDirectConnectGatewayAttachmentsResultTypeDef",
    "DescribeDirectConnectGatewaysResultTypeDef",
    "DescribeInterconnectLoaResponseTypeDef",
    "DescribeTagsResponseTypeDef",
    "InterconnectsTypeDef",
    "LagsTypeDef",
    "ListVirtualInterfaceTestHistoryResponseTypeDef",
    "LocationsTypeDef",
    "NewBGPPeerTypeDef",
    "NewPrivateVirtualInterfaceAllocationTypeDef",
    "NewPrivateVirtualInterfaceTypeDef",
    "NewPublicVirtualInterfaceAllocationTypeDef",
    "NewPublicVirtualInterfaceTypeDef",
    "NewTransitVirtualInterfaceAllocationTypeDef",
    "NewTransitVirtualInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "StartBgpFailoverTestResponseTypeDef",
    "StopBgpFailoverTestResponseTypeDef",
    "UpdateDirectConnectGatewayAssociationResultTypeDef",
    "VirtualGatewaysTypeDef",
    "VirtualInterfacesTypeDef",
)

AssociatedGatewayTypeDef = TypedDict(
    "AssociatedGatewayTypeDef",
    {
        "id": str,
        "type": Literal["virtualPrivateGateway", "transitGateway"],
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
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
        "bgpPeerState": Literal["verifying", "pending", "available", "deleting", "deleted"],
        "bgpStatus": Literal["up", "down", "unknown"],
        "awsDeviceV2": str,
    },
    total=False,
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ownerAccount": str,
        "connectionId": str,
        "connectionName": str,
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
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
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List["TagTypeDef"],
        "providerName": str,
    },
    total=False,
)

DirectConnectGatewayAssociationProposalTypeDef = TypedDict(
    "DirectConnectGatewayAssociationProposalTypeDef",
    {
        "proposalId": str,
        "directConnectGatewayId": str,
        "directConnectGatewayOwnerAccount": str,
        "proposalState": Literal["requested", "accepted", "deleted"],
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
        "associationState": Literal[
            "associating", "associated", "disassociating", "disassociated", "updating"
        ],
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
        "attachmentState": Literal["attaching", "attached", "detaching", "detached"],
        "attachmentType": Literal["TransitVirtualInterface", "PrivateVirtualInterface"],
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
        "directConnectGatewayState": Literal["pending", "available", "deleting", "deleted"],
        "stateChangeError": str,
    },
    total=False,
)

InterconnectTypeDef = TypedDict(
    "InterconnectTypeDef",
    {
        "interconnectId": str,
        "interconnectName": str,
        "interconnectState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ],
        "region": str,
        "location": str,
        "bandwidth": str,
        "loaIssueTime": datetime,
        "lagId": str,
        "awsDevice": str,
        "jumboFrameCapable": bool,
        "awsDeviceV2": str,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List["TagTypeDef"],
        "providerName": str,
    },
    total=False,
)

LagTypeDef = TypedDict(
    "LagTypeDef",
    {
        "connectionsBandwidth": str,
        "numberOfConnections": int,
        "lagId": str,
        "ownerAccount": str,
        "lagName": str,
        "lagState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ],
        "location": str,
        "region": str,
        "minimumLinks": int,
        "awsDevice": str,
        "awsDeviceV2": str,
        "connections": List["ConnectionTypeDef"],
        "allowsHostedConnections": bool,
        "jumboFrameCapable": bool,
        "hasLogicalRedundancy": Literal["unknown", "yes", "no"],
        "tags": List["TagTypeDef"],
        "providerName": str,
    },
    total=False,
)

LoaTypeDef = TypedDict(
    "LoaTypeDef", {"loaContent": bytes, "loaContentType": Literal["application/pdf"]}, total=False
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "locationCode": str,
        "locationName": str,
        "region": str,
        "availablePortSpeeds": List[str],
        "availableProviders": List[str],
    },
    total=False,
)

ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef", {"resourceArn": str, "tags": List["TagTypeDef"]}, total=False
)

RouteFilterPrefixTypeDef = TypedDict("RouteFilterPrefixTypeDef", {"cidr": str}, total=False)

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


VirtualGatewayTypeDef = TypedDict(
    "VirtualGatewayTypeDef", {"virtualGatewayId": str, "virtualGatewayState": str}, total=False
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
        "addressFamily": Literal["ipv4", "ipv6"],
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ],
        "customerRouterConfig": str,
        "mtu": int,
        "jumboFrameCapable": bool,
        "virtualGatewayId": str,
        "directConnectGatewayId": str,
        "routeFilterPrefixes": List["RouteFilterPrefixTypeDef"],
        "bgpPeers": List["BGPPeerTypeDef"],
        "region": str,
        "awsDeviceV2": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

AcceptDirectConnectGatewayAssociationProposalResultTypeDef = TypedDict(
    "AcceptDirectConnectGatewayAssociationProposalResultTypeDef",
    {"directConnectGatewayAssociation": "DirectConnectGatewayAssociationTypeDef"},
    total=False,
)

AllocateTransitVirtualInterfaceResultTypeDef = TypedDict(
    "AllocateTransitVirtualInterfaceResultTypeDef",
    {"virtualInterface": "VirtualInterfaceTypeDef"},
    total=False,
)

ConfirmConnectionResponseTypeDef = TypedDict(
    "ConfirmConnectionResponseTypeDef",
    {
        "connectionState": Literal[
            "ordering",
            "requested",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ]
    },
    total=False,
)

ConfirmPrivateVirtualInterfaceResponseTypeDef = TypedDict(
    "ConfirmPrivateVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ]
    },
    total=False,
)

ConfirmPublicVirtualInterfaceResponseTypeDef = TypedDict(
    "ConfirmPublicVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ]
    },
    total=False,
)

ConfirmTransitVirtualInterfaceResponseTypeDef = TypedDict(
    "ConfirmTransitVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ]
    },
    total=False,
)

ConnectionsTypeDef = TypedDict(
    "ConnectionsTypeDef", {"connections": List["ConnectionTypeDef"]}, total=False
)

CreateBGPPeerResponseTypeDef = TypedDict(
    "CreateBGPPeerResponseTypeDef", {"virtualInterface": "VirtualInterfaceTypeDef"}, total=False
)

CreateDirectConnectGatewayAssociationProposalResultTypeDef = TypedDict(
    "CreateDirectConnectGatewayAssociationProposalResultTypeDef",
    {"directConnectGatewayAssociationProposal": "DirectConnectGatewayAssociationProposalTypeDef"},
    total=False,
)

CreateDirectConnectGatewayAssociationResultTypeDef = TypedDict(
    "CreateDirectConnectGatewayAssociationResultTypeDef",
    {"directConnectGatewayAssociation": "DirectConnectGatewayAssociationTypeDef"},
    total=False,
)

CreateDirectConnectGatewayResultTypeDef = TypedDict(
    "CreateDirectConnectGatewayResultTypeDef",
    {"directConnectGateway": "DirectConnectGatewayTypeDef"},
    total=False,
)

CreateTransitVirtualInterfaceResultTypeDef = TypedDict(
    "CreateTransitVirtualInterfaceResultTypeDef",
    {"virtualInterface": "VirtualInterfaceTypeDef"},
    total=False,
)

DeleteBGPPeerResponseTypeDef = TypedDict(
    "DeleteBGPPeerResponseTypeDef", {"virtualInterface": "VirtualInterfaceTypeDef"}, total=False
)

DeleteDirectConnectGatewayAssociationProposalResultTypeDef = TypedDict(
    "DeleteDirectConnectGatewayAssociationProposalResultTypeDef",
    {"directConnectGatewayAssociationProposal": "DirectConnectGatewayAssociationProposalTypeDef"},
    total=False,
)

DeleteDirectConnectGatewayAssociationResultTypeDef = TypedDict(
    "DeleteDirectConnectGatewayAssociationResultTypeDef",
    {"directConnectGatewayAssociation": "DirectConnectGatewayAssociationTypeDef"},
    total=False,
)

DeleteDirectConnectGatewayResultTypeDef = TypedDict(
    "DeleteDirectConnectGatewayResultTypeDef",
    {"directConnectGateway": "DirectConnectGatewayTypeDef"},
    total=False,
)

DeleteInterconnectResponseTypeDef = TypedDict(
    "DeleteInterconnectResponseTypeDef",
    {
        "interconnectState": Literal[
            "requested", "pending", "available", "down", "deleting", "deleted", "unknown"
        ]
    },
    total=False,
)

DeleteVirtualInterfaceResponseTypeDef = TypedDict(
    "DeleteVirtualInterfaceResponseTypeDef",
    {
        "virtualInterfaceState": Literal[
            "confirming",
            "verifying",
            "pending",
            "available",
            "down",
            "deleting",
            "deleted",
            "rejected",
            "unknown",
        ]
    },
    total=False,
)

DescribeConnectionLoaResponseTypeDef = TypedDict(
    "DescribeConnectionLoaResponseTypeDef", {"loa": "LoaTypeDef"}, total=False
)

DescribeDirectConnectGatewayAssociationProposalsResultTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationProposalsResultTypeDef",
    {
        "directConnectGatewayAssociationProposals": List[
            "DirectConnectGatewayAssociationProposalTypeDef"
        ],
        "nextToken": str,
    },
    total=False,
)

DescribeDirectConnectGatewayAssociationsResultTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAssociationsResultTypeDef",
    {
        "directConnectGatewayAssociations": List["DirectConnectGatewayAssociationTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeDirectConnectGatewayAttachmentsResultTypeDef = TypedDict(
    "DescribeDirectConnectGatewayAttachmentsResultTypeDef",
    {
        "directConnectGatewayAttachments": List["DirectConnectGatewayAttachmentTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeDirectConnectGatewaysResultTypeDef = TypedDict(
    "DescribeDirectConnectGatewaysResultTypeDef",
    {"directConnectGateways": List["DirectConnectGatewayTypeDef"], "nextToken": str},
    total=False,
)

DescribeInterconnectLoaResponseTypeDef = TypedDict(
    "DescribeInterconnectLoaResponseTypeDef", {"loa": "LoaTypeDef"}, total=False
)

DescribeTagsResponseTypeDef = TypedDict(
    "DescribeTagsResponseTypeDef", {"resourceTags": List["ResourceTagTypeDef"]}, total=False
)

InterconnectsTypeDef = TypedDict(
    "InterconnectsTypeDef", {"interconnects": List["InterconnectTypeDef"]}, total=False
)

LagsTypeDef = TypedDict("LagsTypeDef", {"lags": List["LagTypeDef"]}, total=False)

ListVirtualInterfaceTestHistoryResponseTypeDef = TypedDict(
    "ListVirtualInterfaceTestHistoryResponseTypeDef",
    {"virtualInterfaceTestHistory": List["VirtualInterfaceTestHistoryTypeDef"], "nextToken": str},
    total=False,
)

LocationsTypeDef = TypedDict(
    "LocationsTypeDef", {"locations": List["LocationTypeDef"]}, total=False
)

NewBGPPeerTypeDef = TypedDict(
    "NewBGPPeerTypeDef",
    {
        "asn": int,
        "authKey": str,
        "addressFamily": Literal["ipv4", "ipv6"],
        "amazonAddress": str,
        "customerAddress": str,
    },
    total=False,
)

_RequiredNewPrivateVirtualInterfaceAllocationTypeDef = TypedDict(
    "_RequiredNewPrivateVirtualInterfaceAllocationTypeDef",
    {"virtualInterfaceName": str, "vlan": int, "asn": int},
)
_OptionalNewPrivateVirtualInterfaceAllocationTypeDef = TypedDict(
    "_OptionalNewPrivateVirtualInterfaceAllocationTypeDef",
    {
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
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
    {"virtualInterfaceName": str, "vlan": int, "asn": int},
)
_OptionalNewPrivateVirtualInterfaceTypeDef = TypedDict(
    "_OptionalNewPrivateVirtualInterfaceTypeDef",
    {
        "mtu": int,
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
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
    {"virtualInterfaceName": str, "vlan": int, "asn": int},
)
_OptionalNewPublicVirtualInterfaceAllocationTypeDef = TypedDict(
    "_OptionalNewPublicVirtualInterfaceAllocationTypeDef",
    {
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
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
    {"virtualInterfaceName": str, "vlan": int, "asn": int},
)
_OptionalNewPublicVirtualInterfaceTypeDef = TypedDict(
    "_OptionalNewPublicVirtualInterfaceTypeDef",
    {
        "authKey": str,
        "amazonAddress": str,
        "customerAddress": str,
        "addressFamily": Literal["ipv4", "ipv6"],
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
        "addressFamily": Literal["ipv4", "ipv6"],
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
        "addressFamily": Literal["ipv4", "ipv6"],
        "directConnectGatewayId": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartBgpFailoverTestResponseTypeDef = TypedDict(
    "StartBgpFailoverTestResponseTypeDef",
    {"virtualInterfaceTest": "VirtualInterfaceTestHistoryTypeDef"},
    total=False,
)

StopBgpFailoverTestResponseTypeDef = TypedDict(
    "StopBgpFailoverTestResponseTypeDef",
    {"virtualInterfaceTest": "VirtualInterfaceTestHistoryTypeDef"},
    total=False,
)

UpdateDirectConnectGatewayAssociationResultTypeDef = TypedDict(
    "UpdateDirectConnectGatewayAssociationResultTypeDef",
    {"directConnectGatewayAssociation": "DirectConnectGatewayAssociationTypeDef"},
    total=False,
)

VirtualGatewaysTypeDef = TypedDict(
    "VirtualGatewaysTypeDef", {"virtualGateways": List["VirtualGatewayTypeDef"]}, total=False
)

VirtualInterfacesTypeDef = TypedDict(
    "VirtualInterfacesTypeDef", {"virtualInterfaces": List["VirtualInterfaceTypeDef"]}, total=False
)
