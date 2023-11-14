"""
Main interface for marketplace-catalog service.

Usage::

    ```python
    import boto3
    from mypy_boto3_marketplace_catalog import (
        Client,
        ListChangeSetsPaginator,
        ListEntitiesPaginator,
        MarketplaceCatalogClient,
    )

    session = boto3.Session()

    client: MarketplaceCatalogClient = boto3.client("marketplace-catalog")
    session_client: MarketplaceCatalogClient = session.client("marketplace-catalog")

    list_change_sets_paginator: ListChangeSetsPaginator = client.get_paginator("list_change_sets")
    list_entities_paginator: ListEntitiesPaginator = client.get_paginator("list_entities")
    ```
"""
from .client import MarketplaceCatalogClient
from .paginator import ListChangeSetsPaginator, ListEntitiesPaginator

Client = MarketplaceCatalogClient

__all__ = ("Client", "ListChangeSetsPaginator", "ListEntitiesPaginator", "MarketplaceCatalogClient")
