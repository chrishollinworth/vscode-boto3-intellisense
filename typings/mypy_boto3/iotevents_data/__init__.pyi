"""
Main interface for iotevents-data service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iotevents_data import (
        Client,
        IoTEventsDataClient,
    )

    session = Session()
    client: IoTEventsDataClient = session.client("iotevents-data")
    ```
"""

from .client import IoTEventsDataClient

Client = IoTEventsDataClient

__all__ = ("Client", "IoTEventsDataClient")
