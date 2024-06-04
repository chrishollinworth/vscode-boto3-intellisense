"""
Type annotations for workdocs service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html)

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
        SearchResourcesPaginator,
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
    search_resources_paginator: SearchResourcesPaginator = client.get_paginator("search_resources")
    ```
"""

import sys
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    FolderContentTypeType,
    OrderTypeType,
    ResourceSortTypeType,
    SearchQueryScopeTypeType,
    UserFilterTypeType,
    UserSortTypeType,
)
from .type_defs import (
    DescribeActivitiesResponseTypeDef,
    DescribeCommentsResponseTypeDef,
    DescribeDocumentVersionsResponseTypeDef,
    DescribeFolderContentsResponseTypeDef,
    DescribeGroupsResponseTypeDef,
    DescribeNotificationSubscriptionsResponseTypeDef,
    DescribeResourcePermissionsResponseTypeDef,
    DescribeRootFoldersResponseTypeDef,
    DescribeUsersResponseTypeDef,
    FiltersTypeDef,
    PaginatorConfigTypeDef,
    SearchResourcesResponseTypeDef,
    SearchSortResultTypeDef,
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
    "SearchResourcesPaginator",
)

class DescribeActivitiesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeActivities)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describeactivitiespaginator)
    """

    def paginate(
        self,
        *,
        AuthenticationToken: str = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        OrganizationId: str = None,
        ActivityTypes: str = None,
        ResourceId: str = None,
        UserId: str = None,
        IncludeIndirectActivities: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeActivitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeActivities.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describeactivitiespaginator)
        """

class DescribeCommentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeComments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describecommentspaginator)
    """

    def paginate(
        self,
        *,
        DocumentId: str,
        VersionId: str,
        AuthenticationToken: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCommentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeComments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describecommentspaginator)
        """

class DescribeDocumentVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeDocumentVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describedocumentversionspaginator)
    """

    def paginate(
        self,
        *,
        DocumentId: str,
        AuthenticationToken: str = None,
        Include: str = None,
        Fields: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDocumentVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeDocumentVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describedocumentversionspaginator)
        """

class DescribeFolderContentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeFolderContents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describefoldercontentspaginator)
    """

    def paginate(
        self,
        *,
        FolderId: str,
        AuthenticationToken: str = None,
        Sort: ResourceSortTypeType = None,
        Order: OrderTypeType = None,
        Type: FolderContentTypeType = None,
        Include: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFolderContentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeFolderContents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describefoldercontentspaginator)
        """

class DescribeGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describegroupspaginator)
    """

    def paginate(
        self,
        *,
        SearchQuery: str,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describegroupspaginator)
        """

class DescribeNotificationSubscriptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeNotificationSubscriptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describenotificationsubscriptionspaginator)
    """

    def paginate(
        self, *, OrganizationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNotificationSubscriptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeNotificationSubscriptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describenotificationsubscriptionspaginator)
        """

class DescribeResourcePermissionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeResourcePermissions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describeresourcepermissionspaginator)
    """

    def paginate(
        self,
        *,
        ResourceId: str,
        AuthenticationToken: str = None,
        PrincipalId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeResourcePermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeResourcePermissions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describeresourcepermissionspaginator)
        """

class DescribeRootFoldersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeRootFolders)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describerootfolderspaginator)
    """

    def paginate(
        self, *, AuthenticationToken: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRootFoldersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeRootFolders.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describerootfolderspaginator)
        """

class DescribeUsersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeUsers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describeuserspaginator)
    """

    def paginate(
        self,
        *,
        AuthenticationToken: str = None,
        OrganizationId: str = None,
        UserIds: str = None,
        Query: str = None,
        Include: UserFilterTypeType = None,
        Order: OrderTypeType = None,
        Sort: UserSortTypeType = None,
        Fields: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeUsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.DescribeUsers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#describeuserspaginator)
        """

class SearchResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.SearchResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#searchresourcespaginator)
    """

    def paginate(
        self,
        *,
        AuthenticationToken: str = None,
        QueryText: str = None,
        QueryScopes: List[SearchQueryScopeTypeType] = None,
        OrganizationId: str = None,
        AdditionalResponseFields: List[Literal["WEBURL"]] = None,
        Filters: "FiltersTypeDef" = None,
        OrderBy: List["SearchSortResultTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/workdocs.html#WorkDocs.Paginator.SearchResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/paginators.html#searchresourcespaginator)
        """
