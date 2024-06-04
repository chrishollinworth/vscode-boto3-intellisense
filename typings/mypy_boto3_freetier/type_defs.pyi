"""
Type annotations for freetier service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_freetier/type_defs.html)

Usage::

    ```python
    from mypy_boto3_freetier.type_defs import DimensionValuesTypeDef

    data: DimensionValuesTypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict, List

from .literals import DimensionType, MatchOptionType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DimensionValuesTypeDef",
    "ExpressionTypeDef",
    "FreeTierUsageTypeDef",
    "GetFreeTierUsageRequestRequestTypeDef",
    "GetFreeTierUsageResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
)

DimensionValuesTypeDef = TypedDict(
    "DimensionValuesTypeDef",
    {
        "Key": DimensionType,
        "MatchOptions": List[MatchOptionType],
        "Values": List[str],
    },
)

ExpressionTypeDef = TypedDict(
    "ExpressionTypeDef",
    {
        "And": List[Dict[str, Any]],
        "Dimensions": "DimensionValuesTypeDef",
        "Not": Dict[str, Any],
        "Or": List[Dict[str, Any]],
    },
    total=False,
)

FreeTierUsageTypeDef = TypedDict(
    "FreeTierUsageTypeDef",
    {
        "actualUsageAmount": float,
        "description": str,
        "forecastedUsageAmount": float,
        "freeTierType": str,
        "limit": float,
        "operation": str,
        "region": str,
        "service": str,
        "unit": str,
        "usageType": str,
    },
    total=False,
)

GetFreeTierUsageRequestRequestTypeDef = TypedDict(
    "GetFreeTierUsageRequestRequestTypeDef",
    {
        "filter": "ExpressionTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

GetFreeTierUsageResponseTypeDef = TypedDict(
    "GetFreeTierUsageResponseTypeDef",
    {
        "freeTierUsages": List["FreeTierUsageTypeDef"],
        "nextToken": str,
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
