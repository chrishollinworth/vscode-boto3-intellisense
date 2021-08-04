"""
Type annotations for iotsitewise service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotsitewise import IoTSiteWiseClient

    client: IoTSiteWiseClient = boto3.client("iotsitewise")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AggregateTypeType,
    AuthModeType,
    EncryptionTypeType,
    IdentityTypeType,
    ListAssetsFilterType,
    PermissionType,
    PropertyNotificationStateType,
    QualityType,
    ResourceTypeType,
    StorageTypeType,
    TimeOrderingType,
    TraversalDirectionType,
)
from .paginator import (
    GetAssetPropertyAggregatesPaginator,
    GetAssetPropertyValueHistoryPaginator,
    GetInterpolatedAssetPropertyValuesPaginator,
    ListAccessPoliciesPaginator,
    ListAssetModelsPaginator,
    ListAssetRelationshipsPaginator,
    ListAssetsPaginator,
    ListAssociatedAssetsPaginator,
    ListDashboardsPaginator,
    ListGatewaysPaginator,
    ListPortalsPaginator,
    ListProjectAssetsPaginator,
    ListProjectsPaginator,
)
from .type_defs import (
    AlarmsTypeDef,
    AssetModelCompositeModelDefinitionTypeDef,
    AssetModelCompositeModelTypeDef,
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
    DescribeDefaultEncryptionConfigurationResponseTypeDef,
    DescribeGatewayCapabilityConfigurationResponseTypeDef,
    DescribeGatewayResponseTypeDef,
    DescribeLoggingOptionsResponseTypeDef,
    DescribePortalResponseTypeDef,
    DescribeProjectResponseTypeDef,
    DescribeStorageConfigurationResponseTypeDef,
    GatewayPlatformTypeDef,
    GetAssetPropertyAggregatesResponseTypeDef,
    GetAssetPropertyValueHistoryResponseTypeDef,
    GetAssetPropertyValueResponseTypeDef,
    GetInterpolatedAssetPropertyValuesResponseTypeDef,
    IdentityTypeDef,
    ImageFileTypeDef,
    ImageTypeDef,
    ListAccessPoliciesResponseTypeDef,
    ListAssetModelsResponseTypeDef,
    ListAssetRelationshipsResponseTypeDef,
    ListAssetsResponseTypeDef,
    ListAssociatedAssetsResponseTypeDef,
    ListDashboardsResponseTypeDef,
    ListGatewaysResponseTypeDef,
    ListPortalsResponseTypeDef,
    ListProjectAssetsResponseTypeDef,
    ListProjectsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingOptionsTypeDef,
    MultiLayerStorageTypeDef,
    PutAssetPropertyValueEntryTypeDef,
    PutDefaultEncryptionConfigurationResponseTypeDef,
    PutStorageConfigurationResponseTypeDef,
    ResourceTypeDef,
    UpdateAssetModelResponseTypeDef,
    UpdateAssetResponseTypeDef,
    UpdateGatewayCapabilityConfigurationResponseTypeDef,
    UpdatePortalResponseTypeDef,
)
from .waiter import (
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

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictingOperationException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]

class IoTSiteWiseClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        IoTSiteWiseClient exceptions.
        """
    def associate_assets(
        self, *, assetId: str, hierarchyId: str, childAssetId: str, clientToken: str = None
    ) -> None:
        """
        Associates a child asset with the given parent asset through a hierarchy defined
        in the parent asset's model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.associate_assets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#associate_assets)
        """
    def batch_associate_project_assets(
        self, *, projectId: str, assetIds: List[str], clientToken: str = None
    ) -> BatchAssociateProjectAssetsResponseTypeDef:
        """
        Associates a group (batch) of assets with an IoT SiteWise Monitor project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.batch_associate_project_assets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#batch_associate_project_assets)
        """
    def batch_disassociate_project_assets(
        self, *, projectId: str, assetIds: List[str], clientToken: str = None
    ) -> BatchDisassociateProjectAssetsResponseTypeDef:
        """
        Disassociates a group (batch) of assets from an IoT SiteWise Monitor project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.batch_disassociate_project_assets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#batch_disassociate_project_assets)
        """
    def batch_put_asset_property_value(
        self, *, entries: List["PutAssetPropertyValueEntryTypeDef"]
    ) -> BatchPutAssetPropertyValueResponseTypeDef:
        """
        Sends a list of asset property values to IoT SiteWise.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.batch_put_asset_property_value)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#batch_put_asset_property_value)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#can_paginate)
        """
    def create_access_policy(
        self,
        *,
        accessPolicyIdentity: "IdentityTypeDef",
        accessPolicyResource: "ResourceTypeDef",
        accessPolicyPermission: PermissionType,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateAccessPolicyResponseTypeDef:
        """
        Creates an access policy that grants the specified identity (Amazon Web Services
        SSO user, Amazon Web Services SSO group, or IAM user) access to the specified
        IoT SiteWise Monitor portal or project resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.create_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#create_access_policy)
        """
    def create_asset(
        self,
        *,
        assetName: str,
        assetModelId: str,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateAssetResponseTypeDef:
        """
        Creates an asset from an existing asset model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.create_asset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#create_asset)
        """
    def create_asset_model(
        self,
        *,
        assetModelName: str,
        assetModelDescription: str = None,
        assetModelProperties: List["AssetModelPropertyDefinitionTypeDef"] = None,
        assetModelHierarchies: List["AssetModelHierarchyDefinitionTypeDef"] = None,
        assetModelCompositeModels: List["AssetModelCompositeModelDefinitionTypeDef"] = None,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateAssetModelResponseTypeDef:
        """
        Creates an asset model from specified property and hierarchy definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.create_asset_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#create_asset_model)
        """
    def create_dashboard(
        self,
        *,
        projectId: str,
        dashboardName: str,
        dashboardDefinition: str,
        dashboardDescription: str = None,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateDashboardResponseTypeDef:
        """
        Creates a dashboard in an IoT SiteWise Monitor project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.create_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#create_dashboard)
        """
    def create_gateway(
        self,
        *,
        gatewayName: str,
        gatewayPlatform: "GatewayPlatformTypeDef",
        tags: Dict[str, str] = None
    ) -> CreateGatewayResponseTypeDef:
        """
        Creates a gateway, which is a virtual or edge device that delivers industrial
        data streams from local servers to IoT SiteWise.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.create_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#create_gateway)
        """
    def create_portal(
        self,
        *,
        portalName: str,
        portalContactEmail: str,
        roleArn: str,
        portalDescription: str = None,
        clientToken: str = None,
        portalLogoImageFile: "ImageFileTypeDef" = None,
        tags: Dict[str, str] = None,
        portalAuthMode: AuthModeType = None,
        notificationSenderEmail: str = None,
        alarms: "AlarmsTypeDef" = None
    ) -> CreatePortalResponseTypeDef:
        """
        Creates a portal, which can contain projects and dashboards.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.create_portal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#create_portal)
        """
    def create_project(
        self,
        *,
        portalId: str,
        projectName: str,
        projectDescription: str = None,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateProjectResponseTypeDef:
        """
        Creates a project in the specified portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#create_project)
        """
    def delete_access_policy(
        self, *, accessPolicyId: str, clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Deletes an access policy that grants the specified identity access to the
        specified IoT SiteWise Monitor resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#delete_access_policy)
        """
    def delete_asset(self, *, assetId: str, clientToken: str = None) -> DeleteAssetResponseTypeDef:
        """
        Deletes an asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_asset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#delete_asset)
        """
    def delete_asset_model(
        self, *, assetModelId: str, clientToken: str = None
    ) -> DeleteAssetModelResponseTypeDef:
        """
        Deletes an asset model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_asset_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#delete_asset_model)
        """
    def delete_dashboard(self, *, dashboardId: str, clientToken: str = None) -> Dict[str, Any]:
        """
        Deletes a dashboard from IoT SiteWise Monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#delete_dashboard)
        """
    def delete_gateway(self, *, gatewayId: str) -> None:
        """
        Deletes a gateway from IoT SiteWise.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#delete_gateway)
        """
    def delete_portal(
        self, *, portalId: str, clientToken: str = None
    ) -> DeletePortalResponseTypeDef:
        """
        Deletes a portal from IoT SiteWise Monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_portal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#delete_portal)
        """
    def delete_project(self, *, projectId: str, clientToken: str = None) -> Dict[str, Any]:
        """
        Deletes a project from IoT SiteWise Monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.delete_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#delete_project)
        """
    def describe_access_policy(self, *, accessPolicyId: str) -> DescribeAccessPolicyResponseTypeDef:
        """
        Describes an access policy, which specifies an identity's access to an IoT
        SiteWise Monitor portal or project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#describe_access_policy)
        """
    def describe_asset(self, *, assetId: str) -> DescribeAssetResponseTypeDef:
        """
        Retrieves information about an asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_asset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#describe_asset)
        """
    def describe_asset_model(self, *, assetModelId: str) -> DescribeAssetModelResponseTypeDef:
        """
        Retrieves information about an asset model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_asset_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#describe_asset_model)
        """
    def describe_asset_property(
        self, *, assetId: str, propertyId: str
    ) -> DescribeAssetPropertyResponseTypeDef:
        """
        Retrieves information about an asset property.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_asset_property)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#describe_asset_property)
        """
    def describe_dashboard(self, *, dashboardId: str) -> DescribeDashboardResponseTypeDef:
        """
        Retrieves information about a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#describe_dashboard)
        """
    def describe_default_encryption_configuration(
        self,
    ) -> DescribeDefaultEncryptionConfigurationResponseTypeDef:
        """
        Retrieves information about the default encryption configuration for the Amazon
        Web Services account in the default or specified Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_default_encryption_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#describe_default_encryption_configuration)
        """
    def describe_gateway(self, *, gatewayId: str) -> DescribeGatewayResponseTypeDef:
        """
        Retrieves information about a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#describe_gateway)
        """
    def describe_gateway_capability_configuration(
        self, *, gatewayId: str, capabilityNamespace: str
    ) -> DescribeGatewayCapabilityConfigurationResponseTypeDef:
        """
        Retrieves information about a gateway capability configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_gateway_capability_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#describe_gateway_capability_configuration)
        """
    def describe_logging_options(self) -> DescribeLoggingOptionsResponseTypeDef:
        """
        Retrieves the current IoT SiteWise logging options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#describe_logging_options)
        """
    def describe_portal(self, *, portalId: str) -> DescribePortalResponseTypeDef:
        """
        Retrieves information about a portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_portal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#describe_portal)
        """
    def describe_project(self, *, projectId: str) -> DescribeProjectResponseTypeDef:
        """
        Retrieves information about a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#describe_project)
        """
    def describe_storage_configuration(self) -> DescribeStorageConfigurationResponseTypeDef:
        """
        Retrieves information about the storage configuration for IoT SiteWise.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.describe_storage_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#describe_storage_configuration)
        """
    def disassociate_assets(
        self, *, assetId: str, hierarchyId: str, childAssetId: str, clientToken: str = None
    ) -> None:
        """
        Disassociates a child asset from the given parent asset through a hierarchy
        defined in the parent asset's model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.disassociate_assets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#disassociate_assets)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#generate_presigned_url)
        """
    def get_asset_property_aggregates(
        self,
        *,
        aggregateTypes: List[AggregateTypeType],
        resolution: str,
        startDate: Union[datetime, str],
        endDate: Union[datetime, str],
        assetId: str = None,
        propertyId: str = None,
        propertyAlias: str = None,
        qualities: List[QualityType] = None,
        timeOrdering: TimeOrderingType = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetAssetPropertyAggregatesResponseTypeDef:
        """
        Gets aggregated values for an asset property.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.get_asset_property_aggregates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#get_asset_property_aggregates)
        """
    def get_asset_property_value(
        self, *, assetId: str = None, propertyId: str = None, propertyAlias: str = None
    ) -> GetAssetPropertyValueResponseTypeDef:
        """
        Gets an asset property's current value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.get_asset_property_value)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#get_asset_property_value)
        """
    def get_asset_property_value_history(
        self,
        *,
        assetId: str = None,
        propertyId: str = None,
        propertyAlias: str = None,
        startDate: Union[datetime, str] = None,
        endDate: Union[datetime, str] = None,
        qualities: List[QualityType] = None,
        timeOrdering: TimeOrderingType = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetAssetPropertyValueHistoryResponseTypeDef:
        """
        Gets the history of an asset property's values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.get_asset_property_value_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#get_asset_property_value_history)
        """
    def get_interpolated_asset_property_values(
        self,
        *,
        startTimeInSeconds: int,
        endTimeInSeconds: int,
        quality: QualityType,
        intervalInSeconds: int,
        type: str,
        assetId: str = None,
        propertyId: str = None,
        propertyAlias: str = None,
        startTimeOffsetInNanos: int = None,
        endTimeOffsetInNanos: int = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetInterpolatedAssetPropertyValuesResponseTypeDef:
        """
        Get interpolated values for an asset property for a specified time interval,
        during a period of time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.get_interpolated_asset_property_values)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#get_interpolated_asset_property_values)
        """
    def list_access_policies(
        self,
        *,
        identityType: IdentityTypeType = None,
        identityId: str = None,
        resourceType: ResourceTypeType = None,
        resourceId: str = None,
        iamArn: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListAccessPoliciesResponseTypeDef:
        """
        Retrieves a paginated list of access policies for an identity (an Amazon Web
        Services SSO user, an Amazon Web Services SSO group, or an IAM user) or an IoT
        SiteWise Monitor resource (a portal or project).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.list_access_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#list_access_policies)
        """
    def list_asset_models(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListAssetModelsResponseTypeDef:
        """
        Retrieves a paginated list of summaries of all asset models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.list_asset_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#list_asset_models)
        """
    def list_asset_relationships(
        self,
        *,
        assetId: str,
        traversalType: Literal["PATH_TO_ROOT"],
        nextToken: str = None,
        maxResults: int = None
    ) -> ListAssetRelationshipsResponseTypeDef:
        """
        Retrieves a paginated list of asset relationships for an asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.list_asset_relationships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#list_asset_relationships)
        """
    def list_assets(
        self,
        *,
        nextToken: str = None,
        maxResults: int = None,
        assetModelId: str = None,
        filter: ListAssetsFilterType = None
    ) -> ListAssetsResponseTypeDef:
        """
        Retrieves a paginated list of asset summaries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.list_assets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#list_assets)
        """
    def list_associated_assets(
        self,
        *,
        assetId: str,
        hierarchyId: str = None,
        traversalDirection: TraversalDirectionType = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListAssociatedAssetsResponseTypeDef:
        """
        Retrieves a paginated list of associated assets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.list_associated_assets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#list_associated_assets)
        """
    def list_dashboards(
        self, *, projectId: str, nextToken: str = None, maxResults: int = None
    ) -> ListDashboardsResponseTypeDef:
        """
        Retrieves a paginated list of dashboards for an IoT SiteWise Monitor project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.list_dashboards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#list_dashboards)
        """
    def list_gateways(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListGatewaysResponseTypeDef:
        """
        Retrieves a paginated list of gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.list_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#list_gateways)
        """
    def list_portals(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListPortalsResponseTypeDef:
        """
        Retrieves a paginated list of IoT SiteWise Monitor portals.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.list_portals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#list_portals)
        """
    def list_project_assets(
        self, *, projectId: str, nextToken: str = None, maxResults: int = None
    ) -> ListProjectAssetsResponseTypeDef:
        """
        Retrieves a paginated list of assets associated with an IoT SiteWise Monitor
        project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.list_project_assets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#list_project_assets)
        """
    def list_projects(
        self, *, portalId: str, nextToken: str = None, maxResults: int = None
    ) -> ListProjectsResponseTypeDef:
        """
        Retrieves a paginated list of projects for an IoT SiteWise Monitor portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.list_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#list_projects)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the list of tags for an IoT SiteWise resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#list_tags_for_resource)
        """
    def put_default_encryption_configuration(
        self, *, encryptionType: EncryptionTypeType, kmsKeyId: str = None
    ) -> PutDefaultEncryptionConfigurationResponseTypeDef:
        """
        Sets the default encryption configuration for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.put_default_encryption_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#put_default_encryption_configuration)
        """
    def put_logging_options(self, *, loggingOptions: "LoggingOptionsTypeDef") -> Dict[str, Any]:
        """
        Sets logging options for IoT SiteWise.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.put_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#put_logging_options)
        """
    def put_storage_configuration(
        self, *, storageType: StorageTypeType, multiLayerStorage: "MultiLayerStorageTypeDef" = None
    ) -> PutStorageConfigurationResponseTypeDef:
        """
        Configures storage settings for IoT SiteWise.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.put_storage_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#put_storage_configuration)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds tags to an IoT SiteWise resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from an IoT SiteWise resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#untag_resource)
        """
    def update_access_policy(
        self,
        *,
        accessPolicyId: str,
        accessPolicyIdentity: "IdentityTypeDef",
        accessPolicyResource: "ResourceTypeDef",
        accessPolicyPermission: PermissionType,
        clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Updates an existing access policy that specifies an identity's access to an IoT
        SiteWise Monitor portal or project resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.update_access_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#update_access_policy)
        """
    def update_asset(
        self, *, assetId: str, assetName: str, clientToken: str = None
    ) -> UpdateAssetResponseTypeDef:
        """
        Updates an asset's name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.update_asset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#update_asset)
        """
    def update_asset_model(
        self,
        *,
        assetModelId: str,
        assetModelName: str,
        assetModelDescription: str = None,
        assetModelProperties: List["AssetModelPropertyTypeDef"] = None,
        assetModelHierarchies: List["AssetModelHierarchyTypeDef"] = None,
        assetModelCompositeModels: List["AssetModelCompositeModelTypeDef"] = None,
        clientToken: str = None
    ) -> UpdateAssetModelResponseTypeDef:
        """
        Updates an asset model and all of the assets that were created from the model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.update_asset_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#update_asset_model)
        """
    def update_asset_property(
        self,
        *,
        assetId: str,
        propertyId: str,
        propertyAlias: str = None,
        propertyNotificationState: PropertyNotificationStateType = None,
        clientToken: str = None
    ) -> None:
        """
        Updates an asset property's alias and notification state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.update_asset_property)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#update_asset_property)
        """
    def update_dashboard(
        self,
        *,
        dashboardId: str,
        dashboardName: str,
        dashboardDefinition: str,
        dashboardDescription: str = None,
        clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Updates an IoT SiteWise Monitor dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.update_dashboard)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#update_dashboard)
        """
    def update_gateway(self, *, gatewayId: str, gatewayName: str) -> None:
        """
        Updates a gateway's name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.update_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#update_gateway)
        """
    def update_gateway_capability_configuration(
        self, *, gatewayId: str, capabilityNamespace: str, capabilityConfiguration: str
    ) -> UpdateGatewayCapabilityConfigurationResponseTypeDef:
        """
        Updates a gateway capability configuration or defines a new capability
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.update_gateway_capability_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#update_gateway_capability_configuration)
        """
    def update_portal(
        self,
        *,
        portalId: str,
        portalName: str,
        portalContactEmail: str,
        roleArn: str,
        portalDescription: str = None,
        portalLogoImage: "ImageTypeDef" = None,
        clientToken: str = None,
        notificationSenderEmail: str = None,
        alarms: "AlarmsTypeDef" = None
    ) -> UpdatePortalResponseTypeDef:
        """
        Updates an IoT SiteWise Monitor portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.update_portal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#update_portal)
        """
    def update_project(
        self,
        *,
        projectId: str,
        projectName: str,
        projectDescription: str = None,
        clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Updates an IoT SiteWise Monitor project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Client.update_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client.html#update_project)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_asset_property_aggregates"]
    ) -> GetAssetPropertyAggregatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyAggregates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators.html#getassetpropertyaggregatespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_asset_property_value_history"]
    ) -> GetAssetPropertyValueHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetAssetPropertyValueHistory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators.html#getassetpropertyvaluehistorypaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_interpolated_asset_property_values"]
    ) -> GetInterpolatedAssetPropertyValuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Paginator.GetInterpolatedAssetPropertyValues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators.html#getinterpolatedassetpropertyvaluespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_access_policies"]
    ) -> ListAccessPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAccessPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators.html#listaccesspoliciespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_asset_models"]
    ) -> ListAssetModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetModels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators.html#listassetmodelspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_asset_relationships"]
    ) -> ListAssetRelationshipsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssetRelationships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators.html#listassetrelationshipspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_assets"]) -> ListAssetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators.html#listassetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_associated_assets"]
    ) -> ListAssociatedAssetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListAssociatedAssets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators.html#listassociatedassetspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_dashboards"]) -> ListDashboardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListDashboards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators.html#listdashboardspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_gateways"]) -> ListGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListGateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators.html#listgatewayspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_portals"]) -> ListPortalsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListPortals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators.html#listportalspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_project_assets"]
    ) -> ListProjectAssetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjectAssets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators.html#listprojectassetspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Paginator.ListProjects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/paginators.html#listprojectspaginator)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["asset_active"]) -> AssetActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#assetactivewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["asset_model_active"]) -> AssetModelActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetModelActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#assetmodelactivewaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["asset_model_not_exists"]
    ) -> AssetModelNotExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetModelNotExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#assetmodelnotexistswaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["asset_not_exists"]) -> AssetNotExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Waiter.AssetNotExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#assetnotexistswaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["portal_active"]) -> PortalActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Waiter.PortalActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#portalactivewaiter)
        """
    @overload
    def get_waiter(self, waiter_name: Literal["portal_not_exists"]) -> PortalNotExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotsitewise.html#IoTSiteWise.Waiter.PortalNotExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/waiters.html#portalnotexistswaiter)
        """
