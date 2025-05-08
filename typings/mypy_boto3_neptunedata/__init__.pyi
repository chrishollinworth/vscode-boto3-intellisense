"""
Main interface for neptunedata service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_neptunedata import (
        Client,
        NeptuneDataClient,
    )

    session = Session()
    client: NeptuneDataClient = session.client("neptunedata")
    ```
"""

from .client import NeptuneDataClient

Client = NeptuneDataClient

__all__ = ("Client", "NeptuneDataClient")
