"""
Type annotations for cognito-idp service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cognito_idp.type_defs import AccountRecoverySettingTypeTypeDef

    data: AccountRecoverySettingTypeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AccountTakeoverEventActionTypeType,
    AdvancedSecurityModeTypeType,
    AliasAttributeTypeType,
    AttributeDataTypeType,
    AuthFlowTypeType,
    ChallengeNameType,
    ChallengeNameTypeType,
    ChallengeResponseType,
    CompromisedCredentialsEventActionTypeType,
    DefaultEmailOptionTypeType,
    DeliveryMediumTypeType,
    DeviceRememberedStatusTypeType,
    DomainStatusTypeType,
    EmailSendingAccountTypeType,
    EventFilterTypeType,
    EventResponseTypeType,
    EventTypeType,
    ExplicitAuthFlowsTypeType,
    FeedbackValueTypeType,
    IdentityProviderTypeTypeType,
    MessageActionTypeType,
    OAuthFlowTypeType,
    PreventUserExistenceErrorTypesType,
    RecoveryOptionNameTypeType,
    RiskDecisionTypeType,
    RiskLevelTypeType,
    StatusTypeType,
    TimeUnitsTypeType,
    UserImportJobStatusTypeType,
    UsernameAttributeTypeType,
    UserPoolMfaTypeType,
    UserStatusTypeType,
    VerifiedAttributeTypeType,
    VerifySoftwareTokenResponseTypeType,
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
    "AccountRecoverySettingTypeTypeDef",
    "AccountTakeoverActionTypeTypeDef",
    "AccountTakeoverActionsTypeTypeDef",
    "AccountTakeoverRiskConfigurationTypeTypeDef",
    "AddCustomAttributesRequestRequestTypeDef",
    "AdminAddUserToGroupRequestRequestTypeDef",
    "AdminConfirmSignUpRequestRequestTypeDef",
    "AdminCreateUserConfigTypeTypeDef",
    "AdminCreateUserRequestRequestTypeDef",
    "AdminCreateUserResponseTypeDef",
    "AdminDeleteUserAttributesRequestRequestTypeDef",
    "AdminDeleteUserRequestRequestTypeDef",
    "AdminDisableProviderForUserRequestRequestTypeDef",
    "AdminDisableUserRequestRequestTypeDef",
    "AdminEnableUserRequestRequestTypeDef",
    "AdminForgetDeviceRequestRequestTypeDef",
    "AdminGetDeviceRequestRequestTypeDef",
    "AdminGetDeviceResponseTypeDef",
    "AdminGetUserRequestRequestTypeDef",
    "AdminGetUserResponseTypeDef",
    "AdminInitiateAuthRequestRequestTypeDef",
    "AdminInitiateAuthResponseTypeDef",
    "AdminLinkProviderForUserRequestRequestTypeDef",
    "AdminListDevicesRequestRequestTypeDef",
    "AdminListDevicesResponseTypeDef",
    "AdminListGroupsForUserRequestRequestTypeDef",
    "AdminListGroupsForUserResponseTypeDef",
    "AdminListUserAuthEventsRequestRequestTypeDef",
    "AdminListUserAuthEventsResponseTypeDef",
    "AdminRemoveUserFromGroupRequestRequestTypeDef",
    "AdminResetUserPasswordRequestRequestTypeDef",
    "AdminRespondToAuthChallengeRequestRequestTypeDef",
    "AdminRespondToAuthChallengeResponseTypeDef",
    "AdminSetUserMFAPreferenceRequestRequestTypeDef",
    "AdminSetUserPasswordRequestRequestTypeDef",
    "AdminSetUserSettingsRequestRequestTypeDef",
    "AdminUpdateAuthEventFeedbackRequestRequestTypeDef",
    "AdminUpdateDeviceStatusRequestRequestTypeDef",
    "AdminUpdateUserAttributesRequestRequestTypeDef",
    "AdminUserGlobalSignOutRequestRequestTypeDef",
    "AnalyticsConfigurationTypeTypeDef",
    "AnalyticsMetadataTypeTypeDef",
    "AssociateSoftwareTokenRequestRequestTypeDef",
    "AssociateSoftwareTokenResponseTypeDef",
    "AttributeTypeTypeDef",
    "AuthEventTypeTypeDef",
    "AuthenticationResultTypeTypeDef",
    "ChallengeResponseTypeTypeDef",
    "ChangePasswordRequestRequestTypeDef",
    "CodeDeliveryDetailsTypeTypeDef",
    "CompromisedCredentialsActionsTypeTypeDef",
    "CompromisedCredentialsRiskConfigurationTypeTypeDef",
    "ConfirmDeviceRequestRequestTypeDef",
    "ConfirmDeviceResponseTypeDef",
    "ConfirmForgotPasswordRequestRequestTypeDef",
    "ConfirmSignUpRequestRequestTypeDef",
    "ContextDataTypeTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateIdentityProviderRequestRequestTypeDef",
    "CreateIdentityProviderResponseTypeDef",
    "CreateResourceServerRequestRequestTypeDef",
    "CreateResourceServerResponseTypeDef",
    "CreateUserImportJobRequestRequestTypeDef",
    "CreateUserImportJobResponseTypeDef",
    "CreateUserPoolClientRequestRequestTypeDef",
    "CreateUserPoolClientResponseTypeDef",
    "CreateUserPoolDomainRequestRequestTypeDef",
    "CreateUserPoolDomainResponseTypeDef",
    "CreateUserPoolRequestRequestTypeDef",
    "CreateUserPoolResponseTypeDef",
    "CustomDomainConfigTypeTypeDef",
    "CustomEmailLambdaVersionConfigTypeTypeDef",
    "CustomSMSLambdaVersionConfigTypeTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteIdentityProviderRequestRequestTypeDef",
    "DeleteResourceServerRequestRequestTypeDef",
    "DeleteUserAttributesRequestRequestTypeDef",
    "DeleteUserPoolClientRequestRequestTypeDef",
    "DeleteUserPoolDomainRequestRequestTypeDef",
    "DeleteUserPoolRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeIdentityProviderRequestRequestTypeDef",
    "DescribeIdentityProviderResponseTypeDef",
    "DescribeResourceServerRequestRequestTypeDef",
    "DescribeResourceServerResponseTypeDef",
    "DescribeRiskConfigurationRequestRequestTypeDef",
    "DescribeRiskConfigurationResponseTypeDef",
    "DescribeUserImportJobRequestRequestTypeDef",
    "DescribeUserImportJobResponseTypeDef",
    "DescribeUserPoolClientRequestRequestTypeDef",
    "DescribeUserPoolClientResponseTypeDef",
    "DescribeUserPoolDomainRequestRequestTypeDef",
    "DescribeUserPoolDomainResponseTypeDef",
    "DescribeUserPoolRequestRequestTypeDef",
    "DescribeUserPoolResponseTypeDef",
    "DeviceConfigurationTypeTypeDef",
    "DeviceSecretVerifierConfigTypeTypeDef",
    "DeviceTypeTypeDef",
    "DomainDescriptionTypeTypeDef",
    "EmailConfigurationTypeTypeDef",
    "EventContextDataTypeTypeDef",
    "EventFeedbackTypeTypeDef",
    "EventRiskTypeTypeDef",
    "ForgetDeviceRequestRequestTypeDef",
    "ForgotPasswordRequestRequestTypeDef",
    "ForgotPasswordResponseTypeDef",
    "GetCSVHeaderRequestRequestTypeDef",
    "GetCSVHeaderResponseTypeDef",
    "GetDeviceRequestRequestTypeDef",
    "GetDeviceResponseTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GetGroupResponseTypeDef",
    "GetIdentityProviderByIdentifierRequestRequestTypeDef",
    "GetIdentityProviderByIdentifierResponseTypeDef",
    "GetSigningCertificateRequestRequestTypeDef",
    "GetSigningCertificateResponseTypeDef",
    "GetUICustomizationRequestRequestTypeDef",
    "GetUICustomizationResponseTypeDef",
    "GetUserAttributeVerificationCodeRequestRequestTypeDef",
    "GetUserAttributeVerificationCodeResponseTypeDef",
    "GetUserPoolMfaConfigRequestRequestTypeDef",
    "GetUserPoolMfaConfigResponseTypeDef",
    "GetUserRequestRequestTypeDef",
    "GetUserResponseTypeDef",
    "GlobalSignOutRequestRequestTypeDef",
    "GroupTypeTypeDef",
    "HttpHeaderTypeDef",
    "IdentityProviderTypeTypeDef",
    "InitiateAuthRequestRequestTypeDef",
    "InitiateAuthResponseTypeDef",
    "LambdaConfigTypeTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListDevicesResponseTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListIdentityProvidersRequestRequestTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListResourceServersRequestRequestTypeDef",
    "ListResourceServersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUserImportJobsRequestRequestTypeDef",
    "ListUserImportJobsResponseTypeDef",
    "ListUserPoolClientsRequestRequestTypeDef",
    "ListUserPoolClientsResponseTypeDef",
    "ListUserPoolsRequestRequestTypeDef",
    "ListUserPoolsResponseTypeDef",
    "ListUsersInGroupRequestRequestTypeDef",
    "ListUsersInGroupResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "MFAOptionTypeTypeDef",
    "MessageTemplateTypeTypeDef",
    "NewDeviceMetadataTypeTypeDef",
    "NotifyConfigurationTypeTypeDef",
    "NotifyEmailTypeTypeDef",
    "NumberAttributeConstraintsTypeTypeDef",
    "PaginatorConfigTypeDef",
    "PasswordPolicyTypeTypeDef",
    "ProviderDescriptionTypeDef",
    "ProviderUserIdentifierTypeTypeDef",
    "RecoveryOptionTypeTypeDef",
    "ResendConfirmationCodeRequestRequestTypeDef",
    "ResendConfirmationCodeResponseTypeDef",
    "ResourceServerScopeTypeTypeDef",
    "ResourceServerTypeTypeDef",
    "RespondToAuthChallengeRequestRequestTypeDef",
    "RespondToAuthChallengeResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeTokenRequestRequestTypeDef",
    "RiskConfigurationTypeTypeDef",
    "RiskExceptionConfigurationTypeTypeDef",
    "SMSMfaSettingsTypeTypeDef",
    "SchemaAttributeTypeTypeDef",
    "SetRiskConfigurationRequestRequestTypeDef",
    "SetRiskConfigurationResponseTypeDef",
    "SetUICustomizationRequestRequestTypeDef",
    "SetUICustomizationResponseTypeDef",
    "SetUserMFAPreferenceRequestRequestTypeDef",
    "SetUserPoolMfaConfigRequestRequestTypeDef",
    "SetUserPoolMfaConfigResponseTypeDef",
    "SetUserSettingsRequestRequestTypeDef",
    "SignUpRequestRequestTypeDef",
    "SignUpResponseTypeDef",
    "SmsConfigurationTypeTypeDef",
    "SmsMfaConfigTypeTypeDef",
    "SoftwareTokenMfaConfigTypeTypeDef",
    "SoftwareTokenMfaSettingsTypeTypeDef",
    "StartUserImportJobRequestRequestTypeDef",
    "StartUserImportJobResponseTypeDef",
    "StopUserImportJobRequestRequestTypeDef",
    "StopUserImportJobResponseTypeDef",
    "StringAttributeConstraintsTypeTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TokenValidityUnitsTypeTypeDef",
    "UICustomizationTypeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAuthEventFeedbackRequestRequestTypeDef",
    "UpdateDeviceStatusRequestRequestTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateGroupResponseTypeDef",
    "UpdateIdentityProviderRequestRequestTypeDef",
    "UpdateIdentityProviderResponseTypeDef",
    "UpdateResourceServerRequestRequestTypeDef",
    "UpdateResourceServerResponseTypeDef",
    "UpdateUserAttributesRequestRequestTypeDef",
    "UpdateUserAttributesResponseTypeDef",
    "UpdateUserPoolClientRequestRequestTypeDef",
    "UpdateUserPoolClientResponseTypeDef",
    "UpdateUserPoolDomainRequestRequestTypeDef",
    "UpdateUserPoolDomainResponseTypeDef",
    "UpdateUserPoolRequestRequestTypeDef",
    "UserContextDataTypeTypeDef",
    "UserImportJobTypeTypeDef",
    "UserPoolAddOnsTypeTypeDef",
    "UserPoolClientDescriptionTypeDef",
    "UserPoolClientTypeTypeDef",
    "UserPoolDescriptionTypeTypeDef",
    "UserPoolPolicyTypeTypeDef",
    "UserPoolTypeTypeDef",
    "UserTypeTypeDef",
    "UsernameConfigurationTypeTypeDef",
    "VerificationMessageTemplateTypeTypeDef",
    "VerifySoftwareTokenRequestRequestTypeDef",
    "VerifySoftwareTokenResponseTypeDef",
    "VerifyUserAttributeRequestRequestTypeDef",
)

AccountRecoverySettingTypeTypeDef = TypedDict(
    "AccountRecoverySettingTypeTypeDef",
    {
        "RecoveryMechanisms": List["RecoveryOptionTypeTypeDef"],
    },
    total=False,
)

AccountTakeoverActionTypeTypeDef = TypedDict(
    "AccountTakeoverActionTypeTypeDef",
    {
        "Notify": bool,
        "EventAction": AccountTakeoverEventActionTypeType,
    },
)

AccountTakeoverActionsTypeTypeDef = TypedDict(
    "AccountTakeoverActionsTypeTypeDef",
    {
        "LowAction": "AccountTakeoverActionTypeTypeDef",
        "MediumAction": "AccountTakeoverActionTypeTypeDef",
        "HighAction": "AccountTakeoverActionTypeTypeDef",
    },
    total=False,
)

_RequiredAccountTakeoverRiskConfigurationTypeTypeDef = TypedDict(
    "_RequiredAccountTakeoverRiskConfigurationTypeTypeDef",
    {
        "Actions": "AccountTakeoverActionsTypeTypeDef",
    },
)
_OptionalAccountTakeoverRiskConfigurationTypeTypeDef = TypedDict(
    "_OptionalAccountTakeoverRiskConfigurationTypeTypeDef",
    {
        "NotifyConfiguration": "NotifyConfigurationTypeTypeDef",
    },
    total=False,
)

class AccountTakeoverRiskConfigurationTypeTypeDef(
    _RequiredAccountTakeoverRiskConfigurationTypeTypeDef,
    _OptionalAccountTakeoverRiskConfigurationTypeTypeDef,
):
    pass

AddCustomAttributesRequestRequestTypeDef = TypedDict(
    "AddCustomAttributesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "CustomAttributes": List["SchemaAttributeTypeTypeDef"],
    },
)

AdminAddUserToGroupRequestRequestTypeDef = TypedDict(
    "AdminAddUserToGroupRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "GroupName": str,
    },
)

_RequiredAdminConfirmSignUpRequestRequestTypeDef = TypedDict(
    "_RequiredAdminConfirmSignUpRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminConfirmSignUpRequestRequestTypeDef = TypedDict(
    "_OptionalAdminConfirmSignUpRequestRequestTypeDef",
    {
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)

class AdminConfirmSignUpRequestRequestTypeDef(
    _RequiredAdminConfirmSignUpRequestRequestTypeDef,
    _OptionalAdminConfirmSignUpRequestRequestTypeDef,
):
    pass

AdminCreateUserConfigTypeTypeDef = TypedDict(
    "AdminCreateUserConfigTypeTypeDef",
    {
        "AllowAdminCreateUserOnly": bool,
        "UnusedAccountValidityDays": int,
        "InviteMessageTemplate": "MessageTemplateTypeTypeDef",
    },
    total=False,
)

_RequiredAdminCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredAdminCreateUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalAdminCreateUserRequestRequestTypeDef",
    {
        "UserAttributes": List["AttributeTypeTypeDef"],
        "ValidationData": List["AttributeTypeTypeDef"],
        "TemporaryPassword": str,
        "ForceAliasCreation": bool,
        "MessageAction": MessageActionTypeType,
        "DesiredDeliveryMediums": List[DeliveryMediumTypeType],
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)

class AdminCreateUserRequestRequestTypeDef(
    _RequiredAdminCreateUserRequestRequestTypeDef, _OptionalAdminCreateUserRequestRequestTypeDef
):
    pass

AdminCreateUserResponseTypeDef = TypedDict(
    "AdminCreateUserResponseTypeDef",
    {
        "User": "UserTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminDeleteUserAttributesRequestRequestTypeDef = TypedDict(
    "AdminDeleteUserAttributesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "UserAttributeNames": List[str],
    },
)

AdminDeleteUserRequestRequestTypeDef = TypedDict(
    "AdminDeleteUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AdminDisableProviderForUserRequestRequestTypeDef = TypedDict(
    "AdminDisableProviderForUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "User": "ProviderUserIdentifierTypeTypeDef",
    },
)

AdminDisableUserRequestRequestTypeDef = TypedDict(
    "AdminDisableUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AdminEnableUserRequestRequestTypeDef = TypedDict(
    "AdminEnableUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AdminForgetDeviceRequestRequestTypeDef = TypedDict(
    "AdminForgetDeviceRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "DeviceKey": str,
    },
)

AdminGetDeviceRequestRequestTypeDef = TypedDict(
    "AdminGetDeviceRequestRequestTypeDef",
    {
        "DeviceKey": str,
        "UserPoolId": str,
        "Username": str,
    },
)

AdminGetDeviceResponseTypeDef = TypedDict(
    "AdminGetDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminGetUserRequestRequestTypeDef = TypedDict(
    "AdminGetUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AdminGetUserResponseTypeDef = TypedDict(
    "AdminGetUserResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List["AttributeTypeTypeDef"],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": UserStatusTypeType,
        "MFAOptions": List["MFAOptionTypeTypeDef"],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAdminInitiateAuthRequestRequestTypeDef = TypedDict(
    "_RequiredAdminInitiateAuthRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "AuthFlow": AuthFlowTypeType,
    },
)
_OptionalAdminInitiateAuthRequestRequestTypeDef = TypedDict(
    "_OptionalAdminInitiateAuthRequestRequestTypeDef",
    {
        "AuthParameters": Dict[str, str],
        "ClientMetadata": Dict[str, str],
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "ContextData": "ContextDataTypeTypeDef",
    },
    total=False,
)

class AdminInitiateAuthRequestRequestTypeDef(
    _RequiredAdminInitiateAuthRequestRequestTypeDef, _OptionalAdminInitiateAuthRequestRequestTypeDef
):
    pass

AdminInitiateAuthResponseTypeDef = TypedDict(
    "AdminInitiateAuthResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminLinkProviderForUserRequestRequestTypeDef = TypedDict(
    "AdminLinkProviderForUserRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "DestinationUser": "ProviderUserIdentifierTypeTypeDef",
        "SourceUser": "ProviderUserIdentifierTypeTypeDef",
    },
)

_RequiredAdminListDevicesRequestRequestTypeDef = TypedDict(
    "_RequiredAdminListDevicesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminListDevicesRequestRequestTypeDef = TypedDict(
    "_OptionalAdminListDevicesRequestRequestTypeDef",
    {
        "Limit": int,
        "PaginationToken": str,
    },
    total=False,
)

class AdminListDevicesRequestRequestTypeDef(
    _RequiredAdminListDevicesRequestRequestTypeDef, _OptionalAdminListDevicesRequestRequestTypeDef
):
    pass

AdminListDevicesResponseTypeDef = TypedDict(
    "AdminListDevicesResponseTypeDef",
    {
        "Devices": List["DeviceTypeTypeDef"],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAdminListGroupsForUserRequestRequestTypeDef = TypedDict(
    "_RequiredAdminListGroupsForUserRequestRequestTypeDef",
    {
        "Username": str,
        "UserPoolId": str,
    },
)
_OptionalAdminListGroupsForUserRequestRequestTypeDef = TypedDict(
    "_OptionalAdminListGroupsForUserRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class AdminListGroupsForUserRequestRequestTypeDef(
    _RequiredAdminListGroupsForUserRequestRequestTypeDef,
    _OptionalAdminListGroupsForUserRequestRequestTypeDef,
):
    pass

AdminListGroupsForUserResponseTypeDef = TypedDict(
    "AdminListGroupsForUserResponseTypeDef",
    {
        "Groups": List["GroupTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAdminListUserAuthEventsRequestRequestTypeDef = TypedDict(
    "_RequiredAdminListUserAuthEventsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminListUserAuthEventsRequestRequestTypeDef = TypedDict(
    "_OptionalAdminListUserAuthEventsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class AdminListUserAuthEventsRequestRequestTypeDef(
    _RequiredAdminListUserAuthEventsRequestRequestTypeDef,
    _OptionalAdminListUserAuthEventsRequestRequestTypeDef,
):
    pass

AdminListUserAuthEventsResponseTypeDef = TypedDict(
    "AdminListUserAuthEventsResponseTypeDef",
    {
        "AuthEvents": List["AuthEventTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdminRemoveUserFromGroupRequestRequestTypeDef = TypedDict(
    "AdminRemoveUserFromGroupRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "GroupName": str,
    },
)

_RequiredAdminResetUserPasswordRequestRequestTypeDef = TypedDict(
    "_RequiredAdminResetUserPasswordRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)
_OptionalAdminResetUserPasswordRequestRequestTypeDef = TypedDict(
    "_OptionalAdminResetUserPasswordRequestRequestTypeDef",
    {
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)

class AdminResetUserPasswordRequestRequestTypeDef(
    _RequiredAdminResetUserPasswordRequestRequestTypeDef,
    _OptionalAdminResetUserPasswordRequestRequestTypeDef,
):
    pass

_RequiredAdminRespondToAuthChallengeRequestRequestTypeDef = TypedDict(
    "_RequiredAdminRespondToAuthChallengeRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ChallengeName": ChallengeNameTypeType,
    },
)
_OptionalAdminRespondToAuthChallengeRequestRequestTypeDef = TypedDict(
    "_OptionalAdminRespondToAuthChallengeRequestRequestTypeDef",
    {
        "ChallengeResponses": Dict[str, str],
        "Session": str,
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "ContextData": "ContextDataTypeTypeDef",
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)

class AdminRespondToAuthChallengeRequestRequestTypeDef(
    _RequiredAdminRespondToAuthChallengeRequestRequestTypeDef,
    _OptionalAdminRespondToAuthChallengeRequestRequestTypeDef,
):
    pass

AdminRespondToAuthChallengeResponseTypeDef = TypedDict(
    "AdminRespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAdminSetUserMFAPreferenceRequestRequestTypeDef = TypedDict(
    "_RequiredAdminSetUserMFAPreferenceRequestRequestTypeDef",
    {
        "Username": str,
        "UserPoolId": str,
    },
)
_OptionalAdminSetUserMFAPreferenceRequestRequestTypeDef = TypedDict(
    "_OptionalAdminSetUserMFAPreferenceRequestRequestTypeDef",
    {
        "SMSMfaSettings": "SMSMfaSettingsTypeTypeDef",
        "SoftwareTokenMfaSettings": "SoftwareTokenMfaSettingsTypeTypeDef",
    },
    total=False,
)

class AdminSetUserMFAPreferenceRequestRequestTypeDef(
    _RequiredAdminSetUserMFAPreferenceRequestRequestTypeDef,
    _OptionalAdminSetUserMFAPreferenceRequestRequestTypeDef,
):
    pass

_RequiredAdminSetUserPasswordRequestRequestTypeDef = TypedDict(
    "_RequiredAdminSetUserPasswordRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "Password": str,
    },
)
_OptionalAdminSetUserPasswordRequestRequestTypeDef = TypedDict(
    "_OptionalAdminSetUserPasswordRequestRequestTypeDef",
    {
        "Permanent": bool,
    },
    total=False,
)

class AdminSetUserPasswordRequestRequestTypeDef(
    _RequiredAdminSetUserPasswordRequestRequestTypeDef,
    _OptionalAdminSetUserPasswordRequestRequestTypeDef,
):
    pass

AdminSetUserSettingsRequestRequestTypeDef = TypedDict(
    "AdminSetUserSettingsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "MFAOptions": List["MFAOptionTypeTypeDef"],
    },
)

AdminUpdateAuthEventFeedbackRequestRequestTypeDef = TypedDict(
    "AdminUpdateAuthEventFeedbackRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "EventId": str,
        "FeedbackValue": FeedbackValueTypeType,
    },
)

_RequiredAdminUpdateDeviceStatusRequestRequestTypeDef = TypedDict(
    "_RequiredAdminUpdateDeviceStatusRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "DeviceKey": str,
    },
)
_OptionalAdminUpdateDeviceStatusRequestRequestTypeDef = TypedDict(
    "_OptionalAdminUpdateDeviceStatusRequestRequestTypeDef",
    {
        "DeviceRememberedStatus": DeviceRememberedStatusTypeType,
    },
    total=False,
)

class AdminUpdateDeviceStatusRequestRequestTypeDef(
    _RequiredAdminUpdateDeviceStatusRequestRequestTypeDef,
    _OptionalAdminUpdateDeviceStatusRequestRequestTypeDef,
):
    pass

_RequiredAdminUpdateUserAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredAdminUpdateUserAttributesRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "UserAttributes": List["AttributeTypeTypeDef"],
    },
)
_OptionalAdminUpdateUserAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalAdminUpdateUserAttributesRequestRequestTypeDef",
    {
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)

class AdminUpdateUserAttributesRequestRequestTypeDef(
    _RequiredAdminUpdateUserAttributesRequestRequestTypeDef,
    _OptionalAdminUpdateUserAttributesRequestRequestTypeDef,
):
    pass

AdminUserGlobalSignOutRequestRequestTypeDef = TypedDict(
    "AdminUserGlobalSignOutRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
    },
)

AnalyticsConfigurationTypeTypeDef = TypedDict(
    "AnalyticsConfigurationTypeTypeDef",
    {
        "ApplicationId": str,
        "ApplicationArn": str,
        "RoleArn": str,
        "ExternalId": str,
        "UserDataShared": bool,
    },
    total=False,
)

AnalyticsMetadataTypeTypeDef = TypedDict(
    "AnalyticsMetadataTypeTypeDef",
    {
        "AnalyticsEndpointId": str,
    },
    total=False,
)

AssociateSoftwareTokenRequestRequestTypeDef = TypedDict(
    "AssociateSoftwareTokenRequestRequestTypeDef",
    {
        "AccessToken": str,
        "Session": str,
    },
    total=False,
)

AssociateSoftwareTokenResponseTypeDef = TypedDict(
    "AssociateSoftwareTokenResponseTypeDef",
    {
        "SecretCode": str,
        "Session": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAttributeTypeTypeDef = TypedDict(
    "_RequiredAttributeTypeTypeDef",
    {
        "Name": str,
    },
)
_OptionalAttributeTypeTypeDef = TypedDict(
    "_OptionalAttributeTypeTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class AttributeTypeTypeDef(_RequiredAttributeTypeTypeDef, _OptionalAttributeTypeTypeDef):
    pass

AuthEventTypeTypeDef = TypedDict(
    "AuthEventTypeTypeDef",
    {
        "EventId": str,
        "EventType": EventTypeType,
        "CreationDate": datetime,
        "EventResponse": EventResponseTypeType,
        "EventRisk": "EventRiskTypeTypeDef",
        "ChallengeResponses": List["ChallengeResponseTypeTypeDef"],
        "EventContextData": "EventContextDataTypeTypeDef",
        "EventFeedback": "EventFeedbackTypeTypeDef",
    },
    total=False,
)

AuthenticationResultTypeTypeDef = TypedDict(
    "AuthenticationResultTypeTypeDef",
    {
        "AccessToken": str,
        "ExpiresIn": int,
        "TokenType": str,
        "RefreshToken": str,
        "IdToken": str,
        "NewDeviceMetadata": "NewDeviceMetadataTypeTypeDef",
    },
    total=False,
)

ChallengeResponseTypeTypeDef = TypedDict(
    "ChallengeResponseTypeTypeDef",
    {
        "ChallengeName": ChallengeNameType,
        "ChallengeResponse": ChallengeResponseType,
    },
    total=False,
)

ChangePasswordRequestRequestTypeDef = TypedDict(
    "ChangePasswordRequestRequestTypeDef",
    {
        "PreviousPassword": str,
        "ProposedPassword": str,
        "AccessToken": str,
    },
)

CodeDeliveryDetailsTypeTypeDef = TypedDict(
    "CodeDeliveryDetailsTypeTypeDef",
    {
        "Destination": str,
        "DeliveryMedium": DeliveryMediumTypeType,
        "AttributeName": str,
    },
    total=False,
)

CompromisedCredentialsActionsTypeTypeDef = TypedDict(
    "CompromisedCredentialsActionsTypeTypeDef",
    {
        "EventAction": CompromisedCredentialsEventActionTypeType,
    },
)

_RequiredCompromisedCredentialsRiskConfigurationTypeTypeDef = TypedDict(
    "_RequiredCompromisedCredentialsRiskConfigurationTypeTypeDef",
    {
        "Actions": "CompromisedCredentialsActionsTypeTypeDef",
    },
)
_OptionalCompromisedCredentialsRiskConfigurationTypeTypeDef = TypedDict(
    "_OptionalCompromisedCredentialsRiskConfigurationTypeTypeDef",
    {
        "EventFilter": List[EventFilterTypeType],
    },
    total=False,
)

class CompromisedCredentialsRiskConfigurationTypeTypeDef(
    _RequiredCompromisedCredentialsRiskConfigurationTypeTypeDef,
    _OptionalCompromisedCredentialsRiskConfigurationTypeTypeDef,
):
    pass

_RequiredConfirmDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredConfirmDeviceRequestRequestTypeDef",
    {
        "AccessToken": str,
        "DeviceKey": str,
    },
)
_OptionalConfirmDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalConfirmDeviceRequestRequestTypeDef",
    {
        "DeviceSecretVerifierConfig": "DeviceSecretVerifierConfigTypeTypeDef",
        "DeviceName": str,
    },
    total=False,
)

class ConfirmDeviceRequestRequestTypeDef(
    _RequiredConfirmDeviceRequestRequestTypeDef, _OptionalConfirmDeviceRequestRequestTypeDef
):
    pass

ConfirmDeviceResponseTypeDef = TypedDict(
    "ConfirmDeviceResponseTypeDef",
    {
        "UserConfirmationNecessary": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredConfirmForgotPasswordRequestRequestTypeDef = TypedDict(
    "_RequiredConfirmForgotPasswordRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "ConfirmationCode": str,
        "Password": str,
    },
)
_OptionalConfirmForgotPasswordRequestRequestTypeDef = TypedDict(
    "_OptionalConfirmForgotPasswordRequestRequestTypeDef",
    {
        "SecretHash": str,
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "UserContextData": "UserContextDataTypeTypeDef",
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)

class ConfirmForgotPasswordRequestRequestTypeDef(
    _RequiredConfirmForgotPasswordRequestRequestTypeDef,
    _OptionalConfirmForgotPasswordRequestRequestTypeDef,
):
    pass

_RequiredConfirmSignUpRequestRequestTypeDef = TypedDict(
    "_RequiredConfirmSignUpRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "ConfirmationCode": str,
    },
)
_OptionalConfirmSignUpRequestRequestTypeDef = TypedDict(
    "_OptionalConfirmSignUpRequestRequestTypeDef",
    {
        "SecretHash": str,
        "ForceAliasCreation": bool,
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "UserContextData": "UserContextDataTypeTypeDef",
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)

class ConfirmSignUpRequestRequestTypeDef(
    _RequiredConfirmSignUpRequestRequestTypeDef, _OptionalConfirmSignUpRequestRequestTypeDef
):
    pass

_RequiredContextDataTypeTypeDef = TypedDict(
    "_RequiredContextDataTypeTypeDef",
    {
        "IpAddress": str,
        "ServerName": str,
        "ServerPath": str,
        "HttpHeaders": List["HttpHeaderTypeDef"],
    },
)
_OptionalContextDataTypeTypeDef = TypedDict(
    "_OptionalContextDataTypeTypeDef",
    {
        "EncodedData": str,
    },
    total=False,
)

class ContextDataTypeTypeDef(_RequiredContextDataTypeTypeDef, _OptionalContextDataTypeTypeDef):
    pass

_RequiredCreateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)
_OptionalCreateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGroupRequestRequestTypeDef",
    {
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
    },
    total=False,
)

class CreateGroupRequestRequestTypeDef(
    _RequiredCreateGroupRequestRequestTypeDef, _OptionalCreateGroupRequestRequestTypeDef
):
    pass

CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Group": "GroupTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": IdentityProviderTypeTypeType,
        "ProviderDetails": Dict[str, str],
    },
)
_OptionalCreateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIdentityProviderRequestRequestTypeDef",
    {
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
    },
    total=False,
)

class CreateIdentityProviderRequestRequestTypeDef(
    _RequiredCreateIdentityProviderRequestRequestTypeDef,
    _OptionalCreateIdentityProviderRequestRequestTypeDef,
):
    pass

CreateIdentityProviderResponseTypeDef = TypedDict(
    "CreateIdentityProviderResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResourceServerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
    },
)
_OptionalCreateResourceServerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateResourceServerRequestRequestTypeDef",
    {
        "Scopes": List["ResourceServerScopeTypeTypeDef"],
    },
    total=False,
)

class CreateResourceServerRequestRequestTypeDef(
    _RequiredCreateResourceServerRequestRequestTypeDef,
    _OptionalCreateResourceServerRequestRequestTypeDef,
):
    pass

CreateResourceServerResponseTypeDef = TypedDict(
    "CreateResourceServerResponseTypeDef",
    {
        "ResourceServer": "ResourceServerTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserImportJobRequestRequestTypeDef = TypedDict(
    "CreateUserImportJobRequestRequestTypeDef",
    {
        "JobName": str,
        "UserPoolId": str,
        "CloudWatchLogsRoleArn": str,
    },
)

CreateUserImportJobResponseTypeDef = TypedDict(
    "CreateUserImportJobResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserPoolClientRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
    },
)
_OptionalCreateUserPoolClientRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserPoolClientRequestRequestTypeDef",
    {
        "GenerateSecret": bool,
        "RefreshTokenValidity": int,
        "AccessTokenValidity": int,
        "IdTokenValidity": int,
        "TokenValidityUnits": "TokenValidityUnitsTypeTypeDef",
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[ExplicitAuthFlowsTypeType],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[OAuthFlowTypeType],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": "AnalyticsConfigurationTypeTypeDef",
        "PreventUserExistenceErrors": PreventUserExistenceErrorTypesType,
        "EnableTokenRevocation": bool,
    },
    total=False,
)

class CreateUserPoolClientRequestRequestTypeDef(
    _RequiredCreateUserPoolClientRequestRequestTypeDef,
    _OptionalCreateUserPoolClientRequestRequestTypeDef,
):
    pass

CreateUserPoolClientResponseTypeDef = TypedDict(
    "CreateUserPoolClientResponseTypeDef",
    {
        "UserPoolClient": "UserPoolClientTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserPoolDomainRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
        "UserPoolId": str,
    },
)
_OptionalCreateUserPoolDomainRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserPoolDomainRequestRequestTypeDef",
    {
        "CustomDomainConfig": "CustomDomainConfigTypeTypeDef",
    },
    total=False,
)

class CreateUserPoolDomainRequestRequestTypeDef(
    _RequiredCreateUserPoolDomainRequestRequestTypeDef,
    _OptionalCreateUserPoolDomainRequestRequestTypeDef,
):
    pass

CreateUserPoolDomainResponseTypeDef = TypedDict(
    "CreateUserPoolDomainResponseTypeDef",
    {
        "CloudFrontDomain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserPoolRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserPoolRequestRequestTypeDef",
    {
        "PoolName": str,
    },
)
_OptionalCreateUserPoolRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserPoolRequestRequestTypeDef",
    {
        "Policies": "UserPoolPolicyTypeTypeDef",
        "LambdaConfig": "LambdaConfigTypeTypeDef",
        "AutoVerifiedAttributes": List[VerifiedAttributeTypeType],
        "AliasAttributes": List[AliasAttributeTypeType],
        "UsernameAttributes": List[UsernameAttributeTypeType],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": "VerificationMessageTemplateTypeTypeDef",
        "SmsAuthenticationMessage": str,
        "MfaConfiguration": UserPoolMfaTypeType,
        "DeviceConfiguration": "DeviceConfigurationTypeTypeDef",
        "EmailConfiguration": "EmailConfigurationTypeTypeDef",
        "SmsConfiguration": "SmsConfigurationTypeTypeDef",
        "UserPoolTags": Dict[str, str],
        "AdminCreateUserConfig": "AdminCreateUserConfigTypeTypeDef",
        "Schema": List["SchemaAttributeTypeTypeDef"],
        "UserPoolAddOns": "UserPoolAddOnsTypeTypeDef",
        "UsernameConfiguration": "UsernameConfigurationTypeTypeDef",
        "AccountRecoverySetting": "AccountRecoverySettingTypeTypeDef",
    },
    total=False,
)

class CreateUserPoolRequestRequestTypeDef(
    _RequiredCreateUserPoolRequestRequestTypeDef, _OptionalCreateUserPoolRequestRequestTypeDef
):
    pass

CreateUserPoolResponseTypeDef = TypedDict(
    "CreateUserPoolResponseTypeDef",
    {
        "UserPool": "UserPoolTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomDomainConfigTypeTypeDef = TypedDict(
    "CustomDomainConfigTypeTypeDef",
    {
        "CertificateArn": str,
    },
)

CustomEmailLambdaVersionConfigTypeTypeDef = TypedDict(
    "CustomEmailLambdaVersionConfigTypeTypeDef",
    {
        "LambdaVersion": Literal["V1_0"],
        "LambdaArn": str,
    },
)

CustomSMSLambdaVersionConfigTypeTypeDef = TypedDict(
    "CustomSMSLambdaVersionConfigTypeTypeDef",
    {
        "LambdaVersion": Literal["V1_0"],
        "LambdaArn": str,
    },
)

DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)

DeleteIdentityProviderRequestRequestTypeDef = TypedDict(
    "DeleteIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
    },
)

DeleteResourceServerRequestRequestTypeDef = TypedDict(
    "DeleteResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
    },
)

DeleteUserAttributesRequestRequestTypeDef = TypedDict(
    "DeleteUserAttributesRequestRequestTypeDef",
    {
        "UserAttributeNames": List[str],
        "AccessToken": str,
    },
)

DeleteUserPoolClientRequestRequestTypeDef = TypedDict(
    "DeleteUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
    },
)

DeleteUserPoolDomainRequestRequestTypeDef = TypedDict(
    "DeleteUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
        "UserPoolId": str,
    },
)

DeleteUserPoolRequestRequestTypeDef = TypedDict(
    "DeleteUserPoolRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)

DescribeIdentityProviderRequestRequestTypeDef = TypedDict(
    "DescribeIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
    },
)

DescribeIdentityProviderResponseTypeDef = TypedDict(
    "DescribeIdentityProviderResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourceServerRequestRequestTypeDef = TypedDict(
    "DescribeResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
    },
)

DescribeResourceServerResponseTypeDef = TypedDict(
    "DescribeResourceServerResponseTypeDef",
    {
        "ResourceServer": "ResourceServerTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRiskConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRiskConfigurationRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalDescribeRiskConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRiskConfigurationRequestRequestTypeDef",
    {
        "ClientId": str,
    },
    total=False,
)

class DescribeRiskConfigurationRequestRequestTypeDef(
    _RequiredDescribeRiskConfigurationRequestRequestTypeDef,
    _OptionalDescribeRiskConfigurationRequestRequestTypeDef,
):
    pass

DescribeRiskConfigurationResponseTypeDef = TypedDict(
    "DescribeRiskConfigurationResponseTypeDef",
    {
        "RiskConfiguration": "RiskConfigurationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserImportJobRequestRequestTypeDef = TypedDict(
    "DescribeUserImportJobRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "JobId": str,
    },
)

DescribeUserImportJobResponseTypeDef = TypedDict(
    "DescribeUserImportJobResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserPoolClientRequestRequestTypeDef = TypedDict(
    "DescribeUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
    },
)

DescribeUserPoolClientResponseTypeDef = TypedDict(
    "DescribeUserPoolClientResponseTypeDef",
    {
        "UserPoolClient": "UserPoolClientTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserPoolDomainRequestRequestTypeDef = TypedDict(
    "DescribeUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
    },
)

DescribeUserPoolDomainResponseTypeDef = TypedDict(
    "DescribeUserPoolDomainResponseTypeDef",
    {
        "DomainDescription": "DomainDescriptionTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserPoolRequestRequestTypeDef = TypedDict(
    "DescribeUserPoolRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

DescribeUserPoolResponseTypeDef = TypedDict(
    "DescribeUserPoolResponseTypeDef",
    {
        "UserPool": "UserPoolTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceConfigurationTypeTypeDef = TypedDict(
    "DeviceConfigurationTypeTypeDef",
    {
        "ChallengeRequiredOnNewDevice": bool,
        "DeviceOnlyRememberedOnUserPrompt": bool,
    },
    total=False,
)

DeviceSecretVerifierConfigTypeTypeDef = TypedDict(
    "DeviceSecretVerifierConfigTypeTypeDef",
    {
        "PasswordVerifier": str,
        "Salt": str,
    },
    total=False,
)

DeviceTypeTypeDef = TypedDict(
    "DeviceTypeTypeDef",
    {
        "DeviceKey": str,
        "DeviceAttributes": List["AttributeTypeTypeDef"],
        "DeviceCreateDate": datetime,
        "DeviceLastModifiedDate": datetime,
        "DeviceLastAuthenticatedDate": datetime,
    },
    total=False,
)

DomainDescriptionTypeTypeDef = TypedDict(
    "DomainDescriptionTypeTypeDef",
    {
        "UserPoolId": str,
        "AWSAccountId": str,
        "Domain": str,
        "S3Bucket": str,
        "CloudFrontDistribution": str,
        "Version": str,
        "Status": DomainStatusTypeType,
        "CustomDomainConfig": "CustomDomainConfigTypeTypeDef",
    },
    total=False,
)

EmailConfigurationTypeTypeDef = TypedDict(
    "EmailConfigurationTypeTypeDef",
    {
        "SourceArn": str,
        "ReplyToEmailAddress": str,
        "EmailSendingAccount": EmailSendingAccountTypeType,
        "From": str,
        "ConfigurationSet": str,
    },
    total=False,
)

EventContextDataTypeTypeDef = TypedDict(
    "EventContextDataTypeTypeDef",
    {
        "IpAddress": str,
        "DeviceName": str,
        "Timezone": str,
        "City": str,
        "Country": str,
    },
    total=False,
)

_RequiredEventFeedbackTypeTypeDef = TypedDict(
    "_RequiredEventFeedbackTypeTypeDef",
    {
        "FeedbackValue": FeedbackValueTypeType,
        "Provider": str,
    },
)
_OptionalEventFeedbackTypeTypeDef = TypedDict(
    "_OptionalEventFeedbackTypeTypeDef",
    {
        "FeedbackDate": datetime,
    },
    total=False,
)

class EventFeedbackTypeTypeDef(
    _RequiredEventFeedbackTypeTypeDef, _OptionalEventFeedbackTypeTypeDef
):
    pass

EventRiskTypeTypeDef = TypedDict(
    "EventRiskTypeTypeDef",
    {
        "RiskDecision": RiskDecisionTypeType,
        "RiskLevel": RiskLevelTypeType,
        "CompromisedCredentialsDetected": bool,
    },
    total=False,
)

_RequiredForgetDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredForgetDeviceRequestRequestTypeDef",
    {
        "DeviceKey": str,
    },
)
_OptionalForgetDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalForgetDeviceRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
    total=False,
)

class ForgetDeviceRequestRequestTypeDef(
    _RequiredForgetDeviceRequestRequestTypeDef, _OptionalForgetDeviceRequestRequestTypeDef
):
    pass

_RequiredForgotPasswordRequestRequestTypeDef = TypedDict(
    "_RequiredForgotPasswordRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
    },
)
_OptionalForgotPasswordRequestRequestTypeDef = TypedDict(
    "_OptionalForgotPasswordRequestRequestTypeDef",
    {
        "SecretHash": str,
        "UserContextData": "UserContextDataTypeTypeDef",
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)

class ForgotPasswordRequestRequestTypeDef(
    _RequiredForgotPasswordRequestRequestTypeDef, _OptionalForgotPasswordRequestRequestTypeDef
):
    pass

ForgotPasswordResponseTypeDef = TypedDict(
    "ForgotPasswordResponseTypeDef",
    {
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCSVHeaderRequestRequestTypeDef = TypedDict(
    "GetCSVHeaderRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

GetCSVHeaderResponseTypeDef = TypedDict(
    "GetCSVHeaderResponseTypeDef",
    {
        "UserPoolId": str,
        "CSVHeader": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredGetDeviceRequestRequestTypeDef",
    {
        "DeviceKey": str,
    },
)
_OptionalGetDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalGetDeviceRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
    total=False,
)

class GetDeviceRequestRequestTypeDef(
    _RequiredGetDeviceRequestRequestTypeDef, _OptionalGetDeviceRequestRequestTypeDef
):
    pass

GetDeviceResponseTypeDef = TypedDict(
    "GetDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupRequestRequestTypeDef = TypedDict(
    "GetGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)

GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef",
    {
        "Group": "GroupTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityProviderByIdentifierRequestRequestTypeDef = TypedDict(
    "GetIdentityProviderByIdentifierRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "IdpIdentifier": str,
    },
)

GetIdentityProviderByIdentifierResponseTypeDef = TypedDict(
    "GetIdentityProviderByIdentifierResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSigningCertificateRequestRequestTypeDef = TypedDict(
    "GetSigningCertificateRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

GetSigningCertificateResponseTypeDef = TypedDict(
    "GetSigningCertificateResponseTypeDef",
    {
        "Certificate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUICustomizationRequestRequestTypeDef = TypedDict(
    "_RequiredGetUICustomizationRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalGetUICustomizationRequestRequestTypeDef = TypedDict(
    "_OptionalGetUICustomizationRequestRequestTypeDef",
    {
        "ClientId": str,
    },
    total=False,
)

class GetUICustomizationRequestRequestTypeDef(
    _RequiredGetUICustomizationRequestRequestTypeDef,
    _OptionalGetUICustomizationRequestRequestTypeDef,
):
    pass

GetUICustomizationResponseTypeDef = TypedDict(
    "GetUICustomizationResponseTypeDef",
    {
        "UICustomization": "UICustomizationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUserAttributeVerificationCodeRequestRequestTypeDef = TypedDict(
    "_RequiredGetUserAttributeVerificationCodeRequestRequestTypeDef",
    {
        "AccessToken": str,
        "AttributeName": str,
    },
)
_OptionalGetUserAttributeVerificationCodeRequestRequestTypeDef = TypedDict(
    "_OptionalGetUserAttributeVerificationCodeRequestRequestTypeDef",
    {
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)

class GetUserAttributeVerificationCodeRequestRequestTypeDef(
    _RequiredGetUserAttributeVerificationCodeRequestRequestTypeDef,
    _OptionalGetUserAttributeVerificationCodeRequestRequestTypeDef,
):
    pass

GetUserAttributeVerificationCodeResponseTypeDef = TypedDict(
    "GetUserAttributeVerificationCodeResponseTypeDef",
    {
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserPoolMfaConfigRequestRequestTypeDef = TypedDict(
    "GetUserPoolMfaConfigRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)

GetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "GetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": "SmsMfaConfigTypeTypeDef",
        "SoftwareTokenMfaConfiguration": "SoftwareTokenMfaConfigTypeTypeDef",
        "MfaConfiguration": UserPoolMfaTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)

GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "Username": str,
        "UserAttributes": List["AttributeTypeTypeDef"],
        "MFAOptions": List["MFAOptionTypeTypeDef"],
        "PreferredMfaSetting": str,
        "UserMFASettingList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlobalSignOutRequestRequestTypeDef = TypedDict(
    "GlobalSignOutRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)

GroupTypeTypeDef = TypedDict(
    "GroupTypeTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

HttpHeaderTypeDef = TypedDict(
    "HttpHeaderTypeDef",
    {
        "headerName": str,
        "headerValue": str,
    },
    total=False,
)

IdentityProviderTypeTypeDef = TypedDict(
    "IdentityProviderTypeTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
        "ProviderType": IdentityProviderTypeTypeType,
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

_RequiredInitiateAuthRequestRequestTypeDef = TypedDict(
    "_RequiredInitiateAuthRequestRequestTypeDef",
    {
        "AuthFlow": AuthFlowTypeType,
        "ClientId": str,
    },
)
_OptionalInitiateAuthRequestRequestTypeDef = TypedDict(
    "_OptionalInitiateAuthRequestRequestTypeDef",
    {
        "AuthParameters": Dict[str, str],
        "ClientMetadata": Dict[str, str],
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "UserContextData": "UserContextDataTypeTypeDef",
    },
    total=False,
)

class InitiateAuthRequestRequestTypeDef(
    _RequiredInitiateAuthRequestRequestTypeDef, _OptionalInitiateAuthRequestRequestTypeDef
):
    pass

InitiateAuthResponseTypeDef = TypedDict(
    "InitiateAuthResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LambdaConfigTypeTypeDef = TypedDict(
    "LambdaConfigTypeTypeDef",
    {
        "PreSignUp": str,
        "CustomMessage": str,
        "PostConfirmation": str,
        "PreAuthentication": str,
        "PostAuthentication": str,
        "DefineAuthChallenge": str,
        "CreateAuthChallenge": str,
        "VerifyAuthChallengeResponse": str,
        "PreTokenGeneration": str,
        "UserMigration": str,
        "CustomSMSSender": "CustomSMSLambdaVersionConfigTypeTypeDef",
        "CustomEmailSender": "CustomEmailLambdaVersionConfigTypeTypeDef",
        "KMSKeyID": str,
    },
    total=False,
)

_RequiredListDevicesRequestRequestTypeDef = TypedDict(
    "_RequiredListDevicesRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)
_OptionalListDevicesRequestRequestTypeDef = TypedDict(
    "_OptionalListDevicesRequestRequestTypeDef",
    {
        "Limit": int,
        "PaginationToken": str,
    },
    total=False,
)

class ListDevicesRequestRequestTypeDef(
    _RequiredListDevicesRequestRequestTypeDef, _OptionalListDevicesRequestRequestTypeDef
):
    pass

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "Devices": List["DeviceTypeTypeDef"],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupsRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupsRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class ListGroupsRequestRequestTypeDef(
    _RequiredListGroupsRequestRequestTypeDef, _OptionalListGroupsRequestRequestTypeDef
):
    pass

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List["GroupTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "_RequiredListIdentityProvidersRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "_OptionalListIdentityProvidersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListIdentityProvidersRequestRequestTypeDef(
    _RequiredListIdentityProvidersRequestRequestTypeDef,
    _OptionalListIdentityProvidersRequestRequestTypeDef,
):
    pass

ListIdentityProvidersResponseTypeDef = TypedDict(
    "ListIdentityProvidersResponseTypeDef",
    {
        "Providers": List["ProviderDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourceServersRequestRequestTypeDef = TypedDict(
    "_RequiredListResourceServersRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListResourceServersRequestRequestTypeDef = TypedDict(
    "_OptionalListResourceServersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListResourceServersRequestRequestTypeDef(
    _RequiredListResourceServersRequestRequestTypeDef,
    _OptionalListResourceServersRequestRequestTypeDef,
):
    pass

ListResourceServersResponseTypeDef = TypedDict(
    "ListResourceServersResponseTypeDef",
    {
        "ResourceServers": List["ResourceServerTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
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

_RequiredListUserImportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListUserImportJobsRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "MaxResults": int,
    },
)
_OptionalListUserImportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListUserImportJobsRequestRequestTypeDef",
    {
        "PaginationToken": str,
    },
    total=False,
)

class ListUserImportJobsRequestRequestTypeDef(
    _RequiredListUserImportJobsRequestRequestTypeDef,
    _OptionalListUserImportJobsRequestRequestTypeDef,
):
    pass

ListUserImportJobsResponseTypeDef = TypedDict(
    "ListUserImportJobsResponseTypeDef",
    {
        "UserImportJobs": List["UserImportJobTypeTypeDef"],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserPoolClientsRequestRequestTypeDef = TypedDict(
    "_RequiredListUserPoolClientsRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListUserPoolClientsRequestRequestTypeDef = TypedDict(
    "_OptionalListUserPoolClientsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListUserPoolClientsRequestRequestTypeDef(
    _RequiredListUserPoolClientsRequestRequestTypeDef,
    _OptionalListUserPoolClientsRequestRequestTypeDef,
):
    pass

ListUserPoolClientsResponseTypeDef = TypedDict(
    "ListUserPoolClientsResponseTypeDef",
    {
        "UserPoolClients": List["UserPoolClientDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUserPoolsRequestRequestTypeDef = TypedDict(
    "_RequiredListUserPoolsRequestRequestTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalListUserPoolsRequestRequestTypeDef = TypedDict(
    "_OptionalListUserPoolsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListUserPoolsRequestRequestTypeDef(
    _RequiredListUserPoolsRequestRequestTypeDef, _OptionalListUserPoolsRequestRequestTypeDef
):
    pass

ListUserPoolsResponseTypeDef = TypedDict(
    "ListUserPoolsResponseTypeDef",
    {
        "UserPools": List["UserPoolDescriptionTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersInGroupRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersInGroupRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "GroupName": str,
    },
)
_OptionalListUsersInGroupRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersInGroupRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class ListUsersInGroupRequestRequestTypeDef(
    _RequiredListUsersInGroupRequestRequestTypeDef, _OptionalListUsersInGroupRequestRequestTypeDef
):
    pass

ListUsersInGroupResponseTypeDef = TypedDict(
    "ListUsersInGroupResponseTypeDef",
    {
        "Users": List["UserTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "AttributesToGet": List[str],
        "Limit": int,
        "PaginationToken": str,
        "Filter": str,
    },
    total=False,
)

class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List["UserTypeTypeDef"],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MFAOptionTypeTypeDef = TypedDict(
    "MFAOptionTypeTypeDef",
    {
        "DeliveryMedium": DeliveryMediumTypeType,
        "AttributeName": str,
    },
    total=False,
)

MessageTemplateTypeTypeDef = TypedDict(
    "MessageTemplateTypeTypeDef",
    {
        "SMSMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
    },
    total=False,
)

NewDeviceMetadataTypeTypeDef = TypedDict(
    "NewDeviceMetadataTypeTypeDef",
    {
        "DeviceKey": str,
        "DeviceGroupKey": str,
    },
    total=False,
)

_RequiredNotifyConfigurationTypeTypeDef = TypedDict(
    "_RequiredNotifyConfigurationTypeTypeDef",
    {
        "SourceArn": str,
    },
)
_OptionalNotifyConfigurationTypeTypeDef = TypedDict(
    "_OptionalNotifyConfigurationTypeTypeDef",
    {
        "From": str,
        "ReplyTo": str,
        "BlockEmail": "NotifyEmailTypeTypeDef",
        "NoActionEmail": "NotifyEmailTypeTypeDef",
        "MfaEmail": "NotifyEmailTypeTypeDef",
    },
    total=False,
)

class NotifyConfigurationTypeTypeDef(
    _RequiredNotifyConfigurationTypeTypeDef, _OptionalNotifyConfigurationTypeTypeDef
):
    pass

_RequiredNotifyEmailTypeTypeDef = TypedDict(
    "_RequiredNotifyEmailTypeTypeDef",
    {
        "Subject": str,
    },
)
_OptionalNotifyEmailTypeTypeDef = TypedDict(
    "_OptionalNotifyEmailTypeTypeDef",
    {
        "HtmlBody": str,
        "TextBody": str,
    },
    total=False,
)

class NotifyEmailTypeTypeDef(_RequiredNotifyEmailTypeTypeDef, _OptionalNotifyEmailTypeTypeDef):
    pass

NumberAttributeConstraintsTypeTypeDef = TypedDict(
    "NumberAttributeConstraintsTypeTypeDef",
    {
        "MinValue": str,
        "MaxValue": str,
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

PasswordPolicyTypeTypeDef = TypedDict(
    "PasswordPolicyTypeTypeDef",
    {
        "MinimumLength": int,
        "RequireUppercase": bool,
        "RequireLowercase": bool,
        "RequireNumbers": bool,
        "RequireSymbols": bool,
        "TemporaryPasswordValidityDays": int,
    },
    total=False,
)

ProviderDescriptionTypeDef = TypedDict(
    "ProviderDescriptionTypeDef",
    {
        "ProviderName": str,
        "ProviderType": IdentityProviderTypeTypeType,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

ProviderUserIdentifierTypeTypeDef = TypedDict(
    "ProviderUserIdentifierTypeTypeDef",
    {
        "ProviderName": str,
        "ProviderAttributeName": str,
        "ProviderAttributeValue": str,
    },
    total=False,
)

RecoveryOptionTypeTypeDef = TypedDict(
    "RecoveryOptionTypeTypeDef",
    {
        "Priority": int,
        "Name": RecoveryOptionNameTypeType,
    },
)

_RequiredResendConfirmationCodeRequestRequestTypeDef = TypedDict(
    "_RequiredResendConfirmationCodeRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
    },
)
_OptionalResendConfirmationCodeRequestRequestTypeDef = TypedDict(
    "_OptionalResendConfirmationCodeRequestRequestTypeDef",
    {
        "SecretHash": str,
        "UserContextData": "UserContextDataTypeTypeDef",
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)

class ResendConfirmationCodeRequestRequestTypeDef(
    _RequiredResendConfirmationCodeRequestRequestTypeDef,
    _OptionalResendConfirmationCodeRequestRequestTypeDef,
):
    pass

ResendConfirmationCodeResponseTypeDef = TypedDict(
    "ResendConfirmationCodeResponseTypeDef",
    {
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceServerScopeTypeTypeDef = TypedDict(
    "ResourceServerScopeTypeTypeDef",
    {
        "ScopeName": str,
        "ScopeDescription": str,
    },
)

ResourceServerTypeTypeDef = TypedDict(
    "ResourceServerTypeTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
        "Scopes": List["ResourceServerScopeTypeTypeDef"],
    },
    total=False,
)

_RequiredRespondToAuthChallengeRequestRequestTypeDef = TypedDict(
    "_RequiredRespondToAuthChallengeRequestRequestTypeDef",
    {
        "ClientId": str,
        "ChallengeName": ChallengeNameTypeType,
    },
)
_OptionalRespondToAuthChallengeRequestRequestTypeDef = TypedDict(
    "_OptionalRespondToAuthChallengeRequestRequestTypeDef",
    {
        "Session": str,
        "ChallengeResponses": Dict[str, str],
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "UserContextData": "UserContextDataTypeTypeDef",
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)

class RespondToAuthChallengeRequestRequestTypeDef(
    _RequiredRespondToAuthChallengeRequestRequestTypeDef,
    _OptionalRespondToAuthChallengeRequestRequestTypeDef,
):
    pass

RespondToAuthChallengeResponseTypeDef = TypedDict(
    "RespondToAuthChallengeResponseTypeDef",
    {
        "ChallengeName": ChallengeNameTypeType,
        "Session": str,
        "ChallengeParameters": Dict[str, str],
        "AuthenticationResult": "AuthenticationResultTypeTypeDef",
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

_RequiredRevokeTokenRequestRequestTypeDef = TypedDict(
    "_RequiredRevokeTokenRequestRequestTypeDef",
    {
        "Token": str,
        "ClientId": str,
    },
)
_OptionalRevokeTokenRequestRequestTypeDef = TypedDict(
    "_OptionalRevokeTokenRequestRequestTypeDef",
    {
        "ClientSecret": str,
    },
    total=False,
)

class RevokeTokenRequestRequestTypeDef(
    _RequiredRevokeTokenRequestRequestTypeDef, _OptionalRevokeTokenRequestRequestTypeDef
):
    pass

RiskConfigurationTypeTypeDef = TypedDict(
    "RiskConfigurationTypeTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "CompromisedCredentialsRiskConfiguration": "CompromisedCredentialsRiskConfigurationTypeTypeDef",
        "AccountTakeoverRiskConfiguration": "AccountTakeoverRiskConfigurationTypeTypeDef",
        "RiskExceptionConfiguration": "RiskExceptionConfigurationTypeTypeDef",
        "LastModifiedDate": datetime,
    },
    total=False,
)

RiskExceptionConfigurationTypeTypeDef = TypedDict(
    "RiskExceptionConfigurationTypeTypeDef",
    {
        "BlockedIPRangeList": List[str],
        "SkippedIPRangeList": List[str],
    },
    total=False,
)

SMSMfaSettingsTypeTypeDef = TypedDict(
    "SMSMfaSettingsTypeTypeDef",
    {
        "Enabled": bool,
        "PreferredMfa": bool,
    },
    total=False,
)

SchemaAttributeTypeTypeDef = TypedDict(
    "SchemaAttributeTypeTypeDef",
    {
        "Name": str,
        "AttributeDataType": AttributeDataTypeType,
        "DeveloperOnlyAttribute": bool,
        "Mutable": bool,
        "Required": bool,
        "NumberAttributeConstraints": "NumberAttributeConstraintsTypeTypeDef",
        "StringAttributeConstraints": "StringAttributeConstraintsTypeTypeDef",
    },
    total=False,
)

_RequiredSetRiskConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredSetRiskConfigurationRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalSetRiskConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalSetRiskConfigurationRequestRequestTypeDef",
    {
        "ClientId": str,
        "CompromisedCredentialsRiskConfiguration": "CompromisedCredentialsRiskConfigurationTypeTypeDef",
        "AccountTakeoverRiskConfiguration": "AccountTakeoverRiskConfigurationTypeTypeDef",
        "RiskExceptionConfiguration": "RiskExceptionConfigurationTypeTypeDef",
    },
    total=False,
)

class SetRiskConfigurationRequestRequestTypeDef(
    _RequiredSetRiskConfigurationRequestRequestTypeDef,
    _OptionalSetRiskConfigurationRequestRequestTypeDef,
):
    pass

SetRiskConfigurationResponseTypeDef = TypedDict(
    "SetRiskConfigurationResponseTypeDef",
    {
        "RiskConfiguration": "RiskConfigurationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSetUICustomizationRequestRequestTypeDef = TypedDict(
    "_RequiredSetUICustomizationRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalSetUICustomizationRequestRequestTypeDef = TypedDict(
    "_OptionalSetUICustomizationRequestRequestTypeDef",
    {
        "ClientId": str,
        "CSS": str,
        "ImageFile": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

class SetUICustomizationRequestRequestTypeDef(
    _RequiredSetUICustomizationRequestRequestTypeDef,
    _OptionalSetUICustomizationRequestRequestTypeDef,
):
    pass

SetUICustomizationResponseTypeDef = TypedDict(
    "SetUICustomizationResponseTypeDef",
    {
        "UICustomization": "UICustomizationTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSetUserMFAPreferenceRequestRequestTypeDef = TypedDict(
    "_RequiredSetUserMFAPreferenceRequestRequestTypeDef",
    {
        "AccessToken": str,
    },
)
_OptionalSetUserMFAPreferenceRequestRequestTypeDef = TypedDict(
    "_OptionalSetUserMFAPreferenceRequestRequestTypeDef",
    {
        "SMSMfaSettings": "SMSMfaSettingsTypeTypeDef",
        "SoftwareTokenMfaSettings": "SoftwareTokenMfaSettingsTypeTypeDef",
    },
    total=False,
)

class SetUserMFAPreferenceRequestRequestTypeDef(
    _RequiredSetUserMFAPreferenceRequestRequestTypeDef,
    _OptionalSetUserMFAPreferenceRequestRequestTypeDef,
):
    pass

_RequiredSetUserPoolMfaConfigRequestRequestTypeDef = TypedDict(
    "_RequiredSetUserPoolMfaConfigRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalSetUserPoolMfaConfigRequestRequestTypeDef = TypedDict(
    "_OptionalSetUserPoolMfaConfigRequestRequestTypeDef",
    {
        "SmsMfaConfiguration": "SmsMfaConfigTypeTypeDef",
        "SoftwareTokenMfaConfiguration": "SoftwareTokenMfaConfigTypeTypeDef",
        "MfaConfiguration": UserPoolMfaTypeType,
    },
    total=False,
)

class SetUserPoolMfaConfigRequestRequestTypeDef(
    _RequiredSetUserPoolMfaConfigRequestRequestTypeDef,
    _OptionalSetUserPoolMfaConfigRequestRequestTypeDef,
):
    pass

SetUserPoolMfaConfigResponseTypeDef = TypedDict(
    "SetUserPoolMfaConfigResponseTypeDef",
    {
        "SmsMfaConfiguration": "SmsMfaConfigTypeTypeDef",
        "SoftwareTokenMfaConfiguration": "SoftwareTokenMfaConfigTypeTypeDef",
        "MfaConfiguration": UserPoolMfaTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetUserSettingsRequestRequestTypeDef = TypedDict(
    "SetUserSettingsRequestRequestTypeDef",
    {
        "AccessToken": str,
        "MFAOptions": List["MFAOptionTypeTypeDef"],
    },
)

_RequiredSignUpRequestRequestTypeDef = TypedDict(
    "_RequiredSignUpRequestRequestTypeDef",
    {
        "ClientId": str,
        "Username": str,
        "Password": str,
    },
)
_OptionalSignUpRequestRequestTypeDef = TypedDict(
    "_OptionalSignUpRequestRequestTypeDef",
    {
        "SecretHash": str,
        "UserAttributes": List["AttributeTypeTypeDef"],
        "ValidationData": List["AttributeTypeTypeDef"],
        "AnalyticsMetadata": "AnalyticsMetadataTypeTypeDef",
        "UserContextData": "UserContextDataTypeTypeDef",
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)

class SignUpRequestRequestTypeDef(
    _RequiredSignUpRequestRequestTypeDef, _OptionalSignUpRequestRequestTypeDef
):
    pass

SignUpResponseTypeDef = TypedDict(
    "SignUpResponseTypeDef",
    {
        "UserConfirmed": bool,
        "CodeDeliveryDetails": "CodeDeliveryDetailsTypeTypeDef",
        "UserSub": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSmsConfigurationTypeTypeDef = TypedDict(
    "_RequiredSmsConfigurationTypeTypeDef",
    {
        "SnsCallerArn": str,
    },
)
_OptionalSmsConfigurationTypeTypeDef = TypedDict(
    "_OptionalSmsConfigurationTypeTypeDef",
    {
        "ExternalId": str,
    },
    total=False,
)

class SmsConfigurationTypeTypeDef(
    _RequiredSmsConfigurationTypeTypeDef, _OptionalSmsConfigurationTypeTypeDef
):
    pass

SmsMfaConfigTypeTypeDef = TypedDict(
    "SmsMfaConfigTypeTypeDef",
    {
        "SmsAuthenticationMessage": str,
        "SmsConfiguration": "SmsConfigurationTypeTypeDef",
    },
    total=False,
)

SoftwareTokenMfaConfigTypeTypeDef = TypedDict(
    "SoftwareTokenMfaConfigTypeTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

SoftwareTokenMfaSettingsTypeTypeDef = TypedDict(
    "SoftwareTokenMfaSettingsTypeTypeDef",
    {
        "Enabled": bool,
        "PreferredMfa": bool,
    },
    total=False,
)

StartUserImportJobRequestRequestTypeDef = TypedDict(
    "StartUserImportJobRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "JobId": str,
    },
)

StartUserImportJobResponseTypeDef = TypedDict(
    "StartUserImportJobResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopUserImportJobRequestRequestTypeDef = TypedDict(
    "StopUserImportJobRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "JobId": str,
    },
)

StopUserImportJobResponseTypeDef = TypedDict(
    "StopUserImportJobResponseTypeDef",
    {
        "UserImportJob": "UserImportJobTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StringAttributeConstraintsTypeTypeDef = TypedDict(
    "StringAttributeConstraintsTypeTypeDef",
    {
        "MinLength": str,
        "MaxLength": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TokenValidityUnitsTypeTypeDef = TypedDict(
    "TokenValidityUnitsTypeTypeDef",
    {
        "AccessToken": TimeUnitsTypeType,
        "IdToken": TimeUnitsTypeType,
        "RefreshToken": TimeUnitsTypeType,
    },
    total=False,
)

UICustomizationTypeTypeDef = TypedDict(
    "UICustomizationTypeTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
        "ImageUrl": str,
        "CSS": str,
        "CSSVersion": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateAuthEventFeedbackRequestRequestTypeDef = TypedDict(
    "UpdateAuthEventFeedbackRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Username": str,
        "EventId": str,
        "FeedbackToken": str,
        "FeedbackValue": FeedbackValueTypeType,
    },
)

_RequiredUpdateDeviceStatusRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceStatusRequestRequestTypeDef",
    {
        "AccessToken": str,
        "DeviceKey": str,
    },
)
_OptionalUpdateDeviceStatusRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceStatusRequestRequestTypeDef",
    {
        "DeviceRememberedStatus": DeviceRememberedStatusTypeType,
    },
    total=False,
)

class UpdateDeviceStatusRequestRequestTypeDef(
    _RequiredUpdateDeviceStatusRequestRequestTypeDef,
    _OptionalUpdateDeviceStatusRequestRequestTypeDef,
):
    pass

_RequiredUpdateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserPoolId": str,
    },
)
_OptionalUpdateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGroupRequestRequestTypeDef",
    {
        "Description": str,
        "RoleArn": str,
        "Precedence": int,
    },
    total=False,
)

class UpdateGroupRequestRequestTypeDef(
    _RequiredUpdateGroupRequestRequestTypeDef, _OptionalUpdateGroupRequestRequestTypeDef
):
    pass

UpdateGroupResponseTypeDef = TypedDict(
    "UpdateGroupResponseTypeDef",
    {
        "Group": "GroupTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIdentityProviderRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ProviderName": str,
    },
)
_OptionalUpdateIdentityProviderRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIdentityProviderRequestRequestTypeDef",
    {
        "ProviderDetails": Dict[str, str],
        "AttributeMapping": Dict[str, str],
        "IdpIdentifiers": List[str],
    },
    total=False,
)

class UpdateIdentityProviderRequestRequestTypeDef(
    _RequiredUpdateIdentityProviderRequestRequestTypeDef,
    _OptionalUpdateIdentityProviderRequestRequestTypeDef,
):
    pass

UpdateIdentityProviderResponseTypeDef = TypedDict(
    "UpdateIdentityProviderResponseTypeDef",
    {
        "IdentityProvider": "IdentityProviderTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateResourceServerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceServerRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "Identifier": str,
        "Name": str,
    },
)
_OptionalUpdateResourceServerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceServerRequestRequestTypeDef",
    {
        "Scopes": List["ResourceServerScopeTypeTypeDef"],
    },
    total=False,
)

class UpdateResourceServerRequestRequestTypeDef(
    _RequiredUpdateResourceServerRequestRequestTypeDef,
    _OptionalUpdateResourceServerRequestRequestTypeDef,
):
    pass

UpdateResourceServerResponseTypeDef = TypedDict(
    "UpdateResourceServerResponseTypeDef",
    {
        "ResourceServer": "ResourceServerTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserAttributesRequestRequestTypeDef",
    {
        "UserAttributes": List["AttributeTypeTypeDef"],
        "AccessToken": str,
    },
)
_OptionalUpdateUserAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserAttributesRequestRequestTypeDef",
    {
        "ClientMetadata": Dict[str, str],
    },
    total=False,
)

class UpdateUserAttributesRequestRequestTypeDef(
    _RequiredUpdateUserAttributesRequestRequestTypeDef,
    _OptionalUpdateUserAttributesRequestRequestTypeDef,
):
    pass

UpdateUserAttributesResponseTypeDef = TypedDict(
    "UpdateUserAttributesResponseTypeDef",
    {
        "CodeDeliveryDetailsList": List["CodeDeliveryDetailsTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserPoolClientRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserPoolClientRequestRequestTypeDef",
    {
        "UserPoolId": str,
        "ClientId": str,
    },
)
_OptionalUpdateUserPoolClientRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserPoolClientRequestRequestTypeDef",
    {
        "ClientName": str,
        "RefreshTokenValidity": int,
        "AccessTokenValidity": int,
        "IdTokenValidity": int,
        "TokenValidityUnits": "TokenValidityUnitsTypeTypeDef",
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[ExplicitAuthFlowsTypeType],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[OAuthFlowTypeType],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": "AnalyticsConfigurationTypeTypeDef",
        "PreventUserExistenceErrors": PreventUserExistenceErrorTypesType,
        "EnableTokenRevocation": bool,
    },
    total=False,
)

class UpdateUserPoolClientRequestRequestTypeDef(
    _RequiredUpdateUserPoolClientRequestRequestTypeDef,
    _OptionalUpdateUserPoolClientRequestRequestTypeDef,
):
    pass

UpdateUserPoolClientResponseTypeDef = TypedDict(
    "UpdateUserPoolClientResponseTypeDef",
    {
        "UserPoolClient": "UserPoolClientTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserPoolDomainRequestRequestTypeDef = TypedDict(
    "UpdateUserPoolDomainRequestRequestTypeDef",
    {
        "Domain": str,
        "UserPoolId": str,
        "CustomDomainConfig": "CustomDomainConfigTypeTypeDef",
    },
)

UpdateUserPoolDomainResponseTypeDef = TypedDict(
    "UpdateUserPoolDomainResponseTypeDef",
    {
        "CloudFrontDomain": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserPoolRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserPoolRequestRequestTypeDef",
    {
        "UserPoolId": str,
    },
)
_OptionalUpdateUserPoolRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserPoolRequestRequestTypeDef",
    {
        "Policies": "UserPoolPolicyTypeTypeDef",
        "LambdaConfig": "LambdaConfigTypeTypeDef",
        "AutoVerifiedAttributes": List[VerifiedAttributeTypeType],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": "VerificationMessageTemplateTypeTypeDef",
        "SmsAuthenticationMessage": str,
        "MfaConfiguration": UserPoolMfaTypeType,
        "DeviceConfiguration": "DeviceConfigurationTypeTypeDef",
        "EmailConfiguration": "EmailConfigurationTypeTypeDef",
        "SmsConfiguration": "SmsConfigurationTypeTypeDef",
        "UserPoolTags": Dict[str, str],
        "AdminCreateUserConfig": "AdminCreateUserConfigTypeTypeDef",
        "UserPoolAddOns": "UserPoolAddOnsTypeTypeDef",
        "AccountRecoverySetting": "AccountRecoverySettingTypeTypeDef",
    },
    total=False,
)

class UpdateUserPoolRequestRequestTypeDef(
    _RequiredUpdateUserPoolRequestRequestTypeDef, _OptionalUpdateUserPoolRequestRequestTypeDef
):
    pass

UserContextDataTypeTypeDef = TypedDict(
    "UserContextDataTypeTypeDef",
    {
        "EncodedData": str,
    },
    total=False,
)

UserImportJobTypeTypeDef = TypedDict(
    "UserImportJobTypeTypeDef",
    {
        "JobName": str,
        "JobId": str,
        "UserPoolId": str,
        "PreSignedUrl": str,
        "CreationDate": datetime,
        "StartDate": datetime,
        "CompletionDate": datetime,
        "Status": UserImportJobStatusTypeType,
        "CloudWatchLogsRoleArn": str,
        "ImportedUsers": int,
        "SkippedUsers": int,
        "FailedUsers": int,
        "CompletionMessage": str,
    },
    total=False,
)

UserPoolAddOnsTypeTypeDef = TypedDict(
    "UserPoolAddOnsTypeTypeDef",
    {
        "AdvancedSecurityMode": AdvancedSecurityModeTypeType,
    },
)

UserPoolClientDescriptionTypeDef = TypedDict(
    "UserPoolClientDescriptionTypeDef",
    {
        "ClientId": str,
        "UserPoolId": str,
        "ClientName": str,
    },
    total=False,
)

UserPoolClientTypeTypeDef = TypedDict(
    "UserPoolClientTypeTypeDef",
    {
        "UserPoolId": str,
        "ClientName": str,
        "ClientId": str,
        "ClientSecret": str,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "RefreshTokenValidity": int,
        "AccessTokenValidity": int,
        "IdTokenValidity": int,
        "TokenValidityUnits": "TokenValidityUnitsTypeTypeDef",
        "ReadAttributes": List[str],
        "WriteAttributes": List[str],
        "ExplicitAuthFlows": List[ExplicitAuthFlowsTypeType],
        "SupportedIdentityProviders": List[str],
        "CallbackURLs": List[str],
        "LogoutURLs": List[str],
        "DefaultRedirectURI": str,
        "AllowedOAuthFlows": List[OAuthFlowTypeType],
        "AllowedOAuthScopes": List[str],
        "AllowedOAuthFlowsUserPoolClient": bool,
        "AnalyticsConfiguration": "AnalyticsConfigurationTypeTypeDef",
        "PreventUserExistenceErrors": PreventUserExistenceErrorTypesType,
        "EnableTokenRevocation": bool,
    },
    total=False,
)

UserPoolDescriptionTypeTypeDef = TypedDict(
    "UserPoolDescriptionTypeTypeDef",
    {
        "Id": str,
        "Name": str,
        "LambdaConfig": "LambdaConfigTypeTypeDef",
        "Status": StatusTypeType,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
    },
    total=False,
)

UserPoolPolicyTypeTypeDef = TypedDict(
    "UserPoolPolicyTypeTypeDef",
    {
        "PasswordPolicy": "PasswordPolicyTypeTypeDef",
    },
    total=False,
)

UserPoolTypeTypeDef = TypedDict(
    "UserPoolTypeTypeDef",
    {
        "Id": str,
        "Name": str,
        "Policies": "UserPoolPolicyTypeTypeDef",
        "LambdaConfig": "LambdaConfigTypeTypeDef",
        "Status": StatusTypeType,
        "LastModifiedDate": datetime,
        "CreationDate": datetime,
        "SchemaAttributes": List["SchemaAttributeTypeTypeDef"],
        "AutoVerifiedAttributes": List[VerifiedAttributeTypeType],
        "AliasAttributes": List[AliasAttributeTypeType],
        "UsernameAttributes": List[UsernameAttributeTypeType],
        "SmsVerificationMessage": str,
        "EmailVerificationMessage": str,
        "EmailVerificationSubject": str,
        "VerificationMessageTemplate": "VerificationMessageTemplateTypeTypeDef",
        "SmsAuthenticationMessage": str,
        "MfaConfiguration": UserPoolMfaTypeType,
        "DeviceConfiguration": "DeviceConfigurationTypeTypeDef",
        "EstimatedNumberOfUsers": int,
        "EmailConfiguration": "EmailConfigurationTypeTypeDef",
        "SmsConfiguration": "SmsConfigurationTypeTypeDef",
        "UserPoolTags": Dict[str, str],
        "SmsConfigurationFailure": str,
        "EmailConfigurationFailure": str,
        "Domain": str,
        "CustomDomain": str,
        "AdminCreateUserConfig": "AdminCreateUserConfigTypeTypeDef",
        "UserPoolAddOns": "UserPoolAddOnsTypeTypeDef",
        "UsernameConfiguration": "UsernameConfigurationTypeTypeDef",
        "Arn": str,
        "AccountRecoverySetting": "AccountRecoverySettingTypeTypeDef",
    },
    total=False,
)

UserTypeTypeDef = TypedDict(
    "UserTypeTypeDef",
    {
        "Username": str,
        "Attributes": List["AttributeTypeTypeDef"],
        "UserCreateDate": datetime,
        "UserLastModifiedDate": datetime,
        "Enabled": bool,
        "UserStatus": UserStatusTypeType,
        "MFAOptions": List["MFAOptionTypeTypeDef"],
    },
    total=False,
)

UsernameConfigurationTypeTypeDef = TypedDict(
    "UsernameConfigurationTypeTypeDef",
    {
        "CaseSensitive": bool,
    },
)

VerificationMessageTemplateTypeTypeDef = TypedDict(
    "VerificationMessageTemplateTypeTypeDef",
    {
        "SmsMessage": str,
        "EmailMessage": str,
        "EmailSubject": str,
        "EmailMessageByLink": str,
        "EmailSubjectByLink": str,
        "DefaultEmailOption": DefaultEmailOptionTypeType,
    },
    total=False,
)

_RequiredVerifySoftwareTokenRequestRequestTypeDef = TypedDict(
    "_RequiredVerifySoftwareTokenRequestRequestTypeDef",
    {
        "UserCode": str,
    },
)
_OptionalVerifySoftwareTokenRequestRequestTypeDef = TypedDict(
    "_OptionalVerifySoftwareTokenRequestRequestTypeDef",
    {
        "AccessToken": str,
        "Session": str,
        "FriendlyDeviceName": str,
    },
    total=False,
)

class VerifySoftwareTokenRequestRequestTypeDef(
    _RequiredVerifySoftwareTokenRequestRequestTypeDef,
    _OptionalVerifySoftwareTokenRequestRequestTypeDef,
):
    pass

VerifySoftwareTokenResponseTypeDef = TypedDict(
    "VerifySoftwareTokenResponseTypeDef",
    {
        "Status": VerifySoftwareTokenResponseTypeType,
        "Session": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifyUserAttributeRequestRequestTypeDef = TypedDict(
    "VerifyUserAttributeRequestRequestTypeDef",
    {
        "AccessToken": str,
        "AttributeName": str,
        "Code": str,
    },
)
