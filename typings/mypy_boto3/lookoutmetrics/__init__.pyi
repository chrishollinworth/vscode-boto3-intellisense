"""
Main interface for lookoutmetrics service.

Usage::

    ```python
    import boto3
    from mypy_boto3_lookoutmetrics import (
        Client,
        LookoutMetricsClient,
    )

    session = boto3.Session()

    client: LookoutMetricsClient = boto3.client("lookoutmetrics")
    session_client: LookoutMetricsClient = session.client("lookoutmetrics")
    ```
"""
from .client import LookoutMetricsClient

Client = LookoutMetricsClient

__all__ = ("Client", "LookoutMetricsClient")
