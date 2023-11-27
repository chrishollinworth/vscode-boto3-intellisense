"""
Type annotations for cost-optimization-hub service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_cost_optimization_hub import CostOptimizationHubClient
    from mypy_boto3_cost_optimization_hub.paginator import (
        ListEnrollmentStatusesPaginator,
        ListRecommendationSummariesPaginator,
        ListRecommendationsPaginator,
    )

    client: CostOptimizationHubClient = boto3.client("cost-optimization-hub")

    list_enrollment_statuses_paginator: ListEnrollmentStatusesPaginator = client.get_paginator("list_enrollment_statuses")
    list_recommendation_summaries_paginator: ListRecommendationSummariesPaginator = client.get_paginator("list_recommendation_summaries")
    list_recommendations_paginator: ListRecommendationsPaginator = client.get_paginator("list_recommendations")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    FilterTypeDef,
    ListEnrollmentStatusesResponseTypeDef,
    ListRecommendationsResponseTypeDef,
    ListRecommendationSummariesResponseTypeDef,
    OrderByTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListEnrollmentStatusesPaginator",
    "ListRecommendationSummariesPaginator",
    "ListRecommendationsPaginator",
)

class ListEnrollmentStatusesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cost-optimization-hub.html#CostOptimizationHub.Paginator.ListEnrollmentStatuses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators.html#listenrollmentstatusespaginator)
    """

    def paginate(
        self,
        *,
        accountId: str = None,
        includeOrganizationInfo: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnrollmentStatusesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cost-optimization-hub.html#CostOptimizationHub.Paginator.ListEnrollmentStatuses.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators.html#listenrollmentstatusespaginator)
        """

class ListRecommendationSummariesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cost-optimization-hub.html#CostOptimizationHub.Paginator.ListRecommendationSummaries)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators.html#listrecommendationsummariespaginator)
    """

    def paginate(
        self,
        *,
        groupBy: str,
        filter: "FilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecommendationSummariesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cost-optimization-hub.html#CostOptimizationHub.Paginator.ListRecommendationSummaries.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators.html#listrecommendationsummariespaginator)
        """

class ListRecommendationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cost-optimization-hub.html#CostOptimizationHub.Paginator.ListRecommendations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators.html#listrecommendationspaginator)
    """

    def paginate(
        self,
        *,
        filter: "FilterTypeDef" = None,
        includeAllRecommendations: bool = None,
        orderBy: "OrderByTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/cost-optimization-hub.html#CostOptimizationHub.Paginator.ListRecommendations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/paginators.html#listrecommendationspaginator)
        """
