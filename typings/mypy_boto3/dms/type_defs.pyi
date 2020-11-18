from mypy_boto3_dms.type_defs import (
    AccountQuotaTypeDef,
    AvailabilityZoneTypeDef,
    CertificateTypeDef,
    ConnectionTypeDef,
    DmsTransferSettingsTypeDef,
    DocDbSettingsTypeDef,
    DynamoDbSettingsTypeDef,
    ElasticsearchSettingsTypeDef,
    EndpointTypeDef,
    EventCategoryGroupTypeDef,
    EventSubscriptionTypeDef,
    EventTypeDef,
    IBMDb2SettingsTypeDef,
    KafkaSettingsTypeDef,
    KinesisSettingsTypeDef,
    MicrosoftSQLServerSettingsTypeDef,
    MongoDbSettingsTypeDef,
    MySQLSettingsTypeDef,
    NeptuneSettingsTypeDef,
    OracleSettingsTypeDef,
    OrderableReplicationInstanceTypeDef,
    PendingMaintenanceActionTypeDef,
    PostgreSQLSettingsTypeDef,
    RedshiftSettingsTypeDef,
    RefreshSchemasStatusTypeDef,
    ReplicationInstanceTaskLogTypeDef,
    ReplicationInstanceTypeDef,
    ReplicationPendingModifiedValuesTypeDef,
    ReplicationSubnetGroupTypeDef,
    ReplicationTaskAssessmentResultTypeDef,
    ReplicationTaskAssessmentRunProgressTypeDef,
    ReplicationTaskAssessmentRunTypeDef,
    ReplicationTaskIndividualAssessmentTypeDef,
    ReplicationTaskStatsTypeDef,
    ReplicationTaskTypeDef,
    ResourcePendingMaintenanceActionsTypeDef,
    S3SettingsTypeDef,
    SubnetTypeDef,
    SupportedEndpointTypeTypeDef,
    SybaseSettingsTypeDef,
    TableStatisticsTypeDef,
    TagTypeDef,
    VpcSecurityGroupMembershipTypeDef,
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
    DescribeEndpointTypesResponseTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeEventCategoriesResponseTypeDef,
    DescribeEventSubscriptionsResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeOrderableReplicationInstancesResponseTypeDef,
    DescribePendingMaintenanceActionsResponseTypeDef,
    DescribeRefreshSchemasStatusResponseTypeDef,
    DescribeReplicationInstanceTaskLogsResponseTypeDef,
    DescribeReplicationInstancesResponseTypeDef,
    DescribeReplicationSubnetGroupsResponseTypeDef,
    DescribeReplicationTaskAssessmentResultsResponseTypeDef,
    DescribeReplicationTaskAssessmentRunsResponseTypeDef,
    DescribeReplicationTaskIndividualAssessmentsResponseTypeDef,
    DescribeReplicationTasksResponseTypeDef,
    DescribeSchemasResponseTypeDef,
    DescribeTableStatisticsResponseTypeDef,
    FilterTypeDef,
    ImportCertificateResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ModifyEndpointResponseTypeDef,
    ModifyEventSubscriptionResponseTypeDef,
    ModifyReplicationInstanceResponseTypeDef,
    ModifyReplicationSubnetGroupResponseTypeDef,
    ModifyReplicationTaskResponseTypeDef,
    MoveReplicationTaskResponseTypeDef,
    PaginatorConfigTypeDef,
    RebootReplicationInstanceResponseTypeDef,
    RefreshSchemasResponseTypeDef,
    ReloadTablesResponseTypeDef,
    StartReplicationTaskAssessmentResponseTypeDef,
    StartReplicationTaskAssessmentRunResponseTypeDef,
    StartReplicationTaskResponseTypeDef,
    StopReplicationTaskResponseTypeDef,
    TableToReloadTypeDef,
    TestConnectionResponseTypeDef,
    WaiterConfigTypeDef,
)

__all__ = (
    "AccountQuotaTypeDef",
    "AvailabilityZoneTypeDef",
    "CertificateTypeDef",
    "ConnectionTypeDef",
    "DmsTransferSettingsTypeDef",
    "DocDbSettingsTypeDef",
    "DynamoDbSettingsTypeDef",
    "ElasticsearchSettingsTypeDef",
    "EndpointTypeDef",
    "EventCategoryGroupTypeDef",
    "EventSubscriptionTypeDef",
    "EventTypeDef",
    "IBMDb2SettingsTypeDef",
    "KafkaSettingsTypeDef",
    "KinesisSettingsTypeDef",
    "MicrosoftSQLServerSettingsTypeDef",
    "MongoDbSettingsTypeDef",
    "MySQLSettingsTypeDef",
    "NeptuneSettingsTypeDef",
    "OracleSettingsTypeDef",
    "OrderableReplicationInstanceTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PostgreSQLSettingsTypeDef",
    "RedshiftSettingsTypeDef",
    "RefreshSchemasStatusTypeDef",
    "ReplicationInstanceTaskLogTypeDef",
    "ReplicationInstanceTypeDef",
    "ReplicationPendingModifiedValuesTypeDef",
    "ReplicationSubnetGroupTypeDef",
    "ReplicationTaskAssessmentResultTypeDef",
    "ReplicationTaskAssessmentRunProgressTypeDef",
    "ReplicationTaskAssessmentRunTypeDef",
    "ReplicationTaskIndividualAssessmentTypeDef",
    "ReplicationTaskStatsTypeDef",
    "ReplicationTaskTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "S3SettingsTypeDef",
    "SubnetTypeDef",
    "SupportedEndpointTypeTypeDef",
    "SybaseSettingsTypeDef",
    "TableStatisticsTypeDef",
    "TagTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "ApplyPendingMaintenanceActionResponseTypeDef",
    "CancelReplicationTaskAssessmentRunResponseTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreateEventSubscriptionResponseTypeDef",
    "CreateReplicationInstanceResponseTypeDef",
    "CreateReplicationSubnetGroupResponseTypeDef",
    "CreateReplicationTaskResponseTypeDef",
    "DeleteCertificateResponseTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteEndpointResponseTypeDef",
    "DeleteEventSubscriptionResponseTypeDef",
    "DeleteReplicationInstanceResponseTypeDef",
    "DeleteReplicationTaskAssessmentRunResponseTypeDef",
    "DeleteReplicationTaskResponseTypeDef",
    "DescribeAccountAttributesResponseTypeDef",
    "DescribeApplicableIndividualAssessmentsResponseTypeDef",
    "DescribeCertificatesResponseTypeDef",
    "DescribeConnectionsResponseTypeDef",
    "DescribeEndpointTypesResponseTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeEventCategoriesResponseTypeDef",
    "DescribeEventSubscriptionsResponseTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeOrderableReplicationInstancesResponseTypeDef",
    "DescribePendingMaintenanceActionsResponseTypeDef",
    "DescribeRefreshSchemasStatusResponseTypeDef",
    "DescribeReplicationInstanceTaskLogsResponseTypeDef",
    "DescribeReplicationInstancesResponseTypeDef",
    "DescribeReplicationSubnetGroupsResponseTypeDef",
    "DescribeReplicationTaskAssessmentResultsResponseTypeDef",
    "DescribeReplicationTaskAssessmentRunsResponseTypeDef",
    "DescribeReplicationTaskIndividualAssessmentsResponseTypeDef",
    "DescribeReplicationTasksResponseTypeDef",
    "DescribeSchemasResponseTypeDef",
    "DescribeTableStatisticsResponseTypeDef",
    "FilterTypeDef",
    "ImportCertificateResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModifyEndpointResponseTypeDef",
    "ModifyEventSubscriptionResponseTypeDef",
    "ModifyReplicationInstanceResponseTypeDef",
    "ModifyReplicationSubnetGroupResponseTypeDef",
    "ModifyReplicationTaskResponseTypeDef",
    "MoveReplicationTaskResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RebootReplicationInstanceResponseTypeDef",
    "RefreshSchemasResponseTypeDef",
    "ReloadTablesResponseTypeDef",
    "StartReplicationTaskAssessmentResponseTypeDef",
    "StartReplicationTaskAssessmentRunResponseTypeDef",
    "StartReplicationTaskResponseTypeDef",
    "StopReplicationTaskResponseTypeDef",
    "TableToReloadTypeDef",
    "TestConnectionResponseTypeDef",
    "WaiterConfigTypeDef",
)
