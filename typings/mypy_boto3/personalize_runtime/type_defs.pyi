"""
Type annotations for personalize-runtime service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_personalize_runtime.type_defs import GetActionRecommendationsRequestTypeDef

    data: GetActionRecommendationsRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

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
    "GetActionRecommendationsRequestTypeDef",
    "GetActionRecommendationsResponseTypeDef",
    "GetPersonalizedRankingRequestTypeDef",
    "GetPersonalizedRankingResponseTypeDef",
    "GetRecommendationsRequestTypeDef",
    "GetRecommendationsResponseTypeDef",
    "PredictedActionTypeDef",
    "PredictedItemTypeDef",
    "PromotionTypeDef",
    "ResponseMetadataTypeDef",
)

class GetActionRecommendationsRequestTypeDef(TypedDict):
    campaignArn: NotRequired[str]
    userId: NotRequired[str]
    numResults: NotRequired[int]
    filterArn: NotRequired[str]
    filterValues: NotRequired[Mapping[str, str]]

class PredictedActionTypeDef(TypedDict):
    actionId: NotRequired[str]
    score: NotRequired[float]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetPersonalizedRankingRequestTypeDef(TypedDict):
    campaignArn: str
    inputList: Sequence[str]
    userId: str
    context: NotRequired[Mapping[str, str]]
    filterArn: NotRequired[str]
    filterValues: NotRequired[Mapping[str, str]]
    metadataColumns: NotRequired[Mapping[str, Sequence[str]]]

class PredictedItemTypeDef(TypedDict):
    itemId: NotRequired[str]
    score: NotRequired[float]
    promotionName: NotRequired[str]
    metadata: NotRequired[Dict[str, str]]
    reason: NotRequired[List[str]]

class PromotionTypeDef(TypedDict):
    name: NotRequired[str]
    percentPromotedItems: NotRequired[int]
    filterArn: NotRequired[str]
    filterValues: NotRequired[Mapping[str, str]]

class GetActionRecommendationsResponseTypeDef(TypedDict):
    actionList: List[PredictedActionTypeDef]
    recommendationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPersonalizedRankingResponseTypeDef(TypedDict):
    personalizedRanking: List[PredictedItemTypeDef]
    recommendationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommendationsResponseTypeDef(TypedDict):
    itemList: List[PredictedItemTypeDef]
    recommendationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommendationsRequestTypeDef(TypedDict):
    campaignArn: NotRequired[str]
    itemId: NotRequired[str]
    userId: NotRequired[str]
    numResults: NotRequired[int]
    context: NotRequired[Mapping[str, str]]
    filterArn: NotRequired[str]
    filterValues: NotRequired[Mapping[str, str]]
    recommenderArn: NotRequired[str]
    promotions: NotRequired[Sequence[PromotionTypeDef]]
    metadataColumns: NotRequired[Mapping[str, Sequence[str]]]
