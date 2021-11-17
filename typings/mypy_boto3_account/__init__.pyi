"""
Main interface for account service.

Usage::

    ```python
    import boto3
    from mypy_boto3_account import (
        AccountClient,
        Client,
    )

    session = boto3.Session()

    client: AccountClient = boto3.client("account")
    session_client: AccountClient = session.client("account")
    ```
"""
from .client import AccountClient

Client = AccountClient

__all__ = ("AccountClient", "Client")
