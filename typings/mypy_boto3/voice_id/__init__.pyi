"""
Main interface for voice-id service.

Usage::

    ```python
    import boto3
    from mypy_boto3_voice_id import (
        Client,
        VoiceIDClient,
    )

    session = boto3.Session()

    client: VoiceIDClient = boto3.client("voice-id")
    session_client: VoiceIDClient = session.client("voice-id")
    ```
"""
from .client import VoiceIDClient

Client = VoiceIDClient

__all__ = ("Client", "VoiceIDClient")
