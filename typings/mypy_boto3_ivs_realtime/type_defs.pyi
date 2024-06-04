"""
Type annotations for ivs-realtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ivs_realtime.type_defs import ChannelDestinationConfigurationTypeDef

    data: ChannelDestinationConfigurationTypeDef = {...}
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
    "GetStageRequestRequestTypeDef",
    "GetStageResponseTypeDef",
    "GetStageSessionRequestRequestTypeDef",
    "GetStageSessionResponseTypeDef",
    "GetStorageConfigurationRequestRequestTypeDef",
    "GetStorageConfigurationResponseTypeDef",
    "GridConfigurationTypeDef",
    "LayoutConfigurationTypeDef",
    "ListCompositionsRequestRequestTypeDef",
    "ListCompositionsResponseTypeDef",
    "ListEncoderConfigurationsRequestRequestTypeDef",
    "ListEncoderConfigurationsResponseTypeDef",
    "ListParticipantEventsRequestRequestTypeDef",
    "ListParticipantEventsResponseTypeDef",
    "ListParticipantsRequestRequestTypeDef",
    "ListParticipantsResponseTypeDef",
    "ListStageSessionsRequestRequestTypeDef",
    "ListStageSessionsResponseTypeDef",
    "ListStagesRequestRequestTypeDef",
    "ListStagesResponseTypeDef",
    "ListStorageConfigurationsRequestRequestTypeDef",
    "ListStorageConfigurationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ParticipantSummaryTypeDef",
    "ParticipantTokenConfigurationTypeDef",
    "ParticipantTokenTypeDef",
    "ParticipantTypeDef",
    "PipConfigurationTypeDef",
    "RecordingConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationConfigurationTypeDef",
    "S3DetailTypeDef",
    "S3StorageConfigurationTypeDef",
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
        "destinations": List["DestinationSummaryTypeDef"],
        "stageArn": str,
        "state": CompositionStateType,
    },
)
_OptionalCompositionSummaryTypeDef = TypedDict(
    "_OptionalCompositionSummaryTypeDef",
    {
        "endTime": datetime,
        "startTime": datetime,
        "tags": Dict[str, str],
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
        "destinations": List["DestinationTypeDef"],
        "layout": "LayoutConfigurationTypeDef",
        "stageArn": str,
        "state": CompositionStateType,
    },
)
_OptionalCompositionTypeDef = TypedDict(
    "_OptionalCompositionTypeDef",
    {
        "endTime": datetime,
        "startTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

class CompositionTypeDef(_RequiredCompositionTypeDef, _OptionalCompositionTypeDef):
    pass

CreateEncoderConfigurationRequestRequestTypeDef = TypedDict(
    "CreateEncoderConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "tags": Dict[str, str],
        "video": "VideoTypeDef",
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
        "attributes": Dict[str, str],
        "capabilities": List[ParticipantTokenCapabilityType],
        "duration": int,
        "userId": str,
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
    },
    total=False,
)

CreateStageResponseTypeDef = TypedDict(
    "CreateStageResponseTypeDef",
    {
        "participantTokens": List["ParticipantTokenTypeDef"],
        "stage": "StageTypeDef",
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
        "channel": "ChannelDestinationConfigurationTypeDef",
        "name": str,
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
        "endTime": datetime,
        "startTime": datetime,
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
        "configuration": "DestinationConfigurationTypeDef",
        "id": str,
        "state": DestinationStateType,
    },
)
_OptionalDestinationTypeDef = TypedDict(
    "_OptionalDestinationTypeDef",
    {
        "detail": "DestinationDetailTypeDef",
        "endTime": datetime,
        "startTime": datetime,
    },
    total=False,
)

class DestinationTypeDef(_RequiredDestinationTypeDef, _OptionalDestinationTypeDef):
    pass

_RequiredDisconnectParticipantRequestRequestTypeDef = TypedDict(
    "_RequiredDisconnectParticipantRequestRequestTypeDef",
    {
        "participantId": str,
        "stageArn": str,
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
        "tags": Dict[str, str],
        "video": "VideoTypeDef",
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
        "errorCode": EventErrorCodeType,
        "eventTime": datetime,
        "name": EventNameType,
        "participantId": str,
        "remoteParticipantId": str,
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
        "participantId": str,
        "sessionId": str,
        "stageArn": str,
    },
)

GetParticipantResponseTypeDef = TypedDict(
    "GetParticipantResponseTypeDef",
    {
        "participant": "ParticipantTypeDef",
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
        "sessionId": str,
        "stageArn": str,
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
        "gridGap": int,
        "omitStoppedVideo": bool,
        "videoAspectRatio": VideoAspectRatioType,
        "videoFillMode": VideoFillModeType,
    },
    total=False,
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
        "filterByEncoderConfigurationArn": str,
        "filterByStageArn": str,
        "maxResults": int,
        "nextToken": str,
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
        "maxResults": int,
        "nextToken": str,
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
        "participantId": str,
        "sessionId": str,
        "stageArn": str,
    },
)
_OptionalListParticipantEventsRequestRequestTypeDef = TypedDict(
    "_OptionalListParticipantEventsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
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
        "sessionId": str,
        "stageArn": str,
    },
)
_OptionalListParticipantsRequestRequestTypeDef = TypedDict(
    "_OptionalListParticipantsRequestRequestTypeDef",
    {
        "filterByPublished": bool,
        "filterByState": ParticipantStateType,
        "filterByUserId": str,
        "maxResults": int,
        "nextToken": str,
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
        "nextToken": str,
        "participants": List["ParticipantSummaryTypeDef"],
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
        "maxResults": int,
        "nextToken": str,
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
        "nextToken": str,
        "stageSessions": List["StageSessionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStagesRequestRequestTypeDef = TypedDict(
    "ListStagesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListStagesResponseTypeDef = TypedDict(
    "ListStagesResponseTypeDef",
    {
        "nextToken": str,
        "stages": List["StageSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStorageConfigurationsRequestRequestTypeDef = TypedDict(
    "ListStorageConfigurationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListStorageConfigurationsResponseTypeDef = TypedDict(
    "ListStorageConfigurationsResponseTypeDef",
    {
        "nextToken": str,
        "storageConfigurations": List["StorageConfigurationSummaryTypeDef"],
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

ParticipantSummaryTypeDef = TypedDict(
    "ParticipantSummaryTypeDef",
    {
        "firstJoinTime": datetime,
        "participantId": str,
        "published": bool,
        "state": ParticipantStateType,
        "userId": str,
    },
    total=False,
)

ParticipantTokenConfigurationTypeDef = TypedDict(
    "ParticipantTokenConfigurationTypeDef",
    {
        "attributes": Dict[str, str],
        "capabilities": List[ParticipantTokenCapabilityType],
        "duration": int,
        "userId": str,
    },
    total=False,
)

ParticipantTokenTypeDef = TypedDict(
    "ParticipantTokenTypeDef",
    {
        "attributes": Dict[str, str],
        "capabilities": List[ParticipantTokenCapabilityType],
        "duration": int,
        "expirationTime": datetime,
        "participantId": str,
        "token": str,
        "userId": str,
    },
    total=False,
)

ParticipantTypeDef = TypedDict(
    "ParticipantTypeDef",
    {
        "attributes": Dict[str, str],
        "browserName": str,
        "browserVersion": str,
        "firstJoinTime": datetime,
        "ispName": str,
        "osName": str,
        "osVersion": str,
        "participantId": str,
        "published": bool,
        "sdkVersion": str,
        "state": ParticipantStateType,
        "userId": str,
    },
    total=False,
)

PipConfigurationTypeDef = TypedDict(
    "PipConfigurationTypeDef",
    {
        "featuredParticipantAttribute": str,
        "gridGap": int,
        "omitStoppedVideo": bool,
        "pipBehavior": PipBehaviorType,
        "pipHeight": int,
        "pipOffset": int,
        "pipParticipantAttribute": str,
        "pipPosition": PipPositionType,
        "pipWidth": int,
        "videoFillMode": VideoFillModeType,
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
        "encoderConfigurationArns": List[str],
        "storageConfigurationArn": str,
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

StageSessionSummaryTypeDef = TypedDict(
    "StageSessionSummaryTypeDef",
    {
        "endTime": datetime,
        "sessionId": str,
        "startTime": datetime,
    },
    total=False,
)

StageSessionTypeDef = TypedDict(
    "StageSessionTypeDef",
    {
        "endTime": datetime,
        "sessionId": str,
        "startTime": datetime,
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
        "activeSessionId": str,
        "name": str,
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
        "activeSessionId": str,
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class StageTypeDef(_RequiredStageTypeDef, _OptionalStageTypeDef):
    pass

_RequiredStartCompositionRequestRequestTypeDef = TypedDict(
    "_RequiredStartCompositionRequestRequestTypeDef",
    {
        "destinations": List["DestinationConfigurationTypeDef"],
        "stageArn": str,
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
        "bitrate": int,
        "framerate": float,
        "height": int,
        "width": int,
    },
    total=False,
)
