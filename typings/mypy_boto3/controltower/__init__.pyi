"""
Main interface for controltower service.

Usage::

    ```python
    import boto3
    from mypy_boto3_controltower import (
        Client,
        ControlTowerClient,
        ListBaselinesPaginator,
        ListControlOperationsPaginator,
        ListEnabledBaselinesPaginator,
        ListEnabledControlsPaginator,
        ListLandingZoneOperationsPaginator,
        ListLandingZonesPaginator,
    )

    session = boto3.Session()

    client: ControlTowerClient = boto3.client("controltower")
    session_client: ControlTowerClient = session.client("controltower")

    list_baselines_paginator: ListBaselinesPaginator = client.get_paginator("list_baselines")
    list_control_operations_paginator: ListControlOperationsPaginator = client.get_paginator("list_control_operations")
    list_enabled_baselines_paginator: ListEnabledBaselinesPaginator = client.get_paginator("list_enabled_baselines")
    list_enabled_controls_paginator: ListEnabledControlsPaginator = client.get_paginator("list_enabled_controls")
    list_landing_zone_operations_paginator: ListLandingZoneOperationsPaginator = client.get_paginator("list_landing_zone_operations")
    list_landing_zones_paginator: ListLandingZonesPaginator = client.get_paginator("list_landing_zones")
    ```
"""

from .client import ControlTowerClient
from .paginator import (
    ListBaselinesPaginator,
    ListControlOperationsPaginator,
    ListEnabledBaselinesPaginator,
    ListEnabledControlsPaginator,
    ListLandingZoneOperationsPaginator,
    ListLandingZonesPaginator,
)

Client = ControlTowerClient

__all__ = (
    "Client",
    "ControlTowerClient",
    "ListBaselinesPaginator",
    "ListControlOperationsPaginator",
    "ListEnabledBaselinesPaginator",
    "ListEnabledControlsPaginator",
    "ListLandingZoneOperationsPaginator",
    "ListLandingZonesPaginator",
)
