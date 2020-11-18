# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for apigatewaymanagementapi service client

Usage::

    ```python
    import boto3
    from mypy_boto3_apigatewaymanagementapi import ApiGatewayManagementApiClient

    client: ApiGatewayManagementApiClient = boto3.client("apigatewaymanagementapi")
    ```
"""
from typing import IO, Any, Dict, Type, Union

from botocore.client import ClientMeta

from mypy_boto3_apigatewaymanagementapi.type_defs import GetConnectionResponseTypeDef

__all__ = ("ApiGatewayManagementApiClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    GoneException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    PayloadTooLargeException: Type[BotocoreClientError]


class ApiGatewayManagementApiClient:
    """
    [ApiGatewayManagementApi.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.can_paginate)
        """

    def delete_connection(self, ConnectionId: str) -> None:
        """
        [Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.delete_connection)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.generate_presigned_url)
        """

    def get_connection(self, ConnectionId: str) -> GetConnectionResponseTypeDef:
        """
        [Client.get_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.get_connection)
        """

    def post_to_connection(self, Data: Union[bytes, IO[bytes]], ConnectionId: str) -> None:
        """
        [Client.post_to_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.post_to_connection)
        """
