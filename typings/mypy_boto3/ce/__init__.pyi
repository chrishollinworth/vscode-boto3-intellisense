"""
Main interface for ce service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ce/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ce import (
        Client,
        CostExplorerClient,
        GetAnomaliesPaginator,
        GetAnomalyMonitorsPaginator,
        GetAnomalySubscriptionsPaginator,
    )

    session = Session()
    client: CostExplorerClient = session.client("ce")

    get_anomalies_paginator: GetAnomaliesPaginator = client.get_paginator("get_anomalies")
    get_anomaly_monitors_paginator: GetAnomalyMonitorsPaginator = client.get_paginator("get_anomaly_monitors")
    get_anomaly_subscriptions_paginator: GetAnomalySubscriptionsPaginator = client.get_paginator("get_anomaly_subscriptions")
    ```
"""

from .client import CostExplorerClient
from .paginator import (
    GetAnomaliesPaginator,
    GetAnomalyMonitorsPaginator,
    GetAnomalySubscriptionsPaginator,
)

Client = CostExplorerClient

__all__ = (
    "Client",
    "CostExplorerClient",
    "GetAnomaliesPaginator",
    "GetAnomalyMonitorsPaginator",
    "GetAnomalySubscriptionsPaginator",
)
