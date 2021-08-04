"""
Type annotations for personalize-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_personalize_runtime.type_defs import GetPersonalizedRankingRequestRequestTypeDef

    data: GetPersonalizedRankingRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "GetPersonalizedRankingRequestRequestTypeDef",
    "GetPersonalizedRankingResponseTypeDef",
    "GetRecommendationsRequestRequestTypeDef",
    "GetRecommendationsResponseTypeDef",
    "PredictedItemTypeDef",
    "ResponseMetadataTypeDef",
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

_RequiredGetRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetRecommendationsRequestRequestTypeDef",
    {
        "campaignArn": str,
    },
)
_OptionalGetRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetRecommendationsRequestRequestTypeDef",
    {
        "itemId": str,
        "userId": str,
        "numResults": int,
        "context": Dict[str, str],
        "filterArn": str,
        "filterValues": Dict[str, str],
    },
    total=False,
)

class GetRecommendationsRequestRequestTypeDef(
    _RequiredGetRecommendationsRequestRequestTypeDef,
    _OptionalGetRecommendationsRequestRequestTypeDef,
):
    pass

GetRecommendationsResponseTypeDef = TypedDict(
    "GetRecommendationsResponseTypeDef",
    {
        "itemList": List["PredictedItemTypeDef"],
        "recommendationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PredictedItemTypeDef = TypedDict(
    "PredictedItemTypeDef",
    {
        "itemId": str,
        "score": float,
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
