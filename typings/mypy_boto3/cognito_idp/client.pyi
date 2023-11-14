"""
Type annotations for cognito-idp service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cognito_idp import CognitoIdentityProviderClient

    client: CognitoIdentityProviderClient = boto3.client("cognito-idp")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    AliasAttributeTypeType,
    AuthFlowTypeType,
    ChallengeNameTypeType,
    DeletionProtectionTypeType,
    DeliveryMediumTypeType,
    DeviceRememberedStatusTypeType,
    ExplicitAuthFlowsTypeType,
    FeedbackValueTypeType,
    IdentityProviderTypeTypeType,
    MessageActionTypeType,
    OAuthFlowTypeType,
    PreventUserExistenceErrorTypesType,
    UsernameAttributeTypeType,
    UserPoolMfaTypeType,
    VerifiedAttributeTypeType,
)
from .paginator import (
    AdminListGroupsForUserPaginator,
    AdminListUserAuthEventsPaginator,
    ListGroupsPaginator,
    ListIdentityProvidersPaginator,
    ListResourceServersPaginator,
    ListUserPoolClientsPaginator,
    ListUserPoolsPaginator,
    ListUsersInGroupPaginator,
    ListUsersPaginator,
)
from .type_defs import (
    AccountRecoverySettingTypeTypeDef,
    AccountTakeoverRiskConfigurationTypeTypeDef,
    AdminCreateUserConfigTypeTypeDef,
    AdminCreateUserResponseTypeDef,
    AdminGetDeviceResponseTypeDef,
    AdminGetUserResponseTypeDef,
    AdminInitiateAuthResponseTypeDef,
    AdminListDevicesResponseTypeDef,
    AdminListGroupsForUserResponseTypeDef,
    AdminListUserAuthEventsResponseTypeDef,
    AdminRespondToAuthChallengeResponseTypeDef,
    AnalyticsConfigurationTypeTypeDef,
    AnalyticsMetadataTypeTypeDef,
    AssociateSoftwareTokenResponseTypeDef,
    AttributeTypeTypeDef,
    CompromisedCredentialsRiskConfigurationTypeTypeDef,
    ConfirmDeviceResponseTypeDef,
    ContextDataTypeTypeDef,
    CreateGroupResponseTypeDef,
    CreateIdentityProviderResponseTypeDef,
    CreateResourceServerResponseTypeDef,
    CreateUserImportJobResponseTypeDef,
    CreateUserPoolClientResponseTypeDef,
    CreateUserPoolDomainResponseTypeDef,
    CreateUserPoolResponseTypeDef,
    CustomDomainConfigTypeTypeDef,
    DescribeIdentityProviderResponseTypeDef,
    DescribeResourceServerResponseTypeDef,
    DescribeRiskConfigurationResponseTypeDef,
    DescribeUserImportJobResponseTypeDef,
    DescribeUserPoolClientResponseTypeDef,
    DescribeUserPoolDomainResponseTypeDef,
    DescribeUserPoolResponseTypeDef,
    DeviceConfigurationTypeTypeDef,
    DeviceSecretVerifierConfigTypeTypeDef,
    EmailConfigurationTypeTypeDef,
    ForgotPasswordResponseTypeDef,
    GetCSVHeaderResponseTypeDef,
    GetDeviceResponseTypeDef,
    GetGroupResponseTypeDef,
    GetIdentityProviderByIdentifierResponseTypeDef,
    GetLogDeliveryConfigurationResponseTypeDef,
    GetSigningCertificateResponseTypeDef,
    GetUICustomizationResponseTypeDef,
    GetUserAttributeVerificationCodeResponseTypeDef,
    GetUserPoolMfaConfigResponseTypeDef,
    GetUserResponseTypeDef,
    InitiateAuthResponseTypeDef,
    LambdaConfigTypeTypeDef,
    ListDevicesResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListResourceServersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUserImportJobsResponseTypeDef,
    ListUserPoolClientsResponseTypeDef,
    ListUserPoolsResponseTypeDef,
    ListUsersInGroupResponseTypeDef,
    ListUsersResponseTypeDef,
    LogConfigurationTypeTypeDef,
    MFAOptionTypeTypeDef,
    ProviderUserIdentifierTypeTypeDef,
    ResendConfirmationCodeResponseTypeDef,
    ResourceServerScopeTypeTypeDef,
    RespondToAuthChallengeResponseTypeDef,
    RiskExceptionConfigurationTypeTypeDef,
    SchemaAttributeTypeTypeDef,
    SetLogDeliveryConfigurationResponseTypeDef,
    SetRiskConfigurationResponseTypeDef,
    SetUICustomizationResponseTypeDef,
    SetUserPoolMfaConfigResponseTypeDef,
    SignUpResponseTypeDef,
    SmsConfigurationTypeTypeDef,
    SmsMfaConfigTypeTypeDef,
    SMSMfaSettingsTypeTypeDef,
    SoftwareTokenMfaConfigTypeTypeDef,
    SoftwareTokenMfaSettingsTypeTypeDef,
    StartUserImportJobResponseTypeDef,
    StopUserImportJobResponseTypeDef,
    TokenValidityUnitsTypeTypeDef,
    UpdateGroupResponseTypeDef,
    UpdateIdentityProviderResponseTypeDef,
    UpdateResourceServerResponseTypeDef,
    UpdateUserAttributesResponseTypeDef,
    UpdateUserPoolClientResponseTypeDef,
    UpdateUserPoolDomainResponseTypeDef,
    UserAttributeUpdateSettingsTypeTypeDef,
    UserContextDataTypeTypeDef,
    UsernameConfigurationTypeTypeDef,
    UserPoolAddOnsTypeTypeDef,
    UserPoolPolicyTypeTypeDef,
    VerificationMessageTemplateTypeTypeDef,
    VerifySoftwareTokenResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CognitoIdentityProviderClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AliasExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CodeDeliveryFailureException: Type[BotocoreClientError]
    CodeMismatchException: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    DuplicateProviderException: Type[BotocoreClientError]
    EnableSoftwareTokenMFAException: Type[BotocoreClientError]
    ExpiredCodeException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    GroupExistsException: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidEmailRoleAccessPolicyException: Type[BotocoreClientError]
    InvalidLambdaResponseException: Type[BotocoreClientError]
    InvalidOAuthFlowException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidPasswordException: Type[BotocoreClientError]
    InvalidSmsRoleAccessPolicyException: Type[BotocoreClientError]
    InvalidSmsRoleTrustRelationshipException: Type[BotocoreClientError]
    InvalidUserPoolConfigurationException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MFAMethodNotFoundException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]
    PasswordResetRequiredException: Type[BotocoreClientError]
    PreconditionNotMetException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ScopeDoesNotExistException: Type[BotocoreClientError]
    SoftwareTokenMFANotFoundException: Type[BotocoreClientError]
    TooManyFailedAttemptsException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    UnexpectedLambdaException: Type[BotocoreClientError]
    UnsupportedIdentityProviderException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]
    UnsupportedTokenTypeException: Type[BotocoreClientError]
    UnsupportedUserStateException: Type[BotocoreClientError]
    UserImportInProgressException: Type[BotocoreClientError]
    UserLambdaValidationException: Type[BotocoreClientError]
    UserNotConfirmedException: Type[BotocoreClientError]
    UserNotFoundException: Type[BotocoreClientError]
    UserPoolAddOnNotEnabledException: Type[BotocoreClientError]
    UserPoolTaggingException: Type[BotocoreClientError]
    UsernameExistsException: Type[BotocoreClientError]

class CognitoIdentityProviderClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CognitoIdentityProviderClient exceptions.
        """
    def add_custom_attributes(
        self, *, UserPoolId: str, CustomAttributes: List["SchemaAttributeTypeTypeDef"]
    ) -> Dict[str, Any]:
        """
        Adds additional user attributes to the user pool schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.add_custom_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#add_custom_attributes)
        """
    def admin_add_user_to_group(self, *, UserPoolId: str, Username: str, GroupName: str) -> None:
        """
        Adds the specified user to the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_add_user_to_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_add_user_to_group)
        """
    def admin_confirm_sign_up(
        self, *, UserPoolId: str, Username: str, ClientMetadata: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        Confirms user registration as an admin without using a confirmation code.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_confirm_sign_up)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_confirm_sign_up)
        """
    def admin_create_user(
        self,
        *,
        UserPoolId: str,
        Username: str,
        UserAttributes: List["AttributeTypeTypeDef"] = None,
        ValidationData: List["AttributeTypeTypeDef"] = None,
        TemporaryPassword: str = None,
        ForceAliasCreation: bool = None,
        MessageAction: MessageActionTypeType = None,
        DesiredDeliveryMediums: List[DeliveryMediumTypeType] = None,
        ClientMetadata: Dict[str, str] = None
    ) -> AdminCreateUserResponseTypeDef:
        """
        Creates a new user in the specified user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_create_user)
        """
    def admin_delete_user(self, *, UserPoolId: str, Username: str) -> None:
        """
        Deletes a user as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_delete_user)
        """
    def admin_delete_user_attributes(
        self, *, UserPoolId: str, Username: str, UserAttributeNames: List[str]
    ) -> Dict[str, Any]:
        """
        Deletes the user attributes in a user pool as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_delete_user_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_delete_user_attributes)
        """
    def admin_disable_provider_for_user(
        self, *, UserPoolId: str, User: "ProviderUserIdentifierTypeTypeDef"
    ) -> Dict[str, Any]:
        """
        Prevents the user from signing in with the specified external (SAML or social)
        identity provider (IdP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_disable_provider_for_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_disable_provider_for_user)
        """
    def admin_disable_user(self, *, UserPoolId: str, Username: str) -> Dict[str, Any]:
        """
        Deactivates a user and revokes all access tokens for the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_disable_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_disable_user)
        """
    def admin_enable_user(self, *, UserPoolId: str, Username: str) -> Dict[str, Any]:
        """
        Enables the specified user as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_enable_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_enable_user)
        """
    def admin_forget_device(self, *, UserPoolId: str, Username: str, DeviceKey: str) -> None:
        """
        Forgets the device, as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_forget_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_forget_device)
        """
    def admin_get_device(
        self, *, DeviceKey: str, UserPoolId: str, Username: str
    ) -> AdminGetDeviceResponseTypeDef:
        """
        Gets the device, as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_get_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_get_device)
        """
    def admin_get_user(self, *, UserPoolId: str, Username: str) -> AdminGetUserResponseTypeDef:
        """
        Gets the specified user by user name in a user pool as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_get_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_get_user)
        """
    def admin_initiate_auth(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
        AuthFlow: AuthFlowTypeType,
        AuthParameters: Dict[str, str] = None,
        ClientMetadata: Dict[str, str] = None,
        AnalyticsMetadata: "AnalyticsMetadataTypeTypeDef" = None,
        ContextData: "ContextDataTypeTypeDef" = None
    ) -> AdminInitiateAuthResponseTypeDef:
        """
        Initiates the authentication flow, as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_initiate_auth)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_initiate_auth)
        """
    def admin_link_provider_for_user(
        self,
        *,
        UserPoolId: str,
        DestinationUser: "ProviderUserIdentifierTypeTypeDef",
        SourceUser: "ProviderUserIdentifierTypeTypeDef"
    ) -> Dict[str, Any]:
        """
        Links an existing user account in a user pool ( `DestinationUser`) to an
        identity from an external IdP ( `SourceUser`) based on a specified attribute
        name and value from the external IdP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_link_provider_for_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_link_provider_for_user)
        """
    def admin_list_devices(
        self, *, UserPoolId: str, Username: str, Limit: int = None, PaginationToken: str = None
    ) -> AdminListDevicesResponseTypeDef:
        """
        Lists devices, as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_list_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_list_devices)
        """
    def admin_list_groups_for_user(
        self, *, Username: str, UserPoolId: str, Limit: int = None, NextToken: str = None
    ) -> AdminListGroupsForUserResponseTypeDef:
        """
        Lists the groups that the user belongs to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_list_groups_for_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_list_groups_for_user)
        """
    def admin_list_user_auth_events(
        self, *, UserPoolId: str, Username: str, MaxResults: int = None, NextToken: str = None
    ) -> AdminListUserAuthEventsResponseTypeDef:
        """
        A history of user activity and any risks detected as part of Amazon Cognito
        advanced security.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_list_user_auth_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_list_user_auth_events)
        """
    def admin_remove_user_from_group(
        self, *, UserPoolId: str, Username: str, GroupName: str
    ) -> None:
        """
        Removes the specified user from the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_remove_user_from_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_remove_user_from_group)
        """
    def admin_reset_user_password(
        self, *, UserPoolId: str, Username: str, ClientMetadata: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        Resets the specified user's password in a user pool as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_reset_user_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_reset_user_password)
        """
    def admin_respond_to_auth_challenge(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
        ChallengeName: ChallengeNameTypeType,
        ChallengeResponses: Dict[str, str] = None,
        Session: str = None,
        AnalyticsMetadata: "AnalyticsMetadataTypeTypeDef" = None,
        ContextData: "ContextDataTypeTypeDef" = None,
        ClientMetadata: Dict[str, str] = None
    ) -> AdminRespondToAuthChallengeResponseTypeDef:
        """
        Responds to an authentication challenge, as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_respond_to_auth_challenge)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_respond_to_auth_challenge)
        """
    def admin_set_user_mfa_preference(
        self,
        *,
        Username: str,
        UserPoolId: str,
        SMSMfaSettings: "SMSMfaSettingsTypeTypeDef" = None,
        SoftwareTokenMfaSettings: "SoftwareTokenMfaSettingsTypeTypeDef" = None
    ) -> Dict[str, Any]:
        """
        The user's multi-factor authentication (MFA) preference, including which MFA
        options are activated, and if any are preferred.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_set_user_mfa_preference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_set_user_mfa_preference)
        """
    def admin_set_user_password(
        self, *, UserPoolId: str, Username: str, Password: str, Permanent: bool = None
    ) -> Dict[str, Any]:
        """
        Sets the specified user's password in a user pool as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_set_user_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_set_user_password)
        """
    def admin_set_user_settings(
        self, *, UserPoolId: str, Username: str, MFAOptions: List["MFAOptionTypeTypeDef"]
    ) -> Dict[str, Any]:
        """
        *This action is no longer supported.* You can use it to configure only SMS MFA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_set_user_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_set_user_settings)
        """
    def admin_update_auth_event_feedback(
        self, *, UserPoolId: str, Username: str, EventId: str, FeedbackValue: FeedbackValueTypeType
    ) -> Dict[str, Any]:
        """
        Provides feedback for an authentication event indicating if it was from a valid
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_update_auth_event_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_update_auth_event_feedback)
        """
    def admin_update_device_status(
        self,
        *,
        UserPoolId: str,
        Username: str,
        DeviceKey: str,
        DeviceRememberedStatus: DeviceRememberedStatusTypeType = None
    ) -> Dict[str, Any]:
        """
        Updates the device status as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_update_device_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_update_device_status)
        """
    def admin_update_user_attributes(
        self,
        *,
        UserPoolId: str,
        Username: str,
        UserAttributes: List["AttributeTypeTypeDef"],
        ClientMetadata: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_update_user_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_update_user_attributes)
        """
    def admin_user_global_sign_out(self, *, UserPoolId: str, Username: str) -> Dict[str, Any]:
        """
        Signs out a user from all devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_user_global_sign_out)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin_user_global_sign_out)
        """
    def associate_software_token(
        self, *, AccessToken: str = None, Session: str = None
    ) -> AssociateSoftwareTokenResponseTypeDef:
        """
        Begins setup of time-based one-time password (TOTP) multi-factor authentication
        (MFA) for a user, with a unique private key that Amazon Cognito generates and
        returns in the API response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.associate_software_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#associate_software_token)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#can_paginate)
        """
    def change_password(
        self, *, PreviousPassword: str, ProposedPassword: str, AccessToken: str
    ) -> Dict[str, Any]:
        """
        Changes the password for a specified user in a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.change_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#change_password)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#close)
        """
    def confirm_device(
        self,
        *,
        AccessToken: str,
        DeviceKey: str,
        DeviceSecretVerifierConfig: "DeviceSecretVerifierConfigTypeTypeDef" = None,
        DeviceName: str = None
    ) -> ConfirmDeviceResponseTypeDef:
        """
        Confirms tracking of the device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.confirm_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#confirm_device)
        """
    def confirm_forgot_password(
        self,
        *,
        ClientId: str,
        Username: str,
        ConfirmationCode: str,
        Password: str,
        SecretHash: str = None,
        AnalyticsMetadata: "AnalyticsMetadataTypeTypeDef" = None,
        UserContextData: "UserContextDataTypeTypeDef" = None,
        ClientMetadata: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        Allows a user to enter a confirmation code to reset a forgotten password.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.confirm_forgot_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#confirm_forgot_password)
        """
    def confirm_sign_up(
        self,
        *,
        ClientId: str,
        Username: str,
        ConfirmationCode: str,
        SecretHash: str = None,
        ForceAliasCreation: bool = None,
        AnalyticsMetadata: "AnalyticsMetadataTypeTypeDef" = None,
        UserContextData: "UserContextDataTypeTypeDef" = None,
        ClientMetadata: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        Confirms registration of a new user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.confirm_sign_up)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#confirm_sign_up)
        """
    def create_group(
        self,
        *,
        GroupName: str,
        UserPoolId: str,
        Description: str = None,
        RoleArn: str = None,
        Precedence: int = None
    ) -> CreateGroupResponseTypeDef:
        """
        Creates a new group in the specified user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#create_group)
        """
    def create_identity_provider(
        self,
        *,
        UserPoolId: str,
        ProviderName: str,
        ProviderType: IdentityProviderTypeTypeType,
        ProviderDetails: Dict[str, str],
        AttributeMapping: Dict[str, str] = None,
        IdpIdentifiers: List[str] = None
    ) -> CreateIdentityProviderResponseTypeDef:
        """
        Creates an IdP for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#create_identity_provider)
        """
    def create_resource_server(
        self,
        *,
        UserPoolId: str,
        Identifier: str,
        Name: str,
        Scopes: List["ResourceServerScopeTypeTypeDef"] = None
    ) -> CreateResourceServerResponseTypeDef:
        """
        Creates a new OAuth2.0 resource server and defines custom scopes within it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_resource_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#create_resource_server)
        """
    def create_user_import_job(
        self, *, JobName: str, UserPoolId: str, CloudWatchLogsRoleArn: str
    ) -> CreateUserImportJobResponseTypeDef:
        """
        Creates a user import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#create_user_import_job)
        """
    def create_user_pool(
        self,
        *,
        PoolName: str,
        Policies: "UserPoolPolicyTypeTypeDef" = None,
        DeletionProtection: DeletionProtectionTypeType = None,
        LambdaConfig: "LambdaConfigTypeTypeDef" = None,
        AutoVerifiedAttributes: List[VerifiedAttributeTypeType] = None,
        AliasAttributes: List[AliasAttributeTypeType] = None,
        UsernameAttributes: List[UsernameAttributeTypeType] = None,
        SmsVerificationMessage: str = None,
        EmailVerificationMessage: str = None,
        EmailVerificationSubject: str = None,
        VerificationMessageTemplate: "VerificationMessageTemplateTypeTypeDef" = None,
        SmsAuthenticationMessage: str = None,
        MfaConfiguration: UserPoolMfaTypeType = None,
        UserAttributeUpdateSettings: "UserAttributeUpdateSettingsTypeTypeDef" = None,
        DeviceConfiguration: "DeviceConfigurationTypeTypeDef" = None,
        EmailConfiguration: "EmailConfigurationTypeTypeDef" = None,
        SmsConfiguration: "SmsConfigurationTypeTypeDef" = None,
        UserPoolTags: Dict[str, str] = None,
        AdminCreateUserConfig: "AdminCreateUserConfigTypeTypeDef" = None,
        Schema: List["SchemaAttributeTypeTypeDef"] = None,
        UserPoolAddOns: "UserPoolAddOnsTypeTypeDef" = None,
        UsernameConfiguration: "UsernameConfigurationTypeTypeDef" = None,
        AccountRecoverySetting: "AccountRecoverySettingTypeTypeDef" = None
    ) -> CreateUserPoolResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#create_user_pool)
        """
    def create_user_pool_client(
        self,
        *,
        UserPoolId: str,
        ClientName: str,
        GenerateSecret: bool = None,
        RefreshTokenValidity: int = None,
        AccessTokenValidity: int = None,
        IdTokenValidity: int = None,
        TokenValidityUnits: "TokenValidityUnitsTypeTypeDef" = None,
        ReadAttributes: List[str] = None,
        WriteAttributes: List[str] = None,
        ExplicitAuthFlows: List[ExplicitAuthFlowsTypeType] = None,
        SupportedIdentityProviders: List[str] = None,
        CallbackURLs: List[str] = None,
        LogoutURLs: List[str] = None,
        DefaultRedirectURI: str = None,
        AllowedOAuthFlows: List[OAuthFlowTypeType] = None,
        AllowedOAuthScopes: List[str] = None,
        AllowedOAuthFlowsUserPoolClient: bool = None,
        AnalyticsConfiguration: "AnalyticsConfigurationTypeTypeDef" = None,
        PreventUserExistenceErrors: PreventUserExistenceErrorTypesType = None,
        EnableTokenRevocation: bool = None,
        EnablePropagateAdditionalUserContextData: bool = None,
        AuthSessionValidity: int = None
    ) -> CreateUserPoolClientResponseTypeDef:
        """
        Creates the user pool client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool_client)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#create_user_pool_client)
        """
    def create_user_pool_domain(
        self,
        *,
        Domain: str,
        UserPoolId: str,
        CustomDomainConfig: "CustomDomainConfigTypeTypeDef" = None
    ) -> CreateUserPoolDomainResponseTypeDef:
        """
        Creates a new domain for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#create_user_pool_domain)
        """
    def delete_group(self, *, GroupName: str, UserPoolId: str) -> None:
        """
        Deletes a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete_group)
        """
    def delete_identity_provider(self, *, UserPoolId: str, ProviderName: str) -> None:
        """
        Deletes an IdP for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete_identity_provider)
        """
    def delete_resource_server(self, *, UserPoolId: str, Identifier: str) -> None:
        """
        Deletes a resource server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_resource_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete_resource_server)
        """
    def delete_user(self, *, AccessToken: str) -> None:
        """
        Allows a user to delete their own user profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete_user)
        """
    def delete_user_attributes(
        self, *, UserAttributeNames: List[str], AccessToken: str
    ) -> Dict[str, Any]:
        """
        Deletes the attributes for a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete_user_attributes)
        """
    def delete_user_pool(self, *, UserPoolId: str) -> None:
        """
        Deletes the specified Amazon Cognito user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete_user_pool)
        """
    def delete_user_pool_client(self, *, UserPoolId: str, ClientId: str) -> None:
        """
        Allows the developer to delete the user pool client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_pool_client)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete_user_pool_client)
        """
    def delete_user_pool_domain(self, *, Domain: str, UserPoolId: str) -> Dict[str, Any]:
        """
        Deletes a domain for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_pool_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete_user_pool_domain)
        """
    def describe_identity_provider(
        self, *, UserPoolId: str, ProviderName: str
    ) -> DescribeIdentityProviderResponseTypeDef:
        """
        Gets information about a specific IdP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#describe_identity_provider)
        """
    def describe_resource_server(
        self, *, UserPoolId: str, Identifier: str
    ) -> DescribeResourceServerResponseTypeDef:
        """
        Describes a resource server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_resource_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#describe_resource_server)
        """
    def describe_risk_configuration(
        self, *, UserPoolId: str, ClientId: str = None
    ) -> DescribeRiskConfigurationResponseTypeDef:
        """
        Describes the risk configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_risk_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#describe_risk_configuration)
        """
    def describe_user_import_job(
        self, *, UserPoolId: str, JobId: str
    ) -> DescribeUserImportJobResponseTypeDef:
        """
        Describes the user import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#describe_user_import_job)
        """
    def describe_user_pool(self, *, UserPoolId: str) -> DescribeUserPoolResponseTypeDef:
        """
        Returns the configuration information and metadata of the specified user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#describe_user_pool)
        """
    def describe_user_pool_client(
        self, *, UserPoolId: str, ClientId: str
    ) -> DescribeUserPoolClientResponseTypeDef:
        """
        Client method for returning the configuration information and metadata of the
        specified user pool app client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool_client)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#describe_user_pool_client)
        """
    def describe_user_pool_domain(self, *, Domain: str) -> DescribeUserPoolDomainResponseTypeDef:
        """
        Gets information about a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#describe_user_pool_domain)
        """
    def forget_device(self, *, DeviceKey: str, AccessToken: str = None) -> None:
        """
        Forgets the specified device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.forget_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#forget_device)
        """
    def forgot_password(
        self,
        *,
        ClientId: str,
        Username: str,
        SecretHash: str = None,
        UserContextData: "UserContextDataTypeTypeDef" = None,
        AnalyticsMetadata: "AnalyticsMetadataTypeTypeDef" = None,
        ClientMetadata: Dict[str, str] = None
    ) -> ForgotPasswordResponseTypeDef:
        """
        Calling this API causes a message to be sent to the end user with a confirmation
        code that is required to change the user's password.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.forgot_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#forgot_password)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#generate_presigned_url)
        """
    def get_csv_header(self, *, UserPoolId: str) -> GetCSVHeaderResponseTypeDef:
        """
        Gets the header information for the comma-separated value (CSV) file to be used
        as input for the user import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_csv_header)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get_csv_header)
        """
    def get_device(self, *, DeviceKey: str, AccessToken: str = None) -> GetDeviceResponseTypeDef:
        """
        Gets the device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get_device)
        """
    def get_group(self, *, GroupName: str, UserPoolId: str) -> GetGroupResponseTypeDef:
        """
        Gets a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get_group)
        """
    def get_identity_provider_by_identifier(
        self, *, UserPoolId: str, IdpIdentifier: str
    ) -> GetIdentityProviderByIdentifierResponseTypeDef:
        """
        Gets the specified IdP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_identity_provider_by_identifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get_identity_provider_by_identifier)
        """
    def get_log_delivery_configuration(
        self, *, UserPoolId: str
    ) -> GetLogDeliveryConfigurationResponseTypeDef:
        """
        Gets the detailed activity logging configuration for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_log_delivery_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get_log_delivery_configuration)
        """
    def get_signing_certificate(self, *, UserPoolId: str) -> GetSigningCertificateResponseTypeDef:
        """
        This method takes a user pool ID, and returns the signing certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_signing_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get_signing_certificate)
        """
    def get_ui_customization(
        self, *, UserPoolId: str, ClientId: str = None
    ) -> GetUICustomizationResponseTypeDef:
        """
        Gets the user interface (UI) Customization information for a particular app
        client's app UI, if any such information exists for the client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_ui_customization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get_ui_customization)
        """
    def get_user(self, *, AccessToken: str) -> GetUserResponseTypeDef:
        """
        Gets the user attributes and metadata for a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get_user)
        """
    def get_user_attribute_verification_code(
        self, *, AccessToken: str, AttributeName: str, ClientMetadata: Dict[str, str] = None
    ) -> GetUserAttributeVerificationCodeResponseTypeDef:
        """
        Generates a user attribute verification code for the specified attribute name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_user_attribute_verification_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get_user_attribute_verification_code)
        """
    def get_user_pool_mfa_config(self, *, UserPoolId: str) -> GetUserPoolMfaConfigResponseTypeDef:
        """
        Gets the user pool multi-factor authentication (MFA) configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_user_pool_mfa_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get_user_pool_mfa_config)
        """
    def global_sign_out(self, *, AccessToken: str) -> Dict[str, Any]:
        """
        Signs out a user from all devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.global_sign_out)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#global_sign_out)
        """
    def initiate_auth(
        self,
        *,
        AuthFlow: AuthFlowTypeType,
        ClientId: str,
        AuthParameters: Dict[str, str] = None,
        ClientMetadata: Dict[str, str] = None,
        AnalyticsMetadata: "AnalyticsMetadataTypeTypeDef" = None,
        UserContextData: "UserContextDataTypeTypeDef" = None
    ) -> InitiateAuthResponseTypeDef:
        """
        Initiates sign-in for a user in the Amazon Cognito user directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.initiate_auth)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#initiate_auth)
        """
    def list_devices(
        self, *, AccessToken: str, Limit: int = None, PaginationToken: str = None
    ) -> ListDevicesResponseTypeDef:
        """
        Lists the sign-in devices that Amazon Cognito has registered to the current
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list_devices)
        """
    def list_groups(
        self, *, UserPoolId: str, Limit: int = None, NextToken: str = None
    ) -> ListGroupsResponseTypeDef:
        """
        Lists the groups associated with a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list_groups)
        """
    def list_identity_providers(
        self, *, UserPoolId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListIdentityProvidersResponseTypeDef:
        """
        Lists information about all IdPs for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_identity_providers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list_identity_providers)
        """
    def list_resource_servers(
        self, *, UserPoolId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListResourceServersResponseTypeDef:
        """
        Lists the resource servers for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_resource_servers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list_resource_servers)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags that are assigned to an Amazon Cognito user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list_tags_for_resource)
        """
    def list_user_import_jobs(
        self, *, UserPoolId: str, MaxResults: int, PaginationToken: str = None
    ) -> ListUserImportJobsResponseTypeDef:
        """
        Lists user import jobs for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_user_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list_user_import_jobs)
        """
    def list_user_pool_clients(
        self, *, UserPoolId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListUserPoolClientsResponseTypeDef:
        """
        Lists the clients that have been created for the specified user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_user_pool_clients)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list_user_pool_clients)
        """
    def list_user_pools(
        self, *, MaxResults: int, NextToken: str = None
    ) -> ListUserPoolsResponseTypeDef:
        """
        Lists the user pools associated with an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_user_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list_user_pools)
        """
    def list_users(
        self,
        *,
        UserPoolId: str,
        AttributesToGet: List[str] = None,
        Limit: int = None,
        PaginationToken: str = None,
        Filter: str = None
    ) -> ListUsersResponseTypeDef:
        """
        Lists users and their basic details in a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list_users)
        """
    def list_users_in_group(
        self, *, UserPoolId: str, GroupName: str, Limit: int = None, NextToken: str = None
    ) -> ListUsersInGroupResponseTypeDef:
        """
        Lists the users in the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_users_in_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list_users_in_group)
        """
    def resend_confirmation_code(
        self,
        *,
        ClientId: str,
        Username: str,
        SecretHash: str = None,
        UserContextData: "UserContextDataTypeTypeDef" = None,
        AnalyticsMetadata: "AnalyticsMetadataTypeTypeDef" = None,
        ClientMetadata: Dict[str, str] = None
    ) -> ResendConfirmationCodeResponseTypeDef:
        """
        Resends the confirmation (for confirmation of registration) to a specific user
        in the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.resend_confirmation_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#resend_confirmation_code)
        """
    def respond_to_auth_challenge(
        self,
        *,
        ClientId: str,
        ChallengeName: ChallengeNameTypeType,
        Session: str = None,
        ChallengeResponses: Dict[str, str] = None,
        AnalyticsMetadata: "AnalyticsMetadataTypeTypeDef" = None,
        UserContextData: "UserContextDataTypeTypeDef" = None,
        ClientMetadata: Dict[str, str] = None
    ) -> RespondToAuthChallengeResponseTypeDef:
        """
        Responds to the authentication challenge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.respond_to_auth_challenge)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#respond_to_auth_challenge)
        """
    def revoke_token(
        self, *, Token: str, ClientId: str, ClientSecret: str = None
    ) -> Dict[str, Any]:
        """
        Revokes all of the access tokens generated by, and at the same time as, the
        specified refresh token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.revoke_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#revoke_token)
        """
    def set_log_delivery_configuration(
        self, *, UserPoolId: str, LogConfigurations: List["LogConfigurationTypeTypeDef"]
    ) -> SetLogDeliveryConfigurationResponseTypeDef:
        """
        Sets up or modifies the detailed activity logging configuration of a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_log_delivery_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#set_log_delivery_configuration)
        """
    def set_risk_configuration(
        self,
        *,
        UserPoolId: str,
        ClientId: str = None,
        CompromisedCredentialsRiskConfiguration: "CompromisedCredentialsRiskConfigurationTypeTypeDef" = None,
        AccountTakeoverRiskConfiguration: "AccountTakeoverRiskConfigurationTypeTypeDef" = None,
        RiskExceptionConfiguration: "RiskExceptionConfigurationTypeTypeDef" = None
    ) -> SetRiskConfigurationResponseTypeDef:
        """
        Configures actions on detected risks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_risk_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#set_risk_configuration)
        """
    def set_ui_customization(
        self,
        *,
        UserPoolId: str,
        ClientId: str = None,
        CSS: str = None,
        ImageFile: Union[bytes, IO[bytes], StreamingBody] = None
    ) -> SetUICustomizationResponseTypeDef:
        """
        Sets the user interface (UI) customization information for a user pool's built-
        in app UI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_ui_customization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#set_ui_customization)
        """
    def set_user_mfa_preference(
        self,
        *,
        AccessToken: str,
        SMSMfaSettings: "SMSMfaSettingsTypeTypeDef" = None,
        SoftwareTokenMfaSettings: "SoftwareTokenMfaSettingsTypeTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Set the user's multi-factor authentication (MFA) method preference, including
        which MFA factors are activated and if any are preferred.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_user_mfa_preference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#set_user_mfa_preference)
        """
    def set_user_pool_mfa_config(
        self,
        *,
        UserPoolId: str,
        SmsMfaConfiguration: "SmsMfaConfigTypeTypeDef" = None,
        SoftwareTokenMfaConfiguration: "SoftwareTokenMfaConfigTypeTypeDef" = None,
        MfaConfiguration: UserPoolMfaTypeType = None
    ) -> SetUserPoolMfaConfigResponseTypeDef:
        """
        Sets the user pool multi-factor authentication (MFA) configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_user_pool_mfa_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#set_user_pool_mfa_config)
        """
    def set_user_settings(
        self, *, AccessToken: str, MFAOptions: List["MFAOptionTypeTypeDef"]
    ) -> Dict[str, Any]:
        """
        *This action is no longer supported.* You can use it to configure only SMS MFA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_user_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#set_user_settings)
        """
    def sign_up(
        self,
        *,
        ClientId: str,
        Username: str,
        Password: str,
        SecretHash: str = None,
        UserAttributes: List["AttributeTypeTypeDef"] = None,
        ValidationData: List["AttributeTypeTypeDef"] = None,
        AnalyticsMetadata: "AnalyticsMetadataTypeTypeDef" = None,
        UserContextData: "UserContextDataTypeTypeDef" = None,
        ClientMetadata: Dict[str, str] = None
    ) -> SignUpResponseTypeDef:
        """
        Registers the user in the specified user pool and creates a user name, password,
        and user attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.sign_up)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#sign_up)
        """
    def start_user_import_job(
        self, *, UserPoolId: str, JobId: str
    ) -> StartUserImportJobResponseTypeDef:
        """
        Starts the user import.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.start_user_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#start_user_import_job)
        """
    def stop_user_import_job(
        self, *, UserPoolId: str, JobId: str
    ) -> StopUserImportJobResponseTypeDef:
        """
        Stops the user import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.stop_user_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#stop_user_import_job)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns a set of tags to an Amazon Cognito user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from an Amazon Cognito user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#untag_resource)
        """
    def update_auth_event_feedback(
        self,
        *,
        UserPoolId: str,
        Username: str,
        EventId: str,
        FeedbackToken: str,
        FeedbackValue: FeedbackValueTypeType
    ) -> Dict[str, Any]:
        """
        Provides the feedback for an authentication event, whether it was from a valid
        user or not.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_auth_event_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update_auth_event_feedback)
        """
    def update_device_status(
        self,
        *,
        AccessToken: str,
        DeviceKey: str,
        DeviceRememberedStatus: DeviceRememberedStatusTypeType = None
    ) -> Dict[str, Any]:
        """
        Updates the device status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_device_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update_device_status)
        """
    def update_group(
        self,
        *,
        GroupName: str,
        UserPoolId: str,
        Description: str = None,
        RoleArn: str = None,
        Precedence: int = None
    ) -> UpdateGroupResponseTypeDef:
        """
        Updates the specified group with the specified attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update_group)
        """
    def update_identity_provider(
        self,
        *,
        UserPoolId: str,
        ProviderName: str,
        ProviderDetails: Dict[str, str] = None,
        AttributeMapping: Dict[str, str] = None,
        IdpIdentifiers: List[str] = None
    ) -> UpdateIdentityProviderResponseTypeDef:
        """
        Updates IdP information for a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update_identity_provider)
        """
    def update_resource_server(
        self,
        *,
        UserPoolId: str,
        Identifier: str,
        Name: str,
        Scopes: List["ResourceServerScopeTypeTypeDef"] = None
    ) -> UpdateResourceServerResponseTypeDef:
        """
        Updates the name and scopes of resource server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_resource_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update_resource_server)
        """
    def update_user_attributes(
        self,
        *,
        UserAttributes: List["AttributeTypeTypeDef"],
        AccessToken: str,
        ClientMetadata: Dict[str, str] = None
    ) -> UpdateUserAttributesResponseTypeDef:
        """
        Allows a user to update a specific attribute (one at a time).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update_user_attributes)
        """
    def update_user_pool(
        self,
        *,
        UserPoolId: str,
        Policies: "UserPoolPolicyTypeTypeDef" = None,
        DeletionProtection: DeletionProtectionTypeType = None,
        LambdaConfig: "LambdaConfigTypeTypeDef" = None,
        AutoVerifiedAttributes: List[VerifiedAttributeTypeType] = None,
        SmsVerificationMessage: str = None,
        EmailVerificationMessage: str = None,
        EmailVerificationSubject: str = None,
        VerificationMessageTemplate: "VerificationMessageTemplateTypeTypeDef" = None,
        SmsAuthenticationMessage: str = None,
        UserAttributeUpdateSettings: "UserAttributeUpdateSettingsTypeTypeDef" = None,
        MfaConfiguration: UserPoolMfaTypeType = None,
        DeviceConfiguration: "DeviceConfigurationTypeTypeDef" = None,
        EmailConfiguration: "EmailConfigurationTypeTypeDef" = None,
        SmsConfiguration: "SmsConfigurationTypeTypeDef" = None,
        UserPoolTags: Dict[str, str] = None,
        AdminCreateUserConfig: "AdminCreateUserConfigTypeTypeDef" = None,
        UserPoolAddOns: "UserPoolAddOnsTypeTypeDef" = None,
        AccountRecoverySetting: "AccountRecoverySettingTypeTypeDef" = None
    ) -> Dict[str, Any]:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update_user_pool)
        """
    def update_user_pool_client(
        self,
        *,
        UserPoolId: str,
        ClientId: str,
        ClientName: str = None,
        RefreshTokenValidity: int = None,
        AccessTokenValidity: int = None,
        IdTokenValidity: int = None,
        TokenValidityUnits: "TokenValidityUnitsTypeTypeDef" = None,
        ReadAttributes: List[str] = None,
        WriteAttributes: List[str] = None,
        ExplicitAuthFlows: List[ExplicitAuthFlowsTypeType] = None,
        SupportedIdentityProviders: List[str] = None,
        CallbackURLs: List[str] = None,
        LogoutURLs: List[str] = None,
        DefaultRedirectURI: str = None,
        AllowedOAuthFlows: List[OAuthFlowTypeType] = None,
        AllowedOAuthScopes: List[str] = None,
        AllowedOAuthFlowsUserPoolClient: bool = None,
        AnalyticsConfiguration: "AnalyticsConfigurationTypeTypeDef" = None,
        PreventUserExistenceErrors: PreventUserExistenceErrorTypesType = None,
        EnableTokenRevocation: bool = None,
        EnablePropagateAdditionalUserContextData: bool = None,
        AuthSessionValidity: int = None
    ) -> UpdateUserPoolClientResponseTypeDef:
        """
        Updates the specified user pool app client with the specified attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_pool_client)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update_user_pool_client)
        """
    def update_user_pool_domain(
        self, *, Domain: str, UserPoolId: str, CustomDomainConfig: "CustomDomainConfigTypeTypeDef"
    ) -> UpdateUserPoolDomainResponseTypeDef:
        """
        Updates the Secure Sockets Layer (SSL) certificate for the custom domain for
        your user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_pool_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update_user_pool_domain)
        """
    def verify_software_token(
        self,
        *,
        UserCode: str,
        AccessToken: str = None,
        Session: str = None,
        FriendlyDeviceName: str = None
    ) -> VerifySoftwareTokenResponseTypeDef:
        """
        Use this API to register a user's entered time-based one-time password (TOTP)
        code and mark the user's software token MFA status as "verified" if successful.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.verify_software_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#verify_software_token)
        """
    def verify_user_attribute(
        self, *, AccessToken: str, AttributeName: str, Code: str
    ) -> Dict[str, Any]:
        """
        Verifies the specified user attributes in the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.verify_user_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#verify_user_attribute)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["admin_list_groups_for_user"]
    ) -> AdminListGroupsForUserPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListGroupsForUser)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#adminlistgroupsforuserpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["admin_list_user_auth_events"]
    ) -> AdminListUserAuthEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListUserAuthEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#adminlistuserautheventspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_identity_providers"]
    ) -> ListIdentityProvidersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListIdentityProviders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listidentityproviderspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_servers"]
    ) -> ListResourceServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListResourceServers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listresourceserverspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_pool_clients"]
    ) -> ListUserPoolClientsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPoolClients)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listuserpoolclientspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_user_pools"]) -> ListUserPoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listuserpoolspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listuserspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_users_in_group"]
    ) -> ListUsersInGroupPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsersInGroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listusersingrouppaginator)
        """
