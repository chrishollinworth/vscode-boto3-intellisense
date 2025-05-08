"""
Type annotations for cost-optimization-hub service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cost_optimization_hub.client import CostOptimizationHubClient
    from mypy_boto3_cost_optimization_hub.paginator import (
        ListEnrollmentStatusesPaginator,
        ListRecommendationSummariesPaginator,
        ListRecommendationsPaginator,
    )

    session = Session()
    client: CostOptimizationHubClient = session.client("cost-optimization-hub")

    list_enrollment_statuses_paginator: ListEnrollmentStatusesPaginator = client.get_paginator("list_enrollment_statuses")
    list_recommendation_summaries_paginator: ListRecommendationSummariesPaginator = client.get_paginator("list_recommendation_summaries")
    list_recommendations_paginator: ListRecommendationsPaginator = client.get_paginator("list_recommendations")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListEnrollmentStatusesRequestPaginateTypeDef,
    ListEnrollmentStatusesResponseTypeDef,
    ListRecommendationsRequestPaginateTypeDef,
    ListRecommendationsResponseTypeDef,
    ListRecommendationSummariesRequestPaginateTypeDef,
    ListRecommendationSummariesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListEnrollmentStatusesPaginator",
    "ListRecommendationSummariesPaginator",
    "ListRecommendationsPaginator",
)

if TYPE_CHECKING:
    _ListEnrollmentStatusesPaginatorBase = Paginator[ListEnrollmentStatusesResponseTypeDef]
else:
    _ListEnrollmentStatusesPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnrollmentStatusesPaginator(_ListEnrollmentStatusesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/paginator/ListEnrollmentStatuses.html#CostOptimizationHub.Paginator.ListEnrollmentStatuses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators/#listenrollmentstatusespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnrollmentStatusesRequestPaginateTypeDef]
    ) -> PageIterator[ListEnrollmentStatusesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/paginator/ListEnrollmentStatuses.html#CostOptimizationHub.Paginator.ListEnrollmentStatuses.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators/#listenrollmentstatusespaginator)
        """

if TYPE_CHECKING:
    _ListRecommendationSummariesPaginatorBase = Paginator[
        ListRecommendationSummariesResponseTypeDef
    ]
else:
    _ListRecommendationSummariesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecommendationSummariesPaginator(_ListRecommendationSummariesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/paginator/ListRecommendationSummaries.html#CostOptimizationHub.Paginator.ListRecommendationSummaries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators/#listrecommendationsummariespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecommendationSummariesRequestPaginateTypeDef]
    ) -> PageIterator[ListRecommendationSummariesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/paginator/ListRecommendationSummaries.html#CostOptimizationHub.Paginator.ListRecommendationSummaries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators/#listrecommendationsummariespaginator)
        """

if TYPE_CHECKING:
    _ListRecommendationsPaginatorBase = Paginator[ListRecommendationsResponseTypeDef]
else:
    _ListRecommendationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecommendationsPaginator(_ListRecommendationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/paginator/ListRecommendations.html#CostOptimizationHub.Paginator.ListRecommendations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators/#listrecommendationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecommendationsRequestPaginateTypeDef]
    ) -> PageIterator[ListRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cost-optimization-hub/paginator/ListRecommendations.html#CostOptimizationHub.Paginator.ListRecommendations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators/#listrecommendationspaginator)
        """
