"""
Type annotations for rum service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_rum import CloudWatchRUMClient
    from mypy_boto3_rum.paginator import (
        GetAppMonitorDataPaginator,
        ListAppMonitorsPaginator,
    )

    client: CloudWatchRUMClient = boto3.client("rum")

    get_app_monitor_data_paginator: GetAppMonitorDataPaginator = client.get_paginator("get_app_monitor_data")
    list_app_monitors_paginator: ListAppMonitorsPaginator = client.get_paginator("list_app_monitors")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    GetAppMonitorDataResponseTypeDef,
    ListAppMonitorsResponseTypeDef,
    PaginatorConfigTypeDef,
    QueryFilterTypeDef,
    TimeRangeTypeDef,
)

__all__ = ("GetAppMonitorDataPaginator", "ListAppMonitorsPaginator")

class GetAppMonitorDataPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/rum.html#CloudWatchRUM.Paginator.GetAppMonitorData)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/rum.html#CloudWatchRUM.Paginator.GetAppMonitorData.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#getappmonitordatapaginator)
        """

class ListAppMonitorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/rum.html#CloudWatchRUM.Paginator.ListAppMonitors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#listappmonitorspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAppMonitorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/rum.html#CloudWatchRUM.Paginator.ListAppMonitors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rum/paginators.html#listappmonitorspaginator)
        """
