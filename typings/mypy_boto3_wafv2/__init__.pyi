"""
Main interface for wafv2 service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_wafv2 import (
        Client,
        WAFV2Client,
    )

    session = Session()
    client: WAFV2Client = session.client("wafv2")
    ```
"""

from .client import WAFV2Client

Client = WAFV2Client

__all__ = ("Client", "WAFV2Client")
