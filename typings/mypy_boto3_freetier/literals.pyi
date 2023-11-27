"""
Type annotations for freetier service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_freetier/literals.html)

Usage::

    ```python
    from mypy_boto3_freetier.literals import DimensionType

    data: DimensionType = "DESCRIPTION"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DimensionType", "GetFreeTierUsagePaginatorName", "MatchOptionType")

DimensionType = Literal[
    "DESCRIPTION",
    "FREE_TIER_TYPE",
    "OPERATION",
    "REGION",
    "SERVICE",
    "USAGE_PERCENTAGE",
    "USAGE_TYPE",
]
GetFreeTierUsagePaginatorName = Literal["get_free_tier_usage"]
MatchOptionType = Literal["CONTAINS", "ENDS_WITH", "EQUALS", "GREATER_THAN_OR_EQUAL", "STARTS_WITH"]
