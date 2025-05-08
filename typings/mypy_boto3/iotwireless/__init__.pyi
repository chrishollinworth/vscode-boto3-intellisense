"""
Main interface for iotwireless service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iotwireless import (
        Client,
        IoTWirelessClient,
    )

    session = Session()
    client: IoTWirelessClient = session.client("iotwireless")
    ```
"""

from .client import IoTWirelessClient

Client = IoTWirelessClient

__all__ = ("Client", "IoTWirelessClient")
