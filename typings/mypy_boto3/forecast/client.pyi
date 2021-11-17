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

from .literals import DatasetTypeType, DomainType, OptimizationMetricType
from .paginator import (
    ListDatasetGroupsPaginator,
    ListDatasetImportJobsPaginator,
    ListDatasetsPaginator,
    ListForecastExportJobsPaginator,
    ListForecastsPaginator,
    ListPredictorBacktestExportJobsPaginator,
    ListPredictorsPaginator,
)
from .type_defs import (
    CreateDatasetGroupResponseTypeDef,
    CreateDatasetImportJobResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateForecastExportJobResponseTypeDef,
    CreateForecastResponseTypeDef,
    CreatePredictorBacktestExportJobResponseTypeDef,
    CreatePredictorResponseTypeDef,
    DataDestinationTypeDef,
    DataSourceTypeDef,
    DescribeDatasetGroupResponseTypeDef,
    DescribeDatasetImportJobResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeForecastExportJobResponseTypeDef,
    DescribeForecastResponseTypeDef,
    DescribePredictorBacktestExportJobResponseTypeDef,
    DescribePredictorResponseTypeDef,
    EncryptionConfigTypeDef,
    EvaluationParametersTypeDef,
    FeaturizationConfigTypeDef,
    FilterTypeDef,
    GetAccuracyMetricsResponseTypeDef,
    HyperParameterTuningJobConfigTypeDef,
    InputDataConfigTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListForecastExportJobsResponseTypeDef,
    ListForecastsResponseTypeDef,
    ListPredictorBacktestExportJobsResponseTypeDef,
    ListPredictorsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    SchemaTypeDef,
    TagTypeDef,
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#can_paginate)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.create_dataset)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.create_dataset_group)
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
        Tags: List["TagTypeDef"] = None
    ) -> CreateDatasetImportJobResponseTypeDef:
        """
        Imports your training data to an Amazon Forecast dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.create_dataset_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_dataset_import_job)
        """
    def create_forecast(
        self,
        *,
        ForecastName: str,
        PredictorArn: str,
        ForecastTypes: List[str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateForecastResponseTypeDef:
        """
        Creates a forecast for each item in the `TARGET_TIME_SERIES` dataset that was
        used to train the predictor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.create_forecast)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_forecast)
        """
    def create_forecast_export_job(
        self,
        *,
        ForecastExportJobName: str,
        ForecastArn: str,
        Destination: "DataDestinationTypeDef",
        Tags: List["TagTypeDef"] = None
    ) -> CreateForecastExportJobResponseTypeDef:
        """
        Exports a forecast created by the  CreateForecast operation to your Amazon
        Simple Storage Service (Amazon S3) bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.create_forecast_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_forecast_export_job)
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
        AutoMLOverrideStrategy: Literal["LatencyOptimized"] = None,
        PerformHPO: bool = None,
        TrainingParameters: Dict[str, str] = None,
        EvaluationParameters: "EvaluationParametersTypeDef" = None,
        HPOConfig: "HyperParameterTuningJobConfigTypeDef" = None,
        EncryptionConfig: "EncryptionConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        OptimizationMetric: OptimizationMetricType = None
    ) -> CreatePredictorResponseTypeDef:
        """
        Creates an Amazon Forecast predictor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.create_predictor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_predictor)
        """
    def create_predictor_backtest_export_job(
        self,
        *,
        PredictorBacktestExportJobName: str,
        PredictorArn: str,
        Destination: "DataDestinationTypeDef",
        Tags: List["TagTypeDef"] = None
    ) -> CreatePredictorBacktestExportJobResponseTypeDef:
        """
        Exports backtest forecasts and accuracy metrics generated by the
        CreatePredictor operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.create_predictor_backtest_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#create_predictor_backtest_export_job)
        """
    def delete_dataset(self, *, DatasetArn: str) -> None:
        """
        Deletes an Amazon Forecast dataset that was created using the  CreateDataset
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.delete_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_dataset)
        """
    def delete_dataset_group(self, *, DatasetGroupArn: str) -> None:
        """
        Deletes a dataset group created using the  CreateDatasetGroup operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.delete_dataset_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_dataset_group)
        """
    def delete_dataset_import_job(self, *, DatasetImportJobArn: str) -> None:
        """
        Deletes a dataset import job created using the  CreateDatasetImportJob
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.delete_dataset_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_dataset_import_job)
        """
    def delete_forecast(self, *, ForecastArn: str) -> None:
        """
        Deletes a forecast created using the  CreateForecast operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.delete_forecast)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_forecast)
        """
    def delete_forecast_export_job(self, *, ForecastExportJobArn: str) -> None:
        """
        Deletes a forecast export job created using the  CreateForecastExportJob
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.delete_forecast_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_forecast_export_job)
        """
    def delete_predictor(self, *, PredictorArn: str) -> None:
        """
        Deletes a predictor created using the  CreatePredictor operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.delete_predictor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_predictor)
        """
    def delete_predictor_backtest_export_job(self, *, PredictorBacktestExportJobArn: str) -> None:
        """
        Deletes a predictor backtest export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.delete_predictor_backtest_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_predictor_backtest_export_job)
        """
    def delete_resource_tree(self, *, ResourceArn: str) -> None:
        """
        Deletes an entire resource tree.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.delete_resource_tree)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#delete_resource_tree)
        """
    def describe_dataset(self, *, DatasetArn: str) -> DescribeDatasetResponseTypeDef:
        """
        Describes an Amazon Forecast dataset created using the  CreateDataset operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.describe_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_dataset)
        """
    def describe_dataset_group(
        self, *, DatasetGroupArn: str
    ) -> DescribeDatasetGroupResponseTypeDef:
        """
        Describes a dataset group created using the  CreateDatasetGroup operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.describe_dataset_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_dataset_group)
        """
    def describe_dataset_import_job(
        self, *, DatasetImportJobArn: str
    ) -> DescribeDatasetImportJobResponseTypeDef:
        """
        Describes a dataset import job created using the  CreateDatasetImportJob
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.describe_dataset_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_dataset_import_job)
        """
    def describe_forecast(self, *, ForecastArn: str) -> DescribeForecastResponseTypeDef:
        """
        Describes a forecast created using the  CreateForecast operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.describe_forecast)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_forecast)
        """
    def describe_forecast_export_job(
        self, *, ForecastExportJobArn: str
    ) -> DescribeForecastExportJobResponseTypeDef:
        """
        Describes a forecast export job created using the  CreateForecastExportJob
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.describe_forecast_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_forecast_export_job)
        """
    def describe_predictor(self, *, PredictorArn: str) -> DescribePredictorResponseTypeDef:
        """
        Describes a predictor created using the  CreatePredictor operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.describe_predictor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_predictor)
        """
    def describe_predictor_backtest_export_job(
        self, *, PredictorBacktestExportJobArn: str
    ) -> DescribePredictorBacktestExportJobResponseTypeDef:
        """
        Describes a predictor backtest export job created using the
        CreatePredictorBacktestExportJob operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.describe_predictor_backtest_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#describe_predictor_backtest_export_job)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#generate_presigned_url)
        """
    def get_accuracy_metrics(self, *, PredictorArn: str) -> GetAccuracyMetricsResponseTypeDef:
        """
        Provides metrics on the accuracy of the models that were trained by the
        CreatePredictor operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.get_accuracy_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#get_accuracy_metrics)
        """
    def list_dataset_groups(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListDatasetGroupsResponseTypeDef:
        """
        Returns a list of dataset groups created using the  CreateDatasetGroup
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.list_dataset_groups)
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
        Returns a list of dataset import jobs created using the  CreateDatasetImportJob
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.list_dataset_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_dataset_import_jobs)
        """
    def list_datasets(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        Returns a list of datasets created using the  CreateDataset operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.list_datasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_datasets)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.list_forecast_export_jobs)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.list_forecasts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_forecasts)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.list_predictor_backtest_export_jobs)
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
        Returns a list of predictors created using the  CreatePredictor operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.list_predictors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_predictors)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for an Amazon Forecast resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#list_tags_for_resource)
        """
    def stop_resource(self, *, ResourceArn: str) -> None:
        """
        Stops a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.stop_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#stop_resource)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified `resourceArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes the specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#untag_resource)
        """
    def update_dataset_group(
        self, *, DatasetGroupArn: str, DatasetArns: List[str]
    ) -> Dict[str, Any]:
        """
        Replaces the datasets in a dataset group with the specified datasets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Client.update_dataset_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/client.html#update_dataset_group)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_groups"]
    ) -> ListDatasetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Paginator.ListDatasetGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listdatasetgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_import_jobs"]
    ) -> ListDatasetImportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Paginator.ListDatasetImportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listdatasetimportjobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_datasets"]) -> ListDatasetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Paginator.ListDatasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listdatasetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_forecast_export_jobs"]
    ) -> ListForecastExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Paginator.ListForecastExportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listforecastexportjobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_forecasts"]) -> ListForecastsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Paginator.ListForecasts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listforecastspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_predictor_backtest_export_jobs"]
    ) -> ListPredictorBacktestExportJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Paginator.ListPredictorBacktestExportJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listpredictorbacktestexportjobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_predictors"]) -> ListPredictorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/forecast.html#ForecastService.Paginator.ListPredictors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators.html#listpredictorspaginator)
        """
