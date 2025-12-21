"""
Type annotations for keyspacesstreams service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_keyspacesstreams.type_defs import GetRecordsInputTypeDef

    data: GetRecordsInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any

from .literals import OriginTypeType, ShardIteratorTypeType, StreamStatusType, StreamViewTypeType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
else:
    from typing import Dict, List
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "GetRecordsInputTypeDef",
    "GetRecordsOutputTypeDef",
    "GetShardIteratorInputTypeDef",
    "GetShardIteratorOutputTypeDef",
    "GetStreamInputPaginateTypeDef",
    "GetStreamInputTypeDef",
    "GetStreamOutputTypeDef",
    "KeyspacesCellMapDefinitionTypeDef",
    "KeyspacesCellTypeDef",
    "KeyspacesCellValueTypeDef",
    "KeyspacesMetadataTypeDef",
    "KeyspacesRowTypeDef",
    "ListStreamsInputPaginateTypeDef",
    "ListStreamsInputTypeDef",
    "ListStreamsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "RecordTypeDef",
    "ResponseMetadataTypeDef",
    "SequenceNumberRangeTypeDef",
    "ShardFilterTypeDef",
    "ShardTypeDef",
    "StreamTypeDef",
)

class GetRecordsInputTypeDef(TypedDict):
    shardIterator: str
    maxResults: NotRequired[int]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetShardIteratorInputTypeDef(TypedDict):
    streamArn: str
    shardId: str
    shardIteratorType: ShardIteratorTypeType
    sequenceNumber: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

ShardFilterTypeDef = TypedDict(
    "ShardFilterTypeDef",
    {
        "type": NotRequired[Literal["CHILD_SHARDS"]],
        "shardId": NotRequired[str],
    },
)

class KeyspacesMetadataTypeDef(TypedDict):
    expirationTime: NotRequired[str]
    writeTime: NotRequired[str]

class ListStreamsInputTypeDef(TypedDict):
    keyspaceName: NotRequired[str]
    tableName: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class StreamTypeDef(TypedDict):
    streamArn: str
    keyspaceName: str
    tableName: str
    streamLabel: str

class SequenceNumberRangeTypeDef(TypedDict):
    startingSequenceNumber: NotRequired[str]
    endingSequenceNumber: NotRequired[str]

class GetShardIteratorOutputTypeDef(TypedDict):
    shardIterator: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamsInputPaginateTypeDef(TypedDict):
    keyspaceName: NotRequired[str]
    tableName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetStreamInputPaginateTypeDef(TypedDict):
    streamArn: str
    shardFilter: NotRequired[ShardFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetStreamInputTypeDef(TypedDict):
    streamArn: str
    maxResults: NotRequired[int]
    shardFilter: NotRequired[ShardFilterTypeDef]
    nextToken: NotRequired[str]

class KeyspacesCellMapDefinitionTypeDef(TypedDict):
    key: NotRequired[Dict[str, Any]]
    value: NotRequired[Dict[str, Any]]
    metadata: NotRequired[KeyspacesMetadataTypeDef]

class KeyspacesCellTypeDef(TypedDict):
    value: NotRequired[Dict[str, Any]]
    metadata: NotRequired[KeyspacesMetadataTypeDef]

class ListStreamsOutputTypeDef(TypedDict):
    streams: List[StreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ShardTypeDef(TypedDict):
    shardId: NotRequired[str]
    sequenceNumberRange: NotRequired[SequenceNumberRangeTypeDef]
    parentShardIds: NotRequired[List[str]]

class KeyspacesCellValueTypeDef(TypedDict):
    asciiT: NotRequired[str]
    bigintT: NotRequired[str]
    blobT: NotRequired[bytes]
    boolT: NotRequired[bool]
    counterT: NotRequired[str]
    dateT: NotRequired[str]
    decimalT: NotRequired[str]
    doubleT: NotRequired[str]
    floatT: NotRequired[str]
    inetT: NotRequired[str]
    intT: NotRequired[str]
    listT: NotRequired[List[KeyspacesCellTypeDef]]
    mapT: NotRequired[List[KeyspacesCellMapDefinitionTypeDef]]
    setT: NotRequired[List[KeyspacesCellTypeDef]]
    smallintT: NotRequired[str]
    textT: NotRequired[str]
    timeT: NotRequired[str]
    timestampT: NotRequired[str]
    timeuuidT: NotRequired[str]
    tinyintT: NotRequired[str]
    tupleT: NotRequired[List[KeyspacesCellTypeDef]]
    uuidT: NotRequired[str]
    varcharT: NotRequired[str]
    varintT: NotRequired[str]
    udtT: NotRequired[Dict[str, KeyspacesCellTypeDef]]

class KeyspacesRowTypeDef(TypedDict):
    valueCells: NotRequired[Dict[str, KeyspacesCellTypeDef]]
    staticCells: NotRequired[Dict[str, KeyspacesCellTypeDef]]
    rowMetadata: NotRequired[KeyspacesMetadataTypeDef]

class GetStreamOutputTypeDef(TypedDict):
    streamArn: str
    streamLabel: str
    streamStatus: StreamStatusType
    streamViewType: StreamViewTypeType
    creationRequestDateTime: datetime
    keyspaceName: str
    tableName: str
    shards: List[ShardTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RecordTypeDef(TypedDict):
    eventVersion: NotRequired[str]
    createdAt: NotRequired[datetime]
    origin: NotRequired[OriginTypeType]
    partitionKeys: NotRequired[Dict[str, KeyspacesCellValueTypeDef]]
    clusteringKeys: NotRequired[Dict[str, KeyspacesCellValueTypeDef]]
    newImage: NotRequired[KeyspacesRowTypeDef]
    oldImage: NotRequired[KeyspacesRowTypeDef]
    sequenceNumber: NotRequired[str]

class GetRecordsOutputTypeDef(TypedDict):
    changeRecords: List[RecordTypeDef]
    nextShardIterator: str
    ResponseMetadata: ResponseMetadataTypeDef
