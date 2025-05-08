"""
Main interface for opensearchserverless service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opensearchserverless/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_opensearchserverless import (
        Client,
        OpenSearchServiceServerlessClient,
    )

    session = Session()
    client: OpenSearchServiceServerlessClient = session.client("opensearchserverless")
    ```
"""

from .client import OpenSearchServiceServerlessClient

Client = OpenSearchServiceServerlessClient

__all__ = ("Client", "OpenSearchServiceServerlessClient")
