"""
Main interface for marketplace-catalog service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_marketplace_catalog import (
        Client,
        ListChangeSetsPaginator,
        ListEntitiesPaginator,
        MarketplaceCatalogClient,
    )

    session = Session()
    client: MarketplaceCatalogClient = session.client("marketplace-catalog")

    list_change_sets_paginator: ListChangeSetsPaginator = client.get_paginator("list_change_sets")
    list_entities_paginator: ListEntitiesPaginator = client.get_paginator("list_entities")
    ```
"""

from .client import MarketplaceCatalogClient
from .paginator import ListChangeSetsPaginator, ListEntitiesPaginator

Client = MarketplaceCatalogClient

__all__ = ("Client", "ListChangeSetsPaginator", "ListEntitiesPaginator", "MarketplaceCatalogClient")
