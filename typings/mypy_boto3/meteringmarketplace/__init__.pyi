"""
Main interface for meteringmarketplace service.

Usage::

    ```python
    import boto3
    from mypy_boto3_meteringmarketplace import (
        Client,
        MarketplaceMeteringClient,
    )

    session = boto3.Session()

    client: MarketplaceMeteringClient = boto3.client("meteringmarketplace")
    session_client: MarketplaceMeteringClient = session.client("meteringmarketplace")
    ```
"""
from .client import MarketplaceMeteringClient

Client = MarketplaceMeteringClient

__all__ = ("Client", "MarketplaceMeteringClient")
