"""
Main interface for resource-groups service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_resource_groups import (
        Client,
        ListGroupResourcesPaginator,
        ListGroupingStatusesPaginator,
        ListGroupsPaginator,
        ListTagSyncTasksPaginator,
        ResourceGroupsClient,
        SearchResourcesPaginator,
    )

    session = Session()
    client: ResourceGroupsClient = session.client("resource-groups")

    list_group_resources_paginator: ListGroupResourcesPaginator = client.get_paginator("list_group_resources")
    list_grouping_statuses_paginator: ListGroupingStatusesPaginator = client.get_paginator("list_grouping_statuses")
    list_groups_paginator: ListGroupsPaginator = client.get_paginator("list_groups")
    list_tag_sync_tasks_paginator: ListTagSyncTasksPaginator = client.get_paginator("list_tag_sync_tasks")
    search_resources_paginator: SearchResourcesPaginator = client.get_paginator("search_resources")
    ```
"""

from .client import ResourceGroupsClient
from .paginator import (
    ListGroupingStatusesPaginator,
    ListGroupResourcesPaginator,
    ListGroupsPaginator,
    ListTagSyncTasksPaginator,
    SearchResourcesPaginator,
)

Client = ResourceGroupsClient

__all__ = (
    "Client",
    "ListGroupResourcesPaginator",
    "ListGroupingStatusesPaginator",
    "ListGroupsPaginator",
    "ListTagSyncTasksPaginator",
    "ResourceGroupsClient",
    "SearchResourcesPaginator",
)
