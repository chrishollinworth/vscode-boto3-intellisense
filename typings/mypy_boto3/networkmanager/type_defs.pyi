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
    ConnectionStateType,
    ConnectionStatusType,
    ConnectionTypeType,
    CustomerGatewayAssociationStateType,
    DeviceStateType,
    GlobalNetworkStateType,
    LinkAssociationStateType,
    LinkStateType,
    RouteAnalysisCompletionReasonCodeType,
    RouteAnalysisCompletionResultCodeType,
    RouteAnalysisStatusType,
    RouteStateType,
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
    "AssociateCustomerGatewayRequestRequestTypeDef",
    "AssociateCustomerGatewayResponseTypeDef",
    "AssociateLinkRequestRequestTypeDef",
    "AssociateLinkResponseTypeDef",
    "AssociateTransitGatewayConnectPeerRequestRequestTypeDef",
    "AssociateTransitGatewayConnectPeerResponseTypeDef",
    "BandwidthTypeDef",
    "ConnectionHealthTypeDef",
    "ConnectionTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "CreateConnectionResponseTypeDef",
    "CreateDeviceRequestRequestTypeDef",
    "CreateDeviceResponseTypeDef",
    "CreateGlobalNetworkRequestRequestTypeDef",
    "CreateGlobalNetworkResponseTypeDef",
    "CreateLinkRequestRequestTypeDef",
    "CreateLinkResponseTypeDef",
    "CreateSiteRequestRequestTypeDef",
    "CreateSiteResponseTypeDef",
    "CustomerGatewayAssociationTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteDeviceRequestRequestTypeDef",
    "DeleteDeviceResponseTypeDef",
    "DeleteGlobalNetworkRequestRequestTypeDef",
    "DeleteGlobalNetworkResponseTypeDef",
    "DeleteLinkRequestRequestTypeDef",
    "DeleteLinkResponseTypeDef",
    "DeleteSiteRequestRequestTypeDef",
    "DeleteSiteResponseTypeDef",
    "DeregisterTransitGatewayRequestRequestTypeDef",
    "DeregisterTransitGatewayResponseTypeDef",
    "DescribeGlobalNetworksRequestRequestTypeDef",
    "DescribeGlobalNetworksResponseTypeDef",
    "DeviceTypeDef",
    "DisassociateCustomerGatewayRequestRequestTypeDef",
    "DisassociateCustomerGatewayResponseTypeDef",
    "DisassociateLinkRequestRequestTypeDef",
    "DisassociateLinkResponseTypeDef",
    "DisassociateTransitGatewayConnectPeerRequestRequestTypeDef",
    "DisassociateTransitGatewayConnectPeerResponseTypeDef",
    "GetConnectionsRequestRequestTypeDef",
    "GetConnectionsResponseTypeDef",
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
    "GetRouteAnalysisRequestRequestTypeDef",
    "GetRouteAnalysisResponseTypeDef",
    "GetSitesRequestRequestTypeDef",
    "GetSitesResponseTypeDef",
    "GetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef",
    "GetTransitGatewayConnectPeerAssociationsResponseTypeDef",
    "GetTransitGatewayRegistrationsRequestRequestTypeDef",
    "GetTransitGatewayRegistrationsResponseTypeDef",
    "GlobalNetworkTypeDef",
    "LinkAssociationTypeDef",
    "LinkTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationTypeDef",
    "NetworkResourceCountTypeDef",
    "NetworkResourceSummaryTypeDef",
    "NetworkResourceTypeDef",
    "NetworkRouteDestinationTypeDef",
    "NetworkRouteTypeDef",
    "NetworkTelemetryTypeDef",
    "PaginatorConfigTypeDef",
    "PathComponentTypeDef",
    "RegisterTransitGatewayRequestRequestTypeDef",
    "RegisterTransitGatewayResponseTypeDef",
    "RelationshipTypeDef",
    "ResponseMetadataTypeDef",
    "RouteAnalysisCompletionTypeDef",
    "RouteAnalysisEndpointOptionsSpecificationTypeDef",
    "RouteAnalysisEndpointOptionsTypeDef",
    "RouteAnalysisPathTypeDef",
    "RouteAnalysisTypeDef",
    "RouteTableIdentifierTypeDef",
    "SiteTypeDef",
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
)

AWSLocationTypeDef = TypedDict(
    "AWSLocationTypeDef",
    {
        "Zone": str,
        "SubnetArn": str,
    },
    total=False,
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

BandwidthTypeDef = TypedDict(
    "BandwidthTypeDef",
    {
        "UploadSpeed": int,
        "DownloadSpeed": int,
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
        "RouteTableType": Literal["TRANSIT_GATEWAY_ROUTE_TABLE"],
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
        "TransitGatewayAttachmentId": str,
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
