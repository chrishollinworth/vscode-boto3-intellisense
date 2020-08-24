# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
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

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_sso_oidc.type_defs import (
    CreateTokenResponseTypeDef,
    RegisterClientResponseTypeDef,
    StartDeviceAuthorizationResponseTypeDef,
)

__all__ = ("SSOOIDCClient",)


class Exceptions:
    AccessDeniedException: Type[Boto3ClientError]
    AuthorizationPendingException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ExpiredTokenException: Type[Boto3ClientError]
    InternalServerException: Type[Boto3ClientError]
    InvalidClientException: Type[Boto3ClientError]
    InvalidClientMetadataException: Type[Boto3ClientError]
    InvalidGrantException: Type[Boto3ClientError]
    InvalidRequestException: Type[Boto3ClientError]
    InvalidScopeException: Type[Boto3ClientError]
    SlowDownException: Type[Boto3ClientError]
    UnauthorizedClientException: Type[Boto3ClientError]
    UnsupportedGrantTypeException: Type[Boto3ClientError]


class SSOOIDCClient:
    """
    [SSOOIDC.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sso-oidc.html#SSOOIDC.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sso-oidc.html#SSOOIDC.Client.can_paginate)
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
        [Client.create_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sso-oidc.html#SSOOIDC.Client.create_token)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sso-oidc.html#SSOOIDC.Client.generate_presigned_url)
        """

    def register_client(
        self, clientName: str, clientType: str, scopes: List[str] = None
    ) -> RegisterClientResponseTypeDef:
        """
        [Client.register_client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sso-oidc.html#SSOOIDC.Client.register_client)
        """

    def start_device_authorization(
        self, clientId: str, clientSecret: str, startUrl: str
    ) -> StartDeviceAuthorizationResponseTypeDef:
        """
        [Client.start_device_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sso-oidc.html#SSOOIDC.Client.start_device_authorization)
        """
