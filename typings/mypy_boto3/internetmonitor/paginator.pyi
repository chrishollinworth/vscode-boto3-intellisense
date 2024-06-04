"""
Type annotations for internetmonitor service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_internetmonitor import CloudWatchInternetMonitorClient
    from mypy_boto3_internetmonitor.paginator import (
        ListHealthEventsPaginator,
        ListInternetEventsPaginator,
        ListMonitorsPaginator,
    )

    client: CloudWatchInternetMonitorClient = boto3.client("internetmonitor")

    list_health_events_paginator: ListHealthEventsPaginator = client.get_paginator("list_health_events")
    list_internet_events_paginator: ListInternetEventsPaginator = client.get_paginator("list_internet_events")
    list_monitors_paginator: ListMonitorsPaginator = client.get_paginator("list_monitors")
    ```
"""

from datetime import datetime
from typing import Iterator, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import HealthEventStatusType
from .type_defs import (
    ListHealthEventsOutputTypeDef,
    ListInternetEventsOutputTypeDef,
    ListMonitorsOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListHealthEventsPaginator", "ListInternetEventsPaginator", "ListMonitorsPaginator")

class ListHealthEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Paginator.ListHealthEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators.html#listhealtheventspaginator)
    """

    def paginate(
        self,
        *,
        MonitorName: str,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        EventStatus: HealthEventStatusType = None,
        LinkedAccountId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHealthEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Paginator.ListHealthEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators.html#listhealtheventspaginator)
        """

class ListInternetEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Paginator.ListInternetEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators.html#listinterneteventspaginator)
    """

    def paginate(
        self,
        *,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        EventStatus: str = None,
        EventType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInternetEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Paginator.ListInternetEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators.html#listinterneteventspaginator)
        """

class ListMonitorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Paginator.ListMonitors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators.html#listmonitorspaginator)
    """

    def paginate(
        self,
        *,
        MonitorStatus: str = None,
        IncludeLinkedAccounts: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMonitorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/internetmonitor.html#CloudWatchInternetMonitor.Paginator.ListMonitors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators.html#listmonitorspaginator)
        """
