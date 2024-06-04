"""
Main interface for cloudtrail-data service.

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudtrail_data import (
        Client,
        CloudTrailDataServiceClient,
    )

    session = boto3.Session()

    client: CloudTrailDataServiceClient = boto3.client("cloudtrail-data")
    session_client: CloudTrailDataServiceClient = session.client("cloudtrail-data")
    ```
"""

from .client import CloudTrailDataServiceClient

Client = CloudTrailDataServiceClient

__all__ = ("Client", "CloudTrailDataServiceClient")
