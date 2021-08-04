"""
Type annotations for amplifybackend service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/type_defs.html)

Usage::

    ```python
    from mypy_boto3_amplifybackend.type_defs import BackendAPIAppSyncAuthSettingsTypeDef

    data: BackendAPIAppSyncAuthSettingsTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    AdditionalConstraintsElementType,
    AuthResourcesType,
    DeliveryMethodType,
    MFAModeType,
    MfaTypesElementType,
    ModeType,
    OAuthGrantTypeType,
    OAuthScopesElementType,
    RequiredSignUpAttributesElementType,
    ResolutionStrategyType,
    SignInMethodType,
    StatusType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BackendAPIAppSyncAuthSettingsTypeDef",
    "BackendAPIAuthTypeTypeDef",
    "BackendAPIConflictResolutionTypeDef",
    "BackendAPIResourceConfigTypeDef",
    "BackendAuthAppleProviderConfigTypeDef",
    "BackendAuthSocialProviderConfigTypeDef",
    "BackendJobRespObjTypeDef",
    "CloneBackendRequestRequestTypeDef",
    "CloneBackendResponseTypeDef",
    "CreateBackendAPIRequestRequestTypeDef",
    "CreateBackendAPIResponseTypeDef",
    "CreateBackendAuthForgotPasswordConfigTypeDef",
    "CreateBackendAuthIdentityPoolConfigTypeDef",
    "CreateBackendAuthMFAConfigTypeDef",
    "CreateBackendAuthOAuthConfigTypeDef",
    "CreateBackendAuthPasswordPolicyConfigTypeDef",
    "CreateBackendAuthRequestRequestTypeDef",
    "CreateBackendAuthResourceConfigTypeDef",
    "CreateBackendAuthResponseTypeDef",
    "CreateBackendAuthUserPoolConfigTypeDef",
    "CreateBackendConfigRequestRequestTypeDef",
    "CreateBackendConfigResponseTypeDef",
    "CreateBackendRequestRequestTypeDef",
    "CreateBackendResponseTypeDef",
    "CreateTokenRequestRequestTypeDef",
    "CreateTokenResponseTypeDef",
    "DeleteBackendAPIRequestRequestTypeDef",
    "DeleteBackendAPIResponseTypeDef",
    "DeleteBackendAuthRequestRequestTypeDef",
    "DeleteBackendAuthResponseTypeDef",
    "DeleteBackendRequestRequestTypeDef",
    "DeleteBackendResponseTypeDef",
    "DeleteTokenRequestRequestTypeDef",
    "DeleteTokenResponseTypeDef",
    "EmailSettingsTypeDef",
    "GenerateBackendAPIModelsRequestRequestTypeDef",
    "GenerateBackendAPIModelsResponseTypeDef",
    "GetBackendAPIModelsRequestRequestTypeDef",
    "GetBackendAPIModelsResponseTypeDef",
    "GetBackendAPIRequestRequestTypeDef",
    "GetBackendAPIResponseTypeDef",
    "GetBackendAuthRequestRequestTypeDef",
    "GetBackendAuthResponseTypeDef",
    "GetBackendJobRequestRequestTypeDef",
    "GetBackendJobResponseTypeDef",
    "GetBackendRequestRequestTypeDef",
    "GetBackendResponseTypeDef",
    "GetTokenRequestRequestTypeDef",
    "GetTokenResponseTypeDef",
    "ImportBackendAuthRequestRequestTypeDef",
    "ImportBackendAuthResponseTypeDef",
    "ListBackendJobsRequestRequestTypeDef",
    "ListBackendJobsResponseTypeDef",
    "LoginAuthConfigReqObjTypeDef",
    "PaginatorConfigTypeDef",
    "RemoveAllBackendsRequestRequestTypeDef",
    "RemoveAllBackendsResponseTypeDef",
    "RemoveBackendConfigRequestRequestTypeDef",
    "RemoveBackendConfigResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SettingsTypeDef",
    "SmsSettingsTypeDef",
    "SocialProviderSettingsTypeDef",
    "UpdateBackendAPIRequestRequestTypeDef",
    "UpdateBackendAPIResponseTypeDef",
    "UpdateBackendAuthForgotPasswordConfigTypeDef",
    "UpdateBackendAuthIdentityPoolConfigTypeDef",
    "UpdateBackendAuthMFAConfigTypeDef",
    "UpdateBackendAuthOAuthConfigTypeDef",
    "UpdateBackendAuthPasswordPolicyConfigTypeDef",
    "UpdateBackendAuthRequestRequestTypeDef",
    "UpdateBackendAuthResourceConfigTypeDef",
    "UpdateBackendAuthResponseTypeDef",
    "UpdateBackendAuthUserPoolConfigTypeDef",
    "UpdateBackendConfigRequestRequestTypeDef",
    "UpdateBackendConfigResponseTypeDef",
    "UpdateBackendJobRequestRequestTypeDef",
    "UpdateBackendJobResponseTypeDef",
)

BackendAPIAppSyncAuthSettingsTypeDef = TypedDict(
    "BackendAPIAppSyncAuthSettingsTypeDef",
    {
        "CognitoUserPoolId": str,
        "Description": str,
        "ExpirationTime": float,
        "OpenIDAuthTTL": str,
        "OpenIDClientId": str,
        "OpenIDIatTTL": str,
        "OpenIDIssueURL": str,
        "OpenIDProviderName": str,
    },
    total=False,
)

BackendAPIAuthTypeTypeDef = TypedDict(
    "BackendAPIAuthTypeTypeDef",
    {
        "Mode": ModeType,
        "Settings": "BackendAPIAppSyncAuthSettingsTypeDef",
    },
    total=False,
)

BackendAPIConflictResolutionTypeDef = TypedDict(
    "BackendAPIConflictResolutionTypeDef",
    {
        "ResolutionStrategy": ResolutionStrategyType,
    },
    total=False,
)

BackendAPIResourceConfigTypeDef = TypedDict(
    "BackendAPIResourceConfigTypeDef",
    {
        "AdditionalAuthTypes": List["BackendAPIAuthTypeTypeDef"],
        "ApiName": str,
        "ConflictResolution": "BackendAPIConflictResolutionTypeDef",
        "DefaultAuthType": "BackendAPIAuthTypeTypeDef",
        "Service": str,
        "TransformSchema": str,
    },
    total=False,
)

BackendAuthAppleProviderConfigTypeDef = TypedDict(
    "BackendAuthAppleProviderConfigTypeDef",
    {
        "ClientId": str,
        "KeyId": str,
        "PrivateKey": str,
        "TeamId": str,
    },
    total=False,
)

BackendAuthSocialProviderConfigTypeDef = TypedDict(
    "BackendAuthSocialProviderConfigTypeDef",
    {
        "ClientId": str,
        "ClientSecret": str,
    },
    total=False,
)

_RequiredBackendJobRespObjTypeDef = TypedDict(
    "_RequiredBackendJobRespObjTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
    },
)
_OptionalBackendJobRespObjTypeDef = TypedDict(
    "_OptionalBackendJobRespObjTypeDef",
    {
        "CreateTime": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "UpdateTime": str,
    },
    total=False,
)

class BackendJobRespObjTypeDef(
    _RequiredBackendJobRespObjTypeDef, _OptionalBackendJobRespObjTypeDef
):
    pass

CloneBackendRequestRequestTypeDef = TypedDict(
    "CloneBackendRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "TargetEnvironmentName": str,
    },
)

CloneBackendResponseTypeDef = TypedDict(
    "CloneBackendResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBackendAPIRequestRequestTypeDef = TypedDict(
    "CreateBackendAPIRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": "BackendAPIResourceConfigTypeDef",
        "ResourceName": str,
    },
)

CreateBackendAPIResponseTypeDef = TypedDict(
    "CreateBackendAPIResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBackendAuthForgotPasswordConfigTypeDef = TypedDict(
    "_RequiredCreateBackendAuthForgotPasswordConfigTypeDef",
    {
        "DeliveryMethod": DeliveryMethodType,
    },
)
_OptionalCreateBackendAuthForgotPasswordConfigTypeDef = TypedDict(
    "_OptionalCreateBackendAuthForgotPasswordConfigTypeDef",
    {
        "EmailSettings": "EmailSettingsTypeDef",
        "SmsSettings": "SmsSettingsTypeDef",
    },
    total=False,
)

class CreateBackendAuthForgotPasswordConfigTypeDef(
    _RequiredCreateBackendAuthForgotPasswordConfigTypeDef,
    _OptionalCreateBackendAuthForgotPasswordConfigTypeDef,
):
    pass

CreateBackendAuthIdentityPoolConfigTypeDef = TypedDict(
    "CreateBackendAuthIdentityPoolConfigTypeDef",
    {
        "IdentityPoolName": str,
        "UnauthenticatedLogin": bool,
    },
)

_RequiredCreateBackendAuthMFAConfigTypeDef = TypedDict(
    "_RequiredCreateBackendAuthMFAConfigTypeDef",
    {
        "MFAMode": MFAModeType,
    },
)
_OptionalCreateBackendAuthMFAConfigTypeDef = TypedDict(
    "_OptionalCreateBackendAuthMFAConfigTypeDef",
    {
        "Settings": "SettingsTypeDef",
    },
    total=False,
)

class CreateBackendAuthMFAConfigTypeDef(
    _RequiredCreateBackendAuthMFAConfigTypeDef, _OptionalCreateBackendAuthMFAConfigTypeDef
):
    pass

_RequiredCreateBackendAuthOAuthConfigTypeDef = TypedDict(
    "_RequiredCreateBackendAuthOAuthConfigTypeDef",
    {
        "OAuthGrantType": OAuthGrantTypeType,
        "OAuthScopes": List[OAuthScopesElementType],
        "RedirectSignInURIs": List[str],
        "RedirectSignOutURIs": List[str],
    },
)
_OptionalCreateBackendAuthOAuthConfigTypeDef = TypedDict(
    "_OptionalCreateBackendAuthOAuthConfigTypeDef",
    {
        "DomainPrefix": str,
        "SocialProviderSettings": "SocialProviderSettingsTypeDef",
    },
    total=False,
)

class CreateBackendAuthOAuthConfigTypeDef(
    _RequiredCreateBackendAuthOAuthConfigTypeDef, _OptionalCreateBackendAuthOAuthConfigTypeDef
):
    pass

_RequiredCreateBackendAuthPasswordPolicyConfigTypeDef = TypedDict(
    "_RequiredCreateBackendAuthPasswordPolicyConfigTypeDef",
    {
        "MinimumLength": float,
    },
)
_OptionalCreateBackendAuthPasswordPolicyConfigTypeDef = TypedDict(
    "_OptionalCreateBackendAuthPasswordPolicyConfigTypeDef",
    {
        "AdditionalConstraints": List[AdditionalConstraintsElementType],
    },
    total=False,
)

class CreateBackendAuthPasswordPolicyConfigTypeDef(
    _RequiredCreateBackendAuthPasswordPolicyConfigTypeDef,
    _OptionalCreateBackendAuthPasswordPolicyConfigTypeDef,
):
    pass

CreateBackendAuthRequestRequestTypeDef = TypedDict(
    "CreateBackendAuthRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": "CreateBackendAuthResourceConfigTypeDef",
        "ResourceName": str,
    },
)

_RequiredCreateBackendAuthResourceConfigTypeDef = TypedDict(
    "_RequiredCreateBackendAuthResourceConfigTypeDef",
    {
        "AuthResources": AuthResourcesType,
        "Service": Literal["COGNITO"],
        "UserPoolConfigs": "CreateBackendAuthUserPoolConfigTypeDef",
    },
)
_OptionalCreateBackendAuthResourceConfigTypeDef = TypedDict(
    "_OptionalCreateBackendAuthResourceConfigTypeDef",
    {
        "IdentityPoolConfigs": "CreateBackendAuthIdentityPoolConfigTypeDef",
    },
    total=False,
)

class CreateBackendAuthResourceConfigTypeDef(
    _RequiredCreateBackendAuthResourceConfigTypeDef, _OptionalCreateBackendAuthResourceConfigTypeDef
):
    pass

CreateBackendAuthResponseTypeDef = TypedDict(
    "CreateBackendAuthResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBackendAuthUserPoolConfigTypeDef = TypedDict(
    "_RequiredCreateBackendAuthUserPoolConfigTypeDef",
    {
        "RequiredSignUpAttributes": List[RequiredSignUpAttributesElementType],
        "SignInMethod": SignInMethodType,
        "UserPoolName": str,
    },
)
_OptionalCreateBackendAuthUserPoolConfigTypeDef = TypedDict(
    "_OptionalCreateBackendAuthUserPoolConfigTypeDef",
    {
        "ForgotPassword": "CreateBackendAuthForgotPasswordConfigTypeDef",
        "Mfa": "CreateBackendAuthMFAConfigTypeDef",
        "OAuth": "CreateBackendAuthOAuthConfigTypeDef",
        "PasswordPolicy": "CreateBackendAuthPasswordPolicyConfigTypeDef",
    },
    total=False,
)

class CreateBackendAuthUserPoolConfigTypeDef(
    _RequiredCreateBackendAuthUserPoolConfigTypeDef, _OptionalCreateBackendAuthUserPoolConfigTypeDef
):
    pass

_RequiredCreateBackendConfigRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBackendConfigRequestRequestTypeDef",
    {
        "AppId": str,
    },
)
_OptionalCreateBackendConfigRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBackendConfigRequestRequestTypeDef",
    {
        "BackendManagerAppId": str,
    },
    total=False,
)

class CreateBackendConfigRequestRequestTypeDef(
    _RequiredCreateBackendConfigRequestRequestTypeDef,
    _OptionalCreateBackendConfigRequestRequestTypeDef,
):
    pass

CreateBackendConfigResponseTypeDef = TypedDict(
    "CreateBackendConfigResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBackendRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBackendRequestRequestTypeDef",
    {
        "AppId": str,
        "AppName": str,
        "BackendEnvironmentName": str,
    },
)
_OptionalCreateBackendRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBackendRequestRequestTypeDef",
    {
        "ResourceConfig": Dict[str, Any],
        "ResourceName": str,
    },
    total=False,
)

class CreateBackendRequestRequestTypeDef(
    _RequiredCreateBackendRequestRequestTypeDef, _OptionalCreateBackendRequestRequestTypeDef
):
    pass

CreateBackendResponseTypeDef = TypedDict(
    "CreateBackendResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTokenRequestRequestTypeDef = TypedDict(
    "CreateTokenRequestRequestTypeDef",
    {
        "AppId": str,
    },
)

CreateTokenResponseTypeDef = TypedDict(
    "CreateTokenResponseTypeDef",
    {
        "AppId": str,
        "ChallengeCode": str,
        "SessionId": str,
        "Ttl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteBackendAPIRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBackendAPIRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)
_OptionalDeleteBackendAPIRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBackendAPIRequestRequestTypeDef",
    {
        "ResourceConfig": "BackendAPIResourceConfigTypeDef",
    },
    total=False,
)

class DeleteBackendAPIRequestRequestTypeDef(
    _RequiredDeleteBackendAPIRequestRequestTypeDef, _OptionalDeleteBackendAPIRequestRequestTypeDef
):
    pass

DeleteBackendAPIResponseTypeDef = TypedDict(
    "DeleteBackendAPIResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackendAuthRequestRequestTypeDef = TypedDict(
    "DeleteBackendAuthRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)

DeleteBackendAuthResponseTypeDef = TypedDict(
    "DeleteBackendAuthResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackendRequestRequestTypeDef = TypedDict(
    "DeleteBackendRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
    },
)

DeleteBackendResponseTypeDef = TypedDict(
    "DeleteBackendResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTokenRequestRequestTypeDef = TypedDict(
    "DeleteTokenRequestRequestTypeDef",
    {
        "AppId": str,
        "SessionId": str,
    },
)

DeleteTokenResponseTypeDef = TypedDict(
    "DeleteTokenResponseTypeDef",
    {
        "IsSuccess": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EmailSettingsTypeDef = TypedDict(
    "EmailSettingsTypeDef",
    {
        "EmailMessage": str,
        "EmailSubject": str,
    },
    total=False,
)

GenerateBackendAPIModelsRequestRequestTypeDef = TypedDict(
    "GenerateBackendAPIModelsRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)

GenerateBackendAPIModelsResponseTypeDef = TypedDict(
    "GenerateBackendAPIModelsResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackendAPIModelsRequestRequestTypeDef = TypedDict(
    "GetBackendAPIModelsRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)

GetBackendAPIModelsResponseTypeDef = TypedDict(
    "GetBackendAPIModelsResponseTypeDef",
    {
        "Models": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBackendAPIRequestRequestTypeDef = TypedDict(
    "_RequiredGetBackendAPIRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)
_OptionalGetBackendAPIRequestRequestTypeDef = TypedDict(
    "_OptionalGetBackendAPIRequestRequestTypeDef",
    {
        "ResourceConfig": "BackendAPIResourceConfigTypeDef",
    },
    total=False,
)

class GetBackendAPIRequestRequestTypeDef(
    _RequiredGetBackendAPIRequestRequestTypeDef, _OptionalGetBackendAPIRequestRequestTypeDef
):
    pass

GetBackendAPIResponseTypeDef = TypedDict(
    "GetBackendAPIResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "ResourceConfig": "BackendAPIResourceConfigTypeDef",
        "ResourceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackendAuthRequestRequestTypeDef = TypedDict(
    "GetBackendAuthRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)

GetBackendAuthResponseTypeDef = TypedDict(
    "GetBackendAuthResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "ResourceConfig": "CreateBackendAuthResourceConfigTypeDef",
        "ResourceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBackendJobRequestRequestTypeDef = TypedDict(
    "GetBackendJobRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
    },
)

GetBackendJobResponseTypeDef = TypedDict(
    "GetBackendJobResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "CreateTime": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "UpdateTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBackendRequestRequestTypeDef = TypedDict(
    "_RequiredGetBackendRequestRequestTypeDef",
    {
        "AppId": str,
    },
)
_OptionalGetBackendRequestRequestTypeDef = TypedDict(
    "_OptionalGetBackendRequestRequestTypeDef",
    {
        "BackendEnvironmentName": str,
    },
    total=False,
)

class GetBackendRequestRequestTypeDef(
    _RequiredGetBackendRequestRequestTypeDef, _OptionalGetBackendRequestRequestTypeDef
):
    pass

GetBackendResponseTypeDef = TypedDict(
    "GetBackendResponseTypeDef",
    {
        "AmplifyMetaConfig": str,
        "AppId": str,
        "AppName": str,
        "BackendEnvironmentList": List[str],
        "BackendEnvironmentName": str,
        "Error": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTokenRequestRequestTypeDef = TypedDict(
    "GetTokenRequestRequestTypeDef",
    {
        "AppId": str,
        "SessionId": str,
    },
)

GetTokenResponseTypeDef = TypedDict(
    "GetTokenResponseTypeDef",
    {
        "AppId": str,
        "ChallengeCode": str,
        "SessionId": str,
        "Ttl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportBackendAuthRequestRequestTypeDef = TypedDict(
    "_RequiredImportBackendAuthRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "NativeClientId": str,
        "UserPoolId": str,
        "WebClientId": str,
    },
)
_OptionalImportBackendAuthRequestRequestTypeDef = TypedDict(
    "_OptionalImportBackendAuthRequestRequestTypeDef",
    {
        "IdentityPoolId": str,
    },
    total=False,
)

class ImportBackendAuthRequestRequestTypeDef(
    _RequiredImportBackendAuthRequestRequestTypeDef, _OptionalImportBackendAuthRequestRequestTypeDef
):
    pass

ImportBackendAuthResponseTypeDef = TypedDict(
    "ImportBackendAuthResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListBackendJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListBackendJobsRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
    },
)
_OptionalListBackendJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListBackendJobsRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxResults": int,
        "NextToken": str,
        "Operation": str,
        "Status": str,
    },
    total=False,
)

class ListBackendJobsRequestRequestTypeDef(
    _RequiredListBackendJobsRequestRequestTypeDef, _OptionalListBackendJobsRequestRequestTypeDef
):
    pass

ListBackendJobsResponseTypeDef = TypedDict(
    "ListBackendJobsResponseTypeDef",
    {
        "Jobs": List["BackendJobRespObjTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoginAuthConfigReqObjTypeDef = TypedDict(
    "LoginAuthConfigReqObjTypeDef",
    {
        "AwsCognitoIdentityPoolId": str,
        "AwsCognitoRegion": str,
        "AwsUserPoolsId": str,
        "AwsUserPoolsWebClientId": str,
    },
    total=False,
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

_RequiredRemoveAllBackendsRequestRequestTypeDef = TypedDict(
    "_RequiredRemoveAllBackendsRequestRequestTypeDef",
    {
        "AppId": str,
    },
)
_OptionalRemoveAllBackendsRequestRequestTypeDef = TypedDict(
    "_OptionalRemoveAllBackendsRequestRequestTypeDef",
    {
        "CleanAmplifyApp": bool,
    },
    total=False,
)

class RemoveAllBackendsRequestRequestTypeDef(
    _RequiredRemoveAllBackendsRequestRequestTypeDef, _OptionalRemoveAllBackendsRequestRequestTypeDef
):
    pass

RemoveAllBackendsResponseTypeDef = TypedDict(
    "RemoveAllBackendsResponseTypeDef",
    {
        "AppId": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveBackendConfigRequestRequestTypeDef = TypedDict(
    "RemoveBackendConfigRequestRequestTypeDef",
    {
        "AppId": str,
    },
)

RemoveBackendConfigResponseTypeDef = TypedDict(
    "RemoveBackendConfigResponseTypeDef",
    {
        "Error": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "MfaTypes": List[MfaTypesElementType],
        "SmsMessage": str,
    },
    total=False,
)

SmsSettingsTypeDef = TypedDict(
    "SmsSettingsTypeDef",
    {
        "SmsMessage": str,
    },
    total=False,
)

SocialProviderSettingsTypeDef = TypedDict(
    "SocialProviderSettingsTypeDef",
    {
        "Facebook": "BackendAuthSocialProviderConfigTypeDef",
        "Google": "BackendAuthSocialProviderConfigTypeDef",
        "LoginWithAmazon": "BackendAuthSocialProviderConfigTypeDef",
        "SignInWithApple": "BackendAuthAppleProviderConfigTypeDef",
    },
    total=False,
)

_RequiredUpdateBackendAPIRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBackendAPIRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
    },
)
_OptionalUpdateBackendAPIRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBackendAPIRequestRequestTypeDef",
    {
        "ResourceConfig": "BackendAPIResourceConfigTypeDef",
    },
    total=False,
)

class UpdateBackendAPIRequestRequestTypeDef(
    _RequiredUpdateBackendAPIRequestRequestTypeDef, _OptionalUpdateBackendAPIRequestRequestTypeDef
):
    pass

UpdateBackendAPIResponseTypeDef = TypedDict(
    "UpdateBackendAPIResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBackendAuthForgotPasswordConfigTypeDef = TypedDict(
    "UpdateBackendAuthForgotPasswordConfigTypeDef",
    {
        "DeliveryMethod": DeliveryMethodType,
        "EmailSettings": "EmailSettingsTypeDef",
        "SmsSettings": "SmsSettingsTypeDef",
    },
    total=False,
)

UpdateBackendAuthIdentityPoolConfigTypeDef = TypedDict(
    "UpdateBackendAuthIdentityPoolConfigTypeDef",
    {
        "UnauthenticatedLogin": bool,
    },
    total=False,
)

UpdateBackendAuthMFAConfigTypeDef = TypedDict(
    "UpdateBackendAuthMFAConfigTypeDef",
    {
        "MFAMode": MFAModeType,
        "Settings": "SettingsTypeDef",
    },
    total=False,
)

UpdateBackendAuthOAuthConfigTypeDef = TypedDict(
    "UpdateBackendAuthOAuthConfigTypeDef",
    {
        "DomainPrefix": str,
        "OAuthGrantType": OAuthGrantTypeType,
        "OAuthScopes": List[OAuthScopesElementType],
        "RedirectSignInURIs": List[str],
        "RedirectSignOutURIs": List[str],
        "SocialProviderSettings": "SocialProviderSettingsTypeDef",
    },
    total=False,
)

UpdateBackendAuthPasswordPolicyConfigTypeDef = TypedDict(
    "UpdateBackendAuthPasswordPolicyConfigTypeDef",
    {
        "AdditionalConstraints": List[AdditionalConstraintsElementType],
        "MinimumLength": float,
    },
    total=False,
)

UpdateBackendAuthRequestRequestTypeDef = TypedDict(
    "UpdateBackendAuthRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceConfig": "UpdateBackendAuthResourceConfigTypeDef",
        "ResourceName": str,
    },
)

_RequiredUpdateBackendAuthResourceConfigTypeDef = TypedDict(
    "_RequiredUpdateBackendAuthResourceConfigTypeDef",
    {
        "AuthResources": AuthResourcesType,
        "Service": Literal["COGNITO"],
        "UserPoolConfigs": "UpdateBackendAuthUserPoolConfigTypeDef",
    },
)
_OptionalUpdateBackendAuthResourceConfigTypeDef = TypedDict(
    "_OptionalUpdateBackendAuthResourceConfigTypeDef",
    {
        "IdentityPoolConfigs": "UpdateBackendAuthIdentityPoolConfigTypeDef",
    },
    total=False,
)

class UpdateBackendAuthResourceConfigTypeDef(
    _RequiredUpdateBackendAuthResourceConfigTypeDef, _OptionalUpdateBackendAuthResourceConfigTypeDef
):
    pass

UpdateBackendAuthResponseTypeDef = TypedDict(
    "UpdateBackendAuthResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBackendAuthUserPoolConfigTypeDef = TypedDict(
    "UpdateBackendAuthUserPoolConfigTypeDef",
    {
        "ForgotPassword": "UpdateBackendAuthForgotPasswordConfigTypeDef",
        "Mfa": "UpdateBackendAuthMFAConfigTypeDef",
        "OAuth": "UpdateBackendAuthOAuthConfigTypeDef",
        "PasswordPolicy": "UpdateBackendAuthPasswordPolicyConfigTypeDef",
    },
    total=False,
)

_RequiredUpdateBackendConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBackendConfigRequestRequestTypeDef",
    {
        "AppId": str,
    },
)
_OptionalUpdateBackendConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBackendConfigRequestRequestTypeDef",
    {
        "LoginAuthConfig": "LoginAuthConfigReqObjTypeDef",
    },
    total=False,
)

class UpdateBackendConfigRequestRequestTypeDef(
    _RequiredUpdateBackendConfigRequestRequestTypeDef,
    _OptionalUpdateBackendConfigRequestRequestTypeDef,
):
    pass

UpdateBackendConfigResponseTypeDef = TypedDict(
    "UpdateBackendConfigResponseTypeDef",
    {
        "AppId": str,
        "BackendManagerAppId": str,
        "Error": str,
        "LoginAuthConfig": "LoginAuthConfigReqObjTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBackendJobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBackendJobRequestRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "JobId": str,
    },
)
_OptionalUpdateBackendJobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBackendJobRequestRequestTypeDef",
    {
        "Operation": str,
        "Status": str,
    },
    total=False,
)

class UpdateBackendJobRequestRequestTypeDef(
    _RequiredUpdateBackendJobRequestRequestTypeDef, _OptionalUpdateBackendJobRequestRequestTypeDef
):
    pass

UpdateBackendJobResponseTypeDef = TypedDict(
    "UpdateBackendJobResponseTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "CreateTime": str,
        "Error": str,
        "JobId": str,
        "Operation": str,
        "Status": str,
        "UpdateTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
