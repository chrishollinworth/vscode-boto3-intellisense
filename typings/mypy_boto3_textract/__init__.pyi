"""
Main interface for textract service.

Usage::

    ```python
    import boto3
    from mypy_boto3_textract import (
        Client,
        TextractClient,
    )

    session = boto3.Session()

    client: TextractClient = boto3.client("textract")
    session_client: TextractClient = session.client("textract")
    ```
"""
from mypy_boto3_textract.client import TextractClient

Client = TextractClient


__all__ = ("Client", "TextractClient")
