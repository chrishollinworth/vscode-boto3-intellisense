"""
Type annotations for fis service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/type_defs.html)

Usage::

    ```python
    from mypy_boto3_fis.type_defs import ActionParameterTypeDef

    data: ActionParameterTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ExperimentActionStatusType, ExperimentStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ActionParameterTypeDef",
    "ActionSummaryTypeDef",
    "ActionTargetTypeDef",
    "ActionTypeDef",
    "CreateExperimentTemplateActionInputTypeDef",
    "CreateExperimentTemplateLogConfigurationInputTypeDef",
    "CreateExperimentTemplateRequestRequestTypeDef",
    "CreateExperimentTemplateResponseTypeDef",
    "CreateExperimentTemplateStopConditionInputTypeDef",
    "CreateExperimentTemplateTargetInputTypeDef",
    "DeleteExperimentTemplateRequestRequestTypeDef",
    "DeleteExperimentTemplateResponseTypeDef",
    "ExperimentActionStateTypeDef",
    "ExperimentActionTypeDef",
    "ExperimentCloudWatchLogsLogConfigurationTypeDef",
    "ExperimentLogConfigurationTypeDef",
    "ExperimentS3LogConfigurationTypeDef",
    "ExperimentStateTypeDef",
    "ExperimentStopConditionTypeDef",
    "ExperimentSummaryTypeDef",
    "ExperimentTargetFilterTypeDef",
    "ExperimentTargetTypeDef",
    "ExperimentTemplateActionTypeDef",
    "ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef",
    "ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef",
    "ExperimentTemplateLogConfigurationTypeDef",
    "ExperimentTemplateS3LogConfigurationInputTypeDef",
    "ExperimentTemplateS3LogConfigurationTypeDef",
    "ExperimentTemplateStopConditionTypeDef",
    "ExperimentTemplateSummaryTypeDef",
    "ExperimentTemplateTargetFilterTypeDef",
    "ExperimentTemplateTargetInputFilterTypeDef",
    "ExperimentTemplateTargetTypeDef",
    "ExperimentTemplateTypeDef",
    "ExperimentTypeDef",
    "GetActionRequestRequestTypeDef",
    "GetActionResponseTypeDef",
    "GetExperimentRequestRequestTypeDef",
    "GetExperimentResponseTypeDef",
    "GetExperimentTemplateRequestRequestTypeDef",
    "GetExperimentTemplateResponseTypeDef",
    "GetTargetResourceTypeRequestRequestTypeDef",
    "GetTargetResourceTypeResponseTypeDef",
    "ListActionsRequestRequestTypeDef",
    "ListActionsResponseTypeDef",
    "ListExperimentTemplatesRequestRequestTypeDef",
    "ListExperimentTemplatesResponseTypeDef",
    "ListExperimentsRequestRequestTypeDef",
    "ListExperimentsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetResourceTypesRequestRequestTypeDef",
    "ListTargetResourceTypesResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartExperimentRequestRequestTypeDef",
    "StartExperimentResponseTypeDef",
    "StopExperimentRequestRequestTypeDef",
    "StopExperimentResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TargetResourceTypeParameterTypeDef",
    "TargetResourceTypeSummaryTypeDef",
    "TargetResourceTypeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateExperimentTemplateActionInputItemTypeDef",
    "UpdateExperimentTemplateLogConfigurationInputTypeDef",
    "UpdateExperimentTemplateRequestRequestTypeDef",
    "UpdateExperimentTemplateResponseTypeDef",
    "UpdateExperimentTemplateStopConditionInputTypeDef",
    "UpdateExperimentTemplateTargetInputTypeDef",
)

ActionParameterTypeDef = TypedDict(
    "ActionParameterTypeDef",
    {
        "description": str,
        "required": bool,
    },
    total=False,
)

ActionSummaryTypeDef = TypedDict(
    "ActionSummaryTypeDef",
    {
        "id": str,
        "description": str,
        "targets": Dict[str, "ActionTargetTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

ActionTargetTypeDef = TypedDict(
    "ActionTargetTypeDef",
    {
        "resourceType": str,
    },
    total=False,
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "id": str,
        "description": str,
        "parameters": Dict[str, "ActionParameterTypeDef"],
        "targets": Dict[str, "ActionTargetTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredCreateExperimentTemplateActionInputTypeDef = TypedDict(
    "_RequiredCreateExperimentTemplateActionInputTypeDef",
    {
        "actionId": str,
    },
)
_OptionalCreateExperimentTemplateActionInputTypeDef = TypedDict(
    "_OptionalCreateExperimentTemplateActionInputTypeDef",
    {
        "description": str,
        "parameters": Dict[str, str],
        "targets": Dict[str, str],
        "startAfter": List[str],
    },
    total=False,
)

class CreateExperimentTemplateActionInputTypeDef(
    _RequiredCreateExperimentTemplateActionInputTypeDef,
    _OptionalCreateExperimentTemplateActionInputTypeDef,
):
    pass

_RequiredCreateExperimentTemplateLogConfigurationInputTypeDef = TypedDict(
    "_RequiredCreateExperimentTemplateLogConfigurationInputTypeDef",
    {
        "logSchemaVersion": int,
    },
)
_OptionalCreateExperimentTemplateLogConfigurationInputTypeDef = TypedDict(
    "_OptionalCreateExperimentTemplateLogConfigurationInputTypeDef",
    {
        "cloudWatchLogsConfiguration": "ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef",
        "s3Configuration": "ExperimentTemplateS3LogConfigurationInputTypeDef",
    },
    total=False,
)

class CreateExperimentTemplateLogConfigurationInputTypeDef(
    _RequiredCreateExperimentTemplateLogConfigurationInputTypeDef,
    _OptionalCreateExperimentTemplateLogConfigurationInputTypeDef,
):
    pass

_RequiredCreateExperimentTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateExperimentTemplateRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "stopConditions": List["CreateExperimentTemplateStopConditionInputTypeDef"],
        "actions": Dict[str, "CreateExperimentTemplateActionInputTypeDef"],
        "roleArn": str,
    },
)
_OptionalCreateExperimentTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateExperimentTemplateRequestRequestTypeDef",
    {
        "targets": Dict[str, "CreateExperimentTemplateTargetInputTypeDef"],
        "tags": Dict[str, str],
        "logConfiguration": "CreateExperimentTemplateLogConfigurationInputTypeDef",
    },
    total=False,
)

class CreateExperimentTemplateRequestRequestTypeDef(
    _RequiredCreateExperimentTemplateRequestRequestTypeDef,
    _OptionalCreateExperimentTemplateRequestRequestTypeDef,
):
    pass

CreateExperimentTemplateResponseTypeDef = TypedDict(
    "CreateExperimentTemplateResponseTypeDef",
    {
        "experimentTemplate": "ExperimentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateExperimentTemplateStopConditionInputTypeDef = TypedDict(
    "_RequiredCreateExperimentTemplateStopConditionInputTypeDef",
    {
        "source": str,
    },
)
_OptionalCreateExperimentTemplateStopConditionInputTypeDef = TypedDict(
    "_OptionalCreateExperimentTemplateStopConditionInputTypeDef",
    {
        "value": str,
    },
    total=False,
)

class CreateExperimentTemplateStopConditionInputTypeDef(
    _RequiredCreateExperimentTemplateStopConditionInputTypeDef,
    _OptionalCreateExperimentTemplateStopConditionInputTypeDef,
):
    pass

_RequiredCreateExperimentTemplateTargetInputTypeDef = TypedDict(
    "_RequiredCreateExperimentTemplateTargetInputTypeDef",
    {
        "resourceType": str,
        "selectionMode": str,
    },
)
_OptionalCreateExperimentTemplateTargetInputTypeDef = TypedDict(
    "_OptionalCreateExperimentTemplateTargetInputTypeDef",
    {
        "resourceArns": List[str],
        "resourceTags": Dict[str, str],
        "filters": List["ExperimentTemplateTargetInputFilterTypeDef"],
        "parameters": Dict[str, str],
    },
    total=False,
)

class CreateExperimentTemplateTargetInputTypeDef(
    _RequiredCreateExperimentTemplateTargetInputTypeDef,
    _OptionalCreateExperimentTemplateTargetInputTypeDef,
):
    pass

DeleteExperimentTemplateRequestRequestTypeDef = TypedDict(
    "DeleteExperimentTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteExperimentTemplateResponseTypeDef = TypedDict(
    "DeleteExperimentTemplateResponseTypeDef",
    {
        "experimentTemplate": "ExperimentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExperimentActionStateTypeDef = TypedDict(
    "ExperimentActionStateTypeDef",
    {
        "status": ExperimentActionStatusType,
        "reason": str,
    },
    total=False,
)

ExperimentActionTypeDef = TypedDict(
    "ExperimentActionTypeDef",
    {
        "actionId": str,
        "description": str,
        "parameters": Dict[str, str],
        "targets": Dict[str, str],
        "startAfter": List[str],
        "state": "ExperimentActionStateTypeDef",
        "startTime": datetime,
        "endTime": datetime,
    },
    total=False,
)

ExperimentCloudWatchLogsLogConfigurationTypeDef = TypedDict(
    "ExperimentCloudWatchLogsLogConfigurationTypeDef",
    {
        "logGroupArn": str,
    },
    total=False,
)

ExperimentLogConfigurationTypeDef = TypedDict(
    "ExperimentLogConfigurationTypeDef",
    {
        "cloudWatchLogsConfiguration": "ExperimentCloudWatchLogsLogConfigurationTypeDef",
        "s3Configuration": "ExperimentS3LogConfigurationTypeDef",
        "logSchemaVersion": int,
    },
    total=False,
)

ExperimentS3LogConfigurationTypeDef = TypedDict(
    "ExperimentS3LogConfigurationTypeDef",
    {
        "bucketName": str,
        "prefix": str,
    },
    total=False,
)

ExperimentStateTypeDef = TypedDict(
    "ExperimentStateTypeDef",
    {
        "status": ExperimentStatusType,
        "reason": str,
    },
    total=False,
)

ExperimentStopConditionTypeDef = TypedDict(
    "ExperimentStopConditionTypeDef",
    {
        "source": str,
        "value": str,
    },
    total=False,
)

ExperimentSummaryTypeDef = TypedDict(
    "ExperimentSummaryTypeDef",
    {
        "id": str,
        "experimentTemplateId": str,
        "state": "ExperimentStateTypeDef",
        "creationTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ExperimentTargetFilterTypeDef = TypedDict(
    "ExperimentTargetFilterTypeDef",
    {
        "path": str,
        "values": List[str],
    },
    total=False,
)

ExperimentTargetTypeDef = TypedDict(
    "ExperimentTargetTypeDef",
    {
        "resourceType": str,
        "resourceArns": List[str],
        "resourceTags": Dict[str, str],
        "filters": List["ExperimentTargetFilterTypeDef"],
        "selectionMode": str,
        "parameters": Dict[str, str],
    },
    total=False,
)

ExperimentTemplateActionTypeDef = TypedDict(
    "ExperimentTemplateActionTypeDef",
    {
        "actionId": str,
        "description": str,
        "parameters": Dict[str, str],
        "targets": Dict[str, str],
        "startAfter": List[str],
    },
    total=False,
)

ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef = TypedDict(
    "ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef",
    {
        "logGroupArn": str,
    },
)

ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef = TypedDict(
    "ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef",
    {
        "logGroupArn": str,
    },
    total=False,
)

ExperimentTemplateLogConfigurationTypeDef = TypedDict(
    "ExperimentTemplateLogConfigurationTypeDef",
    {
        "cloudWatchLogsConfiguration": "ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef",
        "s3Configuration": "ExperimentTemplateS3LogConfigurationTypeDef",
        "logSchemaVersion": int,
    },
    total=False,
)

_RequiredExperimentTemplateS3LogConfigurationInputTypeDef = TypedDict(
    "_RequiredExperimentTemplateS3LogConfigurationInputTypeDef",
    {
        "bucketName": str,
    },
)
_OptionalExperimentTemplateS3LogConfigurationInputTypeDef = TypedDict(
    "_OptionalExperimentTemplateS3LogConfigurationInputTypeDef",
    {
        "prefix": str,
    },
    total=False,
)

class ExperimentTemplateS3LogConfigurationInputTypeDef(
    _RequiredExperimentTemplateS3LogConfigurationInputTypeDef,
    _OptionalExperimentTemplateS3LogConfigurationInputTypeDef,
):
    pass

ExperimentTemplateS3LogConfigurationTypeDef = TypedDict(
    "ExperimentTemplateS3LogConfigurationTypeDef",
    {
        "bucketName": str,
        "prefix": str,
    },
    total=False,
)

ExperimentTemplateStopConditionTypeDef = TypedDict(
    "ExperimentTemplateStopConditionTypeDef",
    {
        "source": str,
        "value": str,
    },
    total=False,
)

ExperimentTemplateSummaryTypeDef = TypedDict(
    "ExperimentTemplateSummaryTypeDef",
    {
        "id": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ExperimentTemplateTargetFilterTypeDef = TypedDict(
    "ExperimentTemplateTargetFilterTypeDef",
    {
        "path": str,
        "values": List[str],
    },
    total=False,
)

ExperimentTemplateTargetInputFilterTypeDef = TypedDict(
    "ExperimentTemplateTargetInputFilterTypeDef",
    {
        "path": str,
        "values": List[str],
    },
)

ExperimentTemplateTargetTypeDef = TypedDict(
    "ExperimentTemplateTargetTypeDef",
    {
        "resourceType": str,
        "resourceArns": List[str],
        "resourceTags": Dict[str, str],
        "filters": List["ExperimentTemplateTargetFilterTypeDef"],
        "selectionMode": str,
        "parameters": Dict[str, str],
    },
    total=False,
)

ExperimentTemplateTypeDef = TypedDict(
    "ExperimentTemplateTypeDef",
    {
        "id": str,
        "description": str,
        "targets": Dict[str, "ExperimentTemplateTargetTypeDef"],
        "actions": Dict[str, "ExperimentTemplateActionTypeDef"],
        "stopConditions": List["ExperimentTemplateStopConditionTypeDef"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "roleArn": str,
        "tags": Dict[str, str],
        "logConfiguration": "ExperimentTemplateLogConfigurationTypeDef",
    },
    total=False,
)

ExperimentTypeDef = TypedDict(
    "ExperimentTypeDef",
    {
        "id": str,
        "experimentTemplateId": str,
        "roleArn": str,
        "state": "ExperimentStateTypeDef",
        "targets": Dict[str, "ExperimentTargetTypeDef"],
        "actions": Dict[str, "ExperimentActionTypeDef"],
        "stopConditions": List["ExperimentStopConditionTypeDef"],
        "creationTime": datetime,
        "startTime": datetime,
        "endTime": datetime,
        "tags": Dict[str, str],
        "logConfiguration": "ExperimentLogConfigurationTypeDef",
    },
    total=False,
)

GetActionRequestRequestTypeDef = TypedDict(
    "GetActionRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetActionResponseTypeDef = TypedDict(
    "GetActionResponseTypeDef",
    {
        "action": "ActionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExperimentRequestRequestTypeDef = TypedDict(
    "GetExperimentRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetExperimentResponseTypeDef = TypedDict(
    "GetExperimentResponseTypeDef",
    {
        "experiment": "ExperimentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExperimentTemplateRequestRequestTypeDef = TypedDict(
    "GetExperimentTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetExperimentTemplateResponseTypeDef = TypedDict(
    "GetExperimentTemplateResponseTypeDef",
    {
        "experimentTemplate": "ExperimentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTargetResourceTypeRequestRequestTypeDef = TypedDict(
    "GetTargetResourceTypeRequestRequestTypeDef",
    {
        "resourceType": str,
    },
)

GetTargetResourceTypeResponseTypeDef = TypedDict(
    "GetTargetResourceTypeResponseTypeDef",
    {
        "targetResourceType": "TargetResourceTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListActionsRequestRequestTypeDef = TypedDict(
    "ListActionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListActionsResponseTypeDef = TypedDict(
    "ListActionsResponseTypeDef",
    {
        "actions": List["ActionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExperimentTemplatesRequestRequestTypeDef = TypedDict(
    "ListExperimentTemplatesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListExperimentTemplatesResponseTypeDef = TypedDict(
    "ListExperimentTemplatesResponseTypeDef",
    {
        "experimentTemplates": List["ExperimentTemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExperimentsRequestRequestTypeDef = TypedDict(
    "ListExperimentsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListExperimentsResponseTypeDef = TypedDict(
    "ListExperimentsResponseTypeDef",
    {
        "experiments": List["ExperimentSummaryTypeDef"],
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

ListTargetResourceTypesRequestRequestTypeDef = TypedDict(
    "ListTargetResourceTypesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTargetResourceTypesResponseTypeDef = TypedDict(
    "ListTargetResourceTypesResponseTypeDef",
    {
        "targetResourceTypes": List["TargetResourceTypeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredStartExperimentRequestRequestTypeDef = TypedDict(
    "_RequiredStartExperimentRequestRequestTypeDef",
    {
        "clientToken": str,
        "experimentTemplateId": str,
    },
)
_OptionalStartExperimentRequestRequestTypeDef = TypedDict(
    "_OptionalStartExperimentRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class StartExperimentRequestRequestTypeDef(
    _RequiredStartExperimentRequestRequestTypeDef, _OptionalStartExperimentRequestRequestTypeDef
):
    pass

StartExperimentResponseTypeDef = TypedDict(
    "StartExperimentResponseTypeDef",
    {
        "experiment": "ExperimentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopExperimentRequestRequestTypeDef = TypedDict(
    "StopExperimentRequestRequestTypeDef",
    {
        "id": str,
    },
)

StopExperimentResponseTypeDef = TypedDict(
    "StopExperimentResponseTypeDef",
    {
        "experiment": "ExperimentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TargetResourceTypeParameterTypeDef = TypedDict(
    "TargetResourceTypeParameterTypeDef",
    {
        "description": str,
        "required": bool,
    },
    total=False,
)

TargetResourceTypeSummaryTypeDef = TypedDict(
    "TargetResourceTypeSummaryTypeDef",
    {
        "resourceType": str,
        "description": str,
    },
    total=False,
)

TargetResourceTypeTypeDef = TypedDict(
    "TargetResourceTypeTypeDef",
    {
        "resourceType": str,
        "description": str,
        "parameters": Dict[str, "TargetResourceTypeParameterTypeDef"],
    },
    total=False,
)

_RequiredUntagResourceRequestRequestTypeDef = TypedDict(
    "_RequiredUntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalUntagResourceRequestRequestTypeDef = TypedDict(
    "_OptionalUntagResourceRequestRequestTypeDef",
    {
        "tagKeys": List[str],
    },
    total=False,
)

class UntagResourceRequestRequestTypeDef(
    _RequiredUntagResourceRequestRequestTypeDef, _OptionalUntagResourceRequestRequestTypeDef
):
    pass

UpdateExperimentTemplateActionInputItemTypeDef = TypedDict(
    "UpdateExperimentTemplateActionInputItemTypeDef",
    {
        "actionId": str,
        "description": str,
        "parameters": Dict[str, str],
        "targets": Dict[str, str],
        "startAfter": List[str],
    },
    total=False,
)

UpdateExperimentTemplateLogConfigurationInputTypeDef = TypedDict(
    "UpdateExperimentTemplateLogConfigurationInputTypeDef",
    {
        "cloudWatchLogsConfiguration": "ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef",
        "s3Configuration": "ExperimentTemplateS3LogConfigurationInputTypeDef",
        "logSchemaVersion": int,
    },
    total=False,
)

_RequiredUpdateExperimentTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateExperimentTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateExperimentTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateExperimentTemplateRequestRequestTypeDef",
    {
        "description": str,
        "stopConditions": List["UpdateExperimentTemplateStopConditionInputTypeDef"],
        "targets": Dict[str, "UpdateExperimentTemplateTargetInputTypeDef"],
        "actions": Dict[str, "UpdateExperimentTemplateActionInputItemTypeDef"],
        "roleArn": str,
        "logConfiguration": "UpdateExperimentTemplateLogConfigurationInputTypeDef",
    },
    total=False,
)

class UpdateExperimentTemplateRequestRequestTypeDef(
    _RequiredUpdateExperimentTemplateRequestRequestTypeDef,
    _OptionalUpdateExperimentTemplateRequestRequestTypeDef,
):
    pass

UpdateExperimentTemplateResponseTypeDef = TypedDict(
    "UpdateExperimentTemplateResponseTypeDef",
    {
        "experimentTemplate": "ExperimentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateExperimentTemplateStopConditionInputTypeDef = TypedDict(
    "_RequiredUpdateExperimentTemplateStopConditionInputTypeDef",
    {
        "source": str,
    },
)
_OptionalUpdateExperimentTemplateStopConditionInputTypeDef = TypedDict(
    "_OptionalUpdateExperimentTemplateStopConditionInputTypeDef",
    {
        "value": str,
    },
    total=False,
)

class UpdateExperimentTemplateStopConditionInputTypeDef(
    _RequiredUpdateExperimentTemplateStopConditionInputTypeDef,
    _OptionalUpdateExperimentTemplateStopConditionInputTypeDef,
):
    pass

_RequiredUpdateExperimentTemplateTargetInputTypeDef = TypedDict(
    "_RequiredUpdateExperimentTemplateTargetInputTypeDef",
    {
        "resourceType": str,
        "selectionMode": str,
    },
)
_OptionalUpdateExperimentTemplateTargetInputTypeDef = TypedDict(
    "_OptionalUpdateExperimentTemplateTargetInputTypeDef",
    {
        "resourceArns": List[str],
        "resourceTags": Dict[str, str],
        "filters": List["ExperimentTemplateTargetInputFilterTypeDef"],
        "parameters": Dict[str, str],
    },
    total=False,
)

class UpdateExperimentTemplateTargetInputTypeDef(
    _RequiredUpdateExperimentTemplateTargetInputTypeDef,
    _OptionalUpdateExperimentTemplateTargetInputTypeDef,
):
    pass
