"""
Type annotations for backupstorage service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/type_defs.html)

Usage::

    ```python
    from mypy_boto3_backupstorage.type_defs import BackupObjectTypeDef

    data: BackupObjectTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BackupObjectTypeDef",
    "ChunkTypeDef",
    "DeleteObjectInputRequestTypeDef",
    "GetChunkInputRequestTypeDef",
    "GetChunkOutputTypeDef",
    "GetObjectMetadataInputRequestTypeDef",
    "GetObjectMetadataOutputTypeDef",
    "ListChunksInputRequestTypeDef",
    "ListChunksOutputTypeDef",
    "ListObjectsInputRequestTypeDef",
    "ListObjectsOutputTypeDef",
    "NotifyObjectCompleteInputRequestTypeDef",
    "NotifyObjectCompleteOutputTypeDef",
    "PutChunkInputRequestTypeDef",
    "PutChunkOutputTypeDef",
    "PutObjectInputRequestTypeDef",
    "PutObjectOutputTypeDef",
    "ResponseMetadataTypeDef",
    "StartObjectInputRequestTypeDef",
    "StartObjectOutputTypeDef",
)

_RequiredBackupObjectTypeDef = TypedDict(
    "_RequiredBackupObjectTypeDef",
    {
        "Name": str,
        "ObjectChecksum": str,
        "ObjectChecksumAlgorithm": Literal["SUMMARY"],
        "ObjectToken": str,
    },
)
_OptionalBackupObjectTypeDef = TypedDict(
    "_OptionalBackupObjectTypeDef",
    {
        "ChunksCount": int,
        "MetadataString": str,
    },
    total=False,
)

class BackupObjectTypeDef(_RequiredBackupObjectTypeDef, _OptionalBackupObjectTypeDef):
    pass

ChunkTypeDef = TypedDict(
    "ChunkTypeDef",
    {
        "Index": int,
        "Length": int,
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
        "ChunkToken": str,
    },
)

DeleteObjectInputRequestTypeDef = TypedDict(
    "DeleteObjectInputRequestTypeDef",
    {
        "BackupJobId": str,
        "ObjectName": str,
    },
)

GetChunkInputRequestTypeDef = TypedDict(
    "GetChunkInputRequestTypeDef",
    {
        "StorageJobId": str,
        "ChunkToken": str,
    },
)

GetChunkOutputTypeDef = TypedDict(
    "GetChunkOutputTypeDef",
    {
        "Data": StreamingBody,
        "Length": int,
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectMetadataInputRequestTypeDef = TypedDict(
    "GetObjectMetadataInputRequestTypeDef",
    {
        "StorageJobId": str,
        "ObjectToken": str,
    },
)

GetObjectMetadataOutputTypeDef = TypedDict(
    "GetObjectMetadataOutputTypeDef",
    {
        "MetadataString": str,
        "MetadataBlob": StreamingBody,
        "MetadataBlobLength": int,
        "MetadataBlobChecksum": str,
        "MetadataBlobChecksumAlgorithm": Literal["SHA256"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChunksInputRequestTypeDef = TypedDict(
    "_RequiredListChunksInputRequestTypeDef",
    {
        "StorageJobId": str,
        "ObjectToken": str,
    },
)
_OptionalListChunksInputRequestTypeDef = TypedDict(
    "_OptionalListChunksInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListChunksInputRequestTypeDef(
    _RequiredListChunksInputRequestTypeDef, _OptionalListChunksInputRequestTypeDef
):
    pass

ListChunksOutputTypeDef = TypedDict(
    "ListChunksOutputTypeDef",
    {
        "ChunkList": List["ChunkTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListObjectsInputRequestTypeDef = TypedDict(
    "_RequiredListObjectsInputRequestTypeDef",
    {
        "StorageJobId": str,
    },
)
_OptionalListObjectsInputRequestTypeDef = TypedDict(
    "_OptionalListObjectsInputRequestTypeDef",
    {
        "StartingObjectName": str,
        "StartingObjectPrefix": str,
        "MaxResults": int,
        "NextToken": str,
        "CreatedBefore": Union[datetime, str],
        "CreatedAfter": Union[datetime, str],
    },
    total=False,
)

class ListObjectsInputRequestTypeDef(
    _RequiredListObjectsInputRequestTypeDef, _OptionalListObjectsInputRequestTypeDef
):
    pass

ListObjectsOutputTypeDef = TypedDict(
    "ListObjectsOutputTypeDef",
    {
        "ObjectList": List["BackupObjectTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredNotifyObjectCompleteInputRequestTypeDef = TypedDict(
    "_RequiredNotifyObjectCompleteInputRequestTypeDef",
    {
        "BackupJobId": str,
        "UploadId": str,
        "ObjectChecksum": str,
        "ObjectChecksumAlgorithm": Literal["SUMMARY"],
    },
)
_OptionalNotifyObjectCompleteInputRequestTypeDef = TypedDict(
    "_OptionalNotifyObjectCompleteInputRequestTypeDef",
    {
        "MetadataString": str,
        "MetadataBlob": Union[bytes, IO[bytes], StreamingBody],
        "MetadataBlobLength": int,
        "MetadataBlobChecksum": str,
        "MetadataBlobChecksumAlgorithm": Literal["SHA256"],
    },
    total=False,
)

class NotifyObjectCompleteInputRequestTypeDef(
    _RequiredNotifyObjectCompleteInputRequestTypeDef,
    _OptionalNotifyObjectCompleteInputRequestTypeDef,
):
    pass

NotifyObjectCompleteOutputTypeDef = TypedDict(
    "NotifyObjectCompleteOutputTypeDef",
    {
        "ObjectChecksum": str,
        "ObjectChecksumAlgorithm": Literal["SUMMARY"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutChunkInputRequestTypeDef = TypedDict(
    "PutChunkInputRequestTypeDef",
    {
        "BackupJobId": str,
        "UploadId": str,
        "ChunkIndex": int,
        "Data": Union[bytes, IO[bytes], StreamingBody],
        "Length": int,
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
    },
)

PutChunkOutputTypeDef = TypedDict(
    "PutChunkOutputTypeDef",
    {
        "ChunkChecksum": str,
        "ChunkChecksumAlgorithm": Literal["SHA256"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutObjectInputRequestTypeDef = TypedDict(
    "_RequiredPutObjectInputRequestTypeDef",
    {
        "BackupJobId": str,
        "ObjectName": str,
    },
)
_OptionalPutObjectInputRequestTypeDef = TypedDict(
    "_OptionalPutObjectInputRequestTypeDef",
    {
        "MetadataString": str,
        "InlineChunk": Union[bytes, IO[bytes], StreamingBody],
        "InlineChunkLength": int,
        "InlineChunkChecksum": str,
        "InlineChunkChecksumAlgorithm": str,
        "ObjectChecksum": str,
        "ObjectChecksumAlgorithm": Literal["SUMMARY"],
        "ThrowOnDuplicate": bool,
    },
    total=False,
)

class PutObjectInputRequestTypeDef(
    _RequiredPutObjectInputRequestTypeDef, _OptionalPutObjectInputRequestTypeDef
):
    pass

PutObjectOutputTypeDef = TypedDict(
    "PutObjectOutputTypeDef",
    {
        "InlineChunkChecksum": str,
        "InlineChunkChecksumAlgorithm": Literal["SHA256"],
        "ObjectChecksum": str,
        "ObjectChecksumAlgorithm": Literal["SUMMARY"],
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

_RequiredStartObjectInputRequestTypeDef = TypedDict(
    "_RequiredStartObjectInputRequestTypeDef",
    {
        "BackupJobId": str,
        "ObjectName": str,
    },
)
_OptionalStartObjectInputRequestTypeDef = TypedDict(
    "_OptionalStartObjectInputRequestTypeDef",
    {
        "ThrowOnDuplicate": bool,
    },
    total=False,
)

class StartObjectInputRequestTypeDef(
    _RequiredStartObjectInputRequestTypeDef, _OptionalStartObjectInputRequestTypeDef
):
    pass

StartObjectOutputTypeDef = TypedDict(
    "StartObjectOutputTypeDef",
    {
        "UploadId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
