"""
Main interface for meteringmarketplace service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_meteringmarketplace import (
        Client,
        MarketplaceMeteringClient,
    )

    session = Session()
    client: MarketplaceMeteringClient = session.client("meteringmarketplace")
    ```
"""

from .client import MarketplaceMeteringClient

Client = MarketplaceMeteringClient

__all__ = ("Client", "MarketplaceMeteringClient")
