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
    "SubscribeToShardEventStreamTypeDef",
    "SubscribeToShardEventTypeDef",
    "SubscribeToShardInputRequestTypeDef",
    "SubscribeToShardOutputTypeDef",
    "TagTypeDef",
    "UpdateShardCountInputRequestTypeDef",
    "UpdateShardCountOutputTypeDef",
    "WaiterConfigTypeDef",
)

AddTagsToStreamInputRequestTypeDef = TypedDict(
    "AddTagsToStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "Tags": Dict[str, str],
    },
)

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

CreateStreamInputRequestTypeDef = TypedDict(
    "CreateStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "ShardCount": int,
    },
)

DecreaseStreamRetentionPeriodInputRequestTypeDef = TypedDict(
    "DecreaseStreamRetentionPeriodInputRequestTypeDef",
    {
        "StreamName": str,
        "RetentionPeriodHours": int,
    },
)

_RequiredDeleteStreamInputRequestTypeDef = TypedDict(
    "_RequiredDeleteStreamInputRequestTypeDef",
    {
        "StreamName": str,
    },
)
_OptionalDeleteStreamInputRequestTypeDef = TypedDict(
    "_OptionalDeleteStreamInputRequestTypeDef",
    {
        "EnforceConsumerDeletion": bool,
    },
    total=False,
)

class DeleteStreamInputRequestTypeDef(
    _RequiredDeleteStreamInputRequestTypeDef, _OptionalDeleteStreamInputRequestTypeDef
):
    pass

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

_RequiredDescribeStreamInputRequestTypeDef = TypedDict(
    "_RequiredDescribeStreamInputRequestTypeDef",
    {
        "StreamName": str,
    },
)
_OptionalDescribeStreamInputRequestTypeDef = TypedDict(
    "_OptionalDescribeStreamInputRequestTypeDef",
    {
        "Limit": int,
        "ExclusiveStartShardId": str,
    },
    total=False,
)

class DescribeStreamInputRequestTypeDef(
    _RequiredDescribeStreamInputRequestTypeDef, _OptionalDescribeStreamInputRequestTypeDef
):
    pass

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
    },
)

DescribeStreamSummaryOutputTypeDef = TypedDict(
    "DescribeStreamSummaryOutputTypeDef",
    {
        "StreamDescriptionSummary": "StreamDescriptionSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableEnhancedMonitoringInputRequestTypeDef = TypedDict(
    "DisableEnhancedMonitoringInputRequestTypeDef",
    {
        "StreamName": str,
        "ShardLevelMetrics": List[MetricsNameType],
    },
)

EnableEnhancedMonitoringInputRequestTypeDef = TypedDict(
    "EnableEnhancedMonitoringInputRequestTypeDef",
    {
        "StreamName": str,
        "ShardLevelMetrics": List[MetricsNameType],
    },
)

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

_RequiredGetShardIteratorInputRequestTypeDef = TypedDict(
    "_RequiredGetShardIteratorInputRequestTypeDef",
    {
        "StreamName": str,
        "ShardId": str,
        "ShardIteratorType": ShardIteratorTypeType,
    },
)
_OptionalGetShardIteratorInputRequestTypeDef = TypedDict(
    "_OptionalGetShardIteratorInputRequestTypeDef",
    {
        "StartingSequenceNumber": str,
        "Timestamp": Union[datetime, str],
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

IncreaseStreamRetentionPeriodInputRequestTypeDef = TypedDict(
    "IncreaseStreamRetentionPeriodInputRequestTypeDef",
    {
        "StreamName": str,
        "RetentionPeriodHours": int,
    },
)

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
    },
    total=False,
)

ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {
        "StreamNames": List[str],
        "HasMoreStreams": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForStreamInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForStreamInputRequestTypeDef",
    {
        "StreamName": str,
    },
)
_OptionalListTagsForStreamInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForStreamInputRequestTypeDef",
    {
        "ExclusiveStartTagKey": str,
        "Limit": int,
    },
    total=False,
)

class ListTagsForStreamInputRequestTypeDef(
    _RequiredListTagsForStreamInputRequestTypeDef, _OptionalListTagsForStreamInputRequestTypeDef
):
    pass

ListTagsForStreamOutputTypeDef = TypedDict(
    "ListTagsForStreamOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "HasMoreTags": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MergeShardsInputRequestTypeDef = TypedDict(
    "MergeShardsInputRequestTypeDef",
    {
        "StreamName": str,
        "ShardToMerge": str,
        "AdjacentShardToMerge": str,
    },
)

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
        "StreamName": str,
        "Data": Union[bytes, IO[bytes], StreamingBody],
        "PartitionKey": str,
    },
)
_OptionalPutRecordInputRequestTypeDef = TypedDict(
    "_OptionalPutRecordInputRequestTypeDef",
    {
        "ExplicitHashKey": str,
        "SequenceNumberForOrdering": str,
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

PutRecordsInputRequestTypeDef = TypedDict(
    "PutRecordsInputRequestTypeDef",
    {
        "Records": List["PutRecordsRequestEntryTypeDef"],
        "StreamName": str,
    },
)

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

RemoveTagsFromStreamInputRequestTypeDef = TypedDict(
    "RemoveTagsFromStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "TagKeys": List[str],
    },
)

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

SplitShardInputRequestTypeDef = TypedDict(
    "SplitShardInputRequestTypeDef",
    {
        "StreamName": str,
        "ShardToSplit": str,
        "NewStartingHashKey": str,
    },
)

StartStreamEncryptionInputRequestTypeDef = TypedDict(
    "StartStreamEncryptionInputRequestTypeDef",
    {
        "StreamName": str,
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
    },
)

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

StopStreamEncryptionInputRequestTypeDef = TypedDict(
    "StopStreamEncryptionInputRequestTypeDef",
    {
        "StreamName": str,
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
    },
)

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
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
    },
    total=False,
)

class StreamDescriptionTypeDef(
    _RequiredStreamDescriptionTypeDef, _OptionalStreamDescriptionTypeDef
):
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

UpdateShardCountInputRequestTypeDef = TypedDict(
    "UpdateShardCountInputRequestTypeDef",
    {
        "StreamName": str,
        "TargetShardCount": int,
        "ScalingType": Literal["UNIFORM_SCALING"],
    },
)

UpdateShardCountOutputTypeDef = TypedDict(
    "UpdateShardCountOutputTypeDef",
    {
        "StreamName": str,
        "CurrentShardCount": int,
        "TargetShardCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
