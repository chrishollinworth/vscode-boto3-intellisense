"""
Type annotations for sagemaker-a2i-runtime service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_sagemaker_a2i_runtime.type_defs import DeleteHumanLoopRequestTypeDef

    data: DeleteHumanLoopRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import ContentClassifierType, HumanLoopStatusType, SortOrderType

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
    "DeleteHumanLoopRequestTypeDef",
    "DescribeHumanLoopRequestTypeDef",
    "DescribeHumanLoopResponseTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "HumanLoopInputTypeDef",
    "HumanLoopOutputTypeDef",
    "HumanLoopSummaryTypeDef",
    "ListHumanLoopsRequestPaginateTypeDef",
    "ListHumanLoopsRequestTypeDef",
    "ListHumanLoopsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "StartHumanLoopRequestTypeDef",
    "StartHumanLoopResponseTypeDef",
    "StopHumanLoopRequestTypeDef",
    "TimestampTypeDef",
)

class DeleteHumanLoopRequestTypeDef(TypedDict):
    HumanLoopName: str

class DescribeHumanLoopRequestTypeDef(TypedDict):
    HumanLoopName: str

class HumanLoopOutputTypeDef(TypedDict):
    OutputS3Uri: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class HumanLoopDataAttributesTypeDef(TypedDict):
    ContentClassifiers: Sequence[ContentClassifierType]

class HumanLoopInputTypeDef(TypedDict):
    InputContent: str

class HumanLoopSummaryTypeDef(TypedDict):
    HumanLoopName: NotRequired[str]
    HumanLoopStatus: NotRequired[HumanLoopStatusType]
    CreationTime: NotRequired[datetime]
    FailureReason: NotRequired[str]
    FlowDefinitionArn: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class StopHumanLoopRequestTypeDef(TypedDict):
    HumanLoopName: str

class DescribeHumanLoopResponseTypeDef(TypedDict):
    CreationTime: datetime
    FailureReason: str
    FailureCode: str
    HumanLoopStatus: HumanLoopStatusType
    HumanLoopName: str
    HumanLoopArn: str
    FlowDefinitionArn: str
    HumanLoopOutput: HumanLoopOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartHumanLoopResponseTypeDef(TypedDict):
    HumanLoopArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartHumanLoopRequestTypeDef(TypedDict):
    HumanLoopName: str
    FlowDefinitionArn: str
    HumanLoopInput: HumanLoopInputTypeDef
    DataAttributes: NotRequired[HumanLoopDataAttributesTypeDef]

class ListHumanLoopsResponseTypeDef(TypedDict):
    HumanLoopSummaries: List[HumanLoopSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListHumanLoopsRequestPaginateTypeDef(TypedDict):
    FlowDefinitionArn: str
    CreationTimeAfter: NotRequired[TimestampTypeDef]
    CreationTimeBefore: NotRequired[TimestampTypeDef]
    SortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHumanLoopsRequestTypeDef(TypedDict):
    FlowDefinitionArn: str
    CreationTimeAfter: NotRequired[TimestampTypeDef]
    CreationTimeBefore: NotRequired[TimestampTypeDef]
    SortOrder: NotRequired[SortOrderType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
