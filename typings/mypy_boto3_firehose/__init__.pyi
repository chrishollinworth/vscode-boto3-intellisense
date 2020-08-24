"""
Main interface for firehose service.

Usage::

    ```python
    import boto3
    from mypy_boto3_firehose import (
        Client,
        FirehoseClient,
    )

    session = boto3.Session()

    client: FirehoseClient = boto3.client("firehose")
    session_client: FirehoseClient = session.client("firehose")
    ```
"""
from mypy_boto3_firehose.client import FirehoseClient

Client = FirehoseClient


__all__ = ("Client", "FirehoseClient")
