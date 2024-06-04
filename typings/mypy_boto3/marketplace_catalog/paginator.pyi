"""
Type annotations for marketplace-catalog service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_marketplace_catalog import MarketplaceCatalogClient
    from mypy_boto3_marketplace_catalog.paginator import (
        ListChangeSetsPaginator,
        ListEntitiesPaginator,
    )

    client: MarketplaceCatalogClient = boto3.client("marketplace-catalog")

    list_change_sets_paginator: ListChangeSetsPaginator = client.get_paginator("list_change_sets")
    list_entities_paginator: ListEntitiesPaginator = client.get_paginator("list_entities")
    ```
"""

from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import OwnershipTypeType
from .type_defs import (
    EntityTypeFiltersTypeDef,
    EntityTypeSortTypeDef,
    FilterTypeDef,
    ListChangeSetsResponseTypeDef,
    ListEntitiesResponseTypeDef,
    PaginatorConfigTypeDef,
    SortTypeDef,
)

__all__ = ("ListChangeSetsPaginator", "ListEntitiesPaginator")

class ListChangeSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Paginator.ListChangeSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/paginators.html#listchangesetspaginator)
    """

    def paginate(
        self,
        *,
        Catalog: str,
        FilterList: List["FilterTypeDef"] = None,
        Sort: "SortTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChangeSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Paginator.ListChangeSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/paginators.html#listchangesetspaginator)
        """

class ListEntitiesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Paginator.ListEntities)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/paginators.html#listentitiespaginator)
    """

    def paginate(
        self,
        *,
        Catalog: str,
        EntityType: str,
        FilterList: List["FilterTypeDef"] = None,
        Sort: "SortTypeDef" = None,
        OwnershipType: OwnershipTypeType = None,
        EntityTypeFilters: "EntityTypeFiltersTypeDef" = None,
        EntityTypeSort: "EntityTypeSortTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEntitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Paginator.ListEntities.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/paginators.html#listentitiespaginator)
        """
