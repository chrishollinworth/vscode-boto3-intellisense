"""
Main interface for grafana service.

Usage::

    ```python
    import boto3
    from mypy_boto3_grafana import (
        Client,
        ListPermissionsPaginator,
        ListWorkspacesPaginator,
        ManagedGrafanaClient,
    )

    session = boto3.Session()

    client: ManagedGrafanaClient = boto3.client("grafana")
    session_client: ManagedGrafanaClient = session.client("grafana")

    list_permissions_paginator: ListPermissionsPaginator = client.get_paginator("list_permissions")
    list_workspaces_paginator: ListWorkspacesPaginator = client.get_paginator("list_workspaces")
    ```
"""
from .client import ManagedGrafanaClient
from .paginator import ListPermissionsPaginator, ListWorkspacesPaginator

Client = ManagedGrafanaClient

__all__ = ("Client", "ListPermissionsPaginator", "ListWorkspacesPaginator", "ManagedGrafanaClient")
