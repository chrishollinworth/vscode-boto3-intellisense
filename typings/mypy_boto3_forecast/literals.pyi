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
    "DatasetTypeType",
    "DomainType",
    "EvaluationTypeType",
    "FeaturizationMethodNameType",
    "FilterConditionStringType",
    "ListDatasetGroupsPaginatorName",
    "ListDatasetImportJobsPaginatorName",
    "ListDatasetsPaginatorName",
    "ListForecastExportJobsPaginatorName",
    "ListForecastsPaginatorName",
    "ListPredictorBacktestExportJobsPaginatorName",
    "ListPredictorsPaginatorName",
    "ScalingTypeType",
)

AttributeTypeType = Literal["float", "geolocation", "integer", "string", "timestamp"]
AutoMLOverrideStrategyType = Literal["LatencyOptimized"]
DatasetTypeType = Literal["ITEM_METADATA", "RELATED_TIME_SERIES", "TARGET_TIME_SERIES"]
DomainType = Literal[
    "CUSTOM", "EC2_CAPACITY", "INVENTORY_PLANNING", "METRICS", "RETAIL", "WEB_TRAFFIC", "WORK_FORCE"
]
EvaluationTypeType = Literal["COMPUTED", "SUMMARY"]
FeaturizationMethodNameType = Literal["filling"]
FilterConditionStringType = Literal["IS", "IS_NOT"]
ListDatasetGroupsPaginatorName = Literal["list_dataset_groups"]
ListDatasetImportJobsPaginatorName = Literal["list_dataset_import_jobs"]
ListDatasetsPaginatorName = Literal["list_datasets"]
ListForecastExportJobsPaginatorName = Literal["list_forecast_export_jobs"]
ListForecastsPaginatorName = Literal["list_forecasts"]
ListPredictorBacktestExportJobsPaginatorName = Literal["list_predictor_backtest_export_jobs"]
ListPredictorsPaginatorName = Literal["list_predictors"]
ScalingTypeType = Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"]
