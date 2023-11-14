"""
Main interface for chime-sdk-media-pipelines service.

Usage::

    ```python
    import boto3
    from mypy_boto3_chime_sdk_media_pipelines import (
        ChimeSDKMediaPipelinesClient,
        Client,
    )

    session = boto3.Session()

    client: ChimeSDKMediaPipelinesClient = boto3.client("chime-sdk-media-pipelines")
    session_client: ChimeSDKMediaPipelinesClient = session.client("chime-sdk-media-pipelines")
    ```
"""
from .client import ChimeSDKMediaPipelinesClient

Client = ChimeSDKMediaPipelinesClient

__all__ = ("ChimeSDKMediaPipelinesClient", "Client")
