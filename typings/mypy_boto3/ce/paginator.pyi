"""
Type annotations for ce service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ce.client import CostExplorerClient
    from mypy_boto3_ce.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetAnomaliesRequestPaginateTypeDef,
    GetAnomaliesResponseTypeDef,
    GetAnomalyMonitorsRequestPaginateTypeDef,
    GetAnomalyMonitorsResponsePaginatorTypeDef,
    GetAnomalySubscriptionsRequestPaginateTypeDef,
    GetAnomalySubscriptionsResponsePaginatorTypeDef,
    GetCostAndUsageComparisonsRequestPaginateTypeDef,
    GetCostAndUsageComparisonsResponsePaginatorTypeDef,
    GetCostComparisonDriversRequestPaginateTypeDef,
    GetCostComparisonDriversResponsePaginatorTypeDef,
    ListCostAllocationTagBackfillHistoryRequestPaginateTypeDef,
    ListCostAllocationTagBackfillHistoryResponseTypeDef,
    ListCostAllocationTagsRequestPaginateTypeDef,
    ListCostAllocationTagsResponseTypeDef,
    ListCostCategoryDefinitionsRequestPaginateTypeDef,
    ListCostCategoryDefinitionsResponseTypeDef,
    ListCostCategoryResourceAssociationsRequestPaginateTypeDef,
    ListCostCategoryResourceAssociationsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
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

if TYPE_CHECKING:
    _GetAnomaliesPaginatorBase = Paginator[GetAnomaliesResponseTypeDef]
else:
    _GetAnomaliesPaginatorBase = Paginator  # type: ignore[assignment]

class GetAnomaliesPaginator(_GetAnomaliesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetAnomalies.html#CostExplorer.Paginator.GetAnomalies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getanomaliespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAnomaliesRequestPaginateTypeDef]
    ) -> PageIterator[GetAnomaliesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetAnomalies.html#CostExplorer.Paginator.GetAnomalies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getanomaliespaginator)
        """

if TYPE_CHECKING:
    _GetAnomalyMonitorsPaginatorBase = Paginator[GetAnomalyMonitorsResponsePaginatorTypeDef]
else:
    _GetAnomalyMonitorsPaginatorBase = Paginator  # type: ignore[assignment]

class GetAnomalyMonitorsPaginator(_GetAnomalyMonitorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetAnomalyMonitors.html#CostExplorer.Paginator.GetAnomalyMonitors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getanomalymonitorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAnomalyMonitorsRequestPaginateTypeDef]
    ) -> PageIterator[GetAnomalyMonitorsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetAnomalyMonitors.html#CostExplorer.Paginator.GetAnomalyMonitors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getanomalymonitorspaginator)
        """

if TYPE_CHECKING:
    _GetAnomalySubscriptionsPaginatorBase = Paginator[
        GetAnomalySubscriptionsResponsePaginatorTypeDef
    ]
else:
    _GetAnomalySubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class GetAnomalySubscriptionsPaginator(_GetAnomalySubscriptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetAnomalySubscriptions.html#CostExplorer.Paginator.GetAnomalySubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getanomalysubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAnomalySubscriptionsRequestPaginateTypeDef]
    ) -> PageIterator[GetAnomalySubscriptionsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetAnomalySubscriptions.html#CostExplorer.Paginator.GetAnomalySubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getanomalysubscriptionspaginator)
        """

if TYPE_CHECKING:
    _GetCostAndUsageComparisonsPaginatorBase = Paginator[
        GetCostAndUsageComparisonsResponsePaginatorTypeDef
    ]
else:
    _GetCostAndUsageComparisonsPaginatorBase = Paginator  # type: ignore[assignment]

class GetCostAndUsageComparisonsPaginator(_GetCostAndUsageComparisonsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetCostAndUsageComparisons.html#CostExplorer.Paginator.GetCostAndUsageComparisons)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getcostandusagecomparisonspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetCostAndUsageComparisonsRequestPaginateTypeDef]
    ) -> PageIterator[GetCostAndUsageComparisonsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetCostAndUsageComparisons.html#CostExplorer.Paginator.GetCostAndUsageComparisons.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getcostandusagecomparisonspaginator)
        """

if TYPE_CHECKING:
    _GetCostComparisonDriversPaginatorBase = Paginator[
        GetCostComparisonDriversResponsePaginatorTypeDef
    ]
else:
    _GetCostComparisonDriversPaginatorBase = Paginator  # type: ignore[assignment]

class GetCostComparisonDriversPaginator(_GetCostComparisonDriversPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetCostComparisonDrivers.html#CostExplorer.Paginator.GetCostComparisonDrivers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getcostcomparisondriverspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetCostComparisonDriversRequestPaginateTypeDef]
    ) -> PageIterator[GetCostComparisonDriversResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/GetCostComparisonDrivers.html#CostExplorer.Paginator.GetCostComparisonDrivers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#getcostcomparisondriverspaginator)
        """

if TYPE_CHECKING:
    _ListCostAllocationTagBackfillHistoryPaginatorBase = Paginator[
        ListCostAllocationTagBackfillHistoryResponseTypeDef
    ]
else:
    _ListCostAllocationTagBackfillHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class ListCostAllocationTagBackfillHistoryPaginator(
    _ListCostAllocationTagBackfillHistoryPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/ListCostAllocationTagBackfillHistory.html#CostExplorer.Paginator.ListCostAllocationTagBackfillHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#listcostallocationtagbackfillhistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCostAllocationTagBackfillHistoryRequestPaginateTypeDef]
    ) -> PageIterator[ListCostAllocationTagBackfillHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/ListCostAllocationTagBackfillHistory.html#CostExplorer.Paginator.ListCostAllocationTagBackfillHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#listcostallocationtagbackfillhistorypaginator)
        """

if TYPE_CHECKING:
    _ListCostAllocationTagsPaginatorBase = Paginator[ListCostAllocationTagsResponseTypeDef]
else:
    _ListCostAllocationTagsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCostAllocationTagsPaginator(_ListCostAllocationTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/ListCostAllocationTags.html#CostExplorer.Paginator.ListCostAllocationTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#listcostallocationtagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCostAllocationTagsRequestPaginateTypeDef]
    ) -> PageIterator[ListCostAllocationTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/ListCostAllocationTags.html#CostExplorer.Paginator.ListCostAllocationTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#listcostallocationtagspaginator)
        """

if TYPE_CHECKING:
    _ListCostCategoryDefinitionsPaginatorBase = Paginator[
        ListCostCategoryDefinitionsResponseTypeDef
    ]
else:
    _ListCostCategoryDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCostCategoryDefinitionsPaginator(_ListCostCategoryDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/ListCostCategoryDefinitions.html#CostExplorer.Paginator.ListCostCategoryDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#listcostcategorydefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCostCategoryDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[ListCostCategoryDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/ListCostCategoryDefinitions.html#CostExplorer.Paginator.ListCostCategoryDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#listcostcategorydefinitionspaginator)
        """

if TYPE_CHECKING:
    _ListCostCategoryResourceAssociationsPaginatorBase = Paginator[
        ListCostCategoryResourceAssociationsResponseTypeDef
    ]
else:
    _ListCostCategoryResourceAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCostCategoryResourceAssociationsPaginator(
    _ListCostCategoryResourceAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/ListCostCategoryResourceAssociations.html#CostExplorer.Paginator.ListCostCategoryResourceAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#listcostcategoryresourceassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCostCategoryResourceAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListCostCategoryResourceAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ce/paginator/ListCostCategoryResourceAssociations.html#CostExplorer.Paginator.ListCostCategoryResourceAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/paginators/#listcostcategoryresourceassociationspaginator)
        """
