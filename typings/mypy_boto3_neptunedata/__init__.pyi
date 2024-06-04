"""
Main interface for neptunedata service.

Usage::

    ```python
    import boto3
    from mypy_boto3_neptunedata import (
        Client,
        NeptuneDataClient,
    )

    session = boto3.Session()

    client: NeptuneDataClient = boto3.client("neptunedata")
    session_client: NeptuneDataClient = session.client("neptunedata")
    ```
"""

from .client import NeptuneDataClient

Client = NeptuneDataClient

__all__ = ("Client", "NeptuneDataClient")
