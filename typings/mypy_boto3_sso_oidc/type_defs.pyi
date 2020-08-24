"""
Main interface for sso-oidc service type definitions.

Usage::

    ```python
    from mypy_boto3_sso_oidc.type_defs import CreateTokenResponseTypeDef

    data: CreateTokenResponseTypeDef = {...}
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateTokenResponseTypeDef",
    "RegisterClientResponseTypeDef",
    "StartDeviceAuthorizationResponseTypeDef",
)

CreateTokenResponseTypeDef = TypedDict(
    "CreateTokenResponseTypeDef",
    {"accessToken": str, "tokenType": str, "expiresIn": int, "refreshToken": str, "idToken": str},
    total=False,
)

RegisterClientResponseTypeDef = TypedDict(
    "RegisterClientResponseTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "clientIdIssuedAt": int,
        "clientSecretExpiresAt": int,
        "authorizationEndpoint": str,
        "tokenEndpoint": str,
    },
    total=False,
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
    },
    total=False,
)
