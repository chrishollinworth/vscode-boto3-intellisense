"""
Main interface for arc-zonal-shift service.

Usage::

    ```python
    import boto3
    from mypy_boto3_arc_zonal_shift import (
        ARCZonalShiftClient,
        Client,
        ListAutoshiftsPaginator,
        ListManagedResourcesPaginator,
        ListZonalShiftsPaginator,
    )

    session = boto3.Session()

    client: ARCZonalShiftClient = boto3.client("arc-zonal-shift")
    session_client: ARCZonalShiftClient = session.client("arc-zonal-shift")

    list_autoshifts_paginator: ListAutoshiftsPaginator = client.get_paginator("list_autoshifts")
    list_managed_resources_paginator: ListManagedResourcesPaginator = client.get_paginator("list_managed_resources")
    list_zonal_shifts_paginator: ListZonalShiftsPaginator = client.get_paginator("list_zonal_shifts")
    ```
"""

from .client import ARCZonalShiftClient
from .paginator import (
    ListAutoshiftsPaginator,
    ListManagedResourcesPaginator,
    ListZonalShiftsPaginator,
)

Client = ARCZonalShiftClient

__all__ = (
    "ARCZonalShiftClient",
    "Client",
    "ListAutoshiftsPaginator",
    "ListManagedResourcesPaginator",
    "ListZonalShiftsPaginator",
)
