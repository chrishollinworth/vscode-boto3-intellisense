"""
Main interface for osis service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_osis import (
        Client,
        OpenSearchIngestionClient,
    )

    session = Session()
    client: OpenSearchIngestionClient = session.client("osis")
    ```
"""

from .client import OpenSearchIngestionClient

Client = OpenSearchIngestionClient

__all__ = ("Client", "OpenSearchIngestionClient")
