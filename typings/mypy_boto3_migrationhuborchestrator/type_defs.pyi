"""
Type annotations for migrationhuborchestrator service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_migrationhuborchestrator.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    DataTypeType,
    MigrationWorkflowStatusEnumType,
    OwnerType,
    PluginHealthType,
    RunEnvironmentType,
    StepActionTypeType,
    StepGroupStatusType,
    StepStatusType,
    TargetTypeType,
    TemplateStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CreateMigrationWorkflowRequestTypeDef",
    "CreateMigrationWorkflowResponseTypeDef",
    "CreateTemplateRequestTypeDef",
    "CreateTemplateResponseTypeDef",
    "CreateWorkflowStepGroupRequestTypeDef",
    "CreateWorkflowStepGroupResponseTypeDef",
    "CreateWorkflowStepRequestTypeDef",
    "CreateWorkflowStepResponseTypeDef",
    "DeleteMigrationWorkflowRequestTypeDef",
    "DeleteMigrationWorkflowResponseTypeDef",
    "DeleteTemplateRequestTypeDef",
    "DeleteWorkflowStepGroupRequestTypeDef",
    "DeleteWorkflowStepRequestTypeDef",
    "GetMigrationWorkflowRequestTypeDef",
    "GetMigrationWorkflowResponseTypeDef",
    "GetMigrationWorkflowTemplateRequestTypeDef",
    "GetMigrationWorkflowTemplateResponseTypeDef",
    "GetTemplateStepGroupRequestTypeDef",
    "GetTemplateStepGroupResponseTypeDef",
    "GetTemplateStepRequestTypeDef",
    "GetTemplateStepResponseTypeDef",
    "GetWorkflowStepGroupRequestTypeDef",
    "GetWorkflowStepGroupResponseTypeDef",
    "GetWorkflowStepRequestTypeDef",
    "GetWorkflowStepResponseTypeDef",
    "ListMigrationWorkflowTemplatesRequestPaginateTypeDef",
    "ListMigrationWorkflowTemplatesRequestTypeDef",
    "ListMigrationWorkflowTemplatesResponseTypeDef",
    "ListMigrationWorkflowsRequestPaginateTypeDef",
    "ListMigrationWorkflowsRequestTypeDef",
    "ListMigrationWorkflowsResponseTypeDef",
    "ListPluginsRequestPaginateTypeDef",
    "ListPluginsRequestTypeDef",
    "ListPluginsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTemplateStepGroupsRequestPaginateTypeDef",
    "ListTemplateStepGroupsRequestTypeDef",
    "ListTemplateStepGroupsResponseTypeDef",
    "ListTemplateStepsRequestPaginateTypeDef",
    "ListTemplateStepsRequestTypeDef",
    "ListTemplateStepsResponseTypeDef",
    "ListWorkflowStepGroupsRequestPaginateTypeDef",
    "ListWorkflowStepGroupsRequestTypeDef",
    "ListWorkflowStepGroupsResponseTypeDef",
    "ListWorkflowStepsRequestPaginateTypeDef",
    "ListWorkflowStepsRequestTypeDef",
    "ListWorkflowStepsResponseTypeDef",
    "MigrationWorkflowSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PlatformCommandTypeDef",
    "PlatformScriptKeyTypeDef",
    "PluginSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "RetryWorkflowStepRequestTypeDef",
    "RetryWorkflowStepResponseTypeDef",
    "StartMigrationWorkflowRequestTypeDef",
    "StartMigrationWorkflowResponseTypeDef",
    "StepAutomationConfigurationTypeDef",
    "StepInputOutputTypeDef",
    "StepInputTypeDef",
    "StepInputUnionTypeDef",
    "StepOutputTypeDef",
    "StopMigrationWorkflowRequestTypeDef",
    "StopMigrationWorkflowResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TemplateInputTypeDef",
    "TemplateSourceTypeDef",
    "TemplateStepGroupSummaryTypeDef",
    "TemplateStepSummaryTypeDef",
    "TemplateSummaryTypeDef",
    "ToolTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateMigrationWorkflowRequestTypeDef",
    "UpdateMigrationWorkflowResponseTypeDef",
    "UpdateTemplateRequestTypeDef",
    "UpdateTemplateResponseTypeDef",
    "UpdateWorkflowStepGroupRequestTypeDef",
    "UpdateWorkflowStepGroupResponseTypeDef",
    "UpdateWorkflowStepRequestTypeDef",
    "UpdateWorkflowStepResponseTypeDef",
    "WorkflowStepAutomationConfigurationTypeDef",
    "WorkflowStepExtraTypeDef",
    "WorkflowStepGroupSummaryTypeDef",
    "WorkflowStepOutputTypeDef",
    "WorkflowStepOutputUnionOutputTypeDef",
    "WorkflowStepOutputUnionTypeDef",
    "WorkflowStepOutputUnionUnionTypeDef",
    "WorkflowStepSummaryTypeDef",
    "WorkflowStepUnionTypeDef",
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class StepInputOutputTypeDef(TypedDict):
    integerValue: NotRequired[int]
    stringValue: NotRequired[str]
    listOfStringsValue: NotRequired[List[str]]
    mapOfStringValue: NotRequired[Dict[str, str]]

class TemplateSourceTypeDef(TypedDict):
    workflowId: NotRequired[str]

CreateWorkflowStepGroupRequestTypeDef = TypedDict(
    "CreateWorkflowStepGroupRequestTypeDef",
    {
        "workflowId": str,
        "name": str,
        "description": NotRequired[str],
        "next": NotRequired[Sequence[str]],
        "previous": NotRequired[Sequence[str]],
    },
)

class ToolTypeDef(TypedDict):
    name: NotRequired[str]
    url: NotRequired[str]

DeleteMigrationWorkflowRequestTypeDef = TypedDict(
    "DeleteMigrationWorkflowRequestTypeDef",
    {
        "id": str,
    },
)
DeleteTemplateRequestTypeDef = TypedDict(
    "DeleteTemplateRequestTypeDef",
    {
        "id": str,
    },
)
DeleteWorkflowStepGroupRequestTypeDef = TypedDict(
    "DeleteWorkflowStepGroupRequestTypeDef",
    {
        "workflowId": str,
        "id": str,
    },
)
DeleteWorkflowStepRequestTypeDef = TypedDict(
    "DeleteWorkflowStepRequestTypeDef",
    {
        "id": str,
        "stepGroupId": str,
        "workflowId": str,
    },
)
GetMigrationWorkflowRequestTypeDef = TypedDict(
    "GetMigrationWorkflowRequestTypeDef",
    {
        "id": str,
    },
)
GetMigrationWorkflowTemplateRequestTypeDef = TypedDict(
    "GetMigrationWorkflowTemplateRequestTypeDef",
    {
        "id": str,
    },
)

class TemplateInputTypeDef(TypedDict):
    inputName: NotRequired[str]
    dataType: NotRequired[DataTypeType]
    required: NotRequired[bool]

GetTemplateStepGroupRequestTypeDef = TypedDict(
    "GetTemplateStepGroupRequestTypeDef",
    {
        "templateId": str,
        "id": str,
    },
)
GetTemplateStepRequestTypeDef = TypedDict(
    "GetTemplateStepRequestTypeDef",
    {
        "id": str,
        "templateId": str,
        "stepGroupId": str,
    },
)

class StepOutputTypeDef(TypedDict):
    name: NotRequired[str]
    dataType: NotRequired[DataTypeType]
    required: NotRequired[bool]

GetWorkflowStepGroupRequestTypeDef = TypedDict(
    "GetWorkflowStepGroupRequestTypeDef",
    {
        "id": str,
        "workflowId": str,
    },
)
GetWorkflowStepRequestTypeDef = TypedDict(
    "GetWorkflowStepRequestTypeDef",
    {
        "workflowId": str,
        "stepGroupId": str,
        "id": str,
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListMigrationWorkflowTemplatesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    name: NotRequired[str]

TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "description": NotRequired[str],
    },
)

class ListMigrationWorkflowsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    templateId: NotRequired[str]
    adsApplicationConfigurationName: NotRequired[str]
    status: NotRequired[MigrationWorkflowStatusEnumType]
    name: NotRequired[str]

MigrationWorkflowSummaryTypeDef = TypedDict(
    "MigrationWorkflowSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "templateId": NotRequired[str],
        "adsApplicationConfigurationName": NotRequired[str],
        "status": NotRequired[MigrationWorkflowStatusEnumType],
        "creationTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "statusMessage": NotRequired[str],
        "completedSteps": NotRequired[int],
        "totalSteps": NotRequired[int],
    },
)

class ListPluginsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class PluginSummaryTypeDef(TypedDict):
    pluginId: NotRequired[str]
    hostname: NotRequired[str]
    status: NotRequired[PluginHealthType]
    ipAddress: NotRequired[str]
    version: NotRequired[str]
    registeredTime: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListTemplateStepGroupsRequestTypeDef(TypedDict):
    templateId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

TemplateStepGroupSummaryTypeDef = TypedDict(
    "TemplateStepGroupSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "previous": NotRequired[List[str]],
        "next": NotRequired[List[str]],
    },
)

class ListTemplateStepsRequestTypeDef(TypedDict):
    templateId: str
    stepGroupId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

TemplateStepSummaryTypeDef = TypedDict(
    "TemplateStepSummaryTypeDef",
    {
        "id": NotRequired[str],
        "stepGroupId": NotRequired[str],
        "templateId": NotRequired[str],
        "name": NotRequired[str],
        "stepActionType": NotRequired[StepActionTypeType],
        "targetType": NotRequired[TargetTypeType],
        "owner": NotRequired[OwnerType],
        "previous": NotRequired[List[str]],
        "next": NotRequired[List[str]],
    },
)

class ListWorkflowStepGroupsRequestTypeDef(TypedDict):
    workflowId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

WorkflowStepGroupSummaryTypeDef = TypedDict(
    "WorkflowStepGroupSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "owner": NotRequired[OwnerType],
        "status": NotRequired[StepGroupStatusType],
        "previous": NotRequired[List[str]],
        "next": NotRequired[List[str]],
    },
)

class ListWorkflowStepsRequestTypeDef(TypedDict):
    workflowId: str
    stepGroupId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

WorkflowStepSummaryTypeDef = TypedDict(
    "WorkflowStepSummaryTypeDef",
    {
        "stepId": NotRequired[str],
        "name": NotRequired[str],
        "stepActionType": NotRequired[StepActionTypeType],
        "owner": NotRequired[OwnerType],
        "previous": NotRequired[List[str]],
        "next": NotRequired[List[str]],
        "status": NotRequired[StepStatusType],
        "statusMessage": NotRequired[str],
        "noOfSrvCompleted": NotRequired[int],
        "noOfSrvFailed": NotRequired[int],
        "totalNoOfSrv": NotRequired[int],
        "description": NotRequired[str],
        "scriptLocation": NotRequired[str],
    },
)

class PlatformCommandTypeDef(TypedDict):
    linux: NotRequired[str]
    windows: NotRequired[str]

class PlatformScriptKeyTypeDef(TypedDict):
    linux: NotRequired[str]
    windows: NotRequired[str]

RetryWorkflowStepRequestTypeDef = TypedDict(
    "RetryWorkflowStepRequestTypeDef",
    {
        "workflowId": str,
        "stepGroupId": str,
        "id": str,
    },
)
StartMigrationWorkflowRequestTypeDef = TypedDict(
    "StartMigrationWorkflowRequestTypeDef",
    {
        "id": str,
    },
)

class StepInputTypeDef(TypedDict):
    integerValue: NotRequired[int]
    stringValue: NotRequired[str]
    listOfStringsValue: NotRequired[Sequence[str]]
    mapOfStringValue: NotRequired[Mapping[str, str]]

StopMigrationWorkflowRequestTypeDef = TypedDict(
    "StopMigrationWorkflowRequestTypeDef",
    {
        "id": str,
    },
)

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

UpdateTemplateRequestTypeDef = TypedDict(
    "UpdateTemplateRequestTypeDef",
    {
        "id": str,
        "templateName": NotRequired[str],
        "templateDescription": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)
UpdateWorkflowStepGroupRequestTypeDef = TypedDict(
    "UpdateWorkflowStepGroupRequestTypeDef",
    {
        "workflowId": str,
        "id": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "next": NotRequired[Sequence[str]],
        "previous": NotRequired[Sequence[str]],
    },
)

class WorkflowStepOutputUnionOutputTypeDef(TypedDict):
    integerValue: NotRequired[int]
    stringValue: NotRequired[str]
    listOfStringValue: NotRequired[List[str]]

class WorkflowStepOutputUnionTypeDef(TypedDict):
    integerValue: NotRequired[int]
    stringValue: NotRequired[str]
    listOfStringValue: NotRequired[Sequence[str]]

class CreateTemplateResponseTypeDef(TypedDict):
    templateId: str
    templateArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

CreateWorkflowStepResponseTypeDef = TypedDict(
    "CreateWorkflowStepResponseTypeDef",
    {
        "id": str,
        "stepGroupId": str,
        "workflowId": str,
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteMigrationWorkflowResponseTypeDef = TypedDict(
    "DeleteMigrationWorkflowResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "status": MigrationWorkflowStatusEnumType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

RetryWorkflowStepResponseTypeDef = TypedDict(
    "RetryWorkflowStepResponseTypeDef",
    {
        "stepGroupId": str,
        "workflowId": str,
        "id": str,
        "status": StepStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMigrationWorkflowResponseTypeDef = TypedDict(
    "StartMigrationWorkflowResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "status": MigrationWorkflowStatusEnumType,
        "statusMessage": str,
        "lastStartTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopMigrationWorkflowResponseTypeDef = TypedDict(
    "StopMigrationWorkflowResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "status": MigrationWorkflowStatusEnumType,
        "statusMessage": str,
        "lastStopTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UpdateTemplateResponseTypeDef(TypedDict):
    templateId: str
    templateArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

UpdateWorkflowStepResponseTypeDef = TypedDict(
    "UpdateWorkflowStepResponseTypeDef",
    {
        "id": str,
        "stepGroupId": str,
        "workflowId": str,
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateMigrationWorkflowResponseTypeDef = TypedDict(
    "CreateMigrationWorkflowResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "templateId": str,
        "adsApplicationConfigurationId": str,
        "workflowInputs": Dict[str, StepInputOutputTypeDef],
        "stepTargets": List[str],
        "status": MigrationWorkflowStatusEnumType,
        "creationTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateMigrationWorkflowResponseTypeDef = TypedDict(
    "UpdateMigrationWorkflowResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "templateId": str,
        "adsApplicationConfigurationId": str,
        "workflowInputs": Dict[str, StepInputOutputTypeDef],
        "stepTargets": List[str],
        "status": MigrationWorkflowStatusEnumType,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateTemplateRequestTypeDef(TypedDict):
    templateName: str
    templateSource: TemplateSourceTypeDef
    templateDescription: NotRequired[str]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

CreateWorkflowStepGroupResponseTypeDef = TypedDict(
    "CreateWorkflowStepGroupResponseTypeDef",
    {
        "workflowId": str,
        "name": str,
        "id": str,
        "description": str,
        "tools": List[ToolTypeDef],
        "next": List[str],
        "previous": List[str],
        "creationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMigrationWorkflowResponseTypeDef = TypedDict(
    "GetMigrationWorkflowResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "templateId": str,
        "adsApplicationConfigurationId": str,
        "adsApplicationName": str,
        "status": MigrationWorkflowStatusEnumType,
        "statusMessage": str,
        "creationTime": datetime,
        "lastStartTime": datetime,
        "lastStopTime": datetime,
        "lastModifiedTime": datetime,
        "endTime": datetime,
        "tools": List[ToolTypeDef],
        "totalSteps": int,
        "completedSteps": int,
        "workflowInputs": Dict[str, StepInputOutputTypeDef],
        "tags": Dict[str, str],
        "workflowBucket": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTemplateStepGroupResponseTypeDef = TypedDict(
    "GetTemplateStepGroupResponseTypeDef",
    {
        "templateId": str,
        "id": str,
        "name": str,
        "description": str,
        "status": StepGroupStatusType,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "tools": List[ToolTypeDef],
        "previous": List[str],
        "next": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetWorkflowStepGroupResponseTypeDef = TypedDict(
    "GetWorkflowStepGroupResponseTypeDef",
    {
        "id": str,
        "workflowId": str,
        "name": str,
        "description": str,
        "status": StepGroupStatusType,
        "owner": OwnerType,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "endTime": datetime,
        "tools": List[ToolTypeDef],
        "previous": List[str],
        "next": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateWorkflowStepGroupResponseTypeDef = TypedDict(
    "UpdateWorkflowStepGroupResponseTypeDef",
    {
        "workflowId": str,
        "name": str,
        "id": str,
        "description": str,
        "tools": List[ToolTypeDef],
        "next": List[str],
        "previous": List[str],
        "lastModifiedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMigrationWorkflowTemplateResponseTypeDef = TypedDict(
    "GetMigrationWorkflowTemplateResponseTypeDef",
    {
        "id": str,
        "templateArn": str,
        "name": str,
        "description": str,
        "inputs": List[TemplateInputTypeDef],
        "tools": List[ToolTypeDef],
        "creationTime": datetime,
        "owner": str,
        "status": TemplateStatusType,
        "statusMessage": str,
        "templateClass": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListMigrationWorkflowTemplatesRequestPaginateTypeDef(TypedDict):
    name: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMigrationWorkflowsRequestPaginateTypeDef(TypedDict):
    templateId: NotRequired[str]
    adsApplicationConfigurationName: NotRequired[str]
    status: NotRequired[MigrationWorkflowStatusEnumType]
    name: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPluginsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTemplateStepGroupsRequestPaginateTypeDef(TypedDict):
    templateId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTemplateStepsRequestPaginateTypeDef(TypedDict):
    templateId: str
    stepGroupId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkflowStepGroupsRequestPaginateTypeDef(TypedDict):
    workflowId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkflowStepsRequestPaginateTypeDef(TypedDict):
    workflowId: str
    stepGroupId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMigrationWorkflowTemplatesResponseTypeDef(TypedDict):
    templateSummary: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListMigrationWorkflowsResponseTypeDef(TypedDict):
    migrationWorkflowSummary: List[MigrationWorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListPluginsResponseTypeDef(TypedDict):
    plugins: List[PluginSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTemplateStepGroupsResponseTypeDef(TypedDict):
    templateStepGroupSummary: List[TemplateStepGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTemplateStepsResponseTypeDef(TypedDict):
    templateStepSummaryList: List[TemplateStepSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListWorkflowStepGroupsResponseTypeDef(TypedDict):
    workflowStepGroupsSummary: List[WorkflowStepGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListWorkflowStepsResponseTypeDef(TypedDict):
    workflowStepsSummary: List[WorkflowStepSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StepAutomationConfigurationTypeDef(TypedDict):
    scriptLocationS3Bucket: NotRequired[str]
    scriptLocationS3Key: NotRequired[PlatformScriptKeyTypeDef]
    command: NotRequired[PlatformCommandTypeDef]
    runEnvironment: NotRequired[RunEnvironmentType]
    targetType: NotRequired[TargetTypeType]

class WorkflowStepAutomationConfigurationTypeDef(TypedDict):
    scriptLocationS3Bucket: NotRequired[str]
    scriptLocationS3Key: NotRequired[PlatformScriptKeyTypeDef]
    command: NotRequired[PlatformCommandTypeDef]
    runEnvironment: NotRequired[RunEnvironmentType]
    targetType: NotRequired[TargetTypeType]

StepInputUnionTypeDef = Union[StepInputTypeDef, StepInputOutputTypeDef]

class WorkflowStepExtraTypeDef(TypedDict):
    name: NotRequired[str]
    dataType: NotRequired[DataTypeType]
    required: NotRequired[bool]
    value: NotRequired[WorkflowStepOutputUnionOutputTypeDef]

WorkflowStepOutputUnionUnionTypeDef = Union[
    WorkflowStepOutputUnionTypeDef, WorkflowStepOutputUnionOutputTypeDef
]
GetTemplateStepResponseTypeDef = TypedDict(
    "GetTemplateStepResponseTypeDef",
    {
        "id": str,
        "stepGroupId": str,
        "templateId": str,
        "name": str,
        "description": str,
        "stepActionType": StepActionTypeType,
        "creationTime": str,
        "previous": List[str],
        "next": List[str],
        "outputs": List[StepOutputTypeDef],
        "stepAutomationConfiguration": StepAutomationConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateMigrationWorkflowRequestTypeDef(TypedDict):
    name: str
    templateId: str
    inputParameters: Mapping[str, StepInputUnionTypeDef]
    description: NotRequired[str]
    applicationConfigurationId: NotRequired[str]
    stepTargets: NotRequired[Sequence[str]]
    tags: NotRequired[Mapping[str, str]]

UpdateMigrationWorkflowRequestTypeDef = TypedDict(
    "UpdateMigrationWorkflowRequestTypeDef",
    {
        "id": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "inputParameters": NotRequired[Mapping[str, StepInputUnionTypeDef]],
        "stepTargets": NotRequired[Sequence[str]],
    },
)
GetWorkflowStepResponseTypeDef = TypedDict(
    "GetWorkflowStepResponseTypeDef",
    {
        "name": str,
        "stepGroupId": str,
        "workflowId": str,
        "stepId": str,
        "description": str,
        "stepActionType": StepActionTypeType,
        "owner": OwnerType,
        "workflowStepAutomationConfiguration": WorkflowStepAutomationConfigurationTypeDef,
        "stepTarget": List[str],
        "outputs": List[WorkflowStepExtraTypeDef],
        "previous": List[str],
        "next": List[str],
        "status": StepStatusType,
        "statusMessage": str,
        "scriptOutputLocation": str,
        "creationTime": datetime,
        "lastStartTime": datetime,
        "endTime": datetime,
        "noOfSrvCompleted": int,
        "noOfSrvFailed": int,
        "totalNoOfSrv": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class WorkflowStepOutputTypeDef(TypedDict):
    name: NotRequired[str]
    dataType: NotRequired[DataTypeType]
    required: NotRequired[bool]
    value: NotRequired[WorkflowStepOutputUnionUnionTypeDef]

WorkflowStepUnionTypeDef = Union[WorkflowStepOutputTypeDef, WorkflowStepExtraTypeDef]
CreateWorkflowStepRequestTypeDef = TypedDict(
    "CreateWorkflowStepRequestTypeDef",
    {
        "name": str,
        "stepGroupId": str,
        "workflowId": str,
        "stepActionType": StepActionTypeType,
        "description": NotRequired[str],
        "workflowStepAutomationConfiguration": NotRequired[
            WorkflowStepAutomationConfigurationTypeDef
        ],
        "stepTarget": NotRequired[Sequence[str]],
        "outputs": NotRequired[Sequence[WorkflowStepUnionTypeDef]],
        "previous": NotRequired[Sequence[str]],
        "next": NotRequired[Sequence[str]],
    },
)
UpdateWorkflowStepRequestTypeDef = TypedDict(
    "UpdateWorkflowStepRequestTypeDef",
    {
        "id": str,
        "stepGroupId": str,
        "workflowId": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "stepActionType": NotRequired[StepActionTypeType],
        "workflowStepAutomationConfiguration": NotRequired[
            WorkflowStepAutomationConfigurationTypeDef
        ],
        "stepTarget": NotRequired[Sequence[str]],
        "outputs": NotRequired[Sequence[WorkflowStepUnionTypeDef]],
        "previous": NotRequired[Sequence[str]],
        "next": NotRequired[Sequence[str]],
        "status": NotRequired[StepStatusType],
    },
)
