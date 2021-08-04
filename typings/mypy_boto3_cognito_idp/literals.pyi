"""
Type annotations for cognito-idp service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/literals.html)

Usage::

    ```python
    from mypy_boto3_cognito_idp.literals import AccountTakeoverEventActionTypeType

    data: AccountTakeoverEventActionTypeType = "BLOCK"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccountTakeoverEventActionTypeType",
    "AdminListGroupsForUserPaginatorName",
    "AdminListUserAuthEventsPaginatorName",
    "AdvancedSecurityModeTypeType",
    "AliasAttributeTypeType",
    "AttributeDataTypeType",
    "AuthFlowTypeType",
    "ChallengeNameType",
    "ChallengeNameTypeType",
    "ChallengeResponseType",
    "CompromisedCredentialsEventActionTypeType",
    "CustomEmailSenderLambdaVersionTypeType",
    "CustomSMSSenderLambdaVersionTypeType",
    "DefaultEmailOptionTypeType",
    "DeliveryMediumTypeType",
    "DeviceRememberedStatusTypeType",
    "DomainStatusTypeType",
    "EmailSendingAccountTypeType",
    "EventFilterTypeType",
    "EventResponseTypeType",
    "EventTypeType",
    "ExplicitAuthFlowsTypeType",
    "FeedbackValueTypeType",
    "IdentityProviderTypeTypeType",
    "ListGroupsPaginatorName",
    "ListIdentityProvidersPaginatorName",
    "ListResourceServersPaginatorName",
    "ListUserPoolClientsPaginatorName",
    "ListUserPoolsPaginatorName",
    "ListUsersInGroupPaginatorName",
    "ListUsersPaginatorName",
    "MessageActionTypeType",
    "OAuthFlowTypeType",
    "PreventUserExistenceErrorTypesType",
    "RecoveryOptionNameTypeType",
    "RiskDecisionTypeType",
    "RiskLevelTypeType",
    "StatusTypeType",
    "TimeUnitsTypeType",
    "UserImportJobStatusTypeType",
    "UserPoolMfaTypeType",
    "UserStatusTypeType",
    "UsernameAttributeTypeType",
    "VerifiedAttributeTypeType",
    "VerifySoftwareTokenResponseTypeType",
)

AccountTakeoverEventActionTypeType = Literal[
    "BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"
]
AdminListGroupsForUserPaginatorName = Literal["admin_list_groups_for_user"]
AdminListUserAuthEventsPaginatorName = Literal["admin_list_user_auth_events"]
AdvancedSecurityModeTypeType = Literal["AUDIT", "ENFORCED", "OFF"]
AliasAttributeTypeType = Literal["email", "phone_number", "preferred_username"]
AttributeDataTypeType = Literal["Boolean", "DateTime", "Number", "String"]
AuthFlowTypeType = Literal[
    "ADMIN_NO_SRP_AUTH",
    "ADMIN_USER_PASSWORD_AUTH",
    "CUSTOM_AUTH",
    "REFRESH_TOKEN",
    "REFRESH_TOKEN_AUTH",
    "USER_PASSWORD_AUTH",
    "USER_SRP_AUTH",
]
ChallengeNameType = Literal["Mfa", "Password"]
ChallengeNameTypeType = Literal[
    "ADMIN_NO_SRP_AUTH",
    "CUSTOM_CHALLENGE",
    "DEVICE_PASSWORD_VERIFIER",
    "DEVICE_SRP_AUTH",
    "MFA_SETUP",
    "NEW_PASSWORD_REQUIRED",
    "PASSWORD_VERIFIER",
    "SELECT_MFA_TYPE",
    "SMS_MFA",
    "SOFTWARE_TOKEN_MFA",
]
ChallengeResponseType = Literal["Failure", "Success"]
CompromisedCredentialsEventActionTypeType = Literal["BLOCK", "NO_ACTION"]
CustomEmailSenderLambdaVersionTypeType = Literal["V1_0"]
CustomSMSSenderLambdaVersionTypeType = Literal["V1_0"]
DefaultEmailOptionTypeType = Literal["CONFIRM_WITH_CODE", "CONFIRM_WITH_LINK"]
DeliveryMediumTypeType = Literal["EMAIL", "SMS"]
DeviceRememberedStatusTypeType = Literal["not_remembered", "remembered"]
DomainStatusTypeType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
EmailSendingAccountTypeType = Literal["COGNITO_DEFAULT", "DEVELOPER"]
EventFilterTypeType = Literal["PASSWORD_CHANGE", "SIGN_IN", "SIGN_UP"]
EventResponseTypeType = Literal["Failure", "Success"]
EventTypeType = Literal["ForgotPassword", "SignIn", "SignUp"]
ExplicitAuthFlowsTypeType = Literal[
    "ADMIN_NO_SRP_AUTH",
    "ALLOW_ADMIN_USER_PASSWORD_AUTH",
    "ALLOW_CUSTOM_AUTH",
    "ALLOW_REFRESH_TOKEN_AUTH",
    "ALLOW_USER_PASSWORD_AUTH",
    "ALLOW_USER_SRP_AUTH",
    "CUSTOM_AUTH_FLOW_ONLY",
    "USER_PASSWORD_AUTH",
]
FeedbackValueTypeType = Literal["Invalid", "Valid"]
IdentityProviderTypeTypeType = Literal[
    "Facebook", "Google", "LoginWithAmazon", "OIDC", "SAML", "SignInWithApple"
]
ListGroupsPaginatorName = Literal["list_groups"]
ListIdentityProvidersPaginatorName = Literal["list_identity_providers"]
ListResourceServersPaginatorName = Literal["list_resource_servers"]
ListUserPoolClientsPaginatorName = Literal["list_user_pool_clients"]
ListUserPoolsPaginatorName = Literal["list_user_pools"]
ListUsersInGroupPaginatorName = Literal["list_users_in_group"]
ListUsersPaginatorName = Literal["list_users"]
MessageActionTypeType = Literal["RESEND", "SUPPRESS"]
OAuthFlowTypeType = Literal["client_credentials", "code", "implicit"]
PreventUserExistenceErrorTypesType = Literal["ENABLED", "LEGACY"]
RecoveryOptionNameTypeType = Literal["admin_only", "verified_email", "verified_phone_number"]
RiskDecisionTypeType = Literal["AccountTakeover", "Block", "NoRisk"]
RiskLevelTypeType = Literal["High", "Low", "Medium"]
StatusTypeType = Literal["Disabled", "Enabled"]
TimeUnitsTypeType = Literal["days", "hours", "minutes", "seconds"]
UserImportJobStatusTypeType = Literal[
    "Created", "Expired", "Failed", "InProgress", "Pending", "Stopped", "Stopping", "Succeeded"
]
UserPoolMfaTypeType = Literal["OFF", "ON", "OPTIONAL"]
UserStatusTypeType = Literal[
    "ARCHIVED",
    "COMPROMISED",
    "CONFIRMED",
    "FORCE_CHANGE_PASSWORD",
    "RESET_REQUIRED",
    "UNCONFIRMED",
    "UNKNOWN",
]
UsernameAttributeTypeType = Literal["email", "phone_number"]
VerifiedAttributeTypeType = Literal["email", "phone_number"]
VerifySoftwareTokenResponseTypeType = Literal["ERROR", "SUCCESS"]
