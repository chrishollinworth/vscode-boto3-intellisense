"""
Type annotations for dynamodbstreams service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_dynamodbstreams.type_defs import AttributeValueTypeDef

    data: AttributeValueTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any

from .literals import (
    KeyTypeType,
    OperationTypeType,
    ShardIteratorTypeType,
    StreamStatusType,
    StreamViewTypeType,
)

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
    "AttributeValueTypeDef",
    "DescribeStreamInputTypeDef",
    "DescribeStreamOutputTypeDef",
    "GetRecordsInputTypeDef",
    "GetRecordsOutputTypeDef",
    "GetShardIteratorInputTypeDef",
    "GetShardIteratorOutputTypeDef",
    "IdentityTypeDef",
    "KeySchemaElementTypeDef",
    "ListStreamsInputTypeDef",
    "ListStreamsOutputTypeDef",
    "RecordTypeDef",
    "ResponseMetadataTypeDef",
    "SequenceNumberRangeTypeDef",
    "ShardTypeDef",
    "StreamDescriptionTypeDef",
    "StreamRecordTypeDef",
    "StreamTypeDef",
)

class AttributeValueTypeDef(TypedDict):
    S: NotRequired[str]
    N: NotRequired[str]
    B: NotRequired[bytes]
    SS: NotRequired[List[str]]
    NS: NotRequired[List[str]]
    BS: NotRequired[List[bytes]]
    M: NotRequired[Dict[str, Dict[str, Any]]]
    L: NotRequired[List[Dict[str, Any]]]
    NULL: NotRequired[bool]
    BOOL: NotRequired[bool]

class DescribeStreamInputTypeDef(TypedDict):
    StreamArn: str
    Limit: NotRequired[int]
    ExclusiveStartShardId: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetRecordsInputTypeDef(TypedDict):
    ShardIterator: str
    Limit: NotRequired[int]

class GetShardIteratorInputTypeDef(TypedDict):
    StreamArn: str
    ShardId: str
    ShardIteratorType: ShardIteratorTypeType
    SequenceNumber: NotRequired[str]

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "PrincipalId": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class KeySchemaElementTypeDef(TypedDict):
    AttributeName: str
    KeyType: KeyTypeType

class ListStreamsInputTypeDef(TypedDict):
    TableName: NotRequired[str]
    Limit: NotRequired[int]
    ExclusiveStartStreamArn: NotRequired[str]

class StreamTypeDef(TypedDict):
    StreamArn: NotRequired[str]
    TableName: NotRequired[str]
    StreamLabel: NotRequired[str]

class SequenceNumberRangeTypeDef(TypedDict):
    StartingSequenceNumber: NotRequired[str]
    EndingSequenceNumber: NotRequired[str]

class StreamRecordTypeDef(TypedDict):
    ApproximateCreationDateTime: NotRequired[datetime]
    Keys: NotRequired[Dict[str, AttributeValueTypeDef]]
    NewImage: NotRequired[Dict[str, AttributeValueTypeDef]]
    OldImage: NotRequired[Dict[str, AttributeValueTypeDef]]
    SequenceNumber: NotRequired[str]
    SizeBytes: NotRequired[int]
    StreamViewType: NotRequired[StreamViewTypeType]

class GetShardIteratorOutputTypeDef(TypedDict):
    ShardIterator: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamsOutputTypeDef(TypedDict):
    Streams: List[StreamTypeDef]
    LastEvaluatedStreamArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ShardTypeDef(TypedDict):
    ShardId: NotRequired[str]
    SequenceNumberRange: NotRequired[SequenceNumberRangeTypeDef]
    ParentShardId: NotRequired[str]

class RecordTypeDef(TypedDict):
    eventID: NotRequired[str]
    eventName: NotRequired[OperationTypeType]
    eventVersion: NotRequired[str]
    eventSource: NotRequired[str]
    awsRegion: NotRequired[str]
    dynamodb: NotRequired[StreamRecordTypeDef]
    userIdentity: NotRequired[IdentityTypeDef]

class StreamDescriptionTypeDef(TypedDict):
    StreamArn: NotRequired[str]
    StreamLabel: NotRequired[str]
    StreamStatus: NotRequired[StreamStatusType]
    StreamViewType: NotRequired[StreamViewTypeType]
    CreationRequestDateTime: NotRequired[datetime]
    TableName: NotRequired[str]
    KeySchema: NotRequired[List[KeySchemaElementTypeDef]]
    Shards: NotRequired[List[ShardTypeDef]]
    LastEvaluatedShardId: NotRequired[str]

class GetRecordsOutputTypeDef(TypedDict):
    Records: List[RecordTypeDef]
    NextShardIterator: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStreamOutputTypeDef(TypedDict):
    StreamDescription: StreamDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
