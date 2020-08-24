"""
Main interface for kinesis service type definitions.

Usage::

    ```python
    from mypy_boto3_kinesis.type_defs import ChildShardTypeDef

    data: ChildShardTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ChildShardTypeDef",
    "ConsumerDescriptionTypeDef",
    "ConsumerTypeDef",
    "EnhancedMetricsTypeDef",
    "HashKeyRangeTypeDef",
    "InternalFailureExceptionTypeDef",
    "KMSAccessDeniedExceptionTypeDef",
    "KMSDisabledExceptionTypeDef",
    "KMSInvalidStateExceptionTypeDef",
    "KMSNotFoundExceptionTypeDef",
    "KMSOptInRequiredTypeDef",
    "KMSThrottlingExceptionTypeDef",
    "PutRecordsResultEntryTypeDef",
    "RecordTypeDef",
    "ResourceInUseExceptionTypeDef",
    "ResourceNotFoundExceptionTypeDef",
    "SequenceNumberRangeTypeDef",
    "ShardTypeDef",
    "StreamDescriptionSummaryTypeDef",
    "StreamDescriptionTypeDef",
    "SubscribeToShardEventStreamTypeDef",
    "SubscribeToShardEventTypeDef",
    "TagTypeDef",
    "DescribeLimitsOutputTypeDef",
    "DescribeStreamConsumerOutputTypeDef",
    "DescribeStreamOutputTypeDef",
    "DescribeStreamSummaryOutputTypeDef",
    "EnhancedMonitoringOutputTypeDef",
    "GetRecordsOutputTypeDef",
    "GetShardIteratorOutputTypeDef",
    "ListShardsOutputTypeDef",
    "ListStreamConsumersOutputTypeDef",
    "ListStreamsOutputTypeDef",
    "ListTagsForStreamOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PutRecordOutputTypeDef",
    "PutRecordsOutputTypeDef",
    "PutRecordsRequestEntryTypeDef",
    "RegisterStreamConsumerOutputTypeDef",
    "ShardFilterTypeDef",
    "StartingPositionTypeDef",
    "SubscribeToShardOutputTypeDef",
    "UpdateShardCountOutputTypeDef",
    "WaiterConfigTypeDef",
)

ChildShardTypeDef = TypedDict(
    "ChildShardTypeDef",
    {"ShardId": str, "ParentShards": List[str], "HashKeyRange": "HashKeyRangeTypeDef"},
)

ConsumerDescriptionTypeDef = TypedDict(
    "ConsumerDescriptionTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": Literal["CREATING", "DELETING", "ACTIVE"],
        "ConsumerCreationTimestamp": datetime,
        "StreamARN": str,
    },
)

ConsumerTypeDef = TypedDict(
    "ConsumerTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": Literal["CREATING", "DELETING", "ACTIVE"],
        "ConsumerCreationTimestamp": datetime,
    },
)

EnhancedMetricsTypeDef = TypedDict(
    "EnhancedMetricsTypeDef",
    {
        "ShardLevelMetrics": List[
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
        ]
    },
    total=False,
)

HashKeyRangeTypeDef = TypedDict(
    "HashKeyRangeTypeDef", {"StartingHashKey": str, "EndingHashKey": str}
)

InternalFailureExceptionTypeDef = TypedDict(
    "InternalFailureExceptionTypeDef", {"message": str}, total=False
)

KMSAccessDeniedExceptionTypeDef = TypedDict(
    "KMSAccessDeniedExceptionTypeDef", {"message": str}, total=False
)

KMSDisabledExceptionTypeDef = TypedDict(
    "KMSDisabledExceptionTypeDef", {"message": str}, total=False
)

KMSInvalidStateExceptionTypeDef = TypedDict(
    "KMSInvalidStateExceptionTypeDef", {"message": str}, total=False
)

KMSNotFoundExceptionTypeDef = TypedDict(
    "KMSNotFoundExceptionTypeDef", {"message": str}, total=False
)

KMSOptInRequiredTypeDef = TypedDict("KMSOptInRequiredTypeDef", {"message": str}, total=False)

KMSThrottlingExceptionTypeDef = TypedDict(
    "KMSThrottlingExceptionTypeDef", {"message": str}, total=False
)

PutRecordsResultEntryTypeDef = TypedDict(
    "PutRecordsResultEntryTypeDef",
    {"SequenceNumber": str, "ShardId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

_RequiredRecordTypeDef = TypedDict(
    "_RequiredRecordTypeDef", {"SequenceNumber": str, "Data": bytes, "PartitionKey": str}
)
_OptionalRecordTypeDef = TypedDict(
    "_OptionalRecordTypeDef",
    {"ApproximateArrivalTimestamp": datetime, "EncryptionType": Literal["NONE", "KMS"]},
    total=False,
)


class RecordTypeDef(_RequiredRecordTypeDef, _OptionalRecordTypeDef):
    pass


ResourceInUseExceptionTypeDef = TypedDict(
    "ResourceInUseExceptionTypeDef", {"message": str}, total=False
)

ResourceNotFoundExceptionTypeDef = TypedDict(
    "ResourceNotFoundExceptionTypeDef", {"message": str}, total=False
)

_RequiredSequenceNumberRangeTypeDef = TypedDict(
    "_RequiredSequenceNumberRangeTypeDef", {"StartingSequenceNumber": str}
)
_OptionalSequenceNumberRangeTypeDef = TypedDict(
    "_OptionalSequenceNumberRangeTypeDef", {"EndingSequenceNumber": str}, total=False
)


class SequenceNumberRangeTypeDef(
    _RequiredSequenceNumberRangeTypeDef, _OptionalSequenceNumberRangeTypeDef
):
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
    "_OptionalShardTypeDef", {"ParentShardId": str, "AdjacentParentShardId": str}, total=False
)


class ShardTypeDef(_RequiredShardTypeDef, _OptionalShardTypeDef):
    pass


_RequiredStreamDescriptionSummaryTypeDef = TypedDict(
    "_RequiredStreamDescriptionSummaryTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": Literal["CREATING", "DELETING", "ACTIVE", "UPDATING"],
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List["EnhancedMetricsTypeDef"],
        "OpenShardCount": int,
    },
)
_OptionalStreamDescriptionSummaryTypeDef = TypedDict(
    "_OptionalStreamDescriptionSummaryTypeDef",
    {"EncryptionType": Literal["NONE", "KMS"], "KeyId": str, "ConsumerCount": int},
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
        "StreamStatus": Literal["CREATING", "DELETING", "ACTIVE", "UPDATING"],
        "Shards": List["ShardTypeDef"],
        "HasMoreShards": bool,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List["EnhancedMetricsTypeDef"],
    },
)
_OptionalStreamDescriptionTypeDef = TypedDict(
    "_OptionalStreamDescriptionTypeDef",
    {"EncryptionType": Literal["NONE", "KMS"], "KeyId": str},
    total=False,
)


class StreamDescriptionTypeDef(
    _RequiredStreamDescriptionTypeDef, _OptionalStreamDescriptionTypeDef
):
    pass


_RequiredSubscribeToShardEventStreamTypeDef = TypedDict(
    "_RequiredSubscribeToShardEventStreamTypeDef",
    {"SubscribeToShardEvent": "SubscribeToShardEventTypeDef"},
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
    "_OptionalSubscribeToShardEventTypeDef", {"ChildShards": List["ChildShardTypeDef"]}, total=False
)


class SubscribeToShardEventTypeDef(
    _RequiredSubscribeToShardEventTypeDef, _OptionalSubscribeToShardEventTypeDef
):
    pass


_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


DescribeLimitsOutputTypeDef = TypedDict(
    "DescribeLimitsOutputTypeDef", {"ShardLimit": int, "OpenShardCount": int}
)

DescribeStreamConsumerOutputTypeDef = TypedDict(
    "DescribeStreamConsumerOutputTypeDef", {"ConsumerDescription": "ConsumerDescriptionTypeDef"}
)

DescribeStreamOutputTypeDef = TypedDict(
    "DescribeStreamOutputTypeDef", {"StreamDescription": "StreamDescriptionTypeDef"}
)

DescribeStreamSummaryOutputTypeDef = TypedDict(
    "DescribeStreamSummaryOutputTypeDef",
    {"StreamDescriptionSummary": "StreamDescriptionSummaryTypeDef"},
)

EnhancedMonitoringOutputTypeDef = TypedDict(
    "EnhancedMonitoringOutputTypeDef",
    {
        "StreamName": str,
        "CurrentShardLevelMetrics": List[
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
        "DesiredShardLevelMetrics": List[
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
    },
    total=False,
)

_RequiredGetRecordsOutputTypeDef = TypedDict(
    "_RequiredGetRecordsOutputTypeDef", {"Records": List["RecordTypeDef"]}
)
_OptionalGetRecordsOutputTypeDef = TypedDict(
    "_OptionalGetRecordsOutputTypeDef",
    {"NextShardIterator": str, "MillisBehindLatest": int, "ChildShards": List["ChildShardTypeDef"]},
    total=False,
)


class GetRecordsOutputTypeDef(_RequiredGetRecordsOutputTypeDef, _OptionalGetRecordsOutputTypeDef):
    pass


GetShardIteratorOutputTypeDef = TypedDict(
    "GetShardIteratorOutputTypeDef", {"ShardIterator": str}, total=False
)

ListShardsOutputTypeDef = TypedDict(
    "ListShardsOutputTypeDef", {"Shards": List["ShardTypeDef"], "NextToken": str}, total=False
)

ListStreamConsumersOutputTypeDef = TypedDict(
    "ListStreamConsumersOutputTypeDef",
    {"Consumers": List["ConsumerTypeDef"], "NextToken": str},
    total=False,
)

ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef", {"StreamNames": List[str], "HasMoreStreams": bool}
)

ListTagsForStreamOutputTypeDef = TypedDict(
    "ListTagsForStreamOutputTypeDef", {"Tags": List["TagTypeDef"], "HasMoreTags": bool}
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredPutRecordOutputTypeDef = TypedDict(
    "_RequiredPutRecordOutputTypeDef", {"ShardId": str, "SequenceNumber": str}
)
_OptionalPutRecordOutputTypeDef = TypedDict(
    "_OptionalPutRecordOutputTypeDef", {"EncryptionType": Literal["NONE", "KMS"]}, total=False
)


class PutRecordOutputTypeDef(_RequiredPutRecordOutputTypeDef, _OptionalPutRecordOutputTypeDef):
    pass


_RequiredPutRecordsOutputTypeDef = TypedDict(
    "_RequiredPutRecordsOutputTypeDef", {"Records": List["PutRecordsResultEntryTypeDef"]}
)
_OptionalPutRecordsOutputTypeDef = TypedDict(
    "_OptionalPutRecordsOutputTypeDef",
    {"FailedRecordCount": int, "EncryptionType": Literal["NONE", "KMS"]},
    total=False,
)


class PutRecordsOutputTypeDef(_RequiredPutRecordsOutputTypeDef, _OptionalPutRecordsOutputTypeDef):
    pass


_RequiredPutRecordsRequestEntryTypeDef = TypedDict(
    "_RequiredPutRecordsRequestEntryTypeDef", {"Data": bytes, "PartitionKey": str}
)
_OptionalPutRecordsRequestEntryTypeDef = TypedDict(
    "_OptionalPutRecordsRequestEntryTypeDef", {"ExplicitHashKey": str}, total=False
)


class PutRecordsRequestEntryTypeDef(
    _RequiredPutRecordsRequestEntryTypeDef, _OptionalPutRecordsRequestEntryTypeDef
):
    pass


RegisterStreamConsumerOutputTypeDef = TypedDict(
    "RegisterStreamConsumerOutputTypeDef", {"Consumer": "ConsumerTypeDef"}
)

_RequiredShardFilterTypeDef = TypedDict(
    "_RequiredShardFilterTypeDef",
    {
        "Type": Literal[
            "AFTER_SHARD_ID",
            "AT_TRIM_HORIZON",
            "FROM_TRIM_HORIZON",
            "AT_LATEST",
            "AT_TIMESTAMP",
            "FROM_TIMESTAMP",
        ]
    },
)
_OptionalShardFilterTypeDef = TypedDict(
    "_OptionalShardFilterTypeDef", {"ShardId": str, "Timestamp": datetime}, total=False
)


class ShardFilterTypeDef(_RequiredShardFilterTypeDef, _OptionalShardFilterTypeDef):
    pass


_RequiredStartingPositionTypeDef = TypedDict(
    "_RequiredStartingPositionTypeDef",
    {
        "Type": Literal[
            "AT_SEQUENCE_NUMBER", "AFTER_SEQUENCE_NUMBER", "TRIM_HORIZON", "LATEST", "AT_TIMESTAMP"
        ]
    },
)
_OptionalStartingPositionTypeDef = TypedDict(
    "_OptionalStartingPositionTypeDef", {"SequenceNumber": str, "Timestamp": datetime}, total=False
)


class StartingPositionTypeDef(_RequiredStartingPositionTypeDef, _OptionalStartingPositionTypeDef):
    pass


SubscribeToShardOutputTypeDef = TypedDict(
    "SubscribeToShardOutputTypeDef", {"EventStream": "SubscribeToShardEventStreamTypeDef"}
)

UpdateShardCountOutputTypeDef = TypedDict(
    "UpdateShardCountOutputTypeDef",
    {"StreamName": str, "CurrentShardCount": int, "TargetShardCount": int},
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
