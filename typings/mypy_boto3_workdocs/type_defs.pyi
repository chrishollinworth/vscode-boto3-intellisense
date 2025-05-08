"""
Type annotations for workdocs service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_workdocs.type_defs import AbortDocumentVersionUploadRequestTypeDef

    data: AbortDocumentVersionUploadRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ActivityTypeType,
    BooleanEnumTypeType,
    CommentStatusTypeType,
    CommentVisibilityTypeType,
    ContentCategoryTypeType,
    DocumentSourceTypeType,
    DocumentStatusTypeType,
    DocumentThumbnailTypeType,
    FolderContentTypeType,
    LanguageCodeTypeType,
    LocaleTypeType,
    OrderByFieldTypeType,
    OrderTypeType,
    PrincipalRoleTypeType,
    PrincipalTypeType,
    ResourceSortTypeType,
    ResourceStateTypeType,
    ResourceTypeType,
    ResponseItemTypeType,
    RolePermissionTypeType,
    RoleTypeType,
    SearchCollectionTypeType,
    SearchQueryScopeTypeType,
    SearchResourceTypeType,
    ShareStatusTypeType,
    SortOrderType,
    StorageTypeType,
    SubscriptionProtocolTypeType,
    UserFilterTypeType,
    UserSortTypeType,
    UserStatusTypeType,
    UserTypeType,
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
    "AbortDocumentVersionUploadRequestTypeDef",
    "ActivateUserRequestTypeDef",
    "ActivateUserResponseTypeDef",
    "ActivityTypeDef",
    "AddResourcePermissionsRequestTypeDef",
    "AddResourcePermissionsResponseTypeDef",
    "CommentMetadataTypeDef",
    "CommentTypeDef",
    "CreateCommentRequestTypeDef",
    "CreateCommentResponseTypeDef",
    "CreateCustomMetadataRequestTypeDef",
    "CreateFolderRequestTypeDef",
    "CreateFolderResponseTypeDef",
    "CreateLabelsRequestTypeDef",
    "CreateNotificationSubscriptionRequestTypeDef",
    "CreateNotificationSubscriptionResponseTypeDef",
    "CreateUserRequestTypeDef",
    "CreateUserResponseTypeDef",
    "DateRangeTypeTypeDef",
    "DeactivateUserRequestTypeDef",
    "DeleteCommentRequestTypeDef",
    "DeleteCustomMetadataRequestTypeDef",
    "DeleteDocumentRequestTypeDef",
    "DeleteDocumentVersionRequestTypeDef",
    "DeleteFolderContentsRequestTypeDef",
    "DeleteFolderRequestTypeDef",
    "DeleteLabelsRequestTypeDef",
    "DeleteNotificationSubscriptionRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DescribeActivitiesRequestPaginateTypeDef",
    "DescribeActivitiesRequestTypeDef",
    "DescribeActivitiesResponseTypeDef",
    "DescribeCommentsRequestPaginateTypeDef",
    "DescribeCommentsRequestTypeDef",
    "DescribeCommentsResponseTypeDef",
    "DescribeDocumentVersionsRequestPaginateTypeDef",
    "DescribeDocumentVersionsRequestTypeDef",
    "DescribeDocumentVersionsResponseTypeDef",
    "DescribeFolderContentsRequestPaginateTypeDef",
    "DescribeFolderContentsRequestTypeDef",
    "DescribeFolderContentsResponseTypeDef",
    "DescribeGroupsRequestPaginateTypeDef",
    "DescribeGroupsRequestTypeDef",
    "DescribeGroupsResponseTypeDef",
    "DescribeNotificationSubscriptionsRequestPaginateTypeDef",
    "DescribeNotificationSubscriptionsRequestTypeDef",
    "DescribeNotificationSubscriptionsResponseTypeDef",
    "DescribeResourcePermissionsRequestPaginateTypeDef",
    "DescribeResourcePermissionsRequestTypeDef",
    "DescribeResourcePermissionsResponseTypeDef",
    "DescribeRootFoldersRequestPaginateTypeDef",
    "DescribeRootFoldersRequestTypeDef",
    "DescribeRootFoldersResponseTypeDef",
    "DescribeUsersRequestPaginateTypeDef",
    "DescribeUsersRequestTypeDef",
    "DescribeUsersResponseTypeDef",
    "DocumentMetadataTypeDef",
    "DocumentVersionMetadataTypeDef",
    "EmptyResponseMetadataTypeDef",
    "FiltersTypeDef",
    "FolderMetadataTypeDef",
    "GetCurrentUserRequestTypeDef",
    "GetCurrentUserResponseTypeDef",
    "GetDocumentPathRequestTypeDef",
    "GetDocumentPathResponseTypeDef",
    "GetDocumentRequestTypeDef",
    "GetDocumentResponseTypeDef",
    "GetDocumentVersionRequestTypeDef",
    "GetDocumentVersionResponseTypeDef",
    "GetFolderPathRequestTypeDef",
    "GetFolderPathResponseTypeDef",
    "GetFolderRequestTypeDef",
    "GetFolderResponseTypeDef",
    "GetResourcesRequestTypeDef",
    "GetResourcesResponseTypeDef",
    "GroupMetadataTypeDef",
    "InitiateDocumentVersionUploadRequestTypeDef",
    "InitiateDocumentVersionUploadResponseTypeDef",
    "LongRangeTypeTypeDef",
    "NotificationOptionsTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantsTypeDef",
    "PermissionInfoTypeDef",
    "PrincipalTypeDef",
    "RemoveAllResourcePermissionsRequestTypeDef",
    "RemoveResourcePermissionRequestTypeDef",
    "ResourceMetadataTypeDef",
    "ResourcePathComponentTypeDef",
    "ResourcePathTypeDef",
    "ResponseItemTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreDocumentVersionsRequestTypeDef",
    "SearchPrincipalTypeTypeDef",
    "SearchResourcesRequestPaginateTypeDef",
    "SearchResourcesRequestTypeDef",
    "SearchResourcesResponseTypeDef",
    "SearchSortResultTypeDef",
    "SharePrincipalTypeDef",
    "ShareResultTypeDef",
    "StorageRuleTypeTypeDef",
    "SubscriptionTypeDef",
    "TimestampTypeDef",
    "UpdateDocumentRequestTypeDef",
    "UpdateDocumentVersionRequestTypeDef",
    "UpdateFolderRequestTypeDef",
    "UpdateUserRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "UploadMetadataTypeDef",
    "UserMetadataTypeDef",
    "UserStorageMetadataTypeDef",
    "UserTypeDef",
)

class AbortDocumentVersionUploadRequestTypeDef(TypedDict):
    DocumentId: str
    VersionId: str
    AuthenticationToken: NotRequired[str]

class ActivateUserRequestTypeDef(TypedDict):
    UserId: str
    AuthenticationToken: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class UserMetadataTypeDef(TypedDict):
    Id: NotRequired[str]
    Username: NotRequired[str]
    GivenName: NotRequired[str]
    Surname: NotRequired[str]
    EmailAddress: NotRequired[str]

class NotificationOptionsTypeDef(TypedDict):
    SendEmail: NotRequired[bool]
    EmailMessage: NotRequired[str]

SharePrincipalTypeDef = TypedDict(
    "SharePrincipalTypeDef",
    {
        "Id": str,
        "Type": PrincipalTypeType,
        "Role": RoleTypeType,
    },
)

class ShareResultTypeDef(TypedDict):
    PrincipalId: NotRequired[str]
    InviteePrincipalId: NotRequired[str]
    Role: NotRequired[RoleTypeType]
    Status: NotRequired[ShareStatusTypeType]
    ShareId: NotRequired[str]
    StatusMessage: NotRequired[str]

CreateCommentRequestTypeDef = TypedDict(
    "CreateCommentRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "Text": str,
        "AuthenticationToken": NotRequired[str],
        "ParentId": NotRequired[str],
        "ThreadId": NotRequired[str],
        "Visibility": NotRequired[CommentVisibilityTypeType],
        "NotifyCollaborators": NotRequired[bool],
    },
)

class CreateCustomMetadataRequestTypeDef(TypedDict):
    ResourceId: str
    CustomMetadata: Mapping[str, str]
    AuthenticationToken: NotRequired[str]
    VersionId: NotRequired[str]

class CreateFolderRequestTypeDef(TypedDict):
    ParentFolderId: str
    AuthenticationToken: NotRequired[str]
    Name: NotRequired[str]

class FolderMetadataTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    CreatorId: NotRequired[str]
    ParentFolderId: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]
    ModifiedTimestamp: NotRequired[datetime]
    ResourceState: NotRequired[ResourceStateTypeType]
    Signature: NotRequired[str]
    Labels: NotRequired[List[str]]
    Size: NotRequired[int]
    LatestVersionSize: NotRequired[int]

class CreateLabelsRequestTypeDef(TypedDict):
    ResourceId: str
    Labels: Sequence[str]
    AuthenticationToken: NotRequired[str]

CreateNotificationSubscriptionRequestTypeDef = TypedDict(
    "CreateNotificationSubscriptionRequestTypeDef",
    {
        "OrganizationId": str,
        "Endpoint": str,
        "Protocol": SubscriptionProtocolTypeType,
        "SubscriptionType": Literal["ALL"],
    },
)
SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "SubscriptionId": NotRequired[str],
        "EndPoint": NotRequired[str],
        "Protocol": NotRequired[SubscriptionProtocolTypeType],
    },
)

class StorageRuleTypeTypeDef(TypedDict):
    StorageAllocatedInBytes: NotRequired[int]
    StorageType: NotRequired[StorageTypeType]

TimestampTypeDef = Union[datetime, str]

class DeactivateUserRequestTypeDef(TypedDict):
    UserId: str
    AuthenticationToken: NotRequired[str]

class DeleteCommentRequestTypeDef(TypedDict):
    DocumentId: str
    VersionId: str
    CommentId: str
    AuthenticationToken: NotRequired[str]

class DeleteCustomMetadataRequestTypeDef(TypedDict):
    ResourceId: str
    AuthenticationToken: NotRequired[str]
    VersionId: NotRequired[str]
    Keys: NotRequired[Sequence[str]]
    DeleteAll: NotRequired[bool]

class DeleteDocumentRequestTypeDef(TypedDict):
    DocumentId: str
    AuthenticationToken: NotRequired[str]

class DeleteDocumentVersionRequestTypeDef(TypedDict):
    DocumentId: str
    VersionId: str
    DeletePriorVersions: bool
    AuthenticationToken: NotRequired[str]

class DeleteFolderContentsRequestTypeDef(TypedDict):
    FolderId: str
    AuthenticationToken: NotRequired[str]

class DeleteFolderRequestTypeDef(TypedDict):
    FolderId: str
    AuthenticationToken: NotRequired[str]

class DeleteLabelsRequestTypeDef(TypedDict):
    ResourceId: str
    AuthenticationToken: NotRequired[str]
    Labels: NotRequired[Sequence[str]]
    DeleteAll: NotRequired[bool]

class DeleteNotificationSubscriptionRequestTypeDef(TypedDict):
    SubscriptionId: str
    OrganizationId: str

class DeleteUserRequestTypeDef(TypedDict):
    UserId: str
    AuthenticationToken: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeCommentsRequestTypeDef(TypedDict):
    DocumentId: str
    VersionId: str
    AuthenticationToken: NotRequired[str]
    Limit: NotRequired[int]
    Marker: NotRequired[str]

class DescribeDocumentVersionsRequestTypeDef(TypedDict):
    DocumentId: str
    AuthenticationToken: NotRequired[str]
    Marker: NotRequired[str]
    Limit: NotRequired[int]
    Include: NotRequired[str]
    Fields: NotRequired[str]

class DocumentVersionMetadataTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    ContentType: NotRequired[str]
    Size: NotRequired[int]
    Signature: NotRequired[str]
    Status: NotRequired[DocumentStatusTypeType]
    CreatedTimestamp: NotRequired[datetime]
    ModifiedTimestamp: NotRequired[datetime]
    ContentCreatedTimestamp: NotRequired[datetime]
    ContentModifiedTimestamp: NotRequired[datetime]
    CreatorId: NotRequired[str]
    Thumbnail: NotRequired[Dict[DocumentThumbnailTypeType, str]]
    Source: NotRequired[Dict[DocumentSourceTypeType, str]]

DescribeFolderContentsRequestTypeDef = TypedDict(
    "DescribeFolderContentsRequestTypeDef",
    {
        "FolderId": str,
        "AuthenticationToken": NotRequired[str],
        "Sort": NotRequired[ResourceSortTypeType],
        "Order": NotRequired[OrderTypeType],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
        "Type": NotRequired[FolderContentTypeType],
        "Include": NotRequired[str],
    },
)

class DescribeGroupsRequestTypeDef(TypedDict):
    SearchQuery: str
    AuthenticationToken: NotRequired[str]
    OrganizationId: NotRequired[str]
    Marker: NotRequired[str]
    Limit: NotRequired[int]

class GroupMetadataTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]

class DescribeNotificationSubscriptionsRequestTypeDef(TypedDict):
    OrganizationId: str
    Marker: NotRequired[str]
    Limit: NotRequired[int]

class DescribeResourcePermissionsRequestTypeDef(TypedDict):
    ResourceId: str
    AuthenticationToken: NotRequired[str]
    PrincipalId: NotRequired[str]
    Limit: NotRequired[int]
    Marker: NotRequired[str]

class DescribeRootFoldersRequestTypeDef(TypedDict):
    AuthenticationToken: str
    Limit: NotRequired[int]
    Marker: NotRequired[str]

class DescribeUsersRequestTypeDef(TypedDict):
    AuthenticationToken: NotRequired[str]
    OrganizationId: NotRequired[str]
    UserIds: NotRequired[str]
    Query: NotRequired[str]
    Include: NotRequired[UserFilterTypeType]
    Order: NotRequired[OrderTypeType]
    Sort: NotRequired[UserSortTypeType]
    Marker: NotRequired[str]
    Limit: NotRequired[int]
    Fields: NotRequired[str]

class LongRangeTypeTypeDef(TypedDict):
    StartValue: NotRequired[int]
    EndValue: NotRequired[int]

class SearchPrincipalTypeTypeDef(TypedDict):
    Id: str
    Roles: NotRequired[Sequence[PrincipalRoleTypeType]]

class GetCurrentUserRequestTypeDef(TypedDict):
    AuthenticationToken: str

class GetDocumentPathRequestTypeDef(TypedDict):
    DocumentId: str
    AuthenticationToken: NotRequired[str]
    Limit: NotRequired[int]
    Fields: NotRequired[str]
    Marker: NotRequired[str]

class GetDocumentRequestTypeDef(TypedDict):
    DocumentId: str
    AuthenticationToken: NotRequired[str]
    IncludeCustomMetadata: NotRequired[bool]

class GetDocumentVersionRequestTypeDef(TypedDict):
    DocumentId: str
    VersionId: str
    AuthenticationToken: NotRequired[str]
    Fields: NotRequired[str]
    IncludeCustomMetadata: NotRequired[bool]

class GetFolderPathRequestTypeDef(TypedDict):
    FolderId: str
    AuthenticationToken: NotRequired[str]
    Limit: NotRequired[int]
    Fields: NotRequired[str]
    Marker: NotRequired[str]

class GetFolderRequestTypeDef(TypedDict):
    FolderId: str
    AuthenticationToken: NotRequired[str]
    IncludeCustomMetadata: NotRequired[bool]

class GetResourcesRequestTypeDef(TypedDict):
    AuthenticationToken: NotRequired[str]
    UserId: NotRequired[str]
    CollectionType: NotRequired[Literal["SHARED_WITH_ME"]]
    Limit: NotRequired[int]
    Marker: NotRequired[str]

class UploadMetadataTypeDef(TypedDict):
    UploadUrl: NotRequired[str]
    SignedHeaders: NotRequired[Dict[str, str]]

PermissionInfoTypeDef = TypedDict(
    "PermissionInfoTypeDef",
    {
        "Role": NotRequired[RoleTypeType],
        "Type": NotRequired[RolePermissionTypeType],
    },
)

class RemoveAllResourcePermissionsRequestTypeDef(TypedDict):
    ResourceId: str
    AuthenticationToken: NotRequired[str]

class RemoveResourcePermissionRequestTypeDef(TypedDict):
    ResourceId: str
    PrincipalId: str
    AuthenticationToken: NotRequired[str]
    PrincipalType: NotRequired[PrincipalTypeType]

class ResourcePathComponentTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]

class RestoreDocumentVersionsRequestTypeDef(TypedDict):
    DocumentId: str
    AuthenticationToken: NotRequired[str]

class SearchSortResultTypeDef(TypedDict):
    Field: NotRequired[OrderByFieldTypeType]
    Order: NotRequired[SortOrderType]

class UpdateDocumentRequestTypeDef(TypedDict):
    DocumentId: str
    AuthenticationToken: NotRequired[str]
    Name: NotRequired[str]
    ParentFolderId: NotRequired[str]
    ResourceState: NotRequired[ResourceStateTypeType]

class UpdateDocumentVersionRequestTypeDef(TypedDict):
    DocumentId: str
    VersionId: str
    AuthenticationToken: NotRequired[str]
    VersionStatus: NotRequired[Literal["ACTIVE"]]

class UpdateFolderRequestTypeDef(TypedDict):
    FolderId: str
    AuthenticationToken: NotRequired[str]
    Name: NotRequired[str]
    ParentFolderId: NotRequired[str]
    ResourceState: NotRequired[ResourceStateTypeType]

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

ResourceMetadataTypeDef = TypedDict(
    "ResourceMetadataTypeDef",
    {
        "Type": NotRequired[ResourceTypeType],
        "Name": NotRequired[str],
        "OriginalName": NotRequired[str],
        "Id": NotRequired[str],
        "VersionId": NotRequired[str],
        "Owner": NotRequired[UserMetadataTypeDef],
        "ParentId": NotRequired[str],
    },
)

class AddResourcePermissionsRequestTypeDef(TypedDict):
    ResourceId: str
    Principals: Sequence[SharePrincipalTypeDef]
    AuthenticationToken: NotRequired[str]
    NotificationOptions: NotRequired[NotificationOptionsTypeDef]

class AddResourcePermissionsResponseTypeDef(TypedDict):
    ShareResults: List[ShareResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFolderResponseTypeDef(TypedDict):
    Metadata: FolderMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRootFoldersResponseTypeDef(TypedDict):
    Folders: List[FolderMetadataTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFolderResponseTypeDef(TypedDict):
    Metadata: FolderMetadataTypeDef
    CustomMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNotificationSubscriptionResponseTypeDef(TypedDict):
    Subscription: SubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNotificationSubscriptionsResponseTypeDef(TypedDict):
    Subscriptions: List[SubscriptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserRequestTypeDef(TypedDict):
    Username: str
    GivenName: str
    Surname: str
    Password: str
    OrganizationId: NotRequired[str]
    EmailAddress: NotRequired[str]
    TimeZoneId: NotRequired[str]
    StorageRule: NotRequired[StorageRuleTypeTypeDef]
    AuthenticationToken: NotRequired[str]

UpdateUserRequestTypeDef = TypedDict(
    "UpdateUserRequestTypeDef",
    {
        "UserId": str,
        "AuthenticationToken": NotRequired[str],
        "GivenName": NotRequired[str],
        "Surname": NotRequired[str],
        "Type": NotRequired[UserTypeType],
        "StorageRule": NotRequired[StorageRuleTypeTypeDef],
        "TimeZoneId": NotRequired[str],
        "Locale": NotRequired[LocaleTypeType],
        "GrantPoweruserPrivileges": NotRequired[BooleanEnumTypeType],
    },
)

class UserStorageMetadataTypeDef(TypedDict):
    StorageUtilizedInBytes: NotRequired[int]
    StorageRule: NotRequired[StorageRuleTypeTypeDef]

class DateRangeTypeTypeDef(TypedDict):
    StartValue: NotRequired[TimestampTypeDef]
    EndValue: NotRequired[TimestampTypeDef]

class DescribeActivitiesRequestTypeDef(TypedDict):
    AuthenticationToken: NotRequired[str]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    OrganizationId: NotRequired[str]
    ActivityTypes: NotRequired[str]
    ResourceId: NotRequired[str]
    UserId: NotRequired[str]
    IncludeIndirectActivities: NotRequired[bool]
    Limit: NotRequired[int]
    Marker: NotRequired[str]

class InitiateDocumentVersionUploadRequestTypeDef(TypedDict):
    AuthenticationToken: NotRequired[str]
    Id: NotRequired[str]
    Name: NotRequired[str]
    ContentCreatedTimestamp: NotRequired[TimestampTypeDef]
    ContentModifiedTimestamp: NotRequired[TimestampTypeDef]
    ContentType: NotRequired[str]
    DocumentSizeInBytes: NotRequired[int]
    ParentFolderId: NotRequired[str]

class DescribeActivitiesRequestPaginateTypeDef(TypedDict):
    AuthenticationToken: NotRequired[str]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    OrganizationId: NotRequired[str]
    ActivityTypes: NotRequired[str]
    ResourceId: NotRequired[str]
    UserId: NotRequired[str]
    IncludeIndirectActivities: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeCommentsRequestPaginateTypeDef(TypedDict):
    DocumentId: str
    VersionId: str
    AuthenticationToken: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDocumentVersionsRequestPaginateTypeDef(TypedDict):
    DocumentId: str
    AuthenticationToken: NotRequired[str]
    Include: NotRequired[str]
    Fields: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

DescribeFolderContentsRequestPaginateTypeDef = TypedDict(
    "DescribeFolderContentsRequestPaginateTypeDef",
    {
        "FolderId": str,
        "AuthenticationToken": NotRequired[str],
        "Sort": NotRequired[ResourceSortTypeType],
        "Order": NotRequired[OrderTypeType],
        "Type": NotRequired[FolderContentTypeType],
        "Include": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class DescribeGroupsRequestPaginateTypeDef(TypedDict):
    SearchQuery: str
    AuthenticationToken: NotRequired[str]
    OrganizationId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeNotificationSubscriptionsRequestPaginateTypeDef(TypedDict):
    OrganizationId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeResourcePermissionsRequestPaginateTypeDef(TypedDict):
    ResourceId: str
    AuthenticationToken: NotRequired[str]
    PrincipalId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeRootFoldersRequestPaginateTypeDef(TypedDict):
    AuthenticationToken: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeUsersRequestPaginateTypeDef(TypedDict):
    AuthenticationToken: NotRequired[str]
    OrganizationId: NotRequired[str]
    UserIds: NotRequired[str]
    Query: NotRequired[str]
    Include: NotRequired[UserFilterTypeType]
    Order: NotRequired[OrderTypeType]
    Sort: NotRequired[UserSortTypeType]
    Fields: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDocumentVersionsResponseTypeDef(TypedDict):
    DocumentVersions: List[DocumentVersionMetadataTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentMetadataTypeDef(TypedDict):
    Id: NotRequired[str]
    CreatorId: NotRequired[str]
    ParentFolderId: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]
    ModifiedTimestamp: NotRequired[datetime]
    LatestVersionMetadata: NotRequired[DocumentVersionMetadataTypeDef]
    ResourceState: NotRequired[ResourceStateTypeType]
    Labels: NotRequired[List[str]]

class GetDocumentVersionResponseTypeDef(TypedDict):
    Metadata: DocumentVersionMetadataTypeDef
    CustomMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGroupsResponseTypeDef(TypedDict):
    Groups: List[GroupMetadataTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ParticipantsTypeDef(TypedDict):
    Users: NotRequired[List[UserMetadataTypeDef]]
    Groups: NotRequired[List[GroupMetadataTypeDef]]

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[PrincipalTypeType],
        "Roles": NotRequired[List[PermissionInfoTypeDef]],
    },
)

class ResourcePathTypeDef(TypedDict):
    Components: NotRequired[List[ResourcePathComponentTypeDef]]

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": NotRequired[str],
        "Username": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "GivenName": NotRequired[str],
        "Surname": NotRequired[str],
        "OrganizationId": NotRequired[str],
        "RootFolderId": NotRequired[str],
        "RecycleBinFolderId": NotRequired[str],
        "Status": NotRequired[UserStatusTypeType],
        "Type": NotRequired[UserTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "ModifiedTimestamp": NotRequired[datetime],
        "TimeZoneId": NotRequired[str],
        "Locale": NotRequired[LocaleTypeType],
        "Storage": NotRequired[UserStorageMetadataTypeDef],
    },
)

class FiltersTypeDef(TypedDict):
    TextLocales: NotRequired[Sequence[LanguageCodeTypeType]]
    ContentCategories: NotRequired[Sequence[ContentCategoryTypeType]]
    ResourceTypes: NotRequired[Sequence[SearchResourceTypeType]]
    Labels: NotRequired[Sequence[str]]
    Principals: NotRequired[Sequence[SearchPrincipalTypeTypeDef]]
    AncestorIds: NotRequired[Sequence[str]]
    SearchCollectionTypes: NotRequired[Sequence[SearchCollectionTypeType]]
    SizeRange: NotRequired[LongRangeTypeTypeDef]
    CreatedRange: NotRequired[DateRangeTypeTypeDef]
    ModifiedRange: NotRequired[DateRangeTypeTypeDef]

class DescribeFolderContentsResponseTypeDef(TypedDict):
    Folders: List[FolderMetadataTypeDef]
    Documents: List[DocumentMetadataTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDocumentResponseTypeDef(TypedDict):
    Metadata: DocumentMetadataTypeDef
    CustomMetadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcesResponseTypeDef(TypedDict):
    Folders: List[FolderMetadataTypeDef]
    Documents: List[DocumentMetadataTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class InitiateDocumentVersionUploadResponseTypeDef(TypedDict):
    Metadata: DocumentMetadataTypeDef
    UploadMetadata: UploadMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourcePermissionsResponseTypeDef(TypedDict):
    Principals: List[PrincipalTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDocumentPathResponseTypeDef(TypedDict):
    Path: ResourcePathTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFolderPathResponseTypeDef(TypedDict):
    Path: ResourcePathTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ActivateUserResponseTypeDef(TypedDict):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CommentMetadataTypeDef(TypedDict):
    CommentId: NotRequired[str]
    Contributor: NotRequired[UserTypeDef]
    CreatedTimestamp: NotRequired[datetime]
    CommentStatus: NotRequired[CommentStatusTypeType]
    RecipientId: NotRequired[str]
    ContributorId: NotRequired[str]

CommentTypeDef = TypedDict(
    "CommentTypeDef",
    {
        "CommentId": str,
        "ParentId": NotRequired[str],
        "ThreadId": NotRequired[str],
        "Text": NotRequired[str],
        "Contributor": NotRequired[UserTypeDef],
        "CreatedTimestamp": NotRequired[datetime],
        "Status": NotRequired[CommentStatusTypeType],
        "Visibility": NotRequired[CommentVisibilityTypeType],
        "RecipientId": NotRequired[str],
    },
)

class CreateUserResponseTypeDef(TypedDict):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUsersResponseTypeDef(TypedDict):
    Users: List[UserTypeDef]
    TotalNumberOfUsers: int
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCurrentUserResponseTypeDef(TypedDict):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserResponseTypeDef(TypedDict):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchResourcesRequestPaginateTypeDef(TypedDict):
    AuthenticationToken: NotRequired[str]
    QueryText: NotRequired[str]
    QueryScopes: NotRequired[Sequence[SearchQueryScopeTypeType]]
    OrganizationId: NotRequired[str]
    AdditionalResponseFields: NotRequired[Sequence[Literal["WEBURL"]]]
    Filters: NotRequired[FiltersTypeDef]
    OrderBy: NotRequired[Sequence[SearchSortResultTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchResourcesRequestTypeDef(TypedDict):
    AuthenticationToken: NotRequired[str]
    QueryText: NotRequired[str]
    QueryScopes: NotRequired[Sequence[SearchQueryScopeTypeType]]
    OrganizationId: NotRequired[str]
    AdditionalResponseFields: NotRequired[Sequence[Literal["WEBURL"]]]
    Filters: NotRequired[FiltersTypeDef]
    OrderBy: NotRequired[Sequence[SearchSortResultTypeDef]]
    Limit: NotRequired[int]
    Marker: NotRequired[str]

ActivityTypeDef = TypedDict(
    "ActivityTypeDef",
    {
        "Type": NotRequired[ActivityTypeType],
        "TimeStamp": NotRequired[datetime],
        "IsIndirectActivity": NotRequired[bool],
        "OrganizationId": NotRequired[str],
        "Initiator": NotRequired[UserMetadataTypeDef],
        "Participants": NotRequired[ParticipantsTypeDef],
        "ResourceMetadata": NotRequired[ResourceMetadataTypeDef],
        "OriginalParent": NotRequired[ResourceMetadataTypeDef],
        "CommentMetadata": NotRequired[CommentMetadataTypeDef],
    },
)

class ResponseItemTypeDef(TypedDict):
    ResourceType: NotRequired[ResponseItemTypeType]
    WebUrl: NotRequired[str]
    DocumentMetadata: NotRequired[DocumentMetadataTypeDef]
    FolderMetadata: NotRequired[FolderMetadataTypeDef]
    CommentMetadata: NotRequired[CommentMetadataTypeDef]
    DocumentVersionMetadata: NotRequired[DocumentVersionMetadataTypeDef]

class CreateCommentResponseTypeDef(TypedDict):
    Comment: CommentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCommentsResponseTypeDef(TypedDict):
    Comments: List[CommentTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeActivitiesResponseTypeDef(TypedDict):
    UserActivities: List[ActivityTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchResourcesResponseTypeDef(TypedDict):
    Items: List[ResponseItemTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef
