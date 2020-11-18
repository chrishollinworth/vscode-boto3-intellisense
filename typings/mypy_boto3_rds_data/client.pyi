# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for rds-data service client

Usage::

    ```python
    import boto3
    from mypy_boto3_rds_data import RDSDataServiceClient

    client: RDSDataServiceClient = boto3.client("rds-data")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_rds_data.type_defs import (
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


class RDSDataServiceClient:
    """
    [RDSDataService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds-data.html#RDSDataService.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_execute_statement(
        self,
        resourceArn: str,
        secretArn: str,
        sql: str,
        database: str = None,
        parameterSets: List[List[SqlParameterTypeDef]] = None,
        schema: str = None,
        transactionId: str = None,
    ) -> BatchExecuteStatementResponseTypeDef:
        """
        [Client.batch_execute_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds-data.html#RDSDataService.Client.batch_execute_statement)
        """

    def begin_transaction(
        self, resourceArn: str, secretArn: str, database: str = None, schema: str = None
    ) -> BeginTransactionResponseTypeDef:
        """
        [Client.begin_transaction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds-data.html#RDSDataService.Client.begin_transaction)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds-data.html#RDSDataService.Client.can_paginate)
        """

    def commit_transaction(
        self, resourceArn: str, secretArn: str, transactionId: str
    ) -> CommitTransactionResponseTypeDef:
        """
        [Client.commit_transaction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds-data.html#RDSDataService.Client.commit_transaction)
        """

    def execute_sql(
        self,
        awsSecretStoreArn: str,
        dbClusterOrInstanceArn: str,
        sqlStatements: str,
        database: str = None,
        schema: str = None,
    ) -> ExecuteSqlResponseTypeDef:
        """
        [Client.execute_sql documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds-data.html#RDSDataService.Client.execute_sql)
        """

    def execute_statement(
        self,
        resourceArn: str,
        secretArn: str,
        sql: str,
        continueAfterTimeout: bool = None,
        database: str = None,
        includeResultMetadata: bool = None,
        parameters: List[SqlParameterTypeDef] = None,
        resultSetOptions: ResultSetOptionsTypeDef = None,
        schema: str = None,
        transactionId: str = None,
    ) -> ExecuteStatementResponseTypeDef:
        """
        [Client.execute_statement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds-data.html#RDSDataService.Client.execute_statement)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds-data.html#RDSDataService.Client.generate_presigned_url)
        """

    def rollback_transaction(
        self, resourceArn: str, secretArn: str, transactionId: str
    ) -> RollbackTransactionResponseTypeDef:
        """
        [Client.rollback_transaction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rds-data.html#RDSDataService.Client.rollback_transaction)
        """
