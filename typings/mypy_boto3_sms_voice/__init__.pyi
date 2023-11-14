"""
Main interface for sms-voice service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sms_voice import (
        Client,
        PinpointSMSVoiceClient,
    )

    session = boto3.Session()

    client: PinpointSMSVoiceClient = boto3.client("sms-voice")
    session_client: PinpointSMSVoiceClient = session.client("sms-voice")
    ```
"""
from .client import PinpointSMSVoiceClient

Client = PinpointSMSVoiceClient

__all__ = ("Client", "PinpointSMSVoiceClient")
