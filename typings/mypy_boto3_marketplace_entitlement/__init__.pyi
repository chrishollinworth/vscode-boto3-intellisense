"""
Main interface for marketplace-entitlement service.

Usage::

    ```python
    import boto3
    from mypy_boto3_marketplace_entitlement import (
        Client,
        GetEntitlementsPaginator,
        MarketplaceEntitlementServiceClient,
    )

    session = boto3.Session()

    client: MarketplaceEntitlementServiceClient = boto3.client("marketplace-entitlement")
    session_client: MarketplaceEntitlementServiceClient = session.client("marketplace-entitlement")

    get_entitlements_paginator: GetEntitlementsPaginator = client.get_paginator("get_entitlements")
    ```
"""
from .client import MarketplaceEntitlementServiceClient
from .paginator import GetEntitlementsPaginator

Client = MarketplaceEntitlementServiceClient

__all__ = ("Client", "GetEntitlementsPaginator", "MarketplaceEntitlementServiceClient")
