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

from .literals import ParticipantTokenCapabilityType

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
    "GetStageRequestRequestTypeDef",
    "GetStageResponseTypeDef",
    "ListStagesRequestRequestTypeDef",
    "ListStagesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ParticipantTokenConfigurationTypeDef",
    "ParticipantTokenTypeDef",
    "ResponseMetadataTypeDef",
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
