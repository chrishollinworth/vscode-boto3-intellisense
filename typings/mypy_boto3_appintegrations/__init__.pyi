"""
Main interface for appintegrations service.

Usage::

    ```python
    import boto3
    from mypy_boto3_appintegrations import (
        AppIntegrationsClient,
        Client,
    )

    session = boto3.Session()

    client: AppIntegrationsClient = boto3.client("appintegrations")
    session_client: AppIntegrationsClient = session.client("appintegrations")
    ```
"""
from mypy_boto3_appintegrations.client import AppIntegrationsClient

Client = AppIntegrationsClient


__all__ = ("AppIntegrationsClient", "Client")
