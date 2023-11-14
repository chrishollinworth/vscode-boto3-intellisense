"""
Main interface for ce service.

Usage::

    ```python
    import boto3
    from mypy_boto3_ce import (
        Client,
        CostExplorerClient,
    )

    session = boto3.Session()

    client: CostExplorerClient = boto3.client("ce")
    session_client: CostExplorerClient = session.client("ce")
    ```
"""
from .client import CostExplorerClient

Client = CostExplorerClient

__all__ = ("Client", "CostExplorerClient")
