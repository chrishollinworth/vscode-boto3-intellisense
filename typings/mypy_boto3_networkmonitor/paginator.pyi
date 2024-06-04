"""
Type annotations for networkmonitor service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_networkmonitor import CloudWatchNetworkMonitorClient
    from mypy_boto3_networkmonitor.paginator import (
        ListMonitorsPaginator,
    )

    client: CloudWatchNetworkMonitorClient = boto3.client("networkmonitor")

    list_monitors_paginator: ListMonitorsPaginator = client.get_paginator("list_monitors")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListMonitorsOutputTypeDef, PaginatorConfigTypeDef

__all__ = ("ListMonitorsPaginator",)

class ListMonitorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Paginator.ListMonitors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/paginators.html#listmonitorspaginator)
    """

    def paginate(
        self, *, state: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMonitorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/networkmonitor.html#CloudWatchNetworkMonitor.Paginator.ListMonitors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/paginators.html#listmonitorspaginator)
        """
