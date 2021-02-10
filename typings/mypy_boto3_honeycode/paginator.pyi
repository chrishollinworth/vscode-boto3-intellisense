"""
Main interface for honeycode service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_honeycode import HoneycodeClient
    from mypy_boto3_honeycode.paginator import (
        ListTableColumnsPaginator,
        ListTableRowsPaginator,
        ListTablesPaginator,
        QueryTableRowsPaginator,
    )

    client: HoneycodeClient = boto3.client("honeycode")

    list_table_columns_paginator: ListTableColumnsPaginator = client.get_paginator("list_table_columns")
    list_table_rows_paginator: ListTableRowsPaginator = client.get_paginator("list_table_rows")
    list_tables_paginator: ListTablesPaginator = client.get_paginator("list_tables")
    query_table_rows_paginator: QueryTableRowsPaginator = client.get_paginator("query_table_rows")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_honeycode.type_defs import (
    FilterTypeDef,
    ListTableColumnsResultTypeDef,
    ListTableRowsResultTypeDef,
    ListTablesResultTypeDef,
    PaginatorConfigTypeDef,
    QueryTableRowsResultTypeDef,
)

__all__ = (
    "ListTableColumnsPaginator",
    "ListTableRowsPaginator",
    "ListTablesPaginator",
    "QueryTableRowsPaginator",
)


class ListTableColumnsPaginator(Boto3Paginator):
    """
    [Paginator.ListTableColumns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Paginator.ListTableColumns)
    """

    def paginate(
        self, workbookId: str, tableId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTableColumnsResultTypeDef]:
        """
        [ListTableColumns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Paginator.ListTableColumns.paginate)
        """


class ListTableRowsPaginator(Boto3Paginator):
    """
    [Paginator.ListTableRows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Paginator.ListTableRows)
    """

    def paginate(
        self,
        workbookId: str,
        tableId: str,
        rowIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTableRowsResultTypeDef]:
        """
        [ListTableRows.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Paginator.ListTableRows.paginate)
        """


class ListTablesPaginator(Boto3Paginator):
    """
    [Paginator.ListTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Paginator.ListTables)
    """

    def paginate(
        self, workbookId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTablesResultTypeDef]:
        """
        [ListTables.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Paginator.ListTables.paginate)
        """


class QueryTableRowsPaginator(Boto3Paginator):
    """
    [Paginator.QueryTableRows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Paginator.QueryTableRows)
    """

    def paginate(
        self,
        workbookId: str,
        tableId: str,
        filterFormula: "FilterTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[QueryTableRowsResultTypeDef]:
        """
        [QueryTableRows.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/honeycode.html#Honeycode.Paginator.QueryTableRows.paginate)
        """
