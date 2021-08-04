"""
Main interface for amp service.

Usage::

    ```python
    import boto3
    from mypy_boto3_amp import (
        Client,
        ListWorkspacesPaginator,
        PrometheusServiceClient,
    )

    session = boto3.Session()

    client: PrometheusServiceClient = boto3.client("amp")
    session_client: PrometheusServiceClient = session.client("amp")

    list_workspaces_paginator: ListWorkspacesPaginator = client.get_paginator("list_workspaces")
    ```
"""
from .client import PrometheusServiceClient
from .paginator import ListWorkspacesPaginator

Client = PrometheusServiceClient

__all__ = ("Client", "ListWorkspacesPaginator", "PrometheusServiceClient")
