"""
Type annotations for workspaces-web service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/literals.html)

Usage::

    ```python
    from mypy_boto3_workspaces_web.literals import AuthenticationTypeType

    data: AuthenticationTypeType = "IAM_Identity_Center"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AuthenticationTypeType",
    "BrowserTypeType",
    "EnabledTypeType",
    "IdentityProviderTypeType",
    "InstanceTypeType",
    "PortalStatusType",
    "RendererTypeType",
)

AuthenticationTypeType = Literal["IAM_Identity_Center", "Standard"]
BrowserTypeType = Literal["Chrome"]
EnabledTypeType = Literal["Disabled", "Enabled"]
IdentityProviderTypeType = Literal[
    "Facebook", "Google", "LoginWithAmazon", "OIDC", "SAML", "SignInWithApple"
]
InstanceTypeType = Literal["standard.large", "standard.regular", "standard.xlarge"]
PortalStatusType = Literal["Active", "Incomplete", "Pending"]
RendererTypeType = Literal["AppStream"]
