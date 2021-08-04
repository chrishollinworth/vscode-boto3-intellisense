"""
Main interface for iot-jobs-data service.

Usage::

    ```python
    import boto3
    from mypy_boto3_iot_jobs_data import (
        Client,
        IoTJobsDataPlaneClient,
    )

    session = boto3.Session()

    client: IoTJobsDataPlaneClient = boto3.client("iot-jobs-data")
    session_client: IoTJobsDataPlaneClient = session.client("iot-jobs-data")
    ```
"""
from .client import IoTJobsDataPlaneClient

Client = IoTJobsDataPlaneClient

__all__ = ("Client", "IoTJobsDataPlaneClient")
