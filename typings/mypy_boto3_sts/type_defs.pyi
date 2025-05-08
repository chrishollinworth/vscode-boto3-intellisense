"""
Type annotations for sts service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_sts.type_defs import PolicyDescriptorTypeTypeDef

    data: PolicyDescriptorTypeTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from collections.abc import Sequence
else:
    from typing import Dict, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AssumeRoleRequestTypeDef",
    "AssumeRoleResponseTypeDef",
    "AssumeRoleWithSAMLRequestTypeDef",
    "AssumeRoleWithSAMLResponseTypeDef",
    "AssumeRoleWithWebIdentityRequestTypeDef",
    "AssumeRoleWithWebIdentityResponseTypeDef",
    "AssumeRootRequestTypeDef",
    "AssumeRootResponseTypeDef",
    "AssumedRoleUserTypeDef",
    "CredentialsTypeDef",
    "DecodeAuthorizationMessageRequestTypeDef",
    "DecodeAuthorizationMessageResponseTypeDef",
    "FederatedUserTypeDef",
    "GetAccessKeyInfoRequestTypeDef",
    "GetAccessKeyInfoResponseTypeDef",
    "GetCallerIdentityResponseTypeDef",
    "GetFederationTokenRequestTypeDef",
    "GetFederationTokenResponseTypeDef",
    "GetSessionTokenRequestTypeDef",
    "GetSessionTokenResponseTypeDef",
    "PolicyDescriptorTypeTypeDef",
    "ProvidedContextTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
)

class PolicyDescriptorTypeTypeDef(TypedDict):
    arn: NotRequired[str]

class ProvidedContextTypeDef(TypedDict):
    ProviderArn: NotRequired[str]
    ContextAssertion: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class AssumedRoleUserTypeDef(TypedDict):
    AssumedRoleId: str
    Arn: str

class CredentialsTypeDef(TypedDict):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DecodeAuthorizationMessageRequestTypeDef(TypedDict):
    EncodedMessage: str

class FederatedUserTypeDef(TypedDict):
    FederatedUserId: str
    Arn: str

class GetAccessKeyInfoRequestTypeDef(TypedDict):
    AccessKeyId: str

class GetSessionTokenRequestTypeDef(TypedDict):
    DurationSeconds: NotRequired[int]
    SerialNumber: NotRequired[str]
    TokenCode: NotRequired[str]

class AssumeRoleWithSAMLRequestTypeDef(TypedDict):
    RoleArn: str
    PrincipalArn: str
    SAMLAssertion: str
    PolicyArns: NotRequired[Sequence[PolicyDescriptorTypeTypeDef]]
    Policy: NotRequired[str]
    DurationSeconds: NotRequired[int]

class AssumeRoleWithWebIdentityRequestTypeDef(TypedDict):
    RoleArn: str
    RoleSessionName: str
    WebIdentityToken: str
    ProviderId: NotRequired[str]
    PolicyArns: NotRequired[Sequence[PolicyDescriptorTypeTypeDef]]
    Policy: NotRequired[str]
    DurationSeconds: NotRequired[int]

class AssumeRootRequestTypeDef(TypedDict):
    TargetPrincipal: str
    TaskPolicyArn: PolicyDescriptorTypeTypeDef
    DurationSeconds: NotRequired[int]

class AssumeRoleRequestTypeDef(TypedDict):
    RoleArn: str
    RoleSessionName: str
    PolicyArns: NotRequired[Sequence[PolicyDescriptorTypeTypeDef]]
    Policy: NotRequired[str]
    DurationSeconds: NotRequired[int]
    Tags: NotRequired[Sequence[TagTypeDef]]
    TransitiveTagKeys: NotRequired[Sequence[str]]
    ExternalId: NotRequired[str]
    SerialNumber: NotRequired[str]
    TokenCode: NotRequired[str]
    SourceIdentity: NotRequired[str]
    ProvidedContexts: NotRequired[Sequence[ProvidedContextTypeDef]]

class GetFederationTokenRequestTypeDef(TypedDict):
    Name: str
    Policy: NotRequired[str]
    PolicyArns: NotRequired[Sequence[PolicyDescriptorTypeTypeDef]]
    DurationSeconds: NotRequired[int]
    Tags: NotRequired[Sequence[TagTypeDef]]

class AssumeRoleResponseTypeDef(TypedDict):
    Credentials: CredentialsTypeDef
    AssumedRoleUser: AssumedRoleUserTypeDef
    PackedPolicySize: int
    SourceIdentity: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeRoleWithSAMLResponseTypeDef(TypedDict):
    Credentials: CredentialsTypeDef
    AssumedRoleUser: AssumedRoleUserTypeDef
    PackedPolicySize: int
    Subject: str
    SubjectType: str
    Issuer: str
    Audience: str
    NameQualifier: str
    SourceIdentity: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeRoleWithWebIdentityResponseTypeDef(TypedDict):
    Credentials: CredentialsTypeDef
    SubjectFromWebIdentityToken: str
    AssumedRoleUser: AssumedRoleUserTypeDef
    PackedPolicySize: int
    Provider: str
    Audience: str
    SourceIdentity: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssumeRootResponseTypeDef(TypedDict):
    Credentials: CredentialsTypeDef
    SourceIdentity: str
    ResponseMetadata: ResponseMetadataTypeDef

class DecodeAuthorizationMessageResponseTypeDef(TypedDict):
    DecodedMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessKeyInfoResponseTypeDef(TypedDict):
    Account: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCallerIdentityResponseTypeDef(TypedDict):
    UserId: str
    Account: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSessionTokenResponseTypeDef(TypedDict):
    Credentials: CredentialsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFederationTokenResponseTypeDef(TypedDict):
    Credentials: CredentialsTypeDef
    FederatedUser: FederatedUserTypeDef
    PackedPolicySize: int
    ResponseMetadata: ResponseMetadataTypeDef
