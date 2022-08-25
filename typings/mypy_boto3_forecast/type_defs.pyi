"""
Type annotations for forecast service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/type_defs.html)

Usage::

    ```python
    from mypy_boto3_forecast.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AttributeTypeType,
    AutoMLOverrideStrategyType,
    ConditionType,
    DatasetTypeType,
    DayOfWeekType,
    DomainType,
    EvaluationTypeType,
    FilterConditionStringType,
    MonthType,
    OperationType,
    OptimizationMetricType,
    ScalingTypeType,
    StateType,
    TimePointGranularityType,
    TimeSeriesGranularityType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ActionTypeDef",
    "AdditionalDatasetTypeDef",
    "AttributeConfigTypeDef",
    "BaselineMetricTypeDef",
    "BaselineTypeDef",
    "CategoricalParameterRangeTypeDef",
    "ContinuousParameterRangeTypeDef",
    "CreateAutoPredictorRequestRequestTypeDef",
    "CreateAutoPredictorResponseTypeDef",
    "CreateDatasetGroupRequestRequestTypeDef",
    "CreateDatasetGroupResponseTypeDef",
    "CreateDatasetImportJobRequestRequestTypeDef",
    "CreateDatasetImportJobResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateExplainabilityExportRequestRequestTypeDef",
    "CreateExplainabilityExportResponseTypeDef",
    "CreateExplainabilityRequestRequestTypeDef",
    "CreateExplainabilityResponseTypeDef",
    "CreateForecastExportJobRequestRequestTypeDef",
    "CreateForecastExportJobResponseTypeDef",
    "CreateForecastRequestRequestTypeDef",
    "CreateForecastResponseTypeDef",
    "CreateMonitorRequestRequestTypeDef",
    "CreateMonitorResponseTypeDef",
    "CreatePredictorBacktestExportJobRequestRequestTypeDef",
    "CreatePredictorBacktestExportJobResponseTypeDef",
    "CreatePredictorRequestRequestTypeDef",
    "CreatePredictorResponseTypeDef",
    "CreateWhatIfAnalysisRequestRequestTypeDef",
    "CreateWhatIfAnalysisResponseTypeDef",
    "CreateWhatIfForecastExportRequestRequestTypeDef",
    "CreateWhatIfForecastExportResponseTypeDef",
    "CreateWhatIfForecastRequestRequestTypeDef",
    "CreateWhatIfForecastResponseTypeDef",
    "DataConfigTypeDef",
    "DataDestinationTypeDef",
    "DataSourceTypeDef",
    "DatasetGroupSummaryTypeDef",
    "DatasetImportJobSummaryTypeDef",
    "DatasetSummaryTypeDef",
    "DeleteDatasetGroupRequestRequestTypeDef",
    "DeleteDatasetImportJobRequestRequestTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteExplainabilityExportRequestRequestTypeDef",
    "DeleteExplainabilityRequestRequestTypeDef",
    "DeleteForecastExportJobRequestRequestTypeDef",
    "DeleteForecastRequestRequestTypeDef",
    "DeleteMonitorRequestRequestTypeDef",
    "DeletePredictorBacktestExportJobRequestRequestTypeDef",
    "DeletePredictorRequestRequestTypeDef",
    "DeleteResourceTreeRequestRequestTypeDef",
    "DeleteWhatIfAnalysisRequestRequestTypeDef",
    "DeleteWhatIfForecastExportRequestRequestTypeDef",
    "DeleteWhatIfForecastRequestRequestTypeDef",
    "DescribeAutoPredictorRequestRequestTypeDef",
    "DescribeAutoPredictorResponseTypeDef",
    "DescribeDatasetGroupRequestRequestTypeDef",
    "DescribeDatasetGroupResponseTypeDef",
    "DescribeDatasetImportJobRequestRequestTypeDef",
    "DescribeDatasetImportJobResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeExplainabilityExportRequestRequestTypeDef",
    "DescribeExplainabilityExportResponseTypeDef",
    "DescribeExplainabilityRequestRequestTypeDef",
    "DescribeExplainabilityResponseTypeDef",
    "DescribeForecastExportJobRequestRequestTypeDef",
    "DescribeForecastExportJobResponseTypeDef",
    "DescribeForecastRequestRequestTypeDef",
    "DescribeForecastResponseTypeDef",
    "DescribeMonitorRequestRequestTypeDef",
    "DescribeMonitorResponseTypeDef",
    "DescribePredictorBacktestExportJobRequestRequestTypeDef",
    "DescribePredictorBacktestExportJobResponseTypeDef",
    "DescribePredictorRequestRequestTypeDef",
    "DescribePredictorResponseTypeDef",
    "DescribeWhatIfAnalysisRequestRequestTypeDef",
    "DescribeWhatIfAnalysisResponseTypeDef",
    "DescribeWhatIfForecastExportRequestRequestTypeDef",
    "DescribeWhatIfForecastExportResponseTypeDef",
    "DescribeWhatIfForecastRequestRequestTypeDef",
    "DescribeWhatIfForecastResponseTypeDef",
    "EncryptionConfigTypeDef",
    "ErrorMetricTypeDef",
    "EvaluationParametersTypeDef",
    "EvaluationResultTypeDef",
    "ExplainabilityConfigTypeDef",
    "ExplainabilityExportSummaryTypeDef",
    "ExplainabilityInfoTypeDef",
    "ExplainabilitySummaryTypeDef",
    "FeaturizationConfigTypeDef",
    "FeaturizationMethodTypeDef",
    "FeaturizationTypeDef",
    "FilterTypeDef",
    "ForecastExportJobSummaryTypeDef",
    "ForecastSummaryTypeDef",
    "GetAccuracyMetricsRequestRequestTypeDef",
    "GetAccuracyMetricsResponseTypeDef",
    "HyperParameterTuningJobConfigTypeDef",
    "InputDataConfigTypeDef",
    "IntegerParameterRangeTypeDef",
    "ListDatasetGroupsRequestRequestTypeDef",
    "ListDatasetGroupsResponseTypeDef",
    "ListDatasetImportJobsRequestRequestTypeDef",
    "ListDatasetImportJobsResponseTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListExplainabilitiesRequestRequestTypeDef",
    "ListExplainabilitiesResponseTypeDef",
    "ListExplainabilityExportsRequestRequestTypeDef",
    "ListExplainabilityExportsResponseTypeDef",
    "ListForecastExportJobsRequestRequestTypeDef",
    "ListForecastExportJobsResponseTypeDef",
    "ListForecastsRequestRequestTypeDef",
    "ListForecastsResponseTypeDef",
    "ListMonitorEvaluationsRequestRequestTypeDef",
    "ListMonitorEvaluationsResponseTypeDef",
    "ListMonitorsRequestRequestTypeDef",
    "ListMonitorsResponseTypeDef",
    "ListPredictorBacktestExportJobsRequestRequestTypeDef",
    "ListPredictorBacktestExportJobsResponseTypeDef",
    "ListPredictorsRequestRequestTypeDef",
    "ListPredictorsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWhatIfAnalysesRequestRequestTypeDef",
    "ListWhatIfAnalysesResponseTypeDef",
    "ListWhatIfForecastExportsRequestRequestTypeDef",
    "ListWhatIfForecastExportsResponseTypeDef",
    "ListWhatIfForecastsRequestRequestTypeDef",
    "ListWhatIfForecastsResponseTypeDef",
    "MetricResultTypeDef",
    "MetricsTypeDef",
    "MonitorConfigTypeDef",
    "MonitorDataSourceTypeDef",
    "MonitorInfoTypeDef",
    "MonitorSummaryTypeDef",
    "PaginatorConfigTypeDef",
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
    "ResumeResourceRequestRequestTypeDef",
    "S3ConfigTypeDef",
    "SchemaAttributeTypeDef",
    "SchemaTypeDef",
    "StatisticsTypeDef",
    "StopResourceRequestRequestTypeDef",
    "SupplementaryFeatureTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TestWindowSummaryTypeDef",
    "TimeAlignmentBoundaryTypeDef",
    "TimeSeriesConditionTypeDef",
    "TimeSeriesIdentifiersTypeDef",
    "TimeSeriesReplacementsDataSourceTypeDef",
    "TimeSeriesSelectorTypeDef",
    "TimeSeriesTransformationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatasetGroupRequestRequestTypeDef",
    "WeightedQuantileLossTypeDef",
    "WhatIfAnalysisSummaryTypeDef",
    "WhatIfForecastExportSummaryTypeDef",
    "WhatIfForecastSummaryTypeDef",
    "WindowSummaryTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "AttributeName": str,
        "Operation": OperationType,
        "Value": float,
    },
)

_RequiredAdditionalDatasetTypeDef = TypedDict(
    "_RequiredAdditionalDatasetTypeDef",
    {
        "Name": str,
    },
)
_OptionalAdditionalDatasetTypeDef = TypedDict(
    "_OptionalAdditionalDatasetTypeDef",
    {
        "Configuration": Dict[str, List[str]],
    },
    total=False,
)

class AdditionalDatasetTypeDef(
    _RequiredAdditionalDatasetTypeDef, _OptionalAdditionalDatasetTypeDef
):
    pass

AttributeConfigTypeDef = TypedDict(
    "AttributeConfigTypeDef",
    {
        "AttributeName": str,
        "Transformations": Dict[str, str],
    },
)

BaselineMetricTypeDef = TypedDict(
    "BaselineMetricTypeDef",
    {
        "Name": str,
        "Value": float,
    },
    total=False,
)

BaselineTypeDef = TypedDict(
    "BaselineTypeDef",
    {
        "PredictorBaseline": "PredictorBaselineTypeDef",
    },
    total=False,
)

CategoricalParameterRangeTypeDef = TypedDict(
    "CategoricalParameterRangeTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
)

_RequiredContinuousParameterRangeTypeDef = TypedDict(
    "_RequiredContinuousParameterRangeTypeDef",
    {
        "Name": str,
        "MaxValue": float,
        "MinValue": float,
    },
)
_OptionalContinuousParameterRangeTypeDef = TypedDict(
    "_OptionalContinuousParameterRangeTypeDef",
    {
        "ScalingType": ScalingTypeType,
    },
    total=False,
)

class ContinuousParameterRangeTypeDef(
    _RequiredContinuousParameterRangeTypeDef, _OptionalContinuousParameterRangeTypeDef
):
    pass

_RequiredCreateAutoPredictorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAutoPredictorRequestRequestTypeDef",
    {
        "PredictorName": str,
    },
)
_OptionalCreateAutoPredictorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAutoPredictorRequestRequestTypeDef",
    {
        "ForecastHorizon": int,
        "ForecastTypes": List[str],
        "ForecastDimensions": List[str],
        "ForecastFrequency": str,
        "DataConfig": "DataConfigTypeDef",
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "ReferencePredictorArn": str,
        "OptimizationMetric": OptimizationMetricType,
        "ExplainPredictor": bool,
        "Tags": List["TagTypeDef"],
        "MonitorConfig": "MonitorConfigTypeDef",
        "TimeAlignmentBoundary": "TimeAlignmentBoundaryTypeDef",
    },
    total=False,
)

class CreateAutoPredictorRequestRequestTypeDef(
    _RequiredCreateAutoPredictorRequestRequestTypeDef,
    _OptionalCreateAutoPredictorRequestRequestTypeDef,
):
    pass

CreateAutoPredictorResponseTypeDef = TypedDict(
    "CreateAutoPredictorResponseTypeDef",
    {
        "PredictorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetGroupRequestRequestTypeDef",
    {
        "DatasetGroupName": str,
        "Domain": DomainType,
    },
)
_OptionalCreateDatasetGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetGroupRequestRequestTypeDef",
    {
        "DatasetArns": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDatasetGroupRequestRequestTypeDef(
    _RequiredCreateDatasetGroupRequestRequestTypeDef,
    _OptionalCreateDatasetGroupRequestRequestTypeDef,
):
    pass

CreateDatasetGroupResponseTypeDef = TypedDict(
    "CreateDatasetGroupResponseTypeDef",
    {
        "DatasetGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetImportJobRequestRequestTypeDef",
    {
        "DatasetImportJobName": str,
        "DatasetArn": str,
        "DataSource": "DataSourceTypeDef",
    },
)
_OptionalCreateDatasetImportJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetImportJobRequestRequestTypeDef",
    {
        "TimestampFormat": str,
        "TimeZone": str,
        "UseGeolocationForTimeZone": bool,
        "GeolocationFormat": str,
        "Tags": List["TagTypeDef"],
        "Format": str,
    },
    total=False,
)

class CreateDatasetImportJobRequestRequestTypeDef(
    _RequiredCreateDatasetImportJobRequestRequestTypeDef,
    _OptionalCreateDatasetImportJobRequestRequestTypeDef,
):
    pass

CreateDatasetImportJobResponseTypeDef = TypedDict(
    "CreateDatasetImportJobResponseTypeDef",
    {
        "DatasetImportJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestRequestTypeDef",
    {
        "DatasetName": str,
        "Domain": DomainType,
        "DatasetType": DatasetTypeType,
        "Schema": "SchemaTypeDef",
    },
)
_OptionalCreateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestRequestTypeDef",
    {
        "DataFrequency": str,
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDatasetRequestRequestTypeDef(
    _RequiredCreateDatasetRequestRequestTypeDef, _OptionalCreateDatasetRequestRequestTypeDef
):
    pass

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "DatasetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateExplainabilityExportRequestRequestTypeDef = TypedDict(
    "_RequiredCreateExplainabilityExportRequestRequestTypeDef",
    {
        "ExplainabilityExportName": str,
        "ExplainabilityArn": str,
        "Destination": "DataDestinationTypeDef",
    },
)
_OptionalCreateExplainabilityExportRequestRequestTypeDef = TypedDict(
    "_OptionalCreateExplainabilityExportRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "Format": str,
    },
    total=False,
)

class CreateExplainabilityExportRequestRequestTypeDef(
    _RequiredCreateExplainabilityExportRequestRequestTypeDef,
    _OptionalCreateExplainabilityExportRequestRequestTypeDef,
):
    pass

CreateExplainabilityExportResponseTypeDef = TypedDict(
    "CreateExplainabilityExportResponseTypeDef",
    {
        "ExplainabilityExportArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateExplainabilityRequestRequestTypeDef = TypedDict(
    "_RequiredCreateExplainabilityRequestRequestTypeDef",
    {
        "ExplainabilityName": str,
        "ResourceArn": str,
        "ExplainabilityConfig": "ExplainabilityConfigTypeDef",
    },
)
_OptionalCreateExplainabilityRequestRequestTypeDef = TypedDict(
    "_OptionalCreateExplainabilityRequestRequestTypeDef",
    {
        "DataSource": "DataSourceTypeDef",
        "Schema": "SchemaTypeDef",
        "EnableVisualization": bool,
        "StartDateTime": str,
        "EndDateTime": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateExplainabilityRequestRequestTypeDef(
    _RequiredCreateExplainabilityRequestRequestTypeDef,
    _OptionalCreateExplainabilityRequestRequestTypeDef,
):
    pass

CreateExplainabilityResponseTypeDef = TypedDict(
    "CreateExplainabilityResponseTypeDef",
    {
        "ExplainabilityArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateForecastExportJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateForecastExportJobRequestRequestTypeDef",
    {
        "ForecastExportJobName": str,
        "ForecastArn": str,
        "Destination": "DataDestinationTypeDef",
    },
)
_OptionalCreateForecastExportJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateForecastExportJobRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "Format": str,
    },
    total=False,
)

class CreateForecastExportJobRequestRequestTypeDef(
    _RequiredCreateForecastExportJobRequestRequestTypeDef,
    _OptionalCreateForecastExportJobRequestRequestTypeDef,
):
    pass

CreateForecastExportJobResponseTypeDef = TypedDict(
    "CreateForecastExportJobResponseTypeDef",
    {
        "ForecastExportJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateForecastRequestRequestTypeDef = TypedDict(
    "_RequiredCreateForecastRequestRequestTypeDef",
    {
        "ForecastName": str,
        "PredictorArn": str,
    },
)
_OptionalCreateForecastRequestRequestTypeDef = TypedDict(
    "_OptionalCreateForecastRequestRequestTypeDef",
    {
        "ForecastTypes": List[str],
        "Tags": List["TagTypeDef"],
        "TimeSeriesSelector": "TimeSeriesSelectorTypeDef",
    },
    total=False,
)

class CreateForecastRequestRequestTypeDef(
    _RequiredCreateForecastRequestRequestTypeDef, _OptionalCreateForecastRequestRequestTypeDef
):
    pass

CreateForecastResponseTypeDef = TypedDict(
    "CreateForecastResponseTypeDef",
    {
        "ForecastArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMonitorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMonitorRequestRequestTypeDef",
    {
        "MonitorName": str,
        "ResourceArn": str,
    },
)
_OptionalCreateMonitorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMonitorRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateMonitorRequestRequestTypeDef(
    _RequiredCreateMonitorRequestRequestTypeDef, _OptionalCreateMonitorRequestRequestTypeDef
):
    pass

CreateMonitorResponseTypeDef = TypedDict(
    "CreateMonitorResponseTypeDef",
    {
        "MonitorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePredictorBacktestExportJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePredictorBacktestExportJobRequestRequestTypeDef",
    {
        "PredictorBacktestExportJobName": str,
        "PredictorArn": str,
        "Destination": "DataDestinationTypeDef",
    },
)
_OptionalCreatePredictorBacktestExportJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePredictorBacktestExportJobRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "Format": str,
    },
    total=False,
)

class CreatePredictorBacktestExportJobRequestRequestTypeDef(
    _RequiredCreatePredictorBacktestExportJobRequestRequestTypeDef,
    _OptionalCreatePredictorBacktestExportJobRequestRequestTypeDef,
):
    pass

CreatePredictorBacktestExportJobResponseTypeDef = TypedDict(
    "CreatePredictorBacktestExportJobResponseTypeDef",
    {
        "PredictorBacktestExportJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePredictorRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePredictorRequestRequestTypeDef",
    {
        "PredictorName": str,
        "ForecastHorizon": int,
        "InputDataConfig": "InputDataConfigTypeDef",
        "FeaturizationConfig": "FeaturizationConfigTypeDef",
    },
)
_OptionalCreatePredictorRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePredictorRequestRequestTypeDef",
    {
        "AlgorithmArn": str,
        "ForecastTypes": List[str],
        "PerformAutoML": bool,
        "AutoMLOverrideStrategy": AutoMLOverrideStrategyType,
        "PerformHPO": bool,
        "TrainingParameters": Dict[str, str],
        "EvaluationParameters": "EvaluationParametersTypeDef",
        "HPOConfig": "HyperParameterTuningJobConfigTypeDef",
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "Tags": List["TagTypeDef"],
        "OptimizationMetric": OptimizationMetricType,
    },
    total=False,
)

class CreatePredictorRequestRequestTypeDef(
    _RequiredCreatePredictorRequestRequestTypeDef, _OptionalCreatePredictorRequestRequestTypeDef
):
    pass

CreatePredictorResponseTypeDef = TypedDict(
    "CreatePredictorResponseTypeDef",
    {
        "PredictorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWhatIfAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWhatIfAnalysisRequestRequestTypeDef",
    {
        "WhatIfAnalysisName": str,
        "ForecastArn": str,
    },
)
_OptionalCreateWhatIfAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWhatIfAnalysisRequestRequestTypeDef",
    {
        "TimeSeriesSelector": "TimeSeriesSelectorTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateWhatIfAnalysisRequestRequestTypeDef(
    _RequiredCreateWhatIfAnalysisRequestRequestTypeDef,
    _OptionalCreateWhatIfAnalysisRequestRequestTypeDef,
):
    pass

CreateWhatIfAnalysisResponseTypeDef = TypedDict(
    "CreateWhatIfAnalysisResponseTypeDef",
    {
        "WhatIfAnalysisArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWhatIfForecastExportRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWhatIfForecastExportRequestRequestTypeDef",
    {
        "WhatIfForecastExportName": str,
        "WhatIfForecastArns": List[str],
        "Destination": "DataDestinationTypeDef",
    },
)
_OptionalCreateWhatIfForecastExportRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWhatIfForecastExportRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "Format": str,
    },
    total=False,
)

class CreateWhatIfForecastExportRequestRequestTypeDef(
    _RequiredCreateWhatIfForecastExportRequestRequestTypeDef,
    _OptionalCreateWhatIfForecastExportRequestRequestTypeDef,
):
    pass

CreateWhatIfForecastExportResponseTypeDef = TypedDict(
    "CreateWhatIfForecastExportResponseTypeDef",
    {
        "WhatIfForecastExportArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWhatIfForecastRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWhatIfForecastRequestRequestTypeDef",
    {
        "WhatIfForecastName": str,
        "WhatIfAnalysisArn": str,
    },
)
_OptionalCreateWhatIfForecastRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWhatIfForecastRequestRequestTypeDef",
    {
        "TimeSeriesTransformations": List["TimeSeriesTransformationTypeDef"],
        "TimeSeriesReplacementsDataSource": "TimeSeriesReplacementsDataSourceTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateWhatIfForecastRequestRequestTypeDef(
    _RequiredCreateWhatIfForecastRequestRequestTypeDef,
    _OptionalCreateWhatIfForecastRequestRequestTypeDef,
):
    pass

CreateWhatIfForecastResponseTypeDef = TypedDict(
    "CreateWhatIfForecastResponseTypeDef",
    {
        "WhatIfForecastArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDataConfigTypeDef = TypedDict(
    "_RequiredDataConfigTypeDef",
    {
        "DatasetGroupArn": str,
    },
)
_OptionalDataConfigTypeDef = TypedDict(
    "_OptionalDataConfigTypeDef",
    {
        "AttributeConfigs": List["AttributeConfigTypeDef"],
        "AdditionalDatasets": List["AdditionalDatasetTypeDef"],
    },
    total=False,
)

class DataConfigTypeDef(_RequiredDataConfigTypeDef, _OptionalDataConfigTypeDef):
    pass

DataDestinationTypeDef = TypedDict(
    "DataDestinationTypeDef",
    {
        "S3Config": "S3ConfigTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "S3Config": "S3ConfigTypeDef",
    },
)

DatasetGroupSummaryTypeDef = TypedDict(
    "DatasetGroupSummaryTypeDef",
    {
        "DatasetGroupArn": str,
        "DatasetGroupName": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

DatasetImportJobSummaryTypeDef = TypedDict(
    "DatasetImportJobSummaryTypeDef",
    {
        "DatasetImportJobArn": str,
        "DatasetImportJobName": str,
        "DataSource": "DataSourceTypeDef",
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "DatasetArn": str,
        "DatasetName": str,
        "DatasetType": DatasetTypeType,
        "Domain": DomainType,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

DeleteDatasetGroupRequestRequestTypeDef = TypedDict(
    "DeleteDatasetGroupRequestRequestTypeDef",
    {
        "DatasetGroupArn": str,
    },
)

DeleteDatasetImportJobRequestRequestTypeDef = TypedDict(
    "DeleteDatasetImportJobRequestRequestTypeDef",
    {
        "DatasetImportJobArn": str,
    },
)

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "DatasetArn": str,
    },
)

DeleteExplainabilityExportRequestRequestTypeDef = TypedDict(
    "DeleteExplainabilityExportRequestRequestTypeDef",
    {
        "ExplainabilityExportArn": str,
    },
)

DeleteExplainabilityRequestRequestTypeDef = TypedDict(
    "DeleteExplainabilityRequestRequestTypeDef",
    {
        "ExplainabilityArn": str,
    },
)

DeleteForecastExportJobRequestRequestTypeDef = TypedDict(
    "DeleteForecastExportJobRequestRequestTypeDef",
    {
        "ForecastExportJobArn": str,
    },
)

DeleteForecastRequestRequestTypeDef = TypedDict(
    "DeleteForecastRequestRequestTypeDef",
    {
        "ForecastArn": str,
    },
)

DeleteMonitorRequestRequestTypeDef = TypedDict(
    "DeleteMonitorRequestRequestTypeDef",
    {
        "MonitorArn": str,
    },
)

DeletePredictorBacktestExportJobRequestRequestTypeDef = TypedDict(
    "DeletePredictorBacktestExportJobRequestRequestTypeDef",
    {
        "PredictorBacktestExportJobArn": str,
    },
)

DeletePredictorRequestRequestTypeDef = TypedDict(
    "DeletePredictorRequestRequestTypeDef",
    {
        "PredictorArn": str,
    },
)

DeleteResourceTreeRequestRequestTypeDef = TypedDict(
    "DeleteResourceTreeRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeleteWhatIfAnalysisRequestRequestTypeDef = TypedDict(
    "DeleteWhatIfAnalysisRequestRequestTypeDef",
    {
        "WhatIfAnalysisArn": str,
    },
)

DeleteWhatIfForecastExportRequestRequestTypeDef = TypedDict(
    "DeleteWhatIfForecastExportRequestRequestTypeDef",
    {
        "WhatIfForecastExportArn": str,
    },
)

DeleteWhatIfForecastRequestRequestTypeDef = TypedDict(
    "DeleteWhatIfForecastRequestRequestTypeDef",
    {
        "WhatIfForecastArn": str,
    },
)

DescribeAutoPredictorRequestRequestTypeDef = TypedDict(
    "DescribeAutoPredictorRequestRequestTypeDef",
    {
        "PredictorArn": str,
    },
)

DescribeAutoPredictorResponseTypeDef = TypedDict(
    "DescribeAutoPredictorResponseTypeDef",
    {
        "PredictorArn": str,
        "PredictorName": str,
        "ForecastHorizon": int,
        "ForecastTypes": List[str],
        "ForecastFrequency": str,
        "ForecastDimensions": List[str],
        "DatasetImportJobArns": List[str],
        "DataConfig": "DataConfigTypeDef",
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "ReferencePredictorSummary": "ReferencePredictorSummaryTypeDef",
        "EstimatedTimeRemainingInMinutes": int,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "OptimizationMetric": OptimizationMetricType,
        "ExplainabilityInfo": "ExplainabilityInfoTypeDef",
        "MonitorInfo": "MonitorInfoTypeDef",
        "TimeAlignmentBoundary": "TimeAlignmentBoundaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetGroupRequestRequestTypeDef = TypedDict(
    "DescribeDatasetGroupRequestRequestTypeDef",
    {
        "DatasetGroupArn": str,
    },
)

DescribeDatasetGroupResponseTypeDef = TypedDict(
    "DescribeDatasetGroupResponseTypeDef",
    {
        "DatasetGroupName": str,
        "DatasetGroupArn": str,
        "DatasetArns": List[str],
        "Domain": DomainType,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetImportJobRequestRequestTypeDef = TypedDict(
    "DescribeDatasetImportJobRequestRequestTypeDef",
    {
        "DatasetImportJobArn": str,
    },
)

DescribeDatasetImportJobResponseTypeDef = TypedDict(
    "DescribeDatasetImportJobResponseTypeDef",
    {
        "DatasetImportJobName": str,
        "DatasetImportJobArn": str,
        "DatasetArn": str,
        "TimestampFormat": str,
        "TimeZone": str,
        "UseGeolocationForTimeZone": bool,
        "GeolocationFormat": str,
        "DataSource": "DataSourceTypeDef",
        "EstimatedTimeRemainingInMinutes": int,
        "FieldStatistics": Dict[str, "StatisticsTypeDef"],
        "DataSize": float,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Format": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "DatasetArn": str,
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "DatasetArn": str,
        "DatasetName": str,
        "Domain": DomainType,
        "DatasetType": DatasetTypeType,
        "DataFrequency": str,
        "Schema": "SchemaTypeDef",
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExplainabilityExportRequestRequestTypeDef = TypedDict(
    "DescribeExplainabilityExportRequestRequestTypeDef",
    {
        "ExplainabilityExportArn": str,
    },
)

DescribeExplainabilityExportResponseTypeDef = TypedDict(
    "DescribeExplainabilityExportResponseTypeDef",
    {
        "ExplainabilityExportArn": str,
        "ExplainabilityExportName": str,
        "ExplainabilityArn": str,
        "Destination": "DataDestinationTypeDef",
        "Message": str,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Format": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExplainabilityRequestRequestTypeDef = TypedDict(
    "DescribeExplainabilityRequestRequestTypeDef",
    {
        "ExplainabilityArn": str,
    },
)

DescribeExplainabilityResponseTypeDef = TypedDict(
    "DescribeExplainabilityResponseTypeDef",
    {
        "ExplainabilityArn": str,
        "ExplainabilityName": str,
        "ResourceArn": str,
        "ExplainabilityConfig": "ExplainabilityConfigTypeDef",
        "EnableVisualization": bool,
        "DataSource": "DataSourceTypeDef",
        "Schema": "SchemaTypeDef",
        "StartDateTime": str,
        "EndDateTime": str,
        "EstimatedTimeRemainingInMinutes": int,
        "Message": str,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeForecastExportJobRequestRequestTypeDef = TypedDict(
    "DescribeForecastExportJobRequestRequestTypeDef",
    {
        "ForecastExportJobArn": str,
    },
)

DescribeForecastExportJobResponseTypeDef = TypedDict(
    "DescribeForecastExportJobResponseTypeDef",
    {
        "ForecastExportJobArn": str,
        "ForecastExportJobName": str,
        "ForecastArn": str,
        "Destination": "DataDestinationTypeDef",
        "Message": str,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Format": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeForecastRequestRequestTypeDef = TypedDict(
    "DescribeForecastRequestRequestTypeDef",
    {
        "ForecastArn": str,
    },
)

DescribeForecastResponseTypeDef = TypedDict(
    "DescribeForecastResponseTypeDef",
    {
        "ForecastArn": str,
        "ForecastName": str,
        "ForecastTypes": List[str],
        "PredictorArn": str,
        "DatasetGroupArn": str,
        "EstimatedTimeRemainingInMinutes": int,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "TimeSeriesSelector": "TimeSeriesSelectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMonitorRequestRequestTypeDef = TypedDict(
    "DescribeMonitorRequestRequestTypeDef",
    {
        "MonitorArn": str,
    },
)

DescribeMonitorResponseTypeDef = TypedDict(
    "DescribeMonitorResponseTypeDef",
    {
        "MonitorName": str,
        "MonitorArn": str,
        "ResourceArn": str,
        "Status": str,
        "LastEvaluationTime": datetime,
        "LastEvaluationState": str,
        "Baseline": "BaselineTypeDef",
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "EstimatedEvaluationTimeRemainingInMinutes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePredictorBacktestExportJobRequestRequestTypeDef = TypedDict(
    "DescribePredictorBacktestExportJobRequestRequestTypeDef",
    {
        "PredictorBacktestExportJobArn": str,
    },
)

DescribePredictorBacktestExportJobResponseTypeDef = TypedDict(
    "DescribePredictorBacktestExportJobResponseTypeDef",
    {
        "PredictorBacktestExportJobArn": str,
        "PredictorBacktestExportJobName": str,
        "PredictorArn": str,
        "Destination": "DataDestinationTypeDef",
        "Message": str,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Format": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePredictorRequestRequestTypeDef = TypedDict(
    "DescribePredictorRequestRequestTypeDef",
    {
        "PredictorArn": str,
    },
)

DescribePredictorResponseTypeDef = TypedDict(
    "DescribePredictorResponseTypeDef",
    {
        "PredictorArn": str,
        "PredictorName": str,
        "AlgorithmArn": str,
        "AutoMLAlgorithmArns": List[str],
        "ForecastHorizon": int,
        "ForecastTypes": List[str],
        "PerformAutoML": bool,
        "AutoMLOverrideStrategy": AutoMLOverrideStrategyType,
        "PerformHPO": bool,
        "TrainingParameters": Dict[str, str],
        "EvaluationParameters": "EvaluationParametersTypeDef",
        "HPOConfig": "HyperParameterTuningJobConfigTypeDef",
        "InputDataConfig": "InputDataConfigTypeDef",
        "FeaturizationConfig": "FeaturizationConfigTypeDef",
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "PredictorExecutionDetails": "PredictorExecutionDetailsTypeDef",
        "EstimatedTimeRemainingInMinutes": int,
        "IsAutoPredictor": bool,
        "DatasetImportJobArns": List[str],
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "OptimizationMetric": OptimizationMetricType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWhatIfAnalysisRequestRequestTypeDef = TypedDict(
    "DescribeWhatIfAnalysisRequestRequestTypeDef",
    {
        "WhatIfAnalysisArn": str,
    },
)

DescribeWhatIfAnalysisResponseTypeDef = TypedDict(
    "DescribeWhatIfAnalysisResponseTypeDef",
    {
        "WhatIfAnalysisName": str,
        "WhatIfAnalysisArn": str,
        "ForecastArn": str,
        "EstimatedTimeRemainingInMinutes": int,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "TimeSeriesSelector": "TimeSeriesSelectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWhatIfForecastExportRequestRequestTypeDef = TypedDict(
    "DescribeWhatIfForecastExportRequestRequestTypeDef",
    {
        "WhatIfForecastExportArn": str,
    },
)

DescribeWhatIfForecastExportResponseTypeDef = TypedDict(
    "DescribeWhatIfForecastExportResponseTypeDef",
    {
        "WhatIfForecastExportArn": str,
        "WhatIfForecastExportName": str,
        "WhatIfForecastArns": List[str],
        "Destination": "DataDestinationTypeDef",
        "Message": str,
        "Status": str,
        "CreationTime": datetime,
        "EstimatedTimeRemainingInMinutes": int,
        "LastModificationTime": datetime,
        "Format": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWhatIfForecastRequestRequestTypeDef = TypedDict(
    "DescribeWhatIfForecastRequestRequestTypeDef",
    {
        "WhatIfForecastArn": str,
    },
)

DescribeWhatIfForecastResponseTypeDef = TypedDict(
    "DescribeWhatIfForecastResponseTypeDef",
    {
        "WhatIfForecastName": str,
        "WhatIfForecastArn": str,
        "WhatIfAnalysisArn": str,
        "EstimatedTimeRemainingInMinutes": int,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "TimeSeriesTransformations": List["TimeSeriesTransformationTypeDef"],
        "TimeSeriesReplacementsDataSource": "TimeSeriesReplacementsDataSourceTypeDef",
        "ForecastTypes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "RoleArn": str,
        "KMSKeyArn": str,
    },
)

ErrorMetricTypeDef = TypedDict(
    "ErrorMetricTypeDef",
    {
        "ForecastType": str,
        "WAPE": float,
        "RMSE": float,
        "MASE": float,
        "MAPE": float,
    },
    total=False,
)

EvaluationParametersTypeDef = TypedDict(
    "EvaluationParametersTypeDef",
    {
        "NumberOfBacktestWindows": int,
        "BackTestWindowOffset": int,
    },
    total=False,
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "AlgorithmArn": str,
        "TestWindows": List["WindowSummaryTypeDef"],
    },
    total=False,
)

ExplainabilityConfigTypeDef = TypedDict(
    "ExplainabilityConfigTypeDef",
    {
        "TimeSeriesGranularity": TimeSeriesGranularityType,
        "TimePointGranularity": TimePointGranularityType,
    },
)

ExplainabilityExportSummaryTypeDef = TypedDict(
    "ExplainabilityExportSummaryTypeDef",
    {
        "ExplainabilityExportArn": str,
        "ExplainabilityExportName": str,
        "Destination": "DataDestinationTypeDef",
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ExplainabilityInfoTypeDef = TypedDict(
    "ExplainabilityInfoTypeDef",
    {
        "ExplainabilityArn": str,
        "Status": str,
    },
    total=False,
)

ExplainabilitySummaryTypeDef = TypedDict(
    "ExplainabilitySummaryTypeDef",
    {
        "ExplainabilityArn": str,
        "ExplainabilityName": str,
        "ResourceArn": str,
        "ExplainabilityConfig": "ExplainabilityConfigTypeDef",
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

_RequiredFeaturizationConfigTypeDef = TypedDict(
    "_RequiredFeaturizationConfigTypeDef",
    {
        "ForecastFrequency": str,
    },
)
_OptionalFeaturizationConfigTypeDef = TypedDict(
    "_OptionalFeaturizationConfigTypeDef",
    {
        "ForecastDimensions": List[str],
        "Featurizations": List["FeaturizationTypeDef"],
    },
    total=False,
)

class FeaturizationConfigTypeDef(
    _RequiredFeaturizationConfigTypeDef, _OptionalFeaturizationConfigTypeDef
):
    pass

_RequiredFeaturizationMethodTypeDef = TypedDict(
    "_RequiredFeaturizationMethodTypeDef",
    {
        "FeaturizationMethodName": Literal["filling"],
    },
)
_OptionalFeaturizationMethodTypeDef = TypedDict(
    "_OptionalFeaturizationMethodTypeDef",
    {
        "FeaturizationMethodParameters": Dict[str, str],
    },
    total=False,
)

class FeaturizationMethodTypeDef(
    _RequiredFeaturizationMethodTypeDef, _OptionalFeaturizationMethodTypeDef
):
    pass

_RequiredFeaturizationTypeDef = TypedDict(
    "_RequiredFeaturizationTypeDef",
    {
        "AttributeName": str,
    },
)
_OptionalFeaturizationTypeDef = TypedDict(
    "_OptionalFeaturizationTypeDef",
    {
        "FeaturizationPipeline": List["FeaturizationMethodTypeDef"],
    },
    total=False,
)

class FeaturizationTypeDef(_RequiredFeaturizationTypeDef, _OptionalFeaturizationTypeDef):
    pass

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Key": str,
        "Value": str,
        "Condition": FilterConditionStringType,
    },
)

ForecastExportJobSummaryTypeDef = TypedDict(
    "ForecastExportJobSummaryTypeDef",
    {
        "ForecastExportJobArn": str,
        "ForecastExportJobName": str,
        "Destination": "DataDestinationTypeDef",
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ForecastSummaryTypeDef = TypedDict(
    "ForecastSummaryTypeDef",
    {
        "ForecastArn": str,
        "ForecastName": str,
        "PredictorArn": str,
        "CreatedUsingAutoPredictor": bool,
        "DatasetGroupArn": str,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

GetAccuracyMetricsRequestRequestTypeDef = TypedDict(
    "GetAccuracyMetricsRequestRequestTypeDef",
    {
        "PredictorArn": str,
    },
)

GetAccuracyMetricsResponseTypeDef = TypedDict(
    "GetAccuracyMetricsResponseTypeDef",
    {
        "PredictorEvaluationResults": List["EvaluationResultTypeDef"],
        "IsAutoPredictor": bool,
        "AutoMLOverrideStrategy": AutoMLOverrideStrategyType,
        "OptimizationMetric": OptimizationMetricType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HyperParameterTuningJobConfigTypeDef = TypedDict(
    "HyperParameterTuningJobConfigTypeDef",
    {
        "ParameterRanges": "ParameterRangesTypeDef",
    },
    total=False,
)

_RequiredInputDataConfigTypeDef = TypedDict(
    "_RequiredInputDataConfigTypeDef",
    {
        "DatasetGroupArn": str,
    },
)
_OptionalInputDataConfigTypeDef = TypedDict(
    "_OptionalInputDataConfigTypeDef",
    {
        "SupplementaryFeatures": List["SupplementaryFeatureTypeDef"],
    },
    total=False,
)

class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, _OptionalInputDataConfigTypeDef):
    pass

_RequiredIntegerParameterRangeTypeDef = TypedDict(
    "_RequiredIntegerParameterRangeTypeDef",
    {
        "Name": str,
        "MaxValue": int,
        "MinValue": int,
    },
)
_OptionalIntegerParameterRangeTypeDef = TypedDict(
    "_OptionalIntegerParameterRangeTypeDef",
    {
        "ScalingType": ScalingTypeType,
    },
    total=False,
)

class IntegerParameterRangeTypeDef(
    _RequiredIntegerParameterRangeTypeDef, _OptionalIntegerParameterRangeTypeDef
):
    pass

ListDatasetGroupsRequestRequestTypeDef = TypedDict(
    "ListDatasetGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDatasetGroupsResponseTypeDef = TypedDict(
    "ListDatasetGroupsResponseTypeDef",
    {
        "DatasetGroups": List["DatasetGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetImportJobsRequestRequestTypeDef = TypedDict(
    "ListDatasetImportJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListDatasetImportJobsResponseTypeDef = TypedDict(
    "ListDatasetImportJobsResponseTypeDef",
    {
        "DatasetImportJobs": List["DatasetImportJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "Datasets": List["DatasetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExplainabilitiesRequestRequestTypeDef = TypedDict(
    "ListExplainabilitiesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListExplainabilitiesResponseTypeDef = TypedDict(
    "ListExplainabilitiesResponseTypeDef",
    {
        "Explainabilities": List["ExplainabilitySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExplainabilityExportsRequestRequestTypeDef = TypedDict(
    "ListExplainabilityExportsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListExplainabilityExportsResponseTypeDef = TypedDict(
    "ListExplainabilityExportsResponseTypeDef",
    {
        "ExplainabilityExports": List["ExplainabilityExportSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListForecastExportJobsRequestRequestTypeDef = TypedDict(
    "ListForecastExportJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListForecastExportJobsResponseTypeDef = TypedDict(
    "ListForecastExportJobsResponseTypeDef",
    {
        "ForecastExportJobs": List["ForecastExportJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListForecastsRequestRequestTypeDef = TypedDict(
    "ListForecastsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListForecastsResponseTypeDef = TypedDict(
    "ListForecastsResponseTypeDef",
    {
        "Forecasts": List["ForecastSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMonitorEvaluationsRequestRequestTypeDef = TypedDict(
    "_RequiredListMonitorEvaluationsRequestRequestTypeDef",
    {
        "MonitorArn": str,
    },
)
_OptionalListMonitorEvaluationsRequestRequestTypeDef = TypedDict(
    "_OptionalListMonitorEvaluationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

class ListMonitorEvaluationsRequestRequestTypeDef(
    _RequiredListMonitorEvaluationsRequestRequestTypeDef,
    _OptionalListMonitorEvaluationsRequestRequestTypeDef,
):
    pass

ListMonitorEvaluationsResponseTypeDef = TypedDict(
    "ListMonitorEvaluationsResponseTypeDef",
    {
        "NextToken": str,
        "PredictorMonitorEvaluations": List["PredictorMonitorEvaluationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMonitorsRequestRequestTypeDef = TypedDict(
    "ListMonitorsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListMonitorsResponseTypeDef = TypedDict(
    "ListMonitorsResponseTypeDef",
    {
        "Monitors": List["MonitorSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPredictorBacktestExportJobsRequestRequestTypeDef = TypedDict(
    "ListPredictorBacktestExportJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListPredictorBacktestExportJobsResponseTypeDef = TypedDict(
    "ListPredictorBacktestExportJobsResponseTypeDef",
    {
        "PredictorBacktestExportJobs": List["PredictorBacktestExportJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPredictorsRequestRequestTypeDef = TypedDict(
    "ListPredictorsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListPredictorsResponseTypeDef = TypedDict(
    "ListPredictorsResponseTypeDef",
    {
        "Predictors": List["PredictorSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWhatIfAnalysesRequestRequestTypeDef = TypedDict(
    "ListWhatIfAnalysesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListWhatIfAnalysesResponseTypeDef = TypedDict(
    "ListWhatIfAnalysesResponseTypeDef",
    {
        "WhatIfAnalyses": List["WhatIfAnalysisSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWhatIfForecastExportsRequestRequestTypeDef = TypedDict(
    "ListWhatIfForecastExportsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListWhatIfForecastExportsResponseTypeDef = TypedDict(
    "ListWhatIfForecastExportsResponseTypeDef",
    {
        "WhatIfForecastExports": List["WhatIfForecastExportSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWhatIfForecastsRequestRequestTypeDef = TypedDict(
    "ListWhatIfForecastsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListWhatIfForecastsResponseTypeDef = TypedDict(
    "ListWhatIfForecastsResponseTypeDef",
    {
        "WhatIfForecasts": List["WhatIfForecastSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricResultTypeDef = TypedDict(
    "MetricResultTypeDef",
    {
        "MetricName": str,
        "MetricValue": float,
    },
    total=False,
)

MetricsTypeDef = TypedDict(
    "MetricsTypeDef",
    {
        "RMSE": float,
        "WeightedQuantileLosses": List["WeightedQuantileLossTypeDef"],
        "ErrorMetrics": List["ErrorMetricTypeDef"],
        "AverageWeightedQuantileLoss": float,
    },
    total=False,
)

MonitorConfigTypeDef = TypedDict(
    "MonitorConfigTypeDef",
    {
        "MonitorName": str,
    },
)

MonitorDataSourceTypeDef = TypedDict(
    "MonitorDataSourceTypeDef",
    {
        "DatasetImportJobArn": str,
        "ForecastArn": str,
        "PredictorArn": str,
    },
    total=False,
)

MonitorInfoTypeDef = TypedDict(
    "MonitorInfoTypeDef",
    {
        "MonitorArn": str,
        "Status": str,
    },
    total=False,
)

MonitorSummaryTypeDef = TypedDict(
    "MonitorSummaryTypeDef",
    {
        "MonitorArn": str,
        "MonitorName": str,
        "ResourceArn": str,
        "Status": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ParameterRangesTypeDef = TypedDict(
    "ParameterRangesTypeDef",
    {
        "CategoricalParameterRanges": List["CategoricalParameterRangeTypeDef"],
        "ContinuousParameterRanges": List["ContinuousParameterRangeTypeDef"],
        "IntegerParameterRanges": List["IntegerParameterRangeTypeDef"],
    },
    total=False,
)

PredictorBacktestExportJobSummaryTypeDef = TypedDict(
    "PredictorBacktestExportJobSummaryTypeDef",
    {
        "PredictorBacktestExportJobArn": str,
        "PredictorBacktestExportJobName": str,
        "Destination": "DataDestinationTypeDef",
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

PredictorBaselineTypeDef = TypedDict(
    "PredictorBaselineTypeDef",
    {
        "BaselineMetrics": List["BaselineMetricTypeDef"],
    },
    total=False,
)

PredictorEventTypeDef = TypedDict(
    "PredictorEventTypeDef",
    {
        "Detail": str,
        "Datetime": datetime,
    },
    total=False,
)

PredictorExecutionDetailsTypeDef = TypedDict(
    "PredictorExecutionDetailsTypeDef",
    {
        "PredictorExecutions": List["PredictorExecutionTypeDef"],
    },
    total=False,
)

PredictorExecutionTypeDef = TypedDict(
    "PredictorExecutionTypeDef",
    {
        "AlgorithmArn": str,
        "TestWindows": List["TestWindowSummaryTypeDef"],
    },
    total=False,
)

PredictorMonitorEvaluationTypeDef = TypedDict(
    "PredictorMonitorEvaluationTypeDef",
    {
        "ResourceArn": str,
        "MonitorArn": str,
        "EvaluationTime": datetime,
        "EvaluationState": str,
        "WindowStartDatetime": datetime,
        "WindowEndDatetime": datetime,
        "PredictorEvent": "PredictorEventTypeDef",
        "MonitorDataSource": "MonitorDataSourceTypeDef",
        "MetricResults": List["MetricResultTypeDef"],
        "NumItemsEvaluated": int,
        "Message": str,
    },
    total=False,
)

PredictorSummaryTypeDef = TypedDict(
    "PredictorSummaryTypeDef",
    {
        "PredictorArn": str,
        "PredictorName": str,
        "DatasetGroupArn": str,
        "IsAutoPredictor": bool,
        "ReferencePredictorSummary": "ReferencePredictorSummaryTypeDef",
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

ReferencePredictorSummaryTypeDef = TypedDict(
    "ReferencePredictorSummaryTypeDef",
    {
        "Arn": str,
        "State": StateType,
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

ResumeResourceRequestRequestTypeDef = TypedDict(
    "ResumeResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

_RequiredS3ConfigTypeDef = TypedDict(
    "_RequiredS3ConfigTypeDef",
    {
        "Path": str,
        "RoleArn": str,
    },
)
_OptionalS3ConfigTypeDef = TypedDict(
    "_OptionalS3ConfigTypeDef",
    {
        "KMSKeyArn": str,
    },
    total=False,
)

class S3ConfigTypeDef(_RequiredS3ConfigTypeDef, _OptionalS3ConfigTypeDef):
    pass

SchemaAttributeTypeDef = TypedDict(
    "SchemaAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeType": AttributeTypeType,
    },
    total=False,
)

SchemaTypeDef = TypedDict(
    "SchemaTypeDef",
    {
        "Attributes": List["SchemaAttributeTypeDef"],
    },
    total=False,
)

StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {
        "Count": int,
        "CountDistinct": int,
        "CountNull": int,
        "CountNan": int,
        "Min": str,
        "Max": str,
        "Avg": float,
        "Stddev": float,
        "CountLong": int,
        "CountDistinctLong": int,
        "CountNullLong": int,
        "CountNanLong": int,
    },
    total=False,
)

StopResourceRequestRequestTypeDef = TypedDict(
    "StopResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

SupplementaryFeatureTypeDef = TypedDict(
    "SupplementaryFeatureTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TestWindowSummaryTypeDef = TypedDict(
    "TestWindowSummaryTypeDef",
    {
        "TestWindowStart": datetime,
        "TestWindowEnd": datetime,
        "Status": str,
        "Message": str,
    },
    total=False,
)

TimeAlignmentBoundaryTypeDef = TypedDict(
    "TimeAlignmentBoundaryTypeDef",
    {
        "Month": MonthType,
        "DayOfMonth": int,
        "DayOfWeek": DayOfWeekType,
        "Hour": int,
    },
    total=False,
)

TimeSeriesConditionTypeDef = TypedDict(
    "TimeSeriesConditionTypeDef",
    {
        "AttributeName": str,
        "AttributeValue": str,
        "Condition": ConditionType,
    },
)

TimeSeriesIdentifiersTypeDef = TypedDict(
    "TimeSeriesIdentifiersTypeDef",
    {
        "DataSource": "DataSourceTypeDef",
        "Schema": "SchemaTypeDef",
        "Format": str,
    },
    total=False,
)

_RequiredTimeSeriesReplacementsDataSourceTypeDef = TypedDict(
    "_RequiredTimeSeriesReplacementsDataSourceTypeDef",
    {
        "S3Config": "S3ConfigTypeDef",
        "Schema": "SchemaTypeDef",
    },
)
_OptionalTimeSeriesReplacementsDataSourceTypeDef = TypedDict(
    "_OptionalTimeSeriesReplacementsDataSourceTypeDef",
    {
        "Format": str,
        "TimestampFormat": str,
    },
    total=False,
)

class TimeSeriesReplacementsDataSourceTypeDef(
    _RequiredTimeSeriesReplacementsDataSourceTypeDef,
    _OptionalTimeSeriesReplacementsDataSourceTypeDef,
):
    pass

TimeSeriesSelectorTypeDef = TypedDict(
    "TimeSeriesSelectorTypeDef",
    {
        "TimeSeriesIdentifiers": "TimeSeriesIdentifiersTypeDef",
    },
    total=False,
)

TimeSeriesTransformationTypeDef = TypedDict(
    "TimeSeriesTransformationTypeDef",
    {
        "Action": "ActionTypeDef",
        "TimeSeriesConditions": List["TimeSeriesConditionTypeDef"],
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateDatasetGroupRequestRequestTypeDef = TypedDict(
    "UpdateDatasetGroupRequestRequestTypeDef",
    {
        "DatasetGroupArn": str,
        "DatasetArns": List[str],
    },
)

WeightedQuantileLossTypeDef = TypedDict(
    "WeightedQuantileLossTypeDef",
    {
        "Quantile": float,
        "LossValue": float,
    },
    total=False,
)

WhatIfAnalysisSummaryTypeDef = TypedDict(
    "WhatIfAnalysisSummaryTypeDef",
    {
        "WhatIfAnalysisArn": str,
        "WhatIfAnalysisName": str,
        "ForecastArn": str,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

WhatIfForecastExportSummaryTypeDef = TypedDict(
    "WhatIfForecastExportSummaryTypeDef",
    {
        "WhatIfForecastExportArn": str,
        "WhatIfForecastArns": List[str],
        "WhatIfForecastExportName": str,
        "Destination": "DataDestinationTypeDef",
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

WhatIfForecastSummaryTypeDef = TypedDict(
    "WhatIfForecastSummaryTypeDef",
    {
        "WhatIfForecastArn": str,
        "WhatIfForecastName": str,
        "WhatIfAnalysisArn": str,
        "Status": str,
        "Message": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
    },
    total=False,
)

WindowSummaryTypeDef = TypedDict(
    "WindowSummaryTypeDef",
    {
        "TestWindowStart": datetime,
        "TestWindowEnd": datetime,
        "ItemCount": int,
        "EvaluationType": EvaluationTypeType,
        "Metrics": "MetricsTypeDef",
    },
    total=False,
)
