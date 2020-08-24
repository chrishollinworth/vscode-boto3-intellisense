"""
Main interface for transcribe service.

Usage::

    ```python
    import boto3
    from mypy_boto3_transcribe import (
        Client,
        TranscribeServiceClient,
    )

    session = boto3.Session()

    client: TranscribeServiceClient = boto3.client("transcribe")
    session_client: TranscribeServiceClient = session.client("transcribe")
    ```
"""
from mypy_boto3_transcribe.client import TranscribeServiceClient

Client = TranscribeServiceClient


__all__ = ("Client", "TranscribeServiceClient")
