"""
Type annotations for gameliftstreams service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_gameliftstreams.client import GameLiftStreamsClient
    from mypy_boto3_gameliftstreams.waiter import (
        ApplicationDeletedWaiter,
        ApplicationReadyWaiter,
        StreamGroupActiveWaiter,
        StreamGroupDeletedWaiter,
        StreamSessionActiveWaiter,
    )

    session = Session()
    client: GameLiftStreamsClient = session.client("gameliftstreams")

    application_deleted_waiter: ApplicationDeletedWaiter = client.get_waiter("application_deleted")
    application_ready_waiter: ApplicationReadyWaiter = client.get_waiter("application_ready")
    stream_group_active_waiter: StreamGroupActiveWaiter = client.get_waiter("stream_group_active")
    stream_group_deleted_waiter: StreamGroupDeletedWaiter = client.get_waiter("stream_group_deleted")
    stream_session_active_waiter: StreamSessionActiveWaiter = client.get_waiter("stream_session_active")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    GetApplicationInputWaitExtraTypeDef,
    GetApplicationInputWaitTypeDef,
    GetStreamGroupInputWaitExtraTypeDef,
    GetStreamGroupInputWaitTypeDef,
    GetStreamSessionInputWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ApplicationDeletedWaiter",
    "ApplicationReadyWaiter",
    "StreamGroupActiveWaiter",
    "StreamGroupDeletedWaiter",
    "StreamSessionActiveWaiter",
)

class ApplicationDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/waiter/ApplicationDeleted.html#GameLiftStreams.Waiter.ApplicationDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/waiters/#applicationdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetApplicationInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/waiter/ApplicationDeleted.html#GameLiftStreams.Waiter.ApplicationDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/waiters/#applicationdeletedwaiter)
        """

class ApplicationReadyWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/waiter/ApplicationReady.html#GameLiftStreams.Waiter.ApplicationReady)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/waiters/#applicationreadywaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetApplicationInputWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/waiter/ApplicationReady.html#GameLiftStreams.Waiter.ApplicationReady.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/waiters/#applicationreadywaiter)
        """

class StreamGroupActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/waiter/StreamGroupActive.html#GameLiftStreams.Waiter.StreamGroupActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/waiters/#streamgroupactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetStreamGroupInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/waiter/StreamGroupActive.html#GameLiftStreams.Waiter.StreamGroupActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/waiters/#streamgroupactivewaiter)
        """

class StreamGroupDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/waiter/StreamGroupDeleted.html#GameLiftStreams.Waiter.StreamGroupDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/waiters/#streamgroupdeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetStreamGroupInputWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/waiter/StreamGroupDeleted.html#GameLiftStreams.Waiter.StreamGroupDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/waiters/#streamgroupdeletedwaiter)
        """

class StreamSessionActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/waiter/StreamSessionActive.html#GameLiftStreams.Waiter.StreamSessionActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/waiters/#streamsessionactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetStreamSessionInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/waiter/StreamSessionActive.html#GameLiftStreams.Waiter.StreamSessionActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/waiters/#streamsessionactivewaiter)
        """
