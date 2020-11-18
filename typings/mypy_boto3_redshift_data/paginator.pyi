# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for redshift-data service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_redshift_data import RedshiftDataAPIServiceClient
    from mypy_boto3_redshift_data.paginator import (
        DescribeTablePaginator,
        GetStatementResultPaginator,
        ListDatabasesPaginator,
        ListSchemasPaginator,
        ListStatementsPaginator,
        ListTablesPaginator,
    )

    client: RedshiftDataAPIServiceClient = boto3.client("redshift-data")

    describe_table_paginator: DescribeTablePaginator = client.get_paginator("describe_table")
    get_statement_result_paginator: GetStatementResultPaginator = client.get_paginator("get_statement_result")
    list_databases_paginator: ListDatabasesPaginator = client.get_paginator("list_databases")
    list_schemas_paginator: ListSchemasPaginator = client.get_paginator("list_schemas")
    list_statements_paginator: ListStatementsPaginator = client.get_paginator("list_statements")
    list_tables_paginator: ListTablesPaginator = client.get_paginator("list_tables")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_redshift_data.type_defs import (
    DescribeTableResponseTypeDef,
    GetStatementResultResponseTypeDef,
    ListDatabasesResponseTypeDef,
    ListSchemasResponseTypeDef,
    ListStatementsResponseTypeDef,
    ListTablesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeTablePaginator",
    "GetStatementResultPaginator",
    "ListDatabasesPaginator",
    "ListSchemasPaginator",
    "ListStatementsPaginator",
    "ListTablesPaginator",
)


class DescribeTablePaginator(Boto3Paginator):
    """
    [Paginator.DescribeTable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.DescribeTable)
    """

    def paginate(
        self,
        ClusterIdentifier: str,
        Database: str = None,
        DbUser: str = None,
        Schema: str = None,
        SecretArn: str = None,
        Table: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeTableResponseTypeDef]:
        """
        [DescribeTable.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.DescribeTable.paginate)
        """


class GetStatementResultPaginator(Boto3Paginator):
    """
    [Paginator.GetStatementResult documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.GetStatementResult)
    """

    def paginate(
        self, Id: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetStatementResultResponseTypeDef]:
        """
        [GetStatementResult.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.GetStatementResult.paginate)
        """


class ListDatabasesPaginator(Boto3Paginator):
    """
    [Paginator.ListDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListDatabases)
    """

    def paginate(
        self,
        ClusterIdentifier: str,
        Database: str = None,
        DbUser: str = None,
        SecretArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDatabasesResponseTypeDef]:
        """
        [ListDatabases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListDatabases.paginate)
        """


class ListSchemasPaginator(Boto3Paginator):
    """
    [Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListSchemas)
    """

    def paginate(
        self,
        ClusterIdentifier: str,
        Database: str,
        DbUser: str = None,
        SchemaPattern: str = None,
        SecretArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListSchemasResponseTypeDef]:
        """
        [ListSchemas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListSchemas.paginate)
        """


class ListStatementsPaginator(Boto3Paginator):
    """
    [Paginator.ListStatements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListStatements)
    """

    def paginate(
        self,
        StatementName: str = None,
        Status: Literal[
            "ABORTED", "ALL", "FAILED", "FINISHED", "PICKED", "STARTED", "SUBMITTED"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListStatementsResponseTypeDef]:
        """
        [ListStatements.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListStatements.paginate)
        """


class ListTablesPaginator(Boto3Paginator):
    """
    [Paginator.ListTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListTables)
    """

    def paginate(
        self,
        ClusterIdentifier: str,
        Database: str,
        DbUser: str = None,
        SchemaPattern: str = None,
        SecretArn: str = None,
        TablePattern: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTablesResponseTypeDef]:
        """
        [ListTables.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListTables.paginate)
        """
