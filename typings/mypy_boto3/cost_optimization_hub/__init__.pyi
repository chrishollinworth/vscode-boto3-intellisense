"""
Main interface for cost-optimization-hub service.

Usage::

    ```python
    import boto3
    from mypy_boto3_cost_optimization_hub import (
        Client,
        CostOptimizationHubClient,
        ListEnrollmentStatusesPaginator,
        ListRecommendationSummariesPaginator,
        ListRecommendationsPaginator,
    )

    session = boto3.Session()

    client: CostOptimizationHubClient = boto3.client("cost-optimization-hub")
    session_client: CostOptimizationHubClient = session.client("cost-optimization-hub")

    list_enrollment_statuses_paginator: ListEnrollmentStatusesPaginator = client.get_paginator("list_enrollment_statuses")
    list_recommendation_summaries_paginator: ListRecommendationSummariesPaginator = client.get_paginator("list_recommendation_summaries")
    list_recommendations_paginator: ListRecommendationsPaginator = client.get_paginator("list_recommendations")
    ```
"""

from .client import CostOptimizationHubClient
from .paginator import (
    ListEnrollmentStatusesPaginator,
    ListRecommendationsPaginator,
    ListRecommendationSummariesPaginator,
)

Client = CostOptimizationHubClient

__all__ = (
    "Client",
    "CostOptimizationHubClient",
    "ListEnrollmentStatusesPaginator",
    "ListRecommendationSummariesPaginator",
    "ListRecommendationsPaginator",
)
