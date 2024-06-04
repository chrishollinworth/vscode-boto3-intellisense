"""
Main interface for networkmonitor service.

Usage::

    ```python
    import boto3
    from mypy_boto3_networkmonitor import (
        Client,
        CloudWatchNetworkMonitorClient,
        ListMonitorsPaginator,
    )

    session = boto3.Session()

    client: CloudWatchNetworkMonitorClient = boto3.client("networkmonitor")
    session_client: CloudWatchNetworkMonitorClient = session.client("networkmonitor")

    list_monitors_paginator: ListMonitorsPaginator = client.get_paginator("list_monitors")
    ```
"""

from .client import CloudWatchNetworkMonitorClient
from .paginator import ListMonitorsPaginator

Client = CloudWatchNetworkMonitorClient

__all__ = ("Client", "CloudWatchNetworkMonitorClient", "ListMonitorsPaginator")
