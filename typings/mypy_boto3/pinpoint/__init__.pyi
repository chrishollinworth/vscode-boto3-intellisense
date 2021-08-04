"""
Main interface for pinpoint service.

Usage::

    ```python
    import boto3
    from mypy_boto3_pinpoint import (
        Client,
        PinpointClient,
    )

    session = boto3.Session()

    client: PinpointClient = boto3.client("pinpoint")
    session_client: PinpointClient = session.client("pinpoint")
    ```
"""
from .client import PinpointClient

Client = PinpointClient

__all__ = ("Client", "PinpointClient")
