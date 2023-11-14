"""
Type annotations for cognito-identity service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cognito_identity.type_defs import CognitoIdentityProviderTypeDef

    data: CognitoIdentityProviderTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AmbiguousRoleResolutionTypeType,
    ErrorCodeType,
    MappingRuleMatchTypeType,
    RoleMappingTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CognitoIdentityProviderTypeDef",
    "CreateIdentityPoolInputRequestTypeDef",
    "CredentialsTypeDef",
    "DeleteIdentitiesInputRequestTypeDef",
    "DeleteIdentitiesResponseTypeDef",
    "DeleteIdentityPoolInputRequestTypeDef",
    "DescribeIdentityInputRequestTypeDef",
    "DescribeIdentityPoolInputRequestTypeDef",
    "GetCredentialsForIdentityInputRequestTypeDef",
    "GetCredentialsForIdentityResponseTypeDef",
    "GetIdInputRequestTypeDef",
    "GetIdResponseTypeDef",
    "GetIdentityPoolRolesInputRequestTypeDef",
    "GetIdentityPoolRolesResponseTypeDef",
    "GetOpenIdTokenForDeveloperIdentityInputRequestTypeDef",
    "GetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    "GetOpenIdTokenInputRequestTypeDef",
    "GetOpenIdTokenResponseTypeDef",
    "GetPrincipalTagAttributeMapInputRequestTypeDef",
    "GetPrincipalTagAttributeMapResponseTypeDef",
    "IdentityDescriptionResponseMetadataTypeDef",
    "IdentityDescriptionTypeDef",
    "IdentityPoolRequestTypeDef",
    "IdentityPoolShortDescriptionTypeDef",
    "IdentityPoolTypeDef",
    "ListIdentitiesInputRequestTypeDef",
    "ListIdentitiesResponseTypeDef",
    "ListIdentityPoolsInputRequestTypeDef",
    "ListIdentityPoolsResponseTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LookupDeveloperIdentityInputRequestTypeDef",
    "LookupDeveloperIdentityResponseTypeDef",
    "MappingRuleTypeDef",
    "MergeDeveloperIdentitiesInputRequestTypeDef",
    "MergeDeveloperIdentitiesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RoleMappingTypeDef",
    "RulesConfigurationTypeTypeDef",
    "SetIdentityPoolRolesInputRequestTypeDef",
    "SetPrincipalTagAttributeMapInputRequestTypeDef",
    "SetPrincipalTagAttributeMapResponseTypeDef",
    "TagResourceInputRequestTypeDef",
    "UnlinkDeveloperIdentityInputRequestTypeDef",
    "UnlinkIdentityInputRequestTypeDef",
    "UnprocessedIdentityIdTypeDef",
    "UntagResourceInputRequestTypeDef",
)

CognitoIdentityProviderTypeDef = TypedDict(
    "CognitoIdentityProviderTypeDef",
    {
        "ProviderName": str,
        "ClientId": str,
        "ServerSideTokenCheck": bool,
    },
    total=False,
)

_RequiredCreateIdentityPoolInputRequestTypeDef = TypedDict(
    "_RequiredCreateIdentityPoolInputRequestTypeDef",
    {
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
    },
)
_OptionalCreateIdentityPoolInputRequestTypeDef = TypedDict(
    "_OptionalCreateIdentityPoolInputRequestTypeDef",
    {
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List["CognitoIdentityProviderTypeDef"],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
    },
    total=False,
)

class CreateIdentityPoolInputRequestTypeDef(
    _RequiredCreateIdentityPoolInputRequestTypeDef, _OptionalCreateIdentityPoolInputRequestTypeDef
):
    pass

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessKeyId": str,
        "SecretKey": str,
        "SessionToken": str,
        "Expiration": datetime,
    },
    total=False,
)

DeleteIdentitiesInputRequestTypeDef = TypedDict(
    "DeleteIdentitiesInputRequestTypeDef",
    {
        "IdentityIdsToDelete": List[str],
    },
)

DeleteIdentitiesResponseTypeDef = TypedDict(
    "DeleteIdentitiesResponseTypeDef",
    {
        "UnprocessedIdentityIds": List["UnprocessedIdentityIdTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIdentityPoolInputRequestTypeDef = TypedDict(
    "DeleteIdentityPoolInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

DescribeIdentityInputRequestTypeDef = TypedDict(
    "DescribeIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
    },
)

DescribeIdentityPoolInputRequestTypeDef = TypedDict(
    "DescribeIdentityPoolInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

_RequiredGetCredentialsForIdentityInputRequestTypeDef = TypedDict(
    "_RequiredGetCredentialsForIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
    },
)
_OptionalGetCredentialsForIdentityInputRequestTypeDef = TypedDict(
    "_OptionalGetCredentialsForIdentityInputRequestTypeDef",
    {
        "Logins": Dict[str, str],
        "CustomRoleArn": str,
    },
    total=False,
)

class GetCredentialsForIdentityInputRequestTypeDef(
    _RequiredGetCredentialsForIdentityInputRequestTypeDef,
    _OptionalGetCredentialsForIdentityInputRequestTypeDef,
):
    pass

GetCredentialsForIdentityResponseTypeDef = TypedDict(
    "GetCredentialsForIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "Credentials": "CredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIdInputRequestTypeDef = TypedDict(
    "_RequiredGetIdInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)
_OptionalGetIdInputRequestTypeDef = TypedDict(
    "_OptionalGetIdInputRequestTypeDef",
    {
        "AccountId": str,
        "Logins": Dict[str, str],
    },
    total=False,
)

class GetIdInputRequestTypeDef(
    _RequiredGetIdInputRequestTypeDef, _OptionalGetIdInputRequestTypeDef
):
    pass

GetIdResponseTypeDef = TypedDict(
    "GetIdResponseTypeDef",
    {
        "IdentityId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityPoolRolesInputRequestTypeDef = TypedDict(
    "GetIdentityPoolRolesInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)

GetIdentityPoolRolesResponseTypeDef = TypedDict(
    "GetIdentityPoolRolesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Roles": Dict[str, str],
        "RoleMappings": Dict[str, "RoleMappingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOpenIdTokenForDeveloperIdentityInputRequestTypeDef = TypedDict(
    "_RequiredGetOpenIdTokenForDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "Logins": Dict[str, str],
    },
)
_OptionalGetOpenIdTokenForDeveloperIdentityInputRequestTypeDef = TypedDict(
    "_OptionalGetOpenIdTokenForDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
        "PrincipalTags": Dict[str, str],
        "TokenDuration": int,
    },
    total=False,
)

class GetOpenIdTokenForDeveloperIdentityInputRequestTypeDef(
    _RequiredGetOpenIdTokenForDeveloperIdentityInputRequestTypeDef,
    _OptionalGetOpenIdTokenForDeveloperIdentityInputRequestTypeDef,
):
    pass

GetOpenIdTokenForDeveloperIdentityResponseTypeDef = TypedDict(
    "GetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "Token": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOpenIdTokenInputRequestTypeDef = TypedDict(
    "_RequiredGetOpenIdTokenInputRequestTypeDef",
    {
        "IdentityId": str,
    },
)
_OptionalGetOpenIdTokenInputRequestTypeDef = TypedDict(
    "_OptionalGetOpenIdTokenInputRequestTypeDef",
    {
        "Logins": Dict[str, str],
    },
    total=False,
)

class GetOpenIdTokenInputRequestTypeDef(
    _RequiredGetOpenIdTokenInputRequestTypeDef, _OptionalGetOpenIdTokenInputRequestTypeDef
):
    pass

GetOpenIdTokenResponseTypeDef = TypedDict(
    "GetOpenIdTokenResponseTypeDef",
    {
        "IdentityId": str,
        "Token": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPrincipalTagAttributeMapInputRequestTypeDef = TypedDict(
    "GetPrincipalTagAttributeMapInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
    },
)

GetPrincipalTagAttributeMapResponseTypeDef = TypedDict(
    "GetPrincipalTagAttributeMapResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
        "UseDefaults": bool,
        "PrincipalTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityDescriptionResponseMetadataTypeDef = TypedDict(
    "IdentityDescriptionResponseMetadataTypeDef",
    {
        "IdentityId": str,
        "Logins": List[str],
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityDescriptionTypeDef = TypedDict(
    "IdentityDescriptionTypeDef",
    {
        "IdentityId": str,
        "Logins": List[str],
        "CreationDate": datetime,
        "LastModifiedDate": datetime,
    },
    total=False,
)

_RequiredIdentityPoolRequestTypeDef = TypedDict(
    "_RequiredIdentityPoolRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
    },
)
_OptionalIdentityPoolRequestTypeDef = TypedDict(
    "_OptionalIdentityPoolRequestTypeDef",
    {
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List["CognitoIdentityProviderTypeDef"],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
    },
    total=False,
)

class IdentityPoolRequestTypeDef(
    _RequiredIdentityPoolRequestTypeDef, _OptionalIdentityPoolRequestTypeDef
):
    pass

IdentityPoolShortDescriptionTypeDef = TypedDict(
    "IdentityPoolShortDescriptionTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
    },
    total=False,
)

IdentityPoolTypeDef = TypedDict(
    "IdentityPoolTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityPoolName": str,
        "AllowUnauthenticatedIdentities": bool,
        "AllowClassicFlow": bool,
        "SupportedLoginProviders": Dict[str, str],
        "DeveloperProviderName": str,
        "OpenIdConnectProviderARNs": List[str],
        "CognitoIdentityProviders": List["CognitoIdentityProviderTypeDef"],
        "SamlProviderARNs": List[str],
        "IdentityPoolTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIdentitiesInputRequestTypeDef = TypedDict(
    "_RequiredListIdentitiesInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "MaxResults": int,
    },
)
_OptionalListIdentitiesInputRequestTypeDef = TypedDict(
    "_OptionalListIdentitiesInputRequestTypeDef",
    {
        "NextToken": str,
        "HideDisabled": bool,
    },
    total=False,
)

class ListIdentitiesInputRequestTypeDef(
    _RequiredListIdentitiesInputRequestTypeDef, _OptionalListIdentitiesInputRequestTypeDef
):
    pass

ListIdentitiesResponseTypeDef = TypedDict(
    "ListIdentitiesResponseTypeDef",
    {
        "IdentityPoolId": str,
        "Identities": List["IdentityDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIdentityPoolsInputRequestTypeDef = TypedDict(
    "_RequiredListIdentityPoolsInputRequestTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalListIdentityPoolsInputRequestTypeDef = TypedDict(
    "_OptionalListIdentityPoolsInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListIdentityPoolsInputRequestTypeDef(
    _RequiredListIdentityPoolsInputRequestTypeDef, _OptionalListIdentityPoolsInputRequestTypeDef
):
    pass

ListIdentityPoolsResponseTypeDef = TypedDict(
    "ListIdentityPoolsResponseTypeDef",
    {
        "IdentityPools": List["IdentityPoolShortDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLookupDeveloperIdentityInputRequestTypeDef = TypedDict(
    "_RequiredLookupDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
)
_OptionalLookupDeveloperIdentityInputRequestTypeDef = TypedDict(
    "_OptionalLookupDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
        "DeveloperUserIdentifier": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class LookupDeveloperIdentityInputRequestTypeDef(
    _RequiredLookupDeveloperIdentityInputRequestTypeDef,
    _OptionalLookupDeveloperIdentityInputRequestTypeDef,
):
    pass

LookupDeveloperIdentityResponseTypeDef = TypedDict(
    "LookupDeveloperIdentityResponseTypeDef",
    {
        "IdentityId": str,
        "DeveloperUserIdentifierList": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MappingRuleTypeDef = TypedDict(
    "MappingRuleTypeDef",
    {
        "Claim": str,
        "MatchType": MappingRuleMatchTypeType,
        "Value": str,
        "RoleARN": str,
    },
)

MergeDeveloperIdentitiesInputRequestTypeDef = TypedDict(
    "MergeDeveloperIdentitiesInputRequestTypeDef",
    {
        "SourceUserIdentifier": str,
        "DestinationUserIdentifier": str,
        "DeveloperProviderName": str,
        "IdentityPoolId": str,
    },
)

MergeDeveloperIdentitiesResponseTypeDef = TypedDict(
    "MergeDeveloperIdentitiesResponseTypeDef",
    {
        "IdentityId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
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

_RequiredRoleMappingTypeDef = TypedDict(
    "_RequiredRoleMappingTypeDef",
    {
        "Type": RoleMappingTypeType,
    },
)
_OptionalRoleMappingTypeDef = TypedDict(
    "_OptionalRoleMappingTypeDef",
    {
        "AmbiguousRoleResolution": AmbiguousRoleResolutionTypeType,
        "RulesConfiguration": "RulesConfigurationTypeTypeDef",
    },
    total=False,
)

class RoleMappingTypeDef(_RequiredRoleMappingTypeDef, _OptionalRoleMappingTypeDef):
    pass

RulesConfigurationTypeTypeDef = TypedDict(
    "RulesConfigurationTypeTypeDef",
    {
        "Rules": List["MappingRuleTypeDef"],
    },
)

_RequiredSetIdentityPoolRolesInputRequestTypeDef = TypedDict(
    "_RequiredSetIdentityPoolRolesInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "Roles": Dict[str, str],
    },
)
_OptionalSetIdentityPoolRolesInputRequestTypeDef = TypedDict(
    "_OptionalSetIdentityPoolRolesInputRequestTypeDef",
    {
        "RoleMappings": Dict[str, "RoleMappingTypeDef"],
    },
    total=False,
)

class SetIdentityPoolRolesInputRequestTypeDef(
    _RequiredSetIdentityPoolRolesInputRequestTypeDef,
    _OptionalSetIdentityPoolRolesInputRequestTypeDef,
):
    pass

_RequiredSetPrincipalTagAttributeMapInputRequestTypeDef = TypedDict(
    "_RequiredSetPrincipalTagAttributeMapInputRequestTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
    },
)
_OptionalSetPrincipalTagAttributeMapInputRequestTypeDef = TypedDict(
    "_OptionalSetPrincipalTagAttributeMapInputRequestTypeDef",
    {
        "UseDefaults": bool,
        "PrincipalTags": Dict[str, str],
    },
    total=False,
)

class SetPrincipalTagAttributeMapInputRequestTypeDef(
    _RequiredSetPrincipalTagAttributeMapInputRequestTypeDef,
    _OptionalSetPrincipalTagAttributeMapInputRequestTypeDef,
):
    pass

SetPrincipalTagAttributeMapResponseTypeDef = TypedDict(
    "SetPrincipalTagAttributeMapResponseTypeDef",
    {
        "IdentityPoolId": str,
        "IdentityProviderName": str,
        "UseDefaults": bool,
        "PrincipalTags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UnlinkDeveloperIdentityInputRequestTypeDef = TypedDict(
    "UnlinkDeveloperIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
        "IdentityPoolId": str,
        "DeveloperProviderName": str,
        "DeveloperUserIdentifier": str,
    },
)

UnlinkIdentityInputRequestTypeDef = TypedDict(
    "UnlinkIdentityInputRequestTypeDef",
    {
        "IdentityId": str,
        "Logins": Dict[str, str],
        "LoginsToRemove": List[str],
    },
)

UnprocessedIdentityIdTypeDef = TypedDict(
    "UnprocessedIdentityIdTypeDef",
    {
        "IdentityId": str,
        "ErrorCode": ErrorCodeType,
    },
    total=False,
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)
