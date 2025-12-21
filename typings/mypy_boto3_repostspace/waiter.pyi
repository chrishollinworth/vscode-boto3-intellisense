"""
Type annotations for repostspace service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_repostspace.client import RePostPrivateClient
    from mypy_boto3_repostspace.waiter import (
        ChannelCreatedWaiter,
        ChannelDeletedWaiter,
        SpaceCreatedWaiter,
        SpaceDeletedWaiter,
    )

    session = Session()
    client: RePostPrivateClient = session.client("repostspace")

    channel_created_waiter: ChannelCreatedWaiter = client.get_waiter("channel_created")
    channel_deleted_waiter: ChannelDeletedWaiter = client.get_waiter("channel_deleted")
    space_created_waiter: SpaceCreatedWaiter = client.get_waiter("space_created")
    space_deleted_waiter: SpaceDeletedWaiter = client.get_waiter("space_deleted")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    GetChannelInputWaitExtraTypeDef,
    GetChannelInputWaitTypeDef,
    GetSpaceInputWaitExtraTypeDef,
    GetSpaceInputWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ChannelCreatedWaiter",
    "ChannelDeletedWaiter",
    "SpaceCreatedWaiter",
    "SpaceDeletedWaiter",
)

class ChannelCreatedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/waiter/ChannelCreated.html#RePostPrivate.Waiter.ChannelCreated)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/waiters/#channelcreatedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetChannelInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/waiter/ChannelCreated.html#RePostPrivate.Waiter.ChannelCreated.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/waiters/#channelcreatedwaiter)
        """

class ChannelDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/waiter/ChannelDeleted.html#RePostPrivate.Waiter.ChannelDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/waiters/#channeldeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetChannelInputWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/waiter/ChannelDeleted.html#RePostPrivate.Waiter.ChannelDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/waiters/#channeldeletedwaiter)
        """

class SpaceCreatedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/waiter/SpaceCreated.html#RePostPrivate.Waiter.SpaceCreated)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/waiters/#spacecreatedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetSpaceInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/waiter/SpaceCreated.html#RePostPrivate.Waiter.SpaceCreated.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/waiters/#spacecreatedwaiter)
        """

class SpaceDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/waiter/SpaceDeleted.html#RePostPrivate.Waiter.SpaceDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/waiters/#spacedeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetSpaceInputWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/waiter/SpaceDeleted.html#RePostPrivate.Waiter.SpaceDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/waiters/#spacedeletedwaiter)
        """
