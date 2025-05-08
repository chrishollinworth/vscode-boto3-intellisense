"""
Main interface for privatenetworks service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_privatenetworks/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_privatenetworks import (
        Client,
        ListDeviceIdentifiersPaginator,
        ListNetworkResourcesPaginator,
        ListNetworkSitesPaginator,
        ListNetworksPaginator,
        ListOrdersPaginator,
        Private5GClient,
    )

    session = Session()
    client: Private5GClient = session.client("privatenetworks")

    list_device_identifiers_paginator: ListDeviceIdentifiersPaginator = client.get_paginator("list_device_identifiers")
    list_network_resources_paginator: ListNetworkResourcesPaginator = client.get_paginator("list_network_resources")
    list_network_sites_paginator: ListNetworkSitesPaginator = client.get_paginator("list_network_sites")
    list_networks_paginator: ListNetworksPaginator = client.get_paginator("list_networks")
    list_orders_paginator: ListOrdersPaginator = client.get_paginator("list_orders")
    ```
"""

from .client import Private5GClient
from .paginator import (
    ListDeviceIdentifiersPaginator,
    ListNetworkResourcesPaginator,
    ListNetworkSitesPaginator,
    ListNetworksPaginator,
    ListOrdersPaginator,
)

Client = Private5GClient

__all__ = (
    "Client",
    "ListDeviceIdentifiersPaginator",
    "ListNetworkResourcesPaginator",
    "ListNetworkSitesPaginator",
    "ListNetworksPaginator",
    "ListOrdersPaginator",
    "Private5GClient",
)
