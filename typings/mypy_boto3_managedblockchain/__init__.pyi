"""
Main interface for managedblockchain service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_managedblockchain import (
        Client,
        ListAccessorsPaginator,
        ManagedBlockchainClient,
    )

    session = Session()
    client: ManagedBlockchainClient = session.client("managedblockchain")

    list_accessors_paginator: ListAccessorsPaginator = client.get_paginator("list_accessors")
    ```
"""

from .client import ManagedBlockchainClient
from .paginator import ListAccessorsPaginator

Client = ManagedBlockchainClient

__all__ = ("Client", "ListAccessorsPaginator", "ManagedBlockchainClient")
