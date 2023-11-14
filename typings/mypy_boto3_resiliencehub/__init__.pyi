"""
Main interface for resiliencehub service.

Usage::

    ```python
    import boto3
    from mypy_boto3_resiliencehub import (
        Client,
        ResilienceHubClient,
    )

    session = boto3.Session()

    client: ResilienceHubClient = boto3.client("resiliencehub")
    session_client: ResilienceHubClient = session.client("resiliencehub")
    ```
"""
from .client import ResilienceHubClient

Client = ResilienceHubClient

__all__ = ("Client", "ResilienceHubClient")
