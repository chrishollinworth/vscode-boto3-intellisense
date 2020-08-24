"""
Main interface for waf-regional service.

Usage::

    ```python
    import boto3
    from mypy_boto3_waf_regional import (
        Client,
        WAFRegionalClient,
    )

    session = boto3.Session()

    client: WAFRegionalClient = boto3.client("waf-regional")
    session_client: WAFRegionalClient = session.client("waf-regional")
    ```
"""
from mypy_boto3_waf_regional.client import WAFRegionalClient

Client = WAFRegionalClient


__all__ = ("Client", "WAFRegionalClient")
