"""
Type annotations for backupstorage service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_backupstorage import BackupStorageClient

    client: BackupStorageClient = boto3.client("backupstorage")
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, Type, Union

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .type_defs import (
    GetChunkOutputTypeDef,
    GetObjectMetadataOutputTypeDef,
    ListChunksOutputTypeDef,
    ListObjectsOutputTypeDef,
    NotifyObjectCompleteOutputTypeDef,
    PutChunkOutputTypeDef,
    PutObjectOutputTypeDef,
    StartObjectOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("BackupStorageClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DataAlreadyExistsException: Type[BotocoreClientError]
    IllegalArgumentException: Type[BotocoreClientError]
    KMSInvalidKeyUsageException: Type[BotocoreClientError]
    NotReadableInputStreamException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    RetryableException: Type[BotocoreClientError]
    ServiceInternalException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class BackupStorageClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/backupstorage.html#BackupStorage.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BackupStorageClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/backupstorage.html#BackupStorage.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/backupstorage.html#BackupStorage.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/client.html#close)
        """
    def delete_object(self, *, BackupJobId: str, ObjectName: str) -> None:
        """
        Delete Object from the incremental base Backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/backupstorage.html#BackupStorage.Client.delete_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/client.html#delete_object)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/backupstorage.html#BackupStorage.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/client.html#generate_presigned_url)
        """
    def get_chunk(self, *, StorageJobId: str, ChunkToken: str) -> GetChunkOutputTypeDef:
        """
        Gets the specified object's chunk.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/backupstorage.html#BackupStorage.Client.get_chunk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/client.html#get_chunk)
        """
    def get_object_metadata(
        self, *, StorageJobId: str, ObjectToken: str
    ) -> GetObjectMetadataOutputTypeDef:
        """
        Get metadata associated with an Object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/backupstorage.html#BackupStorage.Client.get_object_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/client.html#get_object_metadata)
        """
    def list_chunks(
        self, *, StorageJobId: str, ObjectToken: str, MaxResults: int = None, NextToken: str = None
    ) -> ListChunksOutputTypeDef:
        """
        List chunks in a given Object See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/backupstorage-2018-04-10/ListChunks>`_
        **Request Syntax** response = client.list_chunks( StorageJobId='string',
        ObjectToken='string', MaxResults=123, NextToken=...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/backupstorage.html#BackupStorage.Client.list_chunks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/client.html#list_chunks)
        """
    def list_objects(
        self,
        *,
        StorageJobId: str,
        StartingObjectName: str = None,
        StartingObjectPrefix: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        CreatedBefore: Union[datetime, str] = None,
        CreatedAfter: Union[datetime, str] = None
    ) -> ListObjectsOutputTypeDef:
        """
        List all Objects in a given Backup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/backupstorage.html#BackupStorage.Client.list_objects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/client.html#list_objects)
        """
    def notify_object_complete(
        self,
        *,
        BackupJobId: str,
        UploadId: str,
        ObjectChecksum: str,
        ObjectChecksumAlgorithm: Literal["SUMMARY"],
        MetadataString: str = None,
        MetadataBlob: Union[bytes, IO[bytes], StreamingBody] = None,
        MetadataBlobLength: int = None,
        MetadataBlobChecksum: str = None,
        MetadataBlobChecksumAlgorithm: Literal["SHA256"] = None
    ) -> NotifyObjectCompleteOutputTypeDef:
        """
        Complete upload See also: `AWS API Documentation <https://docs.aws.amazon.com/go
        to/WebAPI/backupstorage-2018-04-10/NotifyObjectComplete>`_ **Request Syntax**
        response = client.notify_object_complete( BackupJobId='string',
        UploadId='string', ObjectChecksum='string', ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/backupstorage.html#BackupStorage.Client.notify_object_complete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/client.html#notify_object_complete)
        """
    def put_chunk(
        self,
        *,
        BackupJobId: str,
        UploadId: str,
        ChunkIndex: int,
        Data: Union[bytes, IO[bytes], StreamingBody],
        Length: int,
        Checksum: str,
        ChecksumAlgorithm: Literal["SHA256"]
    ) -> PutChunkOutputTypeDef:
        """
        Upload chunk.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/backupstorage.html#BackupStorage.Client.put_chunk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/client.html#put_chunk)
        """
    def put_object(
        self,
        *,
        BackupJobId: str,
        ObjectName: str,
        MetadataString: str = None,
        InlineChunk: Union[bytes, IO[bytes], StreamingBody] = None,
        InlineChunkLength: int = None,
        InlineChunkChecksum: str = None,
        InlineChunkChecksumAlgorithm: str = None,
        ObjectChecksum: str = None,
        ObjectChecksumAlgorithm: Literal["SUMMARY"] = None,
        ThrowOnDuplicate: bool = None
    ) -> PutObjectOutputTypeDef:
        """
        Upload object that can store object metadata String and data blob in single API
        call using inline chunk field.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/backupstorage.html#BackupStorage.Client.put_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/client.html#put_object)
        """
    def start_object(
        self, *, BackupJobId: str, ObjectName: str, ThrowOnDuplicate: bool = None
    ) -> StartObjectOutputTypeDef:
        """
        Start upload containing one or many chunks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/backupstorage.html#BackupStorage.Client.start_object)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_backupstorage/client.html#start_object)
        """
