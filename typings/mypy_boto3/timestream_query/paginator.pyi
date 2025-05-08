"""
Type annotations for timestream-query service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_timestream_query.client import TimestreamQueryClient
    from mypy_boto3_timestream_query.paginator import (
        ListScheduledQueriesPaginator,
        ListTagsForResourcePaginator,
        QueryPaginator,
    )

    session = Session()
    client: TimestreamQueryClient = session.client("timestream-query")

    list_scheduled_queries_paginator: ListScheduledQueriesPaginator = client.get_paginator("list_scheduled_queries")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    query_paginator: QueryPaginator = client.get_paginator("query")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListScheduledQueriesRequestPaginateTypeDef,
    ListScheduledQueriesResponseTypeDef,
    ListTagsForResourceRequestPaginateTypeDef,
    ListTagsForResourceResponseTypeDef,
    QueryRequestPaginateTypeDef,
    QueryResponsePaginatorTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListScheduledQueriesPaginator", "ListTagsForResourcePaginator", "QueryPaginator")

if TYPE_CHECKING:
    _ListScheduledQueriesPaginatorBase = Paginator[ListScheduledQueriesResponseTypeDef]
else:
    _ListScheduledQueriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListScheduledQueriesPaginator(_ListScheduledQueriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query/paginator/ListScheduledQueries.html#TimestreamQuery.Paginator.ListScheduledQueries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/paginators/#listscheduledqueriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListScheduledQueriesRequestPaginateTypeDef]
    ) -> PageIterator[ListScheduledQueriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query/paginator/ListScheduledQueries.html#TimestreamQuery.Paginator.ListScheduledQueries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/paginators/#listscheduledqueriespaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceResponseTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query/paginator/ListTagsForResource.html#TimestreamQuery.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query/paginator/ListTagsForResource.html#TimestreamQuery.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/paginators/#listtagsforresourcepaginator)
        """

if TYPE_CHECKING:
    _QueryPaginatorBase = Paginator[QueryResponsePaginatorTypeDef]
else:
    _QueryPaginatorBase = Paginator  # type: ignore[assignment]

class QueryPaginator(_QueryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query/paginator/Query.html#TimestreamQuery.Paginator.Query)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/paginators/#querypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[QueryRequestPaginateTypeDef]
    ) -> PageIterator[QueryResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query/paginator/Query.html#TimestreamQuery.Paginator.Query.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/paginators/#querypaginator)
        """
