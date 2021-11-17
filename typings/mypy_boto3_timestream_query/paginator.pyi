"""
Type annotations for timestream-query service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/paginators.html)

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

from .type_defs import PaginatorConfigTypeDef, QueryResponseTypeDef

__all__ = ("QueryPaginator",)

class QueryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/timestream-query.html#TimestreamQuery.Paginator.Query)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/paginators.html#querypaginator)
    """

    def paginate(
        self,
        *,
        QueryString: str,
        ClientToken: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[QueryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/timestream-query.html#TimestreamQuery.Paginator.Query.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/paginators.html#querypaginator)
        """
