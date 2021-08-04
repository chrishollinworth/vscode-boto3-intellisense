"""
Type annotations for dax service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dax/literals.html)

Usage::

    ```python
    from mypy_boto3_dax.literals import ChangeTypeType

    data: ChangeTypeType = "IMMEDIATE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ChangeTypeType",
    "ClusterEndpointEncryptionTypeType",
    "DescribeClustersPaginatorName",
    "DescribeDefaultParametersPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeParameterGroupsPaginatorName",
    "DescribeParametersPaginatorName",
    "DescribeSubnetGroupsPaginatorName",
    "IsModifiableType",
    "ListTagsPaginatorName",
    "ParameterTypeType",
    "SSEStatusType",
    "SourceTypeType",
)

ChangeTypeType = Literal["IMMEDIATE", "REQUIRES_REBOOT"]
ClusterEndpointEncryptionTypeType = Literal["NONE", "TLS"]
DescribeClustersPaginatorName = Literal["describe_clusters"]
DescribeDefaultParametersPaginatorName = Literal["describe_default_parameters"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeParameterGroupsPaginatorName = Literal["describe_parameter_groups"]
DescribeParametersPaginatorName = Literal["describe_parameters"]
DescribeSubnetGroupsPaginatorName = Literal["describe_subnet_groups"]
IsModifiableType = Literal["CONDITIONAL", "FALSE", "TRUE"]
ListTagsPaginatorName = Literal["list_tags"]
ParameterTypeType = Literal["DEFAULT", "NODE_TYPE_SPECIFIC"]
SSEStatusType = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
SourceTypeType = Literal["CLUSTER", "PARAMETER_GROUP", "SUBNET_GROUP"]
