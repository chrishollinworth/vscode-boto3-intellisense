"""
Main interface for codeconnections service.

Usage::

    ```python
    import boto3
    from mypy_boto3_codeconnections import (
        Client,
        CodeConnectionsClient,
    )

    session = boto3.Session()

    client: CodeConnectionsClient = boto3.client("codeconnections")
    session_client: CodeConnectionsClient = session.client("codeconnections")
    ```
"""

from .client import CodeConnectionsClient

Client = CodeConnectionsClient

__all__ = ("Client", "CodeConnectionsClient")
