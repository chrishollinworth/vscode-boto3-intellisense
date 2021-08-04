"""
Main interface for detective service.

Usage::

    ```python
    import boto3
    from mypy_boto3_detective import (
        Client,
        DetectiveClient,
    )

    session = boto3.Session()

    client: DetectiveClient = boto3.client("detective")
    session_client: DetectiveClient = session.client("detective")
    ```
"""
from .client import DetectiveClient

Client = DetectiveClient

__all__ = ("Client", "DetectiveClient")
