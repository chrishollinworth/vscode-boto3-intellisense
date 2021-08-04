"""
Main interface for finspace service.

Usage::

    ```python
    import boto3
    from mypy_boto3_finspace import (
        Client,
        finspaceClient,
    )

    session = boto3.Session()

    client: finspaceClient = boto3.client("finspace")
    session_client: finspaceClient = session.client("finspace")
    ```
"""
from .client import finspaceClient

Client = finspaceClient

__all__ = ("Client", "finspaceClient")
