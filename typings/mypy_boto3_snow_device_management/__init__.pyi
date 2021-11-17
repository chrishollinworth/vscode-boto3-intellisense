"""
Main interface for snow-device-management service.

Usage::

    ```python
    import boto3
    from mypy_boto3_snow_device_management import (
        Client,
        ListDeviceResourcesPaginator,
        ListDevicesPaginator,
        ListExecutionsPaginator,
        ListTasksPaginator,
        SnowDeviceManagementClient,
    )

    session = boto3.Session()

    client: SnowDeviceManagementClient = boto3.client("snow-device-management")
    session_client: SnowDeviceManagementClient = session.client("snow-device-management")

    list_device_resources_paginator: ListDeviceResourcesPaginator = client.get_paginator("list_device_resources")
    list_devices_paginator: ListDevicesPaginator = client.get_paginator("list_devices")
    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_tasks_paginator: ListTasksPaginator = client.get_paginator("list_tasks")
    ```
"""
from .client import SnowDeviceManagementClient
from .paginator import (
    ListDeviceResourcesPaginator,
    ListDevicesPaginator,
    ListExecutionsPaginator,
    ListTasksPaginator,
)

Client = SnowDeviceManagementClient

__all__ = (
    "Client",
    "ListDeviceResourcesPaginator",
    "ListDevicesPaginator",
    "ListExecutionsPaginator",
    "ListTasksPaginator",
    "SnowDeviceManagementClient",
)
