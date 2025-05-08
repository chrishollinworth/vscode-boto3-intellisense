"""
Type annotations for devops-guru service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_devops_guru.client import DevOpsGuruClient
    from mypy_boto3_devops_guru.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeOrganizationResourceCollectionHealthRequestPaginateTypeDef,
    DescribeOrganizationResourceCollectionHealthResponseTypeDef,
    DescribeResourceCollectionHealthRequestPaginateTypeDef,
    DescribeResourceCollectionHealthResponseTypeDef,
    GetCostEstimationRequestPaginateTypeDef,
    GetCostEstimationResponseTypeDef,
    GetResourceCollectionRequestPaginateTypeDef,
    GetResourceCollectionResponseTypeDef,
    ListAnomaliesForInsightRequestPaginateTypeDef,
    ListAnomaliesForInsightResponseTypeDef,
    ListAnomalousLogGroupsRequestPaginateTypeDef,
    ListAnomalousLogGroupsResponseTypeDef,
    ListEventsRequestPaginateTypeDef,
    ListEventsResponseTypeDef,
    ListInsightsRequestPaginateTypeDef,
    ListInsightsResponseTypeDef,
    ListMonitoredResourcesRequestPaginateTypeDef,
    ListMonitoredResourcesResponseTypeDef,
    ListNotificationChannelsRequestPaginateTypeDef,
    ListNotificationChannelsResponseTypeDef,
    ListOrganizationInsightsRequestPaginateTypeDef,
    ListOrganizationInsightsResponseTypeDef,
    ListRecommendationsRequestPaginateTypeDef,
    ListRecommendationsResponseTypeDef,
    SearchInsightsRequestPaginateTypeDef,
    SearchInsightsResponseTypeDef,
    SearchOrganizationInsightsRequestPaginateTypeDef,
    SearchOrganizationInsightsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeOrganizationResourceCollectionHealthPaginator",
    "DescribeResourceCollectionHealthPaginator",
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

if TYPE_CHECKING:
    _DescribeOrganizationResourceCollectionHealthPaginatorBase = Paginator[
        DescribeOrganizationResourceCollectionHealthResponseTypeDef
    ]
else:
    _DescribeOrganizationResourceCollectionHealthPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeOrganizationResourceCollectionHealthPaginator(
    _DescribeOrganizationResourceCollectionHealthPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/DescribeOrganizationResourceCollectionHealth.html#DevOpsGuru.Paginator.DescribeOrganizationResourceCollectionHealth)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#describeorganizationresourcecollectionhealthpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeOrganizationResourceCollectionHealthRequestPaginateTypeDef]
    ) -> PageIterator[DescribeOrganizationResourceCollectionHealthResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/DescribeOrganizationResourceCollectionHealth.html#DevOpsGuru.Paginator.DescribeOrganizationResourceCollectionHealth.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#describeorganizationresourcecollectionhealthpaginator)
        """

if TYPE_CHECKING:
    _DescribeResourceCollectionHealthPaginatorBase = Paginator[
        DescribeResourceCollectionHealthResponseTypeDef
    ]
else:
    _DescribeResourceCollectionHealthPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeResourceCollectionHealthPaginator(_DescribeResourceCollectionHealthPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/DescribeResourceCollectionHealth.html#DevOpsGuru.Paginator.DescribeResourceCollectionHealth)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#describeresourcecollectionhealthpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeResourceCollectionHealthRequestPaginateTypeDef]
    ) -> PageIterator[DescribeResourceCollectionHealthResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/DescribeResourceCollectionHealth.html#DevOpsGuru.Paginator.DescribeResourceCollectionHealth.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#describeresourcecollectionhealthpaginator)
        """

if TYPE_CHECKING:
    _GetCostEstimationPaginatorBase = Paginator[GetCostEstimationResponseTypeDef]
else:
    _GetCostEstimationPaginatorBase = Paginator  # type: ignore[assignment]

class GetCostEstimationPaginator(_GetCostEstimationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/GetCostEstimation.html#DevOpsGuru.Paginator.GetCostEstimation)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#getcostestimationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetCostEstimationRequestPaginateTypeDef]
    ) -> PageIterator[GetCostEstimationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/GetCostEstimation.html#DevOpsGuru.Paginator.GetCostEstimation.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#getcostestimationpaginator)
        """

if TYPE_CHECKING:
    _GetResourceCollectionPaginatorBase = Paginator[GetResourceCollectionResponseTypeDef]
else:
    _GetResourceCollectionPaginatorBase = Paginator  # type: ignore[assignment]

class GetResourceCollectionPaginator(_GetResourceCollectionPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/GetResourceCollection.html#DevOpsGuru.Paginator.GetResourceCollection)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#getresourcecollectionpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetResourceCollectionRequestPaginateTypeDef]
    ) -> PageIterator[GetResourceCollectionResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/GetResourceCollection.html#DevOpsGuru.Paginator.GetResourceCollection.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#getresourcecollectionpaginator)
        """

if TYPE_CHECKING:
    _ListAnomaliesForInsightPaginatorBase = Paginator[ListAnomaliesForInsightResponseTypeDef]
else:
    _ListAnomaliesForInsightPaginatorBase = Paginator  # type: ignore[assignment]

class ListAnomaliesForInsightPaginator(_ListAnomaliesForInsightPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListAnomaliesForInsight.html#DevOpsGuru.Paginator.ListAnomaliesForInsight)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listanomaliesforinsightpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAnomaliesForInsightRequestPaginateTypeDef]
    ) -> PageIterator[ListAnomaliesForInsightResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListAnomaliesForInsight.html#DevOpsGuru.Paginator.ListAnomaliesForInsight.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listanomaliesforinsightpaginator)
        """

if TYPE_CHECKING:
    _ListAnomalousLogGroupsPaginatorBase = Paginator[ListAnomalousLogGroupsResponseTypeDef]
else:
    _ListAnomalousLogGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAnomalousLogGroupsPaginator(_ListAnomalousLogGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListAnomalousLogGroups.html#DevOpsGuru.Paginator.ListAnomalousLogGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listanomalousloggroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAnomalousLogGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListAnomalousLogGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListAnomalousLogGroups.html#DevOpsGuru.Paginator.ListAnomalousLogGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listanomalousloggroupspaginator)
        """

if TYPE_CHECKING:
    _ListEventsPaginatorBase = Paginator[ListEventsResponseTypeDef]
else:
    _ListEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEventsPaginator(_ListEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListEvents.html#DevOpsGuru.Paginator.ListEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEventsRequestPaginateTypeDef]
    ) -> PageIterator[ListEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListEvents.html#DevOpsGuru.Paginator.ListEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listeventspaginator)
        """

if TYPE_CHECKING:
    _ListInsightsPaginatorBase = Paginator[ListInsightsResponseTypeDef]
else:
    _ListInsightsPaginatorBase = Paginator  # type: ignore[assignment]

class ListInsightsPaginator(_ListInsightsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListInsights.html#DevOpsGuru.Paginator.ListInsights)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listinsightspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInsightsRequestPaginateTypeDef]
    ) -> PageIterator[ListInsightsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListInsights.html#DevOpsGuru.Paginator.ListInsights.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listinsightspaginator)
        """

if TYPE_CHECKING:
    _ListMonitoredResourcesPaginatorBase = Paginator[ListMonitoredResourcesResponseTypeDef]
else:
    _ListMonitoredResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListMonitoredResourcesPaginator(_ListMonitoredResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListMonitoredResources.html#DevOpsGuru.Paginator.ListMonitoredResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listmonitoredresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMonitoredResourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListMonitoredResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListMonitoredResources.html#DevOpsGuru.Paginator.ListMonitoredResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listmonitoredresourcespaginator)
        """

if TYPE_CHECKING:
    _ListNotificationChannelsPaginatorBase = Paginator[ListNotificationChannelsResponseTypeDef]
else:
    _ListNotificationChannelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListNotificationChannelsPaginator(_ListNotificationChannelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListNotificationChannels.html#DevOpsGuru.Paginator.ListNotificationChannels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listnotificationchannelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNotificationChannelsRequestPaginateTypeDef]
    ) -> PageIterator[ListNotificationChannelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListNotificationChannels.html#DevOpsGuru.Paginator.ListNotificationChannels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listnotificationchannelspaginator)
        """

if TYPE_CHECKING:
    _ListOrganizationInsightsPaginatorBase = Paginator[ListOrganizationInsightsResponseTypeDef]
else:
    _ListOrganizationInsightsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOrganizationInsightsPaginator(_ListOrganizationInsightsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListOrganizationInsights.html#DevOpsGuru.Paginator.ListOrganizationInsights)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listorganizationinsightspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOrganizationInsightsRequestPaginateTypeDef]
    ) -> PageIterator[ListOrganizationInsightsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListOrganizationInsights.html#DevOpsGuru.Paginator.ListOrganizationInsights.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listorganizationinsightspaginator)
        """

if TYPE_CHECKING:
    _ListRecommendationsPaginatorBase = Paginator[ListRecommendationsResponseTypeDef]
else:
    _ListRecommendationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecommendationsPaginator(_ListRecommendationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListRecommendations.html#DevOpsGuru.Paginator.ListRecommendations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listrecommendationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecommendationsRequestPaginateTypeDef]
    ) -> PageIterator[ListRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/ListRecommendations.html#DevOpsGuru.Paginator.ListRecommendations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#listrecommendationspaginator)
        """

if TYPE_CHECKING:
    _SearchInsightsPaginatorBase = Paginator[SearchInsightsResponseTypeDef]
else:
    _SearchInsightsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchInsightsPaginator(_SearchInsightsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/SearchInsights.html#DevOpsGuru.Paginator.SearchInsights)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#searchinsightspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchInsightsRequestPaginateTypeDef]
    ) -> PageIterator[SearchInsightsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/SearchInsights.html#DevOpsGuru.Paginator.SearchInsights.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#searchinsightspaginator)
        """

if TYPE_CHECKING:
    _SearchOrganizationInsightsPaginatorBase = Paginator[SearchOrganizationInsightsResponseTypeDef]
else:
    _SearchOrganizationInsightsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchOrganizationInsightsPaginator(_SearchOrganizationInsightsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/SearchOrganizationInsights.html#DevOpsGuru.Paginator.SearchOrganizationInsights)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#searchorganizationinsightspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchOrganizationInsightsRequestPaginateTypeDef]
    ) -> PageIterator[SearchOrganizationInsightsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/paginator/SearchOrganizationInsights.html#DevOpsGuru.Paginator.SearchOrganizationInsights.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators/#searchorganizationinsightspaginator)
        """
