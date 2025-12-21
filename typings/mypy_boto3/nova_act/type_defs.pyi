"""
Type annotations for nova-act service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_nova_act.type_defs import ActErrorTypeDef

    data: ActErrorTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any

from .literals import (
    ActStatusType,
    ModelStatusType,
    SortOrderType,
    WorkflowDefinitionStatusType,
    WorkflowRunStatusType,
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
    "ActErrorTypeDef",
    "ActSummaryTypeDef",
    "CallResultContentTypeDef",
    "CallResultTypeDef",
    "CallTypeDef",
    "ClientInfoTypeDef",
    "CompatibilityInformationTypeDef",
    "CreateActRequestTypeDef",
    "CreateActResponseTypeDef",
    "CreateSessionRequestTypeDef",
    "CreateSessionResponseTypeDef",
    "CreateWorkflowDefinitionRequestTypeDef",
    "CreateWorkflowDefinitionResponseTypeDef",
    "CreateWorkflowRunRequestTypeDef",
    "CreateWorkflowRunResponseTypeDef",
    "DeleteWorkflowDefinitionRequestTypeDef",
    "DeleteWorkflowDefinitionResponseTypeDef",
    "DeleteWorkflowRunRequestTypeDef",
    "DeleteWorkflowRunResponseTypeDef",
    "GetWorkflowDefinitionRequestTypeDef",
    "GetWorkflowDefinitionResponseTypeDef",
    "GetWorkflowRunRequestTypeDef",
    "GetWorkflowRunResponseTypeDef",
    "InvokeActStepRequestTypeDef",
    "InvokeActStepResponseTypeDef",
    "ListActsRequestPaginateTypeDef",
    "ListActsRequestTypeDef",
    "ListActsResponseTypeDef",
    "ListModelsRequestTypeDef",
    "ListModelsResponseTypeDef",
    "ListSessionsRequestPaginateTypeDef",
    "ListSessionsRequestTypeDef",
    "ListSessionsResponseTypeDef",
    "ListWorkflowDefinitionsRequestPaginateTypeDef",
    "ListWorkflowDefinitionsRequestTypeDef",
    "ListWorkflowDefinitionsResponseTypeDef",
    "ListWorkflowRunsRequestPaginateTypeDef",
    "ListWorkflowRunsRequestTypeDef",
    "ListWorkflowRunsResponseTypeDef",
    "ModelAliasTypeDef",
    "ModelLifecycleTypeDef",
    "ModelSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SessionSummaryTypeDef",
    "ToolInputSchemaTypeDef",
    "ToolSpecTypeDef",
    "TraceLocationTypeDef",
    "UpdateActRequestTypeDef",
    "UpdateWorkflowRunRequestTypeDef",
    "WorkflowDefinitionSummaryTypeDef",
    "WorkflowExportConfigTypeDef",
    "WorkflowRunSummaryTypeDef",
)

ActErrorTypeDef = TypedDict(
    "ActErrorTypeDef",
    {
        "message": str,
        "type": NotRequired[str],
    },
)

class TraceLocationTypeDef(TypedDict):
    locationType: Literal["S3"]
    location: str

class CallResultContentTypeDef(TypedDict):
    text: NotRequired[str]

CallTypeDef = TypedDict(
    "CallTypeDef",
    {
        "callId": str,
        "input": Dict[str, Any],
        "name": str,
    },
)

class ClientInfoTypeDef(TypedDict):
    compatibilityVersion: int
    sdkVersion: NotRequired[str]

class CompatibilityInformationTypeDef(TypedDict):
    clientCompatibilityVersion: int
    supportedModelIds: List[str]
    message: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateSessionRequestTypeDef(TypedDict):
    workflowDefinitionName: str
    workflowRunId: str
    clientToken: NotRequired[str]

class WorkflowExportConfigTypeDef(TypedDict):
    s3BucketName: str
    s3KeyPrefix: NotRequired[str]

class DeleteWorkflowDefinitionRequestTypeDef(TypedDict):
    workflowDefinitionName: str

class DeleteWorkflowRunRequestTypeDef(TypedDict):
    workflowDefinitionName: str
    workflowRunId: str

class GetWorkflowDefinitionRequestTypeDef(TypedDict):
    workflowDefinitionName: str

class GetWorkflowRunRequestTypeDef(TypedDict):
    workflowDefinitionName: str
    workflowRunId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListActsRequestTypeDef(TypedDict):
    workflowDefinitionName: str
    workflowRunId: NotRequired[str]
    sessionId: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortOrder: NotRequired[SortOrderType]

class ListModelsRequestTypeDef(TypedDict):
    clientCompatibilityVersion: int

class ModelAliasTypeDef(TypedDict):
    aliasName: str
    latestModelId: str
    resolvedModelId: NotRequired[str]

class ListSessionsRequestTypeDef(TypedDict):
    workflowDefinitionName: str
    workflowRunId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortOrder: NotRequired[SortOrderType]

class SessionSummaryTypeDef(TypedDict):
    sessionId: str

class ListWorkflowDefinitionsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortOrder: NotRequired[SortOrderType]

class WorkflowDefinitionSummaryTypeDef(TypedDict):
    workflowDefinitionArn: str
    workflowDefinitionName: str
    createdAt: datetime
    status: WorkflowDefinitionStatusType

class ListWorkflowRunsRequestTypeDef(TypedDict):
    workflowDefinitionName: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortOrder: NotRequired[SortOrderType]

class ModelLifecycleTypeDef(TypedDict):
    status: ModelStatusType

class ToolInputSchemaTypeDef(TypedDict):
    json: NotRequired[Mapping[str, Any]]

class UpdateWorkflowRunRequestTypeDef(TypedDict):
    workflowDefinitionName: str
    workflowRunId: str
    status: WorkflowRunStatusType

class UpdateActRequestTypeDef(TypedDict):
    workflowDefinitionName: str
    workflowRunId: str
    sessionId: str
    actId: str
    status: ActStatusType
    error: NotRequired[ActErrorTypeDef]

class ActSummaryTypeDef(TypedDict):
    workflowRunId: str
    sessionId: str
    actId: str
    status: ActStatusType
    startedAt: datetime
    endedAt: NotRequired[datetime]
    traceLocation: NotRequired[TraceLocationTypeDef]

class WorkflowRunSummaryTypeDef(TypedDict):
    workflowRunArn: str
    workflowRunId: str
    status: WorkflowRunStatusType
    startedAt: datetime
    endedAt: NotRequired[datetime]
    traceLocation: NotRequired[TraceLocationTypeDef]

class CallResultTypeDef(TypedDict):
    content: Sequence[CallResultContentTypeDef]
    callId: NotRequired[str]

class CreateWorkflowRunRequestTypeDef(TypedDict):
    workflowDefinitionName: str
    modelId: str
    clientInfo: ClientInfoTypeDef
    clientToken: NotRequired[str]
    logGroupName: NotRequired[str]

class CreateActResponseTypeDef(TypedDict):
    actId: str
    status: ActStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSessionResponseTypeDef(TypedDict):
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkflowDefinitionResponseTypeDef(TypedDict):
    status: WorkflowDefinitionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkflowRunResponseTypeDef(TypedDict):
    workflowRunId: str
    status: WorkflowRunStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkflowDefinitionResponseTypeDef(TypedDict):
    status: WorkflowDefinitionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkflowRunResponseTypeDef(TypedDict):
    status: WorkflowRunStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowRunResponseTypeDef(TypedDict):
    workflowRunArn: str
    workflowRunId: str
    status: WorkflowRunStatusType
    startedAt: datetime
    endedAt: datetime
    modelId: str
    logGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class InvokeActStepResponseTypeDef(TypedDict):
    calls: List[CallTypeDef]
    stepId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkflowDefinitionRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    exportConfig: NotRequired[WorkflowExportConfigTypeDef]
    clientToken: NotRequired[str]

class GetWorkflowDefinitionResponseTypeDef(TypedDict):
    name: str
    arn: str
    createdAt: datetime
    description: str
    exportConfig: WorkflowExportConfigTypeDef
    status: WorkflowDefinitionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListActsRequestPaginateTypeDef(TypedDict):
    workflowDefinitionName: str
    workflowRunId: NotRequired[str]
    sessionId: NotRequired[str]
    sortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSessionsRequestPaginateTypeDef(TypedDict):
    workflowDefinitionName: str
    workflowRunId: str
    sortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkflowDefinitionsRequestPaginateTypeDef(TypedDict):
    sortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkflowRunsRequestPaginateTypeDef(TypedDict):
    workflowDefinitionName: str
    sortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSessionsResponseTypeDef(TypedDict):
    sessionSummaries: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListWorkflowDefinitionsResponseTypeDef(TypedDict):
    workflowDefinitionSummaries: List[WorkflowDefinitionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ModelSummaryTypeDef(TypedDict):
    modelId: str
    modelLifecycle: ModelLifecycleTypeDef
    minimumCompatibilityVersion: int

class ToolSpecTypeDef(TypedDict):
    name: str
    description: str
    inputSchema: ToolInputSchemaTypeDef

class ListActsResponseTypeDef(TypedDict):
    actSummaries: List[ActSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListWorkflowRunsResponseTypeDef(TypedDict):
    workflowRunSummaries: List[WorkflowRunSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class InvokeActStepRequestTypeDef(TypedDict):
    workflowDefinitionName: str
    workflowRunId: str
    sessionId: str
    actId: str
    callResults: Sequence[CallResultTypeDef]
    previousStepId: NotRequired[str]

class ListModelsResponseTypeDef(TypedDict):
    modelSummaries: List[ModelSummaryTypeDef]
    modelAliases: List[ModelAliasTypeDef]
    compatibilityInformation: CompatibilityInformationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateActRequestTypeDef(TypedDict):
    workflowDefinitionName: str
    workflowRunId: str
    sessionId: str
    task: str
    toolSpecs: NotRequired[Sequence[ToolSpecTypeDef]]
    clientToken: NotRequired[str]
