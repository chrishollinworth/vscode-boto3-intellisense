"""
Type annotations for workdocs service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/literals.html)

Usage::

    ```python
    from mypy_boto3_workdocs.literals import ActivityTypeType

    data: ActivityTypeType = "DOCUMENT_ANNOTATION_ADDED"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActivityTypeType",
    "AdditionalResponseFieldTypeType",
    "BooleanEnumTypeType",
    "CommentStatusTypeType",
    "CommentVisibilityTypeType",
    "ContentCategoryTypeType",
    "DescribeActivitiesPaginatorName",
    "DescribeCommentsPaginatorName",
    "DescribeDocumentVersionsPaginatorName",
    "DescribeFolderContentsPaginatorName",
    "DescribeGroupsPaginatorName",
    "DescribeNotificationSubscriptionsPaginatorName",
    "DescribeResourcePermissionsPaginatorName",
    "DescribeRootFoldersPaginatorName",
    "DescribeUsersPaginatorName",
    "DocumentSourceTypeType",
    "DocumentStatusTypeType",
    "DocumentThumbnailTypeType",
    "DocumentVersionStatusType",
    "FolderContentTypeType",
    "LanguageCodeTypeType",
    "LocaleTypeType",
    "OrderByFieldTypeType",
    "OrderTypeType",
    "PrincipalRoleTypeType",
    "PrincipalTypeType",
    "ResourceCollectionTypeType",
    "ResourceSortTypeType",
    "ResourceStateTypeType",
    "ResourceTypeType",
    "ResponseItemTypeType",
    "RolePermissionTypeType",
    "RoleTypeType",
    "SearchCollectionTypeType",
    "SearchQueryScopeTypeType",
    "SearchResourceTypeType",
    "SearchResourcesPaginatorName",
    "ShareStatusTypeType",
    "SortOrderType",
    "StorageTypeType",
    "SubscriptionProtocolTypeType",
    "SubscriptionTypeType",
    "UserFilterTypeType",
    "UserSortTypeType",
    "UserStatusTypeType",
    "UserTypeType",
)

ActivityTypeType = Literal[
    "DOCUMENT_ANNOTATION_ADDED",
    "DOCUMENT_ANNOTATION_DELETED",
    "DOCUMENT_CHECKED_IN",
    "DOCUMENT_CHECKED_OUT",
    "DOCUMENT_COMMENT_ADDED",
    "DOCUMENT_COMMENT_DELETED",
    "DOCUMENT_MOVED",
    "DOCUMENT_RECYCLED",
    "DOCUMENT_RENAMED",
    "DOCUMENT_RESTORED",
    "DOCUMENT_REVERTED",
    "DOCUMENT_SHAREABLE_LINK_CREATED",
    "DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED",
    "DOCUMENT_SHAREABLE_LINK_REMOVED",
    "DOCUMENT_SHARED",
    "DOCUMENT_SHARE_PERMISSION_CHANGED",
    "DOCUMENT_UNSHARED",
    "DOCUMENT_VERSION_DELETED",
    "DOCUMENT_VERSION_DOWNLOADED",
    "DOCUMENT_VERSION_UPLOADED",
    "DOCUMENT_VERSION_VIEWED",
    "FOLDER_CREATED",
    "FOLDER_DELETED",
    "FOLDER_MOVED",
    "FOLDER_RECYCLED",
    "FOLDER_RENAMED",
    "FOLDER_RESTORED",
    "FOLDER_SHAREABLE_LINK_CREATED",
    "FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED",
    "FOLDER_SHAREABLE_LINK_REMOVED",
    "FOLDER_SHARED",
    "FOLDER_SHARE_PERMISSION_CHANGED",
    "FOLDER_UNSHARED",
]
AdditionalResponseFieldTypeType = Literal["WEBURL"]
BooleanEnumTypeType = Literal["FALSE", "TRUE"]
CommentStatusTypeType = Literal["DELETED", "DRAFT", "PUBLISHED"]
CommentVisibilityTypeType = Literal["PRIVATE", "PUBLIC"]
ContentCategoryTypeType = Literal[
    "AUDIO",
    "DOCUMENT",
    "IMAGE",
    "OTHER",
    "PDF",
    "PRESENTATION",
    "SOURCE_CODE",
    "SPREADSHEET",
    "VIDEO",
]
DescribeActivitiesPaginatorName = Literal["describe_activities"]
DescribeCommentsPaginatorName = Literal["describe_comments"]
DescribeDocumentVersionsPaginatorName = Literal["describe_document_versions"]
DescribeFolderContentsPaginatorName = Literal["describe_folder_contents"]
DescribeGroupsPaginatorName = Literal["describe_groups"]
DescribeNotificationSubscriptionsPaginatorName = Literal["describe_notification_subscriptions"]
DescribeResourcePermissionsPaginatorName = Literal["describe_resource_permissions"]
DescribeRootFoldersPaginatorName = Literal["describe_root_folders"]
DescribeUsersPaginatorName = Literal["describe_users"]
DocumentSourceTypeType = Literal["ORIGINAL", "WITH_COMMENTS"]
DocumentStatusTypeType = Literal["ACTIVE", "INITIALIZED"]
DocumentThumbnailTypeType = Literal["LARGE", "SMALL", "SMALL_HQ"]
DocumentVersionStatusType = Literal["ACTIVE"]
FolderContentTypeType = Literal["ALL", "DOCUMENT", "FOLDER"]
LanguageCodeTypeType = Literal[
    "AR",
    "BG",
    "BN",
    "CS",
    "DA",
    "DE",
    "DEFAULT",
    "EL",
    "EN",
    "ES",
    "FA",
    "FI",
    "FR",
    "HI",
    "HU",
    "ID",
    "IT",
    "JA",
    "KO",
    "LT",
    "LV",
    "NL",
    "NO",
    "PT",
    "RO",
    "RU",
    "SV",
    "SW",
    "TH",
    "TR",
    "ZH",
]
LocaleTypeType = Literal[
    "de", "default", "en", "es", "fr", "ja", "ko", "pt_BR", "ru", "zh_CN", "zh_TW"
]
OrderByFieldTypeType = Literal[
    "CREATED_TIMESTAMP", "MODIFIED_TIMESTAMP", "NAME", "RELEVANCE", "SIZE"
]
OrderTypeType = Literal["ASCENDING", "DESCENDING"]
PrincipalRoleTypeType = Literal["CONTRIBUTOR", "COOWNER", "OWNER", "VIEWER"]
PrincipalTypeType = Literal["ANONYMOUS", "GROUP", "INVITE", "ORGANIZATION", "USER"]
ResourceCollectionTypeType = Literal["SHARED_WITH_ME"]
ResourceSortTypeType = Literal["DATE", "NAME"]
ResourceStateTypeType = Literal["ACTIVE", "RECYCLED", "RECYCLING", "RESTORING"]
ResourceTypeType = Literal["DOCUMENT", "FOLDER"]
ResponseItemTypeType = Literal["COMMENT", "DOCUMENT", "DOCUMENT_VERSION", "FOLDER"]
RolePermissionTypeType = Literal["DIRECT", "INHERITED"]
RoleTypeType = Literal["CONTRIBUTOR", "COOWNER", "OWNER", "VIEWER"]
SearchCollectionTypeType = Literal["OWNED", "SHARED_WITH_ME"]
SearchQueryScopeTypeType = Literal["CONTENT", "NAME"]
SearchResourceTypeType = Literal["COMMENT", "DOCUMENT", "DOCUMENT_VERSION", "FOLDER"]
SearchResourcesPaginatorName = Literal["search_resources"]
ShareStatusTypeType = Literal["FAILURE", "SUCCESS"]
SortOrderType = Literal["ASC", "DESC"]
StorageTypeType = Literal["QUOTA", "UNLIMITED"]
SubscriptionProtocolTypeType = Literal["HTTPS", "SQS"]
SubscriptionTypeType = Literal["ALL"]
UserFilterTypeType = Literal["ACTIVE_PENDING", "ALL"]
UserSortTypeType = Literal["FULL_NAME", "STORAGE_LIMIT", "STORAGE_USED", "USER_NAME", "USER_STATUS"]
UserStatusTypeType = Literal["ACTIVE", "INACTIVE", "PENDING"]
UserTypeType = Literal["ADMIN", "MINIMALUSER", "POWERUSER", "USER", "WORKSPACESUSER"]
