"""
Type annotations for marketplace-catalog service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_marketplace_catalog.client import MarketplaceCatalogClient
    from mypy_boto3_marketplace_catalog.paginator import (
        ListChangeSetsPaginator,
        ListEntitiesPaginator,
    )

    session = Session()
    client: MarketplaceCatalogClient = session.client("marketplace-catalog")

    list_change_sets_paginator: ListChangeSetsPaginator = client.get_paginator("list_change_sets")
    list_entities_paginator: ListEntitiesPaginator = client.get_paginator("list_entities")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListChangeSetsRequestPaginateTypeDef,
    ListChangeSetsResponseTypeDef,
    ListEntitiesRequestPaginateTypeDef,
    ListEntitiesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListChangeSetsPaginator", "ListEntitiesPaginator")

if TYPE_CHECKING:
    _ListChangeSetsPaginatorBase = Paginator[ListChangeSetsResponseTypeDef]
else:
    _ListChangeSetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListChangeSetsPaginator(_ListChangeSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/paginator/ListChangeSets.html#MarketplaceCatalog.Paginator.ListChangeSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/paginators/#listchangesetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListChangeSetsRequestPaginateTypeDef]
    ) -> PageIterator[ListChangeSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/paginator/ListChangeSets.html#MarketplaceCatalog.Paginator.ListChangeSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/paginators/#listchangesetspaginator)
        """

if TYPE_CHECKING:
    _ListEntitiesPaginatorBase = Paginator[ListEntitiesResponseTypeDef]
else:
    _ListEntitiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListEntitiesPaginator(_ListEntitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/paginator/ListEntities.html#MarketplaceCatalog.Paginator.ListEntities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/paginators/#listentitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEntitiesRequestPaginateTypeDef]
    ) -> PageIterator[ListEntitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/paginator/ListEntities.html#MarketplaceCatalog.Paginator.ListEntities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/paginators/#listentitiespaginator)
        """
