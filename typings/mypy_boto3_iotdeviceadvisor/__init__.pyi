"""
Main interface for iotdeviceadvisor service.

Usage::

    ```python
    import boto3
    from mypy_boto3_iotdeviceadvisor import (
        Client,
        IoTDeviceAdvisorClient,
    )

    session = boto3.Session()

    client: IoTDeviceAdvisorClient = boto3.client("iotdeviceadvisor")
    session_client: IoTDeviceAdvisorClient = session.client("iotdeviceadvisor")
    ```
"""
from mypy_boto3_iotdeviceadvisor.client import IoTDeviceAdvisorClient

Client = IoTDeviceAdvisorClient


__all__ = ("Client", "IoTDeviceAdvisorClient")
