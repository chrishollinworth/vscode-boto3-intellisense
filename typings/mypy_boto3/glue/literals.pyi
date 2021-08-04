"""
Type annotations for glue service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/literals.html)

Usage::

    ```python
    from mypy_boto3_glue.literals import BackfillErrorCodeType

    data: BackfillErrorCodeType = "ENCRYPTED_PARTITION_ERROR"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BackfillErrorCodeType",
    "CatalogEncryptionModeType",
    "CloudWatchEncryptionModeType",
    "ColumnStatisticsTypeType",
    "ComparatorType",
    "CompatibilityType",
    "ConnectionPropertyKeyType",
    "ConnectionTypeType",
    "CrawlStateType",
    "CrawlerLineageSettingsType",
    "CrawlerStateType",
    "CsvHeaderOptionType",
    "DataFormatType",
    "DeleteBehaviorType",
    "EnableHybridValuesType",
    "ExistConditionType",
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
    "JobBookmarksEncryptionModeType",
    "JobRunStateType",
    "LanguageType",
    "LastCrawlStatusType",
    "ListRegistriesPaginatorName",
    "ListSchemaVersionsPaginatorName",
    "ListSchemasPaginatorName",
    "LogicalOperatorType",
    "LogicalType",
    "MLUserDataEncryptionModeStringType",
    "NodeTypeType",
    "PartitionIndexStatusType",
    "PermissionType",
    "PrincipalTypeType",
    "RecrawlBehaviorType",
    "RegistryStatusType",
    "ResourceShareTypeType",
    "ResourceTypeType",
    "S3EncryptionModeType",
    "ScheduleStateType",
    "SchemaDiffTypeType",
    "SchemaStatusType",
    "SchemaVersionStatusType",
    "SortDirectionTypeType",
    "SortType",
    "TaskRunSortColumnTypeType",
    "TaskStatusTypeType",
    "TaskTypeType",
    "TransformSortColumnTypeType",
    "TransformStatusTypeType",
    "TransformTypeType",
    "TriggerStateType",
    "TriggerTypeType",
    "UpdateBehaviorType",
    "WorkerTypeType",
    "WorkflowRunStatusType",
)

BackfillErrorCodeType = Literal[
    "ENCRYPTED_PARTITION_ERROR",
    "INTERNAL_ERROR",
    "INVALID_PARTITION_TYPE_DATA_ERROR",
    "MISSING_PARTITION_VALUE_ERROR",
    "UNSUPPORTED_PARTITION_CHARACTER_ERROR",
]
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
CrawlStateType = Literal["CANCELLED", "CANCELLING", "FAILED", "RUNNING", "SUCCEEDED"]
CrawlerLineageSettingsType = Literal["DISABLE", "ENABLE"]
CrawlerStateType = Literal["READY", "RUNNING", "STOPPING"]
CsvHeaderOptionType = Literal["ABSENT", "PRESENT", "UNKNOWN"]
DataFormatType = Literal["AVRO", "JSON"]
DeleteBehaviorType = Literal["DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE", "LOG"]
EnableHybridValuesType = Literal["FALSE", "TRUE"]
ExistConditionType = Literal["MUST_EXIST", "NONE", "NOT_EXIST"]
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
JobBookmarksEncryptionModeType = Literal["CSE-KMS", "DISABLED"]
JobRunStateType = Literal[
    "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "SUCCEEDED", "TIMEOUT"
]
LanguageType = Literal["PYTHON", "SCALA"]
LastCrawlStatusType = Literal["CANCELLED", "FAILED", "SUCCEEDED"]
ListRegistriesPaginatorName = Literal["list_registries"]
ListSchemaVersionsPaginatorName = Literal["list_schema_versions"]
ListSchemasPaginatorName = Literal["list_schemas"]
LogicalOperatorType = Literal["EQUALS"]
LogicalType = Literal["AND", "ANY"]
MLUserDataEncryptionModeStringType = Literal["DISABLED", "SSE-KMS"]
NodeTypeType = Literal["CRAWLER", "JOB", "TRIGGER"]
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
PrincipalTypeType = Literal["GROUP", "ROLE", "USER"]
RecrawlBehaviorType = Literal["CRAWL_EVERYTHING", "CRAWL_NEW_FOLDERS_ONLY"]
RegistryStatusType = Literal["AVAILABLE", "DELETING"]
ResourceShareTypeType = Literal["ALL", "FOREIGN"]
ResourceTypeType = Literal["ARCHIVE", "FILE", "JAR"]
S3EncryptionModeType = Literal["DISABLED", "SSE-KMS", "SSE-S3"]
ScheduleStateType = Literal["NOT_SCHEDULED", "SCHEDULED", "TRANSITIONING"]
SchemaDiffTypeType = Literal["SYNTAX_DIFF"]
SchemaStatusType = Literal["AVAILABLE", "DELETING", "PENDING"]
SchemaVersionStatusType = Literal["AVAILABLE", "DELETING", "FAILURE", "PENDING"]
SortDirectionTypeType = Literal["ASCENDING", "DESCENDING"]
SortType = Literal["ASC", "DESC"]
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
UpdateBehaviorType = Literal["LOG", "UPDATE_IN_DATABASE"]
WorkerTypeType = Literal["G.1X", "G.2X", "Standard"]
WorkflowRunStatusType = Literal["COMPLETED", "ERROR", "RUNNING", "STOPPED", "STOPPING"]
