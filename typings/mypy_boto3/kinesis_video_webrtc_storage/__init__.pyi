"""
Main interface for kinesis-video-webrtc-storage service.

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesis_video_webrtc_storage import (
        Client,
        KinesisVideoWebRTCStorageClient,
    )

    session = boto3.Session()

    client: KinesisVideoWebRTCStorageClient = boto3.client("kinesis-video-webrtc-storage")
    session_client: KinesisVideoWebRTCStorageClient = session.client("kinesis-video-webrtc-storage")
    ```
"""
from .client import KinesisVideoWebRTCStorageClient

Client = KinesisVideoWebRTCStorageClient

__all__ = ("Client", "KinesisVideoWebRTCStorageClient")
