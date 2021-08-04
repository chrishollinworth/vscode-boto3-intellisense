"""
Type annotations for devops-guru service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_devops_guru import DevOpsGuruClient
    from mypy_boto3_devops_guru.paginator import (
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

    client: DevOpsGuruClient = boto3.client("devops-guru")

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
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import InsightTypeType, LocaleType, ResourceCollectionTypeType
from .type_defs import (
    DescribeResourceCollectionHealthResponseTypeDef,
    GetCostEstimationResponseTypeDef,
    GetResourceCollectionResponseTypeDef,
    ListAnomaliesForInsightResponseTypeDef,
    ListEventsFiltersTypeDef,
    ListEventsResponseTypeDef,
    ListInsightsResponseTypeDef,
    ListInsightsStatusFilterTypeDef,
    ListNotificationChannelsResponseTypeDef,
    ListRecommendationsResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchInsightsFiltersTypeDef,
    SearchInsightsResponseTypeDef,
    StartTimeRangeTypeDef,
)

__all__ = (
    "DescribeResourceCollectionHealthPaginator",
    "GetCostEstimationPaginator",
    "GetResourceCollectionPaginator",
    "ListAnomaliesForInsightPaginator",
    "ListEventsPaginator",
    "ListInsightsPaginator",
    "ListNotificationChannelsPaginator",
    "ListRecommendationsPaginator",
    "SearchInsightsPaginator",
)

class DescribeResourceCollectionHealthPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.DescribeResourceCollectionHealth)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#describeresourcecollectionhealthpaginator)
    """

    def paginate(
        self,
        *,
        ResourceCollectionType: ResourceCollectionTypeType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeResourceCollectionHealthResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.DescribeResourceCollectionHealth.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#describeresourcecollectionhealthpaginator)
        """

class GetCostEstimationPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.GetCostEstimation)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#getcostestimationpaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetCostEstimationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.GetCostEstimation.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#getcostestimationpaginator)
        """

class GetResourceCollectionPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.GetResourceCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#getresourcecollectionpaginator)
    """

    def paginate(
        self,
        *,
        ResourceCollectionType: ResourceCollectionTypeType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetResourceCollectionResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.GetResourceCollection.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#getresourcecollectionpaginator)
        """

class ListAnomaliesForInsightPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListAnomaliesForInsight)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listanomaliesforinsightpaginator)
    """

    def paginate(
        self,
        *,
        InsightId: str,
        StartTimeRange: "StartTimeRangeTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAnomaliesForInsightResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListAnomaliesForInsight.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listanomaliesforinsightpaginator)
        """

class ListEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listeventspaginator)
    """

    def paginate(
        self,
        *,
        Filters: "ListEventsFiltersTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listeventspaginator)
        """

class ListInsightsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListInsights)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listinsightspaginator)
    """

    def paginate(
        self,
        *,
        StatusFilter: "ListInsightsStatusFilterTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInsightsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListInsights.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listinsightspaginator)
        """

class ListNotificationChannelsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListNotificationChannels)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listnotificationchannelspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNotificationChannelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListNotificationChannels.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listnotificationchannelspaginator)
        """

class ListRecommendationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListRecommendations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listrecommendationspaginator)
    """

    def paginate(
        self,
        *,
        InsightId: str,
        Locale: LocaleType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecommendationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListRecommendations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listrecommendationspaginator)
        """

class SearchInsightsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.SearchInsights)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/devops-guru.html#DevOpsGuru.Paginator.SearchInsights.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#searchinsightspaginator)
        """
