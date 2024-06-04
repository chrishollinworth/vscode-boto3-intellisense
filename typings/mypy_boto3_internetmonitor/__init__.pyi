"""
Main interface for internetmonitor service.

Usage::

    ```python
    import boto3
    from mypy_boto3_internetmonitor import (
        Client,
        CloudWatchInternetMonitorClient,
        ListHealthEventsPaginator,
        ListInternetEventsPaginator,
        ListMonitorsPaginator,
    )

    session = boto3.Session()

    client: CloudWatchInternetMonitorClient = boto3.client("internetmonitor")
    session_client: CloudWatchInternetMonitorClient = session.client("internetmonitor")

    list_health_events_paginator: ListHealthEventsPaginator = client.get_paginator("list_health_events")
    list_internet_events_paginator: ListInternetEventsPaginator = client.get_paginator("list_internet_events")
    list_monitors_paginator: ListMonitorsPaginator = client.get_paginator("list_monitors")
    ```
"""

from .client import CloudWatchInternetMonitorClient
from .paginator import ListHealthEventsPaginator, ListInternetEventsPaginator, ListMonitorsPaginator

Client = CloudWatchInternetMonitorClient

__all__ = (
    "Client",
    "CloudWatchInternetMonitorClient",
    "ListHealthEventsPaginator",
    "ListInternetEventsPaginator",
    "ListMonitorsPaginator",
)
