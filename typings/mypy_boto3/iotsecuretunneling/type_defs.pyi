"""
Type annotations for iotsecuretunneling service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_iotsecuretunneling.type_defs import CloseTunnelRequestTypeDef

    data: CloseTunnelRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import ClientModeType, ConnectionStatusType, TunnelStatusType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CloseTunnelRequestTypeDef",
    "ConnectionStateTypeDef",
    "DescribeTunnelRequestTypeDef",
    "DescribeTunnelResponseTypeDef",
    "DestinationConfigOutputTypeDef",
    "DestinationConfigTypeDef",
    "DestinationConfigUnionTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTunnelsRequestTypeDef",
    "ListTunnelsResponseTypeDef",
    "OpenTunnelRequestTypeDef",
    "OpenTunnelResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RotateTunnelAccessTokenRequestTypeDef",
    "RotateTunnelAccessTokenResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimeoutConfigTypeDef",
    "TunnelSummaryTypeDef",
    "TunnelTypeDef",
    "UntagResourceRequestTypeDef",
)

class CloseTunnelRequestTypeDef(TypedDict):
    tunnelId: str
    delete: NotRequired[bool]

class ConnectionStateTypeDef(TypedDict):
    status: NotRequired[ConnectionStatusType]
    lastUpdatedAt: NotRequired[datetime]

class DescribeTunnelRequestTypeDef(TypedDict):
    tunnelId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DestinationConfigOutputTypeDef(TypedDict):
    services: List[str]
    thingName: NotRequired[str]

class DestinationConfigTypeDef(TypedDict):
    services: Sequence[str]
    thingName: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class TagTypeDef(TypedDict):
    key: str
    value: str

class ListTunnelsRequestTypeDef(TypedDict):
    thingName: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class TunnelSummaryTypeDef(TypedDict):
    tunnelId: NotRequired[str]
    tunnelArn: NotRequired[str]
    status: NotRequired[TunnelStatusType]
    description: NotRequired[str]
    createdAt: NotRequired[datetime]
    lastUpdatedAt: NotRequired[datetime]

class TimeoutConfigTypeDef(TypedDict):
    maxLifetimeTimeoutMinutes: NotRequired[int]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class OpenTunnelResponseTypeDef(TypedDict):
    tunnelId: str
    tunnelArn: str
    sourceAccessToken: str
    destinationAccessToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RotateTunnelAccessTokenResponseTypeDef(TypedDict):
    tunnelArn: str
    sourceAccessToken: str
    destinationAccessToken: str
    ResponseMetadata: ResponseMetadataTypeDef

DestinationConfigUnionTypeDef = Union[DestinationConfigTypeDef, DestinationConfigOutputTypeDef]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class ListTunnelsResponseTypeDef(TypedDict):
    tunnelSummaries: List[TunnelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class TunnelTypeDef(TypedDict):
    tunnelId: NotRequired[str]
    tunnelArn: NotRequired[str]
    status: NotRequired[TunnelStatusType]
    sourceConnectionState: NotRequired[ConnectionStateTypeDef]
    destinationConnectionState: NotRequired[ConnectionStateTypeDef]
    description: NotRequired[str]
    destinationConfig: NotRequired[DestinationConfigOutputTypeDef]
    timeoutConfig: NotRequired[TimeoutConfigTypeDef]
    tags: NotRequired[List[TagTypeDef]]
    createdAt: NotRequired[datetime]
    lastUpdatedAt: NotRequired[datetime]

class OpenTunnelRequestTypeDef(TypedDict):
    description: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    destinationConfig: NotRequired[DestinationConfigUnionTypeDef]
    timeoutConfig: NotRequired[TimeoutConfigTypeDef]

class RotateTunnelAccessTokenRequestTypeDef(TypedDict):
    tunnelId: str
    clientMode: ClientModeType
    destinationConfig: NotRequired[DestinationConfigUnionTypeDef]

class DescribeTunnelResponseTypeDef(TypedDict):
    tunnel: TunnelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
