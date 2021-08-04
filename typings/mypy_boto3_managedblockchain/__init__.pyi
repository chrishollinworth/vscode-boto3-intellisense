"""
Main interface for managedblockchain service.

Usage::

    ```python
    import boto3
    from mypy_boto3_managedblockchain import (
        Client,
        ManagedBlockchainClient,
    )

    session = boto3.Session()

    client: ManagedBlockchainClient = boto3.client("managedblockchain")
    session_client: ManagedBlockchainClient = session.client("managedblockchain")
    ```
"""
from .client import ManagedBlockchainClient

Client = ManagedBlockchainClient

__all__ = ("Client", "ManagedBlockchainClient")
