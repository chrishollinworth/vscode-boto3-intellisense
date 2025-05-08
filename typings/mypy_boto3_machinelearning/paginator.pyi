"""
Type annotations for machinelearning service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_machinelearning.client import MachineLearningClient
    from mypy_boto3_machinelearning.paginator import (
        DescribeBatchPredictionsPaginator,
        DescribeDataSourcesPaginator,
        DescribeEvaluationsPaginator,
        DescribeMLModelsPaginator,
    )

    session = Session()
    client: MachineLearningClient = session.client("machinelearning")

    describe_batch_predictions_paginator: DescribeBatchPredictionsPaginator = client.get_paginator("describe_batch_predictions")
    describe_data_sources_paginator: DescribeDataSourcesPaginator = client.get_paginator("describe_data_sources")
    describe_evaluations_paginator: DescribeEvaluationsPaginator = client.get_paginator("describe_evaluations")
    describe_ml_models_paginator: DescribeMLModelsPaginator = client.get_paginator("describe_ml_models")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeBatchPredictionsInputPaginateTypeDef,
    DescribeBatchPredictionsOutputTypeDef,
    DescribeDataSourcesInputPaginateTypeDef,
    DescribeDataSourcesOutputTypeDef,
    DescribeEvaluationsInputPaginateTypeDef,
    DescribeEvaluationsOutputTypeDef,
    DescribeMLModelsInputPaginateTypeDef,
    DescribeMLModelsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeBatchPredictionsPaginator",
    "DescribeDataSourcesPaginator",
    "DescribeEvaluationsPaginator",
    "DescribeMLModelsPaginator",
)

if TYPE_CHECKING:
    _DescribeBatchPredictionsPaginatorBase = Paginator[DescribeBatchPredictionsOutputTypeDef]
else:
    _DescribeBatchPredictionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeBatchPredictionsPaginator(_DescribeBatchPredictionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/paginator/DescribeBatchPredictions.html#MachineLearning.Paginator.DescribeBatchPredictions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators/#describebatchpredictionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBatchPredictionsInputPaginateTypeDef]
    ) -> PageIterator[DescribeBatchPredictionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/paginator/DescribeBatchPredictions.html#MachineLearning.Paginator.DescribeBatchPredictions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators/#describebatchpredictionspaginator)
        """

if TYPE_CHECKING:
    _DescribeDataSourcesPaginatorBase = Paginator[DescribeDataSourcesOutputTypeDef]
else:
    _DescribeDataSourcesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDataSourcesPaginator(_DescribeDataSourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/paginator/DescribeDataSources.html#MachineLearning.Paginator.DescribeDataSources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators/#describedatasourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDataSourcesInputPaginateTypeDef]
    ) -> PageIterator[DescribeDataSourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/paginator/DescribeDataSources.html#MachineLearning.Paginator.DescribeDataSources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators/#describedatasourcespaginator)
        """

if TYPE_CHECKING:
    _DescribeEvaluationsPaginatorBase = Paginator[DescribeEvaluationsOutputTypeDef]
else:
    _DescribeEvaluationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEvaluationsPaginator(_DescribeEvaluationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/paginator/DescribeEvaluations.html#MachineLearning.Paginator.DescribeEvaluations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators/#describeevaluationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEvaluationsInputPaginateTypeDef]
    ) -> PageIterator[DescribeEvaluationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/paginator/DescribeEvaluations.html#MachineLearning.Paginator.DescribeEvaluations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators/#describeevaluationspaginator)
        """

if TYPE_CHECKING:
    _DescribeMLModelsPaginatorBase = Paginator[DescribeMLModelsOutputTypeDef]
else:
    _DescribeMLModelsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMLModelsPaginator(_DescribeMLModelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/paginator/DescribeMLModels.html#MachineLearning.Paginator.DescribeMLModels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators/#describemlmodelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMLModelsInputPaginateTypeDef]
    ) -> PageIterator[DescribeMLModelsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/machinelearning/paginator/DescribeMLModels.html#MachineLearning.Paginator.DescribeMLModels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/paginators/#describemlmodelspaginator)
        """
