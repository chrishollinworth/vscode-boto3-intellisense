"""
Type annotations for freetier service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_freetier.type_defs import DimensionValuesTypeDef

    data: DimensionValuesTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from .literals import DimensionType, MatchOptionType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "DimensionValuesTypeDef",
    "ExpressionPaginatorTypeDef",
    "ExpressionTypeDef",
    "FreeTierUsageTypeDef",
    "GetFreeTierUsageRequestPaginateTypeDef",
    "GetFreeTierUsageRequestTypeDef",
    "GetFreeTierUsageResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
)

class DimensionValuesTypeDef(TypedDict):
    Key: DimensionType
    MatchOptions: Sequence[MatchOptionType]
    Values: Sequence[str]

class FreeTierUsageTypeDef(TypedDict):
    actualUsageAmount: NotRequired[float]
    description: NotRequired[str]
    forecastedUsageAmount: NotRequired[float]
    freeTierType: NotRequired[str]
    limit: NotRequired[float]
    operation: NotRequired[str]
    region: NotRequired[str]
    service: NotRequired[str]
    unit: NotRequired[str]
    usageType: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ExpressionPaginatorTypeDef(TypedDict):
    And: NotRequired[Sequence[Mapping[str, Any]]]
    Dimensions: NotRequired[DimensionValuesTypeDef]
    Not: NotRequired[Mapping[str, Any]]
    Or: NotRequired[Sequence[Mapping[str, Any]]]

class ExpressionTypeDef(TypedDict):
    And: NotRequired[Sequence[Mapping[str, Any]]]
    Dimensions: NotRequired[DimensionValuesTypeDef]
    Not: NotRequired[Mapping[str, Any]]
    Or: NotRequired[Sequence[Mapping[str, Any]]]

class GetFreeTierUsageResponseTypeDef(TypedDict):
    freeTierUsages: List[FreeTierUsageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

GetFreeTierUsageRequestPaginateTypeDef = TypedDict(
    "GetFreeTierUsageRequestPaginateTypeDef",
    {
        "filter": NotRequired[ExpressionPaginatorTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetFreeTierUsageRequestTypeDef = TypedDict(
    "GetFreeTierUsageRequestTypeDef",
    {
        "filter": NotRequired[ExpressionTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
