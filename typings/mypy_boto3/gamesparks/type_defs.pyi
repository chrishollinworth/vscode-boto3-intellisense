"""
Type annotations for gamesparks service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/type_defs.html)

Usage::

    ```python
    from mypy_boto3_gamesparks.type_defs import ConnectionTypeDef

    data: ConnectionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    DeploymentActionType,
    DeploymentStateType,
    GameStateType,
    GeneratedCodeJobStateType,
    OperationType,
    ResultCodeType,
    StageStateType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ConnectionTypeDef",
    "CreateGameRequestRequestTypeDef",
    "CreateGameResultTypeDef",
    "CreateSnapshotRequestRequestTypeDef",
    "CreateSnapshotResultTypeDef",
    "CreateStageRequestRequestTypeDef",
    "CreateStageResultTypeDef",
    "DeleteGameRequestRequestTypeDef",
    "DeleteStageRequestRequestTypeDef",
    "DeploymentResultTypeDef",
    "DisconnectPlayerRequestRequestTypeDef",
    "DisconnectPlayerResultTypeDef",
    "ExportSnapshotRequestRequestTypeDef",
    "ExportSnapshotResultTypeDef",
    "ExtensionDetailsTypeDef",
    "ExtensionVersionDetailsTypeDef",
    "GameConfigurationDetailsTypeDef",
    "GameDetailsTypeDef",
    "GameSummaryTypeDef",
    "GeneratedCodeJobDetailsTypeDef",
    "GeneratorTypeDef",
    "GetExtensionRequestRequestTypeDef",
    "GetExtensionResultTypeDef",
    "GetExtensionVersionRequestRequestTypeDef",
    "GetExtensionVersionResultTypeDef",
    "GetGameConfigurationRequestRequestTypeDef",
    "GetGameConfigurationResultTypeDef",
    "GetGameRequestRequestTypeDef",
    "GetGameResultTypeDef",
    "GetGeneratedCodeJobRequestRequestTypeDef",
    "GetGeneratedCodeJobResultTypeDef",
    "GetPlayerConnectionStatusRequestRequestTypeDef",
    "GetPlayerConnectionStatusResultTypeDef",
    "GetSnapshotRequestRequestTypeDef",
    "GetSnapshotResultTypeDef",
    "GetStageDeploymentRequestRequestTypeDef",
    "GetStageDeploymentResultTypeDef",
    "GetStageRequestRequestTypeDef",
    "GetStageResultTypeDef",
    "ImportGameConfigurationRequestRequestTypeDef",
    "ImportGameConfigurationResultTypeDef",
    "ImportGameConfigurationSourceTypeDef",
    "ListExtensionVersionsRequestRequestTypeDef",
    "ListExtensionVersionsResultTypeDef",
    "ListExtensionsRequestRequestTypeDef",
    "ListExtensionsResultTypeDef",
    "ListGamesRequestRequestTypeDef",
    "ListGamesResultTypeDef",
    "ListGeneratedCodeJobsRequestRequestTypeDef",
    "ListGeneratedCodeJobsResultTypeDef",
    "ListSnapshotsRequestRequestTypeDef",
    "ListSnapshotsResultTypeDef",
    "ListStageDeploymentsRequestRequestTypeDef",
    "ListStageDeploymentsResultTypeDef",
    "ListStagesRequestRequestTypeDef",
    "ListStagesResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SectionModificationTypeDef",
    "SectionTypeDef",
    "SnapshotDetailsTypeDef",
    "SnapshotSummaryTypeDef",
    "StageDeploymentDetailsTypeDef",
    "StageDeploymentSummaryTypeDef",
    "StageDetailsTypeDef",
    "StageSummaryTypeDef",
    "StartGeneratedCodeJobRequestRequestTypeDef",
    "StartGeneratedCodeJobResultTypeDef",
    "StartStageDeploymentRequestRequestTypeDef",
    "StartStageDeploymentResultTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateGameConfigurationRequestRequestTypeDef",
    "UpdateGameConfigurationResultTypeDef",
    "UpdateGameRequestRequestTypeDef",
    "UpdateGameResultTypeDef",
    "UpdateSnapshotRequestRequestTypeDef",
    "UpdateSnapshotResultTypeDef",
    "UpdateStageRequestRequestTypeDef",
    "UpdateStageResultTypeDef",
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "Created": datetime,
        "Id": str,
    },
    total=False,
)

_RequiredCreateGameRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGameRequestRequestTypeDef",
    {
        "GameName": str,
    },
)
_OptionalCreateGameRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGameRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateGameRequestRequestTypeDef(
    _RequiredCreateGameRequestRequestTypeDef, _OptionalCreateGameRequestRequestTypeDef
):
    pass

CreateGameResultTypeDef = TypedDict(
    "CreateGameResultTypeDef",
    {
        "Game": "GameDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSnapshotRequestRequestTypeDef",
    {
        "GameName": str,
    },
)
_OptionalCreateSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSnapshotRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class CreateSnapshotRequestRequestTypeDef(
    _RequiredCreateSnapshotRequestRequestTypeDef, _OptionalCreateSnapshotRequestRequestTypeDef
):
    pass

CreateSnapshotResultTypeDef = TypedDict(
    "CreateSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStageRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStageRequestRequestTypeDef",
    {
        "GameName": str,
        "Role": str,
        "StageName": str,
    },
)
_OptionalCreateStageRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStageRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateStageRequestRequestTypeDef(
    _RequiredCreateStageRequestRequestTypeDef, _OptionalCreateStageRequestRequestTypeDef
):
    pass

CreateStageResultTypeDef = TypedDict(
    "CreateStageResultTypeDef",
    {
        "Stage": "StageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGameRequestRequestTypeDef = TypedDict(
    "DeleteGameRequestRequestTypeDef",
    {
        "GameName": str,
    },
)

DeleteStageRequestRequestTypeDef = TypedDict(
    "DeleteStageRequestRequestTypeDef",
    {
        "GameName": str,
        "StageName": str,
    },
)

DeploymentResultTypeDef = TypedDict(
    "DeploymentResultTypeDef",
    {
        "Message": str,
        "ResultCode": ResultCodeType,
    },
    total=False,
)

DisconnectPlayerRequestRequestTypeDef = TypedDict(
    "DisconnectPlayerRequestRequestTypeDef",
    {
        "GameName": str,
        "PlayerId": str,
        "StageName": str,
    },
)

DisconnectPlayerResultTypeDef = TypedDict(
    "DisconnectPlayerResultTypeDef",
    {
        "DisconnectFailures": List[str],
        "DisconnectSuccesses": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportSnapshotRequestRequestTypeDef = TypedDict(
    "ExportSnapshotRequestRequestTypeDef",
    {
        "GameName": str,
        "SnapshotId": str,
    },
)

ExportSnapshotResultTypeDef = TypedDict(
    "ExportSnapshotResultTypeDef",
    {
        "S3Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExtensionDetailsTypeDef = TypedDict(
    "ExtensionDetailsTypeDef",
    {
        "Description": str,
        "Name": str,
        "Namespace": str,
    },
    total=False,
)

ExtensionVersionDetailsTypeDef = TypedDict(
    "ExtensionVersionDetailsTypeDef",
    {
        "Name": str,
        "Namespace": str,
        "Schema": str,
        "Version": str,
    },
    total=False,
)

GameConfigurationDetailsTypeDef = TypedDict(
    "GameConfigurationDetailsTypeDef",
    {
        "Created": datetime,
        "LastUpdated": datetime,
        "Sections": Dict[str, "SectionTypeDef"],
    },
    total=False,
)

GameDetailsTypeDef = TypedDict(
    "GameDetailsTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Description": str,
        "EnableTerminationProtection": bool,
        "LastUpdated": datetime,
        "Name": str,
        "State": GameStateType,
        "Tags": Dict[str, str],
    },
    total=False,
)

GameSummaryTypeDef = TypedDict(
    "GameSummaryTypeDef",
    {
        "Description": str,
        "Name": str,
        "State": GameStateType,
        "Tags": Dict[str, str],
    },
    total=False,
)

GeneratedCodeJobDetailsTypeDef = TypedDict(
    "GeneratedCodeJobDetailsTypeDef",
    {
        "Description": str,
        "ExpirationTime": datetime,
        "GeneratedCodeJobId": str,
        "S3Url": str,
        "Status": GeneratedCodeJobStateType,
    },
    total=False,
)

GeneratorTypeDef = TypedDict(
    "GeneratorTypeDef",
    {
        "GameSdkVersion": str,
        "Language": str,
        "TargetPlatform": str,
    },
    total=False,
)

GetExtensionRequestRequestTypeDef = TypedDict(
    "GetExtensionRequestRequestTypeDef",
    {
        "Name": str,
        "Namespace": str,
    },
)

GetExtensionResultTypeDef = TypedDict(
    "GetExtensionResultTypeDef",
    {
        "Extension": "ExtensionDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExtensionVersionRequestRequestTypeDef = TypedDict(
    "GetExtensionVersionRequestRequestTypeDef",
    {
        "ExtensionVersion": str,
        "Name": str,
        "Namespace": str,
    },
)

GetExtensionVersionResultTypeDef = TypedDict(
    "GetExtensionVersionResultTypeDef",
    {
        "ExtensionVersion": "ExtensionVersionDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetGameConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredGetGameConfigurationRequestRequestTypeDef",
    {
        "GameName": str,
    },
)
_OptionalGetGameConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalGetGameConfigurationRequestRequestTypeDef",
    {
        "Sections": List[str],
    },
    total=False,
)

class GetGameConfigurationRequestRequestTypeDef(
    _RequiredGetGameConfigurationRequestRequestTypeDef,
    _OptionalGetGameConfigurationRequestRequestTypeDef,
):
    pass

GetGameConfigurationResultTypeDef = TypedDict(
    "GetGameConfigurationResultTypeDef",
    {
        "GameConfiguration": "GameConfigurationDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGameRequestRequestTypeDef = TypedDict(
    "GetGameRequestRequestTypeDef",
    {
        "GameName": str,
    },
)

GetGameResultTypeDef = TypedDict(
    "GetGameResultTypeDef",
    {
        "Game": "GameDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGeneratedCodeJobRequestRequestTypeDef = TypedDict(
    "GetGeneratedCodeJobRequestRequestTypeDef",
    {
        "GameName": str,
        "JobId": str,
        "SnapshotId": str,
    },
)

GetGeneratedCodeJobResultTypeDef = TypedDict(
    "GetGeneratedCodeJobResultTypeDef",
    {
        "GeneratedCodeJob": "GeneratedCodeJobDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPlayerConnectionStatusRequestRequestTypeDef = TypedDict(
    "GetPlayerConnectionStatusRequestRequestTypeDef",
    {
        "GameName": str,
        "PlayerId": str,
        "StageName": str,
    },
)

GetPlayerConnectionStatusResultTypeDef = TypedDict(
    "GetPlayerConnectionStatusResultTypeDef",
    {
        "Connections": List["ConnectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredGetSnapshotRequestRequestTypeDef",
    {
        "GameName": str,
        "SnapshotId": str,
    },
)
_OptionalGetSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalGetSnapshotRequestRequestTypeDef",
    {
        "Sections": List[str],
    },
    total=False,
)

class GetSnapshotRequestRequestTypeDef(
    _RequiredGetSnapshotRequestRequestTypeDef, _OptionalGetSnapshotRequestRequestTypeDef
):
    pass

GetSnapshotResultTypeDef = TypedDict(
    "GetSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetStageDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredGetStageDeploymentRequestRequestTypeDef",
    {
        "GameName": str,
        "StageName": str,
    },
)
_OptionalGetStageDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalGetStageDeploymentRequestRequestTypeDef",
    {
        "DeploymentId": str,
    },
    total=False,
)

class GetStageDeploymentRequestRequestTypeDef(
    _RequiredGetStageDeploymentRequestRequestTypeDef,
    _OptionalGetStageDeploymentRequestRequestTypeDef,
):
    pass

GetStageDeploymentResultTypeDef = TypedDict(
    "GetStageDeploymentResultTypeDef",
    {
        "StageDeployment": "StageDeploymentDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStageRequestRequestTypeDef = TypedDict(
    "GetStageRequestRequestTypeDef",
    {
        "GameName": str,
        "StageName": str,
    },
)

GetStageResultTypeDef = TypedDict(
    "GetStageResultTypeDef",
    {
        "Stage": "StageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportGameConfigurationRequestRequestTypeDef = TypedDict(
    "ImportGameConfigurationRequestRequestTypeDef",
    {
        "GameName": str,
        "ImportSource": "ImportGameConfigurationSourceTypeDef",
    },
)

ImportGameConfigurationResultTypeDef = TypedDict(
    "ImportGameConfigurationResultTypeDef",
    {
        "GameConfiguration": "GameConfigurationDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportGameConfigurationSourceTypeDef = TypedDict(
    "ImportGameConfigurationSourceTypeDef",
    {
        "File": Union[bytes, IO[bytes], StreamingBody],
    },
)

_RequiredListExtensionVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListExtensionVersionsRequestRequestTypeDef",
    {
        "Name": str,
        "Namespace": str,
    },
)
_OptionalListExtensionVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListExtensionVersionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListExtensionVersionsRequestRequestTypeDef(
    _RequiredListExtensionVersionsRequestRequestTypeDef,
    _OptionalListExtensionVersionsRequestRequestTypeDef,
):
    pass

ListExtensionVersionsResultTypeDef = TypedDict(
    "ListExtensionVersionsResultTypeDef",
    {
        "ExtensionVersions": List["ExtensionVersionDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExtensionsRequestRequestTypeDef = TypedDict(
    "ListExtensionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListExtensionsResultTypeDef = TypedDict(
    "ListExtensionsResultTypeDef",
    {
        "Extensions": List["ExtensionDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGamesRequestRequestTypeDef = TypedDict(
    "ListGamesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListGamesResultTypeDef = TypedDict(
    "ListGamesResultTypeDef",
    {
        "Games": List["GameSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGeneratedCodeJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListGeneratedCodeJobsRequestRequestTypeDef",
    {
        "GameName": str,
        "SnapshotId": str,
    },
)
_OptionalListGeneratedCodeJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListGeneratedCodeJobsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListGeneratedCodeJobsRequestRequestTypeDef(
    _RequiredListGeneratedCodeJobsRequestRequestTypeDef,
    _OptionalListGeneratedCodeJobsRequestRequestTypeDef,
):
    pass

ListGeneratedCodeJobsResultTypeDef = TypedDict(
    "ListGeneratedCodeJobsResultTypeDef",
    {
        "GeneratedCodeJobs": List["GeneratedCodeJobDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSnapshotsRequestRequestTypeDef = TypedDict(
    "_RequiredListSnapshotsRequestRequestTypeDef",
    {
        "GameName": str,
    },
)
_OptionalListSnapshotsRequestRequestTypeDef = TypedDict(
    "_OptionalListSnapshotsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListSnapshotsRequestRequestTypeDef(
    _RequiredListSnapshotsRequestRequestTypeDef, _OptionalListSnapshotsRequestRequestTypeDef
):
    pass

ListSnapshotsResultTypeDef = TypedDict(
    "ListSnapshotsResultTypeDef",
    {
        "NextToken": str,
        "Snapshots": List["SnapshotSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStageDeploymentsRequestRequestTypeDef = TypedDict(
    "_RequiredListStageDeploymentsRequestRequestTypeDef",
    {
        "GameName": str,
        "StageName": str,
    },
)
_OptionalListStageDeploymentsRequestRequestTypeDef = TypedDict(
    "_OptionalListStageDeploymentsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListStageDeploymentsRequestRequestTypeDef(
    _RequiredListStageDeploymentsRequestRequestTypeDef,
    _OptionalListStageDeploymentsRequestRequestTypeDef,
):
    pass

ListStageDeploymentsResultTypeDef = TypedDict(
    "ListStageDeploymentsResultTypeDef",
    {
        "NextToken": str,
        "StageDeployments": List["StageDeploymentSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStagesRequestRequestTypeDef = TypedDict(
    "_RequiredListStagesRequestRequestTypeDef",
    {
        "GameName": str,
    },
)
_OptionalListStagesRequestRequestTypeDef = TypedDict(
    "_OptionalListStagesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListStagesRequestRequestTypeDef(
    _RequiredListStagesRequestRequestTypeDef, _OptionalListStagesRequestRequestTypeDef
):
    pass

ListStagesResultTypeDef = TypedDict(
    "ListStagesResultTypeDef",
    {
        "NextToken": str,
        "Stages": List["StageSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
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

_RequiredSectionModificationTypeDef = TypedDict(
    "_RequiredSectionModificationTypeDef",
    {
        "Operation": OperationType,
        "Path": str,
        "Section": str,
    },
)
_OptionalSectionModificationTypeDef = TypedDict(
    "_OptionalSectionModificationTypeDef",
    {
        "Value": Dict[str, Any],
    },
    total=False,
)

class SectionModificationTypeDef(
    _RequiredSectionModificationTypeDef, _OptionalSectionModificationTypeDef
):
    pass

SectionTypeDef = TypedDict(
    "SectionTypeDef",
    {
        "Attributes": Dict[str, Any],
        "Name": str,
        "Size": int,
    },
    total=False,
)

SnapshotDetailsTypeDef = TypedDict(
    "SnapshotDetailsTypeDef",
    {
        "Created": datetime,
        "Description": str,
        "Id": str,
        "LastUpdated": datetime,
        "Sections": Dict[str, "SectionTypeDef"],
    },
    total=False,
)

SnapshotSummaryTypeDef = TypedDict(
    "SnapshotSummaryTypeDef",
    {
        "Created": datetime,
        "Description": str,
        "Id": str,
        "LastUpdated": datetime,
    },
    total=False,
)

StageDeploymentDetailsTypeDef = TypedDict(
    "StageDeploymentDetailsTypeDef",
    {
        "Created": datetime,
        "DeploymentAction": DeploymentActionType,
        "DeploymentId": str,
        "DeploymentResult": "DeploymentResultTypeDef",
        "DeploymentState": DeploymentStateType,
        "LastUpdated": datetime,
        "SnapshotId": str,
    },
    total=False,
)

StageDeploymentSummaryTypeDef = TypedDict(
    "StageDeploymentSummaryTypeDef",
    {
        "DeploymentAction": DeploymentActionType,
        "DeploymentId": str,
        "DeploymentResult": "DeploymentResultTypeDef",
        "DeploymentState": DeploymentStateType,
        "LastUpdated": datetime,
        "SnapshotId": str,
    },
    total=False,
)

StageDetailsTypeDef = TypedDict(
    "StageDetailsTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Description": str,
        "GameKey": str,
        "LastUpdated": datetime,
        "LogGroup": str,
        "Name": str,
        "Role": str,
        "State": StageStateType,
        "Tags": Dict[str, str],
    },
    total=False,
)

StageSummaryTypeDef = TypedDict(
    "StageSummaryTypeDef",
    {
        "Description": str,
        "GameKey": str,
        "Name": str,
        "State": StageStateType,
        "Tags": Dict[str, str],
    },
    total=False,
)

StartGeneratedCodeJobRequestRequestTypeDef = TypedDict(
    "StartGeneratedCodeJobRequestRequestTypeDef",
    {
        "GameName": str,
        "Generator": "GeneratorTypeDef",
        "SnapshotId": str,
    },
)

StartGeneratedCodeJobResultTypeDef = TypedDict(
    "StartGeneratedCodeJobResultTypeDef",
    {
        "GeneratedCodeJobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartStageDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredStartStageDeploymentRequestRequestTypeDef",
    {
        "GameName": str,
        "SnapshotId": str,
        "StageName": str,
    },
)
_OptionalStartStageDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalStartStageDeploymentRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class StartStageDeploymentRequestRequestTypeDef(
    _RequiredStartStageDeploymentRequestRequestTypeDef,
    _OptionalStartStageDeploymentRequestRequestTypeDef,
):
    pass

StartStageDeploymentResultTypeDef = TypedDict(
    "StartStageDeploymentResultTypeDef",
    {
        "StageDeployment": "StageDeploymentDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateGameConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateGameConfigurationRequestRequestTypeDef",
    {
        "GameName": str,
        "Modifications": List["SectionModificationTypeDef"],
    },
)

UpdateGameConfigurationResultTypeDef = TypedDict(
    "UpdateGameConfigurationResultTypeDef",
    {
        "GameConfiguration": "GameConfigurationDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGameRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGameRequestRequestTypeDef",
    {
        "GameName": str,
    },
)
_OptionalUpdateGameRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGameRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateGameRequestRequestTypeDef(
    _RequiredUpdateGameRequestRequestTypeDef, _OptionalUpdateGameRequestRequestTypeDef
):
    pass

UpdateGameResultTypeDef = TypedDict(
    "UpdateGameResultTypeDef",
    {
        "Game": "GameDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSnapshotRequestRequestTypeDef",
    {
        "GameName": str,
        "SnapshotId": str,
    },
)
_OptionalUpdateSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSnapshotRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateSnapshotRequestRequestTypeDef(
    _RequiredUpdateSnapshotRequestRequestTypeDef, _OptionalUpdateSnapshotRequestRequestTypeDef
):
    pass

UpdateSnapshotResultTypeDef = TypedDict(
    "UpdateSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateStageRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStageRequestRequestTypeDef",
    {
        "GameName": str,
        "StageName": str,
    },
)
_OptionalUpdateStageRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStageRequestRequestTypeDef",
    {
        "Description": str,
        "Role": str,
    },
    total=False,
)

class UpdateStageRequestRequestTypeDef(
    _RequiredUpdateStageRequestRequestTypeDef, _OptionalUpdateStageRequestRequestTypeDef
):
    pass

UpdateStageResultTypeDef = TypedDict(
    "UpdateStageResultTypeDef",
    {
        "Stage": "StageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
