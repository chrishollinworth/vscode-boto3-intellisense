"""
Main interface for cognito-sync service.

Usage::

    ```python
    import boto3
    from mypy_boto3_cognito_sync import (
        Client,
        CognitoSyncClient,
    )

    session = boto3.Session()

    client: CognitoSyncClient = boto3.client("cognito-sync")
    session_client: CognitoSyncClient = session.client("cognito-sync")
    ```
"""
from mypy_boto3_cognito_sync.client import CognitoSyncClient

Client = CognitoSyncClient


__all__ = ("Client", "CognitoSyncClient")
