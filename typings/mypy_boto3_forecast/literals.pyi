"""
Type annotations for forecast service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/literals.html)

Usage::

    ```python
    from mypy_boto3_forecast.literals import AttributeTypeType

    data: AttributeTypeType = "float"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AttributeTypeType",
    "AutoMLOverrideStrategyType",
    "ConditionType",
    "DatasetTypeType",
    "DayOfWeekType",
    "DomainType",
    "EvaluationTypeType",
    "FeaturizationMethodNameType",
    "FilterConditionStringType",
    "ImportModeType",
    "ListDatasetGroupsPaginatorName",
    "ListDatasetImportJobsPaginatorName",
    "ListDatasetsPaginatorName",
    "ListExplainabilitiesPaginatorName",
    "ListExplainabilityExportsPaginatorName",
    "ListForecastExportJobsPaginatorName",
    "ListForecastsPaginatorName",
    "ListMonitorEvaluationsPaginatorName",
    "ListMonitorsPaginatorName",
    "ListPredictorBacktestExportJobsPaginatorName",
    "ListPredictorsPaginatorName",
    "ListWhatIfAnalysesPaginatorName",
    "ListWhatIfForecastExportsPaginatorName",
    "ListWhatIfForecastsPaginatorName",
    "MonthType",
    "OperationType",
    "OptimizationMetricType",
    "ScalingTypeType",
    "StateType",
    "TimePointGranularityType",
    "TimeSeriesGranularityType",
)

AttributeTypeType = Literal["float", "geolocation", "integer", "string", "timestamp"]
AutoMLOverrideStrategyType = Literal["AccuracyOptimized", "LatencyOptimized"]
ConditionType = Literal["EQUALS", "GREATER_THAN", "LESS_THAN", "NOT_EQUALS"]
DatasetTypeType = Literal["ITEM_METADATA", "RELATED_TIME_SERIES", "TARGET_TIME_SERIES"]
DayOfWeekType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
DomainType = Literal[
    "CUSTOM", "EC2_CAPACITY", "INVENTORY_PLANNING", "METRICS", "RETAIL", "WEB_TRAFFIC", "WORK_FORCE"
]
EvaluationTypeType = Literal["COMPUTED", "SUMMARY"]
FeaturizationMethodNameType = Literal["filling"]
FilterConditionStringType = Literal["IS", "IS_NOT"]
ImportModeType = Literal["FULL", "INCREMENTAL"]
ListDatasetGroupsPaginatorName = Literal["list_dataset_groups"]
ListDatasetImportJobsPaginatorName = Literal["list_dataset_import_jobs"]
ListDatasetsPaginatorName = Literal["list_datasets"]
ListExplainabilitiesPaginatorName = Literal["list_explainabilities"]
ListExplainabilityExportsPaginatorName = Literal["list_explainability_exports"]
ListForecastExportJobsPaginatorName = Literal["list_forecast_export_jobs"]
ListForecastsPaginatorName = Literal["list_forecasts"]
ListMonitorEvaluationsPaginatorName = Literal["list_monitor_evaluations"]
ListMonitorsPaginatorName = Literal["list_monitors"]
ListPredictorBacktestExportJobsPaginatorName = Literal["list_predictor_backtest_export_jobs"]
ListPredictorsPaginatorName = Literal["list_predictors"]
ListWhatIfAnalysesPaginatorName = Literal["list_what_if_analyses"]
ListWhatIfForecastExportsPaginatorName = Literal["list_what_if_forecast_exports"]
ListWhatIfForecastsPaginatorName = Literal["list_what_if_forecasts"]
MonthType = Literal[
    "APRIL",
    "AUGUST",
    "DECEMBER",
    "FEBRUARY",
    "JANUARY",
    "JULY",
    "JUNE",
    "MARCH",
    "MAY",
    "NOVEMBER",
    "OCTOBER",
    "SEPTEMBER",
]
OperationType = Literal["ADD", "DIVIDE", "MULTIPLY", "SUBTRACT"]
OptimizationMetricType = Literal["AverageWeightedQuantileLoss", "MAPE", "MASE", "RMSE", "WAPE"]
ScalingTypeType = Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"]
StateType = Literal["Active", "Deleted"]
TimePointGranularityType = Literal["ALL", "SPECIFIC"]
TimeSeriesGranularityType = Literal["ALL", "SPECIFIC"]
