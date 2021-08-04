"""
Main interface for timestream-query service.

Usage::

    ```python
    import boto3
    from mypy_boto3_timestream_query import (
        Client,
        QueryPaginator,
        TimestreamQueryClient,
    )

    session = boto3.Session()

    client: TimestreamQueryClient = boto3.client("timestream-query")
    session_client: TimestreamQueryClient = session.client("timestream-query")

    query_paginator: QueryPaginator = client.get_paginator("query")
    ```
"""
from .client import TimestreamQueryClient
from .paginator import QueryPaginator

Client = TimestreamQueryClient

__all__ = ("Client", "QueryPaginator", "TimestreamQueryClient")
