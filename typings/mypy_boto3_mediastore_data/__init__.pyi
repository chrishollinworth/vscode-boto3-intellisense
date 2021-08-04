"""
Main interface for mediastore-data service.

Usage::

    ```python
    import boto3
    from mypy_boto3_mediastore_data import (
        Client,
        ListItemsPaginator,
        MediaStoreDataClient,
    )

    session = boto3.Session()

    client: MediaStoreDataClient = boto3.client("mediastore-data")
    session_client: MediaStoreDataClient = session.client("mediastore-data")

    list_items_paginator: ListItemsPaginator = client.get_paginator("list_items")
    ```
"""
from .client import MediaStoreDataClient
from .paginator import ListItemsPaginator

Client = MediaStoreDataClient

__all__ = ("Client", "ListItemsPaginator", "MediaStoreDataClient")
