"""
Main interface for workspaces-instances service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_workspaces_instances import (
        Client,
        ListInstanceTypesPaginator,
        ListRegionsPaginator,
        ListWorkspaceInstancesPaginator,
        WorkspacesInstancesClient,
    )

    session = Session()
    client: WorkspacesInstancesClient = session.client("workspaces-instances")

    list_instance_types_paginator: ListInstanceTypesPaginator = client.get_paginator("list_instance_types")
    list_regions_paginator: ListRegionsPaginator = client.get_paginator("list_regions")
    list_workspace_instances_paginator: ListWorkspaceInstancesPaginator = client.get_paginator("list_workspace_instances")
    ```
"""

from .client import WorkspacesInstancesClient
from .paginator import (
    ListInstanceTypesPaginator,
    ListRegionsPaginator,
    ListWorkspaceInstancesPaginator,
)

Client = WorkspacesInstancesClient

__all__ = (
    "Client",
    "ListInstanceTypesPaginator",
    "ListRegionsPaginator",
    "ListWorkspaceInstancesPaginator",
    "WorkspacesInstancesClient",
)
