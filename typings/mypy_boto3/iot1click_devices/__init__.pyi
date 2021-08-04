"""
Main interface for iot1click-devices service.

Usage::

    ```python
    import boto3
    from mypy_boto3_iot1click_devices import (
        Client,
        IoT1ClickDevicesServiceClient,
        ListDeviceEventsPaginator,
        ListDevicesPaginator,
    )

    session = boto3.Session()

    client: IoT1ClickDevicesServiceClient = boto3.client("iot1click-devices")
    session_client: IoT1ClickDevicesServiceClient = session.client("iot1click-devices")

    list_device_events_paginator: ListDeviceEventsPaginator = client.get_paginator("list_device_events")
    list_devices_paginator: ListDevicesPaginator = client.get_paginator("list_devices")
    ```
"""
from .client import IoT1ClickDevicesServiceClient
from .paginator import ListDeviceEventsPaginator, ListDevicesPaginator

Client = IoT1ClickDevicesServiceClient

__all__ = (
    "Client",
    "IoT1ClickDevicesServiceClient",
    "ListDeviceEventsPaginator",
    "ListDevicesPaginator",
)
