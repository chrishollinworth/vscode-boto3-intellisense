"""
Main interface for timestream-query service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_timestream_query import (
        Client,
        ListScheduledQueriesPaginator,
        ListTagsForResourcePaginator,
        QueryPaginator,
        TimestreamQueryClient,
    )

    session = Session()
    client: TimestreamQueryClient = session.client("timestream-query")

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
