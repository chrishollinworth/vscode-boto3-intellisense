"""
Type annotations for vpc-lattice service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/literals.html)

Usage::

    ```python
    from mypy_boto3_vpc_lattice.literals import AuthPolicyStateType

    data: AuthPolicyStateType = "Active"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AuthPolicyStateType",
    "AuthTypeType",
    "HealthCheckProtocolVersionType",
    "IpAddressTypeType",
    "LambdaEventStructureVersionType",
    "ListAccessLogSubscriptionsPaginatorName",
    "ListListenersPaginatorName",
    "ListRulesPaginatorName",
    "ListServiceNetworkServiceAssociationsPaginatorName",
    "ListServiceNetworkVpcAssociationsPaginatorName",
    "ListServiceNetworksPaginatorName",
    "ListServicesPaginatorName",
    "ListTargetGroupsPaginatorName",
    "ListTargetsPaginatorName",
    "ListenerProtocolType",
    "ServiceNetworkServiceAssociationStatusType",
    "ServiceNetworkVpcAssociationStatusType",
    "ServiceStatusType",
    "TargetGroupProtocolType",
    "TargetGroupProtocolVersionType",
    "TargetGroupStatusType",
    "TargetGroupTypeType",
    "TargetStatusType",
)

AuthPolicyStateType = Literal["Active", "Inactive"]
AuthTypeType = Literal["AWS_IAM", "NONE"]
HealthCheckProtocolVersionType = Literal["HTTP1", "HTTP2"]
IpAddressTypeType = Literal["IPV4", "IPV6"]
LambdaEventStructureVersionType = Literal["V1", "V2"]
ListAccessLogSubscriptionsPaginatorName = Literal["list_access_log_subscriptions"]
ListListenersPaginatorName = Literal["list_listeners"]
ListRulesPaginatorName = Literal["list_rules"]
ListServiceNetworkServiceAssociationsPaginatorName = Literal[
    "list_service_network_service_associations"
]
ListServiceNetworkVpcAssociationsPaginatorName = Literal["list_service_network_vpc_associations"]
ListServiceNetworksPaginatorName = Literal["list_service_networks"]
ListServicesPaginatorName = Literal["list_services"]
ListTargetGroupsPaginatorName = Literal["list_target_groups"]
ListTargetsPaginatorName = Literal["list_targets"]
ListenerProtocolType = Literal["HTTP", "HTTPS"]
ServiceNetworkServiceAssociationStatusType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETE_FAILED", "DELETE_IN_PROGRESS"
]
ServiceNetworkVpcAssociationStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
ServiceStatusType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETE_FAILED", "DELETE_IN_PROGRESS"
]
TargetGroupProtocolType = Literal["HTTP", "HTTPS"]
TargetGroupProtocolVersionType = Literal["GRPC", "HTTP1", "HTTP2"]
TargetGroupStatusType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETE_FAILED", "DELETE_IN_PROGRESS"
]
TargetGroupTypeType = Literal["ALB", "INSTANCE", "IP", "LAMBDA"]
TargetStatusType = Literal["DRAINING", "HEALTHY", "INITIAL", "UNAVAILABLE", "UNHEALTHY", "UNUSED"]
