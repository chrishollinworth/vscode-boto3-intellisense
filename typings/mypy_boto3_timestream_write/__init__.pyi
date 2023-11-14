"""
Main interface for timestream-write service.

Usage::

    ```python
    import boto3
    from mypy_boto3_timestream_write import (
        Client,
        TimestreamWriteClient,
    )

    session = boto3.Session()

    client: TimestreamWriteClient = boto3.client("timestream-write")
    session_client: TimestreamWriteClient = session.client("timestream-write")
    ```
"""
from .client import TimestreamWriteClient

Client = TimestreamWriteClient

__all__ = ("Client", "TimestreamWriteClient")
