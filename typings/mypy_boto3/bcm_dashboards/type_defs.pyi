"""
Type annotations for bcm-dashboards service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_dashboards/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_bcm_dashboards.type_defs import GroupDefinitionTypeDef

    data: GroupDefinitionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    DateTimeTypeType,
    DimensionType,
    GranularityType,
    GroupDefinitionTypeType,
    MatchOptionType,
    MetricNameType,
    VisualTypeType,
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
    "CostAndUsageQueryOutputTypeDef",
    "CostAndUsageQueryTypeDef",
    "CostAndUsageQueryUnionTypeDef",
    "CostCategoryValuesOutputTypeDef",
    "CostCategoryValuesTypeDef",
    "CostCategoryValuesUnionTypeDef",
    "CreateDashboardRequestTypeDef",
    "CreateDashboardResponseTypeDef",
    "DashboardReferenceTypeDef",
    "DateTimeRangeTypeDef",
    "DateTimeValueTypeDef",
    "DeleteDashboardRequestTypeDef",
    "DeleteDashboardResponseTypeDef",
    "DimensionValuesOutputTypeDef",
    "DimensionValuesTypeDef",
    "DimensionValuesUnionTypeDef",
    "DisplayConfigOutputTypeDef",
    "DisplayConfigTypeDef",
    "DisplayConfigUnionTypeDef",
    "ExpressionOutputTypeDef",
    "ExpressionTypeDef",
    "ExpressionUnionTypeDef",
    "GetDashboardRequestTypeDef",
    "GetDashboardResponseTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GraphDisplayConfigTypeDef",
    "GroupDefinitionTypeDef",
    "ListDashboardsRequestPaginateTypeDef",
    "ListDashboardsRequestTypeDef",
    "ListDashboardsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QueryParametersOutputTypeDef",
    "QueryParametersTypeDef",
    "QueryParametersUnionTypeDef",
    "ReservationCoverageQueryOutputTypeDef",
    "ReservationCoverageQueryTypeDef",
    "ReservationCoverageQueryUnionTypeDef",
    "ReservationUtilizationQueryOutputTypeDef",
    "ReservationUtilizationQueryTypeDef",
    "ReservationUtilizationQueryUnionTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "SavingsPlansCoverageQueryOutputTypeDef",
    "SavingsPlansCoverageQueryTypeDef",
    "SavingsPlansCoverageQueryUnionTypeDef",
    "SavingsPlansUtilizationQueryOutputTypeDef",
    "SavingsPlansUtilizationQueryTypeDef",
    "SavingsPlansUtilizationQueryUnionTypeDef",
    "TagResourceRequestTypeDef",
    "TagValuesOutputTypeDef",
    "TagValuesTypeDef",
    "TagValuesUnionTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDashboardRequestTypeDef",
    "UpdateDashboardResponseTypeDef",
    "WidgetConfigOutputTypeDef",
    "WidgetConfigTypeDef",
    "WidgetConfigUnionTypeDef",
    "WidgetOutputTypeDef",
    "WidgetTypeDef",
    "WidgetUnionTypeDef",
)

GroupDefinitionTypeDef = TypedDict(
    "GroupDefinitionTypeDef",
    {
        "key": str,
        "type": NotRequired[GroupDefinitionTypeType],
    },
)

class CostCategoryValuesOutputTypeDef(TypedDict):
    key: NotRequired[str]
    values: NotRequired[List[str]]
    matchOptions: NotRequired[List[MatchOptionType]]

class CostCategoryValuesTypeDef(TypedDict):
    key: NotRequired[str]
    values: NotRequired[Sequence[str]]
    matchOptions: NotRequired[Sequence[MatchOptionType]]

class ResourceTagTypeDef(TypedDict):
    key: str
    value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

DashboardReferenceTypeDef = TypedDict(
    "DashboardReferenceTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal["CUSTOM"],
        "createdAt": datetime,
        "updatedAt": datetime,
        "description": NotRequired[str],
    },
)
DateTimeValueTypeDef = TypedDict(
    "DateTimeValueTypeDef",
    {
        "type": DateTimeTypeType,
        "value": str,
    },
)

class DeleteDashboardRequestTypeDef(TypedDict):
    arn: str

class DimensionValuesOutputTypeDef(TypedDict):
    key: DimensionType
    values: List[str]
    matchOptions: NotRequired[List[MatchOptionType]]

class DimensionValuesTypeDef(TypedDict):
    key: DimensionType
    values: Sequence[str]
    matchOptions: NotRequired[Sequence[MatchOptionType]]

class GraphDisplayConfigTypeDef(TypedDict):
    visualType: VisualTypeType

class TagValuesOutputTypeDef(TypedDict):
    key: NotRequired[str]
    values: NotRequired[List[str]]
    matchOptions: NotRequired[List[MatchOptionType]]

class GetDashboardRequestTypeDef(TypedDict):
    arn: str

class GetResourcePolicyRequestTypeDef(TypedDict):
    resourceArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListDashboardsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class TagValuesTypeDef(TypedDict):
    key: NotRequired[str]
    values: NotRequired[Sequence[str]]
    matchOptions: NotRequired[Sequence[MatchOptionType]]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    resourceTagKeys: Sequence[str]

CostCategoryValuesUnionTypeDef = Union[CostCategoryValuesTypeDef, CostCategoryValuesOutputTypeDef]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    resourceTags: Sequence[ResourceTagTypeDef]

class CreateDashboardResponseTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDashboardResponseTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(TypedDict):
    resourceArn: str
    policyDocument: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    resourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDashboardResponseTypeDef(TypedDict):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDashboardsResponseTypeDef(TypedDict):
    dashboards: List[DashboardReferenceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DateTimeRangeTypeDef(TypedDict):
    startTime: DateTimeValueTypeDef
    endTime: DateTimeValueTypeDef

DimensionValuesUnionTypeDef = Union[DimensionValuesTypeDef, DimensionValuesOutputTypeDef]

class DisplayConfigOutputTypeDef(TypedDict):
    graph: NotRequired[Dict[str, GraphDisplayConfigTypeDef]]
    table: NotRequired[Dict[str, Any]]

class DisplayConfigTypeDef(TypedDict):
    graph: NotRequired[Mapping[str, GraphDisplayConfigTypeDef]]
    table: NotRequired[Mapping[str, Any]]

ExpressionOutputTypeDef = TypedDict(
    "ExpressionOutputTypeDef",
    {
        "or": NotRequired[List[Dict[str, Any]]],
        "and": NotRequired[List[Dict[str, Any]]],
        "not": NotRequired[Dict[str, Any]],
        "dimensions": NotRequired[DimensionValuesOutputTypeDef],
        "tags": NotRequired[TagValuesOutputTypeDef],
        "costCategories": NotRequired[CostCategoryValuesOutputTypeDef],
    },
)

class ListDashboardsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

TagValuesUnionTypeDef = Union[TagValuesTypeDef, TagValuesOutputTypeDef]
DisplayConfigUnionTypeDef = Union[DisplayConfigTypeDef, DisplayConfigOutputTypeDef]
CostAndUsageQueryOutputTypeDef = TypedDict(
    "CostAndUsageQueryOutputTypeDef",
    {
        "metrics": List[MetricNameType],
        "timeRange": DateTimeRangeTypeDef,
        "granularity": GranularityType,
        "groupBy": NotRequired[List[GroupDefinitionTypeDef]],
        "filter": NotRequired[ExpressionOutputTypeDef],
    },
)
ReservationCoverageQueryOutputTypeDef = TypedDict(
    "ReservationCoverageQueryOutputTypeDef",
    {
        "timeRange": DateTimeRangeTypeDef,
        "groupBy": NotRequired[List[GroupDefinitionTypeDef]],
        "granularity": NotRequired[GranularityType],
        "filter": NotRequired[ExpressionOutputTypeDef],
        "metrics": NotRequired[List[MetricNameType]],
    },
)
ReservationUtilizationQueryOutputTypeDef = TypedDict(
    "ReservationUtilizationQueryOutputTypeDef",
    {
        "timeRange": DateTimeRangeTypeDef,
        "groupBy": NotRequired[List[GroupDefinitionTypeDef]],
        "granularity": NotRequired[GranularityType],
        "filter": NotRequired[ExpressionOutputTypeDef],
    },
)
SavingsPlansCoverageQueryOutputTypeDef = TypedDict(
    "SavingsPlansCoverageQueryOutputTypeDef",
    {
        "timeRange": DateTimeRangeTypeDef,
        "metrics": NotRequired[List[MetricNameType]],
        "granularity": NotRequired[GranularityType],
        "groupBy": NotRequired[List[GroupDefinitionTypeDef]],
        "filter": NotRequired[ExpressionOutputTypeDef],
    },
)
SavingsPlansUtilizationQueryOutputTypeDef = TypedDict(
    "SavingsPlansUtilizationQueryOutputTypeDef",
    {
        "timeRange": DateTimeRangeTypeDef,
        "granularity": NotRequired[GranularityType],
        "filter": NotRequired[ExpressionOutputTypeDef],
    },
)
ExpressionTypeDef = TypedDict(
    "ExpressionTypeDef",
    {
        "or": NotRequired[Sequence[Mapping[str, Any]]],
        "and": NotRequired[Sequence[Mapping[str, Any]]],
        "not": NotRequired[Mapping[str, Any]],
        "dimensions": NotRequired[DimensionValuesUnionTypeDef],
        "tags": NotRequired[TagValuesUnionTypeDef],
        "costCategories": NotRequired[CostCategoryValuesUnionTypeDef],
    },
)

class QueryParametersOutputTypeDef(TypedDict):
    costAndUsage: NotRequired[CostAndUsageQueryOutputTypeDef]
    savingsPlansCoverage: NotRequired[SavingsPlansCoverageQueryOutputTypeDef]
    savingsPlansUtilization: NotRequired[SavingsPlansUtilizationQueryOutputTypeDef]
    reservationCoverage: NotRequired[ReservationCoverageQueryOutputTypeDef]
    reservationUtilization: NotRequired[ReservationUtilizationQueryOutputTypeDef]

ExpressionUnionTypeDef = Union[ExpressionTypeDef, ExpressionOutputTypeDef]

class WidgetConfigOutputTypeDef(TypedDict):
    queryParameters: QueryParametersOutputTypeDef
    displayConfig: DisplayConfigOutputTypeDef

CostAndUsageQueryTypeDef = TypedDict(
    "CostAndUsageQueryTypeDef",
    {
        "metrics": Sequence[MetricNameType],
        "timeRange": DateTimeRangeTypeDef,
        "granularity": GranularityType,
        "groupBy": NotRequired[Sequence[GroupDefinitionTypeDef]],
        "filter": NotRequired[ExpressionUnionTypeDef],
    },
)
ReservationCoverageQueryTypeDef = TypedDict(
    "ReservationCoverageQueryTypeDef",
    {
        "timeRange": DateTimeRangeTypeDef,
        "groupBy": NotRequired[Sequence[GroupDefinitionTypeDef]],
        "granularity": NotRequired[GranularityType],
        "filter": NotRequired[ExpressionUnionTypeDef],
        "metrics": NotRequired[Sequence[MetricNameType]],
    },
)
ReservationUtilizationQueryTypeDef = TypedDict(
    "ReservationUtilizationQueryTypeDef",
    {
        "timeRange": DateTimeRangeTypeDef,
        "groupBy": NotRequired[Sequence[GroupDefinitionTypeDef]],
        "granularity": NotRequired[GranularityType],
        "filter": NotRequired[ExpressionUnionTypeDef],
    },
)
SavingsPlansCoverageQueryTypeDef = TypedDict(
    "SavingsPlansCoverageQueryTypeDef",
    {
        "timeRange": DateTimeRangeTypeDef,
        "metrics": NotRequired[Sequence[MetricNameType]],
        "granularity": NotRequired[GranularityType],
        "groupBy": NotRequired[Sequence[GroupDefinitionTypeDef]],
        "filter": NotRequired[ExpressionUnionTypeDef],
    },
)
SavingsPlansUtilizationQueryTypeDef = TypedDict(
    "SavingsPlansUtilizationQueryTypeDef",
    {
        "timeRange": DateTimeRangeTypeDef,
        "granularity": NotRequired[GranularityType],
        "filter": NotRequired[ExpressionUnionTypeDef],
    },
)

class WidgetOutputTypeDef(TypedDict):
    title: str
    configs: List[WidgetConfigOutputTypeDef]
    description: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    horizontalOffset: NotRequired[int]

CostAndUsageQueryUnionTypeDef = Union[CostAndUsageQueryTypeDef, CostAndUsageQueryOutputTypeDef]
ReservationCoverageQueryUnionTypeDef = Union[
    ReservationCoverageQueryTypeDef, ReservationCoverageQueryOutputTypeDef
]
ReservationUtilizationQueryUnionTypeDef = Union[
    ReservationUtilizationQueryTypeDef, ReservationUtilizationQueryOutputTypeDef
]
SavingsPlansCoverageQueryUnionTypeDef = Union[
    SavingsPlansCoverageQueryTypeDef, SavingsPlansCoverageQueryOutputTypeDef
]
SavingsPlansUtilizationQueryUnionTypeDef = Union[
    SavingsPlansUtilizationQueryTypeDef, SavingsPlansUtilizationQueryOutputTypeDef
]
GetDashboardResponseTypeDef = TypedDict(
    "GetDashboardResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "type": Literal["CUSTOM"],
        "widgets": List[WidgetOutputTypeDef],
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class QueryParametersTypeDef(TypedDict):
    costAndUsage: NotRequired[CostAndUsageQueryUnionTypeDef]
    savingsPlansCoverage: NotRequired[SavingsPlansCoverageQueryUnionTypeDef]
    savingsPlansUtilization: NotRequired[SavingsPlansUtilizationQueryUnionTypeDef]
    reservationCoverage: NotRequired[ReservationCoverageQueryUnionTypeDef]
    reservationUtilization: NotRequired[ReservationUtilizationQueryUnionTypeDef]

QueryParametersUnionTypeDef = Union[QueryParametersTypeDef, QueryParametersOutputTypeDef]

class WidgetConfigTypeDef(TypedDict):
    queryParameters: QueryParametersUnionTypeDef
    displayConfig: DisplayConfigUnionTypeDef

WidgetConfigUnionTypeDef = Union[WidgetConfigTypeDef, WidgetConfigOutputTypeDef]

class WidgetTypeDef(TypedDict):
    title: str
    configs: Sequence[WidgetConfigUnionTypeDef]
    description: NotRequired[str]
    width: NotRequired[int]
    height: NotRequired[int]
    horizontalOffset: NotRequired[int]

WidgetUnionTypeDef = Union[WidgetTypeDef, WidgetOutputTypeDef]

class CreateDashboardRequestTypeDef(TypedDict):
    name: str
    widgets: Sequence[WidgetUnionTypeDef]
    description: NotRequired[str]
    resourceTags: NotRequired[Sequence[ResourceTagTypeDef]]

class UpdateDashboardRequestTypeDef(TypedDict):
    arn: str
    name: NotRequired[str]
    description: NotRequired[str]
    widgets: NotRequired[Sequence[WidgetUnionTypeDef]]
