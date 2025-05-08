"""
Type annotations for mediapackagev2 service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_mediapackagev2.type_defs import CancelHarvestJobRequestTypeDef

    data: CancelHarvestJobRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AdMarkerDashType,
    CmafEncryptionMethodType,
    ContainerTypeType,
    DashDrmSignalingType,
    DashPeriodTriggerType,
    DashUtcTimingModeType,
    DrmSystemType,
    EndpointErrorConditionType,
    HarvestJobStatusType,
    InputTypeType,
    PresetSpeke20AudioType,
    PresetSpeke20VideoType,
    ScteFilterType,
    TsEncryptionMethodType,
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
    "CancelHarvestJobRequestTypeDef",
    "ChannelGroupListConfigurationTypeDef",
    "ChannelListConfigurationTypeDef",
    "CreateChannelGroupRequestTypeDef",
    "CreateChannelGroupResponseTypeDef",
    "CreateChannelRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateDashManifestConfigurationTypeDef",
    "CreateHarvestJobRequestTypeDef",
    "CreateHarvestJobResponseTypeDef",
    "CreateHlsManifestConfigurationTypeDef",
    "CreateLowLatencyHlsManifestConfigurationTypeDef",
    "CreateOriginEndpointRequestTypeDef",
    "CreateOriginEndpointResponseTypeDef",
    "DashUtcTimingTypeDef",
    "DeleteChannelGroupRequestTypeDef",
    "DeleteChannelPolicyRequestTypeDef",
    "DeleteChannelRequestTypeDef",
    "DeleteOriginEndpointPolicyRequestTypeDef",
    "DeleteOriginEndpointRequestTypeDef",
    "DestinationTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionContractConfigurationTypeDef",
    "EncryptionMethodTypeDef",
    "EncryptionOutputTypeDef",
    "EncryptionTypeDef",
    "FilterConfigurationOutputTypeDef",
    "FilterConfigurationTypeDef",
    "FilterConfigurationUnionTypeDef",
    "ForceEndpointErrorConfigurationOutputTypeDef",
    "ForceEndpointErrorConfigurationTypeDef",
    "ForceEndpointErrorConfigurationUnionTypeDef",
    "GetChannelGroupRequestTypeDef",
    "GetChannelGroupResponseTypeDef",
    "GetChannelPolicyRequestTypeDef",
    "GetChannelPolicyResponseTypeDef",
    "GetChannelRequestTypeDef",
    "GetChannelResponseTypeDef",
    "GetDashManifestConfigurationTypeDef",
    "GetHarvestJobRequestTypeDef",
    "GetHarvestJobRequestWaitTypeDef",
    "GetHarvestJobResponseTypeDef",
    "GetHlsManifestConfigurationTypeDef",
    "GetLowLatencyHlsManifestConfigurationTypeDef",
    "GetOriginEndpointPolicyRequestTypeDef",
    "GetOriginEndpointPolicyResponseTypeDef",
    "GetOriginEndpointRequestTypeDef",
    "GetOriginEndpointResponseTypeDef",
    "HarvestJobTypeDef",
    "HarvestedDashManifestTypeDef",
    "HarvestedHlsManifestTypeDef",
    "HarvestedLowLatencyHlsManifestTypeDef",
    "HarvestedManifestsOutputTypeDef",
    "HarvestedManifestsTypeDef",
    "HarvestedManifestsUnionTypeDef",
    "HarvesterScheduleConfigurationOutputTypeDef",
    "HarvesterScheduleConfigurationTypeDef",
    "HarvesterScheduleConfigurationUnionTypeDef",
    "IngestEndpointTypeDef",
    "InputSwitchConfigurationTypeDef",
    "ListChannelGroupsRequestPaginateTypeDef",
    "ListChannelGroupsRequestTypeDef",
    "ListChannelGroupsResponseTypeDef",
    "ListChannelsRequestPaginateTypeDef",
    "ListChannelsRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListDashManifestConfigurationTypeDef",
    "ListHarvestJobsRequestPaginateTypeDef",
    "ListHarvestJobsRequestTypeDef",
    "ListHarvestJobsResponseTypeDef",
    "ListHlsManifestConfigurationTypeDef",
    "ListLowLatencyHlsManifestConfigurationTypeDef",
    "ListOriginEndpointsRequestPaginateTypeDef",
    "ListOriginEndpointsRequestTypeDef",
    "ListOriginEndpointsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OriginEndpointListConfigurationTypeDef",
    "OutputHeaderConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PutChannelPolicyRequestTypeDef",
    "PutOriginEndpointPolicyRequestTypeDef",
    "ResetChannelStateRequestTypeDef",
    "ResetChannelStateResponseTypeDef",
    "ResetOriginEndpointStateRequestTypeDef",
    "ResetOriginEndpointStateResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationConfigTypeDef",
    "ScteDashTypeDef",
    "ScteHlsTypeDef",
    "ScteOutputTypeDef",
    "ScteTypeDef",
    "SegmentOutputTypeDef",
    "SegmentTypeDef",
    "SegmentUnionTypeDef",
    "SpekeKeyProviderOutputTypeDef",
    "SpekeKeyProviderTypeDef",
    "StartTagTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateChannelGroupRequestTypeDef",
    "UpdateChannelGroupResponseTypeDef",
    "UpdateChannelRequestTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateOriginEndpointRequestTypeDef",
    "UpdateOriginEndpointResponseTypeDef",
    "WaiterConfigTypeDef",
)

class CancelHarvestJobRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    HarvestJobName: str
    ETag: NotRequired[str]

class ChannelGroupListConfigurationTypeDef(TypedDict):
    ChannelGroupName: str
    Arn: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: NotRequired[str]

class ChannelListConfigurationTypeDef(TypedDict):
    Arn: str
    ChannelName: str
    ChannelGroupName: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: NotRequired[str]
    InputType: NotRequired[InputTypeType]

class CreateChannelGroupRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ClientToken: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class InputSwitchConfigurationTypeDef(TypedDict):
    MQCSInputSwitching: NotRequired[bool]

class OutputHeaderConfigurationTypeDef(TypedDict):
    PublishMQCS: NotRequired[bool]

class IngestEndpointTypeDef(TypedDict):
    Id: NotRequired[str]
    Url: NotRequired[str]

class DashUtcTimingTypeDef(TypedDict):
    TimingMode: NotRequired[DashUtcTimingModeType]
    TimingSource: NotRequired[str]

class ScteDashTypeDef(TypedDict):
    AdMarkerDash: NotRequired[AdMarkerDashType]

class HarvesterScheduleConfigurationOutputTypeDef(TypedDict):
    StartTime: datetime
    EndTime: datetime

class ScteHlsTypeDef(TypedDict):
    AdMarkerHls: NotRequired[Literal["DATERANGE"]]

class StartTagTypeDef(TypedDict):
    TimeOffset: float
    Precise: NotRequired[bool]

class ForceEndpointErrorConfigurationOutputTypeDef(TypedDict):
    EndpointErrorConditions: NotRequired[List[EndpointErrorConditionType]]

class DeleteChannelGroupRequestTypeDef(TypedDict):
    ChannelGroupName: str

class DeleteChannelPolicyRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str

class DeleteChannelRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str

class DeleteOriginEndpointPolicyRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str

class DeleteOriginEndpointRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str

class S3DestinationConfigTypeDef(TypedDict):
    BucketName: str
    DestinationPath: str

class EncryptionContractConfigurationTypeDef(TypedDict):
    PresetSpeke20Audio: PresetSpeke20AudioType
    PresetSpeke20Video: PresetSpeke20VideoType

class EncryptionMethodTypeDef(TypedDict):
    TsEncryptionMethod: NotRequired[TsEncryptionMethodType]
    CmafEncryptionMethod: NotRequired[CmafEncryptionMethodType]

class FilterConfigurationOutputTypeDef(TypedDict):
    ManifestFilter: NotRequired[str]
    Start: NotRequired[datetime]
    End: NotRequired[datetime]
    TimeDelaySeconds: NotRequired[int]
    ClipStartTime: NotRequired[datetime]

TimestampTypeDef = Union[datetime, str]

class ForceEndpointErrorConfigurationTypeDef(TypedDict):
    EndpointErrorConditions: NotRequired[Sequence[EndpointErrorConditionType]]

class GetChannelGroupRequestTypeDef(TypedDict):
    ChannelGroupName: str

class GetChannelPolicyRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str

class GetChannelRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str

class GetHarvestJobRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    HarvestJobName: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class GetOriginEndpointPolicyRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str

class GetOriginEndpointRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str

class HarvestedDashManifestTypeDef(TypedDict):
    ManifestName: str

class HarvestedHlsManifestTypeDef(TypedDict):
    ManifestName: str

class HarvestedLowLatencyHlsManifestTypeDef(TypedDict):
    ManifestName: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListChannelGroupsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListChannelsRequestTypeDef(TypedDict):
    ChannelGroupName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListDashManifestConfigurationTypeDef(TypedDict):
    ManifestName: str
    Url: NotRequired[str]

class ListHarvestJobsRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: NotRequired[str]
    OriginEndpointName: NotRequired[str]
    Status: NotRequired[HarvestJobStatusType]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListHlsManifestConfigurationTypeDef(TypedDict):
    ManifestName: str
    ChildManifestName: NotRequired[str]
    Url: NotRequired[str]

class ListLowLatencyHlsManifestConfigurationTypeDef(TypedDict):
    ManifestName: str
    ChildManifestName: NotRequired[str]
    Url: NotRequired[str]

class ListOriginEndpointsRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class PutChannelPolicyRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    Policy: str

class PutOriginEndpointPolicyRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Policy: str

class ResetChannelStateRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str

class ResetOriginEndpointStateRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str

class ScteOutputTypeDef(TypedDict):
    ScteFilter: NotRequired[List[ScteFilterType]]

class ScteTypeDef(TypedDict):
    ScteFilter: NotRequired[Sequence[ScteFilterType]]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateChannelGroupRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ETag: NotRequired[str]
    Description: NotRequired[str]

class CreateChannelGroupResponseTypeDef(TypedDict):
    ChannelGroupName: str
    Arn: str
    EgressDomain: str
    CreatedAt: datetime
    ModifiedAt: datetime
    ETag: str
    Description: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelGroupResponseTypeDef(TypedDict):
    ChannelGroupName: str
    Arn: str
    EgressDomain: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelPolicyResponseTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOriginEndpointPolicyResponseTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelGroupsResponseTypeDef(TypedDict):
    Items: List[ChannelGroupListConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListChannelsResponseTypeDef(TypedDict):
    Items: List[ChannelListConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ResetChannelStateResponseTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    Arn: str
    ResetAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ResetOriginEndpointStateResponseTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Arn: str
    ResetAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelGroupResponseTypeDef(TypedDict):
    ChannelGroupName: str
    Arn: str
    EgressDomain: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    ClientToken: NotRequired[str]
    InputType: NotRequired[InputTypeType]
    Description: NotRequired[str]
    InputSwitchConfiguration: NotRequired[InputSwitchConfigurationTypeDef]
    OutputHeaderConfiguration: NotRequired[OutputHeaderConfigurationTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class UpdateChannelRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    ETag: NotRequired[str]
    Description: NotRequired[str]
    InputSwitchConfiguration: NotRequired[InputSwitchConfigurationTypeDef]
    OutputHeaderConfiguration: NotRequired[OutputHeaderConfigurationTypeDef]

class CreateChannelResponseTypeDef(TypedDict):
    Arn: str
    ChannelName: str
    ChannelGroupName: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    IngestEndpoints: List[IngestEndpointTypeDef]
    InputType: InputTypeType
    ETag: str
    Tags: Dict[str, str]
    InputSwitchConfiguration: InputSwitchConfigurationTypeDef
    OutputHeaderConfiguration: OutputHeaderConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelResponseTypeDef(TypedDict):
    Arn: str
    ChannelName: str
    ChannelGroupName: str
    CreatedAt: datetime
    ModifiedAt: datetime
    ResetAt: datetime
    Description: str
    IngestEndpoints: List[IngestEndpointTypeDef]
    InputType: InputTypeType
    ETag: str
    Tags: Dict[str, str]
    InputSwitchConfiguration: InputSwitchConfigurationTypeDef
    OutputHeaderConfiguration: OutputHeaderConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelResponseTypeDef(TypedDict):
    Arn: str
    ChannelName: str
    ChannelGroupName: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    IngestEndpoints: List[IngestEndpointTypeDef]
    InputType: InputTypeType
    ETag: str
    Tags: Dict[str, str]
    InputSwitchConfiguration: InputSwitchConfigurationTypeDef
    OutputHeaderConfiguration: OutputHeaderConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationTypeDef(TypedDict):
    S3Destination: S3DestinationConfigTypeDef

class SpekeKeyProviderOutputTypeDef(TypedDict):
    EncryptionContractConfiguration: EncryptionContractConfigurationTypeDef
    ResourceId: str
    DrmSystems: List[DrmSystemType]
    RoleArn: str
    Url: str

class SpekeKeyProviderTypeDef(TypedDict):
    EncryptionContractConfiguration: EncryptionContractConfigurationTypeDef
    ResourceId: str
    DrmSystems: Sequence[DrmSystemType]
    RoleArn: str
    Url: str

class GetDashManifestConfigurationTypeDef(TypedDict):
    ManifestName: str
    Url: str
    ManifestWindowSeconds: NotRequired[int]
    FilterConfiguration: NotRequired[FilterConfigurationOutputTypeDef]
    MinUpdatePeriodSeconds: NotRequired[int]
    MinBufferTimeSeconds: NotRequired[int]
    SuggestedPresentationDelaySeconds: NotRequired[int]
    SegmentTemplateFormat: NotRequired[Literal["NUMBER_WITH_TIMELINE"]]
    PeriodTriggers: NotRequired[List[DashPeriodTriggerType]]
    ScteDash: NotRequired[ScteDashTypeDef]
    DrmSignaling: NotRequired[DashDrmSignalingType]
    UtcTiming: NotRequired[DashUtcTimingTypeDef]

class GetHlsManifestConfigurationTypeDef(TypedDict):
    ManifestName: str
    Url: str
    ChildManifestName: NotRequired[str]
    ManifestWindowSeconds: NotRequired[int]
    ProgramDateTimeIntervalSeconds: NotRequired[int]
    ScteHls: NotRequired[ScteHlsTypeDef]
    FilterConfiguration: NotRequired[FilterConfigurationOutputTypeDef]
    StartTag: NotRequired[StartTagTypeDef]
    UrlEncodeChildManifest: NotRequired[bool]

class GetLowLatencyHlsManifestConfigurationTypeDef(TypedDict):
    ManifestName: str
    Url: str
    ChildManifestName: NotRequired[str]
    ManifestWindowSeconds: NotRequired[int]
    ProgramDateTimeIntervalSeconds: NotRequired[int]
    ScteHls: NotRequired[ScteHlsTypeDef]
    FilterConfiguration: NotRequired[FilterConfigurationOutputTypeDef]
    StartTag: NotRequired[StartTagTypeDef]
    UrlEncodeChildManifest: NotRequired[bool]

class FilterConfigurationTypeDef(TypedDict):
    ManifestFilter: NotRequired[str]
    Start: NotRequired[TimestampTypeDef]
    End: NotRequired[TimestampTypeDef]
    TimeDelaySeconds: NotRequired[int]
    ClipStartTime: NotRequired[TimestampTypeDef]

class HarvesterScheduleConfigurationTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

ForceEndpointErrorConfigurationUnionTypeDef = Union[
    ForceEndpointErrorConfigurationTypeDef, ForceEndpointErrorConfigurationOutputTypeDef
]

class GetHarvestJobRequestWaitTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    HarvestJobName: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class HarvestedManifestsOutputTypeDef(TypedDict):
    HlsManifests: NotRequired[List[HarvestedHlsManifestTypeDef]]
    DashManifests: NotRequired[List[HarvestedDashManifestTypeDef]]
    LowLatencyHlsManifests: NotRequired[List[HarvestedLowLatencyHlsManifestTypeDef]]

class HarvestedManifestsTypeDef(TypedDict):
    HlsManifests: NotRequired[Sequence[HarvestedHlsManifestTypeDef]]
    DashManifests: NotRequired[Sequence[HarvestedDashManifestTypeDef]]
    LowLatencyHlsManifests: NotRequired[Sequence[HarvestedLowLatencyHlsManifestTypeDef]]

class ListChannelGroupsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListChannelsRequestPaginateTypeDef(TypedDict):
    ChannelGroupName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHarvestJobsRequestPaginateTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: NotRequired[str]
    OriginEndpointName: NotRequired[str]
    Status: NotRequired[HarvestJobStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOriginEndpointsRequestPaginateTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class OriginEndpointListConfigurationTypeDef(TypedDict):
    Arn: str
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Description: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    ModifiedAt: NotRequired[datetime]
    HlsManifests: NotRequired[List[ListHlsManifestConfigurationTypeDef]]
    LowLatencyHlsManifests: NotRequired[List[ListLowLatencyHlsManifestConfigurationTypeDef]]
    DashManifests: NotRequired[List[ListDashManifestConfigurationTypeDef]]
    ForceEndpointErrorConfiguration: NotRequired[ForceEndpointErrorConfigurationOutputTypeDef]

class EncryptionOutputTypeDef(TypedDict):
    EncryptionMethod: EncryptionMethodTypeDef
    SpekeKeyProvider: SpekeKeyProviderOutputTypeDef
    ConstantInitializationVector: NotRequired[str]
    KeyRotationIntervalSeconds: NotRequired[int]

class EncryptionTypeDef(TypedDict):
    EncryptionMethod: EncryptionMethodTypeDef
    SpekeKeyProvider: SpekeKeyProviderTypeDef
    ConstantInitializationVector: NotRequired[str]
    KeyRotationIntervalSeconds: NotRequired[int]

FilterConfigurationUnionTypeDef = Union[
    FilterConfigurationTypeDef, FilterConfigurationOutputTypeDef
]
HarvesterScheduleConfigurationUnionTypeDef = Union[
    HarvesterScheduleConfigurationTypeDef, HarvesterScheduleConfigurationOutputTypeDef
]

class CreateHarvestJobResponseTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Destination: DestinationTypeDef
    HarvestJobName: str
    HarvestedManifests: HarvestedManifestsOutputTypeDef
    Description: str
    ScheduleConfiguration: HarvesterScheduleConfigurationOutputTypeDef
    Arn: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Status: HarvestJobStatusType
    ErrorMessage: str
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetHarvestJobResponseTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Destination: DestinationTypeDef
    HarvestJobName: str
    HarvestedManifests: HarvestedManifestsOutputTypeDef
    Description: str
    ScheduleConfiguration: HarvesterScheduleConfigurationOutputTypeDef
    Arn: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Status: HarvestJobStatusType
    ErrorMessage: str
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class HarvestJobTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    Destination: DestinationTypeDef
    HarvestJobName: str
    HarvestedManifests: HarvestedManifestsOutputTypeDef
    ScheduleConfiguration: HarvesterScheduleConfigurationOutputTypeDef
    Arn: str
    CreatedAt: datetime
    ModifiedAt: datetime
    Status: HarvestJobStatusType
    Description: NotRequired[str]
    ErrorMessage: NotRequired[str]
    ETag: NotRequired[str]

HarvestedManifestsUnionTypeDef = Union[HarvestedManifestsTypeDef, HarvestedManifestsOutputTypeDef]

class ListOriginEndpointsResponseTypeDef(TypedDict):
    Items: List[OriginEndpointListConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SegmentOutputTypeDef(TypedDict):
    SegmentDurationSeconds: NotRequired[int]
    SegmentName: NotRequired[str]
    TsUseAudioRenditionGroup: NotRequired[bool]
    IncludeIframeOnlyStreams: NotRequired[bool]
    TsIncludeDvbSubtitles: NotRequired[bool]
    Scte: NotRequired[ScteOutputTypeDef]
    Encryption: NotRequired[EncryptionOutputTypeDef]

class SegmentTypeDef(TypedDict):
    SegmentDurationSeconds: NotRequired[int]
    SegmentName: NotRequired[str]
    TsUseAudioRenditionGroup: NotRequired[bool]
    IncludeIframeOnlyStreams: NotRequired[bool]
    TsIncludeDvbSubtitles: NotRequired[bool]
    Scte: NotRequired[ScteTypeDef]
    Encryption: NotRequired[EncryptionTypeDef]

class CreateDashManifestConfigurationTypeDef(TypedDict):
    ManifestName: str
    ManifestWindowSeconds: NotRequired[int]
    FilterConfiguration: NotRequired[FilterConfigurationUnionTypeDef]
    MinUpdatePeriodSeconds: NotRequired[int]
    MinBufferTimeSeconds: NotRequired[int]
    SuggestedPresentationDelaySeconds: NotRequired[int]
    SegmentTemplateFormat: NotRequired[Literal["NUMBER_WITH_TIMELINE"]]
    PeriodTriggers: NotRequired[Sequence[DashPeriodTriggerType]]
    ScteDash: NotRequired[ScteDashTypeDef]
    DrmSignaling: NotRequired[DashDrmSignalingType]
    UtcTiming: NotRequired[DashUtcTimingTypeDef]

class CreateHlsManifestConfigurationTypeDef(TypedDict):
    ManifestName: str
    ChildManifestName: NotRequired[str]
    ScteHls: NotRequired[ScteHlsTypeDef]
    StartTag: NotRequired[StartTagTypeDef]
    ManifestWindowSeconds: NotRequired[int]
    ProgramDateTimeIntervalSeconds: NotRequired[int]
    FilterConfiguration: NotRequired[FilterConfigurationUnionTypeDef]
    UrlEncodeChildManifest: NotRequired[bool]

class CreateLowLatencyHlsManifestConfigurationTypeDef(TypedDict):
    ManifestName: str
    ChildManifestName: NotRequired[str]
    ScteHls: NotRequired[ScteHlsTypeDef]
    StartTag: NotRequired[StartTagTypeDef]
    ManifestWindowSeconds: NotRequired[int]
    ProgramDateTimeIntervalSeconds: NotRequired[int]
    FilterConfiguration: NotRequired[FilterConfigurationUnionTypeDef]
    UrlEncodeChildManifest: NotRequired[bool]

class ListHarvestJobsResponseTypeDef(TypedDict):
    Items: List[HarvestJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateHarvestJobRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    HarvestedManifests: HarvestedManifestsUnionTypeDef
    ScheduleConfiguration: HarvesterScheduleConfigurationUnionTypeDef
    Destination: DestinationTypeDef
    Description: NotRequired[str]
    ClientToken: NotRequired[str]
    HarvestJobName: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CreateOriginEndpointResponseTypeDef(TypedDict):
    Arn: str
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: SegmentOutputTypeDef
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    StartoverWindowSeconds: int
    HlsManifests: List[GetHlsManifestConfigurationTypeDef]
    LowLatencyHlsManifests: List[GetLowLatencyHlsManifestConfigurationTypeDef]
    DashManifests: List[GetDashManifestConfigurationTypeDef]
    ForceEndpointErrorConfiguration: ForceEndpointErrorConfigurationOutputTypeDef
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetOriginEndpointResponseTypeDef(TypedDict):
    Arn: str
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: SegmentOutputTypeDef
    CreatedAt: datetime
    ModifiedAt: datetime
    ResetAt: datetime
    Description: str
    StartoverWindowSeconds: int
    HlsManifests: List[GetHlsManifestConfigurationTypeDef]
    LowLatencyHlsManifests: List[GetLowLatencyHlsManifestConfigurationTypeDef]
    DashManifests: List[GetDashManifestConfigurationTypeDef]
    ForceEndpointErrorConfiguration: ForceEndpointErrorConfigurationOutputTypeDef
    ETag: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOriginEndpointResponseTypeDef(TypedDict):
    Arn: str
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: SegmentOutputTypeDef
    CreatedAt: datetime
    ModifiedAt: datetime
    Description: str
    StartoverWindowSeconds: int
    HlsManifests: List[GetHlsManifestConfigurationTypeDef]
    LowLatencyHlsManifests: List[GetLowLatencyHlsManifestConfigurationTypeDef]
    ForceEndpointErrorConfiguration: ForceEndpointErrorConfigurationOutputTypeDef
    ETag: str
    Tags: Dict[str, str]
    DashManifests: List[GetDashManifestConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

SegmentUnionTypeDef = Union[SegmentTypeDef, SegmentOutputTypeDef]

class CreateOriginEndpointRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: NotRequired[SegmentUnionTypeDef]
    ClientToken: NotRequired[str]
    Description: NotRequired[str]
    StartoverWindowSeconds: NotRequired[int]
    HlsManifests: NotRequired[Sequence[CreateHlsManifestConfigurationTypeDef]]
    LowLatencyHlsManifests: NotRequired[Sequence[CreateLowLatencyHlsManifestConfigurationTypeDef]]
    DashManifests: NotRequired[Sequence[CreateDashManifestConfigurationTypeDef]]
    ForceEndpointErrorConfiguration: NotRequired[ForceEndpointErrorConfigurationUnionTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class UpdateOriginEndpointRequestTypeDef(TypedDict):
    ChannelGroupName: str
    ChannelName: str
    OriginEndpointName: str
    ContainerType: ContainerTypeType
    Segment: NotRequired[SegmentUnionTypeDef]
    Description: NotRequired[str]
    StartoverWindowSeconds: NotRequired[int]
    HlsManifests: NotRequired[Sequence[CreateHlsManifestConfigurationTypeDef]]
    LowLatencyHlsManifests: NotRequired[Sequence[CreateLowLatencyHlsManifestConfigurationTypeDef]]
    DashManifests: NotRequired[Sequence[CreateDashManifestConfigurationTypeDef]]
    ForceEndpointErrorConfiguration: NotRequired[ForceEndpointErrorConfigurationUnionTypeDef]
    ETag: NotRequired[str]
