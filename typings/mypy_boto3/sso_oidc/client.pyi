"""
Type annotations for sso-oidc service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sso_oidc import SSOOIDCClient

    client: SSOOIDCClient = boto3.client("sso-oidc")
    ```
"""

from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    CreateTokenResponseTypeDef,
    CreateTokenWithIAMResponseTypeDef,
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
    InvalidRedirectUriException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidRequestRegionException: Type[BotocoreClientError]
    InvalidScopeException: Type[BotocoreClientError]
    SlowDownException: Type[BotocoreClientError]
    UnauthorizedClientException: Type[BotocoreClientError]
    UnsupportedGrantTypeException: Type[BotocoreClientError]

class SSOOIDCClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sso-oidc.html#SSOOIDC.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SSOOIDCClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sso-oidc.html#SSOOIDC.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sso-oidc.html#SSOOIDC.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client.html#close)
        """

    def create_token(
        self,
        *,
        clientId: str,
        clientSecret: str,
        grantType: str,
        deviceCode: str = None,
        code: str = None,
        refreshToken: str = None,
        scope: List[str] = None,
        redirectUri: str = None,
        codeVerifier: str = None
    ) -> CreateTokenResponseTypeDef:
        """
        Creates and returns access and refresh tokens for clients that are authenticated
        using client secrets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sso-oidc.html#SSOOIDC.Client.create_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client.html#create_token)
        """

    def create_token_with_iam(
        self,
        *,
        clientId: str,
        grantType: str,
        code: str = None,
        refreshToken: str = None,
        assertion: str = None,
        scope: List[str] = None,
        redirectUri: str = None,
        subjectToken: str = None,
        subjectTokenType: str = None,
        requestedTokenType: str = None,
        codeVerifier: str = None
    ) -> CreateTokenWithIAMResponseTypeDef:
        """
        Creates and returns access and refresh tokens for clients and applications that
        are authenticated using IAM entities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sso-oidc.html#SSOOIDC.Client.create_token_with_iam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client.html#create_token_with_iam)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sso-oidc.html#SSOOIDC.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client.html#generate_presigned_url)
        """

    def register_client(
        self,
        *,
        clientName: str,
        clientType: str,
        scopes: List[str] = None,
        redirectUris: List[str] = None,
        grantTypes: List[str] = None,
        issuerUrl: str = None,
        entitledApplicationArn: str = None
    ) -> RegisterClientResponseTypeDef:
        """
        Registers a client with IAM Identity Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sso-oidc.html#SSOOIDC.Client.register_client)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client.html#register_client)
        """

    def start_device_authorization(
        self, *, clientId: str, clientSecret: str, startUrl: str
    ) -> StartDeviceAuthorizationResponseTypeDef:
        """
        Initiates device authorization by requesting a pair of verification codes from
        the authorization service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/sso-oidc.html#SSOOIDC.Client.start_device_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client.html#start_device_authorization)
        """
