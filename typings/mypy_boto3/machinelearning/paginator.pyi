"""
Type annotations for machinelearning service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_machinelearning import MachineLearningClient
    from mypy_boto3_machinelearning.paginator import (
        DescribeBatchPredictionsPaginator,
        DescribeDataSourcesPaginator,
        DescribeEvaluationsPaginator,
        DescribeMLModelsPaginator,
    )

    client: MachineLearningClient = boto3.client("machinelearning")

    describe_batch_predictions_paginator: DescribeBatchPredictionsPaginator = client.get_paginator("describe_batch_predictions")
    describe_data_sources_paginator: DescribeDataSourcesPaginator = client.get_paginator("describe_data_sources")
    describe_evaluations_paginator: DescribeEvaluationsPaginator = client.get_paginator("describe_evaluations")
    describe_ml_models_paginator: DescribeMLModelsPaginator = client.get_paginator("describe_ml_models")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    BatchPredictionFilterVariableType,
    DataSourceFilterVariableType,
    EvaluationFilterVariableType,
    MLModelFilterVariableType,
    SortOrderType,
)
from .type_defs import (
    DescribeBatchPredictionsOutputTypeDef,
    DescribeDataSourcesOutputTypeDef,
    DescribeEvaluationsOutputTypeDef,
    DescribeMLModelsOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeBatchPredictionsPaginator",
    "DescribeDataSourcesPaginator",
    "DescribeEvaluationsPaginator",
    "DescribeMLModelsPaginator",
)

class DescribeBatchPredictionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeBatchPredictions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describebatchpredictionspaginator)
    """

    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeBatchPredictionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeBatchPredictions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describebatchpredictionspaginator)
        """

class DescribeDataSourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeDataSources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describedatasourcespaginator)
    """

    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDataSourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeDataSources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describedatasourcespaginator)
        """

class DescribeEvaluationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeEvaluations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describeevaluationspaginator)
    """

    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEvaluationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeEvaluations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describeevaluationspaginator)
        """

class DescribeMLModelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeMLModels)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describemlmodelspaginator)
    """

    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMLModelsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeMLModels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators.html#describemlmodelspaginator)
        """
