"""
Type annotations for rum service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_rum.client import CloudWatchRUMClient
    from mypy_boto3_rum.paginator import (
        BatchGetRumMetricDefinitionsPaginator,
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    BatchGetRumMetricDefinitionsRequestPaginateTypeDef,
    BatchGetRumMetricDefinitionsResponseTypeDef,
    GetAppMonitorDataRequestPaginateTypeDef,
    GetAppMonitorDataResponseTypeDef,
    ListAppMonitorsRequestPaginateTypeDef,
    ListAppMonitorsResponseTypeDef,
    ListRumMetricsDestinationsRequestPaginateTypeDef,
    ListRumMetricsDestinationsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "BatchGetRumMetricDefinitionsPaginator",
    "GetAppMonitorDataPaginator",
    "ListAppMonitorsPaginator",
    "ListRumMetricsDestinationsPaginator",
)

if TYPE_CHECKING:
    _BatchGetRumMetricDefinitionsPaginatorBase = Paginator[
        BatchGetRumMetricDefinitionsResponseTypeDef
    ]
else:
    _BatchGetRumMetricDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class BatchGetRumMetricDefinitionsPaginator(_BatchGetRumMetricDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum/paginator/BatchGetRumMetricDefinitions.html#CloudWatchRUM.Paginator.BatchGetRumMetricDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators/#batchgetrummetricdefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[BatchGetRumMetricDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[BatchGetRumMetricDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum/paginator/BatchGetRumMetricDefinitions.html#CloudWatchRUM.Paginator.BatchGetRumMetricDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators/#batchgetrummetricdefinitionspaginator)
        """

if TYPE_CHECKING:
    _GetAppMonitorDataPaginatorBase = Paginator[GetAppMonitorDataResponseTypeDef]
else:
    _GetAppMonitorDataPaginatorBase = Paginator  # type: ignore[assignment]

class GetAppMonitorDataPaginator(_GetAppMonitorDataPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum/paginator/GetAppMonitorData.html#CloudWatchRUM.Paginator.GetAppMonitorData)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators/#getappmonitordatapaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAppMonitorDataRequestPaginateTypeDef]
    ) -> PageIterator[GetAppMonitorDataResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum/paginator/GetAppMonitorData.html#CloudWatchRUM.Paginator.GetAppMonitorData.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators/#getappmonitordatapaginator)
        """

if TYPE_CHECKING:
    _ListAppMonitorsPaginatorBase = Paginator[ListAppMonitorsResponseTypeDef]
else:
    _ListAppMonitorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAppMonitorsPaginator(_ListAppMonitorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum/paginator/ListAppMonitors.html#CloudWatchRUM.Paginator.ListAppMonitors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators/#listappmonitorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAppMonitorsRequestPaginateTypeDef]
    ) -> PageIterator[ListAppMonitorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum/paginator/ListAppMonitors.html#CloudWatchRUM.Paginator.ListAppMonitors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators/#listappmonitorspaginator)
        """

if TYPE_CHECKING:
    _ListRumMetricsDestinationsPaginatorBase = Paginator[ListRumMetricsDestinationsResponseTypeDef]
else:
    _ListRumMetricsDestinationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRumMetricsDestinationsPaginator(_ListRumMetricsDestinationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum/paginator/ListRumMetricsDestinations.html#CloudWatchRUM.Paginator.ListRumMetricsDestinations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators/#listrummetricsdestinationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRumMetricsDestinationsRequestPaginateTypeDef]
    ) -> PageIterator[ListRumMetricsDestinationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rum/paginator/ListRumMetricsDestinations.html#CloudWatchRUM.Paginator.ListRumMetricsDestinations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators/#listrummetricsdestinationspaginator)
        """
