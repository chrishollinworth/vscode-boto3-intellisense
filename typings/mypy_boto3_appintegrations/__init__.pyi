"""
Main interface for appintegrations service.

Usage::

    ```python
    import boto3
    from mypy_boto3_appintegrations import (
        AppIntegrationsServiceClient,
        Client,
    )

    session = boto3.Session()

    client: AppIntegrationsServiceClient = boto3.client("appintegrations")
    session_client: AppIntegrationsServiceClient = session.client("appintegrations")
    ```
"""
from mypy_boto3_appintegrations.client import AppIntegrationsServiceClient

Client = AppIntegrationsServiceClient


__all__ = ("AppIntegrationsServiceClient", "Client")
