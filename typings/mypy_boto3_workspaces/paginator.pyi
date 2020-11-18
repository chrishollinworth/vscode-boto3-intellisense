# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for workspaces service client paginators.

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
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_workspaces.type_defs import (
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


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
    [Paginator.DescribeAccountModifications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAccountModificationsResultTypeDef]:
        """
        [DescribeAccountModifications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeAccountModifications.paginate)
        """


class DescribeIpGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeIpGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups)
    """

    def paginate(
        self, GroupIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeIpGroupsResultTypeDef]:
        """
        [DescribeIpGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeIpGroups.paginate)
        """


class DescribeWorkspaceBundlesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeWorkspaceBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles)
    """

    def paginate(
        self,
        BundleIds: List[str] = None,
        Owner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeWorkspaceBundlesResultTypeDef]:
        """
        [DescribeWorkspaceBundles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceBundles.paginate)
        """


class DescribeWorkspaceDirectoriesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeWorkspaceDirectories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories)
    """

    def paginate(
        self,
        DirectoryIds: List[str] = None,
        Limit: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeWorkspaceDirectoriesResultTypeDef]:
        """
        [DescribeWorkspaceDirectories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories.paginate)
        """


class DescribeWorkspaceImagesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeWorkspaceImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages)
    """

    def paginate(
        self,
        ImageIds: List[str] = None,
        ImageType: Literal["OWNED", "SHARED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeWorkspaceImagesResultTypeDef]:
        """
        [DescribeWorkspaceImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaceImages.paginate)
        """


class DescribeWorkspacesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeWorkspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces)
    """

    def paginate(
        self,
        WorkspaceIds: List[str] = None,
        DirectoryId: str = None,
        UserName: str = None,
        BundleId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeWorkspacesResultTypeDef]:
        """
        [DescribeWorkspaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspaces.paginate)
        """


class DescribeWorkspacesConnectionStatusPaginator(Boto3Paginator):
    """
    [Paginator.DescribeWorkspacesConnectionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus)
    """

    def paginate(
        self, WorkspaceIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeWorkspacesConnectionStatusResultTypeDef]:
        """
        [DescribeWorkspacesConnectionStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus.paginate)
        """


class ListAvailableManagementCidrRangesPaginator(Boto3Paginator):
    """
    [Paginator.ListAvailableManagementCidrRanges documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges)
    """

    def paginate(
        self, ManagementCidrRangeConstraint: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAvailableManagementCidrRangesResultTypeDef]:
        """
        [ListAvailableManagementCidrRanges.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/workspaces.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges.paginate)
        """
