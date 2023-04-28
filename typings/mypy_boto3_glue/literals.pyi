"""
Type annotations for glue service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/literals.html)

Usage::

    ```python
    from mypy_boto3_glue.literals import AggFunctionType

    data: AggFunctionType = "avg"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AggFunctionType",
    "BackfillErrorCodeType",
    "BlueprintRunStateType",
    "BlueprintStatusType",
    "CatalogEncryptionModeType",
    "CloudWatchEncryptionModeType",
    "ColumnStatisticsTypeType",
    "ComparatorType",
    "CompatibilityType",
    "CompressionTypeType",
    "ConnectionPropertyKeyType",
    "ConnectionTypeType",
    "CrawlStateType",
    "CrawlerHistoryStateType",
    "CrawlerLineageSettingsType",
    "CrawlerStateType",
    "CsvHeaderOptionType",
    "DQStopJobOnFailureTimingType",
    "DQTransformOutputType",
    "DataFormatType",
    "DataQualityRuleResultStatusType",
    "DeleteBehaviorType",
    "DeltaTargetCompressionTypeType",
    "EnableHybridValuesType",
    "ExecutionClassType",
    "ExistConditionType",
    "FieldNameType",
    "FilterLogicalOperatorType",
    "FilterOperationType",
    "FilterOperatorType",
    "FilterValueTypeType",
    "GetClassifiersPaginatorName",
    "GetConnectionsPaginatorName",
    "GetCrawlerMetricsPaginatorName",
    "GetCrawlersPaginatorName",
    "GetDatabasesPaginatorName",
    "GetDevEndpointsPaginatorName",
    "GetJobRunsPaginatorName",
    "GetJobsPaginatorName",
    "GetPartitionIndexesPaginatorName",
    "GetPartitionsPaginatorName",
    "GetResourcePoliciesPaginatorName",
    "GetSecurityConfigurationsPaginatorName",
    "GetTableVersionsPaginatorName",
    "GetTablesPaginatorName",
    "GetTriggersPaginatorName",
    "GetUserDefinedFunctionsPaginatorName",
    "GlueRecordTypeType",
    "HudiTargetCompressionTypeType",
    "JDBCConnectionTypeType",
    "JDBCDataTypeType",
    "JdbcMetadataEntryType",
    "JobBookmarksEncryptionModeType",
    "JobRunStateType",
    "JoinTypeType",
    "LanguageType",
    "LastCrawlStatusType",
    "ListRegistriesPaginatorName",
    "ListSchemaVersionsPaginatorName",
    "ListSchemasPaginatorName",
    "LogicalOperatorType",
    "LogicalType",
    "MLUserDataEncryptionModeStringType",
    "NodeTypeType",
    "ParamTypeType",
    "ParquetCompressionTypeType",
    "PartitionIndexStatusType",
    "PermissionType",
    "PermissionTypeType",
    "PiiTypeType",
    "PrincipalTypeType",
    "QuoteCharType",
    "RecrawlBehaviorType",
    "RegistryStatusType",
    "ResourceShareTypeType",
    "ResourceTypeType",
    "S3EncryptionModeType",
    "ScheduleStateType",
    "SchemaDiffTypeType",
    "SchemaStatusType",
    "SchemaVersionStatusType",
    "SeparatorType",
    "SessionStatusType",
    "SortDirectionTypeType",
    "SortType",
    "SourceControlAuthStrategyType",
    "SourceControlProviderType",
    "StartingPositionType",
    "StatementStateType",
    "TargetFormatType",
    "TaskRunSortColumnTypeType",
    "TaskStatusTypeType",
    "TaskTypeType",
    "TransformSortColumnTypeType",
    "TransformStatusTypeType",
    "TransformTypeType",
    "TriggerStateType",
    "TriggerTypeType",
    "UnionTypeType",
    "UpdateBehaviorType",
    "UpdateCatalogBehaviorType",
    "WorkerTypeType",
    "WorkflowRunStatusType",
)

AggFunctionType = Literal[
    "avg",
    "count",
    "countDistinct",
    "first",
    "kurtosis",
    "last",
    "max",
    "min",
    "skewness",
    "stddev_pop",
    "stddev_samp",
    "sum",
    "sumDistinct",
    "var_pop",
    "var_samp",
]
BackfillErrorCodeType = Literal[
    "ENCRYPTED_PARTITION_ERROR",
    "INTERNAL_ERROR",
    "INVALID_PARTITION_TYPE_DATA_ERROR",
    "MISSING_PARTITION_VALUE_ERROR",
    "UNSUPPORTED_PARTITION_CHARACTER_ERROR",
]
BlueprintRunStateType = Literal["FAILED", "ROLLING_BACK", "RUNNING", "SUCCEEDED"]
BlueprintStatusType = Literal["ACTIVE", "CREATING", "FAILED", "UPDATING"]
CatalogEncryptionModeType = Literal["DISABLED", "SSE-KMS"]
CloudWatchEncryptionModeType = Literal["DISABLED", "SSE-KMS"]
ColumnStatisticsTypeType = Literal[
    "BINARY", "BOOLEAN", "DATE", "DECIMAL", "DOUBLE", "LONG", "STRING"
]
ComparatorType = Literal[
    "EQUALS", "GREATER_THAN", "GREATER_THAN_EQUALS", "LESS_THAN", "LESS_THAN_EQUALS"
]
CompatibilityType = Literal[
    "BACKWARD", "BACKWARD_ALL", "DISABLED", "FORWARD", "FORWARD_ALL", "FULL", "FULL_ALL", "NONE"
]
CompressionTypeType = Literal["bzip2", "gzip"]
ConnectionPropertyKeyType = Literal[
    "CONFIG_FILES",
    "CONNECTION_URL",
    "CONNECTOR_CLASS_NAME",
    "CONNECTOR_TYPE",
    "CONNECTOR_URL",
    "CUSTOM_JDBC_CERT",
    "CUSTOM_JDBC_CERT_STRING",
    "ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD",
    "ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD",
    "ENCRYPTED_PASSWORD",
    "HOST",
    "INSTANCE_ID",
    "JDBC_CONNECTION_URL",
    "JDBC_DRIVER_CLASS_NAME",
    "JDBC_DRIVER_JAR_URI",
    "JDBC_ENFORCE_SSL",
    "JDBC_ENGINE",
    "JDBC_ENGINE_VERSION",
    "KAFKA_BOOTSTRAP_SERVERS",
    "KAFKA_CLIENT_KEYSTORE",
    "KAFKA_CLIENT_KEYSTORE_PASSWORD",
    "KAFKA_CLIENT_KEY_PASSWORD",
    "KAFKA_CUSTOM_CERT",
    "KAFKA_SKIP_CUSTOM_CERT_VALIDATION",
    "KAFKA_SSL_ENABLED",
    "PASSWORD",
    "PORT",
    "SECRET_ID",
    "SKIP_CUSTOM_JDBC_CERT_VALIDATION",
    "USERNAME",
]
ConnectionTypeType = Literal["CUSTOM", "JDBC", "KAFKA", "MARKETPLACE", "MONGODB", "NETWORK", "SFTP"]
CrawlStateType = Literal["CANCELLED", "CANCELLING", "ERROR", "FAILED", "RUNNING", "SUCCEEDED"]
CrawlerHistoryStateType = Literal["COMPLETED", "FAILED", "RUNNING", "STOPPED"]
CrawlerLineageSettingsType = Literal["DISABLE", "ENABLE"]
CrawlerStateType = Literal["READY", "RUNNING", "STOPPING"]
CsvHeaderOptionType = Literal["ABSENT", "PRESENT", "UNKNOWN"]
DQStopJobOnFailureTimingType = Literal["AfterDataLoad", "Immediate"]
DQTransformOutputType = Literal["EvaluationResults", "PrimaryInput"]
DataFormatType = Literal["AVRO", "JSON", "PROTOBUF"]
DataQualityRuleResultStatusType = Literal["ERROR", "FAIL", "PASS"]
DeleteBehaviorType = Literal["DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE", "LOG"]
DeltaTargetCompressionTypeType = Literal["snappy", "uncompressed"]
EnableHybridValuesType = Literal["FALSE", "TRUE"]
ExecutionClassType = Literal["FLEX", "STANDARD"]
ExistConditionType = Literal["MUST_EXIST", "NONE", "NOT_EXIST"]
FieldNameType = Literal["CRAWL_ID", "DPU_HOUR", "END_TIME", "START_TIME", "STATE"]
FilterLogicalOperatorType = Literal["AND", "OR"]
FilterOperationType = Literal["EQ", "GT", "GTE", "ISNULL", "LT", "LTE", "REGEX"]
FilterOperatorType = Literal["EQ", "GE", "GT", "LE", "LT", "NE"]
FilterValueTypeType = Literal["COLUMNEXTRACTED", "CONSTANT"]
GetClassifiersPaginatorName = Literal["get_classifiers"]
GetConnectionsPaginatorName = Literal["get_connections"]
GetCrawlerMetricsPaginatorName = Literal["get_crawler_metrics"]
GetCrawlersPaginatorName = Literal["get_crawlers"]
GetDatabasesPaginatorName = Literal["get_databases"]
GetDevEndpointsPaginatorName = Literal["get_dev_endpoints"]
GetJobRunsPaginatorName = Literal["get_job_runs"]
GetJobsPaginatorName = Literal["get_jobs"]
GetPartitionIndexesPaginatorName = Literal["get_partition_indexes"]
GetPartitionsPaginatorName = Literal["get_partitions"]
GetResourcePoliciesPaginatorName = Literal["get_resource_policies"]
GetSecurityConfigurationsPaginatorName = Literal["get_security_configurations"]
GetTableVersionsPaginatorName = Literal["get_table_versions"]
GetTablesPaginatorName = Literal["get_tables"]
GetTriggersPaginatorName = Literal["get_triggers"]
GetUserDefinedFunctionsPaginatorName = Literal["get_user_defined_functions"]
GlueRecordTypeType = Literal[
    "BIGDECIMAL", "BYTE", "DATE", "DOUBLE", "FLOAT", "INT", "LONG", "SHORT", "STRING", "TIMESTAMP"
]
HudiTargetCompressionTypeType = Literal["gzip", "lzo", "snappy", "uncompressed"]
JDBCConnectionTypeType = Literal["mysql", "oracle", "postgresql", "redshift", "sqlserver"]
JDBCDataTypeType = Literal[
    "ARRAY",
    "BIGINT",
    "BINARY",
    "BIT",
    "BLOB",
    "BOOLEAN",
    "CHAR",
    "CLOB",
    "DATALINK",
    "DATE",
    "DECIMAL",
    "DISTINCT",
    "DOUBLE",
    "FLOAT",
    "INTEGER",
    "JAVA_OBJECT",
    "LONGNVARCHAR",
    "LONGVARBINARY",
    "LONGVARCHAR",
    "NCHAR",
    "NCLOB",
    "NULL",
    "NUMERIC",
    "NVARCHAR",
    "OTHER",
    "REAL",
    "REF",
    "REF_CURSOR",
    "ROWID",
    "SMALLINT",
    "SQLXML",
    "STRUCT",
    "TIME",
    "TIMESTAMP",
    "TIMESTAMP_WITH_TIMEZONE",
    "TIME_WITH_TIMEZONE",
    "TINYINT",
    "VARBINARY",
    "VARCHAR",
]
JdbcMetadataEntryType = Literal["COMMENTS", "RAWTYPES"]
JobBookmarksEncryptionModeType = Literal["CSE-KMS", "DISABLED"]
JobRunStateType = Literal[
    "ERROR",
    "FAILED",
    "RUNNING",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "SUCCEEDED",
    "TIMEOUT",
    "WAITING",
]
JoinTypeType = Literal["equijoin", "left", "leftanti", "leftsemi", "outer", "right"]
LanguageType = Literal["PYTHON", "SCALA"]
LastCrawlStatusType = Literal["CANCELLED", "FAILED", "SUCCEEDED"]
ListRegistriesPaginatorName = Literal["list_registries"]
ListSchemaVersionsPaginatorName = Literal["list_schema_versions"]
ListSchemasPaginatorName = Literal["list_schemas"]
LogicalOperatorType = Literal["EQUALS"]
LogicalType = Literal["AND", "ANY"]
MLUserDataEncryptionModeStringType = Literal["DISABLED", "SSE-KMS"]
NodeTypeType = Literal["CRAWLER", "JOB", "TRIGGER"]
ParamTypeType = Literal["bool", "complex", "float", "int", "list", "null", "str"]
ParquetCompressionTypeType = Literal["gzip", "lzo", "none", "snappy", "uncompressed"]
PartitionIndexStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
PermissionType = Literal[
    "ALL",
    "ALTER",
    "CREATE_DATABASE",
    "CREATE_TABLE",
    "DATA_LOCATION_ACCESS",
    "DELETE",
    "DROP",
    "INSERT",
    "SELECT",
]
PermissionTypeType = Literal["CELL_FILTER_PERMISSION", "COLUMN_PERMISSION"]
PiiTypeType = Literal["ColumnAudit", "ColumnMasking", "RowAudit", "RowMasking"]
PrincipalTypeType = Literal["GROUP", "ROLE", "USER"]
QuoteCharType = Literal["disabled", "quillemet", "quote", "single_quote"]
RecrawlBehaviorType = Literal["CRAWL_EVENT_MODE", "CRAWL_EVERYTHING", "CRAWL_NEW_FOLDERS_ONLY"]
RegistryStatusType = Literal["AVAILABLE", "DELETING"]
ResourceShareTypeType = Literal["ALL", "FEDERATED", "FOREIGN"]
ResourceTypeType = Literal["ARCHIVE", "FILE", "JAR"]
S3EncryptionModeType = Literal["DISABLED", "SSE-KMS", "SSE-S3"]
ScheduleStateType = Literal["NOT_SCHEDULED", "SCHEDULED", "TRANSITIONING"]
SchemaDiffTypeType = Literal["SYNTAX_DIFF"]
SchemaStatusType = Literal["AVAILABLE", "DELETING", "PENDING"]
SchemaVersionStatusType = Literal["AVAILABLE", "DELETING", "FAILURE", "PENDING"]
SeparatorType = Literal["comma", "ctrla", "pipe", "semicolon", "tab"]
SessionStatusType = Literal["FAILED", "PROVISIONING", "READY", "STOPPED", "STOPPING", "TIMEOUT"]
SortDirectionTypeType = Literal["ASCENDING", "DESCENDING"]
SortType = Literal["ASC", "DESC"]
SourceControlAuthStrategyType = Literal["AWS_SECRETS_MANAGER", "PERSONAL_ACCESS_TOKEN"]
SourceControlProviderType = Literal["AWS_CODE_COMMIT", "GITHUB"]
StartingPositionType = Literal["earliest", "latest", "trim_horizon"]
StatementStateType = Literal["AVAILABLE", "CANCELLED", "CANCELLING", "ERROR", "RUNNING", "WAITING"]
TargetFormatType = Literal["avro", "csv", "delta", "hudi", "json", "orc", "parquet"]
TaskRunSortColumnTypeType = Literal["STARTED", "STATUS", "TASK_RUN_TYPE"]
TaskStatusTypeType = Literal[
    "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "SUCCEEDED", "TIMEOUT"
]
TaskTypeType = Literal[
    "EVALUATION", "EXPORT_LABELS", "FIND_MATCHES", "IMPORT_LABELS", "LABELING_SET_GENERATION"
]
TransformSortColumnTypeType = Literal[
    "CREATED", "LAST_MODIFIED", "NAME", "STATUS", "TRANSFORM_TYPE"
]
TransformStatusTypeType = Literal["DELETING", "NOT_READY", "READY"]
TransformTypeType = Literal["FIND_MATCHES"]
TriggerStateType = Literal[
    "ACTIVATED",
    "ACTIVATING",
    "CREATED",
    "CREATING",
    "DEACTIVATED",
    "DEACTIVATING",
    "DELETING",
    "UPDATING",
]
TriggerTypeType = Literal["CONDITIONAL", "EVENT", "ON_DEMAND", "SCHEDULED"]
UnionTypeType = Literal["ALL", "DISTINCT"]
UpdateBehaviorType = Literal["LOG", "UPDATE_IN_DATABASE"]
UpdateCatalogBehaviorType = Literal["LOG", "UPDATE_IN_DATABASE"]
WorkerTypeType = Literal["G.025X", "G.1X", "G.2X", "Standard"]
WorkflowRunStatusType = Literal["COMPLETED", "ERROR", "RUNNING", "STOPPED", "STOPPING"]
