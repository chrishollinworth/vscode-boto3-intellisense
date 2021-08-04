"""
Main interface for worklink service.

Usage::

    ```python
    import boto3
    from mypy_boto3_worklink import (
        Client,
        WorkLinkClient,
    )

    session = boto3.Session()

    client: WorkLinkClient = boto3.client("worklink")
    session_client: WorkLinkClient = session.client("worklink")
    ```
"""
from .client import WorkLinkClient

Client = WorkLinkClient

__all__ = ("Client", "WorkLinkClient")
