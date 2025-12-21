"""
Main interface for iotsitewise service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iotsitewise import (
        AssetActiveWaiter,
        AssetModelActiveWaiter,
        AssetModelNotExistsWaiter,
        AssetNotExistsWaiter,
        Client,
        ExecuteQueryPaginator,
        GetAssetPropertyAggregatesPaginator,
        GetAssetPropertyValueHistoryPaginator,
        GetInterpolatedAssetPropertyValuesPaginator,
        IoTSiteWiseClient,
        ListAccessPoliciesPaginator,
        ListActionsPaginator,
        ListAssetModelCompositeModelsPaginator,
        ListAssetModelPropertiesPaginator,
        ListAssetModelsPaginator,
        ListAssetPropertiesPaginator,
        ListAssetRelationshipsPaginator,
        ListAssetsPaginator,
        ListAssociatedAssetsPaginator,
        ListBulkImportJobsPaginator,
        ListCompositionRelationshipsPaginator,
        ListComputationModelDataBindingUsagesPaginator,
        ListComputationModelResolveToResourcesPaginator,
        ListComputationModelsPaginator,
        ListDashboardsPaginator,
        ListDatasetsPaginator,
        ListExecutionsPaginator,
        ListGatewaysPaginator,
        ListInterfaceRelationshipsPaginator,
        ListPortalsPaginator,
        ListProjectAssetsPaginator,
        ListProjectsPaginator,
        ListTimeSeriesPaginator,
        PortalActiveWaiter,
        PortalNotExistsWaiter,
    )

    session = Session()
    client: IoTSiteWiseClient = session.client("iotsitewise")

    asset_active_waiter: AssetActiveWaiter = client.get_waiter("asset_active")
    asset_model_active_waiter: AssetModelActiveWaiter = client.get_waiter("asset_model_active")
    asset_model_not_exists_waiter: AssetModelNotExistsWaiter = client.get_waiter("asset_model_not_exists")
    asset_not_exists_waiter: AssetNotExistsWaiter = client.get_waiter("asset_not_exists")
    portal_active_waiter: PortalActiveWaiter = client.get_waiter("portal_active")
    portal_not_exists_waiter: PortalNotExistsWaiter = client.get_waiter("portal_not_exists")

    execute_query_paginator: ExecuteQueryPaginator = client.get_paginator("execute_query")
    get_asset_property_aggregates_paginator: GetAssetPropertyAggregatesPaginator = client.get_paginator("get_asset_property_aggregates")
    get_asset_property_value_history_paginator: GetAssetPropertyValueHistoryPaginator = client.get_paginator("get_asset_property_value_history")
    get_interpolated_asset_property_values_paginator: GetInterpolatedAssetPropertyValuesPaginator = client.get_paginator("get_interpolated_asset_property_values")
    list_access_policies_paginator: ListAccessPoliciesPaginator = client.get_paginator("list_access_policies")
    list_actions_paginator: ListActionsPaginator = client.get_paginator("list_actions")
    list_asset_model_composite_models_paginator: ListAssetModelCompositeModelsPaginator = client.get_paginator("list_asset_model_composite_models")
    list_asset_model_properties_paginator: ListAssetModelPropertiesPaginator = client.get_paginator("list_asset_model_properties")
    list_asset_models_paginator: ListAssetModelsPaginator = client.get_paginator("list_asset_models")
    list_asset_properties_paginator: ListAssetPropertiesPaginator = client.get_paginator("list_asset_properties")
    list_asset_relationships_paginator: ListAssetRelationshipsPaginator = client.get_paginator("list_asset_relationships")
    list_assets_paginator: ListAssetsPaginator = client.get_paginator("list_assets")
    list_associated_assets_paginator: ListAssociatedAssetsPaginator = client.get_paginator("list_associated_assets")
    list_bulk_import_jobs_paginator: ListBulkImportJobsPaginator = client.get_paginator("list_bulk_import_jobs")
    list_composition_relationships_paginator: ListCompositionRelationshipsPaginator = client.get_paginator("list_composition_relationships")
    list_computation_model_data_binding_usages_paginator: ListComputationModelDataBindingUsagesPaginator = client.get_paginator("list_computation_model_data_binding_usages")
    list_computation_model_resolve_to_resources_paginator: ListComputationModelResolveToResourcesPaginator = client.get_paginator("list_computation_model_resolve_to_resources")
    list_computation_models_paginator: ListComputationModelsPaginator = client.get_paginator("list_computation_models")
    list_dashboards_paginator: ListDashboardsPaginator = client.get_paginator("list_dashboards")
    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    list_executions_paginator: ListExecutionsPaginator = client.get_paginator("list_executions")
    list_gateways_paginator: ListGatewaysPaginator = client.get_paginator("list_gateways")
    list_interface_relationships_paginator: ListInterfaceRelationshipsPaginator = client.get_paginator("list_interface_relationships")
    list_portals_paginator: ListPortalsPaginator = client.get_paginator("list_portals")
    list_project_assets_paginator: ListProjectAssetsPaginator = client.get_paginator("list_project_assets")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    list_time_series_paginator: ListTimeSeriesPaginator = client.get_paginator("list_time_series")
    ```
"""

from .client import IoTSiteWiseClient
from .paginator import (
    ExecuteQueryPaginator,
    GetAssetPropertyAggregatesPaginator,
    GetAssetPropertyValueHistoryPaginator,
    GetInterpolatedAssetPropertyValuesPaginator,
    ListAccessPoliciesPaginator,
    ListActionsPaginator,
    ListAssetModelCompositeModelsPaginator,
    ListAssetModelPropertiesPaginator,
    ListAssetModelsPaginator,
    ListAssetPropertiesPaginator,
    ListAssetRelationshipsPaginator,
    ListAssetsPaginator,
    ListAssociatedAssetsPaginator,
    ListBulkImportJobsPaginator,
    ListCompositionRelationshipsPaginator,
    ListComputationModelDataBindingUsagesPaginator,
    ListComputationModelResolveToResourcesPaginator,
    ListComputationModelsPaginator,
    ListDashboardsPaginator,
    ListDatasetsPaginator,
    ListExecutionsPaginator,
    ListGatewaysPaginator,
    ListInterfaceRelationshipsPaginator,
    ListPortalsPaginator,
    ListProjectAssetsPaginator,
    ListProjectsPaginator,
    ListTimeSeriesPaginator,
)
from .waiter import (
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
    "ExecuteQueryPaginator",
    "GetAssetPropertyAggregatesPaginator",
    "GetAssetPropertyValueHistoryPaginator",
    "GetInterpolatedAssetPropertyValuesPaginator",
    "IoTSiteWiseClient",
    "ListAccessPoliciesPaginator",
    "ListActionsPaginator",
    "ListAssetModelCompositeModelsPaginator",
    "ListAssetModelPropertiesPaginator",
    "ListAssetModelsPaginator",
    "ListAssetPropertiesPaginator",
    "ListAssetRelationshipsPaginator",
    "ListAssetsPaginator",
    "ListAssociatedAssetsPaginator",
    "ListBulkImportJobsPaginator",
    "ListCompositionRelationshipsPaginator",
    "ListComputationModelDataBindingUsagesPaginator",
    "ListComputationModelResolveToResourcesPaginator",
    "ListComputationModelsPaginator",
    "ListDashboardsPaginator",
    "ListDatasetsPaginator",
    "ListExecutionsPaginator",
    "ListGatewaysPaginator",
    "ListInterfaceRelationshipsPaginator",
    "ListPortalsPaginator",
    "ListProjectAssetsPaginator",
    "ListProjectsPaginator",
    "ListTimeSeriesPaginator",
    "PortalActiveWaiter",
    "PortalNotExistsWaiter",
)
