"""
Main interface for codestar-connections service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_codestar_connections import (
        Client,
        CodeStarconnectionsClient,
    )

    session = Session()
    client: CodeStarconnectionsClient = session.client("codestar-connections")
    ```
"""

from .client import CodeStarconnectionsClient

Client = CodeStarconnectionsClient

__all__ = ("Client", "CodeStarconnectionsClient")
