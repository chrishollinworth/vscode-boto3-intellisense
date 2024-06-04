"""
Type annotations for verifiedpermissions service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/literals.html)

Usage::

    ```python
    from mypy_boto3_verifiedpermissions.literals import DecisionType

    data: DecisionType = "ALLOW"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DecisionType",
    "ListIdentitySourcesPaginatorName",
    "ListPoliciesPaginatorName",
    "ListPolicyStoresPaginatorName",
    "ListPolicyTemplatesPaginatorName",
    "OpenIdIssuerType",
    "PolicyEffectType",
    "PolicyTypeType",
    "ValidationModeType",
)

DecisionType = Literal["ALLOW", "DENY"]
ListIdentitySourcesPaginatorName = Literal["list_identity_sources"]
ListPoliciesPaginatorName = Literal["list_policies"]
ListPolicyStoresPaginatorName = Literal["list_policy_stores"]
ListPolicyTemplatesPaginatorName = Literal["list_policy_templates"]
OpenIdIssuerType = Literal["COGNITO"]
PolicyEffectType = Literal["Forbid", "Permit"]
PolicyTypeType = Literal["STATIC", "TEMPLATE_LINKED"]
ValidationModeType = Literal["OFF", "STRICT"]
