"""
Type annotations for dms service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/literals.html)

Usage::

    ```python
    from mypy_boto3_dms.literals import AssessmentReportTypeType

    data: AssessmentReportTypeType = "csv"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AssessmentReportTypeType",
    "AuthMechanismValueType",
    "AuthTypeValueType",
    "CannedAclForObjectsValueType",
    "CharLengthSemanticsType",
    "CollectorStatusType",
    "CompressionTypeValueType",
    "DataFormatValueType",
    "DatabaseModeType",
    "DatePartitionDelimiterValueType",
    "DatePartitionSequenceValueType",
    "DescribeCertificatesPaginatorName",
    "DescribeConnectionsPaginatorName",
    "DescribeEndpointTypesPaginatorName",
    "DescribeEndpointsPaginatorName",
    "DescribeEventSubscriptionsPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeOrderableReplicationInstancesPaginatorName",
    "DescribeReplicationInstancesPaginatorName",
    "DescribeReplicationSubnetGroupsPaginatorName",
    "DescribeReplicationTaskAssessmentResultsPaginatorName",
    "DescribeReplicationTasksPaginatorName",
    "DescribeSchemasPaginatorName",
    "DescribeTableStatisticsPaginatorName",
    "DmsSslModeValueType",
    "EncodingTypeValueType",
    "EncryptionModeValueType",
    "EndpointDeletedWaiterName",
    "EndpointSettingTypeValueType",
    "KafkaSaslMechanismType",
    "KafkaSecurityProtocolType",
    "KafkaSslEndpointIdentificationAlgorithmType",
    "LongVarcharMappingTypeType",
    "MessageFormatValueType",
    "MigrationTypeValueType",
    "NestingLevelValueType",
    "OriginTypeValueType",
    "ParquetVersionValueType",
    "PluginNameValueType",
    "RedisAuthTypeValueType",
    "RefreshSchemasStatusTypeValueType",
    "ReleaseStatusValuesType",
    "ReloadOptionValueType",
    "ReplicationEndpointTypeValueType",
    "ReplicationInstanceAvailableWaiterName",
    "ReplicationInstanceDeletedWaiterName",
    "ReplicationTaskDeletedWaiterName",
    "ReplicationTaskReadyWaiterName",
    "ReplicationTaskRunningWaiterName",
    "ReplicationTaskStoppedWaiterName",
    "SafeguardPolicyType",
    "SourceTypeType",
    "SslSecurityProtocolValueType",
    "StartReplicationTaskTypeValueType",
    "TargetDbTypeType",
    "TestConnectionSucceedsWaiterName",
    "TlogAccessModeType",
    "VersionStatusType",
)

AssessmentReportTypeType = Literal["csv", "pdf"]
AuthMechanismValueType = Literal["default", "mongodb_cr", "scram_sha_1"]
AuthTypeValueType = Literal["no", "password"]
CannedAclForObjectsValueType = Literal[
    "authenticated-read",
    "aws-exec-read",
    "bucket-owner-full-control",
    "bucket-owner-read",
    "none",
    "private",
    "public-read",
    "public-read-write",
]
CharLengthSemanticsType = Literal["byte", "char", "default"]
CollectorStatusType = Literal["ACTIVE", "UNREGISTERED"]
CompressionTypeValueType = Literal["gzip", "none"]
DataFormatValueType = Literal["csv", "parquet"]
DatabaseModeType = Literal["babelfish", "default"]
DatePartitionDelimiterValueType = Literal["DASH", "NONE", "SLASH", "UNDERSCORE"]
DatePartitionSequenceValueType = Literal["DDMMYYYY", "MMYYYYDD", "YYYYMM", "YYYYMMDD", "YYYYMMDDHH"]
DescribeCertificatesPaginatorName = Literal["describe_certificates"]
DescribeConnectionsPaginatorName = Literal["describe_connections"]
DescribeEndpointTypesPaginatorName = Literal["describe_endpoint_types"]
DescribeEndpointsPaginatorName = Literal["describe_endpoints"]
DescribeEventSubscriptionsPaginatorName = Literal["describe_event_subscriptions"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeOrderableReplicationInstancesPaginatorName = Literal[
    "describe_orderable_replication_instances"
]
DescribeReplicationInstancesPaginatorName = Literal["describe_replication_instances"]
DescribeReplicationSubnetGroupsPaginatorName = Literal["describe_replication_subnet_groups"]
DescribeReplicationTaskAssessmentResultsPaginatorName = Literal[
    "describe_replication_task_assessment_results"
]
DescribeReplicationTasksPaginatorName = Literal["describe_replication_tasks"]
DescribeSchemasPaginatorName = Literal["describe_schemas"]
DescribeTableStatisticsPaginatorName = Literal["describe_table_statistics"]
DmsSslModeValueType = Literal["none", "require", "verify-ca", "verify-full"]
EncodingTypeValueType = Literal["plain", "plain-dictionary", "rle-dictionary"]
EncryptionModeValueType = Literal["sse-kms", "sse-s3"]
EndpointDeletedWaiterName = Literal["endpoint_deleted"]
EndpointSettingTypeValueType = Literal["boolean", "enum", "integer", "string"]
KafkaSaslMechanismType = Literal["plain", "scram-sha-512"]
KafkaSecurityProtocolType = Literal["plaintext", "sasl-ssl", "ssl-authentication", "ssl-encryption"]
KafkaSslEndpointIdentificationAlgorithmType = Literal["https", "none"]
LongVarcharMappingTypeType = Literal["clob", "nclob", "wstring"]
MessageFormatValueType = Literal["json", "json-unformatted"]
MigrationTypeValueType = Literal["cdc", "full-load", "full-load-and-cdc"]
NestingLevelValueType = Literal["none", "one"]
OriginTypeValueType = Literal["SOURCE", "TARGET"]
ParquetVersionValueType = Literal["parquet-1-0", "parquet-2-0"]
PluginNameValueType = Literal["no-preference", "pglogical", "test-decoding"]
RedisAuthTypeValueType = Literal["auth-role", "auth-token", "none"]
RefreshSchemasStatusTypeValueType = Literal["failed", "refreshing", "successful"]
ReleaseStatusValuesType = Literal["beta", "prod"]
ReloadOptionValueType = Literal["data-reload", "validate-only"]
ReplicationEndpointTypeValueType = Literal["source", "target"]
ReplicationInstanceAvailableWaiterName = Literal["replication_instance_available"]
ReplicationInstanceDeletedWaiterName = Literal["replication_instance_deleted"]
ReplicationTaskDeletedWaiterName = Literal["replication_task_deleted"]
ReplicationTaskReadyWaiterName = Literal["replication_task_ready"]
ReplicationTaskRunningWaiterName = Literal["replication_task_running"]
ReplicationTaskStoppedWaiterName = Literal["replication_task_stopped"]
SafeguardPolicyType = Literal[
    "exclusive-automatic-truncation",
    "rely-on-sql-server-replication-agent",
    "shared-automatic-truncation",
]
SourceTypeType = Literal["replication-instance"]
SslSecurityProtocolValueType = Literal["plaintext", "ssl-encryption"]
StartReplicationTaskTypeValueType = Literal[
    "reload-target", "resume-processing", "start-replication"
]
TargetDbTypeType = Literal["multiple-databases", "specific-database"]
TestConnectionSucceedsWaiterName = Literal["test_connection_succeeds"]
TlogAccessModeType = Literal["BackupOnly", "PreferBackup", "PreferTlog", "TlogOnly"]
VersionStatusType = Literal["OUTDATED", "UNSUPPORTED", "UP_TO_DATE"]
