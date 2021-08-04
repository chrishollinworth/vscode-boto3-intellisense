"""
Type annotations for dms service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/literals.html)

Usage::

    ```python
    from mypy_boto3_dms.literals import AuthMechanismValueType

    data: AuthMechanismValueType = "default"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AuthMechanismValueType",
    "AuthTypeValueType",
    "CharLengthSemanticsType",
    "CompressionTypeValueType",
    "DataFormatValueType",
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
    "KafkaSecurityProtocolType",
    "MessageFormatValueType",
    "MigrationTypeValueType",
    "NestingLevelValueType",
    "ParquetVersionValueType",
    "PluginNameValueType",
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
    "StartReplicationTaskTypeValueType",
    "TargetDbTypeType",
    "TestConnectionSucceedsWaiterName",
)

AuthMechanismValueType = Literal["default", "mongodb_cr", "scram_sha_1"]
AuthTypeValueType = Literal["no", "password"]
CharLengthSemanticsType = Literal["byte", "char", "default"]
CompressionTypeValueType = Literal["gzip", "none"]
DataFormatValueType = Literal["csv", "parquet"]
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
KafkaSecurityProtocolType = Literal["plaintext", "sasl-ssl", "ssl-authentication", "ssl-encryption"]
MessageFormatValueType = Literal["json", "json-unformatted"]
MigrationTypeValueType = Literal["cdc", "full-load", "full-load-and-cdc"]
NestingLevelValueType = Literal["none", "one"]
ParquetVersionValueType = Literal["parquet-1-0", "parquet-2-0"]
PluginNameValueType = Literal["no-preference", "pglogical", "test-decoding"]
RefreshSchemasStatusTypeValueType = Literal["failed", "refreshing", "successful"]
ReleaseStatusValuesType = Literal["beta"]
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
StartReplicationTaskTypeValueType = Literal[
    "reload-target", "resume-processing", "start-replication"
]
TargetDbTypeType = Literal["multiple-databases", "specific-database"]
TestConnectionSucceedsWaiterName = Literal["test_connection_succeeds"]
