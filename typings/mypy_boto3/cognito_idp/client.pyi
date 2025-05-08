"""
Type annotations for cognito-idp service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cognito_idp.client import CognitoIdentityProviderClient

    session = Session()
    client: CognitoIdentityProviderClient = session.client("cognito-idp")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
    AddCustomAttributesRequestTypeDef,
    AdminAddUserToGroupRequestTypeDef,
    AdminConfirmSignUpRequestTypeDef,
    AdminCreateUserRequestTypeDef,
    AdminCreateUserResponseTypeDef,
    AdminDeleteUserAttributesRequestTypeDef,
    AdminDeleteUserRequestTypeDef,
    AdminDisableProviderForUserRequestTypeDef,
    AdminDisableUserRequestTypeDef,
    AdminEnableUserRequestTypeDef,
    AdminForgetDeviceRequestTypeDef,
    AdminGetDeviceRequestTypeDef,
    AdminGetDeviceResponseTypeDef,
    AdminGetUserRequestTypeDef,
    AdminGetUserResponseTypeDef,
    AdminInitiateAuthRequestTypeDef,
    AdminInitiateAuthResponseTypeDef,
    AdminLinkProviderForUserRequestTypeDef,
    AdminListDevicesRequestTypeDef,
    AdminListDevicesResponseTypeDef,
    AdminListGroupsForUserRequestTypeDef,
    AdminListGroupsForUserResponseTypeDef,
    AdminListUserAuthEventsRequestTypeDef,
    AdminListUserAuthEventsResponseTypeDef,
    AdminRemoveUserFromGroupRequestTypeDef,
    AdminResetUserPasswordRequestTypeDef,
    AdminRespondToAuthChallengeRequestTypeDef,
    AdminRespondToAuthChallengeResponseTypeDef,
    AdminSetUserMFAPreferenceRequestTypeDef,
    AdminSetUserPasswordRequestTypeDef,
    AdminSetUserSettingsRequestTypeDef,
    AdminUpdateAuthEventFeedbackRequestTypeDef,
    AdminUpdateDeviceStatusRequestTypeDef,
    AdminUpdateUserAttributesRequestTypeDef,
    AdminUserGlobalSignOutRequestTypeDef,
    AssociateSoftwareTokenRequestTypeDef,
    AssociateSoftwareTokenResponseTypeDef,
    ChangePasswordRequestTypeDef,
    CompleteWebAuthnRegistrationRequestTypeDef,
    ConfirmDeviceRequestTypeDef,
    ConfirmDeviceResponseTypeDef,
    ConfirmForgotPasswordRequestTypeDef,
    ConfirmSignUpRequestTypeDef,
    ConfirmSignUpResponseTypeDef,
    CreateGroupRequestTypeDef,
    CreateGroupResponseTypeDef,
    CreateIdentityProviderRequestTypeDef,
    CreateIdentityProviderResponseTypeDef,
    CreateManagedLoginBrandingRequestTypeDef,
    CreateManagedLoginBrandingResponseTypeDef,
    CreateResourceServerRequestTypeDef,
    CreateResourceServerResponseTypeDef,
    CreateUserImportJobRequestTypeDef,
    CreateUserImportJobResponseTypeDef,
    CreateUserPoolClientRequestTypeDef,
    CreateUserPoolClientResponseTypeDef,
    CreateUserPoolDomainRequestTypeDef,
    CreateUserPoolDomainResponseTypeDef,
    CreateUserPoolRequestTypeDef,
    CreateUserPoolResponseTypeDef,
    DeleteGroupRequestTypeDef,
    DeleteIdentityProviderRequestTypeDef,
    DeleteManagedLoginBrandingRequestTypeDef,
    DeleteResourceServerRequestTypeDef,
    DeleteUserAttributesRequestTypeDef,
    DeleteUserPoolClientRequestTypeDef,
    DeleteUserPoolDomainRequestTypeDef,
    DeleteUserPoolRequestTypeDef,
    DeleteUserRequestTypeDef,
    DeleteWebAuthnCredentialRequestTypeDef,
    DescribeIdentityProviderRequestTypeDef,
    DescribeIdentityProviderResponseTypeDef,
    DescribeManagedLoginBrandingByClientRequestTypeDef,
    DescribeManagedLoginBrandingByClientResponseTypeDef,
    DescribeManagedLoginBrandingRequestTypeDef,
    DescribeManagedLoginBrandingResponseTypeDef,
    DescribeResourceServerRequestTypeDef,
    DescribeResourceServerResponseTypeDef,
    DescribeRiskConfigurationRequestTypeDef,
    DescribeRiskConfigurationResponseTypeDef,
    DescribeUserImportJobRequestTypeDef,
    DescribeUserImportJobResponseTypeDef,
    DescribeUserPoolClientRequestTypeDef,
    DescribeUserPoolClientResponseTypeDef,
    DescribeUserPoolDomainRequestTypeDef,
    DescribeUserPoolDomainResponseTypeDef,
    DescribeUserPoolRequestTypeDef,
    DescribeUserPoolResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    ForgetDeviceRequestTypeDef,
    ForgotPasswordRequestTypeDef,
    ForgotPasswordResponseTypeDef,
    GetCSVHeaderRequestTypeDef,
    GetCSVHeaderResponseTypeDef,
    GetDeviceRequestTypeDef,
    GetDeviceResponseTypeDef,
    GetGroupRequestTypeDef,
    GetGroupResponseTypeDef,
    GetIdentityProviderByIdentifierRequestTypeDef,
    GetIdentityProviderByIdentifierResponseTypeDef,
    GetLogDeliveryConfigurationRequestTypeDef,
    GetLogDeliveryConfigurationResponseTypeDef,
    GetSigningCertificateRequestTypeDef,
    GetSigningCertificateResponseTypeDef,
    GetTokensFromRefreshTokenRequestTypeDef,
    GetTokensFromRefreshTokenResponseTypeDef,
    GetUICustomizationRequestTypeDef,
    GetUICustomizationResponseTypeDef,
    GetUserAttributeVerificationCodeRequestTypeDef,
    GetUserAttributeVerificationCodeResponseTypeDef,
    GetUserAuthFactorsRequestTypeDef,
    GetUserAuthFactorsResponseTypeDef,
    GetUserPoolMfaConfigRequestTypeDef,
    GetUserPoolMfaConfigResponseTypeDef,
    GetUserRequestTypeDef,
    GetUserResponseTypeDef,
    GlobalSignOutRequestTypeDef,
    InitiateAuthRequestTypeDef,
    InitiateAuthResponseTypeDef,
    ListDevicesRequestTypeDef,
    ListDevicesResponseTypeDef,
    ListGroupsRequestTypeDef,
    ListGroupsResponseTypeDef,
    ListIdentityProvidersRequestTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListResourceServersRequestTypeDef,
    ListResourceServersResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUserImportJobsRequestTypeDef,
    ListUserImportJobsResponseTypeDef,
    ListUserPoolClientsRequestTypeDef,
    ListUserPoolClientsResponseTypeDef,
    ListUserPoolsRequestTypeDef,
    ListUserPoolsResponseTypeDef,
    ListUsersInGroupRequestTypeDef,
    ListUsersInGroupResponseTypeDef,
    ListUsersRequestTypeDef,
    ListUsersResponseTypeDef,
    ListWebAuthnCredentialsRequestTypeDef,
    ListWebAuthnCredentialsResponseTypeDef,
    ResendConfirmationCodeRequestTypeDef,
    ResendConfirmationCodeResponseTypeDef,
    RespondToAuthChallengeRequestTypeDef,
    RespondToAuthChallengeResponseTypeDef,
    RevokeTokenRequestTypeDef,
    SetLogDeliveryConfigurationRequestTypeDef,
    SetLogDeliveryConfigurationResponseTypeDef,
    SetRiskConfigurationRequestTypeDef,
    SetRiskConfigurationResponseTypeDef,
    SetUICustomizationRequestTypeDef,
    SetUICustomizationResponseTypeDef,
    SetUserMFAPreferenceRequestTypeDef,
    SetUserPoolMfaConfigRequestTypeDef,
    SetUserPoolMfaConfigResponseTypeDef,
    SetUserSettingsRequestTypeDef,
    SignUpRequestTypeDef,
    SignUpResponseTypeDef,
    StartUserImportJobRequestTypeDef,
    StartUserImportJobResponseTypeDef,
    StartWebAuthnRegistrationRequestTypeDef,
    StartWebAuthnRegistrationResponseTypeDef,
    StopUserImportJobRequestTypeDef,
    StopUserImportJobResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAuthEventFeedbackRequestTypeDef,
    UpdateDeviceStatusRequestTypeDef,
    UpdateGroupRequestTypeDef,
    UpdateGroupResponseTypeDef,
    UpdateIdentityProviderRequestTypeDef,
    UpdateIdentityProviderResponseTypeDef,
    UpdateManagedLoginBrandingRequestTypeDef,
    UpdateManagedLoginBrandingResponseTypeDef,
    UpdateResourceServerRequestTypeDef,
    UpdateResourceServerResponseTypeDef,
    UpdateUserAttributesRequestTypeDef,
    UpdateUserAttributesResponseTypeDef,
    UpdateUserPoolClientRequestTypeDef,
    UpdateUserPoolClientResponseTypeDef,
    UpdateUserPoolDomainRequestTypeDef,
    UpdateUserPoolDomainResponseTypeDef,
    UpdateUserPoolRequestTypeDef,
    VerifySoftwareTokenRequestTypeDef,
    VerifySoftwareTokenResponseTypeDef,
    VerifyUserAttributeRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("CognitoIdentityProviderClient",)

class Exceptions(BaseClientExceptions):
    AliasExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CodeDeliveryFailureException: Type[BotocoreClientError]
    CodeMismatchException: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    DeviceKeyExistsException: Type[BotocoreClientError]
    DuplicateProviderException: Type[BotocoreClientError]
    EnableSoftwareTokenMFAException: Type[BotocoreClientError]
    ExpiredCodeException: Type[BotocoreClientError]
    FeatureUnavailableInTierException: Type[BotocoreClientError]
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
    ManagedLoginBrandingExistsException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]
    PasswordHistoryPolicyViolationException: Type[BotocoreClientError]
    PasswordResetRequiredException: Type[BotocoreClientError]
    PreconditionNotMetException: Type[BotocoreClientError]
    RefreshTokenReuseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ScopeDoesNotExistException: Type[BotocoreClientError]
    SoftwareTokenMFANotFoundException: Type[BotocoreClientError]
    TierChangeNotAllowedException: Type[BotocoreClientError]
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
    WebAuthnChallengeNotFoundException: Type[BotocoreClientError]
    WebAuthnClientMismatchException: Type[BotocoreClientError]
    WebAuthnConfigurationMissingException: Type[BotocoreClientError]
    WebAuthnCredentialNotSupportedException: Type[BotocoreClientError]
    WebAuthnNotEnabledException: Type[BotocoreClientError]
    WebAuthnOriginNotAllowedException: Type[BotocoreClientError]
    WebAuthnRelyingPartyMismatchException: Type[BotocoreClientError]

class CognitoIdentityProviderClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CognitoIdentityProviderClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html#CognitoIdentityProvider.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#generate_presigned_url)
        """

    def add_custom_attributes(
        self, **kwargs: Unpack[AddCustomAttributesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds additional user attributes to the user pool schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/add_custom_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#add_custom_attributes)
        """

    def admin_add_user_to_group(
        self, **kwargs: Unpack[AdminAddUserToGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds a user to a group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_add_user_to_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_add_user_to_group)
        """

    def admin_confirm_sign_up(
        self, **kwargs: Unpack[AdminConfirmSignUpRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Confirms user sign-up as an administrator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_confirm_sign_up.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_confirm_sign_up)
        """

    def admin_create_user(
        self, **kwargs: Unpack[AdminCreateUserRequestTypeDef]
    ) -> AdminCreateUserResponseTypeDef:
        """
        Creates a new user in the specified user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_create_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_create_user)
        """

    def admin_delete_user(
        self, **kwargs: Unpack[AdminDeleteUserRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a user profile in your user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_delete_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_delete_user)
        """

    def admin_delete_user_attributes(
        self, **kwargs: Unpack[AdminDeleteUserAttributesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes attribute values from a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_delete_user_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_delete_user_attributes)
        """

    def admin_disable_provider_for_user(
        self, **kwargs: Unpack[AdminDisableProviderForUserRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Prevents the user from signing in with the specified external (SAML or social)
        identity provider (IdP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_disable_provider_for_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_disable_provider_for_user)
        """

    def admin_disable_user(
        self, **kwargs: Unpack[AdminDisableUserRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deactivates a user profile and revokes all access tokens for the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_disable_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_disable_user)
        """

    def admin_enable_user(self, **kwargs: Unpack[AdminEnableUserRequestTypeDef]) -> Dict[str, Any]:
        """
        Activates sign-in for a user profile that previously had sign-in access
        disabled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_enable_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_enable_user)
        """

    def admin_forget_device(
        self, **kwargs: Unpack[AdminForgetDeviceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Forgets, or deletes, a remembered device from a user's profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_forget_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_forget_device)
        """

    def admin_get_device(
        self, **kwargs: Unpack[AdminGetDeviceRequestTypeDef]
    ) -> AdminGetDeviceResponseTypeDef:
        """
        Given the device key, returns details for a user's device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_get_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_get_device)
        """

    def admin_get_user(
        self, **kwargs: Unpack[AdminGetUserRequestTypeDef]
    ) -> AdminGetUserResponseTypeDef:
        """
        Given a username, returns details about a user profile in a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_get_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_get_user)
        """

    def admin_initiate_auth(
        self, **kwargs: Unpack[AdminInitiateAuthRequestTypeDef]
    ) -> AdminInitiateAuthResponseTypeDef:
        """
        Starts sign-in for applications with a server-side component, for example a
        traditional web application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_initiate_auth.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_initiate_auth)
        """

    def admin_link_provider_for_user(
        self, **kwargs: Unpack[AdminLinkProviderForUserRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Links an existing user account in a user pool, or <code>DestinationUser</code>,
        to an identity from an external IdP, or <code>SourceUser</code>, based on a
        specified attribute name and value from the external IdP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_link_provider_for_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_link_provider_for_user)
        """

    def admin_list_devices(
        self, **kwargs: Unpack[AdminListDevicesRequestTypeDef]
    ) -> AdminListDevicesResponseTypeDef:
        """
        Lists a user's registered devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_list_devices.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_list_devices)
        """

    def admin_list_groups_for_user(
        self, **kwargs: Unpack[AdminListGroupsForUserRequestTypeDef]
    ) -> AdminListGroupsForUserResponseTypeDef:
        """
        Lists the groups that a user belongs to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_list_groups_for_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_list_groups_for_user)
        """

    def admin_list_user_auth_events(
        self, **kwargs: Unpack[AdminListUserAuthEventsRequestTypeDef]
    ) -> AdminListUserAuthEventsResponseTypeDef:
        """
        Requests a history of user activity and any risks detected as part of Amazon
        Cognito threat protection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_list_user_auth_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_list_user_auth_events)
        """

    def admin_remove_user_from_group(
        self, **kwargs: Unpack[AdminRemoveUserFromGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Given a username and a group name, removes them from the group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_remove_user_from_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_remove_user_from_group)
        """

    def admin_reset_user_password(
        self, **kwargs: Unpack[AdminResetUserPasswordRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Resets the specified user's password in a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_reset_user_password.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_reset_user_password)
        """

    def admin_respond_to_auth_challenge(
        self, **kwargs: Unpack[AdminRespondToAuthChallengeRequestTypeDef]
    ) -> AdminRespondToAuthChallengeResponseTypeDef:
        """
        Some API operations in a user pool generate a challenge, like a prompt for an
        MFA code, for device authentication that bypasses MFA, or for a custom
        authentication challenge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_respond_to_auth_challenge.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_respond_to_auth_challenge)
        """

    def admin_set_user_mfa_preference(
        self, **kwargs: Unpack[AdminSetUserMFAPreferenceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sets the user's multi-factor authentication (MFA) preference, including which
        MFA options are activated, and if any are preferred.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_set_user_mfa_preference.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_set_user_mfa_preference)
        """

    def admin_set_user_password(
        self, **kwargs: Unpack[AdminSetUserPasswordRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sets the specified user's password in a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_set_user_password.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_set_user_password)
        """

    def admin_set_user_settings(
        self, **kwargs: Unpack[AdminSetUserSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        <i>This action is no longer supported.</i> You can use it to configure only SMS
        MFA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_set_user_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_set_user_settings)
        """

    def admin_update_auth_event_feedback(
        self, **kwargs: Unpack[AdminUpdateAuthEventFeedbackRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Provides the feedback for an authentication event generated by threat
        protection features.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_update_auth_event_feedback.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_update_auth_event_feedback)
        """

    def admin_update_device_status(
        self, **kwargs: Unpack[AdminUpdateDeviceStatusRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the status of a user's device so that it is marked as remembered or not
        remembered for the purpose of device authentication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_update_device_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_update_device_status)
        """

    def admin_update_user_attributes(
        self, **kwargs: Unpack[AdminUpdateUserAttributesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the specified user's attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_update_user_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_update_user_attributes)
        """

    def admin_user_global_sign_out(
        self, **kwargs: Unpack[AdminUserGlobalSignOutRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Invalidates the identity, access, and refresh tokens that Amazon Cognito issued
        to a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/admin_user_global_sign_out.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#admin_user_global_sign_out)
        """

    def associate_software_token(
        self, **kwargs: Unpack[AssociateSoftwareTokenRequestTypeDef]
    ) -> AssociateSoftwareTokenResponseTypeDef:
        """
        Begins setup of time-based one-time password (TOTP) multi-factor authentication
        (MFA) for a user, with a unique private key that Amazon Cognito generates and
        returns in the API response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/associate_software_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#associate_software_token)
        """

    def change_password(self, **kwargs: Unpack[ChangePasswordRequestTypeDef]) -> Dict[str, Any]:
        """
        Changes the password for the currently signed-in user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/change_password.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#change_password)
        """

    def complete_web_authn_registration(
        self, **kwargs: Unpack[CompleteWebAuthnRegistrationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Completes registration of a passkey authenticator for the currently signed-in
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/complete_web_authn_registration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#complete_web_authn_registration)
        """

    def confirm_device(
        self, **kwargs: Unpack[ConfirmDeviceRequestTypeDef]
    ) -> ConfirmDeviceResponseTypeDef:
        """
        Confirms a device that a user wants to remember.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/confirm_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#confirm_device)
        """

    def confirm_forgot_password(
        self, **kwargs: Unpack[ConfirmForgotPasswordRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This public API operation accepts a confirmation code that Amazon Cognito sent
        to a user and accepts a new password for that user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/confirm_forgot_password.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#confirm_forgot_password)
        """

    def confirm_sign_up(
        self, **kwargs: Unpack[ConfirmSignUpRequestTypeDef]
    ) -> ConfirmSignUpResponseTypeDef:
        """
        Confirms the account of a new user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/confirm_sign_up.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#confirm_sign_up)
        """

    def create_group(
        self, **kwargs: Unpack[CreateGroupRequestTypeDef]
    ) -> CreateGroupResponseTypeDef:
        """
        Creates a new group in the specified user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#create_group)
        """

    def create_identity_provider(
        self, **kwargs: Unpack[CreateIdentityProviderRequestTypeDef]
    ) -> CreateIdentityProviderResponseTypeDef:
        """
        Adds a configuration and trust relationship between a third-party identity
        provider (IdP) and a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_identity_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#create_identity_provider)
        """

    def create_managed_login_branding(
        self, **kwargs: Unpack[CreateManagedLoginBrandingRequestTypeDef]
    ) -> CreateManagedLoginBrandingResponseTypeDef:
        """
        Creates a new set of branding settings for a user pool style and associates it
        with an app client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_managed_login_branding.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#create_managed_login_branding)
        """

    def create_resource_server(
        self, **kwargs: Unpack[CreateResourceServerRequestTypeDef]
    ) -> CreateResourceServerResponseTypeDef:
        """
        Creates a new OAuth2.0 resource server and defines custom scopes within it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_resource_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#create_resource_server)
        """

    def create_user_import_job(
        self, **kwargs: Unpack[CreateUserImportJobRequestTypeDef]
    ) -> CreateUserImportJobResponseTypeDef:
        """
        Creates a user import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_user_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#create_user_import_job)
        """

    def create_user_pool(
        self, **kwargs: Unpack[CreateUserPoolRequestTypeDef]
    ) -> CreateUserPoolResponseTypeDef:
        """
        Creates a new Amazon Cognito user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_user_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#create_user_pool)
        """

    def create_user_pool_client(
        self, **kwargs: Unpack[CreateUserPoolClientRequestTypeDef]
    ) -> CreateUserPoolClientResponseTypeDef:
        """
        Creates an app client in a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_user_pool_client.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#create_user_pool_client)
        """

    def create_user_pool_domain(
        self, **kwargs: Unpack[CreateUserPoolDomainRequestTypeDef]
    ) -> CreateUserPoolDomainResponseTypeDef:
        """
        A user pool domain hosts managed login, an authorization server and web server
        for authentication in your application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/create_user_pool_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#create_user_pool_domain)
        """

    def delete_group(
        self, **kwargs: Unpack[DeleteGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a group from the specified user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_group)
        """

    def delete_identity_provider(
        self, **kwargs: Unpack[DeleteIdentityProviderRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a user pool identity provider (IdP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_identity_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_identity_provider)
        """

    def delete_managed_login_branding(
        self, **kwargs: Unpack[DeleteManagedLoginBrandingRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a managed login branding style.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_managed_login_branding.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_managed_login_branding)
        """

    def delete_resource_server(
        self, **kwargs: Unpack[DeleteResourceServerRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a resource server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_resource_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_resource_server)
        """

    def delete_user(
        self, **kwargs: Unpack[DeleteUserRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the profile of the currently signed-in user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_user)
        """

    def delete_user_attributes(
        self, **kwargs: Unpack[DeleteUserAttributesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes attributes from the currently signed-in user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_user_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_user_attributes)
        """

    def delete_user_pool(
        self, **kwargs: Unpack[DeleteUserPoolRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_user_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_user_pool)
        """

    def delete_user_pool_client(
        self, **kwargs: Unpack[DeleteUserPoolClientRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a user pool app client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_user_pool_client.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_user_pool_client)
        """

    def delete_user_pool_domain(
        self, **kwargs: Unpack[DeleteUserPoolDomainRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Given a user pool ID and domain identifier, deletes a user pool domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_user_pool_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_user_pool_domain)
        """

    def delete_web_authn_credential(
        self, **kwargs: Unpack[DeleteWebAuthnCredentialRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a registered passkey, or WebAuthn, authenticator for the currently
        signed-in user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/delete_web_authn_credential.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#delete_web_authn_credential)
        """

    def describe_identity_provider(
        self, **kwargs: Unpack[DescribeIdentityProviderRequestTypeDef]
    ) -> DescribeIdentityProviderResponseTypeDef:
        """
        Given a user pool ID and identity provider (IdP) name, returns details about
        the IdP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_identity_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_identity_provider)
        """

    def describe_managed_login_branding(
        self, **kwargs: Unpack[DescribeManagedLoginBrandingRequestTypeDef]
    ) -> DescribeManagedLoginBrandingResponseTypeDef:
        """
        Given the ID of a managed login branding style, returns detailed information
        about the style.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_managed_login_branding.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_managed_login_branding)
        """

    def describe_managed_login_branding_by_client(
        self, **kwargs: Unpack[DescribeManagedLoginBrandingByClientRequestTypeDef]
    ) -> DescribeManagedLoginBrandingByClientResponseTypeDef:
        """
        Given the ID of a user pool app client, returns detailed information about the
        style assigned to the app client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_managed_login_branding_by_client.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_managed_login_branding_by_client)
        """

    def describe_resource_server(
        self, **kwargs: Unpack[DescribeResourceServerRequestTypeDef]
    ) -> DescribeResourceServerResponseTypeDef:
        """
        Describes a resource server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_resource_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_resource_server)
        """

    def describe_risk_configuration(
        self, **kwargs: Unpack[DescribeRiskConfigurationRequestTypeDef]
    ) -> DescribeRiskConfigurationResponseTypeDef:
        """
        Given an app client or user pool ID where threat protection is configured,
        describes the risk configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_risk_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_risk_configuration)
        """

    def describe_user_import_job(
        self, **kwargs: Unpack[DescribeUserImportJobRequestTypeDef]
    ) -> DescribeUserImportJobResponseTypeDef:
        """
        Describes a user import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_user_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_user_import_job)
        """

    def describe_user_pool(
        self, **kwargs: Unpack[DescribeUserPoolRequestTypeDef]
    ) -> DescribeUserPoolResponseTypeDef:
        """
        Given a user pool ID, returns configuration information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_user_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_user_pool)
        """

    def describe_user_pool_client(
        self, **kwargs: Unpack[DescribeUserPoolClientRequestTypeDef]
    ) -> DescribeUserPoolClientResponseTypeDef:
        """
        Given an app client ID, returns configuration information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_user_pool_client.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_user_pool_client)
        """

    def describe_user_pool_domain(
        self, **kwargs: Unpack[DescribeUserPoolDomainRequestTypeDef]
    ) -> DescribeUserPoolDomainResponseTypeDef:
        """
        Given a user pool domain name, returns information about the domain
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/describe_user_pool_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#describe_user_pool_domain)
        """

    def forget_device(
        self, **kwargs: Unpack[ForgetDeviceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Given a device key, deletes a remembered device as the currently signed-in user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/forget_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#forget_device)
        """

    def forgot_password(
        self, **kwargs: Unpack[ForgotPasswordRequestTypeDef]
    ) -> ForgotPasswordResponseTypeDef:
        """
        Sends a password-reset confirmation code for the currently signed-in user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/forgot_password.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#forgot_password)
        """

    def get_csv_header(
        self, **kwargs: Unpack[GetCSVHeaderRequestTypeDef]
    ) -> GetCSVHeaderResponseTypeDef:
        """
        Given a user pool ID, generates a comma-separated value (CSV) list populated
        with available user attributes in the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_csv_header.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_csv_header)
        """

    def get_device(self, **kwargs: Unpack[GetDeviceRequestTypeDef]) -> GetDeviceResponseTypeDef:
        """
        Given a device key, returns information about a remembered device for the
        current user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_device)
        """

    def get_group(self, **kwargs: Unpack[GetGroupRequestTypeDef]) -> GetGroupResponseTypeDef:
        """
        Given a user pool ID and a group name, returns information about the user group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_group)
        """

    def get_identity_provider_by_identifier(
        self, **kwargs: Unpack[GetIdentityProviderByIdentifierRequestTypeDef]
    ) -> GetIdentityProviderByIdentifierResponseTypeDef:
        """
        Given the identifier of an identity provider (IdP), for example
        <code>examplecorp</code>, returns information about the user pool configuration
        for that IdP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_identity_provider_by_identifier.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_identity_provider_by_identifier)
        """

    def get_log_delivery_configuration(
        self, **kwargs: Unpack[GetLogDeliveryConfigurationRequestTypeDef]
    ) -> GetLogDeliveryConfigurationResponseTypeDef:
        """
        Given a user pool ID, returns the logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_log_delivery_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_log_delivery_configuration)
        """

    def get_signing_certificate(
        self, **kwargs: Unpack[GetSigningCertificateRequestTypeDef]
    ) -> GetSigningCertificateResponseTypeDef:
        """
        Given a user pool ID, returns the signing certificate for SAML 2.0 federation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_signing_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_signing_certificate)
        """

    def get_tokens_from_refresh_token(
        self, **kwargs: Unpack[GetTokensFromRefreshTokenRequestTypeDef]
    ) -> GetTokensFromRefreshTokenResponseTypeDef:
        """
        Given a refresh token, issues new ID, access, and optionally refresh tokens for
        the user who owns the submitted token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_tokens_from_refresh_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_tokens_from_refresh_token)
        """

    def get_ui_customization(
        self, **kwargs: Unpack[GetUICustomizationRequestTypeDef]
    ) -> GetUICustomizationResponseTypeDef:
        """
        Given a user pool ID or app client, returns information about classic hosted UI
        branding that you applied, if any.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_ui_customization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_ui_customization)
        """

    def get_user(self, **kwargs: Unpack[GetUserRequestTypeDef]) -> GetUserResponseTypeDef:
        """
        Gets user attributes and and MFA settings for the currently signed-in user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_user)
        """

    def get_user_attribute_verification_code(
        self, **kwargs: Unpack[GetUserAttributeVerificationCodeRequestTypeDef]
    ) -> GetUserAttributeVerificationCodeResponseTypeDef:
        """
        Given an attribute name, sends a user attribute verification code for the
        specified attribute name to the currently signed-in user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_user_attribute_verification_code.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_user_attribute_verification_code)
        """

    def get_user_auth_factors(
        self, **kwargs: Unpack[GetUserAuthFactorsRequestTypeDef]
    ) -> GetUserAuthFactorsResponseTypeDef:
        """
        Lists the authentication options for the currently signed-in user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_user_auth_factors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_user_auth_factors)
        """

    def get_user_pool_mfa_config(
        self, **kwargs: Unpack[GetUserPoolMfaConfigRequestTypeDef]
    ) -> GetUserPoolMfaConfigResponseTypeDef:
        """
        Given a user pool ID, returns configuration for sign-in with WebAuthn
        authenticators and for multi-factor authentication (MFA).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_user_pool_mfa_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_user_pool_mfa_config)
        """

    def global_sign_out(self, **kwargs: Unpack[GlobalSignOutRequestTypeDef]) -> Dict[str, Any]:
        """
        Invalidates the identity, access, and refresh tokens that Amazon Cognito issued
        to a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/global_sign_out.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#global_sign_out)
        """

    def initiate_auth(
        self, **kwargs: Unpack[InitiateAuthRequestTypeDef]
    ) -> InitiateAuthResponseTypeDef:
        """
        Declares an authentication flow and initiates sign-in for a user in the Amazon
        Cognito user directory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/initiate_auth.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#initiate_auth)
        """

    def list_devices(
        self, **kwargs: Unpack[ListDevicesRequestTypeDef]
    ) -> ListDevicesResponseTypeDef:
        """
        Lists the devices that Amazon Cognito has registered to the currently signed-in
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_devices.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_devices)
        """

    def list_groups(self, **kwargs: Unpack[ListGroupsRequestTypeDef]) -> ListGroupsResponseTypeDef:
        """
        Given a user pool ID, returns user pool groups and their details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_groups)
        """

    def list_identity_providers(
        self, **kwargs: Unpack[ListIdentityProvidersRequestTypeDef]
    ) -> ListIdentityProvidersResponseTypeDef:
        """
        Given a user pool ID, returns information about configured identity providers
        (IdPs).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_identity_providers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_identity_providers)
        """

    def list_resource_servers(
        self, **kwargs: Unpack[ListResourceServersRequestTypeDef]
    ) -> ListResourceServersResponseTypeDef:
        """
        Given a user pool ID, returns all resource servers and their details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_resource_servers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_resource_servers)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags that are assigned to an Amazon Cognito user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_tags_for_resource)
        """

    def list_user_import_jobs(
        self, **kwargs: Unpack[ListUserImportJobsRequestTypeDef]
    ) -> ListUserImportJobsResponseTypeDef:
        """
        Given a user pool ID, returns user import jobs and their details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_user_import_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_user_import_jobs)
        """

    def list_user_pool_clients(
        self, **kwargs: Unpack[ListUserPoolClientsRequestTypeDef]
    ) -> ListUserPoolClientsResponseTypeDef:
        """
        Given a user pool ID, lists app clients.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_user_pool_clients.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_user_pool_clients)
        """

    def list_user_pools(
        self, **kwargs: Unpack[ListUserPoolsRequestTypeDef]
    ) -> ListUserPoolsResponseTypeDef:
        """
        Lists user pools and their details in the current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_user_pools.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_user_pools)
        """

    def list_users(self, **kwargs: Unpack[ListUsersRequestTypeDef]) -> ListUsersResponseTypeDef:
        """
        Given a user pool ID, returns a list of users and their basic details in a user
        pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_users.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_users)
        """

    def list_users_in_group(
        self, **kwargs: Unpack[ListUsersInGroupRequestTypeDef]
    ) -> ListUsersInGroupResponseTypeDef:
        """
        Given a user pool ID and a group name, returns a list of users in the group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_users_in_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_users_in_group)
        """

    def list_web_authn_credentials(
        self, **kwargs: Unpack[ListWebAuthnCredentialsRequestTypeDef]
    ) -> ListWebAuthnCredentialsResponseTypeDef:
        """
        Generates a list of the currently signed-in user's registered passkey, or
        WebAuthn, credentials.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/list_web_authn_credentials.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#list_web_authn_credentials)
        """

    def resend_confirmation_code(
        self, **kwargs: Unpack[ResendConfirmationCodeRequestTypeDef]
    ) -> ResendConfirmationCodeResponseTypeDef:
        """
        Resends the code that confirms a new account for a user who has signed up in
        your user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/resend_confirmation_code.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#resend_confirmation_code)
        """

    def respond_to_auth_challenge(
        self, **kwargs: Unpack[RespondToAuthChallengeRequestTypeDef]
    ) -> RespondToAuthChallengeResponseTypeDef:
        """
        Some API operations in a user pool generate a challenge, like a prompt for an
        MFA code, for device authentication that bypasses MFA, or for a custom
        authentication challenge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/respond_to_auth_challenge.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#respond_to_auth_challenge)
        """

    def revoke_token(self, **kwargs: Unpack[RevokeTokenRequestTypeDef]) -> Dict[str, Any]:
        """
        Revokes all of the access tokens generated by, and at the same time as, the
        specified refresh token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/revoke_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#revoke_token)
        """

    def set_log_delivery_configuration(
        self, **kwargs: Unpack[SetLogDeliveryConfigurationRequestTypeDef]
    ) -> SetLogDeliveryConfigurationResponseTypeDef:
        """
        Sets up or modifies the logging configuration of a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/set_log_delivery_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#set_log_delivery_configuration)
        """

    def set_risk_configuration(
        self, **kwargs: Unpack[SetRiskConfigurationRequestTypeDef]
    ) -> SetRiskConfigurationResponseTypeDef:
        """
        Configures threat protection for a user pool or app client.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/set_risk_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#set_risk_configuration)
        """

    def set_ui_customization(
        self, **kwargs: Unpack[SetUICustomizationRequestTypeDef]
    ) -> SetUICustomizationResponseTypeDef:
        """
        Configures UI branding settings for domains with the hosted UI (classic)
        branding version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/set_ui_customization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#set_ui_customization)
        """

    def set_user_mfa_preference(
        self, **kwargs: Unpack[SetUserMFAPreferenceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Set the user's multi-factor authentication (MFA) method preference, including
        which MFA factors are activated and if any are preferred.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/set_user_mfa_preference.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#set_user_mfa_preference)
        """

    def set_user_pool_mfa_config(
        self, **kwargs: Unpack[SetUserPoolMfaConfigRequestTypeDef]
    ) -> SetUserPoolMfaConfigResponseTypeDef:
        """
        Sets user pool multi-factor authentication (MFA) and passkey configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/set_user_pool_mfa_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#set_user_pool_mfa_config)
        """

    def set_user_settings(self, **kwargs: Unpack[SetUserSettingsRequestTypeDef]) -> Dict[str, Any]:
        """
        <i>This action is no longer supported.</i> You can use it to configure only SMS
        MFA.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/set_user_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#set_user_settings)
        """

    def sign_up(self, **kwargs: Unpack[SignUpRequestTypeDef]) -> SignUpResponseTypeDef:
        """
        Registers a user with an app client and requests a user name, password, and
        user attributes in the user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/sign_up.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#sign_up)
        """

    def start_user_import_job(
        self, **kwargs: Unpack[StartUserImportJobRequestTypeDef]
    ) -> StartUserImportJobResponseTypeDef:
        """
        Instructs your user pool to start importing users from a CSV file that contains
        their usernames and attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/start_user_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#start_user_import_job)
        """

    def start_web_authn_registration(
        self, **kwargs: Unpack[StartWebAuthnRegistrationRequestTypeDef]
    ) -> StartWebAuthnRegistrationResponseTypeDef:
        """
        Requests credential creation options from your user pool for the currently
        signed-in user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/start_web_authn_registration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#start_web_authn_registration)
        """

    def stop_user_import_job(
        self, **kwargs: Unpack[StopUserImportJobRequestTypeDef]
    ) -> StopUserImportJobResponseTypeDef:
        """
        Instructs your user pool to stop a running job that's importing users from a
        CSV file that contains their usernames and attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/stop_user_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#stop_user_import_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns a set of tags to an Amazon Cognito user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Given tag IDs that you previously assigned to a user pool, removes them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#untag_resource)
        """

    def update_auth_event_feedback(
        self, **kwargs: Unpack[UpdateAuthEventFeedbackRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Provides the feedback for an authentication event generated by threat
        protection features.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_auth_event_feedback.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_auth_event_feedback)
        """

    def update_device_status(
        self, **kwargs: Unpack[UpdateDeviceStatusRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the status of a the currently signed-in user's device so that it is
        marked as remembered or not remembered for the purpose of device
        authentication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_device_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_device_status)
        """

    def update_group(
        self, **kwargs: Unpack[UpdateGroupRequestTypeDef]
    ) -> UpdateGroupResponseTypeDef:
        """
        Given the name of a user pool group, updates any of the properties for
        precedence, IAM role, or description.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_group)
        """

    def update_identity_provider(
        self, **kwargs: Unpack[UpdateIdentityProviderRequestTypeDef]
    ) -> UpdateIdentityProviderResponseTypeDef:
        """
        Modifies the configuration and trust relationship between a third-party
        identity provider (IdP) and a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_identity_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_identity_provider)
        """

    def update_managed_login_branding(
        self, **kwargs: Unpack[UpdateManagedLoginBrandingRequestTypeDef]
    ) -> UpdateManagedLoginBrandingResponseTypeDef:
        """
        Configures the branding settings for a user pool style.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_managed_login_branding.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_managed_login_branding)
        """

    def update_resource_server(
        self, **kwargs: Unpack[UpdateResourceServerRequestTypeDef]
    ) -> UpdateResourceServerResponseTypeDef:
        """
        Updates the name and scopes of a resource server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_resource_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_resource_server)
        """

    def update_user_attributes(
        self, **kwargs: Unpack[UpdateUserAttributesRequestTypeDef]
    ) -> UpdateUserAttributesResponseTypeDef:
        """
        Updates the currently signed-in user's attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_user_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_user_attributes)
        """

    def update_user_pool(self, **kwargs: Unpack[UpdateUserPoolRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the configuration of a user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_user_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_user_pool)
        """

    def update_user_pool_client(
        self, **kwargs: Unpack[UpdateUserPoolClientRequestTypeDef]
    ) -> UpdateUserPoolClientResponseTypeDef:
        """
        Given a user pool app client ID, updates the configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_user_pool_client.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_user_pool_client)
        """

    def update_user_pool_domain(
        self, **kwargs: Unpack[UpdateUserPoolDomainRequestTypeDef]
    ) -> UpdateUserPoolDomainResponseTypeDef:
        """
        A user pool domain hosts managed login, an authorization server and web server
        for authentication in your application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/update_user_pool_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#update_user_pool_domain)
        """

    def verify_software_token(
        self, **kwargs: Unpack[VerifySoftwareTokenRequestTypeDef]
    ) -> VerifySoftwareTokenResponseTypeDef:
        """
        Registers the current user's time-based one-time password (TOTP) authenticator
        with a code generated in their authenticator app from a private key that's
        supplied by your user pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/verify_software_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#verify_software_token)
        """

    def verify_user_attribute(
        self, **kwargs: Unpack[VerifyUserAttributeRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Submits a verification code for a signed-in user who has added or changed a
        value of an auto-verified attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/verify_user_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#verify_user_attribute)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["admin_list_groups_for_user"]
    ) -> AdminListGroupsForUserPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["admin_list_user_auth_events"]
    ) -> AdminListUserAuthEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_groups"]
    ) -> ListGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_identity_providers"]
    ) -> ListIdentityProvidersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_servers"]
    ) -> ListResourceServersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_user_pool_clients"]
    ) -> ListUserPoolClientsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_user_pools"]
    ) -> ListUserPoolsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_users_in_group"]
    ) -> ListUsersInGroupPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_users"]
    ) -> ListUsersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client/#get_paginator)
        """
