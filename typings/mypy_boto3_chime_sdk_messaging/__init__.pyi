"""
Main interface for chime-sdk-messaging service.

Usage::

    ```python
    import boto3
    from mypy_boto3_chime_sdk_messaging import (
        ChimeSDKMessagingClient,
        Client,
    )

    session = boto3.Session()

    client: ChimeSDKMessagingClient = boto3.client("chime-sdk-messaging")
    session_client: ChimeSDKMessagingClient = session.client("chime-sdk-messaging")
    ```
"""
from .client import ChimeSDKMessagingClient

Client = ChimeSDKMessagingClient

__all__ = ("ChimeSDKMessagingClient", "Client")
