# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for kinesis service client

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesis import KinesisClient

    client: KinesisClient = boto3.client("kinesis")
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_kinesis.paginator import (
    DescribeStreamPaginator,
    ListShardsPaginator,
    ListStreamConsumersPaginator,
    ListStreamsPaginator,
)
from mypy_boto3_kinesis.type_defs import (
    DescribeLimitsOutputTypeDef,
    DescribeStreamConsumerOutputTypeDef,
    DescribeStreamOutputTypeDef,
    DescribeStreamSummaryOutputTypeDef,
    EnhancedMonitoringOutputTypeDef,
    GetRecordsOutputTypeDef,
    GetShardIteratorOutputTypeDef,
    ListShardsOutputTypeDef,
    ListStreamConsumersOutputTypeDef,
    ListStreamsOutputTypeDef,
    ListTagsForStreamOutputTypeDef,
    PutRecordOutputTypeDef,
    PutRecordsOutputTypeDef,
    PutRecordsRequestEntryTypeDef,
    RegisterStreamConsumerOutputTypeDef,
    ShardFilterTypeDef,
    StartingPositionTypeDef,
    SubscribeToShardOutputTypeDef,
    UpdateShardCountOutputTypeDef,
)
from mypy_boto3_kinesis.waiter import StreamExistsWaiter, StreamNotExistsWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KinesisClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    ExpiredIteratorException: Type[Boto3ClientError]
    ExpiredNextTokenException: Type[Boto3ClientError]
    InternalFailureException: Type[Boto3ClientError]
    InvalidArgumentException: Type[Boto3ClientError]
    KMSAccessDeniedException: Type[Boto3ClientError]
    KMSDisabledException: Type[Boto3ClientError]
    KMSInvalidStateException: Type[Boto3ClientError]
    KMSNotFoundException: Type[Boto3ClientError]
    KMSOptInRequired: Type[Boto3ClientError]
    KMSThrottlingException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ProvisionedThroughputExceededException: Type[Boto3ClientError]
    ResourceInUseException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]


class KinesisClient:
    """
    [Kinesis.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client)
    """

    exceptions: Exceptions

    def add_tags_to_stream(self, StreamName: str, Tags: Dict[str, str]) -> None:
        """
        [Client.add_tags_to_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.add_tags_to_stream)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.can_paginate)
        """

    def create_stream(self, StreamName: str, ShardCount: int) -> None:
        """
        [Client.create_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.create_stream)
        """

    def decrease_stream_retention_period(self, StreamName: str, RetentionPeriodHours: int) -> None:
        """
        [Client.decrease_stream_retention_period documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.decrease_stream_retention_period)
        """

    def delete_stream(self, StreamName: str, EnforceConsumerDeletion: bool = None) -> None:
        """
        [Client.delete_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.delete_stream)
        """

    def deregister_stream_consumer(
        self, StreamARN: str = None, ConsumerName: str = None, ConsumerARN: str = None
    ) -> None:
        """
        [Client.deregister_stream_consumer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.deregister_stream_consumer)
        """

    def describe_limits(self) -> DescribeLimitsOutputTypeDef:
        """
        [Client.describe_limits documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.describe_limits)
        """

    def describe_stream(
        self, StreamName: str, Limit: int = None, ExclusiveStartShardId: str = None
    ) -> DescribeStreamOutputTypeDef:
        """
        [Client.describe_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.describe_stream)
        """

    def describe_stream_consumer(
        self, StreamARN: str = None, ConsumerName: str = None, ConsumerARN: str = None
    ) -> DescribeStreamConsumerOutputTypeDef:
        """
        [Client.describe_stream_consumer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.describe_stream_consumer)
        """

    def describe_stream_summary(self, StreamName: str) -> DescribeStreamSummaryOutputTypeDef:
        """
        [Client.describe_stream_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.describe_stream_summary)
        """

    def disable_enhanced_monitoring(
        self,
        StreamName: str,
        ShardLevelMetrics: List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ],
    ) -> EnhancedMonitoringOutputTypeDef:
        """
        [Client.disable_enhanced_monitoring documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.disable_enhanced_monitoring)
        """

    def enable_enhanced_monitoring(
        self,
        StreamName: str,
        ShardLevelMetrics: List[
            Literal[
                "IncomingBytes",
                "IncomingRecords",
                "OutgoingBytes",
                "OutgoingRecords",
                "WriteProvisionedThroughputExceeded",
                "ReadProvisionedThroughputExceeded",
                "IteratorAgeMilliseconds",
                "ALL",
            ]
        ],
    ) -> EnhancedMonitoringOutputTypeDef:
        """
        [Client.enable_enhanced_monitoring documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.enable_enhanced_monitoring)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.generate_presigned_url)
        """

    def get_records(self, ShardIterator: str, Limit: int = None) -> GetRecordsOutputTypeDef:
        """
        [Client.get_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.get_records)
        """

    def get_shard_iterator(
        self,
        StreamName: str,
        ShardId: str,
        ShardIteratorType: Literal[
            "AT_SEQUENCE_NUMBER", "AFTER_SEQUENCE_NUMBER", "TRIM_HORIZON", "LATEST", "AT_TIMESTAMP"
        ],
        StartingSequenceNumber: str = None,
        Timestamp: datetime = None,
    ) -> GetShardIteratorOutputTypeDef:
        """
        [Client.get_shard_iterator documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.get_shard_iterator)
        """

    def increase_stream_retention_period(self, StreamName: str, RetentionPeriodHours: int) -> None:
        """
        [Client.increase_stream_retention_period documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.increase_stream_retention_period)
        """

    def list_shards(
        self,
        StreamName: str = None,
        NextToken: str = None,
        ExclusiveStartShardId: str = None,
        MaxResults: int = None,
        StreamCreationTimestamp: datetime = None,
        ShardFilter: ShardFilterTypeDef = None,
    ) -> ListShardsOutputTypeDef:
        """
        [Client.list_shards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.list_shards)
        """

    def list_stream_consumers(
        self,
        StreamARN: str,
        NextToken: str = None,
        MaxResults: int = None,
        StreamCreationTimestamp: datetime = None,
    ) -> ListStreamConsumersOutputTypeDef:
        """
        [Client.list_stream_consumers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.list_stream_consumers)
        """

    def list_streams(
        self, Limit: int = None, ExclusiveStartStreamName: str = None
    ) -> ListStreamsOutputTypeDef:
        """
        [Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.list_streams)
        """

    def list_tags_for_stream(
        self, StreamName: str, ExclusiveStartTagKey: str = None, Limit: int = None
    ) -> ListTagsForStreamOutputTypeDef:
        """
        [Client.list_tags_for_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.list_tags_for_stream)
        """

    def merge_shards(self, StreamName: str, ShardToMerge: str, AdjacentShardToMerge: str) -> None:
        """
        [Client.merge_shards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.merge_shards)
        """

    def put_record(
        self,
        StreamName: str,
        Data: Union[bytes, IO[bytes]],
        PartitionKey: str,
        ExplicitHashKey: str = None,
        SequenceNumberForOrdering: str = None,
    ) -> PutRecordOutputTypeDef:
        """
        [Client.put_record documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.put_record)
        """

    def put_records(
        self, Records: List[PutRecordsRequestEntryTypeDef], StreamName: str
    ) -> PutRecordsOutputTypeDef:
        """
        [Client.put_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.put_records)
        """

    def register_stream_consumer(
        self, StreamARN: str, ConsumerName: str
    ) -> RegisterStreamConsumerOutputTypeDef:
        """
        [Client.register_stream_consumer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.register_stream_consumer)
        """

    def remove_tags_from_stream(self, StreamName: str, TagKeys: List[str]) -> None:
        """
        [Client.remove_tags_from_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.remove_tags_from_stream)
        """

    def split_shard(self, StreamName: str, ShardToSplit: str, NewStartingHashKey: str) -> None:
        """
        [Client.split_shard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.split_shard)
        """

    def start_stream_encryption(
        self, StreamName: str, EncryptionType: Literal["NONE", "KMS"], KeyId: str
    ) -> None:
        """
        [Client.start_stream_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.start_stream_encryption)
        """

    def stop_stream_encryption(
        self, StreamName: str, EncryptionType: Literal["NONE", "KMS"], KeyId: str
    ) -> None:
        """
        [Client.stop_stream_encryption documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.stop_stream_encryption)
        """

    def subscribe_to_shard(
        self, ConsumerARN: str, ShardId: str, StartingPosition: StartingPositionTypeDef
    ) -> SubscribeToShardOutputTypeDef:
        """
        [Client.subscribe_to_shard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.subscribe_to_shard)
        """

    def update_shard_count(
        self, StreamName: str, TargetShardCount: int, ScalingType: Literal["UNIFORM_SCALING"]
    ) -> UpdateShardCountOutputTypeDef:
        """
        [Client.update_shard_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Client.update_shard_count)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_stream"]) -> DescribeStreamPaginator:
        """
        [Paginator.DescribeStream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Paginator.DescribeStream)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_shards"]) -> ListShardsPaginator:
        """
        [Paginator.ListShards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Paginator.ListShards)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_stream_consumers"]
    ) -> ListStreamConsumersPaginator:
        """
        [Paginator.ListStreamConsumers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Paginator.ListStreamConsumers)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_streams"]) -> ListStreamsPaginator:
        """
        [Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Paginator.ListStreams)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass

    @overload
    def get_waiter(self, waiter_name: Literal["stream_exists"]) -> StreamExistsWaiter:
        """
        [Waiter.StreamExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Waiter.StreamExists)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["stream_not_exists"]) -> StreamNotExistsWaiter:
        """
        [Waiter.StreamNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis.html#Kinesis.Waiter.StreamNotExists)
        """

    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        pass
