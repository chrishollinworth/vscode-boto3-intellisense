"""
Type annotations for dynamodbstreams service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_dynamodbstreams import DynamoDBStreamsClient

    client: DynamoDBStreamsClient = boto3.client("dynamodbstreams")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .literals import ShardIteratorTypeType
from .type_defs import (
    DescribeStreamOutputTypeDef,
    GetRecordsOutputTypeDef,
    GetShardIteratorOutputTypeDef,
    ListStreamsOutputTypeDef,
)

__all__ = ("DynamoDBStreamsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ExpiredIteratorException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TrimmedDataAccessException: Type[BotocoreClientError]

class DynamoDBStreamsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dynamodbstreams.html#DynamoDBStreams.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        DynamoDBStreamsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client.html#can_paginate)
        """
    def describe_stream(
        self, *, StreamArn: str, Limit: int = None, ExclusiveStartShardId: str = None
    ) -> DescribeStreamOutputTypeDef:
        """
        Returns information about a stream, including the current status of the stream,
        its Amazon Resource Name (ARN), the composition of its shards, and its
        corresponding DynamoDB table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.describe_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client.html#describe_stream)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client.html#generate_presigned_url)
        """
    def get_records(self, *, ShardIterator: str, Limit: int = None) -> GetRecordsOutputTypeDef:
        """
        Retrieves the stream records from a given shard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.get_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client.html#get_records)
        """
    def get_shard_iterator(
        self,
        *,
        StreamArn: str,
        ShardId: str,
        ShardIteratorType: ShardIteratorTypeType,
        SequenceNumber: str = None
    ) -> GetShardIteratorOutputTypeDef:
        """
        Returns a shard iterator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.get_shard_iterator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client.html#get_shard_iterator)
        """
    def list_streams(
        self, *, TableName: str = None, Limit: int = None, ExclusiveStartStreamArn: str = None
    ) -> ListStreamsOutputTypeDef:
        """
        Returns an array of stream ARNs associated with the current account and
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.list_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/client.html#list_streams)
        """
