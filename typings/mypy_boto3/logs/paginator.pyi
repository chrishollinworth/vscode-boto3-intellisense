"""
Type annotations for logs service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_logs import CloudWatchLogsClient
    from mypy_boto3_logs.paginator import (
        DescribeDeliveriesPaginator,
        DescribeDeliveryDestinationsPaginator,
        DescribeDeliverySourcesPaginator,
        DescribeDestinationsPaginator,
        DescribeExportTasksPaginator,
        DescribeLogGroupsPaginator,
        DescribeLogStreamsPaginator,
        DescribeMetricFiltersPaginator,
        DescribeQueriesPaginator,
        DescribeResourcePoliciesPaginator,
        DescribeSubscriptionFiltersPaginator,
        FilterLogEventsPaginator,
        ListAnomaliesPaginator,
        ListLogAnomalyDetectorsPaginator,
    )

    client: CloudWatchLogsClient = boto3.client("logs")

    describe_deliveries_paginator: DescribeDeliveriesPaginator = client.get_paginator("describe_deliveries")
    describe_delivery_destinations_paginator: DescribeDeliveryDestinationsPaginator = client.get_paginator("describe_delivery_destinations")
    describe_delivery_sources_paginator: DescribeDeliverySourcesPaginator = client.get_paginator("describe_delivery_sources")
    describe_destinations_paginator: DescribeDestinationsPaginator = client.get_paginator("describe_destinations")
    describe_export_tasks_paginator: DescribeExportTasksPaginator = client.get_paginator("describe_export_tasks")
    describe_log_groups_paginator: DescribeLogGroupsPaginator = client.get_paginator("describe_log_groups")
    describe_log_streams_paginator: DescribeLogStreamsPaginator = client.get_paginator("describe_log_streams")
    describe_metric_filters_paginator: DescribeMetricFiltersPaginator = client.get_paginator("describe_metric_filters")
    describe_queries_paginator: DescribeQueriesPaginator = client.get_paginator("describe_queries")
    describe_resource_policies_paginator: DescribeResourcePoliciesPaginator = client.get_paginator("describe_resource_policies")
    describe_subscription_filters_paginator: DescribeSubscriptionFiltersPaginator = client.get_paginator("describe_subscription_filters")
    filter_log_events_paginator: FilterLogEventsPaginator = client.get_paginator("filter_log_events")
    list_anomalies_paginator: ListAnomaliesPaginator = client.get_paginator("list_anomalies")
    list_log_anomaly_detectors_paginator: ListLogAnomalyDetectorsPaginator = client.get_paginator("list_log_anomaly_detectors")
    ```
"""

from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    ExportTaskStatusCodeType,
    LogGroupClassType,
    OrderByType,
    QueryStatusType,
    SuppressionStateType,
)
from .type_defs import (
    DescribeDeliveriesResponseTypeDef,
    DescribeDeliveryDestinationsResponseTypeDef,
    DescribeDeliverySourcesResponseTypeDef,
    DescribeDestinationsResponseTypeDef,
    DescribeExportTasksResponseTypeDef,
    DescribeLogGroupsResponseTypeDef,
    DescribeLogStreamsResponseTypeDef,
    DescribeMetricFiltersResponseTypeDef,
    DescribeQueriesResponseTypeDef,
    DescribeResourcePoliciesResponseTypeDef,
    DescribeSubscriptionFiltersResponseTypeDef,
    FilterLogEventsResponseTypeDef,
    ListAnomaliesResponseTypeDef,
    ListLogAnomalyDetectorsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeDeliveriesPaginator",
    "DescribeDeliveryDestinationsPaginator",
    "DescribeDeliverySourcesPaginator",
    "DescribeDestinationsPaginator",
    "DescribeExportTasksPaginator",
    "DescribeLogGroupsPaginator",
    "DescribeLogStreamsPaginator",
    "DescribeMetricFiltersPaginator",
    "DescribeQueriesPaginator",
    "DescribeResourcePoliciesPaginator",
    "DescribeSubscriptionFiltersPaginator",
    "FilterLogEventsPaginator",
    "ListAnomaliesPaginator",
    "ListLogAnomalyDetectorsPaginator",
)

class DescribeDeliveriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDeliveries)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describedeliveriespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDeliveriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDeliveries.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describedeliveriespaginator)
        """

class DescribeDeliveryDestinationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDeliveryDestinations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describedeliverydestinationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDeliveryDestinationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDeliveryDestinations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describedeliverydestinationspaginator)
        """

class DescribeDeliverySourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDeliverySources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describedeliverysourcespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDeliverySourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDeliverySources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describedeliverysourcespaginator)
        """

class DescribeDestinationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDestinations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describedestinationspaginator)
    """

    def paginate(
        self, *, DestinationNamePrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDestinationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDestinations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describedestinationspaginator)
        """

class DescribeExportTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeExportTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describeexporttaskspaginator)
    """

    def paginate(
        self,
        *,
        taskId: str = None,
        statusCode: ExportTaskStatusCodeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeExportTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeExportTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describeexporttaskspaginator)
        """

class DescribeLogGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describeloggroupspaginator)
    """

    def paginate(
        self,
        *,
        accountIdentifiers: List[str] = None,
        logGroupNamePrefix: str = None,
        logGroupNamePattern: str = None,
        includeLinkedAccounts: bool = None,
        logGroupClass: LogGroupClassType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLogGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describeloggroupspaginator)
        """

class DescribeLogStreamsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogStreams)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describelogstreamspaginator)
    """

    def paginate(
        self,
        *,
        logGroupName: str = None,
        logGroupIdentifier: str = None,
        logStreamNamePrefix: str = None,
        orderBy: OrderByType = None,
        descending: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLogStreamsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogStreams.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describelogstreamspaginator)
        """

class DescribeMetricFiltersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeMetricFilters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describemetricfilterspaginator)
    """

    def paginate(
        self,
        *,
        logGroupName: str = None,
        filterNamePrefix: str = None,
        metricName: str = None,
        metricNamespace: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMetricFiltersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeMetricFilters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describemetricfilterspaginator)
        """

class DescribeQueriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeQueries)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describequeriespaginator)
    """

    def paginate(
        self,
        *,
        logGroupName: str = None,
        status: QueryStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeQueriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeQueries.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describequeriespaginator)
        """

class DescribeResourcePoliciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeResourcePolicies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describeresourcepoliciespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeResourcePoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeResourcePolicies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describeresourcepoliciespaginator)
        """

class DescribeSubscriptionFiltersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describesubscriptionfilterspaginator)
    """

    def paginate(
        self,
        *,
        logGroupName: str,
        filterNamePrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSubscriptionFiltersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describesubscriptionfilterspaginator)
        """

class FilterLogEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.FilterLogEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#filterlogeventspaginator)
    """

    def paginate(
        self,
        *,
        logGroupName: str = None,
        logGroupIdentifier: str = None,
        logStreamNames: List[str] = None,
        logStreamNamePrefix: str = None,
        startTime: int = None,
        endTime: int = None,
        filterPattern: str = None,
        interleaved: bool = None,
        unmask: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[FilterLogEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.FilterLogEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#filterlogeventspaginator)
        """

class ListAnomaliesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.ListAnomalies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#listanomaliespaginator)
    """

    def paginate(
        self,
        *,
        anomalyDetectorArn: str = None,
        suppressionState: SuppressionStateType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAnomaliesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.ListAnomalies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#listanomaliespaginator)
        """

class ListLogAnomalyDetectorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.ListLogAnomalyDetectors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#listloganomalydetectorspaginator)
    """

    def paginate(
        self, *, filterLogGroupArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLogAnomalyDetectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/logs.html#CloudWatchLogs.Paginator.ListLogAnomalyDetectors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#listloganomalydetectorspaginator)
        """
