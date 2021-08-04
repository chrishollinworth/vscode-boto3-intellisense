"""
Type annotations for apigatewaymanagementapi service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_apigatewaymanagementapi import ApiGatewayManagementApiClient

    client: ApiGatewayManagementApiClient = boto3.client("apigatewaymanagementapi")
    ```
"""
from typing import IO, Any, Dict, Type, Union

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .type_defs import GetConnectionResponseTypeDef

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

class ApiGatewayManagementApiClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        ApiGatewayManagementApiClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client.html#can_paginate)
        """
    def delete_connection(self, *, ConnectionId: str) -> None:
        """
        Delete the connection with the provided id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.delete_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client.html#delete_connection)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client.html#generate_presigned_url)
        """
    def get_connection(self, *, ConnectionId: str) -> GetConnectionResponseTypeDef:
        """
        Get information about the connection with the provided id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.get_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client.html#get_connection)
        """
    def post_to_connection(
        self, *, Data: Union[bytes, IO[bytes], StreamingBody], ConnectionId: str
    ) -> None:
        """
        Sends the provided data to the specified connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client.post_to_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client.html#post_to_connection)
        """
