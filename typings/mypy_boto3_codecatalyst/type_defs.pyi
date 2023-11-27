"""
Type annotations for codecatalyst service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codecatalyst/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codecatalyst.type_defs import AccessTokenSummaryTypeDef

    data: AccessTokenSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

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

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccessTokenSummaryTypeDef",
    "CreateAccessTokenRequestRequestTypeDef",
    "CreateAccessTokenResponseTypeDef",
    "CreateDevEnvironmentRequestRequestTypeDef",
    "CreateDevEnvironmentResponseTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateSourceRepositoryBranchRequestRequestTypeDef",
    "CreateSourceRepositoryBranchResponseTypeDef",
    "CreateSourceRepositoryRequestRequestTypeDef",
    "CreateSourceRepositoryResponseTypeDef",
    "DeleteAccessTokenRequestRequestTypeDef",
    "DeleteDevEnvironmentRequestRequestTypeDef",
    "DeleteDevEnvironmentResponseTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteSourceRepositoryRequestRequestTypeDef",
    "DeleteSourceRepositoryResponseTypeDef",
    "DeleteSpaceRequestRequestTypeDef",
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
    "GetDevEnvironmentRequestRequestTypeDef",
    "GetDevEnvironmentResponseTypeDef",
    "GetProjectRequestRequestTypeDef",
    "GetProjectResponseTypeDef",
    "GetSourceRepositoryCloneUrlsRequestRequestTypeDef",
    "GetSourceRepositoryCloneUrlsResponseTypeDef",
    "GetSourceRepositoryRequestRequestTypeDef",
    "GetSourceRepositoryResponseTypeDef",
    "GetSpaceRequestRequestTypeDef",
    "GetSpaceResponseTypeDef",
    "GetSubscriptionRequestRequestTypeDef",
    "GetSubscriptionResponseTypeDef",
    "GetUserDetailsRequestRequestTypeDef",
    "GetUserDetailsResponseTypeDef",
    "GetWorkflowRequestRequestTypeDef",
    "GetWorkflowResponseTypeDef",
    "GetWorkflowRunRequestRequestTypeDef",
    "GetWorkflowRunResponseTypeDef",
    "IdeConfigurationTypeDef",
    "IdeTypeDef",
    "ListAccessTokensRequestRequestTypeDef",
    "ListAccessTokensResponseTypeDef",
    "ListDevEnvironmentSessionsRequestRequestTypeDef",
    "ListDevEnvironmentSessionsResponseTypeDef",
    "ListDevEnvironmentsRequestRequestTypeDef",
    "ListDevEnvironmentsResponseTypeDef",
    "ListEventLogsRequestRequestTypeDef",
    "ListEventLogsResponseTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResponseTypeDef",
    "ListSourceRepositoriesItemTypeDef",
    "ListSourceRepositoriesRequestRequestTypeDef",
    "ListSourceRepositoriesResponseTypeDef",
    "ListSourceRepositoryBranchesItemTypeDef",
    "ListSourceRepositoryBranchesRequestRequestTypeDef",
    "ListSourceRepositoryBranchesResponseTypeDef",
    "ListSpacesRequestRequestTypeDef",
    "ListSpacesResponseTypeDef",
    "ListWorkflowRunsRequestRequestTypeDef",
    "ListWorkflowRunsResponseTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
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
    "StartDevEnvironmentRequestRequestTypeDef",
    "StartDevEnvironmentResponseTypeDef",
    "StartDevEnvironmentSessionRequestRequestTypeDef",
    "StartDevEnvironmentSessionResponseTypeDef",
    "StartWorkflowRunRequestRequestTypeDef",
    "StartWorkflowRunResponseTypeDef",
    "StopDevEnvironmentRequestRequestTypeDef",
    "StopDevEnvironmentResponseTypeDef",
    "StopDevEnvironmentSessionRequestRequestTypeDef",
    "StopDevEnvironmentSessionResponseTypeDef",
    "UpdateDevEnvironmentRequestRequestTypeDef",
    "UpdateDevEnvironmentResponseTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "UpdateProjectResponseTypeDef",
    "UpdateSpaceRequestRequestTypeDef",
    "UpdateSpaceResponseTypeDef",
    "UserIdentityTypeDef",
    "VerifySessionResponseTypeDef",
    "WorkflowDefinitionSummaryTypeDef",
    "WorkflowDefinitionTypeDef",
    "WorkflowRunSummaryTypeDef",
    "WorkflowSummaryTypeDef",
)

_RequiredAccessTokenSummaryTypeDef = TypedDict(
    "_RequiredAccessTokenSummaryTypeDef",
    {
        "id": str,
        "name": str,
    },
)
_OptionalAccessTokenSummaryTypeDef = TypedDict(
    "_OptionalAccessTokenSummaryTypeDef",
    {
        "expiresTime": datetime,
    },
    total=False,
)

class AccessTokenSummaryTypeDef(
    _RequiredAccessTokenSummaryTypeDef, _OptionalAccessTokenSummaryTypeDef
):
    pass

_RequiredCreateAccessTokenRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessTokenRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateAccessTokenRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessTokenRequestRequestTypeDef",
    {
        "expiresTime": Union[datetime, str],
    },
    total=False,
)

class CreateAccessTokenRequestRequestTypeDef(
    _RequiredCreateAccessTokenRequestRequestTypeDef, _OptionalCreateAccessTokenRequestRequestTypeDef
):
    pass

CreateAccessTokenResponseTypeDef = TypedDict(
    "CreateAccessTokenResponseTypeDef",
    {
        "secret": str,
        "name": str,
        "expiresTime": datetime,
        "accessTokenId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDevEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDevEnvironmentRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "instanceType": InstanceTypeType,
        "persistentStorage": "PersistentStorageConfigurationTypeDef",
    },
)
_OptionalCreateDevEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDevEnvironmentRequestRequestTypeDef",
    {
        "repositories": List["RepositoryInputTypeDef"],
        "clientToken": str,
        "alias": str,
        "ides": List["IdeConfigurationTypeDef"],
        "inactivityTimeoutMinutes": int,
        "vpcConnectionName": str,
    },
    total=False,
)

class CreateDevEnvironmentRequestRequestTypeDef(
    _RequiredCreateDevEnvironmentRequestRequestTypeDef,
    _OptionalCreateDevEnvironmentRequestRequestTypeDef,
):
    pass

CreateDevEnvironmentResponseTypeDef = TypedDict(
    "CreateDevEnvironmentResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "vpcConnectionName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestRequestTypeDef",
    {
        "spaceName": str,
        "displayName": str,
    },
)
_OptionalCreateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class CreateProjectRequestRequestTypeDef(
    _RequiredCreateProjectRequestRequestTypeDef, _OptionalCreateProjectRequestRequestTypeDef
):
    pass

CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "spaceName": str,
        "name": str,
        "displayName": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSourceRepositoryBranchRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSourceRepositoryBranchRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "sourceRepositoryName": str,
        "name": str,
    },
)
_OptionalCreateSourceRepositoryBranchRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSourceRepositoryBranchRequestRequestTypeDef",
    {
        "headCommitId": str,
    },
    total=False,
)

class CreateSourceRepositoryBranchRequestRequestTypeDef(
    _RequiredCreateSourceRepositoryBranchRequestRequestTypeDef,
    _OptionalCreateSourceRepositoryBranchRequestRequestTypeDef,
):
    pass

CreateSourceRepositoryBranchResponseTypeDef = TypedDict(
    "CreateSourceRepositoryBranchResponseTypeDef",
    {
        "ref": str,
        "name": str,
        "lastUpdatedTime": datetime,
        "headCommitId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSourceRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSourceRepositoryRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "name": str,
    },
)
_OptionalCreateSourceRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSourceRepositoryRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class CreateSourceRepositoryRequestRequestTypeDef(
    _RequiredCreateSourceRepositoryRequestRequestTypeDef,
    _OptionalCreateSourceRepositoryRequestRequestTypeDef,
):
    pass

CreateSourceRepositoryResponseTypeDef = TypedDict(
    "CreateSourceRepositoryResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "name": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccessTokenRequestRequestTypeDef = TypedDict(
    "DeleteAccessTokenRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteDevEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteDevEnvironmentRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
    },
)

DeleteDevEnvironmentResponseTypeDef = TypedDict(
    "DeleteDevEnvironmentResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "spaceName": str,
        "name": str,
    },
)

DeleteProjectResponseTypeDef = TypedDict(
    "DeleteProjectResponseTypeDef",
    {
        "spaceName": str,
        "name": str,
        "displayName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSourceRepositoryRequestRequestTypeDef = TypedDict(
    "DeleteSourceRepositoryRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "name": str,
    },
)

DeleteSourceRepositoryResponseTypeDef = TypedDict(
    "DeleteSourceRepositoryResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSpaceRequestRequestTypeDef = TypedDict(
    "DeleteSpaceRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteSpaceResponseTypeDef = TypedDict(
    "DeleteSpaceResponseTypeDef",
    {
        "name": str,
        "displayName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DevEnvironmentAccessDetailsTypeDef = TypedDict(
    "DevEnvironmentAccessDetailsTypeDef",
    {
        "streamUrl": str,
        "tokenValue": str,
    },
)

_RequiredDevEnvironmentRepositorySummaryTypeDef = TypedDict(
    "_RequiredDevEnvironmentRepositorySummaryTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDevEnvironmentRepositorySummaryTypeDef = TypedDict(
    "_OptionalDevEnvironmentRepositorySummaryTypeDef",
    {
        "branchName": str,
    },
    total=False,
)

class DevEnvironmentRepositorySummaryTypeDef(
    _RequiredDevEnvironmentRepositorySummaryTypeDef, _OptionalDevEnvironmentRepositorySummaryTypeDef
):
    pass

_RequiredDevEnvironmentSessionConfigurationTypeDef = TypedDict(
    "_RequiredDevEnvironmentSessionConfigurationTypeDef",
    {
        "sessionType": DevEnvironmentSessionTypeType,
    },
)
_OptionalDevEnvironmentSessionConfigurationTypeDef = TypedDict(
    "_OptionalDevEnvironmentSessionConfigurationTypeDef",
    {
        "executeCommandSessionConfiguration": "ExecuteCommandSessionConfigurationTypeDef",
    },
    total=False,
)

class DevEnvironmentSessionConfigurationTypeDef(
    _RequiredDevEnvironmentSessionConfigurationTypeDef,
    _OptionalDevEnvironmentSessionConfigurationTypeDef,
):
    pass

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

_RequiredDevEnvironmentSummaryTypeDef = TypedDict(
    "_RequiredDevEnvironmentSummaryTypeDef",
    {
        "id": str,
        "lastUpdatedTime": datetime,
        "creatorId": str,
        "status": DevEnvironmentStatusType,
        "repositories": List["DevEnvironmentRepositorySummaryTypeDef"],
        "instanceType": InstanceTypeType,
        "inactivityTimeoutMinutes": int,
        "persistentStorage": "PersistentStorageTypeDef",
    },
)
_OptionalDevEnvironmentSummaryTypeDef = TypedDict(
    "_OptionalDevEnvironmentSummaryTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "statusReason": str,
        "alias": str,
        "ides": List["IdeTypeDef"],
        "vpcConnectionName": str,
    },
    total=False,
)

class DevEnvironmentSummaryTypeDef(
    _RequiredDevEnvironmentSummaryTypeDef, _OptionalDevEnvironmentSummaryTypeDef
):
    pass

EmailAddressTypeDef = TypedDict(
    "EmailAddressTypeDef",
    {
        "email": str,
        "verified": bool,
    },
    total=False,
)

_RequiredEventLogEntryTypeDef = TypedDict(
    "_RequiredEventLogEntryTypeDef",
    {
        "id": str,
        "eventName": str,
        "eventType": str,
        "eventCategory": str,
        "eventSource": str,
        "eventTime": datetime,
        "operationType": OperationTypeType,
        "userIdentity": "UserIdentityTypeDef",
    },
)
_OptionalEventLogEntryTypeDef = TypedDict(
    "_OptionalEventLogEntryTypeDef",
    {
        "projectInformation": "ProjectInformationTypeDef",
        "requestId": str,
        "requestPayload": "EventPayloadTypeDef",
        "responsePayload": "EventPayloadTypeDef",
        "errorCode": str,
        "sourceIpAddress": str,
        "userAgent": str,
    },
    total=False,
)

class EventLogEntryTypeDef(_RequiredEventLogEntryTypeDef, _OptionalEventLogEntryTypeDef):
    pass

EventPayloadTypeDef = TypedDict(
    "EventPayloadTypeDef",
    {
        "contentType": str,
        "data": str,
    },
    total=False,
)

_RequiredExecuteCommandSessionConfigurationTypeDef = TypedDict(
    "_RequiredExecuteCommandSessionConfigurationTypeDef",
    {
        "command": str,
    },
)
_OptionalExecuteCommandSessionConfigurationTypeDef = TypedDict(
    "_OptionalExecuteCommandSessionConfigurationTypeDef",
    {
        "arguments": List[str],
    },
    total=False,
)

class ExecuteCommandSessionConfigurationTypeDef(
    _RequiredExecuteCommandSessionConfigurationTypeDef,
    _OptionalExecuteCommandSessionConfigurationTypeDef,
):
    pass

_RequiredFilterTypeDef = TypedDict(
    "_RequiredFilterTypeDef",
    {
        "key": str,
        "values": List[str],
    },
)
_OptionalFilterTypeDef = TypedDict(
    "_OptionalFilterTypeDef",
    {
        "comparisonOperator": str,
    },
    total=False,
)

class FilterTypeDef(_RequiredFilterTypeDef, _OptionalFilterTypeDef):
    pass

GetDevEnvironmentRequestRequestTypeDef = TypedDict(
    "GetDevEnvironmentRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
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
        "repositories": List["DevEnvironmentRepositorySummaryTypeDef"],
        "alias": str,
        "ides": List["IdeTypeDef"],
        "instanceType": InstanceTypeType,
        "inactivityTimeoutMinutes": int,
        "persistentStorage": "PersistentStorageTypeDef",
        "vpcConnectionName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProjectRequestRequestTypeDef = TypedDict(
    "GetProjectRequestRequestTypeDef",
    {
        "spaceName": str,
        "name": str,
    },
)

GetProjectResponseTypeDef = TypedDict(
    "GetProjectResponseTypeDef",
    {
        "spaceName": str,
        "name": str,
        "displayName": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSourceRepositoryCloneUrlsRequestRequestTypeDef = TypedDict(
    "GetSourceRepositoryCloneUrlsRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "sourceRepositoryName": str,
    },
)

GetSourceRepositoryCloneUrlsResponseTypeDef = TypedDict(
    "GetSourceRepositoryCloneUrlsResponseTypeDef",
    {
        "https": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSourceRepositoryRequestRequestTypeDef = TypedDict(
    "GetSourceRepositoryRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "name": str,
    },
)

GetSourceRepositoryResponseTypeDef = TypedDict(
    "GetSourceRepositoryResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "name": str,
        "description": str,
        "lastUpdatedTime": datetime,
        "createdTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSpaceRequestRequestTypeDef = TypedDict(
    "GetSpaceRequestRequestTypeDef",
    {
        "name": str,
    },
)

GetSpaceResponseTypeDef = TypedDict(
    "GetSpaceResponseTypeDef",
    {
        "name": str,
        "regionName": str,
        "displayName": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSubscriptionRequestRequestTypeDef = TypedDict(
    "GetSubscriptionRequestRequestTypeDef",
    {
        "spaceName": str,
    },
)

GetSubscriptionResponseTypeDef = TypedDict(
    "GetSubscriptionResponseTypeDef",
    {
        "subscriptionType": str,
        "awsAccountName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserDetailsRequestRequestTypeDef = TypedDict(
    "GetUserDetailsRequestRequestTypeDef",
    {
        "id": str,
        "userName": str,
    },
    total=False,
)

GetUserDetailsResponseTypeDef = TypedDict(
    "GetUserDetailsResponseTypeDef",
    {
        "userId": str,
        "userName": str,
        "displayName": str,
        "primaryEmail": "EmailAddressTypeDef",
        "version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkflowRequestRequestTypeDef = TypedDict(
    "GetWorkflowRequestRequestTypeDef",
    {
        "spaceName": str,
        "id": str,
        "projectName": str,
    },
)

GetWorkflowResponseTypeDef = TypedDict(
    "GetWorkflowResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "name": str,
        "sourceRepositoryName": str,
        "sourceBranchName": str,
        "definition": "WorkflowDefinitionTypeDef",
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "runMode": WorkflowRunModeType,
        "status": WorkflowStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkflowRunRequestRequestTypeDef = TypedDict(
    "GetWorkflowRunRequestRequestTypeDef",
    {
        "spaceName": str,
        "id": str,
        "projectName": str,
    },
)

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdeConfigurationTypeDef = TypedDict(
    "IdeConfigurationTypeDef",
    {
        "runtime": str,
        "name": str,
    },
    total=False,
)

IdeTypeDef = TypedDict(
    "IdeTypeDef",
    {
        "runtime": str,
        "name": str,
    },
    total=False,
)

ListAccessTokensRequestRequestTypeDef = TypedDict(
    "ListAccessTokensRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListAccessTokensResponseTypeDef = TypedDict(
    "ListAccessTokensResponseTypeDef",
    {
        "items": List["AccessTokenSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDevEnvironmentSessionsRequestRequestTypeDef = TypedDict(
    "_RequiredListDevEnvironmentSessionsRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "devEnvironmentId": str,
    },
)
_OptionalListDevEnvironmentSessionsRequestRequestTypeDef = TypedDict(
    "_OptionalListDevEnvironmentSessionsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListDevEnvironmentSessionsRequestRequestTypeDef(
    _RequiredListDevEnvironmentSessionsRequestRequestTypeDef,
    _OptionalListDevEnvironmentSessionsRequestRequestTypeDef,
):
    pass

ListDevEnvironmentSessionsResponseTypeDef = TypedDict(
    "ListDevEnvironmentSessionsResponseTypeDef",
    {
        "items": List["DevEnvironmentSessionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDevEnvironmentsRequestRequestTypeDef = TypedDict(
    "_RequiredListDevEnvironmentsRequestRequestTypeDef",
    {
        "spaceName": str,
    },
)
_OptionalListDevEnvironmentsRequestRequestTypeDef = TypedDict(
    "_OptionalListDevEnvironmentsRequestRequestTypeDef",
    {
        "projectName": str,
        "filters": List["FilterTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListDevEnvironmentsRequestRequestTypeDef(
    _RequiredListDevEnvironmentsRequestRequestTypeDef,
    _OptionalListDevEnvironmentsRequestRequestTypeDef,
):
    pass

ListDevEnvironmentsResponseTypeDef = TypedDict(
    "ListDevEnvironmentsResponseTypeDef",
    {
        "items": List["DevEnvironmentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEventLogsRequestRequestTypeDef = TypedDict(
    "_RequiredListEventLogsRequestRequestTypeDef",
    {
        "spaceName": str,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
    },
)
_OptionalListEventLogsRequestRequestTypeDef = TypedDict(
    "_OptionalListEventLogsRequestRequestTypeDef",
    {
        "eventName": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListEventLogsRequestRequestTypeDef(
    _RequiredListEventLogsRequestRequestTypeDef, _OptionalListEventLogsRequestRequestTypeDef
):
    pass

ListEventLogsResponseTypeDef = TypedDict(
    "ListEventLogsResponseTypeDef",
    {
        "nextToken": str,
        "items": List["EventLogEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProjectsRequestRequestTypeDef = TypedDict(
    "_RequiredListProjectsRequestRequestTypeDef",
    {
        "spaceName": str,
    },
)
_OptionalListProjectsRequestRequestTypeDef = TypedDict(
    "_OptionalListProjectsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "filters": List["ProjectListFilterTypeDef"],
    },
    total=False,
)

class ListProjectsRequestRequestTypeDef(
    _RequiredListProjectsRequestRequestTypeDef, _OptionalListProjectsRequestRequestTypeDef
):
    pass

ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "nextToken": str,
        "items": List["ProjectSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSourceRepositoriesItemTypeDef = TypedDict(
    "_RequiredListSourceRepositoriesItemTypeDef",
    {
        "id": str,
        "name": str,
        "lastUpdatedTime": datetime,
        "createdTime": datetime,
    },
)
_OptionalListSourceRepositoriesItemTypeDef = TypedDict(
    "_OptionalListSourceRepositoriesItemTypeDef",
    {
        "description": str,
    },
    total=False,
)

class ListSourceRepositoriesItemTypeDef(
    _RequiredListSourceRepositoriesItemTypeDef, _OptionalListSourceRepositoriesItemTypeDef
):
    pass

_RequiredListSourceRepositoriesRequestRequestTypeDef = TypedDict(
    "_RequiredListSourceRepositoriesRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
    },
)
_OptionalListSourceRepositoriesRequestRequestTypeDef = TypedDict(
    "_OptionalListSourceRepositoriesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListSourceRepositoriesRequestRequestTypeDef(
    _RequiredListSourceRepositoriesRequestRequestTypeDef,
    _OptionalListSourceRepositoriesRequestRequestTypeDef,
):
    pass

ListSourceRepositoriesResponseTypeDef = TypedDict(
    "ListSourceRepositoriesResponseTypeDef",
    {
        "items": List["ListSourceRepositoriesItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSourceRepositoryBranchesItemTypeDef = TypedDict(
    "ListSourceRepositoryBranchesItemTypeDef",
    {
        "ref": str,
        "name": str,
        "lastUpdatedTime": datetime,
        "headCommitId": str,
    },
    total=False,
)

_RequiredListSourceRepositoryBranchesRequestRequestTypeDef = TypedDict(
    "_RequiredListSourceRepositoryBranchesRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "sourceRepositoryName": str,
    },
)
_OptionalListSourceRepositoryBranchesRequestRequestTypeDef = TypedDict(
    "_OptionalListSourceRepositoryBranchesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListSourceRepositoryBranchesRequestRequestTypeDef(
    _RequiredListSourceRepositoryBranchesRequestRequestTypeDef,
    _OptionalListSourceRepositoryBranchesRequestRequestTypeDef,
):
    pass

ListSourceRepositoryBranchesResponseTypeDef = TypedDict(
    "ListSourceRepositoryBranchesResponseTypeDef",
    {
        "nextToken": str,
        "items": List["ListSourceRepositoryBranchesItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSpacesRequestRequestTypeDef = TypedDict(
    "ListSpacesRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

ListSpacesResponseTypeDef = TypedDict(
    "ListSpacesResponseTypeDef",
    {
        "nextToken": str,
        "items": List["SpaceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWorkflowRunsRequestRequestTypeDef = TypedDict(
    "_RequiredListWorkflowRunsRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
    },
)
_OptionalListWorkflowRunsRequestRequestTypeDef = TypedDict(
    "_OptionalListWorkflowRunsRequestRequestTypeDef",
    {
        "workflowId": str,
        "nextToken": str,
        "maxResults": int,
        "sortBy": List[Dict[str, Any]],
    },
    total=False,
)

class ListWorkflowRunsRequestRequestTypeDef(
    _RequiredListWorkflowRunsRequestRequestTypeDef, _OptionalListWorkflowRunsRequestRequestTypeDef
):
    pass

ListWorkflowRunsResponseTypeDef = TypedDict(
    "ListWorkflowRunsResponseTypeDef",
    {
        "nextToken": str,
        "items": List["WorkflowRunSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWorkflowsRequestRequestTypeDef = TypedDict(
    "_RequiredListWorkflowsRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
    },
)
_OptionalListWorkflowsRequestRequestTypeDef = TypedDict(
    "_OptionalListWorkflowsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "sortBy": List[Dict[str, Any]],
    },
    total=False,
)

class ListWorkflowsRequestRequestTypeDef(
    _RequiredListWorkflowsRequestRequestTypeDef, _OptionalListWorkflowsRequestRequestTypeDef
):
    pass

ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "nextToken": str,
        "items": List["WorkflowSummaryTypeDef"],
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

PersistentStorageConfigurationTypeDef = TypedDict(
    "PersistentStorageConfigurationTypeDef",
    {
        "sizeInGiB": int,
    },
)

PersistentStorageTypeDef = TypedDict(
    "PersistentStorageTypeDef",
    {
        "sizeInGiB": int,
    },
)

ProjectInformationTypeDef = TypedDict(
    "ProjectInformationTypeDef",
    {
        "name": str,
        "projectId": str,
    },
    total=False,
)

_RequiredProjectListFilterTypeDef = TypedDict(
    "_RequiredProjectListFilterTypeDef",
    {
        "key": FilterKeyType,
        "values": List[str],
    },
)
_OptionalProjectListFilterTypeDef = TypedDict(
    "_OptionalProjectListFilterTypeDef",
    {
        "comparisonOperator": ComparisonOperatorType,
    },
    total=False,
)

class ProjectListFilterTypeDef(
    _RequiredProjectListFilterTypeDef, _OptionalProjectListFilterTypeDef
):
    pass

_RequiredProjectSummaryTypeDef = TypedDict(
    "_RequiredProjectSummaryTypeDef",
    {
        "name": str,
    },
)
_OptionalProjectSummaryTypeDef = TypedDict(
    "_OptionalProjectSummaryTypeDef",
    {
        "displayName": str,
        "description": str,
    },
    total=False,
)

class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, _OptionalProjectSummaryTypeDef):
    pass

_RequiredRepositoryInputTypeDef = TypedDict(
    "_RequiredRepositoryInputTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalRepositoryInputTypeDef = TypedDict(
    "_OptionalRepositoryInputTypeDef",
    {
        "branchName": str,
    },
    total=False,
)

class RepositoryInputTypeDef(_RequiredRepositoryInputTypeDef, _OptionalRepositoryInputTypeDef):
    pass

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

_RequiredSpaceSummaryTypeDef = TypedDict(
    "_RequiredSpaceSummaryTypeDef",
    {
        "name": str,
        "regionName": str,
    },
)
_OptionalSpaceSummaryTypeDef = TypedDict(
    "_OptionalSpaceSummaryTypeDef",
    {
        "displayName": str,
        "description": str,
    },
    total=False,
)

class SpaceSummaryTypeDef(_RequiredSpaceSummaryTypeDef, _OptionalSpaceSummaryTypeDef):
    pass

_RequiredStartDevEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredStartDevEnvironmentRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
    },
)
_OptionalStartDevEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalStartDevEnvironmentRequestRequestTypeDef",
    {
        "ides": List["IdeConfigurationTypeDef"],
        "instanceType": InstanceTypeType,
        "inactivityTimeoutMinutes": int,
    },
    total=False,
)

class StartDevEnvironmentRequestRequestTypeDef(
    _RequiredStartDevEnvironmentRequestRequestTypeDef,
    _OptionalStartDevEnvironmentRequestRequestTypeDef,
):
    pass

StartDevEnvironmentResponseTypeDef = TypedDict(
    "StartDevEnvironmentResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "status": DevEnvironmentStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDevEnvironmentSessionRequestRequestTypeDef = TypedDict(
    "StartDevEnvironmentSessionRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "sessionConfiguration": "DevEnvironmentSessionConfigurationTypeDef",
    },
)

StartDevEnvironmentSessionResponseTypeDef = TypedDict(
    "StartDevEnvironmentSessionResponseTypeDef",
    {
        "accessDetails": "DevEnvironmentAccessDetailsTypeDef",
        "sessionId": str,
        "spaceName": str,
        "projectName": str,
        "id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartWorkflowRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartWorkflowRunRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "workflowId": str,
    },
)
_OptionalStartWorkflowRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartWorkflowRunRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class StartWorkflowRunRequestRequestTypeDef(
    _RequiredStartWorkflowRunRequestRequestTypeDef, _OptionalStartWorkflowRunRequestRequestTypeDef
):
    pass

StartWorkflowRunResponseTypeDef = TypedDict(
    "StartWorkflowRunResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "workflowId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDevEnvironmentRequestRequestTypeDef = TypedDict(
    "StopDevEnvironmentRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
    },
)

StopDevEnvironmentResponseTypeDef = TypedDict(
    "StopDevEnvironmentResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "status": DevEnvironmentStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDevEnvironmentSessionRequestRequestTypeDef = TypedDict(
    "StopDevEnvironmentSessionRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "sessionId": str,
    },
)

StopDevEnvironmentSessionResponseTypeDef = TypedDict(
    "StopDevEnvironmentSessionResponseTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
        "sessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDevEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDevEnvironmentRequestRequestTypeDef",
    {
        "spaceName": str,
        "projectName": str,
        "id": str,
    },
)
_OptionalUpdateDevEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDevEnvironmentRequestRequestTypeDef",
    {
        "alias": str,
        "ides": List["IdeConfigurationTypeDef"],
        "instanceType": InstanceTypeType,
        "inactivityTimeoutMinutes": int,
        "clientToken": str,
    },
    total=False,
)

class UpdateDevEnvironmentRequestRequestTypeDef(
    _RequiredUpdateDevEnvironmentRequestRequestTypeDef,
    _OptionalUpdateDevEnvironmentRequestRequestTypeDef,
):
    pass

UpdateDevEnvironmentResponseTypeDef = TypedDict(
    "UpdateDevEnvironmentResponseTypeDef",
    {
        "id": str,
        "spaceName": str,
        "projectName": str,
        "alias": str,
        "ides": List["IdeConfigurationTypeDef"],
        "instanceType": InstanceTypeType,
        "inactivityTimeoutMinutes": int,
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectRequestRequestTypeDef",
    {
        "spaceName": str,
        "name": str,
    },
)
_OptionalUpdateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateProjectRequestRequestTypeDef(
    _RequiredUpdateProjectRequestRequestTypeDef, _OptionalUpdateProjectRequestRequestTypeDef
):
    pass

UpdateProjectResponseTypeDef = TypedDict(
    "UpdateProjectResponseTypeDef",
    {
        "spaceName": str,
        "name": str,
        "displayName": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSpaceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSpaceRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateSpaceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSpaceRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateSpaceRequestRequestTypeDef(
    _RequiredUpdateSpaceRequestRequestTypeDef, _OptionalUpdateSpaceRequestRequestTypeDef
):
    pass

UpdateSpaceResponseTypeDef = TypedDict(
    "UpdateSpaceResponseTypeDef",
    {
        "name": str,
        "displayName": str,
        "description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUserIdentityTypeDef = TypedDict(
    "_RequiredUserIdentityTypeDef",
    {
        "userType": UserTypeType,
        "principalId": str,
    },
)
_OptionalUserIdentityTypeDef = TypedDict(
    "_OptionalUserIdentityTypeDef",
    {
        "userName": str,
        "awsAccountId": str,
    },
    total=False,
)

class UserIdentityTypeDef(_RequiredUserIdentityTypeDef, _OptionalUserIdentityTypeDef):
    pass

VerifySessionResponseTypeDef = TypedDict(
    "VerifySessionResponseTypeDef",
    {
        "identity": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WorkflowDefinitionSummaryTypeDef = TypedDict(
    "WorkflowDefinitionSummaryTypeDef",
    {
        "path": str,
    },
)

WorkflowDefinitionTypeDef = TypedDict(
    "WorkflowDefinitionTypeDef",
    {
        "path": str,
    },
)

_RequiredWorkflowRunSummaryTypeDef = TypedDict(
    "_RequiredWorkflowRunSummaryTypeDef",
    {
        "id": str,
        "workflowId": str,
        "workflowName": str,
        "status": WorkflowRunStatusType,
        "startTime": datetime,
        "lastUpdatedTime": datetime,
    },
)
_OptionalWorkflowRunSummaryTypeDef = TypedDict(
    "_OptionalWorkflowRunSummaryTypeDef",
    {
        "statusReasons": List[Dict[str, Any]],
        "endTime": datetime,
    },
    total=False,
)

class WorkflowRunSummaryTypeDef(
    _RequiredWorkflowRunSummaryTypeDef, _OptionalWorkflowRunSummaryTypeDef
):
    pass

WorkflowSummaryTypeDef = TypedDict(
    "WorkflowSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "sourceRepositoryName": str,
        "sourceBranchName": str,
        "definition": "WorkflowDefinitionSummaryTypeDef",
        "createdTime": datetime,
        "lastUpdatedTime": datetime,
        "runMode": WorkflowRunModeType,
        "status": WorkflowStatusType,
    },
)
