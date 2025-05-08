"""
Type annotations for billing service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billing/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_billing.type_defs import TimestampTypeDef

    data: TimestampTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import BillingViewTypeType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ActiveTimeRangeTypeDef",
    "BillingViewElementTypeDef",
    "BillingViewListElementTypeDef",
    "CreateBillingViewRequestTypeDef",
    "CreateBillingViewResponseTypeDef",
    "DeleteBillingViewRequestTypeDef",
    "DeleteBillingViewResponseTypeDef",
    "DimensionValuesOutputTypeDef",
    "DimensionValuesTypeDef",
    "ExpressionOutputTypeDef",
    "ExpressionTypeDef",
    "ExpressionUnionTypeDef",
    "GetBillingViewRequestTypeDef",
    "GetBillingViewResponseTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "ListBillingViewsRequestPaginateTypeDef",
    "ListBillingViewsRequestTypeDef",
    "ListBillingViewsResponseTypeDef",
    "ListSourceViewsForBillingViewRequestPaginateTypeDef",
    "ListSourceViewsForBillingViewRequestTypeDef",
    "ListSourceViewsForBillingViewResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TagValuesOutputTypeDef",
    "TagValuesTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateBillingViewRequestTypeDef",
    "UpdateBillingViewResponseTypeDef",
)

TimestampTypeDef = Union[datetime, str]

class BillingViewListElementTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    ownerAccountId: NotRequired[str]
    billingViewType: NotRequired[BillingViewTypeType]

class ResourceTagTypeDef(TypedDict):
    key: str
    value: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteBillingViewRequestTypeDef(TypedDict):
    arn: str

class DimensionValuesOutputTypeDef(TypedDict):
    key: Literal["LINKED_ACCOUNT"]
    values: List[str]

class DimensionValuesTypeDef(TypedDict):
    key: Literal["LINKED_ACCOUNT"]
    values: Sequence[str]

class TagValuesOutputTypeDef(TypedDict):
    key: str
    values: List[str]

class TagValuesTypeDef(TypedDict):
    key: str
    values: Sequence[str]

class GetBillingViewRequestTypeDef(TypedDict):
    arn: str

class GetResourcePolicyRequestTypeDef(TypedDict):
    resourceArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListSourceViewsForBillingViewRequestTypeDef(TypedDict):
    arn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    resourceTagKeys: Sequence[str]

class ActiveTimeRangeTypeDef(TypedDict):
    activeAfterInclusive: TimestampTypeDef
    activeBeforeInclusive: TimestampTypeDef

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    resourceTags: Sequence[ResourceTagTypeDef]

class CreateBillingViewResponseTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBillingViewResponseTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(TypedDict):
    resourceArn: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBillingViewsResponseTypeDef(TypedDict):
    billingViews: List[BillingViewListElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSourceViewsForBillingViewResponseTypeDef(TypedDict):
    sourceViews: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    resourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBillingViewResponseTypeDef(TypedDict):
    arn: str
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ExpressionOutputTypeDef(TypedDict):
    dimensions: NotRequired[DimensionValuesOutputTypeDef]
    tags: NotRequired[TagValuesOutputTypeDef]

class ExpressionTypeDef(TypedDict):
    dimensions: NotRequired[DimensionValuesTypeDef]
    tags: NotRequired[TagValuesTypeDef]

class ListSourceViewsForBillingViewRequestPaginateTypeDef(TypedDict):
    arn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBillingViewsRequestPaginateTypeDef(TypedDict):
    activeTimeRange: NotRequired[ActiveTimeRangeTypeDef]
    arns: NotRequired[Sequence[str]]
    billingViewTypes: NotRequired[Sequence[BillingViewTypeType]]
    ownerAccountId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBillingViewsRequestTypeDef(TypedDict):
    activeTimeRange: NotRequired[ActiveTimeRangeTypeDef]
    arns: NotRequired[Sequence[str]]
    billingViewTypes: NotRequired[Sequence[BillingViewTypeType]]
    ownerAccountId: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class BillingViewElementTypeDef(TypedDict):
    arn: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    billingViewType: NotRequired[BillingViewTypeType]
    ownerAccountId: NotRequired[str]
    dataFilterExpression: NotRequired[ExpressionOutputTypeDef]
    createdAt: NotRequired[datetime]
    updatedAt: NotRequired[datetime]

ExpressionUnionTypeDef = Union[ExpressionTypeDef, ExpressionOutputTypeDef]

class GetBillingViewResponseTypeDef(TypedDict):
    billingView: BillingViewElementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBillingViewRequestTypeDef(TypedDict):
    name: str
    sourceViews: Sequence[str]
    description: NotRequired[str]
    dataFilterExpression: NotRequired[ExpressionUnionTypeDef]
    clientToken: NotRequired[str]
    resourceTags: NotRequired[Sequence[ResourceTagTypeDef]]

class UpdateBillingViewRequestTypeDef(TypedDict):
    arn: str
    name: NotRequired[str]
    description: NotRequired[str]
    dataFilterExpression: NotRequired[ExpressionUnionTypeDef]
