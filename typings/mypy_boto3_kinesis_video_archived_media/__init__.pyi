"""
Main interface for kinesis-video-archived-media service.

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesis_video_archived_media import (
        Client,
        KinesisVideoArchivedMediaClient,
        ListFragmentsPaginator,
    )

    session = boto3.Session()

    client: KinesisVideoArchivedMediaClient = boto3.client("kinesis-video-archived-media")
    session_client: KinesisVideoArchivedMediaClient = session.client("kinesis-video-archived-media")

    list_fragments_paginator: ListFragmentsPaginator = client.get_paginator("list_fragments")
    ```
"""
from mypy_boto3_kinesis_video_archived_media.client import KinesisVideoArchivedMediaClient
from mypy_boto3_kinesis_video_archived_media.paginator import ListFragmentsPaginator

Client = KinesisVideoArchivedMediaClient


__all__ = ("Client", "KinesisVideoArchivedMediaClient", "ListFragmentsPaginator")
