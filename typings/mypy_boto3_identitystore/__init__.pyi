"""
Main interface for identitystore service.

Usage::

    ```python
    import boto3
    from mypy_boto3_identitystore import (
        Client,
        IdentityStoreClient,
    )

    session = boto3.Session()

    client: IdentityStoreClient = boto3.client("identitystore")
    session_client: IdentityStoreClient = session.client("identitystore")
    ```
"""
from .client import IdentityStoreClient

Client = IdentityStoreClient

__all__ = ("Client", "IdentityStoreClient")
