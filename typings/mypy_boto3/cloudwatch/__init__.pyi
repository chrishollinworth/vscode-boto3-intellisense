"""
Main interface for cloudwatch service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cloudwatch import (
        AlarmExistsWaiter,
        Client,
        CloudWatchClient,
        CloudWatchServiceResource,
        CompositeAlarmExistsWaiter,
        DescribeAlarmHistoryPaginator,
        DescribeAlarmsPaginator,
        DescribeAnomalyDetectorsPaginator,
        GetMetricDataPaginator,
        ListDashboardsPaginator,
        ListMetricsPaginator,
        ServiceResource,
    )

    session = Session()
    client: CloudWatchClient = session.client("cloudwatch")

    resource: CloudWatchServiceResource = session.resource("cloudwatch")

    alarm_exists_waiter: AlarmExistsWaiter = client.get_waiter("alarm_exists")
    composite_alarm_exists_waiter: CompositeAlarmExistsWaiter = client.get_waiter("composite_alarm_exists")

    describe_alarm_history_paginator: DescribeAlarmHistoryPaginator = client.get_paginator("describe_alarm_history")
    describe_alarms_paginator: DescribeAlarmsPaginator = client.get_paginator("describe_alarms")
    describe_anomaly_detectors_paginator: DescribeAnomalyDetectorsPaginator = client.get_paginator("describe_anomaly_detectors")
    get_metric_data_paginator: GetMetricDataPaginator = client.get_paginator("get_metric_data")
    list_dashboards_paginator: ListDashboardsPaginator = client.get_paginator("list_dashboards")
    list_metrics_paginator: ListMetricsPaginator = client.get_paginator("list_metrics")
    ```
"""

from .client import CloudWatchClient
from .paginator import (
    DescribeAlarmHistoryPaginator,
    DescribeAlarmsPaginator,
    DescribeAnomalyDetectorsPaginator,
    GetMetricDataPaginator,
    ListDashboardsPaginator,
    ListMetricsPaginator,
)
from .waiter import AlarmExistsWaiter, CompositeAlarmExistsWaiter

try:
    from .service_resource import CloudWatchServiceResource
except ImportError:
    from builtins import object as CloudWatchServiceResource  # type: ignore[assignment]

Client = CloudWatchClient

ServiceResource = CloudWatchServiceResource

__all__ = (
    "AlarmExistsWaiter",
    "Client",
    "CloudWatchClient",
    "CloudWatchServiceResource",
    "CompositeAlarmExistsWaiter",
    "DescribeAlarmHistoryPaginator",
    "DescribeAlarmsPaginator",
    "DescribeAnomalyDetectorsPaginator",
    "GetMetricDataPaginator",
    "ListDashboardsPaginator",
    "ListMetricsPaginator",
    "ServiceResource",
)
