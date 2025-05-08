"""
Main interface for networkmonitor service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_networkmonitor import (
        Client,
        CloudWatchNetworkMonitorClient,
        ListMonitorsPaginator,
    )

    session = Session()
    client: CloudWatchNetworkMonitorClient = session.client("networkmonitor")

    list_monitors_paginator: ListMonitorsPaginator = client.get_paginator("list_monitors")
    ```
"""

from .client import CloudWatchNetworkMonitorClient
from .paginator import ListMonitorsPaginator

Client = CloudWatchNetworkMonitorClient

__all__ = ("Client", "CloudWatchNetworkMonitorClient", "ListMonitorsPaginator")
