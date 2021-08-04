"""
Main interface for kendra service.

Usage::

    ```python
    import boto3
    from mypy_boto3_kendra import (
        Client,
        kendraClient,
    )

    session = boto3.Session()

    client: kendraClient = boto3.client("kendra")
    session_client: kendraClient = session.client("kendra")
    ```
"""
from .client import kendraClient

Client = kendraClient

__all__ = ("Client", "kendraClient")
