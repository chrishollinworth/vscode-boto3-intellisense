"""
Type annotations for rum service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_rum import CloudWatchRUMClient
    from mypy_boto3_rum.paginator import (
        BatchGetRumMetricDefinitionsPaginator,
        GetAppMonitorDataPaginator,
        ListAppMonitorsPaginator,
        ListRumMetricsDestinationsPaginator,
    )

    client: CloudWatchRUMClient = boto3.client("rum")

    batch_get_rum_metric_definitions_paginator: BatchGetRumMetricDefinitionsPaginator = client.get_paginator("batch_get_rum_metric_definitions")
    get_app_monitor_data_paginator: GetAppMonitorDataPaginator = client.get_paginator("get_app_monitor_data")
    list_app_monitors_paginator: ListAppMonitorsPaginator = client.get_paginator("list_app_monitors")
    list_rum_metrics_destinations_paginator: ListRumMetricsDestinationsPaginator = client.get_paginator("list_rum_metrics_destinations")
    ```
"""

from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import MetricDestinationType
from .type_defs import (
    BatchGetRumMetricDefinitionsResponseTypeDef,
    GetAppMonitorDataResponseTypeDef,
    ListAppMonitorsResponseTypeDef,
    ListRumMetricsDestinationsResponseTypeDef,
    PaginatorConfigTypeDef,
    QueryFilterTypeDef,
    TimeRangeTypeDef,
)

__all__ = (
    "BatchGetRumMetricDefinitionsPaginator",
    "GetAppMonitorDataPaginator",
    "ListAppMonitorsPaginator",
    "ListRumMetricsDestinationsPaginator",
)

class BatchGetRumMetricDefinitionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/rum.html#CloudWatchRUM.Paginator.BatchGetRumMetricDefinitions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#batchgetrummetricdefinitionspaginator)
    """

    def paginate(
        self,
        *,
        AppMonitorName: str,
        Destination: MetricDestinationType,
        DestinationArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[BatchGetRumMetricDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/rum.html#CloudWatchRUM.Paginator.BatchGetRumMetricDefinitions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#batchgetrummetricdefinitionspaginator)
        """

class GetAppMonitorDataPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/rum.html#CloudWatchRUM.Paginator.GetAppMonitorData)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#getappmonitordatapaginator)
    """

    def paginate(
        self,
        *,
        Name: str,
        TimeRange: "TimeRangeTypeDef",
        Filters: List["QueryFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetAppMonitorDataResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/rum.html#CloudWatchRUM.Paginator.GetAppMonitorData.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#getappmonitordatapaginator)
        """

class ListAppMonitorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/rum.html#CloudWatchRUM.Paginator.ListAppMonitors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#listappmonitorspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAppMonitorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/rum.html#CloudWatchRUM.Paginator.ListAppMonitors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#listappmonitorspaginator)
        """

class ListRumMetricsDestinationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/rum.html#CloudWatchRUM.Paginator.ListRumMetricsDestinations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#listrummetricsdestinationspaginator)
    """

    def paginate(
        self, *, AppMonitorName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRumMetricsDestinationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/rum.html#CloudWatchRUM.Paginator.ListRumMetricsDestinations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#listrummetricsdestinationspaginator)
        """
