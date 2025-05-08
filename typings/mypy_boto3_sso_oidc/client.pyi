"""
Type annotations for sso-oidc service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sso_oidc.client import SSOOIDCClient

    session = Session()
    client: SSOOIDCClient = session.client("sso-oidc")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CreateTokenRequestTypeDef,
    CreateTokenResponseTypeDef,
    CreateTokenWithIAMRequestTypeDef,
    CreateTokenWithIAMResponseTypeDef,
    RegisterClientRequestTypeDef,
    RegisterClientResponseTypeDef,
    StartDeviceAuthorizationRequestTypeDef,
    StartDeviceAuthorizationResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("SSOOIDCClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc.html#SSOOIDC.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SSOOIDCClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc.html#SSOOIDC.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client/#generate_presigned_url)
        """

    def create_token(
        self, **kwargs: Unpack[CreateTokenRequestTypeDef]
    ) -> CreateTokenResponseTypeDef:
        """
        Creates and returns access and refresh tokens for clients that are
        authenticated using client secrets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc/client/create_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client/#create_token)
        """

    def create_token_with_iam(
        self, **kwargs: Unpack[CreateTokenWithIAMRequestTypeDef]
    ) -> CreateTokenWithIAMResponseTypeDef:
        """
        Creates and returns access and refresh tokens for clients and applications that
        are authenticated using IAM entities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc/client/create_token_with_iam.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client/#create_token_with_iam)
        """

    def register_client(
        self, **kwargs: Unpack[RegisterClientRequestTypeDef]
    ) -> RegisterClientResponseTypeDef:
        """
        Registers a public client with IAM Identity Center.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc/client/register_client.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client/#register_client)
        """

    def start_device_authorization(
        self, **kwargs: Unpack[StartDeviceAuthorizationRequestTypeDef]
    ) -> StartDeviceAuthorizationResponseTypeDef:
        """
        Initiates device authorization by requesting a pair of verification codes from
        the authorization service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-oidc/client/start_device_authorization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/client/#start_device_authorization)
        """
