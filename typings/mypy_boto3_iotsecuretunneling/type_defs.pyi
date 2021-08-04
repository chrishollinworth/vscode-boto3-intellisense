"""
Type annotations for iotsecuretunneling service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotsecuretunneling.type_defs import CloseTunnelRequestRequestTypeDef

    data: CloseTunnelRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ConnectionStatusType, TunnelStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CloseTunnelRequestRequestTypeDef",
    "ConnectionStateTypeDef",
    "DescribeTunnelRequestRequestTypeDef",
    "DescribeTunnelResponseTypeDef",
    "DestinationConfigTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTunnelsRequestRequestTypeDef",
    "ListTunnelsResponseTypeDef",
    "OpenTunnelRequestRequestTypeDef",
    "OpenTunnelResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TimeoutConfigTypeDef",
    "TunnelSummaryTypeDef",
    "TunnelTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

_RequiredCloseTunnelRequestRequestTypeDef = TypedDict(
    "_RequiredCloseTunnelRequestRequestTypeDef",
    {
        "tunnelId": str,
    },
)
_OptionalCloseTunnelRequestRequestTypeDef = TypedDict(
    "_OptionalCloseTunnelRequestRequestTypeDef",
    {
        "delete": bool,
    },
    total=False,
)

class CloseTunnelRequestRequestTypeDef(
    _RequiredCloseTunnelRequestRequestTypeDef, _OptionalCloseTunnelRequestRequestTypeDef
):
    pass

ConnectionStateTypeDef = TypedDict(
    "ConnectionStateTypeDef",
    {
        "status": ConnectionStatusType,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

DescribeTunnelRequestRequestTypeDef = TypedDict(
    "DescribeTunnelRequestRequestTypeDef",
    {
        "tunnelId": str,
    },
)

DescribeTunnelResponseTypeDef = TypedDict(
    "DescribeTunnelResponseTypeDef",
    {
        "tunnel": "TunnelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDestinationConfigTypeDef = TypedDict(
    "_RequiredDestinationConfigTypeDef",
    {
        "services": List[str],
    },
)
_OptionalDestinationConfigTypeDef = TypedDict(
    "_OptionalDestinationConfigTypeDef",
    {
        "thingName": str,
    },
    total=False,
)

class DestinationConfigTypeDef(
    _RequiredDestinationConfigTypeDef, _OptionalDestinationConfigTypeDef
):
    pass

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTunnelsRequestRequestTypeDef = TypedDict(
    "ListTunnelsRequestRequestTypeDef",
    {
        "thingName": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTunnelsResponseTypeDef = TypedDict(
    "ListTunnelsResponseTypeDef",
    {
        "tunnelSummaries": List["TunnelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OpenTunnelRequestRequestTypeDef = TypedDict(
    "OpenTunnelRequestRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
        "destinationConfig": "DestinationConfigTypeDef",
        "timeoutConfig": "TimeoutConfigTypeDef",
    },
    total=False,
)

OpenTunnelResponseTypeDef = TypedDict(
    "OpenTunnelResponseTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "sourceAccessToken": str,
        "destinationAccessToken": str,
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TimeoutConfigTypeDef = TypedDict(
    "TimeoutConfigTypeDef",
    {
        "maxLifetimeTimeoutMinutes": int,
    },
    total=False,
)

TunnelSummaryTypeDef = TypedDict(
    "TunnelSummaryTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "status": TunnelStatusType,
        "description": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

TunnelTypeDef = TypedDict(
    "TunnelTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "status": TunnelStatusType,
        "sourceConnectionState": "ConnectionStateTypeDef",
        "destinationConnectionState": "ConnectionStateTypeDef",
        "description": str,
        "destinationConfig": "DestinationConfigTypeDef",
        "timeoutConfig": "TimeoutConfigTypeDef",
        "tags": List["TagTypeDef"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)
