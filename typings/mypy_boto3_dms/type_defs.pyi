"""
Main interface for dms service type definitions.

Usage::

    ```python
    from mypy_boto3_dms.type_defs import AccountQuotaTypeDef

    data: AccountQuotaTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

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
    "AvailabilityZoneTypeDef",
    "CertificateTypeDef",
    "ConnectionTypeDef",
    "DmsTransferSettingsTypeDef",
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

AccountQuotaTypeDef = TypedDict(
    "AccountQuotaTypeDef", {"AccountQuotaName": str, "Used": int, "Max": int}, total=False
)

AvailabilityZoneTypeDef = TypedDict("AvailabilityZoneTypeDef", {"Name": str}, total=False)

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

DmsTransferSettingsTypeDef = TypedDict(
    "DmsTransferSettingsTypeDef", {"ServiceAccessRoleArn": str, "BucketName": str}, total=False
)

DynamoDbSettingsTypeDef = TypedDict("DynamoDbSettingsTypeDef", {"ServiceAccessRoleArn": str})

_RequiredElasticsearchSettingsTypeDef = TypedDict(
    "_RequiredElasticsearchSettingsTypeDef", {"ServiceAccessRoleArn": str, "EndpointUri": str}
)
_OptionalElasticsearchSettingsTypeDef = TypedDict(
    "_OptionalElasticsearchSettingsTypeDef",
    {"FullLoadErrorPercentage": int, "ErrorRetryDuration": int},
    total=False,
)


class ElasticsearchSettingsTypeDef(
    _RequiredElasticsearchSettingsTypeDef, _OptionalElasticsearchSettingsTypeDef
):
    pass


EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "EndpointIdentifier": str,
        "EndpointType": Literal["source", "target"],
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
        "SslMode": Literal["none", "require", "verify-ca", "verify-full"],
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
    },
    total=False,
)

EventCategoryGroupTypeDef = TypedDict(
    "EventCategoryGroupTypeDef", {"SourceType": str, "EventCategories": List[str]}, total=False
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

IBMDb2SettingsTypeDef = TypedDict(
    "IBMDb2SettingsTypeDef",
    {"DatabaseName": str, "Password": str, "Port": int, "ServerName": str, "Username": str},
    total=False,
)

KafkaSettingsTypeDef = TypedDict(
    "KafkaSettingsTypeDef",
    {
        "Broker": str,
        "Topic": str,
        "MessageFormat": Literal["json", "json-unformatted"],
        "IncludeTransactionDetails": bool,
        "IncludePartitionValue": bool,
        "PartitionIncludeSchemaTable": bool,
        "IncludeTableAlterOperations": bool,
        "IncludeControlDetails": bool,
    },
    total=False,
)

KinesisSettingsTypeDef = TypedDict(
    "KinesisSettingsTypeDef",
    {
        "StreamArn": str,
        "MessageFormat": Literal["json", "json-unformatted"],
        "ServiceAccessRoleArn": str,
        "IncludeTransactionDetails": bool,
        "IncludePartitionValue": bool,
        "PartitionIncludeSchemaTable": bool,
        "IncludeTableAlterOperations": bool,
        "IncludeControlDetails": bool,
    },
    total=False,
)

MicrosoftSQLServerSettingsTypeDef = TypedDict(
    "MicrosoftSQLServerSettingsTypeDef",
    {"Port": int, "DatabaseName": str, "Password": str, "ServerName": str, "Username": str},
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
        "AuthType": Literal["no", "password"],
        "AuthMechanism": Literal["default", "mongodb_cr", "scram_sha_1"],
        "NestingLevel": Literal["none", "one"],
        "ExtractDocId": str,
        "DocsToInvestigate": str,
        "AuthSource": str,
        "KmsKeyId": str,
    },
    total=False,
)

MySQLSettingsTypeDef = TypedDict(
    "MySQLSettingsTypeDef",
    {"DatabaseName": str, "Password": str, "Port": int, "ServerName": str, "Username": str},
    total=False,
)

_RequiredNeptuneSettingsTypeDef = TypedDict(
    "_RequiredNeptuneSettingsTypeDef", {"S3BucketName": str, "S3BucketFolder": str}
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


OracleSettingsTypeDef = TypedDict(
    "OracleSettingsTypeDef",
    {
        "AsmPassword": str,
        "AsmServer": str,
        "AsmUser": str,
        "DatabaseName": str,
        "Password": str,
        "Port": int,
        "SecurityDbEncryption": str,
        "SecurityDbEncryptionName": str,
        "ServerName": str,
        "Username": str,
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
        "ReleaseStatus": Literal["beta"],
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
    {"DatabaseName": str, "Password": str, "Port": int, "ServerName": str, "Username": str},
    total=False,
)

RedshiftSettingsTypeDef = TypedDict(
    "RedshiftSettingsTypeDef",
    {
        "AcceptAnyDate": bool,
        "AfterConnectScript": str,
        "BucketFolder": str,
        "BucketName": str,
        "ConnectionTimeout": int,
        "DatabaseName": str,
        "DateFormat": str,
        "EmptyAsNull": bool,
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
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
    },
    total=False,
)

RefreshSchemasStatusTypeDef = TypedDict(
    "RefreshSchemasStatusTypeDef",
    {
        "EndpointArn": str,
        "ReplicationInstanceArn": str,
        "Status": Literal["successful", "failed", "refreshing"],
        "LastRefreshDate": datetime,
        "LastFailureMessage": str,
    },
    total=False,
)

ReplicationInstanceTaskLogTypeDef = TypedDict(
    "ReplicationInstanceTaskLogTypeDef",
    {"ReplicationTaskName": str, "ReplicationTaskArn": str, "ReplicationInstanceTaskLogSize": int},
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
        "PubliclyAccessible": bool,
        "SecondaryAvailabilityZone": str,
        "FreeUntil": datetime,
        "DnsNameServers": str,
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
    {"IndividualAssessmentCount": int, "IndividualAssessmentCompletedCount": int},
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
        "MigrationType": Literal["full-load", "cdc", "full-load-and-cdc"],
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

S3SettingsTypeDef = TypedDict(
    "S3SettingsTypeDef",
    {
        "ServiceAccessRoleArn": str,
        "ExternalTableDefinition": str,
        "CsvRowDelimiter": str,
        "CsvDelimiter": str,
        "BucketFolder": str,
        "BucketName": str,
        "CompressionType": Literal["none", "gzip"],
        "EncryptionMode": Literal["sse-s3", "sse-kms"],
        "ServerSideEncryptionKmsKeyId": str,
        "DataFormat": Literal["csv", "parquet"],
        "EncodingType": Literal["plain", "plain-dictionary", "rle-dictionary"],
        "DictPageSizeLimit": int,
        "RowGroupLength": int,
        "DataPageSize": int,
        "ParquetVersion": Literal["parquet-1-0", "parquet-2-0"],
        "EnableStatistics": bool,
        "IncludeOpForFullLoad": bool,
        "CdcInsertsOnly": bool,
        "TimestampColumnName": str,
        "ParquetTimestampInMillisecond": bool,
        "CdcInsertsAndUpdates": bool,
    },
    total=False,
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
        "EndpointType": Literal["source", "target"],
        "ReplicationInstanceEngineMinimumVersion": str,
        "EngineDisplayName": str,
    },
    total=False,
)

SybaseSettingsTypeDef = TypedDict(
    "SybaseSettingsTypeDef",
    {"DatabaseName": str, "Password": str, "Port": int, "ServerName": str, "Username": str},
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

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef", {"VpcSecurityGroupId": str, "Status": str}, total=False
)

ApplyPendingMaintenanceActionResponseTypeDef = TypedDict(
    "ApplyPendingMaintenanceActionResponseTypeDef",
    {"ResourcePendingMaintenanceActions": "ResourcePendingMaintenanceActionsTypeDef"},
    total=False,
)

CancelReplicationTaskAssessmentRunResponseTypeDef = TypedDict(
    "CancelReplicationTaskAssessmentRunResponseTypeDef",
    {"ReplicationTaskAssessmentRun": "ReplicationTaskAssessmentRunTypeDef"},
    total=False,
)

CreateEndpointResponseTypeDef = TypedDict(
    "CreateEndpointResponseTypeDef", {"Endpoint": "EndpointTypeDef"}, total=False
)

CreateEventSubscriptionResponseTypeDef = TypedDict(
    "CreateEventSubscriptionResponseTypeDef",
    {"EventSubscription": "EventSubscriptionTypeDef"},
    total=False,
)

CreateReplicationInstanceResponseTypeDef = TypedDict(
    "CreateReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": "ReplicationInstanceTypeDef"},
    total=False,
)

CreateReplicationSubnetGroupResponseTypeDef = TypedDict(
    "CreateReplicationSubnetGroupResponseTypeDef",
    {"ReplicationSubnetGroup": "ReplicationSubnetGroupTypeDef"},
    total=False,
)

CreateReplicationTaskResponseTypeDef = TypedDict(
    "CreateReplicationTaskResponseTypeDef",
    {"ReplicationTask": "ReplicationTaskTypeDef"},
    total=False,
)

DeleteCertificateResponseTypeDef = TypedDict(
    "DeleteCertificateResponseTypeDef", {"Certificate": "CertificateTypeDef"}, total=False
)

DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef", {"Connection": "ConnectionTypeDef"}, total=False
)

DeleteEndpointResponseTypeDef = TypedDict(
    "DeleteEndpointResponseTypeDef", {"Endpoint": "EndpointTypeDef"}, total=False
)

DeleteEventSubscriptionResponseTypeDef = TypedDict(
    "DeleteEventSubscriptionResponseTypeDef",
    {"EventSubscription": "EventSubscriptionTypeDef"},
    total=False,
)

DeleteReplicationInstanceResponseTypeDef = TypedDict(
    "DeleteReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": "ReplicationInstanceTypeDef"},
    total=False,
)

DeleteReplicationTaskAssessmentRunResponseTypeDef = TypedDict(
    "DeleteReplicationTaskAssessmentRunResponseTypeDef",
    {"ReplicationTaskAssessmentRun": "ReplicationTaskAssessmentRunTypeDef"},
    total=False,
)

DeleteReplicationTaskResponseTypeDef = TypedDict(
    "DeleteReplicationTaskResponseTypeDef",
    {"ReplicationTask": "ReplicationTaskTypeDef"},
    total=False,
)

DescribeAccountAttributesResponseTypeDef = TypedDict(
    "DescribeAccountAttributesResponseTypeDef",
    {"AccountQuotas": List["AccountQuotaTypeDef"], "UniqueAccountIdentifier": str},
    total=False,
)

DescribeApplicableIndividualAssessmentsResponseTypeDef = TypedDict(
    "DescribeApplicableIndividualAssessmentsResponseTypeDef",
    {"IndividualAssessmentNames": List[str], "Marker": str},
    total=False,
)

DescribeCertificatesResponseTypeDef = TypedDict(
    "DescribeCertificatesResponseTypeDef",
    {"Marker": str, "Certificates": List["CertificateTypeDef"]},
    total=False,
)

DescribeConnectionsResponseTypeDef = TypedDict(
    "DescribeConnectionsResponseTypeDef",
    {"Marker": str, "Connections": List["ConnectionTypeDef"]},
    total=False,
)

DescribeEndpointTypesResponseTypeDef = TypedDict(
    "DescribeEndpointTypesResponseTypeDef",
    {"Marker": str, "SupportedEndpointTypes": List["SupportedEndpointTypeTypeDef"]},
    total=False,
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {"Marker": str, "Endpoints": List["EndpointTypeDef"]},
    total=False,
)

DescribeEventCategoriesResponseTypeDef = TypedDict(
    "DescribeEventCategoriesResponseTypeDef",
    {"EventCategoryGroupList": List["EventCategoryGroupTypeDef"]},
    total=False,
)

DescribeEventSubscriptionsResponseTypeDef = TypedDict(
    "DescribeEventSubscriptionsResponseTypeDef",
    {"Marker": str, "EventSubscriptionsList": List["EventSubscriptionTypeDef"]},
    total=False,
)

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef", {"Marker": str, "Events": List["EventTypeDef"]}, total=False
)

DescribeOrderableReplicationInstancesResponseTypeDef = TypedDict(
    "DescribeOrderableReplicationInstancesResponseTypeDef",
    {"OrderableReplicationInstances": List["OrderableReplicationInstanceTypeDef"], "Marker": str},
    total=False,
)

DescribePendingMaintenanceActionsResponseTypeDef = TypedDict(
    "DescribePendingMaintenanceActionsResponseTypeDef",
    {"PendingMaintenanceActions": List["ResourcePendingMaintenanceActionsTypeDef"], "Marker": str},
    total=False,
)

DescribeRefreshSchemasStatusResponseTypeDef = TypedDict(
    "DescribeRefreshSchemasStatusResponseTypeDef",
    {"RefreshSchemasStatus": "RefreshSchemasStatusTypeDef"},
    total=False,
)

DescribeReplicationInstanceTaskLogsResponseTypeDef = TypedDict(
    "DescribeReplicationInstanceTaskLogsResponseTypeDef",
    {
        "ReplicationInstanceArn": str,
        "ReplicationInstanceTaskLogs": List["ReplicationInstanceTaskLogTypeDef"],
        "Marker": str,
    },
    total=False,
)

DescribeReplicationInstancesResponseTypeDef = TypedDict(
    "DescribeReplicationInstancesResponseTypeDef",
    {"Marker": str, "ReplicationInstances": List["ReplicationInstanceTypeDef"]},
    total=False,
)

DescribeReplicationSubnetGroupsResponseTypeDef = TypedDict(
    "DescribeReplicationSubnetGroupsResponseTypeDef",
    {"Marker": str, "ReplicationSubnetGroups": List["ReplicationSubnetGroupTypeDef"]},
    total=False,
)

DescribeReplicationTaskAssessmentResultsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentResultsResponseTypeDef",
    {
        "Marker": str,
        "BucketName": str,
        "ReplicationTaskAssessmentResults": List["ReplicationTaskAssessmentResultTypeDef"],
    },
    total=False,
)

DescribeReplicationTaskAssessmentRunsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskAssessmentRunsResponseTypeDef",
    {"Marker": str, "ReplicationTaskAssessmentRuns": List["ReplicationTaskAssessmentRunTypeDef"]},
    total=False,
)

DescribeReplicationTaskIndividualAssessmentsResponseTypeDef = TypedDict(
    "DescribeReplicationTaskIndividualAssessmentsResponseTypeDef",
    {
        "Marker": str,
        "ReplicationTaskIndividualAssessments": List["ReplicationTaskIndividualAssessmentTypeDef"],
    },
    total=False,
)

DescribeReplicationTasksResponseTypeDef = TypedDict(
    "DescribeReplicationTasksResponseTypeDef",
    {"Marker": str, "ReplicationTasks": List["ReplicationTaskTypeDef"]},
    total=False,
)

DescribeSchemasResponseTypeDef = TypedDict(
    "DescribeSchemasResponseTypeDef", {"Marker": str, "Schemas": List[str]}, total=False
)

DescribeTableStatisticsResponseTypeDef = TypedDict(
    "DescribeTableStatisticsResponseTypeDef",
    {"ReplicationTaskArn": str, "TableStatistics": List["TableStatisticsTypeDef"], "Marker": str},
    total=False,
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "Values": List[str]})

ImportCertificateResponseTypeDef = TypedDict(
    "ImportCertificateResponseTypeDef", {"Certificate": "CertificateTypeDef"}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"TagList": List["TagTypeDef"]}, total=False
)

ModifyEndpointResponseTypeDef = TypedDict(
    "ModifyEndpointResponseTypeDef", {"Endpoint": "EndpointTypeDef"}, total=False
)

ModifyEventSubscriptionResponseTypeDef = TypedDict(
    "ModifyEventSubscriptionResponseTypeDef",
    {"EventSubscription": "EventSubscriptionTypeDef"},
    total=False,
)

ModifyReplicationInstanceResponseTypeDef = TypedDict(
    "ModifyReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": "ReplicationInstanceTypeDef"},
    total=False,
)

ModifyReplicationSubnetGroupResponseTypeDef = TypedDict(
    "ModifyReplicationSubnetGroupResponseTypeDef",
    {"ReplicationSubnetGroup": "ReplicationSubnetGroupTypeDef"},
    total=False,
)

ModifyReplicationTaskResponseTypeDef = TypedDict(
    "ModifyReplicationTaskResponseTypeDef",
    {"ReplicationTask": "ReplicationTaskTypeDef"},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RebootReplicationInstanceResponseTypeDef = TypedDict(
    "RebootReplicationInstanceResponseTypeDef",
    {"ReplicationInstance": "ReplicationInstanceTypeDef"},
    total=False,
)

RefreshSchemasResponseTypeDef = TypedDict(
    "RefreshSchemasResponseTypeDef",
    {"RefreshSchemasStatus": "RefreshSchemasStatusTypeDef"},
    total=False,
)

ReloadTablesResponseTypeDef = TypedDict(
    "ReloadTablesResponseTypeDef", {"ReplicationTaskArn": str}, total=False
)

StartReplicationTaskAssessmentResponseTypeDef = TypedDict(
    "StartReplicationTaskAssessmentResponseTypeDef",
    {"ReplicationTask": "ReplicationTaskTypeDef"},
    total=False,
)

StartReplicationTaskAssessmentRunResponseTypeDef = TypedDict(
    "StartReplicationTaskAssessmentRunResponseTypeDef",
    {"ReplicationTaskAssessmentRun": "ReplicationTaskAssessmentRunTypeDef"},
    total=False,
)

StartReplicationTaskResponseTypeDef = TypedDict(
    "StartReplicationTaskResponseTypeDef",
    {"ReplicationTask": "ReplicationTaskTypeDef"},
    total=False,
)

StopReplicationTaskResponseTypeDef = TypedDict(
    "StopReplicationTaskResponseTypeDef", {"ReplicationTask": "ReplicationTaskTypeDef"}, total=False
)

TableToReloadTypeDef = TypedDict("TableToReloadTypeDef", {"SchemaName": str, "TableName": str})

TestConnectionResponseTypeDef = TypedDict(
    "TestConnectionResponseTypeDef", {"Connection": "ConnectionTypeDef"}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
