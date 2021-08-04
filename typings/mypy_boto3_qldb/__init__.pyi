"""
Main interface for qldb service.

Usage::

    ```python
    import boto3
    from mypy_boto3_qldb import (
        Client,
        QLDBClient,
    )

    session = boto3.Session()

    client: QLDBClient = boto3.client("qldb")
    session_client: QLDBClient = session.client("qldb")
    ```
"""
from .client import QLDBClient

Client = QLDBClient

__all__ = ("Client", "QLDBClient")
