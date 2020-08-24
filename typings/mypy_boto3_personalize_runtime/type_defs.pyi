"""
Main interface for personalize-runtime service type definitions.

Usage::

    ```python
    from mypy_boto3_personalize_runtime.type_defs import PredictedItemTypeDef

    data: PredictedItemTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "PredictedItemTypeDef",
    "GetPersonalizedRankingResponseTypeDef",
    "GetRecommendationsResponseTypeDef",
)

PredictedItemTypeDef = TypedDict(
    "PredictedItemTypeDef", {"itemId": str, "score": float}, total=False
)

GetPersonalizedRankingResponseTypeDef = TypedDict(
    "GetPersonalizedRankingResponseTypeDef",
    {"personalizedRanking": List["PredictedItemTypeDef"], "recommendationId": str},
    total=False,
)

GetRecommendationsResponseTypeDef = TypedDict(
    "GetRecommendationsResponseTypeDef",
    {"itemList": List["PredictedItemTypeDef"], "recommendationId": str},
    total=False,
)
