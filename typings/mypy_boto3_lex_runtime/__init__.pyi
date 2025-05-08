"""
Main interface for lex-runtime service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_lex_runtime import (
        Client,
        LexRuntimeServiceClient,
    )

    session = Session()
    client: LexRuntimeServiceClient = session.client("lex-runtime")
    ```
"""

from .client import LexRuntimeServiceClient

Client = LexRuntimeServiceClient

__all__ = ("Client", "LexRuntimeServiceClient")
