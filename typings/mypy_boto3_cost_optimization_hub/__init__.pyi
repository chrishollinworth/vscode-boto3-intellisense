"""
Main interface for cost-optimization-hub service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cost_optimization_hub/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cost_optimization_hub import (
        Client,
        CostOptimizationHubClient,
        ListEfficiencyMetricsPaginator,
        ListEnrollmentStatusesPaginator,
        ListRecommendationSummariesPaginator,
        ListRecommendationsPaginator,
    )

    session = Session()
    client: CostOptimizationHubClient = session.client("cost-optimization-hub")

    list_efficiency_metrics_paginator: ListEfficiencyMetricsPaginator = client.get_paginator("list_efficiency_metrics")
    list_enrollment_statuses_paginator: ListEnrollmentStatusesPaginator = client.get_paginator("list_enrollment_statuses")
    list_recommendation_summaries_paginator: ListRecommendationSummariesPaginator = client.get_paginator("list_recommendation_summaries")
    list_recommendations_paginator: ListRecommendationsPaginator = client.get_paginator("list_recommendations")
    ```
"""

from .client import CostOptimizationHubClient
from .paginator import (
    ListEfficiencyMetricsPaginator,
    ListEnrollmentStatusesPaginator,
    ListRecommendationsPaginator,
    ListRecommendationSummariesPaginator,
)

Client = CostOptimizationHubClient

__all__ = (
    "Client",
    "CostOptimizationHubClient",
    "ListEfficiencyMetricsPaginator",
    "ListEnrollmentStatusesPaginator",
    "ListRecommendationSummariesPaginator",
    "ListRecommendationsPaginator",
)
