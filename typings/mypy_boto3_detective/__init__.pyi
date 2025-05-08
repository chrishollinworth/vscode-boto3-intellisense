"""
Main interface for detective service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_detective/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_detective import (
        Client,
        DetectiveClient,
    )

    session = Session()
    client: DetectiveClient = session.client("detective")
    ```
"""

from .client import DetectiveClient

Client = DetectiveClient

__all__ = ("Client", "DetectiveClient")
