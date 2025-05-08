"""
Main interface for workspaces service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_workspaces import (
        Client,
        DescribeAccountModificationsPaginator,
        DescribeIpGroupsPaginator,
        DescribeWorkspaceBundlesPaginator,
        DescribeWorkspaceDirectoriesPaginator,
        DescribeWorkspaceImagesPaginator,
        DescribeWorkspacesConnectionStatusPaginator,
        DescribeWorkspacesPaginator,
        ListAccountLinksPaginator,
        ListAvailableManagementCidrRangesPaginator,
        WorkSpacesClient,
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

from .client import WorkSpacesClient
from .paginator import (
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

Client = WorkSpacesClient

__all__ = (
    "Client",
    "DescribeAccountModificationsPaginator",
    "DescribeIpGroupsPaginator",
    "DescribeWorkspaceBundlesPaginator",
    "DescribeWorkspaceDirectoriesPaginator",
    "DescribeWorkspaceImagesPaginator",
    "DescribeWorkspacesConnectionStatusPaginator",
    "DescribeWorkspacesPaginator",
    "ListAccountLinksPaginator",
    "ListAvailableManagementCidrRangesPaginator",
    "WorkSpacesClient",
)
