"""
Type annotations for rds-data service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds_data/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_rds_data import RDSDataServiceClient

    client: RDSDataServiceClient = boto3.client("rds-data")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    BatchExecuteStatementResponseTypeDef,
    BeginTransactionResponseTypeDef,
    CommitTransactionResponseTypeDef,
    ExecuteSqlResponseTypeDef,
    ExecuteStatementResponseTypeDef,
    ResultSetOptionsTypeDef,
    RollbackTransactionResponseTypeDef,
    SqlParameterTypeDef,
)

__all__ = ("RDSDataServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceUnavailableError: Type[BotocoreClientError]
    StatementTimeoutException: Type[BotocoreClientError]

class RDSDataServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/rds-data.html#RDSDataService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds_data/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        RDSDataServiceClient exceptions.
        """
    def batch_execute_statement(
        self,
        *,
        resourceArn: str,
        secretArn: str,
        sql: str,
        database: str = None,
        parameterSets: List[List["SqlParameterTypeDef"]] = None,
        schema: str = None,
        transactionId: str = None
    ) -> BatchExecuteStatementResponseTypeDef:
        """
        Runs a batch SQL statement over an array of data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/rds-data.html#RDSDataService.Client.batch_execute_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds_data/client.html#batch_execute_statement)
        """
    def begin_transaction(
        self, *, resourceArn: str, secretArn: str, database: str = None, schema: str = None
    ) -> BeginTransactionResponseTypeDef:
        """
        Starts a SQL transaction.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/rds-data.html#RDSDataService.Client.begin_transaction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds_data/client.html#begin_transaction)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/rds-data.html#RDSDataService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds_data/client.html#can_paginate)
        """
    def commit_transaction(
        self, *, resourceArn: str, secretArn: str, transactionId: str
    ) -> CommitTransactionResponseTypeDef:
        """
        Ends a SQL transaction started with the `BeginTransaction` operation and commits
        the changes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/rds-data.html#RDSDataService.Client.commit_transaction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds_data/client.html#commit_transaction)
        """
    def execute_sql(
        self,
        *,
        awsSecretStoreArn: str,
        dbClusterOrInstanceArn: str,
        sqlStatements: str,
        database: str = None,
        schema: str = None
    ) -> ExecuteSqlResponseTypeDef:
        """
        Runs one or more SQL statements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/rds-data.html#RDSDataService.Client.execute_sql)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds_data/client.html#execute_sql)
        """
    def execute_statement(
        self,
        *,
        resourceArn: str,
        secretArn: str,
        sql: str,
        continueAfterTimeout: bool = None,
        database: str = None,
        includeResultMetadata: bool = None,
        parameters: List["SqlParameterTypeDef"] = None,
        resultSetOptions: "ResultSetOptionsTypeDef" = None,
        schema: str = None,
        transactionId: str = None
    ) -> ExecuteStatementResponseTypeDef:
        """
        Runs a SQL statement against a database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/rds-data.html#RDSDataService.Client.execute_statement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds_data/client.html#execute_statement)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/rds-data.html#RDSDataService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds_data/client.html#generate_presigned_url)
        """
    def rollback_transaction(
        self, *, resourceArn: str, secretArn: str, transactionId: str
    ) -> RollbackTransactionResponseTypeDef:
        """
        Performs a rollback of a transaction.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/rds-data.html#RDSDataService.Client.rollback_transaction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds_data/client.html#rollback_transaction)
        """
