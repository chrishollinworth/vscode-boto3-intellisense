"""
Type annotations for privatenetworks service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/type_defs.html)

Usage::

    ```python
    from mypy_boto3_privatenetworks.type_defs import AcknowledgeOrderReceiptRequestRequestTypeDef

    data: AcknowledgeOrderReceiptRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AcknowledgmentStatusType,
    DeviceIdentifierFilterKeysType,
    DeviceIdentifierStatusType,
    ElevationReferenceType,
    HealthStatusType,
    NetworkResourceDefinitionTypeType,
    NetworkResourceFilterKeysType,
    NetworkResourceStatusType,
    NetworkSiteStatusType,
    NetworkStatusType,
    OrderFilterKeysType,
    UpdateTypeType,
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
    "AcknowledgeOrderReceiptRequestRequestTypeDef",
    "AcknowledgeOrderReceiptResponseTypeDef",
    "ActivateDeviceIdentifierRequestRequestTypeDef",
    "ActivateDeviceIdentifierResponseTypeDef",
    "ActivateNetworkSiteRequestRequestTypeDef",
    "ActivateNetworkSiteResponseTypeDef",
    "AddressTypeDef",
    "ConfigureAccessPointRequestRequestTypeDef",
    "ConfigureAccessPointResponseTypeDef",
    "CreateNetworkRequestRequestTypeDef",
    "CreateNetworkResponseTypeDef",
    "CreateNetworkSiteRequestRequestTypeDef",
    "CreateNetworkSiteResponseTypeDef",
    "DeactivateDeviceIdentifierRequestRequestTypeDef",
    "DeactivateDeviceIdentifierResponseTypeDef",
    "DeleteNetworkRequestRequestTypeDef",
    "DeleteNetworkResponseTypeDef",
    "DeleteNetworkSiteRequestRequestTypeDef",
    "DeleteNetworkSiteResponseTypeDef",
    "DeviceIdentifierTypeDef",
    "GetDeviceIdentifierRequestRequestTypeDef",
    "GetDeviceIdentifierResponseTypeDef",
    "GetNetworkRequestRequestTypeDef",
    "GetNetworkResourceRequestRequestTypeDef",
    "GetNetworkResourceResponseTypeDef",
    "GetNetworkResponseTypeDef",
    "GetNetworkSiteRequestRequestTypeDef",
    "GetNetworkSiteResponseTypeDef",
    "GetOrderRequestRequestTypeDef",
    "GetOrderResponseTypeDef",
    "ListDeviceIdentifiersRequestRequestTypeDef",
    "ListDeviceIdentifiersResponseTypeDef",
    "ListNetworkResourcesRequestRequestTypeDef",
    "ListNetworkResourcesResponseTypeDef",
    "ListNetworkSitesRequestRequestTypeDef",
    "ListNetworkSitesResponseTypeDef",
    "ListNetworksRequestRequestTypeDef",
    "ListNetworksResponseTypeDef",
    "ListOrdersRequestRequestTypeDef",
    "ListOrdersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NameValuePairTypeDef",
    "NetworkResourceDefinitionTypeDef",
    "NetworkResourceTypeDef",
    "NetworkSiteTypeDef",
    "NetworkTypeDef",
    "OrderTypeDef",
    "PaginatorConfigTypeDef",
    "PingResponseTypeDef",
    "PositionTypeDef",
    "ResponseMetadataTypeDef",
    "ReturnInformationTypeDef",
    "SitePlanTypeDef",
    "StartNetworkResourceUpdateRequestRequestTypeDef",
    "StartNetworkResourceUpdateResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TrackingInformationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateNetworkSitePlanRequestRequestTypeDef",
    "UpdateNetworkSiteRequestRequestTypeDef",
    "UpdateNetworkSiteResponseTypeDef",
)

AcknowledgeOrderReceiptRequestRequestTypeDef = TypedDict(
    "AcknowledgeOrderReceiptRequestRequestTypeDef",
    {
        "orderArn": str,
    },
)

AcknowledgeOrderReceiptResponseTypeDef = TypedDict(
    "AcknowledgeOrderReceiptResponseTypeDef",
    {
        "order": "OrderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredActivateDeviceIdentifierRequestRequestTypeDef = TypedDict(
    "_RequiredActivateDeviceIdentifierRequestRequestTypeDef",
    {
        "deviceIdentifierArn": str,
    },
)
_OptionalActivateDeviceIdentifierRequestRequestTypeDef = TypedDict(
    "_OptionalActivateDeviceIdentifierRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class ActivateDeviceIdentifierRequestRequestTypeDef(
    _RequiredActivateDeviceIdentifierRequestRequestTypeDef,
    _OptionalActivateDeviceIdentifierRequestRequestTypeDef,
):
    pass

ActivateDeviceIdentifierResponseTypeDef = TypedDict(
    "ActivateDeviceIdentifierResponseTypeDef",
    {
        "deviceIdentifier": "DeviceIdentifierTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredActivateNetworkSiteRequestRequestTypeDef = TypedDict(
    "_RequiredActivateNetworkSiteRequestRequestTypeDef",
    {
        "networkSiteArn": str,
        "shippingAddress": "AddressTypeDef",
    },
)
_OptionalActivateNetworkSiteRequestRequestTypeDef = TypedDict(
    "_OptionalActivateNetworkSiteRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class ActivateNetworkSiteRequestRequestTypeDef(
    _RequiredActivateNetworkSiteRequestRequestTypeDef,
    _OptionalActivateNetworkSiteRequestRequestTypeDef,
):
    pass

ActivateNetworkSiteResponseTypeDef = TypedDict(
    "ActivateNetworkSiteResponseTypeDef",
    {
        "networkSite": "NetworkSiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAddressTypeDef = TypedDict(
    "_RequiredAddressTypeDef",
    {
        "city": str,
        "country": str,
        "name": str,
        "postalCode": str,
        "stateOrProvince": str,
        "street1": str,
    },
)
_OptionalAddressTypeDef = TypedDict(
    "_OptionalAddressTypeDef",
    {
        "company": str,
        "phoneNumber": str,
        "street2": str,
        "street3": str,
    },
    total=False,
)

class AddressTypeDef(_RequiredAddressTypeDef, _OptionalAddressTypeDef):
    pass

_RequiredConfigureAccessPointRequestRequestTypeDef = TypedDict(
    "_RequiredConfigureAccessPointRequestRequestTypeDef",
    {
        "accessPointArn": str,
    },
)
_OptionalConfigureAccessPointRequestRequestTypeDef = TypedDict(
    "_OptionalConfigureAccessPointRequestRequestTypeDef",
    {
        "cpiSecretKey": str,
        "cpiUserId": str,
        "cpiUserPassword": str,
        "cpiUsername": str,
        "position": "PositionTypeDef",
    },
    total=False,
)

class ConfigureAccessPointRequestRequestTypeDef(
    _RequiredConfigureAccessPointRequestRequestTypeDef,
    _OptionalConfigureAccessPointRequestRequestTypeDef,
):
    pass

ConfigureAccessPointResponseTypeDef = TypedDict(
    "ConfigureAccessPointResponseTypeDef",
    {
        "accessPoint": "NetworkResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkRequestRequestTypeDef",
    {
        "networkName": str,
    },
)
_OptionalCreateNetworkRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateNetworkRequestRequestTypeDef(
    _RequiredCreateNetworkRequestRequestTypeDef, _OptionalCreateNetworkRequestRequestTypeDef
):
    pass

CreateNetworkResponseTypeDef = TypedDict(
    "CreateNetworkResponseTypeDef",
    {
        "network": "NetworkTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkSiteRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkSiteRequestRequestTypeDef",
    {
        "networkArn": str,
        "networkSiteName": str,
    },
)
_OptionalCreateNetworkSiteRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkSiteRequestRequestTypeDef",
    {
        "availabilityZone": str,
        "availabilityZoneId": str,
        "clientToken": str,
        "description": str,
        "pendingPlan": "SitePlanTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateNetworkSiteRequestRequestTypeDef(
    _RequiredCreateNetworkSiteRequestRequestTypeDef, _OptionalCreateNetworkSiteRequestRequestTypeDef
):
    pass

CreateNetworkSiteResponseTypeDef = TypedDict(
    "CreateNetworkSiteResponseTypeDef",
    {
        "networkSite": "NetworkSiteTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeactivateDeviceIdentifierRequestRequestTypeDef = TypedDict(
    "_RequiredDeactivateDeviceIdentifierRequestRequestTypeDef",
    {
        "deviceIdentifierArn": str,
    },
)
_OptionalDeactivateDeviceIdentifierRequestRequestTypeDef = TypedDict(
    "_OptionalDeactivateDeviceIdentifierRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeactivateDeviceIdentifierRequestRequestTypeDef(
    _RequiredDeactivateDeviceIdentifierRequestRequestTypeDef,
    _OptionalDeactivateDeviceIdentifierRequestRequestTypeDef,
):
    pass

DeactivateDeviceIdentifierResponseTypeDef = TypedDict(
    "DeactivateDeviceIdentifierResponseTypeDef",
    {
        "deviceIdentifier": "DeviceIdentifierTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteNetworkRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkRequestRequestTypeDef",
    {
        "networkArn": str,
    },
)
_OptionalDeleteNetworkRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteNetworkRequestRequestTypeDef(
    _RequiredDeleteNetworkRequestRequestTypeDef, _OptionalDeleteNetworkRequestRequestTypeDef
):
    pass

DeleteNetworkResponseTypeDef = TypedDict(
    "DeleteNetworkResponseTypeDef",
    {
        "network": "NetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteNetworkSiteRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkSiteRequestRequestTypeDef",
    {
        "networkSiteArn": str,
    },
)
_OptionalDeleteNetworkSiteRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkSiteRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteNetworkSiteRequestRequestTypeDef(
    _RequiredDeleteNetworkSiteRequestRequestTypeDef, _OptionalDeleteNetworkSiteRequestRequestTypeDef
):
    pass

DeleteNetworkSiteResponseTypeDef = TypedDict(
    "DeleteNetworkSiteResponseTypeDef",
    {
        "networkSite": "NetworkSiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceIdentifierTypeDef = TypedDict(
    "DeviceIdentifierTypeDef",
    {
        "createdAt": datetime,
        "deviceIdentifierArn": str,
        "iccid": str,
        "imsi": str,
        "networkArn": str,
        "orderArn": str,
        "status": DeviceIdentifierStatusType,
        "trafficGroupArn": str,
        "vendor": str,
    },
    total=False,
)

GetDeviceIdentifierRequestRequestTypeDef = TypedDict(
    "GetDeviceIdentifierRequestRequestTypeDef",
    {
        "deviceIdentifierArn": str,
    },
)

GetDeviceIdentifierResponseTypeDef = TypedDict(
    "GetDeviceIdentifierResponseTypeDef",
    {
        "deviceIdentifier": "DeviceIdentifierTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkRequestRequestTypeDef = TypedDict(
    "GetNetworkRequestRequestTypeDef",
    {
        "networkArn": str,
    },
)

GetNetworkResourceRequestRequestTypeDef = TypedDict(
    "GetNetworkResourceRequestRequestTypeDef",
    {
        "networkResourceArn": str,
    },
)

GetNetworkResourceResponseTypeDef = TypedDict(
    "GetNetworkResourceResponseTypeDef",
    {
        "networkResource": "NetworkResourceTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkResponseTypeDef = TypedDict(
    "GetNetworkResponseTypeDef",
    {
        "network": "NetworkTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkSiteRequestRequestTypeDef = TypedDict(
    "GetNetworkSiteRequestRequestTypeDef",
    {
        "networkSiteArn": str,
    },
)

GetNetworkSiteResponseTypeDef = TypedDict(
    "GetNetworkSiteResponseTypeDef",
    {
        "networkSite": "NetworkSiteTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOrderRequestRequestTypeDef = TypedDict(
    "GetOrderRequestRequestTypeDef",
    {
        "orderArn": str,
    },
)

GetOrderResponseTypeDef = TypedDict(
    "GetOrderResponseTypeDef",
    {
        "order": "OrderTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeviceIdentifiersRequestRequestTypeDef = TypedDict(
    "_RequiredListDeviceIdentifiersRequestRequestTypeDef",
    {
        "networkArn": str,
    },
)
_OptionalListDeviceIdentifiersRequestRequestTypeDef = TypedDict(
    "_OptionalListDeviceIdentifiersRequestRequestTypeDef",
    {
        "filters": Dict[DeviceIdentifierFilterKeysType, List[str]],
        "maxResults": int,
        "startToken": str,
    },
    total=False,
)

class ListDeviceIdentifiersRequestRequestTypeDef(
    _RequiredListDeviceIdentifiersRequestRequestTypeDef,
    _OptionalListDeviceIdentifiersRequestRequestTypeDef,
):
    pass

ListDeviceIdentifiersResponseTypeDef = TypedDict(
    "ListDeviceIdentifiersResponseTypeDef",
    {
        "deviceIdentifiers": List["DeviceIdentifierTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNetworkResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListNetworkResourcesRequestRequestTypeDef",
    {
        "networkArn": str,
    },
)
_OptionalListNetworkResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListNetworkResourcesRequestRequestTypeDef",
    {
        "filters": Dict[NetworkResourceFilterKeysType, List[str]],
        "maxResults": int,
        "startToken": str,
    },
    total=False,
)

class ListNetworkResourcesRequestRequestTypeDef(
    _RequiredListNetworkResourcesRequestRequestTypeDef,
    _OptionalListNetworkResourcesRequestRequestTypeDef,
):
    pass

ListNetworkResourcesResponseTypeDef = TypedDict(
    "ListNetworkResourcesResponseTypeDef",
    {
        "networkResources": List["NetworkResourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListNetworkSitesRequestRequestTypeDef = TypedDict(
    "_RequiredListNetworkSitesRequestRequestTypeDef",
    {
        "networkArn": str,
    },
)
_OptionalListNetworkSitesRequestRequestTypeDef = TypedDict(
    "_OptionalListNetworkSitesRequestRequestTypeDef",
    {
        "filters": Dict[Literal["STATUS"], List[str]],
        "maxResults": int,
        "startToken": str,
    },
    total=False,
)

class ListNetworkSitesRequestRequestTypeDef(
    _RequiredListNetworkSitesRequestRequestTypeDef, _OptionalListNetworkSitesRequestRequestTypeDef
):
    pass

ListNetworkSitesResponseTypeDef = TypedDict(
    "ListNetworkSitesResponseTypeDef",
    {
        "networkSites": List["NetworkSiteTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNetworksRequestRequestTypeDef = TypedDict(
    "ListNetworksRequestRequestTypeDef",
    {
        "filters": Dict[Literal["STATUS"], List[str]],
        "maxResults": int,
        "startToken": str,
    },
    total=False,
)

ListNetworksResponseTypeDef = TypedDict(
    "ListNetworksResponseTypeDef",
    {
        "networks": List["NetworkTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListOrdersRequestRequestTypeDef = TypedDict(
    "_RequiredListOrdersRequestRequestTypeDef",
    {
        "networkArn": str,
    },
)
_OptionalListOrdersRequestRequestTypeDef = TypedDict(
    "_OptionalListOrdersRequestRequestTypeDef",
    {
        "filters": Dict[OrderFilterKeysType, List[str]],
        "maxResults": int,
        "startToken": str,
    },
    total=False,
)

class ListOrdersRequestRequestTypeDef(
    _RequiredListOrdersRequestRequestTypeDef, _OptionalListOrdersRequestRequestTypeDef
):
    pass

ListOrdersResponseTypeDef = TypedDict(
    "ListOrdersResponseTypeDef",
    {
        "nextToken": str,
        "orders": List["OrderTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredNameValuePairTypeDef = TypedDict(
    "_RequiredNameValuePairTypeDef",
    {
        "name": str,
    },
)
_OptionalNameValuePairTypeDef = TypedDict(
    "_OptionalNameValuePairTypeDef",
    {
        "value": str,
    },
    total=False,
)

class NameValuePairTypeDef(_RequiredNameValuePairTypeDef, _OptionalNameValuePairTypeDef):
    pass

_RequiredNetworkResourceDefinitionTypeDef = TypedDict(
    "_RequiredNetworkResourceDefinitionTypeDef",
    {
        "count": int,
        "type": NetworkResourceDefinitionTypeType,
    },
)
_OptionalNetworkResourceDefinitionTypeDef = TypedDict(
    "_OptionalNetworkResourceDefinitionTypeDef",
    {
        "options": List["NameValuePairTypeDef"],
    },
    total=False,
)

class NetworkResourceDefinitionTypeDef(
    _RequiredNetworkResourceDefinitionTypeDef, _OptionalNetworkResourceDefinitionTypeDef
):
    pass

NetworkResourceTypeDef = TypedDict(
    "NetworkResourceTypeDef",
    {
        "attributes": List["NameValuePairTypeDef"],
        "createdAt": datetime,
        "description": str,
        "health": HealthStatusType,
        "model": str,
        "networkArn": str,
        "networkResourceArn": str,
        "networkSiteArn": str,
        "orderArn": str,
        "position": "PositionTypeDef",
        "returnInformation": "ReturnInformationTypeDef",
        "serialNumber": str,
        "status": NetworkResourceStatusType,
        "statusReason": str,
        "type": Literal["RADIO_UNIT"],
        "vendor": str,
    },
    total=False,
)

_RequiredNetworkSiteTypeDef = TypedDict(
    "_RequiredNetworkSiteTypeDef",
    {
        "networkArn": str,
        "networkSiteArn": str,
        "networkSiteName": str,
        "status": NetworkSiteStatusType,
    },
)
_OptionalNetworkSiteTypeDef = TypedDict(
    "_OptionalNetworkSiteTypeDef",
    {
        "availabilityZone": str,
        "availabilityZoneId": str,
        "createdAt": datetime,
        "currentPlan": "SitePlanTypeDef",
        "description": str,
        "pendingPlan": "SitePlanTypeDef",
        "statusReason": str,
    },
    total=False,
)

class NetworkSiteTypeDef(_RequiredNetworkSiteTypeDef, _OptionalNetworkSiteTypeDef):
    pass

_RequiredNetworkTypeDef = TypedDict(
    "_RequiredNetworkTypeDef",
    {
        "networkArn": str,
        "networkName": str,
        "status": NetworkStatusType,
    },
)
_OptionalNetworkTypeDef = TypedDict(
    "_OptionalNetworkTypeDef",
    {
        "createdAt": datetime,
        "description": str,
        "statusReason": str,
    },
    total=False,
)

class NetworkTypeDef(_RequiredNetworkTypeDef, _OptionalNetworkTypeDef):
    pass

OrderTypeDef = TypedDict(
    "OrderTypeDef",
    {
        "acknowledgmentStatus": AcknowledgmentStatusType,
        "createdAt": datetime,
        "networkArn": str,
        "networkSiteArn": str,
        "orderArn": str,
        "shippingAddress": "AddressTypeDef",
        "trackingInformation": List["TrackingInformationTypeDef"],
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

PingResponseTypeDef = TypedDict(
    "PingResponseTypeDef",
    {
        "status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PositionTypeDef = TypedDict(
    "PositionTypeDef",
    {
        "elevation": float,
        "elevationReference": ElevationReferenceType,
        "elevationUnit": Literal["FEET"],
        "latitude": float,
        "longitude": float,
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

ReturnInformationTypeDef = TypedDict(
    "ReturnInformationTypeDef",
    {
        "replacementOrderArn": str,
        "returnReason": str,
        "shippingAddress": "AddressTypeDef",
        "shippingLabel": str,
    },
    total=False,
)

SitePlanTypeDef = TypedDict(
    "SitePlanTypeDef",
    {
        "options": List["NameValuePairTypeDef"],
        "resourceDefinitions": List["NetworkResourceDefinitionTypeDef"],
    },
    total=False,
)

_RequiredStartNetworkResourceUpdateRequestRequestTypeDef = TypedDict(
    "_RequiredStartNetworkResourceUpdateRequestRequestTypeDef",
    {
        "networkResourceArn": str,
        "updateType": UpdateTypeType,
    },
)
_OptionalStartNetworkResourceUpdateRequestRequestTypeDef = TypedDict(
    "_OptionalStartNetworkResourceUpdateRequestRequestTypeDef",
    {
        "returnReason": str,
        "shippingAddress": "AddressTypeDef",
    },
    total=False,
)

class StartNetworkResourceUpdateRequestRequestTypeDef(
    _RequiredStartNetworkResourceUpdateRequestRequestTypeDef,
    _OptionalStartNetworkResourceUpdateRequestRequestTypeDef,
):
    pass

StartNetworkResourceUpdateResponseTypeDef = TypedDict(
    "StartNetworkResourceUpdateResponseTypeDef",
    {
        "networkResource": "NetworkResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TrackingInformationTypeDef = TypedDict(
    "TrackingInformationTypeDef",
    {
        "trackingNumber": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateNetworkSitePlanRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateNetworkSitePlanRequestRequestTypeDef",
    {
        "networkSiteArn": str,
        "pendingPlan": "SitePlanTypeDef",
    },
)
_OptionalUpdateNetworkSitePlanRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateNetworkSitePlanRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateNetworkSitePlanRequestRequestTypeDef(
    _RequiredUpdateNetworkSitePlanRequestRequestTypeDef,
    _OptionalUpdateNetworkSitePlanRequestRequestTypeDef,
):
    pass

_RequiredUpdateNetworkSiteRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateNetworkSiteRequestRequestTypeDef",
    {
        "networkSiteArn": str,
    },
)
_OptionalUpdateNetworkSiteRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateNetworkSiteRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
    },
    total=False,
)

class UpdateNetworkSiteRequestRequestTypeDef(
    _RequiredUpdateNetworkSiteRequestRequestTypeDef, _OptionalUpdateNetworkSiteRequestRequestTypeDef
):
    pass

UpdateNetworkSiteResponseTypeDef = TypedDict(
    "UpdateNetworkSiteResponseTypeDef",
    {
        "networkSite": "NetworkSiteTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
