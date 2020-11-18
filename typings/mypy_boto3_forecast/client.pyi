# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for forecast service client

Usage::

    ```python
    import boto3
    from mypy_boto3_forecast import ForecastServiceClient

    client: ForecastServiceClient = boto3.client("forecast")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_forecast.paginator import (
    ListDatasetGroupsPaginator,
    ListDatasetImportJobsPaginator,
    ListDatasetsPaginator,
    ListForecastExportJobsPaginator,
    ListForecastsPaginator,
    ListPredictorsPaginator,
)
from mypy_boto3_forecast.type_defs import (
    CreateDatasetGroupResponseTypeDef,
    CreateDatasetImportJobResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateForecastExportJobResponseTypeDef,
    CreateForecastResponseTypeDef,
    CreatePredictorResponseTypeDef,
    DataDestinationTypeDef,
    DataSourceTypeDef,
    DescribeDatasetGroupResponseTypeDef,
    DescribeDatasetImportJobResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeForecastExportJobResponseTypeDef,
    DescribeForecastResponseTypeDef,
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


class ForecastServiceClient:
    """
    [ForecastService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.can_paginate)
        """

    def create_dataset(
        self,
        DatasetName: str,
        Domain: Literal[
            "RETAIL",
            "CUSTOM",
            "INVENTORY_PLANNING",
            "EC2_CAPACITY",
            "WORK_FORCE",
            "WEB_TRAFFIC",
            "METRICS",
        ],
        DatasetType: Literal["TARGET_TIME_SERIES", "RELATED_TIME_SERIES", "ITEM_METADATA"],
        Schema: "SchemaTypeDef",
        DataFrequency: str = None,
        EncryptionConfig: "EncryptionConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDatasetResponseTypeDef:
        """
        [Client.create_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.create_dataset)
        """

    def create_dataset_group(
        self,
        DatasetGroupName: str,
        Domain: Literal[
            "RETAIL",
            "CUSTOM",
            "INVENTORY_PLANNING",
            "EC2_CAPACITY",
            "WORK_FORCE",
            "WEB_TRAFFIC",
            "METRICS",
        ],
        DatasetArns: List[str] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDatasetGroupResponseTypeDef:
        """
        [Client.create_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.create_dataset_group)
        """

    def create_dataset_import_job(
        self,
        DatasetImportJobName: str,
        DatasetArn: str,
        DataSource: "DataSourceTypeDef",
        TimestampFormat: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDatasetImportJobResponseTypeDef:
        """
        [Client.create_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.create_dataset_import_job)
        """

    def create_forecast(
        self,
        ForecastName: str,
        PredictorArn: str,
        ForecastTypes: List[str] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateForecastResponseTypeDef:
        """
        [Client.create_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.create_forecast)
        """

    def create_forecast_export_job(
        self,
        ForecastExportJobName: str,
        ForecastArn: str,
        Destination: "DataDestinationTypeDef",
        Tags: List["TagTypeDef"] = None,
    ) -> CreateForecastExportJobResponseTypeDef:
        """
        [Client.create_forecast_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.create_forecast_export_job)
        """

    def create_predictor(
        self,
        PredictorName: str,
        ForecastHorizon: int,
        InputDataConfig: "InputDataConfigTypeDef",
        FeaturizationConfig: "FeaturizationConfigTypeDef",
        AlgorithmArn: str = None,
        ForecastTypes: List[str] = None,
        PerformAutoML: bool = None,
        PerformHPO: bool = None,
        TrainingParameters: Dict[str, str] = None,
        EvaluationParameters: "EvaluationParametersTypeDef" = None,
        HPOConfig: "HyperParameterTuningJobConfigTypeDef" = None,
        EncryptionConfig: "EncryptionConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreatePredictorResponseTypeDef:
        """
        [Client.create_predictor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.create_predictor)
        """

    def delete_dataset(self, DatasetArn: str) -> None:
        """
        [Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.delete_dataset)
        """

    def delete_dataset_group(self, DatasetGroupArn: str) -> None:
        """
        [Client.delete_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.delete_dataset_group)
        """

    def delete_dataset_import_job(self, DatasetImportJobArn: str) -> None:
        """
        [Client.delete_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.delete_dataset_import_job)
        """

    def delete_forecast(self, ForecastArn: str) -> None:
        """
        [Client.delete_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.delete_forecast)
        """

    def delete_forecast_export_job(self, ForecastExportJobArn: str) -> None:
        """
        [Client.delete_forecast_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.delete_forecast_export_job)
        """

    def delete_predictor(self, PredictorArn: str) -> None:
        """
        [Client.delete_predictor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.delete_predictor)
        """

    def describe_dataset(self, DatasetArn: str) -> DescribeDatasetResponseTypeDef:
        """
        [Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.describe_dataset)
        """

    def describe_dataset_group(self, DatasetGroupArn: str) -> DescribeDatasetGroupResponseTypeDef:
        """
        [Client.describe_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.describe_dataset_group)
        """

    def describe_dataset_import_job(
        self, DatasetImportJobArn: str
    ) -> DescribeDatasetImportJobResponseTypeDef:
        """
        [Client.describe_dataset_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.describe_dataset_import_job)
        """

    def describe_forecast(self, ForecastArn: str) -> DescribeForecastResponseTypeDef:
        """
        [Client.describe_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.describe_forecast)
        """

    def describe_forecast_export_job(
        self, ForecastExportJobArn: str
    ) -> DescribeForecastExportJobResponseTypeDef:
        """
        [Client.describe_forecast_export_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.describe_forecast_export_job)
        """

    def describe_predictor(self, PredictorArn: str) -> DescribePredictorResponseTypeDef:
        """
        [Client.describe_predictor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.describe_predictor)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.generate_presigned_url)
        """

    def get_accuracy_metrics(self, PredictorArn: str) -> GetAccuracyMetricsResponseTypeDef:
        """
        [Client.get_accuracy_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.get_accuracy_metrics)
        """

    def list_dataset_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListDatasetGroupsResponseTypeDef:
        """
        [Client.list_dataset_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.list_dataset_groups)
        """

    def list_dataset_import_jobs(
        self, NextToken: str = None, MaxResults: int = None, Filters: List[FilterTypeDef] = None
    ) -> ListDatasetImportJobsResponseTypeDef:
        """
        [Client.list_dataset_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.list_dataset_import_jobs)
        """

    def list_datasets(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        [Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.list_datasets)
        """

    def list_forecast_export_jobs(
        self, NextToken: str = None, MaxResults: int = None, Filters: List[FilterTypeDef] = None
    ) -> ListForecastExportJobsResponseTypeDef:
        """
        [Client.list_forecast_export_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.list_forecast_export_jobs)
        """

    def list_forecasts(
        self, NextToken: str = None, MaxResults: int = None, Filters: List[FilterTypeDef] = None
    ) -> ListForecastsResponseTypeDef:
        """
        [Client.list_forecasts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.list_forecasts)
        """

    def list_predictors(
        self, NextToken: str = None, MaxResults: int = None, Filters: List[FilterTypeDef] = None
    ) -> ListPredictorsResponseTypeDef:
        """
        [Client.list_predictors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.list_predictors)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.untag_resource)
        """

    def update_dataset_group(self, DatasetGroupArn: str, DatasetArns: List[str]) -> Dict[str, Any]:
        """
        [Client.update_dataset_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Client.update_dataset_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_groups"]
    ) -> ListDatasetGroupsPaginator:
        """
        [Paginator.ListDatasetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListDatasetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_import_jobs"]
    ) -> ListDatasetImportJobsPaginator:
        """
        [Paginator.ListDatasetImportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListDatasetImportJobs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_datasets"]) -> ListDatasetsPaginator:
        """
        [Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListDatasets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_forecast_export_jobs"]
    ) -> ListForecastExportJobsPaginator:
        """
        [Paginator.ListForecastExportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListForecastExportJobs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_forecasts"]) -> ListForecastsPaginator:
        """
        [Paginator.ListForecasts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListForecasts)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_predictors"]) -> ListPredictorsPaginator:
        """
        [Paginator.ListPredictors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListPredictors)
        """
