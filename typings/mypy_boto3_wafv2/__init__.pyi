"""
Main interface for wafv2 service.

Usage::

    ```python
    import boto3
    from mypy_boto3_wafv2 import (
        Client,
        WAFV2Client,
    )

    session = boto3.Session()

    client: WAFV2Client = boto3.client("wafv2")
    session_client: WAFV2Client = session.client("wafv2")
    ```
"""
from .client import WAFV2Client

Client = WAFV2Client

__all__ = ("Client", "WAFV2Client")
