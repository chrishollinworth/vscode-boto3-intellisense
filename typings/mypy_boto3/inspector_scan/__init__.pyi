"""
Main interface for inspector-scan service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector_scan/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_inspector_scan import (
        Client,
        InspectorscanClient,
    )

    session = Session()
    client: InspectorscanClient = session.client("inspector-scan")
    ```
"""

from .client import InspectorscanClient

Client = InspectorscanClient

__all__ = ("Client", "InspectorscanClient")
