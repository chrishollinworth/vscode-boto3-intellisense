"""
Main interface for keyspaces service.

Usage::

    ```python
    import boto3
    from mypy_boto3_keyspaces import (
        Client,
        KeyspacesClient,
        ListKeyspacesPaginator,
        ListTablesPaginator,
        ListTagsForResourcePaginator,
    )

    session = boto3.Session()

    client: KeyspacesClient = boto3.client("keyspaces")
    session_client: KeyspacesClient = session.client("keyspaces")

    list_keyspaces_paginator: ListKeyspacesPaginator = client.get_paginator("list_keyspaces")
    list_tables_paginator: ListTablesPaginator = client.get_paginator("list_tables")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from .client import KeyspacesClient
from .paginator import ListKeyspacesPaginator, ListTablesPaginator, ListTagsForResourcePaginator

Client = KeyspacesClient

__all__ = (
    "Client",
    "KeyspacesClient",
    "ListKeyspacesPaginator",
    "ListTablesPaginator",
    "ListTagsForResourcePaginator",
)
