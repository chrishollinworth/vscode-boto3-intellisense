"""
Type annotations for workspaces service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_workspaces.client import WorkSpacesClient
    from mypy_boto3_workspaces.paginator import (
        DescribeAccountModificationsPaginator,
        DescribeIpGroupsPaginator,
        DescribeWorkspaceBundlesPaginator,
        DescribeWorkspaceDirectoriesPaginator,
        DescribeWorkspaceImagesPaginator,
        DescribeWorkspacesConnectionStatusPaginator,
        DescribeWorkspacesPaginator,
        ListAccountLinksPaginator,
        ListAvailableManagementCidrRangesPaginator,
    )

    session = Session()
    client: WorkSpacesClient = session.client("workspaces")

    describe_account_modifications_paginator: DescribeAccountModificationsPaginator = client.get_paginator("describe_account_modifications")
    describe_ip_groups_paginator: DescribeIpGroupsPaginator = client.get_paginator("describe_ip_groups")
    describe_workspace_bundles_paginator: DescribeWorkspaceBundlesPaginator = client.get_paginator("describe_workspace_bundles")
    describe_workspace_directories_paginator: DescribeWorkspaceDirectoriesPaginator = client.get_paginator("describe_workspace_directories")
    describe_workspace_images_paginator: DescribeWorkspaceImagesPaginator = client.get_paginator("describe_workspace_images")
    describe_workspaces_connection_status_paginator: DescribeWorkspacesConnectionStatusPaginator = client.get_paginator("describe_workspaces_connection_status")
    describe_workspaces_paginator: DescribeWorkspacesPaginator = client.get_paginator("describe_workspaces")
    list_account_links_paginator: ListAccountLinksPaginator = client.get_paginator("list_account_links")
    list_available_management_cidr_ranges_paginator: ListAvailableManagementCidrRangesPaginator = client.get_paginator("list_available_management_cidr_ranges")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeAccountModificationsRequestPaginateTypeDef,
    DescribeAccountModificationsResultTypeDef,
    DescribeIpGroupsRequestPaginateTypeDef,
    DescribeIpGroupsResultTypeDef,
    DescribeWorkspaceBundlesRequestPaginateTypeDef,
    DescribeWorkspaceBundlesResultTypeDef,
    DescribeWorkspaceDirectoriesRequestPaginateTypeDef,
    DescribeWorkspaceDirectoriesResultTypeDef,
    DescribeWorkspaceImagesRequestPaginateTypeDef,
    DescribeWorkspaceImagesResultTypeDef,
    DescribeWorkspacesConnectionStatusRequestPaginateTypeDef,
    DescribeWorkspacesConnectionStatusResultTypeDef,
    DescribeWorkspacesRequestPaginateTypeDef,
    DescribeWorkspacesResultTypeDef,
    ListAccountLinksRequestPaginateTypeDef,
    ListAccountLinksResultTypeDef,
    ListAvailableManagementCidrRangesRequestPaginateTypeDef,
    ListAvailableManagementCidrRangesResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeAccountModificationsPaginator",
    "DescribeIpGroupsPaginator",
    "DescribeWorkspaceBundlesPaginator",
    "DescribeWorkspaceDirectoriesPaginator",
    "DescribeWorkspaceImagesPaginator",
    "DescribeWorkspacesConnectionStatusPaginator",
    "DescribeWorkspacesPaginator",
    "ListAccountLinksPaginator",
    "ListAvailableManagementCidrRangesPaginator",
)

if TYPE_CHECKING:
    _DescribeAccountModificationsPaginatorBase = Paginator[
        DescribeAccountModificationsResultTypeDef
    ]
else:
    _DescribeAccountModificationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAccountModificationsPaginator(_DescribeAccountModificationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/DescribeAccountModifications.html#WorkSpaces.Paginator.DescribeAccountModifications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#describeaccountmodificationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAccountModificationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeAccountModificationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/DescribeAccountModifications.html#WorkSpaces.Paginator.DescribeAccountModifications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#describeaccountmodificationspaginator)
        """

if TYPE_CHECKING:
    _DescribeIpGroupsPaginatorBase = Paginator[DescribeIpGroupsResultTypeDef]
else:
    _DescribeIpGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeIpGroupsPaginator(_DescribeIpGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/DescribeIpGroups.html#WorkSpaces.Paginator.DescribeIpGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#describeipgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeIpGroupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeIpGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/DescribeIpGroups.html#WorkSpaces.Paginator.DescribeIpGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#describeipgroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeWorkspaceBundlesPaginatorBase = Paginator[DescribeWorkspaceBundlesResultTypeDef]
else:
    _DescribeWorkspaceBundlesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeWorkspaceBundlesPaginator(_DescribeWorkspaceBundlesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/DescribeWorkspaceBundles.html#WorkSpaces.Paginator.DescribeWorkspaceBundles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#describeworkspacebundlespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeWorkspaceBundlesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeWorkspaceBundlesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/DescribeWorkspaceBundles.html#WorkSpaces.Paginator.DescribeWorkspaceBundles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#describeworkspacebundlespaginator)
        """

if TYPE_CHECKING:
    _DescribeWorkspaceDirectoriesPaginatorBase = Paginator[
        DescribeWorkspaceDirectoriesResultTypeDef
    ]
else:
    _DescribeWorkspaceDirectoriesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeWorkspaceDirectoriesPaginator(_DescribeWorkspaceDirectoriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/DescribeWorkspaceDirectories.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#describeworkspacedirectoriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeWorkspaceDirectoriesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeWorkspaceDirectoriesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/DescribeWorkspaceDirectories.html#WorkSpaces.Paginator.DescribeWorkspaceDirectories.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#describeworkspacedirectoriespaginator)
        """

if TYPE_CHECKING:
    _DescribeWorkspaceImagesPaginatorBase = Paginator[DescribeWorkspaceImagesResultTypeDef]
else:
    _DescribeWorkspaceImagesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeWorkspaceImagesPaginator(_DescribeWorkspaceImagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/DescribeWorkspaceImages.html#WorkSpaces.Paginator.DescribeWorkspaceImages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#describeworkspaceimagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeWorkspaceImagesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeWorkspaceImagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/DescribeWorkspaceImages.html#WorkSpaces.Paginator.DescribeWorkspaceImages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#describeworkspaceimagespaginator)
        """

if TYPE_CHECKING:
    _DescribeWorkspacesConnectionStatusPaginatorBase = Paginator[
        DescribeWorkspacesConnectionStatusResultTypeDef
    ]
else:
    _DescribeWorkspacesConnectionStatusPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeWorkspacesConnectionStatusPaginator(_DescribeWorkspacesConnectionStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/DescribeWorkspacesConnectionStatus.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#describeworkspacesconnectionstatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeWorkspacesConnectionStatusRequestPaginateTypeDef]
    ) -> PageIterator[DescribeWorkspacesConnectionStatusResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/DescribeWorkspacesConnectionStatus.html#WorkSpaces.Paginator.DescribeWorkspacesConnectionStatus.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#describeworkspacesconnectionstatuspaginator)
        """

if TYPE_CHECKING:
    _DescribeWorkspacesPaginatorBase = Paginator[DescribeWorkspacesResultTypeDef]
else:
    _DescribeWorkspacesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeWorkspacesPaginator(_DescribeWorkspacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/DescribeWorkspaces.html#WorkSpaces.Paginator.DescribeWorkspaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#describeworkspacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeWorkspacesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeWorkspacesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/DescribeWorkspaces.html#WorkSpaces.Paginator.DescribeWorkspaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#describeworkspacespaginator)
        """

if TYPE_CHECKING:
    _ListAccountLinksPaginatorBase = Paginator[ListAccountLinksResultTypeDef]
else:
    _ListAccountLinksPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccountLinksPaginator(_ListAccountLinksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/ListAccountLinks.html#WorkSpaces.Paginator.ListAccountLinks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#listaccountlinkspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccountLinksRequestPaginateTypeDef]
    ) -> PageIterator[ListAccountLinksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/ListAccountLinks.html#WorkSpaces.Paginator.ListAccountLinks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#listaccountlinkspaginator)
        """

if TYPE_CHECKING:
    _ListAvailableManagementCidrRangesPaginatorBase = Paginator[
        ListAvailableManagementCidrRangesResultTypeDef
    ]
else:
    _ListAvailableManagementCidrRangesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAvailableManagementCidrRangesPaginator(_ListAvailableManagementCidrRangesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/ListAvailableManagementCidrRanges.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#listavailablemanagementcidrrangespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAvailableManagementCidrRangesRequestPaginateTypeDef]
    ) -> PageIterator[ListAvailableManagementCidrRangesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces/paginator/ListAvailableManagementCidrRanges.html#WorkSpaces.Paginator.ListAvailableManagementCidrRanges.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/paginators/#listavailablemanagementcidrrangespaginator)
        """
