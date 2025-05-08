"""
Main interface for grafana service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_grafana import (
        Client,
        ListPermissionsPaginator,
        ListVersionsPaginator,
        ListWorkspaceServiceAccountTokensPaginator,
        ListWorkspaceServiceAccountsPaginator,
        ListWorkspacesPaginator,
        ManagedGrafanaClient,
    )

    session = Session()
    client: ManagedGrafanaClient = session.client("grafana")

    list_permissions_paginator: ListPermissionsPaginator = client.get_paginator("list_permissions")
    list_versions_paginator: ListVersionsPaginator = client.get_paginator("list_versions")
    list_workspace_service_account_tokens_paginator: ListWorkspaceServiceAccountTokensPaginator = client.get_paginator("list_workspace_service_account_tokens")
    list_workspace_service_accounts_paginator: ListWorkspaceServiceAccountsPaginator = client.get_paginator("list_workspace_service_accounts")
    list_workspaces_paginator: ListWorkspacesPaginator = client.get_paginator("list_workspaces")
    ```
"""

from .client import ManagedGrafanaClient
from .paginator import (
    ListPermissionsPaginator,
    ListVersionsPaginator,
    ListWorkspaceServiceAccountsPaginator,
    ListWorkspaceServiceAccountTokensPaginator,
    ListWorkspacesPaginator,
)

Client = ManagedGrafanaClient

__all__ = (
    "Client",
    "ListPermissionsPaginator",
    "ListVersionsPaginator",
    "ListWorkspaceServiceAccountTokensPaginator",
    "ListWorkspaceServiceAccountsPaginator",
    "ListWorkspacesPaginator",
    "ManagedGrafanaClient",
)
