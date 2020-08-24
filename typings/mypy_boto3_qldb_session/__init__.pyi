"""
Main interface for qldb-session service.

Usage::

    ```python
    import boto3
    from mypy_boto3_qldb_session import (
        Client,
        QLDBSessionClient,
    )

    session = boto3.Session()

    client: QLDBSessionClient = boto3.client("qldb-session")
    session_client: QLDBSessionClient = session.client("qldb-session")
    ```
"""
from mypy_boto3_qldb_session.client import QLDBSessionClient

Client = QLDBSessionClient


__all__ = ("Client", "QLDBSessionClient")
