"""
Main interface for rtbfabric service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_rtbfabric import (
        Client,
        InboundExternalLinkActiveWaiter,
        LinkAcceptedWaiter,
        LinkActiveWaiter,
        ListLinksPaginator,
        ListRequesterGatewaysPaginator,
        ListResponderGatewaysPaginator,
        OutboundExternalLinkActiveWaiter,
        RTBFabricClient,
        RequesterGatewayActiveWaiter,
        RequesterGatewayDeletedWaiter,
        ResponderGatewayActiveWaiter,
        ResponderGatewayDeletedWaiter,
    )

    session = Session()
    client: RTBFabricClient = session.client("rtbfabric")

    inbound_external_link_active_waiter: InboundExternalLinkActiveWaiter = client.get_waiter("inbound_external_link_active")
    link_accepted_waiter: LinkAcceptedWaiter = client.get_waiter("link_accepted")
    link_active_waiter: LinkActiveWaiter = client.get_waiter("link_active")
    outbound_external_link_active_waiter: OutboundExternalLinkActiveWaiter = client.get_waiter("outbound_external_link_active")
    requester_gateway_active_waiter: RequesterGatewayActiveWaiter = client.get_waiter("requester_gateway_active")
    requester_gateway_deleted_waiter: RequesterGatewayDeletedWaiter = client.get_waiter("requester_gateway_deleted")
    responder_gateway_active_waiter: ResponderGatewayActiveWaiter = client.get_waiter("responder_gateway_active")
    responder_gateway_deleted_waiter: ResponderGatewayDeletedWaiter = client.get_waiter("responder_gateway_deleted")

    list_links_paginator: ListLinksPaginator = client.get_paginator("list_links")
    list_requester_gateways_paginator: ListRequesterGatewaysPaginator = client.get_paginator("list_requester_gateways")
    list_responder_gateways_paginator: ListResponderGatewaysPaginator = client.get_paginator("list_responder_gateways")
    ```
"""

from .client import RTBFabricClient
from .paginator import (
    ListLinksPaginator,
    ListRequesterGatewaysPaginator,
    ListResponderGatewaysPaginator,
)
from .waiter import (
    InboundExternalLinkActiveWaiter,
    LinkAcceptedWaiter,
    LinkActiveWaiter,
    OutboundExternalLinkActiveWaiter,
    RequesterGatewayActiveWaiter,
    RequesterGatewayDeletedWaiter,
    ResponderGatewayActiveWaiter,
    ResponderGatewayDeletedWaiter,
)

Client = RTBFabricClient

__all__ = (
    "Client",
    "InboundExternalLinkActiveWaiter",
    "LinkAcceptedWaiter",
    "LinkActiveWaiter",
    "ListLinksPaginator",
    "ListRequesterGatewaysPaginator",
    "ListResponderGatewaysPaginator",
    "OutboundExternalLinkActiveWaiter",
    "RTBFabricClient",
    "RequesterGatewayActiveWaiter",
    "RequesterGatewayDeletedWaiter",
    "ResponderGatewayActiveWaiter",
    "ResponderGatewayDeletedWaiter",
)
