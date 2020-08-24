"""
Main interface for sts service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sts import (
        Client,
        STSClient,
    )

    session = boto3.Session()

    client: STSClient = boto3.client("sts")
    session_client: STSClient = session.client("sts")
    ```
"""
from mypy_boto3_sts.client import STSClient

Client = STSClient


__all__ = ("Client", "STSClient")
