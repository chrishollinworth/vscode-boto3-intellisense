"""
Type annotations for logs service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_logs.client import CloudWatchLogsClient
    from mypy_boto3_logs.paginator import (
        DescribeConfigurationTemplatesPaginator,
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
        GetScheduledQueryHistoryPaginator,
        ListAggregateLogGroupSummariesPaginator,
        ListAnomaliesPaginator,
        ListLogAnomalyDetectorsPaginator,
        ListLogGroupsForQueryPaginator,
        ListScheduledQueriesPaginator,
        ListSourcesForS3TableIntegrationPaginator,
    )

    session = Session()
    client: CloudWatchLogsClient = session.client("logs")

    describe_configuration_templates_paginator: DescribeConfigurationTemplatesPaginator = client.get_paginator("describe_configuration_templates")
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
    get_scheduled_query_history_paginator: GetScheduledQueryHistoryPaginator = client.get_paginator("get_scheduled_query_history")
    list_aggregate_log_group_summaries_paginator: ListAggregateLogGroupSummariesPaginator = client.get_paginator("list_aggregate_log_group_summaries")
    list_anomalies_paginator: ListAnomaliesPaginator = client.get_paginator("list_anomalies")
    list_log_anomaly_detectors_paginator: ListLogAnomalyDetectorsPaginator = client.get_paginator("list_log_anomaly_detectors")
    list_log_groups_for_query_paginator: ListLogGroupsForQueryPaginator = client.get_paginator("list_log_groups_for_query")
    list_scheduled_queries_paginator: ListScheduledQueriesPaginator = client.get_paginator("list_scheduled_queries")
    list_sources_for_s3_table_integration_paginator: ListSourcesForS3TableIntegrationPaginator = client.get_paginator("list_sources_for_s3_table_integration")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeConfigurationTemplatesRequestPaginateTypeDef,
    DescribeConfigurationTemplatesResponseTypeDef,
    DescribeDeliveriesRequestPaginateTypeDef,
    DescribeDeliveriesResponseTypeDef,
    DescribeDeliveryDestinationsRequestPaginateTypeDef,
    DescribeDeliveryDestinationsResponseTypeDef,
    DescribeDeliverySourcesRequestPaginateTypeDef,
    DescribeDeliverySourcesResponseTypeDef,
    DescribeDestinationsRequestPaginateTypeDef,
    DescribeDestinationsResponseTypeDef,
    DescribeExportTasksRequestPaginateTypeDef,
    DescribeExportTasksResponseTypeDef,
    DescribeLogGroupsRequestPaginateTypeDef,
    DescribeLogGroupsResponseTypeDef,
    DescribeLogStreamsRequestPaginateTypeDef,
    DescribeLogStreamsResponseTypeDef,
    DescribeMetricFiltersRequestPaginateTypeDef,
    DescribeMetricFiltersResponseTypeDef,
    DescribeQueriesRequestPaginateTypeDef,
    DescribeQueriesResponseTypeDef,
    DescribeResourcePoliciesRequestPaginateTypeDef,
    DescribeResourcePoliciesResponseTypeDef,
    DescribeSubscriptionFiltersRequestPaginateTypeDef,
    DescribeSubscriptionFiltersResponseTypeDef,
    FilterLogEventsRequestPaginateTypeDef,
    FilterLogEventsResponseTypeDef,
    GetScheduledQueryHistoryRequestPaginateTypeDef,
    GetScheduledQueryHistoryResponseTypeDef,
    ListAggregateLogGroupSummariesRequestPaginateTypeDef,
    ListAggregateLogGroupSummariesResponseTypeDef,
    ListAnomaliesRequestPaginateTypeDef,
    ListAnomaliesResponseTypeDef,
    ListLogAnomalyDetectorsRequestPaginateTypeDef,
    ListLogAnomalyDetectorsResponseTypeDef,
    ListLogGroupsForQueryRequestPaginateTypeDef,
    ListLogGroupsForQueryResponseTypeDef,
    ListScheduledQueriesRequestPaginateTypeDef,
    ListScheduledQueriesResponseTypeDef,
    ListSourcesForS3TableIntegrationRequestPaginateTypeDef,
    ListSourcesForS3TableIntegrationResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeConfigurationTemplatesPaginator",
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
    "GetScheduledQueryHistoryPaginator",
    "ListAggregateLogGroupSummariesPaginator",
    "ListAnomaliesPaginator",
    "ListLogAnomalyDetectorsPaginator",
    "ListLogGroupsForQueryPaginator",
    "ListScheduledQueriesPaginator",
    "ListSourcesForS3TableIntegrationPaginator",
)

if TYPE_CHECKING:
    _DescribeConfigurationTemplatesPaginatorBase = Paginator[
        DescribeConfigurationTemplatesResponseTypeDef
    ]
else:
    _DescribeConfigurationTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeConfigurationTemplatesPaginator(_DescribeConfigurationTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeConfigurationTemplates.html#CloudWatchLogs.Paginator.DescribeConfigurationTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describeconfigurationtemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeConfigurationTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeConfigurationTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeConfigurationTemplates.html#CloudWatchLogs.Paginator.DescribeConfigurationTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describeconfigurationtemplatespaginator)
        """

if TYPE_CHECKING:
    _DescribeDeliveriesPaginatorBase = Paginator[DescribeDeliveriesResponseTypeDef]
else:
    _DescribeDeliveriesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDeliveriesPaginator(_DescribeDeliveriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeDeliveries.html#CloudWatchLogs.Paginator.DescribeDeliveries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describedeliveriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDeliveriesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDeliveriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeDeliveries.html#CloudWatchLogs.Paginator.DescribeDeliveries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describedeliveriespaginator)
        """

if TYPE_CHECKING:
    _DescribeDeliveryDestinationsPaginatorBase = Paginator[
        DescribeDeliveryDestinationsResponseTypeDef
    ]
else:
    _DescribeDeliveryDestinationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDeliveryDestinationsPaginator(_DescribeDeliveryDestinationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeDeliveryDestinations.html#CloudWatchLogs.Paginator.DescribeDeliveryDestinations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describedeliverydestinationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDeliveryDestinationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDeliveryDestinationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeDeliveryDestinations.html#CloudWatchLogs.Paginator.DescribeDeliveryDestinations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describedeliverydestinationspaginator)
        """

if TYPE_CHECKING:
    _DescribeDeliverySourcesPaginatorBase = Paginator[DescribeDeliverySourcesResponseTypeDef]
else:
    _DescribeDeliverySourcesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDeliverySourcesPaginator(_DescribeDeliverySourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeDeliverySources.html#CloudWatchLogs.Paginator.DescribeDeliverySources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describedeliverysourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDeliverySourcesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDeliverySourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeDeliverySources.html#CloudWatchLogs.Paginator.DescribeDeliverySources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describedeliverysourcespaginator)
        """

if TYPE_CHECKING:
    _DescribeDestinationsPaginatorBase = Paginator[DescribeDestinationsResponseTypeDef]
else:
    _DescribeDestinationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDestinationsPaginator(_DescribeDestinationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeDestinations.html#CloudWatchLogs.Paginator.DescribeDestinations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describedestinationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDestinationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDestinationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeDestinations.html#CloudWatchLogs.Paginator.DescribeDestinations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describedestinationspaginator)
        """

if TYPE_CHECKING:
    _DescribeExportTasksPaginatorBase = Paginator[DescribeExportTasksResponseTypeDef]
else:
    _DescribeExportTasksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeExportTasksPaginator(_DescribeExportTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeExportTasks.html#CloudWatchLogs.Paginator.DescribeExportTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describeexporttaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeExportTasksRequestPaginateTypeDef]
    ) -> PageIterator[DescribeExportTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeExportTasks.html#CloudWatchLogs.Paginator.DescribeExportTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describeexporttaskspaginator)
        """

if TYPE_CHECKING:
    _DescribeLogGroupsPaginatorBase = Paginator[DescribeLogGroupsResponseTypeDef]
else:
    _DescribeLogGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLogGroupsPaginator(_DescribeLogGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeLogGroups.html#CloudWatchLogs.Paginator.DescribeLogGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describeloggroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLogGroupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeLogGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeLogGroups.html#CloudWatchLogs.Paginator.DescribeLogGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describeloggroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeLogStreamsPaginatorBase = Paginator[DescribeLogStreamsResponseTypeDef]
else:
    _DescribeLogStreamsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLogStreamsPaginator(_DescribeLogStreamsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeLogStreams.html#CloudWatchLogs.Paginator.DescribeLogStreams)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describelogstreamspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLogStreamsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeLogStreamsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeLogStreams.html#CloudWatchLogs.Paginator.DescribeLogStreams.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describelogstreamspaginator)
        """

if TYPE_CHECKING:
    _DescribeMetricFiltersPaginatorBase = Paginator[DescribeMetricFiltersResponseTypeDef]
else:
    _DescribeMetricFiltersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMetricFiltersPaginator(_DescribeMetricFiltersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeMetricFilters.html#CloudWatchLogs.Paginator.DescribeMetricFilters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describemetricfilterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMetricFiltersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeMetricFiltersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeMetricFilters.html#CloudWatchLogs.Paginator.DescribeMetricFilters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describemetricfilterspaginator)
        """

if TYPE_CHECKING:
    _DescribeQueriesPaginatorBase = Paginator[DescribeQueriesResponseTypeDef]
else:
    _DescribeQueriesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeQueriesPaginator(_DescribeQueriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeQueries.html#CloudWatchLogs.Paginator.DescribeQueries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describequeriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeQueriesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeQueriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeQueries.html#CloudWatchLogs.Paginator.DescribeQueries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describequeriespaginator)
        """

if TYPE_CHECKING:
    _DescribeResourcePoliciesPaginatorBase = Paginator[DescribeResourcePoliciesResponseTypeDef]
else:
    _DescribeResourcePoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeResourcePoliciesPaginator(_DescribeResourcePoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeResourcePolicies.html#CloudWatchLogs.Paginator.DescribeResourcePolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describeresourcepoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeResourcePoliciesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeResourcePoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeResourcePolicies.html#CloudWatchLogs.Paginator.DescribeResourcePolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describeresourcepoliciespaginator)
        """

if TYPE_CHECKING:
    _DescribeSubscriptionFiltersPaginatorBase = Paginator[
        DescribeSubscriptionFiltersResponseTypeDef
    ]
else:
    _DescribeSubscriptionFiltersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSubscriptionFiltersPaginator(_DescribeSubscriptionFiltersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeSubscriptionFilters.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describesubscriptionfilterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSubscriptionFiltersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSubscriptionFiltersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/DescribeSubscriptionFilters.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#describesubscriptionfilterspaginator)
        """

if TYPE_CHECKING:
    _FilterLogEventsPaginatorBase = Paginator[FilterLogEventsResponseTypeDef]
else:
    _FilterLogEventsPaginatorBase = Paginator  # type: ignore[assignment]

class FilterLogEventsPaginator(_FilterLogEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/FilterLogEvents.html#CloudWatchLogs.Paginator.FilterLogEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#filterlogeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[FilterLogEventsRequestPaginateTypeDef]
    ) -> PageIterator[FilterLogEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/FilterLogEvents.html#CloudWatchLogs.Paginator.FilterLogEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#filterlogeventspaginator)
        """

if TYPE_CHECKING:
    _GetScheduledQueryHistoryPaginatorBase = Paginator[GetScheduledQueryHistoryResponseTypeDef]
else:
    _GetScheduledQueryHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class GetScheduledQueryHistoryPaginator(_GetScheduledQueryHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/GetScheduledQueryHistory.html#CloudWatchLogs.Paginator.GetScheduledQueryHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#getscheduledqueryhistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetScheduledQueryHistoryRequestPaginateTypeDef]
    ) -> PageIterator[GetScheduledQueryHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/GetScheduledQueryHistory.html#CloudWatchLogs.Paginator.GetScheduledQueryHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#getscheduledqueryhistorypaginator)
        """

if TYPE_CHECKING:
    _ListAggregateLogGroupSummariesPaginatorBase = Paginator[
        ListAggregateLogGroupSummariesResponseTypeDef
    ]
else:
    _ListAggregateLogGroupSummariesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAggregateLogGroupSummariesPaginator(_ListAggregateLogGroupSummariesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/ListAggregateLogGroupSummaries.html#CloudWatchLogs.Paginator.ListAggregateLogGroupSummaries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#listaggregateloggroupsummariespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAggregateLogGroupSummariesRequestPaginateTypeDef]
    ) -> PageIterator[ListAggregateLogGroupSummariesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/ListAggregateLogGroupSummaries.html#CloudWatchLogs.Paginator.ListAggregateLogGroupSummaries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#listaggregateloggroupsummariespaginator)
        """

if TYPE_CHECKING:
    _ListAnomaliesPaginatorBase = Paginator[ListAnomaliesResponseTypeDef]
else:
    _ListAnomaliesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAnomaliesPaginator(_ListAnomaliesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/ListAnomalies.html#CloudWatchLogs.Paginator.ListAnomalies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#listanomaliespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAnomaliesRequestPaginateTypeDef]
    ) -> PageIterator[ListAnomaliesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/ListAnomalies.html#CloudWatchLogs.Paginator.ListAnomalies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#listanomaliespaginator)
        """

if TYPE_CHECKING:
    _ListLogAnomalyDetectorsPaginatorBase = Paginator[ListLogAnomalyDetectorsResponseTypeDef]
else:
    _ListLogAnomalyDetectorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListLogAnomalyDetectorsPaginator(_ListLogAnomalyDetectorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/ListLogAnomalyDetectors.html#CloudWatchLogs.Paginator.ListLogAnomalyDetectors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#listloganomalydetectorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLogAnomalyDetectorsRequestPaginateTypeDef]
    ) -> PageIterator[ListLogAnomalyDetectorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/ListLogAnomalyDetectors.html#CloudWatchLogs.Paginator.ListLogAnomalyDetectors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#listloganomalydetectorspaginator)
        """

if TYPE_CHECKING:
    _ListLogGroupsForQueryPaginatorBase = Paginator[ListLogGroupsForQueryResponseTypeDef]
else:
    _ListLogGroupsForQueryPaginatorBase = Paginator  # type: ignore[assignment]

class ListLogGroupsForQueryPaginator(_ListLogGroupsForQueryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/ListLogGroupsForQuery.html#CloudWatchLogs.Paginator.ListLogGroupsForQuery)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#listloggroupsforquerypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListLogGroupsForQueryRequestPaginateTypeDef]
    ) -> PageIterator[ListLogGroupsForQueryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/ListLogGroupsForQuery.html#CloudWatchLogs.Paginator.ListLogGroupsForQuery.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#listloggroupsforquerypaginator)
        """

if TYPE_CHECKING:
    _ListScheduledQueriesPaginatorBase = Paginator[ListScheduledQueriesResponseTypeDef]
else:
    _ListScheduledQueriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListScheduledQueriesPaginator(_ListScheduledQueriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/ListScheduledQueries.html#CloudWatchLogs.Paginator.ListScheduledQueries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#listscheduledqueriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListScheduledQueriesRequestPaginateTypeDef]
    ) -> PageIterator[ListScheduledQueriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/ListScheduledQueries.html#CloudWatchLogs.Paginator.ListScheduledQueries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#listscheduledqueriespaginator)
        """

if TYPE_CHECKING:
    _ListSourcesForS3TableIntegrationPaginatorBase = Paginator[
        ListSourcesForS3TableIntegrationResponseTypeDef
    ]
else:
    _ListSourcesForS3TableIntegrationPaginatorBase = Paginator  # type: ignore[assignment]

class ListSourcesForS3TableIntegrationPaginator(_ListSourcesForS3TableIntegrationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/ListSourcesForS3TableIntegration.html#CloudWatchLogs.Paginator.ListSourcesForS3TableIntegration)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#listsourcesfors3tableintegrationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSourcesForS3TableIntegrationRequestPaginateTypeDef]
    ) -> PageIterator[ListSourcesForS3TableIntegrationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/paginator/ListSourcesForS3TableIntegration.html#CloudWatchLogs.Paginator.ListSourcesForS3TableIntegration.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators/#listsourcesfors3tableintegrationpaginator)
        """
