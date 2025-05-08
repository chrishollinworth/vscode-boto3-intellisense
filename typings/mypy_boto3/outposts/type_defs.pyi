"""
Type annotations for outposts service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_outposts.type_defs import AddressTypeDef

    data: AddressTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AddressTypeType,
    AssetStateType,
    AWSServiceNameType,
    CapacityTaskFailureTypeType,
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
    TaskActionOnBlockingInstancesType,
    UplinkCountType,
    UplinkGbpsType,
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
    "AddressTypeDef",
    "AssetInfoTypeDef",
    "AssetInstanceTypeCapacityTypeDef",
    "AssetInstanceTypeDef",
    "AssetLocationTypeDef",
    "BlockingInstanceTypeDef",
    "CancelCapacityTaskInputTypeDef",
    "CancelOrderInputTypeDef",
    "CapacityTaskFailureTypeDef",
    "CapacityTaskSummaryTypeDef",
    "CatalogItemTypeDef",
    "ComputeAttributesTypeDef",
    "ConnectionDetailsTypeDef",
    "CreateOrderInputTypeDef",
    "CreateOrderOutputTypeDef",
    "CreateOutpostInputTypeDef",
    "CreateOutpostOutputTypeDef",
    "CreateSiteInputTypeDef",
    "CreateSiteOutputTypeDef",
    "DeleteOutpostInputTypeDef",
    "DeleteSiteInputTypeDef",
    "EC2CapacityTypeDef",
    "GetCapacityTaskInputTypeDef",
    "GetCapacityTaskOutputTypeDef",
    "GetCatalogItemInputTypeDef",
    "GetCatalogItemOutputTypeDef",
    "GetConnectionRequestTypeDef",
    "GetConnectionResponseTypeDef",
    "GetOrderInputTypeDef",
    "GetOrderOutputTypeDef",
    "GetOutpostInputTypeDef",
    "GetOutpostInstanceTypesInputPaginateTypeDef",
    "GetOutpostInstanceTypesInputTypeDef",
    "GetOutpostInstanceTypesOutputTypeDef",
    "GetOutpostOutputTypeDef",
    "GetOutpostSupportedInstanceTypesInputPaginateTypeDef",
    "GetOutpostSupportedInstanceTypesInputTypeDef",
    "GetOutpostSupportedInstanceTypesOutputTypeDef",
    "GetSiteAddressInputTypeDef",
    "GetSiteAddressOutputTypeDef",
    "GetSiteInputTypeDef",
    "GetSiteOutputTypeDef",
    "InstanceTypeCapacityTypeDef",
    "InstanceTypeItemTypeDef",
    "InstancesToExcludeOutputTypeDef",
    "InstancesToExcludeTypeDef",
    "InstancesToExcludeUnionTypeDef",
    "LineItemAssetInformationTypeDef",
    "LineItemRequestTypeDef",
    "LineItemTypeDef",
    "ListAssetInstancesInputPaginateTypeDef",
    "ListAssetInstancesInputTypeDef",
    "ListAssetInstancesOutputTypeDef",
    "ListAssetsInputPaginateTypeDef",
    "ListAssetsInputTypeDef",
    "ListAssetsOutputTypeDef",
    "ListBlockingInstancesForCapacityTaskInputPaginateTypeDef",
    "ListBlockingInstancesForCapacityTaskInputTypeDef",
    "ListBlockingInstancesForCapacityTaskOutputTypeDef",
    "ListCapacityTasksInputPaginateTypeDef",
    "ListCapacityTasksInputTypeDef",
    "ListCapacityTasksOutputTypeDef",
    "ListCatalogItemsInputPaginateTypeDef",
    "ListCatalogItemsInputTypeDef",
    "ListCatalogItemsOutputTypeDef",
    "ListOrdersInputPaginateTypeDef",
    "ListOrdersInputTypeDef",
    "ListOrdersOutputTypeDef",
    "ListOutpostsInputPaginateTypeDef",
    "ListOutpostsInputTypeDef",
    "ListOutpostsOutputTypeDef",
    "ListSitesInputPaginateTypeDef",
    "ListSitesInputTypeDef",
    "ListSitesOutputTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OrderSummaryTypeDef",
    "OrderTypeDef",
    "OutpostTypeDef",
    "PaginatorConfigTypeDef",
    "RackPhysicalPropertiesTypeDef",
    "ResponseMetadataTypeDef",
    "ShipmentInformationTypeDef",
    "SiteTypeDef",
    "StartCapacityTaskInputTypeDef",
    "StartCapacityTaskOutputTypeDef",
    "StartConnectionRequestTypeDef",
    "StartConnectionResponseTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateOutpostInputTypeDef",
    "UpdateOutpostOutputTypeDef",
    "UpdateSiteAddressInputTypeDef",
    "UpdateSiteAddressOutputTypeDef",
    "UpdateSiteInputTypeDef",
    "UpdateSiteOutputTypeDef",
    "UpdateSiteRackPhysicalPropertiesInputTypeDef",
    "UpdateSiteRackPhysicalPropertiesOutputTypeDef",
)

class AddressTypeDef(TypedDict):
    AddressLine1: str
    City: str
    StateOrRegion: str
    PostalCode: str
    CountryCode: str
    ContactName: NotRequired[str]
    ContactPhoneNumber: NotRequired[str]
    AddressLine2: NotRequired[str]
    AddressLine3: NotRequired[str]
    DistrictOrCounty: NotRequired[str]
    Municipality: NotRequired[str]

class AssetLocationTypeDef(TypedDict):
    RackElevation: NotRequired[float]

class AssetInstanceTypeCapacityTypeDef(TypedDict):
    InstanceType: str
    Count: int

class AssetInstanceTypeDef(TypedDict):
    InstanceId: NotRequired[str]
    InstanceType: NotRequired[str]
    AssetId: NotRequired[str]
    AccountId: NotRequired[str]
    AwsServiceName: NotRequired[AWSServiceNameType]

class BlockingInstanceTypeDef(TypedDict):
    InstanceId: NotRequired[str]
    AccountId: NotRequired[str]
    AwsServiceName: NotRequired[AWSServiceNameType]

class CancelCapacityTaskInputTypeDef(TypedDict):
    CapacityTaskId: str
    OutpostIdentifier: str

class CancelOrderInputTypeDef(TypedDict):
    OrderId: str

CapacityTaskFailureTypeDef = TypedDict(
    "CapacityTaskFailureTypeDef",
    {
        "Reason": str,
        "Type": NotRequired[CapacityTaskFailureTypeType],
    },
)

class CapacityTaskSummaryTypeDef(TypedDict):
    CapacityTaskId: NotRequired[str]
    OutpostId: NotRequired[str]
    OrderId: NotRequired[str]
    AssetId: NotRequired[str]
    CapacityTaskStatus: NotRequired[CapacityTaskStatusType]
    CreationDate: NotRequired[datetime]
    CompletionDate: NotRequired[datetime]
    LastModifiedDate: NotRequired[datetime]

class EC2CapacityTypeDef(TypedDict):
    Family: NotRequired[str]
    MaxSize: NotRequired[str]
    Quantity: NotRequired[str]

class ConnectionDetailsTypeDef(TypedDict):
    ClientPublicKey: NotRequired[str]
    ServerPublicKey: NotRequired[str]
    ServerEndpoint: NotRequired[str]
    ClientTunnelAddress: NotRequired[str]
    ServerTunnelAddress: NotRequired[str]
    AllowedIps: NotRequired[List[str]]

class LineItemRequestTypeDef(TypedDict):
    CatalogItemId: NotRequired[str]
    Quantity: NotRequired[int]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateOutpostInputTypeDef(TypedDict):
    Name: str
    SiteId: str
    Description: NotRequired[str]
    AvailabilityZone: NotRequired[str]
    AvailabilityZoneId: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    SupportedHardwareType: NotRequired[SupportedHardwareTypeType]

class OutpostTypeDef(TypedDict):
    OutpostId: NotRequired[str]
    OwnerId: NotRequired[str]
    OutpostArn: NotRequired[str]
    SiteId: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    LifeCycleStatus: NotRequired[str]
    AvailabilityZone: NotRequired[str]
    AvailabilityZoneId: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]
    SiteArn: NotRequired[str]
    SupportedHardwareType: NotRequired[SupportedHardwareTypeType]

class RackPhysicalPropertiesTypeDef(TypedDict):
    PowerDrawKva: NotRequired[PowerDrawKvaType]
    PowerPhase: NotRequired[PowerPhaseType]
    PowerConnector: NotRequired[PowerConnectorType]
    PowerFeedDrop: NotRequired[PowerFeedDropType]
    UplinkGbps: NotRequired[UplinkGbpsType]
    UplinkCount: NotRequired[UplinkCountType]
    FiberOpticCableType: NotRequired[FiberOpticCableTypeType]
    OpticalStandard: NotRequired[OpticalStandardType]
    MaximumSupportedWeightLbs: NotRequired[MaximumSupportedWeightLbsType]

class DeleteOutpostInputTypeDef(TypedDict):
    OutpostId: str

class DeleteSiteInputTypeDef(TypedDict):
    SiteId: str

class GetCapacityTaskInputTypeDef(TypedDict):
    CapacityTaskId: str
    OutpostIdentifier: str

class InstanceTypeCapacityTypeDef(TypedDict):
    InstanceType: str
    Count: int

class InstancesToExcludeOutputTypeDef(TypedDict):
    Instances: NotRequired[List[str]]
    AccountIds: NotRequired[List[str]]
    Services: NotRequired[List[AWSServiceNameType]]

class GetCatalogItemInputTypeDef(TypedDict):
    CatalogItemId: str

class GetConnectionRequestTypeDef(TypedDict):
    ConnectionId: str

class GetOrderInputTypeDef(TypedDict):
    OrderId: str

class GetOutpostInputTypeDef(TypedDict):
    OutpostId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetOutpostInstanceTypesInputTypeDef(TypedDict):
    OutpostId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class InstanceTypeItemTypeDef(TypedDict):
    InstanceType: NotRequired[str]
    VCPUs: NotRequired[int]

class GetOutpostSupportedInstanceTypesInputTypeDef(TypedDict):
    OutpostIdentifier: str
    OrderId: NotRequired[str]
    AssetId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetSiteAddressInputTypeDef(TypedDict):
    SiteId: str
    AddressType: AddressTypeType

class GetSiteInputTypeDef(TypedDict):
    SiteId: str

class InstancesToExcludeTypeDef(TypedDict):
    Instances: NotRequired[Sequence[str]]
    AccountIds: NotRequired[Sequence[str]]
    Services: NotRequired[Sequence[AWSServiceNameType]]

class LineItemAssetInformationTypeDef(TypedDict):
    AssetId: NotRequired[str]
    MacAddressList: NotRequired[List[str]]

class ShipmentInformationTypeDef(TypedDict):
    ShipmentTrackingNumber: NotRequired[str]
    ShipmentCarrier: NotRequired[ShipmentCarrierType]

class ListAssetInstancesInputTypeDef(TypedDict):
    OutpostIdentifier: str
    AssetIdFilter: NotRequired[Sequence[str]]
    InstanceTypeFilter: NotRequired[Sequence[str]]
    AccountIdFilter: NotRequired[Sequence[str]]
    AwsServiceFilter: NotRequired[Sequence[AWSServiceNameType]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListAssetsInputTypeDef(TypedDict):
    OutpostIdentifier: str
    HostIdFilter: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    StatusFilter: NotRequired[Sequence[AssetStateType]]

class ListBlockingInstancesForCapacityTaskInputTypeDef(TypedDict):
    OutpostIdentifier: str
    CapacityTaskId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListCapacityTasksInputTypeDef(TypedDict):
    OutpostIdentifierFilter: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    CapacityTaskStatusFilter: NotRequired[Sequence[CapacityTaskStatusType]]

class ListCatalogItemsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ItemClassFilter: NotRequired[Sequence[CatalogItemClassType]]
    SupportedStorageFilter: NotRequired[Sequence[SupportedStorageEnumType]]
    EC2FamilyFilter: NotRequired[Sequence[str]]

class ListOrdersInputTypeDef(TypedDict):
    OutpostIdentifierFilter: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class OrderSummaryTypeDef(TypedDict):
    OutpostId: NotRequired[str]
    OrderId: NotRequired[str]
    OrderType: NotRequired[OrderTypeType]
    Status: NotRequired[OrderStatusType]
    LineItemCountsByStatus: NotRequired[Dict[LineItemStatusType, int]]
    OrderSubmissionDate: NotRequired[datetime]
    OrderFulfilledDate: NotRequired[datetime]

class ListOutpostsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    LifeCycleStatusFilter: NotRequired[Sequence[str]]
    AvailabilityZoneFilter: NotRequired[Sequence[str]]
    AvailabilityZoneIdFilter: NotRequired[Sequence[str]]

class ListSitesInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    OperatingAddressCountryCodeFilter: NotRequired[Sequence[str]]
    OperatingAddressStateOrRegionFilter: NotRequired[Sequence[str]]
    OperatingAddressCityFilter: NotRequired[Sequence[str]]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class StartConnectionRequestTypeDef(TypedDict):
    AssetId: str
    ClientPublicKey: str
    NetworkInterfaceDeviceIndex: int
    DeviceSerialNumber: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateOutpostInputTypeDef(TypedDict):
    OutpostId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    SupportedHardwareType: NotRequired[SupportedHardwareTypeType]

class UpdateSiteInputTypeDef(TypedDict):
    SiteId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    Notes: NotRequired[str]

class UpdateSiteRackPhysicalPropertiesInputTypeDef(TypedDict):
    SiteId: str
    PowerDrawKva: NotRequired[PowerDrawKvaType]
    PowerPhase: NotRequired[PowerPhaseType]
    PowerConnector: NotRequired[PowerConnectorType]
    PowerFeedDrop: NotRequired[PowerFeedDropType]
    UplinkGbps: NotRequired[UplinkGbpsType]
    UplinkCount: NotRequired[UplinkCountType]
    FiberOpticCableType: NotRequired[FiberOpticCableTypeType]
    OpticalStandard: NotRequired[OpticalStandardType]
    MaximumSupportedWeightLbs: NotRequired[MaximumSupportedWeightLbsType]

class UpdateSiteAddressInputTypeDef(TypedDict):
    SiteId: str
    AddressType: AddressTypeType
    Address: AddressTypeDef

class ComputeAttributesTypeDef(TypedDict):
    HostId: NotRequired[str]
    State: NotRequired[ComputeAssetStateType]
    InstanceFamilies: NotRequired[List[str]]
    InstanceTypeCapacities: NotRequired[List[AssetInstanceTypeCapacityTypeDef]]
    MaxVcpus: NotRequired[int]

class CatalogItemTypeDef(TypedDict):
    CatalogItemId: NotRequired[str]
    ItemStatus: NotRequired[CatalogItemStatusType]
    EC2Capacities: NotRequired[List[EC2CapacityTypeDef]]
    PowerKva: NotRequired[float]
    WeightLbs: NotRequired[int]
    SupportedUplinkGbps: NotRequired[List[int]]
    SupportedStorage: NotRequired[List[SupportedStorageEnumType]]

class CreateOrderInputTypeDef(TypedDict):
    OutpostIdentifier: str
    LineItems: Sequence[LineItemRequestTypeDef]
    PaymentOption: PaymentOptionType
    PaymentTerm: NotRequired[PaymentTermType]

class GetConnectionResponseTypeDef(TypedDict):
    ConnectionId: str
    ConnectionDetails: ConnectionDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSiteAddressOutputTypeDef(TypedDict):
    SiteId: str
    AddressType: AddressTypeType
    Address: AddressTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetInstancesOutputTypeDef(TypedDict):
    AssetInstances: List[AssetInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListBlockingInstancesForCapacityTaskOutputTypeDef(TypedDict):
    BlockingInstances: List[BlockingInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCapacityTasksOutputTypeDef(TypedDict):
    CapacityTasks: List[CapacityTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartConnectionResponseTypeDef(TypedDict):
    ConnectionId: str
    UnderlayIpAddress: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSiteAddressOutputTypeDef(TypedDict):
    AddressType: AddressTypeType
    Address: AddressTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOutpostOutputTypeDef(TypedDict):
    Outpost: OutpostTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOutpostOutputTypeDef(TypedDict):
    Outpost: OutpostTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOutpostsOutputTypeDef(TypedDict):
    Outposts: List[OutpostTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateOutpostOutputTypeDef(TypedDict):
    Outpost: OutpostTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSiteInputTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    Notes: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    OperatingAddress: NotRequired[AddressTypeDef]
    ShippingAddress: NotRequired[AddressTypeDef]
    RackPhysicalProperties: NotRequired[RackPhysicalPropertiesTypeDef]

class SiteTypeDef(TypedDict):
    SiteId: NotRequired[str]
    AccountId: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]
    SiteArn: NotRequired[str]
    Notes: NotRequired[str]
    OperatingAddressCountryCode: NotRequired[str]
    OperatingAddressStateOrRegion: NotRequired[str]
    OperatingAddressCity: NotRequired[str]
    RackPhysicalProperties: NotRequired[RackPhysicalPropertiesTypeDef]

class GetCapacityTaskOutputTypeDef(TypedDict):
    CapacityTaskId: str
    OutpostId: str
    OrderId: str
    AssetId: str
    RequestedInstancePools: List[InstanceTypeCapacityTypeDef]
    InstancesToExclude: InstancesToExcludeOutputTypeDef
    DryRun: bool
    CapacityTaskStatus: CapacityTaskStatusType
    Failed: CapacityTaskFailureTypeDef
    CreationDate: datetime
    CompletionDate: datetime
    LastModifiedDate: datetime
    TaskActionOnBlockingInstances: TaskActionOnBlockingInstancesType
    ResponseMetadata: ResponseMetadataTypeDef

class StartCapacityTaskOutputTypeDef(TypedDict):
    CapacityTaskId: str
    OutpostId: str
    OrderId: str
    AssetId: str
    RequestedInstancePools: List[InstanceTypeCapacityTypeDef]
    InstancesToExclude: InstancesToExcludeOutputTypeDef
    DryRun: bool
    CapacityTaskStatus: CapacityTaskStatusType
    Failed: CapacityTaskFailureTypeDef
    CreationDate: datetime
    CompletionDate: datetime
    LastModifiedDate: datetime
    TaskActionOnBlockingInstances: TaskActionOnBlockingInstancesType
    ResponseMetadata: ResponseMetadataTypeDef

class GetOutpostInstanceTypesInputPaginateTypeDef(TypedDict):
    OutpostId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetOutpostSupportedInstanceTypesInputPaginateTypeDef(TypedDict):
    OutpostIdentifier: str
    OrderId: NotRequired[str]
    AssetId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAssetInstancesInputPaginateTypeDef(TypedDict):
    OutpostIdentifier: str
    AssetIdFilter: NotRequired[Sequence[str]]
    InstanceTypeFilter: NotRequired[Sequence[str]]
    AccountIdFilter: NotRequired[Sequence[str]]
    AwsServiceFilter: NotRequired[Sequence[AWSServiceNameType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAssetsInputPaginateTypeDef(TypedDict):
    OutpostIdentifier: str
    HostIdFilter: NotRequired[Sequence[str]]
    StatusFilter: NotRequired[Sequence[AssetStateType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBlockingInstancesForCapacityTaskInputPaginateTypeDef(TypedDict):
    OutpostIdentifier: str
    CapacityTaskId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCapacityTasksInputPaginateTypeDef(TypedDict):
    OutpostIdentifierFilter: NotRequired[str]
    CapacityTaskStatusFilter: NotRequired[Sequence[CapacityTaskStatusType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCatalogItemsInputPaginateTypeDef(TypedDict):
    ItemClassFilter: NotRequired[Sequence[CatalogItemClassType]]
    SupportedStorageFilter: NotRequired[Sequence[SupportedStorageEnumType]]
    EC2FamilyFilter: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOrdersInputPaginateTypeDef(TypedDict):
    OutpostIdentifierFilter: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOutpostsInputPaginateTypeDef(TypedDict):
    LifeCycleStatusFilter: NotRequired[Sequence[str]]
    AvailabilityZoneFilter: NotRequired[Sequence[str]]
    AvailabilityZoneIdFilter: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSitesInputPaginateTypeDef(TypedDict):
    OperatingAddressCountryCodeFilter: NotRequired[Sequence[str]]
    OperatingAddressStateOrRegionFilter: NotRequired[Sequence[str]]
    OperatingAddressCityFilter: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetOutpostInstanceTypesOutputTypeDef(TypedDict):
    InstanceTypes: List[InstanceTypeItemTypeDef]
    OutpostId: str
    OutpostArn: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetOutpostSupportedInstanceTypesOutputTypeDef(TypedDict):
    InstanceTypes: List[InstanceTypeItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

InstancesToExcludeUnionTypeDef = Union[InstancesToExcludeTypeDef, InstancesToExcludeOutputTypeDef]

class LineItemTypeDef(TypedDict):
    CatalogItemId: NotRequired[str]
    LineItemId: NotRequired[str]
    Quantity: NotRequired[int]
    Status: NotRequired[LineItemStatusType]
    ShipmentInformation: NotRequired[ShipmentInformationTypeDef]
    AssetInformationList: NotRequired[List[LineItemAssetInformationTypeDef]]
    PreviousLineItemId: NotRequired[str]
    PreviousOrderId: NotRequired[str]

class ListOrdersOutputTypeDef(TypedDict):
    Orders: List[OrderSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AssetInfoTypeDef(TypedDict):
    AssetId: NotRequired[str]
    RackId: NotRequired[str]
    AssetType: NotRequired[Literal["COMPUTE"]]
    ComputeAttributes: NotRequired[ComputeAttributesTypeDef]
    AssetLocation: NotRequired[AssetLocationTypeDef]

class GetCatalogItemOutputTypeDef(TypedDict):
    CatalogItem: CatalogItemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCatalogItemsOutputTypeDef(TypedDict):
    CatalogItems: List[CatalogItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateSiteOutputTypeDef(TypedDict):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSiteOutputTypeDef(TypedDict):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSitesOutputTypeDef(TypedDict):
    Sites: List[SiteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateSiteOutputTypeDef(TypedDict):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSiteRackPhysicalPropertiesOutputTypeDef(TypedDict):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartCapacityTaskInputTypeDef(TypedDict):
    OutpostIdentifier: str
    InstancePools: Sequence[InstanceTypeCapacityTypeDef]
    OrderId: NotRequired[str]
    AssetId: NotRequired[str]
    InstancesToExclude: NotRequired[InstancesToExcludeUnionTypeDef]
    DryRun: NotRequired[bool]
    TaskActionOnBlockingInstances: NotRequired[TaskActionOnBlockingInstancesType]

class OrderTypeDef(TypedDict):
    OutpostId: NotRequired[str]
    OrderId: NotRequired[str]
    Status: NotRequired[OrderStatusType]
    LineItems: NotRequired[List[LineItemTypeDef]]
    PaymentOption: NotRequired[PaymentOptionType]
    OrderSubmissionDate: NotRequired[datetime]
    OrderFulfilledDate: NotRequired[datetime]
    PaymentTerm: NotRequired[PaymentTermType]
    OrderType: NotRequired[OrderTypeType]

class ListAssetsOutputTypeDef(TypedDict):
    Assets: List[AssetInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateOrderOutputTypeDef(TypedDict):
    Order: OrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOrderOutputTypeDef(TypedDict):
    Order: OrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
