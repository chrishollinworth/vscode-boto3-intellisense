"""
Type annotations for machinelearning service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_machinelearning import MachineLearningClient

    client: MachineLearningClient = boto3.client("machinelearning")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    BatchPredictionFilterVariableType,
    DataSourceFilterVariableType,
    EvaluationFilterVariableType,
    MLModelFilterVariableType,
    MLModelTypeType,
    SortOrderType,
    TaggableResourceTypeType,
)
from .paginator import (
    DescribeBatchPredictionsPaginator,
    DescribeDataSourcesPaginator,
    DescribeEvaluationsPaginator,
    DescribeMLModelsPaginator,
)
from .type_defs import (
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
from .waiter import (
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

class MachineLearningClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MachineLearningClient exceptions.
        """
    def add_tags(
        self, *, Tags: List["TagTypeDef"], ResourceId: str, ResourceType: TaggableResourceTypeType
    ) -> AddTagsOutputTypeDef:
        """
        Adds one or more tags to an object, up to a limit of 10.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.add_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#add_tags)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#close)
        """
    def create_batch_prediction(
        self,
        *,
        BatchPredictionId: str,
        MLModelId: str,
        BatchPredictionDataSourceId: str,
        OutputUri: str,
        BatchPredictionName: str = None
    ) -> CreateBatchPredictionOutputTypeDef:
        """
        Generates predictions for a group of observations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.create_batch_prediction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#create_batch_prediction)
        """
    def create_data_source_from_rds(
        self,
        *,
        DataSourceId: str,
        RDSData: "RDSDataSpecTypeDef",
        RoleARN: str,
        DataSourceName: str = None,
        ComputeStatistics: bool = None
    ) -> CreateDataSourceFromRDSOutputTypeDef:
        """
        Creates a `DataSource` object from an `Amazon Relational Database Service
        <http://aws.amazon.com/rds/>`__ (Amazon RDS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.create_data_source_from_rds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#create_data_source_from_rds)
        """
    def create_data_source_from_redshift(
        self,
        *,
        DataSourceId: str,
        DataSpec: "RedshiftDataSpecTypeDef",
        RoleARN: str,
        DataSourceName: str = None,
        ComputeStatistics: bool = None
    ) -> CreateDataSourceFromRedshiftOutputTypeDef:
        """
        Creates a `DataSource` from a database hosted on an Amazon Redshift cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.create_data_source_from_redshift)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#create_data_source_from_redshift)
        """
    def create_data_source_from_s3(
        self,
        *,
        DataSourceId: str,
        DataSpec: "S3DataSpecTypeDef",
        DataSourceName: str = None,
        ComputeStatistics: bool = None
    ) -> CreateDataSourceFromS3OutputTypeDef:
        """
        Creates a `DataSource` object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.create_data_source_from_s3)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#create_data_source_from_s3)
        """
    def create_evaluation(
        self,
        *,
        EvaluationId: str,
        MLModelId: str,
        EvaluationDataSourceId: str,
        EvaluationName: str = None
    ) -> CreateEvaluationOutputTypeDef:
        """
        Creates a new `Evaluation` of an `MLModel`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.create_evaluation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#create_evaluation)
        """
    def create_ml_model(
        self,
        *,
        MLModelId: str,
        MLModelType: MLModelTypeType,
        TrainingDataSourceId: str,
        MLModelName: str = None,
        Parameters: Dict[str, str] = None,
        Recipe: str = None,
        RecipeUri: str = None
    ) -> CreateMLModelOutputTypeDef:
        """
        Creates a new `MLModel` using the `DataSource` and the recipe as information
        sources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.create_ml_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#create_ml_model)
        """
    def create_realtime_endpoint(self, *, MLModelId: str) -> CreateRealtimeEndpointOutputTypeDef:
        """
        Creates a real-time endpoint for the `MLModel`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.create_realtime_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#create_realtime_endpoint)
        """
    def delete_batch_prediction(
        self, *, BatchPredictionId: str
    ) -> DeleteBatchPredictionOutputTypeDef:
        """
        Assigns the DELETED status to a `BatchPrediction` , rendering it unusable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.delete_batch_prediction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#delete_batch_prediction)
        """
    def delete_data_source(self, *, DataSourceId: str) -> DeleteDataSourceOutputTypeDef:
        """
        Assigns the DELETED status to a `DataSource` , rendering it unusable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.delete_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#delete_data_source)
        """
    def delete_evaluation(self, *, EvaluationId: str) -> DeleteEvaluationOutputTypeDef:
        """
        Assigns the `DELETED` status to an `Evaluation` , rendering it unusable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.delete_evaluation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#delete_evaluation)
        """
    def delete_ml_model(self, *, MLModelId: str) -> DeleteMLModelOutputTypeDef:
        """
        Assigns the `DELETED` status to an `MLModel` , rendering it unusable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.delete_ml_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#delete_ml_model)
        """
    def delete_realtime_endpoint(self, *, MLModelId: str) -> DeleteRealtimeEndpointOutputTypeDef:
        """
        Deletes a real time endpoint of an `MLModel` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.delete_realtime_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#delete_realtime_endpoint)
        """
    def delete_tags(
        self, *, TagKeys: List[str], ResourceId: str, ResourceType: TaggableResourceTypeType
    ) -> DeleteTagsOutputTypeDef:
        """
        Deletes the specified tags associated with an ML object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#delete_tags)
        """
    def describe_batch_predictions(
        self,
        *,
        FilterVariable: BatchPredictionFilterVariableType = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        Limit: int = None
    ) -> DescribeBatchPredictionsOutputTypeDef:
        """
        Returns a list of `BatchPrediction` operations that match the search criteria in
        the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.describe_batch_predictions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#describe_batch_predictions)
        """
    def describe_data_sources(
        self,
        *,
        FilterVariable: DataSourceFilterVariableType = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        Limit: int = None
    ) -> DescribeDataSourcesOutputTypeDef:
        """
        Returns a list of `DataSource` that match the search criteria in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.describe_data_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#describe_data_sources)
        """
    def describe_evaluations(
        self,
        *,
        FilterVariable: EvaluationFilterVariableType = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        Limit: int = None
    ) -> DescribeEvaluationsOutputTypeDef:
        """
        Returns a list of `DescribeEvaluations` that match the search criteria in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.describe_evaluations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#describe_evaluations)
        """
    def describe_ml_models(
        self,
        *,
        FilterVariable: MLModelFilterVariableType = None,
        EQ: str = None,
        GT: str = None,
        LT: str = None,
        GE: str = None,
        LE: str = None,
        NE: str = None,
        Prefix: str = None,
        SortOrder: SortOrderType = None,
        NextToken: str = None,
        Limit: int = None
    ) -> DescribeMLModelsOutputTypeDef:
        """
        Returns a list of `MLModel` that match the search criteria in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.describe_ml_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#describe_ml_models)
        """
    def describe_tags(
        self, *, ResourceId: str, ResourceType: TaggableResourceTypeType
    ) -> DescribeTagsOutputTypeDef:
        """
        Describes one or more of the tags for your Amazon ML object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.describe_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#describe_tags)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#generate_presigned_url)
        """
    def get_batch_prediction(self, *, BatchPredictionId: str) -> GetBatchPredictionOutputTypeDef:
        """
        Returns a `BatchPrediction` that includes detailed metadata, status, and data
        file information for a `Batch Prediction` request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.get_batch_prediction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#get_batch_prediction)
        """
    def get_data_source(
        self, *, DataSourceId: str, Verbose: bool = None
    ) -> GetDataSourceOutputTypeDef:
        """
        Returns a `DataSource` that includes metadata and data file information, as well
        as the current status of the `DataSource` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.get_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#get_data_source)
        """
    def get_evaluation(self, *, EvaluationId: str) -> GetEvaluationOutputTypeDef:
        """
        Returns an `Evaluation` that includes metadata as well as the current status of
        the `Evaluation` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.get_evaluation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#get_evaluation)
        """
    def get_ml_model(self, *, MLModelId: str, Verbose: bool = None) -> GetMLModelOutputTypeDef:
        """
        Returns an `MLModel` that includes detailed metadata, data source information,
        and the current status of the `MLModel` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.get_ml_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#get_ml_model)
        """
    def predict(
        self, *, MLModelId: str, Record: Dict[str, str], PredictEndpoint: str
    ) -> PredictOutputTypeDef:
        """
        Generates a prediction for the observation using the specified `ML Model` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.predict)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#predict)
        """
    def update_batch_prediction(
        self, *, BatchPredictionId: str, BatchPredictionName: str
    ) -> UpdateBatchPredictionOutputTypeDef:
        """
        Updates the `BatchPredictionName` of a `BatchPrediction` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.update_batch_prediction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#update_batch_prediction)
        """
    def update_data_source(
        self, *, DataSourceId: str, DataSourceName: str
    ) -> UpdateDataSourceOutputTypeDef:
        """
        Updates the `DataSourceName` of a `DataSource` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.update_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#update_data_source)
        """
    def update_evaluation(
        self, *, EvaluationId: str, EvaluationName: str
    ) -> UpdateEvaluationOutputTypeDef:
        """
        Updates the `EvaluationName` of an `Evaluation` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.update_evaluation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#update_evaluation)
        """
    def update_ml_model(
        self, *, MLModelId: str, MLModelName: str = None, ScoreThreshold: float = None
    ) -> UpdateMLModelOutputTypeDef:
        """
        Updates the `MLModelName` and the `ScoreThreshold` of an `MLModel` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Client.update_ml_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client.html#update_ml_model)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_batch_predictions"]
    ) -> DescribeBatchPredictionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeBatchPredictions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describebatchpredictionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_data_sources"]
    ) -> DescribeDataSourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeDataSources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describedatasourcespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_evaluations"]
    ) -> DescribeEvaluationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeEvaluations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describeevaluationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ml_models"]
    ) -> DescribeMLModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeMLModels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describemlmodelspaginator)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["batch_prediction_available"]
    ) -> BatchPredictionAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Waiter.BatchPredictionAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#batchpredictionavailablewaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["data_source_available"]
    ) -> DataSourceAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Waiter.DataSourceAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#datasourceavailablewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["evaluation_available"]) -> EvaluationAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Waiter.EvaluationAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#evaluationavailablewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["ml_model_available"]) -> MLModelAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/machinelearning.html#MachineLearning.Waiter.MLModelAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#mlmodelavailablewaiter)
        """
