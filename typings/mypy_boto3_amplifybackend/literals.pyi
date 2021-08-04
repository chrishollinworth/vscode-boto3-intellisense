"""
Type annotations for amplifybackend service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/literals.html)

Usage::

    ```python
    from mypy_boto3_amplifybackend.literals import AdditionalConstraintsElementType

    data: AdditionalConstraintsElementType = "REQUIRE_DIGIT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AdditionalConstraintsElementType",
    "AuthResourcesType",
    "DeliveryMethodType",
    "ListBackendJobsPaginatorName",
    "MFAModeType",
    "MfaTypesElementType",
    "ModeType",
    "OAuthGrantTypeType",
    "OAuthScopesElementType",
    "RequiredSignUpAttributesElementType",
    "ResolutionStrategyType",
    "ServiceType",
    "SignInMethodType",
    "StatusType",
)

AdditionalConstraintsElementType = Literal[
    "REQUIRE_DIGIT", "REQUIRE_LOWERCASE", "REQUIRE_SYMBOL", "REQUIRE_UPPERCASE"
]
AuthResourcesType = Literal["IDENTITY_POOL_AND_USER_POOL", "USER_POOL_ONLY"]
DeliveryMethodType = Literal["EMAIL", "SMS"]
ListBackendJobsPaginatorName = Literal["list_backend_jobs"]
MFAModeType = Literal["OFF", "ON", "OPTIONAL"]
MfaTypesElementType = Literal["SMS", "TOTP"]
ModeType = Literal["AMAZON_COGNITO_USER_POOLS", "API_KEY", "AWS_IAM", "OPENID_CONNECT"]
OAuthGrantTypeType = Literal["CODE", "IMPLICIT"]
OAuthScopesElementType = Literal[
    "AWS_COGNITO_SIGNIN_USER_ADMIN", "EMAIL", "OPENID", "PHONE", "PROFILE"
]
RequiredSignUpAttributesElementType = Literal[
    "ADDRESS",
    "BIRTHDATE",
    "EMAIL",
    "FAMILY_NAME",
    "GENDER",
    "GIVEN_NAME",
    "LOCALE",
    "MIDDLE_NAME",
    "NAME",
    "NICKNAME",
    "PHONE_NUMBER",
    "PICTURE",
    "PREFERRED_USERNAME",
    "PROFILE",
    "UPDATED_AT",
    "WEBSITE",
    "ZONE_INFO",
]
ResolutionStrategyType = Literal["AUTOMERGE", "LAMBDA", "NONE", "OPTIMISTIC_CONCURRENCY"]
ServiceType = Literal["COGNITO"]
SignInMethodType = Literal["EMAIL", "EMAIL_AND_PHONE_NUMBER", "PHONE_NUMBER", "USERNAME"]
StatusType = Literal["LATEST", "STALE"]
