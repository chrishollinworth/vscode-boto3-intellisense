# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for iotsitewise service client

Usage::

    ```python
    import boto3
    from mypy_boto3_iotsitewise import IoTSiteWiseClient

    client: IoTSiteWiseClient = boto3.client("iotsitewise")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

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
from mypy_boto3_iotsitewise.type_defs import (
    AssetModelHierarchyDefinitionTypeDef,
    AssetModelHierarchyTypeDef,
    AssetModelPropertyDefinitionTypeDef,
    AssetModelPropertyTypeDef,
    BatchAssociateProjectAssetsResponseTypeDef,
    BatchDisassociateProjectAssetsResponseTypeDef,
    BatchPutAssetPropertyValueResponseTypeDef,
    CreateAccessPolicyResponseTypeDef,
    CreateAssetModelResponseTypeDef,
    CreateAssetResponseTypeDef,
    CreateDashboardResponseTypeDef,
    CreateGatewayResponseTypeDef,
    CreatePortalResponseTypeDef,
    CreateProjectResponseTypeDef,
    DeleteAssetModelResponseTypeDef,
    DeleteAssetResponseTypeDef,
    DeletePortalResponseTypeDef,
    DescribeAccessPolicyResponseTypeDef,
    DescribeAssetModelResponseTypeDef,
    DescribeAssetPropertyResponseTypeDef,
    DescribeAssetResponseTypeDef,
    DescribeDashboardResponseTypeDef,
    DescribeGatewayCapabilityConfigurationResponseTypeDef,
    DescribeGatewayResponseTypeDef,
    DescribeLoggingOptionsResponseTypeDef,
    DescribePortalResponseTypeDef,
    DescribeProjectResponseTypeDef,
    GatewayPlatformTypeDef,
    GetAssetPropertyAggregatesResponseTypeDef,
    GetAssetPropertyValueHistoryResponseTypeDef,
    GetAssetPropertyValueResponseTypeDef,
    IdentityTypeDef,
    ImageFileTypeDef,
    ImageTypeDef,
    ListAccessPoliciesResponseTypeDef,
    ListAssetModelsResponseTypeDef,
    ListAssetsResponseTypeDef,
    ListAssociatedAssetsResponseTypeDef,
    ListDashboardsResponseTypeDef,
    ListGatewaysResponseTypeDef,
    ListPortalsResponseTypeDef,
    ListProjectAssetsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingOptionsTypeDef,
    PutAssetPropertyValueEntryTypeDef,
    ResourceTypeDef,
    UpdateAssetModelResponseTypeDef,
    UpdateAssetResponseTypeDef,
    UpdateGatewayCapabilityConfigurationResponseTypeDef,
    UpdatePortalResponseTypeDef,
)
from mypy_boto3_iotsitewise.waiter import (
    AssetActiveWaiter,
    AssetModelActiveWaiter,
    AssetModelNotExistsWaiter,
    AssetNotExistsWaiter,
    PortalActiveWaiter,
    PortalNotExistsWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoTSiteWiseClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    ConflictingOperationException: Type[Boto3ClientError]
    InternalFailureException: Type[Boto3ClientError]
    InvalidRequestException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ResourceAlreadyExistsException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ServiceUnavailableException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]
    TooManyTagsException: Type[Boto3ClientError]


class IoTSiteWiseClient:
    """
    [IoTSiteWise.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client)
    """

    exceptions: Exceptions

    def associate_assets(
        self, assetId: str, hierarchyId: str, childAssetId: str, clientToken: str = None
    ) -> None:
        """
        [Client.associate_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.associate_assets)
        """

    def batch_associate_project_assets(
        self, projectId: str, assetIds: List[str], clientToken: str = None
    ) -> BatchAssociateProjectAssetsResponseTypeDef:
        """
        [Client.batch_associate_project_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.batch_associate_project_assets)
        """

    def batch_disassociate_project_assets(
        self, projectId: str, assetIds: List[str], clientToken: str = None
    ) -> BatchDisassociateProjectAssetsResponseTypeDef:
        """
        [Client.batch_disassociate_project_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.batch_disassociate_project_assets)
        """

    def batch_put_asset_property_value(
        self, entries: List[PutAssetPropertyValueEntryTypeDef]
    ) -> BatchPutAssetPropertyValueResponseTypeDef:
        """
        [Client.batch_put_asset_property_value documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.batch_put_asset_property_value)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.can_paginate)
        """

    def create_access_policy(
        self,
        accessPolicyIdentity: "IdentityTypeDef",
        accessPolicyResource: "ResourceTypeDef",
        accessPolicyPermission: Literal["ADMINISTRATOR", "VIEWER"],
        clientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateAccessPolicyResponseTypeDef:
        """
        [Client.create_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.create_access_policy)
        """

    def create_asset(
        self,
        assetName: str,
        assetModelId: str,
        clientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateAssetResponseTypeDef:
        """
        [Client.create_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.create_asset)
        """

    def create_asset_model(
        self,
        assetModelName: str,
        assetModelDescription: str = None,
        assetModelProperties: List[AssetModelPropertyDefinitionTypeDef] = None,
        assetModelHierarchies: List[AssetModelHierarchyDefinitionTypeDef] = None,
        clientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateAssetModelResponseTypeDef:
        """
        [Client.create_asset_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.create_asset_model)
        """

    def create_dashboard(
        self,
        projectId: str,
        dashboardName: str,
        dashboardDefinition: str,
        dashboardDescription: str = None,
        clientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateDashboardResponseTypeDef:
        """
        [Client.create_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.create_dashboard)
        """

    def create_gateway(
        self,
        gatewayName: str,
        gatewayPlatform: "GatewayPlatformTypeDef",
        tags: Dict[str, str] = None,
    ) -> CreateGatewayResponseTypeDef:
        """
        [Client.create_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.create_gateway)
        """

    def create_portal(
        self,
        portalName: str,
        portalContactEmail: str,
        roleArn: str,
        portalDescription: str = None,
        clientToken: str = None,
        portalLogoImageFile: "ImageFileTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreatePortalResponseTypeDef:
        """
        [Client.create_portal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.create_portal)
        """

    def create_project(
        self,
        portalId: str,
        projectName: str,
        projectDescription: str = None,
        clientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateProjectResponseTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.create_project)
        """

    def delete_access_policy(self, accessPolicyId: str, clientToken: str = None) -> Dict[str, Any]:
        """
        [Client.delete_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_access_policy)
        """

    def delete_asset(self, assetId: str, clientToken: str = None) -> DeleteAssetResponseTypeDef:
        """
        [Client.delete_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_asset)
        """

    def delete_asset_model(
        self, assetModelId: str, clientToken: str = None
    ) -> DeleteAssetModelResponseTypeDef:
        """
        [Client.delete_asset_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_asset_model)
        """

    def delete_dashboard(self, dashboardId: str, clientToken: str = None) -> Dict[str, Any]:
        """
        [Client.delete_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_dashboard)
        """

    def delete_gateway(self, gatewayId: str) -> None:
        """
        [Client.delete_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_gateway)
        """

    def delete_portal(self, portalId: str, clientToken: str = None) -> DeletePortalResponseTypeDef:
        """
        [Client.delete_portal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_portal)
        """

    def delete_project(self, projectId: str, clientToken: str = None) -> Dict[str, Any]:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_project)
        """

    def describe_access_policy(self, accessPolicyId: str) -> DescribeAccessPolicyResponseTypeDef:
        """
        [Client.describe_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_access_policy)
        """

    def describe_asset(self, assetId: str) -> DescribeAssetResponseTypeDef:
        """
        [Client.describe_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_asset)
        """

    def describe_asset_model(self, assetModelId: str) -> DescribeAssetModelResponseTypeDef:
        """
        [Client.describe_asset_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_asset_model)
        """

    def describe_asset_property(
        self, assetId: str, propertyId: str
    ) -> DescribeAssetPropertyResponseTypeDef:
        """
        [Client.describe_asset_property documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_asset_property)
        """

    def describe_dashboard(self, dashboardId: str) -> DescribeDashboardResponseTypeDef:
        """
        [Client.describe_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_dashboard)
        """

    def describe_gateway(self, gatewayId: str) -> DescribeGatewayResponseTypeDef:
        """
        [Client.describe_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_gateway)
        """

    def describe_gateway_capability_configuration(
        self, gatewayId: str, capabilityNamespace: str
    ) -> DescribeGatewayCapabilityConfigurationResponseTypeDef:
        """
        [Client.describe_gateway_capability_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_gateway_capability_configuration)
        """

    def describe_logging_options(self) -> DescribeLoggingOptionsResponseTypeDef:
        """
        [Client.describe_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_logging_options)
        """

    def describe_portal(self, portalId: str) -> DescribePortalResponseTypeDef:
        """
        [Client.describe_portal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_portal)
        """

    def describe_project(self, projectId: str) -> DescribeProjectResponseTypeDef:
        """
        [Client.describe_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_project)
        """

    def disassociate_assets(
        self, assetId: str, hierarchyId: str, childAssetId: str, clientToken: str = None
    ) -> None:
        """
        [Client.disassociate_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.disassociate_assets)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.generate_presigned_url)
        """

    def get_asset_property_aggregates(
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
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetAssetPropertyAggregatesResponseTypeDef:
        """
        [Client.get_asset_property_aggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.get_asset_property_aggregates)
        """

    def get_asset_property_value(
        self, assetId: str = None, propertyId: str = None, propertyAlias: str = None
    ) -> GetAssetPropertyValueResponseTypeDef:
        """
        [Client.get_asset_property_value documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.get_asset_property_value)
        """

    def get_asset_property_value_history(
        self,
        assetId: str = None,
        propertyId: str = None,
        propertyAlias: str = None,
        startDate: datetime = None,
        endDate: datetime = None,
        qualities: List[Literal["GOOD", "BAD", "UNCERTAIN"]] = None,
        timeOrdering: Literal["ASCENDING", "DESCENDING"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetAssetPropertyValueHistoryResponseTypeDef:
        """
        [Client.get_asset_property_value_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.get_asset_property_value_history)
        """

    def list_access_policies(
        self,
        identityType: Literal["USER", "GROUP"] = None,
        identityId: str = None,
        resourceType: Literal["PORTAL", "PROJECT"] = None,
        resourceId: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAccessPoliciesResponseTypeDef:
        """
        [Client.list_access_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.list_access_policies)
        """

    def list_asset_models(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListAssetModelsResponseTypeDef:
        """
        [Client.list_asset_models documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.list_asset_models)
        """

    def list_assets(
        self,
        nextToken: str = None,
        maxResults: int = None,
        assetModelId: str = None,
        filter: Literal["ALL", "TOP_LEVEL"] = None,
    ) -> ListAssetsResponseTypeDef:
        """
        [Client.list_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.list_assets)
        """

    def list_associated_assets(
        self, assetId: str, hierarchyId: str, nextToken: str = None, maxResults: int = None
    ) -> ListAssociatedAssetsResponseTypeDef:
        """
        [Client.list_associated_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.list_associated_assets)
        """

    def list_dashboards(
        self, projectId: str, nextToken: str = None, maxResults: int = None
    ) -> ListDashboardsResponseTypeDef:
        """
        [Client.list_dashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.list_dashboards)
        """

    def list_gateways(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListGatewaysResponseTypeDef:
        """
        [Client.list_gateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.list_gateways)
        """

    def list_portals(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListPortalsResponseTypeDef:
        """
        [Client.list_portals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.list_portals)
        """

    def list_project_assets(
        self, projectId: str, nextToken: str = None, maxResults: int = None
    ) -> ListProjectAssetsResponseTypeDef:
        """
        [Client.list_project_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.list_project_assets)
        """

    def list_projects(
        self, portalId: str, nextToken: str = None, maxResults: int = None
    ) -> ListProjectsResponseTypeDef:
        """
        [Client.list_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.list_projects)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.list_tags_for_resource)
        """

    def put_logging_options(self, loggingOptions: "LoggingOptionsTypeDef") -> Dict[str, Any]:
        """
        [Client.put_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.put_logging_options)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.untag_resource)
        """

    def update_access_policy(
        self,
        accessPolicyId: str,
        accessPolicyIdentity: "IdentityTypeDef",
        accessPolicyResource: "ResourceTypeDef",
        accessPolicyPermission: Literal["ADMINISTRATOR", "VIEWER"],
        clientToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_access_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.update_access_policy)
        """

    def update_asset(
        self, assetId: str, assetName: str, clientToken: str = None
    ) -> UpdateAssetResponseTypeDef:
        """
        [Client.update_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.update_asset)
        """

    def update_asset_model(
        self,
        assetModelId: str,
        assetModelName: str,
        assetModelDescription: str = None,
        assetModelProperties: List["AssetModelPropertyTypeDef"] = None,
        assetModelHierarchies: List["AssetModelHierarchyTypeDef"] = None,
        clientToken: str = None,
    ) -> UpdateAssetModelResponseTypeDef:
        """
        [Client.update_asset_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.update_asset_model)
        """

    def update_asset_property(
        self,
        assetId: str,
        propertyId: str,
        propertyAlias: str = None,
        propertyNotificationState: Literal["ENABLED", "DISABLED"] = None,
        clientToken: str = None,
    ) -> None:
        """
        [Client.update_asset_property documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.update_asset_property)
        """

    def update_dashboard(
        self,
        dashboardId: str,
        dashboardName: str,
        dashboardDefinition: str,
        dashboardDescription: str = None,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_dashboard documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.update_dashboard)
        """

    def update_gateway(self, gatewayId: str, gatewayName: str) -> None:
        """
        [Client.update_gateway documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.update_gateway)
        """

    def update_gateway_capability_configuration(
        self, gatewayId: str, capabilityNamespace: str, capabilityConfiguration: str
    ) -> UpdateGatewayCapabilityConfigurationResponseTypeDef:
        """
        [Client.update_gateway_capability_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.update_gateway_capability_configuration)
        """

    def update_portal(
        self,
        portalId: str,
        portalName: str,
        portalContactEmail: str,
        roleArn: str,
        portalDescription: str = None,
        portalLogoImage: ImageTypeDef = None,
        clientToken: str = None,
    ) -> UpdatePortalResponseTypeDef:
        """
        [Client.update_portal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.update_portal)
        """

    def update_project(
        self,
        projectId: str,
        projectName: str,
        projectDescription: str = None,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Client.update_project)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_asset_property_aggregates"]
    ) -> GetAssetPropertyAggregatesPaginator:
        """
        [Paginator.GetAssetPropertyAggregates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyAggregates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_asset_property_value_history"]
    ) -> GetAssetPropertyValueHistoryPaginator:
        """
        [Paginator.GetAssetPropertyValueHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyValueHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_access_policies"]
    ) -> ListAccessPoliciesPaginator:
        """
        [Paginator.ListAccessPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAccessPolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_asset_models"]
    ) -> ListAssetModelsPaginator:
        """
        [Paginator.ListAssetModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetModels)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_assets"]) -> ListAssetsPaginator:
        """
        [Paginator.ListAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_assets"]
    ) -> ListAssociatedAssetsPaginator:
        """
        [Paginator.ListAssociatedAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssociatedAssets)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_dashboards"]) -> ListDashboardsPaginator:
        """
        [Paginator.ListDashboards documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListDashboards)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_gateways"]) -> ListGatewaysPaginator:
        """
        [Paginator.ListGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListGateways)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_portals"]) -> ListPortalsPaginator:
        """
        [Paginator.ListPortals documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListPortals)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_project_assets"]
    ) -> ListProjectAssetsPaginator:
        """
        [Paginator.ListProjectAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjectAssets)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Paginator.ListProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjects)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass

    @overload
    def get_waiter(self, waiter_name: Literal["asset_active"]) -> AssetActiveWaiter:
        """
        [Waiter.AssetActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetActive)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["asset_model_active"]) -> AssetModelActiveWaiter:
        """
        [Waiter.AssetModelActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetModelActive)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["asset_model_not_exists"]
    ) -> AssetModelNotExistsWaiter:
        """
        [Waiter.AssetModelNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetModelNotExists)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["asset_not_exists"]) -> AssetNotExistsWaiter:
        """
        [Waiter.AssetNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetNotExists)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["portal_active"]) -> PortalActiveWaiter:
        """
        [Waiter.PortalActive documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Waiter.PortalActive)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["portal_not_exists"]) -> PortalNotExistsWaiter:
        """
        [Waiter.PortalNotExists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotsitewise.html#IoTSiteWise.Waiter.PortalNotExists)
        """

    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        pass
