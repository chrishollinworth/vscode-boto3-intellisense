"""
Type annotations for dms service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_dms import DatabaseMigrationServiceClient

    client: DatabaseMigrationServiceClient = boto3.client("dms")
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    AssessmentReportTypeType,
    DmsSslModeValueType,
    MigrationTypeValueType,
    OriginTypeValueType,
    ReloadOptionValueType,
    ReplicationEndpointTypeValueType,
    StartReplicationTaskTypeValueType,
)
from .paginator import (
    DescribeCertificatesPaginator,
    DescribeConnectionsPaginator,
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
    ApplyPendingMaintenanceActionResponseTypeDef,
    BatchStartRecommendationsResponseTypeDef,
    CancelReplicationTaskAssessmentRunResponseTypeDef,
    ComputeConfigTypeDef,
    CreateDataProviderResponseTypeDef,
    CreateEndpointResponseTypeDef,
    CreateEventSubscriptionResponseTypeDef,
    CreateFleetAdvisorCollectorResponseTypeDef,
    CreateInstanceProfileResponseTypeDef,
    CreateMigrationProjectResponseTypeDef,
    CreateReplicationConfigResponseTypeDef,
    CreateReplicationInstanceResponseTypeDef,
    CreateReplicationSubnetGroupResponseTypeDef,
    CreateReplicationTaskResponseTypeDef,
    DataProviderDescriptorDefinitionTypeDef,
    DataProviderSettingsTypeDef,
    DeleteCertificateResponseTypeDef,
    DeleteConnectionResponseTypeDef,
    DeleteDataProviderResponseTypeDef,
    DeleteEndpointResponseTypeDef,
    DeleteEventSubscriptionResponseTypeDef,
    DeleteFleetAdvisorDatabasesResponseTypeDef,
    DeleteInstanceProfileResponseTypeDef,
    DeleteMigrationProjectResponseTypeDef,
    DeleteReplicationConfigResponseTypeDef,
    DeleteReplicationInstanceResponseTypeDef,
    DeleteReplicationTaskAssessmentRunResponseTypeDef,
    DeleteReplicationTaskResponseTypeDef,
    DescribeAccountAttributesResponseTypeDef,
    DescribeApplicableIndividualAssessmentsResponseTypeDef,
    DescribeCertificatesResponseTypeDef,
    DescribeConnectionsResponseTypeDef,
    DescribeConversionConfigurationResponseTypeDef,
    DescribeDataProvidersResponseTypeDef,
    DescribeEndpointSettingsResponseTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeEndpointTypesResponseTypeDef,
    DescribeEngineVersionsResponseTypeDef,
    DescribeEventCategoriesResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeEventSubscriptionsResponseTypeDef,
    DescribeExtensionPackAssociationsResponseTypeDef,
    DescribeFleetAdvisorCollectorsResponseTypeDef,
    DescribeFleetAdvisorDatabasesResponseTypeDef,
    DescribeFleetAdvisorLsaAnalysisResponseTypeDef,
    DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef,
    DescribeFleetAdvisorSchemasResponseTypeDef,
    DescribeInstanceProfilesResponseTypeDef,
    DescribeMetadataModelAssessmentsResponseTypeDef,
    DescribeMetadataModelConversionsResponseTypeDef,
    DescribeMetadataModelExportsAsScriptResponseTypeDef,
    DescribeMetadataModelExportsToTargetResponseTypeDef,
    DescribeMetadataModelImportsResponseTypeDef,
    DescribeMigrationProjectsResponseTypeDef,
    DescribeOrderableReplicationInstancesResponseTypeDef,
    DescribePendingMaintenanceActionsResponseTypeDef,
    DescribeRecommendationLimitationsResponseTypeDef,
    DescribeRecommendationsResponseTypeDef,
    DescribeRefreshSchemasStatusResponseTypeDef,
    DescribeReplicationConfigsResponseTypeDef,
    DescribeReplicationInstancesResponseTypeDef,
    DescribeReplicationInstanceTaskLogsResponseTypeDef,
    DescribeReplicationsResponseTypeDef,
    DescribeReplicationSubnetGroupsResponseTypeDef,
    DescribeReplicationTableStatisticsResponseTypeDef,
    DescribeReplicationTaskAssessmentResultsResponseTypeDef,
    DescribeReplicationTaskAssessmentRunsResponseTypeDef,
    DescribeReplicationTaskIndividualAssessmentsResponseTypeDef,
    DescribeReplicationTasksResponseTypeDef,
    DescribeSchemasResponseTypeDef,
    DescribeTableStatisticsResponseTypeDef,
    DmsTransferSettingsTypeDef,
    DocDbSettingsTypeDef,
    DynamoDbSettingsTypeDef,
    ElasticsearchSettingsTypeDef,
    ExportMetadataModelAssessmentResponseTypeDef,
    FilterTypeDef,
    GcpMySQLSettingsTypeDef,
    IBMDb2SettingsTypeDef,
    ImportCertificateResponseTypeDef,
    KafkaSettingsTypeDef,
    KinesisSettingsTypeDef,
    ListTagsForResourceResponseTypeDef,
    MicrosoftSQLServerSettingsTypeDef,
    ModifyConversionConfigurationResponseTypeDef,
    ModifyDataProviderResponseTypeDef,
    ModifyEndpointResponseTypeDef,
    ModifyEventSubscriptionResponseTypeDef,
    ModifyInstanceProfileResponseTypeDef,
    ModifyMigrationProjectResponseTypeDef,
    ModifyReplicationConfigResponseTypeDef,
    ModifyReplicationInstanceResponseTypeDef,
    ModifyReplicationSubnetGroupResponseTypeDef,
    ModifyReplicationTaskResponseTypeDef,
    MongoDbSettingsTypeDef,
    MoveReplicationTaskResponseTypeDef,
    MySQLSettingsTypeDef,
    NeptuneSettingsTypeDef,
    OracleSettingsTypeDef,
    PostgreSQLSettingsTypeDef,
    RebootReplicationInstanceResponseTypeDef,
    RecommendationSettingsTypeDef,
    RedisSettingsTypeDef,
    RedshiftSettingsTypeDef,
    RefreshSchemasResponseTypeDef,
    ReloadReplicationTablesResponseTypeDef,
    ReloadTablesResponseTypeDef,
    RunFleetAdvisorLsaAnalysisResponseTypeDef,
    S3SettingsTypeDef,
    SCApplicationAttributesTypeDef,
    StartExtensionPackAssociationResponseTypeDef,
    StartMetadataModelAssessmentResponseTypeDef,
    StartMetadataModelConversionResponseTypeDef,
    StartMetadataModelExportAsScriptResponseTypeDef,
    StartMetadataModelExportToTargetResponseTypeDef,
    StartMetadataModelImportResponseTypeDef,
    StartRecommendationsRequestEntryTypeDef,
    StartReplicationResponseTypeDef,
    StartReplicationTaskAssessmentResponseTypeDef,
    StartReplicationTaskAssessmentRunResponseTypeDef,
    StartReplicationTaskResponseTypeDef,
    StopReplicationResponseTypeDef,
    StopReplicationTaskResponseTypeDef,
    SybaseSettingsTypeDef,
    TableToReloadTypeDef,
    TagTypeDef,
    TestConnectionResponseTypeDef,
    TimestreamSettingsTypeDef,
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DatabaseMigrationServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CollectorNotFoundFault: Type[BotocoreClientError]
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DatabaseMigrationServiceClient exceptions.
        """

    def add_tags_to_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds metadata tags to an DMS resource, including replication instance, endpoint,
        subnet group, and migration task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.add_tags_to_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#add_tags_to_resource)
        """

    def apply_pending_maintenance_action(
        self, *, ReplicationInstanceArn: str, ApplyAction: str, OptInType: str
    ) -> ApplyPendingMaintenanceActionResponseTypeDef:
        """
        Applies a pending maintenance action to a resource (for example, to a
        replication instance).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.apply_pending_maintenance_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#apply_pending_maintenance_action)
        """

    def batch_start_recommendations(
        self, *, Data: List["StartRecommendationsRequestEntryTypeDef"] = None
    ) -> BatchStartRecommendationsResponseTypeDef:
        """
        Starts the analysis of up to 20 source databases to recommend target engines for
        each source database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.batch_start_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#batch_start_recommendations)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#can_paginate)
        """

    def cancel_replication_task_assessment_run(
        self, *, ReplicationTaskAssessmentRunArn: str
    ) -> CancelReplicationTaskAssessmentRunResponseTypeDef:
        """
        Cancels a single premigration assessment run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.cancel_replication_task_assessment_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#cancel_replication_task_assessment_run)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#close)
        """

    def create_data_provider(
        self,
        *,
        Engine: str,
        Settings: "DataProviderSettingsTypeDef",
        DataProviderName: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDataProviderResponseTypeDef:
        """
        Creates a data provider using the provided settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.create_data_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#create_data_provider)
        """

    def create_endpoint(
        self,
        *,
        EndpointIdentifier: str,
        EndpointType: ReplicationEndpointTypeValueType,
        EngineName: str,
        Username: str = None,
        Password: str = None,
        ServerName: str = None,
        Port: int = None,
        DatabaseName: str = None,
        ExtraConnectionAttributes: str = None,
        KmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None,
        CertificateArn: str = None,
        SslMode: DmsSslModeValueType = None,
        ServiceAccessRoleArn: str = None,
        ExternalTableDefinition: str = None,
        DynamoDbSettings: "DynamoDbSettingsTypeDef" = None,
        S3Settings: "S3SettingsTypeDef" = None,
        DmsTransferSettings: "DmsTransferSettingsTypeDef" = None,
        MongoDbSettings: "MongoDbSettingsTypeDef" = None,
        KinesisSettings: "KinesisSettingsTypeDef" = None,
        KafkaSettings: "KafkaSettingsTypeDef" = None,
        ElasticsearchSettings: "ElasticsearchSettingsTypeDef" = None,
        NeptuneSettings: "NeptuneSettingsTypeDef" = None,
        RedshiftSettings: "RedshiftSettingsTypeDef" = None,
        PostgreSQLSettings: "PostgreSQLSettingsTypeDef" = None,
        MySQLSettings: "MySQLSettingsTypeDef" = None,
        OracleSettings: "OracleSettingsTypeDef" = None,
        SybaseSettings: "SybaseSettingsTypeDef" = None,
        MicrosoftSQLServerSettings: "MicrosoftSQLServerSettingsTypeDef" = None,
        IBMDb2Settings: "IBMDb2SettingsTypeDef" = None,
        ResourceIdentifier: str = None,
        DocDbSettings: "DocDbSettingsTypeDef" = None,
        RedisSettings: "RedisSettingsTypeDef" = None,
        GcpMySQLSettings: "GcpMySQLSettingsTypeDef" = None,
        TimestreamSettings: "TimestreamSettingsTypeDef" = None
    ) -> CreateEndpointResponseTypeDef:
        """
        Creates an endpoint using the provided settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.create_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#create_endpoint)
        """

    def create_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        EventCategories: List[str] = None,
        SourceIds: List[str] = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateEventSubscriptionResponseTypeDef:
        """
        Creates an DMS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.create_event_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#create_event_subscription)
        """

    def create_fleet_advisor_collector(
        self,
        *,
        CollectorName: str,
        ServiceAccessRoleArn: str,
        S3BucketName: str,
        Description: str = None
    ) -> CreateFleetAdvisorCollectorResponseTypeDef:
        """
        Creates a Fleet Advisor collector using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.create_fleet_advisor_collector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#create_fleet_advisor_collector)
        """

    def create_instance_profile(
        self,
        *,
        AvailabilityZone: str = None,
        KmsKeyArn: str = None,
        PubliclyAccessible: bool = None,
        Tags: List["TagTypeDef"] = None,
        NetworkType: str = None,
        InstanceProfileName: str = None,
        Description: str = None,
        SubnetGroupIdentifier: str = None,
        VpcSecurityGroups: List[str] = None
    ) -> CreateInstanceProfileResponseTypeDef:
        """
        Creates the instance profile using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.create_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#create_instance_profile)
        """

    def create_migration_project(
        self,
        *,
        SourceDataProviderDescriptors: List["DataProviderDescriptorDefinitionTypeDef"],
        TargetDataProviderDescriptors: List["DataProviderDescriptorDefinitionTypeDef"],
        InstanceProfileIdentifier: str,
        MigrationProjectName: str = None,
        TransformationRules: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        SchemaConversionApplicationAttributes: "SCApplicationAttributesTypeDef" = None
    ) -> CreateMigrationProjectResponseTypeDef:
        """
        Creates the migration project using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.create_migration_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#create_migration_project)
        """

    def create_replication_config(
        self,
        *,
        ReplicationConfigIdentifier: str,
        SourceEndpointArn: str,
        TargetEndpointArn: str,
        ComputeConfig: "ComputeConfigTypeDef",
        ReplicationType: MigrationTypeValueType,
        TableMappings: str,
        ReplicationSettings: str = None,
        SupplementalSettings: str = None,
        ResourceIdentifier: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateReplicationConfigResponseTypeDef:
        """
        Creates a configuration that you can later provide to configure and start an DMS
        Serverless replication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#create_replication_config)
        """

    def create_replication_instance(
        self,
        *,
        ReplicationInstanceIdentifier: str,
        ReplicationInstanceClass: str,
        AllocatedStorage: int = None,
        VpcSecurityGroupIds: List[str] = None,
        AvailabilityZone: str = None,
        ReplicationSubnetGroupIdentifier: str = None,
        PreferredMaintenanceWindow: str = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AutoMinorVersionUpgrade: bool = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
        PubliclyAccessible: bool = None,
        DnsNameServers: str = None,
        ResourceIdentifier: str = None,
        NetworkType: str = None
    ) -> CreateReplicationInstanceResponseTypeDef:
        """
        Creates the replication instance using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#create_replication_instance)
        """

    def create_replication_subnet_group(
        self,
        *,
        ReplicationSubnetGroupIdentifier: str,
        ReplicationSubnetGroupDescription: str,
        SubnetIds: List[str],
        Tags: List["TagTypeDef"] = None
    ) -> CreateReplicationSubnetGroupResponseTypeDef:
        """
        Creates a replication subnet group given a list of the subnet IDs in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#create_replication_subnet_group)
        """

    def create_replication_task(
        self,
        *,
        ReplicationTaskIdentifier: str,
        SourceEndpointArn: str,
        TargetEndpointArn: str,
        ReplicationInstanceArn: str,
        MigrationType: MigrationTypeValueType,
        TableMappings: str,
        ReplicationTaskSettings: str = None,
        CdcStartTime: Union[datetime, str] = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
        Tags: List["TagTypeDef"] = None,
        TaskData: str = None,
        ResourceIdentifier: str = None
    ) -> CreateReplicationTaskResponseTypeDef:
        """
        Creates a replication task using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#create_replication_task)
        """

    def delete_certificate(self, *, CertificateArn: str) -> DeleteCertificateResponseTypeDef:
        """
        Deletes the specified certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.delete_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#delete_certificate)
        """

    def delete_connection(
        self, *, EndpointArn: str, ReplicationInstanceArn: str
    ) -> DeleteConnectionResponseTypeDef:
        """
        Deletes the connection between a replication instance and an endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.delete_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#delete_connection)
        """

    def delete_data_provider(
        self, *, DataProviderIdentifier: str
    ) -> DeleteDataProviderResponseTypeDef:
        """
        Deletes the specified data provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.delete_data_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#delete_data_provider)
        """

    def delete_endpoint(self, *, EndpointArn: str) -> DeleteEndpointResponseTypeDef:
        """
        Deletes the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.delete_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#delete_endpoint)
        """

    def delete_event_subscription(
        self, *, SubscriptionName: str
    ) -> DeleteEventSubscriptionResponseTypeDef:
        """
        Deletes an DMS event subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.delete_event_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#delete_event_subscription)
        """

    def delete_fleet_advisor_collector(self, *, CollectorReferencedId: str) -> None:
        """
        Deletes the specified Fleet Advisor collector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.delete_fleet_advisor_collector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#delete_fleet_advisor_collector)
        """

    def delete_fleet_advisor_databases(
        self, *, DatabaseIds: List[str]
    ) -> DeleteFleetAdvisorDatabasesResponseTypeDef:
        """
        Deletes the specified Fleet Advisor collector databases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.delete_fleet_advisor_databases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#delete_fleet_advisor_databases)
        """

    def delete_instance_profile(
        self, *, InstanceProfileIdentifier: str
    ) -> DeleteInstanceProfileResponseTypeDef:
        """
        Deletes the specified instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.delete_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#delete_instance_profile)
        """

    def delete_migration_project(
        self, *, MigrationProjectIdentifier: str
    ) -> DeleteMigrationProjectResponseTypeDef:
        """
        Deletes the specified migration project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.delete_migration_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#delete_migration_project)
        """

    def delete_replication_config(
        self, *, ReplicationConfigArn: str
    ) -> DeleteReplicationConfigResponseTypeDef:
        """
        Deletes an DMS Serverless replication configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#delete_replication_config)
        """

    def delete_replication_instance(
        self, *, ReplicationInstanceArn: str
    ) -> DeleteReplicationInstanceResponseTypeDef:
        """
        Deletes the specified replication instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#delete_replication_instance)
        """

    def delete_replication_subnet_group(
        self, *, ReplicationSubnetGroupIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes a subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#delete_replication_subnet_group)
        """

    def delete_replication_task(
        self, *, ReplicationTaskArn: str
    ) -> DeleteReplicationTaskResponseTypeDef:
        """
        Deletes the specified replication task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#delete_replication_task)
        """

    def delete_replication_task_assessment_run(
        self, *, ReplicationTaskAssessmentRunArn: str
    ) -> DeleteReplicationTaskAssessmentRunResponseTypeDef:
        """
        Deletes the record of a single premigration assessment run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_task_assessment_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#delete_replication_task_assessment_run)
        """

    def describe_account_attributes(self) -> DescribeAccountAttributesResponseTypeDef:
        """
        Lists all of the DMS attributes for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_account_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_account_attributes)
        """

    def describe_applicable_individual_assessments(
        self,
        *,
        ReplicationTaskArn: str = None,
        ReplicationInstanceArn: str = None,
        SourceEngineName: str = None,
        TargetEngineName: str = None,
        MigrationType: MigrationTypeValueType = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> DescribeApplicableIndividualAssessmentsResponseTypeDef:
        """
        Provides a list of individual assessments that you can specify for a new
        premigration assessment run, given one or more parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_applicable_individual_assessments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_applicable_individual_assessments)
        """

    def describe_certificates(
        self, *, Filters: List["FilterTypeDef"] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeCertificatesResponseTypeDef:
        """
        Provides a description of the certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_certificates)
        """

    def describe_connections(
        self, *, Filters: List["FilterTypeDef"] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeConnectionsResponseTypeDef:
        """
        Describes the status of the connections that have been made between the
        replication instance and an endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_connections)
        """

    def describe_conversion_configuration(
        self, *, MigrationProjectIdentifier: str
    ) -> DescribeConversionConfigurationResponseTypeDef:
        """
        Returns configuration parameters for a schema conversion project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_conversion_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_conversion_configuration)
        """

    def describe_data_providers(
        self, *, Filters: List["FilterTypeDef"] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeDataProvidersResponseTypeDef:
        """
        Returns a paginated list of data providers for your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_data_providers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_data_providers)
        """

    def describe_endpoint_settings(
        self, *, EngineName: str, MaxRecords: int = None, Marker: str = None
    ) -> DescribeEndpointSettingsResponseTypeDef:
        """
        Returns information about the possible endpoint settings available when you
        create an endpoint for a specific database engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_endpoint_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_endpoint_settings)
        """

    def describe_endpoint_types(
        self, *, Filters: List["FilterTypeDef"] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeEndpointTypesResponseTypeDef:
        """
        Returns information about the type of endpoints available.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_endpoint_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_endpoint_types)
        """

    def describe_endpoints(
        self, *, Filters: List["FilterTypeDef"] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeEndpointsResponseTypeDef:
        """
        Returns information about the endpoints for your account in the current region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_endpoints)
        """

    def describe_engine_versions(
        self, *, MaxRecords: int = None, Marker: str = None
    ) -> DescribeEngineVersionsResponseTypeDef:
        """
        Returns information about the replication instance versions used in the project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_engine_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_engine_versions)
        """

    def describe_event_categories(
        self, *, SourceType: str = None, Filters: List["FilterTypeDef"] = None
    ) -> DescribeEventCategoriesResponseTypeDef:
        """
        Lists categories for all event source types, or, if specified, for a specified
        source type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_event_categories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_event_categories)
        """

    def describe_event_subscriptions(
        self,
        *,
        SubscriptionName: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> DescribeEventSubscriptionsResponseTypeDef:
        """
        Lists all the event subscriptions for a customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_event_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_event_subscriptions)
        """

    def describe_events(
        self,
        *,
        SourceIdentifier: str = None,
        SourceType: Literal["replication-instance"] = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None
    ) -> DescribeEventsResponseTypeDef:
        """
        Lists events for a given source identifier and source type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_events)
        """

    def describe_extension_pack_associations(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: List["FilterTypeDef"] = None,
        Marker: str = None,
        MaxRecords: int = None
    ) -> DescribeExtensionPackAssociationsResponseTypeDef:
        """
        Returns a paginated list of extension pack associations for the specified
        migration project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_extension_pack_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_extension_pack_associations)
        """

    def describe_fleet_advisor_collectors(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        NextToken: str = None
    ) -> DescribeFleetAdvisorCollectorsResponseTypeDef:
        """
        Returns a list of the Fleet Advisor collectors in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_fleet_advisor_collectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_fleet_advisor_collectors)
        """

    def describe_fleet_advisor_databases(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        NextToken: str = None
    ) -> DescribeFleetAdvisorDatabasesResponseTypeDef:
        """
        Returns a list of Fleet Advisor databases in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_fleet_advisor_databases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_fleet_advisor_databases)
        """

    def describe_fleet_advisor_lsa_analysis(
        self, *, MaxRecords: int = None, NextToken: str = None
    ) -> DescribeFleetAdvisorLsaAnalysisResponseTypeDef:
        """
        Provides descriptions of large-scale assessment (LSA) analyses produced by your
        Fleet Advisor collectors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_fleet_advisor_lsa_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_fleet_advisor_lsa_analysis)
        """

    def describe_fleet_advisor_schema_object_summary(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        NextToken: str = None
    ) -> DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef:
        """
        Provides descriptions of the schemas discovered by your Fleet Advisor
        collectors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_fleet_advisor_schema_object_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_fleet_advisor_schema_object_summary)
        """

    def describe_fleet_advisor_schemas(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        NextToken: str = None
    ) -> DescribeFleetAdvisorSchemasResponseTypeDef:
        """
        Returns a list of schemas detected by Fleet Advisor Collectors in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_fleet_advisor_schemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_fleet_advisor_schemas)
        """

    def describe_instance_profiles(
        self, *, Filters: List["FilterTypeDef"] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeInstanceProfilesResponseTypeDef:
        """
        Returns a paginated list of instance profiles for your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_instance_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_instance_profiles)
        """

    def describe_metadata_model_assessments(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: List["FilterTypeDef"] = None,
        Marker: str = None,
        MaxRecords: int = None
    ) -> DescribeMetadataModelAssessmentsResponseTypeDef:
        """
        Returns a paginated list of metadata model assessments for your account in the
        current region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_metadata_model_assessments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_metadata_model_assessments)
        """

    def describe_metadata_model_conversions(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: List["FilterTypeDef"] = None,
        Marker: str = None,
        MaxRecords: int = None
    ) -> DescribeMetadataModelConversionsResponseTypeDef:
        """
        Returns a paginated list of metadata model conversions for a migration project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_metadata_model_conversions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_metadata_model_conversions)
        """

    def describe_metadata_model_exports_as_script(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: List["FilterTypeDef"] = None,
        Marker: str = None,
        MaxRecords: int = None
    ) -> DescribeMetadataModelExportsAsScriptResponseTypeDef:
        """
        Returns a paginated list of metadata model exports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_metadata_model_exports_as_script)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_metadata_model_exports_as_script)
        """

    def describe_metadata_model_exports_to_target(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: List["FilterTypeDef"] = None,
        Marker: str = None,
        MaxRecords: int = None
    ) -> DescribeMetadataModelExportsToTargetResponseTypeDef:
        """
        Returns a paginated list of metadata model exports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_metadata_model_exports_to_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_metadata_model_exports_to_target)
        """

    def describe_metadata_model_imports(
        self,
        *,
        MigrationProjectIdentifier: str,
        Filters: List["FilterTypeDef"] = None,
        Marker: str = None,
        MaxRecords: int = None
    ) -> DescribeMetadataModelImportsResponseTypeDef:
        """
        Returns a paginated list of metadata model imports.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_metadata_model_imports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_metadata_model_imports)
        """

    def describe_migration_projects(
        self, *, Filters: List["FilterTypeDef"] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeMigrationProjectsResponseTypeDef:
        """
        Returns a paginated list of migration projects for your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_migration_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_migration_projects)
        """

    def describe_orderable_replication_instances(
        self, *, MaxRecords: int = None, Marker: str = None
    ) -> DescribeOrderableReplicationInstancesResponseTypeDef:
        """
        Returns information about the replication instance types that can be created in
        the specified region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_orderable_replication_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_orderable_replication_instances)
        """

    def describe_pending_maintenance_actions(
        self,
        *,
        ReplicationInstanceArn: str = None,
        Filters: List["FilterTypeDef"] = None,
        Marker: str = None,
        MaxRecords: int = None
    ) -> DescribePendingMaintenanceActionsResponseTypeDef:
        """
        For internal use only See also: `AWS API Documentation <https://docs.aws.amazon.
        com/goto/WebAPI/dms-2016-01-01/DescribePendingMaintenanceActions>`_ **Request
        Syntax** response = client.describe_pending_maintenance_actions(
        ReplicationInstanceArn='string', Filters=[ ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_pending_maintenance_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_pending_maintenance_actions)
        """

    def describe_recommendation_limitations(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        NextToken: str = None
    ) -> DescribeRecommendationLimitationsResponseTypeDef:
        """
        Returns a paginated list of limitations for recommendations of target Amazon Web
        Services engines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_recommendation_limitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_recommendation_limitations)
        """

    def describe_recommendations(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        NextToken: str = None
    ) -> DescribeRecommendationsResponseTypeDef:
        """
        Returns a paginated list of target engine recommendations for your source
        databases.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_recommendations)
        """

    def describe_refresh_schemas_status(
        self, *, EndpointArn: str
    ) -> DescribeRefreshSchemasStatusResponseTypeDef:
        """
        Returns the status of the RefreshSchemas operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_refresh_schemas_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_refresh_schemas_status)
        """

    def describe_replication_configs(
        self, *, Filters: List["FilterTypeDef"] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationConfigsResponseTypeDef:
        """
        Returns one or more existing DMS Serverless replication configurations as a list
        of structures.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_replication_configs)
        """

    def describe_replication_instance_task_logs(
        self, *, ReplicationInstanceArn: str, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationInstanceTaskLogsResponseTypeDef:
        """
        Returns information about the task logs for the specified task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_instance_task_logs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_replication_instance_task_logs)
        """

    def describe_replication_instances(
        self, *, Filters: List["FilterTypeDef"] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationInstancesResponseTypeDef:
        """
        Returns information about replication instances for your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_replication_instances)
        """

    def describe_replication_subnet_groups(
        self, *, Filters: List["FilterTypeDef"] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationSubnetGroupsResponseTypeDef:
        """
        Returns information about the replication subnet groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_subnet_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_replication_subnet_groups)
        """

    def describe_replication_table_statistics(
        self,
        *,
        ReplicationConfigArn: str,
        MaxRecords: int = None,
        Marker: str = None,
        Filters: List["FilterTypeDef"] = None
    ) -> DescribeReplicationTableStatisticsResponseTypeDef:
        """
        Returns table and schema statistics for one or more provisioned replications
        that use a given DMS Serverless replication configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_table_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_replication_table_statistics)
        """

    def describe_replication_task_assessment_results(
        self, *, ReplicationTaskArn: str = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationTaskAssessmentResultsResponseTypeDef:
        """
        Returns the task assessment results from the Amazon S3 bucket that DMS creates
        in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_task_assessment_results)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_replication_task_assessment_results)
        """

    def describe_replication_task_assessment_runs(
        self, *, Filters: List["FilterTypeDef"] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationTaskAssessmentRunsResponseTypeDef:
        """
        Returns a paginated list of premigration assessment runs based on filter
        settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_task_assessment_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_replication_task_assessment_runs)
        """

    def describe_replication_task_individual_assessments(
        self, *, Filters: List["FilterTypeDef"] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationTaskIndividualAssessmentsResponseTypeDef:
        """
        Returns a paginated list of individual assessments based on filter settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_task_individual_assessments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_replication_task_individual_assessments)
        """

    def describe_replication_tasks(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None
    ) -> DescribeReplicationTasksResponseTypeDef:
        """
        Returns information about replication tasks for your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_replication_tasks)
        """

    def describe_replications(
        self, *, Filters: List["FilterTypeDef"] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationsResponseTypeDef:
        """
        Provides details on replication progress by returning status information for one
        or more provisioned DMS Serverless replications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_replications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_replications)
        """

    def describe_schemas(
        self, *, EndpointArn: str, MaxRecords: int = None, Marker: str = None
    ) -> DescribeSchemasResponseTypeDef:
        """
        Returns information about the schema for the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_schemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_schemas)
        """

    def describe_table_statistics(
        self,
        *,
        ReplicationTaskArn: str,
        MaxRecords: int = None,
        Marker: str = None,
        Filters: List["FilterTypeDef"] = None
    ) -> DescribeTableStatisticsResponseTypeDef:
        """
        Returns table statistics on the database migration task, including table name,
        rows inserted, rows updated, and rows deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.describe_table_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#describe_table_statistics)
        """

    def export_metadata_model_assessment(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
        FileName: str = None,
        AssessmentReportTypes: List[AssessmentReportTypeType] = None
    ) -> ExportMetadataModelAssessmentResponseTypeDef:
        """
        Saves a copy of a database migration assessment report to your Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.export_metadata_model_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#export_metadata_model_assessment)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#generate_presigned_url)
        """

    def import_certificate(
        self,
        *,
        CertificateIdentifier: str,
        CertificatePem: str = None,
        CertificateWallet: Union[bytes, IO[bytes], StreamingBody] = None,
        Tags: List["TagTypeDef"] = None
    ) -> ImportCertificateResponseTypeDef:
        """
        Uploads the specified certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.import_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#import_certificate)
        """

    def list_tags_for_resource(
        self, *, ResourceArn: str = None, ResourceArnList: List[str] = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all metadata tags attached to an DMS resource, including replication
        instance, endpoint, subnet group, and migration task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#list_tags_for_resource)
        """

    def modify_conversion_configuration(
        self, *, MigrationProjectIdentifier: str, ConversionConfiguration: str
    ) -> ModifyConversionConfigurationResponseTypeDef:
        """
        Modifies the specified schema conversion configuration using the provided
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.modify_conversion_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#modify_conversion_configuration)
        """

    def modify_data_provider(
        self,
        *,
        DataProviderIdentifier: str,
        DataProviderName: str = None,
        Description: str = None,
        Engine: str = None,
        ExactSettings: bool = None,
        Settings: "DataProviderSettingsTypeDef" = None
    ) -> ModifyDataProviderResponseTypeDef:
        """
        Modifies the specified data provider using the provided settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.modify_data_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#modify_data_provider)
        """

    def modify_endpoint(
        self,
        *,
        EndpointArn: str,
        EndpointIdentifier: str = None,
        EndpointType: ReplicationEndpointTypeValueType = None,
        EngineName: str = None,
        Username: str = None,
        Password: str = None,
        ServerName: str = None,
        Port: int = None,
        DatabaseName: str = None,
        ExtraConnectionAttributes: str = None,
        CertificateArn: str = None,
        SslMode: DmsSslModeValueType = None,
        ServiceAccessRoleArn: str = None,
        ExternalTableDefinition: str = None,
        DynamoDbSettings: "DynamoDbSettingsTypeDef" = None,
        S3Settings: "S3SettingsTypeDef" = None,
        DmsTransferSettings: "DmsTransferSettingsTypeDef" = None,
        MongoDbSettings: "MongoDbSettingsTypeDef" = None,
        KinesisSettings: "KinesisSettingsTypeDef" = None,
        KafkaSettings: "KafkaSettingsTypeDef" = None,
        ElasticsearchSettings: "ElasticsearchSettingsTypeDef" = None,
        NeptuneSettings: "NeptuneSettingsTypeDef" = None,
        RedshiftSettings: "RedshiftSettingsTypeDef" = None,
        PostgreSQLSettings: "PostgreSQLSettingsTypeDef" = None,
        MySQLSettings: "MySQLSettingsTypeDef" = None,
        OracleSettings: "OracleSettingsTypeDef" = None,
        SybaseSettings: "SybaseSettingsTypeDef" = None,
        MicrosoftSQLServerSettings: "MicrosoftSQLServerSettingsTypeDef" = None,
        IBMDb2Settings: "IBMDb2SettingsTypeDef" = None,
        DocDbSettings: "DocDbSettingsTypeDef" = None,
        RedisSettings: "RedisSettingsTypeDef" = None,
        ExactSettings: bool = None,
        GcpMySQLSettings: "GcpMySQLSettingsTypeDef" = None,
        TimestreamSettings: "TimestreamSettingsTypeDef" = None
    ) -> ModifyEndpointResponseTypeDef:
        """
        Modifies the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.modify_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#modify_endpoint)
        """

    def modify_event_subscription(
        self,
        *,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        EventCategories: List[str] = None,
        Enabled: bool = None
    ) -> ModifyEventSubscriptionResponseTypeDef:
        """
        Modifies an existing DMS event notification subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.modify_event_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#modify_event_subscription)
        """

    def modify_instance_profile(
        self,
        *,
        InstanceProfileIdentifier: str,
        AvailabilityZone: str = None,
        KmsKeyArn: str = None,
        PubliclyAccessible: bool = None,
        NetworkType: str = None,
        InstanceProfileName: str = None,
        Description: str = None,
        SubnetGroupIdentifier: str = None,
        VpcSecurityGroups: List[str] = None
    ) -> ModifyInstanceProfileResponseTypeDef:
        """
        Modifies the specified instance profile using the provided parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.modify_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#modify_instance_profile)
        """

    def modify_migration_project(
        self,
        *,
        MigrationProjectIdentifier: str,
        MigrationProjectName: str = None,
        SourceDataProviderDescriptors: List["DataProviderDescriptorDefinitionTypeDef"] = None,
        TargetDataProviderDescriptors: List["DataProviderDescriptorDefinitionTypeDef"] = None,
        InstanceProfileIdentifier: str = None,
        TransformationRules: str = None,
        Description: str = None,
        SchemaConversionApplicationAttributes: "SCApplicationAttributesTypeDef" = None
    ) -> ModifyMigrationProjectResponseTypeDef:
        """
        Modifies the specified migration project using the provided parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.modify_migration_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#modify_migration_project)
        """

    def modify_replication_config(
        self,
        *,
        ReplicationConfigArn: str,
        ReplicationConfigIdentifier: str = None,
        ReplicationType: MigrationTypeValueType = None,
        TableMappings: str = None,
        ReplicationSettings: str = None,
        SupplementalSettings: str = None,
        ComputeConfig: "ComputeConfigTypeDef" = None,
        SourceEndpointArn: str = None,
        TargetEndpointArn: str = None
    ) -> ModifyReplicationConfigResponseTypeDef:
        """
        Modifies an existing DMS Serverless replication configuration that you can use
        to start a replication.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#modify_replication_config)
        """

    def modify_replication_instance(
        self,
        *,
        ReplicationInstanceArn: str,
        AllocatedStorage: int = None,
        ApplyImmediately: bool = None,
        ReplicationInstanceClass: str = None,
        VpcSecurityGroupIds: List[str] = None,
        PreferredMaintenanceWindow: str = None,
        MultiAZ: bool = None,
        EngineVersion: str = None,
        AllowMajorVersionUpgrade: bool = None,
        AutoMinorVersionUpgrade: bool = None,
        ReplicationInstanceIdentifier: str = None,
        NetworkType: str = None
    ) -> ModifyReplicationInstanceResponseTypeDef:
        """
        Modifies the replication instance to apply new settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#modify_replication_instance)
        """

    def modify_replication_subnet_group(
        self,
        *,
        ReplicationSubnetGroupIdentifier: str,
        SubnetIds: List[str],
        ReplicationSubnetGroupDescription: str = None
    ) -> ModifyReplicationSubnetGroupResponseTypeDef:
        """
        Modifies the settings for the specified replication subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_subnet_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#modify_replication_subnet_group)
        """

    def modify_replication_task(
        self,
        *,
        ReplicationTaskArn: str,
        ReplicationTaskIdentifier: str = None,
        MigrationType: MigrationTypeValueType = None,
        TableMappings: str = None,
        ReplicationTaskSettings: str = None,
        CdcStartTime: Union[datetime, str] = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
        TaskData: str = None
    ) -> ModifyReplicationTaskResponseTypeDef:
        """
        Modifies the specified replication task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#modify_replication_task)
        """

    def move_replication_task(
        self, *, ReplicationTaskArn: str, TargetReplicationInstanceArn: str
    ) -> MoveReplicationTaskResponseTypeDef:
        """
        Moves a replication task from its current replication instance to a different
        target replication instance using the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.move_replication_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#move_replication_task)
        """

    def reboot_replication_instance(
        self,
        *,
        ReplicationInstanceArn: str,
        ForceFailover: bool = None,
        ForcePlannedFailover: bool = None
    ) -> RebootReplicationInstanceResponseTypeDef:
        """
        Reboots a replication instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.reboot_replication_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#reboot_replication_instance)
        """

    def refresh_schemas(
        self, *, EndpointArn: str, ReplicationInstanceArn: str
    ) -> RefreshSchemasResponseTypeDef:
        """
        Populates the schema for the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.refresh_schemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#refresh_schemas)
        """

    def reload_replication_tables(
        self,
        *,
        ReplicationConfigArn: str,
        TablesToReload: List["TableToReloadTypeDef"],
        ReloadOption: ReloadOptionValueType = None
    ) -> ReloadReplicationTablesResponseTypeDef:
        """
        Reloads the target database table with the source data for a given DMS
        Serverless replication configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.reload_replication_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#reload_replication_tables)
        """

    def reload_tables(
        self,
        *,
        ReplicationTaskArn: str,
        TablesToReload: List["TableToReloadTypeDef"],
        ReloadOption: ReloadOptionValueType = None
    ) -> ReloadTablesResponseTypeDef:
        """
        Reloads the target database table with the source data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.reload_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#reload_tables)
        """

    def remove_tags_from_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes metadata tags from an DMS resource, including replication instance,
        endpoint, subnet group, and migration task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.remove_tags_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#remove_tags_from_resource)
        """

    def run_fleet_advisor_lsa_analysis(self) -> RunFleetAdvisorLsaAnalysisResponseTypeDef:
        """
        Runs large-scale assessment (LSA) analysis on every Fleet Advisor collector in
        your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.run_fleet_advisor_lsa_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#run_fleet_advisor_lsa_analysis)
        """

    def start_extension_pack_association(
        self, *, MigrationProjectIdentifier: str
    ) -> StartExtensionPackAssociationResponseTypeDef:
        """
        Applies the extension pack to your target database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.start_extension_pack_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#start_extension_pack_association)
        """

    def start_metadata_model_assessment(
        self, *, MigrationProjectIdentifier: str, SelectionRules: str
    ) -> StartMetadataModelAssessmentResponseTypeDef:
        """
        Creates a database migration assessment report by assessing the migration
        complexity for your source database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.start_metadata_model_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#start_metadata_model_assessment)
        """

    def start_metadata_model_conversion(
        self, *, MigrationProjectIdentifier: str, SelectionRules: str
    ) -> StartMetadataModelConversionResponseTypeDef:
        """
        Converts your source database objects to a format compatible with the target
        database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.start_metadata_model_conversion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#start_metadata_model_conversion)
        """

    def start_metadata_model_export_as_script(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
        Origin: OriginTypeValueType,
        FileName: str = None
    ) -> StartMetadataModelExportAsScriptResponseTypeDef:
        """
        Saves your converted code to a file as a SQL script, and stores this file on
        your Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.start_metadata_model_export_as_script)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#start_metadata_model_export_as_script)
        """

    def start_metadata_model_export_to_target(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
        OverwriteExtensionPack: bool = None
    ) -> StartMetadataModelExportToTargetResponseTypeDef:
        """
        Applies converted database objects to your target database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.start_metadata_model_export_to_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#start_metadata_model_export_to_target)
        """

    def start_metadata_model_import(
        self,
        *,
        MigrationProjectIdentifier: str,
        SelectionRules: str,
        Origin: OriginTypeValueType,
        Refresh: bool = None
    ) -> StartMetadataModelImportResponseTypeDef:
        """
        Loads the metadata for all the dependent database objects of the parent object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.start_metadata_model_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#start_metadata_model_import)
        """

    def start_recommendations(
        self, *, DatabaseId: str, Settings: "RecommendationSettingsTypeDef"
    ) -> None:
        """
        Starts the analysis of your source database to provide recommendations of target
        engines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.start_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#start_recommendations)
        """

    def start_replication(
        self,
        *,
        ReplicationConfigArn: str,
        StartReplicationType: str,
        CdcStartTime: Union[datetime, str] = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None
    ) -> StartReplicationResponseTypeDef:
        """
        For a given DMS Serverless replication configuration, DMS connects to the source
        endpoint and collects the metadata to analyze the replication workload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.start_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#start_replication)
        """

    def start_replication_task(
        self,
        *,
        ReplicationTaskArn: str,
        StartReplicationTaskType: StartReplicationTaskTypeValueType,
        CdcStartTime: Union[datetime, str] = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None
    ) -> StartReplicationTaskResponseTypeDef:
        """
        Starts the replication task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#start_replication_task)
        """

    def start_replication_task_assessment(
        self, *, ReplicationTaskArn: str
    ) -> StartReplicationTaskAssessmentResponseTypeDef:
        """
        Starts the replication task assessment for unsupported data types in the source
        database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#start_replication_task_assessment)
        """

    def start_replication_task_assessment_run(
        self,
        *,
        ReplicationTaskArn: str,
        ServiceAccessRoleArn: str,
        ResultLocationBucket: str,
        AssessmentRunName: str,
        ResultLocationFolder: str = None,
        ResultEncryptionMode: str = None,
        ResultKmsKeyArn: str = None,
        IncludeOnly: List[str] = None,
        Exclude: List[str] = None
    ) -> StartReplicationTaskAssessmentRunResponseTypeDef:
        """
        Starts a new premigration assessment run for one or more individual assessments
        of a migration task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task_assessment_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#start_replication_task_assessment_run)
        """

    def stop_replication(self, *, ReplicationConfigArn: str) -> StopReplicationResponseTypeDef:
        """
        For a given DMS Serverless replication configuration, DMS stops any and all
        ongoing DMS Serverless replications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.stop_replication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#stop_replication)
        """

    def stop_replication_task(
        self, *, ReplicationTaskArn: str
    ) -> StopReplicationTaskResponseTypeDef:
        """
        Stops the replication task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.stop_replication_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#stop_replication_task)
        """

    def test_connection(
        self, *, ReplicationInstanceArn: str, EndpointArn: str
    ) -> TestConnectionResponseTypeDef:
        """
        Tests the connection between the replication instance and the endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.test_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#test_connection)
        """

    def update_subscriptions_to_event_bridge(
        self, *, ForceMove: bool = None
    ) -> UpdateSubscriptionsToEventBridgeResponseTypeDef:
        """
        Migrates 10 active and enabled Amazon SNS subscriptions at a time and converts
        them to corresponding Amazon EventBridge rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Client.update_subscriptions_to_event_bridge)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/client.html#update_subscriptions_to_event_bridge)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_certificates"]
    ) -> DescribeCertificatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeCertificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators.html#describecertificatespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_connections"]
    ) -> DescribeConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeConnections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators.html#describeconnectionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_endpoint_types"]
    ) -> DescribeEndpointTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpointTypes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators.html#describeendpointtypespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_endpoints"]
    ) -> DescribeEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators.html#describeendpointspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> DescribeEventSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEventSubscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators.html#describeeventsubscriptionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators.html#describeeventspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_orderable_replication_instances"]
    ) -> DescribeOrderableReplicationInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeOrderableReplicationInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators.html#describeorderablereplicationinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_instances"]
    ) -> DescribeReplicationInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators.html#describereplicationinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_subnet_groups"]
    ) -> DescribeReplicationSubnetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationSubnetGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators.html#describereplicationsubnetgroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_task_assessment_results"]
    ) -> DescribeReplicationTaskAssessmentResultsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTaskAssessmentResults)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators.html#describereplicationtaskassessmentresultspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_tasks"]
    ) -> DescribeReplicationTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators.html#describereplicationtaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_schemas"]
    ) -> DescribeSchemasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeSchemas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators.html#describeschemaspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_table_statistics"]
    ) -> DescribeTableStatisticsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeTableStatistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/paginators.html#describetablestatisticspaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["endpoint_deleted"]) -> EndpointDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Waiter.EndpointDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#endpointdeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_instance_available"]
    ) -> ReplicationInstanceAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationinstanceavailablewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_instance_deleted"]
    ) -> ReplicationInstanceDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationinstancedeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_deleted"]
    ) -> ReplicationTaskDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationtaskdeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_ready"]
    ) -> ReplicationTaskReadyWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskReady)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationtaskreadywaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_running"]
    ) -> ReplicationTaskRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskRunning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationtaskrunningwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_stopped"]
    ) -> ReplicationTaskStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskStopped)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#replicationtaskstoppedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["test_connection_succeeds"]
    ) -> TestConnectionSucceedsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/dms.html#DatabaseMigrationService.Waiter.TestConnectionSucceeds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/waiters.html#testconnectionsucceedswaiter)
        """
