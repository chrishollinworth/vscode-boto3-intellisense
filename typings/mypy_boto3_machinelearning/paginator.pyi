# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for machinelearning service client paginators.

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
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_machinelearning.type_defs import (
    DescribeBatchPredictionsOutputTypeDef,
    DescribeDataSourcesOutputTypeDef,
    DescribeEvaluationsOutputTypeDef,
    DescribeMLModelsOutputTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeBatchPredictionsPaginator",
    "DescribeDataSourcesPaginator",
    "DescribeEvaluationsPaginator",
    "DescribeMLModelsPaginator",
)


class DescribeBatchPredictionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBatchPredictions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeBatchPredictions)
    """

    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeBatchPredictionsOutputTypeDef]:
        """
        [DescribeBatchPredictions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeBatchPredictions.paginate)
        """


class DescribeDataSourcesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDataSources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeDataSources)
    """

    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeDataSourcesOutputTypeDef]:
        """
        [DescribeDataSources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeDataSources.paginate)
        """


class DescribeEvaluationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvaluations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeEvaluations)
    """

    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeEvaluationsOutputTypeDef]:
        """
        [DescribeEvaluations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeEvaluations.paginate)
        """


class DescribeMLModelsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMLModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeMLModels)
    """

    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeMLModelsOutputTypeDef]:
        """
        [DescribeMLModels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/machinelearning.html#MachineLearning.Paginator.DescribeMLModels.paginate)
        """
