"""
Type annotations for dynamodbstreams service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_dynamodbstreams.client import DynamoDBStreamsClient

    session = Session()
    client: DynamoDBStreamsClient = session.client("dynamodbstreams")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    DescribeStreamInputTypeDef,
    DescribeStreamOutputTypeDef,
    GetRecordsInputTypeDef,
    GetRecordsOutputTypeDef,
    GetShardIteratorInputTypeDef,
    GetShardIteratorOutputTypeDef,
    ListStreamsInputTypeDef,
    ListStreamsOutputTypeDef,
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

__all__ = ("DynamoDBStreamsClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ExpiredIteratorException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TrimmedDataAccessException: Type[BotocoreClientError]

class DynamoDBStreamsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams.html#DynamoDBStreams.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DynamoDBStreamsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams.html#DynamoDBStreams.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client/#generate_presigned_url)
        """

    def describe_stream(
        self, **kwargs: Unpack[DescribeStreamInputTypeDef]
    ) -> DescribeStreamOutputTypeDef:
        """
        Returns information about a stream, including the current status of the stream,
        its Amazon Resource Name (ARN), the composition of its shards, and its
        corresponding DynamoDB table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams/client/describe_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client/#describe_stream)
        """

    def get_records(self, **kwargs: Unpack[GetRecordsInputTypeDef]) -> GetRecordsOutputTypeDef:
        """
        Retrieves the stream records from a given shard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams/client/get_records.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client/#get_records)
        """

    def get_shard_iterator(
        self, **kwargs: Unpack[GetShardIteratorInputTypeDef]
    ) -> GetShardIteratorOutputTypeDef:
        """
        Returns a shard iterator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams/client/get_shard_iterator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client/#get_shard_iterator)
        """

    def list_streams(self, **kwargs: Unpack[ListStreamsInputTypeDef]) -> ListStreamsOutputTypeDef:
        """
        Returns an array of stream ARNs associated with the current account and
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodbstreams/client/list_streams.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client/#list_streams)
        """
