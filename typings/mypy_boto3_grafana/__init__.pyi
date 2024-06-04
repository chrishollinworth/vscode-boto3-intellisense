"""
Main interface for grafana service.

Usage::

    ```python
    import boto3
    from mypy_boto3_grafana import (
        Client,
        ListPermissionsPaginator,
        ListVersionsPaginator,
        ListWorkspaceServiceAccountTokensPaginator,
        ListWorkspaceServiceAccountsPaginator,
        ListWorkspacesPaginator,
        ManagedGrafanaClient,
    )

    session = boto3.Session()

    client: ManagedGrafanaClient = boto3.client("grafana")
    session_client: ManagedGrafanaClient = session.client("grafana")

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
