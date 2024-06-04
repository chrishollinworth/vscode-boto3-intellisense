"""
Type annotations for outposts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_outposts.type_defs import AddressTypeDef

    data: AddressTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AddressTypeType,
    AssetStateType,
    CapacityTaskStatusType,
    CatalogItemClassType,
    CatalogItemStatusType,
    ComputeAssetStateType,
    FiberOpticCableTypeType,
    LineItemStatusType,
    MaximumSupportedWeightLbsType,
    OpticalStandardType,
    OrderStatusType,
    OrderTypeType,
    PaymentOptionType,
    PaymentTermType,
    PowerConnectorType,
    PowerDrawKvaType,
    PowerFeedDropType,
    PowerPhaseType,
    ShipmentCarrierType,
    SupportedHardwareTypeType,
    SupportedStorageEnumType,
    UplinkCountType,
    UplinkGbpsType,
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
    "AddressTypeDef",
    "AssetInfoTypeDef",
    "AssetLocationTypeDef",
    "CancelCapacityTaskInputRequestTypeDef",
    "CancelOrderInputRequestTypeDef",
    "CapacityTaskFailureTypeDef",
    "CapacityTaskSummaryTypeDef",
    "CatalogItemTypeDef",
    "ComputeAttributesTypeDef",
    "ConnectionDetailsTypeDef",
    "CreateOrderInputRequestTypeDef",
    "CreateOrderOutputTypeDef",
    "CreateOutpostInputRequestTypeDef",
    "CreateOutpostOutputTypeDef",
    "CreateSiteInputRequestTypeDef",
    "CreateSiteOutputTypeDef",
    "DeleteOutpostInputRequestTypeDef",
    "DeleteSiteInputRequestTypeDef",
    "EC2CapacityTypeDef",
    "GetCapacityTaskInputRequestTypeDef",
    "GetCapacityTaskOutputTypeDef",
    "GetCatalogItemInputRequestTypeDef",
    "GetCatalogItemOutputTypeDef",
    "GetConnectionRequestRequestTypeDef",
    "GetConnectionResponseTypeDef",
    "GetOrderInputRequestTypeDef",
    "GetOrderOutputTypeDef",
    "GetOutpostInputRequestTypeDef",
    "GetOutpostInstanceTypesInputRequestTypeDef",
    "GetOutpostInstanceTypesOutputTypeDef",
    "GetOutpostOutputTypeDef",
    "GetOutpostSupportedInstanceTypesInputRequestTypeDef",
    "GetOutpostSupportedInstanceTypesOutputTypeDef",
    "GetSiteAddressInputRequestTypeDef",
    "GetSiteAddressOutputTypeDef",
    "GetSiteInputRequestTypeDef",
    "GetSiteOutputTypeDef",
    "InstanceTypeCapacityTypeDef",
    "InstanceTypeItemTypeDef",
    "LineItemAssetInformationTypeDef",
    "LineItemRequestTypeDef",
    "LineItemTypeDef",
    "ListAssetsInputRequestTypeDef",
    "ListAssetsOutputTypeDef",
    "ListCapacityTasksInputRequestTypeDef",
    "ListCapacityTasksOutputTypeDef",
    "ListCatalogItemsInputRequestTypeDef",
    "ListCatalogItemsOutputTypeDef",
    "ListOrdersInputRequestTypeDef",
    "ListOrdersOutputTypeDef",
    "ListOutpostsInputRequestTypeDef",
    "ListOutpostsOutputTypeDef",
    "ListSitesInputRequestTypeDef",
    "ListSitesOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OrderSummaryTypeDef",
    "OrderTypeDef",
    "OutpostTypeDef",
    "PaginatorConfigTypeDef",
    "RackPhysicalPropertiesTypeDef",
    "ResponseMetadataTypeDef",
    "ShipmentInformationTypeDef",
    "SiteTypeDef",
    "StartCapacityTaskInputRequestTypeDef",
    "StartCapacityTaskOutputTypeDef",
    "StartConnectionRequestRequestTypeDef",
    "StartConnectionResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateOutpostInputRequestTypeDef",
    "UpdateOutpostOutputTypeDef",
    "UpdateSiteAddressInputRequestTypeDef",
    "UpdateSiteAddressOutputTypeDef",
    "UpdateSiteInputRequestTypeDef",
    "UpdateSiteOutputTypeDef",
    "UpdateSiteRackPhysicalPropertiesInputRequestTypeDef",
    "UpdateSiteRackPhysicalPropertiesOutputTypeDef",
)

_RequiredAddressTypeDef = TypedDict(
    "_RequiredAddressTypeDef",
    {
        "AddressLine1": str,
        "City": str,
        "StateOrRegion": str,
        "PostalCode": str,
        "CountryCode": str,
    },
)
_OptionalAddressTypeDef = TypedDict(
    "_OptionalAddressTypeDef",
    {
        "ContactName": str,
        "ContactPhoneNumber": str,
        "AddressLine2": str,
        "AddressLine3": str,
        "DistrictOrCounty": str,
        "Municipality": str,
    },
    total=False,
)

class AddressTypeDef(_RequiredAddressTypeDef, _OptionalAddressTypeDef):
    pass

AssetInfoTypeDef = TypedDict(
    "AssetInfoTypeDef",
    {
        "AssetId": str,
        "RackId": str,
        "AssetType": Literal["COMPUTE"],
        "ComputeAttributes": "ComputeAttributesTypeDef",
        "AssetLocation": "AssetLocationTypeDef",
    },
    total=False,
)

AssetLocationTypeDef = TypedDict(
    "AssetLocationTypeDef",
    {
        "RackElevation": float,
    },
    total=False,
)

CancelCapacityTaskInputRequestTypeDef = TypedDict(
    "CancelCapacityTaskInputRequestTypeDef",
    {
        "CapacityTaskId": str,
        "OutpostIdentifier": str,
    },
)

CancelOrderInputRequestTypeDef = TypedDict(
    "CancelOrderInputRequestTypeDef",
    {
        "OrderId": str,
    },
)

_RequiredCapacityTaskFailureTypeDef = TypedDict(
    "_RequiredCapacityTaskFailureTypeDef",
    {
        "Reason": str,
    },
)
_OptionalCapacityTaskFailureTypeDef = TypedDict(
    "_OptionalCapacityTaskFailureTypeDef",
    {
        "Type": Literal["UNSUPPORTED_CAPACITY_CONFIGURATION"],
    },
    total=False,
)

class CapacityTaskFailureTypeDef(
    _RequiredCapacityTaskFailureTypeDef, _OptionalCapacityTaskFailureTypeDef
):
    pass

CapacityTaskSummaryTypeDef = TypedDict(
    "CapacityTaskSummaryTypeDef",
    {
        "CapacityTaskId": str,
        "OutpostId": str,
        "OrderId": str,
        "CapacityTaskStatus": CapacityTaskStatusType,
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "LastModifiedDate": datetime,
    },
    total=False,
)

CatalogItemTypeDef = TypedDict(
    "CatalogItemTypeDef",
    {
        "CatalogItemId": str,
        "ItemStatus": CatalogItemStatusType,
        "EC2Capacities": List["EC2CapacityTypeDef"],
        "PowerKva": float,
        "WeightLbs": int,
        "SupportedUplinkGbps": List[int],
        "SupportedStorage": List[SupportedStorageEnumType],
    },
    total=False,
)

ComputeAttributesTypeDef = TypedDict(
    "ComputeAttributesTypeDef",
    {
        "HostId": str,
        "State": ComputeAssetStateType,
        "InstanceFamilies": List[str],
    },
    total=False,
)

ConnectionDetailsTypeDef = TypedDict(
    "ConnectionDetailsTypeDef",
    {
        "ClientPublicKey": str,
        "ServerPublicKey": str,
        "ServerEndpoint": str,
        "ClientTunnelAddress": str,
        "ServerTunnelAddress": str,
        "AllowedIps": List[str],
    },
    total=False,
)

_RequiredCreateOrderInputRequestTypeDef = TypedDict(
    "_RequiredCreateOrderInputRequestTypeDef",
    {
        "OutpostIdentifier": str,
        "LineItems": List["LineItemRequestTypeDef"],
        "PaymentOption": PaymentOptionType,
    },
)
_OptionalCreateOrderInputRequestTypeDef = TypedDict(
    "_OptionalCreateOrderInputRequestTypeDef",
    {
        "PaymentTerm": PaymentTermType,
    },
    total=False,
)

class CreateOrderInputRequestTypeDef(
    _RequiredCreateOrderInputRequestTypeDef, _OptionalCreateOrderInputRequestTypeDef
):
    pass

CreateOrderOutputTypeDef = TypedDict(
    "CreateOrderOutputTypeDef",
    {
        "Order": "OrderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOutpostInputRequestTypeDef = TypedDict(
    "_RequiredCreateOutpostInputRequestTypeDef",
    {
        "Name": str,
        "SiteId": str,
    },
)
_OptionalCreateOutpostInputRequestTypeDef = TypedDict(
    "_OptionalCreateOutpostInputRequestTypeDef",
    {
        "Description": str,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "Tags": Dict[str, str],
        "SupportedHardwareType": SupportedHardwareTypeType,
    },
    total=False,
)

class CreateOutpostInputRequestTypeDef(
    _RequiredCreateOutpostInputRequestTypeDef, _OptionalCreateOutpostInputRequestTypeDef
):
    pass

CreateOutpostOutputTypeDef = TypedDict(
    "CreateOutpostOutputTypeDef",
    {
        "Outpost": "OutpostTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSiteInputRequestTypeDef = TypedDict(
    "_RequiredCreateSiteInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateSiteInputRequestTypeDef = TypedDict(
    "_OptionalCreateSiteInputRequestTypeDef",
    {
        "Description": str,
        "Notes": str,
        "Tags": Dict[str, str],
        "OperatingAddress": "AddressTypeDef",
        "ShippingAddress": "AddressTypeDef",
        "RackPhysicalProperties": "RackPhysicalPropertiesTypeDef",
    },
    total=False,
)

class CreateSiteInputRequestTypeDef(
    _RequiredCreateSiteInputRequestTypeDef, _OptionalCreateSiteInputRequestTypeDef
):
    pass

CreateSiteOutputTypeDef = TypedDict(
    "CreateSiteOutputTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOutpostInputRequestTypeDef = TypedDict(
    "DeleteOutpostInputRequestTypeDef",
    {
        "OutpostId": str,
    },
)

DeleteSiteInputRequestTypeDef = TypedDict(
    "DeleteSiteInputRequestTypeDef",
    {
        "SiteId": str,
    },
)

EC2CapacityTypeDef = TypedDict(
    "EC2CapacityTypeDef",
    {
        "Family": str,
        "MaxSize": str,
        "Quantity": str,
    },
    total=False,
)

GetCapacityTaskInputRequestTypeDef = TypedDict(
    "GetCapacityTaskInputRequestTypeDef",
    {
        "CapacityTaskId": str,
        "OutpostIdentifier": str,
    },
)

GetCapacityTaskOutputTypeDef = TypedDict(
    "GetCapacityTaskOutputTypeDef",
    {
        "CapacityTaskId": str,
        "OutpostId": str,
        "OrderId": str,
        "RequestedInstancePools": List["InstanceTypeCapacityTypeDef"],
        "DryRun": bool,
        "CapacityTaskStatus": CapacityTaskStatusType,
        "Failed": "CapacityTaskFailureTypeDef",
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "LastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCatalogItemInputRequestTypeDef = TypedDict(
    "GetCatalogItemInputRequestTypeDef",
    {
        "CatalogItemId": str,
    },
)

GetCatalogItemOutputTypeDef = TypedDict(
    "GetCatalogItemOutputTypeDef",
    {
        "CatalogItem": "CatalogItemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectionRequestRequestTypeDef = TypedDict(
    "GetConnectionRequestRequestTypeDef",
    {
        "ConnectionId": str,
    },
)

GetConnectionResponseTypeDef = TypedDict(
    "GetConnectionResponseTypeDef",
    {
        "ConnectionId": str,
        "ConnectionDetails": "ConnectionDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOrderInputRequestTypeDef = TypedDict(
    "GetOrderInputRequestTypeDef",
    {
        "OrderId": str,
    },
)

GetOrderOutputTypeDef = TypedDict(
    "GetOrderOutputTypeDef",
    {
        "Order": "OrderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOutpostInputRequestTypeDef = TypedDict(
    "GetOutpostInputRequestTypeDef",
    {
        "OutpostId": str,
    },
)

_RequiredGetOutpostInstanceTypesInputRequestTypeDef = TypedDict(
    "_RequiredGetOutpostInstanceTypesInputRequestTypeDef",
    {
        "OutpostId": str,
    },
)
_OptionalGetOutpostInstanceTypesInputRequestTypeDef = TypedDict(
    "_OptionalGetOutpostInstanceTypesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetOutpostInstanceTypesInputRequestTypeDef(
    _RequiredGetOutpostInstanceTypesInputRequestTypeDef,
    _OptionalGetOutpostInstanceTypesInputRequestTypeDef,
):
    pass

GetOutpostInstanceTypesOutputTypeDef = TypedDict(
    "GetOutpostInstanceTypesOutputTypeDef",
    {
        "InstanceTypes": List["InstanceTypeItemTypeDef"],
        "NextToken": str,
        "OutpostId": str,
        "OutpostArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOutpostOutputTypeDef = TypedDict(
    "GetOutpostOutputTypeDef",
    {
        "Outpost": "OutpostTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOutpostSupportedInstanceTypesInputRequestTypeDef = TypedDict(
    "_RequiredGetOutpostSupportedInstanceTypesInputRequestTypeDef",
    {
        "OutpostIdentifier": str,
        "OrderId": str,
    },
)
_OptionalGetOutpostSupportedInstanceTypesInputRequestTypeDef = TypedDict(
    "_OptionalGetOutpostSupportedInstanceTypesInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetOutpostSupportedInstanceTypesInputRequestTypeDef(
    _RequiredGetOutpostSupportedInstanceTypesInputRequestTypeDef,
    _OptionalGetOutpostSupportedInstanceTypesInputRequestTypeDef,
):
    pass

GetOutpostSupportedInstanceTypesOutputTypeDef = TypedDict(
    "GetOutpostSupportedInstanceTypesOutputTypeDef",
    {
        "InstanceTypes": List["InstanceTypeItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSiteAddressInputRequestTypeDef = TypedDict(
    "GetSiteAddressInputRequestTypeDef",
    {
        "SiteId": str,
        "AddressType": AddressTypeType,
    },
)

GetSiteAddressOutputTypeDef = TypedDict(
    "GetSiteAddressOutputTypeDef",
    {
        "SiteId": str,
        "AddressType": AddressTypeType,
        "Address": "AddressTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSiteInputRequestTypeDef = TypedDict(
    "GetSiteInputRequestTypeDef",
    {
        "SiteId": str,
    },
)

GetSiteOutputTypeDef = TypedDict(
    "GetSiteOutputTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceTypeCapacityTypeDef = TypedDict(
    "InstanceTypeCapacityTypeDef",
    {
        "InstanceType": str,
        "Count": int,
    },
)

InstanceTypeItemTypeDef = TypedDict(
    "InstanceTypeItemTypeDef",
    {
        "InstanceType": str,
    },
    total=False,
)

LineItemAssetInformationTypeDef = TypedDict(
    "LineItemAssetInformationTypeDef",
    {
        "AssetId": str,
        "MacAddressList": List[str],
    },
    total=False,
)

LineItemRequestTypeDef = TypedDict(
    "LineItemRequestTypeDef",
    {
        "CatalogItemId": str,
        "Quantity": int,
    },
    total=False,
)

LineItemTypeDef = TypedDict(
    "LineItemTypeDef",
    {
        "CatalogItemId": str,
        "LineItemId": str,
        "Quantity": int,
        "Status": LineItemStatusType,
        "ShipmentInformation": "ShipmentInformationTypeDef",
        "AssetInformationList": List["LineItemAssetInformationTypeDef"],
        "PreviousLineItemId": str,
        "PreviousOrderId": str,
    },
    total=False,
)

_RequiredListAssetsInputRequestTypeDef = TypedDict(
    "_RequiredListAssetsInputRequestTypeDef",
    {
        "OutpostIdentifier": str,
    },
)
_OptionalListAssetsInputRequestTypeDef = TypedDict(
    "_OptionalListAssetsInputRequestTypeDef",
    {
        "HostIdFilter": List[str],
        "MaxResults": int,
        "NextToken": str,
        "StatusFilter": List[AssetStateType],
    },
    total=False,
)

class ListAssetsInputRequestTypeDef(
    _RequiredListAssetsInputRequestTypeDef, _OptionalListAssetsInputRequestTypeDef
):
    pass

ListAssetsOutputTypeDef = TypedDict(
    "ListAssetsOutputTypeDef",
    {
        "Assets": List["AssetInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCapacityTasksInputRequestTypeDef = TypedDict(
    "ListCapacityTasksInputRequestTypeDef",
    {
        "OutpostIdentifierFilter": str,
        "MaxResults": int,
        "NextToken": str,
        "CapacityTaskStatusFilter": List[CapacityTaskStatusType],
    },
    total=False,
)

ListCapacityTasksOutputTypeDef = TypedDict(
    "ListCapacityTasksOutputTypeDef",
    {
        "CapacityTasks": List["CapacityTaskSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCatalogItemsInputRequestTypeDef = TypedDict(
    "ListCatalogItemsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ItemClassFilter": List[CatalogItemClassType],
        "SupportedStorageFilter": List[SupportedStorageEnumType],
        "EC2FamilyFilter": List[str],
    },
    total=False,
)

ListCatalogItemsOutputTypeDef = TypedDict(
    "ListCatalogItemsOutputTypeDef",
    {
        "CatalogItems": List["CatalogItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrdersInputRequestTypeDef = TypedDict(
    "ListOrdersInputRequestTypeDef",
    {
        "OutpostIdentifierFilter": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListOrdersOutputTypeDef = TypedDict(
    "ListOrdersOutputTypeDef",
    {
        "Orders": List["OrderSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOutpostsInputRequestTypeDef = TypedDict(
    "ListOutpostsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "LifeCycleStatusFilter": List[str],
        "AvailabilityZoneFilter": List[str],
        "AvailabilityZoneIdFilter": List[str],
    },
    total=False,
)

ListOutpostsOutputTypeDef = TypedDict(
    "ListOutpostsOutputTypeDef",
    {
        "Outposts": List["OutpostTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSitesInputRequestTypeDef = TypedDict(
    "ListSitesInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "OperatingAddressCountryCodeFilter": List[str],
        "OperatingAddressStateOrRegionFilter": List[str],
        "OperatingAddressCityFilter": List[str],
    },
    total=False,
)

ListSitesOutputTypeDef = TypedDict(
    "ListSitesOutputTypeDef",
    {
        "Sites": List["SiteTypeDef"],
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
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OrderSummaryTypeDef = TypedDict(
    "OrderSummaryTypeDef",
    {
        "OutpostId": str,
        "OrderId": str,
        "OrderType": OrderTypeType,
        "Status": OrderStatusType,
        "LineItemCountsByStatus": Dict[LineItemStatusType, int],
        "OrderSubmissionDate": datetime,
        "OrderFulfilledDate": datetime,
    },
    total=False,
)

OrderTypeDef = TypedDict(
    "OrderTypeDef",
    {
        "OutpostId": str,
        "OrderId": str,
        "Status": OrderStatusType,
        "LineItems": List["LineItemTypeDef"],
        "PaymentOption": PaymentOptionType,
        "OrderSubmissionDate": datetime,
        "OrderFulfilledDate": datetime,
        "PaymentTerm": PaymentTermType,
        "OrderType": OrderTypeType,
    },
    total=False,
)

OutpostTypeDef = TypedDict(
    "OutpostTypeDef",
    {
        "OutpostId": str,
        "OwnerId": str,
        "OutpostArn": str,
        "SiteId": str,
        "Name": str,
        "Description": str,
        "LifeCycleStatus": str,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "Tags": Dict[str, str],
        "SiteArn": str,
        "SupportedHardwareType": SupportedHardwareTypeType,
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

RackPhysicalPropertiesTypeDef = TypedDict(
    "RackPhysicalPropertiesTypeDef",
    {
        "PowerDrawKva": PowerDrawKvaType,
        "PowerPhase": PowerPhaseType,
        "PowerConnector": PowerConnectorType,
        "PowerFeedDrop": PowerFeedDropType,
        "UplinkGbps": UplinkGbpsType,
        "UplinkCount": UplinkCountType,
        "FiberOpticCableType": FiberOpticCableTypeType,
        "OpticalStandard": OpticalStandardType,
        "MaximumSupportedWeightLbs": MaximumSupportedWeightLbsType,
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

ShipmentInformationTypeDef = TypedDict(
    "ShipmentInformationTypeDef",
    {
        "ShipmentTrackingNumber": str,
        "ShipmentCarrier": ShipmentCarrierType,
    },
    total=False,
)

SiteTypeDef = TypedDict(
    "SiteTypeDef",
    {
        "SiteId": str,
        "AccountId": str,
        "Name": str,
        "Description": str,
        "Tags": Dict[str, str],
        "SiteArn": str,
        "Notes": str,
        "OperatingAddressCountryCode": str,
        "OperatingAddressStateOrRegion": str,
        "OperatingAddressCity": str,
        "RackPhysicalProperties": "RackPhysicalPropertiesTypeDef",
    },
    total=False,
)

_RequiredStartCapacityTaskInputRequestTypeDef = TypedDict(
    "_RequiredStartCapacityTaskInputRequestTypeDef",
    {
        "OutpostIdentifier": str,
        "OrderId": str,
        "InstancePools": List["InstanceTypeCapacityTypeDef"],
    },
)
_OptionalStartCapacityTaskInputRequestTypeDef = TypedDict(
    "_OptionalStartCapacityTaskInputRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class StartCapacityTaskInputRequestTypeDef(
    _RequiredStartCapacityTaskInputRequestTypeDef, _OptionalStartCapacityTaskInputRequestTypeDef
):
    pass

StartCapacityTaskOutputTypeDef = TypedDict(
    "StartCapacityTaskOutputTypeDef",
    {
        "CapacityTaskId": str,
        "OutpostId": str,
        "OrderId": str,
        "RequestedInstancePools": List["InstanceTypeCapacityTypeDef"],
        "DryRun": bool,
        "CapacityTaskStatus": CapacityTaskStatusType,
        "Failed": "CapacityTaskFailureTypeDef",
        "CreationDate": datetime,
        "CompletionDate": datetime,
        "LastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredStartConnectionRequestRequestTypeDef",
    {
        "AssetId": str,
        "ClientPublicKey": str,
        "NetworkInterfaceDeviceIndex": int,
    },
)
_OptionalStartConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalStartConnectionRequestRequestTypeDef",
    {
        "DeviceSerialNumber": str,
    },
    total=False,
)

class StartConnectionRequestRequestTypeDef(
    _RequiredStartConnectionRequestRequestTypeDef, _OptionalStartConnectionRequestRequestTypeDef
):
    pass

StartConnectionResponseTypeDef = TypedDict(
    "StartConnectionResponseTypeDef",
    {
        "ConnectionId": str,
        "UnderlayIpAddress": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateOutpostInputRequestTypeDef = TypedDict(
    "_RequiredUpdateOutpostInputRequestTypeDef",
    {
        "OutpostId": str,
    },
)
_OptionalUpdateOutpostInputRequestTypeDef = TypedDict(
    "_OptionalUpdateOutpostInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "SupportedHardwareType": SupportedHardwareTypeType,
    },
    total=False,
)

class UpdateOutpostInputRequestTypeDef(
    _RequiredUpdateOutpostInputRequestTypeDef, _OptionalUpdateOutpostInputRequestTypeDef
):
    pass

UpdateOutpostOutputTypeDef = TypedDict(
    "UpdateOutpostOutputTypeDef",
    {
        "Outpost": "OutpostTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSiteAddressInputRequestTypeDef = TypedDict(
    "UpdateSiteAddressInputRequestTypeDef",
    {
        "SiteId": str,
        "AddressType": AddressTypeType,
        "Address": "AddressTypeDef",
    },
)

UpdateSiteAddressOutputTypeDef = TypedDict(
    "UpdateSiteAddressOutputTypeDef",
    {
        "AddressType": AddressTypeType,
        "Address": "AddressTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSiteInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSiteInputRequestTypeDef",
    {
        "SiteId": str,
    },
)
_OptionalUpdateSiteInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSiteInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Notes": str,
    },
    total=False,
)

class UpdateSiteInputRequestTypeDef(
    _RequiredUpdateSiteInputRequestTypeDef, _OptionalUpdateSiteInputRequestTypeDef
):
    pass

UpdateSiteOutputTypeDef = TypedDict(
    "UpdateSiteOutputTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSiteRackPhysicalPropertiesInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSiteRackPhysicalPropertiesInputRequestTypeDef",
    {
        "SiteId": str,
    },
)
_OptionalUpdateSiteRackPhysicalPropertiesInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSiteRackPhysicalPropertiesInputRequestTypeDef",
    {
        "PowerDrawKva": PowerDrawKvaType,
        "PowerPhase": PowerPhaseType,
        "PowerConnector": PowerConnectorType,
        "PowerFeedDrop": PowerFeedDropType,
        "UplinkGbps": UplinkGbpsType,
        "UplinkCount": UplinkCountType,
        "FiberOpticCableType": FiberOpticCableTypeType,
        "OpticalStandard": OpticalStandardType,
        "MaximumSupportedWeightLbs": MaximumSupportedWeightLbsType,
    },
    total=False,
)

class UpdateSiteRackPhysicalPropertiesInputRequestTypeDef(
    _RequiredUpdateSiteRackPhysicalPropertiesInputRequestTypeDef,
    _OptionalUpdateSiteRackPhysicalPropertiesInputRequestTypeDef,
):
    pass

UpdateSiteRackPhysicalPropertiesOutputTypeDef = TypedDict(
    "UpdateSiteRackPhysicalPropertiesOutputTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
