"""
Main interface for kinesis-video-archived-media service type definitions.

Usage::

    ```python
    from mypy_boto3_kinesis_video_archived_media.type_defs import ClipTimestampRangeTypeDef

    data: ClipTimestampRangeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClipTimestampRangeTypeDef",
    "DASHTimestampRangeTypeDef",
    "FragmentTypeDef",
    "HLSTimestampRangeTypeDef",
    "ResponseMetadata",
    "TimestampRangeTypeDef",
    "ClipFragmentSelectorTypeDef",
    "DASHFragmentSelectorTypeDef",
    "FragmentSelectorTypeDef",
    "GetClipOutputTypeDef",
    "GetDASHStreamingSessionURLOutputTypeDef",
    "GetHLSStreamingSessionURLOutputTypeDef",
    "GetMediaForFragmentListOutputTypeDef",
    "HLSFragmentSelectorTypeDef",
    "ListFragmentsOutputTypeDef",
    "PaginatorConfigTypeDef",
)

ClipTimestampRangeTypeDef = TypedDict(
    "ClipTimestampRangeTypeDef", {"StartTimestamp": datetime, "EndTimestamp": datetime}
)

DASHTimestampRangeTypeDef = TypedDict(
    "DASHTimestampRangeTypeDef", {"StartTimestamp": datetime, "EndTimestamp": datetime}, total=False
)

FragmentTypeDef = TypedDict(
    "FragmentTypeDef",
    {
        "FragmentNumber": str,
        "FragmentSizeInBytes": int,
        "ProducerTimestamp": datetime,
        "ServerTimestamp": datetime,
        "FragmentLengthInMilliseconds": int,
    },
    total=False,
)

HLSTimestampRangeTypeDef = TypedDict(
    "HLSTimestampRangeTypeDef", {"StartTimestamp": datetime, "EndTimestamp": datetime}, total=False
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

TimestampRangeTypeDef = TypedDict(
    "TimestampRangeTypeDef", {"StartTimestamp": datetime, "EndTimestamp": datetime}
)

ClipFragmentSelectorTypeDef = TypedDict(
    "ClipFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"],
        "TimestampRange": "ClipTimestampRangeTypeDef",
    },
)

DASHFragmentSelectorTypeDef = TypedDict(
    "DASHFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"],
        "TimestampRange": "DASHTimestampRangeTypeDef",
    },
    total=False,
)

FragmentSelectorTypeDef = TypedDict(
    "FragmentSelectorTypeDef",
    {
        "FragmentSelectorType": Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"],
        "TimestampRange": "TimestampRangeTypeDef",
    },
)

GetClipOutputTypeDef = TypedDict(
    "GetClipOutputTypeDef",
    {"ContentType": str, "Payload": IO[bytes], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetDASHStreamingSessionURLOutputTypeDef = TypedDict(
    "GetDASHStreamingSessionURLOutputTypeDef",
    {"DASHStreamingSessionURL": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetHLSStreamingSessionURLOutputTypeDef = TypedDict(
    "GetHLSStreamingSessionURLOutputTypeDef",
    {"HLSStreamingSessionURL": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetMediaForFragmentListOutputTypeDef = TypedDict(
    "GetMediaForFragmentListOutputTypeDef",
    {"ContentType": str, "Payload": IO[bytes], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

HLSFragmentSelectorTypeDef = TypedDict(
    "HLSFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"],
        "TimestampRange": "HLSTimestampRangeTypeDef",
    },
    total=False,
)

ListFragmentsOutputTypeDef = TypedDict(
    "ListFragmentsOutputTypeDef",
    {
        "Fragments": List["FragmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
