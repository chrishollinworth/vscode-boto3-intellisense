"""
Main interface for dynamodbstreams service type definitions.

Usage::

    ```python
    from mypy_boto3_dynamodbstreams.type_defs import IdentityTypeDef

    data: IdentityTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "IdentityTypeDef",
    "KeySchemaElementTypeDef",
    "RecordTypeDef",
    "ResponseMetadata",
    "SequenceNumberRangeTypeDef",
    "ShardTypeDef",
    "StreamDescriptionTypeDef",
    "StreamRecordTypeDef",
    "StreamTypeDef",
    "DescribeStreamOutputTypeDef",
    "AttributeValueTypeDef",
    "GetRecordsOutputTypeDef",
    "GetShardIteratorOutputTypeDef",
    "ListStreamsOutputTypeDef",
)

IdentityTypeDef = TypedDict("IdentityTypeDef", {"PrincipalId": str, "Type": str}, total=False)

KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef", {"AttributeName": str, "KeyType": Literal["HASH", "RANGE"]}
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "eventID": str,
        "eventName": Literal["INSERT", "MODIFY", "REMOVE"],
        "eventVersion": str,
        "eventSource": str,
        "awsRegion": str,
        "dynamodb": "StreamRecordTypeDef",
        "userIdentity": "IdentityTypeDef",
    },
    total=False,
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

SequenceNumberRangeTypeDef = TypedDict(
    "SequenceNumberRangeTypeDef",
    {"StartingSequenceNumber": str, "EndingSequenceNumber": str},
    total=False,
)

ShardTypeDef = TypedDict(
    "ShardTypeDef",
    {"ShardId": str, "SequenceNumberRange": "SequenceNumberRangeTypeDef", "ParentShardId": str},
    total=False,
)

StreamDescriptionTypeDef = TypedDict(
    "StreamDescriptionTypeDef",
    {
        "StreamArn": str,
        "StreamLabel": str,
        "StreamStatus": Literal["ENABLING", "ENABLED", "DISABLING", "DISABLED"],
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
        "CreationRequestDateTime": datetime,
        "TableName": str,
        "KeySchema": List["KeySchemaElementTypeDef"],
        "Shards": List["ShardTypeDef"],
        "LastEvaluatedShardId": str,
    },
    total=False,
)

StreamRecordTypeDef = TypedDict(
    "StreamRecordTypeDef",
    {
        "ApproximateCreationDateTime": datetime,
        "Keys": Dict[str, Dict[str, Any]],
        "NewImage": Dict[str, Dict[str, Any]],
        "OldImage": Dict[str, Dict[str, Any]],
        "SequenceNumber": str,
        "SizeBytes": int,
        "StreamViewType": Literal["NEW_IMAGE", "OLD_IMAGE", "NEW_AND_OLD_IMAGES", "KEYS_ONLY"],
    },
    total=False,
)

StreamTypeDef = TypedDict(
    "StreamTypeDef", {"StreamArn": str, "TableName": str, "StreamLabel": str}, total=False
)

DescribeStreamOutputTypeDef = TypedDict(
    "DescribeStreamOutputTypeDef",
    {"StreamDescription": "StreamDescriptionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "S": str,
        "N": str,
        "B": Union[bytes, IO[bytes]],
        "SS": List[str],
        "NS": List[str],
        "BS": List[Union[bytes, IO[bytes]]],
        "M": Dict[str, Dict[str, Any]],
        "L": List[Dict[str, Any]],
        "NULL": bool,
        "BOOL": bool,
    },
    total=False,
)

GetRecordsOutputTypeDef = TypedDict(
    "GetRecordsOutputTypeDef",
    {
        "Records": List["RecordTypeDef"],
        "NextShardIterator": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetShardIteratorOutputTypeDef = TypedDict(
    "GetShardIteratorOutputTypeDef",
    {"ShardIterator": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {
        "Streams": List["StreamTypeDef"],
        "LastEvaluatedStreamArn": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)
