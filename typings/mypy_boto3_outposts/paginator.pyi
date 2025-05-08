"""
Type annotations for outposts service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_outposts.client import OutpostsClient
    from mypy_boto3_outposts.paginator import (
        GetOutpostInstanceTypesPaginator,
        GetOutpostSupportedInstanceTypesPaginator,
        ListAssetInstancesPaginator,
        ListAssetsPaginator,
        ListBlockingInstancesForCapacityTaskPaginator,
        ListCapacityTasksPaginator,
        ListCatalogItemsPaginator,
        ListOrdersPaginator,
        ListOutpostsPaginator,
        ListSitesPaginator,
    )

    session = Session()
    client: OutpostsClient = session.client("outposts")

    get_outpost_instance_types_paginator: GetOutpostInstanceTypesPaginator = client.get_paginator("get_outpost_instance_types")
    get_outpost_supported_instance_types_paginator: GetOutpostSupportedInstanceTypesPaginator = client.get_paginator("get_outpost_supported_instance_types")
    list_asset_instances_paginator: ListAssetInstancesPaginator = client.get_paginator("list_asset_instances")
    list_assets_paginator: ListAssetsPaginator = client.get_paginator("list_assets")
    list_blocking_instances_for_capacity_task_paginator: ListBlockingInstancesForCapacityTaskPaginator = client.get_paginator("list_blocking_instances_for_capacity_task")
    list_capacity_tasks_paginator: ListCapacityTasksPaginator = client.get_paginator("list_capacity_tasks")
    list_catalog_items_paginator: ListCatalogItemsPaginator = client.get_paginator("list_catalog_items")
    list_orders_paginator: ListOrdersPaginator = client.get_paginator("list_orders")
    list_outposts_paginator: ListOutpostsPaginator = client.get_paginator("list_outposts")
    list_sites_paginator: ListSitesPaginator = client.get_paginator("list_sites")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetOutpostInstanceTypesInputPaginateTypeDef,
    GetOutpostInstanceTypesOutputTypeDef,
    GetOutpostSupportedInstanceTypesInputPaginateTypeDef,
    GetOutpostSupportedInstanceTypesOutputTypeDef,
    ListAssetInstancesInputPaginateTypeDef,
    ListAssetInstancesOutputTypeDef,
    ListAssetsInputPaginateTypeDef,
    ListAssetsOutputTypeDef,
    ListBlockingInstancesForCapacityTaskInputPaginateTypeDef,
    ListBlockingInstancesForCapacityTaskOutputTypeDef,
    ListCapacityTasksInputPaginateTypeDef,
    ListCapacityTasksOutputTypeDef,
    ListCatalogItemsInputPaginateTypeDef,
    ListCatalogItemsOutputTypeDef,
    ListOrdersInputPaginateTypeDef,
    ListOrdersOutputTypeDef,
    ListOutpostsInputPaginateTypeDef,
    ListOutpostsOutputTypeDef,
    ListSitesInputPaginateTypeDef,
    ListSitesOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetOutpostInstanceTypesPaginator",
    "GetOutpostSupportedInstanceTypesPaginator",
    "ListAssetInstancesPaginator",
    "ListAssetsPaginator",
    "ListBlockingInstancesForCapacityTaskPaginator",
    "ListCapacityTasksPaginator",
    "ListCatalogItemsPaginator",
    "ListOrdersPaginator",
    "ListOutpostsPaginator",
    "ListSitesPaginator",
)

if TYPE_CHECKING:
    _GetOutpostInstanceTypesPaginatorBase = Paginator[GetOutpostInstanceTypesOutputTypeDef]
else:
    _GetOutpostInstanceTypesPaginatorBase = Paginator  # type: ignore[assignment]

class GetOutpostInstanceTypesPaginator(_GetOutpostInstanceTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/GetOutpostInstanceTypes.html#Outposts.Paginator.GetOutpostInstanceTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#getoutpostinstancetypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetOutpostInstanceTypesInputPaginateTypeDef]
    ) -> PageIterator[GetOutpostInstanceTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/GetOutpostInstanceTypes.html#Outposts.Paginator.GetOutpostInstanceTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#getoutpostinstancetypespaginator)
        """

if TYPE_CHECKING:
    _GetOutpostSupportedInstanceTypesPaginatorBase = Paginator[
        GetOutpostSupportedInstanceTypesOutputTypeDef
    ]
else:
    _GetOutpostSupportedInstanceTypesPaginatorBase = Paginator  # type: ignore[assignment]

class GetOutpostSupportedInstanceTypesPaginator(_GetOutpostSupportedInstanceTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/GetOutpostSupportedInstanceTypes.html#Outposts.Paginator.GetOutpostSupportedInstanceTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#getoutpostsupportedinstancetypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetOutpostSupportedInstanceTypesInputPaginateTypeDef]
    ) -> PageIterator[GetOutpostSupportedInstanceTypesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/GetOutpostSupportedInstanceTypes.html#Outposts.Paginator.GetOutpostSupportedInstanceTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#getoutpostsupportedinstancetypespaginator)
        """

if TYPE_CHECKING:
    _ListAssetInstancesPaginatorBase = Paginator[ListAssetInstancesOutputTypeDef]
else:
    _ListAssetInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssetInstancesPaginator(_ListAssetInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListAssetInstances.html#Outposts.Paginator.ListAssetInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listassetinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssetInstancesInputPaginateTypeDef]
    ) -> PageIterator[ListAssetInstancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListAssetInstances.html#Outposts.Paginator.ListAssetInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listassetinstancespaginator)
        """

if TYPE_CHECKING:
    _ListAssetsPaginatorBase = Paginator[ListAssetsOutputTypeDef]
else:
    _ListAssetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssetsPaginator(_ListAssetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListAssets.html#Outposts.Paginator.ListAssets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listassetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssetsInputPaginateTypeDef]
    ) -> PageIterator[ListAssetsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListAssets.html#Outposts.Paginator.ListAssets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listassetspaginator)
        """

if TYPE_CHECKING:
    _ListBlockingInstancesForCapacityTaskPaginatorBase = Paginator[
        ListBlockingInstancesForCapacityTaskOutputTypeDef
    ]
else:
    _ListBlockingInstancesForCapacityTaskPaginatorBase = Paginator  # type: ignore[assignment]

class ListBlockingInstancesForCapacityTaskPaginator(
    _ListBlockingInstancesForCapacityTaskPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListBlockingInstancesForCapacityTask.html#Outposts.Paginator.ListBlockingInstancesForCapacityTask)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listblockinginstancesforcapacitytaskpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBlockingInstancesForCapacityTaskInputPaginateTypeDef]
    ) -> PageIterator[ListBlockingInstancesForCapacityTaskOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListBlockingInstancesForCapacityTask.html#Outposts.Paginator.ListBlockingInstancesForCapacityTask.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listblockinginstancesforcapacitytaskpaginator)
        """

if TYPE_CHECKING:
    _ListCapacityTasksPaginatorBase = Paginator[ListCapacityTasksOutputTypeDef]
else:
    _ListCapacityTasksPaginatorBase = Paginator  # type: ignore[assignment]

class ListCapacityTasksPaginator(_ListCapacityTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListCapacityTasks.html#Outposts.Paginator.ListCapacityTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listcapacitytaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCapacityTasksInputPaginateTypeDef]
    ) -> PageIterator[ListCapacityTasksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListCapacityTasks.html#Outposts.Paginator.ListCapacityTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listcapacitytaskspaginator)
        """

if TYPE_CHECKING:
    _ListCatalogItemsPaginatorBase = Paginator[ListCatalogItemsOutputTypeDef]
else:
    _ListCatalogItemsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCatalogItemsPaginator(_ListCatalogItemsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListCatalogItems.html#Outposts.Paginator.ListCatalogItems)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listcatalogitemspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCatalogItemsInputPaginateTypeDef]
    ) -> PageIterator[ListCatalogItemsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListCatalogItems.html#Outposts.Paginator.ListCatalogItems.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listcatalogitemspaginator)
        """

if TYPE_CHECKING:
    _ListOrdersPaginatorBase = Paginator[ListOrdersOutputTypeDef]
else:
    _ListOrdersPaginatorBase = Paginator  # type: ignore[assignment]

class ListOrdersPaginator(_ListOrdersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListOrders.html#Outposts.Paginator.ListOrders)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listorderspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOrdersInputPaginateTypeDef]
    ) -> PageIterator[ListOrdersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListOrders.html#Outposts.Paginator.ListOrders.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listorderspaginator)
        """

if TYPE_CHECKING:
    _ListOutpostsPaginatorBase = Paginator[ListOutpostsOutputTypeDef]
else:
    _ListOutpostsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOutpostsPaginator(_ListOutpostsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListOutposts.html#Outposts.Paginator.ListOutposts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listoutpostspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOutpostsInputPaginateTypeDef]
    ) -> PageIterator[ListOutpostsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListOutposts.html#Outposts.Paginator.ListOutposts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listoutpostspaginator)
        """

if TYPE_CHECKING:
    _ListSitesPaginatorBase = Paginator[ListSitesOutputTypeDef]
else:
    _ListSitesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSitesPaginator(_ListSitesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListSites.html#Outposts.Paginator.ListSites)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listsitespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSitesInputPaginateTypeDef]
    ) -> PageIterator[ListSitesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/outposts/paginator/ListSites.html#Outposts.Paginator.ListSites.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/paginators/#listsitespaginator)
        """
