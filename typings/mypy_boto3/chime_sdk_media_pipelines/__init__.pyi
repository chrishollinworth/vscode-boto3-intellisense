"""
Main interface for chime-sdk-media-pipelines service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_chime_sdk_media_pipelines import (
        ChimeSDKMediaPipelinesClient,
        Client,
    )

    session = Session()
    client: ChimeSDKMediaPipelinesClient = session.client("chime-sdk-media-pipelines")
    ```
"""

from .client import ChimeSDKMediaPipelinesClient

Client = ChimeSDKMediaPipelinesClient

__all__ = ("ChimeSDKMediaPipelinesClient", "Client")
