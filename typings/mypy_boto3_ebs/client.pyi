"""
Type annotations for ebs service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ebs.client import EBSClient

    session = Session()
    client: EBSClient = session.client("ebs")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CompleteSnapshotRequestTypeDef,
    CompleteSnapshotResponseTypeDef,
    GetSnapshotBlockRequestTypeDef,
    GetSnapshotBlockResponseTypeDef,
    ListChangedBlocksRequestTypeDef,
    ListChangedBlocksResponseTypeDef,
    ListSnapshotBlocksRequestTypeDef,
    ListSnapshotBlocksResponseTypeDef,
    PutSnapshotBlockRequestTypeDef,
    PutSnapshotBlockResponseTypeDef,
    StartSnapshotRequestTypeDef,
    StartSnapshotResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("EBSClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentLimitExceededException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    RequestThrottledException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class EBSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html#EBS.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EBSClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs.html#EBS.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/client/#generate_presigned_url)
        """

    def complete_snapshot(
        self, **kwargs: Unpack[CompleteSnapshotRequestTypeDef]
    ) -> CompleteSnapshotResponseTypeDef:
        """
        Seals and completes the snapshot after all of the required blocks of data have
        been written to it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs/client/complete_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/client/#complete_snapshot)
        """

    def get_snapshot_block(
        self, **kwargs: Unpack[GetSnapshotBlockRequestTypeDef]
    ) -> GetSnapshotBlockResponseTypeDef:
        """
        Returns the data in a block in an Amazon Elastic Block Store snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs/client/get_snapshot_block.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/client/#get_snapshot_block)
        """

    def list_changed_blocks(
        self, **kwargs: Unpack[ListChangedBlocksRequestTypeDef]
    ) -> ListChangedBlocksResponseTypeDef:
        """
        Returns information about the blocks that are different between two Amazon
        Elastic Block Store snapshots of the same volume/snapshot lineage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs/client/list_changed_blocks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/client/#list_changed_blocks)
        """

    def list_snapshot_blocks(
        self, **kwargs: Unpack[ListSnapshotBlocksRequestTypeDef]
    ) -> ListSnapshotBlocksResponseTypeDef:
        """
        Returns information about the blocks in an Amazon Elastic Block Store snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs/client/list_snapshot_blocks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/client/#list_snapshot_blocks)
        """

    def put_snapshot_block(
        self, **kwargs: Unpack[PutSnapshotBlockRequestTypeDef]
    ) -> PutSnapshotBlockResponseTypeDef:
        """
        Writes a block of data to a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs/client/put_snapshot_block.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/client/#put_snapshot_block)
        """

    def start_snapshot(
        self, **kwargs: Unpack[StartSnapshotRequestTypeDef]
    ) -> StartSnapshotResponseTypeDef:
        """
        Creates a new Amazon EBS snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ebs/client/start_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/client/#start_snapshot)
        """
