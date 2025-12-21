"""
Type annotations for freetier service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_freetier.type_defs import MonetaryAmountTypeDef

    data: MonetaryAmountTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any

from .literals import (
    AccountPlanStatusType,
    AccountPlanTypeType,
    ActivityStatusType,
    DimensionType,
    LanguageCodeType,
    MatchOptionType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ActivityRewardTypeDef",
    "ActivitySummaryTypeDef",
    "DimensionValuesTypeDef",
    "ExpressionPaginatorTypeDef",
    "ExpressionTypeDef",
    "FreeTierUsageTypeDef",
    "GetAccountActivityRequestTypeDef",
    "GetAccountActivityResponseTypeDef",
    "GetAccountPlanStateResponseTypeDef",
    "GetFreeTierUsageRequestPaginateTypeDef",
    "GetFreeTierUsageRequestTypeDef",
    "GetFreeTierUsageResponseTypeDef",
    "ListAccountActivitiesRequestPaginateTypeDef",
    "ListAccountActivitiesRequestTypeDef",
    "ListAccountActivitiesResponseTypeDef",
    "MonetaryAmountTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "UpgradeAccountPlanRequestTypeDef",
    "UpgradeAccountPlanResponseTypeDef",
)

class MonetaryAmountTypeDef(TypedDict):
    amount: float
    unit: Literal["USD"]

class DimensionValuesTypeDef(TypedDict):
    Key: DimensionType
    Values: Sequence[str]
    MatchOptions: Sequence[MatchOptionType]

class FreeTierUsageTypeDef(TypedDict):
    service: NotRequired[str]
    operation: NotRequired[str]
    usageType: NotRequired[str]
    region: NotRequired[str]
    actualUsageAmount: NotRequired[float]
    forecastedUsageAmount: NotRequired[float]
    limit: NotRequired[float]
    unit: NotRequired[str]
    description: NotRequired[str]
    freeTierType: NotRequired[str]

class GetAccountActivityRequestTypeDef(TypedDict):
    activityId: str
    languageCode: NotRequired[LanguageCodeType]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAccountActivitiesRequestTypeDef(TypedDict):
    filterActivityStatuses: NotRequired[Sequence[ActivityStatusType]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    languageCode: NotRequired[LanguageCodeType]

class UpgradeAccountPlanRequestTypeDef(TypedDict):
    accountPlanType: AccountPlanTypeType

class ActivityRewardTypeDef(TypedDict):
    credit: NotRequired[MonetaryAmountTypeDef]

class ExpressionPaginatorTypeDef(TypedDict):
    Or: NotRequired[Sequence[Mapping[str, Any]]]
    And: NotRequired[Sequence[Mapping[str, Any]]]
    Not: NotRequired[Mapping[str, Any]]
    Dimensions: NotRequired[DimensionValuesTypeDef]

class ExpressionTypeDef(TypedDict):
    Or: NotRequired[Sequence[Mapping[str, Any]]]
    And: NotRequired[Sequence[Mapping[str, Any]]]
    Not: NotRequired[Mapping[str, Any]]
    Dimensions: NotRequired[DimensionValuesTypeDef]

class GetAccountPlanStateResponseTypeDef(TypedDict):
    accountId: str
    accountPlanType: AccountPlanTypeType
    accountPlanStatus: AccountPlanStatusType
    accountPlanRemainingCredits: MonetaryAmountTypeDef
    accountPlanExpirationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetFreeTierUsageResponseTypeDef(TypedDict):
    freeTierUsages: List[FreeTierUsageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpgradeAccountPlanResponseTypeDef(TypedDict):
    accountId: str
    accountPlanType: AccountPlanTypeType
    accountPlanStatus: AccountPlanStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountActivitiesRequestPaginateTypeDef(TypedDict):
    filterActivityStatuses: NotRequired[Sequence[ActivityStatusType]]
    languageCode: NotRequired[LanguageCodeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ActivitySummaryTypeDef(TypedDict):
    activityId: str
    title: str
    reward: ActivityRewardTypeDef
    status: ActivityStatusType

class GetAccountActivityResponseTypeDef(TypedDict):
    activityId: str
    title: str
    description: str
    status: ActivityStatusType
    instructionsUrl: str
    reward: ActivityRewardTypeDef
    estimatedTimeToCompleteInMinutes: int
    expiresAt: datetime
    startedAt: datetime
    completedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

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

class ListAccountActivitiesResponseTypeDef(TypedDict):
    activities: List[ActivitySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
