"""
Main interface for managedblockchain service.

Usage::

    ```python
    import boto3
    from mypy_boto3_managedblockchain import (
        Client,
        ListAccessorsPaginator,
        ManagedBlockchainClient,
    )

    session = boto3.Session()

    client: ManagedBlockchainClient = boto3.client("managedblockchain")
    session_client: ManagedBlockchainClient = session.client("managedblockchain")

    list_accessors_paginator: ListAccessorsPaginator = client.get_paginator("list_accessors")
    ```
"""

from .client import ManagedBlockchainClient
from .paginator import ListAccessorsPaginator

Client = ManagedBlockchainClient

__all__ = ("Client", "ListAccessorsPaginator", "ManagedBlockchainClient")
