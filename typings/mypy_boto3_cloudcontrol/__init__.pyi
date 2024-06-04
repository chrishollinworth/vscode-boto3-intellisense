"""
Main interface for cloudcontrol service.

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudcontrol import (
        Client,
        CloudControlApiClient,
        ListResourceRequestsPaginator,
        ListResourcesPaginator,
        ResourceRequestSuccessWaiter,
    )

    session = boto3.Session()

    client: CloudControlApiClient = boto3.client("cloudcontrol")
    session_client: CloudControlApiClient = session.client("cloudcontrol")

    resource_request_success_waiter: ResourceRequestSuccessWaiter = client.get_waiter("resource_request_success")

    list_resource_requests_paginator: ListResourceRequestsPaginator = client.get_paginator("list_resource_requests")
    list_resources_paginator: ListResourcesPaginator = client.get_paginator("list_resources")
    ```
"""

from .client import CloudControlApiClient
from .paginator import ListResourceRequestsPaginator, ListResourcesPaginator
from .waiter import ResourceRequestSuccessWaiter

Client = CloudControlApiClient

__all__ = (
    "Client",
    "CloudControlApiClient",
    "ListResourceRequestsPaginator",
    "ListResourcesPaginator",
    "ResourceRequestSuccessWaiter",
)
