"""
Type annotations for bcm-recommended-actions service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_recommended_actions/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_bcm_recommended_actions.type_defs import ActionFilterTypeDef

    data: ActionFilterTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from .literals import ActionTypeType, FeatureType, FilterNameType, MatchOptionType, SeverityType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ActionFilterTypeDef",
    "ListRecommendedActionsRequestPaginateTypeDef",
    "ListRecommendedActionsRequestTypeDef",
    "ListRecommendedActionsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RecommendedActionTypeDef",
    "RequestFilterTypeDef",
    "ResponseMetadataTypeDef",
)

class ActionFilterTypeDef(TypedDict):
    key: FilterNameType
    matchOption: MatchOptionType
    values: Sequence[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

RecommendedActionTypeDef = TypedDict(
    "RecommendedActionTypeDef",
    {
        "id": NotRequired[str],
        "type": NotRequired[ActionTypeType],
        "accountId": NotRequired[str],
        "severity": NotRequired[SeverityType],
        "feature": NotRequired[FeatureType],
        "context": NotRequired[Dict[str, str]],
        "nextSteps": NotRequired[List[str]],
        "lastUpdatedTimeStamp": NotRequired[str],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class RequestFilterTypeDef(TypedDict):
    actions: NotRequired[Sequence[ActionFilterTypeDef]]

class ListRecommendedActionsResponseTypeDef(TypedDict):
    recommendedActions: List[RecommendedActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ListRecommendedActionsRequestPaginateTypeDef = TypedDict(
    "ListRecommendedActionsRequestPaginateTypeDef",
    {
        "filter": NotRequired[RequestFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRecommendedActionsRequestTypeDef = TypedDict(
    "ListRecommendedActionsRequestTypeDef",
    {
        "filter": NotRequired[RequestFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
