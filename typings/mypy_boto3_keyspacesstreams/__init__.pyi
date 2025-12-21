"""
Main interface for keyspacesstreams service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_keyspacesstreams/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_keyspacesstreams import (
        Client,
        GetStreamPaginator,
        KeyspacesStreamsClient,
        ListStreamsPaginator,
    )

    session = Session()
    client: KeyspacesStreamsClient = session.client("keyspacesstreams")

    get_stream_paginator: GetStreamPaginator = client.get_paginator("get_stream")
    list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
    ```
"""

from .client import KeyspacesStreamsClient
from .paginator import GetStreamPaginator, ListStreamsPaginator

Client = KeyspacesStreamsClient

__all__ = ("Client", "GetStreamPaginator", "KeyspacesStreamsClient", "ListStreamsPaginator")
