"""
Type annotations for iot-data service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_data/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_iot_data.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import PayloadFormatIndicatorType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
else:
    from typing import Dict, List
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "BlobTypeDef",
    "DeleteThingShadowRequestTypeDef",
    "DeleteThingShadowResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetRetainedMessageRequestTypeDef",
    "GetRetainedMessageResponseTypeDef",
    "GetThingShadowRequestTypeDef",
    "GetThingShadowResponseTypeDef",
    "ListNamedShadowsForThingRequestTypeDef",
    "ListNamedShadowsForThingResponseTypeDef",
    "ListRetainedMessagesRequestPaginateTypeDef",
    "ListRetainedMessagesRequestTypeDef",
    "ListRetainedMessagesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PublishRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RetainedMessageSummaryTypeDef",
    "UpdateThingShadowRequestTypeDef",
    "UpdateThingShadowResponseTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class DeleteThingShadowRequestTypeDef(TypedDict):
    thingName: str
    shadowName: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetRetainedMessageRequestTypeDef(TypedDict):
    topic: str

class GetThingShadowRequestTypeDef(TypedDict):
    thingName: str
    shadowName: NotRequired[str]

class ListNamedShadowsForThingRequestTypeDef(TypedDict):
    thingName: str
    nextToken: NotRequired[str]
    pageSize: NotRequired[int]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListRetainedMessagesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class RetainedMessageSummaryTypeDef(TypedDict):
    topic: NotRequired[str]
    payloadSize: NotRequired[int]
    qos: NotRequired[int]
    lastModifiedTime: NotRequired[int]

class PublishRequestTypeDef(TypedDict):
    topic: str
    qos: NotRequired[int]
    retain: NotRequired[bool]
    payload: NotRequired[BlobTypeDef]
    userProperties: NotRequired[str]
    payloadFormatIndicator: NotRequired[PayloadFormatIndicatorType]
    contentType: NotRequired[str]
    responseTopic: NotRequired[str]
    correlationData: NotRequired[str]
    messageExpiry: NotRequired[int]

class UpdateThingShadowRequestTypeDef(TypedDict):
    thingName: str
    payload: BlobTypeDef
    shadowName: NotRequired[str]

class DeleteThingShadowResponseTypeDef(TypedDict):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetRetainedMessageResponseTypeDef(TypedDict):
    topic: str
    payload: bytes
    qos: int
    lastModifiedTime: int
    userProperties: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class GetThingShadowResponseTypeDef(TypedDict):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ListNamedShadowsForThingResponseTypeDef(TypedDict):
    results: List[str]
    timestamp: int
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateThingShadowResponseTypeDef(TypedDict):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ListRetainedMessagesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRetainedMessagesResponseTypeDef(TypedDict):
    retainedTopics: List[RetainedMessageSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
