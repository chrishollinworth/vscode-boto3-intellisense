"""
Main interface for iotwireless service.

Usage::

    ```python
    import boto3
    from mypy_boto3_iotwireless import (
        Client,
        IoTWirelessClient,
    )

    session = boto3.Session()

    client: IoTWirelessClient = boto3.client("iotwireless")
    session_client: IoTWirelessClient = session.client("iotwireless")
    ```
"""
from mypy_boto3_iotwireless.client import IoTWirelessClient

Client = IoTWirelessClient


__all__ = ("Client", "IoTWirelessClient")
