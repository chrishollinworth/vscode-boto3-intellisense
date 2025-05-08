"""
Type annotations for workdocs service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_workdocs.client import WorkDocsClient
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
        SearchResourcesPaginator,
    )

    session = Session()
    client: WorkDocsClient = session.client("workdocs")

    describe_activities_paginator: DescribeActivitiesPaginator = client.get_paginator("describe_activities")
    describe_comments_paginator: DescribeCommentsPaginator = client.get_paginator("describe_comments")
    describe_document_versions_paginator: DescribeDocumentVersionsPaginator = client.get_paginator("describe_document_versions")
    describe_folder_contents_paginator: DescribeFolderContentsPaginator = client.get_paginator("describe_folder_contents")
    describe_groups_paginator: DescribeGroupsPaginator = client.get_paginator("describe_groups")
    describe_notification_subscriptions_paginator: DescribeNotificationSubscriptionsPaginator = client.get_paginator("describe_notification_subscriptions")
    describe_resource_permissions_paginator: DescribeResourcePermissionsPaginator = client.get_paginator("describe_resource_permissions")
    describe_root_folders_paginator: DescribeRootFoldersPaginator = client.get_paginator("describe_root_folders")
    describe_users_paginator: DescribeUsersPaginator = client.get_paginator("describe_users")
    search_resources_paginator: SearchResourcesPaginator = client.get_paginator("search_resources")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeActivitiesRequestPaginateTypeDef,
    DescribeActivitiesResponseTypeDef,
    DescribeCommentsRequestPaginateTypeDef,
    DescribeCommentsResponseTypeDef,
    DescribeDocumentVersionsRequestPaginateTypeDef,
    DescribeDocumentVersionsResponseTypeDef,
    DescribeFolderContentsRequestPaginateTypeDef,
    DescribeFolderContentsResponseTypeDef,
    DescribeGroupsRequestPaginateTypeDef,
    DescribeGroupsResponseTypeDef,
    DescribeNotificationSubscriptionsRequestPaginateTypeDef,
    DescribeNotificationSubscriptionsResponseTypeDef,
    DescribeResourcePermissionsRequestPaginateTypeDef,
    DescribeResourcePermissionsResponseTypeDef,
    DescribeRootFoldersRequestPaginateTypeDef,
    DescribeRootFoldersResponseTypeDef,
    DescribeUsersRequestPaginateTypeDef,
    DescribeUsersResponseTypeDef,
    SearchResourcesRequestPaginateTypeDef,
    SearchResourcesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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
    "SearchResourcesPaginator",
)

if TYPE_CHECKING:
    _DescribeActivitiesPaginatorBase = Paginator[DescribeActivitiesResponseTypeDef]
else:
    _DescribeActivitiesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeActivitiesPaginator(_DescribeActivitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeActivities.html#WorkDocs.Paginator.DescribeActivities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describeactivitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeActivitiesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeActivitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeActivities.html#WorkDocs.Paginator.DescribeActivities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describeactivitiespaginator)
        """

if TYPE_CHECKING:
    _DescribeCommentsPaginatorBase = Paginator[DescribeCommentsResponseTypeDef]
else:
    _DescribeCommentsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCommentsPaginator(_DescribeCommentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeComments.html#WorkDocs.Paginator.DescribeComments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describecommentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCommentsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeCommentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeComments.html#WorkDocs.Paginator.DescribeComments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describecommentspaginator)
        """

if TYPE_CHECKING:
    _DescribeDocumentVersionsPaginatorBase = Paginator[DescribeDocumentVersionsResponseTypeDef]
else:
    _DescribeDocumentVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDocumentVersionsPaginator(_DescribeDocumentVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeDocumentVersions.html#WorkDocs.Paginator.DescribeDocumentVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describedocumentversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDocumentVersionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDocumentVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeDocumentVersions.html#WorkDocs.Paginator.DescribeDocumentVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describedocumentversionspaginator)
        """

if TYPE_CHECKING:
    _DescribeFolderContentsPaginatorBase = Paginator[DescribeFolderContentsResponseTypeDef]
else:
    _DescribeFolderContentsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeFolderContentsPaginator(_DescribeFolderContentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeFolderContents.html#WorkDocs.Paginator.DescribeFolderContents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describefoldercontentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFolderContentsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeFolderContentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeFolderContents.html#WorkDocs.Paginator.DescribeFolderContents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describefoldercontentspaginator)
        """

if TYPE_CHECKING:
    _DescribeGroupsPaginatorBase = Paginator[DescribeGroupsResponseTypeDef]
else:
    _DescribeGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeGroupsPaginator(_DescribeGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeGroups.html#WorkDocs.Paginator.DescribeGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describegroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeGroupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeGroups.html#WorkDocs.Paginator.DescribeGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describegroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeNotificationSubscriptionsPaginatorBase = Paginator[
        DescribeNotificationSubscriptionsResponseTypeDef
    ]
else:
    _DescribeNotificationSubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeNotificationSubscriptionsPaginator(_DescribeNotificationSubscriptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeNotificationSubscriptions.html#WorkDocs.Paginator.DescribeNotificationSubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describenotificationsubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNotificationSubscriptionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeNotificationSubscriptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeNotificationSubscriptions.html#WorkDocs.Paginator.DescribeNotificationSubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describenotificationsubscriptionspaginator)
        """

if TYPE_CHECKING:
    _DescribeResourcePermissionsPaginatorBase = Paginator[
        DescribeResourcePermissionsResponseTypeDef
    ]
else:
    _DescribeResourcePermissionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeResourcePermissionsPaginator(_DescribeResourcePermissionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeResourcePermissions.html#WorkDocs.Paginator.DescribeResourcePermissions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describeresourcepermissionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeResourcePermissionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeResourcePermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeResourcePermissions.html#WorkDocs.Paginator.DescribeResourcePermissions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describeresourcepermissionspaginator)
        """

if TYPE_CHECKING:
    _DescribeRootFoldersPaginatorBase = Paginator[DescribeRootFoldersResponseTypeDef]
else:
    _DescribeRootFoldersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeRootFoldersPaginator(_DescribeRootFoldersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeRootFolders.html#WorkDocs.Paginator.DescribeRootFolders)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describerootfolderspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRootFoldersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeRootFoldersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeRootFolders.html#WorkDocs.Paginator.DescribeRootFolders.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describerootfolderspaginator)
        """

if TYPE_CHECKING:
    _DescribeUsersPaginatorBase = Paginator[DescribeUsersResponseTypeDef]
else:
    _DescribeUsersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeUsersPaginator(_DescribeUsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeUsers.html#WorkDocs.Paginator.DescribeUsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describeuserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeUsersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/DescribeUsers.html#WorkDocs.Paginator.DescribeUsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#describeuserspaginator)
        """

if TYPE_CHECKING:
    _SearchResourcesPaginatorBase = Paginator[SearchResourcesResponseTypeDef]
else:
    _SearchResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchResourcesPaginator(_SearchResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/SearchResources.html#WorkDocs.Paginator.SearchResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#searchresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchResourcesRequestPaginateTypeDef]
    ) -> PageIterator[SearchResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workdocs/paginator/SearchResources.html#WorkDocs.Paginator.SearchResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators/#searchresourcespaginator)
        """
