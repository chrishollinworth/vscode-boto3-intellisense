"""
Main interface for memorydb service.

Usage::

    ```python
    import boto3
    from mypy_boto3_memorydb import (
        Client,
        MemoryDBClient,
    )

    session = boto3.Session()

    client: MemoryDBClient = boto3.client("memorydb")
    session_client: MemoryDBClient = session.client("memorydb")
    ```
"""
from .client import MemoryDBClient

Client = MemoryDBClient

__all__ = ("Client", "MemoryDBClient")
