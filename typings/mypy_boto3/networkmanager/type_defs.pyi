"""
Type annotations for networkmanager service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_networkmanager.type_defs import AWSLocationTypeDef

    data: AWSLocationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    AttachmentErrorCodeType,
    AttachmentStateType,
    AttachmentTypeType,
    ChangeActionType,
    ChangeSetStateType,
    ChangeStatusType,
    ChangeTypeType,
    ConnectionStateType,
    ConnectionStatusType,
    ConnectionTypeType,
    ConnectPeerAssociationStateType,
    ConnectPeerErrorCodeType,
    ConnectPeerStateType,
    CoreNetworkPolicyAliasType,
    CoreNetworkStateType,
    CustomerGatewayAssociationStateType,
    DeviceStateType,
    GlobalNetworkStateType,
    LinkAssociationStateType,
    LinkStateType,
    PeeringErrorCodeType,
    PeeringStateType,
    RouteAnalysisCompletionReasonCodeType,
    RouteAnalysisCompletionResultCodeType,
    RouteAnalysisStatusType,
    RouteStateType,
    RouteTableTypeType,
    RouteTypeType,
    SegmentActionServiceInsertionType,
    SendViaModeType,
    SiteStateType,
    TransitGatewayConnectPeerAssociationStateType,
    TransitGatewayRegistrationStateType,
    TunnelProtocolType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AWSLocationTypeDef",
    "AcceptAttachmentRequestTypeDef",
    "AcceptAttachmentResponseTypeDef",
    "AccountStatusTypeDef",
    "AssociateConnectPeerRequestTypeDef",
    "AssociateConnectPeerResponseTypeDef",
    "AssociateCustomerGatewayRequestTypeDef",
    "AssociateCustomerGatewayResponseTypeDef",
    "AssociateLinkRequestTypeDef",
    "AssociateLinkResponseTypeDef",
    "AssociateTransitGatewayConnectPeerRequestTypeDef",
    "AssociateTransitGatewayConnectPeerResponseTypeDef",
    "AttachmentErrorTypeDef",
    "AttachmentTypeDef",
    "BandwidthTypeDef",
    "BgpOptionsTypeDef",
    "ConnectAttachmentOptionsTypeDef",
    "ConnectAttachmentTypeDef",
    "ConnectPeerAssociationTypeDef",
    "ConnectPeerBgpConfigurationTypeDef",
    "ConnectPeerConfigurationTypeDef",
    "ConnectPeerErrorTypeDef",
    "ConnectPeerSummaryTypeDef",
    "ConnectPeerTypeDef",
    "ConnectionHealthTypeDef",
    "ConnectionTypeDef",
    "CoreNetworkChangeEventTypeDef",
    "CoreNetworkChangeEventValuesTypeDef",
    "CoreNetworkChangeTypeDef",
    "CoreNetworkChangeValuesTypeDef",
    "CoreNetworkEdgeTypeDef",
    "CoreNetworkNetworkFunctionGroupIdentifierTypeDef",
    "CoreNetworkNetworkFunctionGroupTypeDef",
    "CoreNetworkPolicyErrorTypeDef",
    "CoreNetworkPolicyTypeDef",
    "CoreNetworkPolicyVersionTypeDef",
    "CoreNetworkSegmentEdgeIdentifierTypeDef",
    "CoreNetworkSegmentTypeDef",
    "CoreNetworkSummaryTypeDef",
    "CoreNetworkTypeDef",
    "CreateConnectAttachmentRequestTypeDef",
    "CreateConnectAttachmentResponseTypeDef",
    "CreateConnectPeerRequestTypeDef",
    "CreateConnectPeerResponseTypeDef",
    "CreateConnectionRequestTypeDef",
    "CreateConnectionResponseTypeDef",
    "CreateCoreNetworkRequestTypeDef",
    "CreateCoreNetworkResponseTypeDef",
    "CreateDeviceRequestTypeDef",
    "CreateDeviceResponseTypeDef",
    "CreateDirectConnectGatewayAttachmentRequestTypeDef",
    "CreateDirectConnectGatewayAttachmentResponseTypeDef",
    "CreateGlobalNetworkRequestTypeDef",
    "CreateGlobalNetworkResponseTypeDef",
    "CreateLinkRequestTypeDef",
    "CreateLinkResponseTypeDef",
    "CreateSiteRequestTypeDef",
    "CreateSiteResponseTypeDef",
    "CreateSiteToSiteVpnAttachmentRequestTypeDef",
    "CreateSiteToSiteVpnAttachmentResponseTypeDef",
    "CreateTransitGatewayPeeringRequestTypeDef",
    "CreateTransitGatewayPeeringResponseTypeDef",
    "CreateTransitGatewayRouteTableAttachmentRequestTypeDef",
    "CreateTransitGatewayRouteTableAttachmentResponseTypeDef",
    "CreateVpcAttachmentRequestTypeDef",
    "CreateVpcAttachmentResponseTypeDef",
    "CustomerGatewayAssociationTypeDef",
    "DeleteAttachmentRequestTypeDef",
    "DeleteAttachmentResponseTypeDef",
    "DeleteConnectPeerRequestTypeDef",
    "DeleteConnectPeerResponseTypeDef",
    "DeleteConnectionRequestTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteCoreNetworkPolicyVersionRequestTypeDef",
    "DeleteCoreNetworkPolicyVersionResponseTypeDef",
    "DeleteCoreNetworkRequestTypeDef",
    "DeleteCoreNetworkResponseTypeDef",
    "DeleteDeviceRequestTypeDef",
    "DeleteDeviceResponseTypeDef",
    "DeleteGlobalNetworkRequestTypeDef",
    "DeleteGlobalNetworkResponseTypeDef",
    "DeleteLinkRequestTypeDef",
    "DeleteLinkResponseTypeDef",
    "DeletePeeringRequestTypeDef",
    "DeletePeeringResponseTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteSiteRequestTypeDef",
    "DeleteSiteResponseTypeDef",
    "DeregisterTransitGatewayRequestTypeDef",
    "DeregisterTransitGatewayResponseTypeDef",
    "DescribeGlobalNetworksRequestPaginateTypeDef",
    "DescribeGlobalNetworksRequestTypeDef",
    "DescribeGlobalNetworksResponseTypeDef",
    "DeviceTypeDef",
    "DirectConnectGatewayAttachmentTypeDef",
    "DisassociateConnectPeerRequestTypeDef",
    "DisassociateConnectPeerResponseTypeDef",
    "DisassociateCustomerGatewayRequestTypeDef",
    "DisassociateCustomerGatewayResponseTypeDef",
    "DisassociateLinkRequestTypeDef",
    "DisassociateLinkResponseTypeDef",
    "DisassociateTransitGatewayConnectPeerRequestTypeDef",
    "DisassociateTransitGatewayConnectPeerResponseTypeDef",
    "EdgeOverrideTypeDef",
    "ExecuteCoreNetworkChangeSetRequestTypeDef",
    "GetConnectAttachmentRequestTypeDef",
    "GetConnectAttachmentResponseTypeDef",
    "GetConnectPeerAssociationsRequestPaginateTypeDef",
    "GetConnectPeerAssociationsRequestTypeDef",
    "GetConnectPeerAssociationsResponseTypeDef",
    "GetConnectPeerRequestTypeDef",
    "GetConnectPeerResponseTypeDef",
    "GetConnectionsRequestPaginateTypeDef",
    "GetConnectionsRequestTypeDef",
    "GetConnectionsResponseTypeDef",
    "GetCoreNetworkChangeEventsRequestPaginateTypeDef",
    "GetCoreNetworkChangeEventsRequestTypeDef",
    "GetCoreNetworkChangeEventsResponseTypeDef",
    "GetCoreNetworkChangeSetRequestPaginateTypeDef",
    "GetCoreNetworkChangeSetRequestTypeDef",
    "GetCoreNetworkChangeSetResponseTypeDef",
    "GetCoreNetworkPolicyRequestTypeDef",
    "GetCoreNetworkPolicyResponseTypeDef",
    "GetCoreNetworkRequestTypeDef",
    "GetCoreNetworkResponseTypeDef",
    "GetCustomerGatewayAssociationsRequestPaginateTypeDef",
    "GetCustomerGatewayAssociationsRequestTypeDef",
    "GetCustomerGatewayAssociationsResponseTypeDef",
    "GetDevicesRequestPaginateTypeDef",
    "GetDevicesRequestTypeDef",
    "GetDevicesResponseTypeDef",
    "GetDirectConnectGatewayAttachmentRequestTypeDef",
    "GetDirectConnectGatewayAttachmentResponseTypeDef",
    "GetLinkAssociationsRequestPaginateTypeDef",
    "GetLinkAssociationsRequestTypeDef",
    "GetLinkAssociationsResponseTypeDef",
    "GetLinksRequestPaginateTypeDef",
    "GetLinksRequestTypeDef",
    "GetLinksResponseTypeDef",
    "GetNetworkResourceCountsRequestPaginateTypeDef",
    "GetNetworkResourceCountsRequestTypeDef",
    "GetNetworkResourceCountsResponseTypeDef",
    "GetNetworkResourceRelationshipsRequestPaginateTypeDef",
    "GetNetworkResourceRelationshipsRequestTypeDef",
    "GetNetworkResourceRelationshipsResponseTypeDef",
    "GetNetworkResourcesRequestPaginateTypeDef",
    "GetNetworkResourcesRequestTypeDef",
    "GetNetworkResourcesResponseTypeDef",
    "GetNetworkRoutesRequestTypeDef",
    "GetNetworkRoutesResponseTypeDef",
    "GetNetworkTelemetryRequestPaginateTypeDef",
    "GetNetworkTelemetryRequestTypeDef",
    "GetNetworkTelemetryResponseTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetRouteAnalysisRequestTypeDef",
    "GetRouteAnalysisResponseTypeDef",
    "GetSiteToSiteVpnAttachmentRequestTypeDef",
    "GetSiteToSiteVpnAttachmentResponseTypeDef",
    "GetSitesRequestPaginateTypeDef",
    "GetSitesRequestTypeDef",
    "GetSitesResponseTypeDef",
    "GetTransitGatewayConnectPeerAssociationsRequestPaginateTypeDef",
    "GetTransitGatewayConnectPeerAssociationsRequestTypeDef",
    "GetTransitGatewayConnectPeerAssociationsResponseTypeDef",
    "GetTransitGatewayPeeringRequestTypeDef",
    "GetTransitGatewayPeeringResponseTypeDef",
    "GetTransitGatewayRegistrationsRequestPaginateTypeDef",
    "GetTransitGatewayRegistrationsRequestTypeDef",
    "GetTransitGatewayRegistrationsResponseTypeDef",
    "GetTransitGatewayRouteTableAttachmentRequestTypeDef",
    "GetTransitGatewayRouteTableAttachmentResponseTypeDef",
    "GetVpcAttachmentRequestTypeDef",
    "GetVpcAttachmentResponseTypeDef",
    "GlobalNetworkTypeDef",
    "LinkAssociationTypeDef",
    "LinkTypeDef",
    "ListAttachmentsRequestPaginateTypeDef",
    "ListAttachmentsRequestTypeDef",
    "ListAttachmentsResponseTypeDef",
    "ListConnectPeersRequestPaginateTypeDef",
    "ListConnectPeersRequestTypeDef",
    "ListConnectPeersResponseTypeDef",
    "ListCoreNetworkPolicyVersionsRequestPaginateTypeDef",
    "ListCoreNetworkPolicyVersionsRequestTypeDef",
    "ListCoreNetworkPolicyVersionsResponseTypeDef",
    "ListCoreNetworksRequestPaginateTypeDef",
    "ListCoreNetworksRequestTypeDef",
    "ListCoreNetworksResponseTypeDef",
    "ListOrganizationServiceAccessStatusRequestTypeDef",
    "ListOrganizationServiceAccessStatusResponseTypeDef",
    "ListPeeringsRequestPaginateTypeDef",
    "ListPeeringsRequestTypeDef",
    "ListPeeringsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationTypeDef",
    "NetworkFunctionGroupTypeDef",
    "NetworkResourceCountTypeDef",
    "NetworkResourceSummaryTypeDef",
    "NetworkResourceTypeDef",
    "NetworkRouteDestinationTypeDef",
    "NetworkRouteTypeDef",
    "NetworkTelemetryTypeDef",
    "OrganizationStatusTypeDef",
    "PaginatorConfigTypeDef",
    "PathComponentTypeDef",
    "PeeringErrorTypeDef",
    "PeeringTypeDef",
    "PermissionsErrorContextTypeDef",
    "ProposedNetworkFunctionGroupChangeTypeDef",
    "ProposedSegmentChangeTypeDef",
    "PutCoreNetworkPolicyRequestTypeDef",
    "PutCoreNetworkPolicyResponseTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "RegisterTransitGatewayRequestTypeDef",
    "RegisterTransitGatewayResponseTypeDef",
    "RejectAttachmentRequestTypeDef",
    "RejectAttachmentResponseTypeDef",
    "RelationshipTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreCoreNetworkPolicyVersionRequestTypeDef",
    "RestoreCoreNetworkPolicyVersionResponseTypeDef",
    "RouteAnalysisCompletionTypeDef",
    "RouteAnalysisEndpointOptionsSpecificationTypeDef",
    "RouteAnalysisEndpointOptionsTypeDef",
    "RouteAnalysisPathTypeDef",
    "RouteAnalysisTypeDef",
    "RouteTableIdentifierTypeDef",
    "ServiceInsertionActionTypeDef",
    "ServiceInsertionSegmentsTypeDef",
    "SiteToSiteVpnAttachmentTypeDef",
    "SiteTypeDef",
    "StartOrganizationServiceAccessUpdateRequestTypeDef",
    "StartOrganizationServiceAccessUpdateResponseTypeDef",
    "StartRouteAnalysisRequestTypeDef",
    "StartRouteAnalysisResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TransitGatewayConnectPeerAssociationTypeDef",
    "TransitGatewayPeeringTypeDef",
    "TransitGatewayRegistrationStateReasonTypeDef",
    "TransitGatewayRegistrationTypeDef",
    "TransitGatewayRouteTableAttachmentTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateConnectionRequestTypeDef",
    "UpdateConnectionResponseTypeDef",
    "UpdateCoreNetworkRequestTypeDef",
    "UpdateCoreNetworkResponseTypeDef",
    "UpdateDeviceRequestTypeDef",
    "UpdateDeviceResponseTypeDef",
    "UpdateDirectConnectGatewayAttachmentRequestTypeDef",
    "UpdateDirectConnectGatewayAttachmentResponseTypeDef",
    "UpdateGlobalNetworkRequestTypeDef",
    "UpdateGlobalNetworkResponseTypeDef",
    "UpdateLinkRequestTypeDef",
    "UpdateLinkResponseTypeDef",
    "UpdateNetworkResourceMetadataRequestTypeDef",
    "UpdateNetworkResourceMetadataResponseTypeDef",
    "UpdateSiteRequestTypeDef",
    "UpdateSiteResponseTypeDef",
    "UpdateVpcAttachmentRequestTypeDef",
    "UpdateVpcAttachmentResponseTypeDef",
    "ViaTypeDef",
    "VpcAttachmentTypeDef",
    "VpcOptionsTypeDef",
    "WhenSentToTypeDef",
)

class AWSLocationTypeDef(TypedDict):
    Zone: NotRequired[str]
    SubnetArn: NotRequired[str]

class AcceptAttachmentRequestTypeDef(TypedDict):
    AttachmentId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AccountStatusTypeDef(TypedDict):
    AccountId: NotRequired[str]
    SLRDeploymentStatus: NotRequired[str]

class AssociateConnectPeerRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    ConnectPeerId: str
    DeviceId: str
    LinkId: NotRequired[str]

class ConnectPeerAssociationTypeDef(TypedDict):
    ConnectPeerId: NotRequired[str]
    GlobalNetworkId: NotRequired[str]
    DeviceId: NotRequired[str]
    LinkId: NotRequired[str]
    State: NotRequired[ConnectPeerAssociationStateType]

class AssociateCustomerGatewayRequestTypeDef(TypedDict):
    CustomerGatewayArn: str
    GlobalNetworkId: str
    DeviceId: str
    LinkId: NotRequired[str]

class CustomerGatewayAssociationTypeDef(TypedDict):
    CustomerGatewayArn: NotRequired[str]
    GlobalNetworkId: NotRequired[str]
    DeviceId: NotRequired[str]
    LinkId: NotRequired[str]
    State: NotRequired[CustomerGatewayAssociationStateType]

class AssociateLinkRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    DeviceId: str
    LinkId: str

class LinkAssociationTypeDef(TypedDict):
    GlobalNetworkId: NotRequired[str]
    DeviceId: NotRequired[str]
    LinkId: NotRequired[str]
    LinkAssociationState: NotRequired[LinkAssociationStateType]

class AssociateTransitGatewayConnectPeerRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArn: str
    DeviceId: str
    LinkId: NotRequired[str]

class TransitGatewayConnectPeerAssociationTypeDef(TypedDict):
    TransitGatewayConnectPeerArn: NotRequired[str]
    GlobalNetworkId: NotRequired[str]
    DeviceId: NotRequired[str]
    LinkId: NotRequired[str]
    State: NotRequired[TransitGatewayConnectPeerAssociationStateType]

class AttachmentErrorTypeDef(TypedDict):
    Code: NotRequired[AttachmentErrorCodeType]
    Message: NotRequired[str]
    ResourceArn: NotRequired[str]
    RequestId: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class BandwidthTypeDef(TypedDict):
    UploadSpeed: NotRequired[int]
    DownloadSpeed: NotRequired[int]

class BgpOptionsTypeDef(TypedDict):
    PeerAsn: NotRequired[int]

ConnectAttachmentOptionsTypeDef = TypedDict(
    "ConnectAttachmentOptionsTypeDef",
    {
        "Protocol": NotRequired[TunnelProtocolType],
    },
)

class ConnectPeerBgpConfigurationTypeDef(TypedDict):
    CoreNetworkAsn: NotRequired[int]
    PeerAsn: NotRequired[int]
    CoreNetworkAddress: NotRequired[str]
    PeerAddress: NotRequired[str]

class ConnectPeerErrorTypeDef(TypedDict):
    Code: NotRequired[ConnectPeerErrorCodeType]
    Message: NotRequired[str]
    ResourceArn: NotRequired[str]
    RequestId: NotRequired[str]

ConnectionHealthTypeDef = TypedDict(
    "ConnectionHealthTypeDef",
    {
        "Type": NotRequired[ConnectionTypeType],
        "Status": NotRequired[ConnectionStatusType],
        "Timestamp": NotRequired[datetime],
    },
)

class CoreNetworkChangeEventValuesTypeDef(TypedDict):
    EdgeLocation: NotRequired[str]
    SegmentName: NotRequired[str]
    NetworkFunctionGroupName: NotRequired[str]
    AttachmentId: NotRequired[str]
    Cidr: NotRequired[str]

class CoreNetworkEdgeTypeDef(TypedDict):
    EdgeLocation: NotRequired[str]
    Asn: NotRequired[int]
    InsideCidrBlocks: NotRequired[List[str]]

class CoreNetworkNetworkFunctionGroupIdentifierTypeDef(TypedDict):
    CoreNetworkId: NotRequired[str]
    NetworkFunctionGroupName: NotRequired[str]
    EdgeLocation: NotRequired[str]

class ServiceInsertionSegmentsTypeDef(TypedDict):
    SendVia: NotRequired[List[str]]
    SendTo: NotRequired[List[str]]

class CoreNetworkPolicyErrorTypeDef(TypedDict):
    ErrorCode: str
    Message: str
    Path: NotRequired[str]

class CoreNetworkPolicyVersionTypeDef(TypedDict):
    CoreNetworkId: NotRequired[str]
    PolicyVersionId: NotRequired[int]
    Alias: NotRequired[CoreNetworkPolicyAliasType]
    Description: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    ChangeSetState: NotRequired[ChangeSetStateType]

class CoreNetworkSegmentEdgeIdentifierTypeDef(TypedDict):
    CoreNetworkId: NotRequired[str]
    SegmentName: NotRequired[str]
    EdgeLocation: NotRequired[str]

class CoreNetworkSegmentTypeDef(TypedDict):
    Name: NotRequired[str]
    EdgeLocations: NotRequired[List[str]]
    SharedSegments: NotRequired[List[str]]

class LocationTypeDef(TypedDict):
    Address: NotRequired[str]
    Latitude: NotRequired[str]
    Longitude: NotRequired[str]

class VpcOptionsTypeDef(TypedDict):
    Ipv6Support: NotRequired[bool]
    ApplianceModeSupport: NotRequired[bool]

class DeleteAttachmentRequestTypeDef(TypedDict):
    AttachmentId: str

class DeleteConnectPeerRequestTypeDef(TypedDict):
    ConnectPeerId: str

class DeleteConnectionRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    ConnectionId: str

class DeleteCoreNetworkPolicyVersionRequestTypeDef(TypedDict):
    CoreNetworkId: str
    PolicyVersionId: int

class DeleteCoreNetworkRequestTypeDef(TypedDict):
    CoreNetworkId: str

class DeleteDeviceRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    DeviceId: str

class DeleteGlobalNetworkRequestTypeDef(TypedDict):
    GlobalNetworkId: str

class DeleteLinkRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    LinkId: str

class DeletePeeringRequestTypeDef(TypedDict):
    PeeringId: str

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: str

class DeleteSiteRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    SiteId: str

class DeregisterTransitGatewayRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    TransitGatewayArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeGlobalNetworksRequestTypeDef(TypedDict):
    GlobalNetworkIds: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class DisassociateConnectPeerRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    ConnectPeerId: str

class DisassociateCustomerGatewayRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    CustomerGatewayArn: str

class DisassociateLinkRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    DeviceId: str
    LinkId: str

class DisassociateTransitGatewayConnectPeerRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArn: str

class EdgeOverrideTypeDef(TypedDict):
    EdgeSets: NotRequired[List[List[str]]]
    UseEdge: NotRequired[str]

class ExecuteCoreNetworkChangeSetRequestTypeDef(TypedDict):
    CoreNetworkId: str
    PolicyVersionId: int

class GetConnectAttachmentRequestTypeDef(TypedDict):
    AttachmentId: str

class GetConnectPeerAssociationsRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    ConnectPeerIds: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetConnectPeerRequestTypeDef(TypedDict):
    ConnectPeerId: str

class GetConnectionsRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    ConnectionIds: NotRequired[Sequence[str]]
    DeviceId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetCoreNetworkChangeEventsRequestTypeDef(TypedDict):
    CoreNetworkId: str
    PolicyVersionId: int
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetCoreNetworkChangeSetRequestTypeDef(TypedDict):
    CoreNetworkId: str
    PolicyVersionId: int
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetCoreNetworkPolicyRequestTypeDef(TypedDict):
    CoreNetworkId: str
    PolicyVersionId: NotRequired[int]
    Alias: NotRequired[CoreNetworkPolicyAliasType]

class GetCoreNetworkRequestTypeDef(TypedDict):
    CoreNetworkId: str

class GetCustomerGatewayAssociationsRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    CustomerGatewayArns: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetDevicesRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    DeviceIds: NotRequired[Sequence[str]]
    SiteId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetDirectConnectGatewayAttachmentRequestTypeDef(TypedDict):
    AttachmentId: str

class GetLinkAssociationsRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    DeviceId: NotRequired[str]
    LinkId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

GetLinksRequestTypeDef = TypedDict(
    "GetLinksRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "LinkIds": NotRequired[Sequence[str]],
        "SiteId": NotRequired[str],
        "Type": NotRequired[str],
        "Provider": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

class GetNetworkResourceCountsRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    ResourceType: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class NetworkResourceCountTypeDef(TypedDict):
    ResourceType: NotRequired[str]
    Count: NotRequired[int]

class GetNetworkResourceRelationshipsRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    CoreNetworkId: NotRequired[str]
    RegisteredGatewayArn: NotRequired[str]
    AwsRegion: NotRequired[str]
    AccountId: NotRequired[str]
    ResourceType: NotRequired[str]
    ResourceArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class RelationshipTypeDef(TypedDict):
    From: NotRequired[str]
    To: NotRequired[str]

class GetNetworkResourcesRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    CoreNetworkId: NotRequired[str]
    RegisteredGatewayArn: NotRequired[str]
    AwsRegion: NotRequired[str]
    AccountId: NotRequired[str]
    ResourceType: NotRequired[str]
    ResourceArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetNetworkTelemetryRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    CoreNetworkId: NotRequired[str]
    RegisteredGatewayArn: NotRequired[str]
    AwsRegion: NotRequired[str]
    AccountId: NotRequired[str]
    ResourceType: NotRequired[str]
    ResourceArn: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: str

class GetRouteAnalysisRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    RouteAnalysisId: str

class GetSiteToSiteVpnAttachmentRequestTypeDef(TypedDict):
    AttachmentId: str

class GetSitesRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    SiteIds: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetTransitGatewayConnectPeerAssociationsRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArns: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetTransitGatewayPeeringRequestTypeDef(TypedDict):
    PeeringId: str

class GetTransitGatewayRegistrationsRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    TransitGatewayArns: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetTransitGatewayRouteTableAttachmentRequestTypeDef(TypedDict):
    AttachmentId: str

class GetVpcAttachmentRequestTypeDef(TypedDict):
    AttachmentId: str

class ListAttachmentsRequestTypeDef(TypedDict):
    CoreNetworkId: NotRequired[str]
    AttachmentType: NotRequired[AttachmentTypeType]
    EdgeLocation: NotRequired[str]
    State: NotRequired[AttachmentStateType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListConnectPeersRequestTypeDef(TypedDict):
    CoreNetworkId: NotRequired[str]
    ConnectAttachmentId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListCoreNetworkPolicyVersionsRequestTypeDef(TypedDict):
    CoreNetworkId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListCoreNetworksRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListOrganizationServiceAccessStatusRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListPeeringsRequestTypeDef(TypedDict):
    CoreNetworkId: NotRequired[str]
    PeeringType: NotRequired[Literal["TRANSIT_GATEWAY"]]
    EdgeLocation: NotRequired[str]
    State: NotRequired[PeeringStateType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class NetworkFunctionGroupTypeDef(TypedDict):
    Name: NotRequired[str]

class NetworkResourceSummaryTypeDef(TypedDict):
    RegisteredGatewayArn: NotRequired[str]
    ResourceArn: NotRequired[str]
    ResourceType: NotRequired[str]
    Definition: NotRequired[str]
    NameTag: NotRequired[str]
    IsMiddlebox: NotRequired[bool]

class NetworkRouteDestinationTypeDef(TypedDict):
    CoreNetworkAttachmentId: NotRequired[str]
    TransitGatewayAttachmentId: NotRequired[str]
    SegmentName: NotRequired[str]
    NetworkFunctionGroupName: NotRequired[str]
    EdgeLocation: NotRequired[str]
    ResourceType: NotRequired[str]
    ResourceId: NotRequired[str]

class PermissionsErrorContextTypeDef(TypedDict):
    MissingPermission: NotRequired[str]

class PutCoreNetworkPolicyRequestTypeDef(TypedDict):
    CoreNetworkId: str
    PolicyDocument: str
    Description: NotRequired[str]
    LatestVersionId: NotRequired[int]
    ClientToken: NotRequired[str]

class PutResourcePolicyRequestTypeDef(TypedDict):
    PolicyDocument: str
    ResourceArn: str

class RegisterTransitGatewayRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    TransitGatewayArn: str

class RejectAttachmentRequestTypeDef(TypedDict):
    AttachmentId: str

class RestoreCoreNetworkPolicyVersionRequestTypeDef(TypedDict):
    CoreNetworkId: str
    PolicyVersionId: int

class RouteAnalysisCompletionTypeDef(TypedDict):
    ResultCode: NotRequired[RouteAnalysisCompletionResultCodeType]
    ReasonCode: NotRequired[RouteAnalysisCompletionReasonCodeType]
    ReasonContext: NotRequired[Dict[str, str]]

class RouteAnalysisEndpointOptionsSpecificationTypeDef(TypedDict):
    TransitGatewayAttachmentArn: NotRequired[str]
    IpAddress: NotRequired[str]

class RouteAnalysisEndpointOptionsTypeDef(TypedDict):
    TransitGatewayAttachmentArn: NotRequired[str]
    TransitGatewayArn: NotRequired[str]
    IpAddress: NotRequired[str]

class WhenSentToTypeDef(TypedDict):
    WhenSentToSegmentsList: NotRequired[List[str]]

class StartOrganizationServiceAccessUpdateRequestTypeDef(TypedDict):
    Action: str

class TransitGatewayRegistrationStateReasonTypeDef(TypedDict):
    Code: NotRequired[TransitGatewayRegistrationStateType]
    Message: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateConnectionRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    ConnectionId: str
    LinkId: NotRequired[str]
    ConnectedLinkId: NotRequired[str]
    Description: NotRequired[str]

class UpdateCoreNetworkRequestTypeDef(TypedDict):
    CoreNetworkId: str
    Description: NotRequired[str]

class UpdateDirectConnectGatewayAttachmentRequestTypeDef(TypedDict):
    AttachmentId: str
    EdgeLocations: NotRequired[Sequence[str]]

class UpdateGlobalNetworkRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    Description: NotRequired[str]

class UpdateNetworkResourceMetadataRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    ResourceArn: str
    Metadata: Mapping[str, str]

class GetResourcePolicyResponseTypeDef(TypedDict):
    PolicyDocument: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNetworkResourceMetadataResponseTypeDef(TypedDict):
    ResourceArn: str
    Metadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class OrganizationStatusTypeDef(TypedDict):
    OrganizationId: NotRequired[str]
    OrganizationAwsServiceAccessStatus: NotRequired[str]
    SLRDeploymentStatus: NotRequired[str]
    AccountStatusList: NotRequired[List[AccountStatusTypeDef]]

class AssociateConnectPeerResponseTypeDef(TypedDict):
    ConnectPeerAssociation: ConnectPeerAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateConnectPeerResponseTypeDef(TypedDict):
    ConnectPeerAssociation: ConnectPeerAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectPeerAssociationsResponseTypeDef(TypedDict):
    ConnectPeerAssociations: List[ConnectPeerAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AssociateCustomerGatewayResponseTypeDef(TypedDict):
    CustomerGatewayAssociation: CustomerGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateCustomerGatewayResponseTypeDef(TypedDict):
    CustomerGatewayAssociation: CustomerGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCustomerGatewayAssociationsResponseTypeDef(TypedDict):
    CustomerGatewayAssociations: List[CustomerGatewayAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AssociateLinkResponseTypeDef(TypedDict):
    LinkAssociation: LinkAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateLinkResponseTypeDef(TypedDict):
    LinkAssociation: LinkAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLinkAssociationsResponseTypeDef(TypedDict):
    LinkAssociations: List[LinkAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AssociateTransitGatewayConnectPeerResponseTypeDef(TypedDict):
    TransitGatewayConnectPeerAssociation: TransitGatewayConnectPeerAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateTransitGatewayConnectPeerResponseTypeDef(TypedDict):
    TransitGatewayConnectPeerAssociation: TransitGatewayConnectPeerAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayConnectPeerAssociationsResponseTypeDef(TypedDict):
    TransitGatewayConnectPeerAssociations: List[TransitGatewayConnectPeerAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ConnectPeerSummaryTypeDef(TypedDict):
    CoreNetworkId: NotRequired[str]
    ConnectAttachmentId: NotRequired[str]
    ConnectPeerId: NotRequired[str]
    EdgeLocation: NotRequired[str]
    ConnectPeerState: NotRequired[ConnectPeerStateType]
    CreatedAt: NotRequired[datetime]
    Tags: NotRequired[List[TagTypeDef]]
    SubnetArn: NotRequired[str]

class ConnectionTypeDef(TypedDict):
    ConnectionId: NotRequired[str]
    ConnectionArn: NotRequired[str]
    GlobalNetworkId: NotRequired[str]
    DeviceId: NotRequired[str]
    ConnectedDeviceId: NotRequired[str]
    LinkId: NotRequired[str]
    ConnectedLinkId: NotRequired[str]
    Description: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    State: NotRequired[ConnectionStateType]
    Tags: NotRequired[List[TagTypeDef]]

class CoreNetworkSummaryTypeDef(TypedDict):
    CoreNetworkId: NotRequired[str]
    CoreNetworkArn: NotRequired[str]
    GlobalNetworkId: NotRequired[str]
    OwnerAccountId: NotRequired[str]
    State: NotRequired[CoreNetworkStateType]
    Description: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

class CreateConnectionRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    DeviceId: str
    ConnectedDeviceId: str
    LinkId: NotRequired[str]
    ConnectedLinkId: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateCoreNetworkRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    PolicyDocument: NotRequired[str]
    ClientToken: NotRequired[str]

class CreateDirectConnectGatewayAttachmentRequestTypeDef(TypedDict):
    CoreNetworkId: str
    DirectConnectGatewayArn: str
    EdgeLocations: Sequence[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

class CreateGlobalNetworkRequestTypeDef(TypedDict):
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateSiteToSiteVpnAttachmentRequestTypeDef(TypedDict):
    CoreNetworkId: str
    VpnConnectionArn: str
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

class CreateTransitGatewayPeeringRequestTypeDef(TypedDict):
    CoreNetworkId: str
    TransitGatewayArn: str
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

class CreateTransitGatewayRouteTableAttachmentRequestTypeDef(TypedDict):
    PeeringId: str
    TransitGatewayRouteTableArn: str
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

class GlobalNetworkTypeDef(TypedDict):
    GlobalNetworkId: NotRequired[str]
    GlobalNetworkArn: NotRequired[str]
    Description: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    State: NotRequired[GlobalNetworkStateType]
    Tags: NotRequired[List[TagTypeDef]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkResourceTypeDef(TypedDict):
    RegisteredGatewayArn: NotRequired[str]
    CoreNetworkId: NotRequired[str]
    AwsRegion: NotRequired[str]
    AccountId: NotRequired[str]
    ResourceType: NotRequired[str]
    ResourceId: NotRequired[str]
    ResourceArn: NotRequired[str]
    Definition: NotRequired[str]
    DefinitionTimestamp: NotRequired[datetime]
    Tags: NotRequired[List[TagTypeDef]]
    Metadata: NotRequired[Dict[str, str]]

class ProposedNetworkFunctionGroupChangeTypeDef(TypedDict):
    Tags: NotRequired[List[TagTypeDef]]
    AttachmentPolicyRuleNumber: NotRequired[int]
    NetworkFunctionGroupName: NotRequired[str]

class ProposedSegmentChangeTypeDef(TypedDict):
    Tags: NotRequired[List[TagTypeDef]]
    AttachmentPolicyRuleNumber: NotRequired[int]
    SegmentName: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

CreateLinkRequestTypeDef = TypedDict(
    "CreateLinkRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "Bandwidth": BandwidthTypeDef,
        "SiteId": str,
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Provider": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
LinkTypeDef = TypedDict(
    "LinkTypeDef",
    {
        "LinkId": NotRequired[str],
        "LinkArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "SiteId": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Bandwidth": NotRequired[BandwidthTypeDef],
        "Provider": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "State": NotRequired[LinkStateType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
UpdateLinkRequestTypeDef = TypedDict(
    "UpdateLinkRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "LinkId": str,
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Bandwidth": NotRequired[BandwidthTypeDef],
        "Provider": NotRequired[str],
    },
)

class CreateConnectPeerRequestTypeDef(TypedDict):
    ConnectAttachmentId: str
    PeerAddress: str
    CoreNetworkAddress: NotRequired[str]
    BgpOptions: NotRequired[BgpOptionsTypeDef]
    InsideCidrBlocks: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]
    SubnetArn: NotRequired[str]

class CreateConnectAttachmentRequestTypeDef(TypedDict):
    CoreNetworkId: str
    EdgeLocation: str
    TransportAttachmentId: str
    Options: ConnectAttachmentOptionsTypeDef
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

ConnectPeerConfigurationTypeDef = TypedDict(
    "ConnectPeerConfigurationTypeDef",
    {
        "CoreNetworkAddress": NotRequired[str],
        "PeerAddress": NotRequired[str],
        "InsideCidrBlocks": NotRequired[List[str]],
        "Protocol": NotRequired[TunnelProtocolType],
        "BgpConfigurations": NotRequired[List[ConnectPeerBgpConfigurationTypeDef]],
    },
)

class NetworkTelemetryTypeDef(TypedDict):
    RegisteredGatewayArn: NotRequired[str]
    CoreNetworkId: NotRequired[str]
    AwsRegion: NotRequired[str]
    AccountId: NotRequired[str]
    ResourceType: NotRequired[str]
    ResourceId: NotRequired[str]
    ResourceArn: NotRequired[str]
    Address: NotRequired[str]
    Health: NotRequired[ConnectionHealthTypeDef]

CoreNetworkChangeEventTypeDef = TypedDict(
    "CoreNetworkChangeEventTypeDef",
    {
        "Type": NotRequired[ChangeTypeType],
        "Action": NotRequired[ChangeActionType],
        "IdentifierPath": NotRequired[str],
        "EventTime": NotRequired[datetime],
        "Status": NotRequired[ChangeStatusType],
        "Values": NotRequired[CoreNetworkChangeEventValuesTypeDef],
    },
)

class CoreNetworkNetworkFunctionGroupTypeDef(TypedDict):
    Name: NotRequired[str]
    EdgeLocations: NotRequired[List[str]]
    Segments: NotRequired[ServiceInsertionSegmentsTypeDef]

class CoreNetworkPolicyTypeDef(TypedDict):
    CoreNetworkId: NotRequired[str]
    PolicyVersionId: NotRequired[int]
    Alias: NotRequired[CoreNetworkPolicyAliasType]
    Description: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    ChangeSetState: NotRequired[ChangeSetStateType]
    PolicyErrors: NotRequired[List[CoreNetworkPolicyErrorTypeDef]]
    PolicyDocument: NotRequired[str]

class ListCoreNetworkPolicyVersionsResponseTypeDef(TypedDict):
    CoreNetworkPolicyVersions: List[CoreNetworkPolicyVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RouteTableIdentifierTypeDef(TypedDict):
    TransitGatewayRouteTableArn: NotRequired[str]
    CoreNetworkSegmentEdge: NotRequired[CoreNetworkSegmentEdgeIdentifierTypeDef]
    CoreNetworkNetworkFunctionGroup: NotRequired[CoreNetworkNetworkFunctionGroupIdentifierTypeDef]

CreateDeviceRequestTypeDef = TypedDict(
    "CreateDeviceRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "AWSLocation": NotRequired[AWSLocationTypeDef],
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Vendor": NotRequired[str],
        "Model": NotRequired[str],
        "SerialNumber": NotRequired[str],
        "Location": NotRequired[LocationTypeDef],
        "SiteId": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)

class CreateSiteRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    Description: NotRequired[str]
    Location: NotRequired[LocationTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "DeviceId": NotRequired[str],
        "DeviceArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "AWSLocation": NotRequired[AWSLocationTypeDef],
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Vendor": NotRequired[str],
        "Model": NotRequired[str],
        "SerialNumber": NotRequired[str],
        "Location": NotRequired[LocationTypeDef],
        "SiteId": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "State": NotRequired[DeviceStateType],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)

class SiteTypeDef(TypedDict):
    SiteId: NotRequired[str]
    SiteArn: NotRequired[str]
    GlobalNetworkId: NotRequired[str]
    Description: NotRequired[str]
    Location: NotRequired[LocationTypeDef]
    CreatedAt: NotRequired[datetime]
    State: NotRequired[SiteStateType]
    Tags: NotRequired[List[TagTypeDef]]

UpdateDeviceRequestTypeDef = TypedDict(
    "UpdateDeviceRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "AWSLocation": NotRequired[AWSLocationTypeDef],
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Vendor": NotRequired[str],
        "Model": NotRequired[str],
        "SerialNumber": NotRequired[str],
        "Location": NotRequired[LocationTypeDef],
        "SiteId": NotRequired[str],
    },
)

class UpdateSiteRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    SiteId: str
    Description: NotRequired[str]
    Location: NotRequired[LocationTypeDef]

class CreateVpcAttachmentRequestTypeDef(TypedDict):
    CoreNetworkId: str
    VpcArn: str
    SubnetArns: Sequence[str]
    Options: NotRequired[VpcOptionsTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

class UpdateVpcAttachmentRequestTypeDef(TypedDict):
    AttachmentId: str
    AddSubnetArns: NotRequired[Sequence[str]]
    RemoveSubnetArns: NotRequired[Sequence[str]]
    Options: NotRequired[VpcOptionsTypeDef]

class DescribeGlobalNetworksRequestPaginateTypeDef(TypedDict):
    GlobalNetworkIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetConnectPeerAssociationsRequestPaginateTypeDef(TypedDict):
    GlobalNetworkId: str
    ConnectPeerIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetConnectionsRequestPaginateTypeDef(TypedDict):
    GlobalNetworkId: str
    ConnectionIds: NotRequired[Sequence[str]]
    DeviceId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetCoreNetworkChangeEventsRequestPaginateTypeDef(TypedDict):
    CoreNetworkId: str
    PolicyVersionId: int
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetCoreNetworkChangeSetRequestPaginateTypeDef(TypedDict):
    CoreNetworkId: str
    PolicyVersionId: int
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetCustomerGatewayAssociationsRequestPaginateTypeDef(TypedDict):
    GlobalNetworkId: str
    CustomerGatewayArns: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetDevicesRequestPaginateTypeDef(TypedDict):
    GlobalNetworkId: str
    DeviceIds: NotRequired[Sequence[str]]
    SiteId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetLinkAssociationsRequestPaginateTypeDef(TypedDict):
    GlobalNetworkId: str
    DeviceId: NotRequired[str]
    LinkId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

GetLinksRequestPaginateTypeDef = TypedDict(
    "GetLinksRequestPaginateTypeDef",
    {
        "GlobalNetworkId": str,
        "LinkIds": NotRequired[Sequence[str]],
        "SiteId": NotRequired[str],
        "Type": NotRequired[str],
        "Provider": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class GetNetworkResourceCountsRequestPaginateTypeDef(TypedDict):
    GlobalNetworkId: str
    ResourceType: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetNetworkResourceRelationshipsRequestPaginateTypeDef(TypedDict):
    GlobalNetworkId: str
    CoreNetworkId: NotRequired[str]
    RegisteredGatewayArn: NotRequired[str]
    AwsRegion: NotRequired[str]
    AccountId: NotRequired[str]
    ResourceType: NotRequired[str]
    ResourceArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetNetworkResourcesRequestPaginateTypeDef(TypedDict):
    GlobalNetworkId: str
    CoreNetworkId: NotRequired[str]
    RegisteredGatewayArn: NotRequired[str]
    AwsRegion: NotRequired[str]
    AccountId: NotRequired[str]
    ResourceType: NotRequired[str]
    ResourceArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetNetworkTelemetryRequestPaginateTypeDef(TypedDict):
    GlobalNetworkId: str
    CoreNetworkId: NotRequired[str]
    RegisteredGatewayArn: NotRequired[str]
    AwsRegion: NotRequired[str]
    AccountId: NotRequired[str]
    ResourceType: NotRequired[str]
    ResourceArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetSitesRequestPaginateTypeDef(TypedDict):
    GlobalNetworkId: str
    SiteIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetTransitGatewayConnectPeerAssociationsRequestPaginateTypeDef(TypedDict):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArns: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetTransitGatewayRegistrationsRequestPaginateTypeDef(TypedDict):
    GlobalNetworkId: str
    TransitGatewayArns: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAttachmentsRequestPaginateTypeDef(TypedDict):
    CoreNetworkId: NotRequired[str]
    AttachmentType: NotRequired[AttachmentTypeType]
    EdgeLocation: NotRequired[str]
    State: NotRequired[AttachmentStateType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConnectPeersRequestPaginateTypeDef(TypedDict):
    CoreNetworkId: NotRequired[str]
    ConnectAttachmentId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCoreNetworkPolicyVersionsRequestPaginateTypeDef(TypedDict):
    CoreNetworkId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCoreNetworksRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPeeringsRequestPaginateTypeDef(TypedDict):
    CoreNetworkId: NotRequired[str]
    PeeringType: NotRequired[Literal["TRANSIT_GATEWAY"]]
    EdgeLocation: NotRequired[str]
    State: NotRequired[PeeringStateType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetNetworkResourceCountsResponseTypeDef(TypedDict):
    NetworkResourceCounts: List[NetworkResourceCountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetNetworkResourceRelationshipsResponseTypeDef(TypedDict):
    Relationships: List[RelationshipTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ViaTypeDef(TypedDict):
    NetworkFunctionGroups: NotRequired[List[NetworkFunctionGroupTypeDef]]
    WithEdgeOverrides: NotRequired[List[EdgeOverrideTypeDef]]

PathComponentTypeDef = TypedDict(
    "PathComponentTypeDef",
    {
        "Sequence": NotRequired[int],
        "Resource": NotRequired[NetworkResourceSummaryTypeDef],
        "DestinationCidrBlock": NotRequired[str],
    },
)
NetworkRouteTypeDef = TypedDict(
    "NetworkRouteTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "Destinations": NotRequired[List[NetworkRouteDestinationTypeDef]],
        "PrefixListId": NotRequired[str],
        "State": NotRequired[RouteStateType],
        "Type": NotRequired[RouteTypeType],
    },
)

class PeeringErrorTypeDef(TypedDict):
    Code: NotRequired[PeeringErrorCodeType]
    Message: NotRequired[str]
    ResourceArn: NotRequired[str]
    RequestId: NotRequired[str]
    MissingPermissionsContext: NotRequired[PermissionsErrorContextTypeDef]

class StartRouteAnalysisRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    Source: RouteAnalysisEndpointOptionsSpecificationTypeDef
    Destination: RouteAnalysisEndpointOptionsSpecificationTypeDef
    IncludeReturnPath: NotRequired[bool]
    UseMiddleboxes: NotRequired[bool]

class TransitGatewayRegistrationTypeDef(TypedDict):
    GlobalNetworkId: NotRequired[str]
    TransitGatewayArn: NotRequired[str]
    State: NotRequired[TransitGatewayRegistrationStateReasonTypeDef]

class ListOrganizationServiceAccessStatusResponseTypeDef(TypedDict):
    OrganizationStatus: OrganizationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StartOrganizationServiceAccessUpdateResponseTypeDef(TypedDict):
    OrganizationStatus: OrganizationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectPeersResponseTypeDef(TypedDict):
    ConnectPeers: List[ConnectPeerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateConnectionResponseTypeDef(TypedDict):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConnectionResponseTypeDef(TypedDict):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionsResponseTypeDef(TypedDict):
    Connections: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateConnectionResponseTypeDef(TypedDict):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCoreNetworksResponseTypeDef(TypedDict):
    CoreNetworks: List[CoreNetworkSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateGlobalNetworkResponseTypeDef(TypedDict):
    GlobalNetwork: GlobalNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGlobalNetworkResponseTypeDef(TypedDict):
    GlobalNetwork: GlobalNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGlobalNetworksResponseTypeDef(TypedDict):
    GlobalNetworks: List[GlobalNetworkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateGlobalNetworkResponseTypeDef(TypedDict):
    GlobalNetwork: GlobalNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkResourcesResponseTypeDef(TypedDict):
    NetworkResources: List[NetworkResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AttachmentTypeDef(TypedDict):
    CoreNetworkId: NotRequired[str]
    CoreNetworkArn: NotRequired[str]
    AttachmentId: NotRequired[str]
    OwnerAccountId: NotRequired[str]
    AttachmentType: NotRequired[AttachmentTypeType]
    State: NotRequired[AttachmentStateType]
    EdgeLocation: NotRequired[str]
    EdgeLocations: NotRequired[List[str]]
    ResourceArn: NotRequired[str]
    AttachmentPolicyRuleNumber: NotRequired[int]
    SegmentName: NotRequired[str]
    NetworkFunctionGroupName: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    ProposedSegmentChange: NotRequired[ProposedSegmentChangeTypeDef]
    ProposedNetworkFunctionGroupChange: NotRequired[ProposedNetworkFunctionGroupChangeTypeDef]
    CreatedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]
    LastModificationErrors: NotRequired[List[AttachmentErrorTypeDef]]

class CreateLinkResponseTypeDef(TypedDict):
    Link: LinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLinkResponseTypeDef(TypedDict):
    Link: LinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLinksResponseTypeDef(TypedDict):
    Links: List[LinkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateLinkResponseTypeDef(TypedDict):
    Link: LinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectPeerTypeDef(TypedDict):
    CoreNetworkId: NotRequired[str]
    ConnectAttachmentId: NotRequired[str]
    ConnectPeerId: NotRequired[str]
    EdgeLocation: NotRequired[str]
    State: NotRequired[ConnectPeerStateType]
    CreatedAt: NotRequired[datetime]
    Configuration: NotRequired[ConnectPeerConfigurationTypeDef]
    Tags: NotRequired[List[TagTypeDef]]
    SubnetArn: NotRequired[str]
    LastModificationErrors: NotRequired[List[ConnectPeerErrorTypeDef]]

class GetNetworkTelemetryResponseTypeDef(TypedDict):
    NetworkTelemetry: List[NetworkTelemetryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetCoreNetworkChangeEventsResponseTypeDef(TypedDict):
    CoreNetworkChangeEvents: List[CoreNetworkChangeEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CoreNetworkTypeDef(TypedDict):
    GlobalNetworkId: NotRequired[str]
    CoreNetworkId: NotRequired[str]
    CoreNetworkArn: NotRequired[str]
    Description: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    State: NotRequired[CoreNetworkStateType]
    Segments: NotRequired[List[CoreNetworkSegmentTypeDef]]
    NetworkFunctionGroups: NotRequired[List[CoreNetworkNetworkFunctionGroupTypeDef]]
    Edges: NotRequired[List[CoreNetworkEdgeTypeDef]]
    Tags: NotRequired[List[TagTypeDef]]

class DeleteCoreNetworkPolicyVersionResponseTypeDef(TypedDict):
    CoreNetworkPolicy: CoreNetworkPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoreNetworkPolicyResponseTypeDef(TypedDict):
    CoreNetworkPolicy: CoreNetworkPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutCoreNetworkPolicyResponseTypeDef(TypedDict):
    CoreNetworkPolicy: CoreNetworkPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreCoreNetworkPolicyVersionResponseTypeDef(TypedDict):
    CoreNetworkPolicy: CoreNetworkPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkRoutesRequestTypeDef(TypedDict):
    GlobalNetworkId: str
    RouteTableIdentifier: RouteTableIdentifierTypeDef
    ExactCidrMatches: NotRequired[Sequence[str]]
    LongestPrefixMatches: NotRequired[Sequence[str]]
    SubnetOfMatches: NotRequired[Sequence[str]]
    SupernetOfMatches: NotRequired[Sequence[str]]
    PrefixListIds: NotRequired[Sequence[str]]
    States: NotRequired[Sequence[RouteStateType]]
    Types: NotRequired[Sequence[RouteTypeType]]
    DestinationFilters: NotRequired[Mapping[str, Sequence[str]]]

class CreateDeviceResponseTypeDef(TypedDict):
    Device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDeviceResponseTypeDef(TypedDict):
    Device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevicesResponseTypeDef(TypedDict):
    Devices: List[DeviceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateDeviceResponseTypeDef(TypedDict):
    Device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSiteResponseTypeDef(TypedDict):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSiteResponseTypeDef(TypedDict):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSitesResponseTypeDef(TypedDict):
    Sites: List[SiteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateSiteResponseTypeDef(TypedDict):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceInsertionActionTypeDef(TypedDict):
    Action: NotRequired[SegmentActionServiceInsertionType]
    Mode: NotRequired[SendViaModeType]
    WhenSentTo: NotRequired[WhenSentToTypeDef]
    Via: NotRequired[ViaTypeDef]

class RouteAnalysisPathTypeDef(TypedDict):
    CompletionStatus: NotRequired[RouteAnalysisCompletionTypeDef]
    Path: NotRequired[List[PathComponentTypeDef]]

class GetNetworkRoutesResponseTypeDef(TypedDict):
    RouteTableArn: str
    CoreNetworkSegmentEdge: CoreNetworkSegmentEdgeIdentifierTypeDef
    RouteTableType: RouteTableTypeType
    RouteTableTimestamp: datetime
    NetworkRoutes: List[NetworkRouteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PeeringTypeDef(TypedDict):
    CoreNetworkId: NotRequired[str]
    CoreNetworkArn: NotRequired[str]
    PeeringId: NotRequired[str]
    OwnerAccountId: NotRequired[str]
    PeeringType: NotRequired[Literal["TRANSIT_GATEWAY"]]
    State: NotRequired[PeeringStateType]
    EdgeLocation: NotRequired[str]
    ResourceArn: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    CreatedAt: NotRequired[datetime]
    LastModificationErrors: NotRequired[List[PeeringErrorTypeDef]]

class DeregisterTransitGatewayResponseTypeDef(TypedDict):
    TransitGatewayRegistration: TransitGatewayRegistrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayRegistrationsResponseTypeDef(TypedDict):
    TransitGatewayRegistrations: List[TransitGatewayRegistrationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RegisterTransitGatewayResponseTypeDef(TypedDict):
    TransitGatewayRegistration: TransitGatewayRegistrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptAttachmentResponseTypeDef(TypedDict):
    Attachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectAttachmentTypeDef(TypedDict):
    Attachment: NotRequired[AttachmentTypeDef]
    TransportAttachmentId: NotRequired[str]
    Options: NotRequired[ConnectAttachmentOptionsTypeDef]

class DeleteAttachmentResponseTypeDef(TypedDict):
    Attachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DirectConnectGatewayAttachmentTypeDef(TypedDict):
    Attachment: NotRequired[AttachmentTypeDef]
    DirectConnectGatewayArn: NotRequired[str]

class ListAttachmentsResponseTypeDef(TypedDict):
    Attachments: List[AttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RejectAttachmentResponseTypeDef(TypedDict):
    Attachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SiteToSiteVpnAttachmentTypeDef(TypedDict):
    Attachment: NotRequired[AttachmentTypeDef]
    VpnConnectionArn: NotRequired[str]

class TransitGatewayRouteTableAttachmentTypeDef(TypedDict):
    Attachment: NotRequired[AttachmentTypeDef]
    PeeringId: NotRequired[str]
    TransitGatewayRouteTableArn: NotRequired[str]

class VpcAttachmentTypeDef(TypedDict):
    Attachment: NotRequired[AttachmentTypeDef]
    SubnetArns: NotRequired[List[str]]
    Options: NotRequired[VpcOptionsTypeDef]

class CreateConnectPeerResponseTypeDef(TypedDict):
    ConnectPeer: ConnectPeerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConnectPeerResponseTypeDef(TypedDict):
    ConnectPeer: ConnectPeerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectPeerResponseTypeDef(TypedDict):
    ConnectPeer: ConnectPeerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCoreNetworkResponseTypeDef(TypedDict):
    CoreNetwork: CoreNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCoreNetworkResponseTypeDef(TypedDict):
    CoreNetwork: CoreNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoreNetworkResponseTypeDef(TypedDict):
    CoreNetwork: CoreNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCoreNetworkResponseTypeDef(TypedDict):
    CoreNetwork: CoreNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CoreNetworkChangeValuesTypeDef(TypedDict):
    SegmentName: NotRequired[str]
    NetworkFunctionGroupName: NotRequired[str]
    EdgeLocations: NotRequired[List[str]]
    Asn: NotRequired[int]
    Cidr: NotRequired[str]
    DestinationIdentifier: NotRequired[str]
    InsideCidrBlocks: NotRequired[List[str]]
    SharedSegments: NotRequired[List[str]]
    ServiceInsertionActions: NotRequired[List[ServiceInsertionActionTypeDef]]

class RouteAnalysisTypeDef(TypedDict):
    GlobalNetworkId: NotRequired[str]
    OwnerAccountId: NotRequired[str]
    RouteAnalysisId: NotRequired[str]
    StartTimestamp: NotRequired[datetime]
    Status: NotRequired[RouteAnalysisStatusType]
    Source: NotRequired[RouteAnalysisEndpointOptionsTypeDef]
    Destination: NotRequired[RouteAnalysisEndpointOptionsTypeDef]
    IncludeReturnPath: NotRequired[bool]
    UseMiddleboxes: NotRequired[bool]
    ForwardPath: NotRequired[RouteAnalysisPathTypeDef]
    ReturnPath: NotRequired[RouteAnalysisPathTypeDef]

class DeletePeeringResponseTypeDef(TypedDict):
    Peering: PeeringTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPeeringsResponseTypeDef(TypedDict):
    Peerings: List[PeeringTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TransitGatewayPeeringTypeDef(TypedDict):
    Peering: NotRequired[PeeringTypeDef]
    TransitGatewayArn: NotRequired[str]
    TransitGatewayPeeringAttachmentId: NotRequired[str]

class CreateConnectAttachmentResponseTypeDef(TypedDict):
    ConnectAttachment: ConnectAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectAttachmentResponseTypeDef(TypedDict):
    ConnectAttachment: ConnectAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDirectConnectGatewayAttachmentResponseTypeDef(TypedDict):
    DirectConnectGatewayAttachment: DirectConnectGatewayAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDirectConnectGatewayAttachmentResponseTypeDef(TypedDict):
    DirectConnectGatewayAttachment: DirectConnectGatewayAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDirectConnectGatewayAttachmentResponseTypeDef(TypedDict):
    DirectConnectGatewayAttachment: DirectConnectGatewayAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSiteToSiteVpnAttachmentResponseTypeDef(TypedDict):
    SiteToSiteVpnAttachment: SiteToSiteVpnAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSiteToSiteVpnAttachmentResponseTypeDef(TypedDict):
    SiteToSiteVpnAttachment: SiteToSiteVpnAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitGatewayRouteTableAttachmentResponseTypeDef(TypedDict):
    TransitGatewayRouteTableAttachment: TransitGatewayRouteTableAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayRouteTableAttachmentResponseTypeDef(TypedDict):
    TransitGatewayRouteTableAttachment: TransitGatewayRouteTableAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcAttachmentResponseTypeDef(TypedDict):
    VpcAttachment: VpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVpcAttachmentResponseTypeDef(TypedDict):
    VpcAttachment: VpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVpcAttachmentResponseTypeDef(TypedDict):
    VpcAttachment: VpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CoreNetworkChangeTypeDef = TypedDict(
    "CoreNetworkChangeTypeDef",
    {
        "Type": NotRequired[ChangeTypeType],
        "Action": NotRequired[ChangeActionType],
        "Identifier": NotRequired[str],
        "PreviousValues": NotRequired[CoreNetworkChangeValuesTypeDef],
        "NewValues": NotRequired[CoreNetworkChangeValuesTypeDef],
        "IdentifierPath": NotRequired[str],
    },
)

class GetRouteAnalysisResponseTypeDef(TypedDict):
    RouteAnalysis: RouteAnalysisTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartRouteAnalysisResponseTypeDef(TypedDict):
    RouteAnalysis: RouteAnalysisTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitGatewayPeeringResponseTypeDef(TypedDict):
    TransitGatewayPeering: TransitGatewayPeeringTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayPeeringResponseTypeDef(TypedDict):
    TransitGatewayPeering: TransitGatewayPeeringTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoreNetworkChangeSetResponseTypeDef(TypedDict):
    CoreNetworkChanges: List[CoreNetworkChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
