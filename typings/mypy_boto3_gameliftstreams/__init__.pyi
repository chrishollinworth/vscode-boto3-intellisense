"""
Main interface for gameliftstreams service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_gameliftstreams import (
        ApplicationDeletedWaiter,
        ApplicationReadyWaiter,
        Client,
        GameLiftStreamsClient,
        ListApplicationsPaginator,
        ListStreamGroupsPaginator,
        ListStreamSessionsByAccountPaginator,
        ListStreamSessionsPaginator,
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

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_stream_groups_paginator: ListStreamGroupsPaginator = client.get_paginator("list_stream_groups")
    list_stream_sessions_by_account_paginator: ListStreamSessionsByAccountPaginator = client.get_paginator("list_stream_sessions_by_account")
    list_stream_sessions_paginator: ListStreamSessionsPaginator = client.get_paginator("list_stream_sessions")
    ```
"""

from .client import GameLiftStreamsClient
from .paginator import (
    ListApplicationsPaginator,
    ListStreamGroupsPaginator,
    ListStreamSessionsByAccountPaginator,
    ListStreamSessionsPaginator,
)
from .waiter import (
    ApplicationDeletedWaiter,
    ApplicationReadyWaiter,
    StreamGroupActiveWaiter,
    StreamGroupDeletedWaiter,
    StreamSessionActiveWaiter,
)

Client = GameLiftStreamsClient

__all__ = (
    "ApplicationDeletedWaiter",
    "ApplicationReadyWaiter",
    "Client",
    "GameLiftStreamsClient",
    "ListApplicationsPaginator",
    "ListStreamGroupsPaginator",
    "ListStreamSessionsByAccountPaginator",
    "ListStreamSessionsPaginator",
    "StreamGroupActiveWaiter",
    "StreamGroupDeletedWaiter",
    "StreamSessionActiveWaiter",
)
