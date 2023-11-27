"""
Type annotations for internetmonitor service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_internetmonitor import CloudWatchInternetMonitorClient
    from mypy_boto3_internetmonitor.paginator import (
        ListHealthEventsPaginator,
        ListMonitorsPaginator,
    )

    client: CloudWatchInternetMonitorClient = boto3.client("internetmonitor")

    list_health_events_paginator: ListHealthEventsPaginator = client.get_paginator("list_health_events")
    list_monitors_paginator: ListMonitorsPaginator = client.get_paginator("list_monitors")
    ```
"""
from datetime import datetime
from typing import Iterator, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import HealthEventStatusType
from .type_defs import (
    ListHealthEventsOutputTypeDef,
    ListMonitorsOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListHealthEventsPaginator", "ListMonitorsPaginator")

class ListHealthEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Paginator.ListHealthEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators.html#listhealtheventspaginator)
    """

    def paginate(
        self,
        *,
        MonitorName: str,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        EventStatus: HealthEventStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHealthEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Paginator.ListHealthEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators.html#listhealtheventspaginator)
        """

class ListMonitorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Paginator.ListMonitors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators.html#listmonitorspaginator)
    """

    def paginate(
        self, *, MonitorStatus: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMonitorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Paginator.ListMonitors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators.html#listmonitorspaginator)
        """
