"""
Main interface for cloudcontrol service.

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudcontrol import (
        Client,
        CloudControlApiClient,
        ResourceRequestSuccessWaiter,
    )

    session = boto3.Session()

    client: CloudControlApiClient = boto3.client("cloudcontrol")
    session_client: CloudControlApiClient = session.client("cloudcontrol")

    resource_request_success_waiter: ResourceRequestSuccessWaiter = client.get_waiter("resource_request_success")
    ```
"""
from .client import CloudControlApiClient
from .waiter import ResourceRequestSuccessWaiter

Client = CloudControlApiClient

__all__ = ("Client", "CloudControlApiClient", "ResourceRequestSuccessWaiter")
