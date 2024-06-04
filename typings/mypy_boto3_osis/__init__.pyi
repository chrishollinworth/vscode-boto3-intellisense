"""
Main interface for osis service.

Usage::

    ```python
    import boto3
    from mypy_boto3_osis import (
        Client,
        OpenSearchIngestionClient,
    )

    session = boto3.Session()

    client: OpenSearchIngestionClient = boto3.client("osis")
    session_client: OpenSearchIngestionClient = session.client("osis")
    ```
"""

from .client import OpenSearchIngestionClient

Client = OpenSearchIngestionClient

__all__ = ("Client", "OpenSearchIngestionClient")
