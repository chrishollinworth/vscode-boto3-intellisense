"""
Type annotations for memorydb service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/literals.html)

Usage::

    ```python
    from mypy_boto3_memorydb.literals import AZStatusType

    data: AZStatusType = "multiaz"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AZStatusType",
    "AuthenticationTypeType",
    "DataTieringStatusType",
    "DescribeACLsPaginatorName",
    "DescribeClustersPaginatorName",
    "DescribeEngineVersionsPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeParameterGroupsPaginatorName",
    "DescribeParametersPaginatorName",
    "DescribeReservedNodesOfferingsPaginatorName",
    "DescribeReservedNodesPaginatorName",
    "DescribeServiceUpdatesPaginatorName",
    "DescribeSnapshotsPaginatorName",
    "DescribeSubnetGroupsPaginatorName",
    "DescribeUsersPaginatorName",
    "InputAuthenticationTypeType",
    "ServiceUpdateStatusType",
    "ServiceUpdateTypeType",
    "SourceTypeType",
)

AZStatusType = Literal["multiaz", "singleaz"]
AuthenticationTypeType = Literal["iam", "no-password", "password"]
DataTieringStatusType = Literal["false", "true"]
DescribeACLsPaginatorName = Literal["describe_acls"]
DescribeClustersPaginatorName = Literal["describe_clusters"]
DescribeEngineVersionsPaginatorName = Literal["describe_engine_versions"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeParameterGroupsPaginatorName = Literal["describe_parameter_groups"]
DescribeParametersPaginatorName = Literal["describe_parameters"]
DescribeReservedNodesOfferingsPaginatorName = Literal["describe_reserved_nodes_offerings"]
DescribeReservedNodesPaginatorName = Literal["describe_reserved_nodes"]
DescribeServiceUpdatesPaginatorName = Literal["describe_service_updates"]
DescribeSnapshotsPaginatorName = Literal["describe_snapshots"]
DescribeSubnetGroupsPaginatorName = Literal["describe_subnet_groups"]
DescribeUsersPaginatorName = Literal["describe_users"]
InputAuthenticationTypeType = Literal["iam", "password"]
ServiceUpdateStatusType = Literal["available", "complete", "in-progress", "scheduled"]
ServiceUpdateTypeType = Literal["security-update"]
SourceTypeType = Literal["acl", "cluster", "node", "parameter-group", "subnet-group", "user"]
