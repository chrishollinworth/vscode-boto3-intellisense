"""
Type annotations for machinelearning service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_machinelearning.client import MachineLearningClient
    from mypy_boto3_machinelearning.waiter import (
        BatchPredictionAvailableWaiter,
        DataSourceAvailableWaiter,
        EvaluationAvailableWaiter,
        MLModelAvailableWaiter,
    )

    session = Session()
    client: MachineLearningClient = session.client("machinelearning")

    batch_prediction_available_waiter: BatchPredictionAvailableWaiter = client.get_waiter("batch_prediction_available")
    data_source_available_waiter: DataSourceAvailableWaiter = client.get_waiter("data_source_available")
    evaluation_available_waiter: EvaluationAvailableWaiter = client.get_waiter("evaluation_available")
    ml_model_available_waiter: MLModelAvailableWaiter = client.get_waiter("ml_model_available")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    DescribeBatchPredictionsInputWaitTypeDef,
    DescribeDataSourcesInputWaitTypeDef,
    DescribeEvaluationsInputWaitTypeDef,
    DescribeMLModelsInputWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "BatchPredictionAvailableWaiter",
    "DataSourceAvailableWaiter",
    "EvaluationAvailableWaiter",
    "MLModelAvailableWaiter",
)

class BatchPredictionAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/waiter/BatchPredictionAvailable.html#MachineLearning.Waiter.BatchPredictionAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters/#batchpredictionavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBatchPredictionsInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/waiter/BatchPredictionAvailable.html#MachineLearning.Waiter.BatchPredictionAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters/#batchpredictionavailablewaiter)
        """

class DataSourceAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/waiter/DataSourceAvailable.html#MachineLearning.Waiter.DataSourceAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters/#datasourceavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDataSourcesInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/waiter/DataSourceAvailable.html#MachineLearning.Waiter.DataSourceAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters/#datasourceavailablewaiter)
        """

class EvaluationAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/waiter/EvaluationAvailable.html#MachineLearning.Waiter.EvaluationAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters/#evaluationavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEvaluationsInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/waiter/EvaluationAvailable.html#MachineLearning.Waiter.EvaluationAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters/#evaluationavailablewaiter)
        """

class MLModelAvailableWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/waiter/MLModelAvailable.html#MachineLearning.Waiter.MLModelAvailable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters/#mlmodelavailablewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMLModelsInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/waiter/MLModelAvailable.html#MachineLearning.Waiter.MLModelAvailable.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/waiters/#mlmodelavailablewaiter)
        """
