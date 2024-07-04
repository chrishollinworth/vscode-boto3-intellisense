"""
Type annotations for machinelearning service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html)

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

from botocore.waiter import Waiter as Boto3Waiter

from .literals import (
    BatchPredictionFilterVariableType,
    DataSourceFilterVariableType,
    EvaluationFilterVariableType,
    MLModelFilterVariableType,
    SortOrderType,
)
from .type_defs import WaiterConfigTypeDef

__all__ = (
    "BatchPredictionAvailableWaiter",
    "DataSourceAvailableWaiter",
    "EvaluationAvailableWaiter",
    "MLModelAvailableWaiter",
)

class BatchPredictionAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/machinelearning.html#MachineLearning.Waiter.BatchPredictionAvailable)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#batchpredictionavailablewaiter)
    """

    def wait(
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
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/machinelearning.html#MachineLearning.Waiter.BatchPredictionAvailable.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#batchpredictionavailablewaiter)
        """

class DataSourceAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/machinelearning.html#MachineLearning.Waiter.DataSourceAvailable)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#datasourceavailablewaiter)
    """

    def wait(
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
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/machinelearning.html#MachineLearning.Waiter.DataSourceAvailable.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#datasourceavailablewaiter)
        """

class EvaluationAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/machinelearning.html#MachineLearning.Waiter.EvaluationAvailable)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#evaluationavailablewaiter)
    """

    def wait(
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
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/machinelearning.html#MachineLearning.Waiter.EvaluationAvailable.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#evaluationavailablewaiter)
        """

class MLModelAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/machinelearning.html#MachineLearning.Waiter.MLModelAvailable)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#mlmodelavailablewaiter)
    """

    def wait(
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
        Limit: int = None,
        WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/machinelearning.html#MachineLearning.Waiter.MLModelAvailable.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters.html#mlmodelavailablewaiter)
        """
