"""
Type annotations for ivs-realtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ivs_realtime.type_defs import AutoParticipantRecordingConfigurationTypeDef

    data: AutoParticipantRecordingConfigurationTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    CompositionStateType,
    DestinationStateType,
    EventErrorCodeType,
    EventNameType,
    ParticipantRecordingFilterByRecordingStateType,
    ParticipantRecordingMediaTypeType,
    ParticipantRecordingStateType,
    ParticipantStateType,
    ParticipantTokenCapabilityType,
    PipBehaviorType,
    PipPositionType,
    VideoAspectRatioType,
    VideoFillModeType,
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
    "AutoParticipantRecordingConfigurationTypeDef",
    "ChannelDestinationConfigurationTypeDef",
    "CompositionSummaryTypeDef",
    "CompositionTypeDef",
    "CreateEncoderConfigurationRequestRequestTypeDef",
    "CreateEncoderConfigurationResponseTypeDef",
    "CreateParticipantTokenRequestRequestTypeDef",
    "CreateParticipantTokenResponseTypeDef",
    "CreateStageRequestRequestTypeDef",
    "CreateStageResponseTypeDef",
    "CreateStorageConfigurationRequestRequestTypeDef",
    "CreateStorageConfigurationResponseTypeDef",
    "DeleteEncoderConfigurationRequestRequestTypeDef",
    "DeletePublicKeyRequestRequestTypeDef",
    "DeleteStageRequestRequestTypeDef",
    "DeleteStorageConfigurationRequestRequestTypeDef",
    "DestinationConfigurationTypeDef",
    "DestinationDetailTypeDef",
    "DestinationSummaryTypeDef",
    "DestinationTypeDef",
    "DisconnectParticipantRequestRequestTypeDef",
    "EncoderConfigurationSummaryTypeDef",
    "EncoderConfigurationTypeDef",
    "EventTypeDef",
    "GetCompositionRequestRequestTypeDef",
    "GetCompositionResponseTypeDef",
    "GetEncoderConfigurationRequestRequestTypeDef",
    "GetEncoderConfigurationResponseTypeDef",
    "GetParticipantRequestRequestTypeDef",
    "GetParticipantResponseTypeDef",
    "GetPublicKeyRequestRequestTypeDef",
    "GetPublicKeyResponseTypeDef",
    "GetStageRequestRequestTypeDef",
    "GetStageResponseTypeDef",
    "GetStageSessionRequestRequestTypeDef",
    "GetStageSessionResponseTypeDef",
    "GetStorageConfigurationRequestRequestTypeDef",
    "GetStorageConfigurationResponseTypeDef",
    "GridConfigurationTypeDef",
    "ImportPublicKeyRequestRequestTypeDef",
    "ImportPublicKeyResponseTypeDef",
    "LayoutConfigurationTypeDef",
    "ListCompositionsRequestRequestTypeDef",
    "ListCompositionsResponseTypeDef",
    "ListEncoderConfigurationsRequestRequestTypeDef",
    "ListEncoderConfigurationsResponseTypeDef",
    "ListParticipantEventsRequestRequestTypeDef",
    "ListParticipantEventsResponseTypeDef",
    "ListParticipantsRequestRequestTypeDef",
    "ListParticipantsResponseTypeDef",
    "ListPublicKeysRequestRequestTypeDef",
    "ListPublicKeysResponseTypeDef",
    "ListStageSessionsRequestRequestTypeDef",
    "ListStageSessionsResponseTypeDef",
    "ListStagesRequestRequestTypeDef",
    "ListStagesResponseTypeDef",
    "ListStorageConfigurationsRequestRequestTypeDef",
    "ListStorageConfigurationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantSummaryTypeDef",
    "ParticipantTokenConfigurationTypeDef",
    "ParticipantTokenTypeDef",
    "ParticipantTypeDef",
    "PipConfigurationTypeDef",
    "PublicKeySummaryTypeDef",
    "PublicKeyTypeDef",
    "RecordingConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationConfigurationTypeDef",
    "S3DetailTypeDef",
    "S3StorageConfigurationTypeDef",
    "StageEndpointsTypeDef",
    "StageSessionSummaryTypeDef",
    "StageSessionTypeDef",
    "StageSummaryTypeDef",
    "StageTypeDef",
    "StartCompositionRequestRequestTypeDef",
    "StartCompositionResponseTypeDef",
    "StopCompositionRequestRequestTypeDef",
    "StorageConfigurationSummaryTypeDef",
    "StorageConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateStageRequestRequestTypeDef",
    "UpdateStageResponseTypeDef",
    "VideoTypeDef",
)

_RequiredAutoParticipantRecordingConfigurationTypeDef = TypedDict(
    "_RequiredAutoParticipantRecordingConfigurationTypeDef",
    {
        "storageConfigurationArn": str,
    },
)
_OptionalAutoParticipantRecordingConfigurationTypeDef = TypedDict(
    "_OptionalAutoParticipantRecordingConfigurationTypeDef",
    {
        "mediaTypes": List[ParticipantRecordingMediaTypeType],
    },
    total=False,
)

class AutoParticipantRecordingConfigurationTypeDef(
    _RequiredAutoParticipantRecordingConfigurationTypeDef,
    _OptionalAutoParticipantRecordingConfigurationTypeDef,
):
    pass

_RequiredChannelDestinationConfigurationTypeDef = TypedDict(
    "_RequiredChannelDestinationConfigurationTypeDef",
    {
        "channelArn": str,
    },
)
_OptionalChannelDestinationConfigurationTypeDef = TypedDict(
    "_OptionalChannelDestinationConfigurationTypeDef",
    {
        "encoderConfigurationArn": str,
    },
    total=False,
)

class ChannelDestinationConfigurationTypeDef(
    _RequiredChannelDestinationConfigurationTypeDef, _OptionalChannelDestinationConfigurationTypeDef
):
    pass

_RequiredCompositionSummaryTypeDef = TypedDict(
    "_RequiredCompositionSummaryTypeDef",
    {
        "arn": str,
        "stageArn": str,
        "destinations": List["DestinationSummaryTypeDef"],
        "state": CompositionStateType,
    },
)
_OptionalCompositionSummaryTypeDef = TypedDict(
    "_OptionalCompositionSummaryTypeDef",
    {
        "tags": Dict[str, str],
        "startTime": datetime,
        "endTime": datetime,
    },
    total=False,
)

class CompositionSummaryTypeDef(
    _RequiredCompositionSummaryTypeDef, _OptionalCompositionSummaryTypeDef
):
    pass

_RequiredCompositionTypeDef = TypedDict(
    "_RequiredCompositionTypeDef",
    {
        "arn": str,
        "stageArn": str,
        "state": CompositionStateType,
        "layout": "LayoutConfigurationTypeDef",
        "destinations": List["DestinationTypeDef"],
    },
)
_OptionalCompositionTypeDef = TypedDict(
    "_OptionalCompositionTypeDef",
    {
        "tags": Dict[str, str],
        "startTime": datetime,
        "endTime": datetime,
    },
    total=False,
)

class CompositionTypeDef(_RequiredCompositionTypeDef, _OptionalCompositionTypeDef):
    pass

CreateEncoderConfigurationRequestRequestTypeDef = TypedDict(
    "CreateEncoderConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "video": "VideoTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

CreateEncoderConfigurationResponseTypeDef = TypedDict(
    "CreateEncoderConfigurationResponseTypeDef",
    {
        "encoderConfiguration": "EncoderConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateParticipantTokenRequestRequestTypeDef = TypedDict(
    "_RequiredCreateParticipantTokenRequestRequestTypeDef",
    {
        "stageArn": str,
    },
)
_OptionalCreateParticipantTokenRequestRequestTypeDef = TypedDict(
    "_OptionalCreateParticipantTokenRequestRequestTypeDef",
    {
        "duration": int,
        "userId": str,
        "attributes": Dict[str, str],
        "capabilities": List[ParticipantTokenCapabilityType],
    },
    total=False,
)

class CreateParticipantTokenRequestRequestTypeDef(
    _RequiredCreateParticipantTokenRequestRequestTypeDef,
    _OptionalCreateParticipantTokenRequestRequestTypeDef,
):
    pass

CreateParticipantTokenResponseTypeDef = TypedDict(
    "CreateParticipantTokenResponseTypeDef",
    {
        "participantToken": "ParticipantTokenTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStageRequestRequestTypeDef = TypedDict(
    "CreateStageRequestRequestTypeDef",
    {
        "name": str,
        "participantTokenConfigurations": List["ParticipantTokenConfigurationTypeDef"],
        "tags": Dict[str, str],
        "autoParticipantRecordingConfiguration": "AutoParticipantRecordingConfigurationTypeDef",
    },
    total=False,
)

CreateStageResponseTypeDef = TypedDict(
    "CreateStageResponseTypeDef",
    {
        "stage": "StageTypeDef",
        "participantTokens": List["ParticipantTokenTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStorageConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStorageConfigurationRequestRequestTypeDef",
    {
        "s3": "S3StorageConfigurationTypeDef",
    },
)
_OptionalCreateStorageConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStorageConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateStorageConfigurationRequestRequestTypeDef(
    _RequiredCreateStorageConfigurationRequestRequestTypeDef,
    _OptionalCreateStorageConfigurationRequestRequestTypeDef,
):
    pass

CreateStorageConfigurationResponseTypeDef = TypedDict(
    "CreateStorageConfigurationResponseTypeDef",
    {
        "storageConfiguration": "StorageConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEncoderConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteEncoderConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeletePublicKeyRequestRequestTypeDef = TypedDict(
    "DeletePublicKeyRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteStageRequestRequestTypeDef = TypedDict(
    "DeleteStageRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteStorageConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteStorageConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "name": str,
        "channel": "ChannelDestinationConfigurationTypeDef",
        "s3": "S3DestinationConfigurationTypeDef",
    },
    total=False,
)

DestinationDetailTypeDef = TypedDict(
    "DestinationDetailTypeDef",
    {
        "s3": "S3DetailTypeDef",
    },
    total=False,
)

_RequiredDestinationSummaryTypeDef = TypedDict(
    "_RequiredDestinationSummaryTypeDef",
    {
        "id": str,
        "state": DestinationStateType,
    },
)
_OptionalDestinationSummaryTypeDef = TypedDict(
    "_OptionalDestinationSummaryTypeDef",
    {
        "startTime": datetime,
        "endTime": datetime,
    },
    total=False,
)

class DestinationSummaryTypeDef(
    _RequiredDestinationSummaryTypeDef, _OptionalDestinationSummaryTypeDef
):
    pass

_RequiredDestinationTypeDef = TypedDict(
    "_RequiredDestinationTypeDef",
    {
        "id": str,
        "state": DestinationStateType,
        "configuration": "DestinationConfigurationTypeDef",
    },
)
_OptionalDestinationTypeDef = TypedDict(
    "_OptionalDestinationTypeDef",
    {
        "startTime": datetime,
        "endTime": datetime,
        "detail": "DestinationDetailTypeDef",
    },
    total=False,
)

class DestinationTypeDef(_RequiredDestinationTypeDef, _OptionalDestinationTypeDef):
    pass

_RequiredDisconnectParticipantRequestRequestTypeDef = TypedDict(
    "_RequiredDisconnectParticipantRequestRequestTypeDef",
    {
        "stageArn": str,
        "participantId": str,
    },
)
_OptionalDisconnectParticipantRequestRequestTypeDef = TypedDict(
    "_OptionalDisconnectParticipantRequestRequestTypeDef",
    {
        "reason": str,
    },
    total=False,
)

class DisconnectParticipantRequestRequestTypeDef(
    _RequiredDisconnectParticipantRequestRequestTypeDef,
    _OptionalDisconnectParticipantRequestRequestTypeDef,
):
    pass

_RequiredEncoderConfigurationSummaryTypeDef = TypedDict(
    "_RequiredEncoderConfigurationSummaryTypeDef",
    {
        "arn": str,
    },
)
_OptionalEncoderConfigurationSummaryTypeDef = TypedDict(
    "_OptionalEncoderConfigurationSummaryTypeDef",
    {
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class EncoderConfigurationSummaryTypeDef(
    _RequiredEncoderConfigurationSummaryTypeDef, _OptionalEncoderConfigurationSummaryTypeDef
):
    pass

_RequiredEncoderConfigurationTypeDef = TypedDict(
    "_RequiredEncoderConfigurationTypeDef",
    {
        "arn": str,
    },
)
_OptionalEncoderConfigurationTypeDef = TypedDict(
    "_OptionalEncoderConfigurationTypeDef",
    {
        "name": str,
        "video": "VideoTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class EncoderConfigurationTypeDef(
    _RequiredEncoderConfigurationTypeDef, _OptionalEncoderConfigurationTypeDef
):
    pass

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "name": EventNameType,
        "participantId": str,
        "eventTime": datetime,
        "remoteParticipantId": str,
        "errorCode": EventErrorCodeType,
    },
    total=False,
)

GetCompositionRequestRequestTypeDef = TypedDict(
    "GetCompositionRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetCompositionResponseTypeDef = TypedDict(
    "GetCompositionResponseTypeDef",
    {
        "composition": "CompositionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEncoderConfigurationRequestRequestTypeDef = TypedDict(
    "GetEncoderConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetEncoderConfigurationResponseTypeDef = TypedDict(
    "GetEncoderConfigurationResponseTypeDef",
    {
        "encoderConfiguration": "EncoderConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetParticipantRequestRequestTypeDef = TypedDict(
    "GetParticipantRequestRequestTypeDef",
    {
        "stageArn": str,
        "sessionId": str,
        "participantId": str,
    },
)

GetParticipantResponseTypeDef = TypedDict(
    "GetParticipantResponseTypeDef",
    {
        "participant": "ParticipantTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPublicKeyRequestRequestTypeDef = TypedDict(
    "GetPublicKeyRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetPublicKeyResponseTypeDef = TypedDict(
    "GetPublicKeyResponseTypeDef",
    {
        "publicKey": "PublicKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStageRequestRequestTypeDef = TypedDict(
    "GetStageRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetStageResponseTypeDef = TypedDict(
    "GetStageResponseTypeDef",
    {
        "stage": "StageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStageSessionRequestRequestTypeDef = TypedDict(
    "GetStageSessionRequestRequestTypeDef",
    {
        "stageArn": str,
        "sessionId": str,
    },
)

GetStageSessionResponseTypeDef = TypedDict(
    "GetStageSessionResponseTypeDef",
    {
        "stageSession": "StageSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStorageConfigurationRequestRequestTypeDef = TypedDict(
    "GetStorageConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetStorageConfigurationResponseTypeDef = TypedDict(
    "GetStorageConfigurationResponseTypeDef",
    {
        "storageConfiguration": "StorageConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GridConfigurationTypeDef = TypedDict(
    "GridConfigurationTypeDef",
    {
        "featuredParticipantAttribute": str,
        "omitStoppedVideo": bool,
        "videoAspectRatio": VideoAspectRatioType,
        "videoFillMode": VideoFillModeType,
        "gridGap": int,
    },
    total=False,
)

_RequiredImportPublicKeyRequestRequestTypeDef = TypedDict(
    "_RequiredImportPublicKeyRequestRequestTypeDef",
    {
        "publicKeyMaterial": str,
    },
)
_OptionalImportPublicKeyRequestRequestTypeDef = TypedDict(
    "_OptionalImportPublicKeyRequestRequestTypeDef",
    {
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class ImportPublicKeyRequestRequestTypeDef(
    _RequiredImportPublicKeyRequestRequestTypeDef, _OptionalImportPublicKeyRequestRequestTypeDef
):
    pass

ImportPublicKeyResponseTypeDef = TypedDict(
    "ImportPublicKeyResponseTypeDef",
    {
        "publicKey": "PublicKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LayoutConfigurationTypeDef = TypedDict(
    "LayoutConfigurationTypeDef",
    {
        "grid": "GridConfigurationTypeDef",
        "pip": "PipConfigurationTypeDef",
    },
    total=False,
)

ListCompositionsRequestRequestTypeDef = TypedDict(
    "ListCompositionsRequestRequestTypeDef",
    {
        "filterByStageArn": str,
        "filterByEncoderConfigurationArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListCompositionsResponseTypeDef = TypedDict(
    "ListCompositionsResponseTypeDef",
    {
        "compositions": List["CompositionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEncoderConfigurationsRequestRequestTypeDef = TypedDict(
    "ListEncoderConfigurationsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListEncoderConfigurationsResponseTypeDef = TypedDict(
    "ListEncoderConfigurationsResponseTypeDef",
    {
        "encoderConfigurations": List["EncoderConfigurationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListParticipantEventsRequestRequestTypeDef = TypedDict(
    "_RequiredListParticipantEventsRequestRequestTypeDef",
    {
        "stageArn": str,
        "sessionId": str,
        "participantId": str,
    },
)
_OptionalListParticipantEventsRequestRequestTypeDef = TypedDict(
    "_OptionalListParticipantEventsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListParticipantEventsRequestRequestTypeDef(
    _RequiredListParticipantEventsRequestRequestTypeDef,
    _OptionalListParticipantEventsRequestRequestTypeDef,
):
    pass

ListParticipantEventsResponseTypeDef = TypedDict(
    "ListParticipantEventsResponseTypeDef",
    {
        "events": List["EventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListParticipantsRequestRequestTypeDef = TypedDict(
    "_RequiredListParticipantsRequestRequestTypeDef",
    {
        "stageArn": str,
        "sessionId": str,
    },
)
_OptionalListParticipantsRequestRequestTypeDef = TypedDict(
    "_OptionalListParticipantsRequestRequestTypeDef",
    {
        "filterByUserId": str,
        "filterByPublished": bool,
        "filterByState": ParticipantStateType,
        "nextToken": str,
        "maxResults": int,
        "filterByRecordingState": ParticipantRecordingFilterByRecordingStateType,
    },
    total=False,
)

class ListParticipantsRequestRequestTypeDef(
    _RequiredListParticipantsRequestRequestTypeDef, _OptionalListParticipantsRequestRequestTypeDef
):
    pass

ListParticipantsResponseTypeDef = TypedDict(
    "ListParticipantsResponseTypeDef",
    {
        "participants": List["ParticipantSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPublicKeysRequestRequestTypeDef = TypedDict(
    "ListPublicKeysRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListPublicKeysResponseTypeDef = TypedDict(
    "ListPublicKeysResponseTypeDef",
    {
        "publicKeys": List["PublicKeySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStageSessionsRequestRequestTypeDef = TypedDict(
    "_RequiredListStageSessionsRequestRequestTypeDef",
    {
        "stageArn": str,
    },
)
_OptionalListStageSessionsRequestRequestTypeDef = TypedDict(
    "_OptionalListStageSessionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListStageSessionsRequestRequestTypeDef(
    _RequiredListStageSessionsRequestRequestTypeDef, _OptionalListStageSessionsRequestRequestTypeDef
):
    pass

ListStageSessionsResponseTypeDef = TypedDict(
    "ListStageSessionsResponseTypeDef",
    {
        "stageSessions": List["StageSessionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStagesRequestRequestTypeDef = TypedDict(
    "ListStagesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListStagesResponseTypeDef = TypedDict(
    "ListStagesResponseTypeDef",
    {
        "stages": List["StageSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStorageConfigurationsRequestRequestTypeDef = TypedDict(
    "ListStorageConfigurationsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListStorageConfigurationsResponseTypeDef = TypedDict(
    "ListStorageConfigurationsResponseTypeDef",
    {
        "storageConfigurations": List["StorageConfigurationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
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

ParticipantSummaryTypeDef = TypedDict(
    "ParticipantSummaryTypeDef",
    {
        "participantId": str,
        "userId": str,
        "state": ParticipantStateType,
        "firstJoinTime": datetime,
        "published": bool,
        "recordingState": ParticipantRecordingStateType,
    },
    total=False,
)

ParticipantTokenConfigurationTypeDef = TypedDict(
    "ParticipantTokenConfigurationTypeDef",
    {
        "duration": int,
        "userId": str,
        "attributes": Dict[str, str],
        "capabilities": List[ParticipantTokenCapabilityType],
    },
    total=False,
)

ParticipantTokenTypeDef = TypedDict(
    "ParticipantTokenTypeDef",
    {
        "participantId": str,
        "token": str,
        "userId": str,
        "attributes": Dict[str, str],
        "duration": int,
        "capabilities": List[ParticipantTokenCapabilityType],
        "expirationTime": datetime,
    },
    total=False,
)

ParticipantTypeDef = TypedDict(
    "ParticipantTypeDef",
    {
        "participantId": str,
        "userId": str,
        "state": ParticipantStateType,
        "firstJoinTime": datetime,
        "attributes": Dict[str, str],
        "published": bool,
        "ispName": str,
        "osName": str,
        "osVersion": str,
        "browserName": str,
        "browserVersion": str,
        "sdkVersion": str,
        "recordingS3BucketName": str,
        "recordingS3Prefix": str,
        "recordingState": ParticipantRecordingStateType,
    },
    total=False,
)

PipConfigurationTypeDef = TypedDict(
    "PipConfigurationTypeDef",
    {
        "featuredParticipantAttribute": str,
        "omitStoppedVideo": bool,
        "videoFillMode": VideoFillModeType,
        "gridGap": int,
        "pipParticipantAttribute": str,
        "pipBehavior": PipBehaviorType,
        "pipOffset": int,
        "pipPosition": PipPositionType,
        "pipWidth": int,
        "pipHeight": int,
    },
    total=False,
)

PublicKeySummaryTypeDef = TypedDict(
    "PublicKeySummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

PublicKeyTypeDef = TypedDict(
    "PublicKeyTypeDef",
    {
        "arn": str,
        "name": str,
        "publicKeyMaterial": str,
        "fingerprint": str,
        "tags": Dict[str, str],
    },
    total=False,
)

RecordingConfigurationTypeDef = TypedDict(
    "RecordingConfigurationTypeDef",
    {
        "format": Literal["HLS"],
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

_RequiredS3DestinationConfigurationTypeDef = TypedDict(
    "_RequiredS3DestinationConfigurationTypeDef",
    {
        "storageConfigurationArn": str,
        "encoderConfigurationArns": List[str],
    },
)
_OptionalS3DestinationConfigurationTypeDef = TypedDict(
    "_OptionalS3DestinationConfigurationTypeDef",
    {
        "recordingConfiguration": "RecordingConfigurationTypeDef",
    },
    total=False,
)

class S3DestinationConfigurationTypeDef(
    _RequiredS3DestinationConfigurationTypeDef, _OptionalS3DestinationConfigurationTypeDef
):
    pass

S3DetailTypeDef = TypedDict(
    "S3DetailTypeDef",
    {
        "recordingPrefix": str,
    },
)

S3StorageConfigurationTypeDef = TypedDict(
    "S3StorageConfigurationTypeDef",
    {
        "bucketName": str,
    },
)

StageEndpointsTypeDef = TypedDict(
    "StageEndpointsTypeDef",
    {
        "events": str,
        "whip": str,
    },
    total=False,
)

StageSessionSummaryTypeDef = TypedDict(
    "StageSessionSummaryTypeDef",
    {
        "sessionId": str,
        "startTime": datetime,
        "endTime": datetime,
    },
    total=False,
)

StageSessionTypeDef = TypedDict(
    "StageSessionTypeDef",
    {
        "sessionId": str,
        "startTime": datetime,
        "endTime": datetime,
    },
    total=False,
)

_RequiredStageSummaryTypeDef = TypedDict(
    "_RequiredStageSummaryTypeDef",
    {
        "arn": str,
    },
)
_OptionalStageSummaryTypeDef = TypedDict(
    "_OptionalStageSummaryTypeDef",
    {
        "name": str,
        "activeSessionId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class StageSummaryTypeDef(_RequiredStageSummaryTypeDef, _OptionalStageSummaryTypeDef):
    pass

_RequiredStageTypeDef = TypedDict(
    "_RequiredStageTypeDef",
    {
        "arn": str,
    },
)
_OptionalStageTypeDef = TypedDict(
    "_OptionalStageTypeDef",
    {
        "name": str,
        "activeSessionId": str,
        "tags": Dict[str, str],
        "autoParticipantRecordingConfiguration": "AutoParticipantRecordingConfigurationTypeDef",
        "endpoints": "StageEndpointsTypeDef",
    },
    total=False,
)

class StageTypeDef(_RequiredStageTypeDef, _OptionalStageTypeDef):
    pass

_RequiredStartCompositionRequestRequestTypeDef = TypedDict(
    "_RequiredStartCompositionRequestRequestTypeDef",
    {
        "stageArn": str,
        "destinations": List["DestinationConfigurationTypeDef"],
    },
)
_OptionalStartCompositionRequestRequestTypeDef = TypedDict(
    "_OptionalStartCompositionRequestRequestTypeDef",
    {
        "idempotencyToken": str,
        "layout": "LayoutConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class StartCompositionRequestRequestTypeDef(
    _RequiredStartCompositionRequestRequestTypeDef, _OptionalStartCompositionRequestRequestTypeDef
):
    pass

StartCompositionResponseTypeDef = TypedDict(
    "StartCompositionResponseTypeDef",
    {
        "composition": "CompositionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopCompositionRequestRequestTypeDef = TypedDict(
    "StopCompositionRequestRequestTypeDef",
    {
        "arn": str,
    },
)

_RequiredStorageConfigurationSummaryTypeDef = TypedDict(
    "_RequiredStorageConfigurationSummaryTypeDef",
    {
        "arn": str,
    },
)
_OptionalStorageConfigurationSummaryTypeDef = TypedDict(
    "_OptionalStorageConfigurationSummaryTypeDef",
    {
        "name": str,
        "s3": "S3StorageConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class StorageConfigurationSummaryTypeDef(
    _RequiredStorageConfigurationSummaryTypeDef, _OptionalStorageConfigurationSummaryTypeDef
):
    pass

_RequiredStorageConfigurationTypeDef = TypedDict(
    "_RequiredStorageConfigurationTypeDef",
    {
        "arn": str,
    },
)
_OptionalStorageConfigurationTypeDef = TypedDict(
    "_OptionalStorageConfigurationTypeDef",
    {
        "name": str,
        "s3": "S3StorageConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class StorageConfigurationTypeDef(
    _RequiredStorageConfigurationTypeDef, _OptionalStorageConfigurationTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateStageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStageRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateStageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStageRequestRequestTypeDef",
    {
        "name": str,
        "autoParticipantRecordingConfiguration": "AutoParticipantRecordingConfigurationTypeDef",
    },
    total=False,
)

class UpdateStageRequestRequestTypeDef(
    _RequiredUpdateStageRequestRequestTypeDef, _OptionalUpdateStageRequestRequestTypeDef
):
    pass

UpdateStageResponseTypeDef = TypedDict(
    "UpdateStageResponseTypeDef",
    {
        "stage": "StageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VideoTypeDef = TypedDict(
    "VideoTypeDef",
    {
        "width": int,
        "height": int,
        "framerate": float,
        "bitrate": int,
    },
    total=False,
)
