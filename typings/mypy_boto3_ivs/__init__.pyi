"""
Main interface for ivs service.

Usage::

    ```python
    import boto3
    from mypy_boto3_ivs import (
        Client,
        IVSClient,
        ListChannelsPaginator,
        ListPlaybackKeyPairsPaginator,
        ListStreamKeysPaginator,
        ListStreamsPaginator,
    )

    session = boto3.Session()

    client: IVSClient = boto3.client("ivs")
    session_client: IVSClient = session.client("ivs")

    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_playback_key_pairs_paginator: ListPlaybackKeyPairsPaginator = client.get_paginator("list_playback_key_pairs")
    list_stream_keys_paginator: ListStreamKeysPaginator = client.get_paginator("list_stream_keys")
    list_streams_paginator: ListStreamsPaginator = client.get_paginator("list_streams")
    ```
"""
from mypy_boto3_ivs.client import IVSClient
from mypy_boto3_ivs.paginator import (
    ListChannelsPaginator,
    ListPlaybackKeyPairsPaginator,
    ListStreamKeysPaginator,
    ListStreamsPaginator,
)

Client = IVSClient


__all__ = (
    "Client",
    "IVSClient",
    "ListChannelsPaginator",
    "ListPlaybackKeyPairsPaginator",
    "ListStreamKeysPaginator",
    "ListStreamsPaginator",
)
