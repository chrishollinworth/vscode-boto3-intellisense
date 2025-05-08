"""
Main interface for chime-sdk-meetings service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_chime_sdk_meetings import (
        ChimeSDKMeetingsClient,
        Client,
    )

    session = Session()
    client: ChimeSDKMeetingsClient = session.client("chime-sdk-meetings")
    ```
"""

from .client import ChimeSDKMeetingsClient

Client = ChimeSDKMeetingsClient

__all__ = ("ChimeSDKMeetingsClient", "Client")
