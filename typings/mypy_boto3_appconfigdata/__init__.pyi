"""
Main interface for appconfigdata service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appconfigdata/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_appconfigdata import (
        AppConfigDataClient,
        Client,
    )

    session = Session()
    client: AppConfigDataClient = session.client("appconfigdata")
    ```
"""

from .client import AppConfigDataClient

Client = AppConfigDataClient

__all__ = ("AppConfigDataClient", "Client")
