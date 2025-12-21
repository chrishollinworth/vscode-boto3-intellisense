"""
Main interface for logs service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_logs import (
        Client,
        CloudWatchLogsClient,
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

from .client import CloudWatchLogsClient
from .paginator import (
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

Client = CloudWatchLogsClient

__all__ = (
    "Client",
    "CloudWatchLogsClient",
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
