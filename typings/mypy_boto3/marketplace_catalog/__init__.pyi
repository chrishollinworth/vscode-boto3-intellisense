"""
Main interface for marketplace-catalog service.

Usage::

    ```python
    import boto3
    from mypy_boto3_marketplace_catalog import (
        Client,
        MarketplaceCatalogClient,
    )

    session = boto3.Session()

    client: MarketplaceCatalogClient = boto3.client("marketplace-catalog")
    session_client: MarketplaceCatalogClient = session.client("marketplace-catalog")
    ```
"""
from .client import MarketplaceCatalogClient

Client = MarketplaceCatalogClient

__all__ = ("Client", "MarketplaceCatalogClient")
