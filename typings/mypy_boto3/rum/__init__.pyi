"""
Main interface for rum service.

Usage::

    ```python
    import boto3
    from mypy_boto3_rum import (
        Client,
        CloudWatchRUMClient,
        GetAppMonitorDataPaginator,
        ListAppMonitorsPaginator,
    )

    session = boto3.Session()

    client: CloudWatchRUMClient = boto3.client("rum")
    session_client: CloudWatchRUMClient = session.client("rum")

    get_app_monitor_data_paginator: GetAppMonitorDataPaginator = client.get_paginator("get_app_monitor_data")
    list_app_monitors_paginator: ListAppMonitorsPaginator = client.get_paginator("list_app_monitors")
    ```
"""
from .client import CloudWatchRUMClient
from .paginator import GetAppMonitorDataPaginator, ListAppMonitorsPaginator

Client = CloudWatchRUMClient

__all__ = (
    "Client",
    "CloudWatchRUMClient",
    "GetAppMonitorDataPaginator",
    "ListAppMonitorsPaginator",
)
