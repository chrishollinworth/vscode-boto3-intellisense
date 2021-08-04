"""
Type annotations for servicediscovery service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/type_defs.html)

Usage::

    ```python
    from mypy_boto3_servicediscovery.type_defs import CreateHttpNamespaceRequestRequestTypeDef

    data: CreateHttpNamespaceRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    CustomHealthStatusType,
    FilterConditionType,
    HealthCheckTypeType,
    HealthStatusFilterType,
    HealthStatusType,
    NamespaceTypeType,
    OperationFilterNameType,
    OperationStatusType,
    OperationTargetTypeType,
    OperationTypeType,
    RecordTypeType,
    RoutingPolicyType,
    ServiceTypeType,
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
    "CreateHttpNamespaceRequestRequestTypeDef",
    "CreateHttpNamespaceResponseTypeDef",
    "CreatePrivateDnsNamespaceRequestRequestTypeDef",
    "CreatePrivateDnsNamespaceResponseTypeDef",
    "CreatePublicDnsNamespaceRequestRequestTypeDef",
    "CreatePublicDnsNamespaceResponseTypeDef",
    "CreateServiceRequestRequestTypeDef",
    "CreateServiceResponseTypeDef",
    "DeleteNamespaceRequestRequestTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeleteServiceRequestRequestTypeDef",
    "DeregisterInstanceRequestRequestTypeDef",
    "DeregisterInstanceResponseTypeDef",
    "DiscoverInstancesRequestRequestTypeDef",
    "DiscoverInstancesResponseTypeDef",
    "DnsConfigChangeTypeDef",
    "DnsConfigTypeDef",
    "DnsPropertiesTypeDef",
    "DnsRecordTypeDef",
    "GetInstanceRequestRequestTypeDef",
    "GetInstanceResponseTypeDef",
    "GetInstancesHealthStatusRequestRequestTypeDef",
    "GetInstancesHealthStatusResponseTypeDef",
    "GetNamespaceRequestRequestTypeDef",
    "GetNamespaceResponseTypeDef",
    "GetOperationRequestRequestTypeDef",
    "GetOperationResponseTypeDef",
    "GetServiceRequestRequestTypeDef",
    "GetServiceResponseTypeDef",
    "HealthCheckConfigTypeDef",
    "HealthCheckCustomConfigTypeDef",
    "HttpInstanceSummaryTypeDef",
    "HttpNamespaceChangeTypeDef",
    "HttpPropertiesTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "ListInstancesRequestRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListNamespacesRequestRequestTypeDef",
    "ListNamespacesResponseTypeDef",
    "ListOperationsRequestRequestTypeDef",
    "ListOperationsResponseTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
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
    "RegisterInstanceRequestRequestTypeDef",
    "RegisterInstanceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SOAChangeTypeDef",
    "SOATypeDef",
    "ServiceChangeTypeDef",
    "ServiceFilterTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateHttpNamespaceRequestRequestTypeDef",
    "UpdateHttpNamespaceResponseTypeDef",
    "UpdateInstanceCustomHealthStatusRequestRequestTypeDef",
    "UpdatePrivateDnsNamespaceRequestRequestTypeDef",
    "UpdatePrivateDnsNamespaceResponseTypeDef",
    "UpdatePublicDnsNamespaceRequestRequestTypeDef",
    "UpdatePublicDnsNamespaceResponseTypeDef",
    "UpdateServiceRequestRequestTypeDef",
    "UpdateServiceResponseTypeDef",
)

_RequiredCreateHttpNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHttpNamespaceRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateHttpNamespaceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHttpNamespaceRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateHttpNamespaceRequestRequestTypeDef(
    _RequiredCreateHttpNamespaceRequestRequestTypeDef,
    _OptionalCreateHttpNamespaceRequestRequestTypeDef,
):
    pass

CreateHttpNamespaceResponseTypeDef = TypedDict(
    "CreateHttpNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePrivateDnsNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePrivateDnsNamespaceRequestRequestTypeDef",
    {
        "Name": str,
        "Vpc": str,
    },
)
_OptionalCreatePrivateDnsNamespaceRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePrivateDnsNamespaceRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
        "Properties": "PrivateDnsNamespacePropertiesTypeDef",
    },
    total=False,
)

class CreatePrivateDnsNamespaceRequestRequestTypeDef(
    _RequiredCreatePrivateDnsNamespaceRequestRequestTypeDef,
    _OptionalCreatePrivateDnsNamespaceRequestRequestTypeDef,
):
    pass

CreatePrivateDnsNamespaceResponseTypeDef = TypedDict(
    "CreatePrivateDnsNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePublicDnsNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePublicDnsNamespaceRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreatePublicDnsNamespaceRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePublicDnsNamespaceRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
        "Properties": "PublicDnsNamespacePropertiesTypeDef",
    },
    total=False,
)

class CreatePublicDnsNamespaceRequestRequestTypeDef(
    _RequiredCreatePublicDnsNamespaceRequestRequestTypeDef,
    _OptionalCreatePublicDnsNamespaceRequestRequestTypeDef,
):
    pass

CreatePublicDnsNamespaceResponseTypeDef = TypedDict(
    "CreatePublicDnsNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateServiceRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateServiceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateServiceRequestRequestTypeDef",
    {
        "NamespaceId": str,
        "CreatorRequestId": str,
        "Description": str,
        "DnsConfig": "DnsConfigTypeDef",
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
        "HealthCheckCustomConfig": "HealthCheckCustomConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "Type": Literal["HTTP"],
    },
    total=False,
)

class CreateServiceRequestRequestTypeDef(
    _RequiredCreateServiceRequestRequestTypeDef, _OptionalCreateServiceRequestRequestTypeDef
):
    pass

CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNamespaceRequestRequestTypeDef = TypedDict(
    "DeleteNamespaceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceRequestRequestTypeDef = TypedDict(
    "DeleteServiceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeregisterInstanceRequestRequestTypeDef = TypedDict(
    "DeregisterInstanceRequestRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
    },
)

DeregisterInstanceResponseTypeDef = TypedDict(
    "DeregisterInstanceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDiscoverInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredDiscoverInstancesRequestRequestTypeDef",
    {
        "NamespaceName": str,
        "ServiceName": str,
    },
)
_OptionalDiscoverInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalDiscoverInstancesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "QueryParameters": Dict[str, str],
        "OptionalParameters": Dict[str, str],
        "HealthStatus": HealthStatusFilterType,
    },
    total=False,
)

class DiscoverInstancesRequestRequestTypeDef(
    _RequiredDiscoverInstancesRequestRequestTypeDef, _OptionalDiscoverInstancesRequestRequestTypeDef
):
    pass

DiscoverInstancesResponseTypeDef = TypedDict(
    "DiscoverInstancesResponseTypeDef",
    {
        "Instances": List["HttpInstanceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DnsConfigChangeTypeDef = TypedDict(
    "DnsConfigChangeTypeDef",
    {
        "DnsRecords": List["DnsRecordTypeDef"],
    },
)

_RequiredDnsConfigTypeDef = TypedDict(
    "_RequiredDnsConfigTypeDef",
    {
        "DnsRecords": List["DnsRecordTypeDef"],
    },
)
_OptionalDnsConfigTypeDef = TypedDict(
    "_OptionalDnsConfigTypeDef",
    {
        "NamespaceId": str,
        "RoutingPolicy": RoutingPolicyType,
    },
    total=False,
)

class DnsConfigTypeDef(_RequiredDnsConfigTypeDef, _OptionalDnsConfigTypeDef):
    pass

DnsPropertiesTypeDef = TypedDict(
    "DnsPropertiesTypeDef",
    {
        "HostedZoneId": str,
        "SOA": "SOATypeDef",
    },
    total=False,
)

DnsRecordTypeDef = TypedDict(
    "DnsRecordTypeDef",
    {
        "Type": RecordTypeType,
        "TTL": int,
    },
)

GetInstanceRequestRequestTypeDef = TypedDict(
    "GetInstanceRequestRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
    },
)

GetInstanceResponseTypeDef = TypedDict(
    "GetInstanceResponseTypeDef",
    {
        "Instance": "InstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInstancesHealthStatusRequestRequestTypeDef = TypedDict(
    "_RequiredGetInstancesHealthStatusRequestRequestTypeDef",
    {
        "ServiceId": str,
    },
)
_OptionalGetInstancesHealthStatusRequestRequestTypeDef = TypedDict(
    "_OptionalGetInstancesHealthStatusRequestRequestTypeDef",
    {
        "Instances": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetInstancesHealthStatusRequestRequestTypeDef(
    _RequiredGetInstancesHealthStatusRequestRequestTypeDef,
    _OptionalGetInstancesHealthStatusRequestRequestTypeDef,
):
    pass

GetInstancesHealthStatusResponseTypeDef = TypedDict(
    "GetInstancesHealthStatusResponseTypeDef",
    {
        "Status": Dict[str, HealthStatusType],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNamespaceRequestRequestTypeDef = TypedDict(
    "GetNamespaceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetNamespaceResponseTypeDef = TypedDict(
    "GetNamespaceResponseTypeDef",
    {
        "Namespace": "NamespaceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOperationRequestRequestTypeDef = TypedDict(
    "GetOperationRequestRequestTypeDef",
    {
        "OperationId": str,
    },
)

GetOperationResponseTypeDef = TypedDict(
    "GetOperationResponseTypeDef",
    {
        "Operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceRequestRequestTypeDef = TypedDict(
    "GetServiceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetServiceResponseTypeDef = TypedDict(
    "GetServiceResponseTypeDef",
    {
        "Service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredHealthCheckConfigTypeDef = TypedDict(
    "_RequiredHealthCheckConfigTypeDef",
    {
        "Type": HealthCheckTypeType,
    },
)
_OptionalHealthCheckConfigTypeDef = TypedDict(
    "_OptionalHealthCheckConfigTypeDef",
    {
        "ResourcePath": str,
        "FailureThreshold": int,
    },
    total=False,
)

class HealthCheckConfigTypeDef(
    _RequiredHealthCheckConfigTypeDef, _OptionalHealthCheckConfigTypeDef
):
    pass

HealthCheckCustomConfigTypeDef = TypedDict(
    "HealthCheckCustomConfigTypeDef",
    {
        "FailureThreshold": int,
    },
    total=False,
)

HttpInstanceSummaryTypeDef = TypedDict(
    "HttpInstanceSummaryTypeDef",
    {
        "InstanceId": str,
        "NamespaceName": str,
        "ServiceName": str,
        "HealthStatus": HealthStatusType,
        "Attributes": Dict[str, str],
    },
    total=False,
)

HttpNamespaceChangeTypeDef = TypedDict(
    "HttpNamespaceChangeTypeDef",
    {
        "Description": str,
    },
)

HttpPropertiesTypeDef = TypedDict(
    "HttpPropertiesTypeDef",
    {
        "HttpName": str,
    },
    total=False,
)

InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "Id": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

_RequiredInstanceTypeDef = TypedDict(
    "_RequiredInstanceTypeDef",
    {
        "Id": str,
    },
)
_OptionalInstanceTypeDef = TypedDict(
    "_OptionalInstanceTypeDef",
    {
        "CreatorRequestId": str,
        "Attributes": Dict[str, str],
    },
    total=False,
)

class InstanceTypeDef(_RequiredInstanceTypeDef, _OptionalInstanceTypeDef):
    pass

_RequiredListInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredListInstancesRequestRequestTypeDef",
    {
        "ServiceId": str,
    },
)
_OptionalListInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalListInstancesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListInstancesRequestRequestTypeDef(
    _RequiredListInstancesRequestRequestTypeDef, _OptionalListInstancesRequestRequestTypeDef
):
    pass

ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {
        "Instances": List["InstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNamespacesRequestRequestTypeDef = TypedDict(
    "ListNamespacesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["NamespaceFilterTypeDef"],
    },
    total=False,
)

ListNamespacesResponseTypeDef = TypedDict(
    "ListNamespacesResponseTypeDef",
    {
        "Namespaces": List["NamespaceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOperationsRequestRequestTypeDef = TypedDict(
    "ListOperationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["OperationFilterTypeDef"],
    },
    total=False,
)

ListOperationsResponseTypeDef = TypedDict(
    "ListOperationsResponseTypeDef",
    {
        "Operations": List["OperationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["ServiceFilterTypeDef"],
    },
    total=False,
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "Services": List["ServiceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredNamespaceFilterTypeDef = TypedDict(
    "_RequiredNamespaceFilterTypeDef",
    {
        "Name": Literal["TYPE"],
        "Values": List[str],
    },
)
_OptionalNamespaceFilterTypeDef = TypedDict(
    "_OptionalNamespaceFilterTypeDef",
    {
        "Condition": FilterConditionType,
    },
    total=False,
)

class NamespaceFilterTypeDef(_RequiredNamespaceFilterTypeDef, _OptionalNamespaceFilterTypeDef):
    pass

NamespacePropertiesTypeDef = TypedDict(
    "NamespacePropertiesTypeDef",
    {
        "DnsProperties": "DnsPropertiesTypeDef",
        "HttpProperties": "HttpPropertiesTypeDef",
    },
    total=False,
)

NamespaceSummaryTypeDef = TypedDict(
    "NamespaceSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": NamespaceTypeType,
        "Description": str,
        "ServiceCount": int,
        "Properties": "NamespacePropertiesTypeDef",
        "CreateDate": datetime,
    },
    total=False,
)

NamespaceTypeDef = TypedDict(
    "NamespaceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": NamespaceTypeType,
        "Description": str,
        "ServiceCount": int,
        "Properties": "NamespacePropertiesTypeDef",
        "CreateDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)

_RequiredOperationFilterTypeDef = TypedDict(
    "_RequiredOperationFilterTypeDef",
    {
        "Name": OperationFilterNameType,
        "Values": List[str],
    },
)
_OptionalOperationFilterTypeDef = TypedDict(
    "_OptionalOperationFilterTypeDef",
    {
        "Condition": FilterConditionType,
    },
    total=False,
)

class OperationFilterTypeDef(_RequiredOperationFilterTypeDef, _OptionalOperationFilterTypeDef):
    pass

OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {
        "Id": str,
        "Status": OperationStatusType,
    },
    total=False,
)

OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "Id": str,
        "Type": OperationTypeType,
        "Status": OperationStatusType,
        "ErrorMessage": str,
        "ErrorCode": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "Targets": Dict[OperationTargetTypeType, str],
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

PrivateDnsNamespaceChangeTypeDef = TypedDict(
    "PrivateDnsNamespaceChangeTypeDef",
    {
        "Description": str,
        "Properties": "PrivateDnsNamespacePropertiesChangeTypeDef",
    },
    total=False,
)

PrivateDnsNamespacePropertiesChangeTypeDef = TypedDict(
    "PrivateDnsNamespacePropertiesChangeTypeDef",
    {
        "DnsProperties": "PrivateDnsPropertiesMutableChangeTypeDef",
    },
)

PrivateDnsNamespacePropertiesTypeDef = TypedDict(
    "PrivateDnsNamespacePropertiesTypeDef",
    {
        "DnsProperties": "PrivateDnsPropertiesMutableTypeDef",
    },
)

PrivateDnsPropertiesMutableChangeTypeDef = TypedDict(
    "PrivateDnsPropertiesMutableChangeTypeDef",
    {
        "SOA": "SOAChangeTypeDef",
    },
)

PrivateDnsPropertiesMutableTypeDef = TypedDict(
    "PrivateDnsPropertiesMutableTypeDef",
    {
        "SOA": "SOATypeDef",
    },
)

PublicDnsNamespaceChangeTypeDef = TypedDict(
    "PublicDnsNamespaceChangeTypeDef",
    {
        "Description": str,
        "Properties": "PublicDnsNamespacePropertiesChangeTypeDef",
    },
    total=False,
)

PublicDnsNamespacePropertiesChangeTypeDef = TypedDict(
    "PublicDnsNamespacePropertiesChangeTypeDef",
    {
        "DnsProperties": "PublicDnsPropertiesMutableChangeTypeDef",
    },
)

PublicDnsNamespacePropertiesTypeDef = TypedDict(
    "PublicDnsNamespacePropertiesTypeDef",
    {
        "DnsProperties": "PublicDnsPropertiesMutableTypeDef",
    },
)

PublicDnsPropertiesMutableChangeTypeDef = TypedDict(
    "PublicDnsPropertiesMutableChangeTypeDef",
    {
        "SOA": "SOAChangeTypeDef",
    },
)

PublicDnsPropertiesMutableTypeDef = TypedDict(
    "PublicDnsPropertiesMutableTypeDef",
    {
        "SOA": "SOATypeDef",
    },
)

_RequiredRegisterInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterInstanceRequestRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
        "Attributes": Dict[str, str],
    },
)
_OptionalRegisterInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterInstanceRequestRequestTypeDef",
    {
        "CreatorRequestId": str,
    },
    total=False,
)

class RegisterInstanceRequestRequestTypeDef(
    _RequiredRegisterInstanceRequestRequestTypeDef, _OptionalRegisterInstanceRequestRequestTypeDef
):
    pass

RegisterInstanceResponseTypeDef = TypedDict(
    "RegisterInstanceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

SOAChangeTypeDef = TypedDict(
    "SOAChangeTypeDef",
    {
        "TTL": int,
    },
)

SOATypeDef = TypedDict(
    "SOATypeDef",
    {
        "TTL": int,
    },
)

ServiceChangeTypeDef = TypedDict(
    "ServiceChangeTypeDef",
    {
        "Description": str,
        "DnsConfig": "DnsConfigChangeTypeDef",
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
    },
    total=False,
)

_RequiredServiceFilterTypeDef = TypedDict(
    "_RequiredServiceFilterTypeDef",
    {
        "Name": Literal["NAMESPACE_ID"],
        "Values": List[str],
    },
)
_OptionalServiceFilterTypeDef = TypedDict(
    "_OptionalServiceFilterTypeDef",
    {
        "Condition": FilterConditionType,
    },
    total=False,
)

class ServiceFilterTypeDef(_RequiredServiceFilterTypeDef, _OptionalServiceFilterTypeDef):
    pass

ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": ServiceTypeType,
        "Description": str,
        "InstanceCount": int,
        "DnsConfig": "DnsConfigTypeDef",
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
        "HealthCheckCustomConfig": "HealthCheckCustomConfigTypeDef",
        "CreateDate": datetime,
    },
    total=False,
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "NamespaceId": str,
        "Description": str,
        "InstanceCount": int,
        "DnsConfig": "DnsConfigTypeDef",
        "Type": ServiceTypeType,
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
        "HealthCheckCustomConfig": "HealthCheckCustomConfigTypeDef",
        "CreateDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateHttpNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateHttpNamespaceRequestRequestTypeDef",
    {
        "Id": str,
        "Namespace": "HttpNamespaceChangeTypeDef",
    },
)
_OptionalUpdateHttpNamespaceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateHttpNamespaceRequestRequestTypeDef",
    {
        "UpdaterRequestId": str,
    },
    total=False,
)

class UpdateHttpNamespaceRequestRequestTypeDef(
    _RequiredUpdateHttpNamespaceRequestRequestTypeDef,
    _OptionalUpdateHttpNamespaceRequestRequestTypeDef,
):
    pass

UpdateHttpNamespaceResponseTypeDef = TypedDict(
    "UpdateHttpNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateInstanceCustomHealthStatusRequestRequestTypeDef = TypedDict(
    "UpdateInstanceCustomHealthStatusRequestRequestTypeDef",
    {
        "ServiceId": str,
        "InstanceId": str,
        "Status": CustomHealthStatusType,
    },
)

_RequiredUpdatePrivateDnsNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePrivateDnsNamespaceRequestRequestTypeDef",
    {
        "Id": str,
        "Namespace": "PrivateDnsNamespaceChangeTypeDef",
    },
)
_OptionalUpdatePrivateDnsNamespaceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePrivateDnsNamespaceRequestRequestTypeDef",
    {
        "UpdaterRequestId": str,
    },
    total=False,
)

class UpdatePrivateDnsNamespaceRequestRequestTypeDef(
    _RequiredUpdatePrivateDnsNamespaceRequestRequestTypeDef,
    _OptionalUpdatePrivateDnsNamespaceRequestRequestTypeDef,
):
    pass

UpdatePrivateDnsNamespaceResponseTypeDef = TypedDict(
    "UpdatePrivateDnsNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePublicDnsNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePublicDnsNamespaceRequestRequestTypeDef",
    {
        "Id": str,
        "Namespace": "PublicDnsNamespaceChangeTypeDef",
    },
)
_OptionalUpdatePublicDnsNamespaceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePublicDnsNamespaceRequestRequestTypeDef",
    {
        "UpdaterRequestId": str,
    },
    total=False,
)

class UpdatePublicDnsNamespaceRequestRequestTypeDef(
    _RequiredUpdatePublicDnsNamespaceRequestRequestTypeDef,
    _OptionalUpdatePublicDnsNamespaceRequestRequestTypeDef,
):
    pass

UpdatePublicDnsNamespaceResponseTypeDef = TypedDict(
    "UpdatePublicDnsNamespaceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceRequestRequestTypeDef = TypedDict(
    "UpdateServiceRequestRequestTypeDef",
    {
        "Id": str,
        "Service": "ServiceChangeTypeDef",
    },
)

UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
