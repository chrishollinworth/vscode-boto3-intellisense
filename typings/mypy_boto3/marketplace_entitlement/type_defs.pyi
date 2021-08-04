"""
Type annotations for marketplace-entitlement service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/type_defs.html)

Usage::

    ```python
    from mypy_boto3_marketplace_entitlement.type_defs import EntitlementTypeDef

    data: EntitlementTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import GetEntitlementFilterNameType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "EntitlementTypeDef",
    "EntitlementValueTypeDef",
    "GetEntitlementsRequestRequestTypeDef",
    "GetEntitlementsResultTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
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
    {
        "IntegerValue": int,
        "DoubleValue": float,
        "BooleanValue": bool,
        "StringValue": str,
    },
    total=False,
)

_RequiredGetEntitlementsRequestRequestTypeDef = TypedDict(
    "_RequiredGetEntitlementsRequestRequestTypeDef",
    {
        "ProductCode": str,
    },
)
_OptionalGetEntitlementsRequestRequestTypeDef = TypedDict(
    "_OptionalGetEntitlementsRequestRequestTypeDef",
    {
        "Filter": Dict[GetEntitlementFilterNameType, List[str]],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetEntitlementsRequestRequestTypeDef(
    _RequiredGetEntitlementsRequestRequestTypeDef, _OptionalGetEntitlementsRequestRequestTypeDef
):
    pass

GetEntitlementsResultTypeDef = TypedDict(
    "GetEntitlementsResultTypeDef",
    {
        "Entitlements": List["EntitlementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
