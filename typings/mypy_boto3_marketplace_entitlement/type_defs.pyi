"""
Main interface for marketplace-entitlement service type definitions.

Usage::

    ```python
    from mypy_boto3_marketplace_entitlement.type_defs import EntitlementTypeDef

    data: EntitlementTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "EntitlementTypeDef",
    "EntitlementValueTypeDef",
    "GetEntitlementsResultTypeDef",
    "PaginatorConfigTypeDef",
)

EntitlementTypeDef = TypedDict(
    "EntitlementTypeDef",
    {
        "ProductCode": str,
        "Dimension": str,
        "CustomerIdentifier": str,
        "Value": "EntitlementValueTypeDef",
        "ExpirationDate": datetime,
    },
    total=False,
)

EntitlementValueTypeDef = TypedDict(
    "EntitlementValueTypeDef",
    {"IntegerValue": int, "DoubleValue": float, "BooleanValue": bool, "StringValue": str},
    total=False,
)

GetEntitlementsResultTypeDef = TypedDict(
    "GetEntitlementsResultTypeDef",
    {"Entitlements": List["EntitlementTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
