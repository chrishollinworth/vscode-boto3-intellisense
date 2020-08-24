"""
Main interface for sts service type definitions.

Usage::

    ```python
    from mypy_boto3_sts.type_defs import AssumedRoleUserTypeDef

    data: AssumedRoleUserTypeDef = {...}
    ```
"""
import sys
from datetime import datetime

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssumedRoleUserTypeDef",
    "CredentialsTypeDef",
    "FederatedUserTypeDef",
    "AssumeRoleResponseTypeDef",
    "AssumeRoleWithSAMLResponseTypeDef",
    "AssumeRoleWithWebIdentityResponseTypeDef",
    "DecodeAuthorizationMessageResponseTypeDef",
    "GetAccessKeyInfoResponseTypeDef",
    "GetCallerIdentityResponseTypeDef",
    "GetFederationTokenResponseTypeDef",
    "GetSessionTokenResponseTypeDef",
    "PolicyDescriptorTypeTypeDef",
    "TagTypeDef",
)

AssumedRoleUserTypeDef = TypedDict("AssumedRoleUserTypeDef", {"AssumedRoleId": str, "Arn": str})

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {"AccessKeyId": str, "SecretAccessKey": str, "SessionToken": str, "Expiration": datetime},
)

FederatedUserTypeDef = TypedDict("FederatedUserTypeDef", {"FederatedUserId": str, "Arn": str})

AssumeRoleResponseTypeDef = TypedDict(
    "AssumeRoleResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "AssumedRoleUser": "AssumedRoleUserTypeDef",
        "PackedPolicySize": int,
    },
    total=False,
)

AssumeRoleWithSAMLResponseTypeDef = TypedDict(
    "AssumeRoleWithSAMLResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "AssumedRoleUser": "AssumedRoleUserTypeDef",
        "PackedPolicySize": int,
        "Subject": str,
        "SubjectType": str,
        "Issuer": str,
        "Audience": str,
        "NameQualifier": str,
    },
    total=False,
)

AssumeRoleWithWebIdentityResponseTypeDef = TypedDict(
    "AssumeRoleWithWebIdentityResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "SubjectFromWebIdentityToken": str,
        "AssumedRoleUser": "AssumedRoleUserTypeDef",
        "PackedPolicySize": int,
        "Provider": str,
        "Audience": str,
    },
    total=False,
)

DecodeAuthorizationMessageResponseTypeDef = TypedDict(
    "DecodeAuthorizationMessageResponseTypeDef", {"DecodedMessage": str}, total=False
)

GetAccessKeyInfoResponseTypeDef = TypedDict(
    "GetAccessKeyInfoResponseTypeDef", {"Account": str}, total=False
)

GetCallerIdentityResponseTypeDef = TypedDict(
    "GetCallerIdentityResponseTypeDef", {"UserId": str, "Account": str, "Arn": str}, total=False
)

GetFederationTokenResponseTypeDef = TypedDict(
    "GetFederationTokenResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "FederatedUser": "FederatedUserTypeDef",
        "PackedPolicySize": int,
    },
    total=False,
)

GetSessionTokenResponseTypeDef = TypedDict(
    "GetSessionTokenResponseTypeDef", {"Credentials": "CredentialsTypeDef"}, total=False
)

PolicyDescriptorTypeTypeDef = TypedDict("PolicyDescriptorTypeTypeDef", {"arn": str}, total=False)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})
