"""
Main interface for repostspace service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_repostspace import (
        Client,
        ListSpacesPaginator,
        RePostPrivateClient,
    )

    session = Session()
    client: RePostPrivateClient = session.client("repostspace")

    list_spaces_paginator: ListSpacesPaginator = client.get_paginator("list_spaces")
    ```
"""

from .client import RePostPrivateClient
from .paginator import ListSpacesPaginator

Client = RePostPrivateClient

__all__ = ("Client", "ListSpacesPaginator", "RePostPrivateClient")
