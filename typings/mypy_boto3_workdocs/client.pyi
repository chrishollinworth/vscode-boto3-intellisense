# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for workdocs service client

Usage::

    ```python
    import boto3
    from mypy_boto3_workdocs import WorkDocsClient

    client: WorkDocsClient = boto3.client("workdocs")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_workdocs.paginator import (
    DescribeActivitiesPaginator,
    DescribeCommentsPaginator,
    DescribeDocumentVersionsPaginator,
    DescribeFolderContentsPaginator,
    DescribeGroupsPaginator,
    DescribeNotificationSubscriptionsPaginator,
    DescribeResourcePermissionsPaginator,
    DescribeRootFoldersPaginator,
    DescribeUsersPaginator,
)
from mypy_boto3_workdocs.type_defs import (
    ActivateUserResponseTypeDef,
    AddResourcePermissionsResponseTypeDef,
    CreateCommentResponseTypeDef,
    CreateFolderResponseTypeDef,
    CreateNotificationSubscriptionResponseTypeDef,
    CreateUserResponseTypeDef,
    DescribeActivitiesResponseTypeDef,
    DescribeCommentsResponseTypeDef,
    DescribeDocumentVersionsResponseTypeDef,
    DescribeFolderContentsResponseTypeDef,
    DescribeGroupsResponseTypeDef,
    DescribeNotificationSubscriptionsResponseTypeDef,
    DescribeResourcePermissionsResponseTypeDef,
    DescribeRootFoldersResponseTypeDef,
    DescribeUsersResponseTypeDef,
    GetCurrentUserResponseTypeDef,
    GetDocumentPathResponseTypeDef,
    GetDocumentResponseTypeDef,
    GetDocumentVersionResponseTypeDef,
    GetFolderPathResponseTypeDef,
    GetFolderResponseTypeDef,
    GetResourcesResponseTypeDef,
    InitiateDocumentVersionUploadResponseTypeDef,
    NotificationOptionsTypeDef,
    SharePrincipalTypeDef,
    StorageRuleTypeTypeDef,
    UpdateUserResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WorkDocsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConflictingOperationException: Type[BotocoreClientError]
    CustomMetadataLimitExceededException: Type[BotocoreClientError]
    DeactivatingLastSystemUserException: Type[BotocoreClientError]
    DocumentLockedForCommentsException: Type[BotocoreClientError]
    DraftUploadOutOfSyncException: Type[BotocoreClientError]
    EntityAlreadyExistsException: Type[BotocoreClientError]
    EntityNotExistsException: Type[BotocoreClientError]
    FailedDependencyException: Type[BotocoreClientError]
    IllegalUserStateException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidCommentOperationException: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidPasswordException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ProhibitedStateException: Type[BotocoreClientError]
    RequestedEntityTooLargeException: Type[BotocoreClientError]
    ResourceAlreadyCheckedOutException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    StorageLimitExceededException: Type[BotocoreClientError]
    StorageLimitWillExceedException: Type[BotocoreClientError]
    TooManyLabelsException: Type[BotocoreClientError]
    TooManySubscriptionsException: Type[BotocoreClientError]
    UnauthorizedOperationException: Type[BotocoreClientError]
    UnauthorizedResourceAccessException: Type[BotocoreClientError]


class WorkDocsClient:
    """
    [WorkDocs.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def abort_document_version_upload(
        self, DocumentId: str, VersionId: str, AuthenticationToken: str = None
    ) -> None:
        """
        [Client.abort_document_version_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.abort_document_version_upload)
        """

    def activate_user(
        self, UserId: str, AuthenticationToken: str = None
    ) -> ActivateUserResponseTypeDef:
        """
        [Client.activate_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.activate_user)
        """

    def add_resource_permissions(
        self,
        ResourceId: str,
        Principals: List[SharePrincipalTypeDef],
        AuthenticationToken: str = None,
        NotificationOptions: NotificationOptionsTypeDef = None,
    ) -> AddResourcePermissionsResponseTypeDef:
        """
        [Client.add_resource_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.add_resource_permissions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.can_paginate)
        """

    def create_comment(
        self,
        DocumentId: str,
        VersionId: str,
        Text: str,
        AuthenticationToken: str = None,
        ParentId: str = None,
        ThreadId: str = None,
        Visibility: Literal["PUBLIC", "PRIVATE"] = None,
        NotifyCollaborators: bool = None,
    ) -> CreateCommentResponseTypeDef:
        """
        [Client.create_comment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.create_comment)
        """

    def create_custom_metadata(
        self,
        ResourceId: str,
        CustomMetadata: Dict[str, str],
        AuthenticationToken: str = None,
        VersionId: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_custom_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.create_custom_metadata)
        """

    def create_folder(
        self, ParentFolderId: str, AuthenticationToken: str = None, Name: str = None
    ) -> CreateFolderResponseTypeDef:
        """
        [Client.create_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.create_folder)
        """

    def create_labels(
        self, ResourceId: str, Labels: List[str], AuthenticationToken: str = None
    ) -> Dict[str, Any]:
        """
        [Client.create_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.create_labels)
        """

    def create_notification_subscription(
        self,
        OrganizationId: str,
        Endpoint: str,
        Protocol: Literal["HTTPS"],
        SubscriptionType: Literal["ALL"],
    ) -> CreateNotificationSubscriptionResponseTypeDef:
        """
        [Client.create_notification_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.create_notification_subscription)
        """

    def create_user(
        self,
        Username: str,
        GivenName: str,
        Surname: str,
        Password: str,
        OrganizationId: str = None,
        EmailAddress: str = None,
        TimeZoneId: str = None,
        StorageRule: "StorageRuleTypeTypeDef" = None,
        AuthenticationToken: str = None,
    ) -> CreateUserResponseTypeDef:
        """
        [Client.create_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.create_user)
        """

    def deactivate_user(self, UserId: str, AuthenticationToken: str = None) -> None:
        """
        [Client.deactivate_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.deactivate_user)
        """

    def delete_comment(
        self, DocumentId: str, VersionId: str, CommentId: str, AuthenticationToken: str = None
    ) -> None:
        """
        [Client.delete_comment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.delete_comment)
        """

    def delete_custom_metadata(
        self,
        ResourceId: str,
        AuthenticationToken: str = None,
        VersionId: str = None,
        Keys: List[str] = None,
        DeleteAll: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.delete_custom_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.delete_custom_metadata)
        """

    def delete_document(self, DocumentId: str, AuthenticationToken: str = None) -> None:
        """
        [Client.delete_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.delete_document)
        """

    def delete_folder(self, FolderId: str, AuthenticationToken: str = None) -> None:
        """
        [Client.delete_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.delete_folder)
        """

    def delete_folder_contents(self, FolderId: str, AuthenticationToken: str = None) -> None:
        """
        [Client.delete_folder_contents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.delete_folder_contents)
        """

    def delete_labels(
        self,
        ResourceId: str,
        AuthenticationToken: str = None,
        Labels: List[str] = None,
        DeleteAll: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.delete_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.delete_labels)
        """

    def delete_notification_subscription(self, SubscriptionId: str, OrganizationId: str) -> None:
        """
        [Client.delete_notification_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.delete_notification_subscription)
        """

    def delete_user(self, UserId: str, AuthenticationToken: str = None) -> None:
        """
        [Client.delete_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.delete_user)
        """

    def describe_activities(
        self,
        AuthenticationToken: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        OrganizationId: str = None,
        ActivityTypes: str = None,
        ResourceId: str = None,
        UserId: str = None,
        IncludeIndirectActivities: bool = None,
        Limit: int = None,
        Marker: str = None,
    ) -> DescribeActivitiesResponseTypeDef:
        """
        [Client.describe_activities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.describe_activities)
        """

    def describe_comments(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        Limit: int = None,
        Marker: str = None,
    ) -> DescribeCommentsResponseTypeDef:
        """
        [Client.describe_comments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.describe_comments)
        """

    def describe_document_versions(
        self,
        DocumentId: str,
        AuthenticationToken: str = None,
        Marker: str = None,
        Limit: int = None,
        Include: str = None,
        Fields: str = None,
    ) -> DescribeDocumentVersionsResponseTypeDef:
        """
        [Client.describe_document_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.describe_document_versions)
        """

    def describe_folder_contents(
        self,
        FolderId: str,
        AuthenticationToken: str = None,
        Sort: Literal["DATE", "NAME"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        Limit: int = None,
        Marker: str = None,
        Type: Literal["ALL", "DOCUMENT", "FOLDER"] = None,
        Include: str = None,
    ) -> DescribeFolderContentsResponseTypeDef:
        """
        [Client.describe_folder_contents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.describe_folder_contents)
        """

    def describe_groups(
        self,
        SearchQuery: str,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        Marker: str = None,
        Limit: int = None,
    ) -> DescribeGroupsResponseTypeDef:
        """
        [Client.describe_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.describe_groups)
        """

    def describe_notification_subscriptions(
        self, OrganizationId: str, Marker: str = None, Limit: int = None
    ) -> DescribeNotificationSubscriptionsResponseTypeDef:
        """
        [Client.describe_notification_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.describe_notification_subscriptions)
        """

    def describe_resource_permissions(
        self,
        ResourceId: str,
        AuthenticationToken: str = None,
        PrincipalId: str = None,
        Limit: int = None,
        Marker: str = None,
    ) -> DescribeResourcePermissionsResponseTypeDef:
        """
        [Client.describe_resource_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.describe_resource_permissions)
        """

    def describe_root_folders(
        self, AuthenticationToken: str, Limit: int = None, Marker: str = None
    ) -> DescribeRootFoldersResponseTypeDef:
        """
        [Client.describe_root_folders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.describe_root_folders)
        """

    def describe_users(
        self,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        UserIds: str = None,
        Query: str = None,
        Include: Literal["ALL", "ACTIVE_PENDING"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        Sort: Literal[
            "USER_NAME", "FULL_NAME", "STORAGE_LIMIT", "USER_STATUS", "STORAGE_USED"
        ] = None,
        Marker: str = None,
        Limit: int = None,
        Fields: str = None,
    ) -> DescribeUsersResponseTypeDef:
        """
        [Client.describe_users documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.describe_users)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.generate_presigned_url)
        """

    def get_current_user(self, AuthenticationToken: str) -> GetCurrentUserResponseTypeDef:
        """
        [Client.get_current_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.get_current_user)
        """

    def get_document(
        self, DocumentId: str, AuthenticationToken: str = None, IncludeCustomMetadata: bool = None
    ) -> GetDocumentResponseTypeDef:
        """
        [Client.get_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.get_document)
        """

    def get_document_path(
        self,
        DocumentId: str,
        AuthenticationToken: str = None,
        Limit: int = None,
        Fields: str = None,
        Marker: str = None,
    ) -> GetDocumentPathResponseTypeDef:
        """
        [Client.get_document_path documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.get_document_path)
        """

    def get_document_version(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        Fields: str = None,
        IncludeCustomMetadata: bool = None,
    ) -> GetDocumentVersionResponseTypeDef:
        """
        [Client.get_document_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.get_document_version)
        """

    def get_folder(
        self, FolderId: str, AuthenticationToken: str = None, IncludeCustomMetadata: bool = None
    ) -> GetFolderResponseTypeDef:
        """
        [Client.get_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.get_folder)
        """

    def get_folder_path(
        self,
        FolderId: str,
        AuthenticationToken: str = None,
        Limit: int = None,
        Fields: str = None,
        Marker: str = None,
    ) -> GetFolderPathResponseTypeDef:
        """
        [Client.get_folder_path documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.get_folder_path)
        """

    def get_resources(
        self,
        AuthenticationToken: str = None,
        UserId: str = None,
        CollectionType: Literal["SHARED_WITH_ME"] = None,
        Limit: int = None,
        Marker: str = None,
    ) -> GetResourcesResponseTypeDef:
        """
        [Client.get_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.get_resources)
        """

    def initiate_document_version_upload(
        self,
        ParentFolderId: str,
        AuthenticationToken: str = None,
        Id: str = None,
        Name: str = None,
        ContentCreatedTimestamp: datetime = None,
        ContentModifiedTimestamp: datetime = None,
        ContentType: str = None,
        DocumentSizeInBytes: int = None,
    ) -> InitiateDocumentVersionUploadResponseTypeDef:
        """
        [Client.initiate_document_version_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.initiate_document_version_upload)
        """

    def remove_all_resource_permissions(
        self, ResourceId: str, AuthenticationToken: str = None
    ) -> None:
        """
        [Client.remove_all_resource_permissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.remove_all_resource_permissions)
        """

    def remove_resource_permission(
        self,
        ResourceId: str,
        PrincipalId: str,
        AuthenticationToken: str = None,
        PrincipalType: Literal["USER", "GROUP", "INVITE", "ANONYMOUS", "ORGANIZATION"] = None,
    ) -> None:
        """
        [Client.remove_resource_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.remove_resource_permission)
        """

    def update_document(
        self,
        DocumentId: str,
        AuthenticationToken: str = None,
        Name: str = None,
        ParentFolderId: str = None,
        ResourceState: Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"] = None,
    ) -> None:
        """
        [Client.update_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.update_document)
        """

    def update_document_version(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        VersionStatus: Literal["ACTIVE"] = None,
    ) -> None:
        """
        [Client.update_document_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.update_document_version)
        """

    def update_folder(
        self,
        FolderId: str,
        AuthenticationToken: str = None,
        Name: str = None,
        ParentFolderId: str = None,
        ResourceState: Literal["ACTIVE", "RESTORING", "RECYCLING", "RECYCLED"] = None,
    ) -> None:
        """
        [Client.update_folder documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.update_folder)
        """

    def update_user(
        self,
        UserId: str,
        AuthenticationToken: str = None,
        GivenName: str = None,
        Surname: str = None,
        Type: Literal["USER", "ADMIN", "POWERUSER", "MINIMALUSER", "WORKSPACESUSER"] = None,
        StorageRule: "StorageRuleTypeTypeDef" = None,
        TimeZoneId: str = None,
        Locale: Literal[
            "en", "fr", "ko", "de", "es", "ja", "ru", "zh_CN", "zh_TW", "pt_BR", "default"
        ] = None,
        GrantPoweruserPrivileges: Literal["TRUE", "FALSE"] = None,
    ) -> UpdateUserResponseTypeDef:
        """
        [Client.update_user documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Client.update_user)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_activities"]
    ) -> DescribeActivitiesPaginator:
        """
        [Paginator.DescribeActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeActivities)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_comments"]
    ) -> DescribeCommentsPaginator:
        """
        [Paginator.DescribeComments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeComments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_document_versions"]
    ) -> DescribeDocumentVersionsPaginator:
        """
        [Paginator.DescribeDocumentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeDocumentVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_folder_contents"]
    ) -> DescribeFolderContentsPaginator:
        """
        [Paginator.DescribeFolderContents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeFolderContents)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_groups"]) -> DescribeGroupsPaginator:
        """
        [Paginator.DescribeGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_notification_subscriptions"]
    ) -> DescribeNotificationSubscriptionsPaginator:
        """
        [Paginator.DescribeNotificationSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeNotificationSubscriptions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_resource_permissions"]
    ) -> DescribeResourcePermissionsPaginator:
        """
        [Paginator.DescribeResourcePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeResourcePermissions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_root_folders"]
    ) -> DescribeRootFoldersPaginator:
        """
        [Paginator.DescribeRootFolders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeRootFolders)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_users"]) -> DescribeUsersPaginator:
        """
        [Paginator.DescribeUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeUsers)
        """
