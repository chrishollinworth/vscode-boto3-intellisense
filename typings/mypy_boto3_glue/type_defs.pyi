"""
Main interface for glue service type definitions.

Usage::

    ```python
    from mypy_boto3_glue.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionTypeDef",
    "BackfillErrorTypeDef",
    "BatchStopJobRunErrorTypeDef",
    "BatchStopJobRunSuccessfulSubmissionTypeDef",
    "BatchUpdatePartitionFailureEntryTypeDef",
    "BinaryColumnStatisticsDataTypeDef",
    "BooleanColumnStatisticsDataTypeDef",
    "CatalogImportStatusTypeDef",
    "CatalogTargetTypeDef",
    "ClassifierTypeDef",
    "CloudWatchEncryptionTypeDef",
    "CodeGenEdgeTypeDef",
    "CodeGenNodeArgTypeDef",
    "CodeGenNodeTypeDef",
    "ColumnErrorTypeDef",
    "ColumnImportanceTypeDef",
    "ColumnStatisticsDataTypeDef",
    "ColumnStatisticsErrorTypeDef",
    "ColumnStatisticsTypeDef",
    "ColumnTypeDef",
    "ConditionTypeDef",
    "ConfusionMatrixTypeDef",
    "ConnectionPasswordEncryptionTypeDef",
    "ConnectionTypeDef",
    "ConnectionsListTypeDef",
    "CrawlTypeDef",
    "CrawlerMetricsTypeDef",
    "CrawlerNodeDetailsTypeDef",
    "CrawlerTargetsTypeDef",
    "CrawlerTypeDef",
    "CsvClassifierTypeDef",
    "DataCatalogEncryptionSettingsTypeDef",
    "DataLakePrincipalTypeDef",
    "DatabaseIdentifierTypeDef",
    "DatabaseTypeDef",
    "DateColumnStatisticsDataTypeDef",
    "DecimalColumnStatisticsDataTypeDef",
    "DecimalNumberTypeDef",
    "DevEndpointTypeDef",
    "DoubleColumnStatisticsDataTypeDef",
    "DynamoDBTargetTypeDef",
    "EdgeTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionConfigurationTypeDef",
    "ErrorDetailTypeDef",
    "ErrorDetailsTypeDef",
    "EvaluationMetricsTypeDef",
    "ExecutionPropertyTypeDef",
    "ExportLabelsTaskRunPropertiesTypeDef",
    "FindMatchesMetricsTypeDef",
    "FindMatchesParametersTypeDef",
    "FindMatchesTaskRunPropertiesTypeDef",
    "GluePolicyTypeDef",
    "GlueTableTypeDef",
    "GrokClassifierTypeDef",
    "ImportLabelsTaskRunPropertiesTypeDef",
    "JdbcTargetTypeDef",
    "JobBookmarkEntryTypeDef",
    "JobBookmarksEncryptionTypeDef",
    "JobCommandTypeDef",
    "JobNodeDetailsTypeDef",
    "JobRunTypeDef",
    "JobTypeDef",
    "JsonClassifierTypeDef",
    "KeySchemaElementTypeDef",
    "LabelingSetGenerationTaskRunPropertiesTypeDef",
    "LastCrawlInfoTypeDef",
    "LineageConfigurationTypeDef",
    "LongColumnStatisticsDataTypeDef",
    "MLTransformTypeDef",
    "MLUserDataEncryptionTypeDef",
    "MappingEntryTypeDef",
    "MetadataInfoTypeDef",
    "MongoDBTargetTypeDef",
    "NodeTypeDef",
    "NotificationPropertyTypeDef",
    "OrderTypeDef",
    "PartitionErrorTypeDef",
    "PartitionIndexDescriptorTypeDef",
    "PartitionInputTypeDef",
    "PartitionTypeDef",
    "PartitionValueListTypeDef",
    "PhysicalConnectionRequirementsTypeDef",
    "PredecessorTypeDef",
    "PredicateTypeDef",
    "PrincipalPermissionsTypeDef",
    "RecrawlPolicyTypeDef",
    "RegistryListItemTypeDef",
    "ResourceUriTypeDef",
    "S3EncryptionTypeDef",
    "S3TargetTypeDef",
    "ScheduleTypeDef",
    "SchemaChangePolicyTypeDef",
    "SchemaColumnTypeDef",
    "SchemaIdTypeDef",
    "SchemaListItemTypeDef",
    "SchemaReferenceTypeDef",
    "SchemaVersionErrorItemTypeDef",
    "SchemaVersionListItemTypeDef",
    "SecurityConfigurationTypeDef",
    "SerDeInfoTypeDef",
    "SkewedInfoTypeDef",
    "StorageDescriptorTypeDef",
    "StringColumnStatisticsDataTypeDef",
    "TableErrorTypeDef",
    "TableIdentifierTypeDef",
    "TableTypeDef",
    "TableVersionErrorTypeDef",
    "TableVersionTypeDef",
    "TaskRunPropertiesTypeDef",
    "TaskRunTypeDef",
    "TransformEncryptionTypeDef",
    "TransformParametersTypeDef",
    "TriggerNodeDetailsTypeDef",
    "TriggerTypeDef",
    "UserDefinedFunctionTypeDef",
    "WorkflowGraphTypeDef",
    "WorkflowRunStatisticsTypeDef",
    "WorkflowRunTypeDef",
    "WorkflowTypeDef",
    "XMLClassifierTypeDef",
    "BatchCreatePartitionResponseTypeDef",
    "BatchDeleteConnectionResponseTypeDef",
    "BatchDeletePartitionResponseTypeDef",
    "BatchDeleteTableResponseTypeDef",
    "BatchDeleteTableVersionResponseTypeDef",
    "BatchGetCrawlersResponseTypeDef",
    "BatchGetDevEndpointsResponseTypeDef",
    "BatchGetJobsResponseTypeDef",
    "BatchGetPartitionResponseTypeDef",
    "BatchGetTriggersResponseTypeDef",
    "BatchGetWorkflowsResponseTypeDef",
    "BatchStopJobRunResponseTypeDef",
    "BatchUpdatePartitionRequestEntryTypeDef",
    "BatchUpdatePartitionResponseTypeDef",
    "CancelMLTaskRunResponseTypeDef",
    "CatalogEntryTypeDef",
    "CheckSchemaVersionValidityResponseTypeDef",
    "ConnectionInputTypeDef",
    "CreateCsvClassifierRequestTypeDef",
    "CreateDevEndpointResponseTypeDef",
    "CreateGrokClassifierRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreateJsonClassifierRequestTypeDef",
    "CreateMLTransformResponseTypeDef",
    "CreateRegistryResponseTypeDef",
    "CreateSchemaResponseTypeDef",
    "CreateScriptResponseTypeDef",
    "CreateSecurityConfigurationResponseTypeDef",
    "CreateTriggerResponseTypeDef",
    "CreateWorkflowResponseTypeDef",
    "CreateXMLClassifierRequestTypeDef",
    "DatabaseInputTypeDef",
    "DeleteJobResponseTypeDef",
    "DeleteMLTransformResponseTypeDef",
    "DeleteRegistryResponseTypeDef",
    "DeleteSchemaResponseTypeDef",
    "DeleteSchemaVersionsResponseTypeDef",
    "DeleteTriggerResponseTypeDef",
    "DeleteWorkflowResponseTypeDef",
    "DevEndpointCustomLibrariesTypeDef",
    "GetCatalogImportStatusResponseTypeDef",
    "GetClassifierResponseTypeDef",
    "GetClassifiersResponseTypeDef",
    "GetColumnStatisticsForPartitionResponseTypeDef",
    "GetColumnStatisticsForTableResponseTypeDef",
    "GetConnectionResponseTypeDef",
    "GetConnectionsFilterTypeDef",
    "GetConnectionsResponseTypeDef",
    "GetCrawlerMetricsResponseTypeDef",
    "GetCrawlerResponseTypeDef",
    "GetCrawlersResponseTypeDef",
    "GetDataCatalogEncryptionSettingsResponseTypeDef",
    "GetDatabaseResponseTypeDef",
    "GetDatabasesResponseTypeDef",
    "GetDataflowGraphResponseTypeDef",
    "GetDevEndpointResponseTypeDef",
    "GetDevEndpointsResponseTypeDef",
    "GetJobBookmarkResponseTypeDef",
    "GetJobResponseTypeDef",
    "GetJobRunResponseTypeDef",
    "GetJobRunsResponseTypeDef",
    "GetJobsResponseTypeDef",
    "GetMLTaskRunResponseTypeDef",
    "GetMLTaskRunsResponseTypeDef",
    "GetMLTransformResponseTypeDef",
    "GetMLTransformsResponseTypeDef",
    "GetMappingResponseTypeDef",
    "GetPartitionIndexesResponseTypeDef",
    "GetPartitionResponseTypeDef",
    "GetPartitionsResponseTypeDef",
    "GetPlanResponseTypeDef",
    "GetRegistryResponseTypeDef",
    "GetResourcePoliciesResponseTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetSchemaByDefinitionResponseTypeDef",
    "GetSchemaResponseTypeDef",
    "GetSchemaVersionResponseTypeDef",
    "GetSchemaVersionsDiffResponseTypeDef",
    "GetSecurityConfigurationResponseTypeDef",
    "GetSecurityConfigurationsResponseTypeDef",
    "GetTableResponseTypeDef",
    "GetTableVersionResponseTypeDef",
    "GetTableVersionsResponseTypeDef",
    "GetTablesResponseTypeDef",
    "GetTagsResponseTypeDef",
    "GetTriggerResponseTypeDef",
    "GetTriggersResponseTypeDef",
    "GetUserDefinedFunctionResponseTypeDef",
    "GetUserDefinedFunctionsResponseTypeDef",
    "GetWorkflowResponseTypeDef",
    "GetWorkflowRunPropertiesResponseTypeDef",
    "GetWorkflowRunResponseTypeDef",
    "GetWorkflowRunsResponseTypeDef",
    "JobUpdateTypeDef",
    "ListCrawlersResponseTypeDef",
    "ListDevEndpointsResponseTypeDef",
    "ListJobsResponseTypeDef",
    "ListMLTransformsResponseTypeDef",
    "ListRegistriesResponseTypeDef",
    "ListSchemaVersionsResponseTypeDef",
    "ListSchemasResponseTypeDef",
    "ListTriggersResponseTypeDef",
    "ListWorkflowsResponseTypeDef",
    "LocationTypeDef",
    "MetadataKeyValuePairTypeDef",
    "PaginatorConfigTypeDef",
    "PartitionIndexTypeDef",
    "PropertyPredicateTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "PutSchemaVersionMetadataResponseTypeDef",
    "QuerySchemaVersionMetadataResponseTypeDef",
    "RegisterSchemaVersionResponseTypeDef",
    "RegistryIdTypeDef",
    "RemoveSchemaVersionMetadataResponseTypeDef",
    "ResetJobBookmarkResponseTypeDef",
    "ResumeWorkflowRunResponseTypeDef",
    "SchemaVersionNumberTypeDef",
    "SearchTablesResponseTypeDef",
    "SegmentTypeDef",
    "SortCriterionTypeDef",
    "StartExportLabelsTaskRunResponseTypeDef",
    "StartImportLabelsTaskRunResponseTypeDef",
    "StartJobRunResponseTypeDef",
    "StartMLEvaluationTaskRunResponseTypeDef",
    "StartMLLabelingSetGenerationTaskRunResponseTypeDef",
    "StartTriggerResponseTypeDef",
    "StartWorkflowRunResponseTypeDef",
    "StopTriggerResponseTypeDef",
    "TableInputTypeDef",
    "TaskRunFilterCriteriaTypeDef",
    "TaskRunSortCriteriaTypeDef",
    "TransformFilterCriteriaTypeDef",
    "TransformSortCriteriaTypeDef",
    "TriggerUpdateTypeDef",
    "UpdateColumnStatisticsForPartitionResponseTypeDef",
    "UpdateColumnStatisticsForTableResponseTypeDef",
    "UpdateCsvClassifierRequestTypeDef",
    "UpdateGrokClassifierRequestTypeDef",
    "UpdateJobResponseTypeDef",
    "UpdateJsonClassifierRequestTypeDef",
    "UpdateMLTransformResponseTypeDef",
    "UpdateRegistryResponseTypeDef",
    "UpdateSchemaResponseTypeDef",
    "UpdateTriggerResponseTypeDef",
    "UpdateWorkflowResponseTypeDef",
    "UpdateXMLClassifierRequestTypeDef",
    "UserDefinedFunctionInputTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "JobName": str,
        "Arguments": Dict[str, str],
        "Timeout": int,
        "SecurityConfiguration": str,
        "NotificationProperty": "NotificationPropertyTypeDef",
        "CrawlerName": str,
    },
    total=False,
)

BackfillErrorTypeDef = TypedDict(
    "BackfillErrorTypeDef",
    {
        "Code": Literal[
            "ENCRYPTED_PARTITION_ERROR",
            "INTERNAL_ERROR",
            "INVALID_PARTITION_TYPE_DATA_ERROR",
            "MISSING_PARTITION_VALUE_ERROR",
            "UNSUPPORTED_PARTITION_CHARACTER_ERROR",
        ],
        "Partitions": List["PartitionValueListTypeDef"],
    },
    total=False,
)

BatchStopJobRunErrorTypeDef = TypedDict(
    "BatchStopJobRunErrorTypeDef",
    {"JobName": str, "JobRunId": str, "ErrorDetail": "ErrorDetailTypeDef"},
    total=False,
)

BatchStopJobRunSuccessfulSubmissionTypeDef = TypedDict(
    "BatchStopJobRunSuccessfulSubmissionTypeDef", {"JobName": str, "JobRunId": str}, total=False
)

BatchUpdatePartitionFailureEntryTypeDef = TypedDict(
    "BatchUpdatePartitionFailureEntryTypeDef",
    {"PartitionValueList": List[str], "ErrorDetail": "ErrorDetailTypeDef"},
    total=False,
)

BinaryColumnStatisticsDataTypeDef = TypedDict(
    "BinaryColumnStatisticsDataTypeDef",
    {"MaximumLength": int, "AverageLength": float, "NumberOfNulls": int},
)

BooleanColumnStatisticsDataTypeDef = TypedDict(
    "BooleanColumnStatisticsDataTypeDef",
    {"NumberOfTrues": int, "NumberOfFalses": int, "NumberOfNulls": int},
)

CatalogImportStatusTypeDef = TypedDict(
    "CatalogImportStatusTypeDef",
    {"ImportCompleted": bool, "ImportTime": datetime, "ImportedBy": str},
    total=False,
)

CatalogTargetTypeDef = TypedDict("CatalogTargetTypeDef", {"DatabaseName": str, "Tables": List[str]})

ClassifierTypeDef = TypedDict(
    "ClassifierTypeDef",
    {
        "GrokClassifier": "GrokClassifierTypeDef",
        "XMLClassifier": "XMLClassifierTypeDef",
        "JsonClassifier": "JsonClassifierTypeDef",
        "CsvClassifier": "CsvClassifierTypeDef",
    },
    total=False,
)

CloudWatchEncryptionTypeDef = TypedDict(
    "CloudWatchEncryptionTypeDef",
    {"CloudWatchEncryptionMode": Literal["DISABLED", "SSE-KMS"], "KmsKeyArn": str},
    total=False,
)

_RequiredCodeGenEdgeTypeDef = TypedDict(
    "_RequiredCodeGenEdgeTypeDef", {"Source": str, "Target": str}
)
_OptionalCodeGenEdgeTypeDef = TypedDict(
    "_OptionalCodeGenEdgeTypeDef", {"TargetParameter": str}, total=False
)


class CodeGenEdgeTypeDef(_RequiredCodeGenEdgeTypeDef, _OptionalCodeGenEdgeTypeDef):
    pass


_RequiredCodeGenNodeArgTypeDef = TypedDict(
    "_RequiredCodeGenNodeArgTypeDef", {"Name": str, "Value": str}
)
_OptionalCodeGenNodeArgTypeDef = TypedDict(
    "_OptionalCodeGenNodeArgTypeDef", {"Param": bool}, total=False
)


class CodeGenNodeArgTypeDef(_RequiredCodeGenNodeArgTypeDef, _OptionalCodeGenNodeArgTypeDef):
    pass


_RequiredCodeGenNodeTypeDef = TypedDict(
    "_RequiredCodeGenNodeTypeDef",
    {"Id": str, "NodeType": str, "Args": List["CodeGenNodeArgTypeDef"]},
)
_OptionalCodeGenNodeTypeDef = TypedDict(
    "_OptionalCodeGenNodeTypeDef", {"LineNumber": int}, total=False
)


class CodeGenNodeTypeDef(_RequiredCodeGenNodeTypeDef, _OptionalCodeGenNodeTypeDef):
    pass


ColumnErrorTypeDef = TypedDict(
    "ColumnErrorTypeDef", {"ColumnName": str, "Error": "ErrorDetailTypeDef"}, total=False
)

ColumnImportanceTypeDef = TypedDict(
    "ColumnImportanceTypeDef", {"ColumnName": str, "Importance": float}, total=False
)

_RequiredColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredColumnStatisticsDataTypeDef",
    {"Type": Literal["BOOLEAN", "DATE", "DECIMAL", "DOUBLE", "LONG", "STRING", "BINARY"]},
)
_OptionalColumnStatisticsDataTypeDef = TypedDict(
    "_OptionalColumnStatisticsDataTypeDef",
    {
        "BooleanColumnStatisticsData": "BooleanColumnStatisticsDataTypeDef",
        "DateColumnStatisticsData": "DateColumnStatisticsDataTypeDef",
        "DecimalColumnStatisticsData": "DecimalColumnStatisticsDataTypeDef",
        "DoubleColumnStatisticsData": "DoubleColumnStatisticsDataTypeDef",
        "LongColumnStatisticsData": "LongColumnStatisticsDataTypeDef",
        "StringColumnStatisticsData": "StringColumnStatisticsDataTypeDef",
        "BinaryColumnStatisticsData": "BinaryColumnStatisticsDataTypeDef",
    },
    total=False,
)


class ColumnStatisticsDataTypeDef(
    _RequiredColumnStatisticsDataTypeDef, _OptionalColumnStatisticsDataTypeDef
):
    pass


ColumnStatisticsErrorTypeDef = TypedDict(
    "ColumnStatisticsErrorTypeDef",
    {"ColumnStatistics": "ColumnStatisticsTypeDef", "Error": "ErrorDetailTypeDef"},
    total=False,
)

ColumnStatisticsTypeDef = TypedDict(
    "ColumnStatisticsTypeDef",
    {
        "ColumnName": str,
        "ColumnType": str,
        "AnalyzedTime": datetime,
        "StatisticsData": "ColumnStatisticsDataTypeDef",
    },
)

_RequiredColumnTypeDef = TypedDict("_RequiredColumnTypeDef", {"Name": str})
_OptionalColumnTypeDef = TypedDict(
    "_OptionalColumnTypeDef",
    {"Type": str, "Comment": str, "Parameters": Dict[str, str]},
    total=False,
)


class ColumnTypeDef(_RequiredColumnTypeDef, _OptionalColumnTypeDef):
    pass


ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "LogicalOperator": Literal["EQUALS"],
        "JobName": str,
        "State": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "CrawlerName": str,
        "CrawlState": Literal["RUNNING", "CANCELLING", "CANCELLED", "SUCCEEDED", "FAILED"],
    },
    total=False,
)

ConfusionMatrixTypeDef = TypedDict(
    "ConfusionMatrixTypeDef",
    {
        "NumTruePositives": int,
        "NumFalsePositives": int,
        "NumTrueNegatives": int,
        "NumFalseNegatives": int,
    },
    total=False,
)

_RequiredConnectionPasswordEncryptionTypeDef = TypedDict(
    "_RequiredConnectionPasswordEncryptionTypeDef", {"ReturnConnectionPasswordEncrypted": bool}
)
_OptionalConnectionPasswordEncryptionTypeDef = TypedDict(
    "_OptionalConnectionPasswordEncryptionTypeDef", {"AwsKmsKeyId": str}, total=False
)


class ConnectionPasswordEncryptionTypeDef(
    _RequiredConnectionPasswordEncryptionTypeDef, _OptionalConnectionPasswordEncryptionTypeDef
):
    pass


ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "Name": str,
        "Description": str,
        "ConnectionType": Literal[
            "JDBC", "SFTP", "MONGODB", "KAFKA", "NETWORK", "MARKETPLACE", "CUSTOM"
        ],
        "MatchCriteria": List[str],
        "ConnectionProperties": Dict[
            Literal[
                "HOST",
                "PORT",
                "USERNAME",
                "PASSWORD",
                "ENCRYPTED_PASSWORD",
                "JDBC_DRIVER_JAR_URI",
                "JDBC_DRIVER_CLASS_NAME",
                "JDBC_ENGINE",
                "JDBC_ENGINE_VERSION",
                "CONFIG_FILES",
                "INSTANCE_ID",
                "JDBC_CONNECTION_URL",
                "JDBC_ENFORCE_SSL",
                "CUSTOM_JDBC_CERT",
                "SKIP_CUSTOM_JDBC_CERT_VALIDATION",
                "CUSTOM_JDBC_CERT_STRING",
                "CONNECTION_URL",
                "KAFKA_BOOTSTRAP_SERVERS",
                "KAFKA_SSL_ENABLED",
                "KAFKA_CUSTOM_CERT",
                "KAFKA_SKIP_CUSTOM_CERT_VALIDATION",
                "SECRET_ID",
                "CONNECTOR_URL",
                "CONNECTOR_TYPE",
                "CONNECTOR_CLASS_NAME",
            ],
            str,
        ],
        "PhysicalConnectionRequirements": "PhysicalConnectionRequirementsTypeDef",
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "LastUpdatedBy": str,
    },
    total=False,
)

ConnectionsListTypeDef = TypedDict(
    "ConnectionsListTypeDef", {"Connections": List[str]}, total=False
)

CrawlTypeDef = TypedDict(
    "CrawlTypeDef",
    {
        "State": Literal["RUNNING", "CANCELLING", "CANCELLED", "SUCCEEDED", "FAILED"],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
    },
    total=False,
)

CrawlerMetricsTypeDef = TypedDict(
    "CrawlerMetricsTypeDef",
    {
        "CrawlerName": str,
        "TimeLeftSeconds": float,
        "StillEstimating": bool,
        "LastRuntimeSeconds": float,
        "MedianRuntimeSeconds": float,
        "TablesCreated": int,
        "TablesUpdated": int,
        "TablesDeleted": int,
    },
    total=False,
)

CrawlerNodeDetailsTypeDef = TypedDict(
    "CrawlerNodeDetailsTypeDef", {"Crawls": List["CrawlTypeDef"]}, total=False
)

CrawlerTargetsTypeDef = TypedDict(
    "CrawlerTargetsTypeDef",
    {
        "S3Targets": List["S3TargetTypeDef"],
        "JdbcTargets": List["JdbcTargetTypeDef"],
        "MongoDBTargets": List["MongoDBTargetTypeDef"],
        "DynamoDBTargets": List["DynamoDBTargetTypeDef"],
        "CatalogTargets": List["CatalogTargetTypeDef"],
    },
    total=False,
)

CrawlerTypeDef = TypedDict(
    "CrawlerTypeDef",
    {
        "Name": str,
        "Role": str,
        "Targets": "CrawlerTargetsTypeDef",
        "DatabaseName": str,
        "Description": str,
        "Classifiers": List[str],
        "RecrawlPolicy": "RecrawlPolicyTypeDef",
        "SchemaChangePolicy": "SchemaChangePolicyTypeDef",
        "LineageConfiguration": "LineageConfigurationTypeDef",
        "State": Literal["READY", "RUNNING", "STOPPING"],
        "TablePrefix": str,
        "Schedule": "ScheduleTypeDef",
        "CrawlElapsedTime": int,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "LastCrawl": "LastCrawlInfoTypeDef",
        "Version": int,
        "Configuration": str,
        "CrawlerSecurityConfiguration": str,
    },
    total=False,
)

_RequiredCsvClassifierTypeDef = TypedDict("_RequiredCsvClassifierTypeDef", {"Name": str})
_OptionalCsvClassifierTypeDef = TypedDict(
    "_OptionalCsvClassifierTypeDef",
    {
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": Literal["UNKNOWN", "PRESENT", "ABSENT"],
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)


class CsvClassifierTypeDef(_RequiredCsvClassifierTypeDef, _OptionalCsvClassifierTypeDef):
    pass


DataCatalogEncryptionSettingsTypeDef = TypedDict(
    "DataCatalogEncryptionSettingsTypeDef",
    {
        "EncryptionAtRest": "EncryptionAtRestTypeDef",
        "ConnectionPasswordEncryption": "ConnectionPasswordEncryptionTypeDef",
    },
    total=False,
)

DataLakePrincipalTypeDef = TypedDict(
    "DataLakePrincipalTypeDef", {"DataLakePrincipalIdentifier": str}, total=False
)

DatabaseIdentifierTypeDef = TypedDict(
    "DatabaseIdentifierTypeDef", {"CatalogId": str, "DatabaseName": str}, total=False
)

_RequiredDatabaseTypeDef = TypedDict("_RequiredDatabaseTypeDef", {"Name": str})
_OptionalDatabaseTypeDef = TypedDict(
    "_OptionalDatabaseTypeDef",
    {
        "Description": str,
        "LocationUri": str,
        "Parameters": Dict[str, str],
        "CreateTime": datetime,
        "CreateTableDefaultPermissions": List["PrincipalPermissionsTypeDef"],
        "TargetDatabase": "DatabaseIdentifierTypeDef",
        "CatalogId": str,
    },
    total=False,
)


class DatabaseTypeDef(_RequiredDatabaseTypeDef, _OptionalDatabaseTypeDef):
    pass


_RequiredDateColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredDateColumnStatisticsDataTypeDef",
    {"NumberOfNulls": int, "NumberOfDistinctValues": int},
)
_OptionalDateColumnStatisticsDataTypeDef = TypedDict(
    "_OptionalDateColumnStatisticsDataTypeDef",
    {"MinimumValue": datetime, "MaximumValue": datetime},
    total=False,
)


class DateColumnStatisticsDataTypeDef(
    _RequiredDateColumnStatisticsDataTypeDef, _OptionalDateColumnStatisticsDataTypeDef
):
    pass


_RequiredDecimalColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredDecimalColumnStatisticsDataTypeDef",
    {"NumberOfNulls": int, "NumberOfDistinctValues": int},
)
_OptionalDecimalColumnStatisticsDataTypeDef = TypedDict(
    "_OptionalDecimalColumnStatisticsDataTypeDef",
    {"MinimumValue": "DecimalNumberTypeDef", "MaximumValue": "DecimalNumberTypeDef"},
    total=False,
)


class DecimalColumnStatisticsDataTypeDef(
    _RequiredDecimalColumnStatisticsDataTypeDef, _OptionalDecimalColumnStatisticsDataTypeDef
):
    pass


DecimalNumberTypeDef = TypedDict(
    "DecimalNumberTypeDef", {"UnscaledValue": Union[bytes, IO[bytes]], "Scale": int}
)

DevEndpointTypeDef = TypedDict(
    "DevEndpointTypeDef",
    {
        "EndpointName": str,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "YarnEndpointAddress": str,
        "PrivateAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "PublicAddress": str,
        "Status": str,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "NumberOfNodes": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "LastUpdateStatus": str,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "PublicKey": str,
        "PublicKeys": List[str],
        "SecurityConfiguration": str,
        "Arguments": Dict[str, str],
    },
    total=False,
)

_RequiredDoubleColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredDoubleColumnStatisticsDataTypeDef",
    {"NumberOfNulls": int, "NumberOfDistinctValues": int},
)
_OptionalDoubleColumnStatisticsDataTypeDef = TypedDict(
    "_OptionalDoubleColumnStatisticsDataTypeDef",
    {"MinimumValue": float, "MaximumValue": float},
    total=False,
)


class DoubleColumnStatisticsDataTypeDef(
    _RequiredDoubleColumnStatisticsDataTypeDef, _OptionalDoubleColumnStatisticsDataTypeDef
):
    pass


DynamoDBTargetTypeDef = TypedDict(
    "DynamoDBTargetTypeDef", {"Path": str, "scanAll": bool, "scanRate": float}, total=False
)

EdgeTypeDef = TypedDict("EdgeTypeDef", {"SourceId": str, "DestinationId": str}, total=False)

_RequiredEncryptionAtRestTypeDef = TypedDict(
    "_RequiredEncryptionAtRestTypeDef", {"CatalogEncryptionMode": Literal["DISABLED", "SSE-KMS"]}
)
_OptionalEncryptionAtRestTypeDef = TypedDict(
    "_OptionalEncryptionAtRestTypeDef", {"SseAwsKmsKeyId": str}, total=False
)


class EncryptionAtRestTypeDef(_RequiredEncryptionAtRestTypeDef, _OptionalEncryptionAtRestTypeDef):
    pass


EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "S3Encryption": List["S3EncryptionTypeDef"],
        "CloudWatchEncryption": "CloudWatchEncryptionTypeDef",
        "JobBookmarksEncryption": "JobBookmarksEncryptionTypeDef",
    },
    total=False,
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef", {"ErrorCode": str, "ErrorMessage": str}, total=False
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef", {"ErrorCode": str, "ErrorMessage": str}, total=False
)

_RequiredEvaluationMetricsTypeDef = TypedDict(
    "_RequiredEvaluationMetricsTypeDef", {"TransformType": Literal["FIND_MATCHES"]}
)
_OptionalEvaluationMetricsTypeDef = TypedDict(
    "_OptionalEvaluationMetricsTypeDef",
    {"FindMatchesMetrics": "FindMatchesMetricsTypeDef"},
    total=False,
)


class EvaluationMetricsTypeDef(
    _RequiredEvaluationMetricsTypeDef, _OptionalEvaluationMetricsTypeDef
):
    pass


ExecutionPropertyTypeDef = TypedDict(
    "ExecutionPropertyTypeDef", {"MaxConcurrentRuns": int}, total=False
)

ExportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "ExportLabelsTaskRunPropertiesTypeDef", {"OutputS3Path": str}, total=False
)

FindMatchesMetricsTypeDef = TypedDict(
    "FindMatchesMetricsTypeDef",
    {
        "AreaUnderPRCurve": float,
        "Precision": float,
        "Recall": float,
        "F1": float,
        "ConfusionMatrix": "ConfusionMatrixTypeDef",
        "ColumnImportances": List["ColumnImportanceTypeDef"],
    },
    total=False,
)

FindMatchesParametersTypeDef = TypedDict(
    "FindMatchesParametersTypeDef",
    {
        "PrimaryKeyColumnName": str,
        "PrecisionRecallTradeoff": float,
        "AccuracyCostTradeoff": float,
        "EnforceProvidedLabels": bool,
    },
    total=False,
)

FindMatchesTaskRunPropertiesTypeDef = TypedDict(
    "FindMatchesTaskRunPropertiesTypeDef",
    {"JobId": str, "JobName": str, "JobRunId": str},
    total=False,
)

GluePolicyTypeDef = TypedDict(
    "GluePolicyTypeDef",
    {"PolicyInJson": str, "PolicyHash": str, "CreateTime": datetime, "UpdateTime": datetime},
    total=False,
)

_RequiredGlueTableTypeDef = TypedDict(
    "_RequiredGlueTableTypeDef", {"DatabaseName": str, "TableName": str}
)
_OptionalGlueTableTypeDef = TypedDict(
    "_OptionalGlueTableTypeDef", {"CatalogId": str, "ConnectionName": str}, total=False
)


class GlueTableTypeDef(_RequiredGlueTableTypeDef, _OptionalGlueTableTypeDef):
    pass


_RequiredGrokClassifierTypeDef = TypedDict(
    "_RequiredGrokClassifierTypeDef", {"Name": str, "Classification": str, "GrokPattern": str}
)
_OptionalGrokClassifierTypeDef = TypedDict(
    "_OptionalGrokClassifierTypeDef",
    {"CreationTime": datetime, "LastUpdated": datetime, "Version": int, "CustomPatterns": str},
    total=False,
)


class GrokClassifierTypeDef(_RequiredGrokClassifierTypeDef, _OptionalGrokClassifierTypeDef):
    pass


ImportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "ImportLabelsTaskRunPropertiesTypeDef", {"InputS3Path": str, "Replace": bool}, total=False
)

JdbcTargetTypeDef = TypedDict(
    "JdbcTargetTypeDef", {"ConnectionName": str, "Path": str, "Exclusions": List[str]}, total=False
)

JobBookmarkEntryTypeDef = TypedDict(
    "JobBookmarkEntryTypeDef",
    {
        "JobName": str,
        "Version": int,
        "Run": int,
        "Attempt": int,
        "PreviousRunId": str,
        "RunId": str,
        "JobBookmark": str,
    },
    total=False,
)

JobBookmarksEncryptionTypeDef = TypedDict(
    "JobBookmarksEncryptionTypeDef",
    {"JobBookmarksEncryptionMode": Literal["DISABLED", "CSE-KMS"], "KmsKeyArn": str},
    total=False,
)

JobCommandTypeDef = TypedDict(
    "JobCommandTypeDef", {"Name": str, "ScriptLocation": str, "PythonVersion": str}, total=False
)

JobNodeDetailsTypeDef = TypedDict(
    "JobNodeDetailsTypeDef", {"JobRuns": List["JobRunTypeDef"]}, total=False
)

JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "Id": str,
        "Attempt": int,
        "PreviousRunId": str,
        "TriggerName": str,
        "JobName": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "JobRunState": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List["PredecessorTypeDef"],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": "NotificationPropertyTypeDef",
        "GlueVersion": str,
    },
    total=False,
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "Name": str,
        "Description": str,
        "LogUri": str,
        "Role": str,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "ExecutionProperty": "ExecutionPropertyTypeDef",
        "Command": "JobCommandTypeDef",
        "DefaultArguments": Dict[str, str],
        "NonOverridableArguments": Dict[str, str],
        "Connections": "ConnectionsListTypeDef",
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": "NotificationPropertyTypeDef",
        "GlueVersion": str,
    },
    total=False,
)

_RequiredJsonClassifierTypeDef = TypedDict(
    "_RequiredJsonClassifierTypeDef", {"Name": str, "JsonPath": str}
)
_OptionalJsonClassifierTypeDef = TypedDict(
    "_OptionalJsonClassifierTypeDef",
    {"CreationTime": datetime, "LastUpdated": datetime, "Version": int},
    total=False,
)


class JsonClassifierTypeDef(_RequiredJsonClassifierTypeDef, _OptionalJsonClassifierTypeDef):
    pass


KeySchemaElementTypeDef = TypedDict("KeySchemaElementTypeDef", {"Name": str, "Type": str})

LabelingSetGenerationTaskRunPropertiesTypeDef = TypedDict(
    "LabelingSetGenerationTaskRunPropertiesTypeDef", {"OutputS3Path": str}, total=False
)

LastCrawlInfoTypeDef = TypedDict(
    "LastCrawlInfoTypeDef",
    {
        "Status": Literal["SUCCEEDED", "CANCELLED", "FAILED"],
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
        "MessagePrefix": str,
        "StartTime": datetime,
    },
    total=False,
)

LineageConfigurationTypeDef = TypedDict(
    "LineageConfigurationTypeDef",
    {"CrawlerLineageSettings": Literal["ENABLE", "DISABLE"]},
    total=False,
)

_RequiredLongColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredLongColumnStatisticsDataTypeDef",
    {"NumberOfNulls": int, "NumberOfDistinctValues": int},
)
_OptionalLongColumnStatisticsDataTypeDef = TypedDict(
    "_OptionalLongColumnStatisticsDataTypeDef",
    {"MinimumValue": int, "MaximumValue": int},
    total=False,
)


class LongColumnStatisticsDataTypeDef(
    _RequiredLongColumnStatisticsDataTypeDef, _OptionalLongColumnStatisticsDataTypeDef
):
    pass


MLTransformTypeDef = TypedDict(
    "MLTransformTypeDef",
    {
        "TransformId": str,
        "Name": str,
        "Description": str,
        "Status": Literal["NOT_READY", "READY", "DELETING"],
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "InputRecordTables": List["GlueTableTypeDef"],
        "Parameters": "TransformParametersTypeDef",
        "EvaluationMetrics": "EvaluationMetricsTypeDef",
        "LabelCount": int,
        "Schema": List["SchemaColumnTypeDef"],
        "Role": str,
        "GlueVersion": str,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
        "TransformEncryption": "TransformEncryptionTypeDef",
    },
    total=False,
)

_RequiredMLUserDataEncryptionTypeDef = TypedDict(
    "_RequiredMLUserDataEncryptionTypeDef",
    {"MlUserDataEncryptionMode": Literal["DISABLED", "SSE-KMS"]},
)
_OptionalMLUserDataEncryptionTypeDef = TypedDict(
    "_OptionalMLUserDataEncryptionTypeDef", {"KmsKeyId": str}, total=False
)


class MLUserDataEncryptionTypeDef(
    _RequiredMLUserDataEncryptionTypeDef, _OptionalMLUserDataEncryptionTypeDef
):
    pass


MappingEntryTypeDef = TypedDict(
    "MappingEntryTypeDef",
    {
        "SourceTable": str,
        "SourcePath": str,
        "SourceType": str,
        "TargetTable": str,
        "TargetPath": str,
        "TargetType": str,
    },
    total=False,
)

MetadataInfoTypeDef = TypedDict(
    "MetadataInfoTypeDef", {"MetadataValue": str, "CreatedTime": str}, total=False
)

MongoDBTargetTypeDef = TypedDict(
    "MongoDBTargetTypeDef", {"ConnectionName": str, "Path": str, "ScanAll": bool}, total=False
)

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "Type": Literal["CRAWLER", "JOB", "TRIGGER"],
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": "TriggerNodeDetailsTypeDef",
        "JobDetails": "JobNodeDetailsTypeDef",
        "CrawlerDetails": "CrawlerNodeDetailsTypeDef",
    },
    total=False,
)

NotificationPropertyTypeDef = TypedDict(
    "NotificationPropertyTypeDef", {"NotifyDelayAfter": int}, total=False
)

OrderTypeDef = TypedDict("OrderTypeDef", {"Column": str, "SortOrder": int})

PartitionErrorTypeDef = TypedDict(
    "PartitionErrorTypeDef",
    {"PartitionValues": List[str], "ErrorDetail": "ErrorDetailTypeDef"},
    total=False,
)

_RequiredPartitionIndexDescriptorTypeDef = TypedDict(
    "_RequiredPartitionIndexDescriptorTypeDef",
    {
        "IndexName": str,
        "Keys": List["KeySchemaElementTypeDef"],
        "IndexStatus": Literal["CREATING", "ACTIVE", "DELETING", "FAILED"],
    },
)
_OptionalPartitionIndexDescriptorTypeDef = TypedDict(
    "_OptionalPartitionIndexDescriptorTypeDef",
    {"BackfillErrors": List["BackfillErrorTypeDef"]},
    total=False,
)


class PartitionIndexDescriptorTypeDef(
    _RequiredPartitionIndexDescriptorTypeDef, _OptionalPartitionIndexDescriptorTypeDef
):
    pass


PartitionInputTypeDef = TypedDict(
    "PartitionInputTypeDef",
    {
        "Values": List[str],
        "LastAccessTime": datetime,
        "StorageDescriptor": "StorageDescriptorTypeDef",
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
    },
    total=False,
)

PartitionTypeDef = TypedDict(
    "PartitionTypeDef",
    {
        "Values": List[str],
        "DatabaseName": str,
        "TableName": str,
        "CreationTime": datetime,
        "LastAccessTime": datetime,
        "StorageDescriptor": "StorageDescriptorTypeDef",
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": datetime,
        "CatalogId": str,
    },
    total=False,
)

PartitionValueListTypeDef = TypedDict("PartitionValueListTypeDef", {"Values": List[str]})

PhysicalConnectionRequirementsTypeDef = TypedDict(
    "PhysicalConnectionRequirementsTypeDef",
    {"SubnetId": str, "SecurityGroupIdList": List[str], "AvailabilityZone": str},
    total=False,
)

PredecessorTypeDef = TypedDict("PredecessorTypeDef", {"JobName": str, "RunId": str}, total=False)

PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {"Logical": Literal["AND", "ANY"], "Conditions": List["ConditionTypeDef"]},
    total=False,
)

PrincipalPermissionsTypeDef = TypedDict(
    "PrincipalPermissionsTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Permissions": List[
            Literal[
                "ALL",
                "SELECT",
                "ALTER",
                "DROP",
                "DELETE",
                "INSERT",
                "CREATE_DATABASE",
                "CREATE_TABLE",
                "DATA_LOCATION_ACCESS",
            ]
        ],
    },
    total=False,
)

RecrawlPolicyTypeDef = TypedDict(
    "RecrawlPolicyTypeDef",
    {"RecrawlBehavior": Literal["CRAWL_EVERYTHING", "CRAWL_NEW_FOLDERS_ONLY"]},
    total=False,
)

RegistryListItemTypeDef = TypedDict(
    "RegistryListItemTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "Description": str,
        "Status": Literal["AVAILABLE", "DELETING"],
        "CreatedTime": str,
        "UpdatedTime": str,
    },
    total=False,
)

ResourceUriTypeDef = TypedDict(
    "ResourceUriTypeDef",
    {"ResourceType": Literal["JAR", "FILE", "ARCHIVE"], "Uri": str},
    total=False,
)

S3EncryptionTypeDef = TypedDict(
    "S3EncryptionTypeDef",
    {"S3EncryptionMode": Literal["DISABLED", "SSE-KMS", "SSE-S3"], "KmsKeyArn": str},
    total=False,
)

S3TargetTypeDef = TypedDict(
    "S3TargetTypeDef", {"Path": str, "Exclusions": List[str], "ConnectionName": str}, total=False
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {"ScheduleExpression": str, "State": Literal["SCHEDULED", "NOT_SCHEDULED", "TRANSITIONING"]},
    total=False,
)

SchemaChangePolicyTypeDef = TypedDict(
    "SchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": Literal["LOG", "UPDATE_IN_DATABASE"],
        "DeleteBehavior": Literal["LOG", "DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE"],
    },
    total=False,
)

SchemaColumnTypeDef = TypedDict("SchemaColumnTypeDef", {"Name": str, "DataType": str}, total=False)

SchemaIdTypeDef = TypedDict(
    "SchemaIdTypeDef", {"SchemaArn": str, "SchemaName": str, "RegistryName": str}, total=False
)

SchemaListItemTypeDef = TypedDict(
    "SchemaListItemTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "SchemaArn": str,
        "Description": str,
        "SchemaStatus": Literal["AVAILABLE", "PENDING", "DELETING"],
        "CreatedTime": str,
        "UpdatedTime": str,
    },
    total=False,
)

SchemaReferenceTypeDef = TypedDict(
    "SchemaReferenceTypeDef",
    {"SchemaId": "SchemaIdTypeDef", "SchemaVersionId": str, "SchemaVersionNumber": int},
    total=False,
)

SchemaVersionErrorItemTypeDef = TypedDict(
    "SchemaVersionErrorItemTypeDef",
    {"VersionNumber": int, "ErrorDetails": "ErrorDetailsTypeDef"},
    total=False,
)

SchemaVersionListItemTypeDef = TypedDict(
    "SchemaVersionListItemTypeDef",
    {
        "SchemaArn": str,
        "SchemaVersionId": str,
        "VersionNumber": int,
        "Status": Literal["AVAILABLE", "PENDING", "FAILURE", "DELETING"],
        "CreatedTime": str,
    },
    total=False,
)

SecurityConfigurationTypeDef = TypedDict(
    "SecurityConfigurationTypeDef",
    {
        "Name": str,
        "CreatedTimeStamp": datetime,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
    total=False,
)

SerDeInfoTypeDef = TypedDict(
    "SerDeInfoTypeDef",
    {"Name": str, "SerializationLibrary": str, "Parameters": Dict[str, str]},
    total=False,
)

SkewedInfoTypeDef = TypedDict(
    "SkewedInfoTypeDef",
    {
        "SkewedColumnNames": List[str],
        "SkewedColumnValues": List[str],
        "SkewedColumnValueLocationMaps": Dict[str, str],
    },
    total=False,
)

StorageDescriptorTypeDef = TypedDict(
    "StorageDescriptorTypeDef",
    {
        "Columns": List["ColumnTypeDef"],
        "Location": str,
        "InputFormat": str,
        "OutputFormat": str,
        "Compressed": bool,
        "NumberOfBuckets": int,
        "SerdeInfo": "SerDeInfoTypeDef",
        "BucketColumns": List[str],
        "SortColumns": List["OrderTypeDef"],
        "Parameters": Dict[str, str],
        "SkewedInfo": "SkewedInfoTypeDef",
        "StoredAsSubDirectories": bool,
        "SchemaReference": "SchemaReferenceTypeDef",
    },
    total=False,
)

StringColumnStatisticsDataTypeDef = TypedDict(
    "StringColumnStatisticsDataTypeDef",
    {
        "MaximumLength": int,
        "AverageLength": float,
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
    },
)

TableErrorTypeDef = TypedDict(
    "TableErrorTypeDef", {"TableName": str, "ErrorDetail": "ErrorDetailTypeDef"}, total=False
)

TableIdentifierTypeDef = TypedDict(
    "TableIdentifierTypeDef", {"CatalogId": str, "DatabaseName": str, "Name": str}, total=False
)

_RequiredTableTypeDef = TypedDict("_RequiredTableTypeDef", {"Name": str})
_OptionalTableTypeDef = TypedDict(
    "_OptionalTableTypeDef",
    {
        "DatabaseName": str,
        "Description": str,
        "Owner": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": "StorageDescriptorTypeDef",
        "PartitionKeys": List["ColumnTypeDef"],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "CreatedBy": str,
        "IsRegisteredWithLakeFormation": bool,
        "TargetTable": "TableIdentifierTypeDef",
        "CatalogId": str,
    },
    total=False,
)


class TableTypeDef(_RequiredTableTypeDef, _OptionalTableTypeDef):
    pass


TableVersionErrorTypeDef = TypedDict(
    "TableVersionErrorTypeDef",
    {"TableName": str, "VersionId": str, "ErrorDetail": "ErrorDetailTypeDef"},
    total=False,
)

TableVersionTypeDef = TypedDict(
    "TableVersionTypeDef", {"Table": "TableTypeDef", "VersionId": str}, total=False
)

TaskRunPropertiesTypeDef = TypedDict(
    "TaskRunPropertiesTypeDef",
    {
        "TaskType": Literal[
            "EVALUATION",
            "LABELING_SET_GENERATION",
            "IMPORT_LABELS",
            "EXPORT_LABELS",
            "FIND_MATCHES",
        ],
        "ImportLabelsTaskRunProperties": "ImportLabelsTaskRunPropertiesTypeDef",
        "ExportLabelsTaskRunProperties": "ExportLabelsTaskRunPropertiesTypeDef",
        "LabelingSetGenerationTaskRunProperties": "LabelingSetGenerationTaskRunPropertiesTypeDef",
        "FindMatchesTaskRunProperties": "FindMatchesTaskRunPropertiesTypeDef",
    },
    total=False,
)

TaskRunTypeDef = TypedDict(
    "TaskRunTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "LogGroupName": str,
        "Properties": "TaskRunPropertiesTypeDef",
        "ErrorString": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "ExecutionTime": int,
    },
    total=False,
)

TransformEncryptionTypeDef = TypedDict(
    "TransformEncryptionTypeDef",
    {
        "MlUserDataEncryption": "MLUserDataEncryptionTypeDef",
        "TaskRunSecurityConfigurationName": str,
    },
    total=False,
)

_RequiredTransformParametersTypeDef = TypedDict(
    "_RequiredTransformParametersTypeDef", {"TransformType": Literal["FIND_MATCHES"]}
)
_OptionalTransformParametersTypeDef = TypedDict(
    "_OptionalTransformParametersTypeDef",
    {"FindMatchesParameters": "FindMatchesParametersTypeDef"},
    total=False,
)


class TransformParametersTypeDef(
    _RequiredTransformParametersTypeDef, _OptionalTransformParametersTypeDef
):
    pass


TriggerNodeDetailsTypeDef = TypedDict(
    "TriggerNodeDetailsTypeDef", {"Trigger": "TriggerTypeDef"}, total=False
)

TriggerTypeDef = TypedDict(
    "TriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": Literal["SCHEDULED", "CONDITIONAL", "ON_DEMAND"],
        "State": Literal[
            "CREATING",
            "CREATED",
            "ACTIVATING",
            "ACTIVATED",
            "DEACTIVATING",
            "DEACTIVATED",
            "DELETING",
            "UPDATING",
        ],
        "Description": str,
        "Schedule": str,
        "Actions": List["ActionTypeDef"],
        "Predicate": "PredicateTypeDef",
    },
    total=False,
)

UserDefinedFunctionTypeDef = TypedDict(
    "UserDefinedFunctionTypeDef",
    {
        "FunctionName": str,
        "DatabaseName": str,
        "ClassName": str,
        "OwnerName": str,
        "OwnerType": Literal["USER", "ROLE", "GROUP"],
        "CreateTime": datetime,
        "ResourceUris": List["ResourceUriTypeDef"],
        "CatalogId": str,
    },
    total=False,
)

WorkflowGraphTypeDef = TypedDict(
    "WorkflowGraphTypeDef",
    {"Nodes": List["NodeTypeDef"], "Edges": List["EdgeTypeDef"]},
    total=False,
)

WorkflowRunStatisticsTypeDef = TypedDict(
    "WorkflowRunStatisticsTypeDef",
    {
        "TotalActions": int,
        "TimeoutActions": int,
        "FailedActions": int,
        "StoppedActions": int,
        "SucceededActions": int,
        "RunningActions": int,
    },
    total=False,
)

WorkflowRunTypeDef = TypedDict(
    "WorkflowRunTypeDef",
    {
        "Name": str,
        "WorkflowRunId": str,
        "PreviousRunId": str,
        "WorkflowRunProperties": Dict[str, str],
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "Status": Literal["RUNNING", "COMPLETED", "STOPPING", "STOPPED", "ERROR"],
        "ErrorMessage": str,
        "Statistics": "WorkflowRunStatisticsTypeDef",
        "Graph": "WorkflowGraphTypeDef",
    },
    total=False,
)

WorkflowTypeDef = TypedDict(
    "WorkflowTypeDef",
    {
        "Name": str,
        "Description": str,
        "DefaultRunProperties": Dict[str, str],
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "LastRun": "WorkflowRunTypeDef",
        "Graph": "WorkflowGraphTypeDef",
        "MaxConcurrentRuns": int,
    },
    total=False,
)

_RequiredXMLClassifierTypeDef = TypedDict(
    "_RequiredXMLClassifierTypeDef", {"Name": str, "Classification": str}
)
_OptionalXMLClassifierTypeDef = TypedDict(
    "_OptionalXMLClassifierTypeDef",
    {"CreationTime": datetime, "LastUpdated": datetime, "Version": int, "RowTag": str},
    total=False,
)


class XMLClassifierTypeDef(_RequiredXMLClassifierTypeDef, _OptionalXMLClassifierTypeDef):
    pass


BatchCreatePartitionResponseTypeDef = TypedDict(
    "BatchCreatePartitionResponseTypeDef", {"Errors": List["PartitionErrorTypeDef"]}, total=False
)

BatchDeleteConnectionResponseTypeDef = TypedDict(
    "BatchDeleteConnectionResponseTypeDef",
    {"Succeeded": List[str], "Errors": Dict[str, "ErrorDetailTypeDef"]},
    total=False,
)

BatchDeletePartitionResponseTypeDef = TypedDict(
    "BatchDeletePartitionResponseTypeDef", {"Errors": List["PartitionErrorTypeDef"]}, total=False
)

BatchDeleteTableResponseTypeDef = TypedDict(
    "BatchDeleteTableResponseTypeDef", {"Errors": List["TableErrorTypeDef"]}, total=False
)

BatchDeleteTableVersionResponseTypeDef = TypedDict(
    "BatchDeleteTableVersionResponseTypeDef",
    {"Errors": List["TableVersionErrorTypeDef"]},
    total=False,
)

BatchGetCrawlersResponseTypeDef = TypedDict(
    "BatchGetCrawlersResponseTypeDef",
    {"Crawlers": List["CrawlerTypeDef"], "CrawlersNotFound": List[str]},
    total=False,
)

BatchGetDevEndpointsResponseTypeDef = TypedDict(
    "BatchGetDevEndpointsResponseTypeDef",
    {"DevEndpoints": List["DevEndpointTypeDef"], "DevEndpointsNotFound": List[str]},
    total=False,
)

BatchGetJobsResponseTypeDef = TypedDict(
    "BatchGetJobsResponseTypeDef",
    {"Jobs": List["JobTypeDef"], "JobsNotFound": List[str]},
    total=False,
)

BatchGetPartitionResponseTypeDef = TypedDict(
    "BatchGetPartitionResponseTypeDef",
    {"Partitions": List["PartitionTypeDef"], "UnprocessedKeys": List["PartitionValueListTypeDef"]},
    total=False,
)

BatchGetTriggersResponseTypeDef = TypedDict(
    "BatchGetTriggersResponseTypeDef",
    {"Triggers": List["TriggerTypeDef"], "TriggersNotFound": List[str]},
    total=False,
)

BatchGetWorkflowsResponseTypeDef = TypedDict(
    "BatchGetWorkflowsResponseTypeDef",
    {"Workflows": List["WorkflowTypeDef"], "MissingWorkflows": List[str]},
    total=False,
)

BatchStopJobRunResponseTypeDef = TypedDict(
    "BatchStopJobRunResponseTypeDef",
    {
        "SuccessfulSubmissions": List["BatchStopJobRunSuccessfulSubmissionTypeDef"],
        "Errors": List["BatchStopJobRunErrorTypeDef"],
    },
    total=False,
)

BatchUpdatePartitionRequestEntryTypeDef = TypedDict(
    "BatchUpdatePartitionRequestEntryTypeDef",
    {"PartitionValueList": List[str], "PartitionInput": "PartitionInputTypeDef"},
)

BatchUpdatePartitionResponseTypeDef = TypedDict(
    "BatchUpdatePartitionResponseTypeDef",
    {"Errors": List["BatchUpdatePartitionFailureEntryTypeDef"]},
    total=False,
)

CancelMLTaskRunResponseTypeDef = TypedDict(
    "CancelMLTaskRunResponseTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
    },
    total=False,
)

CatalogEntryTypeDef = TypedDict("CatalogEntryTypeDef", {"DatabaseName": str, "TableName": str})

CheckSchemaVersionValidityResponseTypeDef = TypedDict(
    "CheckSchemaVersionValidityResponseTypeDef", {"Valid": bool, "Error": str}, total=False
)

_RequiredConnectionInputTypeDef = TypedDict(
    "_RequiredConnectionInputTypeDef",
    {
        "Name": str,
        "ConnectionType": Literal[
            "JDBC", "SFTP", "MONGODB", "KAFKA", "NETWORK", "MARKETPLACE", "CUSTOM"
        ],
        "ConnectionProperties": Dict[
            Literal[
                "HOST",
                "PORT",
                "USERNAME",
                "PASSWORD",
                "ENCRYPTED_PASSWORD",
                "JDBC_DRIVER_JAR_URI",
                "JDBC_DRIVER_CLASS_NAME",
                "JDBC_ENGINE",
                "JDBC_ENGINE_VERSION",
                "CONFIG_FILES",
                "INSTANCE_ID",
                "JDBC_CONNECTION_URL",
                "JDBC_ENFORCE_SSL",
                "CUSTOM_JDBC_CERT",
                "SKIP_CUSTOM_JDBC_CERT_VALIDATION",
                "CUSTOM_JDBC_CERT_STRING",
                "CONNECTION_URL",
                "KAFKA_BOOTSTRAP_SERVERS",
                "KAFKA_SSL_ENABLED",
                "KAFKA_CUSTOM_CERT",
                "KAFKA_SKIP_CUSTOM_CERT_VALIDATION",
                "SECRET_ID",
                "CONNECTOR_URL",
                "CONNECTOR_TYPE",
                "CONNECTOR_CLASS_NAME",
            ],
            str,
        ],
    },
)
_OptionalConnectionInputTypeDef = TypedDict(
    "_OptionalConnectionInputTypeDef",
    {
        "Description": str,
        "MatchCriteria": List[str],
        "PhysicalConnectionRequirements": "PhysicalConnectionRequirementsTypeDef",
    },
    total=False,
)


class ConnectionInputTypeDef(_RequiredConnectionInputTypeDef, _OptionalConnectionInputTypeDef):
    pass


_RequiredCreateCsvClassifierRequestTypeDef = TypedDict(
    "_RequiredCreateCsvClassifierRequestTypeDef", {"Name": str}
)
_OptionalCreateCsvClassifierRequestTypeDef = TypedDict(
    "_OptionalCreateCsvClassifierRequestTypeDef",
    {
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": Literal["UNKNOWN", "PRESENT", "ABSENT"],
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)


class CreateCsvClassifierRequestTypeDef(
    _RequiredCreateCsvClassifierRequestTypeDef, _OptionalCreateCsvClassifierRequestTypeDef
):
    pass


CreateDevEndpointResponseTypeDef = TypedDict(
    "CreateDevEndpointResponseTypeDef",
    {
        "EndpointName": str,
        "Status": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "RoleArn": str,
        "YarnEndpointAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "NumberOfNodes": int,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "SecurityConfiguration": str,
        "CreatedTimestamp": datetime,
        "Arguments": Dict[str, str],
    },
    total=False,
)

_RequiredCreateGrokClassifierRequestTypeDef = TypedDict(
    "_RequiredCreateGrokClassifierRequestTypeDef",
    {"Classification": str, "Name": str, "GrokPattern": str},
)
_OptionalCreateGrokClassifierRequestTypeDef = TypedDict(
    "_OptionalCreateGrokClassifierRequestTypeDef", {"CustomPatterns": str}, total=False
)


class CreateGrokClassifierRequestTypeDef(
    _RequiredCreateGrokClassifierRequestTypeDef, _OptionalCreateGrokClassifierRequestTypeDef
):
    pass


CreateJobResponseTypeDef = TypedDict("CreateJobResponseTypeDef", {"Name": str}, total=False)

CreateJsonClassifierRequestTypeDef = TypedDict(
    "CreateJsonClassifierRequestTypeDef", {"Name": str, "JsonPath": str}
)

CreateMLTransformResponseTypeDef = TypedDict(
    "CreateMLTransformResponseTypeDef", {"TransformId": str}, total=False
)

CreateRegistryResponseTypeDef = TypedDict(
    "CreateRegistryResponseTypeDef",
    {"RegistryArn": str, "RegistryName": str, "Description": str, "Tags": Dict[str, str]},
    total=False,
)

CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "SchemaName": str,
        "SchemaArn": str,
        "Description": str,
        "DataFormat": Literal["AVRO"],
        "Compatibility": Literal[
            "NONE",
            "DISABLED",
            "BACKWARD",
            "BACKWARD_ALL",
            "FORWARD",
            "FORWARD_ALL",
            "FULL",
            "FULL_ALL",
        ],
        "SchemaCheckpoint": int,
        "LatestSchemaVersion": int,
        "NextSchemaVersion": int,
        "SchemaStatus": Literal["AVAILABLE", "PENDING", "DELETING"],
        "Tags": Dict[str, str],
        "SchemaVersionId": str,
        "SchemaVersionStatus": Literal["AVAILABLE", "PENDING", "FAILURE", "DELETING"],
    },
    total=False,
)

CreateScriptResponseTypeDef = TypedDict(
    "CreateScriptResponseTypeDef", {"PythonScript": str, "ScalaCode": str}, total=False
)

CreateSecurityConfigurationResponseTypeDef = TypedDict(
    "CreateSecurityConfigurationResponseTypeDef",
    {"Name": str, "CreatedTimestamp": datetime},
    total=False,
)

CreateTriggerResponseTypeDef = TypedDict("CreateTriggerResponseTypeDef", {"Name": str}, total=False)

CreateWorkflowResponseTypeDef = TypedDict(
    "CreateWorkflowResponseTypeDef", {"Name": str}, total=False
)

_RequiredCreateXMLClassifierRequestTypeDef = TypedDict(
    "_RequiredCreateXMLClassifierRequestTypeDef", {"Classification": str, "Name": str}
)
_OptionalCreateXMLClassifierRequestTypeDef = TypedDict(
    "_OptionalCreateXMLClassifierRequestTypeDef", {"RowTag": str}, total=False
)


class CreateXMLClassifierRequestTypeDef(
    _RequiredCreateXMLClassifierRequestTypeDef, _OptionalCreateXMLClassifierRequestTypeDef
):
    pass


_RequiredDatabaseInputTypeDef = TypedDict("_RequiredDatabaseInputTypeDef", {"Name": str})
_OptionalDatabaseInputTypeDef = TypedDict(
    "_OptionalDatabaseInputTypeDef",
    {
        "Description": str,
        "LocationUri": str,
        "Parameters": Dict[str, str],
        "CreateTableDefaultPermissions": List["PrincipalPermissionsTypeDef"],
        "TargetDatabase": "DatabaseIdentifierTypeDef",
    },
    total=False,
)


class DatabaseInputTypeDef(_RequiredDatabaseInputTypeDef, _OptionalDatabaseInputTypeDef):
    pass


DeleteJobResponseTypeDef = TypedDict("DeleteJobResponseTypeDef", {"JobName": str}, total=False)

DeleteMLTransformResponseTypeDef = TypedDict(
    "DeleteMLTransformResponseTypeDef", {"TransformId": str}, total=False
)

DeleteRegistryResponseTypeDef = TypedDict(
    "DeleteRegistryResponseTypeDef",
    {"RegistryName": str, "RegistryArn": str, "Status": Literal["AVAILABLE", "DELETING"]},
    total=False,
)

DeleteSchemaResponseTypeDef = TypedDict(
    "DeleteSchemaResponseTypeDef",
    {"SchemaArn": str, "SchemaName": str, "Status": Literal["AVAILABLE", "PENDING", "DELETING"]},
    total=False,
)

DeleteSchemaVersionsResponseTypeDef = TypedDict(
    "DeleteSchemaVersionsResponseTypeDef",
    {"SchemaVersionErrors": List["SchemaVersionErrorItemTypeDef"]},
    total=False,
)

DeleteTriggerResponseTypeDef = TypedDict("DeleteTriggerResponseTypeDef", {"Name": str}, total=False)

DeleteWorkflowResponseTypeDef = TypedDict(
    "DeleteWorkflowResponseTypeDef", {"Name": str}, total=False
)

DevEndpointCustomLibrariesTypeDef = TypedDict(
    "DevEndpointCustomLibrariesTypeDef",
    {"ExtraPythonLibsS3Path": str, "ExtraJarsS3Path": str},
    total=False,
)

GetCatalogImportStatusResponseTypeDef = TypedDict(
    "GetCatalogImportStatusResponseTypeDef",
    {"ImportStatus": "CatalogImportStatusTypeDef"},
    total=False,
)

GetClassifierResponseTypeDef = TypedDict(
    "GetClassifierResponseTypeDef", {"Classifier": "ClassifierTypeDef"}, total=False
)

GetClassifiersResponseTypeDef = TypedDict(
    "GetClassifiersResponseTypeDef",
    {"Classifiers": List["ClassifierTypeDef"], "NextToken": str},
    total=False,
)

GetColumnStatisticsForPartitionResponseTypeDef = TypedDict(
    "GetColumnStatisticsForPartitionResponseTypeDef",
    {"ColumnStatisticsList": List["ColumnStatisticsTypeDef"], "Errors": List["ColumnErrorTypeDef"]},
    total=False,
)

GetColumnStatisticsForTableResponseTypeDef = TypedDict(
    "GetColumnStatisticsForTableResponseTypeDef",
    {"ColumnStatisticsList": List["ColumnStatisticsTypeDef"], "Errors": List["ColumnErrorTypeDef"]},
    total=False,
)

GetConnectionResponseTypeDef = TypedDict(
    "GetConnectionResponseTypeDef", {"Connection": "ConnectionTypeDef"}, total=False
)

GetConnectionsFilterTypeDef = TypedDict(
    "GetConnectionsFilterTypeDef",
    {
        "MatchCriteria": List[str],
        "ConnectionType": Literal[
            "JDBC", "SFTP", "MONGODB", "KAFKA", "NETWORK", "MARKETPLACE", "CUSTOM"
        ],
    },
    total=False,
)

GetConnectionsResponseTypeDef = TypedDict(
    "GetConnectionsResponseTypeDef",
    {"ConnectionList": List["ConnectionTypeDef"], "NextToken": str},
    total=False,
)

GetCrawlerMetricsResponseTypeDef = TypedDict(
    "GetCrawlerMetricsResponseTypeDef",
    {"CrawlerMetricsList": List["CrawlerMetricsTypeDef"], "NextToken": str},
    total=False,
)

GetCrawlerResponseTypeDef = TypedDict(
    "GetCrawlerResponseTypeDef", {"Crawler": "CrawlerTypeDef"}, total=False
)

GetCrawlersResponseTypeDef = TypedDict(
    "GetCrawlersResponseTypeDef",
    {"Crawlers": List["CrawlerTypeDef"], "NextToken": str},
    total=False,
)

GetDataCatalogEncryptionSettingsResponseTypeDef = TypedDict(
    "GetDataCatalogEncryptionSettingsResponseTypeDef",
    {"DataCatalogEncryptionSettings": "DataCatalogEncryptionSettingsTypeDef"},
    total=False,
)

GetDatabaseResponseTypeDef = TypedDict(
    "GetDatabaseResponseTypeDef", {"Database": "DatabaseTypeDef"}, total=False
)

_RequiredGetDatabasesResponseTypeDef = TypedDict(
    "_RequiredGetDatabasesResponseTypeDef", {"DatabaseList": List["DatabaseTypeDef"]}
)
_OptionalGetDatabasesResponseTypeDef = TypedDict(
    "_OptionalGetDatabasesResponseTypeDef", {"NextToken": str}, total=False
)


class GetDatabasesResponseTypeDef(
    _RequiredGetDatabasesResponseTypeDef, _OptionalGetDatabasesResponseTypeDef
):
    pass


GetDataflowGraphResponseTypeDef = TypedDict(
    "GetDataflowGraphResponseTypeDef",
    {"DagNodes": List["CodeGenNodeTypeDef"], "DagEdges": List["CodeGenEdgeTypeDef"]},
    total=False,
)

GetDevEndpointResponseTypeDef = TypedDict(
    "GetDevEndpointResponseTypeDef", {"DevEndpoint": "DevEndpointTypeDef"}, total=False
)

GetDevEndpointsResponseTypeDef = TypedDict(
    "GetDevEndpointsResponseTypeDef",
    {"DevEndpoints": List["DevEndpointTypeDef"], "NextToken": str},
    total=False,
)

GetJobBookmarkResponseTypeDef = TypedDict(
    "GetJobBookmarkResponseTypeDef", {"JobBookmarkEntry": "JobBookmarkEntryTypeDef"}, total=False
)

GetJobResponseTypeDef = TypedDict("GetJobResponseTypeDef", {"Job": "JobTypeDef"}, total=False)

GetJobRunResponseTypeDef = TypedDict(
    "GetJobRunResponseTypeDef", {"JobRun": "JobRunTypeDef"}, total=False
)

GetJobRunsResponseTypeDef = TypedDict(
    "GetJobRunsResponseTypeDef", {"JobRuns": List["JobRunTypeDef"], "NextToken": str}, total=False
)

GetJobsResponseTypeDef = TypedDict(
    "GetJobsResponseTypeDef", {"Jobs": List["JobTypeDef"], "NextToken": str}, total=False
)

GetMLTaskRunResponseTypeDef = TypedDict(
    "GetMLTaskRunResponseTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "LogGroupName": str,
        "Properties": "TaskRunPropertiesTypeDef",
        "ErrorString": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "ExecutionTime": int,
    },
    total=False,
)

GetMLTaskRunsResponseTypeDef = TypedDict(
    "GetMLTaskRunsResponseTypeDef",
    {"TaskRuns": List["TaskRunTypeDef"], "NextToken": str},
    total=False,
)

GetMLTransformResponseTypeDef = TypedDict(
    "GetMLTransformResponseTypeDef",
    {
        "TransformId": str,
        "Name": str,
        "Description": str,
        "Status": Literal["NOT_READY", "READY", "DELETING"],
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "InputRecordTables": List["GlueTableTypeDef"],
        "Parameters": "TransformParametersTypeDef",
        "EvaluationMetrics": "EvaluationMetricsTypeDef",
        "LabelCount": int,
        "Schema": List["SchemaColumnTypeDef"],
        "Role": str,
        "GlueVersion": str,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
        "TransformEncryption": "TransformEncryptionTypeDef",
    },
    total=False,
)

_RequiredGetMLTransformsResponseTypeDef = TypedDict(
    "_RequiredGetMLTransformsResponseTypeDef", {"Transforms": List["MLTransformTypeDef"]}
)
_OptionalGetMLTransformsResponseTypeDef = TypedDict(
    "_OptionalGetMLTransformsResponseTypeDef", {"NextToken": str}, total=False
)


class GetMLTransformsResponseTypeDef(
    _RequiredGetMLTransformsResponseTypeDef, _OptionalGetMLTransformsResponseTypeDef
):
    pass


GetMappingResponseTypeDef = TypedDict(
    "GetMappingResponseTypeDef", {"Mapping": List["MappingEntryTypeDef"]}
)

GetPartitionIndexesResponseTypeDef = TypedDict(
    "GetPartitionIndexesResponseTypeDef",
    {"PartitionIndexDescriptorList": List["PartitionIndexDescriptorTypeDef"], "NextToken": str},
    total=False,
)

GetPartitionResponseTypeDef = TypedDict(
    "GetPartitionResponseTypeDef", {"Partition": "PartitionTypeDef"}, total=False
)

GetPartitionsResponseTypeDef = TypedDict(
    "GetPartitionsResponseTypeDef",
    {"Partitions": List["PartitionTypeDef"], "NextToken": str},
    total=False,
)

GetPlanResponseTypeDef = TypedDict(
    "GetPlanResponseTypeDef", {"PythonScript": str, "ScalaCode": str}, total=False
)

GetRegistryResponseTypeDef = TypedDict(
    "GetRegistryResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "Description": str,
        "Status": Literal["AVAILABLE", "DELETING"],
        "CreatedTime": str,
        "UpdatedTime": str,
    },
    total=False,
)

GetResourcePoliciesResponseTypeDef = TypedDict(
    "GetResourcePoliciesResponseTypeDef",
    {"GetResourcePoliciesResponseList": List["GluePolicyTypeDef"], "NextToken": str},
    total=False,
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {"PolicyInJson": str, "PolicyHash": str, "CreateTime": datetime, "UpdateTime": datetime},
    total=False,
)

GetSchemaByDefinitionResponseTypeDef = TypedDict(
    "GetSchemaByDefinitionResponseTypeDef",
    {
        "SchemaVersionId": str,
        "SchemaArn": str,
        "DataFormat": Literal["AVRO"],
        "Status": Literal["AVAILABLE", "PENDING", "FAILURE", "DELETING"],
        "CreatedTime": str,
    },
    total=False,
)

GetSchemaResponseTypeDef = TypedDict(
    "GetSchemaResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "SchemaName": str,
        "SchemaArn": str,
        "Description": str,
        "DataFormat": Literal["AVRO"],
        "Compatibility": Literal[
            "NONE",
            "DISABLED",
            "BACKWARD",
            "BACKWARD_ALL",
            "FORWARD",
            "FORWARD_ALL",
            "FULL",
            "FULL_ALL",
        ],
        "SchemaCheckpoint": int,
        "LatestSchemaVersion": int,
        "NextSchemaVersion": int,
        "SchemaStatus": Literal["AVAILABLE", "PENDING", "DELETING"],
        "CreatedTime": str,
        "UpdatedTime": str,
    },
    total=False,
)

GetSchemaVersionResponseTypeDef = TypedDict(
    "GetSchemaVersionResponseTypeDef",
    {
        "SchemaVersionId": str,
        "SchemaDefinition": str,
        "DataFormat": Literal["AVRO"],
        "SchemaArn": str,
        "VersionNumber": int,
        "Status": Literal["AVAILABLE", "PENDING", "FAILURE", "DELETING"],
        "CreatedTime": str,
    },
    total=False,
)

GetSchemaVersionsDiffResponseTypeDef = TypedDict(
    "GetSchemaVersionsDiffResponseTypeDef", {"Diff": str}, total=False
)

GetSecurityConfigurationResponseTypeDef = TypedDict(
    "GetSecurityConfigurationResponseTypeDef",
    {"SecurityConfiguration": "SecurityConfigurationTypeDef"},
    total=False,
)

GetSecurityConfigurationsResponseTypeDef = TypedDict(
    "GetSecurityConfigurationsResponseTypeDef",
    {"SecurityConfigurations": List["SecurityConfigurationTypeDef"], "NextToken": str},
    total=False,
)

GetTableResponseTypeDef = TypedDict(
    "GetTableResponseTypeDef", {"Table": "TableTypeDef"}, total=False
)

GetTableVersionResponseTypeDef = TypedDict(
    "GetTableVersionResponseTypeDef", {"TableVersion": "TableVersionTypeDef"}, total=False
)

GetTableVersionsResponseTypeDef = TypedDict(
    "GetTableVersionsResponseTypeDef",
    {"TableVersions": List["TableVersionTypeDef"], "NextToken": str},
    total=False,
)

GetTablesResponseTypeDef = TypedDict(
    "GetTablesResponseTypeDef", {"TableList": List["TableTypeDef"], "NextToken": str}, total=False
)

GetTagsResponseTypeDef = TypedDict("GetTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False)

GetTriggerResponseTypeDef = TypedDict(
    "GetTriggerResponseTypeDef", {"Trigger": "TriggerTypeDef"}, total=False
)

GetTriggersResponseTypeDef = TypedDict(
    "GetTriggersResponseTypeDef",
    {"Triggers": List["TriggerTypeDef"], "NextToken": str},
    total=False,
)

GetUserDefinedFunctionResponseTypeDef = TypedDict(
    "GetUserDefinedFunctionResponseTypeDef",
    {"UserDefinedFunction": "UserDefinedFunctionTypeDef"},
    total=False,
)

GetUserDefinedFunctionsResponseTypeDef = TypedDict(
    "GetUserDefinedFunctionsResponseTypeDef",
    {"UserDefinedFunctions": List["UserDefinedFunctionTypeDef"], "NextToken": str},
    total=False,
)

GetWorkflowResponseTypeDef = TypedDict(
    "GetWorkflowResponseTypeDef", {"Workflow": "WorkflowTypeDef"}, total=False
)

GetWorkflowRunPropertiesResponseTypeDef = TypedDict(
    "GetWorkflowRunPropertiesResponseTypeDef", {"RunProperties": Dict[str, str]}, total=False
)

GetWorkflowRunResponseTypeDef = TypedDict(
    "GetWorkflowRunResponseTypeDef", {"Run": "WorkflowRunTypeDef"}, total=False
)

GetWorkflowRunsResponseTypeDef = TypedDict(
    "GetWorkflowRunsResponseTypeDef",
    {"Runs": List["WorkflowRunTypeDef"], "NextToken": str},
    total=False,
)

JobUpdateTypeDef = TypedDict(
    "JobUpdateTypeDef",
    {
        "Description": str,
        "LogUri": str,
        "Role": str,
        "ExecutionProperty": "ExecutionPropertyTypeDef",
        "Command": "JobCommandTypeDef",
        "DefaultArguments": Dict[str, str],
        "NonOverridableArguments": Dict[str, str],
        "Connections": "ConnectionsListTypeDef",
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": Literal["Standard", "G.1X", "G.2X"],
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": "NotificationPropertyTypeDef",
        "GlueVersion": str,
    },
    total=False,
)

ListCrawlersResponseTypeDef = TypedDict(
    "ListCrawlersResponseTypeDef", {"CrawlerNames": List[str], "NextToken": str}, total=False
)

ListDevEndpointsResponseTypeDef = TypedDict(
    "ListDevEndpointsResponseTypeDef",
    {"DevEndpointNames": List[str], "NextToken": str},
    total=False,
)

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef", {"JobNames": List[str], "NextToken": str}, total=False
)

_RequiredListMLTransformsResponseTypeDef = TypedDict(
    "_RequiredListMLTransformsResponseTypeDef", {"TransformIds": List[str]}
)
_OptionalListMLTransformsResponseTypeDef = TypedDict(
    "_OptionalListMLTransformsResponseTypeDef", {"NextToken": str}, total=False
)


class ListMLTransformsResponseTypeDef(
    _RequiredListMLTransformsResponseTypeDef, _OptionalListMLTransformsResponseTypeDef
):
    pass


ListRegistriesResponseTypeDef = TypedDict(
    "ListRegistriesResponseTypeDef",
    {"Registries": List["RegistryListItemTypeDef"], "NextToken": str},
    total=False,
)

ListSchemaVersionsResponseTypeDef = TypedDict(
    "ListSchemaVersionsResponseTypeDef",
    {"Schemas": List["SchemaVersionListItemTypeDef"], "NextToken": str},
    total=False,
)

ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {"Schemas": List["SchemaListItemTypeDef"], "NextToken": str},
    total=False,
)

ListTriggersResponseTypeDef = TypedDict(
    "ListTriggersResponseTypeDef", {"TriggerNames": List[str], "NextToken": str}, total=False
)

ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef", {"Workflows": List[str], "NextToken": str}, total=False
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "Jdbc": List["CodeGenNodeArgTypeDef"],
        "S3": List["CodeGenNodeArgTypeDef"],
        "DynamoDB": List["CodeGenNodeArgTypeDef"],
    },
    total=False,
)

MetadataKeyValuePairTypeDef = TypedDict(
    "MetadataKeyValuePairTypeDef", {"MetadataKey": str, "MetadataValue": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PartitionIndexTypeDef = TypedDict("PartitionIndexTypeDef", {"Keys": List[str], "IndexName": str})

PropertyPredicateTypeDef = TypedDict(
    "PropertyPredicateTypeDef",
    {
        "Key": str,
        "Value": str,
        "Comparator": Literal[
            "EQUALS", "GREATER_THAN", "LESS_THAN", "GREATER_THAN_EQUALS", "LESS_THAN_EQUALS"
        ],
    },
    total=False,
)

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef", {"PolicyHash": str}, total=False
)

PutSchemaVersionMetadataResponseTypeDef = TypedDict(
    "PutSchemaVersionMetadataResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "RegistryName": str,
        "LatestVersion": bool,
        "VersionNumber": int,
        "SchemaVersionId": str,
        "MetadataKey": str,
        "MetadataValue": str,
    },
    total=False,
)

QuerySchemaVersionMetadataResponseTypeDef = TypedDict(
    "QuerySchemaVersionMetadataResponseTypeDef",
    {"MetadataInfoMap": Dict[str, "MetadataInfoTypeDef"], "SchemaVersionId": str, "NextToken": str},
    total=False,
)

RegisterSchemaVersionResponseTypeDef = TypedDict(
    "RegisterSchemaVersionResponseTypeDef",
    {
        "SchemaVersionId": str,
        "VersionNumber": int,
        "Status": Literal["AVAILABLE", "PENDING", "FAILURE", "DELETING"],
    },
    total=False,
)

RegistryIdTypeDef = TypedDict(
    "RegistryIdTypeDef", {"RegistryName": str, "RegistryArn": str}, total=False
)

RemoveSchemaVersionMetadataResponseTypeDef = TypedDict(
    "RemoveSchemaVersionMetadataResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "RegistryName": str,
        "LatestVersion": bool,
        "VersionNumber": int,
        "SchemaVersionId": str,
        "MetadataKey": str,
        "MetadataValue": str,
    },
    total=False,
)

ResetJobBookmarkResponseTypeDef = TypedDict(
    "ResetJobBookmarkResponseTypeDef", {"JobBookmarkEntry": "JobBookmarkEntryTypeDef"}, total=False
)

ResumeWorkflowRunResponseTypeDef = TypedDict(
    "ResumeWorkflowRunResponseTypeDef", {"RunId": str, "NodeIds": List[str]}, total=False
)

SchemaVersionNumberTypeDef = TypedDict(
    "SchemaVersionNumberTypeDef", {"LatestVersion": bool, "VersionNumber": int}, total=False
)

SearchTablesResponseTypeDef = TypedDict(
    "SearchTablesResponseTypeDef",
    {"NextToken": str, "TableList": List["TableTypeDef"]},
    total=False,
)

SegmentTypeDef = TypedDict("SegmentTypeDef", {"SegmentNumber": int, "TotalSegments": int})

SortCriterionTypeDef = TypedDict(
    "SortCriterionTypeDef", {"FieldName": str, "Sort": Literal["ASC", "DESC"]}, total=False
)

StartExportLabelsTaskRunResponseTypeDef = TypedDict(
    "StartExportLabelsTaskRunResponseTypeDef", {"TaskRunId": str}, total=False
)

StartImportLabelsTaskRunResponseTypeDef = TypedDict(
    "StartImportLabelsTaskRunResponseTypeDef", {"TaskRunId": str}, total=False
)

StartJobRunResponseTypeDef = TypedDict("StartJobRunResponseTypeDef", {"JobRunId": str}, total=False)

StartMLEvaluationTaskRunResponseTypeDef = TypedDict(
    "StartMLEvaluationTaskRunResponseTypeDef", {"TaskRunId": str}, total=False
)

StartMLLabelingSetGenerationTaskRunResponseTypeDef = TypedDict(
    "StartMLLabelingSetGenerationTaskRunResponseTypeDef", {"TaskRunId": str}, total=False
)

StartTriggerResponseTypeDef = TypedDict("StartTriggerResponseTypeDef", {"Name": str}, total=False)

StartWorkflowRunResponseTypeDef = TypedDict(
    "StartWorkflowRunResponseTypeDef", {"RunId": str}, total=False
)

StopTriggerResponseTypeDef = TypedDict("StopTriggerResponseTypeDef", {"Name": str}, total=False)

_RequiredTableInputTypeDef = TypedDict("_RequiredTableInputTypeDef", {"Name": str})
_OptionalTableInputTypeDef = TypedDict(
    "_OptionalTableInputTypeDef",
    {
        "Description": str,
        "Owner": str,
        "LastAccessTime": datetime,
        "LastAnalyzedTime": datetime,
        "Retention": int,
        "StorageDescriptor": "StorageDescriptorTypeDef",
        "PartitionKeys": List["ColumnTypeDef"],
        "ViewOriginalText": str,
        "ViewExpandedText": str,
        "TableType": str,
        "Parameters": Dict[str, str],
        "TargetTable": "TableIdentifierTypeDef",
    },
    total=False,
)


class TableInputTypeDef(_RequiredTableInputTypeDef, _OptionalTableInputTypeDef):
    pass


TaskRunFilterCriteriaTypeDef = TypedDict(
    "TaskRunFilterCriteriaTypeDef",
    {
        "TaskRunType": Literal[
            "EVALUATION",
            "LABELING_SET_GENERATION",
            "IMPORT_LABELS",
            "EXPORT_LABELS",
            "FIND_MATCHES",
        ],
        "Status": Literal[
            "STARTING", "RUNNING", "STOPPING", "STOPPED", "SUCCEEDED", "FAILED", "TIMEOUT"
        ],
        "StartedBefore": datetime,
        "StartedAfter": datetime,
    },
    total=False,
)

TaskRunSortCriteriaTypeDef = TypedDict(
    "TaskRunSortCriteriaTypeDef",
    {
        "Column": Literal["TASK_RUN_TYPE", "STATUS", "STARTED"],
        "SortDirection": Literal["DESCENDING", "ASCENDING"],
    },
)

TransformFilterCriteriaTypeDef = TypedDict(
    "TransformFilterCriteriaTypeDef",
    {
        "Name": str,
        "TransformType": Literal["FIND_MATCHES"],
        "Status": Literal["NOT_READY", "READY", "DELETING"],
        "GlueVersion": str,
        "CreatedBefore": datetime,
        "CreatedAfter": datetime,
        "LastModifiedBefore": datetime,
        "LastModifiedAfter": datetime,
        "Schema": List["SchemaColumnTypeDef"],
    },
    total=False,
)

TransformSortCriteriaTypeDef = TypedDict(
    "TransformSortCriteriaTypeDef",
    {
        "Column": Literal["NAME", "TRANSFORM_TYPE", "STATUS", "CREATED", "LAST_MODIFIED"],
        "SortDirection": Literal["DESCENDING", "ASCENDING"],
    },
)

TriggerUpdateTypeDef = TypedDict(
    "TriggerUpdateTypeDef",
    {
        "Name": str,
        "Description": str,
        "Schedule": str,
        "Actions": List["ActionTypeDef"],
        "Predicate": "PredicateTypeDef",
    },
    total=False,
)

UpdateColumnStatisticsForPartitionResponseTypeDef = TypedDict(
    "UpdateColumnStatisticsForPartitionResponseTypeDef",
    {"Errors": List["ColumnStatisticsErrorTypeDef"]},
    total=False,
)

UpdateColumnStatisticsForTableResponseTypeDef = TypedDict(
    "UpdateColumnStatisticsForTableResponseTypeDef",
    {"Errors": List["ColumnStatisticsErrorTypeDef"]},
    total=False,
)

_RequiredUpdateCsvClassifierRequestTypeDef = TypedDict(
    "_RequiredUpdateCsvClassifierRequestTypeDef", {"Name": str}
)
_OptionalUpdateCsvClassifierRequestTypeDef = TypedDict(
    "_OptionalUpdateCsvClassifierRequestTypeDef",
    {
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": Literal["UNKNOWN", "PRESENT", "ABSENT"],
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
    },
    total=False,
)


class UpdateCsvClassifierRequestTypeDef(
    _RequiredUpdateCsvClassifierRequestTypeDef, _OptionalUpdateCsvClassifierRequestTypeDef
):
    pass


_RequiredUpdateGrokClassifierRequestTypeDef = TypedDict(
    "_RequiredUpdateGrokClassifierRequestTypeDef", {"Name": str}
)
_OptionalUpdateGrokClassifierRequestTypeDef = TypedDict(
    "_OptionalUpdateGrokClassifierRequestTypeDef",
    {"Classification": str, "GrokPattern": str, "CustomPatterns": str},
    total=False,
)


class UpdateGrokClassifierRequestTypeDef(
    _RequiredUpdateGrokClassifierRequestTypeDef, _OptionalUpdateGrokClassifierRequestTypeDef
):
    pass


UpdateJobResponseTypeDef = TypedDict("UpdateJobResponseTypeDef", {"JobName": str}, total=False)

_RequiredUpdateJsonClassifierRequestTypeDef = TypedDict(
    "_RequiredUpdateJsonClassifierRequestTypeDef", {"Name": str}
)
_OptionalUpdateJsonClassifierRequestTypeDef = TypedDict(
    "_OptionalUpdateJsonClassifierRequestTypeDef", {"JsonPath": str}, total=False
)


class UpdateJsonClassifierRequestTypeDef(
    _RequiredUpdateJsonClassifierRequestTypeDef, _OptionalUpdateJsonClassifierRequestTypeDef
):
    pass


UpdateMLTransformResponseTypeDef = TypedDict(
    "UpdateMLTransformResponseTypeDef", {"TransformId": str}, total=False
)

UpdateRegistryResponseTypeDef = TypedDict(
    "UpdateRegistryResponseTypeDef", {"RegistryName": str, "RegistryArn": str}, total=False
)

UpdateSchemaResponseTypeDef = TypedDict(
    "UpdateSchemaResponseTypeDef",
    {"SchemaArn": str, "SchemaName": str, "RegistryName": str},
    total=False,
)

UpdateTriggerResponseTypeDef = TypedDict(
    "UpdateTriggerResponseTypeDef", {"Trigger": "TriggerTypeDef"}, total=False
)

UpdateWorkflowResponseTypeDef = TypedDict(
    "UpdateWorkflowResponseTypeDef", {"Name": str}, total=False
)

_RequiredUpdateXMLClassifierRequestTypeDef = TypedDict(
    "_RequiredUpdateXMLClassifierRequestTypeDef", {"Name": str}
)
_OptionalUpdateXMLClassifierRequestTypeDef = TypedDict(
    "_OptionalUpdateXMLClassifierRequestTypeDef",
    {"Classification": str, "RowTag": str},
    total=False,
)


class UpdateXMLClassifierRequestTypeDef(
    _RequiredUpdateXMLClassifierRequestTypeDef, _OptionalUpdateXMLClassifierRequestTypeDef
):
    pass


UserDefinedFunctionInputTypeDef = TypedDict(
    "UserDefinedFunctionInputTypeDef",
    {
        "FunctionName": str,
        "ClassName": str,
        "OwnerName": str,
        "OwnerType": Literal["USER", "ROLE", "GROUP"],
        "ResourceUris": List["ResourceUriTypeDef"],
    },
    total=False,
)
