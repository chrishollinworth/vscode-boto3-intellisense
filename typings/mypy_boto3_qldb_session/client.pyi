# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for qldb-session service client

Usage::

    ```python
    import boto3
    from mypy_boto3_qldb_session import QLDBSessionClient

    client: QLDBSessionClient = boto3.client("qldb-session")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from mypy_boto3_qldb_session.type_defs import (
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
    ClientError: Type[BotocoreClientError]
    InvalidSessionException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    OccConflictException: Type[BotocoreClientError]
    RateExceededException: Type[BotocoreClientError]


class QLDBSessionClient:
    """
    [QLDBSession.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb-session.html#QLDBSession.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb-session.html#QLDBSession.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb-session.html#QLDBSession.Client.generate_presigned_url)
        """

    def send_command(
        self,
        SessionToken: str = None,
        StartSession: StartSessionRequestTypeDef = None,
        StartTransaction: Dict[str, Any] = None,
        EndSession: Dict[str, Any] = None,
        CommitTransaction: CommitTransactionRequestTypeDef = None,
        AbortTransaction: Dict[str, Any] = None,
        ExecuteStatement: ExecuteStatementRequestTypeDef = None,
        FetchPage: FetchPageRequestTypeDef = None,
    ) -> SendCommandResultTypeDef:
        """
        [Client.send_command documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/qldb-session.html#QLDBSession.Client.send_command)
        """
