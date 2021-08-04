"""
Main interface for devops-guru service.

Usage::

    ```python
    import boto3
    from mypy_boto3_devops_guru import (
        Client,
        DescribeResourceCollectionHealthPaginator,
        DevOpsGuruClient,
        GetCostEstimationPaginator,
        GetResourceCollectionPaginator,
        ListAnomaliesForInsightPaginator,
        ListEventsPaginator,
        ListInsightsPaginator,
        ListNotificationChannelsPaginator,
        ListRecommendationsPaginator,
        SearchInsightsPaginator,
    )

    session = boto3.Session()

    client: DevOpsGuruClient = boto3.client("devops-guru")
    session_client: DevOpsGuruClient = session.client("devops-guru")

    describe_resource_collection_health_paginator: DescribeResourceCollectionHealthPaginator = client.get_paginator("describe_resource_collection_health")
    get_cost_estimation_paginator: GetCostEstimationPaginator = client.get_paginator("get_cost_estimation")
    get_resource_collection_paginator: GetResourceCollectionPaginator = client.get_paginator("get_resource_collection")
    list_anomalies_for_insight_paginator: ListAnomaliesForInsightPaginator = client.get_paginator("list_anomalies_for_insight")
    list_events_paginator: ListEventsPaginator = client.get_paginator("list_events")
    list_insights_paginator: ListInsightsPaginator = client.get_paginator("list_insights")
    list_notification_channels_paginator: ListNotificationChannelsPaginator = client.get_paginator("list_notification_channels")
    list_recommendations_paginator: ListRecommendationsPaginator = client.get_paginator("list_recommendations")
    search_insights_paginator: SearchInsightsPaginator = client.get_paginator("search_insights")
    ```
"""
from .client import DevOpsGuruClient
from .paginator import (
    DescribeResourceCollectionHealthPaginator,
    GetCostEstimationPaginator,
    GetResourceCollectionPaginator,
    ListAnomaliesForInsightPaginator,
    ListEventsPaginator,
    ListInsightsPaginator,
    ListNotificationChannelsPaginator,
    ListRecommendationsPaginator,
    SearchInsightsPaginator,
)

Client = DevOpsGuruClient

__all__ = (
    "Client",
    "DescribeResourceCollectionHealthPaginator",
    "DevOpsGuruClient",
    "GetCostEstimationPaginator",
    "GetResourceCollectionPaginator",
    "ListAnomaliesForInsightPaginator",
    "ListEventsPaginator",
    "ListInsightsPaginator",
    "ListNotificationChannelsPaginator",
    "ListRecommendationsPaginator",
    "SearchInsightsPaginator",
)
