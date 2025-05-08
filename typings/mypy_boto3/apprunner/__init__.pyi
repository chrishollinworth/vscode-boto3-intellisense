"""
Main interface for apprunner service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apprunner/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_apprunner import (
        AppRunnerClient,
        Client,
    )

    session = Session()
    client: AppRunnerClient = session.client("apprunner")
    ```
"""

from .client import AppRunnerClient

Client = AppRunnerClient

__all__ = ("AppRunnerClient", "Client")
