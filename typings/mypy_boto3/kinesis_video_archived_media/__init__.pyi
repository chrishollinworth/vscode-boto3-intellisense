"""
Main interface for kinesis-video-archived-media service.

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesis_video_archived_media import (
        Client,
        GetImagesPaginator,
        KinesisVideoArchivedMediaClient,
        ListFragmentsPaginator,
    )

    session = boto3.Session()

    client: KinesisVideoArchivedMediaClient = boto3.client("kinesis-video-archived-media")
    session_client: KinesisVideoArchivedMediaClient = session.client("kinesis-video-archived-media")

    get_images_paginator: GetImagesPaginator = client.get_paginator("get_images")
    list_fragments_paginator: ListFragmentsPaginator = client.get_paginator("list_fragments")
    ```
"""
from .client import KinesisVideoArchivedMediaClient
from .paginator import GetImagesPaginator, ListFragmentsPaginator

Client = KinesisVideoArchivedMediaClient

__all__ = (
    "Client",
    "GetImagesPaginator",
    "KinesisVideoArchivedMediaClient",
    "ListFragmentsPaginator",
)
