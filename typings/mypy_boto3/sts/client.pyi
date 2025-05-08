"""
Type annotations for sts service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sts.client import STSClient

    session = Session()
    client: STSClient = session.client("sts")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    AssumeRoleRequestTypeDef,
    AssumeRoleResponseTypeDef,
    AssumeRoleWithSAMLRequestTypeDef,
    AssumeRoleWithSAMLResponseTypeDef,
    AssumeRoleWithWebIdentityRequestTypeDef,
    AssumeRoleWithWebIdentityResponseTypeDef,
    AssumeRootRequestTypeDef,
    AssumeRootResponseTypeDef,
    DecodeAuthorizationMessageRequestTypeDef,
    DecodeAuthorizationMessageResponseTypeDef,
    GetAccessKeyInfoRequestTypeDef,
    GetAccessKeyInfoResponseTypeDef,
    GetCallerIdentityResponseTypeDef,
    GetFederationTokenRequestTypeDef,
    GetFederationTokenResponseTypeDef,
    GetSessionTokenRequestTypeDef,
    GetSessionTokenResponseTypeDef,
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

__all__ = ("STSClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ExpiredTokenException: Type[BotocoreClientError]
    IDPCommunicationErrorException: Type[BotocoreClientError]
    IDPRejectedClaimException: Type[BotocoreClientError]
    InvalidAuthorizationMessageException: Type[BotocoreClientError]
    InvalidIdentityTokenException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    PackedPolicyTooLargeException: Type[BotocoreClientError]
    RegionDisabledException: Type[BotocoreClientError]

class STSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        STSClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#generate_presigned_url)
        """

    def assume_role(self, **kwargs: Unpack[AssumeRoleRequestTypeDef]) -> AssumeRoleResponseTypeDef:
        """
        Returns a set of temporary security credentials that you can use to access
        Amazon Web Services resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts/client/assume_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#assume_role)
        """

    def assume_role_with_saml(
        self, **kwargs: Unpack[AssumeRoleWithSAMLRequestTypeDef]
    ) -> AssumeRoleWithSAMLResponseTypeDef:
        """
        Returns a set of temporary security credentials for users who have been
        authenticated via a SAML authentication response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts/client/assume_role_with_saml.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#assume_role_with_saml)
        """

    def assume_role_with_web_identity(
        self, **kwargs: Unpack[AssumeRoleWithWebIdentityRequestTypeDef]
    ) -> AssumeRoleWithWebIdentityResponseTypeDef:
        """
        Returns a set of temporary security credentials for users who have been
        authenticated in a mobile or web application with a web identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts/client/assume_role_with_web_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#assume_role_with_web_identity)
        """

    def assume_root(self, **kwargs: Unpack[AssumeRootRequestTypeDef]) -> AssumeRootResponseTypeDef:
        """
        Returns a set of short term credentials you can use to perform privileged tasks
        on a member account in your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts/client/assume_root.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#assume_root)
        """

    def decode_authorization_message(
        self, **kwargs: Unpack[DecodeAuthorizationMessageRequestTypeDef]
    ) -> DecodeAuthorizationMessageResponseTypeDef:
        """
        Decodes additional information about the authorization status of a request from
        an encoded message returned in response to an Amazon Web Services request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts/client/decode_authorization_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#decode_authorization_message)
        """

    def get_access_key_info(
        self, **kwargs: Unpack[GetAccessKeyInfoRequestTypeDef]
    ) -> GetAccessKeyInfoResponseTypeDef:
        """
        Returns the account identifier for the specified access key ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts/client/get_access_key_info.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#get_access_key_info)
        """

    def get_caller_identity(self) -> GetCallerIdentityResponseTypeDef:
        """
        Returns details about the IAM user or role whose credentials are used to call
        the operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts/client/get_caller_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#get_caller_identity)
        """

    def get_federation_token(
        self, **kwargs: Unpack[GetFederationTokenRequestTypeDef]
    ) -> GetFederationTokenResponseTypeDef:
        """
        Returns a set of temporary security credentials (consisting of an access key
        ID, a secret access key, and a security token) for a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts/client/get_federation_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#get_federation_token)
        """

    def get_session_token(
        self, **kwargs: Unpack[GetSessionTokenRequestTypeDef]
    ) -> GetSessionTokenResponseTypeDef:
        """
        Returns a set of temporary credentials for an Amazon Web Services account or
        IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts/client/get_session_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#get_session_token)
        """
