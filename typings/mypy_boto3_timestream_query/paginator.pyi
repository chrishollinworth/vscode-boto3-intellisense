# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for timestream-query service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_timestream_query import TimestreamQueryClient
    from mypy_boto3_timestream_query.paginator import (
        QueryPaginator,
    )

    client: TimestreamQueryClient = boto3.client("timestream-query")

    query_paginator: QueryPaginator = client.get_paginator("query")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_timestream_query.type_defs import PaginatorConfigTypeDef, QueryResponseTypeDef

__all__ = ("QueryPaginator",)


class QueryPaginator(Boto3Paginator):
    """
    [Paginator.Query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-query.html#TimestreamQuery.Paginator.Query)
    """

    def paginate(
        self,
        QueryString: str,
        ClientToken: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[QueryResponseTypeDef]:
        """
        [Query.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/timestream-query.html#TimestreamQuery.Paginator.Query.paginate)
        """
