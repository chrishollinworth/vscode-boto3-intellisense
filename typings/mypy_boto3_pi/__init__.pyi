"""
Main interface for pi service.

Usage::

    ```python
    import boto3
    from mypy_boto3_pi import (
        Client,
        PIClient,
    )

    session = boto3.Session()

    client: PIClient = boto3.client("pi")
    session_client: PIClient = session.client("pi")
    ```
"""
from .client import PIClient

Client = PIClient

__all__ = ("Client", "PIClient")
