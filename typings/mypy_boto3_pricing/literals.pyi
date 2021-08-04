"""
Type annotations for pricing service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/literals.html)

Usage::

    ```python
    from mypy_boto3_pricing.literals import DescribeServicesPaginatorName

    data: DescribeServicesPaginatorName = "describe_services"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DescribeServicesPaginatorName",
    "FilterTypeType",
    "GetAttributeValuesPaginatorName",
    "GetProductsPaginatorName",
)

DescribeServicesPaginatorName = Literal["describe_services"]
FilterTypeType = Literal["TERM_MATCH"]
GetAttributeValuesPaginatorName = Literal["get_attribute_values"]
GetProductsPaginatorName = Literal["get_products"]
