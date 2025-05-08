"""
Type annotations for internetmonitor service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_internetmonitor.client import CloudWatchInternetMonitorClient
    from mypy_boto3_internetmonitor.paginator import (
        ListHealthEventsPaginator,
        ListInternetEventsPaginator,
        ListMonitorsPaginator,
    )

    session = Session()
    client: CloudWatchInternetMonitorClient = session.client("internetmonitor")

    list_health_events_paginator: ListHealthEventsPaginator = client.get_paginator("list_health_events")
    list_internet_events_paginator: ListInternetEventsPaginator = client.get_paginator("list_internet_events")
    list_monitors_paginator: ListMonitorsPaginator = client.get_paginator("list_monitors")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListHealthEventsInputPaginateTypeDef,
    ListHealthEventsOutputTypeDef,
    ListInternetEventsInputPaginateTypeDef,
    ListInternetEventsOutputTypeDef,
    ListMonitorsInputPaginateTypeDef,
    ListMonitorsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListHealthEventsPaginator", "ListInternetEventsPaginator", "ListMonitorsPaginator")

if TYPE_CHECKING:
    _ListHealthEventsPaginatorBase = Paginator[ListHealthEventsOutputTypeDef]
else:
    _ListHealthEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListHealthEventsPaginator(_ListHealthEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/paginator/ListHealthEvents.html#CloudWatchInternetMonitor.Paginator.ListHealthEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators/#listhealtheventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListHealthEventsInputPaginateTypeDef]
    ) -> PageIterator[ListHealthEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/paginator/ListHealthEvents.html#CloudWatchInternetMonitor.Paginator.ListHealthEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators/#listhealtheventspaginator)
        """

if TYPE_CHECKING:
    _ListInternetEventsPaginatorBase = Paginator[ListInternetEventsOutputTypeDef]
else:
    _ListInternetEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListInternetEventsPaginator(_ListInternetEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/paginator/ListInternetEvents.html#CloudWatchInternetMonitor.Paginator.ListInternetEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators/#listinterneteventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInternetEventsInputPaginateTypeDef]
    ) -> PageIterator[ListInternetEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/paginator/ListInternetEvents.html#CloudWatchInternetMonitor.Paginator.ListInternetEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators/#listinterneteventspaginator)
        """

if TYPE_CHECKING:
    _ListMonitorsPaginatorBase = Paginator[ListMonitorsOutputTypeDef]
else:
    _ListMonitorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMonitorsPaginator(_ListMonitorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/paginator/ListMonitors.html#CloudWatchInternetMonitor.Paginator.ListMonitors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators/#listmonitorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMonitorsInputPaginateTypeDef]
    ) -> PageIterator[ListMonitorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/internetmonitor/paginator/ListMonitors.html#CloudWatchInternetMonitor.Paginator.ListMonitors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/paginators/#listmonitorspaginator)
        """
