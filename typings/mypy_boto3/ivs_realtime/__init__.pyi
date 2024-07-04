"""
Main interface for ivs-realtime service.

Usage::

    ```python
    import boto3
    from mypy_boto3_ivs_realtime import (
        Client,
        ListPublicKeysPaginator,
        ivsrealtimeClient,
    )

    session = boto3.Session()

    client: ivsrealtimeClient = boto3.client("ivs-realtime")
    session_client: ivsrealtimeClient = session.client("ivs-realtime")

    list_public_keys_paginator: ListPublicKeysPaginator = client.get_paginator("list_public_keys")
    ```
"""

from .client import ivsrealtimeClient
from .paginator import ListPublicKeysPaginator

Client = ivsrealtimeClient

__all__ = ("Client", "ListPublicKeysPaginator", "ivsrealtimeClient")
