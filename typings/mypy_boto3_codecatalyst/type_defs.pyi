"""
Type annotations for codecatalyst service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_codecatalyst.type_defs import AccessTokenSummaryTypeDef

    data: AccessTokenSummaryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    ComparisonOperatorType,
    DevEnvironmentSessionTypeType,
    DevEnvironmentStatusType,
    FilterKeyType,
    InstanceTypeType,
    OperationTypeType,
    UserTypeType,
    WorkflowRunModeType,
    WorkflowRunStatusType,
    WorkflowStatusType,
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
    "AccessTokenSummaryTypeDef",
    "CreateAccessTokenRequestTypeDef",
    "CreateAccessTokenResponseTypeDef",
    "CreateDevEnvironmentRequestTypeDef",
    "CreateDevEnvironmentResponseTypeDef",
    "CreateProjectRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateSourceRepositoryBranchRequestTypeDef",
    "CreateSourceRepositoryBranchResponseTypeDef",
    "CreateSourceRepositoryRequestTypeDef",
    "CreateSourceRepositoryResponseTypeDef",
    "DeleteAccessTokenRequestTypeDef",
    "DeleteDevEnvironmentRequestTypeDef",
    "DeleteDevEnvironmentResponseTypeDef",
    "DeleteProjectRequestTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteSourceRepositoryRequestTypeDef",
    "DeleteSourceRepositoryResponseTypeDef",
    "DeleteSpaceRequestTypeDef",
    "DeleteSpaceResponseTypeDef",
    "DevEnvironmentAccessDetailsTypeDef",
    "DevEnvironmentRepositorySummaryTypeDef",
    "DevEnvironmentSessionConfigurationTypeDef",
    "DevEnvironmentSessionSummaryTypeDef",
    "DevEnvironmentSummaryTypeDef",
    "EmailAddressTypeDef",
    "EventLogEntryTypeDef",
    "EventPayloadTypeDef",
    "ExecuteCommandSessionConfigurationTypeDef",
    "FilterTypeDef",
    "GetDevEnvironmentRequestTypeDef",
    "GetDevEnvironmentResponseTypeDef",
    "GetProjectRequestTypeDef",
    "GetProjectResponseTypeDef",
    "GetSourceRepositoryCloneUrlsRequestTypeDef",
    "GetSourceRepositoryCloneUrlsResponseTypeDef",
    "GetSourceRepositoryRequestTypeDef",
    "GetSourceRepositoryResponseTypeDef",
    "GetSpaceRequestTypeDef",
    "GetSpaceResponseTypeDef",
    "GetSubscriptionRequestTypeDef",
    "GetSubscriptionResponseTypeDef",
    "GetUserDetailsRequestTypeDef",
    "GetUserDetailsResponseTypeDef",
    "GetWorkflowRequestTypeDef",
    "GetWorkflowResponseTypeDef",
    "GetWorkflowRunRequestTypeDef",
    "GetWorkflowRunResponseTypeDef",
    "IdeConfigurationTypeDef",
    "IdeTypeDef",
    "ListAccessTokensRequestPaginateTypeDef",
    "ListAccessTokensRequestTypeDef",
    "ListAccessTokensResponseTypeDef",
    "ListDevEnvironmentSessionsRequestPaginateTypeDef",
    "ListDevEnvironmentSessionsRequestTypeDef",
    "ListDevEnvironmentSessionsResponseTypeDef",
    "ListDevEnvironmentsRequestPaginateTypeDef",
    "ListDevEnvironmentsRequestTypeDef",
    "ListDevEnvironmentsResponseTypeDef",
    "ListEventLogsRequestPaginateTypeDef",
    "ListEventLogsRequestTypeDef",
    "ListEventLogsResponseTypeDef",
    "ListProjectsRequestPaginateTypeDef",
    "ListProjectsRequestTypeDef",
    "ListProjectsResponseTypeDef",
    "ListSourceRepositoriesItemTypeDef",
    "ListSourceRepositoriesRequestPaginateTypeDef",
    "ListSourceRepositoriesRequestTypeDef",
    "ListSourceRepositoriesResponseTypeDef",
    "ListSourceRepositoryBranchesItemTypeDef",
    "ListSourceRepositoryBranchesRequestPaginateTypeDef",
    "ListSourceRepositoryBranchesRequestTypeDef",
    "ListSourceRepositoryBranchesResponseTypeDef",
    "ListSpacesRequestPaginateTypeDef",
    "ListSpacesRequestTypeDef",
    "ListSpacesResponseTypeDef",
    "ListWorkflowRunsRequestPaginateTypeDef",
    "ListWorkflowRunsRequestTypeDef",
    "ListWorkflowRunsResponseTypeDef",
    "ListWorkflowsRequestPaginateTypeDef",
    "ListWorkflowsRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PersistentStorageConfigurationTypeDef",
    "PersistentStorageTypeDef",
    "ProjectInformationTypeDef",
    "ProjectListFilterTypeDef",
    "ProjectSummaryTypeDef",
    "RepositoryInputTypeDef",
    "ResponseMetadataTypeDef",
    "SpaceSummaryTypeDef",
    "StartDevEnvironmentRequestTypeDef",
    "StartDevEnvironmentResponseTypeDef",
    "StartDevEnvironmentSessionRequestTypeDef",
    "StartDevEnvironmentSessionResponseTypeDef",
    "StartWorkflowRunRequestTypeDef",
    "StartWorkflowRunResponseTypeDef",
    "StopDevEnvironmentRequestTypeDef",
    "StopDevEnvironmentResponseTypeDef",
    "StopDevEnvironmentSessionRequestTypeDef",
    "StopDevEnvironmentSessionResponseTypeDef",
    "TimestampTypeDef",
    "UpdateDevEnvironmentRequestTypeDef",
    "UpdateDevEnvironmentResponseTypeDef",
    "UpdateProjectRequestTypeDef",
    "UpdateProjectResponseTypeDef",
    "UpdateSpaceRequestTypeDef",
    "UpdateSpaceResponseTypeDef",
    "UserIdentityTypeDef",
    "VerifySessionResponseTypeDef",
    "WorkflowDefinitionSummaryTypeDef",
    "WorkflowDefinitionTypeDef",
    "WorkflowRunSummaryTypeDef",
    "WorkflowSummaryTypeDef",
)

AccessTokenSummaryTypeDef = TypedDict(
    "AccessTokenSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "expiresTime": NotRequired[datetime],
    },
)
TimestampTypeDef = Union[datetime, str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class IdeConfigurationTypeDef(TypedDict):
    runtime: NotRequired[str]
    name: NotRequired[str]

class PersistentStorageConfigurationTypeDef(TypedDict):
    sizeInGiB: int

class RepositoryInputTypeDef(TypedDict):
    repositoryName: str
    branchName: NotRequired[str]

class CreateProjectRequestTypeDef(TypedDict):
    spaceName: str
    displayName: str
    description: NotRequired[str]

class CreateSourceRepositoryBranchRequestTypeDef(TypedDict):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    name: str
    headCommitId: NotRequired[str]

class CreateSourceRepositoryRequestTypeDef(TypedDict):
    spaceName: str
    projectName: str
    name: str
    description: NotRequired[str]

DeleteAccessTokenRequestTypeDef = TypedDict(
    "DeleteAccessTokenRequestTypeDef",
    {
        "id": str,
    },
)
DeleteDevEnvironmentRequestTypeDef = TypedDict(
    "DeleteDevEnvironmentRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
    },
)

class DeleteProjectRequestTypeDef(TypedDict):
    spaceName: str
    name: str

class DeleteSourceRepositoryRequestTypeDef(TypedDict):
    spaceName: str
    projectName: str
    name: str

class DeleteSpaceRequestTypeDef(TypedDict):
    name: str

class DevEnvironmentAccessDetailsTypeDef(TypedDict):
    streamUrl: str
    tokenValue: str

class DevEnvironmentRepositorySummaryTypeDef(TypedDict):
    repositoryName: str
    branchName: NotRequired[str]

class ExecuteCommandSessionConfigurationTypeDef(TypedDict):
    command: str
    arguments: NotRequired[Sequence[str]]

DevEnvironmentSessionSummaryTypeDef = TypedDict(
    "DevEnvironmentSessionSummaryTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "devEnvironmentId": str,
        "startedTime": datetime,
        "id": str,
    },
)

class IdeTypeDef(TypedDict):
    runtime: NotRequired[str]
    name: NotRequired[str]

class PersistentStorageTypeDef(TypedDict):
    sizeInGiB: int

class EmailAddressTypeDef(TypedDict):
    email: NotRequired[str]
    verified: NotRequired[bool]

class EventPayloadTypeDef(TypedDict):
    contentType: NotRequired[str]
    data: NotRequired[str]

class ProjectInformationTypeDef(TypedDict):
    name: NotRequired[str]
    projectId: NotRequired[str]

class UserIdentityTypeDef(TypedDict):
    userType: UserTypeType
    principalId: str
    userName: NotRequired[str]
    awsAccountId: NotRequired[str]

class FilterTypeDef(TypedDict):
    key: str
    values: Sequence[str]
    comparisonOperator: NotRequired[str]

GetDevEnvironmentRequestTypeDef = TypedDict(
    "GetDevEnvironmentRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
    },
)

class GetProjectRequestTypeDef(TypedDict):
    spaceName: str
    name: str

class GetSourceRepositoryCloneUrlsRequestTypeDef(TypedDict):
    spaceName: str
    projectName: str
    sourceRepositoryName: str

class GetSourceRepositoryRequestTypeDef(TypedDict):
    spaceName: str
    projectName: str
    name: str

class GetSpaceRequestTypeDef(TypedDict):
    name: str

class GetSubscriptionRequestTypeDef(TypedDict):
    spaceName: str

GetUserDetailsRequestTypeDef = TypedDict(
    "GetUserDetailsRequestTypeDef",
    {
        "id": NotRequired[str],
        "userName": NotRequired[str],
    },
)
GetWorkflowRequestTypeDef = TypedDict(
    "GetWorkflowRequestTypeDef",
    {
        "spaceName": str,
        "id": str,
        "projectName": str,
    },
)

class WorkflowDefinitionTypeDef(TypedDict):
    path: str

GetWorkflowRunRequestTypeDef = TypedDict(
    "GetWorkflowRunRequestTypeDef",
    {
        "spaceName": str,
        "id": str,
        "projectName": str,
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAccessTokensRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListDevEnvironmentSessionsRequestTypeDef(TypedDict):
    spaceName: str
    projectName: str
    devEnvironmentId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ProjectListFilterTypeDef(TypedDict):
    key: FilterKeyType
    values: Sequence[str]
    comparisonOperator: NotRequired[ComparisonOperatorType]

class ProjectSummaryTypeDef(TypedDict):
    name: str
    displayName: NotRequired[str]
    description: NotRequired[str]

ListSourceRepositoriesItemTypeDef = TypedDict(
    "ListSourceRepositoriesItemTypeDef",
    {
        "id": str,
        "name": str,
        "lastUpdatedTime": datetime,
        "createdTime": datetime,
        "description": NotRequired[str],
    },
)

class ListSourceRepositoriesRequestTypeDef(TypedDict):
    spaceName: str
    projectName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListSourceRepositoryBranchesItemTypeDef(TypedDict):
    ref: NotRequired[str]
    name: NotRequired[str]
    lastUpdatedTime: NotRequired[datetime]
    headCommitId: NotRequired[str]

class ListSourceRepositoryBranchesRequestTypeDef(TypedDict):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListSpacesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]

class SpaceSummaryTypeDef(TypedDict):
    name: str
    regionName: str
    displayName: NotRequired[str]
    description: NotRequired[str]

class ListWorkflowRunsRequestTypeDef(TypedDict):
    spaceName: str
    projectName: str
    workflowId: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    sortBy: NotRequired[Sequence[Mapping[str, Any]]]

WorkflowRunSummaryTypeDef = TypedDict(
    "WorkflowRunSummaryTypeDef",
    {
        "id": str,
        "workflowId": str,
        "workflowName": str,
        "status": WorkflowRunStatusType,
        "startTime": datetime,
        "lastUpdatedTime": datetime,
        "statusReasons": NotRequired[List[Dict[str, Any]]],
        "endTime": NotRequired[datetime],
    },
)

class ListWorkflowsRequestTypeDef(TypedDict):
    spaceName: str
    projectName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    sortBy: NotRequired[Sequence[Mapping[str, Any]]]

class StartWorkflowRunRequestTypeDef(TypedDict):
    spaceName: str
    projectName: str
    workflowId: str
    clientToken: NotRequired[str]

StopDevEnvironmentRequestTypeDef = TypedDict(
    "StopDevEnvironmentRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
    },
)
StopDevEnvironmentSessionRequestTypeDef = TypedDict(
    "StopDevEnvironmentSessionRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "sessionId": str,
    },
)

class UpdateProjectRequestTypeDef(TypedDict):
    spaceName: str
    name: str
    description: NotRequired[str]

class UpdateSpaceRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]

class WorkflowDefinitionSummaryTypeDef(TypedDict):
    path: str

class CreateAccessTokenRequestTypeDef(TypedDict):
    name: str
    expiresTime: NotRequired[TimestampTypeDef]

class ListEventLogsRequestTypeDef(TypedDict):
    spaceName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    eventName: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class CreateAccessTokenResponseTypeDef(TypedDict):
    secret: str
    name: str
    expiresTime: datetime
    accessTokenId: str
    ResponseMetadata: ResponseMetadataTypeDef

CreateDevEnvironmentResponseTypeDef = TypedDict(
    "CreateDevEnvironmentResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "vpcConnectionName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateProjectResponseTypeDef(TypedDict):
    spaceName: str
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSourceRepositoryBranchResponseTypeDef(TypedDict):
    ref: str
    name: str
    lastUpdatedTime: datetime
    headCommitId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSourceRepositoryResponseTypeDef(TypedDict):
    spaceName: str
    projectName: str
    name: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

DeleteDevEnvironmentResponseTypeDef = TypedDict(
    "DeleteDevEnvironmentResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DeleteProjectResponseTypeDef(TypedDict):
    spaceName: str
    name: str
    displayName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSourceRepositoryResponseTypeDef(TypedDict):
    spaceName: str
    projectName: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSpaceResponseTypeDef(TypedDict):
    name: str
    displayName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetProjectResponseTypeDef(TypedDict):
    spaceName: str
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSourceRepositoryCloneUrlsResponseTypeDef(TypedDict):
    https: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSourceRepositoryResponseTypeDef(TypedDict):
    spaceName: str
    projectName: str
    name: str
    description: str
    lastUpdatedTime: datetime
    createdTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetSpaceResponseTypeDef(TypedDict):
    name: str
    regionName: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriptionResponseTypeDef(TypedDict):
    subscriptionType: str
    awsAccountName: str
    pendingSubscriptionType: str
    pendingSubscriptionStartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

GetWorkflowRunResponseTypeDef = TypedDict(
    "GetWorkflowRunResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "workflowId": str,
        "status": WorkflowRunStatusType,
        "statusReasons": List[Dict[str, Any]],
        "startTime": datetime,
        "endTime": datetime,
        "lastUpdatedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListAccessTokensResponseTypeDef(TypedDict):
    items: List[AccessTokenSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

StartDevEnvironmentResponseTypeDef = TypedDict(
    "StartDevEnvironmentResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "status": DevEnvironmentStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartWorkflowRunResponseTypeDef = TypedDict(
    "StartWorkflowRunResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "workflowId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopDevEnvironmentResponseTypeDef = TypedDict(
    "StopDevEnvironmentResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "status": DevEnvironmentStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopDevEnvironmentSessionResponseTypeDef = TypedDict(
    "StopDevEnvironmentSessionResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "sessionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UpdateProjectResponseTypeDef(TypedDict):
    spaceName: str
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSpaceResponseTypeDef(TypedDict):
    name: str
    displayName: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifySessionResponseTypeDef(TypedDict):
    identity: str
    ResponseMetadata: ResponseMetadataTypeDef

StartDevEnvironmentRequestTypeDef = TypedDict(
    "StartDevEnvironmentRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "ides": NotRequired[Sequence[IdeConfigurationTypeDef]],
        "instanceType": NotRequired[InstanceTypeType],
        "inactivityTimeoutMinutes": NotRequired[int],
    },
)
UpdateDevEnvironmentRequestTypeDef = TypedDict(
    "UpdateDevEnvironmentRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "alias": NotRequired[str],
        "ides": NotRequired[Sequence[IdeConfigurationTypeDef]],
        "instanceType": NotRequired[InstanceTypeType],
        "inactivityTimeoutMinutes": NotRequired[int],
        "clientToken": NotRequired[str],
    },
)
UpdateDevEnvironmentResponseTypeDef = TypedDict(
    "UpdateDevEnvironmentResponseTypeDef",
    {
        "id": str,
        "spaceName": str,
        "projectName": str,
        "alias": str,
        "ides": List[IdeConfigurationTypeDef],
        "instanceType": InstanceTypeType,
        "inactivityTimeoutMinutes": int,
        "clientToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateDevEnvironmentRequestTypeDef(TypedDict):
    spaceName: str
    projectName: str
    instanceType: InstanceTypeType
    persistentStorage: PersistentStorageConfigurationTypeDef
    repositories: NotRequired[Sequence[RepositoryInputTypeDef]]
    clientToken: NotRequired[str]
    alias: NotRequired[str]
    ides: NotRequired[Sequence[IdeConfigurationTypeDef]]
    inactivityTimeoutMinutes: NotRequired[int]
    vpcConnectionName: NotRequired[str]

StartDevEnvironmentSessionResponseTypeDef = TypedDict(
    "StartDevEnvironmentSessionResponseTypeDef",
    {
        "accessDetails": DevEnvironmentAccessDetailsTypeDef,
        "sessionId": str,
        "spaceName": str,
        "projectName": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DevEnvironmentSessionConfigurationTypeDef(TypedDict):
    sessionType: DevEnvironmentSessionTypeType
    executeCommandSessionConfiguration: NotRequired[ExecuteCommandSessionConfigurationTypeDef]

class ListDevEnvironmentSessionsResponseTypeDef(TypedDict):
    items: List[DevEnvironmentSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

DevEnvironmentSummaryTypeDef = TypedDict(
    "DevEnvironmentSummaryTypeDef",
    {
        "id": str,
        "lastUpdatedTime": datetime,
        "creatorId": str,
        "status": DevEnvironmentStatusType,
        "repositories": List[DevEnvironmentRepositorySummaryTypeDef],
        "instanceType": InstanceTypeType,
        "inactivityTimeoutMinutes": int,
        "persistentStorage": PersistentStorageTypeDef,
        "spaceName": NotRequired[str],
        "projectName": NotRequired[str],
        "statusReason": NotRequired[str],
        "alias": NotRequired[str],
        "ides": NotRequired[List[IdeTypeDef]],
        "vpcConnectionName": NotRequired[str],
    },
)
GetDevEnvironmentResponseTypeDef = TypedDict(
    "GetDevEnvironmentResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "lastUpdatedTime": datetime,
        "creatorId": str,
        "status": DevEnvironmentStatusType,
        "statusReason": str,
        "repositories": List[DevEnvironmentRepositorySummaryTypeDef],
        "alias": str,
        "ides": List[IdeTypeDef],
        "instanceType": InstanceTypeType,
        "inactivityTimeoutMinutes": int,
        "persistentStorage": PersistentStorageTypeDef,
        "vpcConnectionName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetUserDetailsResponseTypeDef(TypedDict):
    userId: str
    userName: str
    displayName: str
    primaryEmail: EmailAddressTypeDef
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

EventLogEntryTypeDef = TypedDict(
    "EventLogEntryTypeDef",
    {
        "id": str,
        "eventName": str,
        "eventType": str,
        "eventCategory": str,
        "eventSource": str,
        "eventTime": datetime,
        "operationType": OperationTypeType,
        "userIdentity": UserIdentityTypeDef,
        "projectInformation": NotRequired[ProjectInformationTypeDef],
        "requestId": NotRequired[str],
        "requestPayload": NotRequired[EventPayloadTypeDef],
        "responsePayload": NotRequired[EventPayloadTypeDef],
        "errorCode": NotRequired[str],
        "sourceIpAddress": NotRequired[str],
        "userAgent": NotRequired[str],
    },
)

class ListDevEnvironmentsRequestTypeDef(TypedDict):
    spaceName: str
    projectName: NotRequired[str]
    filters: NotRequired[Sequence[FilterTypeDef]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

GetWorkflowResponseTypeDef = TypedDict(
    "GetWorkflowResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "name": str,
        "sourceRepositoryName": str,
        "sourceBranchName": str,
        "definition": WorkflowDefinitionTypeDef,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "runMode": WorkflowRunModeType,
        "status": WorkflowStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListAccessTokensRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDevEnvironmentSessionsRequestPaginateTypeDef(TypedDict):
    spaceName: str
    projectName: str
    devEnvironmentId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDevEnvironmentsRequestPaginateTypeDef(TypedDict):
    spaceName: str
    projectName: NotRequired[str]
    filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEventLogsRequestPaginateTypeDef(TypedDict):
    spaceName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    eventName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSourceRepositoriesRequestPaginateTypeDef(TypedDict):
    spaceName: str
    projectName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSourceRepositoryBranchesRequestPaginateTypeDef(TypedDict):
    spaceName: str
    projectName: str
    sourceRepositoryName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSpacesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkflowRunsRequestPaginateTypeDef(TypedDict):
    spaceName: str
    projectName: str
    workflowId: NotRequired[str]
    sortBy: NotRequired[Sequence[Mapping[str, Any]]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkflowsRequestPaginateTypeDef(TypedDict):
    spaceName: str
    projectName: str
    sortBy: NotRequired[Sequence[Mapping[str, Any]]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProjectsRequestPaginateTypeDef(TypedDict):
    spaceName: str
    filters: NotRequired[Sequence[ProjectListFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProjectsRequestTypeDef(TypedDict):
    spaceName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    filters: NotRequired[Sequence[ProjectListFilterTypeDef]]

class ListProjectsResponseTypeDef(TypedDict):
    items: List[ProjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSourceRepositoriesResponseTypeDef(TypedDict):
    items: List[ListSourceRepositoriesItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSourceRepositoryBranchesResponseTypeDef(TypedDict):
    items: List[ListSourceRepositoryBranchesItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSpacesResponseTypeDef(TypedDict):
    items: List[SpaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListWorkflowRunsResponseTypeDef(TypedDict):
    items: List[WorkflowRunSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

WorkflowSummaryTypeDef = TypedDict(
    "WorkflowSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "sourceRepositoryName": str,
        "sourceBranchName": str,
        "definition": WorkflowDefinitionSummaryTypeDef,
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "runMode": WorkflowRunModeType,
        "status": WorkflowStatusType,
    },
)
StartDevEnvironmentSessionRequestTypeDef = TypedDict(
    "StartDevEnvironmentSessionRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "sessionConfiguration": DevEnvironmentSessionConfigurationTypeDef,
    },
)

class ListDevEnvironmentsResponseTypeDef(TypedDict):
    items: List[DevEnvironmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListEventLogsResponseTypeDef(TypedDict):
    items: List[EventLogEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListWorkflowsResponseTypeDef(TypedDict):
    items: List[WorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
