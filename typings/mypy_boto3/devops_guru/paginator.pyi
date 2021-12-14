"""
Type annotations for devops-guru service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_devops_guru import DevOpsGuruClient
    from mypy_boto3_devops_guru.paginator import (
        DescribeOrganizationResourceCollectionHealthPaginator,
        DescribeResourceCollectionHealthPaginator,
        GetCostEstimationPaginator,
        GetResourceCollectionPaginator,
        ListAnomaliesForInsightPaginator,
        ListEventsPaginator,
        ListInsightsPaginator,
        ListNotificationChannelsPaginator,
        ListOrganizationInsightsPaginator,
        ListRecommendationsPaginator,
        SearchInsightsPaginator,
        SearchOrganizationInsightsPaginator,
    )

    client: DevOpsGuruClient = boto3.client("devops-guru")

    describe_organization_resource_collection_health_paginator: DescribeOrganizationResourceCollectionHealthPaginator = client.get_paginator("describe_organization_resource_collection_health")
    describe_resource_collection_health_paginator: DescribeResourceCollectionHealthPaginator = client.get_paginator("describe_resource_collection_health")
    get_cost_estimation_paginator: GetCostEstimationPaginator = client.get_paginator("get_cost_estimation")
    get_resource_collection_paginator: GetResourceCollectionPaginator = client.get_paginator("get_resource_collection")
    list_anomalies_for_insight_paginator: ListAnomaliesForInsightPaginator = client.get_paginator("list_anomalies_for_insight")
    list_events_paginator: ListEventsPaginator = client.get_paginator("list_events")
    list_insights_paginator: ListInsightsPaginator = client.get_paginator("list_insights")
    list_notification_channels_paginator: ListNotificationChannelsPaginator = client.get_paginator("list_notification_channels")
    list_organization_insights_paginator: ListOrganizationInsightsPaginator = client.get_paginator("list_organization_insights")
    list_recommendations_paginator: ListRecommendationsPaginator = client.get_paginator("list_recommendations")
    search_insights_paginator: SearchInsightsPaginator = client.get_paginator("search_insights")
    search_organization_insights_paginator: SearchOrganizationInsightsPaginator = client.get_paginator("search_organization_insights")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    InsightTypeType,
    LocaleType,
    OrganizationResourceCollectionTypeType,
    ResourceCollectionTypeType,
)
from .type_defs import (
    DescribeOrganizationResourceCollectionHealthResponseTypeDef,
    DescribeResourceCollectionHealthResponseTypeDef,
    GetCostEstimationResponseTypeDef,
    GetResourceCollectionResponseTypeDef,
    ListAnomaliesForInsightResponseTypeDef,
    ListEventsFiltersTypeDef,
    ListEventsResponseTypeDef,
    ListInsightsResponseTypeDef,
    ListInsightsStatusFilterTypeDef,
    ListNotificationChannelsResponseTypeDef,
    ListOrganizationInsightsResponseTypeDef,
    ListRecommendationsResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchInsightsFiltersTypeDef,
    SearchInsightsResponseTypeDef,
    SearchOrganizationInsightsFiltersTypeDef,
    SearchOrganizationInsightsResponseTypeDef,
    StartTimeRangeTypeDef,
)

__all__ = (
    "DescribeOrganizationResourceCollectionHealthPaginator",
    "DescribeResourceCollectionHealthPaginator",
    "GetCostEstimationPaginator",
    "GetResourceCollectionPaginator",
    "ListAnomaliesForInsightPaginator",
    "ListEventsPaginator",
    "ListInsightsPaginator",
    "ListNotificationChannelsPaginator",
    "ListOrganizationInsightsPaginator",
    "ListRecommendationsPaginator",
    "SearchInsightsPaginator",
    "SearchOrganizationInsightsPaginator",
)

class DescribeOrganizationResourceCollectionHealthPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.DescribeOrganizationResourceCollectionHealth)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#describeorganizationresourcecollectionhealthpaginator)
    """

    def paginate(
        self,
        *,
        OrganizationResourceCollectionType: OrganizationResourceCollectionTypeType,
        AccountIds: List[str] = None,
        OrganizationalUnitIds: List[str] = None,
        MaxResults: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeOrganizationResourceCollectionHealthResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.DescribeOrganizationResourceCollectionHealth.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#describeorganizationresourcecollectionhealthpaginator)
        """

class DescribeResourceCollectionHealthPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.DescribeResourceCollectionHealth)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#describeresourcecollectionhealthpaginator)
    """

    def paginate(
        self,
        *,
        ResourceCollectionType: ResourceCollectionTypeType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeResourceCollectionHealthResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.DescribeResourceCollectionHealth.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#describeresourcecollectionhealthpaginator)
        """

class GetCostEstimationPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.GetCostEstimation)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#getcostestimationpaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCostEstimationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.GetCostEstimation.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#getcostestimationpaginator)
        """

class GetResourceCollectionPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.GetResourceCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#getresourcecollectionpaginator)
    """

    def paginate(
        self,
        *,
        ResourceCollectionType: ResourceCollectionTypeType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetResourceCollectionResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.GetResourceCollection.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#getresourcecollectionpaginator)
        """

class ListAnomaliesForInsightPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListAnomaliesForInsight)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listanomaliesforinsightpaginator)
    """

    def paginate(
        self,
        *,
        InsightId: str,
        StartTimeRange: "StartTimeRangeTypeDef" = None,
        AccountId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAnomaliesForInsightResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListAnomaliesForInsight.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listanomaliesforinsightpaginator)
        """

class ListEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listeventspaginator)
    """

    def paginate(
        self,
        *,
        Filters: "ListEventsFiltersTypeDef",
        AccountId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listeventspaginator)
        """

class ListInsightsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListInsights)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listinsightspaginator)
    """

    def paginate(
        self,
        *,
        StatusFilter: "ListInsightsStatusFilterTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInsightsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListInsights.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listinsightspaginator)
        """

class ListNotificationChannelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListNotificationChannels)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listnotificationchannelspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNotificationChannelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListNotificationChannels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listnotificationchannelspaginator)
        """

class ListOrganizationInsightsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListOrganizationInsights)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listorganizationinsightspaginator)
    """

    def paginate(
        self,
        *,
        StatusFilter: "ListInsightsStatusFilterTypeDef",
        AccountIds: List[str] = None,
        OrganizationalUnitIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOrganizationInsightsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListOrganizationInsights.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listorganizationinsightspaginator)
        """

class ListRecommendationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListRecommendations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listrecommendationspaginator)
    """

    def paginate(
        self,
        *,
        InsightId: str,
        Locale: LocaleType = None,
        AccountId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListRecommendations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listrecommendationspaginator)
        """

class SearchInsightsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.SearchInsights)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#searchinsightspaginator)
    """

    def paginate(
        self,
        *,
        StartTimeRange: "StartTimeRangeTypeDef",
        Type: InsightTypeType,
        Filters: "SearchInsightsFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchInsightsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.SearchInsights.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#searchinsightspaginator)
        """

class SearchOrganizationInsightsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.SearchOrganizationInsights)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#searchorganizationinsightspaginator)
    """

    def paginate(
        self,
        *,
        AccountIds: List[str],
        StartTimeRange: "StartTimeRangeTypeDef",
        Type: InsightTypeType,
        Filters: "SearchOrganizationInsightsFiltersTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchOrganizationInsightsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/devops-guru.html#DevOpsGuru.Paginator.SearchOrganizationInsights.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#searchorganizationinsightspaginator)
        """
