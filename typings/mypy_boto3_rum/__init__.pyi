"""
Main interface for rum service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_rum import (
        BatchGetRumMetricDefinitionsPaginator,
        Client,
        CloudWatchRUMClient,
        GetAppMonitorDataPaginator,
        ListAppMonitorsPaginator,
        ListRumMetricsDestinationsPaginator,
    )

    session = Session()
    client: CloudWatchRUMClient = session.client("rum")

    batch_get_rum_metric_definitions_paginator: BatchGetRumMetricDefinitionsPaginator = client.get_paginator("batch_get_rum_metric_definitions")
    get_app_monitor_data_paginator: GetAppMonitorDataPaginator = client.get_paginator("get_app_monitor_data")
    list_app_monitors_paginator: ListAppMonitorsPaginator = client.get_paginator("list_app_monitors")
    list_rum_metrics_destinations_paginator: ListRumMetricsDestinationsPaginator = client.get_paginator("list_rum_metrics_destinations")
    ```
"""

from .client import CloudWatchRUMClient
from .paginator import (
    BatchGetRumMetricDefinitionsPaginator,
    GetAppMonitorDataPaginator,
    ListAppMonitorsPaginator,
    ListRumMetricsDestinationsPaginator,
)

Client = CloudWatchRUMClient

__all__ = (
    "BatchGetRumMetricDefinitionsPaginator",
    "Client",
    "CloudWatchRUMClient",
    "GetAppMonitorDataPaginator",
    "ListAppMonitorsPaginator",
    "ListRumMetricsDestinationsPaginator",
)
