"""
Type annotations for athena service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_athena.client import AthenaClient
    from mypy_boto3_athena.paginator import (
        GetQueryResultsPaginator,
        ListDataCatalogsPaginator,
        ListDatabasesPaginator,
        ListNamedQueriesPaginator,
        ListQueryExecutionsPaginator,
        ListTableMetadataPaginator,
        ListTagsForResourcePaginator,
    )

    session = Session()
    client: AthenaClient = session.client("athena")

    get_query_results_paginator: GetQueryResultsPaginator = client.get_paginator("get_query_results")
    list_data_catalogs_paginator: ListDataCatalogsPaginator = client.get_paginator("list_data_catalogs")
    list_databases_paginator: ListDatabasesPaginator = client.get_paginator("list_databases")
    list_named_queries_paginator: ListNamedQueriesPaginator = client.get_paginator("list_named_queries")
    list_query_executions_paginator: ListQueryExecutionsPaginator = client.get_paginator("list_query_executions")
    list_table_metadata_paginator: ListTableMetadataPaginator = client.get_paginator("list_table_metadata")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetQueryResultsInputPaginateTypeDef,
    GetQueryResultsOutputTypeDef,
    ListDatabasesInputPaginateTypeDef,
    ListDatabasesOutputTypeDef,
    ListDataCatalogsInputPaginateTypeDef,
    ListDataCatalogsOutputTypeDef,
    ListNamedQueriesInputPaginateTypeDef,
    ListNamedQueriesOutputTypeDef,
    ListQueryExecutionsInputPaginateTypeDef,
    ListQueryExecutionsOutputTypeDef,
    ListTableMetadataInputPaginateTypeDef,
    ListTableMetadataOutputTypeDef,
    ListTagsForResourceInputPaginateTypeDef,
    ListTagsForResourceOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetQueryResultsPaginator",
    "ListDataCatalogsPaginator",
    "ListDatabasesPaginator",
    "ListNamedQueriesPaginator",
    "ListQueryExecutionsPaginator",
    "ListTableMetadataPaginator",
    "ListTagsForResourcePaginator",
)

if TYPE_CHECKING:
    _GetQueryResultsPaginatorBase = Paginator[GetQueryResultsOutputTypeDef]
else:
    _GetQueryResultsPaginatorBase = Paginator  # type: ignore[assignment]

class GetQueryResultsPaginator(_GetQueryResultsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/paginator/GetQueryResults.html#Athena.Paginator.GetQueryResults)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators/#getqueryresultspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetQueryResultsInputPaginateTypeDef]
    ) -> PageIterator[GetQueryResultsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/paginator/GetQueryResults.html#Athena.Paginator.GetQueryResults.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators/#getqueryresultspaginator)
        """

if TYPE_CHECKING:
    _ListDataCatalogsPaginatorBase = Paginator[ListDataCatalogsOutputTypeDef]
else:
    _ListDataCatalogsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataCatalogsPaginator(_ListDataCatalogsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/paginator/ListDataCatalogs.html#Athena.Paginator.ListDataCatalogs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators/#listdatacatalogspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataCatalogsInputPaginateTypeDef]
    ) -> PageIterator[ListDataCatalogsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/paginator/ListDataCatalogs.html#Athena.Paginator.ListDataCatalogs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators/#listdatacatalogspaginator)
        """

if TYPE_CHECKING:
    _ListDatabasesPaginatorBase = Paginator[ListDatabasesOutputTypeDef]
else:
    _ListDatabasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatabasesPaginator(_ListDatabasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/paginator/ListDatabases.html#Athena.Paginator.ListDatabases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators/#listdatabasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatabasesInputPaginateTypeDef]
    ) -> PageIterator[ListDatabasesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/paginator/ListDatabases.html#Athena.Paginator.ListDatabases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators/#listdatabasespaginator)
        """

if TYPE_CHECKING:
    _ListNamedQueriesPaginatorBase = Paginator[ListNamedQueriesOutputTypeDef]
else:
    _ListNamedQueriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListNamedQueriesPaginator(_ListNamedQueriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/paginator/ListNamedQueries.html#Athena.Paginator.ListNamedQueries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators/#listnamedqueriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNamedQueriesInputPaginateTypeDef]
    ) -> PageIterator[ListNamedQueriesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/paginator/ListNamedQueries.html#Athena.Paginator.ListNamedQueries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators/#listnamedqueriespaginator)
        """

if TYPE_CHECKING:
    _ListQueryExecutionsPaginatorBase = Paginator[ListQueryExecutionsOutputTypeDef]
else:
    _ListQueryExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListQueryExecutionsPaginator(_ListQueryExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/paginator/ListQueryExecutions.html#Athena.Paginator.ListQueryExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators/#listqueryexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQueryExecutionsInputPaginateTypeDef]
    ) -> PageIterator[ListQueryExecutionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/paginator/ListQueryExecutions.html#Athena.Paginator.ListQueryExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators/#listqueryexecutionspaginator)
        """

if TYPE_CHECKING:
    _ListTableMetadataPaginatorBase = Paginator[ListTableMetadataOutputTypeDef]
else:
    _ListTableMetadataPaginatorBase = Paginator  # type: ignore[assignment]

class ListTableMetadataPaginator(_ListTableMetadataPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/paginator/ListTableMetadata.html#Athena.Paginator.ListTableMetadata)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators/#listtablemetadatapaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTableMetadataInputPaginateTypeDef]
    ) -> PageIterator[ListTableMetadataOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/paginator/ListTableMetadata.html#Athena.Paginator.ListTableMetadata.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators/#listtablemetadatapaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceOutputTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/paginator/ListTagsForResource.html#Athena.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceInputPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/paginator/ListTagsForResource.html#Athena.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_athena/paginators/#listtagsforresourcepaginator)
        """
