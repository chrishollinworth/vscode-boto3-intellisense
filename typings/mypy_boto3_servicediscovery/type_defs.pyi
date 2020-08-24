"""
Main interface for servicediscovery service type definitions.

Usage::

    ```python
    from mypy_boto3_servicediscovery.type_defs import DnsConfigChangeTypeDef

    data: DnsConfigChangeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DnsConfigChangeTypeDef",
    "DnsConfigTypeDef",
    "DnsPropertiesTypeDef",
    "DnsRecordTypeDef",
    "HealthCheckConfigTypeDef",
    "HealthCheckCustomConfigTypeDef",
    "HttpInstanceSummaryTypeDef",
    "HttpPropertiesTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "NamespacePropertiesTypeDef",
    "NamespaceSummaryTypeDef",
    "NamespaceTypeDef",
    "OperationSummaryTypeDef",
    "OperationTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTypeDef",
    "TagTypeDef",
    "CreateHttpNamespaceResponseTypeDef",
    "CreatePrivateDnsNamespaceResponseTypeDef",
    "CreatePublicDnsNamespaceResponseTypeDef",
    "CreateServiceResponseTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeregisterInstanceResponseTypeDef",
    "DiscoverInstancesResponseTypeDef",
    "GetInstanceResponseTypeDef",
    "GetInstancesHealthStatusResponseTypeDef",
    "GetNamespaceResponseTypeDef",
    "GetOperationResponseTypeDef",
    "GetServiceResponseTypeDef",
    "ListInstancesResponseTypeDef",
    "ListNamespacesResponseTypeDef",
    "ListOperationsResponseTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NamespaceFilterTypeDef",
    "OperationFilterTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterInstanceResponseTypeDef",
    "ServiceChangeTypeDef",
    "ServiceFilterTypeDef",
    "UpdateServiceResponseTypeDef",
)

DnsConfigChangeTypeDef = TypedDict(
    "DnsConfigChangeTypeDef", {"DnsRecords": List["DnsRecordTypeDef"]}
)

_RequiredDnsConfigTypeDef = TypedDict(
    "_RequiredDnsConfigTypeDef", {"DnsRecords": List["DnsRecordTypeDef"]}
)
_OptionalDnsConfigTypeDef = TypedDict(
    "_OptionalDnsConfigTypeDef",
    {"NamespaceId": str, "RoutingPolicy": Literal["MULTIVALUE", "WEIGHTED"]},
    total=False,
)


class DnsConfigTypeDef(_RequiredDnsConfigTypeDef, _OptionalDnsConfigTypeDef):
    pass


DnsPropertiesTypeDef = TypedDict("DnsPropertiesTypeDef", {"HostedZoneId": str}, total=False)

DnsRecordTypeDef = TypedDict(
    "DnsRecordTypeDef", {"Type": Literal["SRV", "A", "AAAA", "CNAME"], "TTL": int}
)

_RequiredHealthCheckConfigTypeDef = TypedDict(
    "_RequiredHealthCheckConfigTypeDef", {"Type": Literal["HTTP", "HTTPS", "TCP"]}
)
_OptionalHealthCheckConfigTypeDef = TypedDict(
    "_OptionalHealthCheckConfigTypeDef", {"ResourcePath": str, "FailureThreshold": int}, total=False
)


class HealthCheckConfigTypeDef(
    _RequiredHealthCheckConfigTypeDef, _OptionalHealthCheckConfigTypeDef
):
    pass


HealthCheckCustomConfigTypeDef = TypedDict(
    "HealthCheckCustomConfigTypeDef", {"FailureThreshold": int}, total=False
)

HttpInstanceSummaryTypeDef = TypedDict(
    "HttpInstanceSummaryTypeDef",
    {
        "InstanceId": str,
        "NamespaceName": str,
        "ServiceName": str,
        "HealthStatus": Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"],
        "Attributes": Dict[str, str],
    },
    total=False,
)

HttpPropertiesTypeDef = TypedDict("HttpPropertiesTypeDef", {"HttpName": str}, total=False)

InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef", {"Id": str, "Attributes": Dict[str, str]}, total=False
)

_RequiredInstanceTypeDef = TypedDict("_RequiredInstanceTypeDef", {"Id": str})
_OptionalInstanceTypeDef = TypedDict(
    "_OptionalInstanceTypeDef", {"CreatorRequestId": str, "Attributes": Dict[str, str]}, total=False
)


class InstanceTypeDef(_RequiredInstanceTypeDef, _OptionalInstanceTypeDef):
    pass


NamespacePropertiesTypeDef = TypedDict(
    "NamespacePropertiesTypeDef",
    {"DnsProperties": "DnsPropertiesTypeDef", "HttpProperties": "HttpPropertiesTypeDef"},
    total=False,
)

NamespaceSummaryTypeDef = TypedDict(
    "NamespaceSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Type": Literal["DNS_PUBLIC", "DNS_PRIVATE", "HTTP"],
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
        "Type": Literal["DNS_PUBLIC", "DNS_PRIVATE", "HTTP"],
        "Description": str,
        "ServiceCount": int,
        "Properties": "NamespacePropertiesTypeDef",
        "CreateDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)

OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {"Id": str, "Status": Literal["SUBMITTED", "PENDING", "SUCCESS", "FAIL"]},
    total=False,
)

OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "Id": str,
        "Type": Literal[
            "CREATE_NAMESPACE",
            "DELETE_NAMESPACE",
            "UPDATE_SERVICE",
            "REGISTER_INSTANCE",
            "DEREGISTER_INSTANCE",
        ],
        "Status": Literal["SUBMITTED", "PENDING", "SUCCESS", "FAIL"],
        "ErrorMessage": str,
        "ErrorCode": str,
        "CreateDate": datetime,
        "UpdateDate": datetime,
        "Targets": Dict[Literal["NAMESPACE", "SERVICE", "INSTANCE"], str],
    },
    total=False,
)

ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
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
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
        "HealthCheckCustomConfig": "HealthCheckCustomConfigTypeDef",
        "CreateDate": datetime,
        "CreatorRequestId": str,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

CreateHttpNamespaceResponseTypeDef = TypedDict(
    "CreateHttpNamespaceResponseTypeDef", {"OperationId": str}, total=False
)

CreatePrivateDnsNamespaceResponseTypeDef = TypedDict(
    "CreatePrivateDnsNamespaceResponseTypeDef", {"OperationId": str}, total=False
)

CreatePublicDnsNamespaceResponseTypeDef = TypedDict(
    "CreatePublicDnsNamespaceResponseTypeDef", {"OperationId": str}, total=False
)

CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef", {"Service": "ServiceTypeDef"}, total=False
)

DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef", {"OperationId": str}, total=False
)

DeregisterInstanceResponseTypeDef = TypedDict(
    "DeregisterInstanceResponseTypeDef", {"OperationId": str}, total=False
)

DiscoverInstancesResponseTypeDef = TypedDict(
    "DiscoverInstancesResponseTypeDef",
    {"Instances": List["HttpInstanceSummaryTypeDef"]},
    total=False,
)

GetInstanceResponseTypeDef = TypedDict(
    "GetInstanceResponseTypeDef", {"Instance": "InstanceTypeDef"}, total=False
)

GetInstancesHealthStatusResponseTypeDef = TypedDict(
    "GetInstancesHealthStatusResponseTypeDef",
    {"Status": Dict[str, Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]], "NextToken": str},
    total=False,
)

GetNamespaceResponseTypeDef = TypedDict(
    "GetNamespaceResponseTypeDef", {"Namespace": "NamespaceTypeDef"}, total=False
)

GetOperationResponseTypeDef = TypedDict(
    "GetOperationResponseTypeDef", {"Operation": "OperationTypeDef"}, total=False
)

GetServiceResponseTypeDef = TypedDict(
    "GetServiceResponseTypeDef", {"Service": "ServiceTypeDef"}, total=False
)

ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {"Instances": List["InstanceSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListNamespacesResponseTypeDef = TypedDict(
    "ListNamespacesResponseTypeDef",
    {"Namespaces": List["NamespaceSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListOperationsResponseTypeDef = TypedDict(
    "ListOperationsResponseTypeDef",
    {"Operations": List["OperationSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {"Services": List["ServiceSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

_RequiredNamespaceFilterTypeDef = TypedDict(
    "_RequiredNamespaceFilterTypeDef", {"Name": Literal["TYPE"], "Values": List[str]}
)
_OptionalNamespaceFilterTypeDef = TypedDict(
    "_OptionalNamespaceFilterTypeDef", {"Condition": Literal["EQ", "IN", "BETWEEN"]}, total=False
)


class NamespaceFilterTypeDef(_RequiredNamespaceFilterTypeDef, _OptionalNamespaceFilterTypeDef):
    pass


_RequiredOperationFilterTypeDef = TypedDict(
    "_RequiredOperationFilterTypeDef",
    {
        "Name": Literal["NAMESPACE_ID", "SERVICE_ID", "STATUS", "TYPE", "UPDATE_DATE"],
        "Values": List[str],
    },
)
_OptionalOperationFilterTypeDef = TypedDict(
    "_OptionalOperationFilterTypeDef", {"Condition": Literal["EQ", "IN", "BETWEEN"]}, total=False
)


class OperationFilterTypeDef(_RequiredOperationFilterTypeDef, _OptionalOperationFilterTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RegisterInstanceResponseTypeDef = TypedDict(
    "RegisterInstanceResponseTypeDef", {"OperationId": str}, total=False
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
    "_RequiredServiceFilterTypeDef", {"Name": Literal["NAMESPACE_ID"], "Values": List[str]}
)
_OptionalServiceFilterTypeDef = TypedDict(
    "_OptionalServiceFilterTypeDef", {"Condition": Literal["EQ", "IN", "BETWEEN"]}, total=False
)


class ServiceFilterTypeDef(_RequiredServiceFilterTypeDef, _OptionalServiceFilterTypeDef):
    pass


UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef", {"OperationId": str}, total=False
)
