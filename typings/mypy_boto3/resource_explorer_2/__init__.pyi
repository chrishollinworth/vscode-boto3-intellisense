"""
Main interface for resource-explorer-2 service.

Usage::

    ```python
    import boto3
    from mypy_boto3_resource_explorer_2 import (
        Client,
        ListIndexesPaginator,
        ListSupportedResourceTypesPaginator,
        ListViewsPaginator,
        ResourceExplorerClient,
        SearchPaginator,
    )

    session = boto3.Session()

    client: ResourceExplorerClient = boto3.client("resource-explorer-2")
    session_client: ResourceExplorerClient = session.client("resource-explorer-2")

    list_indexes_paginator: ListIndexesPaginator = client.get_paginator("list_indexes")
    list_supported_resource_types_paginator: ListSupportedResourceTypesPaginator = client.get_paginator("list_supported_resource_types")
    list_views_paginator: ListViewsPaginator = client.get_paginator("list_views")
    search_paginator: SearchPaginator = client.get_paginator("search")
    ```
"""
from .client import ResourceExplorerClient
from .paginator import (
    ListIndexesPaginator,
    ListSupportedResourceTypesPaginator,
    ListViewsPaginator,
    SearchPaginator,
)

Client = ResourceExplorerClient

__all__ = (
    "Client",
    "ListIndexesPaginator",
    "ListSupportedResourceTypesPaginator",
    "ListViewsPaginator",
    "ResourceExplorerClient",
    "SearchPaginator",
)
