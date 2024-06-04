"""
Type annotations for kinesis service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesis.type_defs import AddTagsToStreamInputRequestTypeDef

    data: AddTagsToStreamInputRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ConsumerStatusType,
    EncryptionTypeType,
    MetricsNameType,
    ShardFilterTypeType,
    ShardIteratorTypeType,
    StreamModeType,
    StreamStatusType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddTagsToStreamInputRequestTypeDef",
    "ChildShardTypeDef",
    "ConsumerDescriptionTypeDef",
    "ConsumerTypeDef",
    "CreateStreamInputRequestTypeDef",
    "DecreaseStreamRetentionPeriodInputRequestTypeDef",
    "DeleteResourcePolicyInputRequestTypeDef",
    "DeleteStreamInputRequestTypeDef",
    "DeregisterStreamConsumerInputRequestTypeDef",
    "DescribeLimitsOutputTypeDef",
    "DescribeStreamConsumerInputRequestTypeDef",
    "DescribeStreamConsumerOutputTypeDef",
    "DescribeStreamInputRequestTypeDef",
    "DescribeStreamOutputTypeDef",
    "DescribeStreamSummaryInputRequestTypeDef",
    "DescribeStreamSummaryOutputTypeDef",
    "DisableEnhancedMonitoringInputRequestTypeDef",
    "EnableEnhancedMonitoringInputRequestTypeDef",
    "EnhancedMetricsTypeDef",
    "EnhancedMonitoringOutputTypeDef",
    "GetRecordsInputRequestTypeDef",
    "GetRecordsOutputTypeDef",
    "GetResourcePolicyInputRequestTypeDef",
    "GetResourcePolicyOutputTypeDef",
    "GetShardIteratorInputRequestTypeDef",
    "GetShardIteratorOutputTypeDef",
    "HashKeyRangeTypeDef",
    "IncreaseStreamRetentionPeriodInputRequestTypeDef",
    "InternalFailureExceptionTypeDef",
    "KMSAccessDeniedExceptionTypeDef",
    "KMSDisabledExceptionTypeDef",
    "KMSInvalidStateExceptionTypeDef",
    "KMSNotFoundExceptionTypeDef",
    "KMSOptInRequiredTypeDef",
    "KMSThrottlingExceptionTypeDef",
    "ListShardsInputRequestTypeDef",
    "ListShardsOutputTypeDef",
    "ListStreamConsumersInputRequestTypeDef",
    "ListStreamConsumersOutputTypeDef",
    "ListStreamsInputRequestTypeDef",
    "ListStreamsOutputTypeDef",
    "ListTagsForStreamInputRequestTypeDef",
    "ListTagsForStreamOutputTypeDef",
    "MergeShardsInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PutRecordInputRequestTypeDef",
    "PutRecordOutputTypeDef",
    "PutRecordsInputRequestTypeDef",
    "PutRecordsOutputTypeDef",
    "PutRecordsRequestEntryTypeDef",
    "PutRecordsResultEntryTypeDef",
    "PutResourcePolicyInputRequestTypeDef",
    "RecordTypeDef",
    "RegisterStreamConsumerInputRequestTypeDef",
    "RegisterStreamConsumerOutputTypeDef",
    "RemoveTagsFromStreamInputRequestTypeDef",
    "ResourceInUseExceptionTypeDef",
    "ResourceNotFoundExceptionTypeDef",
    "ResponseMetadataTypeDef",
    "SequenceNumberRangeTypeDef",
    "ShardFilterTypeDef",
    "ShardTypeDef",
    "SplitShardInputRequestTypeDef",
    "StartStreamEncryptionInputRequestTypeDef",
    "StartingPositionTypeDef",
    "StopStreamEncryptionInputRequestTypeDef",
    "StreamDescriptionSummaryTypeDef",
    "StreamDescriptionTypeDef",
    "StreamModeDetailsTypeDef",
    "StreamSummaryTypeDef",
    "SubscribeToShardEventStreamTypeDef",
    "SubscribeToShardEventTypeDef",
    "SubscribeToShardInputRequestTypeDef",
    "SubscribeToShardOutputTypeDef",
    "TagTypeDef",
    "UpdateShardCountInputRequestTypeDef",
    "UpdateShardCountOutputTypeDef",
    "UpdateStreamModeInputRequestTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAddTagsToStreamInputRequestTypeDef = TypedDict(
    "_RequiredAddTagsToStreamInputRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
)
_OptionalAddTagsToStreamInputRequestTypeDef = TypedDict(
    "_OptionalAddTagsToStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class AddTagsToStreamInputRequestTypeDef(
    _RequiredAddTagsToStreamInputRequestTypeDef, _OptionalAddTagsToStreamInputRequestTypeDef
):
    pass

ChildShardTypeDef = TypedDict(
    "ChildShardTypeDef",
    {
        "ShardId": str,
        "ParentShards": List[str],
        "HashKeyRange": "HashKeyRangeTypeDef",
    },
)

ConsumerDescriptionTypeDef = TypedDict(
    "ConsumerDescriptionTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": ConsumerStatusType,
        "ConsumerCreationTimestamp": datetime,
        "StreamARN": str,
    },
)

ConsumerTypeDef = TypedDict(
    "ConsumerTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": ConsumerStatusType,
        "ConsumerCreationTimestamp": datetime,
    },
)

_RequiredCreateStreamInputRequestTypeDef = TypedDict(
    "_RequiredCreateStreamInputRequestTypeDef",
    {
        "StreamName": str,
    },
)
_OptionalCreateStreamInputRequestTypeDef = TypedDict(
    "_OptionalCreateStreamInputRequestTypeDef",
    {
        "ShardCount": int,
        "StreamModeDetails": "StreamModeDetailsTypeDef",
    },
    total=False,
)

class CreateStreamInputRequestTypeDef(
    _RequiredCreateStreamInputRequestTypeDef, _OptionalCreateStreamInputRequestTypeDef
):
    pass

_RequiredDecreaseStreamRetentionPeriodInputRequestTypeDef = TypedDict(
    "_RequiredDecreaseStreamRetentionPeriodInputRequestTypeDef",
    {
        "RetentionPeriodHours": int,
    },
)
_OptionalDecreaseStreamRetentionPeriodInputRequestTypeDef = TypedDict(
    "_OptionalDecreaseStreamRetentionPeriodInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class DecreaseStreamRetentionPeriodInputRequestTypeDef(
    _RequiredDecreaseStreamRetentionPeriodInputRequestTypeDef,
    _OptionalDecreaseStreamRetentionPeriodInputRequestTypeDef,
):
    pass

DeleteResourcePolicyInputRequestTypeDef = TypedDict(
    "DeleteResourcePolicyInputRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

DeleteStreamInputRequestTypeDef = TypedDict(
    "DeleteStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "EnforceConsumerDeletion": bool,
        "StreamARN": str,
    },
    total=False,
)

DeregisterStreamConsumerInputRequestTypeDef = TypedDict(
    "DeregisterStreamConsumerInputRequestTypeDef",
    {
        "StreamARN": str,
        "ConsumerName": str,
        "ConsumerARN": str,
    },
    total=False,
)

DescribeLimitsOutputTypeDef = TypedDict(
    "DescribeLimitsOutputTypeDef",
    {
        "ShardLimit": int,
        "OpenShardCount": int,
        "OnDemandStreamCount": int,
        "OnDemandStreamCountLimit": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamConsumerInputRequestTypeDef = TypedDict(
    "DescribeStreamConsumerInputRequestTypeDef",
    {
        "StreamARN": str,
        "ConsumerName": str,
        "ConsumerARN": str,
    },
    total=False,
)

DescribeStreamConsumerOutputTypeDef = TypedDict(
    "DescribeStreamConsumerOutputTypeDef",
    {
        "ConsumerDescription": "ConsumerDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamInputRequestTypeDef = TypedDict(
    "DescribeStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "Limit": int,
        "ExclusiveStartShardId": str,
        "StreamARN": str,
    },
    total=False,
)

DescribeStreamOutputTypeDef = TypedDict(
    "DescribeStreamOutputTypeDef",
    {
        "StreamDescription": "StreamDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamSummaryInputRequestTypeDef = TypedDict(
    "DescribeStreamSummaryInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

DescribeStreamSummaryOutputTypeDef = TypedDict(
    "DescribeStreamSummaryOutputTypeDef",
    {
        "StreamDescriptionSummary": "StreamDescriptionSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableEnhancedMonitoringInputRequestTypeDef = TypedDict(
    "_RequiredDisableEnhancedMonitoringInputRequestTypeDef",
    {
        "ShardLevelMetrics": List[MetricsNameType],
    },
)
_OptionalDisableEnhancedMonitoringInputRequestTypeDef = TypedDict(
    "_OptionalDisableEnhancedMonitoringInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class DisableEnhancedMonitoringInputRequestTypeDef(
    _RequiredDisableEnhancedMonitoringInputRequestTypeDef,
    _OptionalDisableEnhancedMonitoringInputRequestTypeDef,
):
    pass

_RequiredEnableEnhancedMonitoringInputRequestTypeDef = TypedDict(
    "_RequiredEnableEnhancedMonitoringInputRequestTypeDef",
    {
        "ShardLevelMetrics": List[MetricsNameType],
    },
)
_OptionalEnableEnhancedMonitoringInputRequestTypeDef = TypedDict(
    "_OptionalEnableEnhancedMonitoringInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class EnableEnhancedMonitoringInputRequestTypeDef(
    _RequiredEnableEnhancedMonitoringInputRequestTypeDef,
    _OptionalEnableEnhancedMonitoringInputRequestTypeDef,
):
    pass

EnhancedMetricsTypeDef = TypedDict(
    "EnhancedMetricsTypeDef",
    {
        "ShardLevelMetrics": List[MetricsNameType],
    },
    total=False,
)

EnhancedMonitoringOutputTypeDef = TypedDict(
    "EnhancedMonitoringOutputTypeDef",
    {
        "StreamName": str,
        "CurrentShardLevelMetrics": List[MetricsNameType],
        "DesiredShardLevelMetrics": List[MetricsNameType],
        "StreamARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRecordsInputRequestTypeDef = TypedDict(
    "_RequiredGetRecordsInputRequestTypeDef",
    {
        "ShardIterator": str,
    },
)
_OptionalGetRecordsInputRequestTypeDef = TypedDict(
    "_OptionalGetRecordsInputRequestTypeDef",
    {
        "Limit": int,
        "StreamARN": str,
    },
    total=False,
)

class GetRecordsInputRequestTypeDef(
    _RequiredGetRecordsInputRequestTypeDef, _OptionalGetRecordsInputRequestTypeDef
):
    pass

GetRecordsOutputTypeDef = TypedDict(
    "GetRecordsOutputTypeDef",
    {
        "Records": List["RecordTypeDef"],
        "NextShardIterator": str,
        "MillisBehindLatest": int,
        "ChildShards": List["ChildShardTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyInputRequestTypeDef = TypedDict(
    "GetResourcePolicyInputRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

GetResourcePolicyOutputTypeDef = TypedDict(
    "GetResourcePolicyOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetShardIteratorInputRequestTypeDef = TypedDict(
    "_RequiredGetShardIteratorInputRequestTypeDef",
    {
        "ShardId": str,
        "ShardIteratorType": ShardIteratorTypeType,
    },
)
_OptionalGetShardIteratorInputRequestTypeDef = TypedDict(
    "_OptionalGetShardIteratorInputRequestTypeDef",
    {
        "StreamName": str,
        "StartingSequenceNumber": str,
        "Timestamp": Union[datetime, str],
        "StreamARN": str,
    },
    total=False,
)

class GetShardIteratorInputRequestTypeDef(
    _RequiredGetShardIteratorInputRequestTypeDef, _OptionalGetShardIteratorInputRequestTypeDef
):
    pass

GetShardIteratorOutputTypeDef = TypedDict(
    "GetShardIteratorOutputTypeDef",
    {
        "ShardIterator": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HashKeyRangeTypeDef = TypedDict(
    "HashKeyRangeTypeDef",
    {
        "StartingHashKey": str,
        "EndingHashKey": str,
    },
)

_RequiredIncreaseStreamRetentionPeriodInputRequestTypeDef = TypedDict(
    "_RequiredIncreaseStreamRetentionPeriodInputRequestTypeDef",
    {
        "RetentionPeriodHours": int,
    },
)
_OptionalIncreaseStreamRetentionPeriodInputRequestTypeDef = TypedDict(
    "_OptionalIncreaseStreamRetentionPeriodInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class IncreaseStreamRetentionPeriodInputRequestTypeDef(
    _RequiredIncreaseStreamRetentionPeriodInputRequestTypeDef,
    _OptionalIncreaseStreamRetentionPeriodInputRequestTypeDef,
):
    pass

InternalFailureExceptionTypeDef = TypedDict(
    "InternalFailureExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSAccessDeniedExceptionTypeDef = TypedDict(
    "KMSAccessDeniedExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSDisabledExceptionTypeDef = TypedDict(
    "KMSDisabledExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSInvalidStateExceptionTypeDef = TypedDict(
    "KMSInvalidStateExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSNotFoundExceptionTypeDef = TypedDict(
    "KMSNotFoundExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSOptInRequiredTypeDef = TypedDict(
    "KMSOptInRequiredTypeDef",
    {
        "message": str,
    },
    total=False,
)

KMSThrottlingExceptionTypeDef = TypedDict(
    "KMSThrottlingExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

ListShardsInputRequestTypeDef = TypedDict(
    "ListShardsInputRequestTypeDef",
    {
        "StreamName": str,
        "NextToken": str,
        "ExclusiveStartShardId": str,
        "MaxResults": int,
        "StreamCreationTimestamp": Union[datetime, str],
        "ShardFilter": "ShardFilterTypeDef",
        "StreamARN": str,
    },
    total=False,
)

ListShardsOutputTypeDef = TypedDict(
    "ListShardsOutputTypeDef",
    {
        "Shards": List["ShardTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStreamConsumersInputRequestTypeDef = TypedDict(
    "_RequiredListStreamConsumersInputRequestTypeDef",
    {
        "StreamARN": str,
    },
)
_OptionalListStreamConsumersInputRequestTypeDef = TypedDict(
    "_OptionalListStreamConsumersInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StreamCreationTimestamp": Union[datetime, str],
    },
    total=False,
)

class ListStreamConsumersInputRequestTypeDef(
    _RequiredListStreamConsumersInputRequestTypeDef, _OptionalListStreamConsumersInputRequestTypeDef
):
    pass

ListStreamConsumersOutputTypeDef = TypedDict(
    "ListStreamConsumersOutputTypeDef",
    {
        "Consumers": List["ConsumerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamsInputRequestTypeDef = TypedDict(
    "ListStreamsInputRequestTypeDef",
    {
        "Limit": int,
        "ExclusiveStartStreamName": str,
        "NextToken": str,
    },
    total=False,
)

ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {
        "StreamNames": List[str],
        "HasMoreStreams": bool,
        "NextToken": str,
        "StreamSummaries": List["StreamSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForStreamInputRequestTypeDef = TypedDict(
    "ListTagsForStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "ExclusiveStartTagKey": str,
        "Limit": int,
        "StreamARN": str,
    },
    total=False,
)

ListTagsForStreamOutputTypeDef = TypedDict(
    "ListTagsForStreamOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "HasMoreTags": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMergeShardsInputRequestTypeDef = TypedDict(
    "_RequiredMergeShardsInputRequestTypeDef",
    {
        "ShardToMerge": str,
        "AdjacentShardToMerge": str,
    },
)
_OptionalMergeShardsInputRequestTypeDef = TypedDict(
    "_OptionalMergeShardsInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class MergeShardsInputRequestTypeDef(
    _RequiredMergeShardsInputRequestTypeDef, _OptionalMergeShardsInputRequestTypeDef
):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPutRecordInputRequestTypeDef = TypedDict(
    "_RequiredPutRecordInputRequestTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
        "PartitionKey": str,
    },
)
_OptionalPutRecordInputRequestTypeDef = TypedDict(
    "_OptionalPutRecordInputRequestTypeDef",
    {
        "StreamName": str,
        "ExplicitHashKey": str,
        "SequenceNumberForOrdering": str,
        "StreamARN": str,
    },
    total=False,
)

class PutRecordInputRequestTypeDef(
    _RequiredPutRecordInputRequestTypeDef, _OptionalPutRecordInputRequestTypeDef
):
    pass

PutRecordOutputTypeDef = TypedDict(
    "PutRecordOutputTypeDef",
    {
        "ShardId": str,
        "SequenceNumber": str,
        "EncryptionType": EncryptionTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutRecordsInputRequestTypeDef = TypedDict(
    "_RequiredPutRecordsInputRequestTypeDef",
    {
        "Records": List["PutRecordsRequestEntryTypeDef"],
    },
)
_OptionalPutRecordsInputRequestTypeDef = TypedDict(
    "_OptionalPutRecordsInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class PutRecordsInputRequestTypeDef(
    _RequiredPutRecordsInputRequestTypeDef, _OptionalPutRecordsInputRequestTypeDef
):
    pass

PutRecordsOutputTypeDef = TypedDict(
    "PutRecordsOutputTypeDef",
    {
        "FailedRecordCount": int,
        "Records": List["PutRecordsResultEntryTypeDef"],
        "EncryptionType": EncryptionTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutRecordsRequestEntryTypeDef = TypedDict(
    "_RequiredPutRecordsRequestEntryTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
        "PartitionKey": str,
    },
)
_OptionalPutRecordsRequestEntryTypeDef = TypedDict(
    "_OptionalPutRecordsRequestEntryTypeDef",
    {
        "ExplicitHashKey": str,
    },
    total=False,
)

class PutRecordsRequestEntryTypeDef(
    _RequiredPutRecordsRequestEntryTypeDef, _OptionalPutRecordsRequestEntryTypeDef
):
    pass

PutRecordsResultEntryTypeDef = TypedDict(
    "PutRecordsResultEntryTypeDef",
    {
        "SequenceNumber": str,
        "ShardId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

PutResourcePolicyInputRequestTypeDef = TypedDict(
    "PutResourcePolicyInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Policy": str,
    },
)

_RequiredRecordTypeDef = TypedDict(
    "_RequiredRecordTypeDef",
    {
        "SequenceNumber": str,
        "Data": bytes,
        "PartitionKey": str,
    },
)
_OptionalRecordTypeDef = TypedDict(
    "_OptionalRecordTypeDef",
    {
        "ApproximateArrivalTimestamp": datetime,
        "EncryptionType": EncryptionTypeType,
    },
    total=False,
)

class RecordTypeDef(_RequiredRecordTypeDef, _OptionalRecordTypeDef):
    pass

RegisterStreamConsumerInputRequestTypeDef = TypedDict(
    "RegisterStreamConsumerInputRequestTypeDef",
    {
        "StreamARN": str,
        "ConsumerName": str,
    },
)

RegisterStreamConsumerOutputTypeDef = TypedDict(
    "RegisterStreamConsumerOutputTypeDef",
    {
        "Consumer": "ConsumerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRemoveTagsFromStreamInputRequestTypeDef = TypedDict(
    "_RequiredRemoveTagsFromStreamInputRequestTypeDef",
    {
        "TagKeys": List[str],
    },
)
_OptionalRemoveTagsFromStreamInputRequestTypeDef = TypedDict(
    "_OptionalRemoveTagsFromStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class RemoveTagsFromStreamInputRequestTypeDef(
    _RequiredRemoveTagsFromStreamInputRequestTypeDef,
    _OptionalRemoveTagsFromStreamInputRequestTypeDef,
):
    pass

ResourceInUseExceptionTypeDef = TypedDict(
    "ResourceInUseExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

ResourceNotFoundExceptionTypeDef = TypedDict(
    "ResourceNotFoundExceptionTypeDef",
    {
        "message": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredSequenceNumberRangeTypeDef = TypedDict(
    "_RequiredSequenceNumberRangeTypeDef",
    {
        "StartingSequenceNumber": str,
    },
)
_OptionalSequenceNumberRangeTypeDef = TypedDict(
    "_OptionalSequenceNumberRangeTypeDef",
    {
        "EndingSequenceNumber": str,
    },
    total=False,
)

class SequenceNumberRangeTypeDef(
    _RequiredSequenceNumberRangeTypeDef, _OptionalSequenceNumberRangeTypeDef
):
    pass

_RequiredShardFilterTypeDef = TypedDict(
    "_RequiredShardFilterTypeDef",
    {
        "Type": ShardFilterTypeType,
    },
)
_OptionalShardFilterTypeDef = TypedDict(
    "_OptionalShardFilterTypeDef",
    {
        "ShardId": str,
        "Timestamp": Union[datetime, str],
    },
    total=False,
)

class ShardFilterTypeDef(_RequiredShardFilterTypeDef, _OptionalShardFilterTypeDef):
    pass

_RequiredShardTypeDef = TypedDict(
    "_RequiredShardTypeDef",
    {
        "ShardId": str,
        "HashKeyRange": "HashKeyRangeTypeDef",
        "SequenceNumberRange": "SequenceNumberRangeTypeDef",
    },
)
_OptionalShardTypeDef = TypedDict(
    "_OptionalShardTypeDef",
    {
        "ParentShardId": str,
        "AdjacentParentShardId": str,
    },
    total=False,
)

class ShardTypeDef(_RequiredShardTypeDef, _OptionalShardTypeDef):
    pass

_RequiredSplitShardInputRequestTypeDef = TypedDict(
    "_RequiredSplitShardInputRequestTypeDef",
    {
        "ShardToSplit": str,
        "NewStartingHashKey": str,
    },
)
_OptionalSplitShardInputRequestTypeDef = TypedDict(
    "_OptionalSplitShardInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class SplitShardInputRequestTypeDef(
    _RequiredSplitShardInputRequestTypeDef, _OptionalSplitShardInputRequestTypeDef
):
    pass

_RequiredStartStreamEncryptionInputRequestTypeDef = TypedDict(
    "_RequiredStartStreamEncryptionInputRequestTypeDef",
    {
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
    },
)
_OptionalStartStreamEncryptionInputRequestTypeDef = TypedDict(
    "_OptionalStartStreamEncryptionInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class StartStreamEncryptionInputRequestTypeDef(
    _RequiredStartStreamEncryptionInputRequestTypeDef,
    _OptionalStartStreamEncryptionInputRequestTypeDef,
):
    pass

_RequiredStartingPositionTypeDef = TypedDict(
    "_RequiredStartingPositionTypeDef",
    {
        "Type": ShardIteratorTypeType,
    },
)
_OptionalStartingPositionTypeDef = TypedDict(
    "_OptionalStartingPositionTypeDef",
    {
        "SequenceNumber": str,
        "Timestamp": Union[datetime, str],
    },
    total=False,
)

class StartingPositionTypeDef(_RequiredStartingPositionTypeDef, _OptionalStartingPositionTypeDef):
    pass

_RequiredStopStreamEncryptionInputRequestTypeDef = TypedDict(
    "_RequiredStopStreamEncryptionInputRequestTypeDef",
    {
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
    },
)
_OptionalStopStreamEncryptionInputRequestTypeDef = TypedDict(
    "_OptionalStopStreamEncryptionInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class StopStreamEncryptionInputRequestTypeDef(
    _RequiredStopStreamEncryptionInputRequestTypeDef,
    _OptionalStopStreamEncryptionInputRequestTypeDef,
):
    pass

_RequiredStreamDescriptionSummaryTypeDef = TypedDict(
    "_RequiredStreamDescriptionSummaryTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": StreamStatusType,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List["EnhancedMetricsTypeDef"],
        "OpenShardCount": int,
    },
)
_OptionalStreamDescriptionSummaryTypeDef = TypedDict(
    "_OptionalStreamDescriptionSummaryTypeDef",
    {
        "StreamModeDetails": "StreamModeDetailsTypeDef",
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
        "ConsumerCount": int,
    },
    total=False,
)

class StreamDescriptionSummaryTypeDef(
    _RequiredStreamDescriptionSummaryTypeDef, _OptionalStreamDescriptionSummaryTypeDef
):
    pass

_RequiredStreamDescriptionTypeDef = TypedDict(
    "_RequiredStreamDescriptionTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": StreamStatusType,
        "Shards": List["ShardTypeDef"],
        "HasMoreShards": bool,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List["EnhancedMetricsTypeDef"],
    },
)
_OptionalStreamDescriptionTypeDef = TypedDict(
    "_OptionalStreamDescriptionTypeDef",
    {
        "StreamModeDetails": "StreamModeDetailsTypeDef",
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
    },
    total=False,
)

class StreamDescriptionTypeDef(
    _RequiredStreamDescriptionTypeDef, _OptionalStreamDescriptionTypeDef
):
    pass

StreamModeDetailsTypeDef = TypedDict(
    "StreamModeDetailsTypeDef",
    {
        "StreamMode": StreamModeType,
    },
)

_RequiredStreamSummaryTypeDef = TypedDict(
    "_RequiredStreamSummaryTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": StreamStatusType,
    },
)
_OptionalStreamSummaryTypeDef = TypedDict(
    "_OptionalStreamSummaryTypeDef",
    {
        "StreamModeDetails": "StreamModeDetailsTypeDef",
        "StreamCreationTimestamp": datetime,
    },
    total=False,
)

class StreamSummaryTypeDef(_RequiredStreamSummaryTypeDef, _OptionalStreamSummaryTypeDef):
    pass

_RequiredSubscribeToShardEventStreamTypeDef = TypedDict(
    "_RequiredSubscribeToShardEventStreamTypeDef",
    {
        "SubscribeToShardEvent": "SubscribeToShardEventTypeDef",
    },
)
_OptionalSubscribeToShardEventStreamTypeDef = TypedDict(
    "_OptionalSubscribeToShardEventStreamTypeDef",
    {
        "ResourceNotFoundException": "ResourceNotFoundExceptionTypeDef",
        "ResourceInUseException": "ResourceInUseExceptionTypeDef",
        "KMSDisabledException": "KMSDisabledExceptionTypeDef",
        "KMSInvalidStateException": "KMSInvalidStateExceptionTypeDef",
        "KMSAccessDeniedException": "KMSAccessDeniedExceptionTypeDef",
        "KMSNotFoundException": "KMSNotFoundExceptionTypeDef",
        "KMSOptInRequired": "KMSOptInRequiredTypeDef",
        "KMSThrottlingException": "KMSThrottlingExceptionTypeDef",
        "InternalFailureException": "InternalFailureExceptionTypeDef",
    },
    total=False,
)

class SubscribeToShardEventStreamTypeDef(
    _RequiredSubscribeToShardEventStreamTypeDef, _OptionalSubscribeToShardEventStreamTypeDef
):
    pass

_RequiredSubscribeToShardEventTypeDef = TypedDict(
    "_RequiredSubscribeToShardEventTypeDef",
    {
        "Records": List["RecordTypeDef"],
        "ContinuationSequenceNumber": str,
        "MillisBehindLatest": int,
    },
)
_OptionalSubscribeToShardEventTypeDef = TypedDict(
    "_OptionalSubscribeToShardEventTypeDef",
    {
        "ChildShards": List["ChildShardTypeDef"],
    },
    total=False,
)

class SubscribeToShardEventTypeDef(
    _RequiredSubscribeToShardEventTypeDef, _OptionalSubscribeToShardEventTypeDef
):
    pass

SubscribeToShardInputRequestTypeDef = TypedDict(
    "SubscribeToShardInputRequestTypeDef",
    {
        "ConsumerARN": str,
        "ShardId": str,
        "StartingPosition": "StartingPositionTypeDef",
    },
)

SubscribeToShardOutputTypeDef = TypedDict(
    "SubscribeToShardOutputTypeDef",
    {
        "EventStream": "SubscribeToShardEventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

_RequiredUpdateShardCountInputRequestTypeDef = TypedDict(
    "_RequiredUpdateShardCountInputRequestTypeDef",
    {
        "TargetShardCount": int,
        "ScalingType": Literal["UNIFORM_SCALING"],
    },
)
_OptionalUpdateShardCountInputRequestTypeDef = TypedDict(
    "_OptionalUpdateShardCountInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class UpdateShardCountInputRequestTypeDef(
    _RequiredUpdateShardCountInputRequestTypeDef, _OptionalUpdateShardCountInputRequestTypeDef
):
    pass

UpdateShardCountOutputTypeDef = TypedDict(
    "UpdateShardCountOutputTypeDef",
    {
        "StreamName": str,
        "CurrentShardCount": int,
        "TargetShardCount": int,
        "StreamARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStreamModeInputRequestTypeDef = TypedDict(
    "UpdateStreamModeInputRequestTypeDef",
    {
        "StreamARN": str,
        "StreamModeDetails": "StreamModeDetailsTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
