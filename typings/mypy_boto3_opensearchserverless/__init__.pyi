"""
Main interface for opensearchserverless service.

Usage::

    ```python
    import boto3
    from mypy_boto3_opensearchserverless import (
        Client,
        OpenSearchServiceServerlessClient,
    )

    session = boto3.Session()

    client: OpenSearchServiceServerlessClient = boto3.client("opensearchserverless")
    session_client: OpenSearchServiceServerlessClient = session.client("opensearchserverless")
    ```
"""
from .client import OpenSearchServiceServerlessClient

Client = OpenSearchServiceServerlessClient

__all__ = ("Client", "OpenSearchServiceServerlessClient")
