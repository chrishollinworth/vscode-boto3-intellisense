"""
Main interface for globalaccelerator service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_globalaccelerator import (
        Client,
        GlobalAcceleratorClient,
        ListAcceleratorsPaginator,
        ListByoipCidrsPaginator,
        ListCrossAccountAttachmentsPaginator,
        ListCrossAccountResourcesPaginator,
        ListCustomRoutingAcceleratorsPaginator,
        ListCustomRoutingEndpointGroupsPaginator,
        ListCustomRoutingListenersPaginator,
        ListCustomRoutingPortMappingsByDestinationPaginator,
        ListCustomRoutingPortMappingsPaginator,
        ListEndpointGroupsPaginator,
        ListListenersPaginator,
    )

    session = Session()
    client: GlobalAcceleratorClient = session.client("globalaccelerator")

    list_accelerators_paginator: ListAcceleratorsPaginator = client.get_paginator("list_accelerators")
    list_byoip_cidrs_paginator: ListByoipCidrsPaginator = client.get_paginator("list_byoip_cidrs")
    list_cross_account_attachments_paginator: ListCrossAccountAttachmentsPaginator = client.get_paginator("list_cross_account_attachments")
    list_cross_account_resources_paginator: ListCrossAccountResourcesPaginator = client.get_paginator("list_cross_account_resources")
    list_custom_routing_accelerators_paginator: ListCustomRoutingAcceleratorsPaginator = client.get_paginator("list_custom_routing_accelerators")
    list_custom_routing_endpoint_groups_paginator: ListCustomRoutingEndpointGroupsPaginator = client.get_paginator("list_custom_routing_endpoint_groups")
    list_custom_routing_listeners_paginator: ListCustomRoutingListenersPaginator = client.get_paginator("list_custom_routing_listeners")
    list_custom_routing_port_mappings_by_destination_paginator: ListCustomRoutingPortMappingsByDestinationPaginator = client.get_paginator("list_custom_routing_port_mappings_by_destination")
    list_custom_routing_port_mappings_paginator: ListCustomRoutingPortMappingsPaginator = client.get_paginator("list_custom_routing_port_mappings")
    list_endpoint_groups_paginator: ListEndpointGroupsPaginator = client.get_paginator("list_endpoint_groups")
    list_listeners_paginator: ListListenersPaginator = client.get_paginator("list_listeners")
    ```
"""

from .client import GlobalAcceleratorClient
from .paginator import (
    ListAcceleratorsPaginator,
    ListByoipCidrsPaginator,
    ListCrossAccountAttachmentsPaginator,
    ListCrossAccountResourcesPaginator,
    ListCustomRoutingAcceleratorsPaginator,
    ListCustomRoutingEndpointGroupsPaginator,
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
    "ListCrossAccountAttachmentsPaginator",
    "ListCrossAccountResourcesPaginator",
    "ListCustomRoutingAcceleratorsPaginator",
    "ListCustomRoutingEndpointGroupsPaginator",
    "ListCustomRoutingListenersPaginator",
    "ListCustomRoutingPortMappingsByDestinationPaginator",
    "ListCustomRoutingPortMappingsPaginator",
    "ListEndpointGroupsPaginator",
    "ListListenersPaginator",
)
