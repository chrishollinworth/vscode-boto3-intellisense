"""
Main interface for waf-regional service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_waf_regional/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_waf_regional import (
        Client,
        WAFRegionalClient,
    )

    session = Session()
    client: WAFRegionalClient = session.client("waf-regional")
    ```
"""

from .client import WAFRegionalClient

Client = WAFRegionalClient

__all__ = ("Client", "WAFRegionalClient")
