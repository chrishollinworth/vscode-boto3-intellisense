# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
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

from botocore.exceptions import ClientError as Boto3ClientError

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


class Exceptions:
    ClientError: Type[Boto3ClientError]
    ExpiredTokenException: Type[Boto3ClientError]
    IDPCommunicationErrorException: Type[Boto3ClientError]
    IDPRejectedClaimException: Type[Boto3ClientError]
    InvalidAuthorizationMessageException: Type[Boto3ClientError]
    InvalidIdentityTokenException: Type[Boto3ClientError]
    MalformedPolicyDocumentException: Type[Boto3ClientError]
    PackedPolicyTooLargeException: Type[Boto3ClientError]
    RegionDisabledException: Type[Boto3ClientError]


class STSClient:
    """
    [STS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sts.html#STS.Client)
    """

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
        [Client.assume_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sts.html#STS.Client.assume_role)
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
        [Client.assume_role_with_saml documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sts.html#STS.Client.assume_role_with_saml)
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
        [Client.assume_role_with_web_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sts.html#STS.Client.assume_role_with_web_identity)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sts.html#STS.Client.can_paginate)
        """

    def decode_authorization_message(
        self, EncodedMessage: str
    ) -> DecodeAuthorizationMessageResponseTypeDef:
        """
        [Client.decode_authorization_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sts.html#STS.Client.decode_authorization_message)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sts.html#STS.Client.generate_presigned_url)
        """

    def get_access_key_info(self, AccessKeyId: str) -> GetAccessKeyInfoResponseTypeDef:
        """
        [Client.get_access_key_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sts.html#STS.Client.get_access_key_info)
        """

    def get_caller_identity(self) -> GetCallerIdentityResponseTypeDef:
        """
        [Client.get_caller_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sts.html#STS.Client.get_caller_identity)
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
        [Client.get_federation_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sts.html#STS.Client.get_federation_token)
        """

    def get_session_token(
        self, DurationSeconds: int = None, SerialNumber: str = None, TokenCode: str = None
    ) -> GetSessionTokenResponseTypeDef:
        """
        [Client.get_session_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sts.html#STS.Client.get_session_token)
        """
