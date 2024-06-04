"""
Main interface for finspace service.

Usage::

    ```python
    import boto3
    from mypy_boto3_finspace import (
        Client,
        ListKxEnvironmentsPaginator,
        finspaceClient,
    )

    session = boto3.Session()

    client: finspaceClient = boto3.client("finspace")
    session_client: finspaceClient = session.client("finspace")

    list_kx_environments_paginator: ListKxEnvironmentsPaginator = client.get_paginator("list_kx_environments")
    ```
"""

from .client import finspaceClient
from .paginator import ListKxEnvironmentsPaginator

Client = finspaceClient

__all__ = ("Client", "ListKxEnvironmentsPaginator", "finspaceClient")
