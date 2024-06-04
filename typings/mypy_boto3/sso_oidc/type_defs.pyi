"""
Type annotations for sso-oidc service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sso_oidc.type_defs import CreateTokenRequestRequestTypeDef

    data: CreateTokenRequestRequestTypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateTokenRequestRequestTypeDef",
    "CreateTokenResponseTypeDef",
    "CreateTokenWithIAMRequestRequestTypeDef",
    "CreateTokenWithIAMResponseTypeDef",
    "RegisterClientRequestRequestTypeDef",
    "RegisterClientResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartDeviceAuthorizationRequestRequestTypeDef",
    "StartDeviceAuthorizationResponseTypeDef",
)

_RequiredCreateTokenRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTokenRequestRequestTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "grantType": str,
    },
)
_OptionalCreateTokenRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTokenRequestRequestTypeDef",
    {
        "deviceCode": str,
        "code": str,
        "refreshToken": str,
        "scope": List[str],
        "redirectUri": str,
        "codeVerifier": str,
    },
    total=False,
)

class CreateTokenRequestRequestTypeDef(
    _RequiredCreateTokenRequestRequestTypeDef, _OptionalCreateTokenRequestRequestTypeDef
):
    pass

CreateTokenResponseTypeDef = TypedDict(
    "CreateTokenResponseTypeDef",
    {
        "accessToken": str,
        "tokenType": str,
        "expiresIn": int,
        "refreshToken": str,
        "idToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTokenWithIAMRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTokenWithIAMRequestRequestTypeDef",
    {
        "clientId": str,
        "grantType": str,
    },
)
_OptionalCreateTokenWithIAMRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTokenWithIAMRequestRequestTypeDef",
    {
        "code": str,
        "refreshToken": str,
        "assertion": str,
        "scope": List[str],
        "redirectUri": str,
        "subjectToken": str,
        "subjectTokenType": str,
        "requestedTokenType": str,
        "codeVerifier": str,
    },
    total=False,
)

class CreateTokenWithIAMRequestRequestTypeDef(
    _RequiredCreateTokenWithIAMRequestRequestTypeDef,
    _OptionalCreateTokenWithIAMRequestRequestTypeDef,
):
    pass

CreateTokenWithIAMResponseTypeDef = TypedDict(
    "CreateTokenWithIAMResponseTypeDef",
    {
        "accessToken": str,
        "tokenType": str,
        "expiresIn": int,
        "refreshToken": str,
        "idToken": str,
        "issuedTokenType": str,
        "scope": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterClientRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterClientRequestRequestTypeDef",
    {
        "clientName": str,
        "clientType": str,
    },
)
_OptionalRegisterClientRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterClientRequestRequestTypeDef",
    {
        "scopes": List[str],
        "redirectUris": List[str],
        "grantTypes": List[str],
        "issuerUrl": str,
        "entitledApplicationArn": str,
    },
    total=False,
)

class RegisterClientRequestRequestTypeDef(
    _RequiredRegisterClientRequestRequestTypeDef, _OptionalRegisterClientRequestRequestTypeDef
):
    pass

RegisterClientResponseTypeDef = TypedDict(
    "RegisterClientResponseTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "clientIdIssuedAt": int,
        "clientSecretExpiresAt": int,
        "authorizationEndpoint": str,
        "tokenEndpoint": str,
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

StartDeviceAuthorizationRequestRequestTypeDef = TypedDict(
    "StartDeviceAuthorizationRequestRequestTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "startUrl": str,
    },
)

StartDeviceAuthorizationResponseTypeDef = TypedDict(
    "StartDeviceAuthorizationResponseTypeDef",
    {
        "deviceCode": str,
        "userCode": str,
        "verificationUri": str,
        "verificationUriComplete": str,
        "expiresIn": int,
        "interval": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
