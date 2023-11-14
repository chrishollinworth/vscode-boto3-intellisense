"""
Main interface for timestream-query service.

Usage::

    ```python
    import boto3
    from mypy_boto3_timestream_query import (
        Client,
        ListScheduledQueriesPaginator,
        ListTagsForResourcePaginator,
        QueryPaginator,
        TimestreamQueryClient,
    )

    session = boto3.Session()

    client: TimestreamQueryClient = boto3.client("timestream-query")
    session_client: TimestreamQueryClient = session.client("timestream-query")

    list_scheduled_queries_paginator: ListScheduledQueriesPaginator = client.get_paginator("list_scheduled_queries")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    query_paginator: QueryPaginator = client.get_paginator("query")
    ```
"""
from .client import TimestreamQueryClient
from .paginator import ListScheduledQueriesPaginator, ListTagsForResourcePaginator, QueryPaginator

Client = TimestreamQueryClient

__all__ = (
    "Client",
    "ListScheduledQueriesPaginator",
    "ListTagsForResourcePaginator",
    "QueryPaginator",
    "TimestreamQueryClient",
)
