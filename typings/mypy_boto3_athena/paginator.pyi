# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for athena service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_athena import AthenaClient
    from mypy_boto3_athena.paginator import (
        GetQueryResultsPaginator,
        ListDataCatalogsPaginator,
        ListDatabasesPaginator,
        ListNamedQueriesPaginator,
        ListQueryExecutionsPaginator,
        ListTableMetadataPaginator,
        ListTagsForResourcePaginator,
    )

    client: AthenaClient = boto3.client("athena")

    get_query_results_paginator: GetQueryResultsPaginator = client.get_paginator("get_query_results")
    list_data_catalogs_paginator: ListDataCatalogsPaginator = client.get_paginator("list_data_catalogs")
    list_databases_paginator: ListDatabasesPaginator = client.get_paginator("list_databases")
    list_named_queries_paginator: ListNamedQueriesPaginator = client.get_paginator("list_named_queries")
    list_query_executions_paginator: ListQueryExecutionsPaginator = client.get_paginator("list_query_executions")
    list_table_metadata_paginator: ListTableMetadataPaginator = client.get_paginator("list_table_metadata")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_athena.type_defs import (
    GetQueryResultsOutputTypeDef,
    ListDatabasesOutputTypeDef,
    ListDataCatalogsOutputTypeDef,
    ListNamedQueriesOutputTypeDef,
    ListQueryExecutionsOutputTypeDef,
    ListTableMetadataOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetQueryResultsPaginator",
    "ListDataCatalogsPaginator",
    "ListDatabasesPaginator",
    "ListNamedQueriesPaginator",
    "ListQueryExecutionsPaginator",
    "ListTableMetadataPaginator",
    "ListTagsForResourcePaginator",
)


class GetQueryResultsPaginator(Boto3Paginator):
    """
    [Paginator.GetQueryResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.GetQueryResults)
    """

    def paginate(
        self, QueryExecutionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetQueryResultsOutputTypeDef]:
        """
        [GetQueryResults.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.GetQueryResults.paginate)
        """


class ListDataCatalogsPaginator(Boto3Paginator):
    """
    [Paginator.ListDataCatalogs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListDataCatalogs)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataCatalogsOutputTypeDef]:
        """
        [ListDataCatalogs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListDataCatalogs.paginate)
        """


class ListDatabasesPaginator(Boto3Paginator):
    """
    [Paginator.ListDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListDatabases)
    """

    def paginate(
        self, CatalogName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatabasesOutputTypeDef]:
        """
        [ListDatabases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListDatabases.paginate)
        """


class ListNamedQueriesPaginator(Boto3Paginator):
    """
    [Paginator.ListNamedQueries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListNamedQueries)
    """

    def paginate(
        self, WorkGroup: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNamedQueriesOutputTypeDef]:
        """
        [ListNamedQueries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListNamedQueries.paginate)
        """


class ListQueryExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListQueryExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListQueryExecutions)
    """

    def paginate(
        self, WorkGroup: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQueryExecutionsOutputTypeDef]:
        """
        [ListQueryExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListQueryExecutions.paginate)
        """


class ListTableMetadataPaginator(Boto3Paginator):
    """
    [Paginator.ListTableMetadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListTableMetadata)
    """

    def paginate(
        self,
        CatalogName: str,
        DatabaseName: str,
        Expression: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTableMetadataOutputTypeDef]:
        """
        [ListTableMetadata.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListTableMetadata.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListTagsForResource)
    """

    def paginate(
        self, ResourceARN: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceOutputTypeDef]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/athena.html#Athena.Paginator.ListTagsForResource.paginate)
        """
