"""
Type annotations for kinesis service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_kinesis.client import KinesisClient

    session = Session()
    client: KinesisClient = session.client("kinesis")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeStreamPaginator,
    ListShardsPaginator,
    ListStreamConsumersPaginator,
    ListStreamsPaginator,
)
from .type_defs import (
    AddTagsToStreamInputTypeDef,
    CreateStreamInputTypeDef,
    DecreaseStreamRetentionPeriodInputTypeDef,
    DeleteResourcePolicyInputTypeDef,
    DeleteStreamInputTypeDef,
    DeregisterStreamConsumerInputTypeDef,
    DescribeLimitsOutputTypeDef,
    DescribeStreamConsumerInputTypeDef,
    DescribeStreamConsumerOutputTypeDef,
    DescribeStreamInputTypeDef,
    DescribeStreamOutputTypeDef,
    DescribeStreamSummaryInputTypeDef,
    DescribeStreamSummaryOutputTypeDef,
    DisableEnhancedMonitoringInputTypeDef,
    EmptyResponseMetadataTypeDef,
    EnableEnhancedMonitoringInputTypeDef,
    EnhancedMonitoringOutputTypeDef,
    GetRecordsInputTypeDef,
    GetRecordsOutputTypeDef,
    GetResourcePolicyInputTypeDef,
    GetResourcePolicyOutputTypeDef,
    GetShardIteratorInputTypeDef,
    GetShardIteratorOutputTypeDef,
    IncreaseStreamRetentionPeriodInputTypeDef,
    ListShardsInputTypeDef,
    ListShardsOutputTypeDef,
    ListStreamConsumersInputTypeDef,
    ListStreamConsumersOutputTypeDef,
    ListStreamsInputTypeDef,
    ListStreamsOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTagsForStreamInputTypeDef,
    ListTagsForStreamOutputTypeDef,
    MergeShardsInputTypeDef,
    PutRecordInputTypeDef,
    PutRecordOutputTypeDef,
    PutRecordsInputTypeDef,
    PutRecordsOutputTypeDef,
    PutResourcePolicyInputTypeDef,
    RegisterStreamConsumerInputTypeDef,
    RegisterStreamConsumerOutputTypeDef,
    RemoveTagsFromStreamInputTypeDef,
    SplitShardInputTypeDef,
    StartStreamEncryptionInputTypeDef,
    StopStreamEncryptionInputTypeDef,
    SubscribeToShardInputTypeDef,
    SubscribeToShardOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateShardCountInputTypeDef,
    UpdateShardCountOutputTypeDef,
    UpdateStreamModeInputTypeDef,
)
from .waiter import StreamExistsWaiter, StreamNotExistsWaiter

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("KinesisClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
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
    ValidationException: Type[BotocoreClientError]

class KinesisClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KinesisClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis.html#Kinesis.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#generate_presigned_url)
        """

    def add_tags_to_stream(
        self, **kwargs: Unpack[AddTagsToStreamInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or updates tags for the specified Kinesis data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/add_tags_to_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#add_tags_to_stream)
        """

    def create_stream(
        self, **kwargs: Unpack[CreateStreamInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates a Kinesis data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/create_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#create_stream)
        """

    def decrease_stream_retention_period(
        self, **kwargs: Unpack[DecreaseStreamRetentionPeriodInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Decreases the Kinesis data stream's retention period, which is the length of
        time data records are accessible after they are added to the stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/decrease_stream_retention_period.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#decrease_stream_retention_period)
        """

    def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a policy for the specified data stream or consumer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/delete_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#delete_resource_policy)
        """

    def delete_stream(
        self, **kwargs: Unpack[DeleteStreamInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a Kinesis data stream and all its shards and data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/delete_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#delete_stream)
        """

    def deregister_stream_consumer(
        self, **kwargs: Unpack[DeregisterStreamConsumerInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        To deregister a consumer, provide its ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/deregister_stream_consumer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#deregister_stream_consumer)
        """

    def describe_limits(self) -> DescribeLimitsOutputTypeDef:
        """
        Describes the shard limits and usage for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/describe_limits.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#describe_limits)
        """

    def describe_stream(
        self, **kwargs: Unpack[DescribeStreamInputTypeDef]
    ) -> DescribeStreamOutputTypeDef:
        """
        Describes the specified Kinesis data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/describe_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#describe_stream)
        """

    def describe_stream_consumer(
        self, **kwargs: Unpack[DescribeStreamConsumerInputTypeDef]
    ) -> DescribeStreamConsumerOutputTypeDef:
        """
        To get the description of a registered consumer, provide the ARN of the
        consumer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/describe_stream_consumer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#describe_stream_consumer)
        """

    def describe_stream_summary(
        self, **kwargs: Unpack[DescribeStreamSummaryInputTypeDef]
    ) -> DescribeStreamSummaryOutputTypeDef:
        """
        Provides a summarized description of the specified Kinesis data stream without
        the shard list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/describe_stream_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#describe_stream_summary)
        """

    def disable_enhanced_monitoring(
        self, **kwargs: Unpack[DisableEnhancedMonitoringInputTypeDef]
    ) -> EnhancedMonitoringOutputTypeDef:
        """
        Disables enhanced monitoring.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/disable_enhanced_monitoring.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#disable_enhanced_monitoring)
        """

    def enable_enhanced_monitoring(
        self, **kwargs: Unpack[EnableEnhancedMonitoringInputTypeDef]
    ) -> EnhancedMonitoringOutputTypeDef:
        """
        Enables enhanced Kinesis data stream monitoring for shard-level metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/enable_enhanced_monitoring.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#enable_enhanced_monitoring)
        """

    def get_records(self, **kwargs: Unpack[GetRecordsInputTypeDef]) -> GetRecordsOutputTypeDef:
        """
        Gets data records from a Kinesis data stream's shard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/get_records.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#get_records)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyInputTypeDef]
    ) -> GetResourcePolicyOutputTypeDef:
        """
        Returns a policy attached to the specified data stream or consumer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/get_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#get_resource_policy)
        """

    def get_shard_iterator(
        self, **kwargs: Unpack[GetShardIteratorInputTypeDef]
    ) -> GetShardIteratorOutputTypeDef:
        """
        Gets an Amazon Kinesis shard iterator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/get_shard_iterator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#get_shard_iterator)
        """

    def increase_stream_retention_period(
        self, **kwargs: Unpack[IncreaseStreamRetentionPeriodInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Increases the Kinesis data stream's retention period, which is the length of
        time data records are accessible after they are added to the stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/increase_stream_retention_period.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#increase_stream_retention_period)
        """

    def list_shards(self, **kwargs: Unpack[ListShardsInputTypeDef]) -> ListShardsOutputTypeDef:
        """
        Lists the shards in a stream and provides information about each shard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/list_shards.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#list_shards)
        """

    def list_stream_consumers(
        self, **kwargs: Unpack[ListStreamConsumersInputTypeDef]
    ) -> ListStreamConsumersOutputTypeDef:
        """
        Lists the consumers registered to receive data from a stream using enhanced
        fan-out, and provides information about each consumer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/list_stream_consumers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#list_stream_consumers)
        """

    def list_streams(self, **kwargs: Unpack[ListStreamsInputTypeDef]) -> ListStreamsOutputTypeDef:
        """
        Lists your Kinesis data streams.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/list_streams.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#list_streams)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        List all tags added to the specified Kinesis resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#list_tags_for_resource)
        """

    def list_tags_for_stream(
        self, **kwargs: Unpack[ListTagsForStreamInputTypeDef]
    ) -> ListTagsForStreamOutputTypeDef:
        """
        Lists the tags for the specified Kinesis data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/list_tags_for_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#list_tags_for_stream)
        """

    def merge_shards(
        self, **kwargs: Unpack[MergeShardsInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Merges two adjacent shards in a Kinesis data stream and combines them into a
        single shard to reduce the stream's capacity to ingest and transport data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/merge_shards.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#merge_shards)
        """

    def put_record(self, **kwargs: Unpack[PutRecordInputTypeDef]) -> PutRecordOutputTypeDef:
        """
        Writes a single data record into an Amazon Kinesis data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/put_record.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#put_record)
        """

    def put_records(self, **kwargs: Unpack[PutRecordsInputTypeDef]) -> PutRecordsOutputTypeDef:
        """
        Writes multiple data records into a Kinesis data stream in a single call (also
        referred to as a <code>PutRecords</code> request).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/put_records.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#put_records)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Attaches a resource-based policy to a data stream or registered consumer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/put_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#put_resource_policy)
        """

    def register_stream_consumer(
        self, **kwargs: Unpack[RegisterStreamConsumerInputTypeDef]
    ) -> RegisterStreamConsumerOutputTypeDef:
        """
        Registers a consumer with a Kinesis data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/register_stream_consumer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#register_stream_consumer)
        """

    def remove_tags_from_stream(
        self, **kwargs: Unpack[RemoveTagsFromStreamInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes tags from the specified Kinesis data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/remove_tags_from_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#remove_tags_from_stream)
        """

    def split_shard(self, **kwargs: Unpack[SplitShardInputTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Splits a shard into two new shards in the Kinesis data stream, to increase the
        stream's capacity to ingest and transport data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/split_shard.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#split_shard)
        """

    def start_stream_encryption(
        self, **kwargs: Unpack[StartStreamEncryptionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables or updates server-side encryption using an Amazon Web Services KMS key
        for a specified stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/start_stream_encryption.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#start_stream_encryption)
        """

    def stop_stream_encryption(
        self, **kwargs: Unpack[StopStreamEncryptionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disables server-side encryption for a specified stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/stop_stream_encryption.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#stop_stream_encryption)
        """

    def subscribe_to_shard(
        self, **kwargs: Unpack[SubscribeToShardInputTypeDef]
    ) -> SubscribeToShardOutputTypeDef:
        """
        This operation establishes an HTTP/2 connection between the consumer you
        specify in the <code>ConsumerARN</code> parameter and the shard you specify in
        the <code>ShardId</code> parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/subscribe_to_shard.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#subscribe_to_shard)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or updates tags for the specified Kinesis resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes tags from the specified Kinesis resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#untag_resource)
        """

    def update_shard_count(
        self, **kwargs: Unpack[UpdateShardCountInputTypeDef]
    ) -> UpdateShardCountOutputTypeDef:
        """
        Updates the shard count of the specified stream to the specified number of
        shards.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/update_shard_count.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#update_shard_count)
        """

    def update_stream_mode(
        self, **kwargs: Unpack[UpdateStreamModeInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the capacity mode of the data stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/update_stream_mode.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#update_stream_mode)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_stream"]
    ) -> DescribeStreamPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_shards"]
    ) -> ListShardsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_stream_consumers"]
    ) -> ListStreamConsumersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_streams"]
    ) -> ListStreamsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["stream_exists"]
    ) -> StreamExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["stream_not_exists"]
    ) -> StreamNotExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesis/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/client/#get_waiter)
        """
