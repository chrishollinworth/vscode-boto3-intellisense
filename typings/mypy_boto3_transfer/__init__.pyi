"""
Main interface for transfer service.

Usage::

    ```python
    import boto3
    from mypy_boto3_transfer import (
        Client,
        ListServersPaginator,
        TransferClient,
    )

    session = boto3.Session()

    client: TransferClient = boto3.client("transfer")
    session_client: TransferClient = session.client("transfer")

    list_servers_paginator: ListServersPaginator = client.get_paginator("list_servers")
    ```
"""
from mypy_boto3_transfer.client import TransferClient
from mypy_boto3_transfer.paginator import ListServersPaginator

Client = TransferClient


__all__ = ("Client", "ListServersPaginator", "TransferClient")
