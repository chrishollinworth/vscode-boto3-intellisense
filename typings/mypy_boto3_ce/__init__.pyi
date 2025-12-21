"""
Main interface for ce service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ce import (
        Client,
        CostExplorerClient,
        GetAnomaliesPaginator,
        GetAnomalyMonitorsPaginator,
        GetAnomalySubscriptionsPaginator,
        GetCostAndUsageComparisonsPaginator,
        GetCostComparisonDriversPaginator,
        ListCostAllocationTagBackfillHistoryPaginator,
        ListCostAllocationTagsPaginator,
        ListCostCategoryDefinitionsPaginator,
        ListCostCategoryResourceAssociationsPaginator,
    )

    session = Session()
    client: CostExplorerClient = session.client("ce")

    get_anomalies_paginator: GetAnomaliesPaginator = client.get_paginator("get_anomalies")
    get_anomaly_monitors_paginator: GetAnomalyMonitorsPaginator = client.get_paginator("get_anomaly_monitors")
    get_anomaly_subscriptions_paginator: GetAnomalySubscriptionsPaginator = client.get_paginator("get_anomaly_subscriptions")
    get_cost_and_usage_comparisons_paginator: GetCostAndUsageComparisonsPaginator = client.get_paginator("get_cost_and_usage_comparisons")
    get_cost_comparison_drivers_paginator: GetCostComparisonDriversPaginator = client.get_paginator("get_cost_comparison_drivers")
    list_cost_allocation_tag_backfill_history_paginator: ListCostAllocationTagBackfillHistoryPaginator = client.get_paginator("list_cost_allocation_tag_backfill_history")
    list_cost_allocation_tags_paginator: ListCostAllocationTagsPaginator = client.get_paginator("list_cost_allocation_tags")
    list_cost_category_definitions_paginator: ListCostCategoryDefinitionsPaginator = client.get_paginator("list_cost_category_definitions")
    list_cost_category_resource_associations_paginator: ListCostCategoryResourceAssociationsPaginator = client.get_paginator("list_cost_category_resource_associations")
    ```
"""

from .client import CostExplorerClient
from .paginator import (
    GetAnomaliesPaginator,
    GetAnomalyMonitorsPaginator,
    GetAnomalySubscriptionsPaginator,
    GetCostAndUsageComparisonsPaginator,
    GetCostComparisonDriversPaginator,
    ListCostAllocationTagBackfillHistoryPaginator,
    ListCostAllocationTagsPaginator,
    ListCostCategoryDefinitionsPaginator,
    ListCostCategoryResourceAssociationsPaginator,
)

Client = CostExplorerClient

__all__ = (
    "Client",
    "CostExplorerClient",
    "GetAnomaliesPaginator",
    "GetAnomalyMonitorsPaginator",
    "GetAnomalySubscriptionsPaginator",
    "GetCostAndUsageComparisonsPaginator",
    "GetCostComparisonDriversPaginator",
    "ListCostAllocationTagBackfillHistoryPaginator",
    "ListCostAllocationTagsPaginator",
    "ListCostCategoryDefinitionsPaginator",
    "ListCostCategoryResourceAssociationsPaginator",
)
