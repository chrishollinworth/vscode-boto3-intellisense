"""
Main interface for marketplace-reporting service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_reporting/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_marketplace_reporting import (
        Client,
        MarketplaceReportingServiceClient,
    )

    session = Session()
    client: MarketplaceReportingServiceClient = session.client("marketplace-reporting")
    ```
"""

from .client import MarketplaceReportingServiceClient

Client = MarketplaceReportingServiceClient

__all__ = ("Client", "MarketplaceReportingServiceClient")
