"""
Main interface for cloudsearch service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cloudsearch import (
        Client,
        CloudSearchClient,
    )

    session = Session()
    client: CloudSearchClient = session.client("cloudsearch")
    ```
"""

from .client import CloudSearchClient

Client = CloudSearchClient

__all__ = ("Client", "CloudSearchClient")
