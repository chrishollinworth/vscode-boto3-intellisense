# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for sso-oidc service client

Usage::

    ```python
    import boto3
    from mypy_boto3_sso_oidc import SSOOIDCClient

    client: SSOOIDCClient = boto3.client("sso-oidc")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_sso_oidc.type_defs import (
    CreateTokenResponseTypeDef,
    RegisterClientResponseTypeDef,
    StartDeviceAuthorizationResponseTypeDef,
)

__all__ = ("SSOOIDCClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AuthorizationPendingException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ExpiredTokenException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidClientException: Type[BotocoreClientError]
    InvalidClientMetadataException: Type[BotocoreClientError]
    InvalidGrantException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidScopeException: Type[BotocoreClientError]
    SlowDownException: Type[BotocoreClientError]
    UnauthorizedClientException: Type[BotocoreClientError]
    UnsupportedGrantTypeException: Type[BotocoreClientError]


class SSOOIDCClient:
    """
    [SSOOIDC.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-oidc.html#SSOOIDC.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-oidc.html#SSOOIDC.Client.can_paginate)
        """

    def create_token(
        self,
        clientId: str,
        clientSecret: str,
        grantType: str,
        deviceCode: str,
        code: str = None,
        refreshToken: str = None,
        scope: List[str] = None,
        redirectUri: str = None,
    ) -> CreateTokenResponseTypeDef:
        """
        [Client.create_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-oidc.html#SSOOIDC.Client.create_token)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-oidc.html#SSOOIDC.Client.generate_presigned_url)
        """

    def register_client(
        self, clientName: str, clientType: str, scopes: List[str] = None
    ) -> RegisterClientResponseTypeDef:
        """
        [Client.register_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-oidc.html#SSOOIDC.Client.register_client)
        """

    def start_device_authorization(
        self, clientId: str, clientSecret: str, startUrl: str
    ) -> StartDeviceAuthorizationResponseTypeDef:
        """
        [Client.start_device_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-oidc.html#SSOOIDC.Client.start_device_authorization)
        """
