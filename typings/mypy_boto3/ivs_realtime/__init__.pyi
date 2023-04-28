"""
Main interface for ivs-realtime service.

Usage::

    ```python
    import boto3
    from mypy_boto3_ivs_realtime import (
        Client,
        ivsrealtimeClient,
    )

    session = boto3.Session()

    client: ivsrealtimeClient = boto3.client("ivs-realtime")
    session_client: ivsrealtimeClient = session.client("ivs-realtime")
    ```
"""
from .client import ivsrealtimeClient

Client = ivsrealtimeClient

__all__ = ("Client", "ivsrealtimeClient")
