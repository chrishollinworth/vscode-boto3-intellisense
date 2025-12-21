"""
Main interface for outposts service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_outposts/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_outposts import (
        Client,
        GetOutpostBillingInformationPaginator,
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
        OutpostsClient,
    )

    session = Session()
    client: OutpostsClient = session.client("outposts")

    get_outpost_billing_information_paginator: GetOutpostBillingInformationPaginator = client.get_paginator("get_outpost_billing_information")
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

from .client import OutpostsClient
from .paginator import (
    GetOutpostBillingInformationPaginator,
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

Client = OutpostsClient

__all__ = (
    "Client",
    "GetOutpostBillingInformationPaginator",
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
    "OutpostsClient",
)
