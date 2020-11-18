# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for machinelearning service client

Usage::

    ```python
    import boto3
    from mypy_boto3_machinelearning import MachineLearningClient

    client: MachineLearningClient = boto3.client("machinelearning")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_machinelearning.paginator import (
    DescribeBatchPredictionsPaginator,
    DescribeDataSourcesPaginator,
    DescribeEvaluationsPaginator,
    DescribeMLModelsPaginator,
)
from mypy_boto3_machinelearning.type_defs import (
    AddTagsOutputTypeDef,
    CreateBatchPredictionOutputTypeDef,
    CreateDataSourceFromRDSOutputTypeDef,
    CreateDataSourceFromRedshiftOutputTypeDef,
    CreateDataSourceFromS3OutputTypeDef,
    CreateEvaluationOutputTypeDef,
    CreateMLModelOutputTypeDef,
    CreateRealtimeEndpointOutputTypeDef,
    DeleteBatchPredictionOutputTypeDef,
    DeleteDataSourceOutputTypeDef,
    DeleteEvaluationOutputTypeDef,
    DeleteMLModelOutputTypeDef,
    DeleteRealtimeEndpointOutputTypeDef,
    DeleteTagsOutputTypeDef,
    DescribeBatchPredictionsOutputTypeDef,
    DescribeDataSourcesOutputTypeDef,
    DescribeEvaluationsOutputTypeDef,
    DescribeMLModelsOutputTypeDef,
    DescribeTagsOutputTypeDef,
    GetBatchPredictionOutputTypeDef,
    GetDataSourceOutputTypeDef,
    GetEvaluationOutputTypeDef,
    GetMLModelOutputTypeDef,
    PredictOutputTypeDef,
    RDSDataSpecTypeDef,
    RedshiftDataSpecTypeDef,
    S3DataSpecTypeDef,
    TagTypeDef,
    UpdateBatchPredictionOutputTypeDef,
    UpdateDataSourceOutputTypeDef,
    UpdateEvaluationOutputTypeDef,
    UpdateMLModelOutputTypeDef,
)
from mypy_boto3_machinelearning.waiter import (
    BatchPredictionAvailableWaiter,
    DataSourceAvailableWaiter,
    EvaluationAvailableWaiter,
    MLModelAvailableWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MachineLearningClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidTagException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    PredictorNotMountedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TagLimitExceededException: Type[BotocoreClientError]


class MachineLearningClient:
    """
    [MachineLearning.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_tags(
        self,
        Tags: List["TagTypeDef"],
        ResourceId: str,
        ResourceType: Literal["BatchPrediction", "DataSource", "Evaluation", "MLModel"],
    ) -> AddTagsOutputTypeDef:
        """
        [Client.add_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.add_tags)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.can_paginate)
        """

    def create_batch_prediction(
        self,
        BatchPredictionId: str,
        MLModelId: str,
        BatchPredictionDataSourceId: str,
        OutputUri: str,
        BatchPredictionName: str = None,
    ) -> CreateBatchPredictionOutputTypeDef:
        """
        [Client.create_batch_prediction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.create_batch_prediction)
        """

    def create_data_source_from_rds(
        self,
        DataSourceId: str,
        RDSData: RDSDataSpecTypeDef,
        RoleARN: str,
        DataSourceName: str = None,
        ComputeStatistics: bool = None,
    ) -> CreateDataSourceFromRDSOutputTypeDef:
        """
        [Client.create_data_source_from_rds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.create_data_source_from_rds)
        """

    def create_data_source_from_redshift(
        self,
        DataSourceId: str,
        DataSpec: RedshiftDataSpecTypeDef,
        RoleARN: str,
        DataSourceName: str = None,
        ComputeStatistics: bool = None,
    ) -> CreateDataSourceFromRedshiftOutputTypeDef:
        """
        [Client.create_data_source_from_redshift documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.create_data_source_from_redshift)
        """

    def create_data_source_from_s3(
        self,
        DataSourceId: str,
        DataSpec: S3DataSpecTypeDef,
        DataSourceName: str = None,
        ComputeStatistics: bool = None,
    ) -> CreateDataSourceFromS3OutputTypeDef:
        """
        [Client.create_data_source_from_s3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.create_data_source_from_s3)
        """

    def create_evaluation(
        self,
        EvaluationId: str,
        MLModelId: str,
        EvaluationDataSourceId: str,
        EvaluationName: str = None,
    ) -> CreateEvaluationOutputTypeDef:
        """
        [Client.create_evaluation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.create_evaluation)
        """

    def create_ml_model(
        self,
        MLModelId: str,
        MLModelType: Literal["REGRESSION", "BINARY", "MULTICLASS"],
        TrainingDataSourceId: str,
        MLModelName: str = None,
        Parameters: Dict[str, str] = None,
        Recipe: str = None,
        RecipeUri: str = None,
    ) -> CreateMLModelOutputTypeDef:
        """
        [Client.create_ml_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.create_ml_model)
        """

    def create_realtime_endpoint(self, MLModelId: str) -> CreateRealtimeEndpointOutputTypeDef:
        """
        [Client.create_realtime_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.create_realtime_endpoint)
        """

    def delete_batch_prediction(self, BatchPredictionId: str) -> DeleteBatchPredictionOutputTypeDef:
        """
        [Client.delete_batch_prediction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.delete_batch_prediction)
        """

    def delete_data_source(self, DataSourceId: str) -> DeleteDataSourceOutputTypeDef:
        """
        [Client.delete_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.delete_data_source)
        """

    def delete_evaluation(self, EvaluationId: str) -> DeleteEvaluationOutputTypeDef:
        """
        [Client.delete_evaluation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.delete_evaluation)
        """

    def delete_ml_model(self, MLModelId: str) -> DeleteMLModelOutputTypeDef:
        """
        [Client.delete_ml_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.delete_ml_model)
        """

    def delete_realtime_endpoint(self, MLModelId: str) -> DeleteRealtimeEndpointOutputTypeDef:
        """
        [Client.delete_realtime_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.delete_realtime_endpoint)
        """

    def delete_tags(
        self,
        TagKeys: List[str],
        ResourceId: str,
        ResourceType: Literal["BatchPrediction", "DataSource", "Evaluation", "MLModel"],
    ) -> DeleteTagsOutputTypeDef:
        """
        [Client.delete_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.delete_tags)
        """

    def describe_batch_predictions(
        self,
        FilterVariable: Literal[
            "CreatedAt",
            "LastUpdatedAt",
            "Status",
            "Name",
            "IAMUser",
            "MLModelId",
            "DataSourceId",
            "DataURI",
        ] = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: Literal["asc", "dsc"] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeBatchPredictionsOutputTypeDef:
        """
        [Client.describe_batch_predictions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.describe_batch_predictions)
        """

    def describe_data_sources(
        self,
        FilterVariable: Literal[
            "CreatedAt", "LastUpdatedAt", "Status", "Name", "DataLocationS3", "IAMUser"
        ] = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: Literal["asc", "dsc"] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeDataSourcesOutputTypeDef:
        """
        [Client.describe_data_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.describe_data_sources)
        """

    def describe_evaluations(
        self,
        FilterVariable: Literal[
            "CreatedAt",
            "LastUpdatedAt",
            "Status",
            "Name",
            "IAMUser",
            "MLModelId",
            "DataSourceId",
            "DataURI",
        ] = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: Literal["asc", "dsc"] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeEvaluationsOutputTypeDef:
        """
        [Client.describe_evaluations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.describe_evaluations)
        """

    def describe_ml_models(
        self,
        FilterVariable: Literal[
            "CreatedAt",
            "LastUpdatedAt",
            "Status",
            "Name",
            "IAMUser",
            "TrainingDataSourceId",
            "RealtimeEndpointStatus",
            "MLModelType",
            "Algorithm",
            "TrainingDataURI",
        ] = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: Literal["asc", "dsc"] = None,
        NextToken: str = None,
        Limit: int = None,
    ) -> DescribeMLModelsOutputTypeDef:
        """
        [Client.describe_ml_models documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.describe_ml_models)
        """

    def describe_tags(
        self,
        ResourceId: str,
        ResourceType: Literal["BatchPrediction", "DataSource", "Evaluation", "MLModel"],
    ) -> DescribeTagsOutputTypeDef:
        """
        [Client.describe_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.describe_tags)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.generate_presigned_url)
        """

    def get_batch_prediction(self, BatchPredictionId: str) -> GetBatchPredictionOutputTypeDef:
        """
        [Client.get_batch_prediction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.get_batch_prediction)
        """

    def get_data_source(
        self, DataSourceId: str, Verbose: bool = None
    ) -> GetDataSourceOutputTypeDef:
        """
        [Client.get_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.get_data_source)
        """

    def get_evaluation(self, EvaluationId: str) -> GetEvaluationOutputTypeDef:
        """
        [Client.get_evaluation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.get_evaluation)
        """

    def get_ml_model(self, MLModelId: str, Verbose: bool = None) -> GetMLModelOutputTypeDef:
        """
        [Client.get_ml_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.get_ml_model)
        """

    def predict(
        self, MLModelId: str, Record: Dict[str, str], PredictEndpoint: str
    ) -> PredictOutputTypeDef:
        """
        [Client.predict documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.predict)
        """

    def update_batch_prediction(
        self, BatchPredictionId: str, BatchPredictionName: str
    ) -> UpdateBatchPredictionOutputTypeDef:
        """
        [Client.update_batch_prediction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.update_batch_prediction)
        """

    def update_data_source(
        self, DataSourceId: str, DataSourceName: str
    ) -> UpdateDataSourceOutputTypeDef:
        """
        [Client.update_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.update_data_source)
        """

    def update_evaluation(
        self, EvaluationId: str, EvaluationName: str
    ) -> UpdateEvaluationOutputTypeDef:
        """
        [Client.update_evaluation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.update_evaluation)
        """

    def update_ml_model(
        self, MLModelId: str, MLModelName: str = None, ScoreThreshold: float = None
    ) -> UpdateMLModelOutputTypeDef:
        """
        [Client.update_ml_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Client.update_ml_model)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_batch_predictions"]
    ) -> DescribeBatchPredictionsPaginator:
        """
        [Paginator.DescribeBatchPredictions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeBatchPredictions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_data_sources"]
    ) -> DescribeDataSourcesPaginator:
        """
        [Paginator.DescribeDataSources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeDataSources)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_evaluations"]
    ) -> DescribeEvaluationsPaginator:
        """
        [Paginator.DescribeEvaluations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeEvaluations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ml_models"]
    ) -> DescribeMLModelsPaginator:
        """
        [Paginator.DescribeMLModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeMLModels)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["batch_prediction_available"]
    ) -> BatchPredictionAvailableWaiter:
        """
        [Waiter.BatchPredictionAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Waiter.BatchPredictionAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["data_source_available"]
    ) -> DataSourceAvailableWaiter:
        """
        [Waiter.DataSourceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Waiter.DataSourceAvailable)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["evaluation_available"]) -> EvaluationAvailableWaiter:
        """
        [Waiter.EvaluationAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Waiter.EvaluationAvailable)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["ml_model_available"]) -> MLModelAvailableWaiter:
        """
        [Waiter.MLModelAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Waiter.MLModelAvailable)
        """
