"""
Type annotations for iotsitewise service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_iotsitewise.client import IoTSiteWiseClient
    from mypy_boto3_iotsitewise.paginator import (
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
        ListDashboardsPaginator,
        ListDatasetsPaginator,
        ListGatewaysPaginator,
        ListPortalsPaginator,
        ListProjectAssetsPaginator,
        ListProjectsPaginator,
        ListTimeSeriesPaginator,
    )

    session = Session()
    client: IoTSiteWiseClient = session.client("iotsitewise")

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
    list_dashboards_paginator: ListDashboardsPaginator = client.get_paginator("list_dashboards")
    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    list_gateways_paginator: ListGatewaysPaginator = client.get_paginator("list_gateways")
    list_portals_paginator: ListPortalsPaginator = client.get_paginator("list_portals")
    list_project_assets_paginator: ListProjectAssetsPaginator = client.get_paginator("list_project_assets")
    list_projects_paginator: ListProjectsPaginator = client.get_paginator("list_projects")
    list_time_series_paginator: ListTimeSeriesPaginator = client.get_paginator("list_time_series")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ExecuteQueryRequestPaginateTypeDef,
    ExecuteQueryResponsePaginatorTypeDef,
    ExecuteQueryResponseWaiterTypeDef,
    GetAssetPropertyAggregatesRequestPaginateTypeDef,
    GetAssetPropertyAggregatesResponseTypeDef,
    GetAssetPropertyValueHistoryRequestPaginateTypeDef,
    GetAssetPropertyValueHistoryResponseTypeDef,
    GetInterpolatedAssetPropertyValuesRequestPaginateTypeDef,
    GetInterpolatedAssetPropertyValuesResponseTypeDef,
    ListAccessPoliciesRequestPaginateTypeDef,
    ListAccessPoliciesResponseTypeDef,
    ListActionsRequestPaginateTypeDef,
    ListActionsResponseTypeDef,
    ListAssetModelCompositeModelsRequestPaginateTypeDef,
    ListAssetModelCompositeModelsResponseTypeDef,
    ListAssetModelPropertiesRequestPaginateTypeDef,
    ListAssetModelPropertiesResponseTypeDef,
    ListAssetModelsRequestPaginateTypeDef,
    ListAssetModelsResponseTypeDef,
    ListAssetPropertiesRequestPaginateTypeDef,
    ListAssetPropertiesResponseTypeDef,
    ListAssetRelationshipsRequestPaginateTypeDef,
    ListAssetRelationshipsResponseTypeDef,
    ListAssetsRequestPaginateTypeDef,
    ListAssetsResponseTypeDef,
    ListAssociatedAssetsRequestPaginateTypeDef,
    ListAssociatedAssetsResponseTypeDef,
    ListBulkImportJobsRequestPaginateTypeDef,
    ListBulkImportJobsResponseTypeDef,
    ListCompositionRelationshipsRequestPaginateTypeDef,
    ListCompositionRelationshipsResponseTypeDef,
    ListDashboardsRequestPaginateTypeDef,
    ListDashboardsResponseTypeDef,
    ListDatasetsRequestPaginateTypeDef,
    ListDatasetsResponseTypeDef,
    ListGatewaysRequestPaginateTypeDef,
    ListGatewaysResponseTypeDef,
    ListPortalsRequestPaginateTypeDef,
    ListPortalsResponseTypeDef,
    ListProjectAssetsRequestPaginateTypeDef,
    ListProjectAssetsResponseTypeDef,
    ListProjectsRequestPaginateTypeDef,
    ListProjectsResponseTypeDef,
    ListTimeSeriesRequestPaginateTypeDef,
    ListTimeSeriesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ExecuteQueryPaginator",
    "GetAssetPropertyAggregatesPaginator",
    "GetAssetPropertyValueHistoryPaginator",
    "GetInterpolatedAssetPropertyValuesPaginator",
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
    "ListDashboardsPaginator",
    "ListDatasetsPaginator",
    "ListGatewaysPaginator",
    "ListPortalsPaginator",
    "ListProjectAssetsPaginator",
    "ListProjectsPaginator",
    "ListTimeSeriesPaginator",
)

if TYPE_CHECKING:
    _ExecuteQueryPaginatorBase = Paginator[ExecuteQueryResponseWaiterTypeDef]
else:
    _ExecuteQueryPaginatorBase = Paginator  # type: ignore[assignment]

class ExecuteQueryPaginator(_ExecuteQueryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ExecuteQuery.html#IoTSiteWise.Paginator.ExecuteQuery)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#executequerypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ExecuteQueryRequestPaginateTypeDef]
    ) -> PageIterator[ExecuteQueryResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ExecuteQuery.html#IoTSiteWise.Paginator.ExecuteQuery.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#executequerypaginator)
        """

if TYPE_CHECKING:
    _GetAssetPropertyAggregatesPaginatorBase = Paginator[GetAssetPropertyAggregatesResponseTypeDef]
else:
    _GetAssetPropertyAggregatesPaginatorBase = Paginator  # type: ignore[assignment]

class GetAssetPropertyAggregatesPaginator(_GetAssetPropertyAggregatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/GetAssetPropertyAggregates.html#IoTSiteWise.Paginator.GetAssetPropertyAggregates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#getassetpropertyaggregatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAssetPropertyAggregatesRequestPaginateTypeDef]
    ) -> PageIterator[GetAssetPropertyAggregatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/GetAssetPropertyAggregates.html#IoTSiteWise.Paginator.GetAssetPropertyAggregates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#getassetpropertyaggregatespaginator)
        """

if TYPE_CHECKING:
    _GetAssetPropertyValueHistoryPaginatorBase = Paginator[
        GetAssetPropertyValueHistoryResponseTypeDef
    ]
else:
    _GetAssetPropertyValueHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class GetAssetPropertyValueHistoryPaginator(_GetAssetPropertyValueHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/GetAssetPropertyValueHistory.html#IoTSiteWise.Paginator.GetAssetPropertyValueHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#getassetpropertyvaluehistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAssetPropertyValueHistoryRequestPaginateTypeDef]
    ) -> PageIterator[GetAssetPropertyValueHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/GetAssetPropertyValueHistory.html#IoTSiteWise.Paginator.GetAssetPropertyValueHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#getassetpropertyvaluehistorypaginator)
        """

if TYPE_CHECKING:
    _GetInterpolatedAssetPropertyValuesPaginatorBase = Paginator[
        GetInterpolatedAssetPropertyValuesResponseTypeDef
    ]
else:
    _GetInterpolatedAssetPropertyValuesPaginatorBase = Paginator  # type: ignore[assignment]

class GetInterpolatedAssetPropertyValuesPaginator(_GetInterpolatedAssetPropertyValuesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/GetInterpolatedAssetPropertyValues.html#IoTSiteWise.Paginator.GetInterpolatedAssetPropertyValues)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#getinterpolatedassetpropertyvaluespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetInterpolatedAssetPropertyValuesRequestPaginateTypeDef]
    ) -> PageIterator[GetInterpolatedAssetPropertyValuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/GetInterpolatedAssetPropertyValues.html#IoTSiteWise.Paginator.GetInterpolatedAssetPropertyValues.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#getinterpolatedassetpropertyvaluespaginator)
        """

if TYPE_CHECKING:
    _ListAccessPoliciesPaginatorBase = Paginator[ListAccessPoliciesResponseTypeDef]
else:
    _ListAccessPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccessPoliciesPaginator(_ListAccessPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAccessPolicies.html#IoTSiteWise.Paginator.ListAccessPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listaccesspoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccessPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListAccessPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAccessPolicies.html#IoTSiteWise.Paginator.ListAccessPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listaccesspoliciespaginator)
        """

if TYPE_CHECKING:
    _ListActionsPaginatorBase = Paginator[ListActionsResponseTypeDef]
else:
    _ListActionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListActionsPaginator(_ListActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListActions.html#IoTSiteWise.Paginator.ListActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListActionsRequestPaginateTypeDef]
    ) -> PageIterator[ListActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListActions.html#IoTSiteWise.Paginator.ListActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listactionspaginator)
        """

if TYPE_CHECKING:
    _ListAssetModelCompositeModelsPaginatorBase = Paginator[
        ListAssetModelCompositeModelsResponseTypeDef
    ]
else:
    _ListAssetModelCompositeModelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssetModelCompositeModelsPaginator(_ListAssetModelCompositeModelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAssetModelCompositeModels.html#IoTSiteWise.Paginator.ListAssetModelCompositeModels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listassetmodelcompositemodelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssetModelCompositeModelsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssetModelCompositeModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAssetModelCompositeModels.html#IoTSiteWise.Paginator.ListAssetModelCompositeModels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listassetmodelcompositemodelspaginator)
        """

if TYPE_CHECKING:
    _ListAssetModelPropertiesPaginatorBase = Paginator[ListAssetModelPropertiesResponseTypeDef]
else:
    _ListAssetModelPropertiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssetModelPropertiesPaginator(_ListAssetModelPropertiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAssetModelProperties.html#IoTSiteWise.Paginator.ListAssetModelProperties)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listassetmodelpropertiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssetModelPropertiesRequestPaginateTypeDef]
    ) -> PageIterator[ListAssetModelPropertiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAssetModelProperties.html#IoTSiteWise.Paginator.ListAssetModelProperties.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listassetmodelpropertiespaginator)
        """

if TYPE_CHECKING:
    _ListAssetModelsPaginatorBase = Paginator[ListAssetModelsResponseTypeDef]
else:
    _ListAssetModelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssetModelsPaginator(_ListAssetModelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAssetModels.html#IoTSiteWise.Paginator.ListAssetModels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listassetmodelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssetModelsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssetModelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAssetModels.html#IoTSiteWise.Paginator.ListAssetModels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listassetmodelspaginator)
        """

if TYPE_CHECKING:
    _ListAssetPropertiesPaginatorBase = Paginator[ListAssetPropertiesResponseTypeDef]
else:
    _ListAssetPropertiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssetPropertiesPaginator(_ListAssetPropertiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAssetProperties.html#IoTSiteWise.Paginator.ListAssetProperties)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listassetpropertiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssetPropertiesRequestPaginateTypeDef]
    ) -> PageIterator[ListAssetPropertiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAssetProperties.html#IoTSiteWise.Paginator.ListAssetProperties.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listassetpropertiespaginator)
        """

if TYPE_CHECKING:
    _ListAssetRelationshipsPaginatorBase = Paginator[ListAssetRelationshipsResponseTypeDef]
else:
    _ListAssetRelationshipsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssetRelationshipsPaginator(_ListAssetRelationshipsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAssetRelationships.html#IoTSiteWise.Paginator.ListAssetRelationships)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listassetrelationshipspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssetRelationshipsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssetRelationshipsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAssetRelationships.html#IoTSiteWise.Paginator.ListAssetRelationships.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listassetrelationshipspaginator)
        """

if TYPE_CHECKING:
    _ListAssetsPaginatorBase = Paginator[ListAssetsResponseTypeDef]
else:
    _ListAssetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssetsPaginator(_ListAssetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAssets.html#IoTSiteWise.Paginator.ListAssets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listassetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssetsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAssets.html#IoTSiteWise.Paginator.ListAssets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listassetspaginator)
        """

if TYPE_CHECKING:
    _ListAssociatedAssetsPaginatorBase = Paginator[ListAssociatedAssetsResponseTypeDef]
else:
    _ListAssociatedAssetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssociatedAssetsPaginator(_ListAssociatedAssetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAssociatedAssets.html#IoTSiteWise.Paginator.ListAssociatedAssets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listassociatedassetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssociatedAssetsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssociatedAssetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListAssociatedAssets.html#IoTSiteWise.Paginator.ListAssociatedAssets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listassociatedassetspaginator)
        """

if TYPE_CHECKING:
    _ListBulkImportJobsPaginatorBase = Paginator[ListBulkImportJobsResponseTypeDef]
else:
    _ListBulkImportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBulkImportJobsPaginator(_ListBulkImportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListBulkImportJobs.html#IoTSiteWise.Paginator.ListBulkImportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listbulkimportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBulkImportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListBulkImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListBulkImportJobs.html#IoTSiteWise.Paginator.ListBulkImportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listbulkimportjobspaginator)
        """

if TYPE_CHECKING:
    _ListCompositionRelationshipsPaginatorBase = Paginator[
        ListCompositionRelationshipsResponseTypeDef
    ]
else:
    _ListCompositionRelationshipsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCompositionRelationshipsPaginator(_ListCompositionRelationshipsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListCompositionRelationships.html#IoTSiteWise.Paginator.ListCompositionRelationships)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listcompositionrelationshipspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCompositionRelationshipsRequestPaginateTypeDef]
    ) -> PageIterator[ListCompositionRelationshipsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListCompositionRelationships.html#IoTSiteWise.Paginator.ListCompositionRelationships.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listcompositionrelationshipspaginator)
        """

if TYPE_CHECKING:
    _ListDashboardsPaginatorBase = Paginator[ListDashboardsResponseTypeDef]
else:
    _ListDashboardsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDashboardsPaginator(_ListDashboardsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListDashboards.html#IoTSiteWise.Paginator.ListDashboards)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listdashboardspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDashboardsRequestPaginateTypeDef]
    ) -> PageIterator[ListDashboardsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListDashboards.html#IoTSiteWise.Paginator.ListDashboards.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listdashboardspaginator)
        """

if TYPE_CHECKING:
    _ListDatasetsPaginatorBase = Paginator[ListDatasetsResponseTypeDef]
else:
    _ListDatasetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatasetsPaginator(_ListDatasetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListDatasets.html#IoTSiteWise.Paginator.ListDatasets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listdatasetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatasetsRequestPaginateTypeDef]
    ) -> PageIterator[ListDatasetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListDatasets.html#IoTSiteWise.Paginator.ListDatasets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listdatasetspaginator)
        """

if TYPE_CHECKING:
    _ListGatewaysPaginatorBase = Paginator[ListGatewaysResponseTypeDef]
else:
    _ListGatewaysPaginatorBase = Paginator  # type: ignore[assignment]

class ListGatewaysPaginator(_ListGatewaysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListGateways.html#IoTSiteWise.Paginator.ListGateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listgatewayspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGatewaysRequestPaginateTypeDef]
    ) -> PageIterator[ListGatewaysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListGateways.html#IoTSiteWise.Paginator.ListGateways.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listgatewayspaginator)
        """

if TYPE_CHECKING:
    _ListPortalsPaginatorBase = Paginator[ListPortalsResponseTypeDef]
else:
    _ListPortalsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPortalsPaginator(_ListPortalsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListPortals.html#IoTSiteWise.Paginator.ListPortals)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listportalspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPortalsRequestPaginateTypeDef]
    ) -> PageIterator[ListPortalsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListPortals.html#IoTSiteWise.Paginator.ListPortals.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listportalspaginator)
        """

if TYPE_CHECKING:
    _ListProjectAssetsPaginatorBase = Paginator[ListProjectAssetsResponseTypeDef]
else:
    _ListProjectAssetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProjectAssetsPaginator(_ListProjectAssetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListProjectAssets.html#IoTSiteWise.Paginator.ListProjectAssets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listprojectassetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProjectAssetsRequestPaginateTypeDef]
    ) -> PageIterator[ListProjectAssetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListProjectAssets.html#IoTSiteWise.Paginator.ListProjectAssets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listprojectassetspaginator)
        """

if TYPE_CHECKING:
    _ListProjectsPaginatorBase = Paginator[ListProjectsResponseTypeDef]
else:
    _ListProjectsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProjectsPaginator(_ListProjectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListProjects.html#IoTSiteWise.Paginator.ListProjects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listprojectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProjectsRequestPaginateTypeDef]
    ) -> PageIterator[ListProjectsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListProjects.html#IoTSiteWise.Paginator.ListProjects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listprojectspaginator)
        """

if TYPE_CHECKING:
    _ListTimeSeriesPaginatorBase = Paginator[ListTimeSeriesResponseTypeDef]
else:
    _ListTimeSeriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTimeSeriesPaginator(_ListTimeSeriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListTimeSeries.html#IoTSiteWise.Paginator.ListTimeSeries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listtimeseriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTimeSeriesRequestPaginateTypeDef]
    ) -> PageIterator[ListTimeSeriesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/paginator/ListTimeSeries.html#IoTSiteWise.Paginator.ListTimeSeries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators/#listtimeseriespaginator)
        """
