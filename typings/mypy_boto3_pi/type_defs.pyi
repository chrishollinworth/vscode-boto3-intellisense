"""
Type annotations for pi service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pi/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_pi.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AnalysisStatusType,
    ContextTypeType,
    DetailStatusType,
    FeatureStatusType,
    FineGrainedActionType,
    PeriodAlignmentType,
    ServiceTypeType,
    SeverityType,
    TextFormatType,
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
    "AnalysisReportSummaryTypeDef",
    "AnalysisReportTypeDef",
    "CreatePerformanceAnalysisReportRequestTypeDef",
    "CreatePerformanceAnalysisReportResponseTypeDef",
    "DataPointTypeDef",
    "DataTypeDef",
    "DeletePerformanceAnalysisReportRequestTypeDef",
    "DescribeDimensionKeysRequestTypeDef",
    "DescribeDimensionKeysResponseTypeDef",
    "DimensionDetailTypeDef",
    "DimensionGroupDetailTypeDef",
    "DimensionGroupTypeDef",
    "DimensionKeyDescriptionTypeDef",
    "DimensionKeyDetailTypeDef",
    "FeatureMetadataTypeDef",
    "GetDimensionKeyDetailsRequestTypeDef",
    "GetDimensionKeyDetailsResponseTypeDef",
    "GetPerformanceAnalysisReportRequestTypeDef",
    "GetPerformanceAnalysisReportResponseTypeDef",
    "GetResourceMetadataRequestTypeDef",
    "GetResourceMetadataResponseTypeDef",
    "GetResourceMetricsRequestTypeDef",
    "GetResourceMetricsResponseTypeDef",
    "InsightTypeDef",
    "ListAvailableResourceDimensionsRequestTypeDef",
    "ListAvailableResourceDimensionsResponseTypeDef",
    "ListAvailableResourceMetricsRequestTypeDef",
    "ListAvailableResourceMetricsResponseTypeDef",
    "ListPerformanceAnalysisReportsRequestTypeDef",
    "ListPerformanceAnalysisReportsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricDimensionGroupsTypeDef",
    "MetricKeyDataPointsTypeDef",
    "MetricQueryTypeDef",
    "PerformanceInsightsMetricTypeDef",
    "RecommendationTypeDef",
    "ResponseMetadataTypeDef",
    "ResponsePartitionKeyTypeDef",
    "ResponseResourceMetricKeyTypeDef",
    "ResponseResourceMetricTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
)

class TagTypeDef(TypedDict):
    Key: str
    Value: str

TimestampTypeDef = Union[datetime, str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DataPointTypeDef(TypedDict):
    Timestamp: datetime
    Value: float

class PerformanceInsightsMetricTypeDef(TypedDict):
    Metric: NotRequired[str]
    DisplayName: NotRequired[str]
    Dimensions: NotRequired[Dict[str, str]]
    Filter: NotRequired[Dict[str, str]]
    Value: NotRequired[float]

class DeletePerformanceAnalysisReportRequestTypeDef(TypedDict):
    ServiceType: ServiceTypeType
    Identifier: str
    AnalysisReportId: str

class DimensionGroupTypeDef(TypedDict):
    Group: str
    Dimensions: NotRequired[Sequence[str]]
    Limit: NotRequired[int]

class DimensionKeyDescriptionTypeDef(TypedDict):
    Dimensions: NotRequired[Dict[str, str]]
    Total: NotRequired[float]
    AdditionalMetrics: NotRequired[Dict[str, float]]
    Partitions: NotRequired[List[float]]

class ResponsePartitionKeyTypeDef(TypedDict):
    Dimensions: Dict[str, str]

class DimensionDetailTypeDef(TypedDict):
    Identifier: NotRequired[str]

class DimensionKeyDetailTypeDef(TypedDict):
    Value: NotRequired[str]
    Dimension: NotRequired[str]
    Status: NotRequired[DetailStatusType]

class FeatureMetadataTypeDef(TypedDict):
    Status: NotRequired[FeatureStatusType]

class GetDimensionKeyDetailsRequestTypeDef(TypedDict):
    ServiceType: ServiceTypeType
    Identifier: str
    Group: str
    GroupIdentifier: str
    RequestedDimensions: NotRequired[Sequence[str]]

class GetPerformanceAnalysisReportRequestTypeDef(TypedDict):
    ServiceType: ServiceTypeType
    Identifier: str
    AnalysisReportId: str
    TextFormat: NotRequired[TextFormatType]
    AcceptLanguage: NotRequired[Literal["EN_US"]]

class GetResourceMetadataRequestTypeDef(TypedDict):
    ServiceType: ServiceTypeType
    Identifier: str

class RecommendationTypeDef(TypedDict):
    RecommendationId: NotRequired[str]
    RecommendationDescription: NotRequired[str]

class ListAvailableResourceDimensionsRequestTypeDef(TypedDict):
    ServiceType: ServiceTypeType
    Identifier: str
    Metrics: Sequence[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    AuthorizedActions: NotRequired[Sequence[FineGrainedActionType]]

class ListAvailableResourceMetricsRequestTypeDef(TypedDict):
    ServiceType: ServiceTypeType
    Identifier: str
    MetricTypes: Sequence[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ResponseResourceMetricTypeDef(TypedDict):
    Metric: NotRequired[str]
    Description: NotRequired[str]
    Unit: NotRequired[str]

class ListPerformanceAnalysisReportsRequestTypeDef(TypedDict):
    ServiceType: ServiceTypeType
    Identifier: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ListTags: NotRequired[bool]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ServiceType: ServiceTypeType
    ResourceARN: str

class ResponseResourceMetricKeyTypeDef(TypedDict):
    Metric: str
    Dimensions: NotRequired[Dict[str, str]]

class UntagResourceRequestTypeDef(TypedDict):
    ServiceType: ServiceTypeType
    ResourceARN: str
    TagKeys: Sequence[str]

class AnalysisReportSummaryTypeDef(TypedDict):
    AnalysisReportId: NotRequired[str]
    CreateTime: NotRequired[datetime]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    Status: NotRequired[AnalysisStatusType]
    Tags: NotRequired[List[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    ServiceType: ServiceTypeType
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreatePerformanceAnalysisReportRequestTypeDef(TypedDict):
    ServiceType: ServiceTypeType
    Identifier: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreatePerformanceAnalysisReportResponseTypeDef(TypedDict):
    AnalysisReportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DataTypeDef(TypedDict):
    PerformanceInsightsMetric: NotRequired[PerformanceInsightsMetricTypeDef]

class DescribeDimensionKeysRequestTypeDef(TypedDict):
    ServiceType: ServiceTypeType
    Identifier: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Metric: str
    GroupBy: DimensionGroupTypeDef
    PeriodInSeconds: NotRequired[int]
    AdditionalMetrics: NotRequired[Sequence[str]]
    PartitionBy: NotRequired[DimensionGroupTypeDef]
    Filter: NotRequired[Mapping[str, str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class MetricQueryTypeDef(TypedDict):
    Metric: str
    GroupBy: NotRequired[DimensionGroupTypeDef]
    Filter: NotRequired[Mapping[str, str]]

class DescribeDimensionKeysResponseTypeDef(TypedDict):
    AlignedStartTime: datetime
    AlignedEndTime: datetime
    PartitionKeys: List[ResponsePartitionKeyTypeDef]
    Keys: List[DimensionKeyDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DimensionGroupDetailTypeDef(TypedDict):
    Group: NotRequired[str]
    Dimensions: NotRequired[List[DimensionDetailTypeDef]]

class GetDimensionKeyDetailsResponseTypeDef(TypedDict):
    Dimensions: List[DimensionKeyDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceMetadataResponseTypeDef(TypedDict):
    Identifier: str
    Features: Dict[str, FeatureMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAvailableResourceMetricsResponseTypeDef(TypedDict):
    Metrics: List[ResponseResourceMetricTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class MetricKeyDataPointsTypeDef(TypedDict):
    Key: NotRequired[ResponseResourceMetricKeyTypeDef]
    DataPoints: NotRequired[List[DataPointTypeDef]]

class ListPerformanceAnalysisReportsResponseTypeDef(TypedDict):
    AnalysisReports: List[AnalysisReportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class InsightTypeDef(TypedDict):
    InsightId: str
    InsightType: NotRequired[str]
    Context: NotRequired[ContextTypeType]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    Severity: NotRequired[SeverityType]
    SupportingInsights: NotRequired[List[Dict[str, Any]]]
    Description: NotRequired[str]
    Recommendations: NotRequired[List[RecommendationTypeDef]]
    InsightData: NotRequired[List[DataTypeDef]]
    BaselineData: NotRequired[List[DataTypeDef]]

class GetResourceMetricsRequestTypeDef(TypedDict):
    ServiceType: ServiceTypeType
    Identifier: str
    MetricQueries: Sequence[MetricQueryTypeDef]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    PeriodInSeconds: NotRequired[int]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    PeriodAlignment: NotRequired[PeriodAlignmentType]

class MetricDimensionGroupsTypeDef(TypedDict):
    Metric: NotRequired[str]
    Groups: NotRequired[List[DimensionGroupDetailTypeDef]]

class GetResourceMetricsResponseTypeDef(TypedDict):
    AlignedStartTime: datetime
    AlignedEndTime: datetime
    Identifier: str
    MetricList: List[MetricKeyDataPointsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AnalysisReportTypeDef(TypedDict):
    AnalysisReportId: str
    Identifier: NotRequired[str]
    ServiceType: NotRequired[ServiceTypeType]
    CreateTime: NotRequired[datetime]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    Status: NotRequired[AnalysisStatusType]
    Insights: NotRequired[List[InsightTypeDef]]

class ListAvailableResourceDimensionsResponseTypeDef(TypedDict):
    MetricDimensions: List[MetricDimensionGroupsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetPerformanceAnalysisReportResponseTypeDef(TypedDict):
    AnalysisReport: AnalysisReportTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
