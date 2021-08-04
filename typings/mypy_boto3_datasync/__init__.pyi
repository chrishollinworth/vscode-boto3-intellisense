"""
Main interface for datasync service.

Usage::

    ```python
    import boto3
    from mypy_boto3_datasync import (
        Client,
        DataSyncClient,
        ListAgentsPaginator,
        ListLocationsPaginator,
        ListTagsForResourcePaginator,
        ListTaskExecutionsPaginator,
        ListTasksPaginator,
    )

    session = boto3.Session()

    client: DataSyncClient = boto3.client("datasync")
    session_client: DataSyncClient = session.client("datasync")

    list_agents_paginator: ListAgentsPaginator = client.get_paginator("list_agents")
    list_locations_paginator: ListLocationsPaginator = client.get_paginator("list_locations")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    list_task_executions_paginator: ListTaskExecutionsPaginator = client.get_paginator("list_task_executions")
    list_tasks_paginator: ListTasksPaginator = client.get_paginator("list_tasks")
    ```
"""
from .client import DataSyncClient
from .paginator import (
    ListAgentsPaginator,
    ListLocationsPaginator,
    ListTagsForResourcePaginator,
    ListTaskExecutionsPaginator,
    ListTasksPaginator,
)

Client = DataSyncClient

__all__ = (
    "Client",
    "DataSyncClient",
    "ListAgentsPaginator",
    "ListLocationsPaginator",
    "ListTagsForResourcePaginator",
    "ListTaskExecutionsPaginator",
    "ListTasksPaginator",
)
