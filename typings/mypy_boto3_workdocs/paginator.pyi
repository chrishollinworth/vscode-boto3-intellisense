# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for workdocs service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_workdocs import WorkDocsClient
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

    client: WorkDocsClient = boto3.client("workdocs")

    describe_activities_paginator: DescribeActivitiesPaginator = client.get_paginator("describe_activities")
    describe_comments_paginator: DescribeCommentsPaginator = client.get_paginator("describe_comments")
    describe_document_versions_paginator: DescribeDocumentVersionsPaginator = client.get_paginator("describe_document_versions")
    describe_folder_contents_paginator: DescribeFolderContentsPaginator = client.get_paginator("describe_folder_contents")
    describe_groups_paginator: DescribeGroupsPaginator = client.get_paginator("describe_groups")
    describe_notification_subscriptions_paginator: DescribeNotificationSubscriptionsPaginator = client.get_paginator("describe_notification_subscriptions")
    describe_resource_permissions_paginator: DescribeResourcePermissionsPaginator = client.get_paginator("describe_resource_permissions")
    describe_root_folders_paginator: DescribeRootFoldersPaginator = client.get_paginator("describe_root_folders")
    describe_users_paginator: DescribeUsersPaginator = client.get_paginator("describe_users")
    ```
"""
import sys
from datetime import datetime
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_workdocs.type_defs import (
    DescribeActivitiesResponseTypeDef,
    DescribeCommentsResponseTypeDef,
    DescribeDocumentVersionsResponseTypeDef,
    DescribeFolderContentsResponseTypeDef,
    DescribeGroupsResponseTypeDef,
    DescribeNotificationSubscriptionsResponseTypeDef,
    DescribeResourcePermissionsResponseTypeDef,
    DescribeRootFoldersResponseTypeDef,
    DescribeUsersResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeActivitiesPaginator",
    "DescribeCommentsPaginator",
    "DescribeDocumentVersionsPaginator",
    "DescribeFolderContentsPaginator",
    "DescribeGroupsPaginator",
    "DescribeNotificationSubscriptionsPaginator",
    "DescribeResourcePermissionsPaginator",
    "DescribeRootFoldersPaginator",
    "DescribeUsersPaginator",
)


class DescribeActivitiesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeActivities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeActivities)
    """

    def paginate(
        self,
        AuthenticationToken: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        OrganizationId: str = None,
        ActivityTypes: str = None,
        ResourceId: str = None,
        UserId: str = None,
        IncludeIndirectActivities: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeActivitiesResponseTypeDef]:
        """
        [DescribeActivities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeActivities.paginate)
        """


class DescribeCommentsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeComments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeComments)
    """

    def paginate(
        self,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeCommentsResponseTypeDef]:
        """
        [DescribeComments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeComments.paginate)
        """


class DescribeDocumentVersionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDocumentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeDocumentVersions)
    """

    def paginate(
        self,
        DocumentId: str,
        AuthenticationToken: str = None,
        Include: str = None,
        Fields: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeDocumentVersionsResponseTypeDef]:
        """
        [DescribeDocumentVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeDocumentVersions.paginate)
        """


class DescribeFolderContentsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeFolderContents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeFolderContents)
    """

    def paginate(
        self,
        FolderId: str,
        AuthenticationToken: str = None,
        Sort: Literal["DATE", "NAME"] = None,
        Order: Literal["ASCENDING", "DESCENDING"] = None,
        Type: Literal["ALL", "DOCUMENT", "FOLDER"] = None,
        Include: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeFolderContentsResponseTypeDef]:
        """
        [DescribeFolderContents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeFolderContents.paginate)
        """


class DescribeGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeGroups)
    """

    def paginate(
        self,
        SearchQuery: str,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeGroupsResponseTypeDef]:
        """
        [DescribeGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeGroups.paginate)
        """


class DescribeNotificationSubscriptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeNotificationSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeNotificationSubscriptions)
    """

    def paginate(
        self, OrganizationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNotificationSubscriptionsResponseTypeDef]:
        """
        [DescribeNotificationSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeNotificationSubscriptions.paginate)
        """


class DescribeResourcePermissionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeResourcePermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeResourcePermissions)
    """

    def paginate(
        self,
        ResourceId: str,
        AuthenticationToken: str = None,
        PrincipalId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeResourcePermissionsResponseTypeDef]:
        """
        [DescribeResourcePermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeResourcePermissions.paginate)
        """


class DescribeRootFoldersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeRootFolders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeRootFolders)
    """

    def paginate(
        self, AuthenticationToken: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRootFoldersResponseTypeDef]:
        """
        [DescribeRootFolders.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeRootFolders.paginate)
        """


class DescribeUsersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeUsers)
    """

    def paginate(
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
        Fields: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeUsersResponseTypeDef]:
        """
        [DescribeUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workdocs.html#WorkDocs.Paginator.DescribeUsers.paginate)
        """
