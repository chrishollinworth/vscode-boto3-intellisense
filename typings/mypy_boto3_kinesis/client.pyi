"""
Type annotations for kinesis service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html)

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

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import EncryptionTypeType, MetricsNameType, ShardIteratorTypeType
from .paginator import (
    DescribeStreamPaginator,
    ListShardsPaginator,
    ListStreamConsumersPaginator,
    ListStreamsPaginator,
)
from .type_defs import (
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
from .waiter import StreamExistsWaiter, StreamNotExistsWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("KinesisClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ExpiredIteratorException: Type[BotocoreClientError]
    ExpiredNextTokenException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    KMSAccessDeniedException: Type[BotocoreClientError]
    KMSDisabledException: Type[BotocoreClientError]
    KMSInvalidStateException: Type[BotocoreClientError]
    KMSNotFoundException: Type[BotocoreClientError]
    KMSOptInRequired: Type[BotocoreClientError]
    KMSThrottlingException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ProvisionedThroughputExceededException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class KinesisClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        KinesisClient exceptions.
        """
    def add_tags_to_stream(self, *, StreamName: str, Tags: Dict[str, str]) -> None:
        """
        Adds or updates tags for the specified Kinesis data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.add_tags_to_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#add_tags_to_stream)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#can_paginate)
        """
    def create_stream(self, *, StreamName: str, ShardCount: int) -> None:
        """
        Creates a Kinesis data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.create_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#create_stream)
        """
    def decrease_stream_retention_period(
        self, *, StreamName: str, RetentionPeriodHours: int
    ) -> None:
        """
        Decreases the Kinesis data stream's retention period, which is the length of
        time data records are accessible after they are added to the stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.decrease_stream_retention_period)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#decrease_stream_retention_period)
        """
    def delete_stream(self, *, StreamName: str, EnforceConsumerDeletion: bool = None) -> None:
        """
        Deletes a Kinesis data stream and all its shards and data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.delete_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#delete_stream)
        """
    def deregister_stream_consumer(
        self, *, StreamARN: str = None, ConsumerName: str = None, ConsumerARN: str = None
    ) -> None:
        """
        To deregister a consumer, provide its ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.deregister_stream_consumer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#deregister_stream_consumer)
        """
    def describe_limits(self) -> DescribeLimitsOutputTypeDef:
        """
        Describes the shard limits and usage for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.describe_limits)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#describe_limits)
        """
    def describe_stream(
        self, *, StreamName: str, Limit: int = None, ExclusiveStartShardId: str = None
    ) -> DescribeStreamOutputTypeDef:
        """
        Describes the specified Kinesis data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.describe_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#describe_stream)
        """
    def describe_stream_consumer(
        self, *, StreamARN: str = None, ConsumerName: str = None, ConsumerARN: str = None
    ) -> DescribeStreamConsumerOutputTypeDef:
        """
        To get the description of a registered consumer, provide the ARN of the
        consumer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.describe_stream_consumer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#describe_stream_consumer)
        """
    def describe_stream_summary(self, *, StreamName: str) -> DescribeStreamSummaryOutputTypeDef:
        """
        Provides a summarized description of the specified Kinesis data stream without
        the shard list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.describe_stream_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#describe_stream_summary)
        """
    def disable_enhanced_monitoring(
        self, *, StreamName: str, ShardLevelMetrics: List[MetricsNameType]
    ) -> EnhancedMonitoringOutputTypeDef:
        """
        Disables enhanced monitoring.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.disable_enhanced_monitoring)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#disable_enhanced_monitoring)
        """
    def enable_enhanced_monitoring(
        self, *, StreamName: str, ShardLevelMetrics: List[MetricsNameType]
    ) -> EnhancedMonitoringOutputTypeDef:
        """
        Enables enhanced Kinesis data stream monitoring for shard-level metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.enable_enhanced_monitoring)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#enable_enhanced_monitoring)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#generate_presigned_url)
        """
    def get_records(self, *, ShardIterator: str, Limit: int = None) -> GetRecordsOutputTypeDef:
        """
        Gets data records from a Kinesis data stream's shard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.get_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#get_records)
        """
    def get_shard_iterator(
        self,
        *,
        StreamName: str,
        ShardId: str,
        ShardIteratorType: ShardIteratorTypeType,
        StartingSequenceNumber: str = None,
        Timestamp: Union[datetime, str] = None
    ) -> GetShardIteratorOutputTypeDef:
        """
        Gets an Amazon Kinesis shard iterator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.get_shard_iterator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#get_shard_iterator)
        """
    def increase_stream_retention_period(
        self, *, StreamName: str, RetentionPeriodHours: int
    ) -> None:
        """
        Increases the Kinesis data stream's retention period, which is the length of
        time data records are accessible after they are added to the stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.increase_stream_retention_period)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#increase_stream_retention_period)
        """
    def list_shards(
        self,
        *,
        StreamName: str = None,
        NextToken: str = None,
        ExclusiveStartShardId: str = None,
        MaxResults: int = None,
        StreamCreationTimestamp: Union[datetime, str] = None,
        ShardFilter: "ShardFilterTypeDef" = None
    ) -> ListShardsOutputTypeDef:
        """
        Lists the shards in a stream and provides information about each shard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.list_shards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#list_shards)
        """
    def list_stream_consumers(
        self,
        *,
        StreamARN: str,
        NextToken: str = None,
        MaxResults: int = None,
        StreamCreationTimestamp: Union[datetime, str] = None
    ) -> ListStreamConsumersOutputTypeDef:
        """
        Lists the consumers registered to receive data from a stream using enhanced fan-
        out, and provides information about each consumer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.list_stream_consumers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#list_stream_consumers)
        """
    def list_streams(
        self, *, Limit: int = None, ExclusiveStartStreamName: str = None
    ) -> ListStreamsOutputTypeDef:
        """
        Lists your Kinesis data streams.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.list_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#list_streams)
        """
    def list_tags_for_stream(
        self, *, StreamName: str, ExclusiveStartTagKey: str = None, Limit: int = None
    ) -> ListTagsForStreamOutputTypeDef:
        """
        Lists the tags for the specified Kinesis data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.list_tags_for_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#list_tags_for_stream)
        """
    def merge_shards(
        self, *, StreamName: str, ShardToMerge: str, AdjacentShardToMerge: str
    ) -> None:
        """
        Merges two adjacent shards in a Kinesis data stream and combines them into a
        single shard to reduce the stream's capacity to ingest and transport data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.merge_shards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#merge_shards)
        """
    def put_record(
        self,
        *,
        StreamName: str,
        Data: Union[bytes, IO[bytes], StreamingBody],
        PartitionKey: str,
        ExplicitHashKey: str = None,
        SequenceNumberForOrdering: str = None
    ) -> PutRecordOutputTypeDef:
        """
        Writes a single data record into an Amazon Kinesis data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.put_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#put_record)
        """
    def put_records(
        self, *, Records: List["PutRecordsRequestEntryTypeDef"], StreamName: str
    ) -> PutRecordsOutputTypeDef:
        """
        Writes multiple data records into a Kinesis data stream in a single call (also
        referred to as a `PutRecords` request).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.put_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#put_records)
        """
    def register_stream_consumer(
        self, *, StreamARN: str, ConsumerName: str
    ) -> RegisterStreamConsumerOutputTypeDef:
        """
        Registers a consumer with a Kinesis data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.register_stream_consumer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#register_stream_consumer)
        """
    def remove_tags_from_stream(self, *, StreamName: str, TagKeys: List[str]) -> None:
        """
        Removes tags from the specified Kinesis data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.remove_tags_from_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#remove_tags_from_stream)
        """
    def split_shard(self, *, StreamName: str, ShardToSplit: str, NewStartingHashKey: str) -> None:
        """
        Splits a shard into two new shards in the Kinesis data stream, to increase the
        stream's capacity to ingest and transport data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.split_shard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#split_shard)
        """
    def start_stream_encryption(
        self, *, StreamName: str, EncryptionType: EncryptionTypeType, KeyId: str
    ) -> None:
        """
        Enables or updates server-side encryption using an AWS KMS key for a specified
        stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.start_stream_encryption)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#start_stream_encryption)
        """
    def stop_stream_encryption(
        self, *, StreamName: str, EncryptionType: EncryptionTypeType, KeyId: str
    ) -> None:
        """
        Disables server-side encryption for a specified stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.stop_stream_encryption)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#stop_stream_encryption)
        """
    def subscribe_to_shard(
        self, *, ConsumerARN: str, ShardId: str, StartingPosition: "StartingPositionTypeDef"
    ) -> SubscribeToShardOutputTypeDef:
        """
        This operation establishes an HTTP/2 connection between the consumer you specify
        in the `ConsumerARN` parameter and the shard you specify in the `ShardId`
        parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.subscribe_to_shard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#subscribe_to_shard)
        """
    def update_shard_count(
        self, *, StreamName: str, TargetShardCount: int, ScalingType: Literal["UNIFORM_SCALING"]
    ) -> UpdateShardCountOutputTypeDef:
        """
        Updates the shard count of the specified stream to the specified number of
        shards.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Client.update_shard_count)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client.html#update_shard_count)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_stream"]) -> DescribeStreamPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Paginator.DescribeStream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators.html#describestreampaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_shards"]) -> ListShardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Paginator.ListShards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators.html#listshardspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_stream_consumers"]
    ) -> ListStreamConsumersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Paginator.ListStreamConsumers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators.html#liststreamconsumerspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_streams"]) -> ListStreamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Paginator.ListStreams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/paginators.html#liststreamspaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["stream_exists"]) -> StreamExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Waiter.StreamExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/waiters.html#streamexistswaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["stream_not_exists"]) -> StreamNotExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/kinesis.html#Kinesis.Waiter.StreamNotExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/waiters.html#streamnotexistswaiter)
        """
