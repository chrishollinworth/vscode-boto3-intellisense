"""
Main interface for support-app service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support_app/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_support_app import (
        Client,
        SupportAppClient,
    )

    session = Session()
    client: SupportAppClient = session.client("support-app")
    ```
"""

from .client import SupportAppClient

Client = SupportAppClient

__all__ = ("Client", "SupportAppClient")
