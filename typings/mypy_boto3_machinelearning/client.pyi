"""
Type annotations for machinelearning service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_machinelearning.client import MachineLearningClient

    session = Session()
    client: MachineLearningClient = session.client("machinelearning")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeBatchPredictionsPaginator,
    DescribeDataSourcesPaginator,
    DescribeEvaluationsPaginator,
    DescribeMLModelsPaginator,
)
from .type_defs import (
    AddTagsInputTypeDef,
    AddTagsOutputTypeDef,
    CreateBatchPredictionInputTypeDef,
    CreateBatchPredictionOutputTypeDef,
    CreateDataSourceFromRDSInputTypeDef,
    CreateDataSourceFromRDSOutputTypeDef,
    CreateDataSourceFromRedshiftInputTypeDef,
    CreateDataSourceFromRedshiftOutputTypeDef,
    CreateDataSourceFromS3InputTypeDef,
    CreateDataSourceFromS3OutputTypeDef,
    CreateEvaluationInputTypeDef,
    CreateEvaluationOutputTypeDef,
    CreateMLModelInputTypeDef,
    CreateMLModelOutputTypeDef,
    CreateRealtimeEndpointInputTypeDef,
    CreateRealtimeEndpointOutputTypeDef,
    DeleteBatchPredictionInputTypeDef,
    DeleteBatchPredictionOutputTypeDef,
    DeleteDataSourceInputTypeDef,
    DeleteDataSourceOutputTypeDef,
    DeleteEvaluationInputTypeDef,
    DeleteEvaluationOutputTypeDef,
    DeleteMLModelInputTypeDef,
    DeleteMLModelOutputTypeDef,
    DeleteRealtimeEndpointInputTypeDef,
    DeleteRealtimeEndpointOutputTypeDef,
    DeleteTagsInputTypeDef,
    DeleteTagsOutputTypeDef,
    DescribeBatchPredictionsInputTypeDef,
    DescribeBatchPredictionsOutputTypeDef,
    DescribeDataSourcesInputTypeDef,
    DescribeDataSourcesOutputTypeDef,
    DescribeEvaluationsInputTypeDef,
    DescribeEvaluationsOutputTypeDef,
    DescribeMLModelsInputTypeDef,
    DescribeMLModelsOutputTypeDef,
    DescribeTagsInputTypeDef,
    DescribeTagsOutputTypeDef,
    GetBatchPredictionInputTypeDef,
    GetBatchPredictionOutputTypeDef,
    GetDataSourceInputTypeDef,
    GetDataSourceOutputTypeDef,
    GetEvaluationInputTypeDef,
    GetEvaluationOutputTypeDef,
    GetMLModelInputTypeDef,
    GetMLModelOutputTypeDef,
    PredictInputTypeDef,
    PredictOutputTypeDef,
    UpdateBatchPredictionInputTypeDef,
    UpdateBatchPredictionOutputTypeDef,
    UpdateDataSourceInputTypeDef,
    UpdateDataSourceOutputTypeDef,
    UpdateEvaluationInputTypeDef,
    UpdateEvaluationOutputTypeDef,
    UpdateMLModelInputTypeDef,
    UpdateMLModelOutputTypeDef,
)
from .waiter import (
    BatchPredictionAvailableWaiter,
    DataSourceAvailableWaiter,
    EvaluationAvailableWaiter,
    MLModelAvailableWaiter,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("MachineLearningClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MachineLearningClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning.html#MachineLearning.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#generate_presigned_url)
        """

    def add_tags(self, **kwargs: Unpack[AddTagsInputTypeDef]) -> AddTagsOutputTypeDef:
        """
        Adds one or more tags to an object, up to a limit of 10.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/add_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#add_tags)
        """

    def create_batch_prediction(
        self, **kwargs: Unpack[CreateBatchPredictionInputTypeDef]
    ) -> CreateBatchPredictionOutputTypeDef:
        """
        Generates predictions for a group of observations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/create_batch_prediction.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#create_batch_prediction)
        """

    def create_data_source_from_rds(
        self, **kwargs: Unpack[CreateDataSourceFromRDSInputTypeDef]
    ) -> CreateDataSourceFromRDSOutputTypeDef:
        """
        Creates a <code>DataSource</code> object from an <a
        href="http://aws.amazon.com/rds/"> Amazon Relational Database Service</a>
        (Amazon RDS).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/create_data_source_from_rds.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#create_data_source_from_rds)
        """

    def create_data_source_from_redshift(
        self, **kwargs: Unpack[CreateDataSourceFromRedshiftInputTypeDef]
    ) -> CreateDataSourceFromRedshiftOutputTypeDef:
        """
        Creates a <code>DataSource</code> from a database hosted on an Amazon Redshift
        cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/create_data_source_from_redshift.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#create_data_source_from_redshift)
        """

    def create_data_source_from_s3(
        self, **kwargs: Unpack[CreateDataSourceFromS3InputTypeDef]
    ) -> CreateDataSourceFromS3OutputTypeDef:
        """
        Creates a <code>DataSource</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/create_data_source_from_s3.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#create_data_source_from_s3)
        """

    def create_evaluation(
        self, **kwargs: Unpack[CreateEvaluationInputTypeDef]
    ) -> CreateEvaluationOutputTypeDef:
        """
        Creates a new <code>Evaluation</code> of an <code>MLModel</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/create_evaluation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#create_evaluation)
        """

    def create_ml_model(
        self, **kwargs: Unpack[CreateMLModelInputTypeDef]
    ) -> CreateMLModelOutputTypeDef:
        """
        Creates a new <code>MLModel</code> using the <code>DataSource</code> and the
        recipe as information sources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/create_ml_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#create_ml_model)
        """

    def create_realtime_endpoint(
        self, **kwargs: Unpack[CreateRealtimeEndpointInputTypeDef]
    ) -> CreateRealtimeEndpointOutputTypeDef:
        """
        Creates a real-time endpoint for the <code>MLModel</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/create_realtime_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#create_realtime_endpoint)
        """

    def delete_batch_prediction(
        self, **kwargs: Unpack[DeleteBatchPredictionInputTypeDef]
    ) -> DeleteBatchPredictionOutputTypeDef:
        """
        Assigns the DELETED status to a <code>BatchPrediction</code>, rendering it
        unusable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/delete_batch_prediction.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#delete_batch_prediction)
        """

    def delete_data_source(
        self, **kwargs: Unpack[DeleteDataSourceInputTypeDef]
    ) -> DeleteDataSourceOutputTypeDef:
        """
        Assigns the DELETED status to a <code>DataSource</code>, rendering it unusable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/delete_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#delete_data_source)
        """

    def delete_evaluation(
        self, **kwargs: Unpack[DeleteEvaluationInputTypeDef]
    ) -> DeleteEvaluationOutputTypeDef:
        """
        Assigns the <code>DELETED</code> status to an <code>Evaluation</code>,
        rendering it unusable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/delete_evaluation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#delete_evaluation)
        """

    def delete_ml_model(
        self, **kwargs: Unpack[DeleteMLModelInputTypeDef]
    ) -> DeleteMLModelOutputTypeDef:
        """
        Assigns the <code>DELETED</code> status to an <code>MLModel</code>, rendering
        it unusable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/delete_ml_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#delete_ml_model)
        """

    def delete_realtime_endpoint(
        self, **kwargs: Unpack[DeleteRealtimeEndpointInputTypeDef]
    ) -> DeleteRealtimeEndpointOutputTypeDef:
        """
        Deletes a real time endpoint of an <code>MLModel</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/delete_realtime_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#delete_realtime_endpoint)
        """

    def delete_tags(self, **kwargs: Unpack[DeleteTagsInputTypeDef]) -> DeleteTagsOutputTypeDef:
        """
        Deletes the specified tags associated with an ML object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/delete_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#delete_tags)
        """

    def describe_batch_predictions(
        self, **kwargs: Unpack[DescribeBatchPredictionsInputTypeDef]
    ) -> DescribeBatchPredictionsOutputTypeDef:
        """
        Returns a list of <code>BatchPrediction</code> operations that match the search
        criteria in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/describe_batch_predictions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#describe_batch_predictions)
        """

    def describe_data_sources(
        self, **kwargs: Unpack[DescribeDataSourcesInputTypeDef]
    ) -> DescribeDataSourcesOutputTypeDef:
        """
        Returns a list of <code>DataSource</code> that match the search criteria in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/describe_data_sources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#describe_data_sources)
        """

    def describe_evaluations(
        self, **kwargs: Unpack[DescribeEvaluationsInputTypeDef]
    ) -> DescribeEvaluationsOutputTypeDef:
        """
        Returns a list of <code>DescribeEvaluations</code> that match the search
        criteria in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/describe_evaluations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#describe_evaluations)
        """

    def describe_ml_models(
        self, **kwargs: Unpack[DescribeMLModelsInputTypeDef]
    ) -> DescribeMLModelsOutputTypeDef:
        """
        Returns a list of <code>MLModel</code> that match the search criteria in the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/describe_ml_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#describe_ml_models)
        """

    def describe_tags(
        self, **kwargs: Unpack[DescribeTagsInputTypeDef]
    ) -> DescribeTagsOutputTypeDef:
        """
        Describes one or more of the tags for your Amazon ML object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/describe_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#describe_tags)
        """

    def get_batch_prediction(
        self, **kwargs: Unpack[GetBatchPredictionInputTypeDef]
    ) -> GetBatchPredictionOutputTypeDef:
        """
        Returns a <code>BatchPrediction</code> that includes detailed metadata, status,
        and data file information for a <code>Batch Prediction</code> request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/get_batch_prediction.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_batch_prediction)
        """

    def get_data_source(
        self, **kwargs: Unpack[GetDataSourceInputTypeDef]
    ) -> GetDataSourceOutputTypeDef:
        """
        Returns a <code>DataSource</code> that includes metadata and data file
        information, as well as the current status of the <code>DataSource</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/get_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_data_source)
        """

    def get_evaluation(
        self, **kwargs: Unpack[GetEvaluationInputTypeDef]
    ) -> GetEvaluationOutputTypeDef:
        """
        Returns an <code>Evaluation</code> that includes metadata as well as the
        current status of the <code>Evaluation</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/get_evaluation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_evaluation)
        """

    def get_ml_model(self, **kwargs: Unpack[GetMLModelInputTypeDef]) -> GetMLModelOutputTypeDef:
        """
        Returns an <code>MLModel</code> that includes detailed metadata, data source
        information, and the current status of the <code>MLModel</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/get_ml_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_ml_model)
        """

    def predict(self, **kwargs: Unpack[PredictInputTypeDef]) -> PredictOutputTypeDef:
        """
        Generates a prediction for the observation using the specified <code>ML
        Model</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/predict.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#predict)
        """

    def update_batch_prediction(
        self, **kwargs: Unpack[UpdateBatchPredictionInputTypeDef]
    ) -> UpdateBatchPredictionOutputTypeDef:
        """
        Updates the <code>BatchPredictionName</code> of a <code>BatchPrediction</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/update_batch_prediction.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#update_batch_prediction)
        """

    def update_data_source(
        self, **kwargs: Unpack[UpdateDataSourceInputTypeDef]
    ) -> UpdateDataSourceOutputTypeDef:
        """
        Updates the <code>DataSourceName</code> of a <code>DataSource</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/update_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#update_data_source)
        """

    def update_evaluation(
        self, **kwargs: Unpack[UpdateEvaluationInputTypeDef]
    ) -> UpdateEvaluationOutputTypeDef:
        """
        Updates the <code>EvaluationName</code> of an <code>Evaluation</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/update_evaluation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#update_evaluation)
        """

    def update_ml_model(
        self, **kwargs: Unpack[UpdateMLModelInputTypeDef]
    ) -> UpdateMLModelOutputTypeDef:
        """
        Updates the <code>MLModelName</code> and the <code>ScoreThreshold</code> of an
        <code>MLModel</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/update_ml_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#update_ml_model)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_batch_predictions"]
    ) -> DescribeBatchPredictionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_data_sources"]
    ) -> DescribeDataSourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_evaluations"]
    ) -> DescribeEvaluationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_ml_models"]
    ) -> DescribeMLModelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["batch_prediction_available"]
    ) -> BatchPredictionAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["data_source_available"]
    ) -> DataSourceAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["evaluation_available"]
    ) -> EvaluationAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["ml_model_available"]
    ) -> MLModelAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/client/#get_waiter)
        """
