"""
Type annotations for servicediscovery service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicediscovery/literals.html)

Usage::

    ```python
    from mypy_boto3_servicediscovery.literals import CustomHealthStatusType

    data: CustomHealthStatusType = "HEALTHY"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CustomHealthStatusType",
    "FilterConditionType",
    "HealthCheckTypeType",
    "HealthStatusFilterType",
    "HealthStatusType",
    "ListInstancesPaginatorName",
    "ListNamespacesPaginatorName",
    "ListOperationsPaginatorName",
    "ListServicesPaginatorName",
    "NamespaceFilterNameType",
    "NamespaceTypeType",
    "OperationFilterNameType",
    "OperationStatusType",
    "OperationTargetTypeType",
    "OperationTypeType",
    "RecordTypeType",
    "RoutingPolicyType",
    "ServiceFilterNameType",
    "ServiceTypeOptionType",
    "ServiceTypeType",
)

CustomHealthStatusType = Literal["HEALTHY", "UNHEALTHY"]
FilterConditionType = Literal["BETWEEN", "EQ", "IN"]
HealthCheckTypeType = Literal["HTTP", "HTTPS", "TCP"]
HealthStatusFilterType = Literal["ALL", "HEALTHY", "HEALTHY_OR_ELSE_ALL", "UNHEALTHY"]
HealthStatusType = Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]
ListInstancesPaginatorName = Literal["list_instances"]
ListNamespacesPaginatorName = Literal["list_namespaces"]
ListOperationsPaginatorName = Literal["list_operations"]
ListServicesPaginatorName = Literal["list_services"]
NamespaceFilterNameType = Literal["TYPE"]
NamespaceTypeType = Literal["DNS_PRIVATE", "DNS_PUBLIC", "HTTP"]
OperationFilterNameType = Literal["NAMESPACE_ID", "SERVICE_ID", "STATUS", "TYPE", "UPDATE_DATE"]
OperationStatusType = Literal["FAIL", "PENDING", "SUBMITTED", "SUCCESS"]
OperationTargetTypeType = Literal["INSTANCE", "NAMESPACE", "SERVICE"]
OperationTypeType = Literal[
    "CREATE_NAMESPACE",
    "DELETE_NAMESPACE",
    "DEREGISTER_INSTANCE",
    "REGISTER_INSTANCE",
    "UPDATE_NAMESPACE",
    "UPDATE_SERVICE",
]
RecordTypeType = Literal["A", "AAAA", "CNAME", "SRV"]
RoutingPolicyType = Literal["MULTIVALUE", "WEIGHTED"]
ServiceFilterNameType = Literal["NAMESPACE_ID"]
ServiceTypeOptionType = Literal["HTTP"]
ServiceTypeType = Literal["DNS", "DNS_HTTP", "HTTP"]
