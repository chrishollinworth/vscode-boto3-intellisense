"""
Main interface for cloudsearch service.

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudsearch import (
        Client,
        CloudSearchClient,
    )

    session = boto3.Session()

    client: CloudSearchClient = boto3.client("cloudsearch")
    session_client: CloudSearchClient = session.client("cloudsearch")
    ```
"""
from .client import CloudSearchClient

Client = CloudSearchClient

__all__ = ("Client", "CloudSearchClient")
