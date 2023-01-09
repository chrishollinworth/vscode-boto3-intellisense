"""
Type annotations for qldb-session service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb_session/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_qldb_session import QLDBSessionClient

    client: QLDBSessionClient = boto3.client("qldb-session")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    CommitTransactionRequestTypeDef,
    ExecuteStatementRequestTypeDef,
    FetchPageRequestTypeDef,
    SendCommandResultTypeDef,
    StartSessionRequestTypeDef,
)

__all__ = ("QLDBSessionClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    CapacityExceededException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InvalidSessionException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    OccConflictException: Type[BotocoreClientError]
    RateExceededException: Type[BotocoreClientError]

class QLDBSessionClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/qldb-session.html#QLDBSession.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb_session/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        QLDBSessionClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/qldb-session.html#QLDBSession.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb_session/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/qldb-session.html#QLDBSession.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb_session/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/qldb-session.html#QLDBSession.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb_session/client.html#generate_presigned_url)
        """
    def send_command(
        self,
        *,
        SessionToken: str = None,
        StartSession: "StartSessionRequestTypeDef" = None,
        StartTransaction: Dict[str, Any] = None,
        EndSession: Dict[str, Any] = None,
        CommitTransaction: "CommitTransactionRequestTypeDef" = None,
        AbortTransaction: Dict[str, Any] = None,
        ExecuteStatement: "ExecuteStatementRequestTypeDef" = None,
        FetchPage: "FetchPageRequestTypeDef" = None
    ) -> SendCommandResultTypeDef:
        """
        Sends a command to an Amazon QLDB ledger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/qldb-session.html#QLDBSession.Client.send_command)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb_session/client.html#send_command)
        """
