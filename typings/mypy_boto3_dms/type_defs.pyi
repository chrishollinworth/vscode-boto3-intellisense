"""
Type annotations for dms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dms.type_defs import AccountQuotaTypeDef

    data: AccountQuotaTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

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
    OriginTypeValueType,
    ParquetVersionValueType,
    PluginNameValueType,
    RedisAuthTypeValueType,
    RefreshSchemasStatusTypeValueType,
    ReleaseStatusValuesType,
    ReloadOptionValueType,
    ReplicationEndpointTypeValueType,
    SafeguardPolicyType,
    SslSecurityProtocolValueType,
    StartReplicationTaskTypeValueType,
    TargetDbTypeType,
    TlogAccessModeType,
    VersionStatusType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountQuotaTypeDef",
    "AddTagsToResourceMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    "ApplyPendingMaintenanceActionResponseTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchStartRecommendationsErrorEntryTypeDef",
    "BatchStartRecommendationsRequestRequestTypeDef",
    "BatchStartRecommendationsResponseTypeDef",
    "CancelReplicationTaskAssessmentRunMessageRequestTypeDef",
    "CancelReplicationTaskAssessmentRunResponseTypeDef",
    "CertificateTypeDef",
    "CollectorHealthCheckTypeDef",
    "CollectorResponseTypeDef",
    "CollectorShortInfoResponseTypeDef",
    "ComputeConfigTypeDef",
    "ConnectionTypeDef",
    "CreateDataProviderMessageRequestTypeDef",
    "CreateDataProviderResponseTypeDef",
    "CreateEndpointMessageRequestTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreateEventSubscriptionMessageRequestTypeDef",
    "CreateEventSubscriptionResponseTypeDef",
    "CreateFleetAdvisorCollectorRequestRequestTypeDef",
    "CreateFleetAdvisorCollectorResponseTypeDef",
    "CreateInstanceProfileMessageRequestTypeDef",
    "CreateInstanceProfileResponseTypeDef",
    "CreateMigrationProjectMessageRequestTypeDef",
    "CreateMigrationProjectResponseTypeDef",
    "CreateReplicationConfigMessageRequestTypeDef",
    "CreateReplicationConfigResponseTypeDef",
    "CreateReplicationInstanceMessageRequestTypeDef",
    "CreateReplicationInstanceResponseTypeDef",
    "CreateReplicationSubnetGroupMessageRequestTypeDef",
    "CreateReplicationSubnetGroupResponseTypeDef",
    "CreateReplicationTaskMessageRequestTypeDef",
    "CreateReplicationTaskResponseTypeDef",
    "DataProviderDescriptorDefinitionTypeDef",
    "DataProviderDescriptorTypeDef",
    "DataProviderSettingsTypeDef",
    "DataProviderTypeDef",
    "DatabaseInstanceSoftwareDetailsResponseTypeDef",
    "DatabaseResponseTypeDef",
    "DatabaseShortInfoResponseTypeDef",
    "DefaultErrorDetailsTypeDef",
    "DeleteCertificateMessageRequestTypeDef",
    "DeleteCertificateResponseTypeDef",
    "DeleteCollectorRequestRequestTypeDef",
    "DeleteConnectionMessageRequestTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteDataProviderMessageRequestTypeDef",
    "DeleteDataProviderResponseTypeDef",
    "DeleteEndpointMessageRequestTypeDef",
    "DeleteEndpointResponseTypeDef",
    "DeleteEventSubscriptionMessageRequestTypeDef",
    "DeleteEventSubscriptionResponseTypeDef",
    "DeleteFleetAdvisorDatabasesRequestRequestTypeDef",
    "DeleteFleetAdvisorDatabasesResponseTypeDef",
    "DeleteInstanceProfileMessageRequestTypeDef",
    "DeleteInstanceProfileResponseTypeDef",
    "DeleteMigrationProjectMessageRequestTypeDef",
    "DeleteMigrationProjectResponseTypeDef",
    "DeleteReplicationConfigMessageRequestTypeDef",
    "DeleteReplicationConfigResponseTypeDef",
    "DeleteReplicationInstanceMessageRequestTypeDef",
    "DeleteReplicationInstanceResponseTypeDef",
    "DeleteReplicationSubnetGroupMessageRequestTypeDef",
    "DeleteReplicationTaskAssessmentRunMessageRequestTypeDef",
    "DeleteReplicationTaskAssessmentRunResponseTypeDef",
    "DeleteReplicationTaskMessageRequestTypeDef",
    "DeleteReplicationTaskResponseTypeDef",
    "DescribeAccountAttributesResponseTypeDef",
    "DescribeApplicableIndividualAssessmentsMessageRequestTypeDef",
    "DescribeApplicableIndividualAssessmentsResponseTypeDef",
    "DescribeCertificatesMessageRequestTypeDef",
    "DescribeCertificatesResponseTypeDef",
    "DescribeConnectionsMessageRequestTypeDef",
    "DescribeConnectionsResponseTypeDef",
    "DescribeConversionConfigurationMessageRequestTypeDef",
    "DescribeConversionConfigurationResponseTypeDef",
    "DescribeDataProvidersMessageRequestTypeDef",
    "DescribeDataProvidersResponseTypeDef",
    "DescribeEndpointSettingsMessageRequestTypeDef",
    "DescribeEndpointSettingsResponseTypeDef",
    "DescribeEndpointTypesMessageRequestTypeDef",
    "DescribeEndpointTypesResponseTypeDef",
    "DescribeEndpointsMessageRequestTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeEngineVersionsMessageRequestTypeDef",
    "DescribeEngineVersionsResponseTypeDef",
    "DescribeEventCategoriesMessageRequestTypeDef",
    "DescribeEventCategoriesResponseTypeDef",
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    "DescribeEventSubscriptionsResponseTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeExtensionPackAssociationsMessageRequestTypeDef",
    "DescribeExtensionPackAssociationsResponseTypeDef",
    "DescribeFleetAdvisorCollectorsRequestRequestTypeDef",
    "DescribeFleetAdvisorCollectorsResponseTypeDef",
    "DescribeFleetAdvisorDatabasesRequestRequestTypeDef",
    "DescribeFleetAdvisorDatabasesResponseTypeDef",
    "DescribeFleetAdvisorLsaAnalysisRequestRequestTypeDef",
    "DescribeFleetAdvisorLsaAnalysisResponseTypeDef",
    "DescribeFleetAdvisorSchemaObjectSummaryRequestRequestTypeDef",
    "DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef",
    "DescribeFleetAdvisorSchemasRequestRequestTypeDef",
    "DescribeFleetAdvisorSchemasResponseTypeDef",
    "DescribeInstanceProfilesMessageRequestTypeDef",
    "DescribeInstanceProfilesResponseTypeDef",
    "DescribeMetadataModelAssessmentsMessageRequestTypeDef",
    "DescribeMetadataModelAssessmentsResponseTypeDef",
    "DescribeMetadataModelConversionsMessageRequestTypeDef",
    "DescribeMetadataModelConversionsResponseTypeDef",
    "DescribeMetadataModelExportsAsScriptMessageRequestTypeDef",
    "DescribeMetadataModelExportsAsScriptResponseTypeDef",
    "DescribeMetadataModelExportsToTargetMessageRequestTypeDef",
    "DescribeMetadataModelExportsToTargetResponseTypeDef",
    "DescribeMetadataModelImportsMessageRequestTypeDef",
    "DescribeMetadataModelImportsResponseTypeDef",
    "DescribeMigrationProjectsMessageRequestTypeDef",
    "DescribeMigrationProjectsResponseTypeDef",
    "DescribeOrderableReplicationInstancesMessageRequestTypeDef",
    "DescribeOrderableReplicationInstancesResponseTypeDef",
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    "DescribePendingMaintenanceActionsResponseTypeDef",
    "DescribeRecommendationLimitationsRequestRequestTypeDef",
    "DescribeRecommendationLimitationsResponseTypeDef",
    "DescribeRecommendationsRequestRequestTypeDef",
    "DescribeRecommendationsResponseTypeDef",
    "DescribeRefreshSchemasStatusMessageRequestTypeDef",
    "DescribeRefreshSchemasStatusResponseTypeDef",
    "DescribeReplicationConfigsMessageRequestTypeDef",
    "DescribeReplicationConfigsResponseTypeDef",
    "DescribeReplicationInstanceTaskLogsMessageRequestTypeDef",
    "DescribeReplicationInstanceTaskLogsResponseTypeDef",
    "DescribeReplicationInstancesMessageRequestTypeDef",
    "DescribeReplicationInstancesResponseTypeDef",
    "DescribeReplicationSubnetGroupsMessageRequestTypeDef",
    "DescribeReplicationSubnetGroupsResponseTypeDef",
    "DescribeReplicationTableStatisticsMessageRequestTypeDef",
    "DescribeReplicationTableStatisticsResponseTypeDef",
    "DescribeReplicationTaskAssessmentResultsMessageRequestTypeDef",
    "DescribeReplicationTaskAssessmentResultsResponseTypeDef",
    "DescribeReplicationTaskAssessmentRunsMessageRequestTypeDef",
    "DescribeReplicationTaskAssessmentRunsResponseTypeDef",
    "DescribeReplicationTaskIndividualAssessmentsMessageRequestTypeDef",
    "DescribeReplicationTaskIndividualAssessmentsResponseTypeDef",
    "DescribeReplicationTasksMessageRequestTypeDef",
    "DescribeReplicationTasksResponseTypeDef",
    "DescribeReplicationsMessageRequestTypeDef",
    "DescribeReplicationsResponseTypeDef",
    "DescribeSchemasMessageRequestTypeDef",
    "DescribeSchemasResponseTypeDef",
    "DescribeTableStatisticsMessageRequestTypeDef",
    "DescribeTableStatisticsResponseTypeDef",
    "DmsTransferSettingsTypeDef",
    "DocDbDataProviderSettingsTypeDef",
    "DocDbSettingsTypeDef",
    "DynamoDbSettingsTypeDef",
    "ElasticsearchSettingsTypeDef",
    "EndpointSettingTypeDef",
    "EndpointTypeDef",
    "EngineVersionTypeDef",
    "ErrorDetailsTypeDef",
    "EventCategoryGroupTypeDef",
    "EventSubscriptionTypeDef",
    "EventTypeDef",
    "ExportMetadataModelAssessmentMessageRequestTypeDef",
    "ExportMetadataModelAssessmentResponseTypeDef",
    "ExportMetadataModelAssessmentResultEntryTypeDef",
    "ExportSqlDetailsTypeDef",
    "FilterTypeDef",
    "FleetAdvisorLsaAnalysisResponseTypeDef",
    "FleetAdvisorSchemaObjectResponseTypeDef",
    "GcpMySQLSettingsTypeDef",
    "IBMDb2SettingsTypeDef",
    "ImportCertificateMessageRequestTypeDef",
    "ImportCertificateResponseTypeDef",
    "InstanceProfileTypeDef",
    "InventoryDataTypeDef",
    "KafkaSettingsTypeDef",
    "KinesisSettingsTypeDef",
    "LimitationTypeDef",
    "ListTagsForResourceMessageRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MariaDbDataProviderSettingsTypeDef",
    "MicrosoftSQLServerSettingsTypeDef",
    "MicrosoftSqlServerDataProviderSettingsTypeDef",
    "MigrationProjectTypeDef",
    "ModifyConversionConfigurationMessageRequestTypeDef",
    "ModifyConversionConfigurationResponseTypeDef",
    "ModifyDataProviderMessageRequestTypeDef",
    "ModifyDataProviderResponseTypeDef",
    "ModifyEndpointMessageRequestTypeDef",
    "ModifyEndpointResponseTypeDef",
    "ModifyEventSubscriptionMessageRequestTypeDef",
    "ModifyEventSubscriptionResponseTypeDef",
    "ModifyInstanceProfileMessageRequestTypeDef",
    "ModifyInstanceProfileResponseTypeDef",
    "ModifyMigrationProjectMessageRequestTypeDef",
    "ModifyMigrationProjectResponseTypeDef",
    "ModifyReplicationConfigMessageRequestTypeDef",
    "ModifyReplicationConfigResponseTypeDef",
    "ModifyReplicationInstanceMessageRequestTypeDef",
    "ModifyReplicationInstanceResponseTypeDef",
    "ModifyReplicationSubnetGroupMessageRequestTypeDef",
    "ModifyReplicationSubnetGroupResponseTypeDef",
    "ModifyReplicationTaskMessageRequestTypeDef",
    "ModifyReplicationTaskResponseTypeDef",
    "MongoDbDataProviderSettingsTypeDef",
    "MongoDbSettingsTypeDef",
    "MoveReplicationTaskMessageRequestTypeDef",
    "MoveReplicationTaskResponseTypeDef",
    "MySQLSettingsTypeDef",
    "MySqlDataProviderSettingsTypeDef",
    "NeptuneSettingsTypeDef",
    "OracleDataProviderSettingsTypeDef",
    "OracleSettingsTypeDef",
    "OrderableReplicationInstanceTypeDef",
    "PaginatorConfigTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PostgreSQLSettingsTypeDef",
    "PostgreSqlDataProviderSettingsTypeDef",
    "ProvisionDataTypeDef",
    "RdsConfigurationTypeDef",
    "RdsRecommendationTypeDef",
    "RdsRequirementsTypeDef",
    "RebootReplicationInstanceMessageRequestTypeDef",
    "RebootReplicationInstanceResponseTypeDef",
    "RecommendationDataTypeDef",
    "RecommendationSettingsTypeDef",
    "RecommendationTypeDef",
    "RedisSettingsTypeDef",
    "RedshiftDataProviderSettingsTypeDef",
    "RedshiftSettingsTypeDef",
    "RefreshSchemasMessageRequestTypeDef",
    "RefreshSchemasResponseTypeDef",
    "RefreshSchemasStatusTypeDef",
    "ReloadReplicationTablesMessageRequestTypeDef",
    "ReloadReplicationTablesResponseTypeDef",
    "ReloadTablesMessageRequestTypeDef",
    "ReloadTablesResponseTypeDef",
    "RemoveTagsFromResourceMessageRequestTypeDef",
    "ReplicationConfigTypeDef",
    "ReplicationInstanceTaskLogTypeDef",
    "ReplicationInstanceTypeDef",
    "ReplicationPendingModifiedValuesTypeDef",
    "ReplicationStatsTypeDef",
    "ReplicationSubnetGroupTypeDef",
    "ReplicationTaskAssessmentResultTypeDef",
    "ReplicationTaskAssessmentRunProgressTypeDef",
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
    "StartExtensionPackAssociationMessageRequestTypeDef",
    "StartExtensionPackAssociationResponseTypeDef",
    "StartMetadataModelAssessmentMessageRequestTypeDef",
    "StartMetadataModelAssessmentResponseTypeDef",
    "StartMetadataModelConversionMessageRequestTypeDef",
    "StartMetadataModelConversionResponseTypeDef",
    "StartMetadataModelExportAsScriptMessageRequestTypeDef",
    "StartMetadataModelExportAsScriptResponseTypeDef",
    "StartMetadataModelExportToTargetMessageRequestTypeDef",
    "StartMetadataModelExportToTargetResponseTypeDef",
    "StartMetadataModelImportMessageRequestTypeDef",
    "StartMetadataModelImportResponseTypeDef",
    "StartRecommendationsRequestEntryTypeDef",
    "StartRecommendationsRequestRequestTypeDef",
    "StartReplicationMessageRequestTypeDef",
    "StartReplicationResponseTypeDef",
    "StartReplicationTaskAssessmentMessageRequestTypeDef",
    "StartReplicationTaskAssessmentResponseTypeDef",
    "StartReplicationTaskAssessmentRunMessageRequestTypeDef",
    "StartReplicationTaskAssessmentRunResponseTypeDef",
    "StartReplicationTaskMessageRequestTypeDef",
    "StartReplicationTaskResponseTypeDef",
    "StopReplicationMessageRequestTypeDef",
    "StopReplicationResponseTypeDef",
    "StopReplicationTaskMessageRequestTypeDef",
    "StopReplicationTaskResponseTypeDef",
    "SubnetTypeDef",
    "SupportedEndpointTypeTypeDef",
    "SybaseSettingsTypeDef",
    "TableStatisticsTypeDef",
    "TableToReloadTypeDef",
    "TagTypeDef",
    "TestConnectionMessageRequestTypeDef",
    "TestConnectionResponseTypeDef",
    "TimestreamSettingsTypeDef",
    "UpdateSubscriptionsToEventBridgeMessageRequestTypeDef",
    "UpdateSubscriptionsToEventBridgeResponseTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)

AccountQuotaTypeDef = TypedDict(
    "AccountQuotaTypeDef",
    {
        "AccountQuotaName": str,
        "Used": int,
        "Max": int,
    },
    total=False,
)

AddTagsToResourceMessageRequestTypeDef = TypedDict(
    "AddTagsToResourceMessageRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

ApplyPendingMaintenanceActionMessageRequestTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ApplyAction": str,
        "OptInType": str,
    },
)

ApplyPendingMaintenanceActionResponseTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionResponseTypeDef",
    {
        "ResourcePendingMaintenanceActions": "ResourcePendingMaintenanceActionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": str,
    },
    total=False,
)

BatchStartRecommendationsErrorEntryTypeDef = TypedDict(
    "BatchStartRecommendationsErrorEntryTypeDef",
    {
        "DatabaseId": str,
        "Message": str,
        "Code": str,
    },
    total=False,
)

BatchStartRecommendationsRequestRequestTypeDef = TypedDict(
    "BatchStartRecommendationsRequestRequestTypeDef",
    {
        "Data": List["StartRecommendationsRequestEntryTypeDef"],
    },
    total=False,
)

BatchStartRecommendationsResponseTypeDef = TypedDict(
    "BatchStartRecommendationsResponseTypeDef",
    {
        "ErrorEntries": List["BatchStartRecommendationsErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelReplicationTaskAssessmentRunMessageRequestTypeDef = TypedDict(
    "CancelReplicationTaskAssessmentRunMessageRequestTypeDef",
    {
        "ReplicationTaskAssessmentRunArn": str,
    },
)

CancelReplicationTaskAssessmentRunResponseTypeDef = TypedDict(
    "CancelReplicationTaskAssessmentRunResponseTypeDef",
    {
        "ReplicationTaskAssessmentRun": "ReplicationTaskAssessmentRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateIdentifier": str,
        "CertificateCreationDate": datetime,
        "CertificatePem": str,
        "CertificateWallet": bytes,
        "CertificateArn": str,
        "CertificateOwner": str,
        "ValidFromDate": datetime,
        "ValidToDate": datetime,
        "SigningAlgorithm": str,
        "KeyLength": int,
    },
    total=False,
)

CollectorHealthCheckTypeDef = TypedDict(
    "CollectorHealthCheckTypeDef",
    {
        "CollectorStatus": CollectorStatusType,
        "LocalCollectorS3Access": bool,
        "WebCollectorS3Access": bool,
        "WebCollectorGrantedRoleBasedAccess": bool,
    },
    total=False,
)

CollectorResponseTypeDef = TypedDict(
    "CollectorResponseTypeDef",
    {
        "CollectorReferencedId": str,
        "CollectorName": str,
        "CollectorVersion": str,
        "VersionStatus": VersionStatusType,
        "Description": str,
        "S3BucketName": str,
        "ServiceAccessRoleArn": str,
        "CollectorHealthCheck": "CollectorHealthCheckTypeDef",
        "LastDataReceived": str,
        "RegisteredDate": str,
        "CreatedDate": str,
        "ModifiedDate": str,
        "InventoryData": "InventoryDataTypeDef",
    },
    total=False,
)

CollectorShortInfoResponseTypeDef = TypedDict(
    "CollectorShortInfoResponseTypeDef",
    {
        "CollectorReferencedId": str,
        "CollectorName": str,
    },
    total=False,
)

ComputeConfigTypeDef = TypedDict(
    "ComputeConfigTypeDef",
    {
        "AvailabilityZone": str,
        "DnsNameServers": str,
        "KmsKeyId": str,
        "MaxCapacityUnits": int,
        "MinCapacityUnits": int,
        "MultiAZ": bool,
        "PreferredMaintenanceWindow": str,
        "ReplicationSubnetGroupId": str,
        "VpcSecurityGroupIds": List[str],
    },
    total=False,
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
        "Status": str,
        "LastFailureMessage": str,
        "EndpointIdentifier": str,
        "ReplicationInstanceIdentifier": str,
    },
    total=False,
)

_RequiredCreateDataProviderMessageRequestTypeDef = TypedDict(
    "_RequiredCreateDataProviderMessageRequestTypeDef",
    {
        "Engine": str,
        "Settings": "DataProviderSettingsTypeDef",
    },
)
_OptionalCreateDataProviderMessageRequestTypeDef = TypedDict(
    "_OptionalCreateDataProviderMessageRequestTypeDef",
    {
        "DataProviderName": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDataProviderMessageRequestTypeDef(
    _RequiredCreateDataProviderMessageRequestTypeDef,
    _OptionalCreateDataProviderMessageRequestTypeDef,
):
    pass

CreateDataProviderResponseTypeDef = TypedDict(
    "CreateDataProviderResponseTypeDef",
    {
        "DataProvider": "DataProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEndpointMessageRequestTypeDef = TypedDict(
    "_RequiredCreateEndpointMessageRequestTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": ReplicationEndpointTypeValueType,
        "EngineName": str,
    },
)
_OptionalCreateEndpointMessageRequestTypeDef = TypedDict(
    "_OptionalCreateEndpointMessageRequestTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
        "CertificateArn": str,
        "SslMode": DmsSslModeValueType,
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "DynamoDbSettings": "DynamoDbSettingsTypeDef",
        "S3Settings": "S3SettingsTypeDef",
        "DmsTransferSettings": "DmsTransferSettingsTypeDef",
        "MongoDbSettings": "MongoDbSettingsTypeDef",
        "KinesisSettings": "KinesisSettingsTypeDef",
        "KafkaSettings": "KafkaSettingsTypeDef",
        "ElasticsearchSettings": "ElasticsearchSettingsTypeDef",
        "NeptuneSettings": "NeptuneSettingsTypeDef",
        "RedshiftSettings": "RedshiftSettingsTypeDef",
        "PostgreSQLSettings": "PostgreSQLSettingsTypeDef",
        "MySQLSettings": "MySQLSettingsTypeDef",
        "OracleSettings": "OracleSettingsTypeDef",
        "SybaseSettings": "SybaseSettingsTypeDef",
        "MicrosoftSQLServerSettings": "MicrosoftSQLServerSettingsTypeDef",
        "IBMDb2Settings": "IBMDb2SettingsTypeDef",
        "ResourceIdentifier": str,
        "DocDbSettings": "DocDbSettingsTypeDef",
        "RedisSettings": "RedisSettingsTypeDef",
        "GcpMySQLSettings": "GcpMySQLSettingsTypeDef",
        "TimestreamSettings": "TimestreamSettingsTypeDef",
    },
    total=False,
)

class CreateEndpointMessageRequestTypeDef(
    _RequiredCreateEndpointMessageRequestTypeDef, _OptionalCreateEndpointMessageRequestTypeDef
):
    pass

CreateEndpointResponseTypeDef = TypedDict(
    "CreateEndpointResponseTypeDef",
    {
        "Endpoint": "EndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventSubscriptionMessageRequestTypeDef = TypedDict(
    "_RequiredCreateEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "SnsTopicArn": str,
    },
)
_OptionalCreateEventSubscriptionMessageRequestTypeDef = TypedDict(
    "_OptionalCreateEventSubscriptionMessageRequestTypeDef",
    {
        "SourceType": str,
        "EventCategories": List[str],
        "SourceIds": List[str],
        "Enabled": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateEventSubscriptionMessageRequestTypeDef(
    _RequiredCreateEventSubscriptionMessageRequestTypeDef,
    _OptionalCreateEventSubscriptionMessageRequestTypeDef,
):
    pass

CreateEventSubscriptionResponseTypeDef = TypedDict(
    "CreateEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFleetAdvisorCollectorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFleetAdvisorCollectorRequestRequestTypeDef",
    {
        "CollectorName": str,
        "ServiceAccessRoleArn": str,
        "S3BucketName": str,
    },
)
_OptionalCreateFleetAdvisorCollectorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFleetAdvisorCollectorRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class CreateFleetAdvisorCollectorRequestRequestTypeDef(
    _RequiredCreateFleetAdvisorCollectorRequestRequestTypeDef,
    _OptionalCreateFleetAdvisorCollectorRequestRequestTypeDef,
):
    pass

CreateFleetAdvisorCollectorResponseTypeDef = TypedDict(
    "CreateFleetAdvisorCollectorResponseTypeDef",
    {
        "CollectorReferencedId": str,
        "CollectorName": str,
        "Description": str,
        "ServiceAccessRoleArn": str,
        "S3BucketName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstanceProfileMessageRequestTypeDef = TypedDict(
    "CreateInstanceProfileMessageRequestTypeDef",
    {
        "AvailabilityZone": str,
        "KmsKeyArn": str,
        "PubliclyAccessible": bool,
        "Tags": List["TagTypeDef"],
        "NetworkType": str,
        "InstanceProfileName": str,
        "Description": str,
        "SubnetGroupIdentifier": str,
        "VpcSecurityGroups": List[str],
    },
    total=False,
)

CreateInstanceProfileResponseTypeDef = TypedDict(
    "CreateInstanceProfileResponseTypeDef",
    {
        "InstanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMigrationProjectMessageRequestTypeDef = TypedDict(
    "_RequiredCreateMigrationProjectMessageRequestTypeDef",
    {
        "SourceDataProviderDescriptors": List["DataProviderDescriptorDefinitionTypeDef"],
        "TargetDataProviderDescriptors": List["DataProviderDescriptorDefinitionTypeDef"],
        "InstanceProfileIdentifier": str,
    },
)
_OptionalCreateMigrationProjectMessageRequestTypeDef = TypedDict(
    "_OptionalCreateMigrationProjectMessageRequestTypeDef",
    {
        "MigrationProjectName": str,
        "TransformationRules": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
        "SchemaConversionApplicationAttributes": "SCApplicationAttributesTypeDef",
    },
    total=False,
)

class CreateMigrationProjectMessageRequestTypeDef(
    _RequiredCreateMigrationProjectMessageRequestTypeDef,
    _OptionalCreateMigrationProjectMessageRequestTypeDef,
):
    pass

CreateMigrationProjectResponseTypeDef = TypedDict(
    "CreateMigrationProjectResponseTypeDef",
    {
        "MigrationProject": "MigrationProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplicationConfigMessageRequestTypeDef = TypedDict(
    "_RequiredCreateReplicationConfigMessageRequestTypeDef",
    {
        "ReplicationConfigIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ComputeConfig": "ComputeConfigTypeDef",
        "ReplicationType": MigrationTypeValueType,
        "TableMappings": str,
    },
)
_OptionalCreateReplicationConfigMessageRequestTypeDef = TypedDict(
    "_OptionalCreateReplicationConfigMessageRequestTypeDef",
    {
        "ReplicationSettings": str,
        "SupplementalSettings": str,
        "ResourceIdentifier": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateReplicationConfigMessageRequestTypeDef(
    _RequiredCreateReplicationConfigMessageRequestTypeDef,
    _OptionalCreateReplicationConfigMessageRequestTypeDef,
):
    pass

CreateReplicationConfigResponseTypeDef = TypedDict(
    "CreateReplicationConfigResponseTypeDef",
    {
        "ReplicationConfig": "ReplicationConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplicationInstanceMessageRequestTypeDef = TypedDict(
    "_RequiredCreateReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
    },
)
_OptionalCreateReplicationInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalCreateReplicationInstanceMessageRequestTypeDef",
    {
        "AllocatedStorage": int,
        "VpcSecurityGroupIds": List[str],
        "AvailabilityZone": str,
        "ReplicationSubnetGroupIdentifier": str,
        "PreferredMaintenanceWindow": str,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "Tags": List["TagTypeDef"],
        "KmsKeyId": str,
        "PubliclyAccessible": bool,
        "DnsNameServers": str,
        "ResourceIdentifier": str,
        "NetworkType": str,
    },
    total=False,
)

class CreateReplicationInstanceMessageRequestTypeDef(
    _RequiredCreateReplicationInstanceMessageRequestTypeDef,
    _OptionalCreateReplicationInstanceMessageRequestTypeDef,
):
    pass

CreateReplicationInstanceResponseTypeDef = TypedDict(
    "CreateReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "_RequiredCreateReplicationSubnetGroupMessageRequestTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "_OptionalCreateReplicationSubnetGroupMessageRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateReplicationSubnetGroupMessageRequestTypeDef(
    _RequiredCreateReplicationSubnetGroupMessageRequestTypeDef,
    _OptionalCreateReplicationSubnetGroupMessageRequestTypeDef,
):
    pass

CreateReplicationSubnetGroupResponseTypeDef = TypedDict(
    "CreateReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": "ReplicationSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplicationTaskMessageRequestTypeDef = TypedDict(
    "_RequiredCreateReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": MigrationTypeValueType,
        "TableMappings": str,
    },
)
_OptionalCreateReplicationTaskMessageRequestTypeDef = TypedDict(
    "_OptionalCreateReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskSettings": str,
        "CdcStartTime": Union[datetime, str],
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "Tags": List["TagTypeDef"],
        "TaskData": str,
        "ResourceIdentifier": str,
    },
    total=False,
)

class CreateReplicationTaskMessageRequestTypeDef(
    _RequiredCreateReplicationTaskMessageRequestTypeDef,
    _OptionalCreateReplicationTaskMessageRequestTypeDef,
):
    pass

CreateReplicationTaskResponseTypeDef = TypedDict(
    "CreateReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDataProviderDescriptorDefinitionTypeDef = TypedDict(
    "_RequiredDataProviderDescriptorDefinitionTypeDef",
    {
        "DataProviderIdentifier": str,
    },
)
_OptionalDataProviderDescriptorDefinitionTypeDef = TypedDict(
    "_OptionalDataProviderDescriptorDefinitionTypeDef",
    {
        "SecretsManagerSecretId": str,
        "SecretsManagerAccessRoleArn": str,
    },
    total=False,
)

class DataProviderDescriptorDefinitionTypeDef(
    _RequiredDataProviderDescriptorDefinitionTypeDef,
    _OptionalDataProviderDescriptorDefinitionTypeDef,
):
    pass

DataProviderDescriptorTypeDef = TypedDict(
    "DataProviderDescriptorTypeDef",
    {
        "SecretsManagerSecretId": str,
        "SecretsManagerAccessRoleArn": str,
        "DataProviderName": str,
        "DataProviderArn": str,
    },
    total=False,
)

DataProviderSettingsTypeDef = TypedDict(
    "DataProviderSettingsTypeDef",
    {
        "RedshiftSettings": "RedshiftDataProviderSettingsTypeDef",
        "PostgreSqlSettings": "PostgreSqlDataProviderSettingsTypeDef",
        "MySqlSettings": "MySqlDataProviderSettingsTypeDef",
        "OracleSettings": "OracleDataProviderSettingsTypeDef",
        "MicrosoftSqlServerSettings": "MicrosoftSqlServerDataProviderSettingsTypeDef",
        "DocDbSettings": "DocDbDataProviderSettingsTypeDef",
        "MariaDbSettings": "MariaDbDataProviderSettingsTypeDef",
        "MongoDbSettings": "MongoDbDataProviderSettingsTypeDef",
    },
    total=False,
)

DataProviderTypeDef = TypedDict(
    "DataProviderTypeDef",
    {
        "DataProviderName": str,
        "DataProviderArn": str,
        "DataProviderCreationTime": datetime,
        "Description": str,
        "Engine": str,
        "Settings": "DataProviderSettingsTypeDef",
    },
    total=False,
)

DatabaseInstanceSoftwareDetailsResponseTypeDef = TypedDict(
    "DatabaseInstanceSoftwareDetailsResponseTypeDef",
    {
        "Engine": str,
        "EngineVersion": str,
        "EngineEdition": str,
        "ServicePack": str,
        "SupportLevel": str,
        "OsArchitecture": int,
        "Tooltip": str,
    },
    total=False,
)

DatabaseResponseTypeDef = TypedDict(
    "DatabaseResponseTypeDef",
    {
        "DatabaseId": str,
        "DatabaseName": str,
        "IpAddress": str,
        "NumberOfSchemas": int,
        "Server": "ServerShortInfoResponseTypeDef",
        "SoftwareDetails": "DatabaseInstanceSoftwareDetailsResponseTypeDef",
        "Collectors": List["CollectorShortInfoResponseTypeDef"],
    },
    total=False,
)

DatabaseShortInfoResponseTypeDef = TypedDict(
    "DatabaseShortInfoResponseTypeDef",
    {
        "DatabaseId": str,
        "DatabaseName": str,
        "DatabaseIpAddress": str,
        "DatabaseEngine": str,
    },
    total=False,
)

DefaultErrorDetailsTypeDef = TypedDict(
    "DefaultErrorDetailsTypeDef",
    {
        "Message": str,
    },
    total=False,
)

DeleteCertificateMessageRequestTypeDef = TypedDict(
    "DeleteCertificateMessageRequestTypeDef",
    {
        "CertificateArn": str,
    },
)

DeleteCertificateResponseTypeDef = TypedDict(
    "DeleteCertificateResponseTypeDef",
    {
        "Certificate": "CertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCollectorRequestRequestTypeDef = TypedDict(
    "DeleteCollectorRequestRequestTypeDef",
    {
        "CollectorReferencedId": str,
    },
)

DeleteConnectionMessageRequestTypeDef = TypedDict(
    "DeleteConnectionMessageRequestTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
    },
)

DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataProviderMessageRequestTypeDef = TypedDict(
    "DeleteDataProviderMessageRequestTypeDef",
    {
        "DataProviderIdentifier": str,
    },
)

DeleteDataProviderResponseTypeDef = TypedDict(
    "DeleteDataProviderResponseTypeDef",
    {
        "DataProvider": "DataProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointMessageRequestTypeDef = TypedDict(
    "DeleteEndpointMessageRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

DeleteEndpointResponseTypeDef = TypedDict(
    "DeleteEndpointResponseTypeDef",
    {
        "Endpoint": "EndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEventSubscriptionMessageRequestTypeDef = TypedDict(
    "DeleteEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
    },
)

DeleteEventSubscriptionResponseTypeDef = TypedDict(
    "DeleteEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFleetAdvisorDatabasesRequestRequestTypeDef = TypedDict(
    "DeleteFleetAdvisorDatabasesRequestRequestTypeDef",
    {
        "DatabaseIds": List[str],
    },
)

DeleteFleetAdvisorDatabasesResponseTypeDef = TypedDict(
    "DeleteFleetAdvisorDatabasesResponseTypeDef",
    {
        "DatabaseIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInstanceProfileMessageRequestTypeDef = TypedDict(
    "DeleteInstanceProfileMessageRequestTypeDef",
    {
        "InstanceProfileIdentifier": str,
    },
)

DeleteInstanceProfileResponseTypeDef = TypedDict(
    "DeleteInstanceProfileResponseTypeDef",
    {
        "InstanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMigrationProjectMessageRequestTypeDef = TypedDict(
    "DeleteMigrationProjectMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
    },
)

DeleteMigrationProjectResponseTypeDef = TypedDict(
    "DeleteMigrationProjectResponseTypeDef",
    {
        "MigrationProject": "MigrationProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicationConfigMessageRequestTypeDef = TypedDict(
    "DeleteReplicationConfigMessageRequestTypeDef",
    {
        "ReplicationConfigArn": str,
    },
)

DeleteReplicationConfigResponseTypeDef = TypedDict(
    "DeleteReplicationConfigResponseTypeDef",
    {
        "ReplicationConfig": "ReplicationConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicationInstanceMessageRequestTypeDef = TypedDict(
    "DeleteReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
    },
)

DeleteReplicationInstanceResponseTypeDef = TypedDict(
    "DeleteReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "DeleteReplicationSubnetGroupMessageRequestTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
    },
)

DeleteReplicationTaskAssessmentRunMessageRequestTypeDef = TypedDict(
    "DeleteReplicationTaskAssessmentRunMessageRequestTypeDef",
    {
        "ReplicationTaskAssessmentRunArn": str,
    },
)

DeleteReplicationTaskAssessmentRunResponseTypeDef = TypedDict(
    "DeleteReplicationTaskAssessmentRunResponseTypeDef",
    {
        "ReplicationTaskAssessmentRun": "ReplicationTaskAssessmentRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReplicationTaskMessageRequestTypeDef = TypedDict(
    "DeleteReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)

DeleteReplicationTaskResponseTypeDef = TypedDict(
    "DeleteReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountAttributesResponseTypeDef = TypedDict(
    "DescribeAccountAttributesResponseTypeDef",
    {
        "AccountQuotas": List["AccountQuotaTypeDef"],
        "UniqueAccountIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicableIndividualAssessmentsMessageRequestTypeDef = TypedDict(
    "DescribeApplicableIndividualAssessmentsMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "ReplicationInstanceArn": str,
        "SourceEngineName": str,
        "TargetEngineName": str,
        "MigrationType": MigrationTypeValueType,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeApplicableIndividualAssessmentsResponseTypeDef = TypedDict(
    "DescribeApplicableIndividualAssessmentsResponseTypeDef",
    {
        "IndividualAssessmentNames": List[str],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCertificatesMessageRequestTypeDef = TypedDict(
    "DescribeCertificatesMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeCertificatesResponseTypeDef = TypedDict(
    "DescribeCertificatesResponseTypeDef",
    {
        "Marker": str,
        "Certificates": List["CertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectionsMessageRequestTypeDef = TypedDict(
    "DescribeConnectionsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeConnectionsResponseTypeDef = TypedDict(
    "DescribeConnectionsResponseTypeDef",
    {
        "Marker": str,
        "Connections": List["ConnectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConversionConfigurationMessageRequestTypeDef = TypedDict(
    "DescribeConversionConfigurationMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
    },
)

DescribeConversionConfigurationResponseTypeDef = TypedDict(
    "DescribeConversionConfigurationResponseTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "ConversionConfiguration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataProvidersMessageRequestTypeDef = TypedDict(
    "DescribeDataProvidersMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeDataProvidersResponseTypeDef = TypedDict(
    "DescribeDataProvidersResponseTypeDef",
    {
        "Marker": str,
        "DataProviders": List["DataProviderTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEndpointSettingsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeEndpointSettingsMessageRequestTypeDef",
    {
        "EngineName": str,
    },
)
_OptionalDescribeEndpointSettingsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeEndpointSettingsMessageRequestTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeEndpointSettingsMessageRequestTypeDef(
    _RequiredDescribeEndpointSettingsMessageRequestTypeDef,
    _OptionalDescribeEndpointSettingsMessageRequestTypeDef,
):
    pass

DescribeEndpointSettingsResponseTypeDef = TypedDict(
    "DescribeEndpointSettingsResponseTypeDef",
    {
        "Marker": str,
        "EndpointSettings": List["EndpointSettingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointTypesMessageRequestTypeDef = TypedDict(
    "DescribeEndpointTypesMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEndpointTypesResponseTypeDef = TypedDict(
    "DescribeEndpointTypesResponseTypeDef",
    {
        "Marker": str,
        "SupportedEndpointTypes": List["SupportedEndpointTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointsMessageRequestTypeDef = TypedDict(
    "DescribeEndpointsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Marker": str,
        "Endpoints": List["EndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEngineVersionsMessageRequestTypeDef = TypedDict(
    "DescribeEngineVersionsMessageRequestTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEngineVersionsResponseTypeDef = TypedDict(
    "DescribeEngineVersionsResponseTypeDef",
    {
        "EngineVersions": List["EngineVersionTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventCategoriesMessageRequestTypeDef = TypedDict(
    "DescribeEventCategoriesMessageRequestTypeDef",
    {
        "SourceType": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeEventCategoriesResponseTypeDef = TypedDict(
    "DescribeEventCategoriesResponseTypeDef",
    {
        "EventCategoryGroupList": List["EventCategoryGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventSubscriptionsMessageRequestTypeDef = TypedDict(
    "DescribeEventSubscriptionsMessageRequestTypeDef",
    {
        "SubscriptionName": str,
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEventSubscriptionsResponseTypeDef = TypedDict(
    "DescribeEventSubscriptionsResponseTypeDef",
    {
        "Marker": str,
        "EventSubscriptionsList": List["EventSubscriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsMessageRequestTypeDef = TypedDict(
    "DescribeEventsMessageRequestTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal["replication-instance"],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Duration": int,
        "EventCategories": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {
        "Marker": str,
        "Events": List["EventTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeExtensionPackAssociationsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeExtensionPackAssociationsMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
    },
)
_OptionalDescribeExtensionPackAssociationsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeExtensionPackAssociationsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

class DescribeExtensionPackAssociationsMessageRequestTypeDef(
    _RequiredDescribeExtensionPackAssociationsMessageRequestTypeDef,
    _OptionalDescribeExtensionPackAssociationsMessageRequestTypeDef,
):
    pass

DescribeExtensionPackAssociationsResponseTypeDef = TypedDict(
    "DescribeExtensionPackAssociationsResponseTypeDef",
    {
        "Marker": str,
        "Requests": List["SchemaConversionRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetAdvisorCollectorsRequestRequestTypeDef = TypedDict(
    "DescribeFleetAdvisorCollectorsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFleetAdvisorCollectorsResponseTypeDef = TypedDict(
    "DescribeFleetAdvisorCollectorsResponseTypeDef",
    {
        "Collectors": List["CollectorResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetAdvisorDatabasesRequestRequestTypeDef = TypedDict(
    "DescribeFleetAdvisorDatabasesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFleetAdvisorDatabasesResponseTypeDef = TypedDict(
    "DescribeFleetAdvisorDatabasesResponseTypeDef",
    {
        "Databases": List["DatabaseResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetAdvisorLsaAnalysisRequestRequestTypeDef = TypedDict(
    "DescribeFleetAdvisorLsaAnalysisRequestRequestTypeDef",
    {
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFleetAdvisorLsaAnalysisResponseTypeDef = TypedDict(
    "DescribeFleetAdvisorLsaAnalysisResponseTypeDef",
    {
        "Analysis": List["FleetAdvisorLsaAnalysisResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetAdvisorSchemaObjectSummaryRequestRequestTypeDef = TypedDict(
    "DescribeFleetAdvisorSchemaObjectSummaryRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef = TypedDict(
    "DescribeFleetAdvisorSchemaObjectSummaryResponseTypeDef",
    {
        "FleetAdvisorSchemaObjects": List["FleetAdvisorSchemaObjectResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetAdvisorSchemasRequestRequestTypeDef = TypedDict(
    "DescribeFleetAdvisorSchemasRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFleetAdvisorSchemasResponseTypeDef = TypedDict(
    "DescribeFleetAdvisorSchemasResponseTypeDef",
    {
        "FleetAdvisorSchemas": List["SchemaResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceProfilesMessageRequestTypeDef = TypedDict(
    "DescribeInstanceProfilesMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeInstanceProfilesResponseTypeDef = TypedDict(
    "DescribeInstanceProfilesResponseTypeDef",
    {
        "Marker": str,
        "InstanceProfiles": List["InstanceProfileTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMetadataModelAssessmentsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeMetadataModelAssessmentsMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
    },
)
_OptionalDescribeMetadataModelAssessmentsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeMetadataModelAssessmentsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

class DescribeMetadataModelAssessmentsMessageRequestTypeDef(
    _RequiredDescribeMetadataModelAssessmentsMessageRequestTypeDef,
    _OptionalDescribeMetadataModelAssessmentsMessageRequestTypeDef,
):
    pass

DescribeMetadataModelAssessmentsResponseTypeDef = TypedDict(
    "DescribeMetadataModelAssessmentsResponseTypeDef",
    {
        "Marker": str,
        "Requests": List["SchemaConversionRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMetadataModelConversionsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeMetadataModelConversionsMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
    },
)
_OptionalDescribeMetadataModelConversionsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeMetadataModelConversionsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

class DescribeMetadataModelConversionsMessageRequestTypeDef(
    _RequiredDescribeMetadataModelConversionsMessageRequestTypeDef,
    _OptionalDescribeMetadataModelConversionsMessageRequestTypeDef,
):
    pass

DescribeMetadataModelConversionsResponseTypeDef = TypedDict(
    "DescribeMetadataModelConversionsResponseTypeDef",
    {
        "Marker": str,
        "Requests": List["SchemaConversionRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMetadataModelExportsAsScriptMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeMetadataModelExportsAsScriptMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
    },
)
_OptionalDescribeMetadataModelExportsAsScriptMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeMetadataModelExportsAsScriptMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

class DescribeMetadataModelExportsAsScriptMessageRequestTypeDef(
    _RequiredDescribeMetadataModelExportsAsScriptMessageRequestTypeDef,
    _OptionalDescribeMetadataModelExportsAsScriptMessageRequestTypeDef,
):
    pass

DescribeMetadataModelExportsAsScriptResponseTypeDef = TypedDict(
    "DescribeMetadataModelExportsAsScriptResponseTypeDef",
    {
        "Marker": str,
        "Requests": List["SchemaConversionRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMetadataModelExportsToTargetMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeMetadataModelExportsToTargetMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
    },
)
_OptionalDescribeMetadataModelExportsToTargetMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeMetadataModelExportsToTargetMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

class DescribeMetadataModelExportsToTargetMessageRequestTypeDef(
    _RequiredDescribeMetadataModelExportsToTargetMessageRequestTypeDef,
    _OptionalDescribeMetadataModelExportsToTargetMessageRequestTypeDef,
):
    pass

DescribeMetadataModelExportsToTargetResponseTypeDef = TypedDict(
    "DescribeMetadataModelExportsToTargetResponseTypeDef",
    {
        "Marker": str,
        "Requests": List["SchemaConversionRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMetadataModelImportsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeMetadataModelImportsMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
    },
)
_OptionalDescribeMetadataModelImportsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeMetadataModelImportsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

class DescribeMetadataModelImportsMessageRequestTypeDef(
    _RequiredDescribeMetadataModelImportsMessageRequestTypeDef,
    _OptionalDescribeMetadataModelImportsMessageRequestTypeDef,
):
    pass

DescribeMetadataModelImportsResponseTypeDef = TypedDict(
    "DescribeMetadataModelImportsResponseTypeDef",
    {
        "Marker": str,
        "Requests": List["SchemaConversionRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMigrationProjectsMessageRequestTypeDef = TypedDict(
    "DescribeMigrationProjectsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeMigrationProjectsResponseTypeDef = TypedDict(
    "DescribeMigrationProjectsResponseTypeDef",
    {
        "Marker": str,
        "MigrationProjects": List["MigrationProjectTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrderableReplicationInstancesMessageRequestTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesMessageRequestTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeOrderableReplicationInstancesResponseTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesResponseTypeDef",
    {
        "OrderableReplicationInstances": List["OrderableReplicationInstanceTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePendingMaintenanceActionsMessageRequestTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "Filters": List["FilterTypeDef"],
        "Marker": str,
        "MaxRecords": int,
    },
    total=False,
)

DescribePendingMaintenanceActionsResponseTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsResponseTypeDef",
    {
        "PendingMaintenanceActions": List["ResourcePendingMaintenanceActionsTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecommendationLimitationsRequestRequestTypeDef = TypedDict(
    "DescribeRecommendationLimitationsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeRecommendationLimitationsResponseTypeDef = TypedDict(
    "DescribeRecommendationLimitationsResponseTypeDef",
    {
        "NextToken": str,
        "Limitations": List["LimitationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecommendationsRequestRequestTypeDef = TypedDict(
    "DescribeRecommendationsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeRecommendationsResponseTypeDef = TypedDict(
    "DescribeRecommendationsResponseTypeDef",
    {
        "NextToken": str,
        "Recommendations": List["RecommendationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRefreshSchemasStatusMessageRequestTypeDef = TypedDict(
    "DescribeRefreshSchemasStatusMessageRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

DescribeRefreshSchemasStatusResponseTypeDef = TypedDict(
    "DescribeRefreshSchemasStatusResponseTypeDef",
    {
        "RefreshSchemasStatus": "RefreshSchemasStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationConfigsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationConfigsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationConfigsResponseTypeDef = TypedDict(
    "DescribeReplicationConfigsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationConfigs": List["ReplicationConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeReplicationInstanceTaskLogsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeReplicationInstanceTaskLogsMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
    },
)
_OptionalDescribeReplicationInstanceTaskLogsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeReplicationInstanceTaskLogsMessageRequestTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeReplicationInstanceTaskLogsMessageRequestTypeDef(
    _RequiredDescribeReplicationInstanceTaskLogsMessageRequestTypeDef,
    _OptionalDescribeReplicationInstanceTaskLogsMessageRequestTypeDef,
):
    pass

DescribeReplicationInstanceTaskLogsResponseTypeDef = TypedDict(
    "DescribeReplicationInstanceTaskLogsResponseTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ReplicationInstanceTaskLogs": List["ReplicationInstanceTaskLogTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationInstancesMessageRequestTypeDef = TypedDict(
    "DescribeReplicationInstancesMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationInstancesResponseTypeDef = TypedDict(
    "DescribeReplicationInstancesResponseTypeDef",
    {
        "Marker": str,
        "ReplicationInstances": List["ReplicationInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationSubnetGroupsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationSubnetGroupsResponseTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationSubnetGroups": List["ReplicationSubnetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeReplicationTableStatisticsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeReplicationTableStatisticsMessageRequestTypeDef",
    {
        "ReplicationConfigArn": str,
    },
)
_OptionalDescribeReplicationTableStatisticsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeReplicationTableStatisticsMessageRequestTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

class DescribeReplicationTableStatisticsMessageRequestTypeDef(
    _RequiredDescribeReplicationTableStatisticsMessageRequestTypeDef,
    _OptionalDescribeReplicationTableStatisticsMessageRequestTypeDef,
):
    pass

DescribeReplicationTableStatisticsResponseTypeDef = TypedDict(
    "DescribeReplicationTableStatisticsResponseTypeDef",
    {
        "ReplicationConfigArn": str,
        "Marker": str,
        "ReplicationTableStatistics": List["TableStatisticsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTaskAssessmentResultsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationTaskAssessmentResultsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsResponseTypeDef",
    {
        "Marker": str,
        "BucketName": str,
        "ReplicationTaskAssessmentResults": List["ReplicationTaskAssessmentResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTaskAssessmentRunsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentRunsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationTaskAssessmentRunsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentRunsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTaskAssessmentRuns": List["ReplicationTaskAssessmentRunTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTaskIndividualAssessmentsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTaskIndividualAssessmentsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationTaskIndividualAssessmentsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskIndividualAssessmentsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTaskIndividualAssessments": List["ReplicationTaskIndividualAssessmentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationTasksMessageRequestTypeDef = TypedDict(
    "DescribeReplicationTasksMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
        "WithoutSettings": bool,
    },
    total=False,
)

DescribeReplicationTasksResponseTypeDef = TypedDict(
    "DescribeReplicationTasksResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTasks": List["ReplicationTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplicationsMessageRequestTypeDef = TypedDict(
    "DescribeReplicationsMessageRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

DescribeReplicationsResponseTypeDef = TypedDict(
    "DescribeReplicationsResponseTypeDef",
    {
        "Marker": str,
        "Replications": List["ReplicationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSchemasMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeSchemasMessageRequestTypeDef",
    {
        "EndpointArn": str,
    },
)
_OptionalDescribeSchemasMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeSchemasMessageRequestTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
    },
    total=False,
)

class DescribeSchemasMessageRequestTypeDef(
    _RequiredDescribeSchemasMessageRequestTypeDef, _OptionalDescribeSchemasMessageRequestTypeDef
):
    pass

DescribeSchemasResponseTypeDef = TypedDict(
    "DescribeSchemasResponseTypeDef",
    {
        "Marker": str,
        "Schemas": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTableStatisticsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeTableStatisticsMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)
_OptionalDescribeTableStatisticsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeTableStatisticsMessageRequestTypeDef",
    {
        "MaxRecords": int,
        "Marker": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

class DescribeTableStatisticsMessageRequestTypeDef(
    _RequiredDescribeTableStatisticsMessageRequestTypeDef,
    _OptionalDescribeTableStatisticsMessageRequestTypeDef,
):
    pass

DescribeTableStatisticsResponseTypeDef = TypedDict(
    "DescribeTableStatisticsResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "TableStatistics": List["TableStatisticsTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DmsTransferSettingsTypeDef = TypedDict(
    "DmsTransferSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "BucketName": str,
    },
    total=False,
)

DocDbDataProviderSettingsTypeDef = TypedDict(
    "DocDbDataProviderSettingsTypeDef",
    {
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "SslMode": DmsSslModeValueType,
        "CertificateArn": str,
    },
    total=False,
)

DocDbSettingsTypeDef = TypedDict(
    "DocDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "NestingLevel": NestingLevelValueType,
        "ExtractDocId": bool,
        "DocsToInvestigate": int,
        "KmsKeyId": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
        "UseUpdateLookUp": bool,
        "ReplicateShardCollections": bool,
    },
    total=False,
)

DynamoDbSettingsTypeDef = TypedDict(
    "DynamoDbSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
    },
)

_RequiredElasticsearchSettingsTypeDef = TypedDict(
    "_RequiredElasticsearchSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "EndpointUri": str,
    },
)
_OptionalElasticsearchSettingsTypeDef = TypedDict(
    "_OptionalElasticsearchSettingsTypeDef",
    {
        "FullLoadErrorPercentage": int,
        "ErrorRetryDuration": int,
        "UseNewMappingType": bool,
    },
    total=False,
)

class ElasticsearchSettingsTypeDef(
    _RequiredElasticsearchSettingsTypeDef, _OptionalElasticsearchSettingsTypeDef
):
    pass

EndpointSettingTypeDef = TypedDict(
    "EndpointSettingTypeDef",
    {
        "Name": str,
        "Type": EndpointSettingTypeValueType,
        "EnumValues": List[str],
        "Sensitive": bool,
        "Units": str,
        "Applicability": str,
        "IntValueMin": int,
        "IntValueMax": int,
        "DefaultValue": str,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": ReplicationEndpointTypeValueType,
        "EngineName": str,
        "EngineDisplayName": str,
        "Username": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "Status": str,
        "KmsKeyId": str,
        "EndpointArn": str,
        "CertificateArn": str,
        "SslMode": DmsSslModeValueType,
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "ExternalId": str,
        "DynamoDbSettings": "DynamoDbSettingsTypeDef",
        "S3Settings": "S3SettingsTypeDef",
        "DmsTransferSettings": "DmsTransferSettingsTypeDef",
        "MongoDbSettings": "MongoDbSettingsTypeDef",
        "KinesisSettings": "KinesisSettingsTypeDef",
        "KafkaSettings": "KafkaSettingsTypeDef",
        "ElasticsearchSettings": "ElasticsearchSettingsTypeDef",
        "NeptuneSettings": "NeptuneSettingsTypeDef",
        "RedshiftSettings": "RedshiftSettingsTypeDef",
        "PostgreSQLSettings": "PostgreSQLSettingsTypeDef",
        "MySQLSettings": "MySQLSettingsTypeDef",
        "OracleSettings": "OracleSettingsTypeDef",
        "SybaseSettings": "SybaseSettingsTypeDef",
        "MicrosoftSQLServerSettings": "MicrosoftSQLServerSettingsTypeDef",
        "IBMDb2Settings": "IBMDb2SettingsTypeDef",
        "DocDbSettings": "DocDbSettingsTypeDef",
        "RedisSettings": "RedisSettingsTypeDef",
        "GcpMySQLSettings": "GcpMySQLSettingsTypeDef",
        "TimestreamSettings": "TimestreamSettingsTypeDef",
    },
    total=False,
)

EngineVersionTypeDef = TypedDict(
    "EngineVersionTypeDef",
    {
        "Version": str,
        "Lifecycle": str,
        "ReleaseStatus": ReleaseStatusValuesType,
        "LaunchDate": datetime,
        "AutoUpgradeDate": datetime,
        "DeprecationDate": datetime,
        "ForceUpgradeDate": datetime,
        "AvailableUpgrades": List[str],
    },
    total=False,
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "defaultErrorDetails": "DefaultErrorDetailsTypeDef",
    },
    total=False,
)

EventCategoryGroupTypeDef = TypedDict(
    "EventCategoryGroupTypeDef",
    {
        "SourceType": str,
        "EventCategories": List[str],
    },
    total=False,
)

EventSubscriptionTypeDef = TypedDict(
    "EventSubscriptionTypeDef",
    {
        "CustomerAwsId": str,
        "CustSubscriptionId": str,
        "SnsTopicArn": str,
        "Status": str,
        "SubscriptionCreationTime": str,
        "SourceType": str,
        "SourceIdsList": List[str],
        "EventCategoriesList": List[str],
        "Enabled": bool,
    },
    total=False,
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "SourceIdentifier": str,
        "SourceType": Literal["replication-instance"],
        "Message": str,
        "EventCategories": List[str],
        "Date": datetime,
    },
    total=False,
)

_RequiredExportMetadataModelAssessmentMessageRequestTypeDef = TypedDict(
    "_RequiredExportMetadataModelAssessmentMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "SelectionRules": str,
    },
)
_OptionalExportMetadataModelAssessmentMessageRequestTypeDef = TypedDict(
    "_OptionalExportMetadataModelAssessmentMessageRequestTypeDef",
    {
        "FileName": str,
        "AssessmentReportTypes": List[AssessmentReportTypeType],
    },
    total=False,
)

class ExportMetadataModelAssessmentMessageRequestTypeDef(
    _RequiredExportMetadataModelAssessmentMessageRequestTypeDef,
    _OptionalExportMetadataModelAssessmentMessageRequestTypeDef,
):
    pass

ExportMetadataModelAssessmentResponseTypeDef = TypedDict(
    "ExportMetadataModelAssessmentResponseTypeDef",
    {
        "PdfReport": "ExportMetadataModelAssessmentResultEntryTypeDef",
        "CsvReport": "ExportMetadataModelAssessmentResultEntryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportMetadataModelAssessmentResultEntryTypeDef = TypedDict(
    "ExportMetadataModelAssessmentResultEntryTypeDef",
    {
        "S3ObjectKey": str,
        "ObjectURL": str,
    },
    total=False,
)

ExportSqlDetailsTypeDef = TypedDict(
    "ExportSqlDetailsTypeDef",
    {
        "S3ObjectKey": str,
        "ObjectURL": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
)

FleetAdvisorLsaAnalysisResponseTypeDef = TypedDict(
    "FleetAdvisorLsaAnalysisResponseTypeDef",
    {
        "LsaAnalysisId": str,
        "Status": str,
    },
    total=False,
)

FleetAdvisorSchemaObjectResponseTypeDef = TypedDict(
    "FleetAdvisorSchemaObjectResponseTypeDef",
    {
        "SchemaId": str,
        "ObjectType": str,
        "NumberOfObjects": int,
        "CodeLineCount": int,
        "CodeSize": int,
    },
    total=False,
)

GcpMySQLSettingsTypeDef = TypedDict(
    "GcpMySQLSettingsTypeDef",
    {
        "AfterConnectScript": str,
        "CleanSourceMetadataOnMismatch": bool,
        "DatabaseName": str,
        "EventsPollInterval": int,
        "TargetDbType": TargetDbTypeType,
        "MaxFileSize": int,
        "ParallelLoadThreads": int,
        "Password": str,
        "Port": int,
        "ServerName": str,
        "ServerTimezone": str,
        "Username": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

IBMDb2SettingsTypeDef = TypedDict(
    "IBMDb2SettingsTypeDef",
    {
        "DatabaseName": str,
        "Password": str,
        "Port": int,
        "ServerName": str,
        "SetDataCaptureChanges": bool,
        "CurrentLsn": str,
        "MaxKBytesPerRead": int,
        "Username": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
        "LoadTimeout": int,
        "WriteBufferSize": int,
        "MaxFileSize": int,
        "KeepCsvFiles": bool,
    },
    total=False,
)

_RequiredImportCertificateMessageRequestTypeDef = TypedDict(
    "_RequiredImportCertificateMessageRequestTypeDef",
    {
        "CertificateIdentifier": str,
    },
)
_OptionalImportCertificateMessageRequestTypeDef = TypedDict(
    "_OptionalImportCertificateMessageRequestTypeDef",
    {
        "CertificatePem": str,
        "CertificateWallet": Union[bytes, IO[bytes], StreamingBody],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class ImportCertificateMessageRequestTypeDef(
    _RequiredImportCertificateMessageRequestTypeDef, _OptionalImportCertificateMessageRequestTypeDef
):
    pass

ImportCertificateResponseTypeDef = TypedDict(
    "ImportCertificateResponseTypeDef",
    {
        "Certificate": "CertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceProfileTypeDef = TypedDict(
    "InstanceProfileTypeDef",
    {
        "InstanceProfileArn": str,
        "AvailabilityZone": str,
        "KmsKeyArn": str,
        "PubliclyAccessible": bool,
        "NetworkType": str,
        "InstanceProfileName": str,
        "Description": str,
        "InstanceProfileCreationTime": datetime,
        "SubnetGroupIdentifier": str,
        "VpcSecurityGroups": List[str],
    },
    total=False,
)

InventoryDataTypeDef = TypedDict(
    "InventoryDataTypeDef",
    {
        "NumberOfDatabases": int,
        "NumberOfSchemas": int,
    },
    total=False,
)

KafkaSettingsTypeDef = TypedDict(
    "KafkaSettingsTypeDef",
    {
        "Broker": str,
        "Topic": str,
        "MessageFormat": MessageFormatValueType,
        "IncludeTransactionDetails": bool,
        "IncludePartitionValue": bool,
        "PartitionIncludeSchemaTable": bool,
        "IncludeTableAlterOperations": bool,
        "IncludeControlDetails": bool,
        "MessageMaxBytes": int,
        "IncludeNullAndEmpty": bool,
        "SecurityProtocol": KafkaSecurityProtocolType,
        "SslClientCertificateArn": str,
        "SslClientKeyArn": str,
        "SslClientKeyPassword": str,
        "SslCaCertificateArn": str,
        "SaslUsername": str,
        "SaslPassword": str,
        "NoHexPrefix": bool,
        "SaslMechanism": KafkaSaslMechanismType,
        "SslEndpointIdentificationAlgorithm": KafkaSslEndpointIdentificationAlgorithmType,
    },
    total=False,
)

KinesisSettingsTypeDef = TypedDict(
    "KinesisSettingsTypeDef",
    {
        "StreamArn": str,
        "MessageFormat": MessageFormatValueType,
        "ServiceAccessRoleArn": str,
        "IncludeTransactionDetails": bool,
        "IncludePartitionValue": bool,
        "PartitionIncludeSchemaTable": bool,
        "IncludeTableAlterOperations": bool,
        "IncludeControlDetails": bool,
        "IncludeNullAndEmpty": bool,
        "NoHexPrefix": bool,
    },
    total=False,
)

LimitationTypeDef = TypedDict(
    "LimitationTypeDef",
    {
        "DatabaseId": str,
        "EngineName": str,
        "Name": str,
        "Description": str,
        "Impact": str,
        "Type": str,
    },
    total=False,
)

ListTagsForResourceMessageRequestTypeDef = TypedDict(
    "ListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceArn": str,
        "ResourceArnList": List[str],
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MariaDbDataProviderSettingsTypeDef = TypedDict(
    "MariaDbDataProviderSettingsTypeDef",
    {
        "ServerName": str,
        "Port": int,
        "SslMode": DmsSslModeValueType,
        "CertificateArn": str,
    },
    total=False,
)

MicrosoftSQLServerSettingsTypeDef = TypedDict(
    "MicrosoftSQLServerSettingsTypeDef",
    {
        "Port": int,
        "BcpPacketSize": int,
        "DatabaseName": str,
        "ControlTablesFileGroup": str,
        "Password": str,
        "QuerySingleAlwaysOnNode": bool,
        "ReadBackupOnly": bool,
        "SafeguardPolicy": SafeguardPolicyType,
        "ServerName": str,
        "Username": str,
        "UseBcpFullLoad": bool,
        "UseThirdPartyBackupDevice": bool,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
        "TrimSpaceInChar": bool,
        "TlogAccessMode": TlogAccessModeType,
        "ForceLobLookup": bool,
    },
    total=False,
)

MicrosoftSqlServerDataProviderSettingsTypeDef = TypedDict(
    "MicrosoftSqlServerDataProviderSettingsTypeDef",
    {
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "SslMode": DmsSslModeValueType,
        "CertificateArn": str,
    },
    total=False,
)

MigrationProjectTypeDef = TypedDict(
    "MigrationProjectTypeDef",
    {
        "MigrationProjectName": str,
        "MigrationProjectArn": str,
        "MigrationProjectCreationTime": datetime,
        "SourceDataProviderDescriptors": List["DataProviderDescriptorTypeDef"],
        "TargetDataProviderDescriptors": List["DataProviderDescriptorTypeDef"],
        "InstanceProfileArn": str,
        "InstanceProfileName": str,
        "TransformationRules": str,
        "Description": str,
        "SchemaConversionApplicationAttributes": "SCApplicationAttributesTypeDef",
    },
    total=False,
)

ModifyConversionConfigurationMessageRequestTypeDef = TypedDict(
    "ModifyConversionConfigurationMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "ConversionConfiguration": str,
    },
)

ModifyConversionConfigurationResponseTypeDef = TypedDict(
    "ModifyConversionConfigurationResponseTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDataProviderMessageRequestTypeDef = TypedDict(
    "_RequiredModifyDataProviderMessageRequestTypeDef",
    {
        "DataProviderIdentifier": str,
    },
)
_OptionalModifyDataProviderMessageRequestTypeDef = TypedDict(
    "_OptionalModifyDataProviderMessageRequestTypeDef",
    {
        "DataProviderName": str,
        "Description": str,
        "Engine": str,
        "ExactSettings": bool,
        "Settings": "DataProviderSettingsTypeDef",
    },
    total=False,
)

class ModifyDataProviderMessageRequestTypeDef(
    _RequiredModifyDataProviderMessageRequestTypeDef,
    _OptionalModifyDataProviderMessageRequestTypeDef,
):
    pass

ModifyDataProviderResponseTypeDef = TypedDict(
    "ModifyDataProviderResponseTypeDef",
    {
        "DataProvider": "DataProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyEndpointMessageRequestTypeDef = TypedDict(
    "_RequiredModifyEndpointMessageRequestTypeDef",
    {
        "EndpointArn": str,
    },
)
_OptionalModifyEndpointMessageRequestTypeDef = TypedDict(
    "_OptionalModifyEndpointMessageRequestTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": ReplicationEndpointTypeValueType,
        "EngineName": str,
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "ExtraConnectionAttributes": str,
        "CertificateArn": str,
        "SslMode": DmsSslModeValueType,
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "DynamoDbSettings": "DynamoDbSettingsTypeDef",
        "S3Settings": "S3SettingsTypeDef",
        "DmsTransferSettings": "DmsTransferSettingsTypeDef",
        "MongoDbSettings": "MongoDbSettingsTypeDef",
        "KinesisSettings": "KinesisSettingsTypeDef",
        "KafkaSettings": "KafkaSettingsTypeDef",
        "ElasticsearchSettings": "ElasticsearchSettingsTypeDef",
        "NeptuneSettings": "NeptuneSettingsTypeDef",
        "RedshiftSettings": "RedshiftSettingsTypeDef",
        "PostgreSQLSettings": "PostgreSQLSettingsTypeDef",
        "MySQLSettings": "MySQLSettingsTypeDef",
        "OracleSettings": "OracleSettingsTypeDef",
        "SybaseSettings": "SybaseSettingsTypeDef",
        "MicrosoftSQLServerSettings": "MicrosoftSQLServerSettingsTypeDef",
        "IBMDb2Settings": "IBMDb2SettingsTypeDef",
        "DocDbSettings": "DocDbSettingsTypeDef",
        "RedisSettings": "RedisSettingsTypeDef",
        "ExactSettings": bool,
        "GcpMySQLSettings": "GcpMySQLSettingsTypeDef",
        "TimestreamSettings": "TimestreamSettingsTypeDef",
    },
    total=False,
)

class ModifyEndpointMessageRequestTypeDef(
    _RequiredModifyEndpointMessageRequestTypeDef, _OptionalModifyEndpointMessageRequestTypeDef
):
    pass

ModifyEndpointResponseTypeDef = TypedDict(
    "ModifyEndpointResponseTypeDef",
    {
        "Endpoint": "EndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyEventSubscriptionMessageRequestTypeDef = TypedDict(
    "_RequiredModifyEventSubscriptionMessageRequestTypeDef",
    {
        "SubscriptionName": str,
    },
)
_OptionalModifyEventSubscriptionMessageRequestTypeDef = TypedDict(
    "_OptionalModifyEventSubscriptionMessageRequestTypeDef",
    {
        "SnsTopicArn": str,
        "SourceType": str,
        "EventCategories": List[str],
        "Enabled": bool,
    },
    total=False,
)

class ModifyEventSubscriptionMessageRequestTypeDef(
    _RequiredModifyEventSubscriptionMessageRequestTypeDef,
    _OptionalModifyEventSubscriptionMessageRequestTypeDef,
):
    pass

ModifyEventSubscriptionResponseTypeDef = TypedDict(
    "ModifyEventSubscriptionResponseTypeDef",
    {
        "EventSubscription": "EventSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyInstanceProfileMessageRequestTypeDef = TypedDict(
    "_RequiredModifyInstanceProfileMessageRequestTypeDef",
    {
        "InstanceProfileIdentifier": str,
    },
)
_OptionalModifyInstanceProfileMessageRequestTypeDef = TypedDict(
    "_OptionalModifyInstanceProfileMessageRequestTypeDef",
    {
        "AvailabilityZone": str,
        "KmsKeyArn": str,
        "PubliclyAccessible": bool,
        "NetworkType": str,
        "InstanceProfileName": str,
        "Description": str,
        "SubnetGroupIdentifier": str,
        "VpcSecurityGroups": List[str],
    },
    total=False,
)

class ModifyInstanceProfileMessageRequestTypeDef(
    _RequiredModifyInstanceProfileMessageRequestTypeDef,
    _OptionalModifyInstanceProfileMessageRequestTypeDef,
):
    pass

ModifyInstanceProfileResponseTypeDef = TypedDict(
    "ModifyInstanceProfileResponseTypeDef",
    {
        "InstanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyMigrationProjectMessageRequestTypeDef = TypedDict(
    "_RequiredModifyMigrationProjectMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
    },
)
_OptionalModifyMigrationProjectMessageRequestTypeDef = TypedDict(
    "_OptionalModifyMigrationProjectMessageRequestTypeDef",
    {
        "MigrationProjectName": str,
        "SourceDataProviderDescriptors": List["DataProviderDescriptorDefinitionTypeDef"],
        "TargetDataProviderDescriptors": List["DataProviderDescriptorDefinitionTypeDef"],
        "InstanceProfileIdentifier": str,
        "TransformationRules": str,
        "Description": str,
        "SchemaConversionApplicationAttributes": "SCApplicationAttributesTypeDef",
    },
    total=False,
)

class ModifyMigrationProjectMessageRequestTypeDef(
    _RequiredModifyMigrationProjectMessageRequestTypeDef,
    _OptionalModifyMigrationProjectMessageRequestTypeDef,
):
    pass

ModifyMigrationProjectResponseTypeDef = TypedDict(
    "ModifyMigrationProjectResponseTypeDef",
    {
        "MigrationProject": "MigrationProjectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyReplicationConfigMessageRequestTypeDef = TypedDict(
    "_RequiredModifyReplicationConfigMessageRequestTypeDef",
    {
        "ReplicationConfigArn": str,
    },
)
_OptionalModifyReplicationConfigMessageRequestTypeDef = TypedDict(
    "_OptionalModifyReplicationConfigMessageRequestTypeDef",
    {
        "ReplicationConfigIdentifier": str,
        "ReplicationType": MigrationTypeValueType,
        "TableMappings": str,
        "ReplicationSettings": str,
        "SupplementalSettings": str,
        "ComputeConfig": "ComputeConfigTypeDef",
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
    },
    total=False,
)

class ModifyReplicationConfigMessageRequestTypeDef(
    _RequiredModifyReplicationConfigMessageRequestTypeDef,
    _OptionalModifyReplicationConfigMessageRequestTypeDef,
):
    pass

ModifyReplicationConfigResponseTypeDef = TypedDict(
    "ModifyReplicationConfigResponseTypeDef",
    {
        "ReplicationConfig": "ReplicationConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyReplicationInstanceMessageRequestTypeDef = TypedDict(
    "_RequiredModifyReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
    },
)
_OptionalModifyReplicationInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalModifyReplicationInstanceMessageRequestTypeDef",
    {
        "AllocatedStorage": int,
        "ApplyImmediately": bool,
        "ReplicationInstanceClass": str,
        "VpcSecurityGroupIds": List[str],
        "PreferredMaintenanceWindow": str,
        "MultiAZ": bool,
        "EngineVersion": str,
        "AllowMajorVersionUpgrade": bool,
        "AutoMinorVersionUpgrade": bool,
        "ReplicationInstanceIdentifier": str,
        "NetworkType": str,
    },
    total=False,
)

class ModifyReplicationInstanceMessageRequestTypeDef(
    _RequiredModifyReplicationInstanceMessageRequestTypeDef,
    _OptionalModifyReplicationInstanceMessageRequestTypeDef,
):
    pass

ModifyReplicationInstanceResponseTypeDef = TypedDict(
    "ModifyReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "_RequiredModifyReplicationSubnetGroupMessageRequestTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "SubnetIds": List[str],
    },
)
_OptionalModifyReplicationSubnetGroupMessageRequestTypeDef = TypedDict(
    "_OptionalModifyReplicationSubnetGroupMessageRequestTypeDef",
    {
        "ReplicationSubnetGroupDescription": str,
    },
    total=False,
)

class ModifyReplicationSubnetGroupMessageRequestTypeDef(
    _RequiredModifyReplicationSubnetGroupMessageRequestTypeDef,
    _OptionalModifyReplicationSubnetGroupMessageRequestTypeDef,
):
    pass

ModifyReplicationSubnetGroupResponseTypeDef = TypedDict(
    "ModifyReplicationSubnetGroupResponseTypeDef",
    {
        "ReplicationSubnetGroup": "ReplicationSubnetGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyReplicationTaskMessageRequestTypeDef = TypedDict(
    "_RequiredModifyReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)
_OptionalModifyReplicationTaskMessageRequestTypeDef = TypedDict(
    "_OptionalModifyReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "MigrationType": MigrationTypeValueType,
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "CdcStartTime": Union[datetime, str],
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "TaskData": str,
    },
    total=False,
)

class ModifyReplicationTaskMessageRequestTypeDef(
    _RequiredModifyReplicationTaskMessageRequestTypeDef,
    _OptionalModifyReplicationTaskMessageRequestTypeDef,
):
    pass

ModifyReplicationTaskResponseTypeDef = TypedDict(
    "ModifyReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MongoDbDataProviderSettingsTypeDef = TypedDict(
    "MongoDbDataProviderSettingsTypeDef",
    {
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "SslMode": DmsSslModeValueType,
        "CertificateArn": str,
        "AuthType": AuthTypeValueType,
        "AuthSource": str,
        "AuthMechanism": AuthMechanismValueType,
    },
    total=False,
)

MongoDbSettingsTypeDef = TypedDict(
    "MongoDbSettingsTypeDef",
    {
        "Username": str,
        "Password": str,
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "AuthType": AuthTypeValueType,
        "AuthMechanism": AuthMechanismValueType,
        "NestingLevel": NestingLevelValueType,
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
        "UseUpdateLookUp": bool,
        "ReplicateShardCollections": bool,
    },
    total=False,
)

MoveReplicationTaskMessageRequestTypeDef = TypedDict(
    "MoveReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "TargetReplicationInstanceArn": str,
    },
)

MoveReplicationTaskResponseTypeDef = TypedDict(
    "MoveReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MySQLSettingsTypeDef = TypedDict(
    "MySQLSettingsTypeDef",
    {
        "AfterConnectScript": str,
        "CleanSourceMetadataOnMismatch": bool,
        "DatabaseName": str,
        "EventsPollInterval": int,
        "TargetDbType": TargetDbTypeType,
        "MaxFileSize": int,
        "ParallelLoadThreads": int,
        "Password": str,
        "Port": int,
        "ServerName": str,
        "ServerTimezone": str,
        "Username": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
        "ExecuteTimeout": int,
    },
    total=False,
)

MySqlDataProviderSettingsTypeDef = TypedDict(
    "MySqlDataProviderSettingsTypeDef",
    {
        "ServerName": str,
        "Port": int,
        "SslMode": DmsSslModeValueType,
        "CertificateArn": str,
    },
    total=False,
)

_RequiredNeptuneSettingsTypeDef = TypedDict(
    "_RequiredNeptuneSettingsTypeDef",
    {
        "S3BucketName": str,
        "S3BucketFolder": str,
    },
)
_OptionalNeptuneSettingsTypeDef = TypedDict(
    "_OptionalNeptuneSettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ErrorRetryDuration": int,
        "MaxFileSize": int,
        "MaxRetryCount": int,
        "IamAuthEnabled": bool,
    },
    total=False,
)

class NeptuneSettingsTypeDef(_RequiredNeptuneSettingsTypeDef, _OptionalNeptuneSettingsTypeDef):
    pass

OracleDataProviderSettingsTypeDef = TypedDict(
    "OracleDataProviderSettingsTypeDef",
    {
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "SslMode": DmsSslModeValueType,
        "CertificateArn": str,
        "AsmServer": str,
        "SecretsManagerOracleAsmSecretId": str,
        "SecretsManagerOracleAsmAccessRoleArn": str,
        "SecretsManagerSecurityDbEncryptionSecretId": str,
        "SecretsManagerSecurityDbEncryptionAccessRoleArn": str,
    },
    total=False,
)

OracleSettingsTypeDef = TypedDict(
    "OracleSettingsTypeDef",
    {
        "AddSupplementalLogging": bool,
        "ArchivedLogDestId": int,
        "AdditionalArchivedLogDestId": int,
        "ExtraArchivedLogDestIds": List[int],
        "AllowSelectNestedTables": bool,
        "ParallelAsmReadThreads": int,
        "ReadAheadBlocks": int,
        "AccessAlternateDirectly": bool,
        "UseAlternateFolderForOnline": bool,
        "OraclePathPrefix": str,
        "UsePathPrefix": str,
        "ReplacePathPrefix": bool,
        "EnableHomogenousTablespace": bool,
        "DirectPathNoLog": bool,
        "ArchivedLogsOnly": bool,
        "AsmPassword": str,
        "AsmServer": str,
        "AsmUser": str,
        "CharLengthSemantics": CharLengthSemanticsType,
        "DatabaseName": str,
        "DirectPathParallelLoad": bool,
        "FailTasksOnLobTruncation": bool,
        "NumberDatatypeScale": int,
        "Password": str,
        "Port": int,
        "ReadTableSpaceName": bool,
        "RetryInterval": int,
        "SecurityDbEncryption": str,
        "SecurityDbEncryptionName": str,
        "ServerName": str,
        "SpatialDataOptionToGeoJsonFunctionName": str,
        "StandbyDelayTime": int,
        "Username": str,
        "UseBFile": bool,
        "UseDirectPathFullLoad": bool,
        "UseLogminerReader": bool,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
        "SecretsManagerOracleAsmAccessRoleArn": str,
        "SecretsManagerOracleAsmSecretId": str,
        "TrimSpaceInChar": bool,
        "ConvertTimestampWithZoneToUTC": bool,
        "OpenTransactionWindow": int,
    },
    total=False,
)

OrderableReplicationInstanceTypeDef = TypedDict(
    "OrderableReplicationInstanceTypeDef",
    {
        "EngineVersion": str,
        "ReplicationInstanceClass": str,
        "StorageType": str,
        "MinAllocatedStorage": int,
        "MaxAllocatedStorage": int,
        "DefaultAllocatedStorage": int,
        "IncludedAllocatedStorage": int,
        "AvailabilityZones": List[str],
        "ReleaseStatus": ReleaseStatusValuesType,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PendingMaintenanceActionTypeDef = TypedDict(
    "PendingMaintenanceActionTypeDef",
    {
        "Action": str,
        "AutoAppliedAfterDate": datetime,
        "ForcedApplyDate": datetime,
        "OptInStatus": str,
        "CurrentApplyDate": datetime,
        "Description": str,
    },
    total=False,
)

PostgreSQLSettingsTypeDef = TypedDict(
    "PostgreSQLSettingsTypeDef",
    {
        "AfterConnectScript": str,
        "CaptureDdls": bool,
        "MaxFileSize": int,
        "DatabaseName": str,
        "DdlArtifactsSchema": str,
        "ExecuteTimeout": int,
        "FailTasksOnLobTruncation": bool,
        "HeartbeatEnable": bool,
        "HeartbeatSchema": str,
        "HeartbeatFrequency": int,
        "Password": str,
        "Port": int,
        "ServerName": str,
        "Username": str,
        "SlotName": str,
        "PluginName": PluginNameValueType,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
        "TrimSpaceInChar": bool,
        "MapBooleanAsBoolean": bool,
        "MapJsonbAsClob": bool,
        "MapLongVarcharAs": LongVarcharMappingTypeType,
        "DatabaseMode": DatabaseModeType,
        "BabelfishDatabaseName": str,
    },
    total=False,
)

PostgreSqlDataProviderSettingsTypeDef = TypedDict(
    "PostgreSqlDataProviderSettingsTypeDef",
    {
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
        "SslMode": DmsSslModeValueType,
        "CertificateArn": str,
    },
    total=False,
)

ProvisionDataTypeDef = TypedDict(
    "ProvisionDataTypeDef",
    {
        "ProvisionState": str,
        "ProvisionedCapacityUnits": int,
        "DateProvisioned": datetime,
        "IsNewProvisioningAvailable": bool,
        "DateNewProvisioningDataAvailable": datetime,
        "ReasonForNewProvisioningData": str,
    },
    total=False,
)

RdsConfigurationTypeDef = TypedDict(
    "RdsConfigurationTypeDef",
    {
        "EngineEdition": str,
        "InstanceType": str,
        "InstanceVcpu": float,
        "InstanceMemory": float,
        "StorageType": str,
        "StorageSize": int,
        "StorageIops": int,
        "DeploymentOption": str,
        "EngineVersion": str,
    },
    total=False,
)

RdsRecommendationTypeDef = TypedDict(
    "RdsRecommendationTypeDef",
    {
        "RequirementsToTarget": "RdsRequirementsTypeDef",
        "TargetConfiguration": "RdsConfigurationTypeDef",
    },
    total=False,
)

RdsRequirementsTypeDef = TypedDict(
    "RdsRequirementsTypeDef",
    {
        "EngineEdition": str,
        "InstanceVcpu": float,
        "InstanceMemory": float,
        "StorageSize": int,
        "StorageIops": int,
        "DeploymentOption": str,
        "EngineVersion": str,
    },
    total=False,
)

_RequiredRebootReplicationInstanceMessageRequestTypeDef = TypedDict(
    "_RequiredRebootReplicationInstanceMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
    },
)
_OptionalRebootReplicationInstanceMessageRequestTypeDef = TypedDict(
    "_OptionalRebootReplicationInstanceMessageRequestTypeDef",
    {
        "ForceFailover": bool,
        "ForcePlannedFailover": bool,
    },
    total=False,
)

class RebootReplicationInstanceMessageRequestTypeDef(
    _RequiredRebootReplicationInstanceMessageRequestTypeDef,
    _OptionalRebootReplicationInstanceMessageRequestTypeDef,
):
    pass

RebootReplicationInstanceResponseTypeDef = TypedDict(
    "RebootReplicationInstanceResponseTypeDef",
    {
        "ReplicationInstance": "ReplicationInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecommendationDataTypeDef = TypedDict(
    "RecommendationDataTypeDef",
    {
        "RdsEngine": "RdsRecommendationTypeDef",
    },
    total=False,
)

RecommendationSettingsTypeDef = TypedDict(
    "RecommendationSettingsTypeDef",
    {
        "InstanceSizingType": str,
        "WorkloadType": str,
    },
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "DatabaseId": str,
        "EngineName": str,
        "CreatedDate": str,
        "Status": str,
        "Preferred": bool,
        "Settings": "RecommendationSettingsTypeDef",
        "Data": "RecommendationDataTypeDef",
    },
    total=False,
)

_RequiredRedisSettingsTypeDef = TypedDict(
    "_RequiredRedisSettingsTypeDef",
    {
        "ServerName": str,
        "Port": int,
    },
)
_OptionalRedisSettingsTypeDef = TypedDict(
    "_OptionalRedisSettingsTypeDef",
    {
        "SslSecurityProtocol": SslSecurityProtocolValueType,
        "AuthType": RedisAuthTypeValueType,
        "AuthUserName": str,
        "AuthPassword": str,
        "SslCaCertificateArn": str,
    },
    total=False,
)

class RedisSettingsTypeDef(_RequiredRedisSettingsTypeDef, _OptionalRedisSettingsTypeDef):
    pass

RedshiftDataProviderSettingsTypeDef = TypedDict(
    "RedshiftDataProviderSettingsTypeDef",
    {
        "ServerName": str,
        "Port": int,
        "DatabaseName": str,
    },
    total=False,
)

RedshiftSettingsTypeDef = TypedDict(
    "RedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "CaseSensitiveNames": bool,
        "CompUpdate": bool,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": EncryptionModeValueType,
        "ExplicitIds": bool,
        "FileTransferUploadStreams": int,
        "LoadTimeout": int,
        "MaxFileSize": int,
        "Password": str,
        "Port": int,
        "RemoveQuotes": bool,
        "ReplaceInvalidChars": str,
        "ReplaceChars": str,
        "ServerName": str,
        "ServiceAccessRoleArn": str,
        "ServerSideEncryptionKmsKeyId": str,
        "TimeFormat": str,
        "TrimBlanks": bool,
        "TruncateColumns": bool,
        "Username": str,
        "WriteBufferSize": int,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
        "MapBooleanAsBoolean": bool,
    },
    total=False,
)

RefreshSchemasMessageRequestTypeDef = TypedDict(
    "RefreshSchemasMessageRequestTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
    },
)

RefreshSchemasResponseTypeDef = TypedDict(
    "RefreshSchemasResponseTypeDef",
    {
        "RefreshSchemasStatus": "RefreshSchemasStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RefreshSchemasStatusTypeDef = TypedDict(
    "RefreshSchemasStatusTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
        "Status": RefreshSchemasStatusTypeValueType,
        "LastRefreshDate": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)

_RequiredReloadReplicationTablesMessageRequestTypeDef = TypedDict(
    "_RequiredReloadReplicationTablesMessageRequestTypeDef",
    {
        "ReplicationConfigArn": str,
        "TablesToReload": List["TableToReloadTypeDef"],
    },
)
_OptionalReloadReplicationTablesMessageRequestTypeDef = TypedDict(
    "_OptionalReloadReplicationTablesMessageRequestTypeDef",
    {
        "ReloadOption": ReloadOptionValueType,
    },
    total=False,
)

class ReloadReplicationTablesMessageRequestTypeDef(
    _RequiredReloadReplicationTablesMessageRequestTypeDef,
    _OptionalReloadReplicationTablesMessageRequestTypeDef,
):
    pass

ReloadReplicationTablesResponseTypeDef = TypedDict(
    "ReloadReplicationTablesResponseTypeDef",
    {
        "ReplicationConfigArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReloadTablesMessageRequestTypeDef = TypedDict(
    "_RequiredReloadTablesMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "TablesToReload": List["TableToReloadTypeDef"],
    },
)
_OptionalReloadTablesMessageRequestTypeDef = TypedDict(
    "_OptionalReloadTablesMessageRequestTypeDef",
    {
        "ReloadOption": ReloadOptionValueType,
    },
    total=False,
)

class ReloadTablesMessageRequestTypeDef(
    _RequiredReloadTablesMessageRequestTypeDef, _OptionalReloadTablesMessageRequestTypeDef
):
    pass

ReloadTablesResponseTypeDef = TypedDict(
    "ReloadTablesResponseTypeDef",
    {
        "ReplicationTaskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsFromResourceMessageRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceMessageRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

ReplicationConfigTypeDef = TypedDict(
    "ReplicationConfigTypeDef",
    {
        "ReplicationConfigIdentifier": str,
        "ReplicationConfigArn": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationType": MigrationTypeValueType,
        "ComputeConfig": "ComputeConfigTypeDef",
        "ReplicationSettings": str,
        "SupplementalSettings": str,
        "TableMappings": str,
        "ReplicationConfigCreateTime": datetime,
        "ReplicationConfigUpdateTime": datetime,
    },
    total=False,
)

ReplicationInstanceTaskLogTypeDef = TypedDict(
    "ReplicationInstanceTaskLogTypeDef",
    {
        "ReplicationTaskName": str,
        "ReplicationTaskArn": str,
        "ReplicationInstanceTaskLogSize": int,
    },
    total=False,
)

ReplicationInstanceTypeDef = TypedDict(
    "ReplicationInstanceTypeDef",
    {
        "ReplicationInstanceIdentifier": str,
        "ReplicationInstanceClass": str,
        "ReplicationInstanceStatus": str,
        "AllocatedStorage": int,
        "InstanceCreateTime": datetime,
        "VpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "AvailabilityZone": str,
        "ReplicationSubnetGroup": "ReplicationSubnetGroupTypeDef",
        "PreferredMaintenanceWindow": str,
        "PendingModifiedValues": "ReplicationPendingModifiedValuesTypeDef",
        "MultiAZ": bool,
        "EngineVersion": str,
        "AutoMinorVersionUpgrade": bool,
        "KmsKeyId": str,
        "ReplicationInstanceArn": str,
        "ReplicationInstancePublicIpAddress": str,
        "ReplicationInstancePrivateIpAddress": str,
        "ReplicationInstancePublicIpAddresses": List[str],
        "ReplicationInstancePrivateIpAddresses": List[str],
        "ReplicationInstanceIpv6Addresses": List[str],
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
        "NetworkType": str,
    },
    total=False,
)

ReplicationPendingModifiedValuesTypeDef = TypedDict(
    "ReplicationPendingModifiedValuesTypeDef",
    {
        "ReplicationInstanceClass": str,
        "AllocatedStorage": int,
        "MultiAZ": bool,
        "EngineVersion": str,
        "NetworkType": str,
    },
    total=False,
)

ReplicationStatsTypeDef = TypedDict(
    "ReplicationStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ReplicationSubnetGroupTypeDef = TypedDict(
    "ReplicationSubnetGroupTypeDef",
    {
        "ReplicationSubnetGroupIdentifier": str,
        "ReplicationSubnetGroupDescription": str,
        "VpcId": str,
        "SubnetGroupStatus": str,
        "Subnets": List["SubnetTypeDef"],
        "SupportedNetworkTypes": List[str],
    },
    total=False,
)

ReplicationTaskAssessmentResultTypeDef = TypedDict(
    "ReplicationTaskAssessmentResultTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskLastAssessmentDate": datetime,
        "AssessmentStatus": str,
        "AssessmentResultsFile": str,
        "AssessmentResults": str,
        "S3ObjectUrl": str,
    },
    total=False,
)

ReplicationTaskAssessmentRunProgressTypeDef = TypedDict(
    "ReplicationTaskAssessmentRunProgressTypeDef",
    {
        "IndividualAssessmentCount": int,
        "IndividualAssessmentCompletedCount": int,
    },
    total=False,
)

ReplicationTaskAssessmentRunTypeDef = TypedDict(
    "ReplicationTaskAssessmentRunTypeDef",
    {
        "ReplicationTaskAssessmentRunArn": str,
        "ReplicationTaskArn": str,
        "Status": str,
        "ReplicationTaskAssessmentRunCreationDate": datetime,
        "AssessmentProgress": "ReplicationTaskAssessmentRunProgressTypeDef",
        "LastFailureMessage": str,
        "ServiceAccessRoleArn": str,
        "ResultLocationBucket": str,
        "ResultLocationFolder": str,
        "ResultEncryptionMode": str,
        "ResultKmsKeyArn": str,
        "AssessmentRunName": str,
    },
    total=False,
)

ReplicationTaskIndividualAssessmentTypeDef = TypedDict(
    "ReplicationTaskIndividualAssessmentTypeDef",
    {
        "ReplicationTaskIndividualAssessmentArn": str,
        "ReplicationTaskAssessmentRunArn": str,
        "IndividualAssessmentName": str,
        "Status": str,
        "ReplicationTaskIndividualAssessmentStartDate": datetime,
    },
    total=False,
)

ReplicationTaskStatsTypeDef = TypedDict(
    "ReplicationTaskStatsTypeDef",
    {
        "FullLoadProgressPercent": int,
        "ElapsedTimeMillis": int,
        "TablesLoaded": int,
        "TablesLoading": int,
        "TablesQueued": int,
        "TablesErrored": int,
        "FreshStartDate": datetime,
        "StartDate": datetime,
        "StopDate": datetime,
        "FullLoadStartDate": datetime,
        "FullLoadFinishDate": datetime,
    },
    total=False,
)

ReplicationTaskTypeDef = TypedDict(
    "ReplicationTaskTypeDef",
    {
        "ReplicationTaskIdentifier": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationInstanceArn": str,
        "MigrationType": MigrationTypeValueType,
        "TableMappings": str,
        "ReplicationTaskSettings": str,
        "Status": str,
        "LastFailureMessage": str,
        "StopReason": str,
        "ReplicationTaskCreationDate": datetime,
        "ReplicationTaskStartDate": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationTaskArn": str,
        "ReplicationTaskStats": "ReplicationTaskStatsTypeDef",
        "TaskData": str,
        "TargetReplicationInstanceArn": str,
    },
    total=False,
)

ReplicationTypeDef = TypedDict(
    "ReplicationTypeDef",
    {
        "ReplicationConfigIdentifier": str,
        "ReplicationConfigArn": str,
        "SourceEndpointArn": str,
        "TargetEndpointArn": str,
        "ReplicationType": MigrationTypeValueType,
        "Status": str,
        "ProvisionData": "ProvisionDataTypeDef",
        "StopReason": str,
        "FailureMessages": List[str],
        "ReplicationStats": "ReplicationStatsTypeDef",
        "StartReplicationType": str,
        "CdcStartTime": datetime,
        "CdcStartPosition": str,
        "CdcStopPosition": str,
        "RecoveryCheckpoint": str,
        "ReplicationCreateTime": datetime,
        "ReplicationUpdateTime": datetime,
        "ReplicationLastStopTime": datetime,
        "ReplicationDeprovisionTime": datetime,
    },
    total=False,
)

ResourcePendingMaintenanceActionsTypeDef = TypedDict(
    "ResourcePendingMaintenanceActionsTypeDef",
    {
        "ResourceIdentifier": str,
        "PendingMaintenanceActionDetails": List["PendingMaintenanceActionTypeDef"],
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RunFleetAdvisorLsaAnalysisResponseTypeDef = TypedDict(
    "RunFleetAdvisorLsaAnalysisResponseTypeDef",
    {
        "LsaAnalysisId": str,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3SettingsTypeDef = TypedDict(
    "S3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": CompressionTypeValueType,
        "EncryptionMode": EncryptionModeValueType,
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": DataFormatValueType,
        "EncodingType": EncodingTypeValueType,
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": ParquetVersionValueType,
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
        "CdcInsertsAndUpdates": bool,
        "DatePartitionEnabled": bool,
        "DatePartitionSequence": DatePartitionSequenceValueType,
        "DatePartitionDelimiter": DatePartitionDelimiterValueType,
        "UseCsvNoSupValue": bool,
        "CsvNoSupValue": str,
        "PreserveTransactions": bool,
        "CdcPath": str,
        "UseTaskStartTimeForFullLoadTimestamp": bool,
        "CannedAclForObjects": CannedAclForObjectsValueType,
        "AddColumnName": bool,
        "CdcMaxBatchInterval": int,
        "CdcMinFileSize": int,
        "CsvNullValue": str,
        "IgnoreHeaderRows": int,
        "MaxFileSize": int,
        "Rfc4180": bool,
        "DatePartitionTimezone": str,
        "AddTrailingPaddingCharacter": bool,
        "ExpectedBucketOwner": str,
        "GlueCatalogGeneration": bool,
    },
    total=False,
)

SCApplicationAttributesTypeDef = TypedDict(
    "SCApplicationAttributesTypeDef",
    {
        "S3BucketPath": str,
        "S3BucketRoleArn": str,
    },
    total=False,
)

SchemaConversionRequestTypeDef = TypedDict(
    "SchemaConversionRequestTypeDef",
    {
        "Status": str,
        "RequestIdentifier": str,
        "MigrationProjectArn": str,
        "Error": "ErrorDetailsTypeDef",
        "ExportSqlDetails": "ExportSqlDetailsTypeDef",
    },
    total=False,
)

SchemaResponseTypeDef = TypedDict(
    "SchemaResponseTypeDef",
    {
        "CodeLineCount": int,
        "CodeSize": int,
        "Complexity": str,
        "Server": "ServerShortInfoResponseTypeDef",
        "DatabaseInstance": "DatabaseShortInfoResponseTypeDef",
        "SchemaId": str,
        "SchemaName": str,
        "OriginalSchema": "SchemaShortInfoResponseTypeDef",
        "Similarity": float,
    },
    total=False,
)

SchemaShortInfoResponseTypeDef = TypedDict(
    "SchemaShortInfoResponseTypeDef",
    {
        "SchemaId": str,
        "SchemaName": str,
        "DatabaseId": str,
        "DatabaseName": str,
        "DatabaseIpAddress": str,
    },
    total=False,
)

ServerShortInfoResponseTypeDef = TypedDict(
    "ServerShortInfoResponseTypeDef",
    {
        "ServerId": str,
        "IpAddress": str,
        "ServerName": str,
    },
    total=False,
)

StartExtensionPackAssociationMessageRequestTypeDef = TypedDict(
    "StartExtensionPackAssociationMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
    },
)

StartExtensionPackAssociationResponseTypeDef = TypedDict(
    "StartExtensionPackAssociationResponseTypeDef",
    {
        "RequestIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMetadataModelAssessmentMessageRequestTypeDef = TypedDict(
    "StartMetadataModelAssessmentMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "SelectionRules": str,
    },
)

StartMetadataModelAssessmentResponseTypeDef = TypedDict(
    "StartMetadataModelAssessmentResponseTypeDef",
    {
        "RequestIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMetadataModelConversionMessageRequestTypeDef = TypedDict(
    "StartMetadataModelConversionMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "SelectionRules": str,
    },
)

StartMetadataModelConversionResponseTypeDef = TypedDict(
    "StartMetadataModelConversionResponseTypeDef",
    {
        "RequestIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartMetadataModelExportAsScriptMessageRequestTypeDef = TypedDict(
    "_RequiredStartMetadataModelExportAsScriptMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "SelectionRules": str,
        "Origin": OriginTypeValueType,
    },
)
_OptionalStartMetadataModelExportAsScriptMessageRequestTypeDef = TypedDict(
    "_OptionalStartMetadataModelExportAsScriptMessageRequestTypeDef",
    {
        "FileName": str,
    },
    total=False,
)

class StartMetadataModelExportAsScriptMessageRequestTypeDef(
    _RequiredStartMetadataModelExportAsScriptMessageRequestTypeDef,
    _OptionalStartMetadataModelExportAsScriptMessageRequestTypeDef,
):
    pass

StartMetadataModelExportAsScriptResponseTypeDef = TypedDict(
    "StartMetadataModelExportAsScriptResponseTypeDef",
    {
        "RequestIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartMetadataModelExportToTargetMessageRequestTypeDef = TypedDict(
    "_RequiredStartMetadataModelExportToTargetMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "SelectionRules": str,
    },
)
_OptionalStartMetadataModelExportToTargetMessageRequestTypeDef = TypedDict(
    "_OptionalStartMetadataModelExportToTargetMessageRequestTypeDef",
    {
        "OverwriteExtensionPack": bool,
    },
    total=False,
)

class StartMetadataModelExportToTargetMessageRequestTypeDef(
    _RequiredStartMetadataModelExportToTargetMessageRequestTypeDef,
    _OptionalStartMetadataModelExportToTargetMessageRequestTypeDef,
):
    pass

StartMetadataModelExportToTargetResponseTypeDef = TypedDict(
    "StartMetadataModelExportToTargetResponseTypeDef",
    {
        "RequestIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartMetadataModelImportMessageRequestTypeDef = TypedDict(
    "_RequiredStartMetadataModelImportMessageRequestTypeDef",
    {
        "MigrationProjectIdentifier": str,
        "SelectionRules": str,
        "Origin": OriginTypeValueType,
    },
)
_OptionalStartMetadataModelImportMessageRequestTypeDef = TypedDict(
    "_OptionalStartMetadataModelImportMessageRequestTypeDef",
    {
        "Refresh": bool,
    },
    total=False,
)

class StartMetadataModelImportMessageRequestTypeDef(
    _RequiredStartMetadataModelImportMessageRequestTypeDef,
    _OptionalStartMetadataModelImportMessageRequestTypeDef,
):
    pass

StartMetadataModelImportResponseTypeDef = TypedDict(
    "StartMetadataModelImportResponseTypeDef",
    {
        "RequestIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartRecommendationsRequestEntryTypeDef = TypedDict(
    "StartRecommendationsRequestEntryTypeDef",
    {
        "DatabaseId": str,
        "Settings": "RecommendationSettingsTypeDef",
    },
)

StartRecommendationsRequestRequestTypeDef = TypedDict(
    "StartRecommendationsRequestRequestTypeDef",
    {
        "DatabaseId": str,
        "Settings": "RecommendationSettingsTypeDef",
    },
)

_RequiredStartReplicationMessageRequestTypeDef = TypedDict(
    "_RequiredStartReplicationMessageRequestTypeDef",
    {
        "ReplicationConfigArn": str,
        "StartReplicationType": str,
    },
)
_OptionalStartReplicationMessageRequestTypeDef = TypedDict(
    "_OptionalStartReplicationMessageRequestTypeDef",
    {
        "CdcStartTime": Union[datetime, str],
        "CdcStartPosition": str,
        "CdcStopPosition": str,
    },
    total=False,
)

class StartReplicationMessageRequestTypeDef(
    _RequiredStartReplicationMessageRequestTypeDef, _OptionalStartReplicationMessageRequestTypeDef
):
    pass

StartReplicationResponseTypeDef = TypedDict(
    "StartReplicationResponseTypeDef",
    {
        "Replication": "ReplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartReplicationTaskAssessmentMessageRequestTypeDef = TypedDict(
    "StartReplicationTaskAssessmentMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)

StartReplicationTaskAssessmentResponseTypeDef = TypedDict(
    "StartReplicationTaskAssessmentResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartReplicationTaskAssessmentRunMessageRequestTypeDef = TypedDict(
    "_RequiredStartReplicationTaskAssessmentRunMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "ServiceAccessRoleArn": str,
        "ResultLocationBucket": str,
        "AssessmentRunName": str,
    },
)
_OptionalStartReplicationTaskAssessmentRunMessageRequestTypeDef = TypedDict(
    "_OptionalStartReplicationTaskAssessmentRunMessageRequestTypeDef",
    {
        "ResultLocationFolder": str,
        "ResultEncryptionMode": str,
        "ResultKmsKeyArn": str,
        "IncludeOnly": List[str],
        "Exclude": List[str],
    },
    total=False,
)

class StartReplicationTaskAssessmentRunMessageRequestTypeDef(
    _RequiredStartReplicationTaskAssessmentRunMessageRequestTypeDef,
    _OptionalStartReplicationTaskAssessmentRunMessageRequestTypeDef,
):
    pass

StartReplicationTaskAssessmentRunResponseTypeDef = TypedDict(
    "StartReplicationTaskAssessmentRunResponseTypeDef",
    {
        "ReplicationTaskAssessmentRun": "ReplicationTaskAssessmentRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartReplicationTaskMessageRequestTypeDef = TypedDict(
    "_RequiredStartReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
        "StartReplicationTaskType": StartReplicationTaskTypeValueType,
    },
)
_OptionalStartReplicationTaskMessageRequestTypeDef = TypedDict(
    "_OptionalStartReplicationTaskMessageRequestTypeDef",
    {
        "CdcStartTime": Union[datetime, str],
        "CdcStartPosition": str,
        "CdcStopPosition": str,
    },
    total=False,
)

class StartReplicationTaskMessageRequestTypeDef(
    _RequiredStartReplicationTaskMessageRequestTypeDef,
    _OptionalStartReplicationTaskMessageRequestTypeDef,
):
    pass

StartReplicationTaskResponseTypeDef = TypedDict(
    "StartReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopReplicationMessageRequestTypeDef = TypedDict(
    "StopReplicationMessageRequestTypeDef",
    {
        "ReplicationConfigArn": str,
    },
)

StopReplicationResponseTypeDef = TypedDict(
    "StopReplicationResponseTypeDef",
    {
        "Replication": "ReplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopReplicationTaskMessageRequestTypeDef = TypedDict(
    "StopReplicationTaskMessageRequestTypeDef",
    {
        "ReplicationTaskArn": str,
    },
)

StopReplicationTaskResponseTypeDef = TypedDict(
    "StopReplicationTaskResponseTypeDef",
    {
        "ReplicationTask": "ReplicationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "SubnetIdentifier": str,
        "SubnetAvailabilityZone": "AvailabilityZoneTypeDef",
        "SubnetStatus": str,
    },
    total=False,
)

SupportedEndpointTypeTypeDef = TypedDict(
    "SupportedEndpointTypeTypeDef",
    {
        "EngineName": str,
        "SupportsCDC": bool,
        "EndpointType": ReplicationEndpointTypeValueType,
        "ReplicationInstanceEngineMinimumVersion": str,
        "EngineDisplayName": str,
    },
    total=False,
)

SybaseSettingsTypeDef = TypedDict(
    "SybaseSettingsTypeDef",
    {
        "DatabaseName": str,
        "Password": str,
        "Port": int,
        "ServerName": str,
        "Username": str,
        "SecretsManagerAccessRoleArn": str,
        "SecretsManagerSecretId": str,
    },
    total=False,
)

TableStatisticsTypeDef = TypedDict(
    "TableStatisticsTypeDef",
    {
        "SchemaName": str,
        "TableName": str,
        "Inserts": int,
        "Deletes": int,
        "Updates": int,
        "Ddls": int,
        "AppliedInserts": int,
        "AppliedDeletes": int,
        "AppliedUpdates": int,
        "AppliedDdls": int,
        "FullLoadRows": int,
        "FullLoadCondtnlChkFailedRows": int,
        "FullLoadErrorRows": int,
        "FullLoadStartTime": datetime,
        "FullLoadEndTime": datetime,
        "FullLoadReloaded": bool,
        "LastUpdateTime": datetime,
        "TableState": str,
        "ValidationPendingRecords": int,
        "ValidationFailedRecords": int,
        "ValidationSuspendedRecords": int,
        "ValidationState": str,
        "ValidationStateDetails": str,
    },
    total=False,
)

TableToReloadTypeDef = TypedDict(
    "TableToReloadTypeDef",
    {
        "SchemaName": str,
        "TableName": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
        "ResourceArn": str,
    },
    total=False,
)

TestConnectionMessageRequestTypeDef = TypedDict(
    "TestConnectionMessageRequestTypeDef",
    {
        "ReplicationInstanceArn": str,
        "EndpointArn": str,
    },
)

TestConnectionResponseTypeDef = TypedDict(
    "TestConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTimestreamSettingsTypeDef = TypedDict(
    "_RequiredTimestreamSettingsTypeDef",
    {
        "DatabaseName": str,
        "MemoryDuration": int,
        "MagneticDuration": int,
    },
)
_OptionalTimestreamSettingsTypeDef = TypedDict(
    "_OptionalTimestreamSettingsTypeDef",
    {
        "CdcInsertsAndUpdates": bool,
        "EnableMagneticStoreWrites": bool,
    },
    total=False,
)

class TimestreamSettingsTypeDef(
    _RequiredTimestreamSettingsTypeDef, _OptionalTimestreamSettingsTypeDef
):
    pass

UpdateSubscriptionsToEventBridgeMessageRequestTypeDef = TypedDict(
    "UpdateSubscriptionsToEventBridgeMessageRequestTypeDef",
    {
        "ForceMove": bool,
    },
    total=False,
)

UpdateSubscriptionsToEventBridgeResponseTypeDef = TypedDict(
    "UpdateSubscriptionsToEventBridgeResponseTypeDef",
    {
        "Result": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef",
    {
        "VpcSecurityGroupId": str,
        "Status": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
