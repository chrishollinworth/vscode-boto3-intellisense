"""
Type annotations for iotsitewise service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iotsitewise.client import IoTSiteWiseClient

    session = Session()
    client: IoTSiteWiseClient = session.client("iotsitewise")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
    ListDashboardsPaginator,
    ListDatasetsPaginator,
    ListGatewaysPaginator,
    ListPortalsPaginator,
    ListProjectAssetsPaginator,
    ListProjectsPaginator,
    ListTimeSeriesPaginator,
)
from .type_defs import (
    AssociateAssetsRequestTypeDef,
    AssociateTimeSeriesToAssetPropertyRequestTypeDef,
    BatchAssociateProjectAssetsRequestTypeDef,
    BatchAssociateProjectAssetsResponseTypeDef,
    BatchDisassociateProjectAssetsRequestTypeDef,
    BatchDisassociateProjectAssetsResponseTypeDef,
    BatchGetAssetPropertyAggregatesRequestTypeDef,
    BatchGetAssetPropertyAggregatesResponseTypeDef,
    BatchGetAssetPropertyValueHistoryRequestTypeDef,
    BatchGetAssetPropertyValueHistoryResponseTypeDef,
    BatchGetAssetPropertyValueRequestTypeDef,
    BatchGetAssetPropertyValueResponseTypeDef,
    BatchPutAssetPropertyValueRequestTypeDef,
    BatchPutAssetPropertyValueResponseTypeDef,
    CreateAccessPolicyRequestTypeDef,
    CreateAccessPolicyResponseTypeDef,
    CreateAssetModelCompositeModelRequestTypeDef,
    CreateAssetModelCompositeModelResponseTypeDef,
    CreateAssetModelRequestTypeDef,
    CreateAssetModelResponseTypeDef,
    CreateAssetRequestTypeDef,
    CreateAssetResponseTypeDef,
    CreateBulkImportJobRequestTypeDef,
    CreateBulkImportJobResponseTypeDef,
    CreateDashboardRequestTypeDef,
    CreateDashboardResponseTypeDef,
    CreateDatasetRequestTypeDef,
    CreateDatasetResponseTypeDef,
    CreateGatewayRequestTypeDef,
    CreateGatewayResponseTypeDef,
    CreatePortalRequestTypeDef,
    CreatePortalResponseTypeDef,
    CreateProjectRequestTypeDef,
    CreateProjectResponseTypeDef,
    DeleteAccessPolicyRequestTypeDef,
    DeleteAssetModelCompositeModelRequestTypeDef,
    DeleteAssetModelCompositeModelResponseTypeDef,
    DeleteAssetModelRequestTypeDef,
    DeleteAssetModelResponseTypeDef,
    DeleteAssetRequestTypeDef,
    DeleteAssetResponseTypeDef,
    DeleteDashboardRequestTypeDef,
    DeleteDatasetRequestTypeDef,
    DeleteDatasetResponseTypeDef,
    DeleteGatewayRequestTypeDef,
    DeletePortalRequestTypeDef,
    DeletePortalResponseTypeDef,
    DeleteProjectRequestTypeDef,
    DeleteTimeSeriesRequestTypeDef,
    DescribeAccessPolicyRequestTypeDef,
    DescribeAccessPolicyResponseTypeDef,
    DescribeActionRequestTypeDef,
    DescribeActionResponseTypeDef,
    DescribeAssetCompositeModelRequestTypeDef,
    DescribeAssetCompositeModelResponseTypeDef,
    DescribeAssetModelCompositeModelRequestTypeDef,
    DescribeAssetModelCompositeModelResponseTypeDef,
    DescribeAssetModelRequestTypeDef,
    DescribeAssetModelResponseTypeDef,
    DescribeAssetPropertyRequestTypeDef,
    DescribeAssetPropertyResponseTypeDef,
    DescribeAssetRequestTypeDef,
    DescribeAssetResponseTypeDef,
    DescribeBulkImportJobRequestTypeDef,
    DescribeBulkImportJobResponseTypeDef,
    DescribeDashboardRequestTypeDef,
    DescribeDashboardResponseTypeDef,
    DescribeDatasetRequestTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeDefaultEncryptionConfigurationResponseTypeDef,
    DescribeGatewayCapabilityConfigurationRequestTypeDef,
    DescribeGatewayCapabilityConfigurationResponseTypeDef,
    DescribeGatewayRequestTypeDef,
    DescribeGatewayResponseTypeDef,
    DescribeLoggingOptionsResponseTypeDef,
    DescribePortalRequestTypeDef,
    DescribePortalResponseTypeDef,
    DescribeProjectRequestTypeDef,
    DescribeProjectResponseTypeDef,
    DescribeStorageConfigurationResponseTypeDef,
    DescribeTimeSeriesRequestTypeDef,
    DescribeTimeSeriesResponseTypeDef,
    DisassociateAssetsRequestTypeDef,
    DisassociateTimeSeriesFromAssetPropertyRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    ExecuteActionRequestTypeDef,
    ExecuteActionResponseTypeDef,
    ExecuteQueryRequestTypeDef,
    ExecuteQueryResponseTypeDef,
    GetAssetPropertyAggregatesRequestTypeDef,
    GetAssetPropertyAggregatesResponseTypeDef,
    GetAssetPropertyValueHistoryRequestTypeDef,
    GetAssetPropertyValueHistoryResponseTypeDef,
    GetAssetPropertyValueRequestTypeDef,
    GetAssetPropertyValueResponseTypeDef,
    GetInterpolatedAssetPropertyValuesRequestTypeDef,
    GetInterpolatedAssetPropertyValuesResponseTypeDef,
    InvokeAssistantRequestTypeDef,
    InvokeAssistantResponseTypeDef,
    ListAccessPoliciesRequestTypeDef,
    ListAccessPoliciesResponseTypeDef,
    ListActionsRequestTypeDef,
    ListActionsResponseTypeDef,
    ListAssetModelCompositeModelsRequestTypeDef,
    ListAssetModelCompositeModelsResponseTypeDef,
    ListAssetModelPropertiesRequestTypeDef,
    ListAssetModelPropertiesResponseTypeDef,
    ListAssetModelsRequestTypeDef,
    ListAssetModelsResponseTypeDef,
    ListAssetPropertiesRequestTypeDef,
    ListAssetPropertiesResponseTypeDef,
    ListAssetRelationshipsRequestTypeDef,
    ListAssetRelationshipsResponseTypeDef,
    ListAssetsRequestTypeDef,
    ListAssetsResponseTypeDef,
    ListAssociatedAssetsRequestTypeDef,
    ListAssociatedAssetsResponseTypeDef,
    ListBulkImportJobsRequestTypeDef,
    ListBulkImportJobsResponseTypeDef,
    ListCompositionRelationshipsRequestTypeDef,
    ListCompositionRelationshipsResponseTypeDef,
    ListDashboardsRequestTypeDef,
    ListDashboardsResponseTypeDef,
    ListDatasetsRequestTypeDef,
    ListDatasetsResponseTypeDef,
    ListGatewaysRequestTypeDef,
    ListGatewaysResponseTypeDef,
    ListPortalsRequestTypeDef,
    ListPortalsResponseTypeDef,
    ListProjectAssetsRequestTypeDef,
    ListProjectAssetsResponseTypeDef,
    ListProjectsRequestTypeDef,
    ListProjectsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTimeSeriesRequestTypeDef,
    ListTimeSeriesResponseTypeDef,
    PutDefaultEncryptionConfigurationRequestTypeDef,
    PutDefaultEncryptionConfigurationResponseTypeDef,
    PutLoggingOptionsRequestTypeDef,
    PutStorageConfigurationRequestTypeDef,
    PutStorageConfigurationResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAccessPolicyRequestTypeDef,
    UpdateAssetModelCompositeModelRequestTypeDef,
    UpdateAssetModelCompositeModelResponseTypeDef,
    UpdateAssetModelRequestTypeDef,
    UpdateAssetModelResponseTypeDef,
    UpdateAssetPropertyRequestTypeDef,
    UpdateAssetRequestTypeDef,
    UpdateAssetResponseTypeDef,
    UpdateDashboardRequestTypeDef,
    UpdateDatasetRequestTypeDef,
    UpdateDatasetResponseTypeDef,
    UpdateGatewayCapabilityConfigurationRequestTypeDef,
    UpdateGatewayCapabilityConfigurationResponseTypeDef,
    UpdateGatewayRequestTypeDef,
    UpdatePortalRequestTypeDef,
    UpdatePortalResponseTypeDef,
    UpdateProjectRequestTypeDef,
)
from .waiter import (
    AssetActiveWaiter,
    AssetModelActiveWaiter,
    AssetModelNotExistsWaiter,
    AssetNotExistsWaiter,
    PortalActiveWaiter,
    PortalNotExistsWaiter,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("IoTSiteWiseClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictingOperationException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    QueryTimeoutException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class IoTSiteWiseClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTSiteWiseClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise.html#IoTSiteWise.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#generate_presigned_url)
        """

    def associate_assets(
        self, **kwargs: Unpack[AssociateAssetsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates a child asset with the given parent asset through a hierarchy
        defined in the parent asset's model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/associate_assets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#associate_assets)
        """

    def associate_time_series_to_asset_property(
        self, **kwargs: Unpack[AssociateTimeSeriesToAssetPropertyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates a time series (data stream) with an asset property.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/associate_time_series_to_asset_property.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#associate_time_series_to_asset_property)
        """

    def batch_associate_project_assets(
        self, **kwargs: Unpack[BatchAssociateProjectAssetsRequestTypeDef]
    ) -> BatchAssociateProjectAssetsResponseTypeDef:
        """
        Associates a group (batch) of assets with an IoT SiteWise Monitor project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/batch_associate_project_assets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#batch_associate_project_assets)
        """

    def batch_disassociate_project_assets(
        self, **kwargs: Unpack[BatchDisassociateProjectAssetsRequestTypeDef]
    ) -> BatchDisassociateProjectAssetsResponseTypeDef:
        """
        Disassociates a group (batch) of assets from an IoT SiteWise Monitor project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/batch_disassociate_project_assets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#batch_disassociate_project_assets)
        """

    def batch_get_asset_property_aggregates(
        self, **kwargs: Unpack[BatchGetAssetPropertyAggregatesRequestTypeDef]
    ) -> BatchGetAssetPropertyAggregatesResponseTypeDef:
        """
        Gets aggregated values (for example, average, minimum, and maximum) for one or
        more asset properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/batch_get_asset_property_aggregates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#batch_get_asset_property_aggregates)
        """

    def batch_get_asset_property_value(
        self, **kwargs: Unpack[BatchGetAssetPropertyValueRequestTypeDef]
    ) -> BatchGetAssetPropertyValueResponseTypeDef:
        """
        Gets the current value for one or more asset properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/batch_get_asset_property_value.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#batch_get_asset_property_value)
        """

    def batch_get_asset_property_value_history(
        self, **kwargs: Unpack[BatchGetAssetPropertyValueHistoryRequestTypeDef]
    ) -> BatchGetAssetPropertyValueHistoryResponseTypeDef:
        """
        Gets the historical values for one or more asset properties.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/batch_get_asset_property_value_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#batch_get_asset_property_value_history)
        """

    def batch_put_asset_property_value(
        self, **kwargs: Unpack[BatchPutAssetPropertyValueRequestTypeDef]
    ) -> BatchPutAssetPropertyValueResponseTypeDef:
        """
        Sends a list of asset property values to IoT SiteWise.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/batch_put_asset_property_value.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#batch_put_asset_property_value)
        """

    def create_access_policy(
        self, **kwargs: Unpack[CreateAccessPolicyRequestTypeDef]
    ) -> CreateAccessPolicyResponseTypeDef:
        """
        Creates an access policy that grants the specified identity (IAM Identity
        Center user, IAM Identity Center group, or IAM user) access to the specified
        IoT SiteWise Monitor portal or project resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/create_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#create_access_policy)
        """

    def create_asset(
        self, **kwargs: Unpack[CreateAssetRequestTypeDef]
    ) -> CreateAssetResponseTypeDef:
        """
        Creates an asset from an existing asset model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/create_asset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#create_asset)
        """

    def create_asset_model(
        self, **kwargs: Unpack[CreateAssetModelRequestTypeDef]
    ) -> CreateAssetModelResponseTypeDef:
        """
        Creates an asset model from specified property and hierarchy definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/create_asset_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#create_asset_model)
        """

    def create_asset_model_composite_model(
        self, **kwargs: Unpack[CreateAssetModelCompositeModelRequestTypeDef]
    ) -> CreateAssetModelCompositeModelResponseTypeDef:
        """
        Creates a custom composite model from specified property and hierarchy
        definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/create_asset_model_composite_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#create_asset_model_composite_model)
        """

    def create_bulk_import_job(
        self, **kwargs: Unpack[CreateBulkImportJobRequestTypeDef]
    ) -> CreateBulkImportJobResponseTypeDef:
        """
        Defines a job to ingest data to IoT SiteWise from Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/create_bulk_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#create_bulk_import_job)
        """

    def create_dashboard(
        self, **kwargs: Unpack[CreateDashboardRequestTypeDef]
    ) -> CreateDashboardResponseTypeDef:
        """
        Creates a dashboard in an IoT SiteWise Monitor project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/create_dashboard.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#create_dashboard)
        """

    def create_dataset(
        self, **kwargs: Unpack[CreateDatasetRequestTypeDef]
    ) -> CreateDatasetResponseTypeDef:
        """
        Creates a dataset to connect an external datasource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/create_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#create_dataset)
        """

    def create_gateway(
        self, **kwargs: Unpack[CreateGatewayRequestTypeDef]
    ) -> CreateGatewayResponseTypeDef:
        """
        Creates a gateway, which is a virtual or edge device that delivers industrial
        data streams from local servers to IoT SiteWise.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/create_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#create_gateway)
        """

    def create_portal(
        self, **kwargs: Unpack[CreatePortalRequestTypeDef]
    ) -> CreatePortalResponseTypeDef:
        """
        Creates a portal, which can contain projects and dashboards.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/create_portal.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#create_portal)
        """

    def create_project(
        self, **kwargs: Unpack[CreateProjectRequestTypeDef]
    ) -> CreateProjectResponseTypeDef:
        """
        Creates a project in the specified portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/create_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#create_project)
        """

    def delete_access_policy(
        self, **kwargs: Unpack[DeleteAccessPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an access policy that grants the specified identity access to the
        specified IoT SiteWise Monitor resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/delete_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#delete_access_policy)
        """

    def delete_asset(
        self, **kwargs: Unpack[DeleteAssetRequestTypeDef]
    ) -> DeleteAssetResponseTypeDef:
        """
        Deletes an asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/delete_asset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#delete_asset)
        """

    def delete_asset_model(
        self, **kwargs: Unpack[DeleteAssetModelRequestTypeDef]
    ) -> DeleteAssetModelResponseTypeDef:
        """
        Deletes an asset model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/delete_asset_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#delete_asset_model)
        """

    def delete_asset_model_composite_model(
        self, **kwargs: Unpack[DeleteAssetModelCompositeModelRequestTypeDef]
    ) -> DeleteAssetModelCompositeModelResponseTypeDef:
        """
        Deletes a composite model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/delete_asset_model_composite_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#delete_asset_model_composite_model)
        """

    def delete_dashboard(self, **kwargs: Unpack[DeleteDashboardRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a dashboard from IoT SiteWise Monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/delete_dashboard.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#delete_dashboard)
        """

    def delete_dataset(
        self, **kwargs: Unpack[DeleteDatasetRequestTypeDef]
    ) -> DeleteDatasetResponseTypeDef:
        """
        Deletes a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/delete_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#delete_dataset)
        """

    def delete_gateway(
        self, **kwargs: Unpack[DeleteGatewayRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a gateway from IoT SiteWise.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/delete_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#delete_gateway)
        """

    def delete_portal(
        self, **kwargs: Unpack[DeletePortalRequestTypeDef]
    ) -> DeletePortalResponseTypeDef:
        """
        Deletes a portal from IoT SiteWise Monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/delete_portal.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#delete_portal)
        """

    def delete_project(self, **kwargs: Unpack[DeleteProjectRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a project from IoT SiteWise Monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/delete_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#delete_project)
        """

    def delete_time_series(
        self, **kwargs: Unpack[DeleteTimeSeriesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a time series (data stream).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/delete_time_series.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#delete_time_series)
        """

    def describe_access_policy(
        self, **kwargs: Unpack[DescribeAccessPolicyRequestTypeDef]
    ) -> DescribeAccessPolicyResponseTypeDef:
        """
        Describes an access policy, which specifies an identity's access to an IoT
        SiteWise Monitor portal or project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_access_policy)
        """

    def describe_action(
        self, **kwargs: Unpack[DescribeActionRequestTypeDef]
    ) -> DescribeActionResponseTypeDef:
        """
        Retrieves information about an action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_action)
        """

    def describe_asset(
        self, **kwargs: Unpack[DescribeAssetRequestTypeDef]
    ) -> DescribeAssetResponseTypeDef:
        """
        Retrieves information about an asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_asset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_asset)
        """

    def describe_asset_composite_model(
        self, **kwargs: Unpack[DescribeAssetCompositeModelRequestTypeDef]
    ) -> DescribeAssetCompositeModelResponseTypeDef:
        """
        Retrieves information about an asset composite model (also known as an asset
        component).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_asset_composite_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_asset_composite_model)
        """

    def describe_asset_model(
        self, **kwargs: Unpack[DescribeAssetModelRequestTypeDef]
    ) -> DescribeAssetModelResponseTypeDef:
        """
        Retrieves information about an asset model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_asset_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_asset_model)
        """

    def describe_asset_model_composite_model(
        self, **kwargs: Unpack[DescribeAssetModelCompositeModelRequestTypeDef]
    ) -> DescribeAssetModelCompositeModelResponseTypeDef:
        """
        Retrieves information about an asset model composite model (also known as an
        asset model component).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_asset_model_composite_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_asset_model_composite_model)
        """

    def describe_asset_property(
        self, **kwargs: Unpack[DescribeAssetPropertyRequestTypeDef]
    ) -> DescribeAssetPropertyResponseTypeDef:
        """
        Retrieves information about an asset property.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_asset_property.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_asset_property)
        """

    def describe_bulk_import_job(
        self, **kwargs: Unpack[DescribeBulkImportJobRequestTypeDef]
    ) -> DescribeBulkImportJobResponseTypeDef:
        """
        Retrieves information about a bulk import job request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_bulk_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_bulk_import_job)
        """

    def describe_dashboard(
        self, **kwargs: Unpack[DescribeDashboardRequestTypeDef]
    ) -> DescribeDashboardResponseTypeDef:
        """
        Retrieves information about a dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_dashboard.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_dashboard)
        """

    def describe_dataset(
        self, **kwargs: Unpack[DescribeDatasetRequestTypeDef]
    ) -> DescribeDatasetResponseTypeDef:
        """
        Retrieves information about a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_dataset)
        """

    def describe_default_encryption_configuration(
        self,
    ) -> DescribeDefaultEncryptionConfigurationResponseTypeDef:
        """
        Retrieves information about the default encryption configuration for the Amazon
        Web Services account in the default or specified Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_default_encryption_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_default_encryption_configuration)
        """

    def describe_gateway(
        self, **kwargs: Unpack[DescribeGatewayRequestTypeDef]
    ) -> DescribeGatewayResponseTypeDef:
        """
        Retrieves information about a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_gateway)
        """

    def describe_gateway_capability_configuration(
        self, **kwargs: Unpack[DescribeGatewayCapabilityConfigurationRequestTypeDef]
    ) -> DescribeGatewayCapabilityConfigurationResponseTypeDef:
        """
        Retrieves information about a gateway capability configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_gateway_capability_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_gateway_capability_configuration)
        """

    def describe_logging_options(self) -> DescribeLoggingOptionsResponseTypeDef:
        """
        Retrieves the current IoT SiteWise logging options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_logging_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_logging_options)
        """

    def describe_portal(
        self, **kwargs: Unpack[DescribePortalRequestTypeDef]
    ) -> DescribePortalResponseTypeDef:
        """
        Retrieves information about a portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_portal.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_portal)
        """

    def describe_project(
        self, **kwargs: Unpack[DescribeProjectRequestTypeDef]
    ) -> DescribeProjectResponseTypeDef:
        """
        Retrieves information about a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_project)
        """

    def describe_storage_configuration(self) -> DescribeStorageConfigurationResponseTypeDef:
        """
        Retrieves information about the storage configuration for IoT SiteWise.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_storage_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_storage_configuration)
        """

    def describe_time_series(
        self, **kwargs: Unpack[DescribeTimeSeriesRequestTypeDef]
    ) -> DescribeTimeSeriesResponseTypeDef:
        """
        Retrieves information about a time series (data stream).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/describe_time_series.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#describe_time_series)
        """

    def disassociate_assets(
        self, **kwargs: Unpack[DisassociateAssetsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates a child asset from the given parent asset through a hierarchy
        defined in the parent asset's model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/disassociate_assets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#disassociate_assets)
        """

    def disassociate_time_series_from_asset_property(
        self, **kwargs: Unpack[DisassociateTimeSeriesFromAssetPropertyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates a time series (data stream) from an asset property.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/disassociate_time_series_from_asset_property.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#disassociate_time_series_from_asset_property)
        """

    def execute_action(
        self, **kwargs: Unpack[ExecuteActionRequestTypeDef]
    ) -> ExecuteActionResponseTypeDef:
        """
        Executes an action on a target resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/execute_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#execute_action)
        """

    def execute_query(
        self, **kwargs: Unpack[ExecuteQueryRequestTypeDef]
    ) -> ExecuteQueryResponseTypeDef:
        """
        Run SQL queries to retrieve metadata and time-series data from asset models,
        assets, measurements, metrics, transforms, and aggregates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/execute_query.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#execute_query)
        """

    def get_asset_property_aggregates(
        self, **kwargs: Unpack[GetAssetPropertyAggregatesRequestTypeDef]
    ) -> GetAssetPropertyAggregatesResponseTypeDef:
        """
        Gets aggregated values for an asset property.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_asset_property_aggregates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_asset_property_aggregates)
        """

    def get_asset_property_value(
        self, **kwargs: Unpack[GetAssetPropertyValueRequestTypeDef]
    ) -> GetAssetPropertyValueResponseTypeDef:
        """
        Gets an asset property's current value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_asset_property_value.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_asset_property_value)
        """

    def get_asset_property_value_history(
        self, **kwargs: Unpack[GetAssetPropertyValueHistoryRequestTypeDef]
    ) -> GetAssetPropertyValueHistoryResponseTypeDef:
        """
        Gets the history of an asset property's values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_asset_property_value_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_asset_property_value_history)
        """

    def get_interpolated_asset_property_values(
        self, **kwargs: Unpack[GetInterpolatedAssetPropertyValuesRequestTypeDef]
    ) -> GetInterpolatedAssetPropertyValuesResponseTypeDef:
        """
        Get interpolated values for an asset property for a specified time interval,
        during a period of time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_interpolated_asset_property_values.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_interpolated_asset_property_values)
        """

    def invoke_assistant(
        self, **kwargs: Unpack[InvokeAssistantRequestTypeDef]
    ) -> InvokeAssistantResponseTypeDef:
        """
        Invokes SiteWise Assistant to start or continue a conversation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/invoke_assistant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#invoke_assistant)
        """

    def list_access_policies(
        self, **kwargs: Unpack[ListAccessPoliciesRequestTypeDef]
    ) -> ListAccessPoliciesResponseTypeDef:
        """
        Retrieves a paginated list of access policies for an identity (an IAM Identity
        Center user, an IAM Identity Center group, or an IAM user) or an IoT SiteWise
        Monitor resource (a portal or project).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_access_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_access_policies)
        """

    def list_actions(
        self, **kwargs: Unpack[ListActionsRequestTypeDef]
    ) -> ListActionsResponseTypeDef:
        """
        Retrieves a paginated list of actions for a specific target resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_actions)
        """

    def list_asset_model_composite_models(
        self, **kwargs: Unpack[ListAssetModelCompositeModelsRequestTypeDef]
    ) -> ListAssetModelCompositeModelsResponseTypeDef:
        """
        Retrieves a paginated list of composite models associated with the asset model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_asset_model_composite_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_asset_model_composite_models)
        """

    def list_asset_model_properties(
        self, **kwargs: Unpack[ListAssetModelPropertiesRequestTypeDef]
    ) -> ListAssetModelPropertiesResponseTypeDef:
        """
        Retrieves a paginated list of properties associated with an asset model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_asset_model_properties.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_asset_model_properties)
        """

    def list_asset_models(
        self, **kwargs: Unpack[ListAssetModelsRequestTypeDef]
    ) -> ListAssetModelsResponseTypeDef:
        """
        Retrieves a paginated list of summaries of all asset models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_asset_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_asset_models)
        """

    def list_asset_properties(
        self, **kwargs: Unpack[ListAssetPropertiesRequestTypeDef]
    ) -> ListAssetPropertiesResponseTypeDef:
        """
        Retrieves a paginated list of properties associated with an asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_asset_properties.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_asset_properties)
        """

    def list_asset_relationships(
        self, **kwargs: Unpack[ListAssetRelationshipsRequestTypeDef]
    ) -> ListAssetRelationshipsResponseTypeDef:
        """
        Retrieves a paginated list of asset relationships for an asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_asset_relationships.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_asset_relationships)
        """

    def list_assets(self, **kwargs: Unpack[ListAssetsRequestTypeDef]) -> ListAssetsResponseTypeDef:
        """
        Retrieves a paginated list of asset summaries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_assets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_assets)
        """

    def list_associated_assets(
        self, **kwargs: Unpack[ListAssociatedAssetsRequestTypeDef]
    ) -> ListAssociatedAssetsResponseTypeDef:
        """
        Retrieves a paginated list of associated assets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_associated_assets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_associated_assets)
        """

    def list_bulk_import_jobs(
        self, **kwargs: Unpack[ListBulkImportJobsRequestTypeDef]
    ) -> ListBulkImportJobsResponseTypeDef:
        """
        Retrieves a paginated list of bulk import job requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_bulk_import_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_bulk_import_jobs)
        """

    def list_composition_relationships(
        self, **kwargs: Unpack[ListCompositionRelationshipsRequestTypeDef]
    ) -> ListCompositionRelationshipsResponseTypeDef:
        """
        Retrieves a paginated list of composition relationships for an asset model of
        type <code>COMPONENT_MODEL</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_composition_relationships.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_composition_relationships)
        """

    def list_dashboards(
        self, **kwargs: Unpack[ListDashboardsRequestTypeDef]
    ) -> ListDashboardsResponseTypeDef:
        """
        Retrieves a paginated list of dashboards for an IoT SiteWise Monitor project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_dashboards.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_dashboards)
        """

    def list_datasets(
        self, **kwargs: Unpack[ListDatasetsRequestTypeDef]
    ) -> ListDatasetsResponseTypeDef:
        """
        Retrieves a paginated list of datasets for a specific target resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_datasets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_datasets)
        """

    def list_gateways(
        self, **kwargs: Unpack[ListGatewaysRequestTypeDef]
    ) -> ListGatewaysResponseTypeDef:
        """
        Retrieves a paginated list of gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_gateways)
        """

    def list_portals(
        self, **kwargs: Unpack[ListPortalsRequestTypeDef]
    ) -> ListPortalsResponseTypeDef:
        """
        Retrieves a paginated list of IoT SiteWise Monitor portals.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_portals.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_portals)
        """

    def list_project_assets(
        self, **kwargs: Unpack[ListProjectAssetsRequestTypeDef]
    ) -> ListProjectAssetsResponseTypeDef:
        """
        Retrieves a paginated list of assets associated with an IoT SiteWise Monitor
        project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_project_assets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_project_assets)
        """

    def list_projects(
        self, **kwargs: Unpack[ListProjectsRequestTypeDef]
    ) -> ListProjectsResponseTypeDef:
        """
        Retrieves a paginated list of projects for an IoT SiteWise Monitor portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_projects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_projects)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the list of tags for an IoT SiteWise resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_tags_for_resource)
        """

    def list_time_series(
        self, **kwargs: Unpack[ListTimeSeriesRequestTypeDef]
    ) -> ListTimeSeriesResponseTypeDef:
        """
        Retrieves a paginated list of time series (data streams).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/list_time_series.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#list_time_series)
        """

    def put_default_encryption_configuration(
        self, **kwargs: Unpack[PutDefaultEncryptionConfigurationRequestTypeDef]
    ) -> PutDefaultEncryptionConfigurationResponseTypeDef:
        """
        Sets the default encryption configuration for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/put_default_encryption_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#put_default_encryption_configuration)
        """

    def put_logging_options(
        self, **kwargs: Unpack[PutLoggingOptionsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sets logging options for IoT SiteWise.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/put_logging_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#put_logging_options)
        """

    def put_storage_configuration(
        self, **kwargs: Unpack[PutStorageConfigurationRequestTypeDef]
    ) -> PutStorageConfigurationResponseTypeDef:
        """
        Configures storage settings for IoT SiteWise.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/put_storage_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#put_storage_configuration)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds tags to an IoT SiteWise resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag from an IoT SiteWise resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#untag_resource)
        """

    def update_access_policy(
        self, **kwargs: Unpack[UpdateAccessPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates an existing access policy that specifies an identity's access to an IoT
        SiteWise Monitor portal or project resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/update_access_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#update_access_policy)
        """

    def update_asset(
        self, **kwargs: Unpack[UpdateAssetRequestTypeDef]
    ) -> UpdateAssetResponseTypeDef:
        """
        Updates an asset's name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/update_asset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#update_asset)
        """

    def update_asset_model(
        self, **kwargs: Unpack[UpdateAssetModelRequestTypeDef]
    ) -> UpdateAssetModelResponseTypeDef:
        """
        Updates an asset model and all of the assets that were created from the model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/update_asset_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#update_asset_model)
        """

    def update_asset_model_composite_model(
        self, **kwargs: Unpack[UpdateAssetModelCompositeModelRequestTypeDef]
    ) -> UpdateAssetModelCompositeModelResponseTypeDef:
        """
        Updates a composite model and all of the assets that were created from the
        model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/update_asset_model_composite_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#update_asset_model_composite_model)
        """

    def update_asset_property(
        self, **kwargs: Unpack[UpdateAssetPropertyRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates an asset property's alias and notification state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/update_asset_property.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#update_asset_property)
        """

    def update_dashboard(self, **kwargs: Unpack[UpdateDashboardRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates an IoT SiteWise Monitor dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/update_dashboard.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#update_dashboard)
        """

    def update_dataset(
        self, **kwargs: Unpack[UpdateDatasetRequestTypeDef]
    ) -> UpdateDatasetResponseTypeDef:
        """
        Updates a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/update_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#update_dataset)
        """

    def update_gateway(
        self, **kwargs: Unpack[UpdateGatewayRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates a gateway's name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/update_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#update_gateway)
        """

    def update_gateway_capability_configuration(
        self, **kwargs: Unpack[UpdateGatewayCapabilityConfigurationRequestTypeDef]
    ) -> UpdateGatewayCapabilityConfigurationResponseTypeDef:
        """
        Updates a gateway capability configuration or defines a new capability
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/update_gateway_capability_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#update_gateway_capability_configuration)
        """

    def update_portal(
        self, **kwargs: Unpack[UpdatePortalRequestTypeDef]
    ) -> UpdatePortalResponseTypeDef:
        """
        Updates an IoT SiteWise Monitor portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/update_portal.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#update_portal)
        """

    def update_project(self, **kwargs: Unpack[UpdateProjectRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates an IoT SiteWise Monitor project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/update_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#update_project)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["execute_query"]
    ) -> ExecuteQueryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_asset_property_aggregates"]
    ) -> GetAssetPropertyAggregatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_asset_property_value_history"]
    ) -> GetAssetPropertyValueHistoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_interpolated_asset_property_values"]
    ) -> GetInterpolatedAssetPropertyValuesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_access_policies"]
    ) -> ListAccessPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_actions"]
    ) -> ListActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_asset_model_composite_models"]
    ) -> ListAssetModelCompositeModelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_asset_model_properties"]
    ) -> ListAssetModelPropertiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_asset_models"]
    ) -> ListAssetModelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_asset_properties"]
    ) -> ListAssetPropertiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_asset_relationships"]
    ) -> ListAssetRelationshipsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_assets"]
    ) -> ListAssetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_associated_assets"]
    ) -> ListAssociatedAssetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_bulk_import_jobs"]
    ) -> ListBulkImportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_composition_relationships"]
    ) -> ListCompositionRelationshipsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dashboards"]
    ) -> ListDashboardsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_datasets"]
    ) -> ListDatasetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_gateways"]
    ) -> ListGatewaysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_portals"]
    ) -> ListPortalsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_project_assets"]
    ) -> ListProjectAssetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_projects"]
    ) -> ListProjectsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_time_series"]
    ) -> ListTimeSeriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["asset_active"]
    ) -> AssetActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["asset_model_active"]
    ) -> AssetModelActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["asset_model_not_exists"]
    ) -> AssetModelNotExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["asset_not_exists"]
    ) -> AssetNotExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["portal_active"]
    ) -> PortalActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["portal_not_exists"]
    ) -> PortalNotExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotsitewise/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/client/#get_waiter)
        """
