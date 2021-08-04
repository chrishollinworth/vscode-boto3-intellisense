"""
Main interface for finspace-data service.

Usage::

    ```python
    import boto3
    from mypy_boto3_finspace_data import (
        Client,
        FinSpaceDataClient,
    )

    session = boto3.Session()

    client: FinSpaceDataClient = boto3.client("finspace-data")
    session_client: FinSpaceDataClient = session.client("finspace-data")
    ```
"""
from .client import FinSpaceDataClient

Client = FinSpaceDataClient

__all__ = ("Client", "FinSpaceDataClient")
