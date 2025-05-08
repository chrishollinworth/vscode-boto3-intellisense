"""
Main interface for kinesis-video-archived-media service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_kinesis_video_archived_media import (
        Client,
        GetImagesPaginator,
        KinesisVideoArchivedMediaClient,
        ListFragmentsPaginator,
    )

    session = Session()
    client: KinesisVideoArchivedMediaClient = session.client("kinesis-video-archived-media")

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
