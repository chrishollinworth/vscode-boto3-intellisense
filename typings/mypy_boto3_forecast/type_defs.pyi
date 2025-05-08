"""
Type annotations for forecast service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_forecast.type_defs import ActionTypeDef

    data: ActionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AttributeTypeType,
    AutoMLOverrideStrategyType,
    ConditionType,
    DatasetTypeType,
    DayOfWeekType,
    DomainType,
    EvaluationTypeType,
    FilterConditionStringType,
    ImportModeType,
    MonthType,
    OperationType,
    OptimizationMetricType,
    ScalingTypeType,
    StateType,
    TimePointGranularityType,
    TimeSeriesGranularityType,
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
    "ActionTypeDef",
    "AdditionalDatasetOutputTypeDef",
    "AdditionalDatasetTypeDef",
    "AttributeConfigOutputTypeDef",
    "AttributeConfigTypeDef",
    "BaselineMetricTypeDef",
    "BaselineTypeDef",
    "CategoricalParameterRangeOutputTypeDef",
    "CategoricalParameterRangeTypeDef",
    "ContinuousParameterRangeTypeDef",
    "CreateAutoPredictorRequestTypeDef",
    "CreateAutoPredictorResponseTypeDef",
    "CreateDatasetGroupRequestTypeDef",
    "CreateDatasetGroupResponseTypeDef",
    "CreateDatasetImportJobRequestTypeDef",
    "CreateDatasetImportJobResponseTypeDef",
    "CreateDatasetRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateExplainabilityExportRequestTypeDef",
    "CreateExplainabilityExportResponseTypeDef",
    "CreateExplainabilityRequestTypeDef",
    "CreateExplainabilityResponseTypeDef",
    "CreateForecastExportJobRequestTypeDef",
    "CreateForecastExportJobResponseTypeDef",
    "CreateForecastRequestTypeDef",
    "CreateForecastResponseTypeDef",
    "CreateMonitorRequestTypeDef",
    "CreateMonitorResponseTypeDef",
    "CreatePredictorBacktestExportJobRequestTypeDef",
    "CreatePredictorBacktestExportJobResponseTypeDef",
    "CreatePredictorRequestTypeDef",
    "CreatePredictorResponseTypeDef",
    "CreateWhatIfAnalysisRequestTypeDef",
    "CreateWhatIfAnalysisResponseTypeDef",
    "CreateWhatIfForecastExportRequestTypeDef",
    "CreateWhatIfForecastExportResponseTypeDef",
    "CreateWhatIfForecastRequestTypeDef",
    "CreateWhatIfForecastResponseTypeDef",
    "DataConfigOutputTypeDef",
    "DataConfigTypeDef",
    "DataConfigUnionTypeDef",
    "DataDestinationTypeDef",
    "DataSourceTypeDef",
    "DatasetGroupSummaryTypeDef",
    "DatasetImportJobSummaryTypeDef",
    "DatasetSummaryTypeDef",
    "DeleteDatasetGroupRequestTypeDef",
    "DeleteDatasetImportJobRequestTypeDef",
    "DeleteDatasetRequestTypeDef",
    "DeleteExplainabilityExportRequestTypeDef",
    "DeleteExplainabilityRequestTypeDef",
    "DeleteForecastExportJobRequestTypeDef",
    "DeleteForecastRequestTypeDef",
    "DeleteMonitorRequestTypeDef",
    "DeletePredictorBacktestExportJobRequestTypeDef",
    "DeletePredictorRequestTypeDef",
    "DeleteResourceTreeRequestTypeDef",
    "DeleteWhatIfAnalysisRequestTypeDef",
    "DeleteWhatIfForecastExportRequestTypeDef",
    "DeleteWhatIfForecastRequestTypeDef",
    "DescribeAutoPredictorRequestTypeDef",
    "DescribeAutoPredictorResponseTypeDef",
    "DescribeDatasetGroupRequestTypeDef",
    "DescribeDatasetGroupResponseTypeDef",
    "DescribeDatasetImportJobRequestTypeDef",
    "DescribeDatasetImportJobResponseTypeDef",
    "DescribeDatasetRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeExplainabilityExportRequestTypeDef",
    "DescribeExplainabilityExportResponseTypeDef",
    "DescribeExplainabilityRequestTypeDef",
    "DescribeExplainabilityResponseTypeDef",
    "DescribeForecastExportJobRequestTypeDef",
    "DescribeForecastExportJobResponseTypeDef",
    "DescribeForecastRequestTypeDef",
    "DescribeForecastResponseTypeDef",
    "DescribeMonitorRequestTypeDef",
    "DescribeMonitorResponseTypeDef",
    "DescribePredictorBacktestExportJobRequestTypeDef",
    "DescribePredictorBacktestExportJobResponseTypeDef",
    "DescribePredictorRequestTypeDef",
    "DescribePredictorResponseTypeDef",
    "DescribeWhatIfAnalysisRequestTypeDef",
    "DescribeWhatIfAnalysisResponseTypeDef",
    "DescribeWhatIfForecastExportRequestTypeDef",
    "DescribeWhatIfForecastExportResponseTypeDef",
    "DescribeWhatIfForecastRequestTypeDef",
    "DescribeWhatIfForecastResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionConfigTypeDef",
    "ErrorMetricTypeDef",
    "EvaluationParametersTypeDef",
    "EvaluationResultTypeDef",
    "ExplainabilityConfigTypeDef",
    "ExplainabilityExportSummaryTypeDef",
    "ExplainabilityInfoTypeDef",
    "ExplainabilitySummaryTypeDef",
    "FeaturizationConfigOutputTypeDef",
    "FeaturizationConfigTypeDef",
    "FeaturizationConfigUnionTypeDef",
    "FeaturizationMethodOutputTypeDef",
    "FeaturizationMethodTypeDef",
    "FeaturizationOutputTypeDef",
    "FeaturizationTypeDef",
    "FilterTypeDef",
    "ForecastExportJobSummaryTypeDef",
    "ForecastSummaryTypeDef",
    "GetAccuracyMetricsRequestTypeDef",
    "GetAccuracyMetricsResponseTypeDef",
    "HyperParameterTuningJobConfigOutputTypeDef",
    "HyperParameterTuningJobConfigTypeDef",
    "HyperParameterTuningJobConfigUnionTypeDef",
    "InputDataConfigOutputTypeDef",
    "InputDataConfigTypeDef",
    "InputDataConfigUnionTypeDef",
    "IntegerParameterRangeTypeDef",
    "ListDatasetGroupsRequestPaginateTypeDef",
    "ListDatasetGroupsRequestTypeDef",
    "ListDatasetGroupsResponseTypeDef",
    "ListDatasetImportJobsRequestPaginateTypeDef",
    "ListDatasetImportJobsRequestTypeDef",
    "ListDatasetImportJobsResponseTypeDef",
    "ListDatasetsRequestPaginateTypeDef",
    "ListDatasetsRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListExplainabilitiesRequestPaginateTypeDef",
    "ListExplainabilitiesRequestTypeDef",
    "ListExplainabilitiesResponseTypeDef",
    "ListExplainabilityExportsRequestPaginateTypeDef",
    "ListExplainabilityExportsRequestTypeDef",
    "ListExplainabilityExportsResponseTypeDef",
    "ListForecastExportJobsRequestPaginateTypeDef",
    "ListForecastExportJobsRequestTypeDef",
    "ListForecastExportJobsResponseTypeDef",
    "ListForecastsRequestPaginateTypeDef",
    "ListForecastsRequestTypeDef",
    "ListForecastsResponseTypeDef",
    "ListMonitorEvaluationsRequestPaginateTypeDef",
    "ListMonitorEvaluationsRequestTypeDef",
    "ListMonitorEvaluationsResponseTypeDef",
    "ListMonitorsRequestPaginateTypeDef",
    "ListMonitorsRequestTypeDef",
    "ListMonitorsResponseTypeDef",
    "ListPredictorBacktestExportJobsRequestPaginateTypeDef",
    "ListPredictorBacktestExportJobsRequestTypeDef",
    "ListPredictorBacktestExportJobsResponseTypeDef",
    "ListPredictorsRequestPaginateTypeDef",
    "ListPredictorsRequestTypeDef",
    "ListPredictorsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWhatIfAnalysesRequestPaginateTypeDef",
    "ListWhatIfAnalysesRequestTypeDef",
    "ListWhatIfAnalysesResponseTypeDef",
    "ListWhatIfForecastExportsRequestPaginateTypeDef",
    "ListWhatIfForecastExportsRequestTypeDef",
    "ListWhatIfForecastExportsResponseTypeDef",
    "ListWhatIfForecastsRequestPaginateTypeDef",
    "ListWhatIfForecastsRequestTypeDef",
    "ListWhatIfForecastsResponseTypeDef",
    "MetricResultTypeDef",
    "MetricsTypeDef",
    "MonitorConfigTypeDef",
    "MonitorDataSourceTypeDef",
    "MonitorInfoTypeDef",
    "MonitorSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterRangesOutputTypeDef",
    "ParameterRangesTypeDef",
    "PredictorBacktestExportJobSummaryTypeDef",
    "PredictorBaselineTypeDef",
    "PredictorEventTypeDef",
    "PredictorExecutionDetailsTypeDef",
    "PredictorExecutionTypeDef",
    "PredictorMonitorEvaluationTypeDef",
    "PredictorSummaryTypeDef",
    "ReferencePredictorSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeResourceRequestTypeDef",
    "S3ConfigTypeDef",
    "SchemaAttributeTypeDef",
    "SchemaOutputTypeDef",
    "SchemaTypeDef",
    "SchemaUnionTypeDef",
    "StatisticsTypeDef",
    "StopResourceRequestTypeDef",
    "SupplementaryFeatureTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TestWindowSummaryTypeDef",
    "TimeAlignmentBoundaryTypeDef",
    "TimeSeriesConditionTypeDef",
    "TimeSeriesIdentifiersOutputTypeDef",
    "TimeSeriesIdentifiersTypeDef",
    "TimeSeriesReplacementsDataSourceOutputTypeDef",
    "TimeSeriesReplacementsDataSourceTypeDef",
    "TimeSeriesReplacementsDataSourceUnionTypeDef",
    "TimeSeriesSelectorOutputTypeDef",
    "TimeSeriesSelectorTypeDef",
    "TimeSeriesSelectorUnionTypeDef",
    "TimeSeriesTransformationOutputTypeDef",
    "TimeSeriesTransformationTypeDef",
    "TimeSeriesTransformationUnionTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDatasetGroupRequestTypeDef",
    "WeightedQuantileLossTypeDef",
    "WhatIfAnalysisSummaryTypeDef",
    "WhatIfForecastExportSummaryTypeDef",
    "WhatIfForecastSummaryTypeDef",
    "WindowSummaryTypeDef",
)

class ActionTypeDef(TypedDict):
    AttributeName: str
    Operation: OperationType
    Value: float

class AdditionalDatasetOutputTypeDef(TypedDict):
    Name: str
    Configuration: NotRequired[Dict[str, List[str]]]

class AdditionalDatasetTypeDef(TypedDict):
    Name: str
    Configuration: NotRequired[Mapping[str, Sequence[str]]]

class AttributeConfigOutputTypeDef(TypedDict):
    AttributeName: str
    Transformations: Dict[str, str]

class AttributeConfigTypeDef(TypedDict):
    AttributeName: str
    Transformations: Mapping[str, str]

class BaselineMetricTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[float]

class CategoricalParameterRangeOutputTypeDef(TypedDict):
    Name: str
    Values: List[str]

class CategoricalParameterRangeTypeDef(TypedDict):
    Name: str
    Values: Sequence[str]

class ContinuousParameterRangeTypeDef(TypedDict):
    Name: str
    MaxValue: float
    MinValue: float
    ScalingType: NotRequired[ScalingTypeType]

class EncryptionConfigTypeDef(TypedDict):
    RoleArn: str
    KMSKeyArn: str

class MonitorConfigTypeDef(TypedDict):
    MonitorName: str

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class TimeAlignmentBoundaryTypeDef(TypedDict):
    Month: NotRequired[MonthType]
    DayOfMonth: NotRequired[int]
    DayOfWeek: NotRequired[DayOfWeekType]
    Hour: NotRequired[int]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ExplainabilityConfigTypeDef(TypedDict):
    TimeSeriesGranularity: TimeSeriesGranularityType
    TimePointGranularity: TimePointGranularityType

class EvaluationParametersTypeDef(TypedDict):
    NumberOfBacktestWindows: NotRequired[int]
    BackTestWindowOffset: NotRequired[int]

class S3ConfigTypeDef(TypedDict):
    Path: str
    RoleArn: str
    KMSKeyArn: NotRequired[str]

class DatasetGroupSummaryTypeDef(TypedDict):
    DatasetGroupArn: NotRequired[str]
    DatasetGroupName: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastModificationTime: NotRequired[datetime]

class DatasetSummaryTypeDef(TypedDict):
    DatasetArn: NotRequired[str]
    DatasetName: NotRequired[str]
    DatasetType: NotRequired[DatasetTypeType]
    Domain: NotRequired[DomainType]
    CreationTime: NotRequired[datetime]
    LastModificationTime: NotRequired[datetime]

class DeleteDatasetGroupRequestTypeDef(TypedDict):
    DatasetGroupArn: str

class DeleteDatasetImportJobRequestTypeDef(TypedDict):
    DatasetImportJobArn: str

class DeleteDatasetRequestTypeDef(TypedDict):
    DatasetArn: str

class DeleteExplainabilityExportRequestTypeDef(TypedDict):
    ExplainabilityExportArn: str

class DeleteExplainabilityRequestTypeDef(TypedDict):
    ExplainabilityArn: str

class DeleteForecastExportJobRequestTypeDef(TypedDict):
    ForecastExportJobArn: str

class DeleteForecastRequestTypeDef(TypedDict):
    ForecastArn: str

class DeleteMonitorRequestTypeDef(TypedDict):
    MonitorArn: str

class DeletePredictorBacktestExportJobRequestTypeDef(TypedDict):
    PredictorBacktestExportJobArn: str

class DeletePredictorRequestTypeDef(TypedDict):
    PredictorArn: str

class DeleteResourceTreeRequestTypeDef(TypedDict):
    ResourceArn: str

class DeleteWhatIfAnalysisRequestTypeDef(TypedDict):
    WhatIfAnalysisArn: str

class DeleteWhatIfForecastExportRequestTypeDef(TypedDict):
    WhatIfForecastExportArn: str

class DeleteWhatIfForecastRequestTypeDef(TypedDict):
    WhatIfForecastArn: str

class DescribeAutoPredictorRequestTypeDef(TypedDict):
    PredictorArn: str

class ExplainabilityInfoTypeDef(TypedDict):
    ExplainabilityArn: NotRequired[str]
    Status: NotRequired[str]

class MonitorInfoTypeDef(TypedDict):
    MonitorArn: NotRequired[str]
    Status: NotRequired[str]

class ReferencePredictorSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    State: NotRequired[StateType]

class DescribeDatasetGroupRequestTypeDef(TypedDict):
    DatasetGroupArn: str

class DescribeDatasetImportJobRequestTypeDef(TypedDict):
    DatasetImportJobArn: str

class StatisticsTypeDef(TypedDict):
    Count: NotRequired[int]
    CountDistinct: NotRequired[int]
    CountNull: NotRequired[int]
    CountNan: NotRequired[int]
    Min: NotRequired[str]
    Max: NotRequired[str]
    Avg: NotRequired[float]
    Stddev: NotRequired[float]
    CountLong: NotRequired[int]
    CountDistinctLong: NotRequired[int]
    CountNullLong: NotRequired[int]
    CountNanLong: NotRequired[int]

class DescribeDatasetRequestTypeDef(TypedDict):
    DatasetArn: str

class DescribeExplainabilityExportRequestTypeDef(TypedDict):
    ExplainabilityExportArn: str

class DescribeExplainabilityRequestTypeDef(TypedDict):
    ExplainabilityArn: str

class DescribeForecastExportJobRequestTypeDef(TypedDict):
    ForecastExportJobArn: str

class DescribeForecastRequestTypeDef(TypedDict):
    ForecastArn: str

class DescribeMonitorRequestTypeDef(TypedDict):
    MonitorArn: str

class DescribePredictorBacktestExportJobRequestTypeDef(TypedDict):
    PredictorBacktestExportJobArn: str

class DescribePredictorRequestTypeDef(TypedDict):
    PredictorArn: str

class DescribeWhatIfAnalysisRequestTypeDef(TypedDict):
    WhatIfAnalysisArn: str

class DescribeWhatIfForecastExportRequestTypeDef(TypedDict):
    WhatIfForecastExportArn: str

class DescribeWhatIfForecastRequestTypeDef(TypedDict):
    WhatIfForecastArn: str

class ErrorMetricTypeDef(TypedDict):
    ForecastType: NotRequired[str]
    WAPE: NotRequired[float]
    RMSE: NotRequired[float]
    MASE: NotRequired[float]
    MAPE: NotRequired[float]

class FeaturizationMethodOutputTypeDef(TypedDict):
    FeaturizationMethodName: Literal["filling"]
    FeaturizationMethodParameters: NotRequired[Dict[str, str]]

class FeaturizationMethodTypeDef(TypedDict):
    FeaturizationMethodName: Literal["filling"]
    FeaturizationMethodParameters: NotRequired[Mapping[str, str]]

class FilterTypeDef(TypedDict):
    Key: str
    Value: str
    Condition: FilterConditionStringType

class ForecastSummaryTypeDef(TypedDict):
    ForecastArn: NotRequired[str]
    ForecastName: NotRequired[str]
    PredictorArn: NotRequired[str]
    CreatedUsingAutoPredictor: NotRequired[bool]
    DatasetGroupArn: NotRequired[str]
    Status: NotRequired[str]
    Message: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastModificationTime: NotRequired[datetime]

class GetAccuracyMetricsRequestTypeDef(TypedDict):
    PredictorArn: str

class SupplementaryFeatureTypeDef(TypedDict):
    Name: str
    Value: str

class IntegerParameterRangeTypeDef(TypedDict):
    Name: str
    MaxValue: int
    MinValue: int
    ScalingType: NotRequired[ScalingTypeType]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListDatasetGroupsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDatasetsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class MonitorSummaryTypeDef(TypedDict):
    MonitorArn: NotRequired[str]
    MonitorName: NotRequired[str]
    ResourceArn: NotRequired[str]
    Status: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastModificationTime: NotRequired[datetime]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class WhatIfAnalysisSummaryTypeDef(TypedDict):
    WhatIfAnalysisArn: NotRequired[str]
    WhatIfAnalysisName: NotRequired[str]
    ForecastArn: NotRequired[str]
    Status: NotRequired[str]
    Message: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastModificationTime: NotRequired[datetime]

class WhatIfForecastSummaryTypeDef(TypedDict):
    WhatIfForecastArn: NotRequired[str]
    WhatIfForecastName: NotRequired[str]
    WhatIfAnalysisArn: NotRequired[str]
    Status: NotRequired[str]
    Message: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastModificationTime: NotRequired[datetime]

class MetricResultTypeDef(TypedDict):
    MetricName: NotRequired[str]
    MetricValue: NotRequired[float]

class WeightedQuantileLossTypeDef(TypedDict):
    Quantile: NotRequired[float]
    LossValue: NotRequired[float]

class MonitorDataSourceTypeDef(TypedDict):
    DatasetImportJobArn: NotRequired[str]
    ForecastArn: NotRequired[str]
    PredictorArn: NotRequired[str]

class PredictorEventTypeDef(TypedDict):
    Detail: NotRequired[str]
    Datetime: NotRequired[datetime]

class TestWindowSummaryTypeDef(TypedDict):
    TestWindowStart: NotRequired[datetime]
    TestWindowEnd: NotRequired[datetime]
    Status: NotRequired[str]
    Message: NotRequired[str]

class ResumeResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class SchemaAttributeTypeDef(TypedDict):
    AttributeName: NotRequired[str]
    AttributeType: NotRequired[AttributeTypeType]

class StopResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class TimeSeriesConditionTypeDef(TypedDict):
    AttributeName: str
    AttributeValue: str
    Condition: ConditionType

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDatasetGroupRequestTypeDef(TypedDict):
    DatasetGroupArn: str
    DatasetArns: Sequence[str]

class DataConfigOutputTypeDef(TypedDict):
    DatasetGroupArn: str
    AttributeConfigs: NotRequired[List[AttributeConfigOutputTypeDef]]
    AdditionalDatasets: NotRequired[List[AdditionalDatasetOutputTypeDef]]

class DataConfigTypeDef(TypedDict):
    DatasetGroupArn: str
    AttributeConfigs: NotRequired[Sequence[AttributeConfigTypeDef]]
    AdditionalDatasets: NotRequired[Sequence[AdditionalDatasetTypeDef]]

class PredictorBaselineTypeDef(TypedDict):
    BaselineMetrics: NotRequired[List[BaselineMetricTypeDef]]

class CreateDatasetGroupRequestTypeDef(TypedDict):
    DatasetGroupName: str
    Domain: DomainType
    DatasetArns: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateMonitorRequestTypeDef(TypedDict):
    MonitorName: str
    ResourceArn: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateAutoPredictorResponseTypeDef(TypedDict):
    PredictorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetGroupResponseTypeDef(TypedDict):
    DatasetGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetImportJobResponseTypeDef(TypedDict):
    DatasetImportJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetResponseTypeDef(TypedDict):
    DatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExplainabilityExportResponseTypeDef(TypedDict):
    ExplainabilityExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExplainabilityResponseTypeDef(TypedDict):
    ExplainabilityArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateForecastExportJobResponseTypeDef(TypedDict):
    ForecastExportJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateForecastResponseTypeDef(TypedDict):
    ForecastArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMonitorResponseTypeDef(TypedDict):
    MonitorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePredictorBacktestExportJobResponseTypeDef(TypedDict):
    PredictorBacktestExportJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePredictorResponseTypeDef(TypedDict):
    PredictorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWhatIfAnalysisResponseTypeDef(TypedDict):
    WhatIfAnalysisArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWhatIfForecastExportResponseTypeDef(TypedDict):
    WhatIfForecastExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWhatIfForecastResponseTypeDef(TypedDict):
    WhatIfForecastArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDatasetGroupResponseTypeDef(TypedDict):
    DatasetGroupName: str
    DatasetGroupArn: str
    DatasetArns: List[str]
    Domain: DomainType
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ExplainabilitySummaryTypeDef(TypedDict):
    ExplainabilityArn: NotRequired[str]
    ExplainabilityName: NotRequired[str]
    ResourceArn: NotRequired[str]
    ExplainabilityConfig: NotRequired[ExplainabilityConfigTypeDef]
    Status: NotRequired[str]
    Message: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastModificationTime: NotRequired[datetime]

class DataDestinationTypeDef(TypedDict):
    S3Config: S3ConfigTypeDef

class DataSourceTypeDef(TypedDict):
    S3Config: S3ConfigTypeDef

class ListDatasetGroupsResponseTypeDef(TypedDict):
    DatasetGroups: List[DatasetGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDatasetsResponseTypeDef(TypedDict):
    Datasets: List[DatasetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PredictorSummaryTypeDef(TypedDict):
    PredictorArn: NotRequired[str]
    PredictorName: NotRequired[str]
    DatasetGroupArn: NotRequired[str]
    IsAutoPredictor: NotRequired[bool]
    ReferencePredictorSummary: NotRequired[ReferencePredictorSummaryTypeDef]
    Status: NotRequired[str]
    Message: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastModificationTime: NotRequired[datetime]

class FeaturizationOutputTypeDef(TypedDict):
    AttributeName: str
    FeaturizationPipeline: NotRequired[List[FeaturizationMethodOutputTypeDef]]

class FeaturizationTypeDef(TypedDict):
    AttributeName: str
    FeaturizationPipeline: NotRequired[Sequence[FeaturizationMethodTypeDef]]

class ListDatasetImportJobsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListExplainabilitiesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListExplainabilityExportsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListForecastExportJobsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListForecastsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListMonitorEvaluationsRequestTypeDef(TypedDict):
    MonitorArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListMonitorsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListPredictorBacktestExportJobsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListPredictorsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListWhatIfAnalysesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListWhatIfForecastExportsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListWhatIfForecastsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListForecastsResponseTypeDef(TypedDict):
    Forecasts: List[ForecastSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class InputDataConfigOutputTypeDef(TypedDict):
    DatasetGroupArn: str
    SupplementaryFeatures: NotRequired[List[SupplementaryFeatureTypeDef]]

class InputDataConfigTypeDef(TypedDict):
    DatasetGroupArn: str
    SupplementaryFeatures: NotRequired[Sequence[SupplementaryFeatureTypeDef]]

class ParameterRangesOutputTypeDef(TypedDict):
    CategoricalParameterRanges: NotRequired[List[CategoricalParameterRangeOutputTypeDef]]
    ContinuousParameterRanges: NotRequired[List[ContinuousParameterRangeTypeDef]]
    IntegerParameterRanges: NotRequired[List[IntegerParameterRangeTypeDef]]

class ParameterRangesTypeDef(TypedDict):
    CategoricalParameterRanges: NotRequired[Sequence[CategoricalParameterRangeTypeDef]]
    ContinuousParameterRanges: NotRequired[Sequence[ContinuousParameterRangeTypeDef]]
    IntegerParameterRanges: NotRequired[Sequence[IntegerParameterRangeTypeDef]]

class ListDatasetGroupsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDatasetImportJobsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDatasetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListExplainabilitiesRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListExplainabilityExportsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListForecastExportJobsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListForecastsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMonitorEvaluationsRequestPaginateTypeDef(TypedDict):
    MonitorArn: str
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMonitorsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPredictorBacktestExportJobsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPredictorsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWhatIfAnalysesRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWhatIfForecastExportsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWhatIfForecastsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMonitorsResponseTypeDef(TypedDict):
    Monitors: List[MonitorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListWhatIfAnalysesResponseTypeDef(TypedDict):
    WhatIfAnalyses: List[WhatIfAnalysisSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListWhatIfForecastsResponseTypeDef(TypedDict):
    WhatIfForecasts: List[WhatIfForecastSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class MetricsTypeDef(TypedDict):
    RMSE: NotRequired[float]
    WeightedQuantileLosses: NotRequired[List[WeightedQuantileLossTypeDef]]
    ErrorMetrics: NotRequired[List[ErrorMetricTypeDef]]
    AverageWeightedQuantileLoss: NotRequired[float]

class PredictorMonitorEvaluationTypeDef(TypedDict):
    ResourceArn: NotRequired[str]
    MonitorArn: NotRequired[str]
    EvaluationTime: NotRequired[datetime]
    EvaluationState: NotRequired[str]
    WindowStartDatetime: NotRequired[datetime]
    WindowEndDatetime: NotRequired[datetime]
    PredictorEvent: NotRequired[PredictorEventTypeDef]
    MonitorDataSource: NotRequired[MonitorDataSourceTypeDef]
    MetricResults: NotRequired[List[MetricResultTypeDef]]
    NumItemsEvaluated: NotRequired[int]
    Message: NotRequired[str]

class PredictorExecutionTypeDef(TypedDict):
    AlgorithmArn: NotRequired[str]
    TestWindows: NotRequired[List[TestWindowSummaryTypeDef]]

class SchemaOutputTypeDef(TypedDict):
    Attributes: NotRequired[List[SchemaAttributeTypeDef]]

class SchemaTypeDef(TypedDict):
    Attributes: NotRequired[Sequence[SchemaAttributeTypeDef]]

class TimeSeriesTransformationOutputTypeDef(TypedDict):
    Action: NotRequired[ActionTypeDef]
    TimeSeriesConditions: NotRequired[List[TimeSeriesConditionTypeDef]]

class TimeSeriesTransformationTypeDef(TypedDict):
    Action: NotRequired[ActionTypeDef]
    TimeSeriesConditions: NotRequired[Sequence[TimeSeriesConditionTypeDef]]

class DescribeAutoPredictorResponseTypeDef(TypedDict):
    PredictorArn: str
    PredictorName: str
    ForecastHorizon: int
    ForecastTypes: List[str]
    ForecastFrequency: str
    ForecastDimensions: List[str]
    DatasetImportJobArns: List[str]
    DataConfig: DataConfigOutputTypeDef
    EncryptionConfig: EncryptionConfigTypeDef
    ReferencePredictorSummary: ReferencePredictorSummaryTypeDef
    EstimatedTimeRemainingInMinutes: int
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    OptimizationMetric: OptimizationMetricType
    ExplainabilityInfo: ExplainabilityInfoTypeDef
    MonitorInfo: MonitorInfoTypeDef
    TimeAlignmentBoundary: TimeAlignmentBoundaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

DataConfigUnionTypeDef = Union[DataConfigTypeDef, DataConfigOutputTypeDef]

class BaselineTypeDef(TypedDict):
    PredictorBaseline: NotRequired[PredictorBaselineTypeDef]

class ListExplainabilitiesResponseTypeDef(TypedDict):
    Explainabilities: List[ExplainabilitySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateExplainabilityExportRequestTypeDef(TypedDict):
    ExplainabilityExportName: str
    ExplainabilityArn: str
    Destination: DataDestinationTypeDef
    Tags: NotRequired[Sequence[TagTypeDef]]
    Format: NotRequired[str]

class CreateForecastExportJobRequestTypeDef(TypedDict):
    ForecastExportJobName: str
    ForecastArn: str
    Destination: DataDestinationTypeDef
    Tags: NotRequired[Sequence[TagTypeDef]]
    Format: NotRequired[str]

class CreatePredictorBacktestExportJobRequestTypeDef(TypedDict):
    PredictorBacktestExportJobName: str
    PredictorArn: str
    Destination: DataDestinationTypeDef
    Tags: NotRequired[Sequence[TagTypeDef]]
    Format: NotRequired[str]

class CreateWhatIfForecastExportRequestTypeDef(TypedDict):
    WhatIfForecastExportName: str
    WhatIfForecastArns: Sequence[str]
    Destination: DataDestinationTypeDef
    Tags: NotRequired[Sequence[TagTypeDef]]
    Format: NotRequired[str]

class DescribeExplainabilityExportResponseTypeDef(TypedDict):
    ExplainabilityExportArn: str
    ExplainabilityExportName: str
    ExplainabilityArn: str
    Destination: DataDestinationTypeDef
    Message: str
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    Format: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeForecastExportJobResponseTypeDef(TypedDict):
    ForecastExportJobArn: str
    ForecastExportJobName: str
    ForecastArn: str
    Destination: DataDestinationTypeDef
    Message: str
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    Format: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePredictorBacktestExportJobResponseTypeDef(TypedDict):
    PredictorBacktestExportJobArn: str
    PredictorBacktestExportJobName: str
    PredictorArn: str
    Destination: DataDestinationTypeDef
    Message: str
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    Format: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWhatIfForecastExportResponseTypeDef(TypedDict):
    WhatIfForecastExportArn: str
    WhatIfForecastExportName: str
    WhatIfForecastArns: List[str]
    Destination: DataDestinationTypeDef
    Message: str
    Status: str
    CreationTime: datetime
    EstimatedTimeRemainingInMinutes: int
    LastModificationTime: datetime
    Format: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExplainabilityExportSummaryTypeDef(TypedDict):
    ExplainabilityExportArn: NotRequired[str]
    ExplainabilityExportName: NotRequired[str]
    Destination: NotRequired[DataDestinationTypeDef]
    Status: NotRequired[str]
    Message: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastModificationTime: NotRequired[datetime]

class ForecastExportJobSummaryTypeDef(TypedDict):
    ForecastExportJobArn: NotRequired[str]
    ForecastExportJobName: NotRequired[str]
    Destination: NotRequired[DataDestinationTypeDef]
    Status: NotRequired[str]
    Message: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastModificationTime: NotRequired[datetime]

class PredictorBacktestExportJobSummaryTypeDef(TypedDict):
    PredictorBacktestExportJobArn: NotRequired[str]
    PredictorBacktestExportJobName: NotRequired[str]
    Destination: NotRequired[DataDestinationTypeDef]
    Status: NotRequired[str]
    Message: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastModificationTime: NotRequired[datetime]

class WhatIfForecastExportSummaryTypeDef(TypedDict):
    WhatIfForecastExportArn: NotRequired[str]
    WhatIfForecastArns: NotRequired[List[str]]
    WhatIfForecastExportName: NotRequired[str]
    Destination: NotRequired[DataDestinationTypeDef]
    Status: NotRequired[str]
    Message: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastModificationTime: NotRequired[datetime]

class CreateDatasetImportJobRequestTypeDef(TypedDict):
    DatasetImportJobName: str
    DatasetArn: str
    DataSource: DataSourceTypeDef
    TimestampFormat: NotRequired[str]
    TimeZone: NotRequired[str]
    UseGeolocationForTimeZone: NotRequired[bool]
    GeolocationFormat: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    Format: NotRequired[str]
    ImportMode: NotRequired[ImportModeType]

class DatasetImportJobSummaryTypeDef(TypedDict):
    DatasetImportJobArn: NotRequired[str]
    DatasetImportJobName: NotRequired[str]
    DataSource: NotRequired[DataSourceTypeDef]
    Status: NotRequired[str]
    Message: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastModificationTime: NotRequired[datetime]
    ImportMode: NotRequired[ImportModeType]

class DescribeDatasetImportJobResponseTypeDef(TypedDict):
    DatasetImportJobName: str
    DatasetImportJobArn: str
    DatasetArn: str
    TimestampFormat: str
    TimeZone: str
    UseGeolocationForTimeZone: bool
    GeolocationFormat: str
    DataSource: DataSourceTypeDef
    EstimatedTimeRemainingInMinutes: int
    FieldStatistics: Dict[str, StatisticsTypeDef]
    DataSize: float
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    Format: str
    ImportMode: ImportModeType
    ResponseMetadata: ResponseMetadataTypeDef

class ListPredictorsResponseTypeDef(TypedDict):
    Predictors: List[PredictorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class FeaturizationConfigOutputTypeDef(TypedDict):
    ForecastFrequency: str
    ForecastDimensions: NotRequired[List[str]]
    Featurizations: NotRequired[List[FeaturizationOutputTypeDef]]

class FeaturizationConfigTypeDef(TypedDict):
    ForecastFrequency: str
    ForecastDimensions: NotRequired[Sequence[str]]
    Featurizations: NotRequired[Sequence[FeaturizationTypeDef]]

InputDataConfigUnionTypeDef = Union[InputDataConfigTypeDef, InputDataConfigOutputTypeDef]

class HyperParameterTuningJobConfigOutputTypeDef(TypedDict):
    ParameterRanges: NotRequired[ParameterRangesOutputTypeDef]

class HyperParameterTuningJobConfigTypeDef(TypedDict):
    ParameterRanges: NotRequired[ParameterRangesTypeDef]

class WindowSummaryTypeDef(TypedDict):
    TestWindowStart: NotRequired[datetime]
    TestWindowEnd: NotRequired[datetime]
    ItemCount: NotRequired[int]
    EvaluationType: NotRequired[EvaluationTypeType]
    Metrics: NotRequired[MetricsTypeDef]

class ListMonitorEvaluationsResponseTypeDef(TypedDict):
    PredictorMonitorEvaluations: List[PredictorMonitorEvaluationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PredictorExecutionDetailsTypeDef(TypedDict):
    PredictorExecutions: NotRequired[List[PredictorExecutionTypeDef]]

class DescribeDatasetResponseTypeDef(TypedDict):
    DatasetArn: str
    DatasetName: str
    Domain: DomainType
    DatasetType: DatasetTypeType
    DataFrequency: str
    Schema: SchemaOutputTypeDef
    EncryptionConfig: EncryptionConfigTypeDef
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExplainabilityResponseTypeDef(TypedDict):
    ExplainabilityArn: str
    ExplainabilityName: str
    ResourceArn: str
    ExplainabilityConfig: ExplainabilityConfigTypeDef
    EnableVisualization: bool
    DataSource: DataSourceTypeDef
    Schema: SchemaOutputTypeDef
    StartDateTime: str
    EndDateTime: str
    EstimatedTimeRemainingInMinutes: int
    Message: str
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class TimeSeriesIdentifiersOutputTypeDef(TypedDict):
    DataSource: NotRequired[DataSourceTypeDef]
    Schema: NotRequired[SchemaOutputTypeDef]
    Format: NotRequired[str]

class TimeSeriesReplacementsDataSourceOutputTypeDef(TypedDict):
    S3Config: S3ConfigTypeDef
    Schema: SchemaOutputTypeDef
    Format: NotRequired[str]
    TimestampFormat: NotRequired[str]

SchemaUnionTypeDef = Union[SchemaTypeDef, SchemaOutputTypeDef]

class TimeSeriesIdentifiersTypeDef(TypedDict):
    DataSource: NotRequired[DataSourceTypeDef]
    Schema: NotRequired[SchemaTypeDef]
    Format: NotRequired[str]

class TimeSeriesReplacementsDataSourceTypeDef(TypedDict):
    S3Config: S3ConfigTypeDef
    Schema: SchemaTypeDef
    Format: NotRequired[str]
    TimestampFormat: NotRequired[str]

TimeSeriesTransformationUnionTypeDef = Union[
    TimeSeriesTransformationTypeDef, TimeSeriesTransformationOutputTypeDef
]

class CreateAutoPredictorRequestTypeDef(TypedDict):
    PredictorName: str
    ForecastHorizon: NotRequired[int]
    ForecastTypes: NotRequired[Sequence[str]]
    ForecastDimensions: NotRequired[Sequence[str]]
    ForecastFrequency: NotRequired[str]
    DataConfig: NotRequired[DataConfigUnionTypeDef]
    EncryptionConfig: NotRequired[EncryptionConfigTypeDef]
    ReferencePredictorArn: NotRequired[str]
    OptimizationMetric: NotRequired[OptimizationMetricType]
    ExplainPredictor: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]
    MonitorConfig: NotRequired[MonitorConfigTypeDef]
    TimeAlignmentBoundary: NotRequired[TimeAlignmentBoundaryTypeDef]

class DescribeMonitorResponseTypeDef(TypedDict):
    MonitorName: str
    MonitorArn: str
    ResourceArn: str
    Status: str
    LastEvaluationTime: datetime
    LastEvaluationState: str
    Baseline: BaselineTypeDef
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    EstimatedEvaluationTimeRemainingInMinutes: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListExplainabilityExportsResponseTypeDef(TypedDict):
    ExplainabilityExports: List[ExplainabilityExportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListForecastExportJobsResponseTypeDef(TypedDict):
    ForecastExportJobs: List[ForecastExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPredictorBacktestExportJobsResponseTypeDef(TypedDict):
    PredictorBacktestExportJobs: List[PredictorBacktestExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListWhatIfForecastExportsResponseTypeDef(TypedDict):
    WhatIfForecastExports: List[WhatIfForecastExportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDatasetImportJobsResponseTypeDef(TypedDict):
    DatasetImportJobs: List[DatasetImportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

FeaturizationConfigUnionTypeDef = Union[
    FeaturizationConfigTypeDef, FeaturizationConfigOutputTypeDef
]
HyperParameterTuningJobConfigUnionTypeDef = Union[
    HyperParameterTuningJobConfigTypeDef, HyperParameterTuningJobConfigOutputTypeDef
]

class EvaluationResultTypeDef(TypedDict):
    AlgorithmArn: NotRequired[str]
    TestWindows: NotRequired[List[WindowSummaryTypeDef]]

class DescribePredictorResponseTypeDef(TypedDict):
    PredictorArn: str
    PredictorName: str
    AlgorithmArn: str
    AutoMLAlgorithmArns: List[str]
    ForecastHorizon: int
    ForecastTypes: List[str]
    PerformAutoML: bool
    AutoMLOverrideStrategy: AutoMLOverrideStrategyType
    PerformHPO: bool
    TrainingParameters: Dict[str, str]
    EvaluationParameters: EvaluationParametersTypeDef
    HPOConfig: HyperParameterTuningJobConfigOutputTypeDef
    InputDataConfig: InputDataConfigOutputTypeDef
    FeaturizationConfig: FeaturizationConfigOutputTypeDef
    EncryptionConfig: EncryptionConfigTypeDef
    PredictorExecutionDetails: PredictorExecutionDetailsTypeDef
    EstimatedTimeRemainingInMinutes: int
    IsAutoPredictor: bool
    DatasetImportJobArns: List[str]
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    OptimizationMetric: OptimizationMetricType
    ResponseMetadata: ResponseMetadataTypeDef

class TimeSeriesSelectorOutputTypeDef(TypedDict):
    TimeSeriesIdentifiers: NotRequired[TimeSeriesIdentifiersOutputTypeDef]

class DescribeWhatIfForecastResponseTypeDef(TypedDict):
    WhatIfForecastName: str
    WhatIfForecastArn: str
    WhatIfAnalysisArn: str
    EstimatedTimeRemainingInMinutes: int
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    TimeSeriesTransformations: List[TimeSeriesTransformationOutputTypeDef]
    TimeSeriesReplacementsDataSource: TimeSeriesReplacementsDataSourceOutputTypeDef
    ForecastTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetRequestTypeDef(TypedDict):
    DatasetName: str
    Domain: DomainType
    DatasetType: DatasetTypeType
    Schema: SchemaUnionTypeDef
    DataFrequency: NotRequired[str]
    EncryptionConfig: NotRequired[EncryptionConfigTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateExplainabilityRequestTypeDef(TypedDict):
    ExplainabilityName: str
    ResourceArn: str
    ExplainabilityConfig: ExplainabilityConfigTypeDef
    DataSource: NotRequired[DataSourceTypeDef]
    Schema: NotRequired[SchemaUnionTypeDef]
    EnableVisualization: NotRequired[bool]
    StartDateTime: NotRequired[str]
    EndDateTime: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class TimeSeriesSelectorTypeDef(TypedDict):
    TimeSeriesIdentifiers: NotRequired[TimeSeriesIdentifiersTypeDef]

TimeSeriesReplacementsDataSourceUnionTypeDef = Union[
    TimeSeriesReplacementsDataSourceTypeDef, TimeSeriesReplacementsDataSourceOutputTypeDef
]

class CreatePredictorRequestTypeDef(TypedDict):
    PredictorName: str
    ForecastHorizon: int
    InputDataConfig: InputDataConfigUnionTypeDef
    FeaturizationConfig: FeaturizationConfigUnionTypeDef
    AlgorithmArn: NotRequired[str]
    ForecastTypes: NotRequired[Sequence[str]]
    PerformAutoML: NotRequired[bool]
    AutoMLOverrideStrategy: NotRequired[AutoMLOverrideStrategyType]
    PerformHPO: NotRequired[bool]
    TrainingParameters: NotRequired[Mapping[str, str]]
    EvaluationParameters: NotRequired[EvaluationParametersTypeDef]
    HPOConfig: NotRequired[HyperParameterTuningJobConfigUnionTypeDef]
    EncryptionConfig: NotRequired[EncryptionConfigTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    OptimizationMetric: NotRequired[OptimizationMetricType]

class GetAccuracyMetricsResponseTypeDef(TypedDict):
    PredictorEvaluationResults: List[EvaluationResultTypeDef]
    IsAutoPredictor: bool
    AutoMLOverrideStrategy: AutoMLOverrideStrategyType
    OptimizationMetric: OptimizationMetricType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeForecastResponseTypeDef(TypedDict):
    ForecastArn: str
    ForecastName: str
    ForecastTypes: List[str]
    PredictorArn: str
    DatasetGroupArn: str
    EstimatedTimeRemainingInMinutes: int
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    TimeSeriesSelector: TimeSeriesSelectorOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWhatIfAnalysisResponseTypeDef(TypedDict):
    WhatIfAnalysisName: str
    WhatIfAnalysisArn: str
    ForecastArn: str
    EstimatedTimeRemainingInMinutes: int
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime
    TimeSeriesSelector: TimeSeriesSelectorOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

TimeSeriesSelectorUnionTypeDef = Union[TimeSeriesSelectorTypeDef, TimeSeriesSelectorOutputTypeDef]

class CreateWhatIfForecastRequestTypeDef(TypedDict):
    WhatIfForecastName: str
    WhatIfAnalysisArn: str
    TimeSeriesTransformations: NotRequired[Sequence[TimeSeriesTransformationUnionTypeDef]]
    TimeSeriesReplacementsDataSource: NotRequired[TimeSeriesReplacementsDataSourceUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateForecastRequestTypeDef(TypedDict):
    ForecastName: str
    PredictorArn: str
    ForecastTypes: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    TimeSeriesSelector: NotRequired[TimeSeriesSelectorUnionTypeDef]

class CreateWhatIfAnalysisRequestTypeDef(TypedDict):
    WhatIfAnalysisName: str
    ForecastArn: str
    TimeSeriesSelector: NotRequired[TimeSeriesSelectorUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
