"""
Type annotations for marketplace-entitlement service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/literals.html)

Usage::

    ```python
    from mypy_boto3_marketplace_entitlement.literals import GetEntitlementFilterNameType

    data: GetEntitlementFilterNameType = "CUSTOMER_IDENTIFIER"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("GetEntitlementFilterNameType", "GetEntitlementsPaginatorName")

GetEntitlementFilterNameType = Literal["CUSTOMER_IDENTIFIER", "DIMENSION"]
GetEntitlementsPaginatorName = Literal["get_entitlements"]
