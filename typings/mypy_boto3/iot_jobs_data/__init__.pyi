"""
Main interface for iot-jobs-data service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iot_jobs_data import (
        Client,
        IoTJobsDataPlaneClient,
    )

    session = Session()
    client: IoTJobsDataPlaneClient = session.client("iot-jobs-data")
    ```
"""

from .client import IoTJobsDataPlaneClient

Client = IoTJobsDataPlaneClient

__all__ = ("Client", "IoTJobsDataPlaneClient")
