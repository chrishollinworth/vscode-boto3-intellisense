# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for dms service client

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

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_dms.paginator import (
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
from mypy_boto3_dms.type_defs import (
    ApplyPendingMaintenanceActionResponseTypeDef,
    CancelReplicationTaskAssessmentRunResponseTypeDef,
    CreateEndpointResponseTypeDef,
    CreateEventSubscriptionResponseTypeDef,
    CreateReplicationInstanceResponseTypeDef,
    CreateReplicationSubnetGroupResponseTypeDef,
    CreateReplicationTaskResponseTypeDef,
    DeleteCertificateResponseTypeDef,
    DeleteConnectionResponseTypeDef,
    DeleteEndpointResponseTypeDef,
    DeleteEventSubscriptionResponseTypeDef,
    DeleteReplicationInstanceResponseTypeDef,
    DeleteReplicationTaskAssessmentRunResponseTypeDef,
    DeleteReplicationTaskResponseTypeDef,
    DescribeAccountAttributesResponseTypeDef,
    DescribeApplicableIndividualAssessmentsResponseTypeDef,
    DescribeCertificatesResponseTypeDef,
    DescribeConnectionsResponseTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeEndpointTypesResponseTypeDef,
    DescribeEventCategoriesResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeEventSubscriptionsResponseTypeDef,
    DescribeOrderableReplicationInstancesResponseTypeDef,
    DescribePendingMaintenanceActionsResponseTypeDef,
    DescribeRefreshSchemasStatusResponseTypeDef,
    DescribeReplicationInstancesResponseTypeDef,
    DescribeReplicationInstanceTaskLogsResponseTypeDef,
    DescribeReplicationSubnetGroupsResponseTypeDef,
    DescribeReplicationTaskAssessmentResultsResponseTypeDef,
    DescribeReplicationTaskAssessmentRunsResponseTypeDef,
    DescribeReplicationTaskIndividualAssessmentsResponseTypeDef,
    DescribeReplicationTasksResponseTypeDef,
    DescribeSchemasResponseTypeDef,
    DescribeTableStatisticsResponseTypeDef,
    DmsTransferSettingsTypeDef,
    DynamoDbSettingsTypeDef,
    ElasticsearchSettingsTypeDef,
    FilterTypeDef,
    IBMDb2SettingsTypeDef,
    ImportCertificateResponseTypeDef,
    KafkaSettingsTypeDef,
    KinesisSettingsTypeDef,
    ListTagsForResourceResponseTypeDef,
    MicrosoftSQLServerSettingsTypeDef,
    ModifyEndpointResponseTypeDef,
    ModifyEventSubscriptionResponseTypeDef,
    ModifyReplicationInstanceResponseTypeDef,
    ModifyReplicationSubnetGroupResponseTypeDef,
    ModifyReplicationTaskResponseTypeDef,
    MongoDbSettingsTypeDef,
    MySQLSettingsTypeDef,
    NeptuneSettingsTypeDef,
    OracleSettingsTypeDef,
    PostgreSQLSettingsTypeDef,
    RebootReplicationInstanceResponseTypeDef,
    RedshiftSettingsTypeDef,
    RefreshSchemasResponseTypeDef,
    ReloadTablesResponseTypeDef,
    S3SettingsTypeDef,
    StartReplicationTaskAssessmentResponseTypeDef,
    StartReplicationTaskAssessmentRunResponseTypeDef,
    StartReplicationTaskResponseTypeDef,
    StopReplicationTaskResponseTypeDef,
    SybaseSettingsTypeDef,
    TableToReloadTypeDef,
    TagTypeDef,
    TestConnectionResponseTypeDef,
)
from mypy_boto3_dms.waiter import (
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


class Exceptions:
    AccessDeniedFault: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    InsufficientResourceCapacityFault: Type[Boto3ClientError]
    InvalidCertificateFault: Type[Boto3ClientError]
    InvalidResourceStateFault: Type[Boto3ClientError]
    InvalidSubnet: Type[Boto3ClientError]
    KMSAccessDeniedFault: Type[Boto3ClientError]
    KMSDisabledFault: Type[Boto3ClientError]
    KMSFault: Type[Boto3ClientError]
    KMSInvalidStateFault: Type[Boto3ClientError]
    KMSKeyNotAccessibleFault: Type[Boto3ClientError]
    KMSNotFoundFault: Type[Boto3ClientError]
    KMSThrottlingFault: Type[Boto3ClientError]
    ReplicationSubnetGroupDoesNotCoverEnoughAZs: Type[Boto3ClientError]
    ResourceAlreadyExistsFault: Type[Boto3ClientError]
    ResourceNotFoundFault: Type[Boto3ClientError]
    ResourceQuotaExceededFault: Type[Boto3ClientError]
    S3AccessDeniedFault: Type[Boto3ClientError]
    S3ResourceNotFoundFault: Type[Boto3ClientError]
    SNSInvalidTopicFault: Type[Boto3ClientError]
    SNSNoAuthorizationFault: Type[Boto3ClientError]
    StorageQuotaExceededFault: Type[Boto3ClientError]
    SubnetAlreadyInUse: Type[Boto3ClientError]
    UpgradeDependencyFailureFault: Type[Boto3ClientError]


class DatabaseMigrationServiceClient:
    """
    [DatabaseMigrationService.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client)
    """

    exceptions: Exceptions

    def add_tags_to_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.add_tags_to_resource)
        """

    def apply_pending_maintenance_action(
        self, ReplicationInstanceArn: str, ApplyAction: str, OptInType: str
    ) -> ApplyPendingMaintenanceActionResponseTypeDef:
        """
        [Client.apply_pending_maintenance_action documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.apply_pending_maintenance_action)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.can_paginate)
        """

    def cancel_replication_task_assessment_run(
        self, ReplicationTaskAssessmentRunArn: str
    ) -> CancelReplicationTaskAssessmentRunResponseTypeDef:
        """
        [Client.cancel_replication_task_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.cancel_replication_task_assessment_run)
        """

    def create_endpoint(
        self,
        EndpointIdentifier: str,
        EndpointType: Literal["source", "target"],
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
        SslMode: Literal["none", "require", "verify-ca", "verify-full"] = None,
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
    ) -> CreateEndpointResponseTypeDef:
        """
        [Client.create_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.create_endpoint)
        """

    def create_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str,
        SourceType: str = None,
        EventCategories: List[str] = None,
        SourceIds: List[str] = None,
        Enabled: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateEventSubscriptionResponseTypeDef:
        """
        [Client.create_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.create_event_subscription)
        """

    def create_replication_instance(
        self,
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
    ) -> CreateReplicationInstanceResponseTypeDef:
        """
        [Client.create_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_instance)
        """

    def create_replication_subnet_group(
        self,
        ReplicationSubnetGroupIdentifier: str,
        ReplicationSubnetGroupDescription: str,
        SubnetIds: List[str],
        Tags: List["TagTypeDef"] = None,
    ) -> CreateReplicationSubnetGroupResponseTypeDef:
        """
        [Client.create_replication_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_subnet_group)
        """

    def create_replication_task(
        self,
        ReplicationTaskIdentifier: str,
        SourceEndpointArn: str,
        TargetEndpointArn: str,
        ReplicationInstanceArn: str,
        MigrationType: Literal["full-load", "cdc", "full-load-and-cdc"],
        TableMappings: str,
        ReplicationTaskSettings: str = None,
        CdcStartTime: datetime = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
        Tags: List["TagTypeDef"] = None,
        TaskData: str = None,
    ) -> CreateReplicationTaskResponseTypeDef:
        """
        [Client.create_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.create_replication_task)
        """

    def delete_certificate(self, CertificateArn: str) -> DeleteCertificateResponseTypeDef:
        """
        [Client.delete_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.delete_certificate)
        """

    def delete_connection(
        self, EndpointArn: str, ReplicationInstanceArn: str
    ) -> DeleteConnectionResponseTypeDef:
        """
        [Client.delete_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.delete_connection)
        """

    def delete_endpoint(self, EndpointArn: str) -> DeleteEndpointResponseTypeDef:
        """
        [Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.delete_endpoint)
        """

    def delete_event_subscription(
        self, SubscriptionName: str
    ) -> DeleteEventSubscriptionResponseTypeDef:
        """
        [Client.delete_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.delete_event_subscription)
        """

    def delete_replication_instance(
        self, ReplicationInstanceArn: str
    ) -> DeleteReplicationInstanceResponseTypeDef:
        """
        [Client.delete_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_instance)
        """

    def delete_replication_subnet_group(
        self, ReplicationSubnetGroupIdentifier: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_replication_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_subnet_group)
        """

    def delete_replication_task(
        self, ReplicationTaskArn: str
    ) -> DeleteReplicationTaskResponseTypeDef:
        """
        [Client.delete_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_task)
        """

    def delete_replication_task_assessment_run(
        self, ReplicationTaskAssessmentRunArn: str
    ) -> DeleteReplicationTaskAssessmentRunResponseTypeDef:
        """
        [Client.delete_replication_task_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.delete_replication_task_assessment_run)
        """

    def describe_account_attributes(self) -> DescribeAccountAttributesResponseTypeDef:
        """
        [Client.describe_account_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_account_attributes)
        """

    def describe_applicable_individual_assessments(
        self,
        ReplicationTaskArn: str = None,
        ReplicationInstanceArn: str = None,
        SourceEngineName: str = None,
        TargetEngineName: str = None,
        MigrationType: Literal["full-load", "cdc", "full-load-and-cdc"] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeApplicableIndividualAssessmentsResponseTypeDef:
        """
        [Client.describe_applicable_individual_assessments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_applicable_individual_assessments)
        """

    def describe_certificates(
        self, Filters: List[FilterTypeDef] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeCertificatesResponseTypeDef:
        """
        [Client.describe_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_certificates)
        """

    def describe_connections(
        self, Filters: List[FilterTypeDef] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeConnectionsResponseTypeDef:
        """
        [Client.describe_connections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_connections)
        """

    def describe_endpoint_types(
        self, Filters: List[FilterTypeDef] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeEndpointTypesResponseTypeDef:
        """
        [Client.describe_endpoint_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_endpoint_types)
        """

    def describe_endpoints(
        self, Filters: List[FilterTypeDef] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeEndpointsResponseTypeDef:
        """
        [Client.describe_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_endpoints)
        """

    def describe_event_categories(
        self, SourceType: str = None, Filters: List[FilterTypeDef] = None
    ) -> DescribeEventCategoriesResponseTypeDef:
        """
        [Client.describe_event_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_event_categories)
        """

    def describe_event_subscriptions(
        self,
        SubscriptionName: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeEventSubscriptionsResponseTypeDef:
        """
        [Client.describe_event_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_event_subscriptions)
        """

    def describe_events(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal["replication-instance"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
    ) -> DescribeEventsResponseTypeDef:
        """
        [Client.describe_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_events)
        """

    def describe_orderable_replication_instances(
        self, MaxRecords: int = None, Marker: str = None
    ) -> DescribeOrderableReplicationInstancesResponseTypeDef:
        """
        [Client.describe_orderable_replication_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_orderable_replication_instances)
        """

    def describe_pending_maintenance_actions(
        self,
        ReplicationInstanceArn: str = None,
        Filters: List[FilterTypeDef] = None,
        Marker: str = None,
        MaxRecords: int = None,
    ) -> DescribePendingMaintenanceActionsResponseTypeDef:
        """
        [Client.describe_pending_maintenance_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_pending_maintenance_actions)
        """

    def describe_refresh_schemas_status(
        self, EndpointArn: str
    ) -> DescribeRefreshSchemasStatusResponseTypeDef:
        """
        [Client.describe_refresh_schemas_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_refresh_schemas_status)
        """

    def describe_replication_instance_task_logs(
        self, ReplicationInstanceArn: str, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationInstanceTaskLogsResponseTypeDef:
        """
        [Client.describe_replication_instance_task_logs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_instance_task_logs)
        """

    def describe_replication_instances(
        self, Filters: List[FilterTypeDef] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationInstancesResponseTypeDef:
        """
        [Client.describe_replication_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_instances)
        """

    def describe_replication_subnet_groups(
        self, Filters: List[FilterTypeDef] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationSubnetGroupsResponseTypeDef:
        """
        [Client.describe_replication_subnet_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_subnet_groups)
        """

    def describe_replication_task_assessment_results(
        self, ReplicationTaskArn: str = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationTaskAssessmentResultsResponseTypeDef:
        """
        [Client.describe_replication_task_assessment_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_task_assessment_results)
        """

    def describe_replication_task_assessment_runs(
        self, Filters: List[FilterTypeDef] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationTaskAssessmentRunsResponseTypeDef:
        """
        [Client.describe_replication_task_assessment_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_task_assessment_runs)
        """

    def describe_replication_task_individual_assessments(
        self, Filters: List[FilterTypeDef] = None, MaxRecords: int = None, Marker: str = None
    ) -> DescribeReplicationTaskIndividualAssessmentsResponseTypeDef:
        """
        [Client.describe_replication_task_individual_assessments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_task_individual_assessments)
        """

    def describe_replication_tasks(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WithoutSettings: bool = None,
    ) -> DescribeReplicationTasksResponseTypeDef:
        """
        [Client.describe_replication_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_replication_tasks)
        """

    def describe_schemas(
        self, EndpointArn: str, MaxRecords: int = None, Marker: str = None
    ) -> DescribeSchemasResponseTypeDef:
        """
        [Client.describe_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_schemas)
        """

    def describe_table_statistics(
        self,
        ReplicationTaskArn: str,
        MaxRecords: int = None,
        Marker: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> DescribeTableStatisticsResponseTypeDef:
        """
        [Client.describe_table_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.describe_table_statistics)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.generate_presigned_url)
        """

    def import_certificate(
        self,
        CertificateIdentifier: str,
        CertificatePem: str = None,
        CertificateWallet: Union[bytes, IO[bytes]] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> ImportCertificateResponseTypeDef:
        """
        [Client.import_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.import_certificate)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.list_tags_for_resource)
        """

    def modify_endpoint(
        self,
        EndpointArn: str,
        EndpointIdentifier: str = None,
        EndpointType: Literal["source", "target"] = None,
        EngineName: str = None,
        Username: str = None,
        Password: str = None,
        ServerName: str = None,
        Port: int = None,
        DatabaseName: str = None,
        ExtraConnectionAttributes: str = None,
        CertificateArn: str = None,
        SslMode: Literal["none", "require", "verify-ca", "verify-full"] = None,
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
    ) -> ModifyEndpointResponseTypeDef:
        """
        [Client.modify_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.modify_endpoint)
        """

    def modify_event_subscription(
        self,
        SubscriptionName: str,
        SnsTopicArn: str = None,
        SourceType: str = None,
        EventCategories: List[str] = None,
        Enabled: bool = None,
    ) -> ModifyEventSubscriptionResponseTypeDef:
        """
        [Client.modify_event_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.modify_event_subscription)
        """

    def modify_replication_instance(
        self,
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
    ) -> ModifyReplicationInstanceResponseTypeDef:
        """
        [Client.modify_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_instance)
        """

    def modify_replication_subnet_group(
        self,
        ReplicationSubnetGroupIdentifier: str,
        SubnetIds: List[str],
        ReplicationSubnetGroupDescription: str = None,
    ) -> ModifyReplicationSubnetGroupResponseTypeDef:
        """
        [Client.modify_replication_subnet_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_subnet_group)
        """

    def modify_replication_task(
        self,
        ReplicationTaskArn: str,
        ReplicationTaskIdentifier: str = None,
        MigrationType: Literal["full-load", "cdc", "full-load-and-cdc"] = None,
        TableMappings: str = None,
        ReplicationTaskSettings: str = None,
        CdcStartTime: datetime = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
        TaskData: str = None,
    ) -> ModifyReplicationTaskResponseTypeDef:
        """
        [Client.modify_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.modify_replication_task)
        """

    def reboot_replication_instance(
        self, ReplicationInstanceArn: str, ForceFailover: bool = None
    ) -> RebootReplicationInstanceResponseTypeDef:
        """
        [Client.reboot_replication_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.reboot_replication_instance)
        """

    def refresh_schemas(
        self, EndpointArn: str, ReplicationInstanceArn: str
    ) -> RefreshSchemasResponseTypeDef:
        """
        [Client.refresh_schemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.refresh_schemas)
        """

    def reload_tables(
        self,
        ReplicationTaskArn: str,
        TablesToReload: List[TableToReloadTypeDef],
        ReloadOption: Literal["data-reload", "validate-only"] = None,
    ) -> ReloadTablesResponseTypeDef:
        """
        [Client.reload_tables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.reload_tables)
        """

    def remove_tags_from_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.remove_tags_from_resource)
        """

    def start_replication_task(
        self,
        ReplicationTaskArn: str,
        StartReplicationTaskType: Literal[
            "start-replication", "resume-processing", "reload-target"
        ],
        CdcStartTime: datetime = None,
        CdcStartPosition: str = None,
        CdcStopPosition: str = None,
    ) -> StartReplicationTaskResponseTypeDef:
        """
        [Client.start_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task)
        """

    def start_replication_task_assessment(
        self, ReplicationTaskArn: str
    ) -> StartReplicationTaskAssessmentResponseTypeDef:
        """
        [Client.start_replication_task_assessment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task_assessment)
        """

    def start_replication_task_assessment_run(
        self,
        ReplicationTaskArn: str,
        ServiceAccessRoleArn: str,
        ResultLocationBucket: str,
        AssessmentRunName: str,
        ResultLocationFolder: str = None,
        ResultEncryptionMode: str = None,
        ResultKmsKeyArn: str = None,
        IncludeOnly: List[str] = None,
        Exclude: List[str] = None,
    ) -> StartReplicationTaskAssessmentRunResponseTypeDef:
        """
        [Client.start_replication_task_assessment_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.start_replication_task_assessment_run)
        """

    def stop_replication_task(self, ReplicationTaskArn: str) -> StopReplicationTaskResponseTypeDef:
        """
        [Client.stop_replication_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.stop_replication_task)
        """

    def test_connection(
        self, ReplicationInstanceArn: str, EndpointArn: str
    ) -> TestConnectionResponseTypeDef:
        """
        [Client.test_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Client.test_connection)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_certificates"]
    ) -> DescribeCertificatesPaginator:
        """
        [Paginator.DescribeCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeCertificates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_connections"]
    ) -> DescribeConnectionsPaginator:
        """
        [Paginator.DescribeConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeConnections)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_endpoint_types"]
    ) -> DescribeEndpointTypesPaginator:
        """
        [Paginator.DescribeEndpointTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpointTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_endpoints"]
    ) -> DescribeEndpointsPaginator:
        """
        [Paginator.DescribeEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpoints)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_event_subscriptions"]
    ) -> DescribeEventSubscriptionsPaginator:
        """
        [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEventSubscriptions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_events"]) -> DescribeEventsPaginator:
        """
        [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_orderable_replication_instances"]
    ) -> DescribeOrderableReplicationInstancesPaginator:
        """
        [Paginator.DescribeOrderableReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeOrderableReplicationInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_instances"]
    ) -> DescribeReplicationInstancesPaginator:
        """
        [Paginator.DescribeReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_subnet_groups"]
    ) -> DescribeReplicationSubnetGroupsPaginator:
        """
        [Paginator.DescribeReplicationSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationSubnetGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_task_assessment_results"]
    ) -> DescribeReplicationTaskAssessmentResultsPaginator:
        """
        [Paginator.DescribeReplicationTaskAssessmentResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTaskAssessmentResults)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replication_tasks"]
    ) -> DescribeReplicationTasksPaginator:
        """
        [Paginator.DescribeReplicationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_schemas"]
    ) -> DescribeSchemasPaginator:
        """
        [Paginator.DescribeSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeSchemas)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_table_statistics"]
    ) -> DescribeTableStatisticsPaginator:
        """
        [Paginator.DescribeTableStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeTableStatistics)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass

    @overload
    def get_waiter(self, waiter_name: Literal["endpoint_deleted"]) -> EndpointDeletedWaiter:
        """
        [Waiter.EndpointDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Waiter.EndpointDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_instance_available"]
    ) -> ReplicationInstanceAvailableWaiter:
        """
        [Waiter.ReplicationInstanceAvailable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceAvailable)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_instance_deleted"]
    ) -> ReplicationInstanceDeletedWaiter:
        """
        [Waiter.ReplicationInstanceDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationInstanceDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_deleted"]
    ) -> ReplicationTaskDeletedWaiter:
        """
        [Waiter.ReplicationTaskDeleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskDeleted)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_ready"]
    ) -> ReplicationTaskReadyWaiter:
        """
        [Waiter.ReplicationTaskReady documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskReady)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_running"]
    ) -> ReplicationTaskRunningWaiter:
        """
        [Waiter.ReplicationTaskRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskRunning)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["replication_task_stopped"]
    ) -> ReplicationTaskStoppedWaiter:
        """
        [Waiter.ReplicationTaskStopped documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Waiter.ReplicationTaskStopped)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["test_connection_succeeds"]
    ) -> TestConnectionSucceedsWaiter:
        """
        [Waiter.TestConnectionSucceeds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dms.html#DatabaseMigrationService.Waiter.TestConnectionSucceeds)
        """

    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        pass
