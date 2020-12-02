# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for devops-guru service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_devops_guru import DevOpsGuruClient
    from mypy_boto3_devops_guru.paginator import (
        DescribeResourceCollectionHealthPaginator,
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
    get_resource_collection_paginator: GetResourceCollectionPaginator = client.get_paginator("get_resource_collection")
    list_anomalies_for_insight_paginator: ListAnomaliesForInsightPaginator = client.get_paginator("list_anomalies_for_insight")
    list_events_paginator: ListEventsPaginator = client.get_paginator("list_events")
    list_insights_paginator: ListInsightsPaginator = client.get_paginator("list_insights")
    list_notification_channels_paginator: ListNotificationChannelsPaginator = client.get_paginator("list_notification_channels")
    list_recommendations_paginator: ListRecommendationsPaginator = client.get_paginator("list_recommendations")
    search_insights_paginator: SearchInsightsPaginator = client.get_paginator("search_insights")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_devops_guru.type_defs import (
    DescribeResourceCollectionHealthResponseTypeDef,
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeResourceCollectionHealthPaginator",
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
    [Paginator.DescribeResourceCollectionHealth documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.DescribeResourceCollectionHealth)
    """

    def paginate(
        self, ResourceCollectionType: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeResourceCollectionHealthResponseTypeDef]:
        """
        [DescribeResourceCollectionHealth.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.DescribeResourceCollectionHealth.paginate)
        """


class GetResourceCollectionPaginator(Boto3Paginator):
    """
    [Paginator.GetResourceCollection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.GetResourceCollection)
    """

    def paginate(
        self, ResourceCollectionType: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetResourceCollectionResponseTypeDef]:
        """
        [GetResourceCollection.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.GetResourceCollection.paginate)
        """


class ListAnomaliesForInsightPaginator(Boto3Paginator):
    """
    [Paginator.ListAnomaliesForInsight documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListAnomaliesForInsight)
    """

    def paginate(
        self,
        InsightId: str,
        StartTimeRange: "StartTimeRangeTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAnomaliesForInsightResponseTypeDef]:
        """
        [ListAnomaliesForInsight.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListAnomaliesForInsight.paginate)
        """


class ListEventsPaginator(Boto3Paginator):
    """
    [Paginator.ListEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListEvents)
    """

    def paginate(
        self, Filters: ListEventsFiltersTypeDef, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventsResponseTypeDef]:
        """
        [ListEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListEvents.paginate)
        """


class ListInsightsPaginator(Boto3Paginator):
    """
    [Paginator.ListInsights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListInsights)
    """

    def paginate(
        self,
        StatusFilter: ListInsightsStatusFilterTypeDef,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListInsightsResponseTypeDef]:
        """
        [ListInsights.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListInsights.paginate)
        """


class ListNotificationChannelsPaginator(Boto3Paginator):
    """
    [Paginator.ListNotificationChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListNotificationChannels)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListNotificationChannelsResponseTypeDef]:
        """
        [ListNotificationChannels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListNotificationChannels.paginate)
        """


class ListRecommendationsPaginator(Boto3Paginator):
    """
    [Paginator.ListRecommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListRecommendations)
    """

    def paginate(
        self, InsightId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRecommendationsResponseTypeDef]:
        """
        [ListRecommendations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListRecommendations.paginate)
        """


class SearchInsightsPaginator(Boto3Paginator):
    """
    [Paginator.SearchInsights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.SearchInsights)
    """

    def paginate(
        self,
        StartTimeRange: "StartTimeRangeTypeDef",
        Type: Literal["REACTIVE", "PROACTIVE"],
        Filters: SearchInsightsFiltersTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SearchInsightsResponseTypeDef]:
        """
        [SearchInsights.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.28/reference/services/devops-guru.html#DevOpsGuru.Paginator.SearchInsights.paginate)
        """
