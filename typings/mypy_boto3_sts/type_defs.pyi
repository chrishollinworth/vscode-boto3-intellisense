"""
Type annotations for sts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sts.type_defs import AssumeRoleRequestRequestTypeDef

    data: AssumeRoleRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssumeRoleRequestRequestTypeDef",
    "AssumeRoleResponseTypeDef",
    "AssumeRoleWithSAMLRequestRequestTypeDef",
    "AssumeRoleWithSAMLResponseTypeDef",
    "AssumeRoleWithWebIdentityRequestRequestTypeDef",
    "AssumeRoleWithWebIdentityResponseTypeDef",
    "AssumedRoleUserTypeDef",
    "CredentialsTypeDef",
    "DecodeAuthorizationMessageRequestRequestTypeDef",
    "DecodeAuthorizationMessageResponseTypeDef",
    "FederatedUserTypeDef",
    "GetAccessKeyInfoRequestRequestTypeDef",
    "GetAccessKeyInfoResponseTypeDef",
    "GetCallerIdentityResponseTypeDef",
    "GetFederationTokenRequestRequestTypeDef",
    "GetFederationTokenResponseTypeDef",
    "GetSessionTokenRequestRequestTypeDef",
    "GetSessionTokenResponseTypeDef",
    "PolicyDescriptorTypeTypeDef",
    "ResponseMetadataTypeDef",
    "TagTypeDef",
)

_RequiredAssumeRoleRequestRequestTypeDef = TypedDict(
    "_RequiredAssumeRoleRequestRequestTypeDef",
    {
        "RoleArn": str,
        "RoleSessionName": str,
    },
)
_OptionalAssumeRoleRequestRequestTypeDef = TypedDict(
    "_OptionalAssumeRoleRequestRequestTypeDef",
    {
        "PolicyArns": List["PolicyDescriptorTypeTypeDef"],
        "Policy": str,
        "DurationSeconds": int,
        "Tags": List["TagTypeDef"],
        "TransitiveTagKeys": List[str],
        "ExternalId": str,
        "SerialNumber": str,
        "TokenCode": str,
        "SourceIdentity": str,
    },
    total=False,
)

class AssumeRoleRequestRequestTypeDef(
    _RequiredAssumeRoleRequestRequestTypeDef, _OptionalAssumeRoleRequestRequestTypeDef
):
    pass

AssumeRoleResponseTypeDef = TypedDict(
    "AssumeRoleResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "AssumedRoleUser": "AssumedRoleUserTypeDef",
        "PackedPolicySize": int,
        "SourceIdentity": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssumeRoleWithSAMLRequestRequestTypeDef = TypedDict(
    "_RequiredAssumeRoleWithSAMLRequestRequestTypeDef",
    {
        "RoleArn": str,
        "PrincipalArn": str,
        "SAMLAssertion": str,
    },
)
_OptionalAssumeRoleWithSAMLRequestRequestTypeDef = TypedDict(
    "_OptionalAssumeRoleWithSAMLRequestRequestTypeDef",
    {
        "PolicyArns": List["PolicyDescriptorTypeTypeDef"],
        "Policy": str,
        "DurationSeconds": int,
    },
    total=False,
)

class AssumeRoleWithSAMLRequestRequestTypeDef(
    _RequiredAssumeRoleWithSAMLRequestRequestTypeDef,
    _OptionalAssumeRoleWithSAMLRequestRequestTypeDef,
):
    pass

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
        "SourceIdentity": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssumeRoleWithWebIdentityRequestRequestTypeDef = TypedDict(
    "_RequiredAssumeRoleWithWebIdentityRequestRequestTypeDef",
    {
        "RoleArn": str,
        "RoleSessionName": str,
        "WebIdentityToken": str,
    },
)
_OptionalAssumeRoleWithWebIdentityRequestRequestTypeDef = TypedDict(
    "_OptionalAssumeRoleWithWebIdentityRequestRequestTypeDef",
    {
        "ProviderId": str,
        "PolicyArns": List["PolicyDescriptorTypeTypeDef"],
        "Policy": str,
        "DurationSeconds": int,
    },
    total=False,
)

class AssumeRoleWithWebIdentityRequestRequestTypeDef(
    _RequiredAssumeRoleWithWebIdentityRequestRequestTypeDef,
    _OptionalAssumeRoleWithWebIdentityRequestRequestTypeDef,
):
    pass

AssumeRoleWithWebIdentityResponseTypeDef = TypedDict(
    "AssumeRoleWithWebIdentityResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "SubjectFromWebIdentityToken": str,
        "AssumedRoleUser": "AssumedRoleUserTypeDef",
        "PackedPolicySize": int,
        "Provider": str,
        "Audience": str,
        "SourceIdentity": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssumedRoleUserTypeDef = TypedDict(
    "AssumedRoleUserTypeDef",
    {
        "AssumedRoleId": str,
        "Arn": str,
    },
)

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
    },
)

DecodeAuthorizationMessageRequestRequestTypeDef = TypedDict(
    "DecodeAuthorizationMessageRequestRequestTypeDef",
    {
        "EncodedMessage": str,
    },
)

DecodeAuthorizationMessageResponseTypeDef = TypedDict(
    "DecodeAuthorizationMessageResponseTypeDef",
    {
        "DecodedMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FederatedUserTypeDef = TypedDict(
    "FederatedUserTypeDef",
    {
        "FederatedUserId": str,
        "Arn": str,
    },
)

GetAccessKeyInfoRequestRequestTypeDef = TypedDict(
    "GetAccessKeyInfoRequestRequestTypeDef",
    {
        "AccessKeyId": str,
    },
)

GetAccessKeyInfoResponseTypeDef = TypedDict(
    "GetAccessKeyInfoResponseTypeDef",
    {
        "Account": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCallerIdentityResponseTypeDef = TypedDict(
    "GetCallerIdentityResponseTypeDef",
    {
        "UserId": str,
        "Account": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFederationTokenRequestRequestTypeDef = TypedDict(
    "_RequiredGetFederationTokenRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetFederationTokenRequestRequestTypeDef = TypedDict(
    "_OptionalGetFederationTokenRequestRequestTypeDef",
    {
        "Policy": str,
        "PolicyArns": List["PolicyDescriptorTypeTypeDef"],
        "DurationSeconds": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class GetFederationTokenRequestRequestTypeDef(
    _RequiredGetFederationTokenRequestRequestTypeDef,
    _OptionalGetFederationTokenRequestRequestTypeDef,
):
    pass

GetFederationTokenResponseTypeDef = TypedDict(
    "GetFederationTokenResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "FederatedUser": "FederatedUserTypeDef",
        "PackedPolicySize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSessionTokenRequestRequestTypeDef = TypedDict(
    "GetSessionTokenRequestRequestTypeDef",
    {
        "DurationSeconds": int,
        "SerialNumber": str,
        "TokenCode": str,
    },
    total=False,
)

GetSessionTokenResponseTypeDef = TypedDict(
    "GetSessionTokenResponseTypeDef",
    {
        "Credentials": "CredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PolicyDescriptorTypeTypeDef = TypedDict(
    "PolicyDescriptorTypeTypeDef",
    {
        "arn": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
