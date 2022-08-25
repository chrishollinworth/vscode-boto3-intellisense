"""
Type annotations for workspaces service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_workspaces import WorkSpacesClient
    from mypy_boto3_workspaces.paginator import (
        DescribeAccountModificationsPaginator,
        DescribeIpGroupsPaginator,
        DescribeWorkspaceBundlesPaginator,
        DescribeWorkspaceDirectoriesPaginator,
        DescribeWorkspaceImagesPaginator,
        DescribeWorkspacesPaginator,
        DescribeWorkspacesConnectionStatusPaginator,
        ListAvailableManagementCidrRangesPaginator,
    )

    client: WorkSpacesClient = boto3.client("workspaces")

    describe_account_modifications_paginator: DescribeAccountModificationsPaginator = client.get_paginator("describe_account_modifications")
    describe_ip_groups_paginator: DescribeIpGroupsPaginator = client.get_paginator("describe_ip_groups")
    describe_workspace_bundles_paginator: DescribeWorkspaceBundlesPaginator = client.get_paginator("describe_workspace_bundles")
    describe_workspace_directories_paginator: DescribeWorkspaceDirectoriesPaginator = client.get_paginator("describe_workspace_directories")
    describe_workspace_images_paginator: DescribeWorkspaceImagesPaginator = client.get_paginator("describe_workspace_images")
    describe_workspaces_paginator: DescribeWorkspacesPaginator = client.get_paginator("describe_workspaces")
    describe_workspaces_connection_status_paginator: DescribeWorkspacesConnectionStatusPaginator = client.get_paginator("describe_workspaces_connection_status")
    list_available_management_cidr_ranges_paginator: ListAvailableManagementCidrRangesPaginator = client.get_paginator("list_available_management_cidr_ranges")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ImageTypeType
from .type_defs import (
    DescribeAccountModificationsResultTypeDef,
    DescribeIpGroupsResultTypeDef,
    DescribeWorkspaceBundlesResultTypeDef,
    DescribeWorkspaceDirectoriesResultTypeDef,
    DescribeWorkspaceImagesResultTypeDef,
    DescribeWorkspacesConnectionStatusResultTypeDef,
    DescribeWorkspacesResultTypeDef,
    ListAvailableManagementCidrRangesResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeAccountModificationsPaginator",
    "DescribeIpGroupsPaginator",
    "DescribeWorkspaceBundlesPaginator",
    "DescribeWorkspaceDirectoriesPaginator",
    "DescribeWorkspaceImagesPaginator",
    "DescribeWorkspacesPaginator",
    "DescribeWorkspacesConnectionStatusPaginator",
    "ListAvailableManagementCidrRangesPaginator",
)

class DescribeAccountModificationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeaccountmodificationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAccountModificationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeaccountmodificationspaginator)
        """

class DescribeIpGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeipgroupspaginator)
    """

    def paginate(
        self, *, GroupIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeIpGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeipgroupspaginator)
        """

class DescribeWorkspaceBundlesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacebundlespaginator)
    """

    def paginate(
        self,
        *,
        BundleIds: List[str] = None,
        Owner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeWorkspaceBundlesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacebundlespaginator)
        """

class DescribeWorkspaceDirectoriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacedirectoriespaginator)
    """

    def paginate(
        self,
        *,
        DirectoryIds: List[str] = None,
        Limit: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeWorkspaceDirectoriesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacedirectoriespaginator)
        """

class DescribeWorkspaceImagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspaceimagespaginator)
    """

    def paginate(
        self,
        *,
        ImageIds: List[str] = None,
        ImageType: ImageTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeWorkspaceImagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspaceimagespaginator)
        """

class DescribeWorkspacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacespaginator)
    """

    def paginate(
        self,
        *,
        WorkspaceIds: List[str] = None,
        DirectoryId: str = None,
        UserName: str = None,
        BundleId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeWorkspacesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacespaginator)
        """

class DescribeWorkspacesConnectionStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacesconnectionstatuspaginator)
    """

    def paginate(
        self, *, WorkspaceIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeWorkspacesConnectionStatusResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#describeworkspacesconnectionstatuspaginator)
        """

class ListAvailableManagementCidrRangesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#listavailablemanagementcidrrangespaginator)
    """

    def paginate(
        self, *, ManagementCidrRangeConstraint: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAvailableManagementCidrRangesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators.html#listavailablemanagementcidrrangespaginator)
        """
