"""
Type annotations for kinesis-video-archived-media service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesis_video_archived_media.type_defs import ClipFragmentSelectorTypeDef

    data: ClipFragmentSelectorTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ClipFragmentSelectorTypeType,
    ContainerFormatType,
    DASHDisplayFragmentNumberType,
    DASHDisplayFragmentTimestampType,
    DASHFragmentSelectorTypeType,
    DASHPlaybackModeType,
    FragmentSelectorTypeType,
    HLSDiscontinuityModeType,
    HLSDisplayFragmentTimestampType,
    HLSFragmentSelectorTypeType,
    HLSPlaybackModeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ClipFragmentSelectorTypeDef",
    "ClipTimestampRangeTypeDef",
    "DASHFragmentSelectorTypeDef",
    "DASHTimestampRangeTypeDef",
    "FragmentSelectorTypeDef",
    "FragmentTypeDef",
    "GetClipInputRequestTypeDef",
    "GetClipOutputTypeDef",
    "GetDASHStreamingSessionURLInputRequestTypeDef",
    "GetDASHStreamingSessionURLOutputTypeDef",
    "GetHLSStreamingSessionURLInputRequestTypeDef",
    "GetHLSStreamingSessionURLOutputTypeDef",
    "GetMediaForFragmentListInputRequestTypeDef",
    "GetMediaForFragmentListOutputTypeDef",
    "HLSFragmentSelectorTypeDef",
    "HLSTimestampRangeTypeDef",
    "ListFragmentsInputRequestTypeDef",
    "ListFragmentsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampRangeTypeDef",
)

ClipFragmentSelectorTypeDef = TypedDict(
    "ClipFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": ClipFragmentSelectorTypeType,
        "TimestampRange": "ClipTimestampRangeTypeDef",
    },
)

ClipTimestampRangeTypeDef = TypedDict(
    "ClipTimestampRangeTypeDef",
    {
        "StartTimestamp": Union[datetime, str],
        "EndTimestamp": Union[datetime, str],
    },
)

DASHFragmentSelectorTypeDef = TypedDict(
    "DASHFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": DASHFragmentSelectorTypeType,
        "TimestampRange": "DASHTimestampRangeTypeDef",
    },
    total=False,
)

DASHTimestampRangeTypeDef = TypedDict(
    "DASHTimestampRangeTypeDef",
    {
        "StartTimestamp": Union[datetime, str],
        "EndTimestamp": Union[datetime, str],
    },
    total=False,
)

FragmentSelectorTypeDef = TypedDict(
    "FragmentSelectorTypeDef",
    {
        "FragmentSelectorType": FragmentSelectorTypeType,
        "TimestampRange": "TimestampRangeTypeDef",
    },
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

_RequiredGetClipInputRequestTypeDef = TypedDict(
    "_RequiredGetClipInputRequestTypeDef",
    {
        "ClipFragmentSelector": "ClipFragmentSelectorTypeDef",
    },
)
_OptionalGetClipInputRequestTypeDef = TypedDict(
    "_OptionalGetClipInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class GetClipInputRequestTypeDef(
    _RequiredGetClipInputRequestTypeDef, _OptionalGetClipInputRequestTypeDef
):
    pass

GetClipOutputTypeDef = TypedDict(
    "GetClipOutputTypeDef",
    {
        "ContentType": str,
        "Payload": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDASHStreamingSessionURLInputRequestTypeDef = TypedDict(
    "GetDASHStreamingSessionURLInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "PlaybackMode": DASHPlaybackModeType,
        "DisplayFragmentTimestamp": DASHDisplayFragmentTimestampType,
        "DisplayFragmentNumber": DASHDisplayFragmentNumberType,
        "DASHFragmentSelector": "DASHFragmentSelectorTypeDef",
        "Expires": int,
        "MaxManifestFragmentResults": int,
    },
    total=False,
)

GetDASHStreamingSessionURLOutputTypeDef = TypedDict(
    "GetDASHStreamingSessionURLOutputTypeDef",
    {
        "DASHStreamingSessionURL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHLSStreamingSessionURLInputRequestTypeDef = TypedDict(
    "GetHLSStreamingSessionURLInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "PlaybackMode": HLSPlaybackModeType,
        "HLSFragmentSelector": "HLSFragmentSelectorTypeDef",
        "ContainerFormat": ContainerFormatType,
        "DiscontinuityMode": HLSDiscontinuityModeType,
        "DisplayFragmentTimestamp": HLSDisplayFragmentTimestampType,
        "Expires": int,
        "MaxMediaPlaylistFragmentResults": int,
    },
    total=False,
)

GetHLSStreamingSessionURLOutputTypeDef = TypedDict(
    "GetHLSStreamingSessionURLOutputTypeDef",
    {
        "HLSStreamingSessionURL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMediaForFragmentListInputRequestTypeDef = TypedDict(
    "_RequiredGetMediaForFragmentListInputRequestTypeDef",
    {
        "Fragments": List[str],
    },
)
_OptionalGetMediaForFragmentListInputRequestTypeDef = TypedDict(
    "_OptionalGetMediaForFragmentListInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class GetMediaForFragmentListInputRequestTypeDef(
    _RequiredGetMediaForFragmentListInputRequestTypeDef,
    _OptionalGetMediaForFragmentListInputRequestTypeDef,
):
    pass

GetMediaForFragmentListOutputTypeDef = TypedDict(
    "GetMediaForFragmentListOutputTypeDef",
    {
        "ContentType": str,
        "Payload": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HLSFragmentSelectorTypeDef = TypedDict(
    "HLSFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": HLSFragmentSelectorTypeType,
        "TimestampRange": "HLSTimestampRangeTypeDef",
    },
    total=False,
)

HLSTimestampRangeTypeDef = TypedDict(
    "HLSTimestampRangeTypeDef",
    {
        "StartTimestamp": Union[datetime, str],
        "EndTimestamp": Union[datetime, str],
    },
    total=False,
)

ListFragmentsInputRequestTypeDef = TypedDict(
    "ListFragmentsInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "MaxResults": int,
        "NextToken": str,
        "FragmentSelector": "FragmentSelectorTypeDef",
    },
    total=False,
)

ListFragmentsOutputTypeDef = TypedDict(
    "ListFragmentsOutputTypeDef",
    {
        "Fragments": List["FragmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

TimestampRangeTypeDef = TypedDict(
    "TimestampRangeTypeDef",
    {
        "StartTimestamp": Union[datetime, str],
        "EndTimestamp": Union[datetime, str],
    },
)
