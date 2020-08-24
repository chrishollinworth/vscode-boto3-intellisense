"""
Main interface for globalaccelerator service.

Usage::

    ```python
    import boto3
    from mypy_boto3_globalaccelerator import (
        Client,
        GlobalAcceleratorClient,
        ListAcceleratorsPaginator,
        ListEndpointGroupsPaginator,
        ListListenersPaginator,
    )

    session = boto3.Session()

    client: GlobalAcceleratorClient = boto3.client("globalaccelerator")
    session_client: GlobalAcceleratorClient = session.client("globalaccelerator")

    list_accelerators_paginator: ListAcceleratorsPaginator = client.get_paginator("list_accelerators")
    list_endpoint_groups_paginator: ListEndpointGroupsPaginator = client.get_paginator("list_endpoint_groups")
    list_listeners_paginator: ListListenersPaginator = client.get_paginator("list_listeners")
    ```
"""
from mypy_boto3_globalaccelerator.client import GlobalAcceleratorClient
from mypy_boto3_globalaccelerator.paginator import (
    ListAcceleratorsPaginator,
    ListEndpointGroupsPaginator,
    ListListenersPaginator,
)

Client = GlobalAcceleratorClient


__all__ = (
    "Client",
    "GlobalAcceleratorClient",
    "ListAcceleratorsPaginator",
    "ListEndpointGroupsPaginator",
    "ListListenersPaginator",
)
