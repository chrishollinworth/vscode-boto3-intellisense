"""
Type annotations for networkmanager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_networkmanager.type_defs import AWSLocationTypeDef

    data: AWSLocationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AttachmentStateType,
    AttachmentTypeType,
    ChangeActionType,
    ChangeSetStateType,
    ChangeTypeType,
    ConnectionStateType,
    ConnectionStatusType,
    ConnectionTypeType,
    ConnectPeerAssociationStateType,
    ConnectPeerStateType,
    CoreNetworkPolicyAliasType,
    CoreNetworkStateType,
    CustomerGatewayAssociationStateType,
    DeviceStateType,
    GlobalNetworkStateType,
    LinkAssociationStateType,
    LinkStateType,
    RouteAnalysisCompletionReasonCodeType,
    RouteAnalysisCompletionResultCodeType,
    RouteAnalysisStatusType,
    RouteStateType,
    RouteTableTypeType,
    RouteTypeType,
    SiteStateType,
    TransitGatewayConnectPeerAssociationStateType,
    TransitGatewayRegistrationStateType,
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
    "AWSLocationTypeDef",
    "AcceptAttachmentRequestRequestTypeDef",
    "AcceptAttachmentResponseTypeDef",
    "AccountStatusTypeDef",
    "AssociateConnectPeerRequestRequestTypeDef",
    "AssociateConnectPeerResponseTypeDef",
    "AssociateCustomerGatewayRequestRequestTypeDef",
    "AssociateCustomerGatewayResponseTypeDef",
    "AssociateLinkRequestRequestTypeDef",
    "AssociateLinkResponseTypeDef",
    "AssociateTransitGatewayConnectPeerRequestRequestTypeDef",
    "AssociateTransitGatewayConnectPeerResponseTypeDef",
    "AttachmentTypeDef",
    "BandwidthTypeDef",
    "BgpOptionsTypeDef",
    "ConnectAttachmentOptionsTypeDef",
    "ConnectAttachmentTypeDef",
    "ConnectPeerAssociationTypeDef",
    "ConnectPeerBgpConfigurationTypeDef",
    "ConnectPeerConfigurationTypeDef",
    "ConnectPeerSummaryTypeDef",
    "ConnectPeerTypeDef",
    "ConnectionHealthTypeDef",
    "ConnectionTypeDef",
    "CoreNetworkChangeTypeDef",
    "CoreNetworkChangeValuesTypeDef",
    "CoreNetworkEdgeTypeDef",
    "CoreNetworkPolicyErrorTypeDef",
    "CoreNetworkPolicyTypeDef",
    "CoreNetworkPolicyVersionTypeDef",
    "CoreNetworkSegmentEdgeIdentifierTypeDef",
    "CoreNetworkSegmentTypeDef",
    "CoreNetworkSummaryTypeDef",
    "CoreNetworkTypeDef",
    "CreateConnectAttachmentRequestRequestTypeDef",
    "CreateConnectAttachmentResponseTypeDef",
    "CreateConnectPeerRequestRequestTypeDef",
    "CreateConnectPeerResponseTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "CreateConnectionResponseTypeDef",
    "CreateCoreNetworkRequestRequestTypeDef",
    "CreateCoreNetworkResponseTypeDef",
    "CreateDeviceRequestRequestTypeDef",
    "CreateDeviceResponseTypeDef",
    "CreateGlobalNetworkRequestRequestTypeDef",
    "CreateGlobalNetworkResponseTypeDef",
    "CreateLinkRequestRequestTypeDef",
    "CreateLinkResponseTypeDef",
    "CreateSiteRequestRequestTypeDef",
    "CreateSiteResponseTypeDef",
    "CreateSiteToSiteVpnAttachmentRequestRequestTypeDef",
    "CreateSiteToSiteVpnAttachmentResponseTypeDef",
    "CreateVpcAttachmentRequestRequestTypeDef",
    "CreateVpcAttachmentResponseTypeDef",
    "CustomerGatewayAssociationTypeDef",
    "DeleteAttachmentRequestRequestTypeDef",
    "DeleteAttachmentResponseTypeDef",
    "DeleteConnectPeerRequestRequestTypeDef",
    "DeleteConnectPeerResponseTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteCoreNetworkPolicyVersionRequestRequestTypeDef",
    "DeleteCoreNetworkPolicyVersionResponseTypeDef",
    "DeleteCoreNetworkRequestRequestTypeDef",
    "DeleteCoreNetworkResponseTypeDef",
    "DeleteDeviceRequestRequestTypeDef",
    "DeleteDeviceResponseTypeDef",
    "DeleteGlobalNetworkRequestRequestTypeDef",
    "DeleteGlobalNetworkResponseTypeDef",
    "DeleteLinkRequestRequestTypeDef",
    "DeleteLinkResponseTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteSiteRequestRequestTypeDef",
    "DeleteSiteResponseTypeDef",
    "DeregisterTransitGatewayRequestRequestTypeDef",
    "DeregisterTransitGatewayResponseTypeDef",
    "DescribeGlobalNetworksRequestRequestTypeDef",
    "DescribeGlobalNetworksResponseTypeDef",
    "DeviceTypeDef",
    "DisassociateConnectPeerRequestRequestTypeDef",
    "DisassociateConnectPeerResponseTypeDef",
    "DisassociateCustomerGatewayRequestRequestTypeDef",
    "DisassociateCustomerGatewayResponseTypeDef",
    "DisassociateLinkRequestRequestTypeDef",
    "DisassociateLinkResponseTypeDef",
    "DisassociateTransitGatewayConnectPeerRequestRequestTypeDef",
    "DisassociateTransitGatewayConnectPeerResponseTypeDef",
    "ExecuteCoreNetworkChangeSetRequestRequestTypeDef",
    "GetConnectAttachmentRequestRequestTypeDef",
    "GetConnectAttachmentResponseTypeDef",
    "GetConnectPeerAssociationsRequestRequestTypeDef",
    "GetConnectPeerAssociationsResponseTypeDef",
    "GetConnectPeerRequestRequestTypeDef",
    "GetConnectPeerResponseTypeDef",
    "GetConnectionsRequestRequestTypeDef",
    "GetConnectionsResponseTypeDef",
    "GetCoreNetworkChangeSetRequestRequestTypeDef",
    "GetCoreNetworkChangeSetResponseTypeDef",
    "GetCoreNetworkPolicyRequestRequestTypeDef",
    "GetCoreNetworkPolicyResponseTypeDef",
    "GetCoreNetworkRequestRequestTypeDef",
    "GetCoreNetworkResponseTypeDef",
    "GetCustomerGatewayAssociationsRequestRequestTypeDef",
    "GetCustomerGatewayAssociationsResponseTypeDef",
    "GetDevicesRequestRequestTypeDef",
    "GetDevicesResponseTypeDef",
    "GetLinkAssociationsRequestRequestTypeDef",
    "GetLinkAssociationsResponseTypeDef",
    "GetLinksRequestRequestTypeDef",
    "GetLinksResponseTypeDef",
    "GetNetworkResourceCountsRequestRequestTypeDef",
    "GetNetworkResourceCountsResponseTypeDef",
    "GetNetworkResourceRelationshipsRequestRequestTypeDef",
    "GetNetworkResourceRelationshipsResponseTypeDef",
    "GetNetworkResourcesRequestRequestTypeDef",
    "GetNetworkResourcesResponseTypeDef",
    "GetNetworkRoutesRequestRequestTypeDef",
    "GetNetworkRoutesResponseTypeDef",
    "GetNetworkTelemetryRequestRequestTypeDef",
    "GetNetworkTelemetryResponseTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetRouteAnalysisRequestRequestTypeDef",
    "GetRouteAnalysisResponseTypeDef",
    "GetSiteToSiteVpnAttachmentRequestRequestTypeDef",
    "GetSiteToSiteVpnAttachmentResponseTypeDef",
    "GetSitesRequestRequestTypeDef",
    "GetSitesResponseTypeDef",
    "GetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef",
    "GetTransitGatewayConnectPeerAssociationsResponseTypeDef",
    "GetTransitGatewayRegistrationsRequestRequestTypeDef",
    "GetTransitGatewayRegistrationsResponseTypeDef",
    "GetVpcAttachmentRequestRequestTypeDef",
    "GetVpcAttachmentResponseTypeDef",
    "GlobalNetworkTypeDef",
    "LinkAssociationTypeDef",
    "LinkTypeDef",
    "ListAttachmentsRequestRequestTypeDef",
    "ListAttachmentsResponseTypeDef",
    "ListConnectPeersRequestRequestTypeDef",
    "ListConnectPeersResponseTypeDef",
    "ListCoreNetworkPolicyVersionsRequestRequestTypeDef",
    "ListCoreNetworkPolicyVersionsResponseTypeDef",
    "ListCoreNetworksRequestRequestTypeDef",
    "ListCoreNetworksResponseTypeDef",
    "ListOrganizationServiceAccessStatusRequestRequestTypeDef",
    "ListOrganizationServiceAccessStatusResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationTypeDef",
    "NetworkResourceCountTypeDef",
    "NetworkResourceSummaryTypeDef",
    "NetworkResourceTypeDef",
    "NetworkRouteDestinationTypeDef",
    "NetworkRouteTypeDef",
    "NetworkTelemetryTypeDef",
    "OrganizationStatusTypeDef",
    "PaginatorConfigTypeDef",
    "PathComponentTypeDef",
    "ProposedSegmentChangeTypeDef",
    "PutCoreNetworkPolicyRequestRequestTypeDef",
    "PutCoreNetworkPolicyResponseTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "RegisterTransitGatewayRequestRequestTypeDef",
    "RegisterTransitGatewayResponseTypeDef",
    "RejectAttachmentRequestRequestTypeDef",
    "RejectAttachmentResponseTypeDef",
    "RelationshipTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreCoreNetworkPolicyVersionRequestRequestTypeDef",
    "RestoreCoreNetworkPolicyVersionResponseTypeDef",
    "RouteAnalysisCompletionTypeDef",
    "RouteAnalysisEndpointOptionsSpecificationTypeDef",
    "RouteAnalysisEndpointOptionsTypeDef",
    "RouteAnalysisPathTypeDef",
    "RouteAnalysisTypeDef",
    "RouteTableIdentifierTypeDef",
    "SiteToSiteVpnAttachmentTypeDef",
    "SiteTypeDef",
    "StartOrganizationServiceAccessUpdateRequestRequestTypeDef",
    "StartOrganizationServiceAccessUpdateResponseTypeDef",
    "StartRouteAnalysisRequestRequestTypeDef",
    "StartRouteAnalysisResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TransitGatewayConnectPeerAssociationTypeDef",
    "TransitGatewayRegistrationStateReasonTypeDef",
    "TransitGatewayRegistrationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConnectionRequestRequestTypeDef",
    "UpdateConnectionResponseTypeDef",
    "UpdateCoreNetworkRequestRequestTypeDef",
    "UpdateCoreNetworkResponseTypeDef",
    "UpdateDeviceRequestRequestTypeDef",
    "UpdateDeviceResponseTypeDef",
    "UpdateGlobalNetworkRequestRequestTypeDef",
    "UpdateGlobalNetworkResponseTypeDef",
    "UpdateLinkRequestRequestTypeDef",
    "UpdateLinkResponseTypeDef",
    "UpdateNetworkResourceMetadataRequestRequestTypeDef",
    "UpdateNetworkResourceMetadataResponseTypeDef",
    "UpdateSiteRequestRequestTypeDef",
    "UpdateSiteResponseTypeDef",
    "UpdateVpcAttachmentRequestRequestTypeDef",
    "UpdateVpcAttachmentResponseTypeDef",
    "VpcAttachmentTypeDef",
    "VpcOptionsTypeDef",
)

AWSLocationTypeDef = TypedDict(
    "AWSLocationTypeDef",
    {
        "Zone": str,
        "SubnetArn": str,
    },
    total=False,
)

AcceptAttachmentRequestRequestTypeDef = TypedDict(
    "AcceptAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)

AcceptAttachmentResponseTypeDef = TypedDict(
    "AcceptAttachmentResponseTypeDef",
    {
        "Attachment": "AttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccountStatusTypeDef = TypedDict(
    "AccountStatusTypeDef",
    {
        "AccountId": str,
        "SLRDeploymentStatus": str,
    },
    total=False,
)

_RequiredAssociateConnectPeerRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateConnectPeerRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectPeerId": str,
        "DeviceId": str,
    },
)
_OptionalAssociateConnectPeerRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateConnectPeerRequestRequestTypeDef",
    {
        "LinkId": str,
    },
    total=False,
)

class AssociateConnectPeerRequestRequestTypeDef(
    _RequiredAssociateConnectPeerRequestRequestTypeDef,
    _OptionalAssociateConnectPeerRequestRequestTypeDef,
):
    pass

AssociateConnectPeerResponseTypeDef = TypedDict(
    "AssociateConnectPeerResponseTypeDef",
    {
        "ConnectPeerAssociation": "ConnectPeerAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateCustomerGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateCustomerGatewayRequestRequestTypeDef",
    {
        "CustomerGatewayArn": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
    },
)
_OptionalAssociateCustomerGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateCustomerGatewayRequestRequestTypeDef",
    {
        "LinkId": str,
    },
    total=False,
)

class AssociateCustomerGatewayRequestRequestTypeDef(
    _RequiredAssociateCustomerGatewayRequestRequestTypeDef,
    _OptionalAssociateCustomerGatewayRequestRequestTypeDef,
):
    pass

AssociateCustomerGatewayResponseTypeDef = TypedDict(
    "AssociateCustomerGatewayResponseTypeDef",
    {
        "CustomerGatewayAssociation": "CustomerGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateLinkRequestRequestTypeDef = TypedDict(
    "AssociateLinkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
    },
)

AssociateLinkResponseTypeDef = TypedDict(
    "AssociateLinkResponseTypeDef",
    {
        "LinkAssociation": "LinkAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateTransitGatewayConnectPeerRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateTransitGatewayConnectPeerRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayConnectPeerArn": str,
        "DeviceId": str,
    },
)
_OptionalAssociateTransitGatewayConnectPeerRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateTransitGatewayConnectPeerRequestRequestTypeDef",
    {
        "LinkId": str,
    },
    total=False,
)

class AssociateTransitGatewayConnectPeerRequestRequestTypeDef(
    _RequiredAssociateTransitGatewayConnectPeerRequestRequestTypeDef,
    _OptionalAssociateTransitGatewayConnectPeerRequestRequestTypeDef,
):
    pass

AssociateTransitGatewayConnectPeerResponseTypeDef = TypedDict(
    "AssociateTransitGatewayConnectPeerResponseTypeDef",
    {
        "TransitGatewayConnectPeerAssociation": "TransitGatewayConnectPeerAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "CoreNetworkId": str,
        "CoreNetworkArn": str,
        "AttachmentId": str,
        "OwnerAccountId": str,
        "AttachmentType": AttachmentTypeType,
        "State": AttachmentStateType,
        "EdgeLocation": str,
        "ResourceArn": str,
        "AttachmentPolicyRuleNumber": int,
        "SegmentName": str,
        "Tags": List["TagTypeDef"],
        "ProposedSegmentChange": "ProposedSegmentChangeTypeDef",
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
    },
    total=False,
)

BandwidthTypeDef = TypedDict(
    "BandwidthTypeDef",
    {
        "UploadSpeed": int,
        "DownloadSpeed": int,
    },
    total=False,
)

BgpOptionsTypeDef = TypedDict(
    "BgpOptionsTypeDef",
    {
        "PeerAsn": int,
    },
    total=False,
)

ConnectAttachmentOptionsTypeDef = TypedDict(
    "ConnectAttachmentOptionsTypeDef",
    {
        "Protocol": Literal["GRE"],
    },
    total=False,
)

ConnectAttachmentTypeDef = TypedDict(
    "ConnectAttachmentTypeDef",
    {
        "Attachment": "AttachmentTypeDef",
        "TransportAttachmentId": str,
        "Options": "ConnectAttachmentOptionsTypeDef",
    },
    total=False,
)

ConnectPeerAssociationTypeDef = TypedDict(
    "ConnectPeerAssociationTypeDef",
    {
        "ConnectPeerId": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "State": ConnectPeerAssociationStateType,
    },
    total=False,
)

ConnectPeerBgpConfigurationTypeDef = TypedDict(
    "ConnectPeerBgpConfigurationTypeDef",
    {
        "CoreNetworkAsn": int,
        "PeerAsn": int,
        "CoreNetworkAddress": str,
        "PeerAddress": str,
    },
    total=False,
)

ConnectPeerConfigurationTypeDef = TypedDict(
    "ConnectPeerConfigurationTypeDef",
    {
        "CoreNetworkAddress": str,
        "PeerAddress": str,
        "InsideCidrBlocks": List[str],
        "Protocol": Literal["GRE"],
        "BgpConfigurations": List["ConnectPeerBgpConfigurationTypeDef"],
    },
    total=False,
)

ConnectPeerSummaryTypeDef = TypedDict(
    "ConnectPeerSummaryTypeDef",
    {
        "CoreNetworkId": str,
        "ConnectAttachmentId": str,
        "ConnectPeerId": str,
        "EdgeLocation": str,
        "ConnectPeerState": ConnectPeerStateType,
        "CreatedAt": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ConnectPeerTypeDef = TypedDict(
    "ConnectPeerTypeDef",
    {
        "CoreNetworkId": str,
        "ConnectAttachmentId": str,
        "ConnectPeerId": str,
        "EdgeLocation": str,
        "State": ConnectPeerStateType,
        "CreatedAt": datetime,
        "Configuration": "ConnectPeerConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ConnectionHealthTypeDef = TypedDict(
    "ConnectionHealthTypeDef",
    {
        "Type": ConnectionTypeType,
        "Status": ConnectionStatusType,
        "Timestamp": datetime,
    },
    total=False,
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionId": str,
        "ConnectionArn": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
        "ConnectedDeviceId": str,
        "LinkId": str,
        "ConnectedLinkId": str,
        "Description": str,
        "CreatedAt": datetime,
        "State": ConnectionStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CoreNetworkChangeTypeDef = TypedDict(
    "CoreNetworkChangeTypeDef",
    {
        "Type": ChangeTypeType,
        "Action": ChangeActionType,
        "Identifier": str,
        "PreviousValues": "CoreNetworkChangeValuesTypeDef",
        "NewValues": "CoreNetworkChangeValuesTypeDef",
    },
    total=False,
)

CoreNetworkChangeValuesTypeDef = TypedDict(
    "CoreNetworkChangeValuesTypeDef",
    {
        "SegmentName": str,
        "EdgeLocations": List[str],
        "Asn": int,
        "Cidr": str,
        "DestinationIdentifier": str,
        "InsideCidrBlocks": List[str],
        "SharedSegments": List[str],
    },
    total=False,
)

CoreNetworkEdgeTypeDef = TypedDict(
    "CoreNetworkEdgeTypeDef",
    {
        "EdgeLocation": str,
        "Asn": int,
        "InsideCidrBlocks": List[str],
    },
    total=False,
)

_RequiredCoreNetworkPolicyErrorTypeDef = TypedDict(
    "_RequiredCoreNetworkPolicyErrorTypeDef",
    {
        "ErrorCode": str,
        "Message": str,
    },
)
_OptionalCoreNetworkPolicyErrorTypeDef = TypedDict(
    "_OptionalCoreNetworkPolicyErrorTypeDef",
    {
        "Path": str,
    },
    total=False,
)

class CoreNetworkPolicyErrorTypeDef(
    _RequiredCoreNetworkPolicyErrorTypeDef, _OptionalCoreNetworkPolicyErrorTypeDef
):
    pass

CoreNetworkPolicyTypeDef = TypedDict(
    "CoreNetworkPolicyTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
        "Alias": CoreNetworkPolicyAliasType,
        "Description": str,
        "CreatedAt": datetime,
        "ChangeSetState": ChangeSetStateType,
        "PolicyErrors": List["CoreNetworkPolicyErrorTypeDef"],
        "PolicyDocument": str,
    },
    total=False,
)

CoreNetworkPolicyVersionTypeDef = TypedDict(
    "CoreNetworkPolicyVersionTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
        "Alias": CoreNetworkPolicyAliasType,
        "Description": str,
        "CreatedAt": datetime,
        "ChangeSetState": ChangeSetStateType,
    },
    total=False,
)

CoreNetworkSegmentEdgeIdentifierTypeDef = TypedDict(
    "CoreNetworkSegmentEdgeIdentifierTypeDef",
    {
        "CoreNetworkId": str,
        "SegmentName": str,
        "EdgeLocation": str,
    },
    total=False,
)

CoreNetworkSegmentTypeDef = TypedDict(
    "CoreNetworkSegmentTypeDef",
    {
        "Name": str,
        "EdgeLocations": List[str],
        "SharedSegments": List[str],
    },
    total=False,
)

CoreNetworkSummaryTypeDef = TypedDict(
    "CoreNetworkSummaryTypeDef",
    {
        "CoreNetworkId": str,
        "CoreNetworkArn": str,
        "GlobalNetworkId": str,
        "OwnerAccountId": str,
        "State": CoreNetworkStateType,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CoreNetworkTypeDef = TypedDict(
    "CoreNetworkTypeDef",
    {
        "GlobalNetworkId": str,
        "CoreNetworkId": str,
        "CoreNetworkArn": str,
        "Description": str,
        "CreatedAt": datetime,
        "State": CoreNetworkStateType,
        "Segments": List["CoreNetworkSegmentTypeDef"],
        "Edges": List["CoreNetworkEdgeTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredCreateConnectAttachmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectAttachmentRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "EdgeLocation": str,
        "TransportAttachmentId": str,
        "Options": "ConnectAttachmentOptionsTypeDef",
    },
)
_OptionalCreateConnectAttachmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectAttachmentRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreateConnectAttachmentRequestRequestTypeDef(
    _RequiredCreateConnectAttachmentRequestRequestTypeDef,
    _OptionalCreateConnectAttachmentRequestRequestTypeDef,
):
    pass

CreateConnectAttachmentResponseTypeDef = TypedDict(
    "CreateConnectAttachmentResponseTypeDef",
    {
        "ConnectAttachment": "ConnectAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConnectPeerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectPeerRequestRequestTypeDef",
    {
        "ConnectAttachmentId": str,
        "PeerAddress": str,
        "InsideCidrBlocks": List[str],
    },
)
_OptionalCreateConnectPeerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectPeerRequestRequestTypeDef",
    {
        "CoreNetworkAddress": str,
        "BgpOptions": "BgpOptionsTypeDef",
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreateConnectPeerRequestRequestTypeDef(
    _RequiredCreateConnectPeerRequestRequestTypeDef, _OptionalCreateConnectPeerRequestRequestTypeDef
):
    pass

CreateConnectPeerResponseTypeDef = TypedDict(
    "CreateConnectPeerResponseTypeDef",
    {
        "ConnectPeer": "ConnectPeerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "ConnectedDeviceId": str,
    },
)
_OptionalCreateConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionRequestRequestTypeDef",
    {
        "LinkId": str,
        "ConnectedLinkId": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateConnectionRequestRequestTypeDef(
    _RequiredCreateConnectionRequestRequestTypeDef, _OptionalCreateConnectionRequestRequestTypeDef
):
    pass

CreateConnectionResponseTypeDef = TypedDict(
    "CreateConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCoreNetworkRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCoreNetworkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalCreateCoreNetworkRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCoreNetworkRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
        "PolicyDocument": str,
        "ClientToken": str,
    },
    total=False,
)

class CreateCoreNetworkRequestRequestTypeDef(
    _RequiredCreateCoreNetworkRequestRequestTypeDef, _OptionalCreateCoreNetworkRequestRequestTypeDef
):
    pass

CreateCoreNetworkResponseTypeDef = TypedDict(
    "CreateCoreNetworkResponseTypeDef",
    {
        "CoreNetwork": "CoreNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDeviceRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalCreateDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDeviceRequestRequestTypeDef",
    {
        "AWSLocation": "AWSLocationTypeDef",
        "Description": str,
        "Type": str,
        "Vendor": str,
        "Model": str,
        "SerialNumber": str,
        "Location": "LocationTypeDef",
        "SiteId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDeviceRequestRequestTypeDef(
    _RequiredCreateDeviceRequestRequestTypeDef, _OptionalCreateDeviceRequestRequestTypeDef
):
    pass

CreateDeviceResponseTypeDef = TypedDict(
    "CreateDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGlobalNetworkRequestRequestTypeDef = TypedDict(
    "CreateGlobalNetworkRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CreateGlobalNetworkResponseTypeDef = TypedDict(
    "CreateGlobalNetworkResponseTypeDef",
    {
        "GlobalNetwork": "GlobalNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLinkRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLinkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "Bandwidth": "BandwidthTypeDef",
        "SiteId": str,
    },
)
_OptionalCreateLinkRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLinkRequestRequestTypeDef",
    {
        "Description": str,
        "Type": str,
        "Provider": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateLinkRequestRequestTypeDef(
    _RequiredCreateLinkRequestRequestTypeDef, _OptionalCreateLinkRequestRequestTypeDef
):
    pass

CreateLinkResponseTypeDef = TypedDict(
    "CreateLinkResponseTypeDef",
    {
        "Link": "LinkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSiteRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSiteRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalCreateSiteRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSiteRequestRequestTypeDef",
    {
        "Description": str,
        "Location": "LocationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSiteRequestRequestTypeDef(
    _RequiredCreateSiteRequestRequestTypeDef, _OptionalCreateSiteRequestRequestTypeDef
):
    pass

CreateSiteResponseTypeDef = TypedDict(
    "CreateSiteResponseTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSiteToSiteVpnAttachmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSiteToSiteVpnAttachmentRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "VpnConnectionArn": str,
    },
)
_OptionalCreateSiteToSiteVpnAttachmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSiteToSiteVpnAttachmentRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreateSiteToSiteVpnAttachmentRequestRequestTypeDef(
    _RequiredCreateSiteToSiteVpnAttachmentRequestRequestTypeDef,
    _OptionalCreateSiteToSiteVpnAttachmentRequestRequestTypeDef,
):
    pass

CreateSiteToSiteVpnAttachmentResponseTypeDef = TypedDict(
    "CreateSiteToSiteVpnAttachmentResponseTypeDef",
    {
        "SiteToSiteVpnAttachment": "SiteToSiteVpnAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVpcAttachmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpcAttachmentRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "VpcArn": str,
        "SubnetArns": List[str],
    },
)
_OptionalCreateVpcAttachmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpcAttachmentRequestRequestTypeDef",
    {
        "Options": "VpcOptionsTypeDef",
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreateVpcAttachmentRequestRequestTypeDef(
    _RequiredCreateVpcAttachmentRequestRequestTypeDef,
    _OptionalCreateVpcAttachmentRequestRequestTypeDef,
):
    pass

CreateVpcAttachmentResponseTypeDef = TypedDict(
    "CreateVpcAttachmentResponseTypeDef",
    {
        "VpcAttachment": "VpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomerGatewayAssociationTypeDef = TypedDict(
    "CustomerGatewayAssociationTypeDef",
    {
        "CustomerGatewayArn": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "State": CustomerGatewayAssociationStateType,
    },
    total=False,
)

DeleteAttachmentRequestRequestTypeDef = TypedDict(
    "DeleteAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)

DeleteAttachmentResponseTypeDef = TypedDict(
    "DeleteAttachmentResponseTypeDef",
    {
        "Attachment": "AttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectPeerRequestRequestTypeDef = TypedDict(
    "DeleteConnectPeerRequestRequestTypeDef",
    {
        "ConnectPeerId": str,
    },
)

DeleteConnectPeerResponseTypeDef = TypedDict(
    "DeleteConnectPeerResponseTypeDef",
    {
        "ConnectPeer": "ConnectPeerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectionId": str,
    },
)

DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCoreNetworkPolicyVersionRequestRequestTypeDef = TypedDict(
    "DeleteCoreNetworkPolicyVersionRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
    },
)

DeleteCoreNetworkPolicyVersionResponseTypeDef = TypedDict(
    "DeleteCoreNetworkPolicyVersionResponseTypeDef",
    {
        "CoreNetworkPolicy": "CoreNetworkPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCoreNetworkRequestRequestTypeDef = TypedDict(
    "DeleteCoreNetworkRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
    },
)

DeleteCoreNetworkResponseTypeDef = TypedDict(
    "DeleteCoreNetworkResponseTypeDef",
    {
        "CoreNetwork": "CoreNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDeviceRequestRequestTypeDef = TypedDict(
    "DeleteDeviceRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
    },
)

DeleteDeviceResponseTypeDef = TypedDict(
    "DeleteDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGlobalNetworkRequestRequestTypeDef = TypedDict(
    "DeleteGlobalNetworkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)

DeleteGlobalNetworkResponseTypeDef = TypedDict(
    "DeleteGlobalNetworkResponseTypeDef",
    {
        "GlobalNetwork": "GlobalNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLinkRequestRequestTypeDef = TypedDict(
    "DeleteLinkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "LinkId": str,
    },
)

DeleteLinkResponseTypeDef = TypedDict(
    "DeleteLinkResponseTypeDef",
    {
        "Link": "LinkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeleteSiteRequestRequestTypeDef = TypedDict(
    "DeleteSiteRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "SiteId": str,
    },
)

DeleteSiteResponseTypeDef = TypedDict(
    "DeleteSiteResponseTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterTransitGatewayRequestRequestTypeDef = TypedDict(
    "DeregisterTransitGatewayRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArn": str,
    },
)

DeregisterTransitGatewayResponseTypeDef = TypedDict(
    "DeregisterTransitGatewayResponseTypeDef",
    {
        "TransitGatewayRegistration": "TransitGatewayRegistrationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGlobalNetworksRequestRequestTypeDef = TypedDict(
    "DescribeGlobalNetworksRequestRequestTypeDef",
    {
        "GlobalNetworkIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeGlobalNetworksResponseTypeDef = TypedDict(
    "DescribeGlobalNetworksResponseTypeDef",
    {
        "GlobalNetworks": List["GlobalNetworkTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "DeviceId": str,
        "DeviceArn": str,
        "GlobalNetworkId": str,
        "AWSLocation": "AWSLocationTypeDef",
        "Description": str,
        "Type": str,
        "Vendor": str,
        "Model": str,
        "SerialNumber": str,
        "Location": "LocationTypeDef",
        "SiteId": str,
        "CreatedAt": datetime,
        "State": DeviceStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

DisassociateConnectPeerRequestRequestTypeDef = TypedDict(
    "DisassociateConnectPeerRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectPeerId": str,
    },
)

DisassociateConnectPeerResponseTypeDef = TypedDict(
    "DisassociateConnectPeerResponseTypeDef",
    {
        "ConnectPeerAssociation": "ConnectPeerAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateCustomerGatewayRequestRequestTypeDef = TypedDict(
    "DisassociateCustomerGatewayRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "CustomerGatewayArn": str,
    },
)

DisassociateCustomerGatewayResponseTypeDef = TypedDict(
    "DisassociateCustomerGatewayResponseTypeDef",
    {
        "CustomerGatewayAssociation": "CustomerGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateLinkRequestRequestTypeDef = TypedDict(
    "DisassociateLinkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
    },
)

DisassociateLinkResponseTypeDef = TypedDict(
    "DisassociateLinkResponseTypeDef",
    {
        "LinkAssociation": "LinkAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateTransitGatewayConnectPeerRequestRequestTypeDef = TypedDict(
    "DisassociateTransitGatewayConnectPeerRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayConnectPeerArn": str,
    },
)

DisassociateTransitGatewayConnectPeerResponseTypeDef = TypedDict(
    "DisassociateTransitGatewayConnectPeerResponseTypeDef",
    {
        "TransitGatewayConnectPeerAssociation": "TransitGatewayConnectPeerAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecuteCoreNetworkChangeSetRequestRequestTypeDef = TypedDict(
    "ExecuteCoreNetworkChangeSetRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
    },
)

GetConnectAttachmentRequestRequestTypeDef = TypedDict(
    "GetConnectAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)

GetConnectAttachmentResponseTypeDef = TypedDict(
    "GetConnectAttachmentResponseTypeDef",
    {
        "ConnectAttachment": "ConnectAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetConnectPeerAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetConnectPeerAssociationsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetConnectPeerAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetConnectPeerAssociationsRequestRequestTypeDef",
    {
        "ConnectPeerIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetConnectPeerAssociationsRequestRequestTypeDef(
    _RequiredGetConnectPeerAssociationsRequestRequestTypeDef,
    _OptionalGetConnectPeerAssociationsRequestRequestTypeDef,
):
    pass

GetConnectPeerAssociationsResponseTypeDef = TypedDict(
    "GetConnectPeerAssociationsResponseTypeDef",
    {
        "ConnectPeerAssociations": List["ConnectPeerAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectPeerRequestRequestTypeDef = TypedDict(
    "GetConnectPeerRequestRequestTypeDef",
    {
        "ConnectPeerId": str,
    },
)

GetConnectPeerResponseTypeDef = TypedDict(
    "GetConnectPeerResponseTypeDef",
    {
        "ConnectPeer": "ConnectPeerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetConnectionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetConnectionsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetConnectionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetConnectionsRequestRequestTypeDef",
    {
        "ConnectionIds": List[str],
        "DeviceId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetConnectionsRequestRequestTypeDef(
    _RequiredGetConnectionsRequestRequestTypeDef, _OptionalGetConnectionsRequestRequestTypeDef
):
    pass

GetConnectionsResponseTypeDef = TypedDict(
    "GetConnectionsResponseTypeDef",
    {
        "Connections": List["ConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCoreNetworkChangeSetRequestRequestTypeDef = TypedDict(
    "_RequiredGetCoreNetworkChangeSetRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
    },
)
_OptionalGetCoreNetworkChangeSetRequestRequestTypeDef = TypedDict(
    "_OptionalGetCoreNetworkChangeSetRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetCoreNetworkChangeSetRequestRequestTypeDef(
    _RequiredGetCoreNetworkChangeSetRequestRequestTypeDef,
    _OptionalGetCoreNetworkChangeSetRequestRequestTypeDef,
):
    pass

GetCoreNetworkChangeSetResponseTypeDef = TypedDict(
    "GetCoreNetworkChangeSetResponseTypeDef",
    {
        "CoreNetworkChanges": List["CoreNetworkChangeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCoreNetworkPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetCoreNetworkPolicyRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
    },
)
_OptionalGetCoreNetworkPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetCoreNetworkPolicyRequestRequestTypeDef",
    {
        "PolicyVersionId": int,
        "Alias": CoreNetworkPolicyAliasType,
    },
    total=False,
)

class GetCoreNetworkPolicyRequestRequestTypeDef(
    _RequiredGetCoreNetworkPolicyRequestRequestTypeDef,
    _OptionalGetCoreNetworkPolicyRequestRequestTypeDef,
):
    pass

GetCoreNetworkPolicyResponseTypeDef = TypedDict(
    "GetCoreNetworkPolicyResponseTypeDef",
    {
        "CoreNetworkPolicy": "CoreNetworkPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCoreNetworkRequestRequestTypeDef = TypedDict(
    "GetCoreNetworkRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
    },
)

GetCoreNetworkResponseTypeDef = TypedDict(
    "GetCoreNetworkResponseTypeDef",
    {
        "CoreNetwork": "CoreNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCustomerGatewayAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetCustomerGatewayAssociationsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetCustomerGatewayAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetCustomerGatewayAssociationsRequestRequestTypeDef",
    {
        "CustomerGatewayArns": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetCustomerGatewayAssociationsRequestRequestTypeDef(
    _RequiredGetCustomerGatewayAssociationsRequestRequestTypeDef,
    _OptionalGetCustomerGatewayAssociationsRequestRequestTypeDef,
):
    pass

GetCustomerGatewayAssociationsResponseTypeDef = TypedDict(
    "GetCustomerGatewayAssociationsResponseTypeDef",
    {
        "CustomerGatewayAssociations": List["CustomerGatewayAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDevicesRequestRequestTypeDef = TypedDict(
    "_RequiredGetDevicesRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetDevicesRequestRequestTypeDef = TypedDict(
    "_OptionalGetDevicesRequestRequestTypeDef",
    {
        "DeviceIds": List[str],
        "SiteId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetDevicesRequestRequestTypeDef(
    _RequiredGetDevicesRequestRequestTypeDef, _OptionalGetDevicesRequestRequestTypeDef
):
    pass

GetDevicesResponseTypeDef = TypedDict(
    "GetDevicesResponseTypeDef",
    {
        "Devices": List["DeviceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLinkAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetLinkAssociationsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetLinkAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetLinkAssociationsRequestRequestTypeDef",
    {
        "DeviceId": str,
        "LinkId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetLinkAssociationsRequestRequestTypeDef(
    _RequiredGetLinkAssociationsRequestRequestTypeDef,
    _OptionalGetLinkAssociationsRequestRequestTypeDef,
):
    pass

GetLinkAssociationsResponseTypeDef = TypedDict(
    "GetLinkAssociationsResponseTypeDef",
    {
        "LinkAssociations": List["LinkAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLinksRequestRequestTypeDef = TypedDict(
    "_RequiredGetLinksRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetLinksRequestRequestTypeDef = TypedDict(
    "_OptionalGetLinksRequestRequestTypeDef",
    {
        "LinkIds": List[str],
        "SiteId": str,
        "Type": str,
        "Provider": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetLinksRequestRequestTypeDef(
    _RequiredGetLinksRequestRequestTypeDef, _OptionalGetLinksRequestRequestTypeDef
):
    pass

GetLinksResponseTypeDef = TypedDict(
    "GetLinksResponseTypeDef",
    {
        "Links": List["LinkTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetNetworkResourceCountsRequestRequestTypeDef = TypedDict(
    "_RequiredGetNetworkResourceCountsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetNetworkResourceCountsRequestRequestTypeDef = TypedDict(
    "_OptionalGetNetworkResourceCountsRequestRequestTypeDef",
    {
        "ResourceType": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetNetworkResourceCountsRequestRequestTypeDef(
    _RequiredGetNetworkResourceCountsRequestRequestTypeDef,
    _OptionalGetNetworkResourceCountsRequestRequestTypeDef,
):
    pass

GetNetworkResourceCountsResponseTypeDef = TypedDict(
    "GetNetworkResourceCountsResponseTypeDef",
    {
        "NetworkResourceCounts": List["NetworkResourceCountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetNetworkResourceRelationshipsRequestRequestTypeDef = TypedDict(
    "_RequiredGetNetworkResourceRelationshipsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetNetworkResourceRelationshipsRequestRequestTypeDef = TypedDict(
    "_OptionalGetNetworkResourceRelationshipsRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "RegisteredGatewayArn": str,
        "AwsRegion": str,
        "AccountId": str,
        "ResourceType": str,
        "ResourceArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetNetworkResourceRelationshipsRequestRequestTypeDef(
    _RequiredGetNetworkResourceRelationshipsRequestRequestTypeDef,
    _OptionalGetNetworkResourceRelationshipsRequestRequestTypeDef,
):
    pass

GetNetworkResourceRelationshipsResponseTypeDef = TypedDict(
    "GetNetworkResourceRelationshipsResponseTypeDef",
    {
        "Relationships": List["RelationshipTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetNetworkResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredGetNetworkResourcesRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetNetworkResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalGetNetworkResourcesRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "RegisteredGatewayArn": str,
        "AwsRegion": str,
        "AccountId": str,
        "ResourceType": str,
        "ResourceArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetNetworkResourcesRequestRequestTypeDef(
    _RequiredGetNetworkResourcesRequestRequestTypeDef,
    _OptionalGetNetworkResourcesRequestRequestTypeDef,
):
    pass

GetNetworkResourcesResponseTypeDef = TypedDict(
    "GetNetworkResourcesResponseTypeDef",
    {
        "NetworkResources": List["NetworkResourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetNetworkRoutesRequestRequestTypeDef = TypedDict(
    "_RequiredGetNetworkRoutesRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "RouteTableIdentifier": "RouteTableIdentifierTypeDef",
    },
)
_OptionalGetNetworkRoutesRequestRequestTypeDef = TypedDict(
    "_OptionalGetNetworkRoutesRequestRequestTypeDef",
    {
        "ExactCidrMatches": List[str],
        "LongestPrefixMatches": List[str],
        "SubnetOfMatches": List[str],
        "SupernetOfMatches": List[str],
        "PrefixListIds": List[str],
        "States": List[RouteStateType],
        "Types": List[RouteTypeType],
        "DestinationFilters": Dict[str, List[str]],
    },
    total=False,
)

class GetNetworkRoutesRequestRequestTypeDef(
    _RequiredGetNetworkRoutesRequestRequestTypeDef, _OptionalGetNetworkRoutesRequestRequestTypeDef
):
    pass

GetNetworkRoutesResponseTypeDef = TypedDict(
    "GetNetworkRoutesResponseTypeDef",
    {
        "RouteTableArn": str,
        "CoreNetworkSegmentEdge": "CoreNetworkSegmentEdgeIdentifierTypeDef",
        "RouteTableType": RouteTableTypeType,
        "RouteTableTimestamp": datetime,
        "NetworkRoutes": List["NetworkRouteTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetNetworkTelemetryRequestRequestTypeDef = TypedDict(
    "_RequiredGetNetworkTelemetryRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetNetworkTelemetryRequestRequestTypeDef = TypedDict(
    "_OptionalGetNetworkTelemetryRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "RegisteredGatewayArn": str,
        "AwsRegion": str,
        "AccountId": str,
        "ResourceType": str,
        "ResourceArn": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetNetworkTelemetryRequestRequestTypeDef(
    _RequiredGetNetworkTelemetryRequestRequestTypeDef,
    _OptionalGetNetworkTelemetryRequestRequestTypeDef,
):
    pass

GetNetworkTelemetryResponseTypeDef = TypedDict(
    "GetNetworkTelemetryResponseTypeDef",
    {
        "NetworkTelemetry": List["NetworkTelemetryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "PolicyDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRouteAnalysisRequestRequestTypeDef = TypedDict(
    "GetRouteAnalysisRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "RouteAnalysisId": str,
    },
)

GetRouteAnalysisResponseTypeDef = TypedDict(
    "GetRouteAnalysisResponseTypeDef",
    {
        "RouteAnalysis": "RouteAnalysisTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSiteToSiteVpnAttachmentRequestRequestTypeDef = TypedDict(
    "GetSiteToSiteVpnAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)

GetSiteToSiteVpnAttachmentResponseTypeDef = TypedDict(
    "GetSiteToSiteVpnAttachmentResponseTypeDef",
    {
        "SiteToSiteVpnAttachment": "SiteToSiteVpnAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSitesRequestRequestTypeDef = TypedDict(
    "_RequiredGetSitesRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetSitesRequestRequestTypeDef = TypedDict(
    "_OptionalGetSitesRequestRequestTypeDef",
    {
        "SiteIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetSitesRequestRequestTypeDef(
    _RequiredGetSitesRequestRequestTypeDef, _OptionalGetSitesRequestRequestTypeDef
):
    pass

GetSitesResponseTypeDef = TypedDict(
    "GetSitesResponseTypeDef",
    {
        "Sites": List["SiteTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef",
    {
        "TransitGatewayConnectPeerArns": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef(
    _RequiredGetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef,
    _OptionalGetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef,
):
    pass

GetTransitGatewayConnectPeerAssociationsResponseTypeDef = TypedDict(
    "GetTransitGatewayConnectPeerAssociationsResponseTypeDef",
    {
        "TransitGatewayConnectPeerAssociations": List[
            "TransitGatewayConnectPeerAssociationTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransitGatewayRegistrationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetTransitGatewayRegistrationsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalGetTransitGatewayRegistrationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetTransitGatewayRegistrationsRequestRequestTypeDef",
    {
        "TransitGatewayArns": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetTransitGatewayRegistrationsRequestRequestTypeDef(
    _RequiredGetTransitGatewayRegistrationsRequestRequestTypeDef,
    _OptionalGetTransitGatewayRegistrationsRequestRequestTypeDef,
):
    pass

GetTransitGatewayRegistrationsResponseTypeDef = TypedDict(
    "GetTransitGatewayRegistrationsResponseTypeDef",
    {
        "TransitGatewayRegistrations": List["TransitGatewayRegistrationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVpcAttachmentRequestRequestTypeDef = TypedDict(
    "GetVpcAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)

GetVpcAttachmentResponseTypeDef = TypedDict(
    "GetVpcAttachmentResponseTypeDef",
    {
        "VpcAttachment": "VpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlobalNetworkTypeDef = TypedDict(
    "GlobalNetworkTypeDef",
    {
        "GlobalNetworkId": str,
        "GlobalNetworkArn": str,
        "Description": str,
        "CreatedAt": datetime,
        "State": GlobalNetworkStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LinkAssociationTypeDef = TypedDict(
    "LinkAssociationTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "LinkAssociationState": LinkAssociationStateType,
    },
    total=False,
)

LinkTypeDef = TypedDict(
    "LinkTypeDef",
    {
        "LinkId": str,
        "LinkArn": str,
        "GlobalNetworkId": str,
        "SiteId": str,
        "Description": str,
        "Type": str,
        "Bandwidth": "BandwidthTypeDef",
        "Provider": str,
        "CreatedAt": datetime,
        "State": LinkStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ListAttachmentsRequestRequestTypeDef = TypedDict(
    "ListAttachmentsRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "AttachmentType": AttachmentTypeType,
        "EdgeLocation": str,
        "State": AttachmentStateType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAttachmentsResponseTypeDef = TypedDict(
    "ListAttachmentsResponseTypeDef",
    {
        "Attachments": List["AttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConnectPeersRequestRequestTypeDef = TypedDict(
    "ListConnectPeersRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "ConnectAttachmentId": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListConnectPeersResponseTypeDef = TypedDict(
    "ListConnectPeersResponseTypeDef",
    {
        "ConnectPeers": List["ConnectPeerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCoreNetworkPolicyVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListCoreNetworkPolicyVersionsRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
    },
)
_OptionalListCoreNetworkPolicyVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListCoreNetworkPolicyVersionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListCoreNetworkPolicyVersionsRequestRequestTypeDef(
    _RequiredListCoreNetworkPolicyVersionsRequestRequestTypeDef,
    _OptionalListCoreNetworkPolicyVersionsRequestRequestTypeDef,
):
    pass

ListCoreNetworkPolicyVersionsResponseTypeDef = TypedDict(
    "ListCoreNetworkPolicyVersionsResponseTypeDef",
    {
        "CoreNetworkPolicyVersions": List["CoreNetworkPolicyVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCoreNetworksRequestRequestTypeDef = TypedDict(
    "ListCoreNetworksRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListCoreNetworksResponseTypeDef = TypedDict(
    "ListCoreNetworksResponseTypeDef",
    {
        "CoreNetworks": List["CoreNetworkSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationServiceAccessStatusRequestRequestTypeDef = TypedDict(
    "ListOrganizationServiceAccessStatusRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOrganizationServiceAccessStatusResponseTypeDef = TypedDict(
    "ListOrganizationServiceAccessStatusResponseTypeDef",
    {
        "OrganizationStatus": "OrganizationStatusTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "Address": str,
        "Latitude": str,
        "Longitude": str,
    },
    total=False,
)

NetworkResourceCountTypeDef = TypedDict(
    "NetworkResourceCountTypeDef",
    {
        "ResourceType": str,
        "Count": int,
    },
    total=False,
)

NetworkResourceSummaryTypeDef = TypedDict(
    "NetworkResourceSummaryTypeDef",
    {
        "RegisteredGatewayArn": str,
        "ResourceArn": str,
        "ResourceType": str,
        "Definition": str,
        "NameTag": str,
        "IsMiddlebox": bool,
    },
    total=False,
)

NetworkResourceTypeDef = TypedDict(
    "NetworkResourceTypeDef",
    {
        "RegisteredGatewayArn": str,
        "CoreNetworkId": str,
        "AwsRegion": str,
        "AccountId": str,
        "ResourceType": str,
        "ResourceId": str,
        "ResourceArn": str,
        "Definition": str,
        "DefinitionTimestamp": datetime,
        "Tags": List["TagTypeDef"],
        "Metadata": Dict[str, str],
    },
    total=False,
)

NetworkRouteDestinationTypeDef = TypedDict(
    "NetworkRouteDestinationTypeDef",
    {
        "CoreNetworkAttachmentId": str,
        "TransitGatewayAttachmentId": str,
        "SegmentName": str,
        "EdgeLocation": str,
        "ResourceType": str,
        "ResourceId": str,
    },
    total=False,
)

NetworkRouteTypeDef = TypedDict(
    "NetworkRouteTypeDef",
    {
        "DestinationCidrBlock": str,
        "Destinations": List["NetworkRouteDestinationTypeDef"],
        "PrefixListId": str,
        "State": RouteStateType,
        "Type": RouteTypeType,
    },
    total=False,
)

NetworkTelemetryTypeDef = TypedDict(
    "NetworkTelemetryTypeDef",
    {
        "RegisteredGatewayArn": str,
        "CoreNetworkId": str,
        "AwsRegion": str,
        "AccountId": str,
        "ResourceType": str,
        "ResourceId": str,
        "ResourceArn": str,
        "Address": str,
        "Health": "ConnectionHealthTypeDef",
    },
    total=False,
)

OrganizationStatusTypeDef = TypedDict(
    "OrganizationStatusTypeDef",
    {
        "OrganizationId": str,
        "OrganizationAwsServiceAccessStatus": str,
        "SLRDeploymentStatus": str,
        "AccountStatusList": List["AccountStatusTypeDef"],
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

PathComponentTypeDef = TypedDict(
    "PathComponentTypeDef",
    {
        "Sequence": int,
        "Resource": "NetworkResourceSummaryTypeDef",
        "DestinationCidrBlock": str,
    },
    total=False,
)

ProposedSegmentChangeTypeDef = TypedDict(
    "ProposedSegmentChangeTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "AttachmentPolicyRuleNumber": int,
        "SegmentName": str,
    },
    total=False,
)

_RequiredPutCoreNetworkPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutCoreNetworkPolicyRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyDocument": str,
    },
)
_OptionalPutCoreNetworkPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutCoreNetworkPolicyRequestRequestTypeDef",
    {
        "Description": str,
        "LatestVersionId": int,
        "ClientToken": str,
    },
    total=False,
)

class PutCoreNetworkPolicyRequestRequestTypeDef(
    _RequiredPutCoreNetworkPolicyRequestRequestTypeDef,
    _OptionalPutCoreNetworkPolicyRequestRequestTypeDef,
):
    pass

PutCoreNetworkPolicyResponseTypeDef = TypedDict(
    "PutCoreNetworkPolicyResponseTypeDef",
    {
        "CoreNetworkPolicy": "CoreNetworkPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "PolicyDocument": str,
        "ResourceArn": str,
    },
)

RegisterTransitGatewayRequestRequestTypeDef = TypedDict(
    "RegisterTransitGatewayRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArn": str,
    },
)

RegisterTransitGatewayResponseTypeDef = TypedDict(
    "RegisterTransitGatewayResponseTypeDef",
    {
        "TransitGatewayRegistration": "TransitGatewayRegistrationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectAttachmentRequestRequestTypeDef = TypedDict(
    "RejectAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)

RejectAttachmentResponseTypeDef = TypedDict(
    "RejectAttachmentResponseTypeDef",
    {
        "Attachment": "AttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "From": str,
        "To": str,
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

RestoreCoreNetworkPolicyVersionRequestRequestTypeDef = TypedDict(
    "RestoreCoreNetworkPolicyVersionRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
    },
)

RestoreCoreNetworkPolicyVersionResponseTypeDef = TypedDict(
    "RestoreCoreNetworkPolicyVersionResponseTypeDef",
    {
        "CoreNetworkPolicy": "CoreNetworkPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RouteAnalysisCompletionTypeDef = TypedDict(
    "RouteAnalysisCompletionTypeDef",
    {
        "ResultCode": RouteAnalysisCompletionResultCodeType,
        "ReasonCode": RouteAnalysisCompletionReasonCodeType,
        "ReasonContext": Dict[str, str],
    },
    total=False,
)

RouteAnalysisEndpointOptionsSpecificationTypeDef = TypedDict(
    "RouteAnalysisEndpointOptionsSpecificationTypeDef",
    {
        "TransitGatewayAttachmentArn": str,
        "IpAddress": str,
    },
    total=False,
)

RouteAnalysisEndpointOptionsTypeDef = TypedDict(
    "RouteAnalysisEndpointOptionsTypeDef",
    {
        "TransitGatewayAttachmentArn": str,
        "TransitGatewayArn": str,
        "IpAddress": str,
    },
    total=False,
)

RouteAnalysisPathTypeDef = TypedDict(
    "RouteAnalysisPathTypeDef",
    {
        "CompletionStatus": "RouteAnalysisCompletionTypeDef",
        "Path": List["PathComponentTypeDef"],
    },
    total=False,
)

RouteAnalysisTypeDef = TypedDict(
    "RouteAnalysisTypeDef",
    {
        "GlobalNetworkId": str,
        "OwnerAccountId": str,
        "RouteAnalysisId": str,
        "StartTimestamp": datetime,
        "Status": RouteAnalysisStatusType,
        "Source": "RouteAnalysisEndpointOptionsTypeDef",
        "Destination": "RouteAnalysisEndpointOptionsTypeDef",
        "IncludeReturnPath": bool,
        "UseMiddleboxes": bool,
        "ForwardPath": "RouteAnalysisPathTypeDef",
        "ReturnPath": "RouteAnalysisPathTypeDef",
    },
    total=False,
)

RouteTableIdentifierTypeDef = TypedDict(
    "RouteTableIdentifierTypeDef",
    {
        "TransitGatewayRouteTableArn": str,
        "CoreNetworkSegmentEdge": "CoreNetworkSegmentEdgeIdentifierTypeDef",
    },
    total=False,
)

SiteToSiteVpnAttachmentTypeDef = TypedDict(
    "SiteToSiteVpnAttachmentTypeDef",
    {
        "Attachment": "AttachmentTypeDef",
        "VpnConnectionArn": str,
    },
    total=False,
)

SiteTypeDef = TypedDict(
    "SiteTypeDef",
    {
        "SiteId": str,
        "SiteArn": str,
        "GlobalNetworkId": str,
        "Description": str,
        "Location": "LocationTypeDef",
        "CreatedAt": datetime,
        "State": SiteStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

StartOrganizationServiceAccessUpdateRequestRequestTypeDef = TypedDict(
    "StartOrganizationServiceAccessUpdateRequestRequestTypeDef",
    {
        "Action": str,
    },
)

StartOrganizationServiceAccessUpdateResponseTypeDef = TypedDict(
    "StartOrganizationServiceAccessUpdateResponseTypeDef",
    {
        "OrganizationStatus": "OrganizationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartRouteAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredStartRouteAnalysisRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "Source": "RouteAnalysisEndpointOptionsSpecificationTypeDef",
        "Destination": "RouteAnalysisEndpointOptionsSpecificationTypeDef",
    },
)
_OptionalStartRouteAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalStartRouteAnalysisRequestRequestTypeDef",
    {
        "IncludeReturnPath": bool,
        "UseMiddleboxes": bool,
    },
    total=False,
)

class StartRouteAnalysisRequestRequestTypeDef(
    _RequiredStartRouteAnalysisRequestRequestTypeDef,
    _OptionalStartRouteAnalysisRequestRequestTypeDef,
):
    pass

StartRouteAnalysisResponseTypeDef = TypedDict(
    "StartRouteAnalysisResponseTypeDef",
    {
        "RouteAnalysis": "RouteAnalysisTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TransitGatewayConnectPeerAssociationTypeDef = TypedDict(
    "TransitGatewayConnectPeerAssociationTypeDef",
    {
        "TransitGatewayConnectPeerArn": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
        "State": TransitGatewayConnectPeerAssociationStateType,
    },
    total=False,
)

TransitGatewayRegistrationStateReasonTypeDef = TypedDict(
    "TransitGatewayRegistrationStateReasonTypeDef",
    {
        "Code": TransitGatewayRegistrationStateType,
        "Message": str,
    },
    total=False,
)

TransitGatewayRegistrationTypeDef = TypedDict(
    "TransitGatewayRegistrationTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArn": str,
        "State": "TransitGatewayRegistrationStateReasonTypeDef",
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectionRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectionId": str,
    },
)
_OptionalUpdateConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectionRequestRequestTypeDef",
    {
        "LinkId": str,
        "ConnectedLinkId": str,
        "Description": str,
    },
    total=False,
)

class UpdateConnectionRequestRequestTypeDef(
    _RequiredUpdateConnectionRequestRequestTypeDef, _OptionalUpdateConnectionRequestRequestTypeDef
):
    pass

UpdateConnectionResponseTypeDef = TypedDict(
    "UpdateConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateCoreNetworkRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCoreNetworkRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
    },
)
_OptionalUpdateCoreNetworkRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCoreNetworkRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateCoreNetworkRequestRequestTypeDef(
    _RequiredUpdateCoreNetworkRequestRequestTypeDef, _OptionalUpdateCoreNetworkRequestRequestTypeDef
):
    pass

UpdateCoreNetworkResponseTypeDef = TypedDict(
    "UpdateCoreNetworkResponseTypeDef",
    {
        "CoreNetwork": "CoreNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
    },
)
_OptionalUpdateDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceRequestRequestTypeDef",
    {
        "AWSLocation": "AWSLocationTypeDef",
        "Description": str,
        "Type": str,
        "Vendor": str,
        "Model": str,
        "SerialNumber": str,
        "Location": "LocationTypeDef",
        "SiteId": str,
    },
    total=False,
)

class UpdateDeviceRequestRequestTypeDef(
    _RequiredUpdateDeviceRequestRequestTypeDef, _OptionalUpdateDeviceRequestRequestTypeDef
):
    pass

UpdateDeviceResponseTypeDef = TypedDict(
    "UpdateDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGlobalNetworkRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGlobalNetworkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)
_OptionalUpdateGlobalNetworkRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGlobalNetworkRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateGlobalNetworkRequestRequestTypeDef(
    _RequiredUpdateGlobalNetworkRequestRequestTypeDef,
    _OptionalUpdateGlobalNetworkRequestRequestTypeDef,
):
    pass

UpdateGlobalNetworkResponseTypeDef = TypedDict(
    "UpdateGlobalNetworkResponseTypeDef",
    {
        "GlobalNetwork": "GlobalNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateLinkRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLinkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "LinkId": str,
    },
)
_OptionalUpdateLinkRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLinkRequestRequestTypeDef",
    {
        "Description": str,
        "Type": str,
        "Bandwidth": "BandwidthTypeDef",
        "Provider": str,
    },
    total=False,
)

class UpdateLinkRequestRequestTypeDef(
    _RequiredUpdateLinkRequestRequestTypeDef, _OptionalUpdateLinkRequestRequestTypeDef
):
    pass

UpdateLinkResponseTypeDef = TypedDict(
    "UpdateLinkResponseTypeDef",
    {
        "Link": "LinkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateNetworkResourceMetadataRequestRequestTypeDef = TypedDict(
    "UpdateNetworkResourceMetadataRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ResourceArn": str,
        "Metadata": Dict[str, str],
    },
)

UpdateNetworkResourceMetadataResponseTypeDef = TypedDict(
    "UpdateNetworkResourceMetadataResponseTypeDef",
    {
        "ResourceArn": str,
        "Metadata": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSiteRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSiteRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "SiteId": str,
    },
)
_OptionalUpdateSiteRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSiteRequestRequestTypeDef",
    {
        "Description": str,
        "Location": "LocationTypeDef",
    },
    total=False,
)

class UpdateSiteRequestRequestTypeDef(
    _RequiredUpdateSiteRequestRequestTypeDef, _OptionalUpdateSiteRequestRequestTypeDef
):
    pass

UpdateSiteResponseTypeDef = TypedDict(
    "UpdateSiteResponseTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVpcAttachmentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVpcAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)
_OptionalUpdateVpcAttachmentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVpcAttachmentRequestRequestTypeDef",
    {
        "AddSubnetArns": List[str],
        "RemoveSubnetArns": List[str],
        "Options": "VpcOptionsTypeDef",
    },
    total=False,
)

class UpdateVpcAttachmentRequestRequestTypeDef(
    _RequiredUpdateVpcAttachmentRequestRequestTypeDef,
    _OptionalUpdateVpcAttachmentRequestRequestTypeDef,
):
    pass

UpdateVpcAttachmentResponseTypeDef = TypedDict(
    "UpdateVpcAttachmentResponseTypeDef",
    {
        "VpcAttachment": "VpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcAttachmentTypeDef = TypedDict(
    "VpcAttachmentTypeDef",
    {
        "Attachment": "AttachmentTypeDef",
        "SubnetArns": List[str],
        "Options": "VpcOptionsTypeDef",
    },
    total=False,
)

VpcOptionsTypeDef = TypedDict(
    "VpcOptionsTypeDef",
    {
        "Ipv6Support": bool,
    },
    total=False,
)
