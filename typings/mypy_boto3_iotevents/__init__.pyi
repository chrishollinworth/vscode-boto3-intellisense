"""
Main interface for iotevents service.

Usage::

    ```python
    import boto3
    from mypy_boto3_iotevents import (
        Client,
        IoTEventsClient,
    )

    session = boto3.Session()

    client: IoTEventsClient = boto3.client("iotevents")
    session_client: IoTEventsClient = session.client("iotevents")
    ```
"""
from mypy_boto3_iotevents.client import IoTEventsClient

Client = IoTEventsClient


__all__ = ("Client", "IoTEventsClient")
