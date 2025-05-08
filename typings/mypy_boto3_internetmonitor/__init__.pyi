"""
Main interface for internetmonitor service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_internetmonitor/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_internetmonitor import (
        Client,
        CloudWatchInternetMonitorClient,
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
