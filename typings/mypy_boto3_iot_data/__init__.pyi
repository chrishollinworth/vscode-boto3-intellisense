"""
Main interface for iot-data service.

Usage::

    ```python
    import boto3
    from mypy_boto3_iot_data import (
        Client,
        IoTDataPlaneClient,
    )

    session = boto3.Session()

    client: IoTDataPlaneClient = boto3.client("iot-data")
    session_client: IoTDataPlaneClient = session.client("iot-data")
    ```
"""
from mypy_boto3_iot_data.client import IoTDataPlaneClient

Client = IoTDataPlaneClient


__all__ = ("Client", "IoTDataPlaneClient")
