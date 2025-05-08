"""
Main interface for iotevents service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iotevents import (
        Client,
        IoTEventsClient,
    )

    session = Session()
    client: IoTEventsClient = session.client("iotevents")
    ```
"""

from .client import IoTEventsClient

Client = IoTEventsClient

__all__ = ("Client", "IoTEventsClient")
