"""
Main interface for apprunner service.

Usage::

    ```python
    import boto3
    from mypy_boto3_apprunner import (
        AppRunnerClient,
        Client,
    )

    session = boto3.Session()

    client: AppRunnerClient = boto3.client("apprunner")
    session_client: AppRunnerClient = session.client("apprunner")
    ```
"""
from .client import AppRunnerClient

Client = AppRunnerClient

__all__ = ("AppRunnerClient", "Client")
