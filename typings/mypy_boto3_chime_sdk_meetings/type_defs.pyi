"""
Type annotations for chime-sdk-meetings service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_chime_sdk_meetings.type_defs import AttendeeCapabilitiesTypeDef

    data: AttendeeCapabilitiesTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from .literals import (
    ContentResolutionType,
    MediaCapabilitiesType,
    MeetingFeatureStatusType,
    TranscribeLanguageCodeType,
    TranscribeMedicalRegionType,
    TranscribeMedicalSpecialtyType,
    TranscribeMedicalTypeType,
    TranscribePartialResultsStabilityType,
    TranscribeRegionType,
    TranscribeVocabularyFilterMethodType,
    VideoResolutionType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AttendeeCapabilitiesTypeDef",
    "AttendeeFeaturesTypeDef",
    "AttendeeIdItemTypeDef",
    "AttendeeTypeDef",
    "AudioFeaturesTypeDef",
    "BatchCreateAttendeeRequestTypeDef",
    "BatchCreateAttendeeResponseTypeDef",
    "BatchUpdateAttendeeCapabilitiesExceptRequestTypeDef",
    "ContentFeaturesTypeDef",
    "CreateAttendeeErrorTypeDef",
    "CreateAttendeeRequestItemTypeDef",
    "CreateAttendeeRequestTypeDef",
    "CreateAttendeeResponseTypeDef",
    "CreateMeetingRequestTypeDef",
    "CreateMeetingResponseTypeDef",
    "CreateMeetingWithAttendeesRequestTypeDef",
    "CreateMeetingWithAttendeesResponseTypeDef",
    "DeleteAttendeeRequestTypeDef",
    "DeleteMeetingRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EngineTranscribeMedicalSettingsTypeDef",
    "EngineTranscribeSettingsTypeDef",
    "GetAttendeeRequestTypeDef",
    "GetAttendeeResponseTypeDef",
    "GetMeetingRequestTypeDef",
    "GetMeetingResponseTypeDef",
    "ListAttendeesRequestTypeDef",
    "ListAttendeesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MediaPlacementTypeDef",
    "MeetingFeaturesConfigurationTypeDef",
    "MeetingTypeDef",
    "NotificationsConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "StartMeetingTranscriptionRequestTypeDef",
    "StopMeetingTranscriptionRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TranscriptionConfigurationTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAttendeeCapabilitiesRequestTypeDef",
    "UpdateAttendeeCapabilitiesResponseTypeDef",
    "VideoFeaturesTypeDef",
)

class AttendeeCapabilitiesTypeDef(TypedDict):
    Audio: MediaCapabilitiesType
    Video: MediaCapabilitiesType
    Content: MediaCapabilitiesType

class AttendeeFeaturesTypeDef(TypedDict):
    MaxCount: NotRequired[int]

class AttendeeIdItemTypeDef(TypedDict):
    AttendeeId: str

class AudioFeaturesTypeDef(TypedDict):
    EchoReduction: NotRequired[MeetingFeatureStatusType]

class CreateAttendeeErrorTypeDef(TypedDict):
    ExternalUserId: NotRequired[str]
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ContentFeaturesTypeDef(TypedDict):
    MaxResolution: NotRequired[ContentResolutionType]

class NotificationsConfigurationTypeDef(TypedDict):
    LambdaFunctionArn: NotRequired[str]
    SnsTopicArn: NotRequired[str]
    SqsQueueArn: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class DeleteAttendeeRequestTypeDef(TypedDict):
    MeetingId: str
    AttendeeId: str

class DeleteMeetingRequestTypeDef(TypedDict):
    MeetingId: str

EngineTranscribeMedicalSettingsTypeDef = TypedDict(
    "EngineTranscribeMedicalSettingsTypeDef",
    {
        "LanguageCode": Literal["en-US"],
        "Specialty": TranscribeMedicalSpecialtyType,
        "Type": TranscribeMedicalTypeType,
        "VocabularyName": NotRequired[str],
        "Region": NotRequired[TranscribeMedicalRegionType],
        "ContentIdentificationType": NotRequired[Literal["PHI"]],
    },
)

class EngineTranscribeSettingsTypeDef(TypedDict):
    LanguageCode: NotRequired[TranscribeLanguageCodeType]
    VocabularyFilterMethod: NotRequired[TranscribeVocabularyFilterMethodType]
    VocabularyFilterName: NotRequired[str]
    VocabularyName: NotRequired[str]
    Region: NotRequired[TranscribeRegionType]
    EnablePartialResultsStabilization: NotRequired[bool]
    PartialResultsStability: NotRequired[TranscribePartialResultsStabilityType]
    ContentIdentificationType: NotRequired[Literal["PII"]]
    ContentRedactionType: NotRequired[Literal["PII"]]
    PiiEntityTypes: NotRequired[str]
    LanguageModelName: NotRequired[str]
    IdentifyLanguage: NotRequired[bool]
    LanguageOptions: NotRequired[str]
    PreferredLanguage: NotRequired[TranscribeLanguageCodeType]
    VocabularyNames: NotRequired[str]
    VocabularyFilterNames: NotRequired[str]

class GetAttendeeRequestTypeDef(TypedDict):
    MeetingId: str
    AttendeeId: str

class GetMeetingRequestTypeDef(TypedDict):
    MeetingId: str

class ListAttendeesRequestTypeDef(TypedDict):
    MeetingId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class MediaPlacementTypeDef(TypedDict):
    AudioHostUrl: NotRequired[str]
    AudioFallbackUrl: NotRequired[str]
    SignalingUrl: NotRequired[str]
    TurnControlUrl: NotRequired[str]
    ScreenDataUrl: NotRequired[str]
    ScreenViewingUrl: NotRequired[str]
    ScreenSharingUrl: NotRequired[str]
    EventIngestionUrl: NotRequired[str]

class VideoFeaturesTypeDef(TypedDict):
    MaxResolution: NotRequired[VideoResolutionType]

class StopMeetingTranscriptionRequestTypeDef(TypedDict):
    MeetingId: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class AttendeeTypeDef(TypedDict):
    ExternalUserId: NotRequired[str]
    AttendeeId: NotRequired[str]
    JoinToken: NotRequired[str]
    Capabilities: NotRequired[AttendeeCapabilitiesTypeDef]

class CreateAttendeeRequestItemTypeDef(TypedDict):
    ExternalUserId: str
    Capabilities: NotRequired[AttendeeCapabilitiesTypeDef]

class CreateAttendeeRequestTypeDef(TypedDict):
    MeetingId: str
    ExternalUserId: str
    Capabilities: NotRequired[AttendeeCapabilitiesTypeDef]

class UpdateAttendeeCapabilitiesRequestTypeDef(TypedDict):
    MeetingId: str
    AttendeeId: str
    Capabilities: AttendeeCapabilitiesTypeDef

class BatchUpdateAttendeeCapabilitiesExceptRequestTypeDef(TypedDict):
    MeetingId: str
    ExcludedAttendeeIds: Sequence[AttendeeIdItemTypeDef]
    Capabilities: AttendeeCapabilitiesTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class TranscriptionConfigurationTypeDef(TypedDict):
    EngineTranscribeSettings: NotRequired[EngineTranscribeSettingsTypeDef]
    EngineTranscribeMedicalSettings: NotRequired[EngineTranscribeMedicalSettingsTypeDef]

class MeetingFeaturesConfigurationTypeDef(TypedDict):
    Audio: NotRequired[AudioFeaturesTypeDef]
    Video: NotRequired[VideoFeaturesTypeDef]
    Content: NotRequired[ContentFeaturesTypeDef]
    Attendee: NotRequired[AttendeeFeaturesTypeDef]

class BatchCreateAttendeeResponseTypeDef(TypedDict):
    Attendees: List[AttendeeTypeDef]
    Errors: List[CreateAttendeeErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAttendeeResponseTypeDef(TypedDict):
    Attendee: AttendeeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAttendeeResponseTypeDef(TypedDict):
    Attendee: AttendeeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttendeesResponseTypeDef(TypedDict):
    Attendees: List[AttendeeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateAttendeeCapabilitiesResponseTypeDef(TypedDict):
    Attendee: AttendeeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateAttendeeRequestTypeDef(TypedDict):
    MeetingId: str
    Attendees: Sequence[CreateAttendeeRequestItemTypeDef]

class StartMeetingTranscriptionRequestTypeDef(TypedDict):
    MeetingId: str
    TranscriptionConfiguration: TranscriptionConfigurationTypeDef

class CreateMeetingRequestTypeDef(TypedDict):
    ClientRequestToken: str
    MediaRegion: str
    ExternalMeetingId: str
    MeetingHostId: NotRequired[str]
    NotificationsConfiguration: NotRequired[NotificationsConfigurationTypeDef]
    MeetingFeatures: NotRequired[MeetingFeaturesConfigurationTypeDef]
    PrimaryMeetingId: NotRequired[str]
    TenantIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateMeetingWithAttendeesRequestTypeDef(TypedDict):
    ClientRequestToken: str
    MediaRegion: str
    ExternalMeetingId: str
    Attendees: Sequence[CreateAttendeeRequestItemTypeDef]
    MeetingHostId: NotRequired[str]
    MeetingFeatures: NotRequired[MeetingFeaturesConfigurationTypeDef]
    NotificationsConfiguration: NotRequired[NotificationsConfigurationTypeDef]
    PrimaryMeetingId: NotRequired[str]
    TenantIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class MeetingTypeDef(TypedDict):
    MeetingId: NotRequired[str]
    MeetingHostId: NotRequired[str]
    ExternalMeetingId: NotRequired[str]
    MediaRegion: NotRequired[str]
    MediaPlacement: NotRequired[MediaPlacementTypeDef]
    MeetingFeatures: NotRequired[MeetingFeaturesConfigurationTypeDef]
    PrimaryMeetingId: NotRequired[str]
    TenantIds: NotRequired[List[str]]
    MeetingArn: NotRequired[str]

class CreateMeetingResponseTypeDef(TypedDict):
    Meeting: MeetingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMeetingWithAttendeesResponseTypeDef(TypedDict):
    Meeting: MeetingTypeDef
    Attendees: List[AttendeeTypeDef]
    Errors: List[CreateAttendeeErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMeetingResponseTypeDef(TypedDict):
    Meeting: MeetingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
