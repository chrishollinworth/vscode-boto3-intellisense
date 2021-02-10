"""
Main interface for lexv2-runtime service.

Usage::

    ```python
    import boto3
    from mypy_boto3_lexv2_runtime import (
        Client,
        LexRuntimeV2Client,
    )

    session = boto3.Session()

    client: LexRuntimeV2Client = boto3.client("lexv2-runtime")
    session_client: LexRuntimeV2Client = session.client("lexv2-runtime")
    ```
"""
from mypy_boto3_lexv2_runtime.client import LexRuntimeV2Client

Client = LexRuntimeV2Client


__all__ = ("Client", "LexRuntimeV2Client")
