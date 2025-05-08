"""
Type annotations for networkmonitor service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_networkmonitor.client import CloudWatchNetworkMonitorClient
    from mypy_boto3_networkmonitor.paginator import (
        ListMonitorsPaginator,
    )

    session = Session()
    client: CloudWatchNetworkMonitorClient = session.client("networkmonitor")

    list_monitors_paginator: ListMonitorsPaginator = client.get_paginator("list_monitors")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListMonitorsInputPaginateTypeDef, ListMonitorsOutputTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListMonitorsPaginator",)

if TYPE_CHECKING:
    _ListMonitorsPaginatorBase = Paginator[ListMonitorsOutputTypeDef]
else:
    _ListMonitorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMonitorsPaginator(_ListMonitorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/paginator/ListMonitors.html#CloudWatchNetworkMonitor.Paginator.ListMonitors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/paginators/#listmonitorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMonitorsInputPaginateTypeDef]
    ) -> PageIterator[ListMonitorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/networkmonitor/paginator/ListMonitors.html#CloudWatchNetworkMonitor.Paginator.ListMonitors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/paginators/#listmonitorspaginator)
        """
