"""
Main interface for kendra service.

Usage::

    ```python
    import boto3
    from mypy_boto3_kendra import (
        Client,
        KendraClient,
    )

    session = boto3.Session()

    client: KendraClient = boto3.client("kendra")
    session_client: KendraClient = session.client("kendra")
    ```
"""
from mypy_boto3_kendra.client import KendraClient

Client = KendraClient


__all__ = ("Client", "KendraClient")
