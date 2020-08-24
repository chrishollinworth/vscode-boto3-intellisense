# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for dynamodbstreams service client

Usage::

    ```python
    import boto3
    from mypy_boto3_dynamodbstreams import DynamoDBStreamsClient

    client: DynamoDBStreamsClient = boto3.client("dynamodbstreams")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_dynamodbstreams.type_defs import (
    DescribeStreamOutputTypeDef,
    GetRecordsOutputTypeDef,
    GetShardIteratorOutputTypeDef,
    ListStreamsOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DynamoDBStreamsClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    ExpiredIteratorException: Type[Boto3ClientError]
    InternalServerError: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    TrimmedDataAccessException: Type[Boto3ClientError]


class DynamoDBStreamsClient:
    """
    [DynamoDBStreams.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodbstreams.html#DynamoDBStreams.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.can_paginate)
        """

    def describe_stream(
        self, StreamArn: str, Limit: int = None, ExclusiveStartShardId: str = None
    ) -> DescribeStreamOutputTypeDef:
        """
        [Client.describe_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.describe_stream)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.generate_presigned_url)
        """

    def get_records(self, ShardIterator: str, Limit: int = None) -> GetRecordsOutputTypeDef:
        """
        [Client.get_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.get_records)
        """

    def get_shard_iterator(
        self,
        StreamArn: str,
        ShardId: str,
        ShardIteratorType: Literal[
            "TRIM_HORIZON", "LATEST", "AT_SEQUENCE_NUMBER", "AFTER_SEQUENCE_NUMBER"
        ],
        SequenceNumber: str = None,
    ) -> GetShardIteratorOutputTypeDef:
        """
        [Client.get_shard_iterator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.get_shard_iterator)
        """

    def list_streams(
        self, TableName: str = None, Limit: int = None, ExclusiveStartStreamArn: str = None
    ) -> ListStreamsOutputTypeDef:
        """
        [Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dynamodbstreams.html#DynamoDBStreams.Client.list_streams)
        """
