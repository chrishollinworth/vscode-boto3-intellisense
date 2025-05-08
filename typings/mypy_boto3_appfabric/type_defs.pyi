"""
Type annotations for appfabric service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appfabric/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_appfabric.type_defs import ApiKeyCredentialTypeDef

    data: ApiKeyCredentialTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    AppAuthorizationStatusType,
    AuthTypeType,
    FormatType,
    IngestionDestinationStatusType,
    IngestionStateType,
    PersonaType,
    ResultStatusType,
    SchemaType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ApiKeyCredentialTypeDef",
    "AppAuthorizationSummaryTypeDef",
    "AppAuthorizationTypeDef",
    "AppBundleSummaryTypeDef",
    "AppBundleTypeDef",
    "AuditLogDestinationConfigurationTypeDef",
    "AuditLogProcessingConfigurationTypeDef",
    "AuthRequestTypeDef",
    "BatchGetUserAccessTasksRequestTypeDef",
    "BatchGetUserAccessTasksResponseTypeDef",
    "ConnectAppAuthorizationRequestTypeDef",
    "ConnectAppAuthorizationResponseTypeDef",
    "CreateAppAuthorizationRequestTypeDef",
    "CreateAppAuthorizationResponseTypeDef",
    "CreateAppBundleRequestTypeDef",
    "CreateAppBundleResponseTypeDef",
    "CreateIngestionDestinationRequestTypeDef",
    "CreateIngestionDestinationResponseTypeDef",
    "CreateIngestionRequestTypeDef",
    "CreateIngestionResponseTypeDef",
    "CredentialTypeDef",
    "DeleteAppAuthorizationRequestTypeDef",
    "DeleteAppBundleRequestTypeDef",
    "DeleteIngestionDestinationRequestTypeDef",
    "DeleteIngestionRequestTypeDef",
    "DestinationConfigurationTypeDef",
    "DestinationTypeDef",
    "FirehoseStreamTypeDef",
    "GetAppAuthorizationRequestTypeDef",
    "GetAppAuthorizationResponseTypeDef",
    "GetAppBundleRequestTypeDef",
    "GetAppBundleResponseTypeDef",
    "GetIngestionDestinationRequestTypeDef",
    "GetIngestionDestinationResponseTypeDef",
    "GetIngestionRequestTypeDef",
    "GetIngestionResponseTypeDef",
    "IngestionDestinationSummaryTypeDef",
    "IngestionDestinationTypeDef",
    "IngestionSummaryTypeDef",
    "IngestionTypeDef",
    "ListAppAuthorizationsRequestPaginateTypeDef",
    "ListAppAuthorizationsRequestTypeDef",
    "ListAppAuthorizationsResponseTypeDef",
    "ListAppBundlesRequestPaginateTypeDef",
    "ListAppBundlesRequestTypeDef",
    "ListAppBundlesResponseTypeDef",
    "ListIngestionDestinationsRequestPaginateTypeDef",
    "ListIngestionDestinationsRequestTypeDef",
    "ListIngestionDestinationsResponseTypeDef",
    "ListIngestionsRequestPaginateTypeDef",
    "ListIngestionsRequestTypeDef",
    "ListIngestionsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "Oauth2CredentialTypeDef",
    "PaginatorConfigTypeDef",
    "ProcessingConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "S3BucketTypeDef",
    "StartIngestionRequestTypeDef",
    "StartUserAccessTasksRequestTypeDef",
    "StartUserAccessTasksResponseTypeDef",
    "StopIngestionRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TaskErrorTypeDef",
    "TenantTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAppAuthorizationRequestTypeDef",
    "UpdateAppAuthorizationResponseTypeDef",
    "UpdateIngestionDestinationRequestTypeDef",
    "UpdateIngestionDestinationResponseTypeDef",
    "UserAccessResultItemTypeDef",
    "UserAccessTaskItemTypeDef",
)

class ApiKeyCredentialTypeDef(TypedDict):
    apiKey: str

class TenantTypeDef(TypedDict):
    tenantIdentifier: str
    tenantDisplayName: str

class AppBundleSummaryTypeDef(TypedDict):
    arn: str

class AppBundleTypeDef(TypedDict):
    arn: str
    customerManagedKeyArn: NotRequired[str]

AuditLogProcessingConfigurationTypeDef = TypedDict(
    "AuditLogProcessingConfigurationTypeDef",
    {
        "schema": SchemaType,
        "format": FormatType,
    },
)

class AuthRequestTypeDef(TypedDict):
    redirectUri: str
    code: str

class BatchGetUserAccessTasksRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    taskIdList: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class TagTypeDef(TypedDict):
    key: str
    value: str

class IngestionTypeDef(TypedDict):
    arn: str
    appBundleArn: str
    app: str
    tenantId: str
    createdAt: datetime
    updatedAt: datetime
    state: IngestionStateType
    ingestionType: Literal["auditLog"]

class Oauth2CredentialTypeDef(TypedDict):
    clientId: str
    clientSecret: str

class DeleteAppAuthorizationRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str

class DeleteAppBundleRequestTypeDef(TypedDict):
    appBundleIdentifier: str

class DeleteIngestionDestinationRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    ingestionIdentifier: str
    ingestionDestinationIdentifier: str

class DeleteIngestionRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    ingestionIdentifier: str

class FirehoseStreamTypeDef(TypedDict):
    streamName: str

class S3BucketTypeDef(TypedDict):
    bucketName: str
    prefix: NotRequired[str]

class GetAppAuthorizationRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str

class GetAppBundleRequestTypeDef(TypedDict):
    appBundleIdentifier: str

class GetIngestionDestinationRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    ingestionIdentifier: str
    ingestionDestinationIdentifier: str

class GetIngestionRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    ingestionIdentifier: str

class IngestionDestinationSummaryTypeDef(TypedDict):
    arn: str

class IngestionSummaryTypeDef(TypedDict):
    arn: str
    app: str
    tenantId: str
    state: IngestionStateType

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAppAuthorizationsRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAppBundlesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListIngestionDestinationsRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    ingestionIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListIngestionsRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class StartIngestionRequestTypeDef(TypedDict):
    ingestionIdentifier: str
    appBundleIdentifier: str

class StartUserAccessTasksRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    email: str

class StopIngestionRequestTypeDef(TypedDict):
    ingestionIdentifier: str
    appBundleIdentifier: str

class TaskErrorTypeDef(TypedDict):
    errorCode: NotRequired[str]
    errorMessage: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class AppAuthorizationSummaryTypeDef(TypedDict):
    appAuthorizationArn: str
    appBundleArn: str
    app: str
    tenant: TenantTypeDef
    status: AppAuthorizationStatusType
    updatedAt: datetime

class AppAuthorizationTypeDef(TypedDict):
    appAuthorizationArn: str
    appBundleArn: str
    app: str
    tenant: TenantTypeDef
    authType: AuthTypeType
    status: AppAuthorizationStatusType
    createdAt: datetime
    updatedAt: datetime
    persona: NotRequired[PersonaType]
    authUrl: NotRequired[str]

class ProcessingConfigurationTypeDef(TypedDict):
    auditLog: NotRequired[AuditLogProcessingConfigurationTypeDef]

class ConnectAppAuthorizationRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str
    authRequest: NotRequired[AuthRequestTypeDef]

class CreateAppBundleResponseTypeDef(TypedDict):
    appBundle: AppBundleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppBundleResponseTypeDef(TypedDict):
    appBundle: AppBundleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppBundlesResponseTypeDef(TypedDict):
    appBundleSummaryList: List[AppBundleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateAppBundleRequestTypeDef(TypedDict):
    clientToken: NotRequired[str]
    customerManagedKeyIdentifier: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateIngestionRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    app: str
    tenantId: str
    ingestionType: Literal["auditLog"]
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateIngestionResponseTypeDef(TypedDict):
    ingestion: IngestionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIngestionResponseTypeDef(TypedDict):
    ingestion: IngestionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CredentialTypeDef(TypedDict):
    oauth2Credential: NotRequired[Oauth2CredentialTypeDef]
    apiKeyCredential: NotRequired[ApiKeyCredentialTypeDef]

class DestinationTypeDef(TypedDict):
    s3Bucket: NotRequired[S3BucketTypeDef]
    firehoseStream: NotRequired[FirehoseStreamTypeDef]

class ListIngestionDestinationsResponseTypeDef(TypedDict):
    ingestionDestinations: List[IngestionDestinationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListIngestionsResponseTypeDef(TypedDict):
    ingestions: List[IngestionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAppAuthorizationsRequestPaginateTypeDef(TypedDict):
    appBundleIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAppBundlesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIngestionDestinationsRequestPaginateTypeDef(TypedDict):
    appBundleIdentifier: str
    ingestionIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIngestionsRequestPaginateTypeDef(TypedDict):
    appBundleIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class UserAccessResultItemTypeDef(TypedDict):
    app: NotRequired[str]
    tenantId: NotRequired[str]
    tenantDisplayName: NotRequired[str]
    taskId: NotRequired[str]
    resultStatus: NotRequired[ResultStatusType]
    email: NotRequired[str]
    userId: NotRequired[str]
    userFullName: NotRequired[str]
    userFirstName: NotRequired[str]
    userLastName: NotRequired[str]
    userStatus: NotRequired[str]
    taskError: NotRequired[TaskErrorTypeDef]

class UserAccessTaskItemTypeDef(TypedDict):
    app: str
    tenantId: str
    taskId: NotRequired[str]
    error: NotRequired[TaskErrorTypeDef]

class ConnectAppAuthorizationResponseTypeDef(TypedDict):
    appAuthorizationSummary: AppAuthorizationSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppAuthorizationsResponseTypeDef(TypedDict):
    appAuthorizationSummaryList: List[AppAuthorizationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateAppAuthorizationResponseTypeDef(TypedDict):
    appAuthorization: AppAuthorizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppAuthorizationResponseTypeDef(TypedDict):
    appAuthorization: AppAuthorizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppAuthorizationResponseTypeDef(TypedDict):
    appAuthorization: AppAuthorizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppAuthorizationRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    app: str
    credential: CredentialTypeDef
    tenant: TenantTypeDef
    authType: AuthTypeType
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class UpdateAppAuthorizationRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    appAuthorizationIdentifier: str
    credential: NotRequired[CredentialTypeDef]
    tenant: NotRequired[TenantTypeDef]

class AuditLogDestinationConfigurationTypeDef(TypedDict):
    destination: DestinationTypeDef

class BatchGetUserAccessTasksResponseTypeDef(TypedDict):
    userAccessResultsList: List[UserAccessResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartUserAccessTasksResponseTypeDef(TypedDict):
    userAccessTasksList: List[UserAccessTaskItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationConfigurationTypeDef(TypedDict):
    auditLog: NotRequired[AuditLogDestinationConfigurationTypeDef]

class CreateIngestionDestinationRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    ingestionIdentifier: str
    processingConfiguration: ProcessingConfigurationTypeDef
    destinationConfiguration: DestinationConfigurationTypeDef
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class IngestionDestinationTypeDef(TypedDict):
    arn: str
    ingestionArn: str
    processingConfiguration: ProcessingConfigurationTypeDef
    destinationConfiguration: DestinationConfigurationTypeDef
    status: NotRequired[IngestionDestinationStatusType]
    statusReason: NotRequired[str]
    createdAt: NotRequired[datetime]
    updatedAt: NotRequired[datetime]

class UpdateIngestionDestinationRequestTypeDef(TypedDict):
    appBundleIdentifier: str
    ingestionIdentifier: str
    ingestionDestinationIdentifier: str
    destinationConfiguration: DestinationConfigurationTypeDef

class CreateIngestionDestinationResponseTypeDef(TypedDict):
    ingestionDestination: IngestionDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIngestionDestinationResponseTypeDef(TypedDict):
    ingestionDestination: IngestionDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIngestionDestinationResponseTypeDef(TypedDict):
    ingestionDestination: IngestionDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
