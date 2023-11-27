"""
Main interface for controltower service.

Usage::

    ```python
    import boto3
    from mypy_boto3_controltower import (
        Client,
        ControlTowerClient,
        ListEnabledControlsPaginator,
        ListLandingZonesPaginator,
    )

    session = boto3.Session()

    client: ControlTowerClient = boto3.client("controltower")
    session_client: ControlTowerClient = session.client("controltower")

    list_enabled_controls_paginator: ListEnabledControlsPaginator = client.get_paginator("list_enabled_controls")
    list_landing_zones_paginator: ListLandingZonesPaginator = client.get_paginator("list_landing_zones")
    ```
"""
from .client import ControlTowerClient
from .paginator import ListEnabledControlsPaginator, ListLandingZonesPaginator

Client = ControlTowerClient

__all__ = (
    "Client",
    "ControlTowerClient",
    "ListEnabledControlsPaginator",
    "ListLandingZonesPaginator",
)
