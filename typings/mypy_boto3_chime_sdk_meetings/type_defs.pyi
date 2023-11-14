"""
Type annotations for chime-sdk-meetings service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/type_defs.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_meetings.type_defs import AttendeeCapabilitiesTypeDef

    data: AttendeeCapabilitiesTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    MediaCapabilitiesType,
    MeetingFeatureStatusType,
    TranscribeLanguageCodeType,
    TranscribeMedicalRegionType,
    TranscribeMedicalSpecialtyType,
    TranscribeMedicalTypeType,
    TranscribePartialResultsStabilityType,
    TranscribeRegionType,
    TranscribeVocabularyFilterMethodType,
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
    "AttendeeCapabilitiesTypeDef",
    "AttendeeIdItemTypeDef",
    "AttendeeTypeDef",
    "AudioFeaturesTypeDef",
    "BatchCreateAttendeeRequestRequestTypeDef",
    "BatchCreateAttendeeResponseTypeDef",
    "BatchUpdateAttendeeCapabilitiesExceptRequestRequestTypeDef",
    "CreateAttendeeErrorTypeDef",
    "CreateAttendeeRequestItemTypeDef",
    "CreateAttendeeRequestRequestTypeDef",
    "CreateAttendeeResponseTypeDef",
    "CreateMeetingRequestRequestTypeDef",
    "CreateMeetingResponseTypeDef",
    "CreateMeetingWithAttendeesRequestRequestTypeDef",
    "CreateMeetingWithAttendeesResponseTypeDef",
    "DeleteAttendeeRequestRequestTypeDef",
    "DeleteMeetingRequestRequestTypeDef",
    "EngineTranscribeMedicalSettingsTypeDef",
    "EngineTranscribeSettingsTypeDef",
    "GetAttendeeRequestRequestTypeDef",
    "GetAttendeeResponseTypeDef",
    "GetMeetingRequestRequestTypeDef",
    "GetMeetingResponseTypeDef",
    "ListAttendeesRequestRequestTypeDef",
    "ListAttendeesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MediaPlacementTypeDef",
    "MeetingFeaturesConfigurationTypeDef",
    "MeetingTypeDef",
    "NotificationsConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "StartMeetingTranscriptionRequestRequestTypeDef",
    "StopMeetingTranscriptionRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TranscriptionConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAttendeeCapabilitiesRequestRequestTypeDef",
    "UpdateAttendeeCapabilitiesResponseTypeDef",
)

AttendeeCapabilitiesTypeDef = TypedDict(
    "AttendeeCapabilitiesTypeDef",
    {
        "Audio": MediaCapabilitiesType,
        "Video": MediaCapabilitiesType,
        "Content": MediaCapabilitiesType,
    },
)

AttendeeIdItemTypeDef = TypedDict(
    "AttendeeIdItemTypeDef",
    {
        "AttendeeId": str,
    },
)

AttendeeTypeDef = TypedDict(
    "AttendeeTypeDef",
    {
        "ExternalUserId": str,
        "AttendeeId": str,
        "JoinToken": str,
        "Capabilities": "AttendeeCapabilitiesTypeDef",
    },
    total=False,
)

AudioFeaturesTypeDef = TypedDict(
    "AudioFeaturesTypeDef",
    {
        "EchoReduction": MeetingFeatureStatusType,
    },
    total=False,
)

BatchCreateAttendeeRequestRequestTypeDef = TypedDict(
    "BatchCreateAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "Attendees": List["CreateAttendeeRequestItemTypeDef"],
    },
)

BatchCreateAttendeeResponseTypeDef = TypedDict(
    "BatchCreateAttendeeResponseTypeDef",
    {
        "Attendees": List["AttendeeTypeDef"],
        "Errors": List["CreateAttendeeErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateAttendeeCapabilitiesExceptRequestRequestTypeDef = TypedDict(
    "BatchUpdateAttendeeCapabilitiesExceptRequestRequestTypeDef",
    {
        "MeetingId": str,
        "ExcludedAttendeeIds": List["AttendeeIdItemTypeDef"],
        "Capabilities": "AttendeeCapabilitiesTypeDef",
    },
)

CreateAttendeeErrorTypeDef = TypedDict(
    "CreateAttendeeErrorTypeDef",
    {
        "ExternalUserId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredCreateAttendeeRequestItemTypeDef = TypedDict(
    "_RequiredCreateAttendeeRequestItemTypeDef",
    {
        "ExternalUserId": str,
    },
)
_OptionalCreateAttendeeRequestItemTypeDef = TypedDict(
    "_OptionalCreateAttendeeRequestItemTypeDef",
    {
        "Capabilities": "AttendeeCapabilitiesTypeDef",
    },
    total=False,
)

class CreateAttendeeRequestItemTypeDef(
    _RequiredCreateAttendeeRequestItemTypeDef, _OptionalCreateAttendeeRequestItemTypeDef
):
    pass

_RequiredCreateAttendeeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "ExternalUserId": str,
    },
)
_OptionalCreateAttendeeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAttendeeRequestRequestTypeDef",
    {
        "Capabilities": "AttendeeCapabilitiesTypeDef",
    },
    total=False,
)

class CreateAttendeeRequestRequestTypeDef(
    _RequiredCreateAttendeeRequestRequestTypeDef, _OptionalCreateAttendeeRequestRequestTypeDef
):
    pass

CreateAttendeeResponseTypeDef = TypedDict(
    "CreateAttendeeResponseTypeDef",
    {
        "Attendee": "AttendeeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMeetingRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMeetingRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "MediaRegion": str,
        "ExternalMeetingId": str,
    },
)
_OptionalCreateMeetingRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMeetingRequestRequestTypeDef",
    {
        "MeetingHostId": str,
        "NotificationsConfiguration": "NotificationsConfigurationTypeDef",
        "MeetingFeatures": "MeetingFeaturesConfigurationTypeDef",
        "PrimaryMeetingId": str,
        "TenantIds": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateMeetingRequestRequestTypeDef(
    _RequiredCreateMeetingRequestRequestTypeDef, _OptionalCreateMeetingRequestRequestTypeDef
):
    pass

CreateMeetingResponseTypeDef = TypedDict(
    "CreateMeetingResponseTypeDef",
    {
        "Meeting": "MeetingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMeetingWithAttendeesRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMeetingWithAttendeesRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "MediaRegion": str,
        "ExternalMeetingId": str,
        "Attendees": List["CreateAttendeeRequestItemTypeDef"],
    },
)
_OptionalCreateMeetingWithAttendeesRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMeetingWithAttendeesRequestRequestTypeDef",
    {
        "MeetingHostId": str,
        "MeetingFeatures": "MeetingFeaturesConfigurationTypeDef",
        "NotificationsConfiguration": "NotificationsConfigurationTypeDef",
        "PrimaryMeetingId": str,
        "TenantIds": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateMeetingWithAttendeesRequestRequestTypeDef(
    _RequiredCreateMeetingWithAttendeesRequestRequestTypeDef,
    _OptionalCreateMeetingWithAttendeesRequestRequestTypeDef,
):
    pass

CreateMeetingWithAttendeesResponseTypeDef = TypedDict(
    "CreateMeetingWithAttendeesResponseTypeDef",
    {
        "Meeting": "MeetingTypeDef",
        "Attendees": List["AttendeeTypeDef"],
        "Errors": List["CreateAttendeeErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAttendeeRequestRequestTypeDef = TypedDict(
    "DeleteAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

DeleteMeetingRequestRequestTypeDef = TypedDict(
    "DeleteMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

_RequiredEngineTranscribeMedicalSettingsTypeDef = TypedDict(
    "_RequiredEngineTranscribeMedicalSettingsTypeDef",
    {
        "LanguageCode": Literal["en-US"],
        "Specialty": TranscribeMedicalSpecialtyType,
        "Type": TranscribeMedicalTypeType,
    },
)
_OptionalEngineTranscribeMedicalSettingsTypeDef = TypedDict(
    "_OptionalEngineTranscribeMedicalSettingsTypeDef",
    {
        "VocabularyName": str,
        "Region": TranscribeMedicalRegionType,
        "ContentIdentificationType": Literal["PHI"],
    },
    total=False,
)

class EngineTranscribeMedicalSettingsTypeDef(
    _RequiredEngineTranscribeMedicalSettingsTypeDef, _OptionalEngineTranscribeMedicalSettingsTypeDef
):
    pass

EngineTranscribeSettingsTypeDef = TypedDict(
    "EngineTranscribeSettingsTypeDef",
    {
        "LanguageCode": TranscribeLanguageCodeType,
        "VocabularyFilterMethod": TranscribeVocabularyFilterMethodType,
        "VocabularyFilterName": str,
        "VocabularyName": str,
        "Region": TranscribeRegionType,
        "EnablePartialResultsStabilization": bool,
        "PartialResultsStability": TranscribePartialResultsStabilityType,
        "ContentIdentificationType": Literal["PII"],
        "ContentRedactionType": Literal["PII"],
        "PiiEntityTypes": str,
        "LanguageModelName": str,
        "IdentifyLanguage": bool,
        "LanguageOptions": str,
        "PreferredLanguage": TranscribeLanguageCodeType,
        "VocabularyNames": str,
        "VocabularyFilterNames": str,
    },
    total=False,
)

GetAttendeeRequestRequestTypeDef = TypedDict(
    "GetAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

GetAttendeeResponseTypeDef = TypedDict(
    "GetAttendeeResponseTypeDef",
    {
        "Attendee": "AttendeeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMeetingRequestRequestTypeDef = TypedDict(
    "GetMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

GetMeetingResponseTypeDef = TypedDict(
    "GetMeetingResponseTypeDef",
    {
        "Meeting": "MeetingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAttendeesRequestRequestTypeDef = TypedDict(
    "_RequiredListAttendeesRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)
_OptionalListAttendeesRequestRequestTypeDef = TypedDict(
    "_OptionalListAttendeesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListAttendeesRequestRequestTypeDef(
    _RequiredListAttendeesRequestRequestTypeDef, _OptionalListAttendeesRequestRequestTypeDef
):
    pass

ListAttendeesResponseTypeDef = TypedDict(
    "ListAttendeesResponseTypeDef",
    {
        "Attendees": List["AttendeeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MediaPlacementTypeDef = TypedDict(
    "MediaPlacementTypeDef",
    {
        "AudioHostUrl": str,
        "AudioFallbackUrl": str,
        "SignalingUrl": str,
        "TurnControlUrl": str,
        "ScreenDataUrl": str,
        "ScreenViewingUrl": str,
        "ScreenSharingUrl": str,
        "EventIngestionUrl": str,
    },
    total=False,
)

MeetingFeaturesConfigurationTypeDef = TypedDict(
    "MeetingFeaturesConfigurationTypeDef",
    {
        "Audio": "AudioFeaturesTypeDef",
    },
    total=False,
)

MeetingTypeDef = TypedDict(
    "MeetingTypeDef",
    {
        "MeetingId": str,
        "MeetingHostId": str,
        "ExternalMeetingId": str,
        "MediaRegion": str,
        "MediaPlacement": "MediaPlacementTypeDef",
        "MeetingFeatures": "MeetingFeaturesConfigurationTypeDef",
        "PrimaryMeetingId": str,
        "TenantIds": List[str],
        "MeetingArn": str,
    },
    total=False,
)

NotificationsConfigurationTypeDef = TypedDict(
    "NotificationsConfigurationTypeDef",
    {
        "LambdaFunctionArn": str,
        "SnsTopicArn": str,
        "SqsQueueArn": str,
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

StartMeetingTranscriptionRequestRequestTypeDef = TypedDict(
    "StartMeetingTranscriptionRequestRequestTypeDef",
    {
        "MeetingId": str,
        "TranscriptionConfiguration": "TranscriptionConfigurationTypeDef",
    },
)

StopMeetingTranscriptionRequestRequestTypeDef = TypedDict(
    "StopMeetingTranscriptionRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TranscriptionConfigurationTypeDef = TypedDict(
    "TranscriptionConfigurationTypeDef",
    {
        "EngineTranscribeSettings": "EngineTranscribeSettingsTypeDef",
        "EngineTranscribeMedicalSettings": "EngineTranscribeMedicalSettingsTypeDef",
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UpdateAttendeeCapabilitiesRequestRequestTypeDef = TypedDict(
    "UpdateAttendeeCapabilitiesRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
        "Capabilities": "AttendeeCapabilitiesTypeDef",
    },
)

UpdateAttendeeCapabilitiesResponseTypeDef = TypedDict(
    "UpdateAttendeeCapabilitiesResponseTypeDef",
    {
        "Attendee": "AttendeeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
