"""
Main interface for mediaconnect service.

Usage::

    ```python
    import boto3
    from mypy_boto3_mediaconnect import (
        Client,
        FlowActiveWaiter,
        FlowDeletedWaiter,
        FlowStandbyWaiter,
        ListEntitlementsPaginator,
        ListFlowsPaginator,
        ListOfferingsPaginator,
        ListReservationsPaginator,
        MediaConnectClient,
    )

    session = boto3.Session()

    client: MediaConnectClient = boto3.client("mediaconnect")
    session_client: MediaConnectClient = session.client("mediaconnect")

    flow_active_waiter: FlowActiveWaiter = client.get_waiter("flow_active")
    flow_deleted_waiter: FlowDeletedWaiter = client.get_waiter("flow_deleted")
    flow_standby_waiter: FlowStandbyWaiter = client.get_waiter("flow_standby")

    list_entitlements_paginator: ListEntitlementsPaginator = client.get_paginator("list_entitlements")
    list_flows_paginator: ListFlowsPaginator = client.get_paginator("list_flows")
    list_offerings_paginator: ListOfferingsPaginator = client.get_paginator("list_offerings")
    list_reservations_paginator: ListReservationsPaginator = client.get_paginator("list_reservations")
    ```
"""
from .client import MediaConnectClient
from .paginator import (
    ListEntitlementsPaginator,
    ListFlowsPaginator,
    ListOfferingsPaginator,
    ListReservationsPaginator,
)
from .waiter import FlowActiveWaiter, FlowDeletedWaiter, FlowStandbyWaiter

Client = MediaConnectClient

__all__ = (
    "Client",
    "FlowActiveWaiter",
    "FlowDeletedWaiter",
    "FlowStandbyWaiter",
    "ListEntitlementsPaginator",
    "ListFlowsPaginator",
    "ListOfferingsPaginator",
    "ListReservationsPaginator",
    "MediaConnectClient",
)
