"""
Type annotations for sso-oidc service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_sso_oidc.type_defs import AwsAdditionalDetailsTypeDef

    data: AwsAdditionalDetailsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AwsAdditionalDetailsTypeDef",
    "CreateTokenRequestTypeDef",
    "CreateTokenResponseTypeDef",
    "CreateTokenWithIAMRequestTypeDef",
    "CreateTokenWithIAMResponseTypeDef",
    "RegisterClientRequestTypeDef",
    "RegisterClientResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartDeviceAuthorizationRequestTypeDef",
    "StartDeviceAuthorizationResponseTypeDef",
)

class AwsAdditionalDetailsTypeDef(TypedDict):
    identityContext: NotRequired[str]

class CreateTokenRequestTypeDef(TypedDict):
    clientId: str
    clientSecret: str
    grantType: str
    deviceCode: NotRequired[str]
    code: NotRequired[str]
    refreshToken: NotRequired[str]
    scope: NotRequired[Sequence[str]]
    redirectUri: NotRequired[str]
    codeVerifier: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateTokenWithIAMRequestTypeDef(TypedDict):
    clientId: str
    grantType: str
    code: NotRequired[str]
    refreshToken: NotRequired[str]
    assertion: NotRequired[str]
    scope: NotRequired[Sequence[str]]
    redirectUri: NotRequired[str]
    subjectToken: NotRequired[str]
    subjectTokenType: NotRequired[str]
    requestedTokenType: NotRequired[str]
    codeVerifier: NotRequired[str]

class RegisterClientRequestTypeDef(TypedDict):
    clientName: str
    clientType: str
    scopes: NotRequired[Sequence[str]]
    redirectUris: NotRequired[Sequence[str]]
    grantTypes: NotRequired[Sequence[str]]
    issuerUrl: NotRequired[str]
    entitledApplicationArn: NotRequired[str]

class StartDeviceAuthorizationRequestTypeDef(TypedDict):
    clientId: str
    clientSecret: str
    startUrl: str

class CreateTokenResponseTypeDef(TypedDict):
    accessToken: str
    tokenType: str
    expiresIn: int
    refreshToken: str
    idToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTokenWithIAMResponseTypeDef(TypedDict):
    accessToken: str
    tokenType: str
    expiresIn: int
    refreshToken: str
    idToken: str
    issuedTokenType: str
    scope: List[str]
    awsAdditionalDetails: AwsAdditionalDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterClientResponseTypeDef(TypedDict):
    clientId: str
    clientSecret: str
    clientIdIssuedAt: int
    clientSecretExpiresAt: int
    authorizationEndpoint: str
    tokenEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDeviceAuthorizationResponseTypeDef(TypedDict):
    deviceCode: str
    userCode: str
    verificationUri: str
    verificationUriComplete: str
    expiresIn: int
    interval: int
    ResponseMetadata: ResponseMetadataTypeDef
