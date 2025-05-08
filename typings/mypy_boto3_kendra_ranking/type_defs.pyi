"""
Type annotations for kendra-ranking service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_kendra_ranking.type_defs import CapacityUnitsConfigurationTypeDef

    data: CapacityUnitsConfigurationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import RescoreExecutionPlanStatusType

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
    "CapacityUnitsConfigurationTypeDef",
    "CreateRescoreExecutionPlanRequestTypeDef",
    "CreateRescoreExecutionPlanResponseTypeDef",
    "DeleteRescoreExecutionPlanRequestTypeDef",
    "DescribeRescoreExecutionPlanRequestTypeDef",
    "DescribeRescoreExecutionPlanResponseTypeDef",
    "DocumentTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListRescoreExecutionPlansRequestTypeDef",
    "ListRescoreExecutionPlansResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RescoreExecutionPlanSummaryTypeDef",
    "RescoreRequestTypeDef",
    "RescoreResultItemTypeDef",
    "RescoreResultTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateRescoreExecutionPlanRequestTypeDef",
)

class CapacityUnitsConfigurationTypeDef(TypedDict):
    RescoreCapacityUnits: int

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteRescoreExecutionPlanRequestTypeDef(TypedDict):
    Id: str

class DescribeRescoreExecutionPlanRequestTypeDef(TypedDict):
    Id: str

class DocumentTypeDef(TypedDict):
    Id: str
    OriginalScore: float
    GroupId: NotRequired[str]
    Title: NotRequired[str]
    Body: NotRequired[str]
    TokenizedTitle: NotRequired[Sequence[str]]
    TokenizedBody: NotRequired[Sequence[str]]

class ListRescoreExecutionPlansRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class RescoreExecutionPlanSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    Id: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]
    Status: NotRequired[RescoreExecutionPlanStatusType]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class RescoreResultItemTypeDef(TypedDict):
    DocumentId: NotRequired[str]
    Score: NotRequired[float]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateRescoreExecutionPlanRequestTypeDef(TypedDict):
    Id: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    CapacityUnits: NotRequired[CapacityUnitsConfigurationTypeDef]

class CreateRescoreExecutionPlanRequestTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    CapacityUnits: NotRequired[CapacityUnitsConfigurationTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateRescoreExecutionPlanResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRescoreExecutionPlanResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    Name: str
    Description: str
    CapacityUnits: CapacityUnitsConfigurationTypeDef
    CreatedAt: datetime
    UpdatedAt: datetime
    Status: RescoreExecutionPlanStatusType
    ErrorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RescoreRequestTypeDef(TypedDict):
    RescoreExecutionPlanId: str
    SearchQuery: str
    Documents: Sequence[DocumentTypeDef]

class ListRescoreExecutionPlansResponseTypeDef(TypedDict):
    SummaryItems: List[RescoreExecutionPlanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RescoreResultTypeDef(TypedDict):
    RescoreId: str
    ResultItems: List[RescoreResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
