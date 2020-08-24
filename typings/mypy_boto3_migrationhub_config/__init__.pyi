"""
Main interface for migrationhub-config service.

Usage::

    ```python
    import boto3
    from mypy_boto3_migrationhub_config import (
        Client,
        MigrationHubConfigClient,
    )

    session = boto3.Session()

    client: MigrationHubConfigClient = boto3.client("migrationhub-config")
    session_client: MigrationHubConfigClient = session.client("migrationhub-config")
    ```
"""
from mypy_boto3_migrationhub_config.client import MigrationHubConfigClient

Client = MigrationHubConfigClient


__all__ = ("Client", "MigrationHubConfigClient")
