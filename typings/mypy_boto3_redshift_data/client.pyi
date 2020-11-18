# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for redshift-data service client

Usage::

    ```python
    import boto3
    from mypy_boto3_redshift_data import RedshiftDataAPIServiceClient

    client: RedshiftDataAPIServiceClient = boto3.client("redshift-data")
    ```
"""
import sys
from typing import Any, Dict, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_redshift_data.paginator import (
    DescribeTablePaginator,
    GetStatementResultPaginator,
    ListDatabasesPaginator,
    ListSchemasPaginator,
    ListStatementsPaginator,
    ListTablesPaginator,
)
from mypy_boto3_redshift_data.type_defs import (
    CancelStatementResponseTypeDef,
    DescribeStatementResponseTypeDef,
    DescribeTableResponseTypeDef,
    ExecuteStatementOutputTypeDef,
    GetStatementResultResponseTypeDef,
    ListDatabasesResponseTypeDef,
    ListSchemasResponseTypeDef,
    ListStatementsResponseTypeDef,
    ListTablesResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("RedshiftDataAPIServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ExecuteStatementException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class RedshiftDataAPIServiceClient:
    """
    [RedshiftDataAPIService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Client.can_paginate)
        """

    def cancel_statement(self, Id: str) -> CancelStatementResponseTypeDef:
        """
        [Client.cancel_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Client.cancel_statement)
        """

    def describe_statement(self, Id: str) -> DescribeStatementResponseTypeDef:
        """
        [Client.describe_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Client.describe_statement)
        """

    def describe_table(
        self,
        ClusterIdentifier: str,
        Database: str = None,
        DbUser: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Schema: str = None,
        SecretArn: str = None,
        Table: str = None,
    ) -> DescribeTableResponseTypeDef:
        """
        [Client.describe_table documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Client.describe_table)
        """

    def execute_statement(
        self,
        ClusterIdentifier: str,
        Sql: str,
        Database: str = None,
        DbUser: str = None,
        SecretArn: str = None,
        StatementName: str = None,
        WithEvent: bool = None,
    ) -> ExecuteStatementOutputTypeDef:
        """
        [Client.execute_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Client.execute_statement)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Client.generate_presigned_url)
        """

    def get_statement_result(
        self, Id: str, NextToken: str = None
    ) -> GetStatementResultResponseTypeDef:
        """
        [Client.get_statement_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_statement_result)
        """

    def list_databases(
        self,
        ClusterIdentifier: str,
        Database: str = None,
        DbUser: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        SecretArn: str = None,
    ) -> ListDatabasesResponseTypeDef:
        """
        [Client.list_databases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_databases)
        """

    def list_schemas(
        self,
        ClusterIdentifier: str,
        Database: str,
        DbUser: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        SchemaPattern: str = None,
        SecretArn: str = None,
    ) -> ListSchemasResponseTypeDef:
        """
        [Client.list_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_schemas)
        """

    def list_statements(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        StatementName: str = None,
        Status: Literal[
            "ABORTED", "ALL", "FAILED", "FINISHED", "PICKED", "STARTED", "SUBMITTED"
        ] = None,
    ) -> ListStatementsResponseTypeDef:
        """
        [Client.list_statements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_statements)
        """

    def list_tables(
        self,
        ClusterIdentifier: str,
        Database: str,
        DbUser: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        SchemaPattern: str = None,
        SecretArn: str = None,
        TablePattern: str = None,
    ) -> ListTablesResponseTypeDef:
        """
        [Client.list_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_tables)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_table"]) -> DescribeTablePaginator:
        """
        [Paginator.DescribeTable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.DescribeTable)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_statement_result"]
    ) -> GetStatementResultPaginator:
        """
        [Paginator.GetStatementResult documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.GetStatementResult)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_databases"]) -> ListDatabasesPaginator:
        """
        [Paginator.ListDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListDatabases)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_schemas"]) -> ListSchemasPaginator:
        """
        [Paginator.ListSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListSchemas)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_statements"]) -> ListStatementsPaginator:
        """
        [Paginator.ListStatements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListStatements)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tables"]) -> ListTablesPaginator:
        """
        [Paginator.ListTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListTables)
        """
