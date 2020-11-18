# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
"""
Main interface for machinelearning service client waiters.

Usage::

    ```python
    import boto3

    from mypy_boto3_machinelearning import MachineLearningClient
    from mypy_boto3_machinelearning.waiter import (
        BatchPredictionAvailableWaiter,
        DataSourceAvailableWaiter,
        EvaluationAvailableWaiter,
        MLModelAvailableWaiter,
    )

    client: MachineLearningClient = boto3.client("machinelearning")

    batch_prediction_available_waiter: BatchPredictionAvailableWaiter = client.get_waiter("batch_prediction_available")
    data_source_available_waiter: DataSourceAvailableWaiter = client.get_waiter("data_source_available")
    evaluation_available_waiter: EvaluationAvailableWaiter = client.get_waiter("evaluation_available")
    ml_model_available_waiter: MLModelAvailableWaiter = client.get_waiter("ml_model_available")
    ```
"""
import sys

from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_machinelearning.type_defs import WaiterConfigTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BatchPredictionAvailableWaiter",
    "DataSourceAvailableWaiter",
    "EvaluationAvailableWaiter",
    "MLModelAvailableWaiter",
)


class BatchPredictionAvailableWaiter(Boto3Waiter):
    """
    [Waiter.BatchPredictionAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Waiter.BatchPredictionAvailable)
    """

    def wait(
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
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [BatchPredictionAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Waiter.BatchPredictionAvailable.wait)
        """


class DataSourceAvailableWaiter(Boto3Waiter):
    """
    [Waiter.DataSourceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Waiter.DataSourceAvailable)
    """

    def wait(
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
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [DataSourceAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Waiter.DataSourceAvailable.wait)
        """


class EvaluationAvailableWaiter(Boto3Waiter):
    """
    [Waiter.EvaluationAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Waiter.EvaluationAvailable)
    """

    def wait(
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
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [EvaluationAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Waiter.EvaluationAvailable.wait)
        """


class MLModelAvailableWaiter(Boto3Waiter):
    """
    [Waiter.MLModelAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Waiter.MLModelAvailable)
    """

    def wait(
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
        WaiterConfig: WaiterConfigTypeDef = None,
    ) -> None:
        """
        [MLModelAvailable.wait documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Waiter.MLModelAvailable.wait)
        """
