"""
Main interface for pricing service type definitions.

Usage::

    ```python
    from mypy_boto3_pricing.type_defs import AttributeValueTypeDef

    data: AttributeValueTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttributeValueTypeDef",
    "ServiceTypeDef",
    "DescribeServicesResponseTypeDef",
    "FilterTypeDef",
    "GetAttributeValuesResponseTypeDef",
    "GetProductsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

AttributeValueTypeDef = TypedDict("AttributeValueTypeDef", {"Value": str}, total=False)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef", {"ServiceCode": str, "AttributeNames": List[str]}, total=False
)

DescribeServicesResponseTypeDef = TypedDict(
    "DescribeServicesResponseTypeDef",
    {"Services": List["ServiceTypeDef"], "FormatVersion": str, "NextToken": str},
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef", {"Type": Literal["TERM_MATCH"], "Field": str, "Value": str}
)

GetAttributeValuesResponseTypeDef = TypedDict(
    "GetAttributeValuesResponseTypeDef",
    {"AttributeValues": List["AttributeValueTypeDef"], "NextToken": str},
    total=False,
)

GetProductsResponseTypeDef = TypedDict(
    "GetProductsResponseTypeDef",
    {"FormatVersion": str, "PriceList": List[str], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
