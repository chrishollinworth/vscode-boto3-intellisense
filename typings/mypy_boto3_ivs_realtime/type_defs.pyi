"""
Type annotations for ivs-realtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ivs_realtime.type_defs import CreateParticipantTokenRequestRequestTypeDef

    data: CreateParticipantTokenRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    EventErrorCodeType,
    EventNameType,
    ParticipantStateType,
    ParticipantTokenCapabilityType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateParticipantTokenRequestRequestTypeDef",
    "CreateParticipantTokenResponseTypeDef",
    "CreateStageRequestRequestTypeDef",
    "CreateStageResponseTypeDef",
    "DeleteStageRequestRequestTypeDef",
    "DisconnectParticipantRequestRequestTypeDef",
    "EventTypeDef",
    "GetParticipantRequestRequestTypeDef",
    "GetParticipantResponseTypeDef",
    "GetStageRequestRequestTypeDef",
    "GetStageResponseTypeDef",
    "GetStageSessionRequestRequestTypeDef",
    "GetStageSessionResponseTypeDef",
    "ListParticipantEventsRequestRequestTypeDef",
    "ListParticipantEventsResponseTypeDef",
    "ListParticipantsRequestRequestTypeDef",
    "ListParticipantsResponseTypeDef",
    "ListStageSessionsRequestRequestTypeDef",
    "ListStageSessionsResponseTypeDef",
    "ListStagesRequestRequestTypeDef",
    "ListStagesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ParticipantSummaryTypeDef",
    "ParticipantTokenConfigurationTypeDef",
    "ParticipantTokenTypeDef",
    "ParticipantTypeDef",
    "ResponseMetadataTypeDef",
    "StageSessionSummaryTypeDef",
    "StageSessionTypeDef",
    "StageSummaryTypeDef",
    "StageTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateStageRequestRequestTypeDef",
    "UpdateStageResponseTypeDef",
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

DeleteStageRequestRequestTypeDef = TypedDict(
    "DeleteStageRequestRequestTypeDef",
    {
        "arn": str,
    },
)

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
