"""
Main interface for mediaconnect service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mediaconnect import (
        Client,
        FlowActiveWaiter,
        FlowDeletedWaiter,
        FlowStandbyWaiter,
        ListBridgesPaginator,
        ListEntitlementsPaginator,
        ListFlowsPaginator,
        ListGatewayInstancesPaginator,
        ListGatewaysPaginator,
        ListOfferingsPaginator,
        ListReservationsPaginator,
        MediaConnectClient,
    )

    session = Session()
    client: MediaConnectClient = session.client("mediaconnect")

    flow_active_waiter: FlowActiveWaiter = client.get_waiter("flow_active")
    flow_deleted_waiter: FlowDeletedWaiter = client.get_waiter("flow_deleted")
    flow_standby_waiter: FlowStandbyWaiter = client.get_waiter("flow_standby")

    list_bridges_paginator: ListBridgesPaginator = client.get_paginator("list_bridges")
    list_entitlements_paginator: ListEntitlementsPaginator = client.get_paginator("list_entitlements")
    list_flows_paginator: ListFlowsPaginator = client.get_paginator("list_flows")
    list_gateway_instances_paginator: ListGatewayInstancesPaginator = client.get_paginator("list_gateway_instances")
    list_gateways_paginator: ListGatewaysPaginator = client.get_paginator("list_gateways")
    list_offerings_paginator: ListOfferingsPaginator = client.get_paginator("list_offerings")
    list_reservations_paginator: ListReservationsPaginator = client.get_paginator("list_reservations")
    ```
"""

from .client import MediaConnectClient
from .paginator import (
    ListBridgesPaginator,
    ListEntitlementsPaginator,
    ListFlowsPaginator,
    ListGatewayInstancesPaginator,
    ListGatewaysPaginator,
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
    "ListBridgesPaginator",
    "ListEntitlementsPaginator",
    "ListFlowsPaginator",
    "ListGatewayInstancesPaginator",
    "ListGatewaysPaginator",
    "ListOfferingsPaginator",
    "ListReservationsPaginator",
    "MediaConnectClient",
)
