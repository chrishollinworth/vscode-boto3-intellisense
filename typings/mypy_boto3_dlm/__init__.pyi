"""
Main interface for dlm service.

Usage::

    ```python
    import boto3
    from mypy_boto3_dlm import (
        Client,
        DLMClient,
    )

    session = boto3.Session()

    client: DLMClient = boto3.client("dlm")
    session_client: DLMClient = session.client("dlm")
    ```
"""
from mypy_boto3_dlm.client import DLMClient

Client = DLMClient


__all__ = ("Client", "DLMClient")
