"""
Main interface for mediapackagev2 service.

Usage::

    ```python
    import boto3
    from mypy_boto3_mediapackagev2 import (
        Client,
        ListChannelGroupsPaginator,
        ListChannelsPaginator,
        ListOriginEndpointsPaginator,
        mediapackagev2Client,
    )

    session = boto3.Session()

    client: mediapackagev2Client = boto3.client("mediapackagev2")
    session_client: mediapackagev2Client = session.client("mediapackagev2")

    list_channel_groups_paginator: ListChannelGroupsPaginator = client.get_paginator("list_channel_groups")
    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_origin_endpoints_paginator: ListOriginEndpointsPaginator = client.get_paginator("list_origin_endpoints")
    ```
"""

from .client import mediapackagev2Client
from .paginator import (
    ListChannelGroupsPaginator,
    ListChannelsPaginator,
    ListOriginEndpointsPaginator,
)

Client = mediapackagev2Client

__all__ = (
    "Client",
    "ListChannelGroupsPaginator",
    "ListChannelsPaginator",
    "ListOriginEndpointsPaginator",
    "mediapackagev2Client",
)
