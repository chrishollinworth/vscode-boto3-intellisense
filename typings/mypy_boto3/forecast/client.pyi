"""
Type annotations for forecast service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_forecast import ForecastServiceClient

    client: ForecastServiceClient = boto3.client("forecast")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AutoMLOverrideStrategyType,
    DatasetTypeType,
    DomainType,
    ImportModeType,
    OptimizationMetricType,
)
from .paginator import (
    ListDatasetGroupsPaginator,
    ListDatasetImportJobsPaginator,
    ListDatasetsPaginator,
    ListExplainabilitiesPaginator,
    ListExplainabilityExportsPaginator,
    ListForecastExportJobsPaginator,
    ListForecastsPaginator,
    ListMonitorEvaluationsPaginator,
    ListMonitorsPaginator,
    ListPredictorBacktestExportJobsPaginator,
    ListPredictorsPaginator,
    ListWhatIfAnalysesPaginator,
    ListWhatIfForecastExportsPaginator,
    ListWhatIfForecastsPaginator,
)
from .type_defs import (
    CreateAutoPredictorResponseTypeDef,
    CreateDatasetGroupResponseTypeDef,
    CreateDatasetImportJobResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateExplainabilityExportResponseTypeDef,
    CreateExplainabilityResponseTypeDef,
    CreateForecastExportJobResponseTypeDef,
    CreateForecastResponseTypeDef,
    CreateMonitorResponseTypeDef,
    CreatePredictorBacktestExportJobResponseTypeDef,
    CreatePredictorResponseTypeDef,
    CreateWhatIfAnalysisResponseTypeDef,
    CreateWhatIfForecastExportResponseTypeDef,
    CreateWhatIfForecastResponseTypeDef,
    DataConfigTypeDef,
    DataDestinationTypeDef,
    DataSourceTypeDef,
    DescribeAutoPredictorResponseTypeDef,
    DescribeDatasetGroupResponseTypeDef,
    DescribeDatasetImportJobResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeExplainabilityExportResponseTypeDef,
    DescribeExplainabilityResponseTypeDef,
    DescribeForecastExportJobResponseTypeDef,
    DescribeForecastResponseTypeDef,
    DescribeMonitorResponseTypeDef,
    DescribePredictorBacktestExportJobResponseTypeDef,
    DescribePredictorResponseTypeDef,
    DescribeWhatIfAnalysisResponseTypeDef,
    DescribeWhatIfForecastExportResponseTypeDef,
    DescribeWhatIfForecastResponseTypeDef,
    EncryptionConfigTypeDef,
    EvaluationParametersTypeDef,
    ExplainabilityConfigTypeDef,
    FeaturizationConfigTypeDef,
    FilterTypeDef,
    GetAccuracyMetricsResponseTypeDef,
    HyperParameterTuningJobConfigTypeDef,
    InputDataConfigTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListExplainabilitiesResponseTypeDef,
    ListExplainabilityExportsResponseTypeDef,
    ListForecastExportJobsResponseTypeDef,
    ListForecastsResponseTypeDef,
    ListMonitorEvaluationsResponseTypeDef,
    ListMonitorsResponseTypeDef,
    ListPredictorBacktestExportJobsResponseTypeDef,
    ListPredictorsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWhatIfAnalysesResponseTypeDef,
    ListWhatIfForecastExportsResponseTypeDef,
    ListWhatIfForecastsResponseTypeDef,
    MonitorConfigTypeDef,
    SchemaTypeDef,
    TagTypeDef,
    TimeAlignmentBoundaryTypeDef,
    TimeSeriesReplacementsDataSourceTypeDef,
    TimeSeriesSelectorTypeDef,
    TimeSeriesTransformationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ForecastServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class ForecastServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ForecastServiceClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#close)
        """
    def create_auto_predictor(
        self,
        *,
        PredictorName: str,
        ForecastHorizon: int = None,
        ForecastTypes: List[str] = None,
        ForecastDimensions: List[str] = None,
        ForecastFrequency: str = None,
        DataConfig: "DataConfigTypeDef" = None,
        EncryptionConfig: "EncryptionConfigTypeDef" = None,
        ReferencePredictorArn: str = None,
        OptimizationMetric: OptimizationMetricType = None,
        ExplainPredictor: bool = None,
        Tags: List["TagTypeDef"] = None,
        MonitorConfig: "MonitorConfigTypeDef" = None,
        TimeAlignmentBoundary: "TimeAlignmentBoundaryTypeDef" = None
    ) -> CreateAutoPredictorResponseTypeDef:
        """
        Creates an Amazon Forecast predictor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.create_auto_predictor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_auto_predictor)
        """
    def create_dataset(
        self,
        *,
        DatasetName: str,
        Domain: DomainType,
        DatasetType: DatasetTypeType,
        Schema: "SchemaTypeDef",
        DataFrequency: str = None,
        EncryptionConfig: "EncryptionConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDatasetResponseTypeDef:
        """
        Creates an Amazon Forecast dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.create_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_dataset)
        """
    def create_dataset_group(
        self,
        *,
        DatasetGroupName: str,
        Domain: DomainType,
        DatasetArns: List[str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDatasetGroupResponseTypeDef:
        """
        Creates a dataset group, which holds a collection of related datasets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.create_dataset_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_dataset_group)
        """
    def create_dataset_import_job(
        self,
        *,
        DatasetImportJobName: str,
        DatasetArn: str,
        DataSource: "DataSourceTypeDef",
        TimestampFormat: str = None,
        TimeZone: str = None,
        UseGeolocationForTimeZone: bool = None,
        GeolocationFormat: str = None,
        Tags: List["TagTypeDef"] = None,
        Format: str = None,
        ImportMode: ImportModeType = None
    ) -> CreateDatasetImportJobResponseTypeDef:
        """
        Imports your training data to an Amazon Forecast dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.create_dataset_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_dataset_import_job)
        """
    def create_explainability(
        self,
        *,
        ExplainabilityName: str,
        ResourceArn: str,
        ExplainabilityConfig: "ExplainabilityConfigTypeDef",
        DataSource: "DataSourceTypeDef" = None,
        Schema: "SchemaTypeDef" = None,
        EnableVisualization: bool = None,
        StartDateTime: str = None,
        EndDateTime: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateExplainabilityResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.create_explainability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_explainability)
        """
    def create_explainability_export(
        self,
        *,
        ExplainabilityExportName: str,
        ExplainabilityArn: str,
        Destination: "DataDestinationTypeDef",
        Tags: List["TagTypeDef"] = None,
        Format: str = None
    ) -> CreateExplainabilityExportResponseTypeDef:
        """
        Exports an Explainability resource created by the  CreateExplainability
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.create_explainability_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_explainability_export)
        """
    def create_forecast(
        self,
        *,
        ForecastName: str,
        PredictorArn: str,
        ForecastTypes: List[str] = None,
        Tags: List["TagTypeDef"] = None,
        TimeSeriesSelector: "TimeSeriesSelectorTypeDef" = None
    ) -> CreateForecastResponseTypeDef:
        """
        Creates a forecast for each item in the `TARGET_TIME_SERIES` dataset that was
        used to train the predictor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.create_forecast)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_forecast)
        """
    def create_forecast_export_job(
        self,
        *,
        ForecastExportJobName: str,
        ForecastArn: str,
        Destination: "DataDestinationTypeDef",
        Tags: List["TagTypeDef"] = None,
        Format: str = None
    ) -> CreateForecastExportJobResponseTypeDef:
        """
        Exports a forecast created by the  CreateForecast operation to your Amazon
        Simple Storage Service (Amazon S3) bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.create_forecast_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_forecast_export_job)
        """
    def create_monitor(
        self, *, MonitorName: str, ResourceArn: str, Tags: List["TagTypeDef"] = None
    ) -> CreateMonitorResponseTypeDef:
        """
        Creates a predictor monitor resource for an existing auto predictor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.create_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_monitor)
        """
    def create_predictor(
        self,
        *,
        PredictorName: str,
        ForecastHorizon: int,
        InputDataConfig: "InputDataConfigTypeDef",
        FeaturizationConfig: "FeaturizationConfigTypeDef",
        AlgorithmArn: str = None,
        ForecastTypes: List[str] = None,
        PerformAutoML: bool = None,
        AutoMLOverrideStrategy: AutoMLOverrideStrategyType = None,
        PerformHPO: bool = None,
        TrainingParameters: Dict[str, str] = None,
        EvaluationParameters: "EvaluationParametersTypeDef" = None,
        HPOConfig: "HyperParameterTuningJobConfigTypeDef" = None,
        EncryptionConfig: "EncryptionConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        OptimizationMetric: OptimizationMetricType = None
    ) -> CreatePredictorResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.create_predictor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_predictor)
        """
    def create_predictor_backtest_export_job(
        self,
        *,
        PredictorBacktestExportJobName: str,
        PredictorArn: str,
        Destination: "DataDestinationTypeDef",
        Tags: List["TagTypeDef"] = None,
        Format: str = None
    ) -> CreatePredictorBacktestExportJobResponseTypeDef:
        """
        Exports backtest forecasts and accuracy metrics generated by the
        CreateAutoPredictor or  CreatePredictor operations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.create_predictor_backtest_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_predictor_backtest_export_job)
        """
    def create_what_if_analysis(
        self,
        *,
        WhatIfAnalysisName: str,
        ForecastArn: str,
        TimeSeriesSelector: "TimeSeriesSelectorTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateWhatIfAnalysisResponseTypeDef:
        """
        What-if analysis is a scenario modeling technique where you make a hypothetical
        change to a time series and compare the forecasts generated by these changes
        against the baseline, unchanged time series.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.create_what_if_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_what_if_analysis)
        """
    def create_what_if_forecast(
        self,
        *,
        WhatIfForecastName: str,
        WhatIfAnalysisArn: str,
        TimeSeriesTransformations: List["TimeSeriesTransformationTypeDef"] = None,
        TimeSeriesReplacementsDataSource: "TimeSeriesReplacementsDataSourceTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateWhatIfForecastResponseTypeDef:
        """
        A what-if forecast is a forecast that is created from a modified version of the
        baseline forecast.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.create_what_if_forecast)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_what_if_forecast)
        """
    def create_what_if_forecast_export(
        self,
        *,
        WhatIfForecastExportName: str,
        WhatIfForecastArns: List[str],
        Destination: "DataDestinationTypeDef",
        Tags: List["TagTypeDef"] = None,
        Format: str = None
    ) -> CreateWhatIfForecastExportResponseTypeDef:
        """
        Exports a forecast created by the  CreateWhatIfForecast operation to your Amazon
        Simple Storage Service (Amazon S3) bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.create_what_if_forecast_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_what_if_forecast_export)
        """
    def delete_dataset(self, *, DatasetArn: str) -> None:
        """
        Deletes an Amazon Forecast dataset that was created using the `CreateDataset
        <https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html>`__
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.delete_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_dataset)
        """
    def delete_dataset_group(self, *, DatasetGroupArn: str) -> None:
        """
        Deletes a dataset group created using the `CreateDatasetGroup
        <https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html>`__
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.delete_dataset_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_dataset_group)
        """
    def delete_dataset_import_job(self, *, DatasetImportJobArn: str) -> None:
        """
        Deletes a dataset import job created using the `CreateDatasetImportJob <https://
        docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html>`__
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.delete_dataset_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_dataset_import_job)
        """
    def delete_explainability(self, *, ExplainabilityArn: str) -> None:
        """
        Deletes an Explainability resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.delete_explainability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_explainability)
        """
    def delete_explainability_export(self, *, ExplainabilityExportArn: str) -> None:
        """
        Deletes an Explainability export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.delete_explainability_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_explainability_export)
        """
    def delete_forecast(self, *, ForecastArn: str) -> None:
        """
        Deletes a forecast created using the  CreateForecast operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.delete_forecast)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_forecast)
        """
    def delete_forecast_export_job(self, *, ForecastExportJobArn: str) -> None:
        """
        Deletes a forecast export job created using the  CreateForecastExportJob
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.delete_forecast_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_forecast_export_job)
        """
    def delete_monitor(self, *, MonitorArn: str) -> None:
        """
        Deletes a monitor resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.delete_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_monitor)
        """
    def delete_predictor(self, *, PredictorArn: str) -> None:
        """
        Deletes a predictor created using the  DescribePredictor or  CreatePredictor
        operations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.delete_predictor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_predictor)
        """
    def delete_predictor_backtest_export_job(self, *, PredictorBacktestExportJobArn: str) -> None:
        """
        Deletes a predictor backtest export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.delete_predictor_backtest_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_predictor_backtest_export_job)
        """
    def delete_resource_tree(self, *, ResourceArn: str) -> None:
        """
        Deletes an entire resource tree.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.delete_resource_tree)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_resource_tree)
        """
    def delete_what_if_analysis(self, *, WhatIfAnalysisArn: str) -> None:
        """
        Deletes a what-if analysis created using the  CreateWhatIfAnalysis operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.delete_what_if_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_what_if_analysis)
        """
    def delete_what_if_forecast(self, *, WhatIfForecastArn: str) -> None:
        """
        Deletes a what-if forecast created using the  CreateWhatIfForecast operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.delete_what_if_forecast)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_what_if_forecast)
        """
    def delete_what_if_forecast_export(self, *, WhatIfForecastExportArn: str) -> None:
        """
        Deletes a what-if forecast export created using the  CreateWhatIfForecastExport
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.delete_what_if_forecast_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_what_if_forecast_export)
        """
    def describe_auto_predictor(self, *, PredictorArn: str) -> DescribeAutoPredictorResponseTypeDef:
        """
        Describes a predictor created using the CreateAutoPredictor operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.describe_auto_predictor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_auto_predictor)
        """
    def describe_dataset(self, *, DatasetArn: str) -> DescribeDatasetResponseTypeDef:
        """
        Describes an Amazon Forecast dataset created using the `CreateDataset
        <https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html>`__
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.describe_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_dataset)
        """
    def describe_dataset_group(
        self, *, DatasetGroupArn: str
    ) -> DescribeDatasetGroupResponseTypeDef:
        """
        Describes a dataset group created using the `CreateDatasetGroup
        <https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html>`__
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.describe_dataset_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_dataset_group)
        """
    def describe_dataset_import_job(
        self, *, DatasetImportJobArn: str
    ) -> DescribeDatasetImportJobResponseTypeDef:
        """
        Describes a dataset import job created using the `CreateDatasetImportJob <https:
        //docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html>`__
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.describe_dataset_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_dataset_import_job)
        """
    def describe_explainability(
        self, *, ExplainabilityArn: str
    ) -> DescribeExplainabilityResponseTypeDef:
        """
        Describes an Explainability resource created using the  CreateExplainability
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.describe_explainability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_explainability)
        """
    def describe_explainability_export(
        self, *, ExplainabilityExportArn: str
    ) -> DescribeExplainabilityExportResponseTypeDef:
        """
        Describes an Explainability export created using the  CreateExplainabilityExport
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.describe_explainability_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_explainability_export)
        """
    def describe_forecast(self, *, ForecastArn: str) -> DescribeForecastResponseTypeDef:
        """
        Describes a forecast created using the  CreateForecast operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.describe_forecast)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_forecast)
        """
    def describe_forecast_export_job(
        self, *, ForecastExportJobArn: str
    ) -> DescribeForecastExportJobResponseTypeDef:
        """
        Describes a forecast export job created using the  CreateForecastExportJob
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.describe_forecast_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_forecast_export_job)
        """
    def describe_monitor(self, *, MonitorArn: str) -> DescribeMonitorResponseTypeDef:
        """
        Describes a monitor resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.describe_monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_monitor)
        """
    def describe_predictor(self, *, PredictorArn: str) -> DescribePredictorResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.describe_predictor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_predictor)
        """
    def describe_predictor_backtest_export_job(
        self, *, PredictorBacktestExportJobArn: str
    ) -> DescribePredictorBacktestExportJobResponseTypeDef:
        """
        Describes a predictor backtest export job created using the
        CreatePredictorBacktestExportJob operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.describe_predictor_backtest_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_predictor_backtest_export_job)
        """
    def describe_what_if_analysis(
        self, *, WhatIfAnalysisArn: str
    ) -> DescribeWhatIfAnalysisResponseTypeDef:
        """
        Describes the what-if analysis created using the  CreateWhatIfAnalysis
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.describe_what_if_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_what_if_analysis)
        """
    def describe_what_if_forecast(
        self, *, WhatIfForecastArn: str
    ) -> DescribeWhatIfForecastResponseTypeDef:
        """
        Describes the what-if forecast created using the  CreateWhatIfForecast
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.describe_what_if_forecast)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_what_if_forecast)
        """
    def describe_what_if_forecast_export(
        self, *, WhatIfForecastExportArn: str
    ) -> DescribeWhatIfForecastExportResponseTypeDef:
        """
        Describes the what-if forecast export created using the
        CreateWhatIfForecastExport operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.describe_what_if_forecast_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_what_if_forecast_export)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#generate_presigned_url)
        """
    def get_accuracy_metrics(self, *, PredictorArn: str) -> GetAccuracyMetricsResponseTypeDef:
        """
        Provides metrics on the accuracy of the models that were trained by the
        CreatePredictor operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.get_accuracy_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#get_accuracy_metrics)
        """
    def list_dataset_groups(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListDatasetGroupsResponseTypeDef:
        """
        Returns a list of dataset groups created using the `CreateDatasetGroup
        <https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html>`__
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.list_dataset_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_dataset_groups)
        """
    def list_dataset_import_jobs(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListDatasetImportJobsResponseTypeDef:
        """
        Returns a list of dataset import jobs created using the `CreateDatasetImportJob
        <https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html>
        `__ operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.list_dataset_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_dataset_import_jobs)
        """
    def list_datasets(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        Returns a list of datasets created using the `CreateDataset
        <https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html>`__
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.list_datasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_datasets)
        """
    def list_explainabilities(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListExplainabilitiesResponseTypeDef:
        """
        Returns a list of Explainability resources created using the
        CreateExplainability operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.list_explainabilities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_explainabilities)
        """
    def list_explainability_exports(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListExplainabilityExportsResponseTypeDef:
        """
        Returns a list of Explainability exports created using the
        CreateExplainabilityExport operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.list_explainability_exports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_explainability_exports)
        """
    def list_forecast_export_jobs(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListForecastExportJobsResponseTypeDef:
        """
        Returns a list of forecast export jobs created using the
        CreateForecastExportJob operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.list_forecast_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_forecast_export_jobs)
        """
    def list_forecasts(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListForecastsResponseTypeDef:
        """
        Returns a list of forecasts created using the  CreateForecast operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.list_forecasts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_forecasts)
        """
    def list_monitor_evaluations(
        self,
        *,
        MonitorArn: str,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListMonitorEvaluationsResponseTypeDef:
        """
        Returns a list of the monitoring evaluation results and predictor events
        collected by the monitor resource during different windows of time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.list_monitor_evaluations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_monitor_evaluations)
        """
    def list_monitors(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListMonitorsResponseTypeDef:
        """
        Returns a list of monitors created with the  CreateMonitor operation and
        CreateAutoPredictor operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.list_monitors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_monitors)
        """
    def list_predictor_backtest_export_jobs(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListPredictorBacktestExportJobsResponseTypeDef:
        """
        Returns a list of predictor backtest export jobs created using the
        CreatePredictorBacktestExportJob operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.list_predictor_backtest_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_predictor_backtest_export_jobs)
        """
    def list_predictors(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListPredictorsResponseTypeDef:
        """
        Returns a list of predictors created using the  CreateAutoPredictor or
        CreatePredictor operations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.list_predictors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_predictors)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for an Amazon Forecast resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_tags_for_resource)
        """
    def list_what_if_analyses(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListWhatIfAnalysesResponseTypeDef:
        """
        Returns a list of what-if analyses created using the  CreateWhatIfAnalysis
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.list_what_if_analyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_what_if_analyses)
        """
    def list_what_if_forecast_exports(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListWhatIfForecastExportsResponseTypeDef:
        """
        Returns a list of what-if forecast exports created using the
        CreateWhatIfForecastExport operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.list_what_if_forecast_exports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_what_if_forecast_exports)
        """
    def list_what_if_forecasts(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> ListWhatIfForecastsResponseTypeDef:
        """
        Returns a list of what-if forecasts created using the  CreateWhatIfForecast
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.list_what_if_forecasts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_what_if_forecasts)
        """
    def resume_resource(self, *, ResourceArn: str) -> None:
        """
        Resumes a stopped monitor resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.resume_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#resume_resource)
        """
    def stop_resource(self, *, ResourceArn: str) -> None:
        """
        Stops a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.stop_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#stop_resource)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified `resourceArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes the specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#untag_resource)
        """
    def update_dataset_group(
        self, *, DatasetGroupArn: str, DatasetArns: List[str]
    ) -> Dict[str, Any]:
        """
        Replaces the datasets in a dataset group with the specified datasets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Client.update_dataset_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#update_dataset_group)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_groups"]
    ) -> ListDatasetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Paginator.ListDatasetGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listdatasetgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_import_jobs"]
    ) -> ListDatasetImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Paginator.ListDatasetImportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listdatasetimportjobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_datasets"]) -> ListDatasetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Paginator.ListDatasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listdatasetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_explainabilities"]
    ) -> ListExplainabilitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Paginator.ListExplainabilities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listexplainabilitiespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_explainability_exports"]
    ) -> ListExplainabilityExportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Paginator.ListExplainabilityExports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listexplainabilityexportspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_forecast_export_jobs"]
    ) -> ListForecastExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Paginator.ListForecastExportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listforecastexportjobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_forecasts"]) -> ListForecastsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Paginator.ListForecasts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listforecastspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitor_evaluations"]
    ) -> ListMonitorEvaluationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Paginator.ListMonitorEvaluations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listmonitorevaluationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_monitors"]) -> ListMonitorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Paginator.ListMonitors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listmonitorspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_predictor_backtest_export_jobs"]
    ) -> ListPredictorBacktestExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Paginator.ListPredictorBacktestExportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listpredictorbacktestexportjobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_predictors"]) -> ListPredictorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Paginator.ListPredictors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listpredictorspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_what_if_analyses"]
    ) -> ListWhatIfAnalysesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Paginator.ListWhatIfAnalyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listwhatifanalysespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_what_if_forecast_exports"]
    ) -> ListWhatIfForecastExportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Paginator.ListWhatIfForecastExports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listwhatifforecastexportspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_what_if_forecasts"]
    ) -> ListWhatIfForecastsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/forecast.html#ForecastService.Paginator.ListWhatIfForecasts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listwhatifforecastspaginator)
        """
