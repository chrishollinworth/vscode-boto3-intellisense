"""
Type annotations for redshift-data service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_redshift_data import RedshiftDataAPIServiceClient

    client: RedshiftDataAPIServiceClient = boto3.client("redshift-data")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import StatusStringType
from .paginator import (
    DescribeTablePaginator,
    GetStatementResultPaginator,
    ListDatabasesPaginator,
    ListSchemasPaginator,
    ListStatementsPaginator,
    ListTablesPaginator,
)
from .type_defs import (
    BatchExecuteStatementOutputTypeDef,
    CancelStatementResponseTypeDef,
    DescribeStatementResponseTypeDef,
    DescribeTableResponseTypeDef,
    ExecuteStatementOutputTypeDef,
    GetStatementResultResponseTypeDef,
    ListDatabasesResponseTypeDef,
    ListSchemasResponseTypeDef,
    ListStatementsResponseTypeDef,
    ListTablesResponseTypeDef,
    SqlParameterTypeDef,
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
    ActiveStatementsExceededException: Type[BotocoreClientError]
    BatchExecuteStatementException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DatabaseConnectionException: Type[BotocoreClientError]
    ExecuteStatementException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class RedshiftDataAPIServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RedshiftDataAPIServiceClient exceptions.
        """
    def batch_execute_statement(
        self,
        *,
        Database: str,
        Sqls: List[str],
        ClusterIdentifier: str = None,
        DbUser: str = None,
        SecretArn: str = None,
        StatementName: str = None,
        WithEvent: bool = None,
        WorkgroupName: str = None
    ) -> BatchExecuteStatementOutputTypeDef:
        """
        Runs one or more SQL statements, which can be data manipulation language (DML)
        or data definition language (DDL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Client.batch_execute_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client.html#batch_execute_statement)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client.html#can_paginate)
        """
    def cancel_statement(self, *, Id: str) -> CancelStatementResponseTypeDef:
        """
        Cancels a running query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Client.cancel_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client.html#cancel_statement)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client.html#close)
        """
    def describe_statement(self, *, Id: str) -> DescribeStatementResponseTypeDef:
        """
        Describes the details about a specific instance when a query was run by the
        Amazon Redshift Data API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Client.describe_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client.html#describe_statement)
        """
    def describe_table(
        self,
        *,
        Database: str,
        ClusterIdentifier: str = None,
        ConnectedDatabase: str = None,
        DbUser: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Schema: str = None,
        SecretArn: str = None,
        Table: str = None,
        WorkgroupName: str = None
    ) -> DescribeTableResponseTypeDef:
        """
        Describes the detailed information about a table from metadata in the cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Client.describe_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client.html#describe_table)
        """
    def execute_statement(
        self,
        *,
        Database: str,
        Sql: str,
        ClusterIdentifier: str = None,
        DbUser: str = None,
        Parameters: List["SqlParameterTypeDef"] = None,
        SecretArn: str = None,
        StatementName: str = None,
        WithEvent: bool = None,
        WorkgroupName: str = None
    ) -> ExecuteStatementOutputTypeDef:
        """
        Runs an SQL statement, which can be data manipulation language (DML) or data
        definition language (DDL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Client.execute_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client.html#execute_statement)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client.html#generate_presigned_url)
        """
    def get_statement_result(
        self, *, Id: str, NextToken: str = None
    ) -> GetStatementResultResponseTypeDef:
        """
        Fetches the temporarily cached result of an SQL statement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Client.get_statement_result)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client.html#get_statement_result)
        """
    def list_databases(
        self,
        *,
        Database: str,
        ClusterIdentifier: str = None,
        DbUser: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        SecretArn: str = None,
        WorkgroupName: str = None
    ) -> ListDatabasesResponseTypeDef:
        """
        List the databases in a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_databases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client.html#list_databases)
        """
    def list_schemas(
        self,
        *,
        Database: str,
        ClusterIdentifier: str = None,
        ConnectedDatabase: str = None,
        DbUser: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        SchemaPattern: str = None,
        SecretArn: str = None,
        WorkgroupName: str = None
    ) -> ListSchemasResponseTypeDef:
        """
        Lists the schemas in a database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_schemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client.html#list_schemas)
        """
    def list_statements(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        RoleLevel: bool = None,
        StatementName: str = None,
        Status: StatusStringType = None
    ) -> ListStatementsResponseTypeDef:
        """
        List of SQL statements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_statements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client.html#list_statements)
        """
    def list_tables(
        self,
        *,
        Database: str,
        ClusterIdentifier: str = None,
        ConnectedDatabase: str = None,
        DbUser: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        SchemaPattern: str = None,
        SecretArn: str = None,
        TablePattern: str = None,
        WorkgroupName: str = None
    ) -> ListTablesResponseTypeDef:
        """
        List the tables in a database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Client.list_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/client.html#list_tables)
        """
    @overload
    def get_paginator(self, operation_name: Literal["describe_table"]) -> DescribeTablePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.DescribeTable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators.html#describetablepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_statement_result"]
    ) -> GetStatementResultPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.GetStatementResult)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators.html#getstatementresultpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_databases"]) -> ListDatabasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListDatabases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators.html#listdatabasespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_schemas"]) -> ListSchemasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListSchemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators.html#listschemaspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_statements"]) -> ListStatementsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListStatements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators.html#liststatementspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_tables"]) -> ListTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/redshift-data.html#RedshiftDataAPIService.Paginator.ListTables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/paginators.html#listtablespaginator)
        """
