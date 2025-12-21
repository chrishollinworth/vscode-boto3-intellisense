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
        InputActiveWaiter,
        InputDeletedWaiter,
        InputStandbyWaiter,
        ListBridgesPaginator,
        ListEntitlementsPaginator,
        ListFlowsPaginator,
        ListGatewayInstancesPaginator,
        ListGatewaysPaginator,
        ListOfferingsPaginator,
        ListReservationsPaginator,
        ListRouterInputsPaginator,
        ListRouterNetworkInterfacesPaginator,
        ListRouterOutputsPaginator,
        MediaConnectClient,
        OutputActiveWaiter,
        OutputDeletedWaiter,
        OutputRoutedWaiter,
        OutputStandbyWaiter,
    )

    session = Session()
    client: MediaConnectClient = session.client("mediaconnect")

    flow_active_waiter: FlowActiveWaiter = client.get_waiter("flow_active")
    flow_deleted_waiter: FlowDeletedWaiter = client.get_waiter("flow_deleted")
    flow_standby_waiter: FlowStandbyWaiter = client.get_waiter("flow_standby")
    input_active_waiter: InputActiveWaiter = client.get_waiter("input_active")
    input_deleted_waiter: InputDeletedWaiter = client.get_waiter("input_deleted")
    input_standby_waiter: InputStandbyWaiter = client.get_waiter("input_standby")
    output_active_waiter: OutputActiveWaiter = client.get_waiter("output_active")
    output_deleted_waiter: OutputDeletedWaiter = client.get_waiter("output_deleted")
    output_routed_waiter: OutputRoutedWaiter = client.get_waiter("output_routed")
    output_standby_waiter: OutputStandbyWaiter = client.get_waiter("output_standby")

    list_bridges_paginator: ListBridgesPaginator = client.get_paginator("list_bridges")
    list_entitlements_paginator: ListEntitlementsPaginator = client.get_paginator("list_entitlements")
    list_flows_paginator: ListFlowsPaginator = client.get_paginator("list_flows")
    list_gateway_instances_paginator: ListGatewayInstancesPaginator = client.get_paginator("list_gateway_instances")
    list_gateways_paginator: ListGatewaysPaginator = client.get_paginator("list_gateways")
    list_offerings_paginator: ListOfferingsPaginator = client.get_paginator("list_offerings")
    list_reservations_paginator: ListReservationsPaginator = client.get_paginator("list_reservations")
    list_router_inputs_paginator: ListRouterInputsPaginator = client.get_paginator("list_router_inputs")
    list_router_network_interfaces_paginator: ListRouterNetworkInterfacesPaginator = client.get_paginator("list_router_network_interfaces")
    list_router_outputs_paginator: ListRouterOutputsPaginator = client.get_paginator("list_router_outputs")
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
    ListRouterInputsPaginator,
    ListRouterNetworkInterfacesPaginator,
    ListRouterOutputsPaginator,
)
from .waiter import (
    FlowActiveWaiter,
    FlowDeletedWaiter,
    FlowStandbyWaiter,
    InputActiveWaiter,
    InputDeletedWaiter,
    InputStandbyWaiter,
    OutputActiveWaiter,
    OutputDeletedWaiter,
    OutputRoutedWaiter,
    OutputStandbyWaiter,
)

Client = MediaConnectClient

__all__ = (
    "Client",
    "FlowActiveWaiter",
    "FlowDeletedWaiter",
    "FlowStandbyWaiter",
    "InputActiveWaiter",
    "InputDeletedWaiter",
    "InputStandbyWaiter",
    "ListBridgesPaginator",
    "ListEntitlementsPaginator",
    "ListFlowsPaginator",
    "ListGatewayInstancesPaginator",
    "ListGatewaysPaginator",
    "ListOfferingsPaginator",
    "ListReservationsPaginator",
    "ListRouterInputsPaginator",
    "ListRouterNetworkInterfacesPaginator",
    "ListRouterOutputsPaginator",
    "MediaConnectClient",
    "OutputActiveWaiter",
    "OutputDeletedWaiter",
    "OutputRoutedWaiter",
    "OutputStandbyWaiter",
)
