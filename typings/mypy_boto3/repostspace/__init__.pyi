"""
Main interface for repostspace service.

Usage::

    ```python
    import boto3
    from mypy_boto3_repostspace import (
        Client,
        ListSpacesPaginator,
        rePostPrivateClient,
    )

    session = boto3.Session()

    client: rePostPrivateClient = boto3.client("repostspace")
    session_client: rePostPrivateClient = session.client("repostspace")

    list_spaces_paginator: ListSpacesPaginator = client.get_paginator("list_spaces")
    ```
"""
from .client import rePostPrivateClient
from .paginator import ListSpacesPaginator

Client = rePostPrivateClient

__all__ = ("Client", "ListSpacesPaginator", "rePostPrivateClient")
