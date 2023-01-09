"""
Type annotations for honeycode service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/paginators.html)

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

from .type_defs import (
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/honeycode.html#Honeycode.Paginator.ListTableColumns)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/paginators.html#listtablecolumnspaginator)
    """

    def paginate(
        self, *, workbookId: str, tableId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTableColumnsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/honeycode.html#Honeycode.Paginator.ListTableColumns.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/paginators.html#listtablecolumnspaginator)
        """

class ListTableRowsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/honeycode.html#Honeycode.Paginator.ListTableRows)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/paginators.html#listtablerowspaginator)
    """

    def paginate(
        self,
        *,
        workbookId: str,
        tableId: str,
        rowIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTableRowsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/honeycode.html#Honeycode.Paginator.ListTableRows.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/paginators.html#listtablerowspaginator)
        """

class ListTablesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/honeycode.html#Honeycode.Paginator.ListTables)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/paginators.html#listtablespaginator)
    """

    def paginate(
        self, *, workbookId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTablesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/honeycode.html#Honeycode.Paginator.ListTables.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/paginators.html#listtablespaginator)
        """

class QueryTableRowsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/honeycode.html#Honeycode.Paginator.QueryTableRows)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/paginators.html#querytablerowspaginator)
    """

    def paginate(
        self,
        *,
        workbookId: str,
        tableId: str,
        filterFormula: "FilterTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[QueryTableRowsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/honeycode.html#Honeycode.Paginator.QueryTableRows.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/paginators.html#querytablerowspaginator)
        """
