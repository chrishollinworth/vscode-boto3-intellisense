"""
Type annotations for outposts service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_outposts import OutpostsClient
    from mypy_boto3_outposts.paginator import (
        GetOutpostInstanceTypesPaginator,
        ListAssetsPaginator,
        ListCatalogItemsPaginator,
        ListOrdersPaginator,
        ListOutpostsPaginator,
        ListSitesPaginator,
    )

    client: OutpostsClient = boto3.client("outposts")

    get_outpost_instance_types_paginator: GetOutpostInstanceTypesPaginator = client.get_paginator("get_outpost_instance_types")
    list_assets_paginator: ListAssetsPaginator = client.get_paginator("list_assets")
    list_catalog_items_paginator: ListCatalogItemsPaginator = client.get_paginator("list_catalog_items")
    list_orders_paginator: ListOrdersPaginator = client.get_paginator("list_orders")
    list_outposts_paginator: ListOutpostsPaginator = client.get_paginator("list_outposts")
    list_sites_paginator: ListSitesPaginator = client.get_paginator("list_sites")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import AssetStateType, CatalogItemClassType, SupportedStorageEnumType
from .type_defs import (
    GetOutpostInstanceTypesOutputTypeDef,
    ListAssetsOutputTypeDef,
    ListCatalogItemsOutputTypeDef,
    ListOrdersOutputTypeDef,
    ListOutpostsOutputTypeDef,
    ListSitesOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetOutpostInstanceTypesPaginator",
    "ListAssetsPaginator",
    "ListCatalogItemsPaginator",
    "ListOrdersPaginator",
    "ListOutpostsPaginator",
    "ListSitesPaginator",
)

class GetOutpostInstanceTypesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/outposts.html#Outposts.Paginator.GetOutpostInstanceTypes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#getoutpostinstancetypespaginator)
    """

    def paginate(
        self, *, OutpostId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetOutpostInstanceTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/outposts.html#Outposts.Paginator.GetOutpostInstanceTypes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#getoutpostinstancetypespaginator)
        """

class ListAssetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/outposts.html#Outposts.Paginator.ListAssets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listassetspaginator)
    """

    def paginate(
        self,
        *,
        OutpostIdentifier: str,
        HostIdFilter: List[str] = None,
        StatusFilter: List[AssetStateType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/outposts.html#Outposts.Paginator.ListAssets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listassetspaginator)
        """

class ListCatalogItemsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/outposts.html#Outposts.Paginator.ListCatalogItems)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listcatalogitemspaginator)
    """

    def paginate(
        self,
        *,
        ItemClassFilter: List[CatalogItemClassType] = None,
        SupportedStorageFilter: List[SupportedStorageEnumType] = None,
        EC2FamilyFilter: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCatalogItemsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/outposts.html#Outposts.Paginator.ListCatalogItems.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listcatalogitemspaginator)
        """

class ListOrdersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/outposts.html#Outposts.Paginator.ListOrders)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listorderspaginator)
    """

    def paginate(
        self,
        *,
        OutpostIdentifierFilter: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOrdersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/outposts.html#Outposts.Paginator.ListOrders.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listorderspaginator)
        """

class ListOutpostsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/outposts.html#Outposts.Paginator.ListOutposts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listoutpostspaginator)
    """

    def paginate(
        self,
        *,
        LifeCycleStatusFilter: List[str] = None,
        AvailabilityZoneFilter: List[str] = None,
        AvailabilityZoneIdFilter: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOutpostsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/outposts.html#Outposts.Paginator.ListOutposts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listoutpostspaginator)
        """

class ListSitesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/outposts.html#Outposts.Paginator.ListSites)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listsitespaginator)
    """

    def paginate(
        self,
        *,
        OperatingAddressCountryCodeFilter: List[str] = None,
        OperatingAddressStateOrRegionFilter: List[str] = None,
        OperatingAddressCityFilter: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSitesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/outposts.html#Outposts.Paginator.ListSites.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listsitespaginator)
        """
