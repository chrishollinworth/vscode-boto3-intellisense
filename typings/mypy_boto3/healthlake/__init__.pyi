"""
Main interface for healthlake service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_healthlake import (
        Client,
        HealthLakeClient,
    )

    session = Session()
    client: HealthLakeClient = session.client("healthlake")
    ```
"""

from .client import HealthLakeClient

Client = HealthLakeClient

__all__ = ("Client", "HealthLakeClient")
