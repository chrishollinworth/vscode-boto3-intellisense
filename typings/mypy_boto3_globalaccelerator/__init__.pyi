"""
Main interface for globalaccelerator service.

Usage::

    ```python
    import boto3
    from mypy_boto3_globalaccelerator import (
        Client,
        GlobalAcceleratorClient,
        ListAcceleratorsPaginator,
        ListByoipCidrsPaginator,
        ListCustomRoutingAcceleratorsPaginator,
        ListCustomRoutingListenersPaginator,
        ListCustomRoutingPortMappingsByDestinationPaginator,
        ListCustomRoutingPortMappingsPaginator,
        ListEndpointGroupsPaginator,
        ListListenersPaginator,
    )

    session = boto3.Session()

    client: GlobalAcceleratorClient = boto3.client("globalaccelerator")
    session_client: GlobalAcceleratorClient = session.client("globalaccelerator")

    list_accelerators_paginator: ListAcceleratorsPaginator = client.get_paginator("list_accelerators")
    list_byoip_cidrs_paginator: ListByoipCidrsPaginator = client.get_paginator("list_byoip_cidrs")
    list_custom_routing_accelerators_paginator: ListCustomRoutingAcceleratorsPaginator = client.get_paginator("list_custom_routing_accelerators")
    list_custom_routing_listeners_paginator: ListCustomRoutingListenersPaginator = client.get_paginator("list_custom_routing_listeners")
    list_custom_routing_port_mappings_paginator: ListCustomRoutingPortMappingsPaginator = client.get_paginator("list_custom_routing_port_mappings")
    list_custom_routing_port_mappings_by_destination_paginator: ListCustomRoutingPortMappingsByDestinationPaginator = client.get_paginator("list_custom_routing_port_mappings_by_destination")
    list_endpoint_groups_paginator: ListEndpointGroupsPaginator = client.get_paginator("list_endpoint_groups")
    list_listeners_paginator: ListListenersPaginator = client.get_paginator("list_listeners")
    ```
"""
from mypy_boto3_globalaccelerator.client import GlobalAcceleratorClient
from mypy_boto3_globalaccelerator.paginator import (
    ListAcceleratorsPaginator,
    ListByoipCidrsPaginator,
    ListCustomRoutingAcceleratorsPaginator,
    ListCustomRoutingListenersPaginator,
    ListCustomRoutingPortMappingsByDestinationPaginator,
    ListCustomRoutingPortMappingsPaginator,
    ListEndpointGroupsPaginator,
    ListListenersPaginator,
)

Client = GlobalAcceleratorClient


__all__ = (
    "Client",
    "GlobalAcceleratorClient",
    "ListAcceleratorsPaginator",
    "ListByoipCidrsPaginator",
    "ListCustomRoutingAcceleratorsPaginator",
    "ListCustomRoutingListenersPaginator",
    "ListCustomRoutingPortMappingsByDestinationPaginator",
    "ListCustomRoutingPortMappingsPaginator",
    "ListEndpointGroupsPaginator",
    "ListListenersPaginator",
)
