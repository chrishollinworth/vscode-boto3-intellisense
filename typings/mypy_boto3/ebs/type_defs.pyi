"""
Type annotations for ebs service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_ebs.type_defs import BlobTypeDef

    data: BlobTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import SSETypeType, StatusType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "BlobTypeDef",
    "BlockTypeDef",
    "ChangedBlockTypeDef",
    "CompleteSnapshotRequestTypeDef",
    "CompleteSnapshotResponseTypeDef",
    "GetSnapshotBlockRequestTypeDef",
    "GetSnapshotBlockResponseTypeDef",
    "ListChangedBlocksRequestTypeDef",
    "ListChangedBlocksResponseTypeDef",
    "ListSnapshotBlocksRequestTypeDef",
    "ListSnapshotBlocksResponseTypeDef",
    "PutSnapshotBlockRequestTypeDef",
    "PutSnapshotBlockResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartSnapshotRequestTypeDef",
    "StartSnapshotResponseTypeDef",
    "TagTypeDef",
)

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class BlockTypeDef(TypedDict):
    BlockIndex: NotRequired[int]
    BlockToken: NotRequired[str]

class ChangedBlockTypeDef(TypedDict):
    BlockIndex: NotRequired[int]
    FirstBlockToken: NotRequired[str]
    SecondBlockToken: NotRequired[str]

class CompleteSnapshotRequestTypeDef(TypedDict):
    SnapshotId: str
    ChangedBlocksCount: int
    Checksum: NotRequired[str]
    ChecksumAlgorithm: NotRequired[Literal["SHA256"]]
    ChecksumAggregationMethod: NotRequired[Literal["LINEAR"]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetSnapshotBlockRequestTypeDef(TypedDict):
    SnapshotId: str
    BlockIndex: int
    BlockToken: str

class ListChangedBlocksRequestTypeDef(TypedDict):
    SecondSnapshotId: str
    FirstSnapshotId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    StartingBlockIndex: NotRequired[int]

class ListSnapshotBlocksRequestTypeDef(TypedDict):
    SnapshotId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    StartingBlockIndex: NotRequired[int]

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class PutSnapshotBlockRequestTypeDef(TypedDict):
    SnapshotId: str
    BlockIndex: int
    BlockData: BlobTypeDef
    DataLength: int
    Checksum: str
    ChecksumAlgorithm: Literal["SHA256"]
    Progress: NotRequired[int]

class CompleteSnapshotResponseTypeDef(TypedDict):
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetSnapshotBlockResponseTypeDef(TypedDict):
    DataLength: int
    BlockData: StreamingBody
    Checksum: str
    ChecksumAlgorithm: Literal["SHA256"]
    ResponseMetadata: ResponseMetadataTypeDef

class ListChangedBlocksResponseTypeDef(TypedDict):
    ChangedBlocks: List[ChangedBlockTypeDef]
    ExpiryTime: datetime
    VolumeSize: int
    BlockSize: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSnapshotBlocksResponseTypeDef(TypedDict):
    Blocks: List[BlockTypeDef]
    ExpiryTime: datetime
    VolumeSize: int
    BlockSize: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutSnapshotBlockResponseTypeDef(TypedDict):
    Checksum: str
    ChecksumAlgorithm: Literal["SHA256"]
    ResponseMetadata: ResponseMetadataTypeDef

class StartSnapshotRequestTypeDef(TypedDict):
    VolumeSize: int
    ParentSnapshotId: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    Description: NotRequired[str]
    ClientToken: NotRequired[str]
    Encrypted: NotRequired[bool]
    KmsKeyArn: NotRequired[str]
    Timeout: NotRequired[int]

class StartSnapshotResponseTypeDef(TypedDict):
    Description: str
    SnapshotId: str
    OwnerId: str
    Status: StatusType
    StartTime: datetime
    VolumeSize: int
    BlockSize: int
    Tags: List[TagTypeDef]
    ParentSnapshotId: str
    KmsKeyArn: str
    SseType: SSETypeType
    ResponseMetadata: ResponseMetadataTypeDef
