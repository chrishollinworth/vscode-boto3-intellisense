"""
Main interface for iot-data service.

Usage::

    ```python
    import boto3
    from mypy_boto3_iot_data import (
        Client,
        IoTDataPlaneClient,
        ListRetainedMessagesPaginator,
    )

    session = boto3.Session()

    client: IoTDataPlaneClient = boto3.client("iot-data")
    session_client: IoTDataPlaneClient = session.client("iot-data")

    list_retained_messages_paginator: ListRetainedMessagesPaginator = client.get_paginator("list_retained_messages")
    ```
"""
from .client import IoTDataPlaneClient
from .paginator import ListRetainedMessagesPaginator

Client = IoTDataPlaneClient

__all__ = ("Client", "IoTDataPlaneClient", "ListRetainedMessagesPaginator")
