"""
Main interface for appflow service.

Usage::

    ```python
    import boto3
    from mypy_boto3_appflow import (
        AppflowClient,
        Client,
    )

    session = boto3.Session()

    client: AppflowClient = boto3.client("appflow")
    session_client: AppflowClient = session.client("appflow")
    ```
"""
from mypy_boto3_appflow.client import AppflowClient

Client = AppflowClient


__all__ = ("AppflowClient", "Client")
