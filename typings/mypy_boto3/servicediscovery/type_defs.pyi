"""
Type annotations for servicediscovery service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_servicediscovery.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    CustomHealthStatusType,
    FilterConditionType,
    HealthCheckTypeType,
    HealthStatusFilterType,
    HealthStatusType,
    NamespaceFilterNameType,
    NamespaceTypeType,
    OperationFilterNameType,
    OperationStatusType,
    OperationTargetTypeType,
    OperationTypeType,
    RecordTypeType,
    RoutingPolicyType,
    ServiceTypeType,
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
    "CreateHttpNamespaceRequestTypeDef",
    "CreateHttpNamespaceResponseTypeDef",
    "CreatePrivateDnsNamespaceRequestTypeDef",
    "CreatePrivateDnsNamespaceResponseTypeDef",
    "CreatePublicDnsNamespaceRequestTypeDef",
    "CreatePublicDnsNamespaceResponseTypeDef",
    "CreateServiceRequestTypeDef",
    "CreateServiceResponseTypeDef",
    "DeleteNamespaceRequestTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeleteServiceAttributesRequestTypeDef",
    "DeleteServiceRequestTypeDef",
    "DeregisterInstanceRequestTypeDef",
    "DeregisterInstanceResponseTypeDef",
    "DiscoverInstancesRequestTypeDef",
    "DiscoverInstancesResponseTypeDef",
    "DiscoverInstancesRevisionRequestTypeDef",
    "DiscoverInstancesRevisionResponseTypeDef",
    "DnsConfigChangeTypeDef",
    "DnsConfigOutputTypeDef",
    "DnsConfigTypeDef",
    "DnsConfigUnionTypeDef",
    "DnsPropertiesTypeDef",
    "DnsRecordTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetInstanceRequestTypeDef",
    "GetInstanceResponseTypeDef",
    "GetInstancesHealthStatusRequestTypeDef",
    "GetInstancesHealthStatusResponseTypeDef",
    "GetNamespaceRequestTypeDef",
    "GetNamespaceResponseTypeDef",
    "GetOperationRequestTypeDef",
    "GetOperationResponseTypeDef",
    "GetServiceAttributesRequestTypeDef",
    "GetServiceAttributesResponseTypeDef",
    "GetServiceRequestTypeDef",
    "GetServiceResponseTypeDef",
    "HealthCheckConfigTypeDef",
    "HealthCheckCustomConfigTypeDef",
    "HttpInstanceSummaryTypeDef",
    "HttpNamespaceChangeTypeDef",
    "HttpPropertiesTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "ListInstancesRequestPaginateTypeDef",
    "ListInstancesRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListNamespacesRequestPaginateTypeDef",
    "ListNamespacesRequestTypeDef",
    "ListNamespacesResponseTypeDef",
    "ListOperationsRequestPaginateTypeDef",
    "ListOperationsRequestTypeDef",
    "ListOperationsResponseTypeDef",
    "ListServicesRequestPaginateTypeDef",
    "ListServicesRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NamespaceFilterTypeDef",
    "NamespacePropertiesTypeDef",
    "NamespaceSummaryTypeDef",
    "NamespaceTypeDef",
    "OperationFilterTypeDef",
    "OperationSummaryTypeDef",
    "OperationTypeDef",
    "PaginatorConfigTypeDef",
    "PrivateDnsNamespaceChangeTypeDef",
    "PrivateDnsNamespacePropertiesChangeTypeDef",
    "PrivateDnsNamespacePropertiesTypeDef",
    "PrivateDnsPropertiesMutableChangeTypeDef",
    "PrivateDnsPropertiesMutableTypeDef",
    "PublicDnsNamespaceChangeTypeDef",
    "PublicDnsNamespacePropertiesChangeTypeDef",
    "PublicDnsNamespacePropertiesTypeDef",
    "PublicDnsPropertiesMutableChangeTypeDef",
    "PublicDnsPropertiesMutableTypeDef",
    "RegisterInstanceRequestTypeDef",
    "RegisterInstanceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SOAChangeTypeDef",
    "SOATypeDef",
    "ServiceAttributesTypeDef",
    "ServiceChangeTypeDef",
    "ServiceFilterTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateHttpNamespaceRequestTypeDef",
    "UpdateHttpNamespaceResponseTypeDef",
    "UpdateInstanceCustomHealthStatusRequestTypeDef",
    "UpdatePrivateDnsNamespaceRequestTypeDef",
    "UpdatePrivateDnsNamespaceResponseTypeDef",
    "UpdatePublicDnsNamespaceRequestTypeDef",
    "UpdatePublicDnsNamespaceResponseTypeDef",
    "UpdateServiceAttributesRequestTypeDef",
    "UpdateServiceRequestTypeDef",
    "UpdateServiceResponseTypeDef",
)

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

HealthCheckConfigTypeDef = TypedDict(
    "HealthCheckConfigTypeDef",
    {
        "Type": HealthCheckTypeType,
        "ResourcePath": NotRequired[str],
        "FailureThreshold": NotRequired[int],
    },
)

class HealthCheckCustomConfigTypeDef(TypedDict):
    FailureThreshold: NotRequired[int]

class DeleteNamespaceRequestTypeDef(TypedDict):
    Id: str

class DeleteServiceAttributesRequestTypeDef(TypedDict):
    ServiceId: str
    Attributes: Sequence[str]

class DeleteServiceRequestTypeDef(TypedDict):
    Id: str

class DeregisterInstanceRequestTypeDef(TypedDict):
    ServiceId: str
    InstanceId: str

DiscoverInstancesRequestTypeDef = TypedDict(
    "DiscoverInstancesRequestTypeDef",
    {
        "NamespaceName": str,
        "ServiceName": str,
        "MaxResults": NotRequired[int],
        "QueryParameters": NotRequired[Mapping[str, str]],
        "OptionalParameters": NotRequired[Mapping[str, str]],
        "HealthStatus": NotRequired[HealthStatusFilterType],
    },
)
HttpInstanceSummaryTypeDef = TypedDict(
    "HttpInstanceSummaryTypeDef",
    {
        "InstanceId": NotRequired[str],
        "NamespaceName": NotRequired[str],
        "ServiceName": NotRequired[str],
        "HealthStatus": NotRequired[HealthStatusType],
        "Attributes": NotRequired[Dict[str, str]],
    },
)
DiscoverInstancesRevisionRequestTypeDef = TypedDict(
    "DiscoverInstancesRevisionRequestTypeDef",
    {
        "NamespaceName": str,
        "ServiceName": str,
    },
)
DnsRecordTypeDef = TypedDict(
    "DnsRecordTypeDef",
    {
        "Type": RecordTypeType,
        "TTL": int,
    },
)

class SOATypeDef(TypedDict):
    TTL: int

class GetInstanceRequestTypeDef(TypedDict):
    ServiceId: str
    InstanceId: str

class InstanceTypeDef(TypedDict):
    Id: str
    CreatorRequestId: NotRequired[str]
    Attributes: NotRequired[Dict[str, str]]

class GetInstancesHealthStatusRequestTypeDef(TypedDict):
    ServiceId: str
    Instances: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetNamespaceRequestTypeDef(TypedDict):
    Id: str

class GetOperationRequestTypeDef(TypedDict):
    OperationId: str

OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[OperationTypeType],
        "Status": NotRequired[OperationStatusType],
        "ErrorMessage": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "UpdateDate": NotRequired[datetime],
        "Targets": NotRequired[Dict[OperationTargetTypeType, str]],
    },
)

class GetServiceAttributesRequestTypeDef(TypedDict):
    ServiceId: str

class ServiceAttributesTypeDef(TypedDict):
    ServiceArn: NotRequired[str]
    Attributes: NotRequired[Dict[str, str]]

class GetServiceRequestTypeDef(TypedDict):
    Id: str

class HttpNamespaceChangeTypeDef(TypedDict):
    Description: str

class HttpPropertiesTypeDef(TypedDict):
    HttpName: NotRequired[str]

class InstanceSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Attributes: NotRequired[Dict[str, str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListInstancesRequestTypeDef(TypedDict):
    ServiceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class NamespaceFilterTypeDef(TypedDict):
    Name: NamespaceFilterNameType
    Values: Sequence[str]
    Condition: NotRequired[FilterConditionType]

class OperationFilterTypeDef(TypedDict):
    Name: OperationFilterNameType
    Values: Sequence[str]
    Condition: NotRequired[FilterConditionType]

class OperationSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Status: NotRequired[OperationStatusType]

class ServiceFilterTypeDef(TypedDict):
    Name: Literal["NAMESPACE_ID"]
    Values: Sequence[str]
    Condition: NotRequired[FilterConditionType]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class SOAChangeTypeDef(TypedDict):
    TTL: int

class RegisterInstanceRequestTypeDef(TypedDict):
    ServiceId: str
    InstanceId: str
    Attributes: Mapping[str, str]
    CreatorRequestId: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateInstanceCustomHealthStatusRequestTypeDef(TypedDict):
    ServiceId: str
    InstanceId: str
    Status: CustomHealthStatusType

class UpdateServiceAttributesRequestTypeDef(TypedDict):
    ServiceId: str
    Attributes: Mapping[str, str]

class CreateHttpNamespaceRequestTypeDef(TypedDict):
    Name: str
    CreatorRequestId: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateHttpNamespaceResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePrivateDnsNamespaceResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePublicDnsNamespaceResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNamespaceResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterInstanceResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DiscoverInstancesRevisionResponseTypeDef(TypedDict):
    InstancesRevision: int
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstancesHealthStatusResponseTypeDef(TypedDict):
    Status: Dict[str, HealthStatusType]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterInstanceResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHttpNamespaceResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePrivateDnsNamespaceResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePublicDnsNamespaceResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DiscoverInstancesResponseTypeDef(TypedDict):
    Instances: List[HttpInstanceSummaryTypeDef]
    InstancesRevision: int
    ResponseMetadata: ResponseMetadataTypeDef

class DnsConfigChangeTypeDef(TypedDict):
    DnsRecords: Sequence[DnsRecordTypeDef]

class DnsConfigOutputTypeDef(TypedDict):
    DnsRecords: List[DnsRecordTypeDef]
    NamespaceId: NotRequired[str]
    RoutingPolicy: NotRequired[RoutingPolicyType]

class DnsConfigTypeDef(TypedDict):
    DnsRecords: Sequence[DnsRecordTypeDef]
    NamespaceId: NotRequired[str]
    RoutingPolicy: NotRequired[RoutingPolicyType]

class DnsPropertiesTypeDef(TypedDict):
    HostedZoneId: NotRequired[str]
    SOA: NotRequired[SOATypeDef]

class PrivateDnsPropertiesMutableTypeDef(TypedDict):
    SOA: SOATypeDef

class PublicDnsPropertiesMutableTypeDef(TypedDict):
    SOA: SOATypeDef

class GetInstanceResponseTypeDef(TypedDict):
    Instance: InstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOperationResponseTypeDef(TypedDict):
    Operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceAttributesResponseTypeDef(TypedDict):
    ServiceAttributes: ServiceAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHttpNamespaceRequestTypeDef(TypedDict):
    Id: str
    Namespace: HttpNamespaceChangeTypeDef
    UpdaterRequestId: NotRequired[str]

class ListInstancesResponseTypeDef(TypedDict):
    Instances: List[InstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListInstancesRequestPaginateTypeDef(TypedDict):
    ServiceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNamespacesRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[NamespaceFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNamespacesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[NamespaceFilterTypeDef]]

class ListOperationsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[OperationFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOperationsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[OperationFilterTypeDef]]

class ListOperationsResponseTypeDef(TypedDict):
    Operations: List[OperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListServicesRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[ServiceFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServicesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[ServiceFilterTypeDef]]

class PrivateDnsPropertiesMutableChangeTypeDef(TypedDict):
    SOA: SOAChangeTypeDef

class PublicDnsPropertiesMutableChangeTypeDef(TypedDict):
    SOA: SOAChangeTypeDef

class ServiceChangeTypeDef(TypedDict):
    Description: NotRequired[str]
    DnsConfig: NotRequired[DnsConfigChangeTypeDef]
    HealthCheckConfig: NotRequired[HealthCheckConfigTypeDef]

ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[ServiceTypeType],
        "Description": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "DnsConfig": NotRequired[DnsConfigOutputTypeDef],
        "HealthCheckConfig": NotRequired[HealthCheckConfigTypeDef],
        "HealthCheckCustomConfig": NotRequired[HealthCheckCustomConfigTypeDef],
        "CreateDate": NotRequired[datetime],
    },
)
ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "NamespaceId": NotRequired[str],
        "Description": NotRequired[str],
        "InstanceCount": NotRequired[int],
        "DnsConfig": NotRequired[DnsConfigOutputTypeDef],
        "Type": NotRequired[ServiceTypeType],
        "HealthCheckConfig": NotRequired[HealthCheckConfigTypeDef],
        "HealthCheckCustomConfig": NotRequired[HealthCheckCustomConfigTypeDef],
        "CreateDate": NotRequired[datetime],
        "CreatorRequestId": NotRequired[str],
    },
)
DnsConfigUnionTypeDef = Union[DnsConfigTypeDef, DnsConfigOutputTypeDef]

class NamespacePropertiesTypeDef(TypedDict):
    DnsProperties: NotRequired[DnsPropertiesTypeDef]
    HttpProperties: NotRequired[HttpPropertiesTypeDef]

class PrivateDnsNamespacePropertiesTypeDef(TypedDict):
    DnsProperties: PrivateDnsPropertiesMutableTypeDef

class PublicDnsNamespacePropertiesTypeDef(TypedDict):
    DnsProperties: PublicDnsPropertiesMutableTypeDef

class PrivateDnsNamespacePropertiesChangeTypeDef(TypedDict):
    DnsProperties: PrivateDnsPropertiesMutableChangeTypeDef

class PublicDnsNamespacePropertiesChangeTypeDef(TypedDict):
    DnsProperties: PublicDnsPropertiesMutableChangeTypeDef

class UpdateServiceRequestTypeDef(TypedDict):
    Id: str
    Service: ServiceChangeTypeDef

class ListServicesResponseTypeDef(TypedDict):
    Services: List[ServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateServiceResponseTypeDef(TypedDict):
    Service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceResponseTypeDef(TypedDict):
    Service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CreateServiceRequestTypeDef = TypedDict(
    "CreateServiceRequestTypeDef",
    {
        "Name": str,
        "NamespaceId": NotRequired[str],
        "CreatorRequestId": NotRequired[str],
        "Description": NotRequired[str],
        "DnsConfig": NotRequired[DnsConfigUnionTypeDef],
        "HealthCheckConfig": NotRequired[HealthCheckConfigTypeDef],
        "HealthCheckCustomConfig": NotRequired[HealthCheckCustomConfigTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Type": NotRequired[Literal["HTTP"]],
    },
)
NamespaceSummaryTypeDef = TypedDict(
    "NamespaceSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[NamespaceTypeType],
        "Description": NotRequired[str],
        "ServiceCount": NotRequired[int],
        "Properties": NotRequired[NamespacePropertiesTypeDef],
        "CreateDate": NotRequired[datetime],
    },
)
NamespaceTypeDef = TypedDict(
    "NamespaceTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[NamespaceTypeType],
        "Description": NotRequired[str],
        "ServiceCount": NotRequired[int],
        "Properties": NotRequired[NamespacePropertiesTypeDef],
        "CreateDate": NotRequired[datetime],
        "CreatorRequestId": NotRequired[str],
    },
)

class CreatePrivateDnsNamespaceRequestTypeDef(TypedDict):
    Name: str
    Vpc: str
    CreatorRequestId: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    Properties: NotRequired[PrivateDnsNamespacePropertiesTypeDef]

class CreatePublicDnsNamespaceRequestTypeDef(TypedDict):
    Name: str
    CreatorRequestId: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    Properties: NotRequired[PublicDnsNamespacePropertiesTypeDef]

class PrivateDnsNamespaceChangeTypeDef(TypedDict):
    Description: NotRequired[str]
    Properties: NotRequired[PrivateDnsNamespacePropertiesChangeTypeDef]

class PublicDnsNamespaceChangeTypeDef(TypedDict):
    Description: NotRequired[str]
    Properties: NotRequired[PublicDnsNamespacePropertiesChangeTypeDef]

class ListNamespacesResponseTypeDef(TypedDict):
    Namespaces: List[NamespaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetNamespaceResponseTypeDef(TypedDict):
    Namespace: NamespaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePrivateDnsNamespaceRequestTypeDef(TypedDict):
    Id: str
    Namespace: PrivateDnsNamespaceChangeTypeDef
    UpdaterRequestId: NotRequired[str]

class UpdatePublicDnsNamespaceRequestTypeDef(TypedDict):
    Id: str
    Namespace: PublicDnsNamespaceChangeTypeDef
    UpdaterRequestId: NotRequired[str]
