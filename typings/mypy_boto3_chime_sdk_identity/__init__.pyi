"""
Main interface for chime-sdk-identity service.

Usage::

    ```python
    import boto3
    from mypy_boto3_chime_sdk_identity import (
        ChimeSDKIdentityClient,
        Client,
    )

    session = boto3.Session()

    client: ChimeSDKIdentityClient = boto3.client("chime-sdk-identity")
    session_client: ChimeSDKIdentityClient = session.client("chime-sdk-identity")
    ```
"""
from .client import ChimeSDKIdentityClient

Client = ChimeSDKIdentityClient

__all__ = ("ChimeSDKIdentityClient", "Client")
