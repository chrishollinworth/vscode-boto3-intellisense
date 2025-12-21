"""
Type annotations for keyspacesstreams service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_keyspacesstreams.client import KeyspacesStreamsClient

    session = Session()
    client: KeyspacesStreamsClient = session.client("keyspacesstreams")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import GetStreamPaginator, ListStreamsPaginator
from .type_defs import (
    GetRecordsInputTypeDef,
    GetRecordsOutputTypeDef,
    GetShardIteratorInputTypeDef,
    GetShardIteratorOutputTypeDef,
    GetStreamInputTypeDef,
    GetStreamOutputTypeDef,
    ListStreamsInputTypeDef,
    ListStreamsOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("KeyspacesStreamsClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class KeyspacesStreamsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspacesstreams.html#KeyspacesStreams.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KeyspacesStreamsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspacesstreams.html#KeyspacesStreams.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspacesstreams/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspacesstreams/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/client/#generate_presigned_url)
        """

    def get_records(self, **kwargs: Unpack[GetRecordsInputTypeDef]) -> GetRecordsOutputTypeDef:
        """
        Retrieves data records from a specified shard in an Amazon Keyspaces data
        stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspacesstreams/client/get_records.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/client/#get_records)
        """

    def get_shard_iterator(
        self, **kwargs: Unpack[GetShardIteratorInputTypeDef]
    ) -> GetShardIteratorOutputTypeDef:
        """
        Returns a shard iterator that serves as a bookmark for reading data from a
        specific position in an Amazon Keyspaces data stream's shard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspacesstreams/client/get_shard_iterator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/client/#get_shard_iterator)
        """

    def get_stream(self, **kwargs: Unpack[GetStreamInputTypeDef]) -> GetStreamOutputTypeDef:
        """
        Returns detailed information about a specific data capture stream for an Amazon
        Keyspaces table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspacesstreams/client/get_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/client/#get_stream)
        """

    def list_streams(self, **kwargs: Unpack[ListStreamsInputTypeDef]) -> ListStreamsOutputTypeDef:
        """
        Returns a list of all data capture streams associated with your Amazon
        Keyspaces account or for a specific keyspace or table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspacesstreams/client/list_streams.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/client/#list_streams)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_stream"]
    ) -> GetStreamPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspacesstreams/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_streams"]
    ) -> ListStreamsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/keyspacesstreams/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/client/#get_paginator)
        """
