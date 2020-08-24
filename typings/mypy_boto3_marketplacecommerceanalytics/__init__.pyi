"""
Main interface for marketplacecommerceanalytics service.

Usage::

    ```python
    import boto3
    from mypy_boto3_marketplacecommerceanalytics import (
        Client,
        MarketplaceCommerceAnalyticsClient,
    )

    session = boto3.Session()

    client: MarketplaceCommerceAnalyticsClient = boto3.client("marketplacecommerceanalytics")
    session_client: MarketplaceCommerceAnalyticsClient = session.client("marketplacecommerceanalytics")
    ```
"""
from mypy_boto3_marketplacecommerceanalytics.client import MarketplaceCommerceAnalyticsClient

Client = MarketplaceCommerceAnalyticsClient


__all__ = ("Client", "MarketplaceCommerceAnalyticsClient")
