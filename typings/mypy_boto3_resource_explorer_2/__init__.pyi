"""
Main interface for resource-explorer-2 service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_resource_explorer_2 import (
        Client,
        ListIndexesForMembersPaginator,
        ListIndexesPaginator,
        ListManagedViewsPaginator,
        ListResourcesPaginator,
        ListSupportedResourceTypesPaginator,
        ListViewsPaginator,
        ResourceExplorerClient,
        SearchPaginator,
    )

    session = Session()
    client: ResourceExplorerClient = session.client("resource-explorer-2")

    list_indexes_for_members_paginator: ListIndexesForMembersPaginator = client.get_paginator("list_indexes_for_members")
    list_indexes_paginator: ListIndexesPaginator = client.get_paginator("list_indexes")
    list_managed_views_paginator: ListManagedViewsPaginator = client.get_paginator("list_managed_views")
    list_resources_paginator: ListResourcesPaginator = client.get_paginator("list_resources")
    list_supported_resource_types_paginator: ListSupportedResourceTypesPaginator = client.get_paginator("list_supported_resource_types")
    list_views_paginator: ListViewsPaginator = client.get_paginator("list_views")
    search_paginator: SearchPaginator = client.get_paginator("search")
    ```
"""

from .client import ResourceExplorerClient
from .paginator import (
    ListIndexesForMembersPaginator,
    ListIndexesPaginator,
    ListManagedViewsPaginator,
    ListResourcesPaginator,
    ListSupportedResourceTypesPaginator,
    ListViewsPaginator,
    SearchPaginator,
)

Client = ResourceExplorerClient

__all__ = (
    "Client",
    "ListIndexesForMembersPaginator",
    "ListIndexesPaginator",
    "ListManagedViewsPaginator",
    "ListResourcesPaginator",
    "ListSupportedResourceTypesPaginator",
    "ListViewsPaginator",
    "ResourceExplorerClient",
    "SearchPaginator",
)
