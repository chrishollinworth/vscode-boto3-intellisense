"""
Main interface for appconfigdata service.

Usage::

    ```python
    import boto3
    from mypy_boto3_appconfigdata import (
        AppConfigDataClient,
        Client,
    )

    session = boto3.Session()

    client: AppConfigDataClient = boto3.client("appconfigdata")
    session_client: AppConfigDataClient = session.client("appconfigdata")
    ```
"""

from .client import AppConfigDataClient

Client = AppConfigDataClient

__all__ = ("AppConfigDataClient", "Client")
