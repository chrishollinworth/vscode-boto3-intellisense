"""
Type annotations for ivs service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_ivs.type_defs import AudioConfigurationTypeDef

    data: AudioConfigurationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ChannelLatencyModeType,
    ChannelTypeType,
    ContainerFormatType,
    MultitrackMaximumResolutionType,
    MultitrackPolicyType,
    RecordingConfigurationStateType,
    RecordingModeType,
    RenditionConfigurationRenditionSelectionType,
    RenditionConfigurationRenditionType,
    StreamHealthType,
    StreamStateType,
    ThumbnailConfigurationResolutionType,
    ThumbnailConfigurationStorageType,
    TranscodePresetType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AudioConfigurationTypeDef",
    "BatchErrorTypeDef",
    "BatchGetChannelRequestTypeDef",
    "BatchGetChannelResponseTypeDef",
    "BatchGetStreamKeyRequestTypeDef",
    "BatchGetStreamKeyResponseTypeDef",
    "BatchStartViewerSessionRevocationErrorTypeDef",
    "BatchStartViewerSessionRevocationRequestTypeDef",
    "BatchStartViewerSessionRevocationResponseTypeDef",
    "BatchStartViewerSessionRevocationViewerSessionTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "CreateChannelRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreatePlaybackRestrictionPolicyRequestTypeDef",
    "CreatePlaybackRestrictionPolicyResponseTypeDef",
    "CreateRecordingConfigurationRequestTypeDef",
    "CreateRecordingConfigurationResponseTypeDef",
    "CreateStreamKeyRequestTypeDef",
    "CreateStreamKeyResponseTypeDef",
    "DeleteChannelRequestTypeDef",
    "DeletePlaybackKeyPairRequestTypeDef",
    "DeletePlaybackRestrictionPolicyRequestTypeDef",
    "DeleteRecordingConfigurationRequestTypeDef",
    "DeleteStreamKeyRequestTypeDef",
    "DestinationConfigurationTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetChannelRequestTypeDef",
    "GetChannelResponseTypeDef",
    "GetPlaybackKeyPairRequestTypeDef",
    "GetPlaybackKeyPairResponseTypeDef",
    "GetPlaybackRestrictionPolicyRequestTypeDef",
    "GetPlaybackRestrictionPolicyResponseTypeDef",
    "GetRecordingConfigurationRequestTypeDef",
    "GetRecordingConfigurationResponseTypeDef",
    "GetStreamKeyRequestTypeDef",
    "GetStreamKeyResponseTypeDef",
    "GetStreamRequestTypeDef",
    "GetStreamResponseTypeDef",
    "GetStreamSessionRequestTypeDef",
    "GetStreamSessionResponseTypeDef",
    "ImportPlaybackKeyPairRequestTypeDef",
    "ImportPlaybackKeyPairResponseTypeDef",
    "IngestConfigurationTypeDef",
    "IngestConfigurationsTypeDef",
    "ListChannelsRequestPaginateTypeDef",
    "ListChannelsRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListPlaybackKeyPairsRequestPaginateTypeDef",
    "ListPlaybackKeyPairsRequestTypeDef",
    "ListPlaybackKeyPairsResponseTypeDef",
    "ListPlaybackRestrictionPoliciesRequestTypeDef",
    "ListPlaybackRestrictionPoliciesResponseTypeDef",
    "ListRecordingConfigurationsRequestPaginateTypeDef",
    "ListRecordingConfigurationsRequestTypeDef",
    "ListRecordingConfigurationsResponseTypeDef",
    "ListStreamKeysRequestPaginateTypeDef",
    "ListStreamKeysRequestTypeDef",
    "ListStreamKeysResponseTypeDef",
    "ListStreamSessionsRequestTypeDef",
    "ListStreamSessionsResponseTypeDef",
    "ListStreamsRequestPaginateTypeDef",
    "ListStreamsRequestTypeDef",
    "ListStreamsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MultitrackInputConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PlaybackKeyPairSummaryTypeDef",
    "PlaybackKeyPairTypeDef",
    "PlaybackRestrictionPolicySummaryTypeDef",
    "PlaybackRestrictionPolicyTypeDef",
    "PutMetadataRequestTypeDef",
    "RecordingConfigurationSummaryTypeDef",
    "RecordingConfigurationTypeDef",
    "RenditionConfigurationOutputTypeDef",
    "RenditionConfigurationTypeDef",
    "RenditionConfigurationUnionTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationConfigurationTypeDef",
    "SrtTypeDef",
    "StartViewerSessionRevocationRequestTypeDef",
    "StopStreamRequestTypeDef",
    "StreamEventTypeDef",
    "StreamFiltersTypeDef",
    "StreamKeySummaryTypeDef",
    "StreamKeyTypeDef",
    "StreamSessionSummaryTypeDef",
    "StreamSessionTypeDef",
    "StreamSummaryTypeDef",
    "StreamTypeDef",
    "TagResourceRequestTypeDef",
    "ThumbnailConfigurationOutputTypeDef",
    "ThumbnailConfigurationTypeDef",
    "ThumbnailConfigurationUnionTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateChannelRequestTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdatePlaybackRestrictionPolicyRequestTypeDef",
    "UpdatePlaybackRestrictionPolicyResponseTypeDef",
    "VideoConfigurationTypeDef",
)

class AudioConfigurationTypeDef(TypedDict):
    channels: NotRequired[int]
    codec: NotRequired[str]
    sampleRate: NotRequired[int]
    targetBitrate: NotRequired[int]
    track: NotRequired[str]

class BatchErrorTypeDef(TypedDict):
    arn: NotRequired[str]
    code: NotRequired[str]
    message: NotRequired[str]

class BatchGetChannelRequestTypeDef(TypedDict):
    arns: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BatchGetStreamKeyRequestTypeDef(TypedDict):
    arns: Sequence[str]

class StreamKeyTypeDef(TypedDict):
    arn: NotRequired[str]
    channelArn: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    value: NotRequired[str]

class BatchStartViewerSessionRevocationErrorTypeDef(TypedDict):
    channelArn: str
    viewerId: str
    code: NotRequired[str]
    message: NotRequired[str]

class BatchStartViewerSessionRevocationViewerSessionTypeDef(TypedDict):
    channelArn: str
    viewerId: str
    viewerSessionVersionsLessThanOrEqualTo: NotRequired[int]

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "authorized": NotRequired[bool],
        "insecureIngest": NotRequired[bool],
        "latencyMode": NotRequired[ChannelLatencyModeType],
        "name": NotRequired[str],
        "playbackRestrictionPolicyArn": NotRequired[str],
        "preset": NotRequired[TranscodePresetType],
        "recordingConfigurationArn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "type": NotRequired[ChannelTypeType],
    },
)

class MultitrackInputConfigurationTypeDef(TypedDict):
    enabled: NotRequired[bool]
    maximumResolution: NotRequired[MultitrackMaximumResolutionType]
    policy: NotRequired[MultitrackPolicyType]

class SrtTypeDef(TypedDict):
    endpoint: NotRequired[str]
    passphrase: NotRequired[str]

class CreatePlaybackRestrictionPolicyRequestTypeDef(TypedDict):
    allowedCountries: NotRequired[Sequence[str]]
    allowedOrigins: NotRequired[Sequence[str]]
    enableStrictOriginEnforcement: NotRequired[bool]
    name: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class PlaybackRestrictionPolicyTypeDef(TypedDict):
    allowedCountries: List[str]
    allowedOrigins: List[str]
    arn: str
    enableStrictOriginEnforcement: NotRequired[bool]
    name: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class CreateStreamKeyRequestTypeDef(TypedDict):
    channelArn: str
    tags: NotRequired[Mapping[str, str]]

class DeleteChannelRequestTypeDef(TypedDict):
    arn: str

class DeletePlaybackKeyPairRequestTypeDef(TypedDict):
    arn: str

class DeletePlaybackRestrictionPolicyRequestTypeDef(TypedDict):
    arn: str

class DeleteRecordingConfigurationRequestTypeDef(TypedDict):
    arn: str

class DeleteStreamKeyRequestTypeDef(TypedDict):
    arn: str

class S3DestinationConfigurationTypeDef(TypedDict):
    bucketName: str

class GetChannelRequestTypeDef(TypedDict):
    arn: str

class GetPlaybackKeyPairRequestTypeDef(TypedDict):
    arn: str

class PlaybackKeyPairTypeDef(TypedDict):
    arn: NotRequired[str]
    fingerprint: NotRequired[str]
    name: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class GetPlaybackRestrictionPolicyRequestTypeDef(TypedDict):
    arn: str

class GetRecordingConfigurationRequestTypeDef(TypedDict):
    arn: str

class GetStreamKeyRequestTypeDef(TypedDict):
    arn: str

class GetStreamRequestTypeDef(TypedDict):
    channelArn: str

class StreamTypeDef(TypedDict):
    channelArn: NotRequired[str]
    health: NotRequired[StreamHealthType]
    playbackUrl: NotRequired[str]
    startTime: NotRequired[datetime]
    state: NotRequired[StreamStateType]
    streamId: NotRequired[str]
    viewerCount: NotRequired[int]

class GetStreamSessionRequestTypeDef(TypedDict):
    channelArn: str
    streamId: NotRequired[str]

class ImportPlaybackKeyPairRequestTypeDef(TypedDict):
    publicKeyMaterial: str
    name: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class VideoConfigurationTypeDef(TypedDict):
    avcLevel: NotRequired[str]
    avcProfile: NotRequired[str]
    codec: NotRequired[str]
    encoder: NotRequired[str]
    level: NotRequired[str]
    profile: NotRequired[str]
    targetBitrate: NotRequired[int]
    targetFramerate: NotRequired[int]
    track: NotRequired[str]
    videoHeight: NotRequired[int]
    videoWidth: NotRequired[int]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListChannelsRequestTypeDef(TypedDict):
    filterByName: NotRequired[str]
    filterByPlaybackRestrictionPolicyArn: NotRequired[str]
    filterByRecordingConfigurationArn: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListPlaybackKeyPairsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class PlaybackKeyPairSummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class ListPlaybackRestrictionPoliciesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class PlaybackRestrictionPolicySummaryTypeDef(TypedDict):
    allowedCountries: List[str]
    allowedOrigins: List[str]
    arn: str
    enableStrictOriginEnforcement: NotRequired[bool]
    name: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class ListRecordingConfigurationsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListStreamKeysRequestTypeDef(TypedDict):
    channelArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class StreamKeySummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    channelArn: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class ListStreamSessionsRequestTypeDef(TypedDict):
    channelArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class StreamSessionSummaryTypeDef(TypedDict):
    endTime: NotRequired[datetime]
    hasErrorEvent: NotRequired[bool]
    startTime: NotRequired[datetime]
    streamId: NotRequired[str]

class StreamFiltersTypeDef(TypedDict):
    health: NotRequired[StreamHealthType]

class StreamSummaryTypeDef(TypedDict):
    channelArn: NotRequired[str]
    health: NotRequired[StreamHealthType]
    startTime: NotRequired[datetime]
    state: NotRequired[StreamStateType]
    streamId: NotRequired[str]
    viewerCount: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class PutMetadataRequestTypeDef(TypedDict):
    channelArn: str
    metadata: str

class RenditionConfigurationOutputTypeDef(TypedDict):
    renditionSelection: NotRequired[RenditionConfigurationRenditionSelectionType]
    renditions: NotRequired[List[RenditionConfigurationRenditionType]]

class ThumbnailConfigurationOutputTypeDef(TypedDict):
    recordingMode: NotRequired[RecordingModeType]
    resolution: NotRequired[ThumbnailConfigurationResolutionType]
    storage: NotRequired[List[ThumbnailConfigurationStorageType]]
    targetIntervalSeconds: NotRequired[int]

class RenditionConfigurationTypeDef(TypedDict):
    renditionSelection: NotRequired[RenditionConfigurationRenditionSelectionType]
    renditions: NotRequired[Sequence[RenditionConfigurationRenditionType]]

class StartViewerSessionRevocationRequestTypeDef(TypedDict):
    channelArn: str
    viewerId: str
    viewerSessionVersionsLessThanOrEqualTo: NotRequired[int]

class StopStreamRequestTypeDef(TypedDict):
    channelArn: str

StreamEventTypeDef = TypedDict(
    "StreamEventTypeDef",
    {
        "code": NotRequired[str],
        "eventTime": NotRequired[datetime],
        "name": NotRequired[str],
        "type": NotRequired[str],
    },
)

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class ThumbnailConfigurationTypeDef(TypedDict):
    recordingMode: NotRequired[RecordingModeType]
    resolution: NotRequired[ThumbnailConfigurationResolutionType]
    storage: NotRequired[Sequence[ThumbnailConfigurationStorageType]]
    targetIntervalSeconds: NotRequired[int]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdatePlaybackRestrictionPolicyRequestTypeDef(TypedDict):
    arn: str
    allowedCountries: NotRequired[Sequence[str]]
    allowedOrigins: NotRequired[Sequence[str]]
    enableStrictOriginEnforcement: NotRequired[bool]
    name: NotRequired[str]

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetStreamKeyResponseTypeDef(TypedDict):
    errors: List[BatchErrorTypeDef]
    streamKeys: List[StreamKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamKeyResponseTypeDef(TypedDict):
    streamKey: StreamKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamKeyResponseTypeDef(TypedDict):
    streamKey: StreamKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchStartViewerSessionRevocationResponseTypeDef(TypedDict):
    errors: List[BatchStartViewerSessionRevocationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchStartViewerSessionRevocationRequestTypeDef(TypedDict):
    viewerSessions: Sequence[BatchStartViewerSessionRevocationViewerSessionTypeDef]

class ListChannelsResponseTypeDef(TypedDict):
    channels: List[ChannelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

CreateChannelRequestTypeDef = TypedDict(
    "CreateChannelRequestTypeDef",
    {
        "authorized": NotRequired[bool],
        "containerFormat": NotRequired[ContainerFormatType],
        "insecureIngest": NotRequired[bool],
        "latencyMode": NotRequired[ChannelLatencyModeType],
        "multitrackInputConfiguration": NotRequired[MultitrackInputConfigurationTypeDef],
        "name": NotRequired[str],
        "playbackRestrictionPolicyArn": NotRequired[str],
        "preset": NotRequired[TranscodePresetType],
        "recordingConfigurationArn": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "type": NotRequired[ChannelTypeType],
    },
)
UpdateChannelRequestTypeDef = TypedDict(
    "UpdateChannelRequestTypeDef",
    {
        "arn": str,
        "authorized": NotRequired[bool],
        "containerFormat": NotRequired[ContainerFormatType],
        "insecureIngest": NotRequired[bool],
        "latencyMode": NotRequired[ChannelLatencyModeType],
        "multitrackInputConfiguration": NotRequired[MultitrackInputConfigurationTypeDef],
        "name": NotRequired[str],
        "playbackRestrictionPolicyArn": NotRequired[str],
        "preset": NotRequired[TranscodePresetType],
        "recordingConfigurationArn": NotRequired[str],
        "type": NotRequired[ChannelTypeType],
    },
)
ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "arn": NotRequired[str],
        "authorized": NotRequired[bool],
        "containerFormat": NotRequired[ContainerFormatType],
        "ingestEndpoint": NotRequired[str],
        "insecureIngest": NotRequired[bool],
        "latencyMode": NotRequired[ChannelLatencyModeType],
        "multitrackInputConfiguration": NotRequired[MultitrackInputConfigurationTypeDef],
        "name": NotRequired[str],
        "playbackRestrictionPolicyArn": NotRequired[str],
        "playbackUrl": NotRequired[str],
        "preset": NotRequired[TranscodePresetType],
        "recordingConfigurationArn": NotRequired[str],
        "srt": NotRequired[SrtTypeDef],
        "tags": NotRequired[Dict[str, str]],
        "type": NotRequired[ChannelTypeType],
    },
)

class CreatePlaybackRestrictionPolicyResponseTypeDef(TypedDict):
    playbackRestrictionPolicy: PlaybackRestrictionPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPlaybackRestrictionPolicyResponseTypeDef(TypedDict):
    playbackRestrictionPolicy: PlaybackRestrictionPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePlaybackRestrictionPolicyResponseTypeDef(TypedDict):
    playbackRestrictionPolicy: PlaybackRestrictionPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationConfigurationTypeDef(TypedDict):
    s3: NotRequired[S3DestinationConfigurationTypeDef]

class GetPlaybackKeyPairResponseTypeDef(TypedDict):
    keyPair: PlaybackKeyPairTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportPlaybackKeyPairResponseTypeDef(TypedDict):
    keyPair: PlaybackKeyPairTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamResponseTypeDef(TypedDict):
    stream: StreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IngestConfigurationTypeDef(TypedDict):
    audio: NotRequired[AudioConfigurationTypeDef]
    video: NotRequired[VideoConfigurationTypeDef]

class IngestConfigurationsTypeDef(TypedDict):
    audioConfigurations: List[AudioConfigurationTypeDef]
    videoConfigurations: List[VideoConfigurationTypeDef]

class ListChannelsRequestPaginateTypeDef(TypedDict):
    filterByName: NotRequired[str]
    filterByPlaybackRestrictionPolicyArn: NotRequired[str]
    filterByRecordingConfigurationArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPlaybackKeyPairsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRecordingConfigurationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStreamKeysRequestPaginateTypeDef(TypedDict):
    channelArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPlaybackKeyPairsResponseTypeDef(TypedDict):
    keyPairs: List[PlaybackKeyPairSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListPlaybackRestrictionPoliciesResponseTypeDef(TypedDict):
    playbackRestrictionPolicies: List[PlaybackRestrictionPolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListStreamKeysResponseTypeDef(TypedDict):
    streamKeys: List[StreamKeySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListStreamSessionsResponseTypeDef(TypedDict):
    streamSessions: List[StreamSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListStreamsRequestPaginateTypeDef(TypedDict):
    filterBy: NotRequired[StreamFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStreamsRequestTypeDef(TypedDict):
    filterBy: NotRequired[StreamFiltersTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListStreamsResponseTypeDef(TypedDict):
    streams: List[StreamSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

RenditionConfigurationUnionTypeDef = Union[
    RenditionConfigurationTypeDef, RenditionConfigurationOutputTypeDef
]
ThumbnailConfigurationUnionTypeDef = Union[
    ThumbnailConfigurationTypeDef, ThumbnailConfigurationOutputTypeDef
]

class BatchGetChannelResponseTypeDef(TypedDict):
    channels: List[ChannelTypeDef]
    errors: List[BatchErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelResponseTypeDef(TypedDict):
    channel: ChannelTypeDef
    streamKey: StreamKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelResponseTypeDef(TypedDict):
    channel: ChannelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelResponseTypeDef(TypedDict):
    channel: ChannelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RecordingConfigurationSummaryTypeDef(TypedDict):
    arn: str
    destinationConfiguration: DestinationConfigurationTypeDef
    state: RecordingConfigurationStateType
    name: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class RecordingConfigurationTypeDef(TypedDict):
    arn: str
    destinationConfiguration: DestinationConfigurationTypeDef
    state: RecordingConfigurationStateType
    name: NotRequired[str]
    recordingReconnectWindowSeconds: NotRequired[int]
    renditionConfiguration: NotRequired[RenditionConfigurationOutputTypeDef]
    tags: NotRequired[Dict[str, str]]
    thumbnailConfiguration: NotRequired[ThumbnailConfigurationOutputTypeDef]

class CreateRecordingConfigurationRequestTypeDef(TypedDict):
    destinationConfiguration: DestinationConfigurationTypeDef
    name: NotRequired[str]
    recordingReconnectWindowSeconds: NotRequired[int]
    renditionConfiguration: NotRequired[RenditionConfigurationUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]
    thumbnailConfiguration: NotRequired[ThumbnailConfigurationUnionTypeDef]

class ListRecordingConfigurationsResponseTypeDef(TypedDict):
    recordingConfigurations: List[RecordingConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateRecordingConfigurationResponseTypeDef(TypedDict):
    recordingConfiguration: RecordingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecordingConfigurationResponseTypeDef(TypedDict):
    recordingConfiguration: RecordingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StreamSessionTypeDef(TypedDict):
    channel: NotRequired[ChannelTypeDef]
    endTime: NotRequired[datetime]
    ingestConfiguration: NotRequired[IngestConfigurationTypeDef]
    ingestConfigurations: NotRequired[IngestConfigurationsTypeDef]
    recordingConfiguration: NotRequired[RecordingConfigurationTypeDef]
    startTime: NotRequired[datetime]
    streamId: NotRequired[str]
    truncatedEvents: NotRequired[List[StreamEventTypeDef]]

class GetStreamSessionResponseTypeDef(TypedDict):
    streamSession: StreamSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
