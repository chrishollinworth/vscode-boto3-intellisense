"""
Main interface for marketplacecommerceanalytics service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplacecommerceanalytics/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_marketplacecommerceanalytics import (
        Client,
        MarketplaceCommerceAnalyticsClient,
    )

    session = Session()
    client: MarketplaceCommerceAnalyticsClient = session.client("marketplacecommerceanalytics")
    ```
"""

from .client import MarketplaceCommerceAnalyticsClient

Client = MarketplaceCommerceAnalyticsClient

__all__ = ("Client", "MarketplaceCommerceAnalyticsClient")
