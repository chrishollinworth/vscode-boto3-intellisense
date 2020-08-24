"""
Main interface for iotsitewise service.

Usage::

    ```python
    import boto3
    from mypy_boto3_iotsitewise import (
        AssetActiveWaiter,
        AssetModelActiveWaiter,
        AssetModelNotExistsWaiter,
        AssetNotExistsWaiter,
        Client,
        GetAssetPropertyAggregatesPaginator,
        GetAssetPropertyValueHistoryPaginator,
        IoTSiteWiseClient,
        ListAccessPoliciesPaginator,
        ListAssetModelsPaginator,
        ListAssetsPaginator,
        ListAssociatedAssetsPaginator,
        ListDashboardsPaginator,
        ListGatewaysPaginator,
        ListPortalsPaginator,
        ListProjectAssetsPaginator,
        ListProjectsPaginator,
        PortalActiveWaiter,
        PortalNotExistsWaiter,
    )

    session = boto3.Session()

    client: IoTSiteWiseClient = boto3.client("iotsitewise")
    session_client: IoTSiteWiseClient = session.client("iotsitewise")

    asset_active_waiter: AssetActiveWaiter = client.get_waiter("asset_active")
    asset_model_active_waiter: AssetModelActiveWaiter = client.get_waiter("asset_model_active")
    asset_model_not_exists_waiter: AssetModelNotExistsWaiter = client.get_waiter("asset_model_not_exists")
    asset_not_exists_waiter: AssetNotExistsWaiter = client.get_waiter("asset_not_exists")
    portal_active_waiter: PortalActiveWaiter = client.get_waiter("portal_active")
    portal_not_exists_waiter: PortalNotExistsWaiter = client.get_waiter("portal_not_exists")

    get_asset_property_aggregates_paginator: GetAssetPropertyAggregatesPaginator = client.get_paginator("get_asset_property_aggregates")
    get_asset_property_value_history_paginator: GetAssetPropertyValueHistoryPaginator = client.get_paginator("get_asset_property_value_history")
    list_access_policies_paginator: ListAccessPoliciesPaginator = client.get_paginator("list_access_policies")
    list_asset_models_paginator: ListAssetModelsPaginator = client.get_paginator("list_asset_models")
    list_assets_paginator: ListAssetsPaginator = client.get_paginator("list_assets")
    list_associated_assets_paginator: ListAssociatedAssetsPaginator = client.get_paginator("list_associated_assets")
    list_dashboards_paginator: ListDashboardsPaginator = client.get_paginator("list_dashboards")
    list_gateways_paginator: ListGatewaysPaginator = client.get_paginator("list_gateways")
    list_portals_paginator: ListPortalsPaginator = client.get_paginator("list_portals")
    list_project_assets_paginator: ListProjectAssetsPaginator = client.get_paginator("list_project_assets")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    ```
"""
from mypy_boto3_iotsitewise.client import IoTSiteWiseClient
from mypy_boto3_iotsitewise.paginator import (
    GetAssetPropertyAggregatesPaginator,
    GetAssetPropertyValueHistoryPaginator,
    ListAccessPoliciesPaginator,
    ListAssetModelsPaginator,
    ListAssetsPaginator,
    ListAssociatedAssetsPaginator,
    ListDashboardsPaginator,
    ListGatewaysPaginator,
    ListPortalsPaginator,
    ListProjectAssetsPaginator,
    ListProjectsPaginator,
)
from mypy_boto3_iotsitewise.waiter import (
    AssetActiveWaiter,
    AssetModelActiveWaiter,
    AssetModelNotExistsWaiter,
    AssetNotExistsWaiter,
    PortalActiveWaiter,
    PortalNotExistsWaiter,
)

Client = IoTSiteWiseClient


__all__ = (
    "AssetActiveWaiter",
    "AssetModelActiveWaiter",
    "AssetModelNotExistsWaiter",
    "AssetNotExistsWaiter",
    "Client",
    "GetAssetPropertyAggregatesPaginator",
    "GetAssetPropertyValueHistoryPaginator",
    "IoTSiteWiseClient",
    "ListAccessPoliciesPaginator",
    "ListAssetModelsPaginator",
    "ListAssetsPaginator",
    "ListAssociatedAssetsPaginator",
    "ListDashboardsPaginator",
    "ListGatewaysPaginator",
    "ListPortalsPaginator",
    "ListProjectAssetsPaginator",
    "ListProjectsPaginator",
    "PortalActiveWaiter",
    "PortalNotExistsWaiter",
)
