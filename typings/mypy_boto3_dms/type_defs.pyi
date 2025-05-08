"""
Type annotations for dms service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dms/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_dms.type_defs import AccountQuotaTypeDef

    data: AccountQuotaTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AssessmentReportTypeType,
    AuthMechanismValueType,
    AuthTypeValueType,
    CannedAclForObjectsValueType,
    CharLengthSemanticsType,
    CollectorStatusType,
    CompressionTypeValueType,
    DatabaseModeType,
    DataFormatValueType,
    DatePartitionDelimiterValueType,
    DatePartitionSequenceValueType,
    DmsSslModeValueType,
    EncodingTypeValueType,
    EncryptionModeValueType,
    EndpointSettingTypeValueType,
    KafkaSaslMechanismType,
    KafkaSecurityProtocolType,
    KafkaSslEndpointIdentificationAlgorithmType,
    LongVarcharMappingTypeType,
    MessageFormatValueType,
    MigrationTypeValueType,
    NestingLevelValueType,
    OracleAuthenticationMethodType,
    OriginTypeValueType,
    ParquetVersionValueType,
    PluginNameValueType,
    RedisAuthTypeValueType,
    RefreshSchemasStatusTypeValueType,
    ReleaseStatusValuesType,
    ReloadOptionValueType,
    ReplicationEndpointTypeValueType,
    SafeguardPolicyType,
    SqlServerAuthenticationMethodType,
    SslSecurityProtocolValueType,
    StartReplicationMigrationTypeValueType,
    StartReplicationTaskTypeValueType,
    TablePreparationModeType,
    TargetDbTypeType,
    TlogAccessModeType,
    VersionStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccountQuotaTypeDef",
    "AddTagsToResourceMessageTypeDef",
    "ApplyPendingMaintenanceActionMessageTypeDef",
    "ApplyPendingMaintenanceActionResponseTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchStartRecommendationsErrorEntryTypeDef",
    "BatchStartRecommendationsRequestTypeDef",
    "BatchStartRecommendationsResponseTypeDef",
    "BlobTypeDef",
    "CancelReplicationTaskAssessmentRunMessageTypeDef",
    "CancelReplicationTaskAssessmentRunResponseTypeDef",
    "CertificateTypeDef",
    "CollectorHealthCheckTypeDef",
    "CollectorResponseTypeDef",
    "CollectorShortInfoResponseTypeDef",
    "ComputeConfigOutputTypeDef",
    "ComputeConfigTypeDef",
    "ComputeConfigUnionTypeDef",
    "ConnectionTypeDef",
    "CreateDataMigrationMessageTypeDef",
    "CreateDataMigrationResponseTypeDef",
    "CreateDataProviderMessageTypeDef",
    "CreateDataProviderResponseTypeDef",
    "CreateEndpointMessageTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreateEventSubscriptionMessageTypeDef",
    "CreateEventSubscriptionResponseTypeDef",
    "CreateFleetAdvisorCollectorRequestTypeDef",
    "CreateFleetAdvisorCollectorResponseTypeDef",
    "CreateInstanceProfileMessageTypeDef",
    "CreateInstanceProfileResponseTypeDef",
    "CreateMigrationProjectMessageTypeDef",
    "CreateMigrationProjectResponseTypeDef",
    "CreateReplicationConfigMessageTypeDef",
    "CreateReplicationConfigResponseTypeDef",
    "CreateReplicationInstanceMessageTypeDef",
    "CreateReplicationInstanceResponseTypeDef",
    "CreateReplicationSubnetGroupMessageTypeDef",
    "CreateReplicationSubnetGroupResponseTypeDef",
    "CreateReplicationTaskMessageTypeDef",
    "CreateReplicationTaskResponseTypeDef",
    "DataMigrationSettingsTypeDef",
    "DataMigrationStatisticsTypeDef",
    "DataMigrationTypeDef",
    "DataProviderDescriptorDefinitionTypeDef",
    "DataProviderDescriptorTypeDef",
    "DataProviderSettingsTypeDef",
    "DataProviderTypeDef",
    "DatabaseInstanceSoftwareDetailsResponseTypeDef",
    "DatabaseResponseTypeDef",
    "DatabaseShortInfoResponseTypeDef",
    "DefaultErrorDetailsTypeDef",
    "DeleteCertificateMessageTypeDef",
    "DeleteCertificateResponseTypeDef",
    "DeleteCollectorRequestTypeDef",
    "DeleteConnectionMessageTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteDataMigrationMessageTypeDef",
    "DeleteDataMigrationResponseTypeDef",
    "DeleteDataProviderMessageTypeDef",
    "DeleteDataProviderResponseTypeDef",
    "DeleteEndpointMessageTypeDef",
    "DeleteEndpointResponseTypeDef",
    "DeleteEventSubscriptionMessageTypeDef",
    "DeleteEventSubscriptionResponseTypeDef",
    "DeleteFleetAdvisorDatabasesRequestTypeDef",
    "DeleteFleetAdvisorDatabasesResponseTypeDef",
    "DeleteInstanceProfileMessageTypeDef",
    "DeleteInstanceProfileResponseTypeDef",
    "DeleteMigrationProjectMessageTypeDef",
    "DeleteMigrationProjectResponseTypeDef",
    "DeleteReplicationConfigMessageTypeDef",
    "DeleteReplicationConfigResponseTypeDef",
    "DeleteReplicationInstanceMessageTypeDef",
    "DeleteReplicationInstanceResponseTypeDef",
    "DeleteReplicationSubnetGroupMessageTypeDef",
    "DeleteReplicationTaskAssessmentRunMessageTypeDef",
    "DeleteReplicationTaskAssessmentRunResponseTypeDef",
    "DeleteReplicationTaskMessageTypeDef",
    "DeleteReplicationTaskResponseTypeDef",
    "DescribeAccountAttributesResponseTypeDef",
    "DescribeApplicableIndividualAssessmentsMessageTypeDef",
    "DescribeApplicableIndividualAssessmentsResponseTypeDef",
    "DescribeCertificatesMessagePaginateTypeDef",
    "DescribeCertificatesMessageTypeDef",
    "DescribeCertificatesResponseTypeDef",
    "DescribeConnectionsMessagePaginateTypeDef",
    "DescribeConnectionsMessageTypeDef",
    "DescribeConnectionsMessageWaitTypeDef",
    "DescribeConnectionsResponseTypeDef",
    "DescribeConversionConfigurationMessageTypeDef",
    "DescribeConversionConfigurationResponseTypeDef",
    "DescribeDataMigrationsMessagePaginateTypeDef",
    "DescribeDataMigrationsMessageTypeDef",
    "DescribeDataMigrationsResponseTypeDef",
    "DescribeDataProvidersMessageTypeDef",
    "DescribeDataProvidersResponseTypeDef",
    "DescribeEndpointSettingsMessageTypeDef",
    "DescribeEndpointSettingsResponseTypeDef",
    "DescribeEndpointTypesMessagePaginateTypeDef",
    "DescribeEndpointTypesMessageTypeDef",
    "DescribeEndpointTypesResponseTypeDef",
    "DescribeEndpointsMessagePaginateTypeDef",
    "DescribeEndpointsMessageTypeDef",
    "DescribeEndpointsMessageWaitTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeEngineVersionsMessageTypeDef",
    "DescribeEngineVersionsResponseTypeDef",
    "DescribeEventCategoriesMessageTypeDef",
    "DescribeEventCategoriesResponseTypeDef",
    "DescribeEventSubscriptionsMessagePaginateTypeDef",
    "DescribeEventSubscriptionsMessageTypeDef",
    "DescribeEventSubscriptionsResponseTypeDef",
    "DescribeEventsMessagePaginateTypeDef",
    "DescribeEventsMessageTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeExtensionPackAssociationsMessageTypeDef",
    "DescribeExtensionPackAssociationsResponseTypeDef",
    "DescribeFleetAdvisorCollectorsRequestTypeDef",
    "DescribeFleetAdvisorCollectorsResponseTypeDef",
    "DescribeFleetAdvisorDatabasesRequestTypeDef",
    "DescribeFleetAdvisorDatabasesResponseTypeDef",
    "DescribeFleetAdvisorLsaAnalysisRequestTypeDef",
    "DescribeFleetAdvisorLsaAnalysisResponseTypeDef",
    "DescribeFleetAdvisorSchemaObjectSummaryRequestTypeDef",
    "DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef",
    "DescribeFleetAdvisorSchemasRequestTypeDef",
    "DescribeFleetAdvisorSchemasResponseTypeDef",
    "DescribeInstanceProfilesMessageTypeDef",
    "DescribeInstanceProfilesResponseTypeDef",
    "DescribeMetadataModelAssessmentsMessageTypeDef",
    "DescribeMetadataModelAssessmentsResponseTypeDef",
    "DescribeMetadataModelConversionsMessageTypeDef",
    "DescribeMetadataModelConversionsResponseTypeDef",
    "DescribeMetadataModelExportsAsScriptMessageTypeDef",
    "DescribeMetadataModelExportsAsScriptResponseTypeDef",
    "DescribeMetadataModelExportsToTargetMessageTypeDef",
    "DescribeMetadataModelExportsToTargetResponseTypeDef",
    "DescribeMetadataModelImportsMessageTypeDef",
    "DescribeMetadataModelImportsResponseTypeDef",
    "DescribeMigrationProjectsMessageTypeDef",
    "DescribeMigrationProjectsResponseTypeDef",
    "DescribeOrderableReplicationInstancesMessagePaginateTypeDef",
    "DescribeOrderableReplicationInstancesMessageTypeDef",
    "DescribeOrderableReplicationInstancesResponseTypeDef",
    "DescribePendingMaintenanceActionsMessageTypeDef",
    "DescribePendingMaintenanceActionsResponseTypeDef",
    "DescribeRecommendationLimitationsRequestTypeDef",
    "DescribeRecommendationLimitationsResponseTypeDef",
    "DescribeRecommendationsRequestTypeDef",
    "DescribeRecommendationsResponseTypeDef",
    "DescribeRefreshSchemasStatusMessageTypeDef",
    "DescribeRefreshSchemasStatusResponseTypeDef",
    "DescribeReplicationConfigsMessageTypeDef",
    "DescribeReplicationConfigsResponseTypeDef",
    "DescribeReplicationInstanceTaskLogsMessageTypeDef",
    "DescribeReplicationInstanceTaskLogsResponseTypeDef",
    "DescribeReplicationInstancesMessagePaginateTypeDef",
    "DescribeReplicationInstancesMessageTypeDef",
    "DescribeReplicationInstancesMessageWaitExtraTypeDef",
    "DescribeReplicationInstancesMessageWaitTypeDef",
    "DescribeReplicationInstancesResponseTypeDef",
    "DescribeReplicationSubnetGroupsMessagePaginateTypeDef",
    "DescribeReplicationSubnetGroupsMessageTypeDef",
    "DescribeReplicationSubnetGroupsResponseTypeDef",
    "DescribeReplicationTableStatisticsMessageTypeDef",
    "DescribeReplicationTableStatisticsResponseTypeDef",
    "DescribeReplicationTaskAssessmentResultsMessagePaginateTypeDef",
    "DescribeReplicationTaskAssessmentResultsMessageTypeDef",
    "DescribeReplicationTaskAssessmentResultsResponseTypeDef",
    "DescribeReplicationTaskAssessmentRunsMessageTypeDef",
    "DescribeReplicationTaskAssessmentRunsResponseTypeDef",
    "DescribeReplicationTaskIndividualAssessmentsMessageTypeDef",
    "DescribeReplicationTaskIndividualAssessmentsResponseTypeDef",
    "DescribeReplicationTasksMessagePaginateTypeDef",
    "DescribeReplicationTasksMessageTypeDef",
    "DescribeReplicationTasksMessageWaitExtraExtraExtraTypeDef",
    "DescribeReplicationTasksMessageWaitExtraExtraTypeDef",
    "DescribeReplicationTasksMessageWaitExtraTypeDef",
    "DescribeReplicationTasksMessageWaitTypeDef",
    "DescribeReplicationTasksResponseTypeDef",
    "DescribeReplicationsMessageTypeDef",
    "DescribeReplicationsResponseTypeDef",
    "DescribeSchemasMessagePaginateTypeDef",
    "DescribeSchemasMessageTypeDef",
    "DescribeSchemasResponseTypeDef",
    "DescribeTableStatisticsMessagePaginateTypeDef",
    "DescribeTableStatisticsMessageTypeDef",
    "DescribeTableStatisticsResponseTypeDef",
    "DmsTransferSettingsTypeDef",
    "DocDbDataProviderSettingsTypeDef",
    "DocDbSettingsTypeDef",
    "DynamoDbSettingsTypeDef",
    "ElasticsearchSettingsTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EndpointSettingTypeDef",
    "EndpointTypeDef",
    "EngineVersionTypeDef",
    "ErrorDetailsTypeDef",
    "EventCategoryGroupTypeDef",
    "EventSubscriptionTypeDef",
    "EventTypeDef",
    "ExportMetadataModelAssessmentMessageTypeDef",
    "ExportMetadataModelAssessmentResponseTypeDef",
    "ExportMetadataModelAssessmentResultEntryTypeDef",
    "ExportSqlDetailsTypeDef",
    "FilterTypeDef",
    "FleetAdvisorLsaAnalysisResponseTypeDef",
    "FleetAdvisorSchemaObjectResponseTypeDef",
    "GcpMySQLSettingsTypeDef",
    "IBMDb2SettingsTypeDef",
    "IbmDb2LuwDataProviderSettingsTypeDef",
    "IbmDb2zOsDataProviderSettingsTypeDef",
    "ImportCertificateMessageTypeDef",
    "ImportCertificateResponseTypeDef",
    "InstanceProfileTypeDef",
    "InventoryDataTypeDef",
    "KafkaSettingsTypeDef",
    "KerberosAuthenticationSettingsTypeDef",
    "KinesisSettingsTypeDef",
    "LimitationTypeDef",
    "ListTagsForResourceMessageTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MariaDbDataProviderSettingsTypeDef",
    "MicrosoftSQLServerSettingsTypeDef",
    "MicrosoftSqlServerDataProviderSettingsTypeDef",
    "MigrationProjectTypeDef",
    "ModifyConversionConfigurationMessageTypeDef",
    "ModifyConversionConfigurationResponseTypeDef",
    "ModifyDataMigrationMessageTypeDef",
    "ModifyDataMigrationResponseTypeDef",
    "ModifyDataProviderMessageTypeDef",
    "ModifyDataProviderResponseTypeDef",
    "ModifyEndpointMessageTypeDef",
    "ModifyEndpointResponseTypeDef",
    "ModifyEventSubscriptionMessageTypeDef",
    "ModifyEventSubscriptionResponseTypeDef",
    "ModifyInstanceProfileMessageTypeDef",
    "ModifyInstanceProfileResponseTypeDef",
    "ModifyMigrationProjectMessageTypeDef",
    "ModifyMigrationProjectResponseTypeDef",
    "ModifyReplicationConfigMessageTypeDef",
    "ModifyReplicationConfigResponseTypeDef",
    "ModifyReplicationInstanceMessageTypeDef",
    "ModifyReplicationInstanceResponseTypeDef",
    "ModifyReplicationSubnetGroupMessageTypeDef",
    "ModifyReplicationSubnetGroupResponseTypeDef",
    "ModifyReplicationTaskMessageTypeDef",
    "ModifyReplicationTaskResponseTypeDef",
    "MongoDbDataProviderSettingsTypeDef",
    "MongoDbSettingsTypeDef",
    "MoveReplicationTaskMessageTypeDef",
    "MoveReplicationTaskResponseTypeDef",
    "MySQLSettingsTypeDef",
    "MySqlDataProviderSettingsTypeDef",
    "NeptuneSettingsTypeDef",
    "OracleDataProviderSettingsTypeDef",
    "OracleSettingsOutputTypeDef",
    "OracleSettingsTypeDef",
    "OracleSettingsUnionTypeDef",
    "OrderableReplicationInstanceTypeDef",
    "PaginatorConfigTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PostgreSQLSettingsTypeDef",
    "PostgreSqlDataProviderSettingsTypeDef",
    "PremigrationAssessmentStatusTypeDef",
    "ProvisionDataTypeDef",
    "RdsConfigurationTypeDef",
    "RdsRecommendationTypeDef",
    "RdsRequirementsTypeDef",
    "RebootReplicationInstanceMessageTypeDef",
    "RebootReplicationInstanceResponseTypeDef",
    "RecommendationDataTypeDef",
    "RecommendationSettingsTypeDef",
    "RecommendationTypeDef",
    "RedisSettingsTypeDef",
    "RedshiftDataProviderSettingsTypeDef",
    "RedshiftSettingsTypeDef",
    "RefreshSchemasMessageTypeDef",
    "RefreshSchemasResponseTypeDef",
    "RefreshSchemasStatusTypeDef",
    "ReloadReplicationTablesMessageTypeDef",
    "ReloadReplicationTablesResponseTypeDef",
    "ReloadTablesMessageTypeDef",
    "ReloadTablesResponseTypeDef",
    "RemoveTagsFromResourceMessageTypeDef",
    "ReplicationConfigTypeDef",
    "ReplicationInstanceTaskLogTypeDef",
    "ReplicationInstanceTypeDef",
    "ReplicationPendingModifiedValuesTypeDef",
    "ReplicationStatsTypeDef",
    "ReplicationSubnetGroupTypeDef",
    "ReplicationTaskAssessmentResultTypeDef",
    "ReplicationTaskAssessmentRunProgressTypeDef",
    "ReplicationTaskAssessmentRunResultStatisticTypeDef",
    "ReplicationTaskAssessmentRunTypeDef",
    "ReplicationTaskIndividualAssessmentTypeDef",
    "ReplicationTaskStatsTypeDef",
    "ReplicationTaskTypeDef",
    "ReplicationTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "ResponseMetadataTypeDef",
    "RunFleetAdvisorLsaAnalysisResponseTypeDef",
    "S3SettingsTypeDef",
    "SCApplicationAttributesTypeDef",
    "SchemaConversionRequestTypeDef",
    "SchemaResponseTypeDef",
    "SchemaShortInfoResponseTypeDef",
    "ServerShortInfoResponseTypeDef",
    "SourceDataSettingOutputTypeDef",
    "SourceDataSettingTypeDef",
    "SourceDataSettingUnionTypeDef",
    "StartDataMigrationMessageTypeDef",
    "StartDataMigrationResponseTypeDef",
    "StartExtensionPackAssociationMessageTypeDef",
    "StartExtensionPackAssociationResponseTypeDef",
    "StartMetadataModelAssessmentMessageTypeDef",
    "StartMetadataModelAssessmentResponseTypeDef",
    "StartMetadataModelConversionMessageTypeDef",
    "StartMetadataModelConversionResponseTypeDef",
    "StartMetadataModelExportAsScriptMessageTypeDef",
    "StartMetadataModelExportAsScriptResponseTypeDef",
    "StartMetadataModelExportToTargetMessageTypeDef",
    "StartMetadataModelExportToTargetResponseTypeDef",
    "StartMetadataModelImportMessageTypeDef",
    "StartMetadataModelImportResponseTypeDef",
    "StartRecommendationsRequestEntryTypeDef",
    "StartRecommendationsRequestTypeDef",
    "StartReplicationMessageTypeDef",
    "StartReplicationResponseTypeDef",
    "StartReplicationTaskAssessmentMessageTypeDef",
    "StartReplicationTaskAssessmentResponseTypeDef",
    "StartReplicationTaskAssessmentRunMessageTypeDef",
    "StartReplicationTaskAssessmentRunResponseTypeDef",
    "StartReplicationTaskMessageTypeDef",
    "StartReplicationTaskResponseTypeDef",
    "StopDataMigrationMessageTypeDef",
    "StopDataMigrationResponseTypeDef",
    "StopReplicationMessageTypeDef",
    "StopReplicationResponseTypeDef",
    "StopReplicationTaskMessageTypeDef",
    "StopReplicationTaskResponseTypeDef",
    "SubnetTypeDef",
    "SupportedEndpointTypeTypeDef",
    "SybaseSettingsTypeDef",
    "TableStatisticsTypeDef",
    "TableToReloadTypeDef",
    "TagTypeDef",
    "TargetDataSettingTypeDef",
    "TestConnectionMessageTypeDef",
    "TestConnectionResponseTypeDef",
    "TimestampTypeDef",
    "TimestreamSettingsTypeDef",
    "UpdateSubscriptionsToEventBridgeMessageTypeDef",
    "UpdateSubscriptionsToEventBridgeResponseTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

class AccountQuotaTypeDef(TypedDict):
    AccountQuotaName: NotRequired[str]
    Used: NotRequired[int]
    Max: NotRequired[int]

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]
    ResourceArn: NotRequired[str]

class ApplyPendingMaintenanceActionMessageTypeDef(TypedDict):
    ReplicationInstanceArn: str
    ApplyAction: str
    OptInType: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AvailabilityZoneTypeDef(TypedDict):
    Name: NotRequired[str]

class BatchStartRecommendationsErrorEntryTypeDef(TypedDict):
    DatabaseId: NotRequired[str]
    Message: NotRequired[str]
    Code: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CancelReplicationTaskAssessmentRunMessageTypeDef(TypedDict):
    ReplicationTaskAssessmentRunArn: str

class CertificateTypeDef(TypedDict):
    CertificateIdentifier: NotRequired[str]
    CertificateCreationDate: NotRequired[datetime]
    CertificatePem: NotRequired[str]
    CertificateWallet: NotRequired[bytes]
    CertificateArn: NotRequired[str]
    CertificateOwner: NotRequired[str]
    ValidFromDate: NotRequired[datetime]
    ValidToDate: NotRequired[datetime]
    SigningAlgorithm: NotRequired[str]
    KeyLength: NotRequired[int]

class CollectorHealthCheckTypeDef(TypedDict):
    CollectorStatus: NotRequired[CollectorStatusType]
    LocalCollectorS3Access: NotRequired[bool]
    WebCollectorS3Access: NotRequired[bool]
    WebCollectorGrantedRoleBasedAccess: NotRequired[bool]

class InventoryDataTypeDef(TypedDict):
    NumberOfDatabases: NotRequired[int]
    NumberOfSchemas: NotRequired[int]

class CollectorShortInfoResponseTypeDef(TypedDict):
    CollectorReferencedId: NotRequired[str]
    CollectorName: NotRequired[str]

class ComputeConfigOutputTypeDef(TypedDict):
    AvailabilityZone: NotRequired[str]
    DnsNameServers: NotRequired[str]
    KmsKeyId: NotRequired[str]
    MaxCapacityUnits: NotRequired[int]
    MinCapacityUnits: NotRequired[int]
    MultiAZ: NotRequired[bool]
    PreferredMaintenanceWindow: NotRequired[str]
    ReplicationSubnetGroupId: NotRequired[str]
    VpcSecurityGroupIds: NotRequired[List[str]]

class ComputeConfigTypeDef(TypedDict):
    AvailabilityZone: NotRequired[str]
    DnsNameServers: NotRequired[str]
    KmsKeyId: NotRequired[str]
    MaxCapacityUnits: NotRequired[int]
    MinCapacityUnits: NotRequired[int]
    MultiAZ: NotRequired[bool]
    PreferredMaintenanceWindow: NotRequired[str]
    ReplicationSubnetGroupId: NotRequired[str]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]

class ConnectionTypeDef(TypedDict):
    ReplicationInstanceArn: NotRequired[str]
    EndpointArn: NotRequired[str]
    Status: NotRequired[str]
    LastFailureMessage: NotRequired[str]
    EndpointIdentifier: NotRequired[str]
    ReplicationInstanceIdentifier: NotRequired[str]

class TargetDataSettingTypeDef(TypedDict):
    TablePreparationMode: NotRequired[TablePreparationModeType]

class DmsTransferSettingsTypeDef(TypedDict):
    ServiceAccessRoleArn: NotRequired[str]
    BucketName: NotRequired[str]

class DocDbSettingsTypeDef(TypedDict):
    Username: NotRequired[str]
    Password: NotRequired[str]
    ServerName: NotRequired[str]
    Port: NotRequired[int]
    DatabaseName: NotRequired[str]
    NestingLevel: NotRequired[NestingLevelValueType]
    ExtractDocId: NotRequired[bool]
    DocsToInvestigate: NotRequired[int]
    KmsKeyId: NotRequired[str]
    SecretsManagerAccessRoleArn: NotRequired[str]
    SecretsManagerSecretId: NotRequired[str]
    UseUpdateLookUp: NotRequired[bool]
    ReplicateShardCollections: NotRequired[bool]

class DynamoDbSettingsTypeDef(TypedDict):
    ServiceAccessRoleArn: str

class ElasticsearchSettingsTypeDef(TypedDict):
    ServiceAccessRoleArn: str
    EndpointUri: str
    FullLoadErrorPercentage: NotRequired[int]
    ErrorRetryDuration: NotRequired[int]
    UseNewMappingType: NotRequired[bool]

class GcpMySQLSettingsTypeDef(TypedDict):
    AfterConnectScript: NotRequired[str]
    CleanSourceMetadataOnMismatch: NotRequired[bool]
    DatabaseName: NotRequired[str]
    EventsPollInterval: NotRequired[int]
    TargetDbType: NotRequired[TargetDbTypeType]
    MaxFileSize: NotRequired[int]
    ParallelLoadThreads: NotRequired[int]
    Password: NotRequired[str]
    Port: NotRequired[int]
    ServerName: NotRequired[str]
    ServerTimezone: NotRequired[str]
    Username: NotRequired[str]
    SecretsManagerAccessRoleArn: NotRequired[str]
    SecretsManagerSecretId: NotRequired[str]

class IBMDb2SettingsTypeDef(TypedDict):
    DatabaseName: NotRequired[str]
    Password: NotRequired[str]
    Port: NotRequired[int]
    ServerName: NotRequired[str]
    SetDataCaptureChanges: NotRequired[bool]
    CurrentLsn: NotRequired[str]
    MaxKBytesPerRead: NotRequired[int]
    Username: NotRequired[str]
    SecretsManagerAccessRoleArn: NotRequired[str]
    SecretsManagerSecretId: NotRequired[str]
    LoadTimeout: NotRequired[int]
    WriteBufferSize: NotRequired[int]
    MaxFileSize: NotRequired[int]
    KeepCsvFiles: NotRequired[bool]

class KafkaSettingsTypeDef(TypedDict):
    Broker: NotRequired[str]
    Topic: NotRequired[str]
    MessageFormat: NotRequired[MessageFormatValueType]
    IncludeTransactionDetails: NotRequired[bool]
    IncludePartitionValue: NotRequired[bool]
    PartitionIncludeSchemaTable: NotRequired[bool]
    IncludeTableAlterOperations: NotRequired[bool]
    IncludeControlDetails: NotRequired[bool]
    MessageMaxBytes: NotRequired[int]
    IncludeNullAndEmpty: NotRequired[bool]
    SecurityProtocol: NotRequired[KafkaSecurityProtocolType]
    SslClientCertificateArn: NotRequired[str]
    SslClientKeyArn: NotRequired[str]
    SslClientKeyPassword: NotRequired[str]
    SslCaCertificateArn: NotRequired[str]
    SaslUsername: NotRequired[str]
    SaslPassword: NotRequired[str]
    NoHexPrefix: NotRequired[bool]
    SaslMechanism: NotRequired[KafkaSaslMechanismType]
    SslEndpointIdentificationAlgorithm: NotRequired[KafkaSslEndpointIdentificationAlgorithmType]
    UseLargeIntegerValue: NotRequired[bool]

class KinesisSettingsTypeDef(TypedDict):
    StreamArn: NotRequired[str]
    MessageFormat: NotRequired[MessageFormatValueType]
    ServiceAccessRoleArn: NotRequired[str]
    IncludeTransactionDetails: NotRequired[bool]
    IncludePartitionValue: NotRequired[bool]
    PartitionIncludeSchemaTable: NotRequired[bool]
    IncludeTableAlterOperations: NotRequired[bool]
    IncludeControlDetails: NotRequired[bool]
    IncludeNullAndEmpty: NotRequired[bool]
    NoHexPrefix: NotRequired[bool]
    UseLargeIntegerValue: NotRequired[bool]

class MicrosoftSQLServerSettingsTypeDef(TypedDict):
    Port: NotRequired[int]
    BcpPacketSize: NotRequired[int]
    DatabaseName: NotRequired[str]
    ControlTablesFileGroup: NotRequired[str]
    Password: NotRequired[str]
    QuerySingleAlwaysOnNode: NotRequired[bool]
    ReadBackupOnly: NotRequired[bool]
    SafeguardPolicy: NotRequired[SafeguardPolicyType]
    ServerName: NotRequired[str]
    Username: NotRequired[str]
    UseBcpFullLoad: NotRequired[bool]
    UseThirdPartyBackupDevice: NotRequired[bool]
    SecretsManagerAccessRoleArn: NotRequired[str]
    SecretsManagerSecretId: NotRequired[str]
    TrimSpaceInChar: NotRequired[bool]
    TlogAccessMode: NotRequired[TlogAccessModeType]
    ForceLobLookup: NotRequired[bool]
    AuthenticationMethod: NotRequired[SqlServerAuthenticationMethodType]

class MongoDbSettingsTypeDef(TypedDict):
    Username: NotRequired[str]
    Password: NotRequired[str]
    ServerName: NotRequired[str]
    Port: NotRequired[int]
    DatabaseName: NotRequired[str]
    AuthType: NotRequired[AuthTypeValueType]
    AuthMechanism: NotRequired[AuthMechanismValueType]
    NestingLevel: NotRequired[NestingLevelValueType]
    ExtractDocId: NotRequired[str]
    DocsToInvestigate: NotRequired[str]
    AuthSource: NotRequired[str]
    KmsKeyId: NotRequired[str]
    SecretsManagerAccessRoleArn: NotRequired[str]
    SecretsManagerSecretId: NotRequired[str]
    UseUpdateLookUp: NotRequired[bool]
    ReplicateShardCollections: NotRequired[bool]

class MySQLSettingsTypeDef(TypedDict):
    AfterConnectScript: NotRequired[str]
    CleanSourceMetadataOnMismatch: NotRequired[bool]
    DatabaseName: NotRequired[str]
    EventsPollInterval: NotRequired[int]
    TargetDbType: NotRequired[TargetDbTypeType]
    MaxFileSize: NotRequired[int]
    ParallelLoadThreads: NotRequired[int]
    Password: NotRequired[str]
    Port: NotRequired[int]
    ServerName: NotRequired[str]
    ServerTimezone: NotRequired[str]
    Username: NotRequired[str]
    SecretsManagerAccessRoleArn: NotRequired[str]
    SecretsManagerSecretId: NotRequired[str]
    ExecuteTimeout: NotRequired[int]

class NeptuneSettingsTypeDef(TypedDict):
    S3BucketName: str
    S3BucketFolder: str
    ServiceAccessRoleArn: NotRequired[str]
    ErrorRetryDuration: NotRequired[int]
    MaxFileSize: NotRequired[int]
    MaxRetryCount: NotRequired[int]
    IamAuthEnabled: NotRequired[bool]

class PostgreSQLSettingsTypeDef(TypedDict):
    AfterConnectScript: NotRequired[str]
    CaptureDdls: NotRequired[bool]
    MaxFileSize: NotRequired[int]
    DatabaseName: NotRequired[str]
    DdlArtifactsSchema: NotRequired[str]
    ExecuteTimeout: NotRequired[int]
    FailTasksOnLobTruncation: NotRequired[bool]
    HeartbeatEnable: NotRequired[bool]
    HeartbeatSchema: NotRequired[str]
    HeartbeatFrequency: NotRequired[int]
    Password: NotRequired[str]
    Port: NotRequired[int]
    ServerName: NotRequired[str]
    Username: NotRequired[str]
    SlotName: NotRequired[str]
    PluginName: NotRequired[PluginNameValueType]
    SecretsManagerAccessRoleArn: NotRequired[str]
    SecretsManagerSecretId: NotRequired[str]
    TrimSpaceInChar: NotRequired[bool]
    MapBooleanAsBoolean: NotRequired[bool]
    MapJsonbAsClob: NotRequired[bool]
    MapLongVarcharAs: NotRequired[LongVarcharMappingTypeType]
    DatabaseMode: NotRequired[DatabaseModeType]
    BabelfishDatabaseName: NotRequired[str]
    DisableUnicodeSourceFilter: NotRequired[bool]

class RedisSettingsTypeDef(TypedDict):
    ServerName: str
    Port: int
    SslSecurityProtocol: NotRequired[SslSecurityProtocolValueType]
    AuthType: NotRequired[RedisAuthTypeValueType]
    AuthUserName: NotRequired[str]
    AuthPassword: NotRequired[str]
    SslCaCertificateArn: NotRequired[str]

class RedshiftSettingsTypeDef(TypedDict):
    AcceptAnyDate: NotRequired[bool]
    AfterConnectScript: NotRequired[str]
    BucketFolder: NotRequired[str]
    BucketName: NotRequired[str]
    CaseSensitiveNames: NotRequired[bool]
    CompUpdate: NotRequired[bool]
    ConnectionTimeout: NotRequired[int]
    DatabaseName: NotRequired[str]
    DateFormat: NotRequired[str]
    EmptyAsNull: NotRequired[bool]
    EncryptionMode: NotRequired[EncryptionModeValueType]
    ExplicitIds: NotRequired[bool]
    FileTransferUploadStreams: NotRequired[int]
    LoadTimeout: NotRequired[int]
    MaxFileSize: NotRequired[int]
    Password: NotRequired[str]
    Port: NotRequired[int]
    RemoveQuotes: NotRequired[bool]
    ReplaceInvalidChars: NotRequired[str]
    ReplaceChars: NotRequired[str]
    ServerName: NotRequired[str]
    ServiceAccessRoleArn: NotRequired[str]
    ServerSideEncryptionKmsKeyId: NotRequired[str]
    TimeFormat: NotRequired[str]
    TrimBlanks: NotRequired[bool]
    TruncateColumns: NotRequired[bool]
    Username: NotRequired[str]
    WriteBufferSize: NotRequired[int]
    SecretsManagerAccessRoleArn: NotRequired[str]
    SecretsManagerSecretId: NotRequired[str]
    MapBooleanAsBoolean: NotRequired[bool]

class S3SettingsTypeDef(TypedDict):
    ServiceAccessRoleArn: NotRequired[str]
    ExternalTableDefinition: NotRequired[str]
    CsvRowDelimiter: NotRequired[str]
    CsvDelimiter: NotRequired[str]
    BucketFolder: NotRequired[str]
    BucketName: NotRequired[str]
    CompressionType: NotRequired[CompressionTypeValueType]
    EncryptionMode: NotRequired[EncryptionModeValueType]
    ServerSideEncryptionKmsKeyId: NotRequired[str]
    DataFormat: NotRequired[DataFormatValueType]
    EncodingType: NotRequired[EncodingTypeValueType]
    DictPageSizeLimit: NotRequired[int]
    RowGroupLength: NotRequired[int]
    DataPageSize: NotRequired[int]
    ParquetVersion: NotRequired[ParquetVersionValueType]
    EnableStatistics: NotRequired[bool]
    IncludeOpForFullLoad: NotRequired[bool]
    CdcInsertsOnly: NotRequired[bool]
    TimestampColumnName: NotRequired[str]
    ParquetTimestampInMillisecond: NotRequired[bool]
    CdcInsertsAndUpdates: NotRequired[bool]
    DatePartitionEnabled: NotRequired[bool]
    DatePartitionSequence: NotRequired[DatePartitionSequenceValueType]
    DatePartitionDelimiter: NotRequired[DatePartitionDelimiterValueType]
    UseCsvNoSupValue: NotRequired[bool]
    CsvNoSupValue: NotRequired[str]
    PreserveTransactions: NotRequired[bool]
    CdcPath: NotRequired[str]
    UseTaskStartTimeForFullLoadTimestamp: NotRequired[bool]
    CannedAclForObjects: NotRequired[CannedAclForObjectsValueType]
    AddColumnName: NotRequired[bool]
    CdcMaxBatchInterval: NotRequired[int]
    CdcMinFileSize: NotRequired[int]
    CsvNullValue: NotRequired[str]
    IgnoreHeaderRows: NotRequired[int]
    MaxFileSize: NotRequired[int]
    Rfc4180: NotRequired[bool]
    DatePartitionTimezone: NotRequired[str]
    AddTrailingPaddingCharacter: NotRequired[bool]
    ExpectedBucketOwner: NotRequired[str]
    GlueCatalogGeneration: NotRequired[bool]

class SybaseSettingsTypeDef(TypedDict):
    DatabaseName: NotRequired[str]
    Password: NotRequired[str]
    Port: NotRequired[int]
    ServerName: NotRequired[str]
    Username: NotRequired[str]
    SecretsManagerAccessRoleArn: NotRequired[str]
    SecretsManagerSecretId: NotRequired[str]

class TimestreamSettingsTypeDef(TypedDict):
    DatabaseName: str
    MemoryDuration: int
    MagneticDuration: int
    CdcInsertsAndUpdates: NotRequired[bool]
    EnableMagneticStoreWrites: NotRequired[bool]

class EventSubscriptionTypeDef(TypedDict):
    CustomerAwsId: NotRequired[str]
    CustSubscriptionId: NotRequired[str]
    SnsTopicArn: NotRequired[str]
    Status: NotRequired[str]
    SubscriptionCreationTime: NotRequired[str]
    SourceType: NotRequired[str]
    SourceIdsList: NotRequired[List[str]]
    EventCategoriesList: NotRequired[List[str]]
    Enabled: NotRequired[bool]

class CreateFleetAdvisorCollectorRequestTypeDef(TypedDict):
    CollectorName: str
    ServiceAccessRoleArn: str
    S3BucketName: str
    Description: NotRequired[str]

class InstanceProfileTypeDef(TypedDict):
    InstanceProfileArn: NotRequired[str]
    AvailabilityZone: NotRequired[str]
    KmsKeyArn: NotRequired[str]
    PubliclyAccessible: NotRequired[bool]
    NetworkType: NotRequired[str]
    InstanceProfileName: NotRequired[str]
    Description: NotRequired[str]
    InstanceProfileCreationTime: NotRequired[datetime]
    SubnetGroupIdentifier: NotRequired[str]
    VpcSecurityGroups: NotRequired[List[str]]

class DataProviderDescriptorDefinitionTypeDef(TypedDict):
    DataProviderIdentifier: str
    SecretsManagerSecretId: NotRequired[str]
    SecretsManagerAccessRoleArn: NotRequired[str]

class SCApplicationAttributesTypeDef(TypedDict):
    S3BucketPath: NotRequired[str]
    S3BucketRoleArn: NotRequired[str]

class KerberosAuthenticationSettingsTypeDef(TypedDict):
    KeyCacheSecretId: NotRequired[str]
    KeyCacheSecretIamArn: NotRequired[str]
    Krb5FileContents: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class DataMigrationSettingsTypeDef(TypedDict):
    NumberOfJobs: NotRequired[int]
    CloudwatchLogsEnabled: NotRequired[bool]
    SelectionRules: NotRequired[str]

class DataMigrationStatisticsTypeDef(TypedDict):
    TablesLoaded: NotRequired[int]
    ElapsedTimeMillis: NotRequired[int]
    TablesLoading: NotRequired[int]
    FullLoadPercentage: NotRequired[int]
    CDCLatency: NotRequired[int]
    TablesQueued: NotRequired[int]
    TablesErrored: NotRequired[int]
    StartTime: NotRequired[datetime]
    StopTime: NotRequired[datetime]

class SourceDataSettingOutputTypeDef(TypedDict):
    CDCStartPosition: NotRequired[str]
    CDCStartTime: NotRequired[datetime]
    CDCStopTime: NotRequired[datetime]
    SlotName: NotRequired[str]

class DataProviderDescriptorTypeDef(TypedDict):
    SecretsManagerSecretId: NotRequired[str]
    SecretsManagerAccessRoleArn: NotRequired[str]
    DataProviderName: NotRequired[str]
    DataProviderArn: NotRequired[str]

class DocDbDataProviderSettingsTypeDef(TypedDict):
    ServerName: NotRequired[str]
    Port: NotRequired[int]
    DatabaseName: NotRequired[str]
    SslMode: NotRequired[DmsSslModeValueType]
    CertificateArn: NotRequired[str]

class IbmDb2LuwDataProviderSettingsTypeDef(TypedDict):
    ServerName: NotRequired[str]
    Port: NotRequired[int]
    DatabaseName: NotRequired[str]
    SslMode: NotRequired[DmsSslModeValueType]
    CertificateArn: NotRequired[str]

class IbmDb2zOsDataProviderSettingsTypeDef(TypedDict):
    ServerName: NotRequired[str]
    Port: NotRequired[int]
    DatabaseName: NotRequired[str]
    SslMode: NotRequired[DmsSslModeValueType]
    CertificateArn: NotRequired[str]

class MariaDbDataProviderSettingsTypeDef(TypedDict):
    ServerName: NotRequired[str]
    Port: NotRequired[int]
    SslMode: NotRequired[DmsSslModeValueType]
    CertificateArn: NotRequired[str]

class MicrosoftSqlServerDataProviderSettingsTypeDef(TypedDict):
    ServerName: NotRequired[str]
    Port: NotRequired[int]
    DatabaseName: NotRequired[str]
    SslMode: NotRequired[DmsSslModeValueType]
    CertificateArn: NotRequired[str]

class MongoDbDataProviderSettingsTypeDef(TypedDict):
    ServerName: NotRequired[str]
    Port: NotRequired[int]
    DatabaseName: NotRequired[str]
    SslMode: NotRequired[DmsSslModeValueType]
    CertificateArn: NotRequired[str]
    AuthType: NotRequired[AuthTypeValueType]
    AuthSource: NotRequired[str]
    AuthMechanism: NotRequired[AuthMechanismValueType]

class MySqlDataProviderSettingsTypeDef(TypedDict):
    ServerName: NotRequired[str]
    Port: NotRequired[int]
    SslMode: NotRequired[DmsSslModeValueType]
    CertificateArn: NotRequired[str]

class OracleDataProviderSettingsTypeDef(TypedDict):
    ServerName: NotRequired[str]
    Port: NotRequired[int]
    DatabaseName: NotRequired[str]
    SslMode: NotRequired[DmsSslModeValueType]
    CertificateArn: NotRequired[str]
    AsmServer: NotRequired[str]
    SecretsManagerOracleAsmSecretId: NotRequired[str]
    SecretsManagerOracleAsmAccessRoleArn: NotRequired[str]
    SecretsManagerSecurityDbEncryptionSecretId: NotRequired[str]
    SecretsManagerSecurityDbEncryptionAccessRoleArn: NotRequired[str]

class PostgreSqlDataProviderSettingsTypeDef(TypedDict):
    ServerName: NotRequired[str]
    Port: NotRequired[int]
    DatabaseName: NotRequired[str]
    SslMode: NotRequired[DmsSslModeValueType]
    CertificateArn: NotRequired[str]

class RedshiftDataProviderSettingsTypeDef(TypedDict):
    ServerName: NotRequired[str]
    Port: NotRequired[int]
    DatabaseName: NotRequired[str]

class DatabaseInstanceSoftwareDetailsResponseTypeDef(TypedDict):
    Engine: NotRequired[str]
    EngineVersion: NotRequired[str]
    EngineEdition: NotRequired[str]
    ServicePack: NotRequired[str]
    SupportLevel: NotRequired[str]
    OsArchitecture: NotRequired[int]
    Tooltip: NotRequired[str]

class ServerShortInfoResponseTypeDef(TypedDict):
    ServerId: NotRequired[str]
    IpAddress: NotRequired[str]
    ServerName: NotRequired[str]

class DatabaseShortInfoResponseTypeDef(TypedDict):
    DatabaseId: NotRequired[str]
    DatabaseName: NotRequired[str]
    DatabaseIpAddress: NotRequired[str]
    DatabaseEngine: NotRequired[str]

class DefaultErrorDetailsTypeDef(TypedDict):
    Message: NotRequired[str]

class DeleteCertificateMessageTypeDef(TypedDict):
    CertificateArn: str

class DeleteCollectorRequestTypeDef(TypedDict):
    CollectorReferencedId: str

class DeleteConnectionMessageTypeDef(TypedDict):
    EndpointArn: str
    ReplicationInstanceArn: str

class DeleteDataMigrationMessageTypeDef(TypedDict):
    DataMigrationIdentifier: str

class DeleteDataProviderMessageTypeDef(TypedDict):
    DataProviderIdentifier: str

class DeleteEndpointMessageTypeDef(TypedDict):
    EndpointArn: str

class DeleteEventSubscriptionMessageTypeDef(TypedDict):
    SubscriptionName: str

class DeleteFleetAdvisorDatabasesRequestTypeDef(TypedDict):
    DatabaseIds: Sequence[str]

class DeleteInstanceProfileMessageTypeDef(TypedDict):
    InstanceProfileIdentifier: str

class DeleteMigrationProjectMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str

class DeleteReplicationConfigMessageTypeDef(TypedDict):
    ReplicationConfigArn: str

class DeleteReplicationInstanceMessageTypeDef(TypedDict):
    ReplicationInstanceArn: str

class DeleteReplicationSubnetGroupMessageTypeDef(TypedDict):
    ReplicationSubnetGroupIdentifier: str

class DeleteReplicationTaskAssessmentRunMessageTypeDef(TypedDict):
    ReplicationTaskAssessmentRunArn: str

class DeleteReplicationTaskMessageTypeDef(TypedDict):
    ReplicationTaskArn: str

class DescribeApplicableIndividualAssessmentsMessageTypeDef(TypedDict):
    ReplicationTaskArn: NotRequired[str]
    ReplicationInstanceArn: NotRequired[str]
    ReplicationConfigArn: NotRequired[str]
    SourceEngineName: NotRequired[str]
    TargetEngineName: NotRequired[str]
    MigrationType: NotRequired[MigrationTypeValueType]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class FilterTypeDef(TypedDict):
    Name: str
    Values: Sequence[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeConversionConfigurationMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str

class DescribeEndpointSettingsMessageTypeDef(TypedDict):
    EngineName: str
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

EndpointSettingTypeDef = TypedDict(
    "EndpointSettingTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[EndpointSettingTypeValueType],
        "EnumValues": NotRequired[List[str]],
        "Sensitive": NotRequired[bool],
        "Units": NotRequired[str],
        "Applicability": NotRequired[str],
        "IntValueMin": NotRequired[int],
        "IntValueMax": NotRequired[int],
        "DefaultValue": NotRequired[str],
    },
)

class SupportedEndpointTypeTypeDef(TypedDict):
    EngineName: NotRequired[str]
    SupportsCDC: NotRequired[bool]
    EndpointType: NotRequired[ReplicationEndpointTypeValueType]
    ReplicationInstanceEngineMinimumVersion: NotRequired[str]
    EngineDisplayName: NotRequired[str]

class DescribeEngineVersionsMessageTypeDef(TypedDict):
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class EngineVersionTypeDef(TypedDict):
    Version: NotRequired[str]
    Lifecycle: NotRequired[str]
    ReleaseStatus: NotRequired[ReleaseStatusValuesType]
    LaunchDate: NotRequired[datetime]
    AutoUpgradeDate: NotRequired[datetime]
    DeprecationDate: NotRequired[datetime]
    ForceUpgradeDate: NotRequired[datetime]
    AvailableUpgrades: NotRequired[List[str]]

class EventCategoryGroupTypeDef(TypedDict):
    SourceType: NotRequired[str]
    EventCategories: NotRequired[List[str]]

class EventTypeDef(TypedDict):
    SourceIdentifier: NotRequired[str]
    SourceType: NotRequired[Literal["replication-instance"]]
    Message: NotRequired[str]
    EventCategories: NotRequired[List[str]]
    Date: NotRequired[datetime]

class DescribeFleetAdvisorLsaAnalysisRequestTypeDef(TypedDict):
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

class FleetAdvisorLsaAnalysisResponseTypeDef(TypedDict):
    LsaAnalysisId: NotRequired[str]
    Status: NotRequired[str]

class FleetAdvisorSchemaObjectResponseTypeDef(TypedDict):
    SchemaId: NotRequired[str]
    ObjectType: NotRequired[str]
    NumberOfObjects: NotRequired[int]
    CodeLineCount: NotRequired[int]
    CodeSize: NotRequired[int]

class DescribeOrderableReplicationInstancesMessageTypeDef(TypedDict):
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class OrderableReplicationInstanceTypeDef(TypedDict):
    EngineVersion: NotRequired[str]
    ReplicationInstanceClass: NotRequired[str]
    StorageType: NotRequired[str]
    MinAllocatedStorage: NotRequired[int]
    MaxAllocatedStorage: NotRequired[int]
    DefaultAllocatedStorage: NotRequired[int]
    IncludedAllocatedStorage: NotRequired[int]
    AvailabilityZones: NotRequired[List[str]]
    ReleaseStatus: NotRequired[ReleaseStatusValuesType]

LimitationTypeDef = TypedDict(
    "LimitationTypeDef",
    {
        "DatabaseId": NotRequired[str],
        "EngineName": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Impact": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class DescribeRefreshSchemasStatusMessageTypeDef(TypedDict):
    EndpointArn: str

class RefreshSchemasStatusTypeDef(TypedDict):
    EndpointArn: NotRequired[str]
    ReplicationInstanceArn: NotRequired[str]
    Status: NotRequired[RefreshSchemasStatusTypeValueType]
    LastRefreshDate: NotRequired[datetime]
    LastFailureMessage: NotRequired[str]

class DescribeReplicationInstanceTaskLogsMessageTypeDef(TypedDict):
    ReplicationInstanceArn: str
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class ReplicationInstanceTaskLogTypeDef(TypedDict):
    ReplicationTaskName: NotRequired[str]
    ReplicationTaskArn: NotRequired[str]
    ReplicationInstanceTaskLogSize: NotRequired[int]

class TableStatisticsTypeDef(TypedDict):
    SchemaName: NotRequired[str]
    TableName: NotRequired[str]
    Inserts: NotRequired[int]
    Deletes: NotRequired[int]
    Updates: NotRequired[int]
    Ddls: NotRequired[int]
    AppliedInserts: NotRequired[int]
    AppliedDeletes: NotRequired[int]
    AppliedUpdates: NotRequired[int]
    AppliedDdls: NotRequired[int]
    FullLoadRows: NotRequired[int]
    FullLoadCondtnlChkFailedRows: NotRequired[int]
    FullLoadErrorRows: NotRequired[int]
    FullLoadStartTime: NotRequired[datetime]
    FullLoadEndTime: NotRequired[datetime]
    FullLoadReloaded: NotRequired[bool]
    LastUpdateTime: NotRequired[datetime]
    TableState: NotRequired[str]
    ValidationPendingRecords: NotRequired[int]
    ValidationFailedRecords: NotRequired[int]
    ValidationSuspendedRecords: NotRequired[int]
    ValidationState: NotRequired[str]
    ValidationStateDetails: NotRequired[str]

class DescribeReplicationTaskAssessmentResultsMessageTypeDef(TypedDict):
    ReplicationTaskArn: NotRequired[str]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class ReplicationTaskAssessmentResultTypeDef(TypedDict):
    ReplicationTaskIdentifier: NotRequired[str]
    ReplicationTaskArn: NotRequired[str]
    ReplicationTaskLastAssessmentDate: NotRequired[datetime]
    AssessmentStatus: NotRequired[str]
    AssessmentResultsFile: NotRequired[str]
    AssessmentResults: NotRequired[str]
    S3ObjectUrl: NotRequired[str]

class ReplicationTaskIndividualAssessmentTypeDef(TypedDict):
    ReplicationTaskIndividualAssessmentArn: NotRequired[str]
    ReplicationTaskAssessmentRunArn: NotRequired[str]
    IndividualAssessmentName: NotRequired[str]
    Status: NotRequired[str]
    ReplicationTaskIndividualAssessmentStartDate: NotRequired[datetime]

class DescribeSchemasMessageTypeDef(TypedDict):
    EndpointArn: str
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class OracleSettingsOutputTypeDef(TypedDict):
    AddSupplementalLogging: NotRequired[bool]
    ArchivedLogDestId: NotRequired[int]
    AdditionalArchivedLogDestId: NotRequired[int]
    ExtraArchivedLogDestIds: NotRequired[List[int]]
    AllowSelectNestedTables: NotRequired[bool]
    ParallelAsmReadThreads: NotRequired[int]
    ReadAheadBlocks: NotRequired[int]
    AccessAlternateDirectly: NotRequired[bool]
    UseAlternateFolderForOnline: NotRequired[bool]
    OraclePathPrefix: NotRequired[str]
    UsePathPrefix: NotRequired[str]
    ReplacePathPrefix: NotRequired[bool]
    EnableHomogenousTablespace: NotRequired[bool]
    DirectPathNoLog: NotRequired[bool]
    ArchivedLogsOnly: NotRequired[bool]
    AsmPassword: NotRequired[str]
    AsmServer: NotRequired[str]
    AsmUser: NotRequired[str]
    CharLengthSemantics: NotRequired[CharLengthSemanticsType]
    DatabaseName: NotRequired[str]
    DirectPathParallelLoad: NotRequired[bool]
    FailTasksOnLobTruncation: NotRequired[bool]
    NumberDatatypeScale: NotRequired[int]
    Password: NotRequired[str]
    Port: NotRequired[int]
    ReadTableSpaceName: NotRequired[bool]
    RetryInterval: NotRequired[int]
    SecurityDbEncryption: NotRequired[str]
    SecurityDbEncryptionName: NotRequired[str]
    ServerName: NotRequired[str]
    SpatialDataOptionToGeoJsonFunctionName: NotRequired[str]
    StandbyDelayTime: NotRequired[int]
    Username: NotRequired[str]
    UseBFile: NotRequired[bool]
    UseDirectPathFullLoad: NotRequired[bool]
    UseLogminerReader: NotRequired[bool]
    SecretsManagerAccessRoleArn: NotRequired[str]
    SecretsManagerSecretId: NotRequired[str]
    SecretsManagerOracleAsmAccessRoleArn: NotRequired[str]
    SecretsManagerOracleAsmSecretId: NotRequired[str]
    TrimSpaceInChar: NotRequired[bool]
    ConvertTimestampWithZoneToUTC: NotRequired[bool]
    OpenTransactionWindow: NotRequired[int]
    AuthenticationMethod: NotRequired[OracleAuthenticationMethodType]

class ExportMetadataModelAssessmentMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    SelectionRules: str
    FileName: NotRequired[str]
    AssessmentReportTypes: NotRequired[Sequence[AssessmentReportTypeType]]

class ExportMetadataModelAssessmentResultEntryTypeDef(TypedDict):
    S3ObjectKey: NotRequired[str]
    ObjectURL: NotRequired[str]

class ExportSqlDetailsTypeDef(TypedDict):
    S3ObjectKey: NotRequired[str]
    ObjectURL: NotRequired[str]

class ListTagsForResourceMessageTypeDef(TypedDict):
    ResourceArn: NotRequired[str]
    ResourceArnList: NotRequired[Sequence[str]]

class ModifyConversionConfigurationMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    ConversionConfiguration: str

class ModifyEventSubscriptionMessageTypeDef(TypedDict):
    SubscriptionName: str
    SnsTopicArn: NotRequired[str]
    SourceType: NotRequired[str]
    EventCategories: NotRequired[Sequence[str]]
    Enabled: NotRequired[bool]

class ModifyInstanceProfileMessageTypeDef(TypedDict):
    InstanceProfileIdentifier: str
    AvailabilityZone: NotRequired[str]
    KmsKeyArn: NotRequired[str]
    PubliclyAccessible: NotRequired[bool]
    NetworkType: NotRequired[str]
    InstanceProfileName: NotRequired[str]
    Description: NotRequired[str]
    SubnetGroupIdentifier: NotRequired[str]
    VpcSecurityGroups: NotRequired[Sequence[str]]

class ModifyReplicationSubnetGroupMessageTypeDef(TypedDict):
    ReplicationSubnetGroupIdentifier: str
    SubnetIds: Sequence[str]
    ReplicationSubnetGroupDescription: NotRequired[str]

class MoveReplicationTaskMessageTypeDef(TypedDict):
    ReplicationTaskArn: str
    TargetReplicationInstanceArn: str

class OracleSettingsTypeDef(TypedDict):
    AddSupplementalLogging: NotRequired[bool]
    ArchivedLogDestId: NotRequired[int]
    AdditionalArchivedLogDestId: NotRequired[int]
    ExtraArchivedLogDestIds: NotRequired[Sequence[int]]
    AllowSelectNestedTables: NotRequired[bool]
    ParallelAsmReadThreads: NotRequired[int]
    ReadAheadBlocks: NotRequired[int]
    AccessAlternateDirectly: NotRequired[bool]
    UseAlternateFolderForOnline: NotRequired[bool]
    OraclePathPrefix: NotRequired[str]
    UsePathPrefix: NotRequired[str]
    ReplacePathPrefix: NotRequired[bool]
    EnableHomogenousTablespace: NotRequired[bool]
    DirectPathNoLog: NotRequired[bool]
    ArchivedLogsOnly: NotRequired[bool]
    AsmPassword: NotRequired[str]
    AsmServer: NotRequired[str]
    AsmUser: NotRequired[str]
    CharLengthSemantics: NotRequired[CharLengthSemanticsType]
    DatabaseName: NotRequired[str]
    DirectPathParallelLoad: NotRequired[bool]
    FailTasksOnLobTruncation: NotRequired[bool]
    NumberDatatypeScale: NotRequired[int]
    Password: NotRequired[str]
    Port: NotRequired[int]
    ReadTableSpaceName: NotRequired[bool]
    RetryInterval: NotRequired[int]
    SecurityDbEncryption: NotRequired[str]
    SecurityDbEncryptionName: NotRequired[str]
    ServerName: NotRequired[str]
    SpatialDataOptionToGeoJsonFunctionName: NotRequired[str]
    StandbyDelayTime: NotRequired[int]
    Username: NotRequired[str]
    UseBFile: NotRequired[bool]
    UseDirectPathFullLoad: NotRequired[bool]
    UseLogminerReader: NotRequired[bool]
    SecretsManagerAccessRoleArn: NotRequired[str]
    SecretsManagerSecretId: NotRequired[str]
    SecretsManagerOracleAsmAccessRoleArn: NotRequired[str]
    SecretsManagerOracleAsmSecretId: NotRequired[str]
    TrimSpaceInChar: NotRequired[bool]
    ConvertTimestampWithZoneToUTC: NotRequired[bool]
    OpenTransactionWindow: NotRequired[int]
    AuthenticationMethod: NotRequired[OracleAuthenticationMethodType]

class PendingMaintenanceActionTypeDef(TypedDict):
    Action: NotRequired[str]
    AutoAppliedAfterDate: NotRequired[datetime]
    ForcedApplyDate: NotRequired[datetime]
    OptInStatus: NotRequired[str]
    CurrentApplyDate: NotRequired[datetime]
    Description: NotRequired[str]

class ReplicationTaskAssessmentRunProgressTypeDef(TypedDict):
    IndividualAssessmentCount: NotRequired[int]
    IndividualAssessmentCompletedCount: NotRequired[int]

ReplicationTaskAssessmentRunResultStatisticTypeDef = TypedDict(
    "ReplicationTaskAssessmentRunResultStatisticTypeDef",
    {
        "Passed": NotRequired[int],
        "Failed": NotRequired[int],
        "Error": NotRequired[int],
        "Warning": NotRequired[int],
        "Cancelled": NotRequired[int],
        "Skipped": NotRequired[int],
    },
)

class ProvisionDataTypeDef(TypedDict):
    ProvisionState: NotRequired[str]
    ProvisionedCapacityUnits: NotRequired[int]
    DateProvisioned: NotRequired[datetime]
    IsNewProvisioningAvailable: NotRequired[bool]
    DateNewProvisioningDataAvailable: NotRequired[datetime]
    ReasonForNewProvisioningData: NotRequired[str]

class RdsConfigurationTypeDef(TypedDict):
    EngineEdition: NotRequired[str]
    InstanceType: NotRequired[str]
    InstanceVcpu: NotRequired[float]
    InstanceMemory: NotRequired[float]
    StorageType: NotRequired[str]
    StorageSize: NotRequired[int]
    StorageIops: NotRequired[int]
    DeploymentOption: NotRequired[str]
    EngineVersion: NotRequired[str]

class RdsRequirementsTypeDef(TypedDict):
    EngineEdition: NotRequired[str]
    InstanceVcpu: NotRequired[float]
    InstanceMemory: NotRequired[float]
    StorageSize: NotRequired[int]
    StorageIops: NotRequired[int]
    DeploymentOption: NotRequired[str]
    EngineVersion: NotRequired[str]

class RebootReplicationInstanceMessageTypeDef(TypedDict):
    ReplicationInstanceArn: str
    ForceFailover: NotRequired[bool]
    ForcePlannedFailover: NotRequired[bool]

class RecommendationSettingsTypeDef(TypedDict):
    InstanceSizingType: str
    WorkloadType: str

class RefreshSchemasMessageTypeDef(TypedDict):
    EndpointArn: str
    ReplicationInstanceArn: str

class TableToReloadTypeDef(TypedDict):
    SchemaName: str
    TableName: str

class RemoveTagsFromResourceMessageTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class ReplicationPendingModifiedValuesTypeDef(TypedDict):
    ReplicationInstanceClass: NotRequired[str]
    AllocatedStorage: NotRequired[int]
    MultiAZ: NotRequired[bool]
    EngineVersion: NotRequired[str]
    NetworkType: NotRequired[str]

class VpcSecurityGroupMembershipTypeDef(TypedDict):
    VpcSecurityGroupId: NotRequired[str]
    Status: NotRequired[str]

class ReplicationStatsTypeDef(TypedDict):
    FullLoadProgressPercent: NotRequired[int]
    ElapsedTimeMillis: NotRequired[int]
    TablesLoaded: NotRequired[int]
    TablesLoading: NotRequired[int]
    TablesQueued: NotRequired[int]
    TablesErrored: NotRequired[int]
    FreshStartDate: NotRequired[datetime]
    StartDate: NotRequired[datetime]
    StopDate: NotRequired[datetime]
    FullLoadStartDate: NotRequired[datetime]
    FullLoadFinishDate: NotRequired[datetime]

class ReplicationTaskStatsTypeDef(TypedDict):
    FullLoadProgressPercent: NotRequired[int]
    ElapsedTimeMillis: NotRequired[int]
    TablesLoaded: NotRequired[int]
    TablesLoading: NotRequired[int]
    TablesQueued: NotRequired[int]
    TablesErrored: NotRequired[int]
    FreshStartDate: NotRequired[datetime]
    StartDate: NotRequired[datetime]
    StopDate: NotRequired[datetime]
    FullLoadStartDate: NotRequired[datetime]
    FullLoadFinishDate: NotRequired[datetime]

class SchemaShortInfoResponseTypeDef(TypedDict):
    SchemaId: NotRequired[str]
    SchemaName: NotRequired[str]
    DatabaseId: NotRequired[str]
    DatabaseName: NotRequired[str]
    DatabaseIpAddress: NotRequired[str]

class StartDataMigrationMessageTypeDef(TypedDict):
    DataMigrationIdentifier: str
    StartType: StartReplicationMigrationTypeValueType

class StartExtensionPackAssociationMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str

class StartMetadataModelAssessmentMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    SelectionRules: str

class StartMetadataModelConversionMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    SelectionRules: str

class StartMetadataModelExportAsScriptMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    SelectionRules: str
    Origin: OriginTypeValueType
    FileName: NotRequired[str]

class StartMetadataModelExportToTargetMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    SelectionRules: str
    OverwriteExtensionPack: NotRequired[bool]

class StartMetadataModelImportMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    SelectionRules: str
    Origin: OriginTypeValueType
    Refresh: NotRequired[bool]

class StartReplicationTaskAssessmentMessageTypeDef(TypedDict):
    ReplicationTaskArn: str

class StopDataMigrationMessageTypeDef(TypedDict):
    DataMigrationIdentifier: str

class StopReplicationMessageTypeDef(TypedDict):
    ReplicationConfigArn: str

class StopReplicationTaskMessageTypeDef(TypedDict):
    ReplicationTaskArn: str

class TestConnectionMessageTypeDef(TypedDict):
    ReplicationInstanceArn: str
    EndpointArn: str

class UpdateSubscriptionsToEventBridgeMessageTypeDef(TypedDict):
    ForceMove: NotRequired[bool]

class AddTagsToResourceMessageTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateEventSubscriptionMessageTypeDef(TypedDict):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: NotRequired[str]
    EventCategories: NotRequired[Sequence[str]]
    SourceIds: NotRequired[Sequence[str]]
    Enabled: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateInstanceProfileMessageTypeDef(TypedDict):
    AvailabilityZone: NotRequired[str]
    KmsKeyArn: NotRequired[str]
    PubliclyAccessible: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]
    NetworkType: NotRequired[str]
    InstanceProfileName: NotRequired[str]
    Description: NotRequired[str]
    SubnetGroupIdentifier: NotRequired[str]
    VpcSecurityGroups: NotRequired[Sequence[str]]

class CreateReplicationSubnetGroupMessageTypeDef(TypedDict):
    ReplicationSubnetGroupIdentifier: str
    ReplicationSubnetGroupDescription: str
    SubnetIds: Sequence[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class StartReplicationTaskAssessmentRunMessageTypeDef(TypedDict):
    ReplicationTaskArn: str
    ServiceAccessRoleArn: str
    ResultLocationBucket: str
    AssessmentRunName: str
    ResultLocationFolder: NotRequired[str]
    ResultEncryptionMode: NotRequired[str]
    ResultKmsKeyArn: NotRequired[str]
    IncludeOnly: NotRequired[Sequence[str]]
    Exclude: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateFleetAdvisorCollectorResponseTypeDef(TypedDict):
    CollectorReferencedId: str
    CollectorName: str
    Description: str
    ServiceAccessRoleArn: str
    S3BucketName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFleetAdvisorDatabasesResponseTypeDef(TypedDict):
    DatabaseIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountAttributesResponseTypeDef(TypedDict):
    AccountQuotas: List[AccountQuotaTypeDef]
    UniqueAccountIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicableIndividualAssessmentsResponseTypeDef(TypedDict):
    IndividualAssessmentNames: List[str]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConversionConfigurationResponseTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    ConversionConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSchemasResponseTypeDef(TypedDict):
    Marker: str
    Schemas: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyConversionConfigurationResponseTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReloadReplicationTablesResponseTypeDef(TypedDict):
    ReplicationConfigArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReloadTablesResponseTypeDef(TypedDict):
    ReplicationTaskArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RunFleetAdvisorLsaAnalysisResponseTypeDef(TypedDict):
    LsaAnalysisId: str
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartExtensionPackAssociationResponseTypeDef(TypedDict):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMetadataModelAssessmentResponseTypeDef(TypedDict):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMetadataModelConversionResponseTypeDef(TypedDict):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMetadataModelExportAsScriptResponseTypeDef(TypedDict):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMetadataModelExportToTargetResponseTypeDef(TypedDict):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMetadataModelImportResponseTypeDef(TypedDict):
    RequestIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSubscriptionsToEventBridgeResponseTypeDef(TypedDict):
    Result: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubnetTypeDef(TypedDict):
    SubnetIdentifier: NotRequired[str]
    SubnetAvailabilityZone: NotRequired[AvailabilityZoneTypeDef]
    SubnetStatus: NotRequired[str]

class BatchStartRecommendationsResponseTypeDef(TypedDict):
    ErrorEntries: List[BatchStartRecommendationsErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportCertificateMessageTypeDef(TypedDict):
    CertificateIdentifier: str
    CertificatePem: NotRequired[str]
    CertificateWallet: NotRequired[BlobTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class DeleteCertificateResponseTypeDef(TypedDict):
    Certificate: CertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCertificatesResponseTypeDef(TypedDict):
    Marker: str
    Certificates: List[CertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportCertificateResponseTypeDef(TypedDict):
    Certificate: CertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CollectorResponseTypeDef(TypedDict):
    CollectorReferencedId: NotRequired[str]
    CollectorName: NotRequired[str]
    CollectorVersion: NotRequired[str]
    VersionStatus: NotRequired[VersionStatusType]
    Description: NotRequired[str]
    S3BucketName: NotRequired[str]
    ServiceAccessRoleArn: NotRequired[str]
    CollectorHealthCheck: NotRequired[CollectorHealthCheckTypeDef]
    LastDataReceived: NotRequired[str]
    RegisteredDate: NotRequired[str]
    CreatedDate: NotRequired[str]
    ModifiedDate: NotRequired[str]
    InventoryData: NotRequired[InventoryDataTypeDef]

class ReplicationConfigTypeDef(TypedDict):
    ReplicationConfigIdentifier: NotRequired[str]
    ReplicationConfigArn: NotRequired[str]
    SourceEndpointArn: NotRequired[str]
    TargetEndpointArn: NotRequired[str]
    ReplicationType: NotRequired[MigrationTypeValueType]
    ComputeConfig: NotRequired[ComputeConfigOutputTypeDef]
    ReplicationSettings: NotRequired[str]
    SupplementalSettings: NotRequired[str]
    TableMappings: NotRequired[str]
    ReplicationConfigCreateTime: NotRequired[datetime]
    ReplicationConfigUpdateTime: NotRequired[datetime]

ComputeConfigUnionTypeDef = Union[ComputeConfigTypeDef, ComputeConfigOutputTypeDef]

class DeleteConnectionResponseTypeDef(TypedDict):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectionsResponseTypeDef(TypedDict):
    Marker: str
    Connections: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TestConnectionResponseTypeDef(TypedDict):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventSubscriptionResponseTypeDef(TypedDict):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEventSubscriptionResponseTypeDef(TypedDict):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventSubscriptionsResponseTypeDef(TypedDict):
    Marker: str
    EventSubscriptionsList: List[EventSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyEventSubscriptionResponseTypeDef(TypedDict):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceProfileResponseTypeDef(TypedDict):
    InstanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInstanceProfileResponseTypeDef(TypedDict):
    InstanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInstanceProfilesResponseTypeDef(TypedDict):
    Marker: str
    InstanceProfiles: List[InstanceProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyInstanceProfileResponseTypeDef(TypedDict):
    InstanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMigrationProjectMessageTypeDef(TypedDict):
    SourceDataProviderDescriptors: Sequence[DataProviderDescriptorDefinitionTypeDef]
    TargetDataProviderDescriptors: Sequence[DataProviderDescriptorDefinitionTypeDef]
    InstanceProfileIdentifier: str
    MigrationProjectName: NotRequired[str]
    TransformationRules: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    SchemaConversionApplicationAttributes: NotRequired[SCApplicationAttributesTypeDef]

class ModifyMigrationProjectMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    MigrationProjectName: NotRequired[str]
    SourceDataProviderDescriptors: NotRequired[Sequence[DataProviderDescriptorDefinitionTypeDef]]
    TargetDataProviderDescriptors: NotRequired[Sequence[DataProviderDescriptorDefinitionTypeDef]]
    InstanceProfileIdentifier: NotRequired[str]
    TransformationRules: NotRequired[str]
    Description: NotRequired[str]
    SchemaConversionApplicationAttributes: NotRequired[SCApplicationAttributesTypeDef]

class CreateReplicationInstanceMessageTypeDef(TypedDict):
    ReplicationInstanceIdentifier: str
    ReplicationInstanceClass: str
    AllocatedStorage: NotRequired[int]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]
    AvailabilityZone: NotRequired[str]
    ReplicationSubnetGroupIdentifier: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    MultiAZ: NotRequired[bool]
    EngineVersion: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]
    KmsKeyId: NotRequired[str]
    PubliclyAccessible: NotRequired[bool]
    DnsNameServers: NotRequired[str]
    ResourceIdentifier: NotRequired[str]
    NetworkType: NotRequired[str]
    KerberosAuthenticationSettings: NotRequired[KerberosAuthenticationSettingsTypeDef]

class ModifyReplicationInstanceMessageTypeDef(TypedDict):
    ReplicationInstanceArn: str
    AllocatedStorage: NotRequired[int]
    ApplyImmediately: NotRequired[bool]
    ReplicationInstanceClass: NotRequired[str]
    VpcSecurityGroupIds: NotRequired[Sequence[str]]
    PreferredMaintenanceWindow: NotRequired[str]
    MultiAZ: NotRequired[bool]
    EngineVersion: NotRequired[str]
    AllowMajorVersionUpgrade: NotRequired[bool]
    AutoMinorVersionUpgrade: NotRequired[bool]
    ReplicationInstanceIdentifier: NotRequired[str]
    NetworkType: NotRequired[str]
    KerberosAuthenticationSettings: NotRequired[KerberosAuthenticationSettingsTypeDef]

class CreateReplicationTaskMessageTypeDef(TypedDict):
    ReplicationTaskIdentifier: str
    SourceEndpointArn: str
    TargetEndpointArn: str
    ReplicationInstanceArn: str
    MigrationType: MigrationTypeValueType
    TableMappings: str
    ReplicationTaskSettings: NotRequired[str]
    CdcStartTime: NotRequired[TimestampTypeDef]
    CdcStartPosition: NotRequired[str]
    CdcStopPosition: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    TaskData: NotRequired[str]
    ResourceIdentifier: NotRequired[str]

class ModifyReplicationTaskMessageTypeDef(TypedDict):
    ReplicationTaskArn: str
    ReplicationTaskIdentifier: NotRequired[str]
    MigrationType: NotRequired[MigrationTypeValueType]
    TableMappings: NotRequired[str]
    ReplicationTaskSettings: NotRequired[str]
    CdcStartTime: NotRequired[TimestampTypeDef]
    CdcStartPosition: NotRequired[str]
    CdcStopPosition: NotRequired[str]
    TaskData: NotRequired[str]

class SourceDataSettingTypeDef(TypedDict):
    CDCStartPosition: NotRequired[str]
    CDCStartTime: NotRequired[TimestampTypeDef]
    CDCStopTime: NotRequired[TimestampTypeDef]
    SlotName: NotRequired[str]

class StartReplicationMessageTypeDef(TypedDict):
    ReplicationConfigArn: str
    StartReplicationType: str
    PremigrationAssessmentSettings: NotRequired[str]
    CdcStartTime: NotRequired[TimestampTypeDef]
    CdcStartPosition: NotRequired[str]
    CdcStopPosition: NotRequired[str]

class StartReplicationTaskMessageTypeDef(TypedDict):
    ReplicationTaskArn: str
    StartReplicationTaskType: StartReplicationTaskTypeValueType
    CdcStartTime: NotRequired[TimestampTypeDef]
    CdcStartPosition: NotRequired[str]
    CdcStopPosition: NotRequired[str]

class DataMigrationTypeDef(TypedDict):
    DataMigrationName: NotRequired[str]
    DataMigrationArn: NotRequired[str]
    DataMigrationCreateTime: NotRequired[datetime]
    DataMigrationStartTime: NotRequired[datetime]
    DataMigrationEndTime: NotRequired[datetime]
    ServiceAccessRoleArn: NotRequired[str]
    MigrationProjectArn: NotRequired[str]
    DataMigrationType: NotRequired[MigrationTypeValueType]
    DataMigrationSettings: NotRequired[DataMigrationSettingsTypeDef]
    SourceDataSettings: NotRequired[List[SourceDataSettingOutputTypeDef]]
    TargetDataSettings: NotRequired[List[TargetDataSettingTypeDef]]
    DataMigrationStatistics: NotRequired[DataMigrationStatisticsTypeDef]
    DataMigrationStatus: NotRequired[str]
    PublicIpAddresses: NotRequired[List[str]]
    DataMigrationCidrBlocks: NotRequired[List[str]]
    LastFailureMessage: NotRequired[str]
    StopReason: NotRequired[str]

class MigrationProjectTypeDef(TypedDict):
    MigrationProjectName: NotRequired[str]
    MigrationProjectArn: NotRequired[str]
    MigrationProjectCreationTime: NotRequired[datetime]
    SourceDataProviderDescriptors: NotRequired[List[DataProviderDescriptorTypeDef]]
    TargetDataProviderDescriptors: NotRequired[List[DataProviderDescriptorTypeDef]]
    InstanceProfileArn: NotRequired[str]
    InstanceProfileName: NotRequired[str]
    TransformationRules: NotRequired[str]
    Description: NotRequired[str]
    SchemaConversionApplicationAttributes: NotRequired[SCApplicationAttributesTypeDef]

class DataProviderSettingsTypeDef(TypedDict):
    RedshiftSettings: NotRequired[RedshiftDataProviderSettingsTypeDef]
    PostgreSqlSettings: NotRequired[PostgreSqlDataProviderSettingsTypeDef]
    MySqlSettings: NotRequired[MySqlDataProviderSettingsTypeDef]
    OracleSettings: NotRequired[OracleDataProviderSettingsTypeDef]
    MicrosoftSqlServerSettings: NotRequired[MicrosoftSqlServerDataProviderSettingsTypeDef]
    DocDbSettings: NotRequired[DocDbDataProviderSettingsTypeDef]
    MariaDbSettings: NotRequired[MariaDbDataProviderSettingsTypeDef]
    IbmDb2LuwSettings: NotRequired[IbmDb2LuwDataProviderSettingsTypeDef]
    IbmDb2zOsSettings: NotRequired[IbmDb2zOsDataProviderSettingsTypeDef]
    MongoDbSettings: NotRequired[MongoDbDataProviderSettingsTypeDef]

class DatabaseResponseTypeDef(TypedDict):
    DatabaseId: NotRequired[str]
    DatabaseName: NotRequired[str]
    IpAddress: NotRequired[str]
    NumberOfSchemas: NotRequired[int]
    Server: NotRequired[ServerShortInfoResponseTypeDef]
    SoftwareDetails: NotRequired[DatabaseInstanceSoftwareDetailsResponseTypeDef]
    Collectors: NotRequired[List[CollectorShortInfoResponseTypeDef]]

class ErrorDetailsTypeDef(TypedDict):
    defaultErrorDetails: NotRequired[DefaultErrorDetailsTypeDef]

class DescribeCertificatesMessageTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeConnectionsMessageTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeDataMigrationsMessageTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    WithoutSettings: NotRequired[bool]
    WithoutStatistics: NotRequired[bool]

class DescribeDataProvidersMessageTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeEndpointTypesMessageTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeEndpointsMessageTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeEventCategoriesMessageTypeDef(TypedDict):
    SourceType: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class DescribeEventSubscriptionsMessageTypeDef(TypedDict):
    SubscriptionName: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeEventsMessageTypeDef(TypedDict):
    SourceIdentifier: NotRequired[str]
    SourceType: NotRequired[Literal["replication-instance"]]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Duration: NotRequired[int]
    EventCategories: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeExtensionPackAssociationsMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    Filters: NotRequired[Sequence[FilterTypeDef]]
    Marker: NotRequired[str]
    MaxRecords: NotRequired[int]

class DescribeFleetAdvisorCollectorsRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeFleetAdvisorDatabasesRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeFleetAdvisorSchemaObjectSummaryRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeFleetAdvisorSchemasRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeInstanceProfilesMessageTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeMetadataModelAssessmentsMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    Filters: NotRequired[Sequence[FilterTypeDef]]
    Marker: NotRequired[str]
    MaxRecords: NotRequired[int]

class DescribeMetadataModelConversionsMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    Filters: NotRequired[Sequence[FilterTypeDef]]
    Marker: NotRequired[str]
    MaxRecords: NotRequired[int]

class DescribeMetadataModelExportsAsScriptMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    Filters: NotRequired[Sequence[FilterTypeDef]]
    Marker: NotRequired[str]
    MaxRecords: NotRequired[int]

class DescribeMetadataModelExportsToTargetMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    Filters: NotRequired[Sequence[FilterTypeDef]]
    Marker: NotRequired[str]
    MaxRecords: NotRequired[int]

class DescribeMetadataModelImportsMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    Filters: NotRequired[Sequence[FilterTypeDef]]
    Marker: NotRequired[str]
    MaxRecords: NotRequired[int]

class DescribeMigrationProjectsMessageTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribePendingMaintenanceActionsMessageTypeDef(TypedDict):
    ReplicationInstanceArn: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    Marker: NotRequired[str]
    MaxRecords: NotRequired[int]

class DescribeRecommendationLimitationsRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeRecommendationsRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeReplicationConfigsMessageTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeReplicationInstancesMessageTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeReplicationSubnetGroupsMessageTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeReplicationTableStatisticsMessageTypeDef(TypedDict):
    ReplicationConfigArn: str
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class DescribeReplicationTaskAssessmentRunsMessageTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeReplicationTaskIndividualAssessmentsMessageTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeReplicationTasksMessageTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    WithoutSettings: NotRequired[bool]

class DescribeReplicationsMessageTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]

class DescribeTableStatisticsMessageTypeDef(TypedDict):
    ReplicationTaskArn: str
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class DescribeCertificatesMessagePaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeConnectionsMessagePaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDataMigrationsMessagePaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    WithoutSettings: NotRequired[bool]
    WithoutStatistics: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEndpointTypesMessagePaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEndpointsMessagePaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEventSubscriptionsMessagePaginateTypeDef(TypedDict):
    SubscriptionName: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEventsMessagePaginateTypeDef(TypedDict):
    SourceIdentifier: NotRequired[str]
    SourceType: NotRequired[Literal["replication-instance"]]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    Duration: NotRequired[int]
    EventCategories: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeOrderableReplicationInstancesMessagePaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeReplicationInstancesMessagePaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeReplicationSubnetGroupsMessagePaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeReplicationTaskAssessmentResultsMessagePaginateTypeDef(TypedDict):
    ReplicationTaskArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeReplicationTasksMessagePaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    WithoutSettings: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSchemasMessagePaginateTypeDef(TypedDict):
    EndpointArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeTableStatisticsMessagePaginateTypeDef(TypedDict):
    ReplicationTaskArn: str
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeConnectionsMessageWaitTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeEndpointsMessageWaitTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeReplicationInstancesMessageWaitExtraTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeReplicationInstancesMessageWaitTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeReplicationTasksMessageWaitExtraExtraExtraTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    WithoutSettings: NotRequired[bool]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeReplicationTasksMessageWaitExtraExtraTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    WithoutSettings: NotRequired[bool]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeReplicationTasksMessageWaitExtraTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    WithoutSettings: NotRequired[bool]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeReplicationTasksMessageWaitTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    MaxRecords: NotRequired[int]
    Marker: NotRequired[str]
    WithoutSettings: NotRequired[bool]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeEndpointSettingsResponseTypeDef(TypedDict):
    Marker: str
    EndpointSettings: List[EndpointSettingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointTypesResponseTypeDef(TypedDict):
    Marker: str
    SupportedEndpointTypes: List[SupportedEndpointTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEngineVersionsResponseTypeDef(TypedDict):
    EngineVersions: List[EngineVersionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventCategoriesResponseTypeDef(TypedDict):
    EventCategoryGroupList: List[EventCategoryGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventsResponseTypeDef(TypedDict):
    Marker: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetAdvisorLsaAnalysisResponseTypeDef(TypedDict):
    Analysis: List[FleetAdvisorLsaAnalysisResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef(TypedDict):
    FleetAdvisorSchemaObjects: List[FleetAdvisorSchemaObjectResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeOrderableReplicationInstancesResponseTypeDef(TypedDict):
    OrderableReplicationInstances: List[OrderableReplicationInstanceTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRecommendationLimitationsResponseTypeDef(TypedDict):
    Limitations: List[LimitationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeRefreshSchemasStatusResponseTypeDef(TypedDict):
    RefreshSchemasStatus: RefreshSchemasStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RefreshSchemasResponseTypeDef(TypedDict):
    RefreshSchemasStatus: RefreshSchemasStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationInstanceTaskLogsResponseTypeDef(TypedDict):
    ReplicationInstanceArn: str
    ReplicationInstanceTaskLogs: List[ReplicationInstanceTaskLogTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationTableStatisticsResponseTypeDef(TypedDict):
    ReplicationConfigArn: str
    Marker: str
    ReplicationTableStatistics: List[TableStatisticsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTableStatisticsResponseTypeDef(TypedDict):
    ReplicationTaskArn: str
    TableStatistics: List[TableStatisticsTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationTaskAssessmentResultsResponseTypeDef(TypedDict):
    Marker: str
    BucketName: str
    ReplicationTaskAssessmentResults: List[ReplicationTaskAssessmentResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationTaskIndividualAssessmentsResponseTypeDef(TypedDict):
    Marker: str
    ReplicationTaskIndividualAssessments: List[ReplicationTaskIndividualAssessmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EndpointTypeDef(TypedDict):
    EndpointIdentifier: NotRequired[str]
    EndpointType: NotRequired[ReplicationEndpointTypeValueType]
    EngineName: NotRequired[str]
    EngineDisplayName: NotRequired[str]
    Username: NotRequired[str]
    ServerName: NotRequired[str]
    Port: NotRequired[int]
    DatabaseName: NotRequired[str]
    ExtraConnectionAttributes: NotRequired[str]
    Status: NotRequired[str]
    KmsKeyId: NotRequired[str]
    EndpointArn: NotRequired[str]
    CertificateArn: NotRequired[str]
    SslMode: NotRequired[DmsSslModeValueType]
    ServiceAccessRoleArn: NotRequired[str]
    ExternalTableDefinition: NotRequired[str]
    ExternalId: NotRequired[str]
    DynamoDbSettings: NotRequired[DynamoDbSettingsTypeDef]
    S3Settings: NotRequired[S3SettingsTypeDef]
    DmsTransferSettings: NotRequired[DmsTransferSettingsTypeDef]
    MongoDbSettings: NotRequired[MongoDbSettingsTypeDef]
    KinesisSettings: NotRequired[KinesisSettingsTypeDef]
    KafkaSettings: NotRequired[KafkaSettingsTypeDef]
    ElasticsearchSettings: NotRequired[ElasticsearchSettingsTypeDef]
    NeptuneSettings: NotRequired[NeptuneSettingsTypeDef]
    RedshiftSettings: NotRequired[RedshiftSettingsTypeDef]
    PostgreSQLSettings: NotRequired[PostgreSQLSettingsTypeDef]
    MySQLSettings: NotRequired[MySQLSettingsTypeDef]
    OracleSettings: NotRequired[OracleSettingsOutputTypeDef]
    SybaseSettings: NotRequired[SybaseSettingsTypeDef]
    MicrosoftSQLServerSettings: NotRequired[MicrosoftSQLServerSettingsTypeDef]
    IBMDb2Settings: NotRequired[IBMDb2SettingsTypeDef]
    DocDbSettings: NotRequired[DocDbSettingsTypeDef]
    RedisSettings: NotRequired[RedisSettingsTypeDef]
    GcpMySQLSettings: NotRequired[GcpMySQLSettingsTypeDef]
    TimestreamSettings: NotRequired[TimestreamSettingsTypeDef]

class ExportMetadataModelAssessmentResponseTypeDef(TypedDict):
    PdfReport: ExportMetadataModelAssessmentResultEntryTypeDef
    CsvReport: ExportMetadataModelAssessmentResultEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

OracleSettingsUnionTypeDef = Union[OracleSettingsTypeDef, OracleSettingsOutputTypeDef]

class ResourcePendingMaintenanceActionsTypeDef(TypedDict):
    ResourceIdentifier: NotRequired[str]
    PendingMaintenanceActionDetails: NotRequired[List[PendingMaintenanceActionTypeDef]]

class PremigrationAssessmentStatusTypeDef(TypedDict):
    PremigrationAssessmentRunArn: NotRequired[str]
    FailOnAssessmentFailure: NotRequired[bool]
    Status: NotRequired[str]
    PremigrationAssessmentRunCreationDate: NotRequired[datetime]
    AssessmentProgress: NotRequired[ReplicationTaskAssessmentRunProgressTypeDef]
    LastFailureMessage: NotRequired[str]
    ResultLocationBucket: NotRequired[str]
    ResultLocationFolder: NotRequired[str]
    ResultEncryptionMode: NotRequired[str]
    ResultKmsKeyArn: NotRequired[str]
    ResultStatistic: NotRequired[ReplicationTaskAssessmentRunResultStatisticTypeDef]

class ReplicationTaskAssessmentRunTypeDef(TypedDict):
    ReplicationTaskAssessmentRunArn: NotRequired[str]
    ReplicationTaskArn: NotRequired[str]
    Status: NotRequired[str]
    ReplicationTaskAssessmentRunCreationDate: NotRequired[datetime]
    AssessmentProgress: NotRequired[ReplicationTaskAssessmentRunProgressTypeDef]
    LastFailureMessage: NotRequired[str]
    ServiceAccessRoleArn: NotRequired[str]
    ResultLocationBucket: NotRequired[str]
    ResultLocationFolder: NotRequired[str]
    ResultEncryptionMode: NotRequired[str]
    ResultKmsKeyArn: NotRequired[str]
    AssessmentRunName: NotRequired[str]
    IsLatestTaskAssessmentRun: NotRequired[bool]
    ResultStatistic: NotRequired[ReplicationTaskAssessmentRunResultStatisticTypeDef]

class RdsRecommendationTypeDef(TypedDict):
    RequirementsToTarget: NotRequired[RdsRequirementsTypeDef]
    TargetConfiguration: NotRequired[RdsConfigurationTypeDef]

class StartRecommendationsRequestEntryTypeDef(TypedDict):
    DatabaseId: str
    Settings: RecommendationSettingsTypeDef

class StartRecommendationsRequestTypeDef(TypedDict):
    DatabaseId: str
    Settings: RecommendationSettingsTypeDef

class ReloadReplicationTablesMessageTypeDef(TypedDict):
    ReplicationConfigArn: str
    TablesToReload: Sequence[TableToReloadTypeDef]
    ReloadOption: NotRequired[ReloadOptionValueType]

class ReloadTablesMessageTypeDef(TypedDict):
    ReplicationTaskArn: str
    TablesToReload: Sequence[TableToReloadTypeDef]
    ReloadOption: NotRequired[ReloadOptionValueType]

class ReplicationTaskTypeDef(TypedDict):
    ReplicationTaskIdentifier: NotRequired[str]
    SourceEndpointArn: NotRequired[str]
    TargetEndpointArn: NotRequired[str]
    ReplicationInstanceArn: NotRequired[str]
    MigrationType: NotRequired[MigrationTypeValueType]
    TableMappings: NotRequired[str]
    ReplicationTaskSettings: NotRequired[str]
    Status: NotRequired[str]
    LastFailureMessage: NotRequired[str]
    StopReason: NotRequired[str]
    ReplicationTaskCreationDate: NotRequired[datetime]
    ReplicationTaskStartDate: NotRequired[datetime]
    CdcStartPosition: NotRequired[str]
    CdcStopPosition: NotRequired[str]
    RecoveryCheckpoint: NotRequired[str]
    ReplicationTaskArn: NotRequired[str]
    ReplicationTaskStats: NotRequired[ReplicationTaskStatsTypeDef]
    TaskData: NotRequired[str]
    TargetReplicationInstanceArn: NotRequired[str]

class SchemaResponseTypeDef(TypedDict):
    CodeLineCount: NotRequired[int]
    CodeSize: NotRequired[int]
    Complexity: NotRequired[str]
    Server: NotRequired[ServerShortInfoResponseTypeDef]
    DatabaseInstance: NotRequired[DatabaseShortInfoResponseTypeDef]
    SchemaId: NotRequired[str]
    SchemaName: NotRequired[str]
    OriginalSchema: NotRequired[SchemaShortInfoResponseTypeDef]
    Similarity: NotRequired[float]

class ReplicationSubnetGroupTypeDef(TypedDict):
    ReplicationSubnetGroupIdentifier: NotRequired[str]
    ReplicationSubnetGroupDescription: NotRequired[str]
    VpcId: NotRequired[str]
    SubnetGroupStatus: NotRequired[str]
    Subnets: NotRequired[List[SubnetTypeDef]]
    SupportedNetworkTypes: NotRequired[List[str]]

class DescribeFleetAdvisorCollectorsResponseTypeDef(TypedDict):
    Collectors: List[CollectorResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateReplicationConfigResponseTypeDef(TypedDict):
    ReplicationConfig: ReplicationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteReplicationConfigResponseTypeDef(TypedDict):
    ReplicationConfig: ReplicationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationConfigsResponseTypeDef(TypedDict):
    Marker: str
    ReplicationConfigs: List[ReplicationConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyReplicationConfigResponseTypeDef(TypedDict):
    ReplicationConfig: ReplicationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReplicationConfigMessageTypeDef(TypedDict):
    ReplicationConfigIdentifier: str
    SourceEndpointArn: str
    TargetEndpointArn: str
    ComputeConfig: ComputeConfigUnionTypeDef
    ReplicationType: MigrationTypeValueType
    TableMappings: str
    ReplicationSettings: NotRequired[str]
    SupplementalSettings: NotRequired[str]
    ResourceIdentifier: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ModifyReplicationConfigMessageTypeDef(TypedDict):
    ReplicationConfigArn: str
    ReplicationConfigIdentifier: NotRequired[str]
    ReplicationType: NotRequired[MigrationTypeValueType]
    TableMappings: NotRequired[str]
    ReplicationSettings: NotRequired[str]
    SupplementalSettings: NotRequired[str]
    ComputeConfig: NotRequired[ComputeConfigUnionTypeDef]
    SourceEndpointArn: NotRequired[str]
    TargetEndpointArn: NotRequired[str]

SourceDataSettingUnionTypeDef = Union[SourceDataSettingTypeDef, SourceDataSettingOutputTypeDef]

class CreateDataMigrationResponseTypeDef(TypedDict):
    DataMigration: DataMigrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataMigrationResponseTypeDef(TypedDict):
    DataMigration: DataMigrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataMigrationsResponseTypeDef(TypedDict):
    DataMigrations: List[DataMigrationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDataMigrationResponseTypeDef(TypedDict):
    DataMigration: DataMigrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataMigrationResponseTypeDef(TypedDict):
    DataMigration: DataMigrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopDataMigrationResponseTypeDef(TypedDict):
    DataMigration: DataMigrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMigrationProjectResponseTypeDef(TypedDict):
    MigrationProject: MigrationProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMigrationProjectResponseTypeDef(TypedDict):
    MigrationProject: MigrationProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMigrationProjectsResponseTypeDef(TypedDict):
    Marker: str
    MigrationProjects: List[MigrationProjectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyMigrationProjectResponseTypeDef(TypedDict):
    MigrationProject: MigrationProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataProviderMessageTypeDef(TypedDict):
    Engine: str
    Settings: DataProviderSettingsTypeDef
    DataProviderName: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class DataProviderTypeDef(TypedDict):
    DataProviderName: NotRequired[str]
    DataProviderArn: NotRequired[str]
    DataProviderCreationTime: NotRequired[datetime]
    Description: NotRequired[str]
    Engine: NotRequired[str]
    Settings: NotRequired[DataProviderSettingsTypeDef]

class ModifyDataProviderMessageTypeDef(TypedDict):
    DataProviderIdentifier: str
    DataProviderName: NotRequired[str]
    Description: NotRequired[str]
    Engine: NotRequired[str]
    ExactSettings: NotRequired[bool]
    Settings: NotRequired[DataProviderSettingsTypeDef]

class DescribeFleetAdvisorDatabasesResponseTypeDef(TypedDict):
    Databases: List[DatabaseResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SchemaConversionRequestTypeDef(TypedDict):
    Status: NotRequired[str]
    RequestIdentifier: NotRequired[str]
    MigrationProjectArn: NotRequired[str]
    Error: NotRequired[ErrorDetailsTypeDef]
    ExportSqlDetails: NotRequired[ExportSqlDetailsTypeDef]

class CreateEndpointResponseTypeDef(TypedDict):
    Endpoint: EndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEndpointResponseTypeDef(TypedDict):
    Endpoint: EndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointsResponseTypeDef(TypedDict):
    Marker: str
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyEndpointResponseTypeDef(TypedDict):
    Endpoint: EndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointMessageTypeDef(TypedDict):
    EndpointIdentifier: str
    EndpointType: ReplicationEndpointTypeValueType
    EngineName: str
    Username: NotRequired[str]
    Password: NotRequired[str]
    ServerName: NotRequired[str]
    Port: NotRequired[int]
    DatabaseName: NotRequired[str]
    ExtraConnectionAttributes: NotRequired[str]
    KmsKeyId: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    CertificateArn: NotRequired[str]
    SslMode: NotRequired[DmsSslModeValueType]
    ServiceAccessRoleArn: NotRequired[str]
    ExternalTableDefinition: NotRequired[str]
    DynamoDbSettings: NotRequired[DynamoDbSettingsTypeDef]
    S3Settings: NotRequired[S3SettingsTypeDef]
    DmsTransferSettings: NotRequired[DmsTransferSettingsTypeDef]
    MongoDbSettings: NotRequired[MongoDbSettingsTypeDef]
    KinesisSettings: NotRequired[KinesisSettingsTypeDef]
    KafkaSettings: NotRequired[KafkaSettingsTypeDef]
    ElasticsearchSettings: NotRequired[ElasticsearchSettingsTypeDef]
    NeptuneSettings: NotRequired[NeptuneSettingsTypeDef]
    RedshiftSettings: NotRequired[RedshiftSettingsTypeDef]
    PostgreSQLSettings: NotRequired[PostgreSQLSettingsTypeDef]
    MySQLSettings: NotRequired[MySQLSettingsTypeDef]
    OracleSettings: NotRequired[OracleSettingsUnionTypeDef]
    SybaseSettings: NotRequired[SybaseSettingsTypeDef]
    MicrosoftSQLServerSettings: NotRequired[MicrosoftSQLServerSettingsTypeDef]
    IBMDb2Settings: NotRequired[IBMDb2SettingsTypeDef]
    ResourceIdentifier: NotRequired[str]
    DocDbSettings: NotRequired[DocDbSettingsTypeDef]
    RedisSettings: NotRequired[RedisSettingsTypeDef]
    GcpMySQLSettings: NotRequired[GcpMySQLSettingsTypeDef]
    TimestreamSettings: NotRequired[TimestreamSettingsTypeDef]

class ModifyEndpointMessageTypeDef(TypedDict):
    EndpointArn: str
    EndpointIdentifier: NotRequired[str]
    EndpointType: NotRequired[ReplicationEndpointTypeValueType]
    EngineName: NotRequired[str]
    Username: NotRequired[str]
    Password: NotRequired[str]
    ServerName: NotRequired[str]
    Port: NotRequired[int]
    DatabaseName: NotRequired[str]
    ExtraConnectionAttributes: NotRequired[str]
    CertificateArn: NotRequired[str]
    SslMode: NotRequired[DmsSslModeValueType]
    ServiceAccessRoleArn: NotRequired[str]
    ExternalTableDefinition: NotRequired[str]
    DynamoDbSettings: NotRequired[DynamoDbSettingsTypeDef]
    S3Settings: NotRequired[S3SettingsTypeDef]
    DmsTransferSettings: NotRequired[DmsTransferSettingsTypeDef]
    MongoDbSettings: NotRequired[MongoDbSettingsTypeDef]
    KinesisSettings: NotRequired[KinesisSettingsTypeDef]
    KafkaSettings: NotRequired[KafkaSettingsTypeDef]
    ElasticsearchSettings: NotRequired[ElasticsearchSettingsTypeDef]
    NeptuneSettings: NotRequired[NeptuneSettingsTypeDef]
    RedshiftSettings: NotRequired[RedshiftSettingsTypeDef]
    PostgreSQLSettings: NotRequired[PostgreSQLSettingsTypeDef]
    MySQLSettings: NotRequired[MySQLSettingsTypeDef]
    OracleSettings: NotRequired[OracleSettingsUnionTypeDef]
    SybaseSettings: NotRequired[SybaseSettingsTypeDef]
    MicrosoftSQLServerSettings: NotRequired[MicrosoftSQLServerSettingsTypeDef]
    IBMDb2Settings: NotRequired[IBMDb2SettingsTypeDef]
    DocDbSettings: NotRequired[DocDbSettingsTypeDef]
    RedisSettings: NotRequired[RedisSettingsTypeDef]
    ExactSettings: NotRequired[bool]
    GcpMySQLSettings: NotRequired[GcpMySQLSettingsTypeDef]
    TimestreamSettings: NotRequired[TimestreamSettingsTypeDef]

class ApplyPendingMaintenanceActionResponseTypeDef(TypedDict):
    ResourcePendingMaintenanceActions: ResourcePendingMaintenanceActionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePendingMaintenanceActionsResponseTypeDef(TypedDict):
    PendingMaintenanceActions: List[ResourcePendingMaintenanceActionsTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationTypeDef(TypedDict):
    ReplicationConfigIdentifier: NotRequired[str]
    ReplicationConfigArn: NotRequired[str]
    SourceEndpointArn: NotRequired[str]
    TargetEndpointArn: NotRequired[str]
    ReplicationType: NotRequired[MigrationTypeValueType]
    Status: NotRequired[str]
    ProvisionData: NotRequired[ProvisionDataTypeDef]
    PremigrationAssessmentStatuses: NotRequired[List[PremigrationAssessmentStatusTypeDef]]
    StopReason: NotRequired[str]
    FailureMessages: NotRequired[List[str]]
    ReplicationStats: NotRequired[ReplicationStatsTypeDef]
    StartReplicationType: NotRequired[str]
    CdcStartTime: NotRequired[datetime]
    CdcStartPosition: NotRequired[str]
    CdcStopPosition: NotRequired[str]
    RecoveryCheckpoint: NotRequired[str]
    ReplicationCreateTime: NotRequired[datetime]
    ReplicationUpdateTime: NotRequired[datetime]
    ReplicationLastStopTime: NotRequired[datetime]
    ReplicationDeprovisionTime: NotRequired[datetime]

class CancelReplicationTaskAssessmentRunResponseTypeDef(TypedDict):
    ReplicationTaskAssessmentRun: ReplicationTaskAssessmentRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteReplicationTaskAssessmentRunResponseTypeDef(TypedDict):
    ReplicationTaskAssessmentRun: ReplicationTaskAssessmentRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationTaskAssessmentRunsResponseTypeDef(TypedDict):
    Marker: str
    ReplicationTaskAssessmentRuns: List[ReplicationTaskAssessmentRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartReplicationTaskAssessmentRunResponseTypeDef(TypedDict):
    ReplicationTaskAssessmentRun: ReplicationTaskAssessmentRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RecommendationDataTypeDef(TypedDict):
    RdsEngine: NotRequired[RdsRecommendationTypeDef]

class BatchStartRecommendationsRequestTypeDef(TypedDict):
    Data: NotRequired[Sequence[StartRecommendationsRequestEntryTypeDef]]

class CreateReplicationTaskResponseTypeDef(TypedDict):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteReplicationTaskResponseTypeDef(TypedDict):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationTasksResponseTypeDef(TypedDict):
    Marker: str
    ReplicationTasks: List[ReplicationTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyReplicationTaskResponseTypeDef(TypedDict):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MoveReplicationTaskResponseTypeDef(TypedDict):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartReplicationTaskAssessmentResponseTypeDef(TypedDict):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartReplicationTaskResponseTypeDef(TypedDict):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopReplicationTaskResponseTypeDef(TypedDict):
    ReplicationTask: ReplicationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetAdvisorSchemasResponseTypeDef(TypedDict):
    FleetAdvisorSchemas: List[SchemaResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateReplicationSubnetGroupResponseTypeDef(TypedDict):
    ReplicationSubnetGroup: ReplicationSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationSubnetGroupsResponseTypeDef(TypedDict):
    Marker: str
    ReplicationSubnetGroups: List[ReplicationSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyReplicationSubnetGroupResponseTypeDef(TypedDict):
    ReplicationSubnetGroup: ReplicationSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationInstanceTypeDef(TypedDict):
    ReplicationInstanceIdentifier: NotRequired[str]
    ReplicationInstanceClass: NotRequired[str]
    ReplicationInstanceStatus: NotRequired[str]
    AllocatedStorage: NotRequired[int]
    InstanceCreateTime: NotRequired[datetime]
    VpcSecurityGroups: NotRequired[List[VpcSecurityGroupMembershipTypeDef]]
    AvailabilityZone: NotRequired[str]
    ReplicationSubnetGroup: NotRequired[ReplicationSubnetGroupTypeDef]
    PreferredMaintenanceWindow: NotRequired[str]
    PendingModifiedValues: NotRequired[ReplicationPendingModifiedValuesTypeDef]
    MultiAZ: NotRequired[bool]
    EngineVersion: NotRequired[str]
    AutoMinorVersionUpgrade: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    ReplicationInstanceArn: NotRequired[str]
    ReplicationInstancePublicIpAddress: NotRequired[str]
    ReplicationInstancePrivateIpAddress: NotRequired[str]
    ReplicationInstancePublicIpAddresses: NotRequired[List[str]]
    ReplicationInstancePrivateIpAddresses: NotRequired[List[str]]
    ReplicationInstanceIpv6Addresses: NotRequired[List[str]]
    PubliclyAccessible: NotRequired[bool]
    SecondaryAvailabilityZone: NotRequired[str]
    FreeUntil: NotRequired[datetime]
    DnsNameServers: NotRequired[str]
    NetworkType: NotRequired[str]
    KerberosAuthenticationSettings: NotRequired[KerberosAuthenticationSettingsTypeDef]

class CreateDataMigrationMessageTypeDef(TypedDict):
    MigrationProjectIdentifier: str
    DataMigrationType: MigrationTypeValueType
    ServiceAccessRoleArn: str
    DataMigrationName: NotRequired[str]
    EnableCloudwatchLogs: NotRequired[bool]
    SourceDataSettings: NotRequired[Sequence[SourceDataSettingUnionTypeDef]]
    TargetDataSettings: NotRequired[Sequence[TargetDataSettingTypeDef]]
    NumberOfJobs: NotRequired[int]
    Tags: NotRequired[Sequence[TagTypeDef]]
    SelectionRules: NotRequired[str]

class ModifyDataMigrationMessageTypeDef(TypedDict):
    DataMigrationIdentifier: str
    DataMigrationName: NotRequired[str]
    EnableCloudwatchLogs: NotRequired[bool]
    ServiceAccessRoleArn: NotRequired[str]
    DataMigrationType: NotRequired[MigrationTypeValueType]
    SourceDataSettings: NotRequired[Sequence[SourceDataSettingUnionTypeDef]]
    TargetDataSettings: NotRequired[Sequence[TargetDataSettingTypeDef]]
    NumberOfJobs: NotRequired[int]
    SelectionRules: NotRequired[str]

class CreateDataProviderResponseTypeDef(TypedDict):
    DataProvider: DataProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataProviderResponseTypeDef(TypedDict):
    DataProvider: DataProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataProvidersResponseTypeDef(TypedDict):
    Marker: str
    DataProviders: List[DataProviderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDataProviderResponseTypeDef(TypedDict):
    DataProvider: DataProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExtensionPackAssociationsResponseTypeDef(TypedDict):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMetadataModelAssessmentsResponseTypeDef(TypedDict):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMetadataModelConversionsResponseTypeDef(TypedDict):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMetadataModelExportsAsScriptResponseTypeDef(TypedDict):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMetadataModelExportsToTargetResponseTypeDef(TypedDict):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMetadataModelImportsResponseTypeDef(TypedDict):
    Marker: str
    Requests: List[SchemaConversionRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationsResponseTypeDef(TypedDict):
    Marker: str
    Replications: List[ReplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartReplicationResponseTypeDef(TypedDict):
    Replication: ReplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopReplicationResponseTypeDef(TypedDict):
    Replication: ReplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RecommendationTypeDef(TypedDict):
    DatabaseId: NotRequired[str]
    EngineName: NotRequired[str]
    CreatedDate: NotRequired[str]
    Status: NotRequired[str]
    Preferred: NotRequired[bool]
    Settings: NotRequired[RecommendationSettingsTypeDef]
    Data: NotRequired[RecommendationDataTypeDef]

class CreateReplicationInstanceResponseTypeDef(TypedDict):
    ReplicationInstance: ReplicationInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteReplicationInstanceResponseTypeDef(TypedDict):
    ReplicationInstance: ReplicationInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplicationInstancesResponseTypeDef(TypedDict):
    Marker: str
    ReplicationInstances: List[ReplicationInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyReplicationInstanceResponseTypeDef(TypedDict):
    ReplicationInstance: ReplicationInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootReplicationInstanceResponseTypeDef(TypedDict):
    ReplicationInstance: ReplicationInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRecommendationsResponseTypeDef(TypedDict):
    Recommendations: List[RecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
