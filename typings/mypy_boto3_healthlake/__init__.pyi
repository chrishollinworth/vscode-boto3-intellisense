"""
Main interface for healthlake service.

Usage::

    ```python
    import boto3
    from mypy_boto3_healthlake import (
        Client,
        HealthLakeClient,
    )

    session = boto3.Session()

    client: HealthLakeClient = boto3.client("healthlake")
    session_client: HealthLakeClient = session.client("healthlake")
    ```
"""
from .client import HealthLakeClient

Client = HealthLakeClient

__all__ = ("Client", "HealthLakeClient")
