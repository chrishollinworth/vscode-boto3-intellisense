"""
Type annotations for amplifybackend service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_amplifybackend.type_defs import BackendAPIAppSyncAuthSettingsTypeDef

    data: BackendAPIAppSyncAuthSettingsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Any, Union

from .literals import (
    AdditionalConstraintsElementType,
    AuthenticatedElementType,
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
    UnAuthenticatedElementType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "BackendAPIAppSyncAuthSettingsTypeDef",
    "BackendAPIAuthTypeTypeDef",
    "BackendAPIConflictResolutionTypeDef",
    "BackendAPIResourceConfigOutputTypeDef",
    "BackendAPIResourceConfigTypeDef",
    "BackendAPIResourceConfigUnionTypeDef",
    "BackendAuthAppleProviderConfigTypeDef",
    "BackendAuthSocialProviderConfigTypeDef",
    "BackendJobRespObjTypeDef",
    "BackendStoragePermissionsOutputTypeDef",
    "BackendStoragePermissionsTypeDef",
    "BackendStoragePermissionsUnionTypeDef",
    "CloneBackendRequestTypeDef",
    "CloneBackendResponseTypeDef",
    "CreateBackendAPIRequestTypeDef",
    "CreateBackendAPIResponseTypeDef",
    "CreateBackendAuthForgotPasswordConfigTypeDef",
    "CreateBackendAuthIdentityPoolConfigTypeDef",
    "CreateBackendAuthMFAConfigOutputTypeDef",
    "CreateBackendAuthMFAConfigTypeDef",
    "CreateBackendAuthOAuthConfigOutputTypeDef",
    "CreateBackendAuthOAuthConfigTypeDef",
    "CreateBackendAuthPasswordPolicyConfigOutputTypeDef",
    "CreateBackendAuthPasswordPolicyConfigTypeDef",
    "CreateBackendAuthRequestTypeDef",
    "CreateBackendAuthResourceConfigOutputTypeDef",
    "CreateBackendAuthResourceConfigTypeDef",
    "CreateBackendAuthResourceConfigUnionTypeDef",
    "CreateBackendAuthResponseTypeDef",
    "CreateBackendAuthUserPoolConfigOutputTypeDef",
    "CreateBackendAuthUserPoolConfigTypeDef",
    "CreateBackendAuthVerificationMessageConfigTypeDef",
    "CreateBackendConfigRequestTypeDef",
    "CreateBackendConfigResponseTypeDef",
    "CreateBackendRequestTypeDef",
    "CreateBackendResponseTypeDef",
    "CreateBackendStorageRequestTypeDef",
    "CreateBackendStorageResourceConfigTypeDef",
    "CreateBackendStorageResponseTypeDef",
    "CreateTokenRequestTypeDef",
    "CreateTokenResponseTypeDef",
    "DeleteBackendAPIRequestTypeDef",
    "DeleteBackendAPIResponseTypeDef",
    "DeleteBackendAuthRequestTypeDef",
    "DeleteBackendAuthResponseTypeDef",
    "DeleteBackendRequestTypeDef",
    "DeleteBackendResponseTypeDef",
    "DeleteBackendStorageRequestTypeDef",
    "DeleteBackendStorageResponseTypeDef",
    "DeleteTokenRequestTypeDef",
    "DeleteTokenResponseTypeDef",
    "EmailSettingsTypeDef",
    "GenerateBackendAPIModelsRequestTypeDef",
    "GenerateBackendAPIModelsResponseTypeDef",
    "GetBackendAPIModelsRequestTypeDef",
    "GetBackendAPIModelsResponseTypeDef",
    "GetBackendAPIRequestTypeDef",
    "GetBackendAPIResponseTypeDef",
    "GetBackendAuthRequestTypeDef",
    "GetBackendAuthResponseTypeDef",
    "GetBackendJobRequestTypeDef",
    "GetBackendJobResponseTypeDef",
    "GetBackendRequestTypeDef",
    "GetBackendResponseTypeDef",
    "GetBackendStorageRequestTypeDef",
    "GetBackendStorageResourceConfigTypeDef",
    "GetBackendStorageResponseTypeDef",
    "GetTokenRequestTypeDef",
    "GetTokenResponseTypeDef",
    "ImportBackendAuthRequestTypeDef",
    "ImportBackendAuthResponseTypeDef",
    "ImportBackendStorageRequestTypeDef",
    "ImportBackendStorageResponseTypeDef",
    "ListBackendJobsRequestPaginateTypeDef",
    "ListBackendJobsRequestTypeDef",
    "ListBackendJobsResponseTypeDef",
    "ListS3BucketsRequestTypeDef",
    "ListS3BucketsResponseTypeDef",
    "LoginAuthConfigReqObjTypeDef",
    "PaginatorConfigTypeDef",
    "RemoveAllBackendsRequestTypeDef",
    "RemoveAllBackendsResponseTypeDef",
    "RemoveBackendConfigRequestTypeDef",
    "RemoveBackendConfigResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3BucketInfoTypeDef",
    "SettingsOutputTypeDef",
    "SettingsTypeDef",
    "SettingsUnionTypeDef",
    "SmsSettingsTypeDef",
    "SocialProviderSettingsTypeDef",
    "UpdateBackendAPIRequestTypeDef",
    "UpdateBackendAPIResponseTypeDef",
    "UpdateBackendAuthForgotPasswordConfigTypeDef",
    "UpdateBackendAuthIdentityPoolConfigTypeDef",
    "UpdateBackendAuthMFAConfigTypeDef",
    "UpdateBackendAuthOAuthConfigTypeDef",
    "UpdateBackendAuthPasswordPolicyConfigTypeDef",
    "UpdateBackendAuthRequestTypeDef",
    "UpdateBackendAuthResourceConfigTypeDef",
    "UpdateBackendAuthResponseTypeDef",
    "UpdateBackendAuthUserPoolConfigTypeDef",
    "UpdateBackendAuthVerificationMessageConfigTypeDef",
    "UpdateBackendConfigRequestTypeDef",
    "UpdateBackendConfigResponseTypeDef",
    "UpdateBackendJobRequestTypeDef",
    "UpdateBackendJobResponseTypeDef",
    "UpdateBackendStorageRequestTypeDef",
    "UpdateBackendStorageResourceConfigTypeDef",
    "UpdateBackendStorageResponseTypeDef",
)

class BackendAPIAppSyncAuthSettingsTypeDef(TypedDict):
    CognitoUserPoolId: NotRequired[str]
    Description: NotRequired[str]
    ExpirationTime: NotRequired[float]
    OpenIDAuthTTL: NotRequired[str]
    OpenIDClientId: NotRequired[str]
    OpenIDIatTTL: NotRequired[str]
    OpenIDIssueURL: NotRequired[str]
    OpenIDProviderName: NotRequired[str]

class BackendAPIConflictResolutionTypeDef(TypedDict):
    ResolutionStrategy: NotRequired[ResolutionStrategyType]

class BackendAuthAppleProviderConfigTypeDef(TypedDict):
    ClientId: NotRequired[str]
    KeyId: NotRequired[str]
    PrivateKey: NotRequired[str]
    TeamId: NotRequired[str]

class BackendAuthSocialProviderConfigTypeDef(TypedDict):
    ClientId: NotRequired[str]
    ClientSecret: NotRequired[str]

class BackendJobRespObjTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    CreateTime: NotRequired[str]
    Error: NotRequired[str]
    JobId: NotRequired[str]
    Operation: NotRequired[str]
    Status: NotRequired[str]
    UpdateTime: NotRequired[str]

class BackendStoragePermissionsOutputTypeDef(TypedDict):
    Authenticated: List[AuthenticatedElementType]
    UnAuthenticated: NotRequired[List[UnAuthenticatedElementType]]

class BackendStoragePermissionsTypeDef(TypedDict):
    Authenticated: Sequence[AuthenticatedElementType]
    UnAuthenticated: NotRequired[Sequence[UnAuthenticatedElementType]]

class CloneBackendRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    TargetEnvironmentName: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class EmailSettingsTypeDef(TypedDict):
    EmailMessage: NotRequired[str]
    EmailSubject: NotRequired[str]

class SmsSettingsTypeDef(TypedDict):
    SmsMessage: NotRequired[str]

class CreateBackendAuthIdentityPoolConfigTypeDef(TypedDict):
    IdentityPoolName: str
    UnauthenticatedLogin: bool

class SettingsOutputTypeDef(TypedDict):
    MfaTypes: NotRequired[List[MfaTypesElementType]]
    SmsMessage: NotRequired[str]

class SettingsTypeDef(TypedDict):
    MfaTypes: NotRequired[Sequence[MfaTypesElementType]]
    SmsMessage: NotRequired[str]

class CreateBackendAuthPasswordPolicyConfigOutputTypeDef(TypedDict):
    MinimumLength: float
    AdditionalConstraints: NotRequired[List[AdditionalConstraintsElementType]]

class CreateBackendAuthPasswordPolicyConfigTypeDef(TypedDict):
    MinimumLength: float
    AdditionalConstraints: NotRequired[Sequence[AdditionalConstraintsElementType]]

class CreateBackendConfigRequestTypeDef(TypedDict):
    AppId: str
    BackendManagerAppId: NotRequired[str]

class CreateBackendRequestTypeDef(TypedDict):
    AppId: str
    AppName: str
    BackendEnvironmentName: str
    ResourceConfig: NotRequired[Mapping[str, Any]]
    ResourceName: NotRequired[str]

class CreateTokenRequestTypeDef(TypedDict):
    AppId: str

class DeleteBackendAuthRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str

class DeleteBackendRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str

DeleteBackendStorageRequestTypeDef = TypedDict(
    "DeleteBackendStorageRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ResourceName": str,
        "ServiceName": Literal["S3"],
    },
)

class DeleteTokenRequestTypeDef(TypedDict):
    AppId: str
    SessionId: str

class GenerateBackendAPIModelsRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str

class GetBackendAPIModelsRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str

class GetBackendAuthRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str

class GetBackendJobRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    JobId: str

class GetBackendRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: NotRequired[str]

class GetBackendStorageRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str

class GetTokenRequestTypeDef(TypedDict):
    AppId: str
    SessionId: str

class ImportBackendAuthRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    NativeClientId: str
    UserPoolId: str
    WebClientId: str
    IdentityPoolId: NotRequired[str]

ImportBackendStorageRequestTypeDef = TypedDict(
    "ImportBackendStorageRequestTypeDef",
    {
        "AppId": str,
        "BackendEnvironmentName": str,
        "ServiceName": Literal["S3"],
        "BucketName": NotRequired[str],
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListBackendJobsRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    JobId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Operation: NotRequired[str]
    Status: NotRequired[str]

class ListS3BucketsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]

class S3BucketInfoTypeDef(TypedDict):
    CreationDate: NotRequired[str]
    Name: NotRequired[str]

class LoginAuthConfigReqObjTypeDef(TypedDict):
    AwsCognitoIdentityPoolId: NotRequired[str]
    AwsCognitoRegion: NotRequired[str]
    AwsUserPoolsId: NotRequired[str]
    AwsUserPoolsWebClientId: NotRequired[str]

class RemoveAllBackendsRequestTypeDef(TypedDict):
    AppId: str
    CleanAmplifyApp: NotRequired[bool]

class RemoveBackendConfigRequestTypeDef(TypedDict):
    AppId: str

class UpdateBackendAuthIdentityPoolConfigTypeDef(TypedDict):
    UnauthenticatedLogin: NotRequired[bool]

class UpdateBackendAuthPasswordPolicyConfigTypeDef(TypedDict):
    AdditionalConstraints: NotRequired[Sequence[AdditionalConstraintsElementType]]
    MinimumLength: NotRequired[float]

class UpdateBackendJobRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Operation: NotRequired[str]
    Status: NotRequired[str]

class BackendAPIAuthTypeTypeDef(TypedDict):
    Mode: NotRequired[ModeType]
    Settings: NotRequired[BackendAPIAppSyncAuthSettingsTypeDef]

class SocialProviderSettingsTypeDef(TypedDict):
    Facebook: NotRequired[BackendAuthSocialProviderConfigTypeDef]
    Google: NotRequired[BackendAuthSocialProviderConfigTypeDef]
    LoginWithAmazon: NotRequired[BackendAuthSocialProviderConfigTypeDef]
    SignInWithApple: NotRequired[BackendAuthAppleProviderConfigTypeDef]

GetBackendStorageResourceConfigTypeDef = TypedDict(
    "GetBackendStorageResourceConfigTypeDef",
    {
        "Imported": bool,
        "ServiceName": Literal["S3"],
        "BucketName": NotRequired[str],
        "Permissions": NotRequired[BackendStoragePermissionsOutputTypeDef],
    },
)
BackendStoragePermissionsUnionTypeDef = Union[
    BackendStoragePermissionsTypeDef, BackendStoragePermissionsOutputTypeDef
]

class CloneBackendResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackendAPIResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackendAuthResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackendConfigResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackendResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackendStorageResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTokenResponseTypeDef(TypedDict):
    AppId: str
    ChallengeCode: str
    SessionId: str
    Ttl: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackendAPIResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackendAuthResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackendResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackendStorageResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTokenResponseTypeDef(TypedDict):
    IsSuccess: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateBackendAPIModelsResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackendAPIModelsResponseTypeDef(TypedDict):
    Models: str
    Status: StatusType
    ModelIntrospectionSchema: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackendJobResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    CreateTime: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    UpdateTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBackendResponseTypeDef(TypedDict):
    AmplifyFeatureFlags: str
    AmplifyMetaConfig: str
    AppId: str
    AppName: str
    BackendEnvironmentList: List[str]
    BackendEnvironmentName: str
    Error: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTokenResponseTypeDef(TypedDict):
    AppId: str
    ChallengeCode: str
    SessionId: str
    Ttl: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportBackendAuthResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportBackendStorageResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackendJobsResponseTypeDef(TypedDict):
    Jobs: List[BackendJobRespObjTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RemoveAllBackendsResponseTypeDef(TypedDict):
    AppId: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveBackendConfigResponseTypeDef(TypedDict):
    Error: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBackendAPIResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBackendAuthResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBackendJobResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    CreateTime: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    UpdateTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBackendStorageResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackendAuthForgotPasswordConfigTypeDef(TypedDict):
    DeliveryMethod: DeliveryMethodType
    EmailSettings: NotRequired[EmailSettingsTypeDef]
    SmsSettings: NotRequired[SmsSettingsTypeDef]

class CreateBackendAuthVerificationMessageConfigTypeDef(TypedDict):
    DeliveryMethod: DeliveryMethodType
    EmailSettings: NotRequired[EmailSettingsTypeDef]
    SmsSettings: NotRequired[SmsSettingsTypeDef]

class UpdateBackendAuthForgotPasswordConfigTypeDef(TypedDict):
    DeliveryMethod: NotRequired[DeliveryMethodType]
    EmailSettings: NotRequired[EmailSettingsTypeDef]
    SmsSettings: NotRequired[SmsSettingsTypeDef]

class UpdateBackendAuthVerificationMessageConfigTypeDef(TypedDict):
    DeliveryMethod: DeliveryMethodType
    EmailSettings: NotRequired[EmailSettingsTypeDef]
    SmsSettings: NotRequired[SmsSettingsTypeDef]

class CreateBackendAuthMFAConfigOutputTypeDef(TypedDict):
    MFAMode: MFAModeType
    Settings: NotRequired[SettingsOutputTypeDef]

class CreateBackendAuthMFAConfigTypeDef(TypedDict):
    MFAMode: MFAModeType
    Settings: NotRequired[SettingsTypeDef]

SettingsUnionTypeDef = Union[SettingsTypeDef, SettingsOutputTypeDef]

class ListBackendJobsRequestPaginateTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    JobId: NotRequired[str]
    Operation: NotRequired[str]
    Status: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListS3BucketsResponseTypeDef(TypedDict):
    Buckets: List[S3BucketInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateBackendConfigRequestTypeDef(TypedDict):
    AppId: str
    LoginAuthConfig: NotRequired[LoginAuthConfigReqObjTypeDef]

class UpdateBackendConfigResponseTypeDef(TypedDict):
    AppId: str
    BackendManagerAppId: str
    Error: str
    LoginAuthConfig: LoginAuthConfigReqObjTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BackendAPIResourceConfigOutputTypeDef(TypedDict):
    AdditionalAuthTypes: NotRequired[List[BackendAPIAuthTypeTypeDef]]
    ApiName: NotRequired[str]
    ConflictResolution: NotRequired[BackendAPIConflictResolutionTypeDef]
    DefaultAuthType: NotRequired[BackendAPIAuthTypeTypeDef]
    Service: NotRequired[str]
    TransformSchema: NotRequired[str]

class BackendAPIResourceConfigTypeDef(TypedDict):
    AdditionalAuthTypes: NotRequired[Sequence[BackendAPIAuthTypeTypeDef]]
    ApiName: NotRequired[str]
    ConflictResolution: NotRequired[BackendAPIConflictResolutionTypeDef]
    DefaultAuthType: NotRequired[BackendAPIAuthTypeTypeDef]
    Service: NotRequired[str]
    TransformSchema: NotRequired[str]

class CreateBackendAuthOAuthConfigOutputTypeDef(TypedDict):
    OAuthGrantType: OAuthGrantTypeType
    OAuthScopes: List[OAuthScopesElementType]
    RedirectSignInURIs: List[str]
    RedirectSignOutURIs: List[str]
    DomainPrefix: NotRequired[str]
    SocialProviderSettings: NotRequired[SocialProviderSettingsTypeDef]

class CreateBackendAuthOAuthConfigTypeDef(TypedDict):
    OAuthGrantType: OAuthGrantTypeType
    OAuthScopes: Sequence[OAuthScopesElementType]
    RedirectSignInURIs: Sequence[str]
    RedirectSignOutURIs: Sequence[str]
    DomainPrefix: NotRequired[str]
    SocialProviderSettings: NotRequired[SocialProviderSettingsTypeDef]

class UpdateBackendAuthOAuthConfigTypeDef(TypedDict):
    DomainPrefix: NotRequired[str]
    OAuthGrantType: NotRequired[OAuthGrantTypeType]
    OAuthScopes: NotRequired[Sequence[OAuthScopesElementType]]
    RedirectSignInURIs: NotRequired[Sequence[str]]
    RedirectSignOutURIs: NotRequired[Sequence[str]]
    SocialProviderSettings: NotRequired[SocialProviderSettingsTypeDef]

class GetBackendStorageResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: GetBackendStorageResourceConfigTypeDef
    ResourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

CreateBackendStorageResourceConfigTypeDef = TypedDict(
    "CreateBackendStorageResourceConfigTypeDef",
    {
        "Permissions": BackendStoragePermissionsUnionTypeDef,
        "ServiceName": Literal["S3"],
        "BucketName": NotRequired[str],
    },
)
UpdateBackendStorageResourceConfigTypeDef = TypedDict(
    "UpdateBackendStorageResourceConfigTypeDef",
    {
        "Permissions": BackendStoragePermissionsUnionTypeDef,
        "ServiceName": Literal["S3"],
    },
)

class UpdateBackendAuthMFAConfigTypeDef(TypedDict):
    MFAMode: NotRequired[MFAModeType]
    Settings: NotRequired[SettingsUnionTypeDef]

class GetBackendAPIResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    ResourceConfig: BackendAPIResourceConfigOutputTypeDef
    ResourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

BackendAPIResourceConfigUnionTypeDef = Union[
    BackendAPIResourceConfigTypeDef, BackendAPIResourceConfigOutputTypeDef
]

class CreateBackendAuthUserPoolConfigOutputTypeDef(TypedDict):
    RequiredSignUpAttributes: List[RequiredSignUpAttributesElementType]
    SignInMethod: SignInMethodType
    UserPoolName: str
    ForgotPassword: NotRequired[CreateBackendAuthForgotPasswordConfigTypeDef]
    Mfa: NotRequired[CreateBackendAuthMFAConfigOutputTypeDef]
    OAuth: NotRequired[CreateBackendAuthOAuthConfigOutputTypeDef]
    PasswordPolicy: NotRequired[CreateBackendAuthPasswordPolicyConfigOutputTypeDef]
    VerificationMessage: NotRequired[CreateBackendAuthVerificationMessageConfigTypeDef]

class CreateBackendAuthUserPoolConfigTypeDef(TypedDict):
    RequiredSignUpAttributes: Sequence[RequiredSignUpAttributesElementType]
    SignInMethod: SignInMethodType
    UserPoolName: str
    ForgotPassword: NotRequired[CreateBackendAuthForgotPasswordConfigTypeDef]
    Mfa: NotRequired[CreateBackendAuthMFAConfigTypeDef]
    OAuth: NotRequired[CreateBackendAuthOAuthConfigTypeDef]
    PasswordPolicy: NotRequired[CreateBackendAuthPasswordPolicyConfigTypeDef]
    VerificationMessage: NotRequired[CreateBackendAuthVerificationMessageConfigTypeDef]

class CreateBackendStorageRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: CreateBackendStorageResourceConfigTypeDef
    ResourceName: str

class UpdateBackendStorageRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: UpdateBackendStorageResourceConfigTypeDef
    ResourceName: str

class UpdateBackendAuthUserPoolConfigTypeDef(TypedDict):
    ForgotPassword: NotRequired[UpdateBackendAuthForgotPasswordConfigTypeDef]
    Mfa: NotRequired[UpdateBackendAuthMFAConfigTypeDef]
    OAuth: NotRequired[UpdateBackendAuthOAuthConfigTypeDef]
    PasswordPolicy: NotRequired[UpdateBackendAuthPasswordPolicyConfigTypeDef]
    VerificationMessage: NotRequired[UpdateBackendAuthVerificationMessageConfigTypeDef]

class CreateBackendAPIRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: BackendAPIResourceConfigUnionTypeDef
    ResourceName: str

class DeleteBackendAPIRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ResourceConfig: NotRequired[BackendAPIResourceConfigUnionTypeDef]

class GetBackendAPIRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ResourceConfig: NotRequired[BackendAPIResourceConfigUnionTypeDef]

class UpdateBackendAPIRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    ResourceName: str
    ResourceConfig: NotRequired[BackendAPIResourceConfigUnionTypeDef]

class CreateBackendAuthResourceConfigOutputTypeDef(TypedDict):
    AuthResources: AuthResourcesType
    Service: Literal["COGNITO"]
    UserPoolConfigs: CreateBackendAuthUserPoolConfigOutputTypeDef
    IdentityPoolConfigs: NotRequired[CreateBackendAuthIdentityPoolConfigTypeDef]

class CreateBackendAuthResourceConfigTypeDef(TypedDict):
    AuthResources: AuthResourcesType
    Service: Literal["COGNITO"]
    UserPoolConfigs: CreateBackendAuthUserPoolConfigTypeDef
    IdentityPoolConfigs: NotRequired[CreateBackendAuthIdentityPoolConfigTypeDef]

class UpdateBackendAuthResourceConfigTypeDef(TypedDict):
    AuthResources: AuthResourcesType
    Service: Literal["COGNITO"]
    UserPoolConfigs: UpdateBackendAuthUserPoolConfigTypeDef
    IdentityPoolConfigs: NotRequired[UpdateBackendAuthIdentityPoolConfigTypeDef]

class GetBackendAuthResponseTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    ResourceConfig: CreateBackendAuthResourceConfigOutputTypeDef
    ResourceName: str
    ResponseMetadata: ResponseMetadataTypeDef

CreateBackendAuthResourceConfigUnionTypeDef = Union[
    CreateBackendAuthResourceConfigTypeDef, CreateBackendAuthResourceConfigOutputTypeDef
]

class UpdateBackendAuthRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: UpdateBackendAuthResourceConfigTypeDef
    ResourceName: str

class CreateBackendAuthRequestTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str
    ResourceConfig: CreateBackendAuthResourceConfigUnionTypeDef
    ResourceName: str
