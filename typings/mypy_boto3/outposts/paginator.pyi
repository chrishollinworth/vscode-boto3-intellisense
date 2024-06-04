"""
Type annotations for outposts service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_outposts import OutpostsClient
    from mypy_boto3_outposts.paginator import (
        GetOutpostInstanceTypesPaginator,
        GetOutpostSupportedInstanceTypesPaginator,
        ListAssetsPaginator,
        ListCapacityTasksPaginator,
        ListCatalogItemsPaginator,
        ListOrdersPaginator,
        ListOutpostsPaginator,
        ListSitesPaginator,
    )

    client: OutpostsClient = boto3.client("outposts")

    get_outpost_instance_types_paginator: GetOutpostInstanceTypesPaginator = client.get_paginator("get_outpost_instance_types")
    get_outpost_supported_instance_types_paginator: GetOutpostSupportedInstanceTypesPaginator = client.get_paginator("get_outpost_supported_instance_types")
    list_assets_paginator: ListAssetsPaginator = client.get_paginator("list_assets")
    list_capacity_tasks_paginator: ListCapacityTasksPaginator = client.get_paginator("list_capacity_tasks")
    list_catalog_items_paginator: ListCatalogItemsPaginator = client.get_paginator("list_catalog_items")
    list_orders_paginator: ListOrdersPaginator = client.get_paginator("list_orders")
    list_outposts_paginator: ListOutpostsPaginator = client.get_paginator("list_outposts")
    list_sites_paginator: ListSitesPaginator = client.get_paginator("list_sites")
    ```
"""

from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    AssetStateType,
    CapacityTaskStatusType,
    CatalogItemClassType,
    SupportedStorageEnumType,
)
from .type_defs import (
    GetOutpostInstanceTypesOutputTypeDef,
    GetOutpostSupportedInstanceTypesOutputTypeDef,
    ListAssetsOutputTypeDef,
    ListCapacityTasksOutputTypeDef,
    ListCatalogItemsOutputTypeDef,
    ListOrdersOutputTypeDef,
    ListOutpostsOutputTypeDef,
    ListSitesOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "GetOutpostInstanceTypesPaginator",
    "GetOutpostSupportedInstanceTypesPaginator",
    "ListAssetsPaginator",
    "ListCapacityTasksPaginator",
    "ListCatalogItemsPaginator",
    "ListOrdersPaginator",
    "ListOutpostsPaginator",
    "ListSitesPaginator",
)

class GetOutpostInstanceTypesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.GetOutpostInstanceTypes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#getoutpostinstancetypespaginator)
    """

    def paginate(
        self, *, OutpostId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetOutpostInstanceTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.GetOutpostInstanceTypes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#getoutpostinstancetypespaginator)
        """

class GetOutpostSupportedInstanceTypesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.GetOutpostSupportedInstanceTypes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#getoutpostsupportedinstancetypespaginator)
    """

    def paginate(
        self,
        *,
        OutpostIdentifier: str,
        OrderId: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetOutpostSupportedInstanceTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.GetOutpostSupportedInstanceTypes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#getoutpostsupportedinstancetypespaginator)
        """

class ListAssetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.ListAssets)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.ListAssets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listassetspaginator)
        """

class ListCapacityTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.ListCapacityTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listcapacitytaskspaginator)
    """

    def paginate(
        self,
        *,
        OutpostIdentifierFilter: str = None,
        CapacityTaskStatusFilter: List[CapacityTaskStatusType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCapacityTasksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.ListCapacityTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listcapacitytaskspaginator)
        """

class ListCatalogItemsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.ListCatalogItems)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.ListCatalogItems.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listcatalogitemspaginator)
        """

class ListOrdersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.ListOrders)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listorderspaginator)
    """

    def paginate(
        self,
        *,
        OutpostIdentifierFilter: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOrdersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.ListOrders.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listorderspaginator)
        """

class ListOutpostsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.ListOutposts)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.ListOutposts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listoutpostspaginator)
        """

class ListSitesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.ListSites)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/outposts.html#Outposts.Paginator.ListSites.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators.html#listsitespaginator)
        """
