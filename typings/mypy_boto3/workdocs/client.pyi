"""
Type annotations for workdocs service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_workdocs.client import WorkDocsClient

    session = Session()
    client: WorkDocsClient = session.client("workdocs")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeActivitiesPaginator,
    DescribeCommentsPaginator,
    DescribeDocumentVersionsPaginator,
    DescribeFolderContentsPaginator,
    DescribeGroupsPaginator,
    DescribeNotificationSubscriptionsPaginator,
    DescribeResourcePermissionsPaginator,
    DescribeRootFoldersPaginator,
    DescribeUsersPaginator,
    SearchResourcesPaginator,
)
from .type_defs import (
    AbortDocumentVersionUploadRequestTypeDef,
    ActivateUserRequestTypeDef,
    ActivateUserResponseTypeDef,
    AddResourcePermissionsRequestTypeDef,
    AddResourcePermissionsResponseTypeDef,
    CreateCommentRequestTypeDef,
    CreateCommentResponseTypeDef,
    CreateCustomMetadataRequestTypeDef,
    CreateFolderRequestTypeDef,
    CreateFolderResponseTypeDef,
    CreateLabelsRequestTypeDef,
    CreateNotificationSubscriptionRequestTypeDef,
    CreateNotificationSubscriptionResponseTypeDef,
    CreateUserRequestTypeDef,
    CreateUserResponseTypeDef,
    DeactivateUserRequestTypeDef,
    DeleteCommentRequestTypeDef,
    DeleteCustomMetadataRequestTypeDef,
    DeleteDocumentRequestTypeDef,
    DeleteDocumentVersionRequestTypeDef,
    DeleteFolderContentsRequestTypeDef,
    DeleteFolderRequestTypeDef,
    DeleteLabelsRequestTypeDef,
    DeleteNotificationSubscriptionRequestTypeDef,
    DeleteUserRequestTypeDef,
    DescribeActivitiesRequestTypeDef,
    DescribeActivitiesResponseTypeDef,
    DescribeCommentsRequestTypeDef,
    DescribeCommentsResponseTypeDef,
    DescribeDocumentVersionsRequestTypeDef,
    DescribeDocumentVersionsResponseTypeDef,
    DescribeFolderContentsRequestTypeDef,
    DescribeFolderContentsResponseTypeDef,
    DescribeGroupsRequestTypeDef,
    DescribeGroupsResponseTypeDef,
    DescribeNotificationSubscriptionsRequestTypeDef,
    DescribeNotificationSubscriptionsResponseTypeDef,
    DescribeResourcePermissionsRequestTypeDef,
    DescribeResourcePermissionsResponseTypeDef,
    DescribeRootFoldersRequestTypeDef,
    DescribeRootFoldersResponseTypeDef,
    DescribeUsersRequestTypeDef,
    DescribeUsersResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetCurrentUserRequestTypeDef,
    GetCurrentUserResponseTypeDef,
    GetDocumentPathRequestTypeDef,
    GetDocumentPathResponseTypeDef,
    GetDocumentRequestTypeDef,
    GetDocumentResponseTypeDef,
    GetDocumentVersionRequestTypeDef,
    GetDocumentVersionResponseTypeDef,
    GetFolderPathRequestTypeDef,
    GetFolderPathResponseTypeDef,
    GetFolderRequestTypeDef,
    GetFolderResponseTypeDef,
    GetResourcesRequestTypeDef,
    GetResourcesResponseTypeDef,
    InitiateDocumentVersionUploadRequestTypeDef,
    InitiateDocumentVersionUploadResponseTypeDef,
    RemoveAllResourcePermissionsRequestTypeDef,
    RemoveResourcePermissionRequestTypeDef,
    RestoreDocumentVersionsRequestTypeDef,
    SearchResourcesRequestTypeDef,
    SearchResourcesResponseTypeDef,
    UpdateDocumentRequestTypeDef,
    UpdateDocumentVersionRequestTypeDef,
    UpdateFolderRequestTypeDef,
    UpdateUserRequestTypeDef,
    UpdateUserResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("WorkDocsClient",)

class Exceptions(BaseClientExceptions):
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

class WorkDocsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        WorkDocsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs.html#WorkDocs.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#generate_presigned_url)
        """

    def abort_document_version_upload(
        self, **kwargs: Unpack[AbortDocumentVersionUploadRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Aborts the upload of the specified document version that was previously
        initiated by <a>InitiateDocumentVersionUpload</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/abort_document_version_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#abort_document_version_upload)
        """

    def activate_user(
        self, **kwargs: Unpack[ActivateUserRequestTypeDef]
    ) -> ActivateUserResponseTypeDef:
        """
        Activates the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/activate_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#activate_user)
        """

    def add_resource_permissions(
        self, **kwargs: Unpack[AddResourcePermissionsRequestTypeDef]
    ) -> AddResourcePermissionsResponseTypeDef:
        """
        Creates a set of permissions for the specified folder or document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/add_resource_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#add_resource_permissions)
        """

    def create_comment(
        self, **kwargs: Unpack[CreateCommentRequestTypeDef]
    ) -> CreateCommentResponseTypeDef:
        """
        Adds a new comment to the specified document version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/create_comment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#create_comment)
        """

    def create_custom_metadata(
        self, **kwargs: Unpack[CreateCustomMetadataRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds one or more custom properties to the specified resource (a folder,
        document, or version).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/create_custom_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#create_custom_metadata)
        """

    def create_folder(
        self, **kwargs: Unpack[CreateFolderRequestTypeDef]
    ) -> CreateFolderResponseTypeDef:
        """
        Creates a folder with the specified name and parent folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/create_folder.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#create_folder)
        """

    def create_labels(self, **kwargs: Unpack[CreateLabelsRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified list of labels to the given resource (a document or folder).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/create_labels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#create_labels)
        """

    def create_notification_subscription(
        self, **kwargs: Unpack[CreateNotificationSubscriptionRequestTypeDef]
    ) -> CreateNotificationSubscriptionResponseTypeDef:
        """
        Configure Amazon WorkDocs to use Amazon SNS notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/create_notification_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#create_notification_subscription)
        """

    def create_user(self, **kwargs: Unpack[CreateUserRequestTypeDef]) -> CreateUserResponseTypeDef:
        """
        Creates a user in a Simple AD or Microsoft AD directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/create_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#create_user)
        """

    def deactivate_user(
        self, **kwargs: Unpack[DeactivateUserRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deactivates the specified user, which revokes the user's access to Amazon
        WorkDocs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/deactivate_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#deactivate_user)
        """

    def delete_comment(
        self, **kwargs: Unpack[DeleteCommentRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified comment from the document version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/delete_comment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#delete_comment)
        """

    def delete_custom_metadata(
        self, **kwargs: Unpack[DeleteCustomMetadataRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes custom metadata from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/delete_custom_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#delete_custom_metadata)
        """

    def delete_document(
        self, **kwargs: Unpack[DeleteDocumentRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Permanently deletes the specified document and its associated metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/delete_document.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#delete_document)
        """

    def delete_document_version(
        self, **kwargs: Unpack[DeleteDocumentVersionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a specific version of a document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/delete_document_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#delete_document_version)
        """

    def delete_folder(
        self, **kwargs: Unpack[DeleteFolderRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Permanently deletes the specified folder and its contents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/delete_folder.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#delete_folder)
        """

    def delete_folder_contents(
        self, **kwargs: Unpack[DeleteFolderContentsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the contents of the specified folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/delete_folder_contents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#delete_folder_contents)
        """

    def delete_labels(self, **kwargs: Unpack[DeleteLabelsRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified list of labels from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/delete_labels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#delete_labels)
        """

    def delete_notification_subscription(
        self, **kwargs: Unpack[DeleteNotificationSubscriptionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified subscription from the specified organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/delete_notification_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#delete_notification_subscription)
        """

    def delete_user(
        self, **kwargs: Unpack[DeleteUserRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified user from a Simple AD or Microsoft AD directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/delete_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#delete_user)
        """

    def describe_activities(
        self, **kwargs: Unpack[DescribeActivitiesRequestTypeDef]
    ) -> DescribeActivitiesResponseTypeDef:
        """
        Describes the user activities in a specified time period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/describe_activities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#describe_activities)
        """

    def describe_comments(
        self, **kwargs: Unpack[DescribeCommentsRequestTypeDef]
    ) -> DescribeCommentsResponseTypeDef:
        """
        List all the comments for the specified document version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/describe_comments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#describe_comments)
        """

    def describe_document_versions(
        self, **kwargs: Unpack[DescribeDocumentVersionsRequestTypeDef]
    ) -> DescribeDocumentVersionsResponseTypeDef:
        """
        Retrieves the document versions for the specified document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/describe_document_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#describe_document_versions)
        """

    def describe_folder_contents(
        self, **kwargs: Unpack[DescribeFolderContentsRequestTypeDef]
    ) -> DescribeFolderContentsResponseTypeDef:
        """
        Describes the contents of the specified folder, including its documents and
        subfolders.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/describe_folder_contents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#describe_folder_contents)
        """

    def describe_groups(
        self, **kwargs: Unpack[DescribeGroupsRequestTypeDef]
    ) -> DescribeGroupsResponseTypeDef:
        """
        Describes the groups specified by the query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/describe_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#describe_groups)
        """

    def describe_notification_subscriptions(
        self, **kwargs: Unpack[DescribeNotificationSubscriptionsRequestTypeDef]
    ) -> DescribeNotificationSubscriptionsResponseTypeDef:
        """
        Lists the specified notification subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/describe_notification_subscriptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#describe_notification_subscriptions)
        """

    def describe_resource_permissions(
        self, **kwargs: Unpack[DescribeResourcePermissionsRequestTypeDef]
    ) -> DescribeResourcePermissionsResponseTypeDef:
        """
        Describes the permissions of a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/describe_resource_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#describe_resource_permissions)
        """

    def describe_root_folders(
        self, **kwargs: Unpack[DescribeRootFoldersRequestTypeDef]
    ) -> DescribeRootFoldersResponseTypeDef:
        """
        Describes the current user's special folders; the <code>RootFolder</code> and
        the <code>RecycleBin</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/describe_root_folders.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#describe_root_folders)
        """

    def describe_users(
        self, **kwargs: Unpack[DescribeUsersRequestTypeDef]
    ) -> DescribeUsersResponseTypeDef:
        """
        Describes the specified users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/describe_users.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#describe_users)
        """

    def get_current_user(
        self, **kwargs: Unpack[GetCurrentUserRequestTypeDef]
    ) -> GetCurrentUserResponseTypeDef:
        """
        Retrieves details of the current user for whom the authentication token was
        generated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_current_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_current_user)
        """

    def get_document(
        self, **kwargs: Unpack[GetDocumentRequestTypeDef]
    ) -> GetDocumentResponseTypeDef:
        """
        Retrieves details of a document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_document.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_document)
        """

    def get_document_path(
        self, **kwargs: Unpack[GetDocumentPathRequestTypeDef]
    ) -> GetDocumentPathResponseTypeDef:
        """
        Retrieves the path information (the hierarchy from the root folder) for the
        requested document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_document_path.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_document_path)
        """

    def get_document_version(
        self, **kwargs: Unpack[GetDocumentVersionRequestTypeDef]
    ) -> GetDocumentVersionResponseTypeDef:
        """
        Retrieves version metadata for the specified document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_document_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_document_version)
        """

    def get_folder(self, **kwargs: Unpack[GetFolderRequestTypeDef]) -> GetFolderResponseTypeDef:
        """
        Retrieves the metadata of the specified folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_folder.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_folder)
        """

    def get_folder_path(
        self, **kwargs: Unpack[GetFolderPathRequestTypeDef]
    ) -> GetFolderPathResponseTypeDef:
        """
        Retrieves the path information (the hierarchy from the root folder) for the
        specified folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_folder_path.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_folder_path)
        """

    def get_resources(
        self, **kwargs: Unpack[GetResourcesRequestTypeDef]
    ) -> GetResourcesResponseTypeDef:
        """
        Retrieves a collection of resources, including folders and documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_resources)
        """

    def initiate_document_version_upload(
        self, **kwargs: Unpack[InitiateDocumentVersionUploadRequestTypeDef]
    ) -> InitiateDocumentVersionUploadResponseTypeDef:
        """
        Creates a new document object and version object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/initiate_document_version_upload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#initiate_document_version_upload)
        """

    def remove_all_resource_permissions(
        self, **kwargs: Unpack[RemoveAllResourcePermissionsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes all the permissions from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/remove_all_resource_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#remove_all_resource_permissions)
        """

    def remove_resource_permission(
        self, **kwargs: Unpack[RemoveResourcePermissionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the permission for the specified principal from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/remove_resource_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#remove_resource_permission)
        """

    def restore_document_versions(
        self, **kwargs: Unpack[RestoreDocumentVersionsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Recovers a deleted version of an Amazon WorkDocs document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/restore_document_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#restore_document_versions)
        """

    def search_resources(
        self, **kwargs: Unpack[SearchResourcesRequestTypeDef]
    ) -> SearchResourcesResponseTypeDef:
        """
        Searches metadata and the content of folders, documents, document versions, and
        comments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/search_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#search_resources)
        """

    def update_document(
        self, **kwargs: Unpack[UpdateDocumentRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the specified attributes of a document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/update_document.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#update_document)
        """

    def update_document_version(
        self, **kwargs: Unpack[UpdateDocumentVersionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Changes the status of the document version to ACTIVE.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/update_document_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#update_document_version)
        """

    def update_folder(
        self, **kwargs: Unpack[UpdateFolderRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the specified attributes of the specified folder.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/update_folder.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#update_folder)
        """

    def update_user(self, **kwargs: Unpack[UpdateUserRequestTypeDef]) -> UpdateUserResponseTypeDef:
        """
        Updates the specified attributes of the specified user, and grants or revokes
        administrative privileges to the Amazon WorkDocs site.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/update_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#update_user)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_activities"]
    ) -> DescribeActivitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_comments"]
    ) -> DescribeCommentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_document_versions"]
    ) -> DescribeDocumentVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_folder_contents"]
    ) -> DescribeFolderContentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_groups"]
    ) -> DescribeGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_notification_subscriptions"]
    ) -> DescribeNotificationSubscriptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_resource_permissions"]
    ) -> DescribeResourcePermissionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_root_folders"]
    ) -> DescribeRootFoldersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_users"]
    ) -> DescribeUsersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_resources"]
    ) -> SearchResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/client/#get_paginator)
        """
