# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for iotsitewise service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_iotsitewise import IoTSiteWiseClient
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

    client: IoTSiteWiseClient = boto3.client("iotsitewise")

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
import sys
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_iotsitewise.type_defs import (
    GetAssetPropertyAggregatesResponseTypeDef,
    GetAssetPropertyValueHistoryResponseTypeDef,
    ListAccessPoliciesResponseTypeDef,
    ListAssetModelsResponseTypeDef,
    ListAssetsResponseTypeDef,
    ListAssociatedAssetsResponseTypeDef,
    ListDashboardsResponseTypeDef,
    ListGatewaysResponseTypeDef,
    ListPortalsResponseTypeDef,
    ListProjectAssetsResponseTypeDef,
    ListProjectsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "GetAssetPropertyAggregatesPaginator",
    "GetAssetPropertyValueHistoryPaginator",
    "ListAccessPoliciesPaginator",
    "ListAssetModelsPaginator",
    "ListAssetsPaginator",
    "ListAssociatedAssetsPaginator",
    "ListDashboardsPaginator",
    "ListGatewaysPaginator",
    "ListPortalsPaginator",
    "ListProjectAssetsPaginator",
    "ListProjectsPaginator",
)


class GetAssetPropertyAggregatesPaginator(Boto3Paginator):
    """
    [Paginator.GetAssetPropertyAggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyAggregates)
    """

    def paginate(
        self,
        aggregateTypes: List[
            Literal["AVERAGE", "COUNT", "MAXIMUM", "MINIMUM", "SUM", "STANDARD_DEVIATION"]
        ],
        resolution: str,
        startDate: datetime,
        endDate: datetime,
        assetId: str = None,
        propertyId: str = None,
        propertyAlias: str = None,
        qualities: List[Literal["GOOD", "BAD", "UNCERTAIN"]] = None,
        timeOrdering: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetAssetPropertyAggregatesResponseTypeDef]:
        """
        [GetAssetPropertyAggregates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyAggregates.paginate)
        """


class GetAssetPropertyValueHistoryPaginator(Boto3Paginator):
    """
    [Paginator.GetAssetPropertyValueHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyValueHistory)
    """

    def paginate(
        self,
        assetId: str = None,
        propertyId: str = None,
        propertyAlias: str = None,
        startDate: datetime = None,
        endDate: datetime = None,
        qualities: List[Literal["GOOD", "BAD", "UNCERTAIN"]] = None,
        timeOrdering: Literal["ASCENDING", "DESCENDING"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetAssetPropertyValueHistoryResponseTypeDef]:
        """
        [GetAssetPropertyValueHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyValueHistory.paginate)
        """


class ListAccessPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListAccessPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAccessPolicies)
    """

    def paginate(
        self,
        identityType: Literal["USER", "GROUP"] = None,
        identityId: str = None,
        resourceType: Literal["PORTAL", "PROJECT"] = None,
        resourceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAccessPoliciesResponseTypeDef]:
        """
        [ListAccessPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAccessPolicies.paginate)
        """


class ListAssetModelsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssetModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetModels)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssetModelsResponseTypeDef]:
        """
        [ListAssetModels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetModels.paginate)
        """


class ListAssetsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssets)
    """

    def paginate(
        self,
        assetModelId: str = None,
        filter: Literal["ALL", "TOP_LEVEL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAssetsResponseTypeDef]:
        """
        [ListAssets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssets.paginate)
        """


class ListAssociatedAssetsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssociatedAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssociatedAssets)
    """

    def paginate(
        self, assetId: str, hierarchyId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociatedAssetsResponseTypeDef]:
        """
        [ListAssociatedAssets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssociatedAssets.paginate)
        """


class ListDashboardsPaginator(Boto3Paginator):
    """
    [Paginator.ListDashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListDashboards)
    """

    def paginate(
        self, projectId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDashboardsResponseTypeDef]:
        """
        [ListDashboards.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListDashboards.paginate)
        """


class ListGatewaysPaginator(Boto3Paginator):
    """
    [Paginator.ListGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListGateways)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGatewaysResponseTypeDef]:
        """
        [ListGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListGateways.paginate)
        """


class ListPortalsPaginator(Boto3Paginator):
    """
    [Paginator.ListPortals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListPortals)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPortalsResponseTypeDef]:
        """
        [ListPortals.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListPortals.paginate)
        """


class ListProjectAssetsPaginator(Boto3Paginator):
    """
    [Paginator.ListProjectAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjectAssets)
    """

    def paginate(
        self, projectId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectAssetsResponseTypeDef]:
        """
        [ListProjectAssets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjectAssets.paginate)
        """


class ListProjectsPaginator(Boto3Paginator):
    """
    [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjects)
    """

    def paginate(
        self, portalId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProjectsResponseTypeDef]:
        """
        [ListProjects.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjects.paginate)
        """
