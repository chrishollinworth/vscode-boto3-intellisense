"""
Main interface for sms-voice service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sms_voice import (
        Client,
        SMSVoiceClient,
    )

    session = boto3.Session()

    client: SMSVoiceClient = boto3.client("sms-voice")
    session_client: SMSVoiceClient = session.client("sms-voice")
    ```
"""
from mypy_boto3_sms_voice.client import SMSVoiceClient

Client = SMSVoiceClient


__all__ = ("Client", "SMSVoiceClient")
