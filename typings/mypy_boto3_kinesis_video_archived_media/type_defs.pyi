"""
Type annotations for kinesis-video-archived-media service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_kinesis_video_archived_media.type_defs import TimestampTypeDef

    data: TimestampTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from botocore.response import StreamingBody

from .literals import (
    ClipFragmentSelectorTypeType,
    ContainerFormatType,
    DASHDisplayFragmentNumberType,
    DASHDisplayFragmentTimestampType,
    DASHFragmentSelectorTypeType,
    DASHPlaybackModeType,
    FormatType,
    FragmentSelectorTypeType,
    HLSDiscontinuityModeType,
    HLSDisplayFragmentTimestampType,
    HLSFragmentSelectorTypeType,
    HLSPlaybackModeType,
    ImageErrorType,
    ImageSelectorTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ClipFragmentSelectorTypeDef",
    "ClipTimestampRangeTypeDef",
    "DASHFragmentSelectorTypeDef",
    "DASHTimestampRangeTypeDef",
    "FragmentSelectorTypeDef",
    "FragmentTypeDef",
    "GetClipInputTypeDef",
    "GetClipOutputTypeDef",
    "GetDASHStreamingSessionURLInputTypeDef",
    "GetDASHStreamingSessionURLOutputTypeDef",
    "GetHLSStreamingSessionURLInputTypeDef",
    "GetHLSStreamingSessionURLOutputTypeDef",
    "GetImagesInputPaginateTypeDef",
    "GetImagesInputTypeDef",
    "GetImagesOutputTypeDef",
    "GetMediaForFragmentListInputTypeDef",
    "GetMediaForFragmentListOutputTypeDef",
    "HLSFragmentSelectorTypeDef",
    "HLSTimestampRangeTypeDef",
    "ImageTypeDef",
    "ListFragmentsInputPaginateTypeDef",
    "ListFragmentsInputTypeDef",
    "ListFragmentsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampRangeTypeDef",
    "TimestampTypeDef",
)

TimestampTypeDef = Union[datetime, str]

class FragmentTypeDef(TypedDict):
    FragmentNumber: NotRequired[str]
    FragmentSizeInBytes: NotRequired[int]
    ProducerTimestamp: NotRequired[datetime]
    ServerTimestamp: NotRequired[datetime]
    FragmentLengthInMilliseconds: NotRequired[int]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ImageTypeDef(TypedDict):
    TimeStamp: NotRequired[datetime]
    Error: NotRequired[ImageErrorType]
    ImageContent: NotRequired[str]

class GetMediaForFragmentListInputTypeDef(TypedDict):
    Fragments: Sequence[str]
    StreamName: NotRequired[str]
    StreamARN: NotRequired[str]

class ClipTimestampRangeTypeDef(TypedDict):
    StartTimestamp: TimestampTypeDef
    EndTimestamp: TimestampTypeDef

class DASHTimestampRangeTypeDef(TypedDict):
    StartTimestamp: NotRequired[TimestampTypeDef]
    EndTimestamp: NotRequired[TimestampTypeDef]

class GetImagesInputTypeDef(TypedDict):
    ImageSelectorType: ImageSelectorTypeType
    StartTimestamp: TimestampTypeDef
    EndTimestamp: TimestampTypeDef
    Format: FormatType
    StreamName: NotRequired[str]
    StreamARN: NotRequired[str]
    SamplingInterval: NotRequired[int]
    FormatConfig: NotRequired[Mapping[Literal["JPEGQuality"], str]]
    WidthPixels: NotRequired[int]
    HeightPixels: NotRequired[int]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class HLSTimestampRangeTypeDef(TypedDict):
    StartTimestamp: NotRequired[TimestampTypeDef]
    EndTimestamp: NotRequired[TimestampTypeDef]

class TimestampRangeTypeDef(TypedDict):
    StartTimestamp: TimestampTypeDef
    EndTimestamp: TimestampTypeDef

class GetClipOutputTypeDef(TypedDict):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetDASHStreamingSessionURLOutputTypeDef(TypedDict):
    DASHStreamingSessionURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetHLSStreamingSessionURLOutputTypeDef(TypedDict):
    HLSStreamingSessionURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMediaForFragmentListOutputTypeDef(TypedDict):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ListFragmentsOutputTypeDef(TypedDict):
    Fragments: List[FragmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetImagesInputPaginateTypeDef(TypedDict):
    ImageSelectorType: ImageSelectorTypeType
    StartTimestamp: TimestampTypeDef
    EndTimestamp: TimestampTypeDef
    Format: FormatType
    StreamName: NotRequired[str]
    StreamARN: NotRequired[str]
    SamplingInterval: NotRequired[int]
    FormatConfig: NotRequired[Mapping[Literal["JPEGQuality"], str]]
    WidthPixels: NotRequired[int]
    HeightPixels: NotRequired[int]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetImagesOutputTypeDef(TypedDict):
    Images: List[ImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ClipFragmentSelectorTypeDef(TypedDict):
    FragmentSelectorType: ClipFragmentSelectorTypeType
    TimestampRange: ClipTimestampRangeTypeDef

class DASHFragmentSelectorTypeDef(TypedDict):
    FragmentSelectorType: NotRequired[DASHFragmentSelectorTypeType]
    TimestampRange: NotRequired[DASHTimestampRangeTypeDef]

class HLSFragmentSelectorTypeDef(TypedDict):
    FragmentSelectorType: NotRequired[HLSFragmentSelectorTypeType]
    TimestampRange: NotRequired[HLSTimestampRangeTypeDef]

class FragmentSelectorTypeDef(TypedDict):
    FragmentSelectorType: FragmentSelectorTypeType
    TimestampRange: TimestampRangeTypeDef

class GetClipInputTypeDef(TypedDict):
    ClipFragmentSelector: ClipFragmentSelectorTypeDef
    StreamName: NotRequired[str]
    StreamARN: NotRequired[str]

class GetDASHStreamingSessionURLInputTypeDef(TypedDict):
    StreamName: NotRequired[str]
    StreamARN: NotRequired[str]
    PlaybackMode: NotRequired[DASHPlaybackModeType]
    DisplayFragmentTimestamp: NotRequired[DASHDisplayFragmentTimestampType]
    DisplayFragmentNumber: NotRequired[DASHDisplayFragmentNumberType]
    DASHFragmentSelector: NotRequired[DASHFragmentSelectorTypeDef]
    Expires: NotRequired[int]
    MaxManifestFragmentResults: NotRequired[int]

class GetHLSStreamingSessionURLInputTypeDef(TypedDict):
    StreamName: NotRequired[str]
    StreamARN: NotRequired[str]
    PlaybackMode: NotRequired[HLSPlaybackModeType]
    HLSFragmentSelector: NotRequired[HLSFragmentSelectorTypeDef]
    ContainerFormat: NotRequired[ContainerFormatType]
    DiscontinuityMode: NotRequired[HLSDiscontinuityModeType]
    DisplayFragmentTimestamp: NotRequired[HLSDisplayFragmentTimestampType]
    Expires: NotRequired[int]
    MaxMediaPlaylistFragmentResults: NotRequired[int]

class ListFragmentsInputPaginateTypeDef(TypedDict):
    StreamName: NotRequired[str]
    StreamARN: NotRequired[str]
    FragmentSelector: NotRequired[FragmentSelectorTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFragmentsInputTypeDef(TypedDict):
    StreamName: NotRequired[str]
    StreamARN: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    FragmentSelector: NotRequired[FragmentSelectorTypeDef]
