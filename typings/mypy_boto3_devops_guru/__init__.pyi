"""
Main interface for devops-guru service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_devops_guru import (
        Client,
        DescribeOrganizationResourceCollectionHealthPaginator,
        DescribeResourceCollectionHealthPaginator,
        DevOpsGuruClient,
        GetCostEstimationPaginator,
        GetResourceCollectionPaginator,
        ListAnomaliesForInsightPaginator,
        ListAnomalousLogGroupsPaginator,
        ListEventsPaginator,
        ListInsightsPaginator,
        ListMonitoredResourcesPaginator,
        ListNotificationChannelsPaginator,
        ListOrganizationInsightsPaginator,
        ListRecommendationsPaginator,
        SearchInsightsPaginator,
        SearchOrganizationInsightsPaginator,
    )

    session = Session()
    client: DevOpsGuruClient = session.client("devops-guru")

    describe_organization_resource_collection_health_paginator: DescribeOrganizationResourceCollectionHealthPaginator = client.get_paginator("describe_organization_resource_collection_health")
    describe_resource_collection_health_paginator: DescribeResourceCollectionHealthPaginator = client.get_paginator("describe_resource_collection_health")
    get_cost_estimation_paginator: GetCostEstimationPaginator = client.get_paginator("get_cost_estimation")
    get_resource_collection_paginator: GetResourceCollectionPaginator = client.get_paginator("get_resource_collection")
    list_anomalies_for_insight_paginator: ListAnomaliesForInsightPaginator = client.get_paginator("list_anomalies_for_insight")
    list_anomalous_log_groups_paginator: ListAnomalousLogGroupsPaginator = client.get_paginator("list_anomalous_log_groups")
    list_events_paginator: ListEventsPaginator = client.get_paginator("list_events")
    list_insights_paginator: ListInsightsPaginator = client.get_paginator("list_insights")
    list_monitored_resources_paginator: ListMonitoredResourcesPaginator = client.get_paginator("list_monitored_resources")
    list_notification_channels_paginator: ListNotificationChannelsPaginator = client.get_paginator("list_notification_channels")
    list_organization_insights_paginator: ListOrganizationInsightsPaginator = client.get_paginator("list_organization_insights")
    list_recommendations_paginator: ListRecommendationsPaginator = client.get_paginator("list_recommendations")
    search_insights_paginator: SearchInsightsPaginator = client.get_paginator("search_insights")
    search_organization_insights_paginator: SearchOrganizationInsightsPaginator = client.get_paginator("search_organization_insights")
    ```
"""

from .client import DevOpsGuruClient
from .paginator import (
    DescribeOrganizationResourceCollectionHealthPaginator,
    DescribeResourceCollectionHealthPaginator,
    GetCostEstimationPaginator,
    GetResourceCollectionPaginator,
    ListAnomaliesForInsightPaginator,
    ListAnomalousLogGroupsPaginator,
    ListEventsPaginator,
    ListInsightsPaginator,
    ListMonitoredResourcesPaginator,
    ListNotificationChannelsPaginator,
    ListOrganizationInsightsPaginator,
    ListRecommendationsPaginator,
    SearchInsightsPaginator,
    SearchOrganizationInsightsPaginator,
)

Client = DevOpsGuruClient

__all__ = (
    "Client",
    "DescribeOrganizationResourceCollectionHealthPaginator",
    "DescribeResourceCollectionHealthPaginator",
    "DevOpsGuruClient",
    "GetCostEstimationPaginator",
    "GetResourceCollectionPaginator",
    "ListAnomaliesForInsightPaginator",
    "ListAnomalousLogGroupsPaginator",
    "ListEventsPaginator",
    "ListInsightsPaginator",
    "ListMonitoredResourcesPaginator",
    "ListNotificationChannelsPaginator",
    "ListOrganizationInsightsPaginator",
    "ListRecommendationsPaginator",
    "SearchInsightsPaginator",
    "SearchOrganizationInsightsPaginator",
)
