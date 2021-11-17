"""
Main interface for chime-sdk-meetings service.

Usage::

    ```python
    import boto3
    from mypy_boto3_chime_sdk_meetings import (
        ChimeSDKMeetingsClient,
        Client,
    )

    session = boto3.Session()

    client: ChimeSDKMeetingsClient = boto3.client("chime-sdk-meetings")
    session_client: ChimeSDKMeetingsClient = session.client("chime-sdk-meetings")
    ```
"""
from .client import ChimeSDKMeetingsClient

Client = ChimeSDKMeetingsClient

__all__ = ("ChimeSDKMeetingsClient", "Client")
