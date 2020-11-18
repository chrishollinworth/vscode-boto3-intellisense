"""
Main interface for honeycode service.

Usage::

    ```python
    import boto3
    from mypy_boto3_honeycode import (
        Client,
        HoneycodeClient,
    )

    session = boto3.Session()

    client: HoneycodeClient = boto3.client("honeycode")
    session_client: HoneycodeClient = session.client("honeycode")
    ```
"""
from mypy_boto3_honeycode.client import HoneycodeClient

Client = HoneycodeClient


__all__ = ("Client", "HoneycodeClient")
