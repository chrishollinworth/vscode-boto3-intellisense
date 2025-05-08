"""
Main interface for iot-data service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_data/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iot_data import (
        Client,
        IoTDataPlaneClient,
        ListRetainedMessagesPaginator,
    )

    session = Session()
    client: IoTDataPlaneClient = session.client("iot-data")

    list_retained_messages_paginator: ListRetainedMessagesPaginator = client.get_paginator("list_retained_messages")
    ```
"""

from .client import IoTDataPlaneClient
from .paginator import ListRetainedMessagesPaginator

Client = IoTDataPlaneClient

__all__ = ("Client", "IoTDataPlaneClient", "ListRetainedMessagesPaginator")
