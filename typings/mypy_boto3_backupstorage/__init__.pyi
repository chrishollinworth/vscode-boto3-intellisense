"""
Main interface for backupstorage service.

Usage::

    ```python
    import boto3
    from mypy_boto3_backupstorage import (
        BackupStorageClient,
        Client,
    )

    session = boto3.Session()

    client: BackupStorageClient = boto3.client("backupstorage")
    session_client: BackupStorageClient = session.client("backupstorage")
    ```
"""

from .client import BackupStorageClient

Client = BackupStorageClient

__all__ = ("BackupStorageClient", "Client")
