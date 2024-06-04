"""
Main interface for support-app service.

Usage::

    ```python
    import boto3
    from mypy_boto3_support_app import (
        Client,
        SupportAppClient,
    )

    session = boto3.Session()

    client: SupportAppClient = boto3.client("support-app")
    session_client: SupportAppClient = session.client("support-app")
    ```
"""

from .client import SupportAppClient

Client = SupportAppClient

__all__ = ("Client", "SupportAppClient")
