"""
Main interface for inspector-scan service.

Usage::

    ```python
    import boto3
    from mypy_boto3_inspector_scan import (
        Client,
        inspectorscanClient,
    )

    session = boto3.Session()

    client: inspectorscanClient = boto3.client("inspector-scan")
    session_client: inspectorscanClient = session.client("inspector-scan")
    ```
"""

from .client import inspectorscanClient

Client = inspectorscanClient

__all__ = ("Client", "inspectorscanClient")
