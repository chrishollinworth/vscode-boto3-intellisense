"""
Type annotations for directconnect service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_directconnect/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_directconnect.type_defs import RouteFilterPrefixTypeDef

    data: RouteFilterPrefixTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

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
    NniPartnerTypeType,
    VirtualInterfaceStateType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcceptDirectConnectGatewayAssociationProposalRequestTypeDef",
    "AcceptDirectConnectGatewayAssociationProposalResultTypeDef",
    "AllocateConnectionOnInterconnectRequestTypeDef",
    "AllocateHostedConnectionRequestTypeDef",
    "AllocatePrivateVirtualInterfaceRequestTypeDef",
    "AllocatePublicVirtualInterfaceRequestTypeDef",
    "AllocateTransitVirtualInterfaceRequestTypeDef",
    "AllocateTransitVirtualInterfaceResultTypeDef",
    "AssociateConnectionWithLagRequestTypeDef",
    "AssociateHostedConnectionRequestTypeDef",
    "AssociateMacSecKeyRequestTypeDef",
    "AssociateMacSecKeyResponseTypeDef",
    "AssociateVirtualInterfaceRequestTypeDef",
    "AssociatedCoreNetworkTypeDef",
    "AssociatedGatewayTypeDef",
    "BGPPeerTypeDef",
    "ConfirmConnectionRequestTypeDef",
    "ConfirmConnectionResponseTypeDef",
    "ConfirmCustomerAgreementRequestTypeDef",
    "ConfirmCustomerAgreementResponseTypeDef",
    "ConfirmPrivateVirtualInterfaceRequestTypeDef",
    "ConfirmPrivateVirtualInterfaceResponseTypeDef",
    "ConfirmPublicVirtualInterfaceRequestTypeDef",
    "ConfirmPublicVirtualInterfaceResponseTypeDef",
    "ConfirmTransitVirtualInterfaceRequestTypeDef",
    "ConfirmTransitVirtualInterfaceResponseTypeDef",
    "ConnectionResponseTypeDef",
    "ConnectionTypeDef",
    "ConnectionsTypeDef",
    "CreateBGPPeerRequestTypeDef",
    "CreateBGPPeerResponseTypeDef",
    "CreateConnectionRequestTypeDef",
    "CreateDirectConnectGatewayAssociationProposalRequestTypeDef",
    "CreateDirectConnectGatewayAssociationProposalResultTypeDef",
    "CreateDirectConnectGatewayAssociationRequestTypeDef",
    "CreateDirectConnectGatewayAssociationResultTypeDef",
    "CreateDirectConnectGatewayRequestTypeDef",
    "CreateDirectConnectGatewayResultTypeDef",
    "CreateInterconnectRequestTypeDef",
    "CreateLagRequestTypeDef",
    "CreatePrivateVirtualInterfaceRequestTypeDef",
    "CreatePublicVirtualInterfaceRequestTypeDef",
    "CreateTransitVirtualInterfaceRequestTypeDef",
    "CreateTransitVirtualInterfaceResultTypeDef",
    "CustomerAgreementTypeDef",
    "DeleteBGPPeerRequestTypeDef",
    "DeleteBGPPeerResponseTypeDef",
    "DeleteConnectionRequestTypeDef",
    "DeleteDirectConnectGatewayAssociationProposalRequestTypeDef",
    "DeleteDirectConnectGatewayAssociationProposalResultTypeDef",
    "DeleteDirectConnectGatewayAssociationRequestTypeDef",
    "DeleteDirectConnectGatewayAssociationResultTypeDef",
    "DeleteDirectConnectGatewayRequestTypeDef",
    "DeleteDirectConnectGatewayResultTypeDef",
    "DeleteInterconnectRequestTypeDef",
    "DeleteInterconnectResponseTypeDef",
    "DeleteLagRequestTypeDef",
    "DeleteVirtualInterfaceRequestTypeDef",
    "DeleteVirtualInterfaceResponseTypeDef",
    "DescribeConnectionLoaRequestTypeDef",
    "DescribeConnectionLoaResponseTypeDef",
    "DescribeConnectionsOnInterconnectRequestTypeDef",
    "DescribeConnectionsRequestTypeDef",
    "DescribeCustomerMetadataResponseTypeDef",
    "DescribeDirectConnectGatewayAssociationProposalsRequestTypeDef",
    "DescribeDirectConnectGatewayAssociationProposalsResultTypeDef",
    "DescribeDirectConnectGatewayAssociationsRequestPaginateTypeDef",
    "DescribeDirectConnectGatewayAssociationsRequestTypeDef",
    "DescribeDirectConnectGatewayAssociationsResultTypeDef",
    "DescribeDirectConnectGatewayAttachmentsRequestPaginateTypeDef",
    "DescribeDirectConnectGatewayAttachmentsRequestTypeDef",
    "DescribeDirectConnectGatewayAttachmentsResultTypeDef",
    "DescribeDirectConnectGatewaysRequestPaginateTypeDef",
    "DescribeDirectConnectGatewaysRequestTypeDef",
    "DescribeDirectConnectGatewaysResultTypeDef",
    "DescribeHostedConnectionsRequestTypeDef",
    "DescribeInterconnectLoaRequestTypeDef",
    "DescribeInterconnectLoaResponseTypeDef",
    "DescribeInterconnectsRequestTypeDef",
    "DescribeLagsRequestTypeDef",
    "DescribeLoaRequestTypeDef",
    "DescribeRouterConfigurationRequestTypeDef",
    "DescribeRouterConfigurationResponseTypeDef",
    "DescribeTagsRequestTypeDef",
    "DescribeTagsResponseTypeDef",
    "DescribeVirtualInterfacesRequestTypeDef",
    "DirectConnectGatewayAssociationProposalTypeDef",
    "DirectConnectGatewayAssociationTypeDef",
    "DirectConnectGatewayAttachmentTypeDef",
    "DirectConnectGatewayTypeDef",
    "DisassociateConnectionFromLagRequestTypeDef",
    "DisassociateMacSecKeyRequestTypeDef",
    "DisassociateMacSecKeyResponseTypeDef",
    "InterconnectResponseTypeDef",
    "InterconnectTypeDef",
    "InterconnectsTypeDef",
    "LagResponseTypeDef",
    "LagTypeDef",
    "LagsTypeDef",
    "ListVirtualInterfaceTestHistoryRequestTypeDef",
    "ListVirtualInterfaceTestHistoryResponseTypeDef",
    "LoaResponseTypeDef",
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
    "RouterTypeTypeDef",
    "StartBgpFailoverTestRequestTypeDef",
    "StartBgpFailoverTestResponseTypeDef",
    "StopBgpFailoverTestRequestTypeDef",
    "StopBgpFailoverTestResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateConnectionRequestTypeDef",
    "UpdateDirectConnectGatewayAssociationRequestTypeDef",
    "UpdateDirectConnectGatewayAssociationResultTypeDef",
    "UpdateDirectConnectGatewayRequestTypeDef",
    "UpdateDirectConnectGatewayResponseTypeDef",
    "UpdateLagRequestTypeDef",
    "UpdateVirtualInterfaceAttributesRequestTypeDef",
    "VirtualGatewayTypeDef",
    "VirtualGatewaysTypeDef",
    "VirtualInterfaceResponseTypeDef",
    "VirtualInterfaceTestHistoryTypeDef",
    "VirtualInterfaceTypeDef",
    "VirtualInterfacesTypeDef",
)

class RouteFilterPrefixTypeDef(TypedDict):
    cidr: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AllocateConnectionOnInterconnectRequestTypeDef(TypedDict):
    bandwidth: str
    connectionName: str
    ownerAccount: str
    interconnectId: str
    vlan: int

class TagTypeDef(TypedDict):
    key: str
    value: NotRequired[str]

class AssociateConnectionWithLagRequestTypeDef(TypedDict):
    connectionId: str
    lagId: str

class AssociateHostedConnectionRequestTypeDef(TypedDict):
    connectionId: str
    parentConnectionId: str

class AssociateMacSecKeyRequestTypeDef(TypedDict):
    connectionId: str
    secretARN: NotRequired[str]
    ckn: NotRequired[str]
    cak: NotRequired[str]

class MacSecKeyTypeDef(TypedDict):
    secretARN: NotRequired[str]
    ckn: NotRequired[str]
    state: NotRequired[str]
    startOn: NotRequired[str]

class AssociateVirtualInterfaceRequestTypeDef(TypedDict):
    virtualInterfaceId: str
    connectionId: str

AssociatedCoreNetworkTypeDef = TypedDict(
    "AssociatedCoreNetworkTypeDef",
    {
        "id": NotRequired[str],
        "ownerAccount": NotRequired[str],
        "attachmentId": NotRequired[str],
    },
)
AssociatedGatewayTypeDef = TypedDict(
    "AssociatedGatewayTypeDef",
    {
        "id": NotRequired[str],
        "type": NotRequired[GatewayTypeType],
        "ownerAccount": NotRequired[str],
        "region": NotRequired[str],
    },
)

class BGPPeerTypeDef(TypedDict):
    bgpPeerId: NotRequired[str]
    asn: NotRequired[int]
    authKey: NotRequired[str]
    addressFamily: NotRequired[AddressFamilyType]
    amazonAddress: NotRequired[str]
    customerAddress: NotRequired[str]
    bgpPeerState: NotRequired[BGPPeerStateType]
    bgpStatus: NotRequired[BGPStatusType]
    awsDeviceV2: NotRequired[str]
    awsLogicalDeviceId: NotRequired[str]

class ConfirmConnectionRequestTypeDef(TypedDict):
    connectionId: str

class ConfirmCustomerAgreementRequestTypeDef(TypedDict):
    agreementName: NotRequired[str]

class ConfirmPrivateVirtualInterfaceRequestTypeDef(TypedDict):
    virtualInterfaceId: str
    virtualGatewayId: NotRequired[str]
    directConnectGatewayId: NotRequired[str]

class ConfirmPublicVirtualInterfaceRequestTypeDef(TypedDict):
    virtualInterfaceId: str

class ConfirmTransitVirtualInterfaceRequestTypeDef(TypedDict):
    virtualInterfaceId: str
    directConnectGatewayId: str

class NewBGPPeerTypeDef(TypedDict):
    asn: NotRequired[int]
    authKey: NotRequired[str]
    addressFamily: NotRequired[AddressFamilyType]
    amazonAddress: NotRequired[str]
    customerAddress: NotRequired[str]

class CustomerAgreementTypeDef(TypedDict):
    agreementName: NotRequired[str]
    status: NotRequired[str]

class DeleteBGPPeerRequestTypeDef(TypedDict):
    virtualInterfaceId: NotRequired[str]
    asn: NotRequired[int]
    customerAddress: NotRequired[str]
    bgpPeerId: NotRequired[str]

class DeleteConnectionRequestTypeDef(TypedDict):
    connectionId: str

class DeleteDirectConnectGatewayAssociationProposalRequestTypeDef(TypedDict):
    proposalId: str

class DeleteDirectConnectGatewayAssociationRequestTypeDef(TypedDict):
    associationId: NotRequired[str]
    directConnectGatewayId: NotRequired[str]
    virtualGatewayId: NotRequired[str]

class DeleteDirectConnectGatewayRequestTypeDef(TypedDict):
    directConnectGatewayId: str

class DeleteInterconnectRequestTypeDef(TypedDict):
    interconnectId: str

class DeleteLagRequestTypeDef(TypedDict):
    lagId: str

class DeleteVirtualInterfaceRequestTypeDef(TypedDict):
    virtualInterfaceId: str

class DescribeConnectionLoaRequestTypeDef(TypedDict):
    connectionId: str
    providerName: NotRequired[str]
    loaContentType: NotRequired[Literal["application/pdf"]]

class LoaTypeDef(TypedDict):
    loaContent: NotRequired[bytes]
    loaContentType: NotRequired[Literal["application/pdf"]]

class DescribeConnectionsOnInterconnectRequestTypeDef(TypedDict):
    interconnectId: str

class DescribeConnectionsRequestTypeDef(TypedDict):
    connectionId: NotRequired[str]

class DescribeDirectConnectGatewayAssociationProposalsRequestTypeDef(TypedDict):
    directConnectGatewayId: NotRequired[str]
    proposalId: NotRequired[str]
    associatedGatewayId: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeDirectConnectGatewayAssociationsRequestTypeDef(TypedDict):
    associationId: NotRequired[str]
    associatedGatewayId: NotRequired[str]
    directConnectGatewayId: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    virtualGatewayId: NotRequired[str]

class DescribeDirectConnectGatewayAttachmentsRequestTypeDef(TypedDict):
    directConnectGatewayId: NotRequired[str]
    virtualInterfaceId: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class DirectConnectGatewayAttachmentTypeDef(TypedDict):
    directConnectGatewayId: NotRequired[str]
    virtualInterfaceId: NotRequired[str]
    virtualInterfaceRegion: NotRequired[str]
    virtualInterfaceOwnerAccount: NotRequired[str]
    attachmentState: NotRequired[DirectConnectGatewayAttachmentStateType]
    attachmentType: NotRequired[DirectConnectGatewayAttachmentTypeType]
    stateChangeError: NotRequired[str]

class DescribeDirectConnectGatewaysRequestTypeDef(TypedDict):
    directConnectGatewayId: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class DescribeHostedConnectionsRequestTypeDef(TypedDict):
    connectionId: str

class DescribeInterconnectLoaRequestTypeDef(TypedDict):
    interconnectId: str
    providerName: NotRequired[str]
    loaContentType: NotRequired[Literal["application/pdf"]]

class DescribeInterconnectsRequestTypeDef(TypedDict):
    interconnectId: NotRequired[str]

class DescribeLagsRequestTypeDef(TypedDict):
    lagId: NotRequired[str]

class DescribeLoaRequestTypeDef(TypedDict):
    connectionId: str
    providerName: NotRequired[str]
    loaContentType: NotRequired[Literal["application/pdf"]]

class DescribeRouterConfigurationRequestTypeDef(TypedDict):
    virtualInterfaceId: str
    routerTypeIdentifier: NotRequired[str]

class RouterTypeTypeDef(TypedDict):
    vendor: NotRequired[str]
    platform: NotRequired[str]
    software: NotRequired[str]
    xsltTemplateName: NotRequired[str]
    xsltTemplateNameForMacSec: NotRequired[str]
    routerTypeIdentifier: NotRequired[str]

class DescribeTagsRequestTypeDef(TypedDict):
    resourceArns: Sequence[str]

class DescribeVirtualInterfacesRequestTypeDef(TypedDict):
    connectionId: NotRequired[str]
    virtualInterfaceId: NotRequired[str]

class DisassociateConnectionFromLagRequestTypeDef(TypedDict):
    connectionId: str
    lagId: str

class DisassociateMacSecKeyRequestTypeDef(TypedDict):
    connectionId: str
    secretARN: str

class ListVirtualInterfaceTestHistoryRequestTypeDef(TypedDict):
    testId: NotRequired[str]
    virtualInterfaceId: NotRequired[str]
    bgpPeers: NotRequired[Sequence[str]]
    status: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class VirtualInterfaceTestHistoryTypeDef(TypedDict):
    testId: NotRequired[str]
    virtualInterfaceId: NotRequired[str]
    bgpPeers: NotRequired[List[str]]
    status: NotRequired[str]
    ownerAccount: NotRequired[str]
    testDurationInMinutes: NotRequired[int]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]

class LocationTypeDef(TypedDict):
    locationCode: NotRequired[str]
    locationName: NotRequired[str]
    region: NotRequired[str]
    availablePortSpeeds: NotRequired[List[str]]
    availableProviders: NotRequired[List[str]]
    availableMacSecPortSpeeds: NotRequired[List[str]]

class StartBgpFailoverTestRequestTypeDef(TypedDict):
    virtualInterfaceId: str
    bgpPeers: NotRequired[Sequence[str]]
    testDurationInMinutes: NotRequired[int]

class StopBgpFailoverTestRequestTypeDef(TypedDict):
    virtualInterfaceId: str

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateConnectionRequestTypeDef(TypedDict):
    connectionId: str
    connectionName: NotRequired[str]
    encryptionMode: NotRequired[str]

class UpdateDirectConnectGatewayRequestTypeDef(TypedDict):
    directConnectGatewayId: str
    newDirectConnectGatewayName: str

class UpdateLagRequestTypeDef(TypedDict):
    lagId: str
    lagName: NotRequired[str]
    minimumLinks: NotRequired[int]
    encryptionMode: NotRequired[str]

class UpdateVirtualInterfaceAttributesRequestTypeDef(TypedDict):
    virtualInterfaceId: str
    mtu: NotRequired[int]
    enableSiteLink: NotRequired[bool]
    virtualInterfaceName: NotRequired[str]

class VirtualGatewayTypeDef(TypedDict):
    virtualGatewayId: NotRequired[str]
    virtualGatewayState: NotRequired[str]

class AcceptDirectConnectGatewayAssociationProposalRequestTypeDef(TypedDict):
    directConnectGatewayId: str
    proposalId: str
    associatedGatewayOwnerAccount: str
    overrideAllowedPrefixesToDirectConnectGateway: NotRequired[Sequence[RouteFilterPrefixTypeDef]]

class CreateDirectConnectGatewayAssociationProposalRequestTypeDef(TypedDict):
    directConnectGatewayId: str
    directConnectGatewayOwnerAccount: str
    gatewayId: str
    addAllowedPrefixesToDirectConnectGateway: NotRequired[Sequence[RouteFilterPrefixTypeDef]]
    removeAllowedPrefixesToDirectConnectGateway: NotRequired[Sequence[RouteFilterPrefixTypeDef]]

class CreateDirectConnectGatewayAssociationRequestTypeDef(TypedDict):
    directConnectGatewayId: str
    gatewayId: NotRequired[str]
    addAllowedPrefixesToDirectConnectGateway: NotRequired[Sequence[RouteFilterPrefixTypeDef]]
    virtualGatewayId: NotRequired[str]

class UpdateDirectConnectGatewayAssociationRequestTypeDef(TypedDict):
    associationId: NotRequired[str]
    addAllowedPrefixesToDirectConnectGateway: NotRequired[Sequence[RouteFilterPrefixTypeDef]]
    removeAllowedPrefixesToDirectConnectGateway: NotRequired[Sequence[RouteFilterPrefixTypeDef]]

class ConfirmConnectionResponseTypeDef(TypedDict):
    connectionState: ConnectionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ConfirmCustomerAgreementResponseTypeDef(TypedDict):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConfirmPrivateVirtualInterfaceResponseTypeDef(TypedDict):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ConfirmPublicVirtualInterfaceResponseTypeDef(TypedDict):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ConfirmTransitVirtualInterfaceResponseTypeDef(TypedDict):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInterconnectResponseTypeDef(TypedDict):
    interconnectState: InterconnectStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualInterfaceResponseTypeDef(TypedDict):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadataTypeDef

class LoaResponseTypeDef(TypedDict):
    loaContent: bytes
    loaContentType: Literal["application/pdf"]
    ResponseMetadata: ResponseMetadataTypeDef

class AllocateHostedConnectionRequestTypeDef(TypedDict):
    connectionId: str
    ownerAccount: str
    bandwidth: str
    connectionName: str
    vlan: int
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateConnectionRequestTypeDef(TypedDict):
    location: str
    bandwidth: str
    connectionName: str
    lagId: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    providerName: NotRequired[str]
    requestMACSec: NotRequired[bool]

class CreateDirectConnectGatewayRequestTypeDef(TypedDict):
    directConnectGatewayName: str
    tags: NotRequired[Sequence[TagTypeDef]]
    amazonSideAsn: NotRequired[int]

class CreateInterconnectRequestTypeDef(TypedDict):
    interconnectName: str
    bandwidth: str
    location: str
    lagId: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    providerName: NotRequired[str]

class CreateLagRequestTypeDef(TypedDict):
    numberOfConnections: int
    location: str
    connectionsBandwidth: str
    lagName: str
    connectionId: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    childConnectionTags: NotRequired[Sequence[TagTypeDef]]
    providerName: NotRequired[str]
    requestMACSec: NotRequired[bool]

class DirectConnectGatewayTypeDef(TypedDict):
    directConnectGatewayId: NotRequired[str]
    directConnectGatewayName: NotRequired[str]
    amazonSideAsn: NotRequired[int]
    ownerAccount: NotRequired[str]
    directConnectGatewayState: NotRequired[DirectConnectGatewayStateType]
    stateChangeError: NotRequired[str]
    tags: NotRequired[List[TagTypeDef]]

class InterconnectResponseTypeDef(TypedDict):
    interconnectId: str
    interconnectName: str
    interconnectState: InterconnectStateType
    region: str
    location: str
    bandwidth: str
    loaIssueTime: datetime
    lagId: str
    awsDevice: str
    jumboFrameCapable: bool
    awsDeviceV2: str
    awsLogicalDeviceId: str
    hasLogicalRedundancy: HasLogicalRedundancyType
    tags: List[TagTypeDef]
    providerName: str
    ResponseMetadata: ResponseMetadataTypeDef

class InterconnectTypeDef(TypedDict):
    interconnectId: NotRequired[str]
    interconnectName: NotRequired[str]
    interconnectState: NotRequired[InterconnectStateType]
    region: NotRequired[str]
    location: NotRequired[str]
    bandwidth: NotRequired[str]
    loaIssueTime: NotRequired[datetime]
    lagId: NotRequired[str]
    awsDevice: NotRequired[str]
    jumboFrameCapable: NotRequired[bool]
    awsDeviceV2: NotRequired[str]
    awsLogicalDeviceId: NotRequired[str]
    hasLogicalRedundancy: NotRequired[HasLogicalRedundancyType]
    tags: NotRequired[List[TagTypeDef]]
    providerName: NotRequired[str]

class NewPrivateVirtualInterfaceAllocationTypeDef(TypedDict):
    virtualInterfaceName: str
    vlan: int
    asn: int
    mtu: NotRequired[int]
    authKey: NotRequired[str]
    amazonAddress: NotRequired[str]
    addressFamily: NotRequired[AddressFamilyType]
    customerAddress: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class NewPrivateVirtualInterfaceTypeDef(TypedDict):
    virtualInterfaceName: str
    vlan: int
    asn: int
    mtu: NotRequired[int]
    authKey: NotRequired[str]
    amazonAddress: NotRequired[str]
    customerAddress: NotRequired[str]
    addressFamily: NotRequired[AddressFamilyType]
    virtualGatewayId: NotRequired[str]
    directConnectGatewayId: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    enableSiteLink: NotRequired[bool]

class NewPublicVirtualInterfaceAllocationTypeDef(TypedDict):
    virtualInterfaceName: str
    vlan: int
    asn: int
    authKey: NotRequired[str]
    amazonAddress: NotRequired[str]
    customerAddress: NotRequired[str]
    addressFamily: NotRequired[AddressFamilyType]
    routeFilterPrefixes: NotRequired[Sequence[RouteFilterPrefixTypeDef]]
    tags: NotRequired[Sequence[TagTypeDef]]

class NewPublicVirtualInterfaceTypeDef(TypedDict):
    virtualInterfaceName: str
    vlan: int
    asn: int
    authKey: NotRequired[str]
    amazonAddress: NotRequired[str]
    customerAddress: NotRequired[str]
    addressFamily: NotRequired[AddressFamilyType]
    routeFilterPrefixes: NotRequired[Sequence[RouteFilterPrefixTypeDef]]
    tags: NotRequired[Sequence[TagTypeDef]]

class NewTransitVirtualInterfaceAllocationTypeDef(TypedDict):
    virtualInterfaceName: NotRequired[str]
    vlan: NotRequired[int]
    asn: NotRequired[int]
    mtu: NotRequired[int]
    authKey: NotRequired[str]
    amazonAddress: NotRequired[str]
    customerAddress: NotRequired[str]
    addressFamily: NotRequired[AddressFamilyType]
    tags: NotRequired[Sequence[TagTypeDef]]

class NewTransitVirtualInterfaceTypeDef(TypedDict):
    virtualInterfaceName: NotRequired[str]
    vlan: NotRequired[int]
    asn: NotRequired[int]
    mtu: NotRequired[int]
    authKey: NotRequired[str]
    amazonAddress: NotRequired[str]
    customerAddress: NotRequired[str]
    addressFamily: NotRequired[AddressFamilyType]
    directConnectGatewayId: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    enableSiteLink: NotRequired[bool]

class ResourceTagTypeDef(TypedDict):
    resourceArn: NotRequired[str]
    tags: NotRequired[List[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class AssociateMacSecKeyResponseTypeDef(TypedDict):
    connectionId: str
    macSecKeys: List[MacSecKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectionResponseTypeDef(TypedDict):
    ownerAccount: str
    connectionId: str
    connectionName: str
    connectionState: ConnectionStateType
    region: str
    location: str
    bandwidth: str
    vlan: int
    partnerName: str
    loaIssueTime: datetime
    lagId: str
    awsDevice: str
    jumboFrameCapable: bool
    awsDeviceV2: str
    awsLogicalDeviceId: str
    hasLogicalRedundancy: HasLogicalRedundancyType
    tags: List[TagTypeDef]
    providerName: str
    macSecCapable: bool
    portEncryptionStatus: str
    encryptionMode: str
    macSecKeys: List[MacSecKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectionTypeDef(TypedDict):
    ownerAccount: NotRequired[str]
    connectionId: NotRequired[str]
    connectionName: NotRequired[str]
    connectionState: NotRequired[ConnectionStateType]
    region: NotRequired[str]
    location: NotRequired[str]
    bandwidth: NotRequired[str]
    vlan: NotRequired[int]
    partnerName: NotRequired[str]
    loaIssueTime: NotRequired[datetime]
    lagId: NotRequired[str]
    awsDevice: NotRequired[str]
    jumboFrameCapable: NotRequired[bool]
    awsDeviceV2: NotRequired[str]
    awsLogicalDeviceId: NotRequired[str]
    hasLogicalRedundancy: NotRequired[HasLogicalRedundancyType]
    tags: NotRequired[List[TagTypeDef]]
    providerName: NotRequired[str]
    macSecCapable: NotRequired[bool]
    portEncryptionStatus: NotRequired[str]
    encryptionMode: NotRequired[str]
    macSecKeys: NotRequired[List[MacSecKeyTypeDef]]

class DisassociateMacSecKeyResponseTypeDef(TypedDict):
    connectionId: str
    macSecKeys: List[MacSecKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DirectConnectGatewayAssociationProposalTypeDef(TypedDict):
    proposalId: NotRequired[str]
    directConnectGatewayId: NotRequired[str]
    directConnectGatewayOwnerAccount: NotRequired[str]
    proposalState: NotRequired[DirectConnectGatewayAssociationProposalStateType]
    associatedGateway: NotRequired[AssociatedGatewayTypeDef]
    existingAllowedPrefixesToDirectConnectGateway: NotRequired[List[RouteFilterPrefixTypeDef]]
    requestedAllowedPrefixesToDirectConnectGateway: NotRequired[List[RouteFilterPrefixTypeDef]]

class DirectConnectGatewayAssociationTypeDef(TypedDict):
    directConnectGatewayId: NotRequired[str]
    directConnectGatewayOwnerAccount: NotRequired[str]
    associationState: NotRequired[DirectConnectGatewayAssociationStateType]
    stateChangeError: NotRequired[str]
    associatedGateway: NotRequired[AssociatedGatewayTypeDef]
    associationId: NotRequired[str]
    allowedPrefixesToDirectConnectGateway: NotRequired[List[RouteFilterPrefixTypeDef]]
    associatedCoreNetwork: NotRequired[AssociatedCoreNetworkTypeDef]
    virtualGatewayId: NotRequired[str]
    virtualGatewayRegion: NotRequired[str]
    virtualGatewayOwnerAccount: NotRequired[str]

class VirtualInterfaceResponseTypeDef(TypedDict):
    ownerAccount: str
    virtualInterfaceId: str
    location: str
    connectionId: str
    virtualInterfaceType: str
    virtualInterfaceName: str
    vlan: int
    asn: int
    amazonSideAsn: int
    authKey: str
    amazonAddress: str
    customerAddress: str
    addressFamily: AddressFamilyType
    virtualInterfaceState: VirtualInterfaceStateType
    customerRouterConfig: str
    mtu: int
    jumboFrameCapable: bool
    virtualGatewayId: str
    directConnectGatewayId: str
    routeFilterPrefixes: List[RouteFilterPrefixTypeDef]
    bgpPeers: List[BGPPeerTypeDef]
    region: str
    awsDeviceV2: str
    awsLogicalDeviceId: str
    tags: List[TagTypeDef]
    siteLinkEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class VirtualInterfaceTypeDef(TypedDict):
    ownerAccount: NotRequired[str]
    virtualInterfaceId: NotRequired[str]
    location: NotRequired[str]
    connectionId: NotRequired[str]
    virtualInterfaceType: NotRequired[str]
    virtualInterfaceName: NotRequired[str]
    vlan: NotRequired[int]
    asn: NotRequired[int]
    amazonSideAsn: NotRequired[int]
    authKey: NotRequired[str]
    amazonAddress: NotRequired[str]
    customerAddress: NotRequired[str]
    addressFamily: NotRequired[AddressFamilyType]
    virtualInterfaceState: NotRequired[VirtualInterfaceStateType]
    customerRouterConfig: NotRequired[str]
    mtu: NotRequired[int]
    jumboFrameCapable: NotRequired[bool]
    virtualGatewayId: NotRequired[str]
    directConnectGatewayId: NotRequired[str]
    routeFilterPrefixes: NotRequired[List[RouteFilterPrefixTypeDef]]
    bgpPeers: NotRequired[List[BGPPeerTypeDef]]
    region: NotRequired[str]
    awsDeviceV2: NotRequired[str]
    awsLogicalDeviceId: NotRequired[str]
    tags: NotRequired[List[TagTypeDef]]
    siteLinkEnabled: NotRequired[bool]

class CreateBGPPeerRequestTypeDef(TypedDict):
    virtualInterfaceId: NotRequired[str]
    newBGPPeer: NotRequired[NewBGPPeerTypeDef]

class DescribeCustomerMetadataResponseTypeDef(TypedDict):
    agreements: List[CustomerAgreementTypeDef]
    nniPartnerType: NniPartnerTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectionLoaResponseTypeDef(TypedDict):
    loa: LoaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInterconnectLoaResponseTypeDef(TypedDict):
    loa: LoaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDirectConnectGatewayAssociationsRequestPaginateTypeDef(TypedDict):
    associationId: NotRequired[str]
    associatedGatewayId: NotRequired[str]
    directConnectGatewayId: NotRequired[str]
    virtualGatewayId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDirectConnectGatewayAttachmentsRequestPaginateTypeDef(TypedDict):
    directConnectGatewayId: NotRequired[str]
    virtualInterfaceId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDirectConnectGatewaysRequestPaginateTypeDef(TypedDict):
    directConnectGatewayId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDirectConnectGatewayAttachmentsResultTypeDef(TypedDict):
    directConnectGatewayAttachments: List[DirectConnectGatewayAttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeRouterConfigurationResponseTypeDef(TypedDict):
    customerRouterConfig: str
    router: RouterTypeTypeDef
    virtualInterfaceId: str
    virtualInterfaceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualInterfaceTestHistoryResponseTypeDef(TypedDict):
    virtualInterfaceTestHistory: List[VirtualInterfaceTestHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartBgpFailoverTestResponseTypeDef(TypedDict):
    virtualInterfaceTest: VirtualInterfaceTestHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopBgpFailoverTestResponseTypeDef(TypedDict):
    virtualInterfaceTest: VirtualInterfaceTestHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LocationsTypeDef(TypedDict):
    locations: List[LocationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VirtualGatewaysTypeDef(TypedDict):
    virtualGateways: List[VirtualGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDirectConnectGatewayResultTypeDef(TypedDict):
    directConnectGateway: DirectConnectGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDirectConnectGatewayResultTypeDef(TypedDict):
    directConnectGateway: DirectConnectGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDirectConnectGatewaysResultTypeDef(TypedDict):
    directConnectGateways: List[DirectConnectGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateDirectConnectGatewayResponseTypeDef(TypedDict):
    directConnectGateway: DirectConnectGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InterconnectsTypeDef(TypedDict):
    interconnects: List[InterconnectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AllocatePrivateVirtualInterfaceRequestTypeDef(TypedDict):
    connectionId: str
    ownerAccount: str
    newPrivateVirtualInterfaceAllocation: NewPrivateVirtualInterfaceAllocationTypeDef

class CreatePrivateVirtualInterfaceRequestTypeDef(TypedDict):
    connectionId: str
    newPrivateVirtualInterface: NewPrivateVirtualInterfaceTypeDef

class AllocatePublicVirtualInterfaceRequestTypeDef(TypedDict):
    connectionId: str
    ownerAccount: str
    newPublicVirtualInterfaceAllocation: NewPublicVirtualInterfaceAllocationTypeDef

class CreatePublicVirtualInterfaceRequestTypeDef(TypedDict):
    connectionId: str
    newPublicVirtualInterface: NewPublicVirtualInterfaceTypeDef

class AllocateTransitVirtualInterfaceRequestTypeDef(TypedDict):
    connectionId: str
    ownerAccount: str
    newTransitVirtualInterfaceAllocation: NewTransitVirtualInterfaceAllocationTypeDef

class CreateTransitVirtualInterfaceRequestTypeDef(TypedDict):
    connectionId: str
    newTransitVirtualInterface: NewTransitVirtualInterfaceTypeDef

class DescribeTagsResponseTypeDef(TypedDict):
    resourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectionsTypeDef(TypedDict):
    connections: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LagResponseTypeDef(TypedDict):
    connectionsBandwidth: str
    numberOfConnections: int
    lagId: str
    ownerAccount: str
    lagName: str
    lagState: LagStateType
    location: str
    region: str
    minimumLinks: int
    awsDevice: str
    awsDeviceV2: str
    awsLogicalDeviceId: str
    connections: List[ConnectionTypeDef]
    allowsHostedConnections: bool
    jumboFrameCapable: bool
    hasLogicalRedundancy: HasLogicalRedundancyType
    tags: List[TagTypeDef]
    providerName: str
    macSecCapable: bool
    encryptionMode: str
    macSecKeys: List[MacSecKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LagTypeDef(TypedDict):
    connectionsBandwidth: NotRequired[str]
    numberOfConnections: NotRequired[int]
    lagId: NotRequired[str]
    ownerAccount: NotRequired[str]
    lagName: NotRequired[str]
    lagState: NotRequired[LagStateType]
    location: NotRequired[str]
    region: NotRequired[str]
    minimumLinks: NotRequired[int]
    awsDevice: NotRequired[str]
    awsDeviceV2: NotRequired[str]
    awsLogicalDeviceId: NotRequired[str]
    connections: NotRequired[List[ConnectionTypeDef]]
    allowsHostedConnections: NotRequired[bool]
    jumboFrameCapable: NotRequired[bool]
    hasLogicalRedundancy: NotRequired[HasLogicalRedundancyType]
    tags: NotRequired[List[TagTypeDef]]
    providerName: NotRequired[str]
    macSecCapable: NotRequired[bool]
    encryptionMode: NotRequired[str]
    macSecKeys: NotRequired[List[MacSecKeyTypeDef]]

class CreateDirectConnectGatewayAssociationProposalResultTypeDef(TypedDict):
    directConnectGatewayAssociationProposal: DirectConnectGatewayAssociationProposalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDirectConnectGatewayAssociationProposalResultTypeDef(TypedDict):
    directConnectGatewayAssociationProposal: DirectConnectGatewayAssociationProposalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDirectConnectGatewayAssociationProposalsResultTypeDef(TypedDict):
    directConnectGatewayAssociationProposals: List[DirectConnectGatewayAssociationProposalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AcceptDirectConnectGatewayAssociationProposalResultTypeDef(TypedDict):
    directConnectGatewayAssociation: DirectConnectGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDirectConnectGatewayAssociationResultTypeDef(TypedDict):
    directConnectGatewayAssociation: DirectConnectGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDirectConnectGatewayAssociationResultTypeDef(TypedDict):
    directConnectGatewayAssociation: DirectConnectGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDirectConnectGatewayAssociationsResultTypeDef(TypedDict):
    directConnectGatewayAssociations: List[DirectConnectGatewayAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateDirectConnectGatewayAssociationResultTypeDef(TypedDict):
    directConnectGatewayAssociation: DirectConnectGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AllocateTransitVirtualInterfaceResultTypeDef(TypedDict):
    virtualInterface: VirtualInterfaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBGPPeerResponseTypeDef(TypedDict):
    virtualInterface: VirtualInterfaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitVirtualInterfaceResultTypeDef(TypedDict):
    virtualInterface: VirtualInterfaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBGPPeerResponseTypeDef(TypedDict):
    virtualInterface: VirtualInterfaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class VirtualInterfacesTypeDef(TypedDict):
    virtualInterfaces: List[VirtualInterfaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LagsTypeDef(TypedDict):
    lags: List[LagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
