# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for ebs service client

Usage::

    ```python
    import boto3
    from mypy_boto3_ebs import EBSClient

    client: EBSClient = boto3.client("ebs")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import ClientMeta

from mypy_boto3_ebs.type_defs import (
    CompleteSnapshotResponseTypeDef,
    GetSnapshotBlockResponseTypeDef,
    ListChangedBlocksResponseTypeDef,
    ListSnapshotBlocksResponseTypeDef,
    PutSnapshotBlockResponseTypeDef,
    StartSnapshotResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EBSClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentLimitExceededException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    RequestThrottledException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class EBSClient:
    """
    [EBS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ebs.html#EBS.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ebs.html#EBS.Client.can_paginate)
        """

    def complete_snapshot(
        self,
        SnapshotId: str,
        ChangedBlocksCount: int,
        Checksum: str = None,
        ChecksumAlgorithm: Literal["SHA256"] = None,
        ChecksumAggregationMethod: Literal["LINEAR"] = None,
    ) -> CompleteSnapshotResponseTypeDef:
        """
        [Client.complete_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ebs.html#EBS.Client.complete_snapshot)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ebs.html#EBS.Client.generate_presigned_url)
        """

    def get_snapshot_block(
        self, SnapshotId: str, BlockIndex: int, BlockToken: str
    ) -> GetSnapshotBlockResponseTypeDef:
        """
        [Client.get_snapshot_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ebs.html#EBS.Client.get_snapshot_block)
        """

    def list_changed_blocks(
        self,
        SecondSnapshotId: str,
        FirstSnapshotId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        StartingBlockIndex: int = None,
    ) -> ListChangedBlocksResponseTypeDef:
        """
        [Client.list_changed_blocks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ebs.html#EBS.Client.list_changed_blocks)
        """

    def list_snapshot_blocks(
        self,
        SnapshotId: str,
        NextToken: str = None,
        MaxResults: int = None,
        StartingBlockIndex: int = None,
    ) -> ListSnapshotBlocksResponseTypeDef:
        """
        [Client.list_snapshot_blocks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ebs.html#EBS.Client.list_snapshot_blocks)
        """

    def put_snapshot_block(
        self,
        SnapshotId: str,
        BlockIndex: int,
        BlockData: Union[bytes, IO[bytes]],
        DataLength: int,
        Checksum: str,
        ChecksumAlgorithm: Literal["SHA256"],
        Progress: int = None,
    ) -> PutSnapshotBlockResponseTypeDef:
        """
        [Client.put_snapshot_block documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ebs.html#EBS.Client.put_snapshot_block)
        """

    def start_snapshot(
        self,
        VolumeSize: int,
        ParentSnapshotId: str = None,
        Tags: List["TagTypeDef"] = None,
        Description: str = None,
        ClientToken: str = None,
        Encrypted: bool = None,
        KmsKeyArn: str = None,
        Timeout: int = None,
    ) -> StartSnapshotResponseTypeDef:
        """
        [Client.start_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ebs.html#EBS.Client.start_snapshot)
        """
