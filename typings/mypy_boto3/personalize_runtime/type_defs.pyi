"""
Type annotations for personalize-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_personalize_runtime.type_defs import GetActionRecommendationsRequestRequestTypeDef

    data: GetActionRecommendationsRequestRequestTypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "GetActionRecommendationsRequestRequestTypeDef",
    "GetActionRecommendationsResponseTypeDef",
    "GetPersonalizedRankingRequestRequestTypeDef",
    "GetPersonalizedRankingResponseTypeDef",
    "GetRecommendationsRequestRequestTypeDef",
    "GetRecommendationsResponseTypeDef",
    "PredictedActionTypeDef",
    "PredictedItemTypeDef",
    "PromotionTypeDef",
    "ResponseMetadataTypeDef",
)

GetActionRecommendationsRequestRequestTypeDef = TypedDict(
    "GetActionRecommendationsRequestRequestTypeDef",
    {
        "campaignArn": str,
        "userId": str,
        "numResults": int,
        "filterArn": str,
        "filterValues": Dict[str, str],
    },
    total=False,
)

GetActionRecommendationsResponseTypeDef = TypedDict(
    "GetActionRecommendationsResponseTypeDef",
    {
        "actionList": List["PredictedActionTypeDef"],
        "recommendationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPersonalizedRankingRequestRequestTypeDef = TypedDict(
    "_RequiredGetPersonalizedRankingRequestRequestTypeDef",
    {
        "campaignArn": str,
        "inputList": List[str],
        "userId": str,
    },
)
_OptionalGetPersonalizedRankingRequestRequestTypeDef = TypedDict(
    "_OptionalGetPersonalizedRankingRequestRequestTypeDef",
    {
        "context": Dict[str, str],
        "filterArn": str,
        "filterValues": Dict[str, str],
        "metadataColumns": Dict[str, List[str]],
    },
    total=False,
)

class GetPersonalizedRankingRequestRequestTypeDef(
    _RequiredGetPersonalizedRankingRequestRequestTypeDef,
    _OptionalGetPersonalizedRankingRequestRequestTypeDef,
):
    pass

GetPersonalizedRankingResponseTypeDef = TypedDict(
    "GetPersonalizedRankingResponseTypeDef",
    {
        "personalizedRanking": List["PredictedItemTypeDef"],
        "recommendationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommendationsRequestRequestTypeDef = TypedDict(
    "GetRecommendationsRequestRequestTypeDef",
    {
        "campaignArn": str,
        "itemId": str,
        "userId": str,
        "numResults": int,
        "context": Dict[str, str],
        "filterArn": str,
        "filterValues": Dict[str, str],
        "recommenderArn": str,
        "promotions": List["PromotionTypeDef"],
        "metadataColumns": Dict[str, List[str]],
    },
    total=False,
)

GetRecommendationsResponseTypeDef = TypedDict(
    "GetRecommendationsResponseTypeDef",
    {
        "itemList": List["PredictedItemTypeDef"],
        "recommendationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PredictedActionTypeDef = TypedDict(
    "PredictedActionTypeDef",
    {
        "actionId": str,
        "score": float,
    },
    total=False,
)

PredictedItemTypeDef = TypedDict(
    "PredictedItemTypeDef",
    {
        "itemId": str,
        "score": float,
        "promotionName": str,
        "metadata": Dict[str, str],
        "reason": List[str],
    },
    total=False,
)

PromotionTypeDef = TypedDict(
    "PromotionTypeDef",
    {
        "name": str,
        "percentPromotedItems": int,
        "filterArn": str,
        "filterValues": Dict[str, str],
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
