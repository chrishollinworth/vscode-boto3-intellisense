"""
Main interface for kinesisanalytics service.

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesisanalytics import (
        Client,
        KinesisAnalyticsClient,
    )

    session = boto3.Session()

    client: KinesisAnalyticsClient = boto3.client("kinesisanalytics")
    session_client: KinesisAnalyticsClient = session.client("kinesisanalytics")
    ```
"""
from .client import KinesisAnalyticsClient

Client = KinesisAnalyticsClient

__all__ = ("Client", "KinesisAnalyticsClient")
