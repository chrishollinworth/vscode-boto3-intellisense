"""
Type annotations for privatenetworks service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_privatenetworks.type_defs import AcknowledgeOrderReceiptRequestTypeDef

    data: AcknowledgeOrderReceiptRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AcknowledgmentStatusType,
    CommitmentLengthType,
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
    "AcknowledgeOrderReceiptRequestTypeDef",
    "AcknowledgeOrderReceiptResponseTypeDef",
    "ActivateDeviceIdentifierRequestTypeDef",
    "ActivateDeviceIdentifierResponseTypeDef",
    "ActivateNetworkSiteRequestTypeDef",
    "ActivateNetworkSiteResponseTypeDef",
    "AddressTypeDef",
    "CommitmentConfigurationTypeDef",
    "CommitmentInformationTypeDef",
    "ConfigureAccessPointRequestTypeDef",
    "ConfigureAccessPointResponseTypeDef",
    "CreateNetworkRequestTypeDef",
    "CreateNetworkResponseTypeDef",
    "CreateNetworkSiteRequestTypeDef",
    "CreateNetworkSiteResponseTypeDef",
    "DeactivateDeviceIdentifierRequestTypeDef",
    "DeactivateDeviceIdentifierResponseTypeDef",
    "DeleteNetworkRequestTypeDef",
    "DeleteNetworkResponseTypeDef",
    "DeleteNetworkSiteRequestTypeDef",
    "DeleteNetworkSiteResponseTypeDef",
    "DeviceIdentifierTypeDef",
    "GetDeviceIdentifierRequestTypeDef",
    "GetDeviceIdentifierResponseTypeDef",
    "GetNetworkRequestTypeDef",
    "GetNetworkResourceRequestTypeDef",
    "GetNetworkResourceResponseTypeDef",
    "GetNetworkResponseTypeDef",
    "GetNetworkSiteRequestTypeDef",
    "GetNetworkSiteResponseTypeDef",
    "GetOrderRequestTypeDef",
    "GetOrderResponseTypeDef",
    "ListDeviceIdentifiersRequestPaginateTypeDef",
    "ListDeviceIdentifiersRequestTypeDef",
    "ListDeviceIdentifiersResponseTypeDef",
    "ListNetworkResourcesRequestPaginateTypeDef",
    "ListNetworkResourcesRequestTypeDef",
    "ListNetworkResourcesResponseTypeDef",
    "ListNetworkSitesRequestPaginateTypeDef",
    "ListNetworkSitesRequestTypeDef",
    "ListNetworkSitesResponseTypeDef",
    "ListNetworksRequestPaginateTypeDef",
    "ListNetworksRequestTypeDef",
    "ListNetworksResponseTypeDef",
    "ListOrdersRequestPaginateTypeDef",
    "ListOrdersRequestTypeDef",
    "ListOrdersResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NameValuePairTypeDef",
    "NetworkResourceDefinitionOutputTypeDef",
    "NetworkResourceDefinitionTypeDef",
    "NetworkResourceTypeDef",
    "NetworkSiteTypeDef",
    "NetworkTypeDef",
    "OrderTypeDef",
    "OrderedResourceDefinitionTypeDef",
    "PaginatorConfigTypeDef",
    "PingResponseTypeDef",
    "PositionTypeDef",
    "ResponseMetadataTypeDef",
    "ReturnInformationTypeDef",
    "SitePlanOutputTypeDef",
    "SitePlanTypeDef",
    "SitePlanUnionTypeDef",
    "StartNetworkResourceUpdateRequestTypeDef",
    "StartNetworkResourceUpdateResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TrackingInformationTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateNetworkSitePlanRequestTypeDef",
    "UpdateNetworkSiteRequestTypeDef",
    "UpdateNetworkSiteResponseTypeDef",
)

class AcknowledgeOrderReceiptRequestTypeDef(TypedDict):
    orderArn: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ActivateDeviceIdentifierRequestTypeDef(TypedDict):
    deviceIdentifierArn: str
    clientToken: NotRequired[str]

class DeviceIdentifierTypeDef(TypedDict):
    createdAt: NotRequired[datetime]
    deviceIdentifierArn: NotRequired[str]
    iccid: NotRequired[str]
    imsi: NotRequired[str]
    networkArn: NotRequired[str]
    orderArn: NotRequired[str]
    status: NotRequired[DeviceIdentifierStatusType]
    trafficGroupArn: NotRequired[str]
    vendor: NotRequired[str]

class AddressTypeDef(TypedDict):
    city: str
    country: str
    name: str
    postalCode: str
    stateOrProvince: str
    street1: str
    company: NotRequired[str]
    emailAddress: NotRequired[str]
    phoneNumber: NotRequired[str]
    street2: NotRequired[str]
    street3: NotRequired[str]

class CommitmentConfigurationTypeDef(TypedDict):
    automaticRenewal: bool
    commitmentLength: CommitmentLengthType

class PositionTypeDef(TypedDict):
    elevation: NotRequired[float]
    elevationReference: NotRequired[ElevationReferenceType]
    elevationUnit: NotRequired[Literal["FEET"]]
    latitude: NotRequired[float]
    longitude: NotRequired[float]

class CreateNetworkRequestTypeDef(TypedDict):
    networkName: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class NetworkTypeDef(TypedDict):
    networkArn: str
    networkName: str
    status: NetworkStatusType
    createdAt: NotRequired[datetime]
    description: NotRequired[str]
    statusReason: NotRequired[str]

class DeactivateDeviceIdentifierRequestTypeDef(TypedDict):
    deviceIdentifierArn: str
    clientToken: NotRequired[str]

class DeleteNetworkRequestTypeDef(TypedDict):
    networkArn: str
    clientToken: NotRequired[str]

class DeleteNetworkSiteRequestTypeDef(TypedDict):
    networkSiteArn: str
    clientToken: NotRequired[str]

class GetDeviceIdentifierRequestTypeDef(TypedDict):
    deviceIdentifierArn: str

class GetNetworkRequestTypeDef(TypedDict):
    networkArn: str

class GetNetworkResourceRequestTypeDef(TypedDict):
    networkResourceArn: str

class GetNetworkSiteRequestTypeDef(TypedDict):
    networkSiteArn: str

class GetOrderRequestTypeDef(TypedDict):
    orderArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListDeviceIdentifiersRequestTypeDef(TypedDict):
    networkArn: str
    filters: NotRequired[Mapping[DeviceIdentifierFilterKeysType, Sequence[str]]]
    maxResults: NotRequired[int]
    startToken: NotRequired[str]

class ListNetworkResourcesRequestTypeDef(TypedDict):
    networkArn: str
    filters: NotRequired[Mapping[NetworkResourceFilterKeysType, Sequence[str]]]
    maxResults: NotRequired[int]
    startToken: NotRequired[str]

class ListNetworkSitesRequestTypeDef(TypedDict):
    networkArn: str
    filters: NotRequired[Mapping[Literal["STATUS"], Sequence[str]]]
    maxResults: NotRequired[int]
    startToken: NotRequired[str]

class ListNetworksRequestTypeDef(TypedDict):
    filters: NotRequired[Mapping[Literal["STATUS"], Sequence[str]]]
    maxResults: NotRequired[int]
    startToken: NotRequired[str]

class ListOrdersRequestTypeDef(TypedDict):
    networkArn: str
    filters: NotRequired[Mapping[OrderFilterKeysType, Sequence[str]]]
    maxResults: NotRequired[int]
    startToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class NameValuePairTypeDef(TypedDict):
    name: str
    value: NotRequired[str]

class TrackingInformationTypeDef(TypedDict):
    trackingNumber: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateNetworkSiteRequestTypeDef(TypedDict):
    networkSiteArn: str
    clientToken: NotRequired[str]
    description: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PingResponseTypeDef(TypedDict):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class ActivateDeviceIdentifierResponseTypeDef(TypedDict):
    deviceIdentifier: DeviceIdentifierTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeactivateDeviceIdentifierResponseTypeDef(TypedDict):
    deviceIdentifier: DeviceIdentifierTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeviceIdentifierResponseTypeDef(TypedDict):
    deviceIdentifier: DeviceIdentifierTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeviceIdentifiersResponseTypeDef(TypedDict):
    deviceIdentifiers: List[DeviceIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ReturnInformationTypeDef(TypedDict):
    replacementOrderArn: NotRequired[str]
    returnReason: NotRequired[str]
    shippingAddress: NotRequired[AddressTypeDef]
    shippingLabel: NotRequired[str]

class ActivateNetworkSiteRequestTypeDef(TypedDict):
    networkSiteArn: str
    shippingAddress: AddressTypeDef
    clientToken: NotRequired[str]
    commitmentConfiguration: NotRequired[CommitmentConfigurationTypeDef]

class CommitmentInformationTypeDef(TypedDict):
    commitmentConfiguration: CommitmentConfigurationTypeDef
    expiresOn: NotRequired[datetime]
    startAt: NotRequired[datetime]

OrderedResourceDefinitionTypeDef = TypedDict(
    "OrderedResourceDefinitionTypeDef",
    {
        "count": int,
        "type": NetworkResourceDefinitionTypeType,
        "commitmentConfiguration": NotRequired[CommitmentConfigurationTypeDef],
    },
)

class StartNetworkResourceUpdateRequestTypeDef(TypedDict):
    networkResourceArn: str
    updateType: UpdateTypeType
    commitmentConfiguration: NotRequired[CommitmentConfigurationTypeDef]
    returnReason: NotRequired[str]
    shippingAddress: NotRequired[AddressTypeDef]

class ConfigureAccessPointRequestTypeDef(TypedDict):
    accessPointArn: str
    cpiSecretKey: NotRequired[str]
    cpiUserId: NotRequired[str]
    cpiUserPassword: NotRequired[str]
    cpiUsername: NotRequired[str]
    position: NotRequired[PositionTypeDef]

class CreateNetworkResponseTypeDef(TypedDict):
    network: NetworkTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkResponseTypeDef(TypedDict):
    network: NetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkResponseTypeDef(TypedDict):
    network: NetworkTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNetworksResponseTypeDef(TypedDict):
    networks: List[NetworkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListDeviceIdentifiersRequestPaginateTypeDef(TypedDict):
    networkArn: str
    filters: NotRequired[Mapping[DeviceIdentifierFilterKeysType, Sequence[str]]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNetworkResourcesRequestPaginateTypeDef(TypedDict):
    networkArn: str
    filters: NotRequired[Mapping[NetworkResourceFilterKeysType, Sequence[str]]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNetworkSitesRequestPaginateTypeDef(TypedDict):
    networkArn: str
    filters: NotRequired[Mapping[Literal["STATUS"], Sequence[str]]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNetworksRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Mapping[Literal["STATUS"], Sequence[str]]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOrdersRequestPaginateTypeDef(TypedDict):
    networkArn: str
    filters: NotRequired[Mapping[OrderFilterKeysType, Sequence[str]]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

NetworkResourceDefinitionOutputTypeDef = TypedDict(
    "NetworkResourceDefinitionOutputTypeDef",
    {
        "count": int,
        "type": NetworkResourceDefinitionTypeType,
        "options": NotRequired[List[NameValuePairTypeDef]],
    },
)
NetworkResourceDefinitionTypeDef = TypedDict(
    "NetworkResourceDefinitionTypeDef",
    {
        "count": int,
        "type": NetworkResourceDefinitionTypeType,
        "options": NotRequired[Sequence[NameValuePairTypeDef]],
    },
)
NetworkResourceTypeDef = TypedDict(
    "NetworkResourceTypeDef",
    {
        "attributes": NotRequired[List[NameValuePairTypeDef]],
        "commitmentInformation": NotRequired[CommitmentInformationTypeDef],
        "createdAt": NotRequired[datetime],
        "description": NotRequired[str],
        "health": NotRequired[HealthStatusType],
        "model": NotRequired[str],
        "networkArn": NotRequired[str],
        "networkResourceArn": NotRequired[str],
        "networkSiteArn": NotRequired[str],
        "orderArn": NotRequired[str],
        "position": NotRequired[PositionTypeDef],
        "returnInformation": NotRequired[ReturnInformationTypeDef],
        "serialNumber": NotRequired[str],
        "status": NotRequired[NetworkResourceStatusType],
        "statusReason": NotRequired[str],
        "type": NotRequired[Literal["RADIO_UNIT"]],
        "vendor": NotRequired[str],
    },
)

class OrderTypeDef(TypedDict):
    acknowledgmentStatus: NotRequired[AcknowledgmentStatusType]
    createdAt: NotRequired[datetime]
    networkArn: NotRequired[str]
    networkSiteArn: NotRequired[str]
    orderArn: NotRequired[str]
    orderedResources: NotRequired[List[OrderedResourceDefinitionTypeDef]]
    shippingAddress: NotRequired[AddressTypeDef]
    trackingInformation: NotRequired[List[TrackingInformationTypeDef]]

class SitePlanOutputTypeDef(TypedDict):
    options: NotRequired[List[NameValuePairTypeDef]]
    resourceDefinitions: NotRequired[List[NetworkResourceDefinitionOutputTypeDef]]

class SitePlanTypeDef(TypedDict):
    options: NotRequired[Sequence[NameValuePairTypeDef]]
    resourceDefinitions: NotRequired[Sequence[NetworkResourceDefinitionTypeDef]]

class ConfigureAccessPointResponseTypeDef(TypedDict):
    accessPoint: NetworkResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkResourceResponseTypeDef(TypedDict):
    networkResource: NetworkResourceTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNetworkResourcesResponseTypeDef(TypedDict):
    networkResources: List[NetworkResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartNetworkResourceUpdateResponseTypeDef(TypedDict):
    networkResource: NetworkResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AcknowledgeOrderReceiptResponseTypeDef(TypedDict):
    order: OrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOrderResponseTypeDef(TypedDict):
    order: OrderTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListOrdersResponseTypeDef(TypedDict):
    orders: List[OrderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class NetworkSiteTypeDef(TypedDict):
    networkArn: str
    networkSiteArn: str
    networkSiteName: str
    status: NetworkSiteStatusType
    availabilityZone: NotRequired[str]
    availabilityZoneId: NotRequired[str]
    createdAt: NotRequired[datetime]
    currentPlan: NotRequired[SitePlanOutputTypeDef]
    description: NotRequired[str]
    pendingPlan: NotRequired[SitePlanOutputTypeDef]
    statusReason: NotRequired[str]

SitePlanUnionTypeDef = Union[SitePlanTypeDef, SitePlanOutputTypeDef]

class ActivateNetworkSiteResponseTypeDef(TypedDict):
    networkSite: NetworkSiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkSiteResponseTypeDef(TypedDict):
    networkSite: NetworkSiteTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkSiteResponseTypeDef(TypedDict):
    networkSite: NetworkSiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkSiteResponseTypeDef(TypedDict):
    networkSite: NetworkSiteTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListNetworkSitesResponseTypeDef(TypedDict):
    networkSites: List[NetworkSiteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateNetworkSiteResponseTypeDef(TypedDict):
    networkSite: NetworkSiteTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkSiteRequestTypeDef(TypedDict):
    networkArn: str
    networkSiteName: str
    availabilityZone: NotRequired[str]
    availabilityZoneId: NotRequired[str]
    clientToken: NotRequired[str]
    description: NotRequired[str]
    pendingPlan: NotRequired[SitePlanUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]

class UpdateNetworkSitePlanRequestTypeDef(TypedDict):
    networkSiteArn: str
    pendingPlan: SitePlanUnionTypeDef
    clientToken: NotRequired[str]
