"""
Type annotations for machinelearning service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/literals.html)

Usage::

    ```python
    from mypy_boto3_machinelearning.literals import AlgorithmType

    data: AlgorithmType = "sgd"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AlgorithmType",
    "BatchPredictionAvailableWaiterName",
    "BatchPredictionFilterVariableType",
    "DataSourceAvailableWaiterName",
    "DataSourceFilterVariableType",
    "DescribeBatchPredictionsPaginatorName",
    "DescribeDataSourcesPaginatorName",
    "DescribeEvaluationsPaginatorName",
    "DescribeMLModelsPaginatorName",
    "DetailsAttributesType",
    "EntityStatusType",
    "EvaluationAvailableWaiterName",
    "EvaluationFilterVariableType",
    "MLModelAvailableWaiterName",
    "MLModelFilterVariableType",
    "MLModelTypeType",
    "RealtimeEndpointStatusType",
    "SortOrderType",
    "TaggableResourceTypeType",
)

AlgorithmType = Literal["sgd"]
BatchPredictionAvailableWaiterName = Literal["batch_prediction_available"]
BatchPredictionFilterVariableType = Literal[
    "CreatedAt",
    "DataSourceId",
    "DataURI",
    "IAMUser",
    "LastUpdatedAt",
    "MLModelId",
    "Name",
    "Status",
]
DataSourceAvailableWaiterName = Literal["data_source_available"]
DataSourceFilterVariableType = Literal[
    "CreatedAt", "DataLocationS3", "IAMUser", "LastUpdatedAt", "Name", "Status"
]
DescribeBatchPredictionsPaginatorName = Literal["describe_batch_predictions"]
DescribeDataSourcesPaginatorName = Literal["describe_data_sources"]
DescribeEvaluationsPaginatorName = Literal["describe_evaluations"]
DescribeMLModelsPaginatorName = Literal["describe_ml_models"]
DetailsAttributesType = Literal["Algorithm", "PredictiveModelType"]
EntityStatusType = Literal["COMPLETED", "DELETED", "FAILED", "INPROGRESS", "PENDING"]
EvaluationAvailableWaiterName = Literal["evaluation_available"]
EvaluationFilterVariableType = Literal[
    "CreatedAt",
    "DataSourceId",
    "DataURI",
    "IAMUser",
    "LastUpdatedAt",
    "MLModelId",
    "Name",
    "Status",
]
MLModelAvailableWaiterName = Literal["ml_model_available"]
MLModelFilterVariableType = Literal[
    "Algorithm",
    "CreatedAt",
    "IAMUser",
    "LastUpdatedAt",
    "MLModelType",
    "Name",
    "RealtimeEndpointStatus",
    "Status",
    "TrainingDataSourceId",
    "TrainingDataURI",
]
MLModelTypeType = Literal["BINARY", "MULTICLASS", "REGRESSION"]
RealtimeEndpointStatusType = Literal["FAILED", "NONE", "READY", "UPDATING"]
SortOrderType = Literal["asc", "dsc"]
TaggableResourceTypeType = Literal["BatchPrediction", "DataSource", "Evaluation", "MLModel"]
