"""
Main interface for iottwinmaker service.

Usage::

    ```python
    import boto3
    from mypy_boto3_iottwinmaker import (
        Client,
        IoTTwinMakerClient,
    )

    session = boto3.Session()

    client: IoTTwinMakerClient = boto3.client("iottwinmaker")
    session_client: IoTTwinMakerClient = session.client("iottwinmaker")
    ```
"""
from .client import IoTTwinMakerClient

Client = IoTTwinMakerClient

__all__ = ("Client", "IoTTwinMakerClient")
