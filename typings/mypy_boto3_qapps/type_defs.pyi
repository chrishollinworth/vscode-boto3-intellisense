"""
Type annotations for qapps service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_qapps.type_defs import AssociateLibraryItemReviewInputTypeDef

    data: AssociateLibraryItemReviewInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AppRequiredCapabilityType,
    AppStatusType,
    CardOutputSourceType,
    CardTypeType,
    DocumentScopeType,
    ExecutionStatusType,
    InputCardComputeModeType,
    LibraryItemStatusType,
    PermissionInputActionEnumType,
    PermissionOutputActionEnumType,
    PluginTypeType,
    PrincipalOutputUserTypeEnumType,
    SenderType,
    SubmissionMutationKindType,
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
    "AppDefinitionInputOutputTypeDef",
    "AppDefinitionInputTypeDef",
    "AppDefinitionInputUnionTypeDef",
    "AppDefinitionTypeDef",
    "AssociateLibraryItemReviewInputTypeDef",
    "AssociateQAppWithUserInputTypeDef",
    "AttributeFilterOutputTypeDef",
    "AttributeFilterTypeDef",
    "BatchCreateCategoryInputCategoryTypeDef",
    "BatchCreateCategoryInputTypeDef",
    "BatchDeleteCategoryInputTypeDef",
    "BatchUpdateCategoryInputTypeDef",
    "CardInputOutputTypeDef",
    "CardInputTypeDef",
    "CardStatusTypeDef",
    "CardTypeDef",
    "CardValueTypeDef",
    "CategoryInputTypeDef",
    "CategoryTypeDef",
    "ConversationMessageTypeDef",
    "CreateLibraryItemInputTypeDef",
    "CreateLibraryItemOutputTypeDef",
    "CreatePresignedUrlInputTypeDef",
    "CreatePresignedUrlOutputTypeDef",
    "CreateQAppInputTypeDef",
    "CreateQAppOutputTypeDef",
    "DeleteLibraryItemInputTypeDef",
    "DeleteQAppInputTypeDef",
    "DescribeQAppPermissionsInputTypeDef",
    "DescribeQAppPermissionsOutputTypeDef",
    "DisassociateLibraryItemReviewInputTypeDef",
    "DisassociateQAppFromUserInputTypeDef",
    "DocumentAttributeOutputTypeDef",
    "DocumentAttributeTypeDef",
    "DocumentAttributeValueOutputTypeDef",
    "DocumentAttributeValueTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportQAppSessionDataInputTypeDef",
    "ExportQAppSessionDataOutputTypeDef",
    "FileUploadCardInputTypeDef",
    "FileUploadCardTypeDef",
    "FormInputCardInputOutputTypeDef",
    "FormInputCardInputTypeDef",
    "FormInputCardMetadataOutputTypeDef",
    "FormInputCardMetadataTypeDef",
    "FormInputCardTypeDef",
    "GetLibraryItemInputTypeDef",
    "GetLibraryItemOutputTypeDef",
    "GetQAppInputTypeDef",
    "GetQAppOutputTypeDef",
    "GetQAppSessionInputTypeDef",
    "GetQAppSessionMetadataInputTypeDef",
    "GetQAppSessionMetadataOutputTypeDef",
    "GetQAppSessionOutputTypeDef",
    "ImportDocumentInputTypeDef",
    "ImportDocumentOutputTypeDef",
    "LibraryItemMemberTypeDef",
    "ListCategoriesInputTypeDef",
    "ListCategoriesOutputTypeDef",
    "ListLibraryItemsInputPaginateTypeDef",
    "ListLibraryItemsInputTypeDef",
    "ListLibraryItemsOutputTypeDef",
    "ListQAppSessionDataInputTypeDef",
    "ListQAppSessionDataOutputTypeDef",
    "ListQAppsInputPaginateTypeDef",
    "ListQAppsInputTypeDef",
    "ListQAppsOutputTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionInputTypeDef",
    "PermissionOutputTypeDef",
    "PredictAppDefinitionTypeDef",
    "PredictQAppInputOptionsTypeDef",
    "PredictQAppInputTypeDef",
    "PredictQAppOutputTypeDef",
    "PrincipalOutputTypeDef",
    "QAppSessionDataTypeDef",
    "QPluginCardInputTypeDef",
    "QPluginCardTypeDef",
    "QQueryCardInputOutputTypeDef",
    "QQueryCardInputTypeDef",
    "QQueryCardTypeDef",
    "ResponseMetadataTypeDef",
    "SessionSharingConfigurationTypeDef",
    "StartQAppSessionInputTypeDef",
    "StartQAppSessionOutputTypeDef",
    "StopQAppSessionInputTypeDef",
    "SubmissionMutationTypeDef",
    "SubmissionTypeDef",
    "TagResourceRequestTypeDef",
    "TextInputCardInputTypeDef",
    "TextInputCardTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateLibraryItemInputTypeDef",
    "UpdateLibraryItemMetadataInputTypeDef",
    "UpdateLibraryItemOutputTypeDef",
    "UpdateQAppInputTypeDef",
    "UpdateQAppOutputTypeDef",
    "UpdateQAppPermissionsInputTypeDef",
    "UpdateQAppPermissionsOutputTypeDef",
    "UpdateQAppSessionInputTypeDef",
    "UpdateQAppSessionMetadataInputTypeDef",
    "UpdateQAppSessionMetadataOutputTypeDef",
    "UpdateQAppSessionOutputTypeDef",
    "UserAppItemTypeDef",
    "UserTypeDef",
)

class AssociateLibraryItemReviewInputTypeDef(TypedDict):
    instanceId: str
    libraryItemId: str

class AssociateQAppWithUserInputTypeDef(TypedDict):
    instanceId: str
    appId: str

BatchCreateCategoryInputCategoryTypeDef = TypedDict(
    "BatchCreateCategoryInputCategoryTypeDef",
    {
        "title": str,
        "id": NotRequired[str],
        "color": NotRequired[str],
    },
)

class BatchDeleteCategoryInputTypeDef(TypedDict):
    instanceId: str
    categories: Sequence[str]

CategoryInputTypeDef = TypedDict(
    "CategoryInputTypeDef",
    {
        "id": str,
        "title": str,
        "color": NotRequired[str],
    },
)
FileUploadCardInputTypeDef = TypedDict(
    "FileUploadCardInputTypeDef",
    {
        "title": str,
        "id": str,
        "type": CardTypeType,
        "filename": NotRequired[str],
        "fileId": NotRequired[str],
        "allowOverride": NotRequired[bool],
    },
)
QPluginCardInputTypeDef = TypedDict(
    "QPluginCardInputTypeDef",
    {
        "title": str,
        "id": str,
        "type": CardTypeType,
        "prompt": str,
        "pluginId": str,
        "actionIdentifier": NotRequired[str],
    },
)
TextInputCardInputTypeDef = TypedDict(
    "TextInputCardInputTypeDef",
    {
        "title": str,
        "id": str,
        "type": CardTypeType,
        "placeholder": NotRequired[str],
        "defaultValue": NotRequired[str],
    },
)

class SubmissionTypeDef(TypedDict):
    value: NotRequired[Dict[str, Any]]
    submissionId: NotRequired[str]
    timestamp: NotRequired[datetime]

FileUploadCardTypeDef = TypedDict(
    "FileUploadCardTypeDef",
    {
        "id": str,
        "title": str,
        "dependencies": List[str],
        "type": CardTypeType,
        "filename": NotRequired[str],
        "fileId": NotRequired[str],
        "allowOverride": NotRequired[bool],
    },
)
QPluginCardTypeDef = TypedDict(
    "QPluginCardTypeDef",
    {
        "id": str,
        "title": str,
        "dependencies": List[str],
        "type": CardTypeType,
        "prompt": str,
        "pluginType": PluginTypeType,
        "pluginId": str,
        "actionIdentifier": NotRequired[str],
    },
)
TextInputCardTypeDef = TypedDict(
    "TextInputCardTypeDef",
    {
        "id": str,
        "title": str,
        "dependencies": List[str],
        "type": CardTypeType,
        "placeholder": NotRequired[str],
        "defaultValue": NotRequired[str],
    },
)

class SubmissionMutationTypeDef(TypedDict):
    submissionId: str
    mutationType: SubmissionMutationKindType

CategoryTypeDef = TypedDict(
    "CategoryTypeDef",
    {
        "id": str,
        "title": str,
        "color": NotRequired[str],
        "appCount": NotRequired[int],
    },
)
ConversationMessageTypeDef = TypedDict(
    "ConversationMessageTypeDef",
    {
        "body": str,
        "type": SenderType,
    },
)

class CreateLibraryItemInputTypeDef(TypedDict):
    instanceId: str
    appId: str
    appVersion: int
    categories: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreatePresignedUrlInputTypeDef(TypedDict):
    instanceId: str
    cardId: str
    appId: str
    fileContentsSha256: str
    fileName: str
    scope: DocumentScopeType
    sessionId: NotRequired[str]

class DeleteLibraryItemInputTypeDef(TypedDict):
    instanceId: str
    libraryItemId: str

class DeleteQAppInputTypeDef(TypedDict):
    instanceId: str
    appId: str

class DescribeQAppPermissionsInputTypeDef(TypedDict):
    instanceId: str
    appId: str

class DisassociateLibraryItemReviewInputTypeDef(TypedDict):
    instanceId: str
    libraryItemId: str

class DisassociateQAppFromUserInputTypeDef(TypedDict):
    instanceId: str
    appId: str

class DocumentAttributeValueOutputTypeDef(TypedDict):
    stringValue: NotRequired[str]
    stringListValue: NotRequired[List[str]]
    longValue: NotRequired[int]
    dateValue: NotRequired[datetime]

TimestampTypeDef = Union[datetime, str]

class ExportQAppSessionDataInputTypeDef(TypedDict):
    instanceId: str
    sessionId: str

class FormInputCardMetadataOutputTypeDef(TypedDict):
    schema: Dict[str, Any]

class FormInputCardMetadataTypeDef(TypedDict):
    schema: Mapping[str, Any]

class GetLibraryItemInputTypeDef(TypedDict):
    instanceId: str
    libraryItemId: str
    appId: NotRequired[str]

class GetQAppInputTypeDef(TypedDict):
    instanceId: str
    appId: str
    appVersion: NotRequired[int]

class GetQAppSessionInputTypeDef(TypedDict):
    instanceId: str
    sessionId: str

class GetQAppSessionMetadataInputTypeDef(TypedDict):
    instanceId: str
    sessionId: str

class SessionSharingConfigurationTypeDef(TypedDict):
    enabled: bool
    acceptResponses: NotRequired[bool]
    revealCards: NotRequired[bool]

class ImportDocumentInputTypeDef(TypedDict):
    instanceId: str
    cardId: str
    appId: str
    fileContentsBase64: str
    fileName: str
    scope: DocumentScopeType
    sessionId: NotRequired[str]

class ListCategoriesInputTypeDef(TypedDict):
    instanceId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListLibraryItemsInputTypeDef(TypedDict):
    instanceId: str
    limit: NotRequired[int]
    nextToken: NotRequired[str]
    categoryId: NotRequired[str]

class ListQAppSessionDataInputTypeDef(TypedDict):
    instanceId: str
    sessionId: str

class ListQAppsInputTypeDef(TypedDict):
    instanceId: str
    limit: NotRequired[int]
    nextToken: NotRequired[str]

class UserAppItemTypeDef(TypedDict):
    appId: str
    appArn: str
    title: str
    createdAt: datetime
    description: NotRequired[str]
    canEdit: NotRequired[bool]
    status: NotRequired[str]
    isVerified: NotRequired[bool]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceARN: str

class PermissionInputTypeDef(TypedDict):
    action: PermissionInputActionEnumType
    principal: str

class PrincipalOutputTypeDef(TypedDict):
    userId: NotRequired[str]
    userType: NotRequired[PrincipalOutputUserTypeEnumType]
    email: NotRequired[str]

class UserTypeDef(TypedDict):
    userId: NotRequired[str]

class StopQAppSessionInputTypeDef(TypedDict):
    instanceId: str
    sessionId: str

class TagResourceRequestTypeDef(TypedDict):
    resourceARN: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceARN: str
    tagKeys: Sequence[str]

class UpdateLibraryItemInputTypeDef(TypedDict):
    instanceId: str
    libraryItemId: str
    status: NotRequired[LibraryItemStatusType]
    categories: NotRequired[Sequence[str]]

class UpdateLibraryItemMetadataInputTypeDef(TypedDict):
    instanceId: str
    libraryItemId: str
    isVerified: NotRequired[bool]

class BatchCreateCategoryInputTypeDef(TypedDict):
    instanceId: str
    categories: Sequence[BatchCreateCategoryInputCategoryTypeDef]

class BatchUpdateCategoryInputTypeDef(TypedDict):
    instanceId: str
    categories: Sequence[CategoryInputTypeDef]

class CardStatusTypeDef(TypedDict):
    currentState: ExecutionStatusType
    currentValue: str
    submissions: NotRequired[List[SubmissionTypeDef]]

class CardValueTypeDef(TypedDict):
    cardId: str
    value: str
    submissionMutation: NotRequired[SubmissionMutationTypeDef]

class LibraryItemMemberTypeDef(TypedDict):
    libraryItemId: str
    appId: str
    appVersion: int
    categories: List[CategoryTypeDef]
    status: str
    createdAt: datetime
    createdBy: str
    ratingCount: int
    updatedAt: NotRequired[datetime]
    updatedBy: NotRequired[str]
    isRatedByUser: NotRequired[bool]
    userCount: NotRequired[int]
    isVerified: NotRequired[bool]

class PredictQAppInputOptionsTypeDef(TypedDict):
    conversation: NotRequired[Sequence[ConversationMessageTypeDef]]
    problemStatement: NotRequired[str]

class CreateLibraryItemOutputTypeDef(TypedDict):
    libraryItemId: str
    status: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ratingCount: int
    isVerified: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePresignedUrlOutputTypeDef(TypedDict):
    fileId: str
    presignedUrl: str
    presignedUrlFields: Dict[str, str]
    presignedUrlExpiration: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQAppOutputTypeDef(TypedDict):
    appId: str
    appArn: str
    title: str
    description: str
    initialPrompt: str
    appVersion: int
    status: AppStatusType
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    requiredCapabilities: List[AppRequiredCapabilityType]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ExportQAppSessionDataOutputTypeDef(TypedDict):
    csvFileLink: str
    expiresAt: datetime
    sessionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLibraryItemOutputTypeDef(TypedDict):
    libraryItemId: str
    appId: str
    appVersion: int
    categories: List[CategoryTypeDef]
    status: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ratingCount: int
    isRatedByUser: bool
    userCount: int
    isVerified: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ImportDocumentOutputTypeDef(TypedDict):
    fileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCategoriesOutputTypeDef(TypedDict):
    categories: List[CategoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartQAppSessionOutputTypeDef(TypedDict):
    sessionId: str
    sessionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLibraryItemOutputTypeDef(TypedDict):
    libraryItemId: str
    appId: str
    appVersion: int
    categories: List[CategoryTypeDef]
    status: str
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    ratingCount: int
    isRatedByUser: bool
    userCount: int
    isVerified: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateQAppOutputTypeDef(TypedDict):
    appId: str
    appArn: str
    title: str
    description: str
    initialPrompt: str
    appVersion: int
    status: AppStatusType
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    requiredCapabilities: List[AppRequiredCapabilityType]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateQAppSessionOutputTypeDef(TypedDict):
    sessionId: str
    sessionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentAttributeOutputTypeDef(TypedDict):
    name: str
    value: DocumentAttributeValueOutputTypeDef

class DocumentAttributeValueTypeDef(TypedDict):
    stringValue: NotRequired[str]
    stringListValue: NotRequired[Sequence[str]]
    longValue: NotRequired[int]
    dateValue: NotRequired[TimestampTypeDef]

FormInputCardInputOutputTypeDef = TypedDict(
    "FormInputCardInputOutputTypeDef",
    {
        "title": str,
        "id": str,
        "type": CardTypeType,
        "metadata": FormInputCardMetadataOutputTypeDef,
        "computeMode": NotRequired[InputCardComputeModeType],
    },
)
FormInputCardTypeDef = TypedDict(
    "FormInputCardTypeDef",
    {
        "id": str,
        "title": str,
        "dependencies": List[str],
        "type": CardTypeType,
        "metadata": FormInputCardMetadataOutputTypeDef,
        "computeMode": NotRequired[InputCardComputeModeType],
    },
)
FormInputCardInputTypeDef = TypedDict(
    "FormInputCardInputTypeDef",
    {
        "title": str,
        "id": str,
        "type": CardTypeType,
        "metadata": FormInputCardMetadataTypeDef,
        "computeMode": NotRequired[InputCardComputeModeType],
    },
)

class GetQAppSessionMetadataOutputTypeDef(TypedDict):
    sessionId: str
    sessionArn: str
    sessionName: str
    sharingConfiguration: SessionSharingConfigurationTypeDef
    sessionOwner: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateQAppSessionMetadataInputTypeDef(TypedDict):
    instanceId: str
    sessionId: str
    sharingConfiguration: SessionSharingConfigurationTypeDef
    sessionName: NotRequired[str]

class UpdateQAppSessionMetadataOutputTypeDef(TypedDict):
    sessionId: str
    sessionArn: str
    sessionName: str
    sharingConfiguration: SessionSharingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLibraryItemsInputPaginateTypeDef(TypedDict):
    instanceId: str
    categoryId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQAppsInputPaginateTypeDef(TypedDict):
    instanceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQAppsOutputTypeDef(TypedDict):
    apps: List[UserAppItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateQAppPermissionsInputTypeDef(TypedDict):
    instanceId: str
    appId: str
    grantPermissions: NotRequired[Sequence[PermissionInputTypeDef]]
    revokePermissions: NotRequired[Sequence[PermissionInputTypeDef]]

class PermissionOutputTypeDef(TypedDict):
    action: PermissionOutputActionEnumType
    principal: PrincipalOutputTypeDef

class QAppSessionDataTypeDef(TypedDict):
    cardId: str
    user: UserTypeDef
    value: NotRequired[Dict[str, Any]]
    submissionId: NotRequired[str]
    timestamp: NotRequired[datetime]

class GetQAppSessionOutputTypeDef(TypedDict):
    sessionId: str
    sessionArn: str
    sessionName: str
    appVersion: int
    latestPublishedAppVersion: int
    status: ExecutionStatusType
    cardStatus: Dict[str, CardStatusTypeDef]
    userIsHost: bool
    ResponseMetadata: ResponseMetadataTypeDef

class StartQAppSessionInputTypeDef(TypedDict):
    instanceId: str
    appId: str
    appVersion: int
    initialValues: NotRequired[Sequence[CardValueTypeDef]]
    sessionId: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateQAppSessionInputTypeDef(TypedDict):
    instanceId: str
    sessionId: str
    values: NotRequired[Sequence[CardValueTypeDef]]

class ListLibraryItemsOutputTypeDef(TypedDict):
    libraryItems: List[LibraryItemMemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PredictQAppInputTypeDef(TypedDict):
    instanceId: str
    options: NotRequired[PredictQAppInputOptionsTypeDef]

class AttributeFilterOutputTypeDef(TypedDict):
    andAllFilters: NotRequired[List[Dict[str, Any]]]
    orAllFilters: NotRequired[List[Dict[str, Any]]]
    notFilter: NotRequired[Dict[str, Any]]
    equalsTo: NotRequired[DocumentAttributeOutputTypeDef]
    containsAll: NotRequired[DocumentAttributeOutputTypeDef]
    containsAny: NotRequired[DocumentAttributeOutputTypeDef]
    greaterThan: NotRequired[DocumentAttributeOutputTypeDef]
    greaterThanOrEquals: NotRequired[DocumentAttributeOutputTypeDef]
    lessThan: NotRequired[DocumentAttributeOutputTypeDef]
    lessThanOrEquals: NotRequired[DocumentAttributeOutputTypeDef]

class DocumentAttributeTypeDef(TypedDict):
    name: str
    value: DocumentAttributeValueTypeDef

class DescribeQAppPermissionsOutputTypeDef(TypedDict):
    resourceArn: str
    appId: str
    permissions: List[PermissionOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateQAppPermissionsOutputTypeDef(TypedDict):
    resourceArn: str
    appId: str
    permissions: List[PermissionOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListQAppSessionDataOutputTypeDef(TypedDict):
    sessionId: str
    sessionArn: str
    sessionData: List[QAppSessionDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

QQueryCardInputOutputTypeDef = TypedDict(
    "QQueryCardInputOutputTypeDef",
    {
        "title": str,
        "id": str,
        "type": CardTypeType,
        "prompt": str,
        "outputSource": NotRequired[CardOutputSourceType],
        "attributeFilter": NotRequired[AttributeFilterOutputTypeDef],
    },
)
QQueryCardTypeDef = TypedDict(
    "QQueryCardTypeDef",
    {
        "id": str,
        "title": str,
        "dependencies": List[str],
        "type": CardTypeType,
        "prompt": str,
        "outputSource": CardOutputSourceType,
        "attributeFilter": NotRequired[AttributeFilterOutputTypeDef],
        "memoryReferences": NotRequired[List[str]],
    },
)

class AttributeFilterTypeDef(TypedDict):
    andAllFilters: NotRequired[Sequence[Mapping[str, Any]]]
    orAllFilters: NotRequired[Sequence[Mapping[str, Any]]]
    notFilter: NotRequired[Mapping[str, Any]]
    equalsTo: NotRequired[DocumentAttributeTypeDef]
    containsAll: NotRequired[DocumentAttributeTypeDef]
    containsAny: NotRequired[DocumentAttributeTypeDef]
    greaterThan: NotRequired[DocumentAttributeTypeDef]
    greaterThanOrEquals: NotRequired[DocumentAttributeTypeDef]
    lessThan: NotRequired[DocumentAttributeTypeDef]
    lessThanOrEquals: NotRequired[DocumentAttributeTypeDef]

class CardInputOutputTypeDef(TypedDict):
    textInput: NotRequired[TextInputCardInputTypeDef]
    qQuery: NotRequired[QQueryCardInputOutputTypeDef]
    qPlugin: NotRequired[QPluginCardInputTypeDef]
    fileUpload: NotRequired[FileUploadCardInputTypeDef]
    formInput: NotRequired[FormInputCardInputOutputTypeDef]

class CardTypeDef(TypedDict):
    textInput: NotRequired[TextInputCardTypeDef]
    qQuery: NotRequired[QQueryCardTypeDef]
    qPlugin: NotRequired[QPluginCardTypeDef]
    fileUpload: NotRequired[FileUploadCardTypeDef]
    formInput: NotRequired[FormInputCardTypeDef]

QQueryCardInputTypeDef = TypedDict(
    "QQueryCardInputTypeDef",
    {
        "title": str,
        "id": str,
        "type": CardTypeType,
        "prompt": str,
        "outputSource": NotRequired[CardOutputSourceType],
        "attributeFilter": NotRequired[AttributeFilterTypeDef],
    },
)

class AppDefinitionInputOutputTypeDef(TypedDict):
    cards: List[CardInputOutputTypeDef]
    initialPrompt: NotRequired[str]

class AppDefinitionTypeDef(TypedDict):
    appDefinitionVersion: str
    cards: List[CardTypeDef]
    canEdit: NotRequired[bool]

class CardInputTypeDef(TypedDict):
    textInput: NotRequired[TextInputCardInputTypeDef]
    qQuery: NotRequired[QQueryCardInputTypeDef]
    qPlugin: NotRequired[QPluginCardInputTypeDef]
    fileUpload: NotRequired[FileUploadCardInputTypeDef]
    formInput: NotRequired[FormInputCardInputTypeDef]

class PredictAppDefinitionTypeDef(TypedDict):
    title: str
    appDefinition: AppDefinitionInputOutputTypeDef
    description: NotRequired[str]

class GetQAppOutputTypeDef(TypedDict):
    appId: str
    appArn: str
    title: str
    description: str
    initialPrompt: str
    appVersion: int
    status: AppStatusType
    createdAt: datetime
    createdBy: str
    updatedAt: datetime
    updatedBy: str
    requiredCapabilities: List[AppRequiredCapabilityType]
    appDefinition: AppDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AppDefinitionInputTypeDef(TypedDict):
    cards: Sequence[CardInputTypeDef]
    initialPrompt: NotRequired[str]

class PredictQAppOutputTypeDef(TypedDict):
    app: PredictAppDefinitionTypeDef
    problemStatement: str
    ResponseMetadata: ResponseMetadataTypeDef

AppDefinitionInputUnionTypeDef = Union[AppDefinitionInputTypeDef, AppDefinitionInputOutputTypeDef]

class CreateQAppInputTypeDef(TypedDict):
    instanceId: str
    title: str
    appDefinition: AppDefinitionInputUnionTypeDef
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateQAppInputTypeDef(TypedDict):
    instanceId: str
    appId: str
    title: NotRequired[str]
    description: NotRequired[str]
    appDefinition: NotRequired[AppDefinitionInputUnionTypeDef]
