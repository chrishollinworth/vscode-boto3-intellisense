"""
Main interface for iotevents-data service.

Usage::

    ```python
    import boto3
    from mypy_boto3_iotevents_data import (
        Client,
        IoTEventsDataClient,
    )

    session = boto3.Session()

    client: IoTEventsDataClient = boto3.client("iotevents-data")
    session_client: IoTEventsDataClient = session.client("iotevents-data")
    ```
"""
from mypy_boto3_iotevents_data.client import IoTEventsDataClient

Client = IoTEventsDataClient


__all__ = ("Client", "IoTEventsDataClient")
