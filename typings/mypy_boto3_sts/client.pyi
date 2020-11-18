# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for sts service client

Usage::

    ```python
    import boto3
    from mypy_boto3_sts import STSClient

    client: STSClient = boto3.client("sts")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_sts.type_defs import (
    AssumeRoleResponseTypeDef,
    AssumeRoleWithSAMLResponseTypeDef,
    AssumeRoleWithWebIdentityResponseTypeDef,
    DecodeAuthorizationMessageResponseTypeDef,
    GetAccessKeyInfoResponseTypeDef,
    GetCallerIdentityResponseTypeDef,
    GetFederationTokenResponseTypeDef,
    GetSessionTokenResponseTypeDef,
    PolicyDescriptorTypeTypeDef,
    TagTypeDef,
)

__all__ = ("STSClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ExpiredTokenException: Type[BotocoreClientError]
    IDPCommunicationErrorException: Type[BotocoreClientError]
    IDPRejectedClaimException: Type[BotocoreClientError]
    InvalidAuthorizationMessageException: Type[BotocoreClientError]
    InvalidIdentityTokenException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    PackedPolicyTooLargeException: Type[BotocoreClientError]
    RegionDisabledException: Type[BotocoreClientError]


class STSClient:
    """
    [STS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sts.html#STS.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def assume_role(
        self,
        RoleArn: str,
        RoleSessionName: str,
        PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
        Policy: str = None,
        DurationSeconds: int = None,
        Tags: List[TagTypeDef] = None,
        TransitiveTagKeys: List[str] = None,
        ExternalId: str = None,
        SerialNumber: str = None,
        TokenCode: str = None,
    ) -> AssumeRoleResponseTypeDef:
        """
        [Client.assume_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sts.html#STS.Client.assume_role)
        """

    def assume_role_with_saml(
        self,
        RoleArn: str,
        PrincipalArn: str,
        SAMLAssertion: str,
        PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
        Policy: str = None,
        DurationSeconds: int = None,
    ) -> AssumeRoleWithSAMLResponseTypeDef:
        """
        [Client.assume_role_with_saml documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sts.html#STS.Client.assume_role_with_saml)
        """

    def assume_role_with_web_identity(
        self,
        RoleArn: str,
        RoleSessionName: str,
        WebIdentityToken: str,
        ProviderId: str = None,
        PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
        Policy: str = None,
        DurationSeconds: int = None,
    ) -> AssumeRoleWithWebIdentityResponseTypeDef:
        """
        [Client.assume_role_with_web_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sts.html#STS.Client.assume_role_with_web_identity)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sts.html#STS.Client.can_paginate)
        """

    def decode_authorization_message(
        self, EncodedMessage: str
    ) -> DecodeAuthorizationMessageResponseTypeDef:
        """
        [Client.decode_authorization_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sts.html#STS.Client.decode_authorization_message)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sts.html#STS.Client.generate_presigned_url)
        """

    def get_access_key_info(self, AccessKeyId: str) -> GetAccessKeyInfoResponseTypeDef:
        """
        [Client.get_access_key_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sts.html#STS.Client.get_access_key_info)
        """

    def get_caller_identity(self) -> GetCallerIdentityResponseTypeDef:
        """
        [Client.get_caller_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sts.html#STS.Client.get_caller_identity)
        """

    def get_federation_token(
        self,
        Name: str,
        Policy: str = None,
        PolicyArns: List[PolicyDescriptorTypeTypeDef] = None,
        DurationSeconds: int = None,
        Tags: List[TagTypeDef] = None,
    ) -> GetFederationTokenResponseTypeDef:
        """
        [Client.get_federation_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sts.html#STS.Client.get_federation_token)
        """

    def get_session_token(
        self, DurationSeconds: int = None, SerialNumber: str = None, TokenCode: str = None
    ) -> GetSessionTokenResponseTypeDef:
        """
        [Client.get_session_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sts.html#STS.Client.get_session_token)
        """
