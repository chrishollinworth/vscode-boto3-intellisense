"""
Main interface for workdocs service type definitions.

Usage::

    ```python
    from mypy_boto3_workdocs.type_defs import ActivityTypeDef

    data: ActivityTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActivityTypeDef",
    "CommentMetadataTypeDef",
    "CommentTypeDef",
    "DocumentMetadataTypeDef",
    "DocumentVersionMetadataTypeDef",
    "FolderMetadataTypeDef",
    "GroupMetadataTypeDef",
    "ParticipantsTypeDef",
    "PermissionInfoTypeDef",
    "PrincipalTypeDef",
    "ResourceMetadataTypeDef",
    "ResourcePathComponentTypeDef",
    "ResourcePathTypeDef",
    "ShareResultTypeDef",
    "StorageRuleTypeTypeDef",
    "SubscriptionTypeDef",
    "UploadMetadataTypeDef",
    "UserMetadataTypeDef",
    "UserStorageMetadataTypeDef",
    "UserTypeDef",
    "ActivateUserResponseTypeDef",
    "AddResourcePermissionsResponseTypeDef",
    "CreateCommentResponseTypeDef",
    "CreateFolderResponseTypeDef",
    "CreateNotificationSubscriptionResponseTypeDef",
    "CreateUserResponseTypeDef",
    "DescribeActivitiesResponseTypeDef",
    "DescribeCommentsResponseTypeDef",
    "DescribeDocumentVersionsResponseTypeDef",
    "DescribeFolderContentsResponseTypeDef",
    "DescribeGroupsResponseTypeDef",
    "DescribeNotificationSubscriptionsResponseTypeDef",
    "DescribeResourcePermissionsResponseTypeDef",
    "DescribeRootFoldersResponseTypeDef",
    "DescribeUsersResponseTypeDef",
    "GetCurrentUserResponseTypeDef",
    "GetDocumentPathResponseTypeDef",
    "GetDocumentResponseTypeDef",
    "GetDocumentVersionResponseTypeDef",
    "GetFolderPathResponseTypeDef",
    "GetFolderResponseTypeDef",
    "GetResourcesResponseTypeDef",
    "InitiateDocumentVersionUploadResponseTypeDef",
    "NotificationOptionsTypeDef",
    "PaginatorConfigTypeDef",
    "SharePrincipalTypeDef",
    "UpdateUserResponseTypeDef",
)

ActivityTypeDef = TypedDict(
    "ActivityTypeDef",
    {
        "Type": Literal[
            "DOCUMENT_CHECKED_IN",
            "DOCUMENT_CHECKED_OUT",
            "DOCUMENT_RENAMED",
            "DOCUMENT_VERSION_UPLOADED",
            "DOCUMENT_VERSION_DELETED",
            "DOCUMENT_VERSION_VIEWED",
            "DOCUMENT_VERSION_DOWNLOADED",
            "DOCUMENT_RECYCLED",
            "DOCUMENT_RESTORED",
            "DOCUMENT_REVERTED",
            "DOCUMENT_SHARED",
            "DOCUMENT_UNSHARED",
            "DOCUMENT_SHARE_PERMISSION_CHANGED",
            "DOCUMENT_SHAREABLE_LINK_CREATED",
            "DOCUMENT_SHAREABLE_LINK_REMOVED",
            "DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED",
            "DOCUMENT_MOVED",
            "DOCUMENT_COMMENT_ADDED",
            "DOCUMENT_COMMENT_DELETED",
            "DOCUMENT_ANNOTATION_ADDED",
            "DOCUMENT_ANNOTATION_DELETED",
            "FOLDER_CREATED",
            "FOLDER_DELETED",
            "FOLDER_RENAMED",
            "FOLDER_RECYCLED",
            "FOLDER_RESTORED",
            "FOLDER_SHARED",
            "FOLDER_UNSHARED",
            "FOLDER_SHARE_PERMISSION_CHANGED",
            "FOLDER_SHAREABLE_LINK_CREATED",
            "FOLDER_SHAREABLE_LINK_REMOVED",
            "FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED",
            "FOLDER_MOVED",
        ],
        "TimeStamp": datetime,
        "IsIndirectActivity": bool,
        "OrganizationId": str,
        "Initiator": "UserMetadataTypeDef",
        "Participants": "ParticipantsTypeDef",
        "ResourceMetadata": "ResourceMetadataTypeDef",
        "OriginalParent": "ResourceMetadataTypeDef",
        "CommentMetadata": "CommentMetadataTypeDef",
    },
    total=False,
)

CommentMetadataTypeDef = TypedDict(
    "CommentMetadataTypeDef",
    {
        "CommentId": str,
        "Contributor": "UserTypeDef",
        "CreatedTimestamp": datetime,
        "CommentStatus": Literal["DRAFT", "PUBLISHED", "DELETED"],
        "RecipientId": str,
    },
    total=False,
)

_RequiredCommentTypeDef = TypedDict("_RequiredCommentTypeDef", {"CommentId": str})
_OptionalCommentTypeDef = TypedDict(
    "_OptionalCommentTypeDef",
    {
        "ParentId": str,
        "ThreadId": str,
        "Text": str,
        "Contributor": "UserTypeDef",
        "CreatedTimestamp": datetime,
        "Status": Literal["DRAFT", "PUBLISHED", "DELETED"],
        "Visibility": Literal["PUBLIC", "PRIVATE"],
        "RecipientId": str,
    },
    total=False,
)


class CommentTypeDef(_RequiredCommentTypeDef, _OptionalCommentTypeDef):
    pass


DocumentMetadataTypeDef = TypedDict(
    "DocumentMetadataTypeDef",
    {
        "Id": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "LatestVersionMetadata": "DocumentVersionMetadataTypeDef",
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Labels": List[str],
    },
    total=False,
)

DocumentVersionMetadataTypeDef = TypedDict(
    "DocumentVersionMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "ContentType": str,
        "Size": int,
        "Signature": str,
        "Status": Literal["INITIALIZED", "ACTIVE"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ContentCreatedTimestamp": datetime,
        "ContentModifiedTimestamp": datetime,
        "CreatorId": str,
        "Thumbnail": Dict[Literal["SMALL", "SMALL_HQ", "LARGE"], str],
        "Source": Dict[Literal["ORIGINAL", "WITH_COMMENTS"], str],
    },
    total=False,
)

FolderMetadataTypeDef = TypedDict(
    "FolderMetadataTypeDef",
    {
        "Id": str,
        "Name": str,
        "CreatorId": str,
        "ParentFolderId": str,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "ResourceState": Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"],
        "Signature": str,
        "Labels": List[str],
        "Size": int,
        "LatestVersionSize": int,
    },
    total=False,
)

GroupMetadataTypeDef = TypedDict("GroupMetadataTypeDef", {"Id": str, "Name": str}, total=False)

ParticipantsTypeDef = TypedDict(
    "ParticipantsTypeDef",
    {"Users": List["UserMetadataTypeDef"], "Groups": List["GroupMetadataTypeDef"]},
    total=False,
)

PermissionInfoTypeDef = TypedDict(
    "PermissionInfoTypeDef",
    {
        "Role": Literal["VIEWER", "CONTRIBUTOR", "OWNER", "COOWNER"],
        "Type": Literal["DIRECT", "INHERITED"],
    },
    total=False,
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "Id": str,
        "Type": Literal["USER", "GROUP", "INVITE", "ANONYMOUS", "ORGANIZATION"],
        "Roles": List["PermissionInfoTypeDef"],
    },
    total=False,
)

ResourceMetadataTypeDef = TypedDict(
    "ResourceMetadataTypeDef",
    {
        "Type": Literal["FOLDER", "DOCUMENT"],
        "Name": str,
        "OriginalName": str,
        "Id": str,
        "VersionId": str,
        "Owner": "UserMetadataTypeDef",
        "ParentId": str,
    },
    total=False,
)

ResourcePathComponentTypeDef = TypedDict(
    "ResourcePathComponentTypeDef", {"Id": str, "Name": str}, total=False
)

ResourcePathTypeDef = TypedDict(
    "ResourcePathTypeDef", {"Components": List["ResourcePathComponentTypeDef"]}, total=False
)

ShareResultTypeDef = TypedDict(
    "ShareResultTypeDef",
    {
        "PrincipalId": str,
        "InviteePrincipalId": str,
        "Role": Literal["VIEWER", "CONTRIBUTOR", "OWNER", "COOWNER"],
        "Status": Literal["SUCCESS", "FAILURE"],
        "ShareId": str,
        "StatusMessage": str,
    },
    total=False,
)

StorageRuleTypeTypeDef = TypedDict(
    "StorageRuleTypeTypeDef",
    {"StorageAllocatedInBytes": int, "StorageType": Literal["UNLIMITED", "QUOTA"]},
    total=False,
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {"SubscriptionId": str, "EndPoint": str, "Protocol": Literal["HTTPS"]},
    total=False,
)

UploadMetadataTypeDef = TypedDict(
    "UploadMetadataTypeDef", {"UploadUrl": str, "SignedHeaders": Dict[str, str]}, total=False
)

UserMetadataTypeDef = TypedDict(
    "UserMetadataTypeDef",
    {"Id": str, "Username": str, "GivenName": str, "Surname": str, "EmailAddress": str},
    total=False,
)

UserStorageMetadataTypeDef = TypedDict(
    "UserStorageMetadataTypeDef",
    {"StorageUtilizedInBytes": int, "StorageRule": "StorageRuleTypeTypeDef"},
    total=False,
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": Literal["ACTIVE", "INACTIVE", "PENDING"],
        "Type": Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"],
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ],
        "Storage": "UserStorageMetadataTypeDef",
    },
    total=False,
)

ActivateUserResponseTypeDef = TypedDict(
    "ActivateUserResponseTypeDef", {"User": "UserTypeDef"}, total=False
)

AddResourcePermissionsResponseTypeDef = TypedDict(
    "AddResourcePermissionsResponseTypeDef",
    {"ShareResults": List["ShareResultTypeDef"]},
    total=False,
)

CreateCommentResponseTypeDef = TypedDict(
    "CreateCommentResponseTypeDef", {"Comment": "CommentTypeDef"}, total=False
)

CreateFolderResponseTypeDef = TypedDict(
    "CreateFolderResponseTypeDef", {"Metadata": "FolderMetadataTypeDef"}, total=False
)

CreateNotificationSubscriptionResponseTypeDef = TypedDict(
    "CreateNotificationSubscriptionResponseTypeDef",
    {"Subscription": "SubscriptionTypeDef"},
    total=False,
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef", {"User": "UserTypeDef"}, total=False
)

DescribeActivitiesResponseTypeDef = TypedDict(
    "DescribeActivitiesResponseTypeDef",
    {"UserActivities": List["ActivityTypeDef"], "Marker": str},
    total=False,
)

DescribeCommentsResponseTypeDef = TypedDict(
    "DescribeCommentsResponseTypeDef",
    {"Comments": List["CommentTypeDef"], "Marker": str},
    total=False,
)

DescribeDocumentVersionsResponseTypeDef = TypedDict(
    "DescribeDocumentVersionsResponseTypeDef",
    {"DocumentVersions": List["DocumentVersionMetadataTypeDef"], "Marker": str},
    total=False,
)

DescribeFolderContentsResponseTypeDef = TypedDict(
    "DescribeFolderContentsResponseTypeDef",
    {
        "Folders": List["FolderMetadataTypeDef"],
        "Documents": List["DocumentMetadataTypeDef"],
        "Marker": str,
    },
    total=False,
)

DescribeGroupsResponseTypeDef = TypedDict(
    "DescribeGroupsResponseTypeDef",
    {"Groups": List["GroupMetadataTypeDef"], "Marker": str},
    total=False,
)

DescribeNotificationSubscriptionsResponseTypeDef = TypedDict(
    "DescribeNotificationSubscriptionsResponseTypeDef",
    {"Subscriptions": List["SubscriptionTypeDef"], "Marker": str},
    total=False,
)

DescribeResourcePermissionsResponseTypeDef = TypedDict(
    "DescribeResourcePermissionsResponseTypeDef",
    {"Principals": List["PrincipalTypeDef"], "Marker": str},
    total=False,
)

DescribeRootFoldersResponseTypeDef = TypedDict(
    "DescribeRootFoldersResponseTypeDef",
    {"Folders": List["FolderMetadataTypeDef"], "Marker": str},
    total=False,
)

DescribeUsersResponseTypeDef = TypedDict(
    "DescribeUsersResponseTypeDef",
    {"Users": List["UserTypeDef"], "TotalNumberOfUsers": int, "Marker": str},
    total=False,
)

GetCurrentUserResponseTypeDef = TypedDict(
    "GetCurrentUserResponseTypeDef", {"User": "UserTypeDef"}, total=False
)

GetDocumentPathResponseTypeDef = TypedDict(
    "GetDocumentPathResponseTypeDef", {"Path": "ResourcePathTypeDef"}, total=False
)

GetDocumentResponseTypeDef = TypedDict(
    "GetDocumentResponseTypeDef",
    {"Metadata": "DocumentMetadataTypeDef", "CustomMetadata": Dict[str, str]},
    total=False,
)

GetDocumentVersionResponseTypeDef = TypedDict(
    "GetDocumentVersionResponseTypeDef",
    {"Metadata": "DocumentVersionMetadataTypeDef", "CustomMetadata": Dict[str, str]},
    total=False,
)

GetFolderPathResponseTypeDef = TypedDict(
    "GetFolderPathResponseTypeDef", {"Path": "ResourcePathTypeDef"}, total=False
)

GetFolderResponseTypeDef = TypedDict(
    "GetFolderResponseTypeDef",
    {"Metadata": "FolderMetadataTypeDef", "CustomMetadata": Dict[str, str]},
    total=False,
)

GetResourcesResponseTypeDef = TypedDict(
    "GetResourcesResponseTypeDef",
    {
        "Folders": List["FolderMetadataTypeDef"],
        "Documents": List["DocumentMetadataTypeDef"],
        "Marker": str,
    },
    total=False,
)

InitiateDocumentVersionUploadResponseTypeDef = TypedDict(
    "InitiateDocumentVersionUploadResponseTypeDef",
    {"Metadata": "DocumentMetadataTypeDef", "UploadMetadata": "UploadMetadataTypeDef"},
    total=False,
)

NotificationOptionsTypeDef = TypedDict(
    "NotificationOptionsTypeDef", {"SendEmail": bool, "EmailMessage": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SharePrincipalTypeDef = TypedDict(
    "SharePrincipalTypeDef",
    {
        "Id": str,
        "Type": Literal["USER", "GROUP", "INVITE", "ANONYMOUS", "ORGANIZATION"],
        "Role": Literal["VIEWER", "CONTRIBUTOR", "OWNER", "COOWNER"],
    },
)

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef", {"User": "UserTypeDef"}, total=False
)
