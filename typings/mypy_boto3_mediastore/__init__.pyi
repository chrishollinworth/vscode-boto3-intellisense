"""
Main interface for mediastore service.

Usage::

    ```python
    import boto3
    from mypy_boto3_mediastore import (
        Client,
        ListContainersPaginator,
        MediaStoreClient,
    )

    session = boto3.Session()

    client: MediaStoreClient = boto3.client("mediastore")
    session_client: MediaStoreClient = session.client("mediastore")

    list_containers_paginator: ListContainersPaginator = client.get_paginator("list_containers")
    ```
"""
from mypy_boto3_mediastore.client import MediaStoreClient
from mypy_boto3_mediastore.paginator import ListContainersPaginator

Client = MediaStoreClient


__all__ = ("Client", "ListContainersPaginator", "MediaStoreClient")
