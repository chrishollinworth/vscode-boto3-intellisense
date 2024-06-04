"""
Type annotations for appfabric service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appfabric.type_defs import ApiKeyCredentialTypeDef

    data: ApiKeyCredentialTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ApiKeyCredentialTypeDef",
    "AppAuthorizationSummaryTypeDef",
    "AppAuthorizationTypeDef",
    "AppBundleSummaryTypeDef",
    "AppBundleTypeDef",
    "AuditLogDestinationConfigurationTypeDef",
    "AuditLogProcessingConfigurationTypeDef",
    "AuthRequestTypeDef",
    "BatchGetUserAccessTasksRequestRequestTypeDef",
    "BatchGetUserAccessTasksResponseTypeDef",
    "ConnectAppAuthorizationRequestRequestTypeDef",
    "ConnectAppAuthorizationResponseTypeDef",
    "CreateAppAuthorizationRequestRequestTypeDef",
    "CreateAppAuthorizationResponseTypeDef",
    "CreateAppBundleRequestRequestTypeDef",
    "CreateAppBundleResponseTypeDef",
    "CreateIngestionDestinationRequestRequestTypeDef",
    "CreateIngestionDestinationResponseTypeDef",
    "CreateIngestionRequestRequestTypeDef",
    "CreateIngestionResponseTypeDef",
    "CredentialTypeDef",
    "DeleteAppAuthorizationRequestRequestTypeDef",
    "DeleteAppBundleRequestRequestTypeDef",
    "DeleteIngestionDestinationRequestRequestTypeDef",
    "DeleteIngestionRequestRequestTypeDef",
    "DestinationConfigurationTypeDef",
    "DestinationTypeDef",
    "FirehoseStreamTypeDef",
    "GetAppAuthorizationRequestRequestTypeDef",
    "GetAppAuthorizationResponseTypeDef",
    "GetAppBundleRequestRequestTypeDef",
    "GetAppBundleResponseTypeDef",
    "GetIngestionDestinationRequestRequestTypeDef",
    "GetIngestionDestinationResponseTypeDef",
    "GetIngestionRequestRequestTypeDef",
    "GetIngestionResponseTypeDef",
    "IngestionDestinationSummaryTypeDef",
    "IngestionDestinationTypeDef",
    "IngestionSummaryTypeDef",
    "IngestionTypeDef",
    "ListAppAuthorizationsRequestRequestTypeDef",
    "ListAppAuthorizationsResponseTypeDef",
    "ListAppBundlesRequestRequestTypeDef",
    "ListAppBundlesResponseTypeDef",
    "ListIngestionDestinationsRequestRequestTypeDef",
    "ListIngestionDestinationsResponseTypeDef",
    "ListIngestionsRequestRequestTypeDef",
    "ListIngestionsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "Oauth2CredentialTypeDef",
    "PaginatorConfigTypeDef",
    "ProcessingConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "S3BucketTypeDef",
    "StartIngestionRequestRequestTypeDef",
    "StartUserAccessTasksRequestRequestTypeDef",
    "StartUserAccessTasksResponseTypeDef",
    "StopIngestionRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TaskErrorTypeDef",
    "TenantTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAppAuthorizationRequestRequestTypeDef",
    "UpdateAppAuthorizationResponseTypeDef",
    "UpdateIngestionDestinationRequestRequestTypeDef",
    "UpdateIngestionDestinationResponseTypeDef",
    "UserAccessResultItemTypeDef",
    "UserAccessTaskItemTypeDef",
)

ApiKeyCredentialTypeDef = TypedDict(
    "ApiKeyCredentialTypeDef",
    {
        "apiKey": str,
    },
)

AppAuthorizationSummaryTypeDef = TypedDict(
    "AppAuthorizationSummaryTypeDef",
    {
        "appAuthorizationArn": str,
        "appBundleArn": str,
        "app": str,
        "tenant": "TenantTypeDef",
        "status": AppAuthorizationStatusType,
        "updatedAt": datetime,
    },
)

_RequiredAppAuthorizationTypeDef = TypedDict(
    "_RequiredAppAuthorizationTypeDef",
    {
        "appAuthorizationArn": str,
        "appBundleArn": str,
        "app": str,
        "tenant": "TenantTypeDef",
        "authType": AuthTypeType,
        "status": AppAuthorizationStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalAppAuthorizationTypeDef = TypedDict(
    "_OptionalAppAuthorizationTypeDef",
    {
        "persona": PersonaType,
        "authUrl": str,
    },
    total=False,
)

class AppAuthorizationTypeDef(_RequiredAppAuthorizationTypeDef, _OptionalAppAuthorizationTypeDef):
    pass

AppBundleSummaryTypeDef = TypedDict(
    "AppBundleSummaryTypeDef",
    {
        "arn": str,
    },
)

_RequiredAppBundleTypeDef = TypedDict(
    "_RequiredAppBundleTypeDef",
    {
        "arn": str,
    },
)
_OptionalAppBundleTypeDef = TypedDict(
    "_OptionalAppBundleTypeDef",
    {
        "customerManagedKeyArn": str,
    },
    total=False,
)

class AppBundleTypeDef(_RequiredAppBundleTypeDef, _OptionalAppBundleTypeDef):
    pass

AuditLogDestinationConfigurationTypeDef = TypedDict(
    "AuditLogDestinationConfigurationTypeDef",
    {
        "destination": "DestinationTypeDef",
    },
)

AuditLogProcessingConfigurationTypeDef = TypedDict(
    "AuditLogProcessingConfigurationTypeDef",
    {
        "schema": SchemaType,
        "format": FormatType,
    },
)

AuthRequestTypeDef = TypedDict(
    "AuthRequestTypeDef",
    {
        "redirectUri": str,
        "code": str,
    },
)

BatchGetUserAccessTasksRequestRequestTypeDef = TypedDict(
    "BatchGetUserAccessTasksRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "taskIdList": List[str],
    },
)

BatchGetUserAccessTasksResponseTypeDef = TypedDict(
    "BatchGetUserAccessTasksResponseTypeDef",
    {
        "userAccessResultsList": List["UserAccessResultItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredConnectAppAuthorizationRequestRequestTypeDef = TypedDict(
    "_RequiredConnectAppAuthorizationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "appAuthorizationIdentifier": str,
    },
)
_OptionalConnectAppAuthorizationRequestRequestTypeDef = TypedDict(
    "_OptionalConnectAppAuthorizationRequestRequestTypeDef",
    {
        "authRequest": "AuthRequestTypeDef",
    },
    total=False,
)

class ConnectAppAuthorizationRequestRequestTypeDef(
    _RequiredConnectAppAuthorizationRequestRequestTypeDef,
    _OptionalConnectAppAuthorizationRequestRequestTypeDef,
):
    pass

ConnectAppAuthorizationResponseTypeDef = TypedDict(
    "ConnectAppAuthorizationResponseTypeDef",
    {
        "appAuthorizationSummary": "AppAuthorizationSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppAuthorizationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppAuthorizationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "app": str,
        "credential": "CredentialTypeDef",
        "tenant": "TenantTypeDef",
        "authType": AuthTypeType,
    },
)
_OptionalCreateAppAuthorizationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppAuthorizationRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAppAuthorizationRequestRequestTypeDef(
    _RequiredCreateAppAuthorizationRequestRequestTypeDef,
    _OptionalCreateAppAuthorizationRequestRequestTypeDef,
):
    pass

CreateAppAuthorizationResponseTypeDef = TypedDict(
    "CreateAppAuthorizationResponseTypeDef",
    {
        "appAuthorization": "AppAuthorizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAppBundleRequestRequestTypeDef = TypedDict(
    "CreateAppBundleRequestRequestTypeDef",
    {
        "clientToken": str,
        "customerManagedKeyIdentifier": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

CreateAppBundleResponseTypeDef = TypedDict(
    "CreateAppBundleResponseTypeDef",
    {
        "appBundle": "AppBundleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIngestionDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIngestionDestinationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "ingestionIdentifier": str,
        "processingConfiguration": "ProcessingConfigurationTypeDef",
        "destinationConfiguration": "DestinationConfigurationTypeDef",
    },
)
_OptionalCreateIngestionDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIngestionDestinationRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateIngestionDestinationRequestRequestTypeDef(
    _RequiredCreateIngestionDestinationRequestRequestTypeDef,
    _OptionalCreateIngestionDestinationRequestRequestTypeDef,
):
    pass

CreateIngestionDestinationResponseTypeDef = TypedDict(
    "CreateIngestionDestinationResponseTypeDef",
    {
        "ingestionDestination": "IngestionDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIngestionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIngestionRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "app": str,
        "tenantId": str,
        "ingestionType": Literal["auditLog"],
    },
)
_OptionalCreateIngestionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIngestionRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateIngestionRequestRequestTypeDef(
    _RequiredCreateIngestionRequestRequestTypeDef, _OptionalCreateIngestionRequestRequestTypeDef
):
    pass

CreateIngestionResponseTypeDef = TypedDict(
    "CreateIngestionResponseTypeDef",
    {
        "ingestion": "IngestionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialTypeDef = TypedDict(
    "CredentialTypeDef",
    {
        "oauth2Credential": "Oauth2CredentialTypeDef",
        "apiKeyCredential": "ApiKeyCredentialTypeDef",
    },
    total=False,
)

DeleteAppAuthorizationRequestRequestTypeDef = TypedDict(
    "DeleteAppAuthorizationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "appAuthorizationIdentifier": str,
    },
)

DeleteAppBundleRequestRequestTypeDef = TypedDict(
    "DeleteAppBundleRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
    },
)

DeleteIngestionDestinationRequestRequestTypeDef = TypedDict(
    "DeleteIngestionDestinationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "ingestionIdentifier": str,
        "ingestionDestinationIdentifier": str,
    },
)

DeleteIngestionRequestRequestTypeDef = TypedDict(
    "DeleteIngestionRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "ingestionIdentifier": str,
    },
)

DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "auditLog": "AuditLogDestinationConfigurationTypeDef",
    },
    total=False,
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "s3Bucket": "S3BucketTypeDef",
        "firehoseStream": "FirehoseStreamTypeDef",
    },
    total=False,
)

FirehoseStreamTypeDef = TypedDict(
    "FirehoseStreamTypeDef",
    {
        "streamName": str,
    },
)

GetAppAuthorizationRequestRequestTypeDef = TypedDict(
    "GetAppAuthorizationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "appAuthorizationIdentifier": str,
    },
)

GetAppAuthorizationResponseTypeDef = TypedDict(
    "GetAppAuthorizationResponseTypeDef",
    {
        "appAuthorization": "AppAuthorizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppBundleRequestRequestTypeDef = TypedDict(
    "GetAppBundleRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
    },
)

GetAppBundleResponseTypeDef = TypedDict(
    "GetAppBundleResponseTypeDef",
    {
        "appBundle": "AppBundleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIngestionDestinationRequestRequestTypeDef = TypedDict(
    "GetIngestionDestinationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "ingestionIdentifier": str,
        "ingestionDestinationIdentifier": str,
    },
)

GetIngestionDestinationResponseTypeDef = TypedDict(
    "GetIngestionDestinationResponseTypeDef",
    {
        "ingestionDestination": "IngestionDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIngestionRequestRequestTypeDef = TypedDict(
    "GetIngestionRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "ingestionIdentifier": str,
    },
)

GetIngestionResponseTypeDef = TypedDict(
    "GetIngestionResponseTypeDef",
    {
        "ingestion": "IngestionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IngestionDestinationSummaryTypeDef = TypedDict(
    "IngestionDestinationSummaryTypeDef",
    {
        "arn": str,
    },
)

_RequiredIngestionDestinationTypeDef = TypedDict(
    "_RequiredIngestionDestinationTypeDef",
    {
        "arn": str,
        "ingestionArn": str,
        "processingConfiguration": "ProcessingConfigurationTypeDef",
        "destinationConfiguration": "DestinationConfigurationTypeDef",
    },
)
_OptionalIngestionDestinationTypeDef = TypedDict(
    "_OptionalIngestionDestinationTypeDef",
    {
        "status": IngestionDestinationStatusType,
        "statusReason": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)

class IngestionDestinationTypeDef(
    _RequiredIngestionDestinationTypeDef, _OptionalIngestionDestinationTypeDef
):
    pass

IngestionSummaryTypeDef = TypedDict(
    "IngestionSummaryTypeDef",
    {
        "arn": str,
        "app": str,
        "tenantId": str,
        "state": IngestionStateType,
    },
)

IngestionTypeDef = TypedDict(
    "IngestionTypeDef",
    {
        "arn": str,
        "appBundleArn": str,
        "app": str,
        "tenantId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "state": IngestionStateType,
        "ingestionType": Literal["auditLog"],
    },
)

_RequiredListAppAuthorizationsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppAuthorizationsRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
    },
)
_OptionalListAppAuthorizationsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppAuthorizationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAppAuthorizationsRequestRequestTypeDef(
    _RequiredListAppAuthorizationsRequestRequestTypeDef,
    _OptionalListAppAuthorizationsRequestRequestTypeDef,
):
    pass

ListAppAuthorizationsResponseTypeDef = TypedDict(
    "ListAppAuthorizationsResponseTypeDef",
    {
        "appAuthorizationSummaryList": List["AppAuthorizationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppBundlesRequestRequestTypeDef = TypedDict(
    "ListAppBundlesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListAppBundlesResponseTypeDef = TypedDict(
    "ListAppBundlesResponseTypeDef",
    {
        "appBundleSummaryList": List["AppBundleSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIngestionDestinationsRequestRequestTypeDef = TypedDict(
    "_RequiredListIngestionDestinationsRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "ingestionIdentifier": str,
    },
)
_OptionalListIngestionDestinationsRequestRequestTypeDef = TypedDict(
    "_OptionalListIngestionDestinationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListIngestionDestinationsRequestRequestTypeDef(
    _RequiredListIngestionDestinationsRequestRequestTypeDef,
    _OptionalListIngestionDestinationsRequestRequestTypeDef,
):
    pass

ListIngestionDestinationsResponseTypeDef = TypedDict(
    "ListIngestionDestinationsResponseTypeDef",
    {
        "ingestionDestinations": List["IngestionDestinationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIngestionsRequestRequestTypeDef = TypedDict(
    "_RequiredListIngestionsRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
    },
)
_OptionalListIngestionsRequestRequestTypeDef = TypedDict(
    "_OptionalListIngestionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListIngestionsRequestRequestTypeDef(
    _RequiredListIngestionsRequestRequestTypeDef, _OptionalListIngestionsRequestRequestTypeDef
):
    pass

ListIngestionsResponseTypeDef = TypedDict(
    "ListIngestionsResponseTypeDef",
    {
        "ingestions": List["IngestionSummaryTypeDef"],
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
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

Oauth2CredentialTypeDef = TypedDict(
    "Oauth2CredentialTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
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

ProcessingConfigurationTypeDef = TypedDict(
    "ProcessingConfigurationTypeDef",
    {
        "auditLog": "AuditLogProcessingConfigurationTypeDef",
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

_RequiredS3BucketTypeDef = TypedDict(
    "_RequiredS3BucketTypeDef",
    {
        "bucketName": str,
    },
)
_OptionalS3BucketTypeDef = TypedDict(
    "_OptionalS3BucketTypeDef",
    {
        "prefix": str,
    },
    total=False,
)

class S3BucketTypeDef(_RequiredS3BucketTypeDef, _OptionalS3BucketTypeDef):
    pass

StartIngestionRequestRequestTypeDef = TypedDict(
    "StartIngestionRequestRequestTypeDef",
    {
        "ingestionIdentifier": str,
        "appBundleIdentifier": str,
    },
)

StartUserAccessTasksRequestRequestTypeDef = TypedDict(
    "StartUserAccessTasksRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "email": str,
    },
)

StartUserAccessTasksResponseTypeDef = TypedDict(
    "StartUserAccessTasksResponseTypeDef",
    {
        "userAccessTasksList": List["UserAccessTaskItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopIngestionRequestRequestTypeDef = TypedDict(
    "StopIngestionRequestRequestTypeDef",
    {
        "ingestionIdentifier": str,
        "appBundleIdentifier": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TaskErrorTypeDef = TypedDict(
    "TaskErrorTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
    },
    total=False,
)

TenantTypeDef = TypedDict(
    "TenantTypeDef",
    {
        "tenantIdentifier": str,
        "tenantDisplayName": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAppAuthorizationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAppAuthorizationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "appAuthorizationIdentifier": str,
    },
)
_OptionalUpdateAppAuthorizationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAppAuthorizationRequestRequestTypeDef",
    {
        "credential": "CredentialTypeDef",
        "tenant": "TenantTypeDef",
    },
    total=False,
)

class UpdateAppAuthorizationRequestRequestTypeDef(
    _RequiredUpdateAppAuthorizationRequestRequestTypeDef,
    _OptionalUpdateAppAuthorizationRequestRequestTypeDef,
):
    pass

UpdateAppAuthorizationResponseTypeDef = TypedDict(
    "UpdateAppAuthorizationResponseTypeDef",
    {
        "appAuthorization": "AppAuthorizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIngestionDestinationRequestRequestTypeDef = TypedDict(
    "UpdateIngestionDestinationRequestRequestTypeDef",
    {
        "appBundleIdentifier": str,
        "ingestionIdentifier": str,
        "ingestionDestinationIdentifier": str,
        "destinationConfiguration": "DestinationConfigurationTypeDef",
    },
)

UpdateIngestionDestinationResponseTypeDef = TypedDict(
    "UpdateIngestionDestinationResponseTypeDef",
    {
        "ingestionDestination": "IngestionDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserAccessResultItemTypeDef = TypedDict(
    "UserAccessResultItemTypeDef",
    {
        "app": str,
        "tenantId": str,
        "tenantDisplayName": str,
        "taskId": str,
        "resultStatus": ResultStatusType,
        "email": str,
        "userId": str,
        "userFullName": str,
        "userFirstName": str,
        "userLastName": str,
        "userStatus": str,
        "taskError": "TaskErrorTypeDef",
    },
    total=False,
)

_RequiredUserAccessTaskItemTypeDef = TypedDict(
    "_RequiredUserAccessTaskItemTypeDef",
    {
        "app": str,
        "tenantId": str,
    },
)
_OptionalUserAccessTaskItemTypeDef = TypedDict(
    "_OptionalUserAccessTaskItemTypeDef",
    {
        "taskId": str,
        "error": "TaskErrorTypeDef",
    },
    total=False,
)

class UserAccessTaskItemTypeDef(
    _RequiredUserAccessTaskItemTypeDef, _OptionalUserAccessTaskItemTypeDef
):
    pass
