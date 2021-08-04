"""
Type annotations for route53-recovery-cluster service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/type_defs.html)

Usage::

    ```python
    from mypy_boto3_route53_recovery_cluster.type_defs import GetRoutingControlStateRequestRequestTypeDef

    data: GetRoutingControlStateRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import RoutingControlStateType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "GetRoutingControlStateRequestRequestTypeDef",
    "GetRoutingControlStateResponseTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateRoutingControlStateEntryTypeDef",
    "UpdateRoutingControlStateRequestRequestTypeDef",
    "UpdateRoutingControlStatesRequestRequestTypeDef",
)

GetRoutingControlStateRequestRequestTypeDef = TypedDict(
    "GetRoutingControlStateRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
    },
)

GetRoutingControlStateResponseTypeDef = TypedDict(
    "GetRoutingControlStateResponseTypeDef",
    {
        "RoutingControlArn": str,
        "RoutingControlState": RoutingControlStateType,
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

UpdateRoutingControlStateEntryTypeDef = TypedDict(
    "UpdateRoutingControlStateEntryTypeDef",
    {
        "RoutingControlArn": str,
        "RoutingControlState": RoutingControlStateType,
    },
)

UpdateRoutingControlStateRequestRequestTypeDef = TypedDict(
    "UpdateRoutingControlStateRequestRequestTypeDef",
    {
        "RoutingControlArn": str,
        "RoutingControlState": RoutingControlStateType,
    },
)

UpdateRoutingControlStatesRequestRequestTypeDef = TypedDict(
    "UpdateRoutingControlStatesRequestRequestTypeDef",
    {
        "UpdateRoutingControlStateEntries": List["UpdateRoutingControlStateEntryTypeDef"],
    },
)
