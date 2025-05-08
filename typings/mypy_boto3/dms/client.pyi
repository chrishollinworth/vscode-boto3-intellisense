"""
Type annotations for dms service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_dms.client import DatabaseMigrationServiceClient

    session = Session()
    client: DatabaseMigrationServiceClient = session.client("dms")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeCertificatesPaginator,
    DescribeConnectionsPaginator,
    DescribeDataMigrationsPaginator,
    DescribeEndpointsPaginator,
    DescribeEndpointTypesPaginator,
    DescribeEventsPaginator,
    DescribeEventSubscriptionsPaginator,
    DescribeOrderableReplicationInstancesPaginator,
    DescribeReplicationInstancesPaginator,
    DescribeReplicationSubnetGroupsPaginator,
    DescribeReplicationTaskAssessmentResultsPaginator,
    DescribeReplicationTasksPaginator,
    DescribeSchemasPaginator,
    DescribeTableStatisticsPaginator,
)
from .type_defs import (
    AddTagsToResourceMessageTypeDef,
    ApplyPendingMaintenanceActionMessageTypeDef,
    ApplyPendingMaintenanceActionResponseTypeDef,
    BatchStartRecommendationsRequestTypeDef,
    BatchStartRecommendationsResponseTypeDef,
    CancelReplicationTaskAssessmentRunMessageTypeDef,
    CancelReplicationTaskAssessmentRunResponseTypeDef,
    CreateDataMigrationMessageTypeDef,
    CreateDataMigrationResponseTypeDef,
    CreateDataProviderMessageTypeDef,
    CreateDataProviderResponseTypeDef,
    CreateEndpointMessageTypeDef,
    CreateEndpointResponseTypeDef,
    CreateEventSubscriptionMessageTypeDef,
    CreateEventSubscriptionResponseTypeDef,
    CreateFleetAdvisorCollectorRequestTypeDef,
    CreateFleetAdvisorCollectorResponseTypeDef,
    CreateInstanceProfileMessageTypeDef,
    CreateInstanceProfileResponseTypeDef,
    CreateMigrationProjectMessageTypeDef,
    CreateMigrationProjectResponseTypeDef,
    CreateReplicationConfigMessageTypeDef,
    CreateReplicationConfigResponseTypeDef,
    CreateReplicationInstanceMessageTypeDef,
    CreateReplicationInstanceResponseTypeDef,
    CreateReplicationSubnetGroupMessageTypeDef,
    CreateReplicationSubnetGroupResponseTypeDef,
    CreateReplicationTaskMessageTypeDef,
    CreateReplicationTaskResponseTypeDef,
    DeleteCertificateMessageTypeDef,
    DeleteCertificateResponseTypeDef,
    DeleteCollectorRequestTypeDef,
    DeleteConnectionMessageTypeDef,
    DeleteConnectionResponseTypeDef,
    DeleteDataMigrationMessageTypeDef,
    DeleteDataMigrationResponseTypeDef,
    DeleteDataProviderMessageTypeDef,
    DeleteDataProviderResponseTypeDef,
    DeleteEndpointMessageTypeDef,
    DeleteEndpointResponseTypeDef,
    DeleteEventSubscriptionMessageTypeDef,
    DeleteEventSubscriptionResponseTypeDef,
    DeleteFleetAdvisorDatabasesRequestTypeDef,
    DeleteFleetAdvisorDatabasesResponseTypeDef,
    DeleteInstanceProfileMessageTypeDef,
    DeleteInstanceProfileResponseTypeDef,
    DeleteMigrationProjectMessageTypeDef,
    DeleteMigrationProjectResponseTypeDef,
    DeleteReplicationConfigMessageTypeDef,
    DeleteReplicationConfigResponseTypeDef,
    DeleteReplicationInstanceMessageTypeDef,
    DeleteReplicationInstanceResponseTypeDef,
    DeleteReplicationSubnetGroupMessageTypeDef,
    DeleteReplicationTaskAssessmentRunMessageTypeDef,
    DeleteReplicationTaskAssessmentRunResponseTypeDef,
    DeleteReplicationTaskMessageTypeDef,
    DeleteReplicationTaskResponseTypeDef,
    DescribeAccountAttributesResponseTypeDef,
    DescribeApplicableIndividualAssessmentsMessageTypeDef,
    DescribeApplicableIndividualAssessmentsResponseTypeDef,
    DescribeCertificatesMessageTypeDef,
    DescribeCertificatesResponseTypeDef,
    DescribeConnectionsMessageTypeDef,
    DescribeConnectionsResponseTypeDef,
    DescribeConversionConfigurationMessageTypeDef,
    DescribeConversionConfigurationResponseTypeDef,
    DescribeDataMigrationsMessageTypeDef,
    DescribeDataMigrationsResponseTypeDef,
    DescribeDataProvidersMessageTypeDef,
    DescribeDataProvidersResponseTypeDef,
    DescribeEndpointSettingsMessageTypeDef,
    DescribeEndpointSettingsResponseTypeDef,
    DescribeEndpointsMessageTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeEndpointTypesMessageTypeDef,
    DescribeEndpointTypesResponseTypeDef,
    DescribeEngineVersionsMessageTypeDef,
    DescribeEngineVersionsResponseTypeDef,
    DescribeEventCategoriesMessageTypeDef,
    DescribeEventCategoriesResponseTypeDef,
    DescribeEventsMessageTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeEventSubscriptionsMessageTypeDef,
    DescribeEventSubscriptionsResponseTypeDef,
    DescribeExtensionPackAssociationsMessageTypeDef,
    DescribeExtensionPackAssociationsResponseTypeDef,
    DescribeFleetAdvisorCollectorsRequestTypeDef,
    DescribeFleetAdvisorCollectorsResponseTypeDef,
    DescribeFleetAdvisorDatabasesRequestTypeDef,
    DescribeFleetAdvisorDatabasesResponseTypeDef,
    DescribeFleetAdvisorLsaAnalysisRequestTypeDef,
    DescribeFleetAdvisorLsaAnalysisResponseTypeDef,
    DescribeFleetAdvisorSchemaObjectSummaryRequestTypeDef,
    DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef,
    DescribeFleetAdvisorSchemasRequestTypeDef,
    DescribeFleetAdvisorSchemasResponseTypeDef,
    DescribeInstanceProfilesMessageTypeDef,
    DescribeInstanceProfilesResponseTypeDef,
    DescribeMetadataModelAssessmentsMessageTypeDef,
    DescribeMetadataModelAssessmentsResponseTypeDef,
    DescribeMetadataModelConversionsMessageTypeDef,
    DescribeMetadataModelConversionsResponseTypeDef,
    DescribeMetadataModelExportsAsScriptMessageTypeDef,
    DescribeMetadataModelExportsAsScriptResponseTypeDef,
    DescribeMetadataModelExportsToTargetMessageTypeDef,
    DescribeMetadataModelExportsToTargetResponseTypeDef,
    DescribeMetadataModelImportsMessageTypeDef,
    DescribeMetadataModelImportsResponseTypeDef,
    DescribeMigrationProjectsMessageTypeDef,
    DescribeMigrationProjectsResponseTypeDef,
    DescribeOrderableReplicationInstancesMessageTypeDef,
    DescribeOrderableReplicationInstancesResponseTypeDef,
    DescribePendingMaintenanceActionsMessageTypeDef,
    DescribePendingMaintenanceActionsResponseTypeDef,
    DescribeRecommendationLimitationsRequestTypeDef,
    DescribeRecommendationLimitationsResponseTypeDef,
    DescribeRecommendationsRequestTypeDef,
    DescribeRecommendationsResponseTypeDef,
    DescribeRefreshSchemasStatusMessageTypeDef,
    DescribeRefreshSchemasStatusResponseTypeDef,
    DescribeReplicationConfigsMessageTypeDef,
    DescribeReplicationConfigsResponseTypeDef,
    DescribeReplicationInstancesMessageTypeDef,
    DescribeReplicationInstancesResponseTypeDef,
    DescribeReplicationInstanceTaskLogsMessageTypeDef,
    DescribeReplicationInstanceTaskLogsResponseTypeDef,
    DescribeReplicationsMessageTypeDef,
    DescribeReplicationsResponseTypeDef,
    DescribeReplicationSubnetGroupsMessageTypeDef,
    DescribeReplicationSubnetGroupsResponseTypeDef,
    DescribeReplicationTableStatisticsMessageTypeDef,
    DescribeReplicationTableStatisticsResponseTypeDef,
    DescribeReplicationTaskAssessmentResultsMessageTypeDef,
    DescribeReplicationTaskAssessmentResultsResponseTypeDef,
    DescribeReplicationTaskAssessmentRunsMessageTypeDef,
    DescribeReplicationTaskAssessmentRunsResponseTypeDef,
    DescribeReplicationTaskIndividualAssessmentsMessageTypeDef,
    DescribeReplicationTaskIndividualAssessmentsResponseTypeDef,
    DescribeReplicationTasksMessageTypeDef,
    DescribeReplicationTasksResponseTypeDef,
    DescribeSchemasMessageTypeDef,
    DescribeSchemasResponseTypeDef,
    DescribeTableStatisticsMessageTypeDef,
    DescribeTableStatisticsResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    ExportMetadataModelAssessmentMessageTypeDef,
    ExportMetadataModelAssessmentResponseTypeDef,
    ImportCertificateMessageTypeDef,
    ImportCertificateResponseTypeDef,
    ListTagsForResourceMessageTypeDef,
    ListTagsForResourceResponseTypeDef,
    ModifyConversionConfigurationMessageTypeDef,
    ModifyConversionConfigurationResponseTypeDef,
    ModifyDataMigrationMessageTypeDef,
    ModifyDataMigrationResponseTypeDef,
    ModifyDataProviderMessageTypeDef,
    ModifyDataProviderResponseTypeDef,
    ModifyEndpointMessageTypeDef,
    ModifyEndpointResponseTypeDef,
    ModifyEventSubscriptionMessageTypeDef,
    ModifyEventSubscriptionResponseTypeDef,
    ModifyInstanceProfileMessageTypeDef,
    ModifyInstanceProfileResponseTypeDef,
    ModifyMigrationProjectMessageTypeDef,
    ModifyMigrationProjectResponseTypeDef,
    ModifyReplicationConfigMessageTypeDef,
    ModifyReplicationConfigResponseTypeDef,
    ModifyReplicationInstanceMessageTypeDef,
    ModifyReplicationInstanceResponseTypeDef,
    ModifyReplicationSubnetGroupMessageTypeDef,
    ModifyReplicationSubnetGroupResponseTypeDef,
    ModifyReplicationTaskMessageTypeDef,
    ModifyReplicationTaskResponseTypeDef,
    MoveReplicationTaskMessageTypeDef,
    MoveReplicationTaskResponseTypeDef,
    RebootReplicationInstanceMessageTypeDef,
    RebootReplicationInstanceResponseTypeDef,
    RefreshSchemasMessageTypeDef,
    RefreshSchemasResponseTypeDef,
    ReloadReplicationTablesMessageTypeDef,
    ReloadReplicationTablesResponseTypeDef,
    ReloadTablesMessageTypeDef,
    ReloadTablesResponseTypeDef,
    RemoveTagsFromResourceMessageTypeDef,
    RunFleetAdvisorLsaAnalysisResponseTypeDef,
    StartDataMigrationMessageTypeDef,
    StartDataMigrationResponseTypeDef,
    StartExtensionPackAssociationMessageTypeDef,
    StartExtensionPackAssociationResponseTypeDef,
    StartMetadataModelAssessmentMessageTypeDef,
    StartMetadataModelAssessmentResponseTypeDef,
    StartMetadataModelConversionMessageTypeDef,
    StartMetadataModelConversionResponseTypeDef,
    StartMetadataModelExportAsScriptMessageTypeDef,
    StartMetadataModelExportAsScriptResponseTypeDef,
    StartMetadataModelExportToTargetMessageTypeDef,
    StartMetadataModelExportToTargetResponseTypeDef,
    StartMetadataModelImportMessageTypeDef,
    StartMetadataModelImportResponseTypeDef,
    StartRecommendationsRequestTypeDef,
    StartReplicationMessageTypeDef,
    StartReplicationResponseTypeDef,
    StartReplicationTaskAssessmentMessageTypeDef,
    StartReplicationTaskAssessmentResponseTypeDef,
    StartReplicationTaskAssessmentRunMessageTypeDef,
    StartReplicationTaskAssessmentRunResponseTypeDef,
    StartReplicationTaskMessageTypeDef,
    StartReplicationTaskResponseTypeDef,
    StopDataMigrationMessageTypeDef,
    StopDataMigrationResponseTypeDef,
    StopReplicationMessageTypeDef,
    StopReplicationResponseTypeDef,
    StopReplicationTaskMessageTypeDef,
    StopReplicationTaskResponseTypeDef,
    TestConnectionMessageTypeDef,
    TestConnectionResponseTypeDef,
    UpdateSubscriptionsToEventBridgeMessageTypeDef,
    UpdateSubscriptionsToEventBridgeResponseTypeDef,
)
from .waiter import (
    EndpointDeletedWaiter,
    ReplicationInstanceAvailableWaiter,
    ReplicationInstanceDeletedWaiter,
    ReplicationTaskDeletedWaiter,
    ReplicationTaskReadyWaiter,
    ReplicationTaskRunningWaiter,
    ReplicationTaskStoppedWaiter,
    TestConnectionSucceedsWaiter,
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

__all__ = ("DatabaseMigrationServiceClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CollectorNotFoundFault: Type[BotocoreClientError]
    FailedDependencyFault: Type[BotocoreClientError]
    InsufficientResourceCapacityFault: Type[BotocoreClientError]
    InvalidCertificateFault: Type[BotocoreClientError]
    InvalidOperationFault: Type[BotocoreClientError]
    InvalidResourceStateFault: Type[BotocoreClientError]
    InvalidSubnet: Type[BotocoreClientError]
    KMSAccessDeniedFault: Type[BotocoreClientError]
    KMSDisabledFault: Type[BotocoreClientError]
    KMSFault: Type[BotocoreClientError]
    KMSInvalidStateFault: Type[BotocoreClientError]
    KMSKeyNotAccessibleFault: Type[BotocoreClientError]
    KMSNotFoundFault: Type[BotocoreClientError]
    KMSThrottlingFault: Type[BotocoreClientError]
    ReplicationSubnetGroupDoesNotCoverEnoughAZs: Type[BotocoreClientError]
    ResourceAlreadyExistsFault: Type[BotocoreClientError]
    ResourceNotFoundFault: Type[BotocoreClientError]
    ResourceQuotaExceededFault: Type[BotocoreClientError]
    S3AccessDeniedFault: Type[BotocoreClientError]
    S3ResourceNotFoundFault: Type[BotocoreClientError]
    SNSInvalidTopicFault: Type[BotocoreClientError]
    SNSNoAuthorizationFault: Type[BotocoreClientError]
    StorageQuotaExceededFault: Type[BotocoreClientError]
    SubnetAlreadyInUse: Type[BotocoreClientError]
    UpgradeDependencyFailureFault: Type[BotocoreClientError]

class DatabaseMigrationServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DatabaseMigrationServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms.html#DatabaseMigrationService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#generate_presigned_url)
        """

    def add_tags_to_resource(
        self, **kwargs: Unpack[AddTagsToResourceMessageTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds metadata tags to an DMS resource, including replication instance,
        endpoint, subnet group, and migration task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/add_tags_to_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#add_tags_to_resource)
        """

    def apply_pending_maintenance_action(
        self, **kwargs: Unpack[ApplyPendingMaintenanceActionMessageTypeDef]
    ) -> ApplyPendingMaintenanceActionResponseTypeDef:
        """
        Applies a pending maintenance action to a resource (for example, to a
        replication instance).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/apply_pending_maintenance_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#apply_pending_maintenance_action)
        """

    def batch_start_recommendations(
        self, **kwargs: Unpack[BatchStartRecommendationsRequestTypeDef]
    ) -> BatchStartRecommendationsResponseTypeDef:
        """
        Starts the analysis of up to 20 source databases to recommend target engines
        for each source database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/batch_start_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#batch_start_recommendations)
        """

    def cancel_replication_task_assessment_run(
        self, **kwargs: Unpack[CancelReplicationTaskAssessmentRunMessageTypeDef]
    ) -> CancelReplicationTaskAssessmentRunResponseTypeDef:
        """
        Cancels a single premigration assessment run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/cancel_replication_task_assessment_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#cancel_replication_task_assessment_run)
        """

    def create_data_migration(
        self, **kwargs: Unpack[CreateDataMigrationMessageTypeDef]
    ) -> CreateDataMigrationResponseTypeDef:
        """
        Creates a data migration using the provided settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/create_data_migration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#create_data_migration)
        """

    def create_data_provider(
        self, **kwargs: Unpack[CreateDataProviderMessageTypeDef]
    ) -> CreateDataProviderResponseTypeDef:
        """
        Creates a data provider using the provided settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/create_data_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#create_data_provider)
        """

    def create_endpoint(
        self, **kwargs: Unpack[CreateEndpointMessageTypeDef]
    ) -> CreateEndpointResponseTypeDef:
        """
        Creates an endpoint using the provided settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/create_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#create_endpoint)
        """

    def create_event_subscription(
        self, **kwargs: Unpack[CreateEventSubscriptionMessageTypeDef]
    ) -> CreateEventSubscriptionResponseTypeDef:
        """
        Creates an DMS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/create_event_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#create_event_subscription)
        """

    def create_fleet_advisor_collector(
        self, **kwargs: Unpack[CreateFleetAdvisorCollectorRequestTypeDef]
    ) -> CreateFleetAdvisorCollectorResponseTypeDef:
        """
        Creates a Fleet Advisor collector using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/create_fleet_advisor_collector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#create_fleet_advisor_collector)
        """

    def create_instance_profile(
        self, **kwargs: Unpack[CreateInstanceProfileMessageTypeDef]
    ) -> CreateInstanceProfileResponseTypeDef:
        """
        Creates the instance profile using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/create_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#create_instance_profile)
        """

    def create_migration_project(
        self, **kwargs: Unpack[CreateMigrationProjectMessageTypeDef]
    ) -> CreateMigrationProjectResponseTypeDef:
        """
        Creates the migration project using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/create_migration_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#create_migration_project)
        """

    def create_replication_config(
        self, **kwargs: Unpack[CreateReplicationConfigMessageTypeDef]
    ) -> CreateReplicationConfigResponseTypeDef:
        """
        Creates a configuration that you can later provide to configure and start an
        DMS Serverless replication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/create_replication_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#create_replication_config)
        """

    def create_replication_instance(
        self, **kwargs: Unpack[CreateReplicationInstanceMessageTypeDef]
    ) -> CreateReplicationInstanceResponseTypeDef:
        """
        Creates the replication instance using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/create_replication_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#create_replication_instance)
        """

    def create_replication_subnet_group(
        self, **kwargs: Unpack[CreateReplicationSubnetGroupMessageTypeDef]
    ) -> CreateReplicationSubnetGroupResponseTypeDef:
        """
        Creates a replication subnet group given a list of the subnet IDs in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/create_replication_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#create_replication_subnet_group)
        """

    def create_replication_task(
        self, **kwargs: Unpack[CreateReplicationTaskMessageTypeDef]
    ) -> CreateReplicationTaskResponseTypeDef:
        """
        Creates a replication task using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/create_replication_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#create_replication_task)
        """

    def delete_certificate(
        self, **kwargs: Unpack[DeleteCertificateMessageTypeDef]
    ) -> DeleteCertificateResponseTypeDef:
        """
        Deletes the specified certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/delete_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#delete_certificate)
        """

    def delete_connection(
        self, **kwargs: Unpack[DeleteConnectionMessageTypeDef]
    ) -> DeleteConnectionResponseTypeDef:
        """
        Deletes the connection between a replication instance and an endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/delete_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#delete_connection)
        """

    def delete_data_migration(
        self, **kwargs: Unpack[DeleteDataMigrationMessageTypeDef]
    ) -> DeleteDataMigrationResponseTypeDef:
        """
        Deletes the specified data migration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/delete_data_migration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#delete_data_migration)
        """

    def delete_data_provider(
        self, **kwargs: Unpack[DeleteDataProviderMessageTypeDef]
    ) -> DeleteDataProviderResponseTypeDef:
        """
        Deletes the specified data provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/delete_data_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#delete_data_provider)
        """

    def delete_endpoint(
        self, **kwargs: Unpack[DeleteEndpointMessageTypeDef]
    ) -> DeleteEndpointResponseTypeDef:
        """
        Deletes the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/delete_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#delete_endpoint)
        """

    def delete_event_subscription(
        self, **kwargs: Unpack[DeleteEventSubscriptionMessageTypeDef]
    ) -> DeleteEventSubscriptionResponseTypeDef:
        """
        Deletes an DMS event subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/delete_event_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#delete_event_subscription)
        """

    def delete_fleet_advisor_collector(
        self, **kwargs: Unpack[DeleteCollectorRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified Fleet Advisor collector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/delete_fleet_advisor_collector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#delete_fleet_advisor_collector)
        """

    def delete_fleet_advisor_databases(
        self, **kwargs: Unpack[DeleteFleetAdvisorDatabasesRequestTypeDef]
    ) -> DeleteFleetAdvisorDatabasesResponseTypeDef:
        """
        Deletes the specified Fleet Advisor collector databases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/delete_fleet_advisor_databases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#delete_fleet_advisor_databases)
        """

    def delete_instance_profile(
        self, **kwargs: Unpack[DeleteInstanceProfileMessageTypeDef]
    ) -> DeleteInstanceProfileResponseTypeDef:
        """
        Deletes the specified instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/delete_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#delete_instance_profile)
        """

    def delete_migration_project(
        self, **kwargs: Unpack[DeleteMigrationProjectMessageTypeDef]
    ) -> DeleteMigrationProjectResponseTypeDef:
        """
        Deletes the specified migration project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/delete_migration_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#delete_migration_project)
        """

    def delete_replication_config(
        self, **kwargs: Unpack[DeleteReplicationConfigMessageTypeDef]
    ) -> DeleteReplicationConfigResponseTypeDef:
        """
        Deletes an DMS Serverless replication configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/delete_replication_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#delete_replication_config)
        """

    def delete_replication_instance(
        self, **kwargs: Unpack[DeleteReplicationInstanceMessageTypeDef]
    ) -> DeleteReplicationInstanceResponseTypeDef:
        """
        Deletes the specified replication instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/delete_replication_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#delete_replication_instance)
        """

    def delete_replication_subnet_group(
        self, **kwargs: Unpack[DeleteReplicationSubnetGroupMessageTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/delete_replication_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#delete_replication_subnet_group)
        """

    def delete_replication_task(
        self, **kwargs: Unpack[DeleteReplicationTaskMessageTypeDef]
    ) -> DeleteReplicationTaskResponseTypeDef:
        """
        Deletes the specified replication task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/delete_replication_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#delete_replication_task)
        """

    def delete_replication_task_assessment_run(
        self, **kwargs: Unpack[DeleteReplicationTaskAssessmentRunMessageTypeDef]
    ) -> DeleteReplicationTaskAssessmentRunResponseTypeDef:
        """
        Deletes the record of a single premigration assessment run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/delete_replication_task_assessment_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#delete_replication_task_assessment_run)
        """

    def describe_account_attributes(self) -> DescribeAccountAttributesResponseTypeDef:
        """
        Lists all of the DMS attributes for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_account_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_account_attributes)
        """

    def describe_applicable_individual_assessments(
        self, **kwargs: Unpack[DescribeApplicableIndividualAssessmentsMessageTypeDef]
    ) -> DescribeApplicableIndividualAssessmentsResponseTypeDef:
        """
        Provides a list of individual assessments that you can specify for a new
        premigration assessment run, given one or more parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_applicable_individual_assessments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_applicable_individual_assessments)
        """

    def describe_certificates(
        self, **kwargs: Unpack[DescribeCertificatesMessageTypeDef]
    ) -> DescribeCertificatesResponseTypeDef:
        """
        Provides a description of the certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_certificates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_certificates)
        """

    def describe_connections(
        self, **kwargs: Unpack[DescribeConnectionsMessageTypeDef]
    ) -> DescribeConnectionsResponseTypeDef:
        """
        Describes the status of the connections that have been made between the
        replication instance and an endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_connections)
        """

    def describe_conversion_configuration(
        self, **kwargs: Unpack[DescribeConversionConfigurationMessageTypeDef]
    ) -> DescribeConversionConfigurationResponseTypeDef:
        """
        Returns configuration parameters for a schema conversion project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_conversion_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_conversion_configuration)
        """

    def describe_data_migrations(
        self, **kwargs: Unpack[DescribeDataMigrationsMessageTypeDef]
    ) -> DescribeDataMigrationsResponseTypeDef:
        """
        Returns information about data migrations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_data_migrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_data_migrations)
        """

    def describe_data_providers(
        self, **kwargs: Unpack[DescribeDataProvidersMessageTypeDef]
    ) -> DescribeDataProvidersResponseTypeDef:
        """
        Returns a paginated list of data providers for your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_data_providers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_data_providers)
        """

    def describe_endpoint_settings(
        self, **kwargs: Unpack[DescribeEndpointSettingsMessageTypeDef]
    ) -> DescribeEndpointSettingsResponseTypeDef:
        """
        Returns information about the possible endpoint settings available when you
        create an endpoint for a specific database engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_endpoint_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_endpoint_settings)
        """

    def describe_endpoint_types(
        self, **kwargs: Unpack[DescribeEndpointTypesMessageTypeDef]
    ) -> DescribeEndpointTypesResponseTypeDef:
        """
        Returns information about the type of endpoints available.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_endpoint_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_endpoint_types)
        """

    def describe_endpoints(
        self, **kwargs: Unpack[DescribeEndpointsMessageTypeDef]
    ) -> DescribeEndpointsResponseTypeDef:
        """
        Returns information about the endpoints for your account in the current region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_endpoints)
        """

    def describe_engine_versions(
        self, **kwargs: Unpack[DescribeEngineVersionsMessageTypeDef]
    ) -> DescribeEngineVersionsResponseTypeDef:
        """
        Returns information about the replication instance versions used in the project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_engine_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_engine_versions)
        """

    def describe_event_categories(
        self, **kwargs: Unpack[DescribeEventCategoriesMessageTypeDef]
    ) -> DescribeEventCategoriesResponseTypeDef:
        """
        Lists categories for all event source types, or, if specified, for a specified
        source type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_event_categories.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_event_categories)
        """

    def describe_event_subscriptions(
        self, **kwargs: Unpack[DescribeEventSubscriptionsMessageTypeDef]
    ) -> DescribeEventSubscriptionsResponseTypeDef:
        """
        Lists all the event subscriptions for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_event_subscriptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_event_subscriptions)
        """

    def describe_events(
        self, **kwargs: Unpack[DescribeEventsMessageTypeDef]
    ) -> DescribeEventsResponseTypeDef:
        """
        Lists events for a given source identifier and source type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_events)
        """

    def describe_extension_pack_associations(
        self, **kwargs: Unpack[DescribeExtensionPackAssociationsMessageTypeDef]
    ) -> DescribeExtensionPackAssociationsResponseTypeDef:
        """
        Returns a paginated list of extension pack associations for the specified
        migration project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_extension_pack_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_extension_pack_associations)
        """

    def describe_fleet_advisor_collectors(
        self, **kwargs: Unpack[DescribeFleetAdvisorCollectorsRequestTypeDef]
    ) -> DescribeFleetAdvisorCollectorsResponseTypeDef:
        """
        Returns a list of the Fleet Advisor collectors in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_fleet_advisor_collectors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_fleet_advisor_collectors)
        """

    def describe_fleet_advisor_databases(
        self, **kwargs: Unpack[DescribeFleetAdvisorDatabasesRequestTypeDef]
    ) -> DescribeFleetAdvisorDatabasesResponseTypeDef:
        """
        Returns a list of Fleet Advisor databases in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_fleet_advisor_databases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_fleet_advisor_databases)
        """

    def describe_fleet_advisor_lsa_analysis(
        self, **kwargs: Unpack[DescribeFleetAdvisorLsaAnalysisRequestTypeDef]
    ) -> DescribeFleetAdvisorLsaAnalysisResponseTypeDef:
        """
        Provides descriptions of large-scale assessment (LSA) analyses produced by your
        Fleet Advisor collectors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_fleet_advisor_lsa_analysis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_fleet_advisor_lsa_analysis)
        """

    def describe_fleet_advisor_schema_object_summary(
        self, **kwargs: Unpack[DescribeFleetAdvisorSchemaObjectSummaryRequestTypeDef]
    ) -> DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef:
        """
        Provides descriptions of the schemas discovered by your Fleet Advisor
        collectors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_fleet_advisor_schema_object_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_fleet_advisor_schema_object_summary)
        """

    def describe_fleet_advisor_schemas(
        self, **kwargs: Unpack[DescribeFleetAdvisorSchemasRequestTypeDef]
    ) -> DescribeFleetAdvisorSchemasResponseTypeDef:
        """
        Returns a list of schemas detected by Fleet Advisor Collectors in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_fleet_advisor_schemas.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_fleet_advisor_schemas)
        """

    def describe_instance_profiles(
        self, **kwargs: Unpack[DescribeInstanceProfilesMessageTypeDef]
    ) -> DescribeInstanceProfilesResponseTypeDef:
        """
        Returns a paginated list of instance profiles for your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_instance_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_instance_profiles)
        """

    def describe_metadata_model_assessments(
        self, **kwargs: Unpack[DescribeMetadataModelAssessmentsMessageTypeDef]
    ) -> DescribeMetadataModelAssessmentsResponseTypeDef:
        """
        Returns a paginated list of metadata model assessments for your account in the
        current region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_metadata_model_assessments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_metadata_model_assessments)
        """

    def describe_metadata_model_conversions(
        self, **kwargs: Unpack[DescribeMetadataModelConversionsMessageTypeDef]
    ) -> DescribeMetadataModelConversionsResponseTypeDef:
        """
        Returns a paginated list of metadata model conversions for a migration project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_metadata_model_conversions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_metadata_model_conversions)
        """

    def describe_metadata_model_exports_as_script(
        self, **kwargs: Unpack[DescribeMetadataModelExportsAsScriptMessageTypeDef]
    ) -> DescribeMetadataModelExportsAsScriptResponseTypeDef:
        """
        Returns a paginated list of metadata model exports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_metadata_model_exports_as_script.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_metadata_model_exports_as_script)
        """

    def describe_metadata_model_exports_to_target(
        self, **kwargs: Unpack[DescribeMetadataModelExportsToTargetMessageTypeDef]
    ) -> DescribeMetadataModelExportsToTargetResponseTypeDef:
        """
        Returns a paginated list of metadata model exports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_metadata_model_exports_to_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_metadata_model_exports_to_target)
        """

    def describe_metadata_model_imports(
        self, **kwargs: Unpack[DescribeMetadataModelImportsMessageTypeDef]
    ) -> DescribeMetadataModelImportsResponseTypeDef:
        """
        Returns a paginated list of metadata model imports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_metadata_model_imports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_metadata_model_imports)
        """

    def describe_migration_projects(
        self, **kwargs: Unpack[DescribeMigrationProjectsMessageTypeDef]
    ) -> DescribeMigrationProjectsResponseTypeDef:
        """
        Returns a paginated list of migration projects for your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_migration_projects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_migration_projects)
        """

    def describe_orderable_replication_instances(
        self, **kwargs: Unpack[DescribeOrderableReplicationInstancesMessageTypeDef]
    ) -> DescribeOrderableReplicationInstancesResponseTypeDef:
        """
        Returns information about the replication instance types that can be created in
        the specified region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_orderable_replication_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_orderable_replication_instances)
        """

    def describe_pending_maintenance_actions(
        self, **kwargs: Unpack[DescribePendingMaintenanceActionsMessageTypeDef]
    ) -> DescribePendingMaintenanceActionsResponseTypeDef:
        """
        Returns a list of upcoming maintenance events for replication instances in your
        account in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_pending_maintenance_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_pending_maintenance_actions)
        """

    def describe_recommendation_limitations(
        self, **kwargs: Unpack[DescribeRecommendationLimitationsRequestTypeDef]
    ) -> DescribeRecommendationLimitationsResponseTypeDef:
        """
        Returns a paginated list of limitations for recommendations of target Amazon
        Web Services engines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_recommendation_limitations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_recommendation_limitations)
        """

    def describe_recommendations(
        self, **kwargs: Unpack[DescribeRecommendationsRequestTypeDef]
    ) -> DescribeRecommendationsResponseTypeDef:
        """
        Returns a paginated list of target engine recommendations for your source
        databases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_recommendations)
        """

    def describe_refresh_schemas_status(
        self, **kwargs: Unpack[DescribeRefreshSchemasStatusMessageTypeDef]
    ) -> DescribeRefreshSchemasStatusResponseTypeDef:
        """
        Returns the status of the RefreshSchemas operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_refresh_schemas_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_refresh_schemas_status)
        """

    def describe_replication_configs(
        self, **kwargs: Unpack[DescribeReplicationConfigsMessageTypeDef]
    ) -> DescribeReplicationConfigsResponseTypeDef:
        """
        Returns one or more existing DMS Serverless replication configurations as a
        list of structures.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_replication_configs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_replication_configs)
        """

    def describe_replication_instance_task_logs(
        self, **kwargs: Unpack[DescribeReplicationInstanceTaskLogsMessageTypeDef]
    ) -> DescribeReplicationInstanceTaskLogsResponseTypeDef:
        """
        Returns information about the task logs for the specified task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_replication_instance_task_logs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_replication_instance_task_logs)
        """

    def describe_replication_instances(
        self, **kwargs: Unpack[DescribeReplicationInstancesMessageTypeDef]
    ) -> DescribeReplicationInstancesResponseTypeDef:
        """
        Returns information about replication instances for your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_replication_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_replication_instances)
        """

    def describe_replication_subnet_groups(
        self, **kwargs: Unpack[DescribeReplicationSubnetGroupsMessageTypeDef]
    ) -> DescribeReplicationSubnetGroupsResponseTypeDef:
        """
        Returns information about the replication subnet groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_replication_subnet_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_replication_subnet_groups)
        """

    def describe_replication_table_statistics(
        self, **kwargs: Unpack[DescribeReplicationTableStatisticsMessageTypeDef]
    ) -> DescribeReplicationTableStatisticsResponseTypeDef:
        """
        Returns table and schema statistics for one or more provisioned replications
        that use a given DMS Serverless replication configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_replication_table_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_replication_table_statistics)
        """

    def describe_replication_task_assessment_results(
        self, **kwargs: Unpack[DescribeReplicationTaskAssessmentResultsMessageTypeDef]
    ) -> DescribeReplicationTaskAssessmentResultsResponseTypeDef:
        """
        Returns the task assessment results from the Amazon S3 bucket that DMS creates
        in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_replication_task_assessment_results.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_replication_task_assessment_results)
        """

    def describe_replication_task_assessment_runs(
        self, **kwargs: Unpack[DescribeReplicationTaskAssessmentRunsMessageTypeDef]
    ) -> DescribeReplicationTaskAssessmentRunsResponseTypeDef:
        """
        Returns a paginated list of premigration assessment runs based on filter
        settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_replication_task_assessment_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_replication_task_assessment_runs)
        """

    def describe_replication_task_individual_assessments(
        self, **kwargs: Unpack[DescribeReplicationTaskIndividualAssessmentsMessageTypeDef]
    ) -> DescribeReplicationTaskIndividualAssessmentsResponseTypeDef:
        """
        Returns a paginated list of individual assessments based on filter settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_replication_task_individual_assessments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_replication_task_individual_assessments)
        """

    def describe_replication_tasks(
        self, **kwargs: Unpack[DescribeReplicationTasksMessageTypeDef]
    ) -> DescribeReplicationTasksResponseTypeDef:
        """
        Returns information about replication tasks for your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_replication_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_replication_tasks)
        """

    def describe_replications(
        self, **kwargs: Unpack[DescribeReplicationsMessageTypeDef]
    ) -> DescribeReplicationsResponseTypeDef:
        """
        Provides details on replication progress by returning status information for
        one or more provisioned DMS Serverless replications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_replications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_replications)
        """

    def describe_schemas(
        self, **kwargs: Unpack[DescribeSchemasMessageTypeDef]
    ) -> DescribeSchemasResponseTypeDef:
        """
        Returns information about the schema for the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_schemas.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_schemas)
        """

    def describe_table_statistics(
        self, **kwargs: Unpack[DescribeTableStatisticsMessageTypeDef]
    ) -> DescribeTableStatisticsResponseTypeDef:
        """
        Returns table statistics on the database migration task, including table name,
        rows inserted, rows updated, and rows deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_table_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#describe_table_statistics)
        """

    def export_metadata_model_assessment(
        self, **kwargs: Unpack[ExportMetadataModelAssessmentMessageTypeDef]
    ) -> ExportMetadataModelAssessmentResponseTypeDef:
        """
        Saves a copy of a database migration assessment report to your Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/export_metadata_model_assessment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#export_metadata_model_assessment)
        """

    def import_certificate(
        self, **kwargs: Unpack[ImportCertificateMessageTypeDef]
    ) -> ImportCertificateResponseTypeDef:
        """
        Uploads the specified certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/import_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#import_certificate)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceMessageTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all metadata tags attached to an DMS resource, including replication
        instance, endpoint, subnet group, and migration task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#list_tags_for_resource)
        """

    def modify_conversion_configuration(
        self, **kwargs: Unpack[ModifyConversionConfigurationMessageTypeDef]
    ) -> ModifyConversionConfigurationResponseTypeDef:
        """
        Modifies the specified schema conversion configuration using the provided
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/modify_conversion_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#modify_conversion_configuration)
        """

    def modify_data_migration(
        self, **kwargs: Unpack[ModifyDataMigrationMessageTypeDef]
    ) -> ModifyDataMigrationResponseTypeDef:
        """
        Modifies an existing DMS data migration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/modify_data_migration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#modify_data_migration)
        """

    def modify_data_provider(
        self, **kwargs: Unpack[ModifyDataProviderMessageTypeDef]
    ) -> ModifyDataProviderResponseTypeDef:
        """
        Modifies the specified data provider using the provided settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/modify_data_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#modify_data_provider)
        """

    def modify_endpoint(
        self, **kwargs: Unpack[ModifyEndpointMessageTypeDef]
    ) -> ModifyEndpointResponseTypeDef:
        """
        Modifies the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/modify_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#modify_endpoint)
        """

    def modify_event_subscription(
        self, **kwargs: Unpack[ModifyEventSubscriptionMessageTypeDef]
    ) -> ModifyEventSubscriptionResponseTypeDef:
        """
        Modifies an existing DMS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/modify_event_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#modify_event_subscription)
        """

    def modify_instance_profile(
        self, **kwargs: Unpack[ModifyInstanceProfileMessageTypeDef]
    ) -> ModifyInstanceProfileResponseTypeDef:
        """
        Modifies the specified instance profile using the provided parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/modify_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#modify_instance_profile)
        """

    def modify_migration_project(
        self, **kwargs: Unpack[ModifyMigrationProjectMessageTypeDef]
    ) -> ModifyMigrationProjectResponseTypeDef:
        """
        Modifies the specified migration project using the provided parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/modify_migration_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#modify_migration_project)
        """

    def modify_replication_config(
        self, **kwargs: Unpack[ModifyReplicationConfigMessageTypeDef]
    ) -> ModifyReplicationConfigResponseTypeDef:
        """
        Modifies an existing DMS Serverless replication configuration that you can use
        to start a replication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/modify_replication_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#modify_replication_config)
        """

    def modify_replication_instance(
        self, **kwargs: Unpack[ModifyReplicationInstanceMessageTypeDef]
    ) -> ModifyReplicationInstanceResponseTypeDef:
        """
        Modifies the replication instance to apply new settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/modify_replication_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#modify_replication_instance)
        """

    def modify_replication_subnet_group(
        self, **kwargs: Unpack[ModifyReplicationSubnetGroupMessageTypeDef]
    ) -> ModifyReplicationSubnetGroupResponseTypeDef:
        """
        Modifies the settings for the specified replication subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/modify_replication_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#modify_replication_subnet_group)
        """

    def modify_replication_task(
        self, **kwargs: Unpack[ModifyReplicationTaskMessageTypeDef]
    ) -> ModifyReplicationTaskResponseTypeDef:
        """
        Modifies the specified replication task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/modify_replication_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#modify_replication_task)
        """

    def move_replication_task(
        self, **kwargs: Unpack[MoveReplicationTaskMessageTypeDef]
    ) -> MoveReplicationTaskResponseTypeDef:
        """
        Moves a replication task from its current replication instance to a different
        target replication instance using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/move_replication_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#move_replication_task)
        """

    def reboot_replication_instance(
        self, **kwargs: Unpack[RebootReplicationInstanceMessageTypeDef]
    ) -> RebootReplicationInstanceResponseTypeDef:
        """
        Reboots a replication instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/reboot_replication_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#reboot_replication_instance)
        """

    def refresh_schemas(
        self, **kwargs: Unpack[RefreshSchemasMessageTypeDef]
    ) -> RefreshSchemasResponseTypeDef:
        """
        Populates the schema for the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/refresh_schemas.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#refresh_schemas)
        """

    def reload_replication_tables(
        self, **kwargs: Unpack[ReloadReplicationTablesMessageTypeDef]
    ) -> ReloadReplicationTablesResponseTypeDef:
        """
        Reloads the target database table with the source data for a given DMS
        Serverless replication configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/reload_replication_tables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#reload_replication_tables)
        """

    def reload_tables(
        self, **kwargs: Unpack[ReloadTablesMessageTypeDef]
    ) -> ReloadTablesResponseTypeDef:
        """
        Reloads the target database table with the source data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/reload_tables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#reload_tables)
        """

    def remove_tags_from_resource(
        self, **kwargs: Unpack[RemoveTagsFromResourceMessageTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes metadata tags from an DMS resource, including replication instance,
        endpoint, subnet group, and migration task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/remove_tags_from_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#remove_tags_from_resource)
        """

    def run_fleet_advisor_lsa_analysis(self) -> RunFleetAdvisorLsaAnalysisResponseTypeDef:
        """
        Runs large-scale assessment (LSA) analysis on every Fleet Advisor collector in
        your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/run_fleet_advisor_lsa_analysis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#run_fleet_advisor_lsa_analysis)
        """

    def start_data_migration(
        self, **kwargs: Unpack[StartDataMigrationMessageTypeDef]
    ) -> StartDataMigrationResponseTypeDef:
        """
        Starts the specified data migration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/start_data_migration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#start_data_migration)
        """

    def start_extension_pack_association(
        self, **kwargs: Unpack[StartExtensionPackAssociationMessageTypeDef]
    ) -> StartExtensionPackAssociationResponseTypeDef:
        """
        Applies the extension pack to your target database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/start_extension_pack_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#start_extension_pack_association)
        """

    def start_metadata_model_assessment(
        self, **kwargs: Unpack[StartMetadataModelAssessmentMessageTypeDef]
    ) -> StartMetadataModelAssessmentResponseTypeDef:
        """
        Creates a database migration assessment report by assessing the migration
        complexity for your source database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/start_metadata_model_assessment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#start_metadata_model_assessment)
        """

    def start_metadata_model_conversion(
        self, **kwargs: Unpack[StartMetadataModelConversionMessageTypeDef]
    ) -> StartMetadataModelConversionResponseTypeDef:
        """
        Converts your source database objects to a format compatible with the target
        database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/start_metadata_model_conversion.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#start_metadata_model_conversion)
        """

    def start_metadata_model_export_as_script(
        self, **kwargs: Unpack[StartMetadataModelExportAsScriptMessageTypeDef]
    ) -> StartMetadataModelExportAsScriptResponseTypeDef:
        """
        Saves your converted code to a file as a SQL script, and stores this file on
        your Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/start_metadata_model_export_as_script.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#start_metadata_model_export_as_script)
        """

    def start_metadata_model_export_to_target(
        self, **kwargs: Unpack[StartMetadataModelExportToTargetMessageTypeDef]
    ) -> StartMetadataModelExportToTargetResponseTypeDef:
        """
        Applies converted database objects to your target database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/start_metadata_model_export_to_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#start_metadata_model_export_to_target)
        """

    def start_metadata_model_import(
        self, **kwargs: Unpack[StartMetadataModelImportMessageTypeDef]
    ) -> StartMetadataModelImportResponseTypeDef:
        """
        Loads the metadata for all the dependent database objects of the parent object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/start_metadata_model_import.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#start_metadata_model_import)
        """

    def start_recommendations(
        self, **kwargs: Unpack[StartRecommendationsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Starts the analysis of your source database to provide recommendations of
        target engines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/start_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#start_recommendations)
        """

    def start_replication(
        self, **kwargs: Unpack[StartReplicationMessageTypeDef]
    ) -> StartReplicationResponseTypeDef:
        """
        For a given DMS Serverless replication configuration, DMS connects to the
        source endpoint and collects the metadata to analyze the replication workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/start_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#start_replication)
        """

    def start_replication_task(
        self, **kwargs: Unpack[StartReplicationTaskMessageTypeDef]
    ) -> StartReplicationTaskResponseTypeDef:
        """
        Starts the replication task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/start_replication_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#start_replication_task)
        """

    def start_replication_task_assessment(
        self, **kwargs: Unpack[StartReplicationTaskAssessmentMessageTypeDef]
    ) -> StartReplicationTaskAssessmentResponseTypeDef:
        """
        Starts the replication task assessment for unsupported data types in the source
        database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/start_replication_task_assessment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#start_replication_task_assessment)
        """

    def start_replication_task_assessment_run(
        self, **kwargs: Unpack[StartReplicationTaskAssessmentRunMessageTypeDef]
    ) -> StartReplicationTaskAssessmentRunResponseTypeDef:
        """
        Starts a new premigration assessment run for one or more individual assessments
        of a migration task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/start_replication_task_assessment_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#start_replication_task_assessment_run)
        """

    def stop_data_migration(
        self, **kwargs: Unpack[StopDataMigrationMessageTypeDef]
    ) -> StopDataMigrationResponseTypeDef:
        """
        Stops the specified data migration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/stop_data_migration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#stop_data_migration)
        """

    def stop_replication(
        self, **kwargs: Unpack[StopReplicationMessageTypeDef]
    ) -> StopReplicationResponseTypeDef:
        """
        For a given DMS Serverless replication configuration, DMS stops any and all
        ongoing DMS Serverless replications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/stop_replication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#stop_replication)
        """

    def stop_replication_task(
        self, **kwargs: Unpack[StopReplicationTaskMessageTypeDef]
    ) -> StopReplicationTaskResponseTypeDef:
        """
        Stops the replication task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/stop_replication_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#stop_replication_task)
        """

    def test_connection(
        self, **kwargs: Unpack[TestConnectionMessageTypeDef]
    ) -> TestConnectionResponseTypeDef:
        """
        Tests the connection between the replication instance and the endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/test_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#test_connection)
        """

    def update_subscriptions_to_event_bridge(
        self, **kwargs: Unpack[UpdateSubscriptionsToEventBridgeMessageTypeDef]
    ) -> UpdateSubscriptionsToEventBridgeResponseTypeDef:
        """
        Migrates 10 active and enabled Amazon SNS subscriptions at a time and converts
        them to corresponding Amazon EventBridge rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/update_subscriptions_to_event_bridge.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#update_subscriptions_to_event_bridge)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_certificates"]
    ) -> DescribeCertificatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_connections"]
    ) -> DescribeConnectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_data_migrations"]
    ) -> DescribeDataMigrationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_endpoint_types"]
    ) -> DescribeEndpointTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_endpoints"]
    ) -> DescribeEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> DescribeEventSubscriptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_events"]
    ) -> DescribeEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_orderable_replication_instances"]
    ) -> DescribeOrderableReplicationInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_replication_instances"]
    ) -> DescribeReplicationInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_replication_subnet_groups"]
    ) -> DescribeReplicationSubnetGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_replication_task_assessment_results"]
    ) -> DescribeReplicationTaskAssessmentResultsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_replication_tasks"]
    ) -> DescribeReplicationTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_schemas"]
    ) -> DescribeSchemasPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_table_statistics"]
    ) -> DescribeTableStatisticsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["endpoint_deleted"]
    ) -> EndpointDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["replication_instance_available"]
    ) -> ReplicationInstanceAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["replication_instance_deleted"]
    ) -> ReplicationInstanceDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["replication_task_deleted"]
    ) -> ReplicationTaskDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["replication_task_ready"]
    ) -> ReplicationTaskReadyWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["replication_task_running"]
    ) -> ReplicationTaskRunningWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["replication_task_stopped"]
    ) -> ReplicationTaskStoppedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["test_connection_succeeds"]
    ) -> TestConnectionSucceedsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/client/#get_waiter)
        """
