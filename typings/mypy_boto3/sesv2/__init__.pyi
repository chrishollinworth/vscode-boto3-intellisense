"""
Main interface for sesv2 service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sesv2 import (
        Client,
        SESV2Client,
    )

    session = boto3.Session()

    client: SESV2Client = boto3.client("sesv2")
    session_client: SESV2Client = session.client("sesv2")
    ```
"""
from .client import SESV2Client

Client = SESV2Client

__all__ = ("Client", "SESV2Client")
