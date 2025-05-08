"""
Type annotations for ivs-realtime service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_ivs_realtime.type_defs import ParticipantRecordingHlsConfigurationTypeDef

    data: ParticipantRecordingHlsConfigurationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    CompositionStateType,
    DestinationStateType,
    EventErrorCodeType,
    EventNameType,
    IngestConfigurationStateType,
    IngestProtocolType,
    ParticipantProtocolType,
    ParticipantRecordingFilterByRecordingStateType,
    ParticipantRecordingMediaTypeType,
    ParticipantRecordingStateType,
    ParticipantStateType,
    ParticipantTokenCapabilityType,
    PipBehaviorType,
    PipPositionType,
    ThumbnailRecordingModeType,
    ThumbnailStorageTypeType,
    VideoAspectRatioType,
    VideoFillModeType,
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
    "AutoParticipantRecordingConfigurationOutputTypeDef",
    "AutoParticipantRecordingConfigurationTypeDef",
    "AutoParticipantRecordingConfigurationUnionTypeDef",
    "ChannelDestinationConfigurationTypeDef",
    "CompositionRecordingHlsConfigurationTypeDef",
    "CompositionSummaryTypeDef",
    "CompositionThumbnailConfigurationOutputTypeDef",
    "CompositionThumbnailConfigurationTypeDef",
    "CompositionThumbnailConfigurationUnionTypeDef",
    "CompositionTypeDef",
    "CreateEncoderConfigurationRequestTypeDef",
    "CreateEncoderConfigurationResponseTypeDef",
    "CreateIngestConfigurationRequestTypeDef",
    "CreateIngestConfigurationResponseTypeDef",
    "CreateParticipantTokenRequestTypeDef",
    "CreateParticipantTokenResponseTypeDef",
    "CreateStageRequestTypeDef",
    "CreateStageResponseTypeDef",
    "CreateStorageConfigurationRequestTypeDef",
    "CreateStorageConfigurationResponseTypeDef",
    "DeleteEncoderConfigurationRequestTypeDef",
    "DeleteIngestConfigurationRequestTypeDef",
    "DeletePublicKeyRequestTypeDef",
    "DeleteStageRequestTypeDef",
    "DeleteStorageConfigurationRequestTypeDef",
    "DestinationConfigurationOutputTypeDef",
    "DestinationConfigurationTypeDef",
    "DestinationConfigurationUnionTypeDef",
    "DestinationDetailTypeDef",
    "DestinationSummaryTypeDef",
    "DestinationTypeDef",
    "DisconnectParticipantRequestTypeDef",
    "EncoderConfigurationSummaryTypeDef",
    "EncoderConfigurationTypeDef",
    "EventTypeDef",
    "GetCompositionRequestTypeDef",
    "GetCompositionResponseTypeDef",
    "GetEncoderConfigurationRequestTypeDef",
    "GetEncoderConfigurationResponseTypeDef",
    "GetIngestConfigurationRequestTypeDef",
    "GetIngestConfigurationResponseTypeDef",
    "GetParticipantRequestTypeDef",
    "GetParticipantResponseTypeDef",
    "GetPublicKeyRequestTypeDef",
    "GetPublicKeyResponseTypeDef",
    "GetStageRequestTypeDef",
    "GetStageResponseTypeDef",
    "GetStageSessionRequestTypeDef",
    "GetStageSessionResponseTypeDef",
    "GetStorageConfigurationRequestTypeDef",
    "GetStorageConfigurationResponseTypeDef",
    "GridConfigurationTypeDef",
    "ImportPublicKeyRequestTypeDef",
    "ImportPublicKeyResponseTypeDef",
    "IngestConfigurationSummaryTypeDef",
    "IngestConfigurationTypeDef",
    "LayoutConfigurationTypeDef",
    "ListCompositionsRequestTypeDef",
    "ListCompositionsResponseTypeDef",
    "ListEncoderConfigurationsRequestTypeDef",
    "ListEncoderConfigurationsResponseTypeDef",
    "ListIngestConfigurationsRequestPaginateTypeDef",
    "ListIngestConfigurationsRequestTypeDef",
    "ListIngestConfigurationsResponseTypeDef",
    "ListParticipantEventsRequestTypeDef",
    "ListParticipantEventsResponseTypeDef",
    "ListParticipantsRequestTypeDef",
    "ListParticipantsResponseTypeDef",
    "ListPublicKeysRequestPaginateTypeDef",
    "ListPublicKeysRequestTypeDef",
    "ListPublicKeysResponseTypeDef",
    "ListStageSessionsRequestTypeDef",
    "ListStageSessionsResponseTypeDef",
    "ListStagesRequestTypeDef",
    "ListStagesResponseTypeDef",
    "ListStorageConfigurationsRequestTypeDef",
    "ListStorageConfigurationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantRecordingHlsConfigurationTypeDef",
    "ParticipantSummaryTypeDef",
    "ParticipantThumbnailConfigurationOutputTypeDef",
    "ParticipantThumbnailConfigurationTypeDef",
    "ParticipantTokenConfigurationTypeDef",
    "ParticipantTokenTypeDef",
    "ParticipantTypeDef",
    "PipConfigurationTypeDef",
    "PublicKeySummaryTypeDef",
    "PublicKeyTypeDef",
    "RecordingConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationConfigurationOutputTypeDef",
    "S3DestinationConfigurationTypeDef",
    "S3DestinationConfigurationUnionTypeDef",
    "S3DetailTypeDef",
    "S3StorageConfigurationTypeDef",
    "StageEndpointsTypeDef",
    "StageSessionSummaryTypeDef",
    "StageSessionTypeDef",
    "StageSummaryTypeDef",
    "StageTypeDef",
    "StartCompositionRequestTypeDef",
    "StartCompositionResponseTypeDef",
    "StopCompositionRequestTypeDef",
    "StorageConfigurationSummaryTypeDef",
    "StorageConfigurationTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateIngestConfigurationRequestTypeDef",
    "UpdateIngestConfigurationResponseTypeDef",
    "UpdateStageRequestTypeDef",
    "UpdateStageResponseTypeDef",
    "VideoTypeDef",
)

class ParticipantRecordingHlsConfigurationTypeDef(TypedDict):
    targetSegmentDurationSeconds: NotRequired[int]

class ParticipantThumbnailConfigurationOutputTypeDef(TypedDict):
    targetIntervalSeconds: NotRequired[int]
    storage: NotRequired[List[ThumbnailStorageTypeType]]
    recordingMode: NotRequired[ThumbnailRecordingModeType]

class ParticipantThumbnailConfigurationTypeDef(TypedDict):
    targetIntervalSeconds: NotRequired[int]
    storage: NotRequired[Sequence[ThumbnailStorageTypeType]]
    recordingMode: NotRequired[ThumbnailRecordingModeType]

class ChannelDestinationConfigurationTypeDef(TypedDict):
    channelArn: str
    encoderConfigurationArn: NotRequired[str]

class CompositionRecordingHlsConfigurationTypeDef(TypedDict):
    targetSegmentDurationSeconds: NotRequired[int]

DestinationSummaryTypeDef = TypedDict(
    "DestinationSummaryTypeDef",
    {
        "id": str,
        "state": DestinationStateType,
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
    },
)

class CompositionThumbnailConfigurationOutputTypeDef(TypedDict):
    targetIntervalSeconds: NotRequired[int]
    storage: NotRequired[List[ThumbnailStorageTypeType]]

class CompositionThumbnailConfigurationTypeDef(TypedDict):
    targetIntervalSeconds: NotRequired[int]
    storage: NotRequired[Sequence[ThumbnailStorageTypeType]]

class VideoTypeDef(TypedDict):
    width: NotRequired[int]
    height: NotRequired[int]
    framerate: NotRequired[float]
    bitrate: NotRequired[int]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateIngestConfigurationRequestTypeDef(TypedDict):
    ingestProtocol: IngestProtocolType
    name: NotRequired[str]
    stageArn: NotRequired[str]
    userId: NotRequired[str]
    attributes: NotRequired[Mapping[str, str]]
    insecureIngest: NotRequired[bool]
    tags: NotRequired[Mapping[str, str]]

class IngestConfigurationTypeDef(TypedDict):
    arn: str
    ingestProtocol: IngestProtocolType
    streamKey: str
    stageArn: str
    participantId: str
    state: IngestConfigurationStateType
    name: NotRequired[str]
    userId: NotRequired[str]
    attributes: NotRequired[Dict[str, str]]
    tags: NotRequired[Dict[str, str]]

class CreateParticipantTokenRequestTypeDef(TypedDict):
    stageArn: str
    duration: NotRequired[int]
    userId: NotRequired[str]
    attributes: NotRequired[Mapping[str, str]]
    capabilities: NotRequired[Sequence[ParticipantTokenCapabilityType]]

class ParticipantTokenTypeDef(TypedDict):
    participantId: NotRequired[str]
    token: NotRequired[str]
    userId: NotRequired[str]
    attributes: NotRequired[Dict[str, str]]
    duration: NotRequired[int]
    capabilities: NotRequired[List[ParticipantTokenCapabilityType]]
    expirationTime: NotRequired[datetime]

class ParticipantTokenConfigurationTypeDef(TypedDict):
    duration: NotRequired[int]
    userId: NotRequired[str]
    attributes: NotRequired[Mapping[str, str]]
    capabilities: NotRequired[Sequence[ParticipantTokenCapabilityType]]

class S3StorageConfigurationTypeDef(TypedDict):
    bucketName: str

class DeleteEncoderConfigurationRequestTypeDef(TypedDict):
    arn: str

class DeleteIngestConfigurationRequestTypeDef(TypedDict):
    arn: str
    force: NotRequired[bool]

class DeletePublicKeyRequestTypeDef(TypedDict):
    arn: str

class DeleteStageRequestTypeDef(TypedDict):
    arn: str

class DeleteStorageConfigurationRequestTypeDef(TypedDict):
    arn: str

class S3DetailTypeDef(TypedDict):
    recordingPrefix: str

class DisconnectParticipantRequestTypeDef(TypedDict):
    stageArn: str
    participantId: str
    reason: NotRequired[str]

class EncoderConfigurationSummaryTypeDef(TypedDict):
    arn: str
    name: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class EventTypeDef(TypedDict):
    name: NotRequired[EventNameType]
    participantId: NotRequired[str]
    eventTime: NotRequired[datetime]
    remoteParticipantId: NotRequired[str]
    errorCode: NotRequired[EventErrorCodeType]

class GetCompositionRequestTypeDef(TypedDict):
    arn: str

class GetEncoderConfigurationRequestTypeDef(TypedDict):
    arn: str

class GetIngestConfigurationRequestTypeDef(TypedDict):
    arn: str

class GetParticipantRequestTypeDef(TypedDict):
    stageArn: str
    sessionId: str
    participantId: str

class ParticipantTypeDef(TypedDict):
    participantId: NotRequired[str]
    userId: NotRequired[str]
    state: NotRequired[ParticipantStateType]
    firstJoinTime: NotRequired[datetime]
    attributes: NotRequired[Dict[str, str]]
    published: NotRequired[bool]
    ispName: NotRequired[str]
    osName: NotRequired[str]
    osVersion: NotRequired[str]
    browserName: NotRequired[str]
    browserVersion: NotRequired[str]
    sdkVersion: NotRequired[str]
    recordingS3BucketName: NotRequired[str]
    recordingS3Prefix: NotRequired[str]
    recordingState: NotRequired[ParticipantRecordingStateType]
    protocol: NotRequired[ParticipantProtocolType]

class GetPublicKeyRequestTypeDef(TypedDict):
    arn: str

class PublicKeyTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]
    publicKeyMaterial: NotRequired[str]
    fingerprint: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class GetStageRequestTypeDef(TypedDict):
    arn: str

class GetStageSessionRequestTypeDef(TypedDict):
    stageArn: str
    sessionId: str

class StageSessionTypeDef(TypedDict):
    sessionId: NotRequired[str]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]

class GetStorageConfigurationRequestTypeDef(TypedDict):
    arn: str

class GridConfigurationTypeDef(TypedDict):
    featuredParticipantAttribute: NotRequired[str]
    omitStoppedVideo: NotRequired[bool]
    videoAspectRatio: NotRequired[VideoAspectRatioType]
    videoFillMode: NotRequired[VideoFillModeType]
    gridGap: NotRequired[int]

class ImportPublicKeyRequestTypeDef(TypedDict):
    publicKeyMaterial: str
    name: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class IngestConfigurationSummaryTypeDef(TypedDict):
    arn: str
    ingestProtocol: IngestProtocolType
    stageArn: str
    participantId: str
    state: IngestConfigurationStateType
    name: NotRequired[str]
    userId: NotRequired[str]

class PipConfigurationTypeDef(TypedDict):
    featuredParticipantAttribute: NotRequired[str]
    omitStoppedVideo: NotRequired[bool]
    videoFillMode: NotRequired[VideoFillModeType]
    gridGap: NotRequired[int]
    pipParticipantAttribute: NotRequired[str]
    pipBehavior: NotRequired[PipBehaviorType]
    pipOffset: NotRequired[int]
    pipPosition: NotRequired[PipPositionType]
    pipWidth: NotRequired[int]
    pipHeight: NotRequired[int]

class ListCompositionsRequestTypeDef(TypedDict):
    filterByStageArn: NotRequired[str]
    filterByEncoderConfigurationArn: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListEncoderConfigurationsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListIngestConfigurationsRequestTypeDef(TypedDict):
    filterByStageArn: NotRequired[str]
    filterByState: NotRequired[IngestConfigurationStateType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListParticipantEventsRequestTypeDef(TypedDict):
    stageArn: str
    sessionId: str
    participantId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListParticipantsRequestTypeDef(TypedDict):
    stageArn: str
    sessionId: str
    filterByUserId: NotRequired[str]
    filterByPublished: NotRequired[bool]
    filterByState: NotRequired[ParticipantStateType]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filterByRecordingState: NotRequired[ParticipantRecordingFilterByRecordingStateType]

class ParticipantSummaryTypeDef(TypedDict):
    participantId: NotRequired[str]
    userId: NotRequired[str]
    state: NotRequired[ParticipantStateType]
    firstJoinTime: NotRequired[datetime]
    published: NotRequired[bool]
    recordingState: NotRequired[ParticipantRecordingStateType]

class ListPublicKeysRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class PublicKeySummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class ListStageSessionsRequestTypeDef(TypedDict):
    stageArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class StageSessionSummaryTypeDef(TypedDict):
    sessionId: NotRequired[str]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]

class ListStagesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class StageSummaryTypeDef(TypedDict):
    arn: str
    name: NotRequired[str]
    activeSessionId: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class ListStorageConfigurationsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class StageEndpointsTypeDef(TypedDict):
    events: NotRequired[str]
    whip: NotRequired[str]
    rtmp: NotRequired[str]
    rtmps: NotRequired[str]

class StopCompositionRequestTypeDef(TypedDict):
    arn: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateIngestConfigurationRequestTypeDef(TypedDict):
    arn: str
    stageArn: NotRequired[str]

class AutoParticipantRecordingConfigurationOutputTypeDef(TypedDict):
    storageConfigurationArn: str
    mediaTypes: NotRequired[List[ParticipantRecordingMediaTypeType]]
    thumbnailConfiguration: NotRequired[ParticipantThumbnailConfigurationOutputTypeDef]
    recordingReconnectWindowSeconds: NotRequired[int]
    hlsConfiguration: NotRequired[ParticipantRecordingHlsConfigurationTypeDef]

class AutoParticipantRecordingConfigurationTypeDef(TypedDict):
    storageConfigurationArn: str
    mediaTypes: NotRequired[Sequence[ParticipantRecordingMediaTypeType]]
    thumbnailConfiguration: NotRequired[ParticipantThumbnailConfigurationTypeDef]
    recordingReconnectWindowSeconds: NotRequired[int]
    hlsConfiguration: NotRequired[ParticipantRecordingHlsConfigurationTypeDef]

RecordingConfigurationTypeDef = TypedDict(
    "RecordingConfigurationTypeDef",
    {
        "hlsConfiguration": NotRequired[CompositionRecordingHlsConfigurationTypeDef],
        "format": NotRequired[Literal["HLS"]],
    },
)

class CompositionSummaryTypeDef(TypedDict):
    arn: str
    stageArn: str
    destinations: List[DestinationSummaryTypeDef]
    state: CompositionStateType
    tags: NotRequired[Dict[str, str]]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]

CompositionThumbnailConfigurationUnionTypeDef = Union[
    CompositionThumbnailConfigurationTypeDef, CompositionThumbnailConfigurationOutputTypeDef
]

class CreateEncoderConfigurationRequestTypeDef(TypedDict):
    name: NotRequired[str]
    video: NotRequired[VideoTypeDef]
    tags: NotRequired[Mapping[str, str]]

class EncoderConfigurationTypeDef(TypedDict):
    arn: str
    name: NotRequired[str]
    video: NotRequired[VideoTypeDef]
    tags: NotRequired[Dict[str, str]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIngestConfigurationResponseTypeDef(TypedDict):
    ingestConfiguration: IngestConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIngestConfigurationResponseTypeDef(TypedDict):
    ingestConfiguration: IngestConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIngestConfigurationResponseTypeDef(TypedDict):
    ingestConfiguration: IngestConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateParticipantTokenResponseTypeDef(TypedDict):
    participantToken: ParticipantTokenTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStorageConfigurationRequestTypeDef(TypedDict):
    s3: S3StorageConfigurationTypeDef
    name: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class StorageConfigurationSummaryTypeDef(TypedDict):
    arn: str
    name: NotRequired[str]
    s3: NotRequired[S3StorageConfigurationTypeDef]
    tags: NotRequired[Dict[str, str]]

class StorageConfigurationTypeDef(TypedDict):
    arn: str
    name: NotRequired[str]
    s3: NotRequired[S3StorageConfigurationTypeDef]
    tags: NotRequired[Dict[str, str]]

class DestinationDetailTypeDef(TypedDict):
    s3: NotRequired[S3DetailTypeDef]

class ListEncoderConfigurationsResponseTypeDef(TypedDict):
    encoderConfigurations: List[EncoderConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListParticipantEventsResponseTypeDef(TypedDict):
    events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetParticipantResponseTypeDef(TypedDict):
    participant: ParticipantTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPublicKeyResponseTypeDef(TypedDict):
    publicKey: PublicKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportPublicKeyResponseTypeDef(TypedDict):
    publicKey: PublicKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStageSessionResponseTypeDef(TypedDict):
    stageSession: StageSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIngestConfigurationsResponseTypeDef(TypedDict):
    ingestConfigurations: List[IngestConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class LayoutConfigurationTypeDef(TypedDict):
    grid: NotRequired[GridConfigurationTypeDef]
    pip: NotRequired[PipConfigurationTypeDef]

class ListIngestConfigurationsRequestPaginateTypeDef(TypedDict):
    filterByStageArn: NotRequired[str]
    filterByState: NotRequired[IngestConfigurationStateType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPublicKeysRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListParticipantsResponseTypeDef(TypedDict):
    participants: List[ParticipantSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListPublicKeysResponseTypeDef(TypedDict):
    publicKeys: List[PublicKeySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListStageSessionsResponseTypeDef(TypedDict):
    stageSessions: List[StageSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListStagesResponseTypeDef(TypedDict):
    stages: List[StageSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StageTypeDef(TypedDict):
    arn: str
    name: NotRequired[str]
    activeSessionId: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    autoParticipantRecordingConfiguration: NotRequired[
        AutoParticipantRecordingConfigurationOutputTypeDef
    ]
    endpoints: NotRequired[StageEndpointsTypeDef]

AutoParticipantRecordingConfigurationUnionTypeDef = Union[
    AutoParticipantRecordingConfigurationTypeDef, AutoParticipantRecordingConfigurationOutputTypeDef
]

class S3DestinationConfigurationOutputTypeDef(TypedDict):
    storageConfigurationArn: str
    encoderConfigurationArns: List[str]
    recordingConfiguration: NotRequired[RecordingConfigurationTypeDef]
    thumbnailConfigurations: NotRequired[List[CompositionThumbnailConfigurationOutputTypeDef]]

class ListCompositionsResponseTypeDef(TypedDict):
    compositions: List[CompositionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class S3DestinationConfigurationTypeDef(TypedDict):
    storageConfigurationArn: str
    encoderConfigurationArns: Sequence[str]
    recordingConfiguration: NotRequired[RecordingConfigurationTypeDef]
    thumbnailConfigurations: NotRequired[Sequence[CompositionThumbnailConfigurationUnionTypeDef]]

class CreateEncoderConfigurationResponseTypeDef(TypedDict):
    encoderConfiguration: EncoderConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEncoderConfigurationResponseTypeDef(TypedDict):
    encoderConfiguration: EncoderConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStorageConfigurationsResponseTypeDef(TypedDict):
    storageConfigurations: List[StorageConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateStorageConfigurationResponseTypeDef(TypedDict):
    storageConfiguration: StorageConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStorageConfigurationResponseTypeDef(TypedDict):
    storageConfiguration: StorageConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStageResponseTypeDef(TypedDict):
    stage: StageTypeDef
    participantTokens: List[ParticipantTokenTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetStageResponseTypeDef(TypedDict):
    stage: StageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStageResponseTypeDef(TypedDict):
    stage: StageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStageRequestTypeDef(TypedDict):
    name: NotRequired[str]
    participantTokenConfigurations: NotRequired[Sequence[ParticipantTokenConfigurationTypeDef]]
    tags: NotRequired[Mapping[str, str]]
    autoParticipantRecordingConfiguration: NotRequired[
        AutoParticipantRecordingConfigurationUnionTypeDef
    ]

class UpdateStageRequestTypeDef(TypedDict):
    arn: str
    name: NotRequired[str]
    autoParticipantRecordingConfiguration: NotRequired[
        AutoParticipantRecordingConfigurationUnionTypeDef
    ]

class DestinationConfigurationOutputTypeDef(TypedDict):
    name: NotRequired[str]
    channel: NotRequired[ChannelDestinationConfigurationTypeDef]
    s3: NotRequired[S3DestinationConfigurationOutputTypeDef]

S3DestinationConfigurationUnionTypeDef = Union[
    S3DestinationConfigurationTypeDef, S3DestinationConfigurationOutputTypeDef
]
DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "id": str,
        "state": DestinationStateType,
        "configuration": DestinationConfigurationOutputTypeDef,
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "detail": NotRequired[DestinationDetailTypeDef],
    },
)

class DestinationConfigurationTypeDef(TypedDict):
    name: NotRequired[str]
    channel: NotRequired[ChannelDestinationConfigurationTypeDef]
    s3: NotRequired[S3DestinationConfigurationUnionTypeDef]

class CompositionTypeDef(TypedDict):
    arn: str
    stageArn: str
    state: CompositionStateType
    layout: LayoutConfigurationTypeDef
    destinations: List[DestinationTypeDef]
    tags: NotRequired[Dict[str, str]]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]

DestinationConfigurationUnionTypeDef = Union[
    DestinationConfigurationTypeDef, DestinationConfigurationOutputTypeDef
]

class GetCompositionResponseTypeDef(TypedDict):
    composition: CompositionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartCompositionResponseTypeDef(TypedDict):
    composition: CompositionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartCompositionRequestTypeDef(TypedDict):
    stageArn: str
    destinations: Sequence[DestinationConfigurationUnionTypeDef]
    idempotencyToken: NotRequired[str]
    layout: NotRequired[LayoutConfigurationTypeDef]
    tags: NotRequired[Mapping[str, str]]
