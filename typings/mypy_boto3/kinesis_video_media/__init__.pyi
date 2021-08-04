"""
Main interface for kinesis-video-media service.

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesis_video_media import (
        Client,
        KinesisVideoMediaClient,
    )

    session = boto3.Session()

    client: KinesisVideoMediaClient = boto3.client("kinesis-video-media")
    session_client: KinesisVideoMediaClient = session.client("kinesis-video-media")
    ```
"""
from .client import KinesisVideoMediaClient

Client = KinesisVideoMediaClient

__all__ = ("Client", "KinesisVideoMediaClient")
