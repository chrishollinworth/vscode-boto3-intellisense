"""
Main interface for codeconnections service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_codeconnections import (
        Client,
        CodeConnectionsClient,
    )

    session = Session()
    client: CodeConnectionsClient = session.client("codeconnections")
    ```
"""

from .client import CodeConnectionsClient

Client = CodeConnectionsClient

__all__ = ("Client", "CodeConnectionsClient")
