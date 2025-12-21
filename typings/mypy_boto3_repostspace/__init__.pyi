"""
Main interface for repostspace service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_repostspace import (
        ChannelCreatedWaiter,
        ChannelDeletedWaiter,
        Client,
        ListChannelsPaginator,
        ListSpacesPaginator,
        RePostPrivateClient,
        SpaceCreatedWaiter,
        SpaceDeletedWaiter,
    )

    session = Session()
    client: RePostPrivateClient = session.client("repostspace")

    channel_created_waiter: ChannelCreatedWaiter = client.get_waiter("channel_created")
    channel_deleted_waiter: ChannelDeletedWaiter = client.get_waiter("channel_deleted")
    space_created_waiter: SpaceCreatedWaiter = client.get_waiter("space_created")
    space_deleted_waiter: SpaceDeletedWaiter = client.get_waiter("space_deleted")

    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_spaces_paginator: ListSpacesPaginator = client.get_paginator("list_spaces")
    ```
"""

from .client import RePostPrivateClient
from .paginator import ListChannelsPaginator, ListSpacesPaginator
from .waiter import (
    ChannelCreatedWaiter,
    ChannelDeletedWaiter,
    SpaceCreatedWaiter,
    SpaceDeletedWaiter,
)

Client = RePostPrivateClient

__all__ = (
    "ChannelCreatedWaiter",
    "ChannelDeletedWaiter",
    "Client",
    "ListChannelsPaginator",
    "ListSpacesPaginator",
    "RePostPrivateClient",
    "SpaceCreatedWaiter",
    "SpaceDeletedWaiter",
)
