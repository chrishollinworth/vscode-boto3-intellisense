"""
Type annotations for glue service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/type_defs.html)

Usage::

    ```python
    from mypy_boto3_glue.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AggFunctionType,
    BackfillErrorCodeType,
    BlueprintRunStateType,
    BlueprintStatusType,
    CatalogEncryptionModeType,
    CloudWatchEncryptionModeType,
    ColumnStatisticsTypeType,
    ComparatorType,
    CompatibilityType,
    CompressionTypeType,
    ConnectionPropertyKeyType,
    ConnectionTypeType,
    CrawlerHistoryStateType,
    CrawlerLineageSettingsType,
    CrawlerStateType,
    CrawlStateType,
    CsvHeaderOptionType,
    DataFormatType,
    DataQualityRuleResultStatusType,
    DeleteBehaviorType,
    DeltaTargetCompressionTypeType,
    DQStopJobOnFailureTimingType,
    DQTransformOutputType,
    EnableHybridValuesType,
    ExecutionClassType,
    ExistConditionType,
    FieldNameType,
    FilterLogicalOperatorType,
    FilterOperationType,
    FilterOperatorType,
    FilterValueTypeType,
    GlueRecordTypeType,
    HudiTargetCompressionTypeType,
    JDBCConnectionTypeType,
    JDBCDataTypeType,
    JdbcMetadataEntryType,
    JobBookmarksEncryptionModeType,
    JobRunStateType,
    JoinTypeType,
    LanguageType,
    LastCrawlStatusType,
    LogicalType,
    MLUserDataEncryptionModeStringType,
    NodeTypeType,
    ParamTypeType,
    ParquetCompressionTypeType,
    PartitionIndexStatusType,
    PermissionType,
    PermissionTypeType,
    PiiTypeType,
    PrincipalTypeType,
    QuoteCharType,
    RecrawlBehaviorType,
    RegistryStatusType,
    ResourceShareTypeType,
    ResourceTypeType,
    S3EncryptionModeType,
    ScheduleStateType,
    SchemaStatusType,
    SchemaVersionStatusType,
    SeparatorType,
    SessionStatusType,
    SortDirectionTypeType,
    SortType,
    SourceControlAuthStrategyType,
    SourceControlProviderType,
    StartingPositionType,
    StatementStateType,
    TargetFormatType,
    TaskRunSortColumnTypeType,
    TaskStatusTypeType,
    TaskTypeType,
    TransformSortColumnTypeType,
    TransformStatusTypeType,
    TriggerStateType,
    TriggerTypeType,
    UnionTypeType,
    UpdateBehaviorType,
    UpdateCatalogBehaviorType,
    WorkerTypeType,
    WorkflowRunStatusType,
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
    "ActionTypeDef",
    "AggregateOperationTypeDef",
    "AggregateTypeDef",
    "ApplyMappingTypeDef",
    "AthenaConnectorSourceTypeDef",
    "AuditContextTypeDef",
    "BackfillErrorTypeDef",
    "BasicCatalogTargetTypeDef",
    "BatchCreatePartitionRequestRequestTypeDef",
    "BatchCreatePartitionResponseTypeDef",
    "BatchDeleteConnectionRequestRequestTypeDef",
    "BatchDeleteConnectionResponseTypeDef",
    "BatchDeletePartitionRequestRequestTypeDef",
    "BatchDeletePartitionResponseTypeDef",
    "BatchDeleteTableRequestRequestTypeDef",
    "BatchDeleteTableResponseTypeDef",
    "BatchDeleteTableVersionRequestRequestTypeDef",
    "BatchDeleteTableVersionResponseTypeDef",
    "BatchGetBlueprintsRequestRequestTypeDef",
    "BatchGetBlueprintsResponseTypeDef",
    "BatchGetCrawlersRequestRequestTypeDef",
    "BatchGetCrawlersResponseTypeDef",
    "BatchGetCustomEntityTypesRequestRequestTypeDef",
    "BatchGetCustomEntityTypesResponseTypeDef",
    "BatchGetDataQualityResultRequestRequestTypeDef",
    "BatchGetDataQualityResultResponseTypeDef",
    "BatchGetDevEndpointsRequestRequestTypeDef",
    "BatchGetDevEndpointsResponseTypeDef",
    "BatchGetJobsRequestRequestTypeDef",
    "BatchGetJobsResponseTypeDef",
    "BatchGetPartitionRequestRequestTypeDef",
    "BatchGetPartitionResponseTypeDef",
    "BatchGetTriggersRequestRequestTypeDef",
    "BatchGetTriggersResponseTypeDef",
    "BatchGetWorkflowsRequestRequestTypeDef",
    "BatchGetWorkflowsResponseTypeDef",
    "BatchStopJobRunErrorTypeDef",
    "BatchStopJobRunRequestRequestTypeDef",
    "BatchStopJobRunResponseTypeDef",
    "BatchStopJobRunSuccessfulSubmissionTypeDef",
    "BatchUpdatePartitionFailureEntryTypeDef",
    "BatchUpdatePartitionRequestEntryTypeDef",
    "BatchUpdatePartitionRequestRequestTypeDef",
    "BatchUpdatePartitionResponseTypeDef",
    "BinaryColumnStatisticsDataTypeDef",
    "BlueprintDetailsTypeDef",
    "BlueprintRunTypeDef",
    "BlueprintTypeDef",
    "BooleanColumnStatisticsDataTypeDef",
    "CancelDataQualityRuleRecommendationRunRequestRequestTypeDef",
    "CancelDataQualityRulesetEvaluationRunRequestRequestTypeDef",
    "CancelMLTaskRunRequestRequestTypeDef",
    "CancelMLTaskRunResponseTypeDef",
    "CancelStatementRequestRequestTypeDef",
    "CatalogDeltaSourceTypeDef",
    "CatalogEntryTypeDef",
    "CatalogHudiSourceTypeDef",
    "CatalogImportStatusTypeDef",
    "CatalogKafkaSourceTypeDef",
    "CatalogKinesisSourceTypeDef",
    "CatalogSchemaChangePolicyTypeDef",
    "CatalogSourceTypeDef",
    "CatalogTargetTypeDef",
    "CheckSchemaVersionValidityInputRequestTypeDef",
    "CheckSchemaVersionValidityResponseTypeDef",
    "ClassifierTypeDef",
    "CloudWatchEncryptionTypeDef",
    "CodeGenConfigurationNodeTypeDef",
    "CodeGenEdgeTypeDef",
    "CodeGenNodeArgTypeDef",
    "CodeGenNodeTypeDef",
    "ColumnErrorTypeDef",
    "ColumnImportanceTypeDef",
    "ColumnRowFilterTypeDef",
    "ColumnStatisticsDataTypeDef",
    "ColumnStatisticsErrorTypeDef",
    "ColumnStatisticsTypeDef",
    "ColumnTypeDef",
    "ConditionTypeDef",
    "ConfusionMatrixTypeDef",
    "ConnectionInputTypeDef",
    "ConnectionPasswordEncryptionTypeDef",
    "ConnectionTypeDef",
    "ConnectionsListTypeDef",
    "CrawlTypeDef",
    "CrawlerHistoryTypeDef",
    "CrawlerMetricsTypeDef",
    "CrawlerNodeDetailsTypeDef",
    "CrawlerTargetsTypeDef",
    "CrawlerTypeDef",
    "CrawlsFilterTypeDef",
    "CreateBlueprintRequestRequestTypeDef",
    "CreateBlueprintResponseTypeDef",
    "CreateClassifierRequestRequestTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "CreateCrawlerRequestRequestTypeDef",
    "CreateCsvClassifierRequestTypeDef",
    "CreateCustomEntityTypeRequestRequestTypeDef",
    "CreateCustomEntityTypeResponseTypeDef",
    "CreateDataQualityRulesetRequestRequestTypeDef",
    "CreateDataQualityRulesetResponseTypeDef",
    "CreateDatabaseRequestRequestTypeDef",
    "CreateDevEndpointRequestRequestTypeDef",
    "CreateDevEndpointResponseTypeDef",
    "CreateGrokClassifierRequestTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreateJsonClassifierRequestTypeDef",
    "CreateMLTransformRequestRequestTypeDef",
    "CreateMLTransformResponseTypeDef",
    "CreatePartitionIndexRequestRequestTypeDef",
    "CreatePartitionRequestRequestTypeDef",
    "CreateRegistryInputRequestTypeDef",
    "CreateRegistryResponseTypeDef",
    "CreateSchemaInputRequestTypeDef",
    "CreateSchemaResponseTypeDef",
    "CreateScriptRequestRequestTypeDef",
    "CreateScriptResponseTypeDef",
    "CreateSecurityConfigurationRequestRequestTypeDef",
    "CreateSecurityConfigurationResponseTypeDef",
    "CreateSessionRequestRequestTypeDef",
    "CreateSessionResponseTypeDef",
    "CreateTableRequestRequestTypeDef",
    "CreateTriggerRequestRequestTypeDef",
    "CreateTriggerResponseTypeDef",
    "CreateUserDefinedFunctionRequestRequestTypeDef",
    "CreateWorkflowRequestRequestTypeDef",
    "CreateWorkflowResponseTypeDef",
    "CreateXMLClassifierRequestTypeDef",
    "CsvClassifierTypeDef",
    "CustomCodeTypeDef",
    "CustomEntityTypeTypeDef",
    "DQResultsPublishingOptionsTypeDef",
    "DQStopJobOnFailureOptionsTypeDef",
    "DataCatalogEncryptionSettingsTypeDef",
    "DataLakePrincipalTypeDef",
    "DataQualityEvaluationRunAdditionalRunOptionsTypeDef",
    "DataQualityResultDescriptionTypeDef",
    "DataQualityResultFilterCriteriaTypeDef",
    "DataQualityResultTypeDef",
    "DataQualityRuleRecommendationRunDescriptionTypeDef",
    "DataQualityRuleRecommendationRunFilterTypeDef",
    "DataQualityRuleResultTypeDef",
    "DataQualityRulesetEvaluationRunDescriptionTypeDef",
    "DataQualityRulesetEvaluationRunFilterTypeDef",
    "DataQualityRulesetFilterCriteriaTypeDef",
    "DataQualityRulesetListDetailsTypeDef",
    "DataQualityTargetTableTypeDef",
    "DataSourceTypeDef",
    "DatabaseIdentifierTypeDef",
    "DatabaseInputTypeDef",
    "DatabaseTypeDef",
    "DatatypeTypeDef",
    "DateColumnStatisticsDataTypeDef",
    "DecimalColumnStatisticsDataTypeDef",
    "DecimalNumberTypeDef",
    "DeleteBlueprintRequestRequestTypeDef",
    "DeleteBlueprintResponseTypeDef",
    "DeleteClassifierRequestRequestTypeDef",
    "DeleteColumnStatisticsForPartitionRequestRequestTypeDef",
    "DeleteColumnStatisticsForTableRequestRequestTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteCrawlerRequestRequestTypeDef",
    "DeleteCustomEntityTypeRequestRequestTypeDef",
    "DeleteCustomEntityTypeResponseTypeDef",
    "DeleteDataQualityRulesetRequestRequestTypeDef",
    "DeleteDatabaseRequestRequestTypeDef",
    "DeleteDevEndpointRequestRequestTypeDef",
    "DeleteJobRequestRequestTypeDef",
    "DeleteJobResponseTypeDef",
    "DeleteMLTransformRequestRequestTypeDef",
    "DeleteMLTransformResponseTypeDef",
    "DeletePartitionIndexRequestRequestTypeDef",
    "DeletePartitionRequestRequestTypeDef",
    "DeleteRegistryInputRequestTypeDef",
    "DeleteRegistryResponseTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteSchemaInputRequestTypeDef",
    "DeleteSchemaResponseTypeDef",
    "DeleteSchemaVersionsInputRequestTypeDef",
    "DeleteSchemaVersionsResponseTypeDef",
    "DeleteSecurityConfigurationRequestRequestTypeDef",
    "DeleteSessionRequestRequestTypeDef",
    "DeleteSessionResponseTypeDef",
    "DeleteTableRequestRequestTypeDef",
    "DeleteTableVersionRequestRequestTypeDef",
    "DeleteTriggerRequestRequestTypeDef",
    "DeleteTriggerResponseTypeDef",
    "DeleteUserDefinedFunctionRequestRequestTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "DeleteWorkflowResponseTypeDef",
    "DeltaTargetTypeDef",
    "DevEndpointCustomLibrariesTypeDef",
    "DevEndpointTypeDef",
    "DirectJDBCSourceTypeDef",
    "DirectKafkaSourceTypeDef",
    "DirectKinesisSourceTypeDef",
    "DirectSchemaChangePolicyTypeDef",
    "DoubleColumnStatisticsDataTypeDef",
    "DropDuplicatesTypeDef",
    "DropFieldsTypeDef",
    "DropNullFieldsTypeDef",
    "DynamicTransformTypeDef",
    "DynamoDBCatalogSourceTypeDef",
    "DynamoDBTargetTypeDef",
    "EdgeTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionConfigurationTypeDef",
    "ErrorDetailTypeDef",
    "ErrorDetailsTypeDef",
    "EvaluateDataQualityTypeDef",
    "EvaluationMetricsTypeDef",
    "EventBatchingConditionTypeDef",
    "ExecutionPropertyTypeDef",
    "ExportLabelsTaskRunPropertiesTypeDef",
    "FederatedDatabaseTypeDef",
    "FederatedTableTypeDef",
    "FillMissingValuesTypeDef",
    "FilterExpressionTypeDef",
    "FilterTypeDef",
    "FilterValueTypeDef",
    "FindMatchesMetricsTypeDef",
    "FindMatchesParametersTypeDef",
    "FindMatchesTaskRunPropertiesTypeDef",
    "GetBlueprintRequestRequestTypeDef",
    "GetBlueprintResponseTypeDef",
    "GetBlueprintRunRequestRequestTypeDef",
    "GetBlueprintRunResponseTypeDef",
    "GetBlueprintRunsRequestRequestTypeDef",
    "GetBlueprintRunsResponseTypeDef",
    "GetCatalogImportStatusRequestRequestTypeDef",
    "GetCatalogImportStatusResponseTypeDef",
    "GetClassifierRequestRequestTypeDef",
    "GetClassifierResponseTypeDef",
    "GetClassifiersRequestRequestTypeDef",
    "GetClassifiersResponseTypeDef",
    "GetColumnStatisticsForPartitionRequestRequestTypeDef",
    "GetColumnStatisticsForPartitionResponseTypeDef",
    "GetColumnStatisticsForTableRequestRequestTypeDef",
    "GetColumnStatisticsForTableResponseTypeDef",
    "GetConnectionRequestRequestTypeDef",
    "GetConnectionResponseTypeDef",
    "GetConnectionsFilterTypeDef",
    "GetConnectionsRequestRequestTypeDef",
    "GetConnectionsResponseTypeDef",
    "GetCrawlerMetricsRequestRequestTypeDef",
    "GetCrawlerMetricsResponseTypeDef",
    "GetCrawlerRequestRequestTypeDef",
    "GetCrawlerResponseTypeDef",
    "GetCrawlersRequestRequestTypeDef",
    "GetCrawlersResponseTypeDef",
    "GetCustomEntityTypeRequestRequestTypeDef",
    "GetCustomEntityTypeResponseTypeDef",
    "GetDataCatalogEncryptionSettingsRequestRequestTypeDef",
    "GetDataCatalogEncryptionSettingsResponseTypeDef",
    "GetDataQualityResultRequestRequestTypeDef",
    "GetDataQualityResultResponseTypeDef",
    "GetDataQualityRuleRecommendationRunRequestRequestTypeDef",
    "GetDataQualityRuleRecommendationRunResponseTypeDef",
    "GetDataQualityRulesetEvaluationRunRequestRequestTypeDef",
    "GetDataQualityRulesetEvaluationRunResponseTypeDef",
    "GetDataQualityRulesetRequestRequestTypeDef",
    "GetDataQualityRulesetResponseTypeDef",
    "GetDatabaseRequestRequestTypeDef",
    "GetDatabaseResponseTypeDef",
    "GetDatabasesRequestRequestTypeDef",
    "GetDatabasesResponseTypeDef",
    "GetDataflowGraphRequestRequestTypeDef",
    "GetDataflowGraphResponseTypeDef",
    "GetDevEndpointRequestRequestTypeDef",
    "GetDevEndpointResponseTypeDef",
    "GetDevEndpointsRequestRequestTypeDef",
    "GetDevEndpointsResponseTypeDef",
    "GetJobBookmarkRequestRequestTypeDef",
    "GetJobBookmarkResponseTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetJobResponseTypeDef",
    "GetJobRunRequestRequestTypeDef",
    "GetJobRunResponseTypeDef",
    "GetJobRunsRequestRequestTypeDef",
    "GetJobRunsResponseTypeDef",
    "GetJobsRequestRequestTypeDef",
    "GetJobsResponseTypeDef",
    "GetMLTaskRunRequestRequestTypeDef",
    "GetMLTaskRunResponseTypeDef",
    "GetMLTaskRunsRequestRequestTypeDef",
    "GetMLTaskRunsResponseTypeDef",
    "GetMLTransformRequestRequestTypeDef",
    "GetMLTransformResponseTypeDef",
    "GetMLTransformsRequestRequestTypeDef",
    "GetMLTransformsResponseTypeDef",
    "GetMappingRequestRequestTypeDef",
    "GetMappingResponseTypeDef",
    "GetPartitionIndexesRequestRequestTypeDef",
    "GetPartitionIndexesResponseTypeDef",
    "GetPartitionRequestRequestTypeDef",
    "GetPartitionResponseTypeDef",
    "GetPartitionsRequestRequestTypeDef",
    "GetPartitionsResponseTypeDef",
    "GetPlanRequestRequestTypeDef",
    "GetPlanResponseTypeDef",
    "GetRegistryInputRequestTypeDef",
    "GetRegistryResponseTypeDef",
    "GetResourcePoliciesRequestRequestTypeDef",
    "GetResourcePoliciesResponseTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetSchemaByDefinitionInputRequestTypeDef",
    "GetSchemaByDefinitionResponseTypeDef",
    "GetSchemaInputRequestTypeDef",
    "GetSchemaResponseTypeDef",
    "GetSchemaVersionInputRequestTypeDef",
    "GetSchemaVersionResponseTypeDef",
    "GetSchemaVersionsDiffInputRequestTypeDef",
    "GetSchemaVersionsDiffResponseTypeDef",
    "GetSecurityConfigurationRequestRequestTypeDef",
    "GetSecurityConfigurationResponseTypeDef",
    "GetSecurityConfigurationsRequestRequestTypeDef",
    "GetSecurityConfigurationsResponseTypeDef",
    "GetSessionRequestRequestTypeDef",
    "GetSessionResponseTypeDef",
    "GetStatementRequestRequestTypeDef",
    "GetStatementResponseTypeDef",
    "GetTableRequestRequestTypeDef",
    "GetTableResponseTypeDef",
    "GetTableVersionRequestRequestTypeDef",
    "GetTableVersionResponseTypeDef",
    "GetTableVersionsRequestRequestTypeDef",
    "GetTableVersionsResponseTypeDef",
    "GetTablesRequestRequestTypeDef",
    "GetTablesResponseTypeDef",
    "GetTagsRequestRequestTypeDef",
    "GetTagsResponseTypeDef",
    "GetTriggerRequestRequestTypeDef",
    "GetTriggerResponseTypeDef",
    "GetTriggersRequestRequestTypeDef",
    "GetTriggersResponseTypeDef",
    "GetUnfilteredPartitionMetadataRequestRequestTypeDef",
    "GetUnfilteredPartitionMetadataResponseTypeDef",
    "GetUnfilteredPartitionsMetadataRequestRequestTypeDef",
    "GetUnfilteredPartitionsMetadataResponseTypeDef",
    "GetUnfilteredTableMetadataRequestRequestTypeDef",
    "GetUnfilteredTableMetadataResponseTypeDef",
    "GetUserDefinedFunctionRequestRequestTypeDef",
    "GetUserDefinedFunctionResponseTypeDef",
    "GetUserDefinedFunctionsRequestRequestTypeDef",
    "GetUserDefinedFunctionsResponseTypeDef",
    "GetWorkflowRequestRequestTypeDef",
    "GetWorkflowResponseTypeDef",
    "GetWorkflowRunPropertiesRequestRequestTypeDef",
    "GetWorkflowRunPropertiesResponseTypeDef",
    "GetWorkflowRunRequestRequestTypeDef",
    "GetWorkflowRunResponseTypeDef",
    "GetWorkflowRunsRequestRequestTypeDef",
    "GetWorkflowRunsResponseTypeDef",
    "GluePolicyTypeDef",
    "GlueSchemaTypeDef",
    "GlueStudioSchemaColumnTypeDef",
    "GlueTableTypeDef",
    "GovernedCatalogSourceTypeDef",
    "GovernedCatalogTargetTypeDef",
    "GrokClassifierTypeDef",
    "ImportCatalogToGlueRequestRequestTypeDef",
    "ImportLabelsTaskRunPropertiesTypeDef",
    "JDBCConnectorOptionsTypeDef",
    "JDBCConnectorSourceTypeDef",
    "JDBCConnectorTargetTypeDef",
    "JdbcTargetTypeDef",
    "JobBookmarkEntryTypeDef",
    "JobBookmarksEncryptionTypeDef",
    "JobCommandTypeDef",
    "JobNodeDetailsTypeDef",
    "JobRunTypeDef",
    "JobTypeDef",
    "JobUpdateTypeDef",
    "JoinColumnTypeDef",
    "JoinTypeDef",
    "JsonClassifierTypeDef",
    "KafkaStreamingSourceOptionsTypeDef",
    "KeySchemaElementTypeDef",
    "KinesisStreamingSourceOptionsTypeDef",
    "LabelingSetGenerationTaskRunPropertiesTypeDef",
    "LakeFormationConfigurationTypeDef",
    "LastActiveDefinitionTypeDef",
    "LastCrawlInfoTypeDef",
    "LineageConfigurationTypeDef",
    "ListBlueprintsRequestRequestTypeDef",
    "ListBlueprintsResponseTypeDef",
    "ListCrawlersRequestRequestTypeDef",
    "ListCrawlersResponseTypeDef",
    "ListCrawlsRequestRequestTypeDef",
    "ListCrawlsResponseTypeDef",
    "ListCustomEntityTypesRequestRequestTypeDef",
    "ListCustomEntityTypesResponseTypeDef",
    "ListDataQualityResultsRequestRequestTypeDef",
    "ListDataQualityResultsResponseTypeDef",
    "ListDataQualityRuleRecommendationRunsRequestRequestTypeDef",
    "ListDataQualityRuleRecommendationRunsResponseTypeDef",
    "ListDataQualityRulesetEvaluationRunsRequestRequestTypeDef",
    "ListDataQualityRulesetEvaluationRunsResponseTypeDef",
    "ListDataQualityRulesetsRequestRequestTypeDef",
    "ListDataQualityRulesetsResponseTypeDef",
    "ListDevEndpointsRequestRequestTypeDef",
    "ListDevEndpointsResponseTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListMLTransformsRequestRequestTypeDef",
    "ListMLTransformsResponseTypeDef",
    "ListRegistriesInputRequestTypeDef",
    "ListRegistriesResponseTypeDef",
    "ListSchemaVersionsInputRequestTypeDef",
    "ListSchemaVersionsResponseTypeDef",
    "ListSchemasInputRequestTypeDef",
    "ListSchemasResponseTypeDef",
    "ListSessionsRequestRequestTypeDef",
    "ListSessionsResponseTypeDef",
    "ListStatementsRequestRequestTypeDef",
    "ListStatementsResponseTypeDef",
    "ListTriggersRequestRequestTypeDef",
    "ListTriggersResponseTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "LocationTypeDef",
    "LongColumnStatisticsDataTypeDef",
    "MLTransformTypeDef",
    "MLUserDataEncryptionTypeDef",
    "MappingEntryTypeDef",
    "MappingTypeDef",
    "MergeTypeDef",
    "MetadataInfoTypeDef",
    "MetadataKeyValuePairTypeDef",
    "MicrosoftSQLServerCatalogSourceTypeDef",
    "MicrosoftSQLServerCatalogTargetTypeDef",
    "MongoDBTargetTypeDef",
    "MySQLCatalogSourceTypeDef",
    "MySQLCatalogTargetTypeDef",
    "NodeTypeDef",
    "NotificationPropertyTypeDef",
    "NullCheckBoxListTypeDef",
    "NullValueFieldTypeDef",
    "OracleSQLCatalogSourceTypeDef",
    "OracleSQLCatalogTargetTypeDef",
    "OrderTypeDef",
    "OtherMetadataValueListItemTypeDef",
    "PIIDetectionTypeDef",
    "PaginatorConfigTypeDef",
    "PartitionErrorTypeDef",
    "PartitionIndexDescriptorTypeDef",
    "PartitionIndexTypeDef",
    "PartitionInputTypeDef",
    "PartitionTypeDef",
    "PartitionValueListTypeDef",
    "PhysicalConnectionRequirementsTypeDef",
    "PostgreSQLCatalogSourceTypeDef",
    "PostgreSQLCatalogTargetTypeDef",
    "PredecessorTypeDef",
    "PredicateTypeDef",
    "PrincipalPermissionsTypeDef",
    "PropertyPredicateTypeDef",
    "PutDataCatalogEncryptionSettingsRequestRequestTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "PutSchemaVersionMetadataInputRequestTypeDef",
    "PutSchemaVersionMetadataResponseTypeDef",
    "PutWorkflowRunPropertiesRequestRequestTypeDef",
    "QuerySchemaVersionMetadataInputRequestTypeDef",
    "QuerySchemaVersionMetadataResponseTypeDef",
    "RecrawlPolicyTypeDef",
    "RedshiftSourceTypeDef",
    "RedshiftTargetTypeDef",
    "RegisterSchemaVersionInputRequestTypeDef",
    "RegisterSchemaVersionResponseTypeDef",
    "RegistryIdTypeDef",
    "RegistryListItemTypeDef",
    "RelationalCatalogSourceTypeDef",
    "RemoveSchemaVersionMetadataInputRequestTypeDef",
    "RemoveSchemaVersionMetadataResponseTypeDef",
    "RenameFieldTypeDef",
    "ResetJobBookmarkRequestRequestTypeDef",
    "ResetJobBookmarkResponseTypeDef",
    "ResourceUriTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeWorkflowRunRequestRequestTypeDef",
    "ResumeWorkflowRunResponseTypeDef",
    "RunStatementRequestRequestTypeDef",
    "RunStatementResponseTypeDef",
    "S3CatalogDeltaSourceTypeDef",
    "S3CatalogHudiSourceTypeDef",
    "S3CatalogSourceTypeDef",
    "S3CatalogTargetTypeDef",
    "S3CsvSourceTypeDef",
    "S3DeltaCatalogTargetTypeDef",
    "S3DeltaDirectTargetTypeDef",
    "S3DeltaSourceTypeDef",
    "S3DirectSourceAdditionalOptionsTypeDef",
    "S3DirectTargetTypeDef",
    "S3EncryptionTypeDef",
    "S3GlueParquetTargetTypeDef",
    "S3HudiCatalogTargetTypeDef",
    "S3HudiDirectTargetTypeDef",
    "S3HudiSourceTypeDef",
    "S3JsonSourceTypeDef",
    "S3ParquetSourceTypeDef",
    "S3SourceAdditionalOptionsTypeDef",
    "S3TargetTypeDef",
    "ScheduleTypeDef",
    "SchemaChangePolicyTypeDef",
    "SchemaColumnTypeDef",
    "SchemaIdTypeDef",
    "SchemaListItemTypeDef",
    "SchemaReferenceTypeDef",
    "SchemaVersionErrorItemTypeDef",
    "SchemaVersionListItemTypeDef",
    "SchemaVersionNumberTypeDef",
    "SearchTablesRequestRequestTypeDef",
    "SearchTablesResponseTypeDef",
    "SecurityConfigurationTypeDef",
    "SegmentTypeDef",
    "SelectFieldsTypeDef",
    "SelectFromCollectionTypeDef",
    "SerDeInfoTypeDef",
    "SessionCommandTypeDef",
    "SessionTypeDef",
    "SkewedInfoTypeDef",
    "SortCriterionTypeDef",
    "SourceControlDetailsTypeDef",
    "SparkConnectorSourceTypeDef",
    "SparkConnectorTargetTypeDef",
    "SparkSQLTypeDef",
    "SpigotTypeDef",
    "SplitFieldsTypeDef",
    "SqlAliasTypeDef",
    "StartBlueprintRunRequestRequestTypeDef",
    "StartBlueprintRunResponseTypeDef",
    "StartCrawlerRequestRequestTypeDef",
    "StartCrawlerScheduleRequestRequestTypeDef",
    "StartDataQualityRuleRecommendationRunRequestRequestTypeDef",
    "StartDataQualityRuleRecommendationRunResponseTypeDef",
    "StartDataQualityRulesetEvaluationRunRequestRequestTypeDef",
    "StartDataQualityRulesetEvaluationRunResponseTypeDef",
    "StartExportLabelsTaskRunRequestRequestTypeDef",
    "StartExportLabelsTaskRunResponseTypeDef",
    "StartImportLabelsTaskRunRequestRequestTypeDef",
    "StartImportLabelsTaskRunResponseTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "StartJobRunResponseTypeDef",
    "StartMLEvaluationTaskRunRequestRequestTypeDef",
    "StartMLEvaluationTaskRunResponseTypeDef",
    "StartMLLabelingSetGenerationTaskRunRequestRequestTypeDef",
    "StartMLLabelingSetGenerationTaskRunResponseTypeDef",
    "StartTriggerRequestRequestTypeDef",
    "StartTriggerResponseTypeDef",
    "StartWorkflowRunRequestRequestTypeDef",
    "StartWorkflowRunResponseTypeDef",
    "StartingEventBatchConditionTypeDef",
    "StatementOutputDataTypeDef",
    "StatementOutputTypeDef",
    "StatementTypeDef",
    "StopCrawlerRequestRequestTypeDef",
    "StopCrawlerScheduleRequestRequestTypeDef",
    "StopSessionRequestRequestTypeDef",
    "StopSessionResponseTypeDef",
    "StopTriggerRequestRequestTypeDef",
    "StopTriggerResponseTypeDef",
    "StopWorkflowRunRequestRequestTypeDef",
    "StorageDescriptorTypeDef",
    "StreamingDataPreviewOptionsTypeDef",
    "StringColumnStatisticsDataTypeDef",
    "TableErrorTypeDef",
    "TableIdentifierTypeDef",
    "TableInputTypeDef",
    "TableTypeDef",
    "TableVersionErrorTypeDef",
    "TableVersionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaskRunFilterCriteriaTypeDef",
    "TaskRunPropertiesTypeDef",
    "TaskRunSortCriteriaTypeDef",
    "TaskRunTypeDef",
    "TransformConfigParameterTypeDef",
    "TransformEncryptionTypeDef",
    "TransformFilterCriteriaTypeDef",
    "TransformParametersTypeDef",
    "TransformSortCriteriaTypeDef",
    "TriggerNodeDetailsTypeDef",
    "TriggerTypeDef",
    "TriggerUpdateTypeDef",
    "UnfilteredPartitionTypeDef",
    "UnionTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBlueprintRequestRequestTypeDef",
    "UpdateBlueprintResponseTypeDef",
    "UpdateClassifierRequestRequestTypeDef",
    "UpdateColumnStatisticsForPartitionRequestRequestTypeDef",
    "UpdateColumnStatisticsForPartitionResponseTypeDef",
    "UpdateColumnStatisticsForTableRequestRequestTypeDef",
    "UpdateColumnStatisticsForTableResponseTypeDef",
    "UpdateConnectionRequestRequestTypeDef",
    "UpdateCrawlerRequestRequestTypeDef",
    "UpdateCrawlerScheduleRequestRequestTypeDef",
    "UpdateCsvClassifierRequestTypeDef",
    "UpdateDataQualityRulesetRequestRequestTypeDef",
    "UpdateDataQualityRulesetResponseTypeDef",
    "UpdateDatabaseRequestRequestTypeDef",
    "UpdateDevEndpointRequestRequestTypeDef",
    "UpdateGrokClassifierRequestTypeDef",
    "UpdateJobFromSourceControlRequestRequestTypeDef",
    "UpdateJobFromSourceControlResponseTypeDef",
    "UpdateJobRequestRequestTypeDef",
    "UpdateJobResponseTypeDef",
    "UpdateJsonClassifierRequestTypeDef",
    "UpdateMLTransformRequestRequestTypeDef",
    "UpdateMLTransformResponseTypeDef",
    "UpdatePartitionRequestRequestTypeDef",
    "UpdateRegistryInputRequestTypeDef",
    "UpdateRegistryResponseTypeDef",
    "UpdateSchemaInputRequestTypeDef",
    "UpdateSchemaResponseTypeDef",
    "UpdateSourceControlFromJobRequestRequestTypeDef",
    "UpdateSourceControlFromJobResponseTypeDef",
    "UpdateTableRequestRequestTypeDef",
    "UpdateTriggerRequestRequestTypeDef",
    "UpdateTriggerResponseTypeDef",
    "UpdateUserDefinedFunctionRequestRequestTypeDef",
    "UpdateWorkflowRequestRequestTypeDef",
    "UpdateWorkflowResponseTypeDef",
    "UpdateXMLClassifierRequestTypeDef",
    "UpsertRedshiftTargetOptionsTypeDef",
    "UserDefinedFunctionInputTypeDef",
    "UserDefinedFunctionTypeDef",
    "WorkflowGraphTypeDef",
    "WorkflowRunStatisticsTypeDef",
    "WorkflowRunTypeDef",
    "WorkflowTypeDef",
    "XMLClassifierTypeDef",
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

AggregateOperationTypeDef = TypedDict(
    "AggregateOperationTypeDef",
    {
        "Column": List[str],
        "AggFunc": AggFunctionType,
    },
)

AggregateTypeDef = TypedDict(
    "AggregateTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Groups": List[List[str]],
        "Aggs": List["AggregateOperationTypeDef"],
    },
)

ApplyMappingTypeDef = TypedDict(
    "ApplyMappingTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Mapping": List["MappingTypeDef"],
    },
)

_RequiredAthenaConnectorSourceTypeDef = TypedDict(
    "_RequiredAthenaConnectorSourceTypeDef",
    {
        "Name": str,
        "ConnectionName": str,
        "ConnectorName": str,
        "ConnectionType": str,
        "SchemaName": str,
    },
)
_OptionalAthenaConnectorSourceTypeDef = TypedDict(
    "_OptionalAthenaConnectorSourceTypeDef",
    {
        "ConnectionTable": str,
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class AthenaConnectorSourceTypeDef(
    _RequiredAthenaConnectorSourceTypeDef, _OptionalAthenaConnectorSourceTypeDef
):
    pass

AuditContextTypeDef = TypedDict(
    "AuditContextTypeDef",
    {
        "AdditionalAuditContext": str,
        "RequestedColumns": List[str],
        "AllColumnsRequested": bool,
    },
    total=False,
)

BackfillErrorTypeDef = TypedDict(
    "BackfillErrorTypeDef",
    {
        "Code": BackfillErrorCodeType,
        "Partitions": List["PartitionValueListTypeDef"],
    },
    total=False,
)

BasicCatalogTargetTypeDef = TypedDict(
    "BasicCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Database": str,
        "Table": str,
    },
)

_RequiredBatchCreatePartitionRequestRequestTypeDef = TypedDict(
    "_RequiredBatchCreatePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionInputList": List["PartitionInputTypeDef"],
    },
)
_OptionalBatchCreatePartitionRequestRequestTypeDef = TypedDict(
    "_OptionalBatchCreatePartitionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class BatchCreatePartitionRequestRequestTypeDef(
    _RequiredBatchCreatePartitionRequestRequestTypeDef,
    _OptionalBatchCreatePartitionRequestRequestTypeDef,
):
    pass

BatchCreatePartitionResponseTypeDef = TypedDict(
    "BatchCreatePartitionResponseTypeDef",
    {
        "Errors": List["PartitionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDeleteConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteConnectionRequestRequestTypeDef",
    {
        "ConnectionNameList": List[str],
    },
)
_OptionalBatchDeleteConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteConnectionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class BatchDeleteConnectionRequestRequestTypeDef(
    _RequiredBatchDeleteConnectionRequestRequestTypeDef,
    _OptionalBatchDeleteConnectionRequestRequestTypeDef,
):
    pass

BatchDeleteConnectionResponseTypeDef = TypedDict(
    "BatchDeleteConnectionResponseTypeDef",
    {
        "Succeeded": List[str],
        "Errors": Dict[str, "ErrorDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDeletePartitionRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDeletePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionsToDelete": List["PartitionValueListTypeDef"],
    },
)
_OptionalBatchDeletePartitionRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDeletePartitionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class BatchDeletePartitionRequestRequestTypeDef(
    _RequiredBatchDeletePartitionRequestRequestTypeDef,
    _OptionalBatchDeletePartitionRequestRequestTypeDef,
):
    pass

BatchDeletePartitionResponseTypeDef = TypedDict(
    "BatchDeletePartitionResponseTypeDef",
    {
        "Errors": List["PartitionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDeleteTableRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TablesToDelete": List[str],
    },
)
_OptionalBatchDeleteTableRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteTableRequestRequestTypeDef",
    {
        "CatalogId": str,
        "TransactionId": str,
    },
    total=False,
)

class BatchDeleteTableRequestRequestTypeDef(
    _RequiredBatchDeleteTableRequestRequestTypeDef, _OptionalBatchDeleteTableRequestRequestTypeDef
):
    pass

BatchDeleteTableResponseTypeDef = TypedDict(
    "BatchDeleteTableResponseTypeDef",
    {
        "Errors": List["TableErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDeleteTableVersionRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteTableVersionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "VersionIds": List[str],
    },
)
_OptionalBatchDeleteTableVersionRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteTableVersionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class BatchDeleteTableVersionRequestRequestTypeDef(
    _RequiredBatchDeleteTableVersionRequestRequestTypeDef,
    _OptionalBatchDeleteTableVersionRequestRequestTypeDef,
):
    pass

BatchDeleteTableVersionResponseTypeDef = TypedDict(
    "BatchDeleteTableVersionResponseTypeDef",
    {
        "Errors": List["TableVersionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetBlueprintsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchGetBlueprintsRequestRequestTypeDef",
    {
        "Names": List[str],
    },
)
_OptionalBatchGetBlueprintsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchGetBlueprintsRequestRequestTypeDef",
    {
        "IncludeBlueprint": bool,
        "IncludeParameterSpec": bool,
    },
    total=False,
)

class BatchGetBlueprintsRequestRequestTypeDef(
    _RequiredBatchGetBlueprintsRequestRequestTypeDef,
    _OptionalBatchGetBlueprintsRequestRequestTypeDef,
):
    pass

BatchGetBlueprintsResponseTypeDef = TypedDict(
    "BatchGetBlueprintsResponseTypeDef",
    {
        "Blueprints": List["BlueprintTypeDef"],
        "MissingBlueprints": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetCrawlersRequestRequestTypeDef = TypedDict(
    "BatchGetCrawlersRequestRequestTypeDef",
    {
        "CrawlerNames": List[str],
    },
)

BatchGetCrawlersResponseTypeDef = TypedDict(
    "BatchGetCrawlersResponseTypeDef",
    {
        "Crawlers": List["CrawlerTypeDef"],
        "CrawlersNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetCustomEntityTypesRequestRequestTypeDef = TypedDict(
    "BatchGetCustomEntityTypesRequestRequestTypeDef",
    {
        "Names": List[str],
    },
)

BatchGetCustomEntityTypesResponseTypeDef = TypedDict(
    "BatchGetCustomEntityTypesResponseTypeDef",
    {
        "CustomEntityTypes": List["CustomEntityTypeTypeDef"],
        "CustomEntityTypesNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDataQualityResultRequestRequestTypeDef = TypedDict(
    "BatchGetDataQualityResultRequestRequestTypeDef",
    {
        "ResultIds": List[str],
    },
)

BatchGetDataQualityResultResponseTypeDef = TypedDict(
    "BatchGetDataQualityResultResponseTypeDef",
    {
        "Results": List["DataQualityResultTypeDef"],
        "ResultsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDevEndpointsRequestRequestTypeDef = TypedDict(
    "BatchGetDevEndpointsRequestRequestTypeDef",
    {
        "DevEndpointNames": List[str],
    },
)

BatchGetDevEndpointsResponseTypeDef = TypedDict(
    "BatchGetDevEndpointsResponseTypeDef",
    {
        "DevEndpoints": List["DevEndpointTypeDef"],
        "DevEndpointsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetJobsRequestRequestTypeDef = TypedDict(
    "BatchGetJobsRequestRequestTypeDef",
    {
        "JobNames": List[str],
    },
)

BatchGetJobsResponseTypeDef = TypedDict(
    "BatchGetJobsResponseTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "JobsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetPartitionRequestRequestTypeDef = TypedDict(
    "_RequiredBatchGetPartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionsToGet": List["PartitionValueListTypeDef"],
    },
)
_OptionalBatchGetPartitionRequestRequestTypeDef = TypedDict(
    "_OptionalBatchGetPartitionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class BatchGetPartitionRequestRequestTypeDef(
    _RequiredBatchGetPartitionRequestRequestTypeDef, _OptionalBatchGetPartitionRequestRequestTypeDef
):
    pass

BatchGetPartitionResponseTypeDef = TypedDict(
    "BatchGetPartitionResponseTypeDef",
    {
        "Partitions": List["PartitionTypeDef"],
        "UnprocessedKeys": List["PartitionValueListTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetTriggersRequestRequestTypeDef = TypedDict(
    "BatchGetTriggersRequestRequestTypeDef",
    {
        "TriggerNames": List[str],
    },
)

BatchGetTriggersResponseTypeDef = TypedDict(
    "BatchGetTriggersResponseTypeDef",
    {
        "Triggers": List["TriggerTypeDef"],
        "TriggersNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchGetWorkflowsRequestRequestTypeDef = TypedDict(
    "_RequiredBatchGetWorkflowsRequestRequestTypeDef",
    {
        "Names": List[str],
    },
)
_OptionalBatchGetWorkflowsRequestRequestTypeDef = TypedDict(
    "_OptionalBatchGetWorkflowsRequestRequestTypeDef",
    {
        "IncludeGraph": bool,
    },
    total=False,
)

class BatchGetWorkflowsRequestRequestTypeDef(
    _RequiredBatchGetWorkflowsRequestRequestTypeDef, _OptionalBatchGetWorkflowsRequestRequestTypeDef
):
    pass

BatchGetWorkflowsResponseTypeDef = TypedDict(
    "BatchGetWorkflowsResponseTypeDef",
    {
        "Workflows": List["WorkflowTypeDef"],
        "MissingWorkflows": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchStopJobRunErrorTypeDef = TypedDict(
    "BatchStopJobRunErrorTypeDef",
    {
        "JobName": str,
        "JobRunId": str,
        "ErrorDetail": "ErrorDetailTypeDef",
    },
    total=False,
)

BatchStopJobRunRequestRequestTypeDef = TypedDict(
    "BatchStopJobRunRequestRequestTypeDef",
    {
        "JobName": str,
        "JobRunIds": List[str],
    },
)

BatchStopJobRunResponseTypeDef = TypedDict(
    "BatchStopJobRunResponseTypeDef",
    {
        "SuccessfulSubmissions": List["BatchStopJobRunSuccessfulSubmissionTypeDef"],
        "Errors": List["BatchStopJobRunErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchStopJobRunSuccessfulSubmissionTypeDef = TypedDict(
    "BatchStopJobRunSuccessfulSubmissionTypeDef",
    {
        "JobName": str,
        "JobRunId": str,
    },
    total=False,
)

BatchUpdatePartitionFailureEntryTypeDef = TypedDict(
    "BatchUpdatePartitionFailureEntryTypeDef",
    {
        "PartitionValueList": List[str],
        "ErrorDetail": "ErrorDetailTypeDef",
    },
    total=False,
)

BatchUpdatePartitionRequestEntryTypeDef = TypedDict(
    "BatchUpdatePartitionRequestEntryTypeDef",
    {
        "PartitionValueList": List[str],
        "PartitionInput": "PartitionInputTypeDef",
    },
)

_RequiredBatchUpdatePartitionRequestRequestTypeDef = TypedDict(
    "_RequiredBatchUpdatePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "Entries": List["BatchUpdatePartitionRequestEntryTypeDef"],
    },
)
_OptionalBatchUpdatePartitionRequestRequestTypeDef = TypedDict(
    "_OptionalBatchUpdatePartitionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class BatchUpdatePartitionRequestRequestTypeDef(
    _RequiredBatchUpdatePartitionRequestRequestTypeDef,
    _OptionalBatchUpdatePartitionRequestRequestTypeDef,
):
    pass

BatchUpdatePartitionResponseTypeDef = TypedDict(
    "BatchUpdatePartitionResponseTypeDef",
    {
        "Errors": List["BatchUpdatePartitionFailureEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BinaryColumnStatisticsDataTypeDef = TypedDict(
    "BinaryColumnStatisticsDataTypeDef",
    {
        "MaximumLength": int,
        "AverageLength": float,
        "NumberOfNulls": int,
    },
)

BlueprintDetailsTypeDef = TypedDict(
    "BlueprintDetailsTypeDef",
    {
        "BlueprintName": str,
        "RunId": str,
    },
    total=False,
)

BlueprintRunTypeDef = TypedDict(
    "BlueprintRunTypeDef",
    {
        "BlueprintName": str,
        "RunId": str,
        "WorkflowName": str,
        "State": BlueprintRunStateType,
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "RollbackErrorMessage": str,
        "Parameters": str,
        "RoleArn": str,
    },
    total=False,
)

BlueprintTypeDef = TypedDict(
    "BlueprintTypeDef",
    {
        "Name": str,
        "Description": str,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "ParameterSpec": str,
        "BlueprintLocation": str,
        "BlueprintServiceLocation": str,
        "Status": BlueprintStatusType,
        "ErrorMessage": str,
        "LastActiveDefinition": "LastActiveDefinitionTypeDef",
    },
    total=False,
)

BooleanColumnStatisticsDataTypeDef = TypedDict(
    "BooleanColumnStatisticsDataTypeDef",
    {
        "NumberOfTrues": int,
        "NumberOfFalses": int,
        "NumberOfNulls": int,
    },
)

CancelDataQualityRuleRecommendationRunRequestRequestTypeDef = TypedDict(
    "CancelDataQualityRuleRecommendationRunRequestRequestTypeDef",
    {
        "RunId": str,
    },
)

CancelDataQualityRulesetEvaluationRunRequestRequestTypeDef = TypedDict(
    "CancelDataQualityRulesetEvaluationRunRequestRequestTypeDef",
    {
        "RunId": str,
    },
)

CancelMLTaskRunRequestRequestTypeDef = TypedDict(
    "CancelMLTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
    },
)

CancelMLTaskRunResponseTypeDef = TypedDict(
    "CancelMLTaskRunResponseTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": TaskStatusTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCancelStatementRequestRequestTypeDef = TypedDict(
    "_RequiredCancelStatementRequestRequestTypeDef",
    {
        "SessionId": str,
        "Id": int,
    },
)
_OptionalCancelStatementRequestRequestTypeDef = TypedDict(
    "_OptionalCancelStatementRequestRequestTypeDef",
    {
        "RequestOrigin": str,
    },
    total=False,
)

class CancelStatementRequestRequestTypeDef(
    _RequiredCancelStatementRequestRequestTypeDef, _OptionalCancelStatementRequestRequestTypeDef
):
    pass

_RequiredCatalogDeltaSourceTypeDef = TypedDict(
    "_RequiredCatalogDeltaSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)
_OptionalCatalogDeltaSourceTypeDef = TypedDict(
    "_OptionalCatalogDeltaSourceTypeDef",
    {
        "AdditionalDeltaOptions": Dict[str, str],
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class CatalogDeltaSourceTypeDef(
    _RequiredCatalogDeltaSourceTypeDef, _OptionalCatalogDeltaSourceTypeDef
):
    pass

CatalogEntryTypeDef = TypedDict(
    "CatalogEntryTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)

_RequiredCatalogHudiSourceTypeDef = TypedDict(
    "_RequiredCatalogHudiSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)
_OptionalCatalogHudiSourceTypeDef = TypedDict(
    "_OptionalCatalogHudiSourceTypeDef",
    {
        "AdditionalHudiOptions": Dict[str, str],
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class CatalogHudiSourceTypeDef(
    _RequiredCatalogHudiSourceTypeDef, _OptionalCatalogHudiSourceTypeDef
):
    pass

CatalogImportStatusTypeDef = TypedDict(
    "CatalogImportStatusTypeDef",
    {
        "ImportCompleted": bool,
        "ImportTime": datetime,
        "ImportedBy": str,
    },
    total=False,
)

_RequiredCatalogKafkaSourceTypeDef = TypedDict(
    "_RequiredCatalogKafkaSourceTypeDef",
    {
        "Name": str,
        "Table": str,
        "Database": str,
    },
)
_OptionalCatalogKafkaSourceTypeDef = TypedDict(
    "_OptionalCatalogKafkaSourceTypeDef",
    {
        "WindowSize": int,
        "DetectSchema": bool,
        "StreamingOptions": "KafkaStreamingSourceOptionsTypeDef",
        "DataPreviewOptions": "StreamingDataPreviewOptionsTypeDef",
    },
    total=False,
)

class CatalogKafkaSourceTypeDef(
    _RequiredCatalogKafkaSourceTypeDef, _OptionalCatalogKafkaSourceTypeDef
):
    pass

_RequiredCatalogKinesisSourceTypeDef = TypedDict(
    "_RequiredCatalogKinesisSourceTypeDef",
    {
        "Name": str,
        "Table": str,
        "Database": str,
    },
)
_OptionalCatalogKinesisSourceTypeDef = TypedDict(
    "_OptionalCatalogKinesisSourceTypeDef",
    {
        "WindowSize": int,
        "DetectSchema": bool,
        "StreamingOptions": "KinesisStreamingSourceOptionsTypeDef",
        "DataPreviewOptions": "StreamingDataPreviewOptionsTypeDef",
    },
    total=False,
)

class CatalogKinesisSourceTypeDef(
    _RequiredCatalogKinesisSourceTypeDef, _OptionalCatalogKinesisSourceTypeDef
):
    pass

CatalogSchemaChangePolicyTypeDef = TypedDict(
    "CatalogSchemaChangePolicyTypeDef",
    {
        "EnableUpdateCatalog": bool,
        "UpdateBehavior": UpdateCatalogBehaviorType,
    },
    total=False,
)

CatalogSourceTypeDef = TypedDict(
    "CatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)

_RequiredCatalogTargetTypeDef = TypedDict(
    "_RequiredCatalogTargetTypeDef",
    {
        "DatabaseName": str,
        "Tables": List[str],
    },
)
_OptionalCatalogTargetTypeDef = TypedDict(
    "_OptionalCatalogTargetTypeDef",
    {
        "ConnectionName": str,
        "EventQueueArn": str,
        "DlqEventQueueArn": str,
    },
    total=False,
)

class CatalogTargetTypeDef(_RequiredCatalogTargetTypeDef, _OptionalCatalogTargetTypeDef):
    pass

CheckSchemaVersionValidityInputRequestTypeDef = TypedDict(
    "CheckSchemaVersionValidityInputRequestTypeDef",
    {
        "DataFormat": DataFormatType,
        "SchemaDefinition": str,
    },
)

CheckSchemaVersionValidityResponseTypeDef = TypedDict(
    "CheckSchemaVersionValidityResponseTypeDef",
    {
        "Valid": bool,
        "Error": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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
    {
        "CloudWatchEncryptionMode": CloudWatchEncryptionModeType,
        "KmsKeyArn": str,
    },
    total=False,
)

CodeGenConfigurationNodeTypeDef = TypedDict(
    "CodeGenConfigurationNodeTypeDef",
    {
        "AthenaConnectorSource": "AthenaConnectorSourceTypeDef",
        "JDBCConnectorSource": "JDBCConnectorSourceTypeDef",
        "SparkConnectorSource": "SparkConnectorSourceTypeDef",
        "CatalogSource": "CatalogSourceTypeDef",
        "RedshiftSource": "RedshiftSourceTypeDef",
        "S3CatalogSource": "S3CatalogSourceTypeDef",
        "S3CsvSource": "S3CsvSourceTypeDef",
        "S3JsonSource": "S3JsonSourceTypeDef",
        "S3ParquetSource": "S3ParquetSourceTypeDef",
        "RelationalCatalogSource": "RelationalCatalogSourceTypeDef",
        "DynamoDBCatalogSource": "DynamoDBCatalogSourceTypeDef",
        "JDBCConnectorTarget": "JDBCConnectorTargetTypeDef",
        "SparkConnectorTarget": "SparkConnectorTargetTypeDef",
        "CatalogTarget": "BasicCatalogTargetTypeDef",
        "RedshiftTarget": "RedshiftTargetTypeDef",
        "S3CatalogTarget": "S3CatalogTargetTypeDef",
        "S3GlueParquetTarget": "S3GlueParquetTargetTypeDef",
        "S3DirectTarget": "S3DirectTargetTypeDef",
        "ApplyMapping": "ApplyMappingTypeDef",
        "SelectFields": "SelectFieldsTypeDef",
        "DropFields": "DropFieldsTypeDef",
        "RenameField": "RenameFieldTypeDef",
        "Spigot": "SpigotTypeDef",
        "Join": "JoinTypeDef",
        "SplitFields": "SplitFieldsTypeDef",
        "SelectFromCollection": "SelectFromCollectionTypeDef",
        "FillMissingValues": "FillMissingValuesTypeDef",
        "Filter": "FilterTypeDef",
        "CustomCode": "CustomCodeTypeDef",
        "SparkSQL": "SparkSQLTypeDef",
        "DirectKinesisSource": "DirectKinesisSourceTypeDef",
        "DirectKafkaSource": "DirectKafkaSourceTypeDef",
        "CatalogKinesisSource": "CatalogKinesisSourceTypeDef",
        "CatalogKafkaSource": "CatalogKafkaSourceTypeDef",
        "DropNullFields": "DropNullFieldsTypeDef",
        "Merge": "MergeTypeDef",
        "Union": "UnionTypeDef",
        "PIIDetection": "PIIDetectionTypeDef",
        "Aggregate": "AggregateTypeDef",
        "DropDuplicates": "DropDuplicatesTypeDef",
        "GovernedCatalogTarget": "GovernedCatalogTargetTypeDef",
        "GovernedCatalogSource": "GovernedCatalogSourceTypeDef",
        "MicrosoftSQLServerCatalogSource": "MicrosoftSQLServerCatalogSourceTypeDef",
        "MySQLCatalogSource": "MySQLCatalogSourceTypeDef",
        "OracleSQLCatalogSource": "OracleSQLCatalogSourceTypeDef",
        "PostgreSQLCatalogSource": "PostgreSQLCatalogSourceTypeDef",
        "MicrosoftSQLServerCatalogTarget": "MicrosoftSQLServerCatalogTargetTypeDef",
        "MySQLCatalogTarget": "MySQLCatalogTargetTypeDef",
        "OracleSQLCatalogTarget": "OracleSQLCatalogTargetTypeDef",
        "PostgreSQLCatalogTarget": "PostgreSQLCatalogTargetTypeDef",
        "DynamicTransform": "DynamicTransformTypeDef",
        "EvaluateDataQuality": "EvaluateDataQualityTypeDef",
        "S3CatalogHudiSource": "S3CatalogHudiSourceTypeDef",
        "CatalogHudiSource": "CatalogHudiSourceTypeDef",
        "S3HudiSource": "S3HudiSourceTypeDef",
        "S3HudiCatalogTarget": "S3HudiCatalogTargetTypeDef",
        "S3HudiDirectTarget": "S3HudiDirectTargetTypeDef",
        "DirectJDBCSource": "DirectJDBCSourceTypeDef",
        "S3CatalogDeltaSource": "S3CatalogDeltaSourceTypeDef",
        "CatalogDeltaSource": "CatalogDeltaSourceTypeDef",
        "S3DeltaSource": "S3DeltaSourceTypeDef",
        "S3DeltaCatalogTarget": "S3DeltaCatalogTargetTypeDef",
        "S3DeltaDirectTarget": "S3DeltaDirectTargetTypeDef",
    },
    total=False,
)

_RequiredCodeGenEdgeTypeDef = TypedDict(
    "_RequiredCodeGenEdgeTypeDef",
    {
        "Source": str,
        "Target": str,
    },
)
_OptionalCodeGenEdgeTypeDef = TypedDict(
    "_OptionalCodeGenEdgeTypeDef",
    {
        "TargetParameter": str,
    },
    total=False,
)

class CodeGenEdgeTypeDef(_RequiredCodeGenEdgeTypeDef, _OptionalCodeGenEdgeTypeDef):
    pass

_RequiredCodeGenNodeArgTypeDef = TypedDict(
    "_RequiredCodeGenNodeArgTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
_OptionalCodeGenNodeArgTypeDef = TypedDict(
    "_OptionalCodeGenNodeArgTypeDef",
    {
        "Param": bool,
    },
    total=False,
)

class CodeGenNodeArgTypeDef(_RequiredCodeGenNodeArgTypeDef, _OptionalCodeGenNodeArgTypeDef):
    pass

_RequiredCodeGenNodeTypeDef = TypedDict(
    "_RequiredCodeGenNodeTypeDef",
    {
        "Id": str,
        "NodeType": str,
        "Args": List["CodeGenNodeArgTypeDef"],
    },
)
_OptionalCodeGenNodeTypeDef = TypedDict(
    "_OptionalCodeGenNodeTypeDef",
    {
        "LineNumber": int,
    },
    total=False,
)

class CodeGenNodeTypeDef(_RequiredCodeGenNodeTypeDef, _OptionalCodeGenNodeTypeDef):
    pass

ColumnErrorTypeDef = TypedDict(
    "ColumnErrorTypeDef",
    {
        "ColumnName": str,
        "Error": "ErrorDetailTypeDef",
    },
    total=False,
)

ColumnImportanceTypeDef = TypedDict(
    "ColumnImportanceTypeDef",
    {
        "ColumnName": str,
        "Importance": float,
    },
    total=False,
)

ColumnRowFilterTypeDef = TypedDict(
    "ColumnRowFilterTypeDef",
    {
        "ColumnName": str,
        "RowFilterExpression": str,
    },
    total=False,
)

_RequiredColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredColumnStatisticsDataTypeDef",
    {
        "Type": ColumnStatisticsTypeType,
    },
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
    {
        "ColumnStatistics": "ColumnStatisticsTypeDef",
        "Error": "ErrorDetailTypeDef",
    },
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

_RequiredColumnTypeDef = TypedDict(
    "_RequiredColumnTypeDef",
    {
        "Name": str,
    },
)
_OptionalColumnTypeDef = TypedDict(
    "_OptionalColumnTypeDef",
    {
        "Type": str,
        "Comment": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)

class ColumnTypeDef(_RequiredColumnTypeDef, _OptionalColumnTypeDef):
    pass

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "LogicalOperator": Literal["EQUALS"],
        "JobName": str,
        "State": JobRunStateType,
        "CrawlerName": str,
        "CrawlState": CrawlStateType,
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

_RequiredConnectionInputTypeDef = TypedDict(
    "_RequiredConnectionInputTypeDef",
    {
        "Name": str,
        "ConnectionType": ConnectionTypeType,
        "ConnectionProperties": Dict[ConnectionPropertyKeyType, str],
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

_RequiredConnectionPasswordEncryptionTypeDef = TypedDict(
    "_RequiredConnectionPasswordEncryptionTypeDef",
    {
        "ReturnConnectionPasswordEncrypted": bool,
    },
)
_OptionalConnectionPasswordEncryptionTypeDef = TypedDict(
    "_OptionalConnectionPasswordEncryptionTypeDef",
    {
        "AwsKmsKeyId": str,
    },
    total=False,
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
        "ConnectionType": ConnectionTypeType,
        "MatchCriteria": List[str],
        "ConnectionProperties": Dict[ConnectionPropertyKeyType, str],
        "PhysicalConnectionRequirements": "PhysicalConnectionRequirementsTypeDef",
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "LastUpdatedBy": str,
    },
    total=False,
)

ConnectionsListTypeDef = TypedDict(
    "ConnectionsListTypeDef",
    {
        "Connections": List[str],
    },
    total=False,
)

CrawlTypeDef = TypedDict(
    "CrawlTypeDef",
    {
        "State": CrawlStateType,
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
    },
    total=False,
)

CrawlerHistoryTypeDef = TypedDict(
    "CrawlerHistoryTypeDef",
    {
        "CrawlId": str,
        "State": CrawlerHistoryStateType,
        "StartTime": datetime,
        "EndTime": datetime,
        "Summary": str,
        "ErrorMessage": str,
        "LogGroup": str,
        "LogStream": str,
        "MessagePrefix": str,
        "DPUHour": float,
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
    "CrawlerNodeDetailsTypeDef",
    {
        "Crawls": List["CrawlTypeDef"],
    },
    total=False,
)

CrawlerTargetsTypeDef = TypedDict(
    "CrawlerTargetsTypeDef",
    {
        "S3Targets": List["S3TargetTypeDef"],
        "JdbcTargets": List["JdbcTargetTypeDef"],
        "MongoDBTargets": List["MongoDBTargetTypeDef"],
        "DynamoDBTargets": List["DynamoDBTargetTypeDef"],
        "CatalogTargets": List["CatalogTargetTypeDef"],
        "DeltaTargets": List["DeltaTargetTypeDef"],
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
        "State": CrawlerStateType,
        "TablePrefix": str,
        "Schedule": "ScheduleTypeDef",
        "CrawlElapsedTime": int,
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "LastCrawl": "LastCrawlInfoTypeDef",
        "Version": int,
        "Configuration": str,
        "CrawlerSecurityConfiguration": str,
        "LakeFormationConfiguration": "LakeFormationConfigurationTypeDef",
    },
    total=False,
)

CrawlsFilterTypeDef = TypedDict(
    "CrawlsFilterTypeDef",
    {
        "FieldName": FieldNameType,
        "FilterOperator": FilterOperatorType,
        "FieldValue": str,
    },
    total=False,
)

_RequiredCreateBlueprintRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBlueprintRequestRequestTypeDef",
    {
        "Name": str,
        "BlueprintLocation": str,
    },
)
_OptionalCreateBlueprintRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBlueprintRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateBlueprintRequestRequestTypeDef(
    _RequiredCreateBlueprintRequestRequestTypeDef, _OptionalCreateBlueprintRequestRequestTypeDef
):
    pass

CreateBlueprintResponseTypeDef = TypedDict(
    "CreateBlueprintResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClassifierRequestRequestTypeDef = TypedDict(
    "CreateClassifierRequestRequestTypeDef",
    {
        "GrokClassifier": "CreateGrokClassifierRequestTypeDef",
        "XMLClassifier": "CreateXMLClassifierRequestTypeDef",
        "JsonClassifier": "CreateJsonClassifierRequestTypeDef",
        "CsvClassifier": "CreateCsvClassifierRequestTypeDef",
    },
    total=False,
)

_RequiredCreateConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionRequestRequestTypeDef",
    {
        "ConnectionInput": "ConnectionInputTypeDef",
    },
)
_OptionalCreateConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionRequestRequestTypeDef",
    {
        "CatalogId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateConnectionRequestRequestTypeDef(
    _RequiredCreateConnectionRequestRequestTypeDef, _OptionalCreateConnectionRequestRequestTypeDef
):
    pass

_RequiredCreateCrawlerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCrawlerRequestRequestTypeDef",
    {
        "Name": str,
        "Role": str,
        "Targets": "CrawlerTargetsTypeDef",
    },
)
_OptionalCreateCrawlerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCrawlerRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "Description": str,
        "Schedule": str,
        "Classifiers": List[str],
        "TablePrefix": str,
        "SchemaChangePolicy": "SchemaChangePolicyTypeDef",
        "RecrawlPolicy": "RecrawlPolicyTypeDef",
        "LineageConfiguration": "LineageConfigurationTypeDef",
        "LakeFormationConfiguration": "LakeFormationConfigurationTypeDef",
        "Configuration": str,
        "CrawlerSecurityConfiguration": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateCrawlerRequestRequestTypeDef(
    _RequiredCreateCrawlerRequestRequestTypeDef, _OptionalCreateCrawlerRequestRequestTypeDef
):
    pass

_RequiredCreateCsvClassifierRequestTypeDef = TypedDict(
    "_RequiredCreateCsvClassifierRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateCsvClassifierRequestTypeDef = TypedDict(
    "_OptionalCreateCsvClassifierRequestTypeDef",
    {
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": CsvHeaderOptionType,
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
        "CustomDatatypeConfigured": bool,
        "CustomDatatypes": List[str],
    },
    total=False,
)

class CreateCsvClassifierRequestTypeDef(
    _RequiredCreateCsvClassifierRequestTypeDef, _OptionalCreateCsvClassifierRequestTypeDef
):
    pass

_RequiredCreateCustomEntityTypeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCustomEntityTypeRequestRequestTypeDef",
    {
        "Name": str,
        "RegexString": str,
    },
)
_OptionalCreateCustomEntityTypeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCustomEntityTypeRequestRequestTypeDef",
    {
        "ContextWords": List[str],
    },
    total=False,
)

class CreateCustomEntityTypeRequestRequestTypeDef(
    _RequiredCreateCustomEntityTypeRequestRequestTypeDef,
    _OptionalCreateCustomEntityTypeRequestRequestTypeDef,
):
    pass

CreateCustomEntityTypeResponseTypeDef = TypedDict(
    "CreateCustomEntityTypeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataQualityRulesetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataQualityRulesetRequestRequestTypeDef",
    {
        "Name": str,
        "Ruleset": str,
    },
)
_OptionalCreateDataQualityRulesetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataQualityRulesetRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
        "TargetTable": "DataQualityTargetTableTypeDef",
        "ClientToken": str,
    },
    total=False,
)

class CreateDataQualityRulesetRequestRequestTypeDef(
    _RequiredCreateDataQualityRulesetRequestRequestTypeDef,
    _OptionalCreateDataQualityRulesetRequestRequestTypeDef,
):
    pass

CreateDataQualityRulesetResponseTypeDef = TypedDict(
    "CreateDataQualityRulesetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatabaseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatabaseRequestRequestTypeDef",
    {
        "DatabaseInput": "DatabaseInputTypeDef",
    },
)
_OptionalCreateDatabaseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatabaseRequestRequestTypeDef",
    {
        "CatalogId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateDatabaseRequestRequestTypeDef(
    _RequiredCreateDatabaseRequestRequestTypeDef, _OptionalCreateDatabaseRequestRequestTypeDef
):
    pass

_RequiredCreateDevEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDevEndpointRequestRequestTypeDef",
    {
        "EndpointName": str,
        "RoleArn": str,
    },
)
_OptionalCreateDevEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDevEndpointRequestRequestTypeDef",
    {
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "PublicKey": str,
        "PublicKeys": List[str],
        "NumberOfNodes": int,
        "WorkerType": WorkerTypeType,
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "SecurityConfiguration": str,
        "Tags": Dict[str, str],
        "Arguments": Dict[str, str],
    },
    total=False,
)

class CreateDevEndpointRequestRequestTypeDef(
    _RequiredCreateDevEndpointRequestRequestTypeDef, _OptionalCreateDevEndpointRequestRequestTypeDef
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
        "WorkerType": WorkerTypeType,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGrokClassifierRequestTypeDef = TypedDict(
    "_RequiredCreateGrokClassifierRequestTypeDef",
    {
        "Classification": str,
        "Name": str,
        "GrokPattern": str,
    },
)
_OptionalCreateGrokClassifierRequestTypeDef = TypedDict(
    "_OptionalCreateGrokClassifierRequestTypeDef",
    {
        "CustomPatterns": str,
    },
    total=False,
)

class CreateGrokClassifierRequestTypeDef(
    _RequiredCreateGrokClassifierRequestTypeDef, _OptionalCreateGrokClassifierRequestTypeDef
):
    pass

_RequiredCreateJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateJobRequestRequestTypeDef",
    {
        "Name": str,
        "Role": str,
        "Command": "JobCommandTypeDef",
    },
)
_OptionalCreateJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateJobRequestRequestTypeDef",
    {
        "Description": str,
        "LogUri": str,
        "ExecutionProperty": "ExecutionPropertyTypeDef",
        "DefaultArguments": Dict[str, str],
        "NonOverridableArguments": Dict[str, str],
        "Connections": "ConnectionsListTypeDef",
        "MaxRetries": int,
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "SecurityConfiguration": str,
        "Tags": Dict[str, str],
        "NotificationProperty": "NotificationPropertyTypeDef",
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "WorkerType": WorkerTypeType,
        "CodeGenConfigurationNodes": Dict[str, "CodeGenConfigurationNodeTypeDef"],
        "ExecutionClass": ExecutionClassType,
        "SourceControlDetails": "SourceControlDetailsTypeDef",
    },
    total=False,
)

class CreateJobRequestRequestTypeDef(
    _RequiredCreateJobRequestRequestTypeDef, _OptionalCreateJobRequestRequestTypeDef
):
    pass

CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJsonClassifierRequestTypeDef = TypedDict(
    "CreateJsonClassifierRequestTypeDef",
    {
        "Name": str,
        "JsonPath": str,
    },
)

_RequiredCreateMLTransformRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMLTransformRequestRequestTypeDef",
    {
        "Name": str,
        "InputRecordTables": List["GlueTableTypeDef"],
        "Parameters": "TransformParametersTypeDef",
        "Role": str,
    },
)
_OptionalCreateMLTransformRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMLTransformRequestRequestTypeDef",
    {
        "Description": str,
        "GlueVersion": str,
        "MaxCapacity": float,
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
        "Tags": Dict[str, str],
        "TransformEncryption": "TransformEncryptionTypeDef",
    },
    total=False,
)

class CreateMLTransformRequestRequestTypeDef(
    _RequiredCreateMLTransformRequestRequestTypeDef, _OptionalCreateMLTransformRequestRequestTypeDef
):
    pass

CreateMLTransformResponseTypeDef = TypedDict(
    "CreateMLTransformResponseTypeDef",
    {
        "TransformId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePartitionIndexRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePartitionIndexRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionIndex": "PartitionIndexTypeDef",
    },
)
_OptionalCreatePartitionIndexRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePartitionIndexRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class CreatePartitionIndexRequestRequestTypeDef(
    _RequiredCreatePartitionIndexRequestRequestTypeDef,
    _OptionalCreatePartitionIndexRequestRequestTypeDef,
):
    pass

_RequiredCreatePartitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionInput": "PartitionInputTypeDef",
    },
)
_OptionalCreatePartitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePartitionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class CreatePartitionRequestRequestTypeDef(
    _RequiredCreatePartitionRequestRequestTypeDef, _OptionalCreatePartitionRequestRequestTypeDef
):
    pass

_RequiredCreateRegistryInputRequestTypeDef = TypedDict(
    "_RequiredCreateRegistryInputRequestTypeDef",
    {
        "RegistryName": str,
    },
)
_OptionalCreateRegistryInputRequestTypeDef = TypedDict(
    "_OptionalCreateRegistryInputRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateRegistryInputRequestTypeDef(
    _RequiredCreateRegistryInputRequestTypeDef, _OptionalCreateRegistryInputRequestTypeDef
):
    pass

CreateRegistryResponseTypeDef = TypedDict(
    "CreateRegistryResponseTypeDef",
    {
        "RegistryArn": str,
        "RegistryName": str,
        "Description": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSchemaInputRequestTypeDef = TypedDict(
    "_RequiredCreateSchemaInputRequestTypeDef",
    {
        "SchemaName": str,
        "DataFormat": DataFormatType,
    },
)
_OptionalCreateSchemaInputRequestTypeDef = TypedDict(
    "_OptionalCreateSchemaInputRequestTypeDef",
    {
        "RegistryId": "RegistryIdTypeDef",
        "Compatibility": CompatibilityType,
        "Description": str,
        "Tags": Dict[str, str],
        "SchemaDefinition": str,
    },
    total=False,
)

class CreateSchemaInputRequestTypeDef(
    _RequiredCreateSchemaInputRequestTypeDef, _OptionalCreateSchemaInputRequestTypeDef
):
    pass

CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "SchemaName": str,
        "SchemaArn": str,
        "Description": str,
        "DataFormat": DataFormatType,
        "Compatibility": CompatibilityType,
        "SchemaCheckpoint": int,
        "LatestSchemaVersion": int,
        "NextSchemaVersion": int,
        "SchemaStatus": SchemaStatusType,
        "Tags": Dict[str, str],
        "SchemaVersionId": str,
        "SchemaVersionStatus": SchemaVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateScriptRequestRequestTypeDef = TypedDict(
    "CreateScriptRequestRequestTypeDef",
    {
        "DagNodes": List["CodeGenNodeTypeDef"],
        "DagEdges": List["CodeGenEdgeTypeDef"],
        "Language": LanguageType,
    },
    total=False,
)

CreateScriptResponseTypeDef = TypedDict(
    "CreateScriptResponseTypeDef",
    {
        "PythonScript": str,
        "ScalaCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSecurityConfigurationRequestRequestTypeDef = TypedDict(
    "CreateSecurityConfigurationRequestRequestTypeDef",
    {
        "Name": str,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
)

CreateSecurityConfigurationResponseTypeDef = TypedDict(
    "CreateSecurityConfigurationResponseTypeDef",
    {
        "Name": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSessionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSessionRequestRequestTypeDef",
    {
        "Id": str,
        "Role": str,
        "Command": "SessionCommandTypeDef",
    },
)
_OptionalCreateSessionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSessionRequestRequestTypeDef",
    {
        "Description": str,
        "Timeout": int,
        "IdleTimeout": int,
        "DefaultArguments": Dict[str, str],
        "Connections": "ConnectionsListTypeDef",
        "MaxCapacity": float,
        "NumberOfWorkers": int,
        "WorkerType": WorkerTypeType,
        "SecurityConfiguration": str,
        "GlueVersion": str,
        "Tags": Dict[str, str],
        "RequestOrigin": str,
    },
    total=False,
)

class CreateSessionRequestRequestTypeDef(
    _RequiredCreateSessionRequestRequestTypeDef, _OptionalCreateSessionRequestRequestTypeDef
):
    pass

CreateSessionResponseTypeDef = TypedDict(
    "CreateSessionResponseTypeDef",
    {
        "Session": "SessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTableRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableInput": "TableInputTypeDef",
    },
)
_OptionalCreateTableRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTableRequestRequestTypeDef",
    {
        "CatalogId": str,
        "PartitionIndexes": List["PartitionIndexTypeDef"],
        "TransactionId": str,
    },
    total=False,
)

class CreateTableRequestRequestTypeDef(
    _RequiredCreateTableRequestRequestTypeDef, _OptionalCreateTableRequestRequestTypeDef
):
    pass

_RequiredCreateTriggerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTriggerRequestRequestTypeDef",
    {
        "Name": str,
        "Type": TriggerTypeType,
        "Actions": List["ActionTypeDef"],
    },
)
_OptionalCreateTriggerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTriggerRequestRequestTypeDef",
    {
        "WorkflowName": str,
        "Schedule": str,
        "Predicate": "PredicateTypeDef",
        "Description": str,
        "StartOnCreation": bool,
        "Tags": Dict[str, str],
        "EventBatchingCondition": "EventBatchingConditionTypeDef",
    },
    total=False,
)

class CreateTriggerRequestRequestTypeDef(
    _RequiredCreateTriggerRequestRequestTypeDef, _OptionalCreateTriggerRequestRequestTypeDef
):
    pass

CreateTriggerResponseTypeDef = TypedDict(
    "CreateTriggerResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserDefinedFunctionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionInput": "UserDefinedFunctionInputTypeDef",
    },
)
_OptionalCreateUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserDefinedFunctionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class CreateUserDefinedFunctionRequestRequestTypeDef(
    _RequiredCreateUserDefinedFunctionRequestRequestTypeDef,
    _OptionalCreateUserDefinedFunctionRequestRequestTypeDef,
):
    pass

_RequiredCreateWorkflowRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkflowRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateWorkflowRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkflowRequestRequestTypeDef",
    {
        "Description": str,
        "DefaultRunProperties": Dict[str, str],
        "Tags": Dict[str, str],
        "MaxConcurrentRuns": int,
    },
    total=False,
)

class CreateWorkflowRequestRequestTypeDef(
    _RequiredCreateWorkflowRequestRequestTypeDef, _OptionalCreateWorkflowRequestRequestTypeDef
):
    pass

CreateWorkflowResponseTypeDef = TypedDict(
    "CreateWorkflowResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateXMLClassifierRequestTypeDef = TypedDict(
    "_RequiredCreateXMLClassifierRequestTypeDef",
    {
        "Classification": str,
        "Name": str,
    },
)
_OptionalCreateXMLClassifierRequestTypeDef = TypedDict(
    "_OptionalCreateXMLClassifierRequestTypeDef",
    {
        "RowTag": str,
    },
    total=False,
)

class CreateXMLClassifierRequestTypeDef(
    _RequiredCreateXMLClassifierRequestTypeDef, _OptionalCreateXMLClassifierRequestTypeDef
):
    pass

_RequiredCsvClassifierTypeDef = TypedDict(
    "_RequiredCsvClassifierTypeDef",
    {
        "Name": str,
    },
)
_OptionalCsvClassifierTypeDef = TypedDict(
    "_OptionalCsvClassifierTypeDef",
    {
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": CsvHeaderOptionType,
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
        "CustomDatatypeConfigured": bool,
        "CustomDatatypes": List[str],
    },
    total=False,
)

class CsvClassifierTypeDef(_RequiredCsvClassifierTypeDef, _OptionalCsvClassifierTypeDef):
    pass

_RequiredCustomCodeTypeDef = TypedDict(
    "_RequiredCustomCodeTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Code": str,
        "ClassName": str,
    },
)
_OptionalCustomCodeTypeDef = TypedDict(
    "_OptionalCustomCodeTypeDef",
    {
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class CustomCodeTypeDef(_RequiredCustomCodeTypeDef, _OptionalCustomCodeTypeDef):
    pass

_RequiredCustomEntityTypeTypeDef = TypedDict(
    "_RequiredCustomEntityTypeTypeDef",
    {
        "Name": str,
        "RegexString": str,
    },
)
_OptionalCustomEntityTypeTypeDef = TypedDict(
    "_OptionalCustomEntityTypeTypeDef",
    {
        "ContextWords": List[str],
    },
    total=False,
)

class CustomEntityTypeTypeDef(_RequiredCustomEntityTypeTypeDef, _OptionalCustomEntityTypeTypeDef):
    pass

DQResultsPublishingOptionsTypeDef = TypedDict(
    "DQResultsPublishingOptionsTypeDef",
    {
        "EvaluationContext": str,
        "ResultsS3Prefix": str,
        "CloudWatchMetricsEnabled": bool,
        "ResultsPublishingEnabled": bool,
    },
    total=False,
)

DQStopJobOnFailureOptionsTypeDef = TypedDict(
    "DQStopJobOnFailureOptionsTypeDef",
    {
        "StopJobOnFailureTiming": DQStopJobOnFailureTimingType,
    },
    total=False,
)

DataCatalogEncryptionSettingsTypeDef = TypedDict(
    "DataCatalogEncryptionSettingsTypeDef",
    {
        "EncryptionAtRest": "EncryptionAtRestTypeDef",
        "ConnectionPasswordEncryption": "ConnectionPasswordEncryptionTypeDef",
    },
    total=False,
)

DataLakePrincipalTypeDef = TypedDict(
    "DataLakePrincipalTypeDef",
    {
        "DataLakePrincipalIdentifier": str,
    },
    total=False,
)

DataQualityEvaluationRunAdditionalRunOptionsTypeDef = TypedDict(
    "DataQualityEvaluationRunAdditionalRunOptionsTypeDef",
    {
        "CloudWatchMetricsEnabled": bool,
        "ResultsS3Prefix": str,
    },
    total=False,
)

DataQualityResultDescriptionTypeDef = TypedDict(
    "DataQualityResultDescriptionTypeDef",
    {
        "ResultId": str,
        "DataSource": "DataSourceTypeDef",
        "JobName": str,
        "JobRunId": str,
        "StartedOn": datetime,
    },
    total=False,
)

DataQualityResultFilterCriteriaTypeDef = TypedDict(
    "DataQualityResultFilterCriteriaTypeDef",
    {
        "DataSource": "DataSourceTypeDef",
        "JobName": str,
        "JobRunId": str,
        "StartedAfter": Union[datetime, str],
        "StartedBefore": Union[datetime, str],
    },
    total=False,
)

DataQualityResultTypeDef = TypedDict(
    "DataQualityResultTypeDef",
    {
        "ResultId": str,
        "Score": float,
        "DataSource": "DataSourceTypeDef",
        "RulesetName": str,
        "EvaluationContext": str,
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "JobName": str,
        "JobRunId": str,
        "RulesetEvaluationRunId": str,
        "RuleResults": List["DataQualityRuleResultTypeDef"],
    },
    total=False,
)

DataQualityRuleRecommendationRunDescriptionTypeDef = TypedDict(
    "DataQualityRuleRecommendationRunDescriptionTypeDef",
    {
        "RunId": str,
        "Status": TaskStatusTypeType,
        "StartedOn": datetime,
        "DataSource": "DataSourceTypeDef",
    },
    total=False,
)

_RequiredDataQualityRuleRecommendationRunFilterTypeDef = TypedDict(
    "_RequiredDataQualityRuleRecommendationRunFilterTypeDef",
    {
        "DataSource": "DataSourceTypeDef",
    },
)
_OptionalDataQualityRuleRecommendationRunFilterTypeDef = TypedDict(
    "_OptionalDataQualityRuleRecommendationRunFilterTypeDef",
    {
        "StartedBefore": Union[datetime, str],
        "StartedAfter": Union[datetime, str],
    },
    total=False,
)

class DataQualityRuleRecommendationRunFilterTypeDef(
    _RequiredDataQualityRuleRecommendationRunFilterTypeDef,
    _OptionalDataQualityRuleRecommendationRunFilterTypeDef,
):
    pass

DataQualityRuleResultTypeDef = TypedDict(
    "DataQualityRuleResultTypeDef",
    {
        "Name": str,
        "Description": str,
        "EvaluationMessage": str,
        "Result": DataQualityRuleResultStatusType,
    },
    total=False,
)

DataQualityRulesetEvaluationRunDescriptionTypeDef = TypedDict(
    "DataQualityRulesetEvaluationRunDescriptionTypeDef",
    {
        "RunId": str,
        "Status": TaskStatusTypeType,
        "StartedOn": datetime,
        "DataSource": "DataSourceTypeDef",
    },
    total=False,
)

_RequiredDataQualityRulesetEvaluationRunFilterTypeDef = TypedDict(
    "_RequiredDataQualityRulesetEvaluationRunFilterTypeDef",
    {
        "DataSource": "DataSourceTypeDef",
    },
)
_OptionalDataQualityRulesetEvaluationRunFilterTypeDef = TypedDict(
    "_OptionalDataQualityRulesetEvaluationRunFilterTypeDef",
    {
        "StartedBefore": Union[datetime, str],
        "StartedAfter": Union[datetime, str],
    },
    total=False,
)

class DataQualityRulesetEvaluationRunFilterTypeDef(
    _RequiredDataQualityRulesetEvaluationRunFilterTypeDef,
    _OptionalDataQualityRulesetEvaluationRunFilterTypeDef,
):
    pass

DataQualityRulesetFilterCriteriaTypeDef = TypedDict(
    "DataQualityRulesetFilterCriteriaTypeDef",
    {
        "Name": str,
        "Description": str,
        "CreatedBefore": Union[datetime, str],
        "CreatedAfter": Union[datetime, str],
        "LastModifiedBefore": Union[datetime, str],
        "LastModifiedAfter": Union[datetime, str],
        "TargetTable": "DataQualityTargetTableTypeDef",
    },
    total=False,
)

DataQualityRulesetListDetailsTypeDef = TypedDict(
    "DataQualityRulesetListDetailsTypeDef",
    {
        "Name": str,
        "Description": str,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "TargetTable": "DataQualityTargetTableTypeDef",
        "RecommendationRunId": str,
        "RuleCount": int,
    },
    total=False,
)

DataQualityTargetTableTypeDef = TypedDict(
    "DataQualityTargetTableTypeDef",
    {
        "TableName": str,
        "DatabaseName": str,
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "GlueTable": "GlueTableTypeDef",
    },
)

DatabaseIdentifierTypeDef = TypedDict(
    "DatabaseIdentifierTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
    },
    total=False,
)

_RequiredDatabaseInputTypeDef = TypedDict(
    "_RequiredDatabaseInputTypeDef",
    {
        "Name": str,
    },
)
_OptionalDatabaseInputTypeDef = TypedDict(
    "_OptionalDatabaseInputTypeDef",
    {
        "Description": str,
        "LocationUri": str,
        "Parameters": Dict[str, str],
        "CreateTableDefaultPermissions": List["PrincipalPermissionsTypeDef"],
        "TargetDatabase": "DatabaseIdentifierTypeDef",
        "FederatedDatabase": "FederatedDatabaseTypeDef",
    },
    total=False,
)

class DatabaseInputTypeDef(_RequiredDatabaseInputTypeDef, _OptionalDatabaseInputTypeDef):
    pass

_RequiredDatabaseTypeDef = TypedDict(
    "_RequiredDatabaseTypeDef",
    {
        "Name": str,
    },
)
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
        "FederatedDatabase": "FederatedDatabaseTypeDef",
    },
    total=False,
)

class DatabaseTypeDef(_RequiredDatabaseTypeDef, _OptionalDatabaseTypeDef):
    pass

DatatypeTypeDef = TypedDict(
    "DatatypeTypeDef",
    {
        "Id": str,
        "Label": str,
    },
)

_RequiredDateColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredDateColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
    },
)
_OptionalDateColumnStatisticsDataTypeDef = TypedDict(
    "_OptionalDateColumnStatisticsDataTypeDef",
    {
        "MinimumValue": datetime,
        "MaximumValue": datetime,
    },
    total=False,
)

class DateColumnStatisticsDataTypeDef(
    _RequiredDateColumnStatisticsDataTypeDef, _OptionalDateColumnStatisticsDataTypeDef
):
    pass

_RequiredDecimalColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredDecimalColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
    },
)
_OptionalDecimalColumnStatisticsDataTypeDef = TypedDict(
    "_OptionalDecimalColumnStatisticsDataTypeDef",
    {
        "MinimumValue": "DecimalNumberTypeDef",
        "MaximumValue": "DecimalNumberTypeDef",
    },
    total=False,
)

class DecimalColumnStatisticsDataTypeDef(
    _RequiredDecimalColumnStatisticsDataTypeDef, _OptionalDecimalColumnStatisticsDataTypeDef
):
    pass

DecimalNumberTypeDef = TypedDict(
    "DecimalNumberTypeDef",
    {
        "UnscaledValue": bytes,
        "Scale": int,
    },
)

DeleteBlueprintRequestRequestTypeDef = TypedDict(
    "DeleteBlueprintRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteBlueprintResponseTypeDef = TypedDict(
    "DeleteBlueprintResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClassifierRequestRequestTypeDef = TypedDict(
    "DeleteClassifierRequestRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredDeleteColumnStatisticsForPartitionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteColumnStatisticsForPartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": List[str],
        "ColumnName": str,
    },
)
_OptionalDeleteColumnStatisticsForPartitionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteColumnStatisticsForPartitionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class DeleteColumnStatisticsForPartitionRequestRequestTypeDef(
    _RequiredDeleteColumnStatisticsForPartitionRequestRequestTypeDef,
    _OptionalDeleteColumnStatisticsForPartitionRequestRequestTypeDef,
):
    pass

_RequiredDeleteColumnStatisticsForTableRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteColumnStatisticsForTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "ColumnName": str,
    },
)
_OptionalDeleteColumnStatisticsForTableRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteColumnStatisticsForTableRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class DeleteColumnStatisticsForTableRequestRequestTypeDef(
    _RequiredDeleteColumnStatisticsForTableRequestRequestTypeDef,
    _OptionalDeleteColumnStatisticsForTableRequestRequestTypeDef,
):
    pass

_RequiredDeleteConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteConnectionRequestRequestTypeDef",
    {
        "ConnectionName": str,
    },
)
_OptionalDeleteConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteConnectionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class DeleteConnectionRequestRequestTypeDef(
    _RequiredDeleteConnectionRequestRequestTypeDef, _OptionalDeleteConnectionRequestRequestTypeDef
):
    pass

DeleteCrawlerRequestRequestTypeDef = TypedDict(
    "DeleteCrawlerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteCustomEntityTypeRequestRequestTypeDef = TypedDict(
    "DeleteCustomEntityTypeRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteCustomEntityTypeResponseTypeDef = TypedDict(
    "DeleteCustomEntityTypeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataQualityRulesetRequestRequestTypeDef = TypedDict(
    "DeleteDataQualityRulesetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredDeleteDatabaseRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDatabaseRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDeleteDatabaseRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDatabaseRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class DeleteDatabaseRequestRequestTypeDef(
    _RequiredDeleteDatabaseRequestRequestTypeDef, _OptionalDeleteDatabaseRequestRequestTypeDef
):
    pass

DeleteDevEndpointRequestRequestTypeDef = TypedDict(
    "DeleteDevEndpointRequestRequestTypeDef",
    {
        "EndpointName": str,
    },
)

DeleteJobRequestRequestTypeDef = TypedDict(
    "DeleteJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
)

DeleteJobResponseTypeDef = TypedDict(
    "DeleteJobResponseTypeDef",
    {
        "JobName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMLTransformRequestRequestTypeDef = TypedDict(
    "DeleteMLTransformRequestRequestTypeDef",
    {
        "TransformId": str,
    },
)

DeleteMLTransformResponseTypeDef = TypedDict(
    "DeleteMLTransformResponseTypeDef",
    {
        "TransformId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeletePartitionIndexRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePartitionIndexRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "IndexName": str,
    },
)
_OptionalDeletePartitionIndexRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePartitionIndexRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class DeletePartitionIndexRequestRequestTypeDef(
    _RequiredDeletePartitionIndexRequestRequestTypeDef,
    _OptionalDeletePartitionIndexRequestRequestTypeDef,
):
    pass

_RequiredDeletePartitionRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": List[str],
    },
)
_OptionalDeletePartitionRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePartitionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class DeletePartitionRequestRequestTypeDef(
    _RequiredDeletePartitionRequestRequestTypeDef, _OptionalDeletePartitionRequestRequestTypeDef
):
    pass

DeleteRegistryInputRequestTypeDef = TypedDict(
    "DeleteRegistryInputRequestTypeDef",
    {
        "RegistryId": "RegistryIdTypeDef",
    },
)

DeleteRegistryResponseTypeDef = TypedDict(
    "DeleteRegistryResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "Status": RegistryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "PolicyHashCondition": str,
        "ResourceArn": str,
    },
    total=False,
)

DeleteSchemaInputRequestTypeDef = TypedDict(
    "DeleteSchemaInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
    },
)

DeleteSchemaResponseTypeDef = TypedDict(
    "DeleteSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "Status": SchemaStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSchemaVersionsInputRequestTypeDef = TypedDict(
    "DeleteSchemaVersionsInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "Versions": str,
    },
)

DeleteSchemaVersionsResponseTypeDef = TypedDict(
    "DeleteSchemaVersionsResponseTypeDef",
    {
        "SchemaVersionErrors": List["SchemaVersionErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSecurityConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteSecurityConfigurationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredDeleteSessionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteSessionRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalDeleteSessionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteSessionRequestRequestTypeDef",
    {
        "RequestOrigin": str,
    },
    total=False,
)

class DeleteSessionRequestRequestTypeDef(
    _RequiredDeleteSessionRequestRequestTypeDef, _OptionalDeleteSessionRequestRequestTypeDef
):
    pass

DeleteSessionResponseTypeDef = TypedDict(
    "DeleteSessionResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTableRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
    },
)
_OptionalDeleteTableRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTableRequestRequestTypeDef",
    {
        "CatalogId": str,
        "TransactionId": str,
    },
    total=False,
)

class DeleteTableRequestRequestTypeDef(
    _RequiredDeleteTableRequestRequestTypeDef, _OptionalDeleteTableRequestRequestTypeDef
):
    pass

_RequiredDeleteTableVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTableVersionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "VersionId": str,
    },
)
_OptionalDeleteTableVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTableVersionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class DeleteTableVersionRequestRequestTypeDef(
    _RequiredDeleteTableVersionRequestRequestTypeDef,
    _OptionalDeleteTableVersionRequestRequestTypeDef,
):
    pass

DeleteTriggerRequestRequestTypeDef = TypedDict(
    "DeleteTriggerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteTriggerResponseTypeDef = TypedDict(
    "DeleteTriggerResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteUserDefinedFunctionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionName": str,
    },
)
_OptionalDeleteUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteUserDefinedFunctionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class DeleteUserDefinedFunctionRequestRequestTypeDef(
    _RequiredDeleteUserDefinedFunctionRequestRequestTypeDef,
    _OptionalDeleteUserDefinedFunctionRequestRequestTypeDef,
):
    pass

DeleteWorkflowRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteWorkflowResponseTypeDef = TypedDict(
    "DeleteWorkflowResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeltaTargetTypeDef = TypedDict(
    "DeltaTargetTypeDef",
    {
        "DeltaTables": List[str],
        "ConnectionName": str,
        "WriteManifest": bool,
        "CreateNativeDeltaTable": bool,
    },
    total=False,
)

DevEndpointCustomLibrariesTypeDef = TypedDict(
    "DevEndpointCustomLibrariesTypeDef",
    {
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
    },
    total=False,
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
        "WorkerType": WorkerTypeType,
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

_RequiredDirectJDBCSourceTypeDef = TypedDict(
    "_RequiredDirectJDBCSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
        "ConnectionName": str,
        "ConnectionType": JDBCConnectionTypeType,
    },
)
_OptionalDirectJDBCSourceTypeDef = TypedDict(
    "_OptionalDirectJDBCSourceTypeDef",
    {
        "RedshiftTmpDir": str,
    },
    total=False,
)

class DirectJDBCSourceTypeDef(_RequiredDirectJDBCSourceTypeDef, _OptionalDirectJDBCSourceTypeDef):
    pass

_RequiredDirectKafkaSourceTypeDef = TypedDict(
    "_RequiredDirectKafkaSourceTypeDef",
    {
        "Name": str,
    },
)
_OptionalDirectKafkaSourceTypeDef = TypedDict(
    "_OptionalDirectKafkaSourceTypeDef",
    {
        "StreamingOptions": "KafkaStreamingSourceOptionsTypeDef",
        "WindowSize": int,
        "DetectSchema": bool,
        "DataPreviewOptions": "StreamingDataPreviewOptionsTypeDef",
    },
    total=False,
)

class DirectKafkaSourceTypeDef(
    _RequiredDirectKafkaSourceTypeDef, _OptionalDirectKafkaSourceTypeDef
):
    pass

_RequiredDirectKinesisSourceTypeDef = TypedDict(
    "_RequiredDirectKinesisSourceTypeDef",
    {
        "Name": str,
    },
)
_OptionalDirectKinesisSourceTypeDef = TypedDict(
    "_OptionalDirectKinesisSourceTypeDef",
    {
        "WindowSize": int,
        "DetectSchema": bool,
        "StreamingOptions": "KinesisStreamingSourceOptionsTypeDef",
        "DataPreviewOptions": "StreamingDataPreviewOptionsTypeDef",
    },
    total=False,
)

class DirectKinesisSourceTypeDef(
    _RequiredDirectKinesisSourceTypeDef, _OptionalDirectKinesisSourceTypeDef
):
    pass

DirectSchemaChangePolicyTypeDef = TypedDict(
    "DirectSchemaChangePolicyTypeDef",
    {
        "EnableUpdateCatalog": bool,
        "UpdateBehavior": UpdateCatalogBehaviorType,
        "Table": str,
        "Database": str,
    },
    total=False,
)

_RequiredDoubleColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredDoubleColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
    },
)
_OptionalDoubleColumnStatisticsDataTypeDef = TypedDict(
    "_OptionalDoubleColumnStatisticsDataTypeDef",
    {
        "MinimumValue": float,
        "MaximumValue": float,
    },
    total=False,
)

class DoubleColumnStatisticsDataTypeDef(
    _RequiredDoubleColumnStatisticsDataTypeDef, _OptionalDoubleColumnStatisticsDataTypeDef
):
    pass

_RequiredDropDuplicatesTypeDef = TypedDict(
    "_RequiredDropDuplicatesTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
    },
)
_OptionalDropDuplicatesTypeDef = TypedDict(
    "_OptionalDropDuplicatesTypeDef",
    {
        "Columns": List[List[str]],
    },
    total=False,
)

class DropDuplicatesTypeDef(_RequiredDropDuplicatesTypeDef, _OptionalDropDuplicatesTypeDef):
    pass

DropFieldsTypeDef = TypedDict(
    "DropFieldsTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Paths": List[List[str]],
    },
)

_RequiredDropNullFieldsTypeDef = TypedDict(
    "_RequiredDropNullFieldsTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
    },
)
_OptionalDropNullFieldsTypeDef = TypedDict(
    "_OptionalDropNullFieldsTypeDef",
    {
        "NullCheckBoxList": "NullCheckBoxListTypeDef",
        "NullTextList": List["NullValueFieldTypeDef"],
    },
    total=False,
)

class DropNullFieldsTypeDef(_RequiredDropNullFieldsTypeDef, _OptionalDropNullFieldsTypeDef):
    pass

_RequiredDynamicTransformTypeDef = TypedDict(
    "_RequiredDynamicTransformTypeDef",
    {
        "Name": str,
        "TransformName": str,
        "Inputs": List[str],
        "FunctionName": str,
        "Path": str,
    },
)
_OptionalDynamicTransformTypeDef = TypedDict(
    "_OptionalDynamicTransformTypeDef",
    {
        "Parameters": List["TransformConfigParameterTypeDef"],
        "Version": str,
    },
    total=False,
)

class DynamicTransformTypeDef(_RequiredDynamicTransformTypeDef, _OptionalDynamicTransformTypeDef):
    pass

DynamoDBCatalogSourceTypeDef = TypedDict(
    "DynamoDBCatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)

DynamoDBTargetTypeDef = TypedDict(
    "DynamoDBTargetTypeDef",
    {
        "Path": str,
        "scanAll": bool,
        "scanRate": float,
    },
    total=False,
)

EdgeTypeDef = TypedDict(
    "EdgeTypeDef",
    {
        "SourceId": str,
        "DestinationId": str,
    },
    total=False,
)

_RequiredEncryptionAtRestTypeDef = TypedDict(
    "_RequiredEncryptionAtRestTypeDef",
    {
        "CatalogEncryptionMode": CatalogEncryptionModeType,
    },
)
_OptionalEncryptionAtRestTypeDef = TypedDict(
    "_OptionalEncryptionAtRestTypeDef",
    {
        "SseAwsKmsKeyId": str,
    },
    total=False,
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
    "ErrorDetailTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredEvaluateDataQualityTypeDef = TypedDict(
    "_RequiredEvaluateDataQualityTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Ruleset": str,
    },
)
_OptionalEvaluateDataQualityTypeDef = TypedDict(
    "_OptionalEvaluateDataQualityTypeDef",
    {
        "Output": DQTransformOutputType,
        "PublishingOptions": "DQResultsPublishingOptionsTypeDef",
        "StopJobOnFailureOptions": "DQStopJobOnFailureOptionsTypeDef",
    },
    total=False,
)

class EvaluateDataQualityTypeDef(
    _RequiredEvaluateDataQualityTypeDef, _OptionalEvaluateDataQualityTypeDef
):
    pass

_RequiredEvaluationMetricsTypeDef = TypedDict(
    "_RequiredEvaluationMetricsTypeDef",
    {
        "TransformType": Literal["FIND_MATCHES"],
    },
)
_OptionalEvaluationMetricsTypeDef = TypedDict(
    "_OptionalEvaluationMetricsTypeDef",
    {
        "FindMatchesMetrics": "FindMatchesMetricsTypeDef",
    },
    total=False,
)

class EvaluationMetricsTypeDef(
    _RequiredEvaluationMetricsTypeDef, _OptionalEvaluationMetricsTypeDef
):
    pass

_RequiredEventBatchingConditionTypeDef = TypedDict(
    "_RequiredEventBatchingConditionTypeDef",
    {
        "BatchSize": int,
    },
)
_OptionalEventBatchingConditionTypeDef = TypedDict(
    "_OptionalEventBatchingConditionTypeDef",
    {
        "BatchWindow": int,
    },
    total=False,
)

class EventBatchingConditionTypeDef(
    _RequiredEventBatchingConditionTypeDef, _OptionalEventBatchingConditionTypeDef
):
    pass

ExecutionPropertyTypeDef = TypedDict(
    "ExecutionPropertyTypeDef",
    {
        "MaxConcurrentRuns": int,
    },
    total=False,
)

ExportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "ExportLabelsTaskRunPropertiesTypeDef",
    {
        "OutputS3Path": str,
    },
    total=False,
)

FederatedDatabaseTypeDef = TypedDict(
    "FederatedDatabaseTypeDef",
    {
        "Identifier": str,
        "ConnectionName": str,
    },
    total=False,
)

FederatedTableTypeDef = TypedDict(
    "FederatedTableTypeDef",
    {
        "Identifier": str,
        "DatabaseIdentifier": str,
        "ConnectionName": str,
    },
    total=False,
)

_RequiredFillMissingValuesTypeDef = TypedDict(
    "_RequiredFillMissingValuesTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "ImputedPath": str,
    },
)
_OptionalFillMissingValuesTypeDef = TypedDict(
    "_OptionalFillMissingValuesTypeDef",
    {
        "FilledPath": str,
    },
    total=False,
)

class FillMissingValuesTypeDef(
    _RequiredFillMissingValuesTypeDef, _OptionalFillMissingValuesTypeDef
):
    pass

_RequiredFilterExpressionTypeDef = TypedDict(
    "_RequiredFilterExpressionTypeDef",
    {
        "Operation": FilterOperationType,
        "Values": List["FilterValueTypeDef"],
    },
)
_OptionalFilterExpressionTypeDef = TypedDict(
    "_OptionalFilterExpressionTypeDef",
    {
        "Negated": bool,
    },
    total=False,
)

class FilterExpressionTypeDef(_RequiredFilterExpressionTypeDef, _OptionalFilterExpressionTypeDef):
    pass

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "LogicalOperator": FilterLogicalOperatorType,
        "Filters": List["FilterExpressionTypeDef"],
    },
)

FilterValueTypeDef = TypedDict(
    "FilterValueTypeDef",
    {
        "Type": FilterValueTypeType,
        "Value": List[str],
    },
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
    {
        "JobId": str,
        "JobName": str,
        "JobRunId": str,
    },
    total=False,
)

_RequiredGetBlueprintRequestRequestTypeDef = TypedDict(
    "_RequiredGetBlueprintRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetBlueprintRequestRequestTypeDef = TypedDict(
    "_OptionalGetBlueprintRequestRequestTypeDef",
    {
        "IncludeBlueprint": bool,
        "IncludeParameterSpec": bool,
    },
    total=False,
)

class GetBlueprintRequestRequestTypeDef(
    _RequiredGetBlueprintRequestRequestTypeDef, _OptionalGetBlueprintRequestRequestTypeDef
):
    pass

GetBlueprintResponseTypeDef = TypedDict(
    "GetBlueprintResponseTypeDef",
    {
        "Blueprint": "BlueprintTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBlueprintRunRequestRequestTypeDef = TypedDict(
    "GetBlueprintRunRequestRequestTypeDef",
    {
        "BlueprintName": str,
        "RunId": str,
    },
)

GetBlueprintRunResponseTypeDef = TypedDict(
    "GetBlueprintRunResponseTypeDef",
    {
        "BlueprintRun": "BlueprintRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetBlueprintRunsRequestRequestTypeDef = TypedDict(
    "_RequiredGetBlueprintRunsRequestRequestTypeDef",
    {
        "BlueprintName": str,
    },
)
_OptionalGetBlueprintRunsRequestRequestTypeDef = TypedDict(
    "_OptionalGetBlueprintRunsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetBlueprintRunsRequestRequestTypeDef(
    _RequiredGetBlueprintRunsRequestRequestTypeDef, _OptionalGetBlueprintRunsRequestRequestTypeDef
):
    pass

GetBlueprintRunsResponseTypeDef = TypedDict(
    "GetBlueprintRunsResponseTypeDef",
    {
        "BlueprintRuns": List["BlueprintRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCatalogImportStatusRequestRequestTypeDef = TypedDict(
    "GetCatalogImportStatusRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

GetCatalogImportStatusResponseTypeDef = TypedDict(
    "GetCatalogImportStatusResponseTypeDef",
    {
        "ImportStatus": "CatalogImportStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetClassifierRequestRequestTypeDef = TypedDict(
    "GetClassifierRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetClassifierResponseTypeDef = TypedDict(
    "GetClassifierResponseTypeDef",
    {
        "Classifier": "ClassifierTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetClassifiersRequestRequestTypeDef = TypedDict(
    "GetClassifiersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

GetClassifiersResponseTypeDef = TypedDict(
    "GetClassifiersResponseTypeDef",
    {
        "Classifiers": List["ClassifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetColumnStatisticsForPartitionRequestRequestTypeDef = TypedDict(
    "_RequiredGetColumnStatisticsForPartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": List[str],
        "ColumnNames": List[str],
    },
)
_OptionalGetColumnStatisticsForPartitionRequestRequestTypeDef = TypedDict(
    "_OptionalGetColumnStatisticsForPartitionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class GetColumnStatisticsForPartitionRequestRequestTypeDef(
    _RequiredGetColumnStatisticsForPartitionRequestRequestTypeDef,
    _OptionalGetColumnStatisticsForPartitionRequestRequestTypeDef,
):
    pass

GetColumnStatisticsForPartitionResponseTypeDef = TypedDict(
    "GetColumnStatisticsForPartitionResponseTypeDef",
    {
        "ColumnStatisticsList": List["ColumnStatisticsTypeDef"],
        "Errors": List["ColumnErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetColumnStatisticsForTableRequestRequestTypeDef = TypedDict(
    "_RequiredGetColumnStatisticsForTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "ColumnNames": List[str],
    },
)
_OptionalGetColumnStatisticsForTableRequestRequestTypeDef = TypedDict(
    "_OptionalGetColumnStatisticsForTableRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class GetColumnStatisticsForTableRequestRequestTypeDef(
    _RequiredGetColumnStatisticsForTableRequestRequestTypeDef,
    _OptionalGetColumnStatisticsForTableRequestRequestTypeDef,
):
    pass

GetColumnStatisticsForTableResponseTypeDef = TypedDict(
    "GetColumnStatisticsForTableResponseTypeDef",
    {
        "ColumnStatisticsList": List["ColumnStatisticsTypeDef"],
        "Errors": List["ColumnErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredGetConnectionRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalGetConnectionRequestRequestTypeDef",
    {
        "CatalogId": str,
        "HidePassword": bool,
    },
    total=False,
)

class GetConnectionRequestRequestTypeDef(
    _RequiredGetConnectionRequestRequestTypeDef, _OptionalGetConnectionRequestRequestTypeDef
):
    pass

GetConnectionResponseTypeDef = TypedDict(
    "GetConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectionsFilterTypeDef = TypedDict(
    "GetConnectionsFilterTypeDef",
    {
        "MatchCriteria": List[str],
        "ConnectionType": ConnectionTypeType,
    },
    total=False,
)

GetConnectionsRequestRequestTypeDef = TypedDict(
    "GetConnectionsRequestRequestTypeDef",
    {
        "CatalogId": str,
        "Filter": "GetConnectionsFilterTypeDef",
        "HidePassword": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetConnectionsResponseTypeDef = TypedDict(
    "GetConnectionsResponseTypeDef",
    {
        "ConnectionList": List["ConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCrawlerMetricsRequestRequestTypeDef = TypedDict(
    "GetCrawlerMetricsRequestRequestTypeDef",
    {
        "CrawlerNameList": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

GetCrawlerMetricsResponseTypeDef = TypedDict(
    "GetCrawlerMetricsResponseTypeDef",
    {
        "CrawlerMetricsList": List["CrawlerMetricsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCrawlerRequestRequestTypeDef = TypedDict(
    "GetCrawlerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetCrawlerResponseTypeDef = TypedDict(
    "GetCrawlerResponseTypeDef",
    {
        "Crawler": "CrawlerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCrawlersRequestRequestTypeDef = TypedDict(
    "GetCrawlersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

GetCrawlersResponseTypeDef = TypedDict(
    "GetCrawlersResponseTypeDef",
    {
        "Crawlers": List["CrawlerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCustomEntityTypeRequestRequestTypeDef = TypedDict(
    "GetCustomEntityTypeRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetCustomEntityTypeResponseTypeDef = TypedDict(
    "GetCustomEntityTypeResponseTypeDef",
    {
        "Name": str,
        "RegexString": str,
        "ContextWords": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataCatalogEncryptionSettingsRequestRequestTypeDef = TypedDict(
    "GetDataCatalogEncryptionSettingsRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

GetDataCatalogEncryptionSettingsResponseTypeDef = TypedDict(
    "GetDataCatalogEncryptionSettingsResponseTypeDef",
    {
        "DataCatalogEncryptionSettings": "DataCatalogEncryptionSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataQualityResultRequestRequestTypeDef = TypedDict(
    "GetDataQualityResultRequestRequestTypeDef",
    {
        "ResultId": str,
    },
)

GetDataQualityResultResponseTypeDef = TypedDict(
    "GetDataQualityResultResponseTypeDef",
    {
        "ResultId": str,
        "Score": float,
        "DataSource": "DataSourceTypeDef",
        "RulesetName": str,
        "EvaluationContext": str,
        "StartedOn": datetime,
        "CompletedOn": datetime,
        "JobName": str,
        "JobRunId": str,
        "RulesetEvaluationRunId": str,
        "RuleResults": List["DataQualityRuleResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataQualityRuleRecommendationRunRequestRequestTypeDef = TypedDict(
    "GetDataQualityRuleRecommendationRunRequestRequestTypeDef",
    {
        "RunId": str,
    },
)

GetDataQualityRuleRecommendationRunResponseTypeDef = TypedDict(
    "GetDataQualityRuleRecommendationRunResponseTypeDef",
    {
        "RunId": str,
        "DataSource": "DataSourceTypeDef",
        "Role": str,
        "NumberOfWorkers": int,
        "Timeout": int,
        "Status": TaskStatusTypeType,
        "ErrorString": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "ExecutionTime": int,
        "RecommendedRuleset": str,
        "CreatedRulesetName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataQualityRulesetEvaluationRunRequestRequestTypeDef = TypedDict(
    "GetDataQualityRulesetEvaluationRunRequestRequestTypeDef",
    {
        "RunId": str,
    },
)

GetDataQualityRulesetEvaluationRunResponseTypeDef = TypedDict(
    "GetDataQualityRulesetEvaluationRunResponseTypeDef",
    {
        "RunId": str,
        "DataSource": "DataSourceTypeDef",
        "Role": str,
        "NumberOfWorkers": int,
        "Timeout": int,
        "AdditionalRunOptions": "DataQualityEvaluationRunAdditionalRunOptionsTypeDef",
        "Status": TaskStatusTypeType,
        "ErrorString": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "ExecutionTime": int,
        "RulesetNames": List[str],
        "ResultIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataQualityRulesetRequestRequestTypeDef = TypedDict(
    "GetDataQualityRulesetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetDataQualityRulesetResponseTypeDef = TypedDict(
    "GetDataQualityRulesetResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "Ruleset": str,
        "TargetTable": "DataQualityTargetTableTypeDef",
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "RecommendationRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDatabaseRequestRequestTypeDef = TypedDict(
    "_RequiredGetDatabaseRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetDatabaseRequestRequestTypeDef = TypedDict(
    "_OptionalGetDatabaseRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class GetDatabaseRequestRequestTypeDef(
    _RequiredGetDatabaseRequestRequestTypeDef, _OptionalGetDatabaseRequestRequestTypeDef
):
    pass

GetDatabaseResponseTypeDef = TypedDict(
    "GetDatabaseResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatabasesRequestRequestTypeDef = TypedDict(
    "GetDatabasesRequestRequestTypeDef",
    {
        "CatalogId": str,
        "NextToken": str,
        "MaxResults": int,
        "ResourceShareType": ResourceShareTypeType,
    },
    total=False,
)

GetDatabasesResponseTypeDef = TypedDict(
    "GetDatabasesResponseTypeDef",
    {
        "DatabaseList": List["DatabaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataflowGraphRequestRequestTypeDef = TypedDict(
    "GetDataflowGraphRequestRequestTypeDef",
    {
        "PythonScript": str,
    },
    total=False,
)

GetDataflowGraphResponseTypeDef = TypedDict(
    "GetDataflowGraphResponseTypeDef",
    {
        "DagNodes": List["CodeGenNodeTypeDef"],
        "DagEdges": List["CodeGenEdgeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDevEndpointRequestRequestTypeDef = TypedDict(
    "GetDevEndpointRequestRequestTypeDef",
    {
        "EndpointName": str,
    },
)

GetDevEndpointResponseTypeDef = TypedDict(
    "GetDevEndpointResponseTypeDef",
    {
        "DevEndpoint": "DevEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDevEndpointsRequestRequestTypeDef = TypedDict(
    "GetDevEndpointsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

GetDevEndpointsResponseTypeDef = TypedDict(
    "GetDevEndpointsResponseTypeDef",
    {
        "DevEndpoints": List["DevEndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetJobBookmarkRequestRequestTypeDef = TypedDict(
    "_RequiredGetJobBookmarkRequestRequestTypeDef",
    {
        "JobName": str,
    },
)
_OptionalGetJobBookmarkRequestRequestTypeDef = TypedDict(
    "_OptionalGetJobBookmarkRequestRequestTypeDef",
    {
        "RunId": str,
    },
    total=False,
)

class GetJobBookmarkRequestRequestTypeDef(
    _RequiredGetJobBookmarkRequestRequestTypeDef, _OptionalGetJobBookmarkRequestRequestTypeDef
):
    pass

GetJobBookmarkResponseTypeDef = TypedDict(
    "GetJobBookmarkResponseTypeDef",
    {
        "JobBookmarkEntry": "JobBookmarkEntryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRequestRequestTypeDef = TypedDict(
    "GetJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
)

GetJobResponseTypeDef = TypedDict(
    "GetJobResponseTypeDef",
    {
        "Job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetJobRunRequestRequestTypeDef = TypedDict(
    "_RequiredGetJobRunRequestRequestTypeDef",
    {
        "JobName": str,
        "RunId": str,
    },
)
_OptionalGetJobRunRequestRequestTypeDef = TypedDict(
    "_OptionalGetJobRunRequestRequestTypeDef",
    {
        "PredecessorsIncluded": bool,
    },
    total=False,
)

class GetJobRunRequestRequestTypeDef(
    _RequiredGetJobRunRequestRequestTypeDef, _OptionalGetJobRunRequestRequestTypeDef
):
    pass

GetJobRunResponseTypeDef = TypedDict(
    "GetJobRunResponseTypeDef",
    {
        "JobRun": "JobRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetJobRunsRequestRequestTypeDef = TypedDict(
    "_RequiredGetJobRunsRequestRequestTypeDef",
    {
        "JobName": str,
    },
)
_OptionalGetJobRunsRequestRequestTypeDef = TypedDict(
    "_OptionalGetJobRunsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetJobRunsRequestRequestTypeDef(
    _RequiredGetJobRunsRequestRequestTypeDef, _OptionalGetJobRunsRequestRequestTypeDef
):
    pass

GetJobRunsResponseTypeDef = TypedDict(
    "GetJobRunsResponseTypeDef",
    {
        "JobRuns": List["JobRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobsRequestRequestTypeDef = TypedDict(
    "GetJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetJobsResponseTypeDef = TypedDict(
    "GetJobsResponseTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMLTaskRunRequestRequestTypeDef = TypedDict(
    "GetMLTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
    },
)

GetMLTaskRunResponseTypeDef = TypedDict(
    "GetMLTaskRunResponseTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": TaskStatusTypeType,
        "LogGroupName": str,
        "Properties": "TaskRunPropertiesTypeDef",
        "ErrorString": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "ExecutionTime": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMLTaskRunsRequestRequestTypeDef = TypedDict(
    "_RequiredGetMLTaskRunsRequestRequestTypeDef",
    {
        "TransformId": str,
    },
)
_OptionalGetMLTaskRunsRequestRequestTypeDef = TypedDict(
    "_OptionalGetMLTaskRunsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filter": "TaskRunFilterCriteriaTypeDef",
        "Sort": "TaskRunSortCriteriaTypeDef",
    },
    total=False,
)

class GetMLTaskRunsRequestRequestTypeDef(
    _RequiredGetMLTaskRunsRequestRequestTypeDef, _OptionalGetMLTaskRunsRequestRequestTypeDef
):
    pass

GetMLTaskRunsResponseTypeDef = TypedDict(
    "GetMLTaskRunsResponseTypeDef",
    {
        "TaskRuns": List["TaskRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMLTransformRequestRequestTypeDef = TypedDict(
    "GetMLTransformRequestRequestTypeDef",
    {
        "TransformId": str,
    },
)

GetMLTransformResponseTypeDef = TypedDict(
    "GetMLTransformResponseTypeDef",
    {
        "TransformId": str,
        "Name": str,
        "Description": str,
        "Status": TransformStatusTypeType,
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
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
        "TransformEncryption": "TransformEncryptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMLTransformsRequestRequestTypeDef = TypedDict(
    "GetMLTransformsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filter": "TransformFilterCriteriaTypeDef",
        "Sort": "TransformSortCriteriaTypeDef",
    },
    total=False,
)

GetMLTransformsResponseTypeDef = TypedDict(
    "GetMLTransformsResponseTypeDef",
    {
        "Transforms": List["MLTransformTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMappingRequestRequestTypeDef = TypedDict(
    "_RequiredGetMappingRequestRequestTypeDef",
    {
        "Source": "CatalogEntryTypeDef",
    },
)
_OptionalGetMappingRequestRequestTypeDef = TypedDict(
    "_OptionalGetMappingRequestRequestTypeDef",
    {
        "Sinks": List["CatalogEntryTypeDef"],
        "Location": "LocationTypeDef",
    },
    total=False,
)

class GetMappingRequestRequestTypeDef(
    _RequiredGetMappingRequestRequestTypeDef, _OptionalGetMappingRequestRequestTypeDef
):
    pass

GetMappingResponseTypeDef = TypedDict(
    "GetMappingResponseTypeDef",
    {
        "Mapping": List["MappingEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPartitionIndexesRequestRequestTypeDef = TypedDict(
    "_RequiredGetPartitionIndexesRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalGetPartitionIndexesRequestRequestTypeDef = TypedDict(
    "_OptionalGetPartitionIndexesRequestRequestTypeDef",
    {
        "CatalogId": str,
        "NextToken": str,
    },
    total=False,
)

class GetPartitionIndexesRequestRequestTypeDef(
    _RequiredGetPartitionIndexesRequestRequestTypeDef,
    _OptionalGetPartitionIndexesRequestRequestTypeDef,
):
    pass

GetPartitionIndexesResponseTypeDef = TypedDict(
    "GetPartitionIndexesResponseTypeDef",
    {
        "PartitionIndexDescriptorList": List["PartitionIndexDescriptorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPartitionRequestRequestTypeDef = TypedDict(
    "_RequiredGetPartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": List[str],
    },
)
_OptionalGetPartitionRequestRequestTypeDef = TypedDict(
    "_OptionalGetPartitionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class GetPartitionRequestRequestTypeDef(
    _RequiredGetPartitionRequestRequestTypeDef, _OptionalGetPartitionRequestRequestTypeDef
):
    pass

GetPartitionResponseTypeDef = TypedDict(
    "GetPartitionResponseTypeDef",
    {
        "Partition": "PartitionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPartitionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetPartitionsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalGetPartitionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetPartitionsRequestRequestTypeDef",
    {
        "CatalogId": str,
        "Expression": str,
        "NextToken": str,
        "Segment": "SegmentTypeDef",
        "MaxResults": int,
        "ExcludeColumnSchema": bool,
        "TransactionId": str,
        "QueryAsOfTime": Union[datetime, str],
    },
    total=False,
)

class GetPartitionsRequestRequestTypeDef(
    _RequiredGetPartitionsRequestRequestTypeDef, _OptionalGetPartitionsRequestRequestTypeDef
):
    pass

GetPartitionsResponseTypeDef = TypedDict(
    "GetPartitionsResponseTypeDef",
    {
        "Partitions": List["PartitionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPlanRequestRequestTypeDef = TypedDict(
    "_RequiredGetPlanRequestRequestTypeDef",
    {
        "Mapping": List["MappingEntryTypeDef"],
        "Source": "CatalogEntryTypeDef",
    },
)
_OptionalGetPlanRequestRequestTypeDef = TypedDict(
    "_OptionalGetPlanRequestRequestTypeDef",
    {
        "Sinks": List["CatalogEntryTypeDef"],
        "Location": "LocationTypeDef",
        "Language": LanguageType,
        "AdditionalPlanOptionsMap": Dict[str, str],
    },
    total=False,
)

class GetPlanRequestRequestTypeDef(
    _RequiredGetPlanRequestRequestTypeDef, _OptionalGetPlanRequestRequestTypeDef
):
    pass

GetPlanResponseTypeDef = TypedDict(
    "GetPlanResponseTypeDef",
    {
        "PythonScript": str,
        "ScalaCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegistryInputRequestTypeDef = TypedDict(
    "GetRegistryInputRequestTypeDef",
    {
        "RegistryId": "RegistryIdTypeDef",
    },
)

GetRegistryResponseTypeDef = TypedDict(
    "GetRegistryResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "Description": str,
        "Status": RegistryStatusType,
        "CreatedTime": str,
        "UpdatedTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePoliciesRequestRequestTypeDef = TypedDict(
    "GetResourcePoliciesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetResourcePoliciesResponseTypeDef = TypedDict(
    "GetResourcePoliciesResponseTypeDef",
    {
        "GetResourcePoliciesResponseList": List["GluePolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
    total=False,
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "PolicyInJson": str,
        "PolicyHash": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaByDefinitionInputRequestTypeDef = TypedDict(
    "GetSchemaByDefinitionInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaDefinition": str,
    },
)

GetSchemaByDefinitionResponseTypeDef = TypedDict(
    "GetSchemaByDefinitionResponseTypeDef",
    {
        "SchemaVersionId": str,
        "SchemaArn": str,
        "DataFormat": DataFormatType,
        "Status": SchemaVersionStatusType,
        "CreatedTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaInputRequestTypeDef = TypedDict(
    "GetSchemaInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
    },
)

GetSchemaResponseTypeDef = TypedDict(
    "GetSchemaResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "SchemaName": str,
        "SchemaArn": str,
        "Description": str,
        "DataFormat": DataFormatType,
        "Compatibility": CompatibilityType,
        "SchemaCheckpoint": int,
        "LatestSchemaVersion": int,
        "NextSchemaVersion": int,
        "SchemaStatus": SchemaStatusType,
        "CreatedTime": str,
        "UpdatedTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaVersionInputRequestTypeDef = TypedDict(
    "GetSchemaVersionInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaVersionId": str,
        "SchemaVersionNumber": "SchemaVersionNumberTypeDef",
    },
    total=False,
)

GetSchemaVersionResponseTypeDef = TypedDict(
    "GetSchemaVersionResponseTypeDef",
    {
        "SchemaVersionId": str,
        "SchemaDefinition": str,
        "DataFormat": DataFormatType,
        "SchemaArn": str,
        "VersionNumber": int,
        "Status": SchemaVersionStatusType,
        "CreatedTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaVersionsDiffInputRequestTypeDef = TypedDict(
    "GetSchemaVersionsDiffInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "FirstSchemaVersionNumber": "SchemaVersionNumberTypeDef",
        "SecondSchemaVersionNumber": "SchemaVersionNumberTypeDef",
        "SchemaDiffType": Literal["SYNTAX_DIFF"],
    },
)

GetSchemaVersionsDiffResponseTypeDef = TypedDict(
    "GetSchemaVersionsDiffResponseTypeDef",
    {
        "Diff": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSecurityConfigurationRequestRequestTypeDef = TypedDict(
    "GetSecurityConfigurationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetSecurityConfigurationResponseTypeDef = TypedDict(
    "GetSecurityConfigurationResponseTypeDef",
    {
        "SecurityConfiguration": "SecurityConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSecurityConfigurationsRequestRequestTypeDef = TypedDict(
    "GetSecurityConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

GetSecurityConfigurationsResponseTypeDef = TypedDict(
    "GetSecurityConfigurationsResponseTypeDef",
    {
        "SecurityConfigurations": List["SecurityConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSessionRequestRequestTypeDef = TypedDict(
    "_RequiredGetSessionRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalGetSessionRequestRequestTypeDef = TypedDict(
    "_OptionalGetSessionRequestRequestTypeDef",
    {
        "RequestOrigin": str,
    },
    total=False,
)

class GetSessionRequestRequestTypeDef(
    _RequiredGetSessionRequestRequestTypeDef, _OptionalGetSessionRequestRequestTypeDef
):
    pass

GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "Session": "SessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetStatementRequestRequestTypeDef = TypedDict(
    "_RequiredGetStatementRequestRequestTypeDef",
    {
        "SessionId": str,
        "Id": int,
    },
)
_OptionalGetStatementRequestRequestTypeDef = TypedDict(
    "_OptionalGetStatementRequestRequestTypeDef",
    {
        "RequestOrigin": str,
    },
    total=False,
)

class GetStatementRequestRequestTypeDef(
    _RequiredGetStatementRequestRequestTypeDef, _OptionalGetStatementRequestRequestTypeDef
):
    pass

GetStatementResponseTypeDef = TypedDict(
    "GetStatementResponseTypeDef",
    {
        "Statement": "StatementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTableRequestRequestTypeDef = TypedDict(
    "_RequiredGetTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
    },
)
_OptionalGetTableRequestRequestTypeDef = TypedDict(
    "_OptionalGetTableRequestRequestTypeDef",
    {
        "CatalogId": str,
        "TransactionId": str,
        "QueryAsOfTime": Union[datetime, str],
    },
    total=False,
)

class GetTableRequestRequestTypeDef(
    _RequiredGetTableRequestRequestTypeDef, _OptionalGetTableRequestRequestTypeDef
):
    pass

GetTableResponseTypeDef = TypedDict(
    "GetTableResponseTypeDef",
    {
        "Table": "TableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTableVersionRequestRequestTypeDef = TypedDict(
    "_RequiredGetTableVersionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalGetTableVersionRequestRequestTypeDef = TypedDict(
    "_OptionalGetTableVersionRequestRequestTypeDef",
    {
        "CatalogId": str,
        "VersionId": str,
    },
    total=False,
)

class GetTableVersionRequestRequestTypeDef(
    _RequiredGetTableVersionRequestRequestTypeDef, _OptionalGetTableVersionRequestRequestTypeDef
):
    pass

GetTableVersionResponseTypeDef = TypedDict(
    "GetTableVersionResponseTypeDef",
    {
        "TableVersion": "TableVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTableVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetTableVersionsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalGetTableVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetTableVersionsRequestRequestTypeDef",
    {
        "CatalogId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetTableVersionsRequestRequestTypeDef(
    _RequiredGetTableVersionsRequestRequestTypeDef, _OptionalGetTableVersionsRequestRequestTypeDef
):
    pass

GetTableVersionsResponseTypeDef = TypedDict(
    "GetTableVersionsResponseTypeDef",
    {
        "TableVersions": List["TableVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTablesRequestRequestTypeDef = TypedDict(
    "_RequiredGetTablesRequestRequestTypeDef",
    {
        "DatabaseName": str,
    },
)
_OptionalGetTablesRequestRequestTypeDef = TypedDict(
    "_OptionalGetTablesRequestRequestTypeDef",
    {
        "CatalogId": str,
        "Expression": str,
        "NextToken": str,
        "MaxResults": int,
        "TransactionId": str,
        "QueryAsOfTime": Union[datetime, str],
    },
    total=False,
)

class GetTablesRequestRequestTypeDef(
    _RequiredGetTablesRequestRequestTypeDef, _OptionalGetTablesRequestRequestTypeDef
):
    pass

GetTablesResponseTypeDef = TypedDict(
    "GetTablesResponseTypeDef",
    {
        "TableList": List["TableTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTagsRequestRequestTypeDef = TypedDict(
    "GetTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetTagsResponseTypeDef = TypedDict(
    "GetTagsResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTriggerRequestRequestTypeDef = TypedDict(
    "GetTriggerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetTriggerResponseTypeDef = TypedDict(
    "GetTriggerResponseTypeDef",
    {
        "Trigger": "TriggerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTriggersRequestRequestTypeDef = TypedDict(
    "GetTriggersRequestRequestTypeDef",
    {
        "NextToken": str,
        "DependentJobName": str,
        "MaxResults": int,
    },
    total=False,
)

GetTriggersResponseTypeDef = TypedDict(
    "GetTriggersResponseTypeDef",
    {
        "Triggers": List["TriggerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUnfilteredPartitionMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredGetUnfilteredPartitionMetadataRequestRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": List[str],
        "SupportedPermissionTypes": List[PermissionTypeType],
    },
)
_OptionalGetUnfilteredPartitionMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalGetUnfilteredPartitionMetadataRequestRequestTypeDef",
    {
        "AuditContext": "AuditContextTypeDef",
    },
    total=False,
)

class GetUnfilteredPartitionMetadataRequestRequestTypeDef(
    _RequiredGetUnfilteredPartitionMetadataRequestRequestTypeDef,
    _OptionalGetUnfilteredPartitionMetadataRequestRequestTypeDef,
):
    pass

GetUnfilteredPartitionMetadataResponseTypeDef = TypedDict(
    "GetUnfilteredPartitionMetadataResponseTypeDef",
    {
        "Partition": "PartitionTypeDef",
        "AuthorizedColumns": List[str],
        "IsRegisteredWithLakeFormation": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUnfilteredPartitionsMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredGetUnfilteredPartitionsMetadataRequestRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "SupportedPermissionTypes": List[PermissionTypeType],
    },
)
_OptionalGetUnfilteredPartitionsMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalGetUnfilteredPartitionsMetadataRequestRequestTypeDef",
    {
        "Expression": str,
        "AuditContext": "AuditContextTypeDef",
        "NextToken": str,
        "Segment": "SegmentTypeDef",
        "MaxResults": int,
    },
    total=False,
)

class GetUnfilteredPartitionsMetadataRequestRequestTypeDef(
    _RequiredGetUnfilteredPartitionsMetadataRequestRequestTypeDef,
    _OptionalGetUnfilteredPartitionsMetadataRequestRequestTypeDef,
):
    pass

GetUnfilteredPartitionsMetadataResponseTypeDef = TypedDict(
    "GetUnfilteredPartitionsMetadataResponseTypeDef",
    {
        "UnfilteredPartitions": List["UnfilteredPartitionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUnfilteredTableMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredGetUnfilteredTableMetadataRequestRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "Name": str,
        "SupportedPermissionTypes": List[PermissionTypeType],
    },
)
_OptionalGetUnfilteredTableMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalGetUnfilteredTableMetadataRequestRequestTypeDef",
    {
        "AuditContext": "AuditContextTypeDef",
    },
    total=False,
)

class GetUnfilteredTableMetadataRequestRequestTypeDef(
    _RequiredGetUnfilteredTableMetadataRequestRequestTypeDef,
    _OptionalGetUnfilteredTableMetadataRequestRequestTypeDef,
):
    pass

GetUnfilteredTableMetadataResponseTypeDef = TypedDict(
    "GetUnfilteredTableMetadataResponseTypeDef",
    {
        "Table": "TableTypeDef",
        "AuthorizedColumns": List[str],
        "IsRegisteredWithLakeFormation": bool,
        "CellFilters": List["ColumnRowFilterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredGetUserDefinedFunctionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionName": str,
    },
)
_OptionalGetUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalGetUserDefinedFunctionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class GetUserDefinedFunctionRequestRequestTypeDef(
    _RequiredGetUserDefinedFunctionRequestRequestTypeDef,
    _OptionalGetUserDefinedFunctionRequestRequestTypeDef,
):
    pass

GetUserDefinedFunctionResponseTypeDef = TypedDict(
    "GetUserDefinedFunctionResponseTypeDef",
    {
        "UserDefinedFunction": "UserDefinedFunctionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetUserDefinedFunctionsRequestRequestTypeDef = TypedDict(
    "_RequiredGetUserDefinedFunctionsRequestRequestTypeDef",
    {
        "Pattern": str,
    },
)
_OptionalGetUserDefinedFunctionsRequestRequestTypeDef = TypedDict(
    "_OptionalGetUserDefinedFunctionsRequestRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetUserDefinedFunctionsRequestRequestTypeDef(
    _RequiredGetUserDefinedFunctionsRequestRequestTypeDef,
    _OptionalGetUserDefinedFunctionsRequestRequestTypeDef,
):
    pass

GetUserDefinedFunctionsResponseTypeDef = TypedDict(
    "GetUserDefinedFunctionsResponseTypeDef",
    {
        "UserDefinedFunctions": List["UserDefinedFunctionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetWorkflowRequestRequestTypeDef = TypedDict(
    "_RequiredGetWorkflowRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetWorkflowRequestRequestTypeDef = TypedDict(
    "_OptionalGetWorkflowRequestRequestTypeDef",
    {
        "IncludeGraph": bool,
    },
    total=False,
)

class GetWorkflowRequestRequestTypeDef(
    _RequiredGetWorkflowRequestRequestTypeDef, _OptionalGetWorkflowRequestRequestTypeDef
):
    pass

GetWorkflowResponseTypeDef = TypedDict(
    "GetWorkflowResponseTypeDef",
    {
        "Workflow": "WorkflowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkflowRunPropertiesRequestRequestTypeDef = TypedDict(
    "GetWorkflowRunPropertiesRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)

GetWorkflowRunPropertiesResponseTypeDef = TypedDict(
    "GetWorkflowRunPropertiesResponseTypeDef",
    {
        "RunProperties": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetWorkflowRunRequestRequestTypeDef = TypedDict(
    "_RequiredGetWorkflowRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)
_OptionalGetWorkflowRunRequestRequestTypeDef = TypedDict(
    "_OptionalGetWorkflowRunRequestRequestTypeDef",
    {
        "IncludeGraph": bool,
    },
    total=False,
)

class GetWorkflowRunRequestRequestTypeDef(
    _RequiredGetWorkflowRunRequestRequestTypeDef, _OptionalGetWorkflowRunRequestRequestTypeDef
):
    pass

GetWorkflowRunResponseTypeDef = TypedDict(
    "GetWorkflowRunResponseTypeDef",
    {
        "Run": "WorkflowRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetWorkflowRunsRequestRequestTypeDef = TypedDict(
    "_RequiredGetWorkflowRunsRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetWorkflowRunsRequestRequestTypeDef = TypedDict(
    "_OptionalGetWorkflowRunsRequestRequestTypeDef",
    {
        "IncludeGraph": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetWorkflowRunsRequestRequestTypeDef(
    _RequiredGetWorkflowRunsRequestRequestTypeDef, _OptionalGetWorkflowRunsRequestRequestTypeDef
):
    pass

GetWorkflowRunsResponseTypeDef = TypedDict(
    "GetWorkflowRunsResponseTypeDef",
    {
        "Runs": List["WorkflowRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GluePolicyTypeDef = TypedDict(
    "GluePolicyTypeDef",
    {
        "PolicyInJson": str,
        "PolicyHash": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
    },
    total=False,
)

GlueSchemaTypeDef = TypedDict(
    "GlueSchemaTypeDef",
    {
        "Columns": List["GlueStudioSchemaColumnTypeDef"],
    },
    total=False,
)

_RequiredGlueStudioSchemaColumnTypeDef = TypedDict(
    "_RequiredGlueStudioSchemaColumnTypeDef",
    {
        "Name": str,
    },
)
_OptionalGlueStudioSchemaColumnTypeDef = TypedDict(
    "_OptionalGlueStudioSchemaColumnTypeDef",
    {
        "Type": str,
    },
    total=False,
)

class GlueStudioSchemaColumnTypeDef(
    _RequiredGlueStudioSchemaColumnTypeDef, _OptionalGlueStudioSchemaColumnTypeDef
):
    pass

_RequiredGlueTableTypeDef = TypedDict(
    "_RequiredGlueTableTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)
_OptionalGlueTableTypeDef = TypedDict(
    "_OptionalGlueTableTypeDef",
    {
        "CatalogId": str,
        "ConnectionName": str,
        "AdditionalOptions": Dict[str, str],
    },
    total=False,
)

class GlueTableTypeDef(_RequiredGlueTableTypeDef, _OptionalGlueTableTypeDef):
    pass

_RequiredGovernedCatalogSourceTypeDef = TypedDict(
    "_RequiredGovernedCatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)
_OptionalGovernedCatalogSourceTypeDef = TypedDict(
    "_OptionalGovernedCatalogSourceTypeDef",
    {
        "PartitionPredicate": str,
        "AdditionalOptions": "S3SourceAdditionalOptionsTypeDef",
    },
    total=False,
)

class GovernedCatalogSourceTypeDef(
    _RequiredGovernedCatalogSourceTypeDef, _OptionalGovernedCatalogSourceTypeDef
):
    pass

_RequiredGovernedCatalogTargetTypeDef = TypedDict(
    "_RequiredGovernedCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Table": str,
        "Database": str,
    },
)
_OptionalGovernedCatalogTargetTypeDef = TypedDict(
    "_OptionalGovernedCatalogTargetTypeDef",
    {
        "PartitionKeys": List[List[str]],
        "SchemaChangePolicy": "CatalogSchemaChangePolicyTypeDef",
    },
    total=False,
)

class GovernedCatalogTargetTypeDef(
    _RequiredGovernedCatalogTargetTypeDef, _OptionalGovernedCatalogTargetTypeDef
):
    pass

_RequiredGrokClassifierTypeDef = TypedDict(
    "_RequiredGrokClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "GrokPattern": str,
    },
)
_OptionalGrokClassifierTypeDef = TypedDict(
    "_OptionalGrokClassifierTypeDef",
    {
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "CustomPatterns": str,
    },
    total=False,
)

class GrokClassifierTypeDef(_RequiredGrokClassifierTypeDef, _OptionalGrokClassifierTypeDef):
    pass

ImportCatalogToGlueRequestRequestTypeDef = TypedDict(
    "ImportCatalogToGlueRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

ImportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "ImportLabelsTaskRunPropertiesTypeDef",
    {
        "InputS3Path": str,
        "Replace": bool,
    },
    total=False,
)

JDBCConnectorOptionsTypeDef = TypedDict(
    "JDBCConnectorOptionsTypeDef",
    {
        "FilterPredicate": str,
        "PartitionColumn": str,
        "LowerBound": int,
        "UpperBound": int,
        "NumPartitions": int,
        "JobBookmarkKeys": List[str],
        "JobBookmarkKeysSortOrder": str,
        "DataTypeMapping": Dict[JDBCDataTypeType, GlueRecordTypeType],
    },
    total=False,
)

_RequiredJDBCConnectorSourceTypeDef = TypedDict(
    "_RequiredJDBCConnectorSourceTypeDef",
    {
        "Name": str,
        "ConnectionName": str,
        "ConnectorName": str,
        "ConnectionType": str,
    },
)
_OptionalJDBCConnectorSourceTypeDef = TypedDict(
    "_OptionalJDBCConnectorSourceTypeDef",
    {
        "AdditionalOptions": "JDBCConnectorOptionsTypeDef",
        "ConnectionTable": str,
        "Query": str,
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class JDBCConnectorSourceTypeDef(
    _RequiredJDBCConnectorSourceTypeDef, _OptionalJDBCConnectorSourceTypeDef
):
    pass

_RequiredJDBCConnectorTargetTypeDef = TypedDict(
    "_RequiredJDBCConnectorTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "ConnectionName": str,
        "ConnectionTable": str,
        "ConnectorName": str,
        "ConnectionType": str,
    },
)
_OptionalJDBCConnectorTargetTypeDef = TypedDict(
    "_OptionalJDBCConnectorTargetTypeDef",
    {
        "AdditionalOptions": Dict[str, str],
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class JDBCConnectorTargetTypeDef(
    _RequiredJDBCConnectorTargetTypeDef, _OptionalJDBCConnectorTargetTypeDef
):
    pass

JdbcTargetTypeDef = TypedDict(
    "JdbcTargetTypeDef",
    {
        "ConnectionName": str,
        "Path": str,
        "Exclusions": List[str],
        "EnableAdditionalMetadata": List[JdbcMetadataEntryType],
    },
    total=False,
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
    {
        "JobBookmarksEncryptionMode": JobBookmarksEncryptionModeType,
        "KmsKeyArn": str,
    },
    total=False,
)

JobCommandTypeDef = TypedDict(
    "JobCommandTypeDef",
    {
        "Name": str,
        "ScriptLocation": str,
        "PythonVersion": str,
    },
    total=False,
)

JobNodeDetailsTypeDef = TypedDict(
    "JobNodeDetailsTypeDef",
    {
        "JobRuns": List["JobRunTypeDef"],
    },
    total=False,
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
        "JobRunState": JobRunStateType,
        "Arguments": Dict[str, str],
        "ErrorMessage": str,
        "PredecessorRuns": List["PredecessorTypeDef"],
        "AllocatedCapacity": int,
        "ExecutionTime": int,
        "Timeout": int,
        "MaxCapacity": float,
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "LogGroupName": str,
        "NotificationProperty": "NotificationPropertyTypeDef",
        "GlueVersion": str,
        "DPUSeconds": float,
        "ExecutionClass": ExecutionClassType,
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
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": "NotificationPropertyTypeDef",
        "GlueVersion": str,
        "CodeGenConfigurationNodes": Dict[str, "CodeGenConfigurationNodeTypeDef"],
        "ExecutionClass": ExecutionClassType,
        "SourceControlDetails": "SourceControlDetailsTypeDef",
    },
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
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "SecurityConfiguration": str,
        "NotificationProperty": "NotificationPropertyTypeDef",
        "GlueVersion": str,
        "CodeGenConfigurationNodes": Dict[str, "CodeGenConfigurationNodeTypeDef"],
        "ExecutionClass": ExecutionClassType,
        "SourceControlDetails": "SourceControlDetailsTypeDef",
    },
    total=False,
)

JoinColumnTypeDef = TypedDict(
    "JoinColumnTypeDef",
    {
        "From": str,
        "Keys": List[List[str]],
    },
)

JoinTypeDef = TypedDict(
    "JoinTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "JoinType": JoinTypeType,
        "Columns": List["JoinColumnTypeDef"],
    },
)

_RequiredJsonClassifierTypeDef = TypedDict(
    "_RequiredJsonClassifierTypeDef",
    {
        "Name": str,
        "JsonPath": str,
    },
)
_OptionalJsonClassifierTypeDef = TypedDict(
    "_OptionalJsonClassifierTypeDef",
    {
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
    },
    total=False,
)

class JsonClassifierTypeDef(_RequiredJsonClassifierTypeDef, _OptionalJsonClassifierTypeDef):
    pass

KafkaStreamingSourceOptionsTypeDef = TypedDict(
    "KafkaStreamingSourceOptionsTypeDef",
    {
        "BootstrapServers": str,
        "SecurityProtocol": str,
        "ConnectionName": str,
        "TopicName": str,
        "Assign": str,
        "SubscribePattern": str,
        "Classification": str,
        "Delimiter": str,
        "StartingOffsets": str,
        "EndingOffsets": str,
        "PollTimeoutMs": int,
        "NumRetries": int,
        "RetryIntervalMs": int,
        "MaxOffsetsPerTrigger": int,
        "MinPartitions": int,
        "IncludeHeaders": bool,
        "AddRecordTimestamp": str,
        "EmitConsumerLagMetrics": str,
    },
    total=False,
)

KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef",
    {
        "Name": str,
        "Type": str,
    },
)

KinesisStreamingSourceOptionsTypeDef = TypedDict(
    "KinesisStreamingSourceOptionsTypeDef",
    {
        "EndpointUrl": str,
        "StreamName": str,
        "Classification": str,
        "Delimiter": str,
        "StartingPosition": StartingPositionType,
        "MaxFetchTimeInMs": int,
        "MaxFetchRecordsPerShard": int,
        "MaxRecordPerRead": int,
        "AddIdleTimeBetweenReads": bool,
        "IdleTimeBetweenReadsInMs": int,
        "DescribeShardInterval": int,
        "NumRetries": int,
        "RetryIntervalMs": int,
        "MaxRetryIntervalMs": int,
        "AvoidEmptyBatches": bool,
        "StreamArn": str,
        "RoleArn": str,
        "RoleSessionName": str,
        "AddRecordTimestamp": str,
        "EmitConsumerLagMetrics": str,
    },
    total=False,
)

LabelingSetGenerationTaskRunPropertiesTypeDef = TypedDict(
    "LabelingSetGenerationTaskRunPropertiesTypeDef",
    {
        "OutputS3Path": str,
    },
    total=False,
)

LakeFormationConfigurationTypeDef = TypedDict(
    "LakeFormationConfigurationTypeDef",
    {
        "UseLakeFormationCredentials": bool,
        "AccountId": str,
    },
    total=False,
)

LastActiveDefinitionTypeDef = TypedDict(
    "LastActiveDefinitionTypeDef",
    {
        "Description": str,
        "LastModifiedOn": datetime,
        "ParameterSpec": str,
        "BlueprintLocation": str,
        "BlueprintServiceLocation": str,
    },
    total=False,
)

LastCrawlInfoTypeDef = TypedDict(
    "LastCrawlInfoTypeDef",
    {
        "Status": LastCrawlStatusType,
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
    {
        "CrawlerLineageSettings": CrawlerLineageSettingsType,
    },
    total=False,
)

ListBlueprintsRequestRequestTypeDef = TypedDict(
    "ListBlueprintsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListBlueprintsResponseTypeDef = TypedDict(
    "ListBlueprintsResponseTypeDef",
    {
        "Blueprints": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCrawlersRequestRequestTypeDef = TypedDict(
    "ListCrawlersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListCrawlersResponseTypeDef = TypedDict(
    "ListCrawlersResponseTypeDef",
    {
        "CrawlerNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCrawlsRequestRequestTypeDef = TypedDict(
    "_RequiredListCrawlsRequestRequestTypeDef",
    {
        "CrawlerName": str,
    },
)
_OptionalListCrawlsRequestRequestTypeDef = TypedDict(
    "_OptionalListCrawlsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "Filters": List["CrawlsFilterTypeDef"],
        "NextToken": str,
    },
    total=False,
)

class ListCrawlsRequestRequestTypeDef(
    _RequiredListCrawlsRequestRequestTypeDef, _OptionalListCrawlsRequestRequestTypeDef
):
    pass

ListCrawlsResponseTypeDef = TypedDict(
    "ListCrawlsResponseTypeDef",
    {
        "Crawls": List["CrawlerHistoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomEntityTypesRequestRequestTypeDef = TypedDict(
    "ListCustomEntityTypesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListCustomEntityTypesResponseTypeDef = TypedDict(
    "ListCustomEntityTypesResponseTypeDef",
    {
        "CustomEntityTypes": List["CustomEntityTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataQualityResultsRequestRequestTypeDef = TypedDict(
    "ListDataQualityResultsRequestRequestTypeDef",
    {
        "Filter": "DataQualityResultFilterCriteriaTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDataQualityResultsResponseTypeDef = TypedDict(
    "ListDataQualityResultsResponseTypeDef",
    {
        "Results": List["DataQualityResultDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataQualityRuleRecommendationRunsRequestRequestTypeDef = TypedDict(
    "ListDataQualityRuleRecommendationRunsRequestRequestTypeDef",
    {
        "Filter": "DataQualityRuleRecommendationRunFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDataQualityRuleRecommendationRunsResponseTypeDef = TypedDict(
    "ListDataQualityRuleRecommendationRunsResponseTypeDef",
    {
        "Runs": List["DataQualityRuleRecommendationRunDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataQualityRulesetEvaluationRunsRequestRequestTypeDef = TypedDict(
    "ListDataQualityRulesetEvaluationRunsRequestRequestTypeDef",
    {
        "Filter": "DataQualityRulesetEvaluationRunFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDataQualityRulesetEvaluationRunsResponseTypeDef = TypedDict(
    "ListDataQualityRulesetEvaluationRunsResponseTypeDef",
    {
        "Runs": List["DataQualityRulesetEvaluationRunDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataQualityRulesetsRequestRequestTypeDef = TypedDict(
    "ListDataQualityRulesetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filter": "DataQualityRulesetFilterCriteriaTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

ListDataQualityRulesetsResponseTypeDef = TypedDict(
    "ListDataQualityRulesetsResponseTypeDef",
    {
        "Rulesets": List["DataQualityRulesetListDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevEndpointsRequestRequestTypeDef = TypedDict(
    "ListDevEndpointsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListDevEndpointsResponseTypeDef = TypedDict(
    "ListDevEndpointsResponseTypeDef",
    {
        "DevEndpointNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "JobNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMLTransformsRequestRequestTypeDef = TypedDict(
    "ListMLTransformsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filter": "TransformFilterCriteriaTypeDef",
        "Sort": "TransformSortCriteriaTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

ListMLTransformsResponseTypeDef = TypedDict(
    "ListMLTransformsResponseTypeDef",
    {
        "TransformIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRegistriesInputRequestTypeDef = TypedDict(
    "ListRegistriesInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListRegistriesResponseTypeDef = TypedDict(
    "ListRegistriesResponseTypeDef",
    {
        "Registries": List["RegistryListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSchemaVersionsInputRequestTypeDef = TypedDict(
    "_RequiredListSchemaVersionsInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
    },
)
_OptionalListSchemaVersionsInputRequestTypeDef = TypedDict(
    "_OptionalListSchemaVersionsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListSchemaVersionsInputRequestTypeDef(
    _RequiredListSchemaVersionsInputRequestTypeDef, _OptionalListSchemaVersionsInputRequestTypeDef
):
    pass

ListSchemaVersionsResponseTypeDef = TypedDict(
    "ListSchemaVersionsResponseTypeDef",
    {
        "Schemas": List["SchemaVersionListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchemasInputRequestTypeDef = TypedDict(
    "ListSchemasInputRequestTypeDef",
    {
        "RegistryId": "RegistryIdTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {
        "Schemas": List["SchemaListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSessionsRequestRequestTypeDef = TypedDict(
    "ListSessionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Tags": Dict[str, str],
        "RequestOrigin": str,
    },
    total=False,
)

ListSessionsResponseTypeDef = TypedDict(
    "ListSessionsResponseTypeDef",
    {
        "Ids": List[str],
        "Sessions": List["SessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStatementsRequestRequestTypeDef = TypedDict(
    "_RequiredListStatementsRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)
_OptionalListStatementsRequestRequestTypeDef = TypedDict(
    "_OptionalListStatementsRequestRequestTypeDef",
    {
        "RequestOrigin": str,
        "NextToken": str,
    },
    total=False,
)

class ListStatementsRequestRequestTypeDef(
    _RequiredListStatementsRequestRequestTypeDef, _OptionalListStatementsRequestRequestTypeDef
):
    pass

ListStatementsResponseTypeDef = TypedDict(
    "ListStatementsResponseTypeDef",
    {
        "Statements": List["StatementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTriggersRequestRequestTypeDef = TypedDict(
    "ListTriggersRequestRequestTypeDef",
    {
        "NextToken": str,
        "DependentJobName": str,
        "MaxResults": int,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListTriggersResponseTypeDef = TypedDict(
    "ListTriggersResponseTypeDef",
    {
        "TriggerNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkflowsRequestRequestTypeDef = TypedDict(
    "ListWorkflowsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "Workflows": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredLongColumnStatisticsDataTypeDef = TypedDict(
    "_RequiredLongColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
    },
)
_OptionalLongColumnStatisticsDataTypeDef = TypedDict(
    "_OptionalLongColumnStatisticsDataTypeDef",
    {
        "MinimumValue": int,
        "MaximumValue": int,
    },
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
        "Status": TransformStatusTypeType,
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
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
        "TransformEncryption": "TransformEncryptionTypeDef",
    },
    total=False,
)

_RequiredMLUserDataEncryptionTypeDef = TypedDict(
    "_RequiredMLUserDataEncryptionTypeDef",
    {
        "MlUserDataEncryptionMode": MLUserDataEncryptionModeStringType,
    },
)
_OptionalMLUserDataEncryptionTypeDef = TypedDict(
    "_OptionalMLUserDataEncryptionTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
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

MappingTypeDef = TypedDict(
    "MappingTypeDef",
    {
        "ToKey": str,
        "FromPath": List[str],
        "FromType": str,
        "ToType": str,
        "Dropped": bool,
        "Children": List[Dict[str, Any]],
    },
    total=False,
)

MergeTypeDef = TypedDict(
    "MergeTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Source": str,
        "PrimaryKeys": List[List[str]],
    },
)

MetadataInfoTypeDef = TypedDict(
    "MetadataInfoTypeDef",
    {
        "MetadataValue": str,
        "CreatedTime": str,
        "OtherMetadataValueList": List["OtherMetadataValueListItemTypeDef"],
    },
    total=False,
)

MetadataKeyValuePairTypeDef = TypedDict(
    "MetadataKeyValuePairTypeDef",
    {
        "MetadataKey": str,
        "MetadataValue": str,
    },
    total=False,
)

MicrosoftSQLServerCatalogSourceTypeDef = TypedDict(
    "MicrosoftSQLServerCatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)

MicrosoftSQLServerCatalogTargetTypeDef = TypedDict(
    "MicrosoftSQLServerCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Database": str,
        "Table": str,
    },
)

MongoDBTargetTypeDef = TypedDict(
    "MongoDBTargetTypeDef",
    {
        "ConnectionName": str,
        "Path": str,
        "ScanAll": bool,
    },
    total=False,
)

MySQLCatalogSourceTypeDef = TypedDict(
    "MySQLCatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)

MySQLCatalogTargetTypeDef = TypedDict(
    "MySQLCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Database": str,
        "Table": str,
    },
)

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "Type": NodeTypeType,
        "Name": str,
        "UniqueId": str,
        "TriggerDetails": "TriggerNodeDetailsTypeDef",
        "JobDetails": "JobNodeDetailsTypeDef",
        "CrawlerDetails": "CrawlerNodeDetailsTypeDef",
    },
    total=False,
)

NotificationPropertyTypeDef = TypedDict(
    "NotificationPropertyTypeDef",
    {
        "NotifyDelayAfter": int,
    },
    total=False,
)

NullCheckBoxListTypeDef = TypedDict(
    "NullCheckBoxListTypeDef",
    {
        "IsEmpty": bool,
        "IsNullString": bool,
        "IsNegOne": bool,
    },
    total=False,
)

NullValueFieldTypeDef = TypedDict(
    "NullValueFieldTypeDef",
    {
        "Value": str,
        "Datatype": "DatatypeTypeDef",
    },
)

OracleSQLCatalogSourceTypeDef = TypedDict(
    "OracleSQLCatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)

OracleSQLCatalogTargetTypeDef = TypedDict(
    "OracleSQLCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Database": str,
        "Table": str,
    },
)

OrderTypeDef = TypedDict(
    "OrderTypeDef",
    {
        "Column": str,
        "SortOrder": int,
    },
)

OtherMetadataValueListItemTypeDef = TypedDict(
    "OtherMetadataValueListItemTypeDef",
    {
        "MetadataValue": str,
        "CreatedTime": str,
    },
    total=False,
)

_RequiredPIIDetectionTypeDef = TypedDict(
    "_RequiredPIIDetectionTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "PiiType": PiiTypeType,
        "EntityTypesToDetect": List[str],
    },
)
_OptionalPIIDetectionTypeDef = TypedDict(
    "_OptionalPIIDetectionTypeDef",
    {
        "OutputColumnName": str,
        "SampleFraction": float,
        "ThresholdFraction": float,
        "MaskValue": str,
    },
    total=False,
)

class PIIDetectionTypeDef(_RequiredPIIDetectionTypeDef, _OptionalPIIDetectionTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PartitionErrorTypeDef = TypedDict(
    "PartitionErrorTypeDef",
    {
        "PartitionValues": List[str],
        "ErrorDetail": "ErrorDetailTypeDef",
    },
    total=False,
)

_RequiredPartitionIndexDescriptorTypeDef = TypedDict(
    "_RequiredPartitionIndexDescriptorTypeDef",
    {
        "IndexName": str,
        "Keys": List["KeySchemaElementTypeDef"],
        "IndexStatus": PartitionIndexStatusType,
    },
)
_OptionalPartitionIndexDescriptorTypeDef = TypedDict(
    "_OptionalPartitionIndexDescriptorTypeDef",
    {
        "BackfillErrors": List["BackfillErrorTypeDef"],
    },
    total=False,
)

class PartitionIndexDescriptorTypeDef(
    _RequiredPartitionIndexDescriptorTypeDef, _OptionalPartitionIndexDescriptorTypeDef
):
    pass

PartitionIndexTypeDef = TypedDict(
    "PartitionIndexTypeDef",
    {
        "Keys": List[str],
        "IndexName": str,
    },
)

PartitionInputTypeDef = TypedDict(
    "PartitionInputTypeDef",
    {
        "Values": List[str],
        "LastAccessTime": Union[datetime, str],
        "StorageDescriptor": "StorageDescriptorTypeDef",
        "Parameters": Dict[str, str],
        "LastAnalyzedTime": Union[datetime, str],
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

PartitionValueListTypeDef = TypedDict(
    "PartitionValueListTypeDef",
    {
        "Values": List[str],
    },
)

PhysicalConnectionRequirementsTypeDef = TypedDict(
    "PhysicalConnectionRequirementsTypeDef",
    {
        "SubnetId": str,
        "SecurityGroupIdList": List[str],
        "AvailabilityZone": str,
    },
    total=False,
)

PostgreSQLCatalogSourceTypeDef = TypedDict(
    "PostgreSQLCatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)

PostgreSQLCatalogTargetTypeDef = TypedDict(
    "PostgreSQLCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Database": str,
        "Table": str,
    },
)

PredecessorTypeDef = TypedDict(
    "PredecessorTypeDef",
    {
        "JobName": str,
        "RunId": str,
    },
    total=False,
)

PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {
        "Logical": LogicalType,
        "Conditions": List["ConditionTypeDef"],
    },
    total=False,
)

PrincipalPermissionsTypeDef = TypedDict(
    "PrincipalPermissionsTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Permissions": List[PermissionType],
    },
    total=False,
)

PropertyPredicateTypeDef = TypedDict(
    "PropertyPredicateTypeDef",
    {
        "Key": str,
        "Value": str,
        "Comparator": ComparatorType,
    },
    total=False,
)

_RequiredPutDataCatalogEncryptionSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredPutDataCatalogEncryptionSettingsRequestRequestTypeDef",
    {
        "DataCatalogEncryptionSettings": "DataCatalogEncryptionSettingsTypeDef",
    },
)
_OptionalPutDataCatalogEncryptionSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalPutDataCatalogEncryptionSettingsRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class PutDataCatalogEncryptionSettingsRequestRequestTypeDef(
    _RequiredPutDataCatalogEncryptionSettingsRequestRequestTypeDef,
    _OptionalPutDataCatalogEncryptionSettingsRequestRequestTypeDef,
):
    pass

_RequiredPutResourcePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutResourcePolicyRequestRequestTypeDef",
    {
        "PolicyInJson": str,
    },
)
_OptionalPutResourcePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "PolicyHashCondition": str,
        "PolicyExistsCondition": ExistConditionType,
        "EnableHybrid": EnableHybridValuesType,
    },
    total=False,
)

class PutResourcePolicyRequestRequestTypeDef(
    _RequiredPutResourcePolicyRequestRequestTypeDef, _OptionalPutResourcePolicyRequestRequestTypeDef
):
    pass

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "PolicyHash": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutSchemaVersionMetadataInputRequestTypeDef = TypedDict(
    "_RequiredPutSchemaVersionMetadataInputRequestTypeDef",
    {
        "MetadataKeyValue": "MetadataKeyValuePairTypeDef",
    },
)
_OptionalPutSchemaVersionMetadataInputRequestTypeDef = TypedDict(
    "_OptionalPutSchemaVersionMetadataInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaVersionNumber": "SchemaVersionNumberTypeDef",
        "SchemaVersionId": str,
    },
    total=False,
)

class PutSchemaVersionMetadataInputRequestTypeDef(
    _RequiredPutSchemaVersionMetadataInputRequestTypeDef,
    _OptionalPutSchemaVersionMetadataInputRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutWorkflowRunPropertiesRequestRequestTypeDef = TypedDict(
    "PutWorkflowRunPropertiesRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
        "RunProperties": Dict[str, str],
    },
)

QuerySchemaVersionMetadataInputRequestTypeDef = TypedDict(
    "QuerySchemaVersionMetadataInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaVersionNumber": "SchemaVersionNumberTypeDef",
        "SchemaVersionId": str,
        "MetadataList": List["MetadataKeyValuePairTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

QuerySchemaVersionMetadataResponseTypeDef = TypedDict(
    "QuerySchemaVersionMetadataResponseTypeDef",
    {
        "MetadataInfoMap": Dict[str, "MetadataInfoTypeDef"],
        "SchemaVersionId": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecrawlPolicyTypeDef = TypedDict(
    "RecrawlPolicyTypeDef",
    {
        "RecrawlBehavior": RecrawlBehaviorType,
    },
    total=False,
)

_RequiredRedshiftSourceTypeDef = TypedDict(
    "_RequiredRedshiftSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)
_OptionalRedshiftSourceTypeDef = TypedDict(
    "_OptionalRedshiftSourceTypeDef",
    {
        "RedshiftTmpDir": str,
        "TmpDirIAMRole": str,
    },
    total=False,
)

class RedshiftSourceTypeDef(_RequiredRedshiftSourceTypeDef, _OptionalRedshiftSourceTypeDef):
    pass

_RequiredRedshiftTargetTypeDef = TypedDict(
    "_RequiredRedshiftTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Database": str,
        "Table": str,
    },
)
_OptionalRedshiftTargetTypeDef = TypedDict(
    "_OptionalRedshiftTargetTypeDef",
    {
        "RedshiftTmpDir": str,
        "TmpDirIAMRole": str,
        "UpsertRedshiftOptions": "UpsertRedshiftTargetOptionsTypeDef",
    },
    total=False,
)

class RedshiftTargetTypeDef(_RequiredRedshiftTargetTypeDef, _OptionalRedshiftTargetTypeDef):
    pass

RegisterSchemaVersionInputRequestTypeDef = TypedDict(
    "RegisterSchemaVersionInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaDefinition": str,
    },
)

RegisterSchemaVersionResponseTypeDef = TypedDict(
    "RegisterSchemaVersionResponseTypeDef",
    {
        "SchemaVersionId": str,
        "VersionNumber": int,
        "Status": SchemaVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegistryIdTypeDef = TypedDict(
    "RegistryIdTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
    },
    total=False,
)

RegistryListItemTypeDef = TypedDict(
    "RegistryListItemTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "Description": str,
        "Status": RegistryStatusType,
        "CreatedTime": str,
        "UpdatedTime": str,
    },
    total=False,
)

RelationalCatalogSourceTypeDef = TypedDict(
    "RelationalCatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)

_RequiredRemoveSchemaVersionMetadataInputRequestTypeDef = TypedDict(
    "_RequiredRemoveSchemaVersionMetadataInputRequestTypeDef",
    {
        "MetadataKeyValue": "MetadataKeyValuePairTypeDef",
    },
)
_OptionalRemoveSchemaVersionMetadataInputRequestTypeDef = TypedDict(
    "_OptionalRemoveSchemaVersionMetadataInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaVersionNumber": "SchemaVersionNumberTypeDef",
        "SchemaVersionId": str,
    },
    total=False,
)

class RemoveSchemaVersionMetadataInputRequestTypeDef(
    _RequiredRemoveSchemaVersionMetadataInputRequestTypeDef,
    _OptionalRemoveSchemaVersionMetadataInputRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RenameFieldTypeDef = TypedDict(
    "RenameFieldTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "SourcePath": List[str],
        "TargetPath": List[str],
    },
)

_RequiredResetJobBookmarkRequestRequestTypeDef = TypedDict(
    "_RequiredResetJobBookmarkRequestRequestTypeDef",
    {
        "JobName": str,
    },
)
_OptionalResetJobBookmarkRequestRequestTypeDef = TypedDict(
    "_OptionalResetJobBookmarkRequestRequestTypeDef",
    {
        "RunId": str,
    },
    total=False,
)

class ResetJobBookmarkRequestRequestTypeDef(
    _RequiredResetJobBookmarkRequestRequestTypeDef, _OptionalResetJobBookmarkRequestRequestTypeDef
):
    pass

ResetJobBookmarkResponseTypeDef = TypedDict(
    "ResetJobBookmarkResponseTypeDef",
    {
        "JobBookmarkEntry": "JobBookmarkEntryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceUriTypeDef = TypedDict(
    "ResourceUriTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Uri": str,
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

ResumeWorkflowRunRequestRequestTypeDef = TypedDict(
    "ResumeWorkflowRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
        "NodeIds": List[str],
    },
)

ResumeWorkflowRunResponseTypeDef = TypedDict(
    "ResumeWorkflowRunResponseTypeDef",
    {
        "RunId": str,
        "NodeIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRunStatementRequestRequestTypeDef = TypedDict(
    "_RequiredRunStatementRequestRequestTypeDef",
    {
        "SessionId": str,
        "Code": str,
    },
)
_OptionalRunStatementRequestRequestTypeDef = TypedDict(
    "_OptionalRunStatementRequestRequestTypeDef",
    {
        "RequestOrigin": str,
    },
    total=False,
)

class RunStatementRequestRequestTypeDef(
    _RequiredRunStatementRequestRequestTypeDef, _OptionalRunStatementRequestRequestTypeDef
):
    pass

RunStatementResponseTypeDef = TypedDict(
    "RunStatementResponseTypeDef",
    {
        "Id": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredS3CatalogDeltaSourceTypeDef = TypedDict(
    "_RequiredS3CatalogDeltaSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)
_OptionalS3CatalogDeltaSourceTypeDef = TypedDict(
    "_OptionalS3CatalogDeltaSourceTypeDef",
    {
        "AdditionalDeltaOptions": Dict[str, str],
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class S3CatalogDeltaSourceTypeDef(
    _RequiredS3CatalogDeltaSourceTypeDef, _OptionalS3CatalogDeltaSourceTypeDef
):
    pass

_RequiredS3CatalogHudiSourceTypeDef = TypedDict(
    "_RequiredS3CatalogHudiSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)
_OptionalS3CatalogHudiSourceTypeDef = TypedDict(
    "_OptionalS3CatalogHudiSourceTypeDef",
    {
        "AdditionalHudiOptions": Dict[str, str],
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class S3CatalogHudiSourceTypeDef(
    _RequiredS3CatalogHudiSourceTypeDef, _OptionalS3CatalogHudiSourceTypeDef
):
    pass

_RequiredS3CatalogSourceTypeDef = TypedDict(
    "_RequiredS3CatalogSourceTypeDef",
    {
        "Name": str,
        "Database": str,
        "Table": str,
    },
)
_OptionalS3CatalogSourceTypeDef = TypedDict(
    "_OptionalS3CatalogSourceTypeDef",
    {
        "PartitionPredicate": str,
        "AdditionalOptions": "S3SourceAdditionalOptionsTypeDef",
    },
    total=False,
)

class S3CatalogSourceTypeDef(_RequiredS3CatalogSourceTypeDef, _OptionalS3CatalogSourceTypeDef):
    pass

_RequiredS3CatalogTargetTypeDef = TypedDict(
    "_RequiredS3CatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Table": str,
        "Database": str,
    },
)
_OptionalS3CatalogTargetTypeDef = TypedDict(
    "_OptionalS3CatalogTargetTypeDef",
    {
        "PartitionKeys": List[List[str]],
        "SchemaChangePolicy": "CatalogSchemaChangePolicyTypeDef",
    },
    total=False,
)

class S3CatalogTargetTypeDef(_RequiredS3CatalogTargetTypeDef, _OptionalS3CatalogTargetTypeDef):
    pass

_RequiredS3CsvSourceTypeDef = TypedDict(
    "_RequiredS3CsvSourceTypeDef",
    {
        "Name": str,
        "Paths": List[str],
        "Separator": SeparatorType,
        "QuoteChar": QuoteCharType,
    },
)
_OptionalS3CsvSourceTypeDef = TypedDict(
    "_OptionalS3CsvSourceTypeDef",
    {
        "CompressionType": CompressionTypeType,
        "Exclusions": List[str],
        "GroupSize": str,
        "GroupFiles": str,
        "Recurse": bool,
        "MaxBand": int,
        "MaxFilesInBand": int,
        "AdditionalOptions": "S3DirectSourceAdditionalOptionsTypeDef",
        "Escaper": str,
        "Multiline": bool,
        "WithHeader": bool,
        "WriteHeader": bool,
        "SkipFirst": bool,
        "OptimizePerformance": bool,
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class S3CsvSourceTypeDef(_RequiredS3CsvSourceTypeDef, _OptionalS3CsvSourceTypeDef):
    pass

_RequiredS3DeltaCatalogTargetTypeDef = TypedDict(
    "_RequiredS3DeltaCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Table": str,
        "Database": str,
    },
)
_OptionalS3DeltaCatalogTargetTypeDef = TypedDict(
    "_OptionalS3DeltaCatalogTargetTypeDef",
    {
        "PartitionKeys": List[List[str]],
        "AdditionalOptions": Dict[str, str],
        "SchemaChangePolicy": "CatalogSchemaChangePolicyTypeDef",
    },
    total=False,
)

class S3DeltaCatalogTargetTypeDef(
    _RequiredS3DeltaCatalogTargetTypeDef, _OptionalS3DeltaCatalogTargetTypeDef
):
    pass

_RequiredS3DeltaDirectTargetTypeDef = TypedDict(
    "_RequiredS3DeltaDirectTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Path": str,
        "Compression": DeltaTargetCompressionTypeType,
        "Format": TargetFormatType,
    },
)
_OptionalS3DeltaDirectTargetTypeDef = TypedDict(
    "_OptionalS3DeltaDirectTargetTypeDef",
    {
        "PartitionKeys": List[List[str]],
        "AdditionalOptions": Dict[str, str],
        "SchemaChangePolicy": "DirectSchemaChangePolicyTypeDef",
    },
    total=False,
)

class S3DeltaDirectTargetTypeDef(
    _RequiredS3DeltaDirectTargetTypeDef, _OptionalS3DeltaDirectTargetTypeDef
):
    pass

_RequiredS3DeltaSourceTypeDef = TypedDict(
    "_RequiredS3DeltaSourceTypeDef",
    {
        "Name": str,
        "Paths": List[str],
    },
)
_OptionalS3DeltaSourceTypeDef = TypedDict(
    "_OptionalS3DeltaSourceTypeDef",
    {
        "AdditionalDeltaOptions": Dict[str, str],
        "AdditionalOptions": "S3DirectSourceAdditionalOptionsTypeDef",
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class S3DeltaSourceTypeDef(_RequiredS3DeltaSourceTypeDef, _OptionalS3DeltaSourceTypeDef):
    pass

S3DirectSourceAdditionalOptionsTypeDef = TypedDict(
    "S3DirectSourceAdditionalOptionsTypeDef",
    {
        "BoundedSize": int,
        "BoundedFiles": int,
        "EnableSamplePath": bool,
        "SamplePath": str,
    },
    total=False,
)

_RequiredS3DirectTargetTypeDef = TypedDict(
    "_RequiredS3DirectTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Path": str,
        "Format": TargetFormatType,
    },
)
_OptionalS3DirectTargetTypeDef = TypedDict(
    "_OptionalS3DirectTargetTypeDef",
    {
        "PartitionKeys": List[List[str]],
        "Compression": str,
        "SchemaChangePolicy": "DirectSchemaChangePolicyTypeDef",
    },
    total=False,
)

class S3DirectTargetTypeDef(_RequiredS3DirectTargetTypeDef, _OptionalS3DirectTargetTypeDef):
    pass

S3EncryptionTypeDef = TypedDict(
    "S3EncryptionTypeDef",
    {
        "S3EncryptionMode": S3EncryptionModeType,
        "KmsKeyArn": str,
    },
    total=False,
)

_RequiredS3GlueParquetTargetTypeDef = TypedDict(
    "_RequiredS3GlueParquetTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Path": str,
    },
)
_OptionalS3GlueParquetTargetTypeDef = TypedDict(
    "_OptionalS3GlueParquetTargetTypeDef",
    {
        "PartitionKeys": List[List[str]],
        "Compression": ParquetCompressionTypeType,
        "SchemaChangePolicy": "DirectSchemaChangePolicyTypeDef",
    },
    total=False,
)

class S3GlueParquetTargetTypeDef(
    _RequiredS3GlueParquetTargetTypeDef, _OptionalS3GlueParquetTargetTypeDef
):
    pass

_RequiredS3HudiCatalogTargetTypeDef = TypedDict(
    "_RequiredS3HudiCatalogTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Table": str,
        "Database": str,
        "AdditionalOptions": Dict[str, str],
    },
)
_OptionalS3HudiCatalogTargetTypeDef = TypedDict(
    "_OptionalS3HudiCatalogTargetTypeDef",
    {
        "PartitionKeys": List[List[str]],
        "SchemaChangePolicy": "CatalogSchemaChangePolicyTypeDef",
    },
    total=False,
)

class S3HudiCatalogTargetTypeDef(
    _RequiredS3HudiCatalogTargetTypeDef, _OptionalS3HudiCatalogTargetTypeDef
):
    pass

_RequiredS3HudiDirectTargetTypeDef = TypedDict(
    "_RequiredS3HudiDirectTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Path": str,
        "Compression": HudiTargetCompressionTypeType,
        "Format": TargetFormatType,
        "AdditionalOptions": Dict[str, str],
    },
)
_OptionalS3HudiDirectTargetTypeDef = TypedDict(
    "_OptionalS3HudiDirectTargetTypeDef",
    {
        "PartitionKeys": List[List[str]],
        "SchemaChangePolicy": "DirectSchemaChangePolicyTypeDef",
    },
    total=False,
)

class S3HudiDirectTargetTypeDef(
    _RequiredS3HudiDirectTargetTypeDef, _OptionalS3HudiDirectTargetTypeDef
):
    pass

_RequiredS3HudiSourceTypeDef = TypedDict(
    "_RequiredS3HudiSourceTypeDef",
    {
        "Name": str,
        "Paths": List[str],
    },
)
_OptionalS3HudiSourceTypeDef = TypedDict(
    "_OptionalS3HudiSourceTypeDef",
    {
        "AdditionalHudiOptions": Dict[str, str],
        "AdditionalOptions": "S3DirectSourceAdditionalOptionsTypeDef",
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class S3HudiSourceTypeDef(_RequiredS3HudiSourceTypeDef, _OptionalS3HudiSourceTypeDef):
    pass

_RequiredS3JsonSourceTypeDef = TypedDict(
    "_RequiredS3JsonSourceTypeDef",
    {
        "Name": str,
        "Paths": List[str],
    },
)
_OptionalS3JsonSourceTypeDef = TypedDict(
    "_OptionalS3JsonSourceTypeDef",
    {
        "CompressionType": CompressionTypeType,
        "Exclusions": List[str],
        "GroupSize": str,
        "GroupFiles": str,
        "Recurse": bool,
        "MaxBand": int,
        "MaxFilesInBand": int,
        "AdditionalOptions": "S3DirectSourceAdditionalOptionsTypeDef",
        "JsonPath": str,
        "Multiline": bool,
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class S3JsonSourceTypeDef(_RequiredS3JsonSourceTypeDef, _OptionalS3JsonSourceTypeDef):
    pass

_RequiredS3ParquetSourceTypeDef = TypedDict(
    "_RequiredS3ParquetSourceTypeDef",
    {
        "Name": str,
        "Paths": List[str],
    },
)
_OptionalS3ParquetSourceTypeDef = TypedDict(
    "_OptionalS3ParquetSourceTypeDef",
    {
        "CompressionType": ParquetCompressionTypeType,
        "Exclusions": List[str],
        "GroupSize": str,
        "GroupFiles": str,
        "Recurse": bool,
        "MaxBand": int,
        "MaxFilesInBand": int,
        "AdditionalOptions": "S3DirectSourceAdditionalOptionsTypeDef",
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class S3ParquetSourceTypeDef(_RequiredS3ParquetSourceTypeDef, _OptionalS3ParquetSourceTypeDef):
    pass

S3SourceAdditionalOptionsTypeDef = TypedDict(
    "S3SourceAdditionalOptionsTypeDef",
    {
        "BoundedSize": int,
        "BoundedFiles": int,
    },
    total=False,
)

S3TargetTypeDef = TypedDict(
    "S3TargetTypeDef",
    {
        "Path": str,
        "Exclusions": List[str],
        "ConnectionName": str,
        "SampleSize": int,
        "EventQueueArn": str,
        "DlqEventQueueArn": str,
    },
    total=False,
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "ScheduleExpression": str,
        "State": ScheduleStateType,
    },
    total=False,
)

SchemaChangePolicyTypeDef = TypedDict(
    "SchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": UpdateBehaviorType,
        "DeleteBehavior": DeleteBehaviorType,
    },
    total=False,
)

SchemaColumnTypeDef = TypedDict(
    "SchemaColumnTypeDef",
    {
        "Name": str,
        "DataType": str,
    },
    total=False,
)

SchemaIdTypeDef = TypedDict(
    "SchemaIdTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "RegistryName": str,
    },
    total=False,
)

SchemaListItemTypeDef = TypedDict(
    "SchemaListItemTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "SchemaArn": str,
        "Description": str,
        "SchemaStatus": SchemaStatusType,
        "CreatedTime": str,
        "UpdatedTime": str,
    },
    total=False,
)

SchemaReferenceTypeDef = TypedDict(
    "SchemaReferenceTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaVersionId": str,
        "SchemaVersionNumber": int,
    },
    total=False,
)

SchemaVersionErrorItemTypeDef = TypedDict(
    "SchemaVersionErrorItemTypeDef",
    {
        "VersionNumber": int,
        "ErrorDetails": "ErrorDetailsTypeDef",
    },
    total=False,
)

SchemaVersionListItemTypeDef = TypedDict(
    "SchemaVersionListItemTypeDef",
    {
        "SchemaArn": str,
        "SchemaVersionId": str,
        "VersionNumber": int,
        "Status": SchemaVersionStatusType,
        "CreatedTime": str,
    },
    total=False,
)

SchemaVersionNumberTypeDef = TypedDict(
    "SchemaVersionNumberTypeDef",
    {
        "LatestVersion": bool,
        "VersionNumber": int,
    },
    total=False,
)

SearchTablesRequestRequestTypeDef = TypedDict(
    "SearchTablesRequestRequestTypeDef",
    {
        "CatalogId": str,
        "NextToken": str,
        "Filters": List["PropertyPredicateTypeDef"],
        "SearchText": str,
        "SortCriteria": List["SortCriterionTypeDef"],
        "MaxResults": int,
        "ResourceShareType": ResourceShareTypeType,
    },
    total=False,
)

SearchTablesResponseTypeDef = TypedDict(
    "SearchTablesResponseTypeDef",
    {
        "NextToken": str,
        "TableList": List["TableTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

SegmentTypeDef = TypedDict(
    "SegmentTypeDef",
    {
        "SegmentNumber": int,
        "TotalSegments": int,
    },
)

SelectFieldsTypeDef = TypedDict(
    "SelectFieldsTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Paths": List[List[str]],
    },
)

SelectFromCollectionTypeDef = TypedDict(
    "SelectFromCollectionTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Index": int,
    },
)

SerDeInfoTypeDef = TypedDict(
    "SerDeInfoTypeDef",
    {
        "Name": str,
        "SerializationLibrary": str,
        "Parameters": Dict[str, str],
    },
    total=False,
)

SessionCommandTypeDef = TypedDict(
    "SessionCommandTypeDef",
    {
        "Name": str,
        "PythonVersion": str,
    },
    total=False,
)

SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "Id": str,
        "CreatedOn": datetime,
        "Status": SessionStatusType,
        "ErrorMessage": str,
        "Description": str,
        "Role": str,
        "Command": "SessionCommandTypeDef",
        "DefaultArguments": Dict[str, str],
        "Connections": "ConnectionsListTypeDef",
        "Progress": float,
        "MaxCapacity": float,
        "SecurityConfiguration": str,
        "GlueVersion": str,
    },
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

SortCriterionTypeDef = TypedDict(
    "SortCriterionTypeDef",
    {
        "FieldName": str,
        "Sort": SortType,
    },
    total=False,
)

SourceControlDetailsTypeDef = TypedDict(
    "SourceControlDetailsTypeDef",
    {
        "Provider": SourceControlProviderType,
        "Repository": str,
        "Owner": str,
        "Branch": str,
        "Folder": str,
        "LastCommitId": str,
        "AuthStrategy": SourceControlAuthStrategyType,
        "AuthToken": str,
    },
    total=False,
)

_RequiredSparkConnectorSourceTypeDef = TypedDict(
    "_RequiredSparkConnectorSourceTypeDef",
    {
        "Name": str,
        "ConnectionName": str,
        "ConnectorName": str,
        "ConnectionType": str,
    },
)
_OptionalSparkConnectorSourceTypeDef = TypedDict(
    "_OptionalSparkConnectorSourceTypeDef",
    {
        "AdditionalOptions": Dict[str, str],
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class SparkConnectorSourceTypeDef(
    _RequiredSparkConnectorSourceTypeDef, _OptionalSparkConnectorSourceTypeDef
):
    pass

_RequiredSparkConnectorTargetTypeDef = TypedDict(
    "_RequiredSparkConnectorTargetTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "ConnectionName": str,
        "ConnectorName": str,
        "ConnectionType": str,
    },
)
_OptionalSparkConnectorTargetTypeDef = TypedDict(
    "_OptionalSparkConnectorTargetTypeDef",
    {
        "AdditionalOptions": Dict[str, str],
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class SparkConnectorTargetTypeDef(
    _RequiredSparkConnectorTargetTypeDef, _OptionalSparkConnectorTargetTypeDef
):
    pass

_RequiredSparkSQLTypeDef = TypedDict(
    "_RequiredSparkSQLTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "SqlQuery": str,
        "SqlAliases": List["SqlAliasTypeDef"],
    },
)
_OptionalSparkSQLTypeDef = TypedDict(
    "_OptionalSparkSQLTypeDef",
    {
        "OutputSchemas": List["GlueSchemaTypeDef"],
    },
    total=False,
)

class SparkSQLTypeDef(_RequiredSparkSQLTypeDef, _OptionalSparkSQLTypeDef):
    pass

_RequiredSpigotTypeDef = TypedDict(
    "_RequiredSpigotTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Path": str,
    },
)
_OptionalSpigotTypeDef = TypedDict(
    "_OptionalSpigotTypeDef",
    {
        "Topk": int,
        "Prob": float,
    },
    total=False,
)

class SpigotTypeDef(_RequiredSpigotTypeDef, _OptionalSpigotTypeDef):
    pass

SplitFieldsTypeDef = TypedDict(
    "SplitFieldsTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Paths": List[List[str]],
    },
)

SqlAliasTypeDef = TypedDict(
    "SqlAliasTypeDef",
    {
        "From": str,
        "Alias": str,
    },
)

_RequiredStartBlueprintRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartBlueprintRunRequestRequestTypeDef",
    {
        "BlueprintName": str,
        "RoleArn": str,
    },
)
_OptionalStartBlueprintRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartBlueprintRunRequestRequestTypeDef",
    {
        "Parameters": str,
    },
    total=False,
)

class StartBlueprintRunRequestRequestTypeDef(
    _RequiredStartBlueprintRunRequestRequestTypeDef, _OptionalStartBlueprintRunRequestRequestTypeDef
):
    pass

StartBlueprintRunResponseTypeDef = TypedDict(
    "StartBlueprintRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartCrawlerRequestRequestTypeDef = TypedDict(
    "StartCrawlerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartCrawlerScheduleRequestRequestTypeDef = TypedDict(
    "StartCrawlerScheduleRequestRequestTypeDef",
    {
        "CrawlerName": str,
    },
)

_RequiredStartDataQualityRuleRecommendationRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartDataQualityRuleRecommendationRunRequestRequestTypeDef",
    {
        "DataSource": "DataSourceTypeDef",
        "Role": str,
    },
)
_OptionalStartDataQualityRuleRecommendationRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartDataQualityRuleRecommendationRunRequestRequestTypeDef",
    {
        "NumberOfWorkers": int,
        "Timeout": int,
        "CreatedRulesetName": str,
        "ClientToken": str,
    },
    total=False,
)

class StartDataQualityRuleRecommendationRunRequestRequestTypeDef(
    _RequiredStartDataQualityRuleRecommendationRunRequestRequestTypeDef,
    _OptionalStartDataQualityRuleRecommendationRunRequestRequestTypeDef,
):
    pass

StartDataQualityRuleRecommendationRunResponseTypeDef = TypedDict(
    "StartDataQualityRuleRecommendationRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartDataQualityRulesetEvaluationRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartDataQualityRulesetEvaluationRunRequestRequestTypeDef",
    {
        "DataSource": "DataSourceTypeDef",
        "Role": str,
        "RulesetNames": List[str],
    },
)
_OptionalStartDataQualityRulesetEvaluationRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartDataQualityRulesetEvaluationRunRequestRequestTypeDef",
    {
        "NumberOfWorkers": int,
        "Timeout": int,
        "ClientToken": str,
        "AdditionalRunOptions": "DataQualityEvaluationRunAdditionalRunOptionsTypeDef",
    },
    total=False,
)

class StartDataQualityRulesetEvaluationRunRequestRequestTypeDef(
    _RequiredStartDataQualityRulesetEvaluationRunRequestRequestTypeDef,
    _OptionalStartDataQualityRulesetEvaluationRunRequestRequestTypeDef,
):
    pass

StartDataQualityRulesetEvaluationRunResponseTypeDef = TypedDict(
    "StartDataQualityRulesetEvaluationRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartExportLabelsTaskRunRequestRequestTypeDef = TypedDict(
    "StartExportLabelsTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
        "OutputS3Path": str,
    },
)

StartExportLabelsTaskRunResponseTypeDef = TypedDict(
    "StartExportLabelsTaskRunResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartImportLabelsTaskRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartImportLabelsTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
        "InputS3Path": str,
    },
)
_OptionalStartImportLabelsTaskRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartImportLabelsTaskRunRequestRequestTypeDef",
    {
        "ReplaceAllLabels": bool,
    },
    total=False,
)

class StartImportLabelsTaskRunRequestRequestTypeDef(
    _RequiredStartImportLabelsTaskRunRequestRequestTypeDef,
    _OptionalStartImportLabelsTaskRunRequestRequestTypeDef,
):
    pass

StartImportLabelsTaskRunResponseTypeDef = TypedDict(
    "StartImportLabelsTaskRunResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartJobRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartJobRunRequestRequestTypeDef",
    {
        "JobName": str,
    },
)
_OptionalStartJobRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartJobRunRequestRequestTypeDef",
    {
        "JobRunId": str,
        "Arguments": Dict[str, str],
        "AllocatedCapacity": int,
        "Timeout": int,
        "MaxCapacity": float,
        "SecurityConfiguration": str,
        "NotificationProperty": "NotificationPropertyTypeDef",
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "ExecutionClass": ExecutionClassType,
    },
    total=False,
)

class StartJobRunRequestRequestTypeDef(
    _RequiredStartJobRunRequestRequestTypeDef, _OptionalStartJobRunRequestRequestTypeDef
):
    pass

StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "JobRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMLEvaluationTaskRunRequestRequestTypeDef = TypedDict(
    "StartMLEvaluationTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
    },
)

StartMLEvaluationTaskRunResponseTypeDef = TypedDict(
    "StartMLEvaluationTaskRunResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMLLabelingSetGenerationTaskRunRequestRequestTypeDef = TypedDict(
    "StartMLLabelingSetGenerationTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
        "OutputS3Path": str,
    },
)

StartMLLabelingSetGenerationTaskRunResponseTypeDef = TypedDict(
    "StartMLLabelingSetGenerationTaskRunResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartTriggerRequestRequestTypeDef = TypedDict(
    "StartTriggerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartTriggerResponseTypeDef = TypedDict(
    "StartTriggerResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartWorkflowRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartWorkflowRunRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalStartWorkflowRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartWorkflowRunRequestRequestTypeDef",
    {
        "RunProperties": Dict[str, str],
    },
    total=False,
)

class StartWorkflowRunRequestRequestTypeDef(
    _RequiredStartWorkflowRunRequestRequestTypeDef, _OptionalStartWorkflowRunRequestRequestTypeDef
):
    pass

StartWorkflowRunResponseTypeDef = TypedDict(
    "StartWorkflowRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartingEventBatchConditionTypeDef = TypedDict(
    "StartingEventBatchConditionTypeDef",
    {
        "BatchSize": int,
        "BatchWindow": int,
    },
    total=False,
)

StatementOutputDataTypeDef = TypedDict(
    "StatementOutputDataTypeDef",
    {
        "TextPlain": str,
    },
    total=False,
)

StatementOutputTypeDef = TypedDict(
    "StatementOutputTypeDef",
    {
        "Data": "StatementOutputDataTypeDef",
        "ExecutionCount": int,
        "Status": StatementStateType,
        "ErrorName": str,
        "ErrorValue": str,
        "Traceback": List[str],
    },
    total=False,
)

StatementTypeDef = TypedDict(
    "StatementTypeDef",
    {
        "Id": int,
        "Code": str,
        "State": StatementStateType,
        "Output": "StatementOutputTypeDef",
        "Progress": float,
        "StartedOn": int,
        "CompletedOn": int,
    },
    total=False,
)

StopCrawlerRequestRequestTypeDef = TypedDict(
    "StopCrawlerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StopCrawlerScheduleRequestRequestTypeDef = TypedDict(
    "StopCrawlerScheduleRequestRequestTypeDef",
    {
        "CrawlerName": str,
    },
)

_RequiredStopSessionRequestRequestTypeDef = TypedDict(
    "_RequiredStopSessionRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalStopSessionRequestRequestTypeDef = TypedDict(
    "_OptionalStopSessionRequestRequestTypeDef",
    {
        "RequestOrigin": str,
    },
    total=False,
)

class StopSessionRequestRequestTypeDef(
    _RequiredStopSessionRequestRequestTypeDef, _OptionalStopSessionRequestRequestTypeDef
):
    pass

StopSessionResponseTypeDef = TypedDict(
    "StopSessionResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopTriggerRequestRequestTypeDef = TypedDict(
    "StopTriggerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StopTriggerResponseTypeDef = TypedDict(
    "StopTriggerResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopWorkflowRunRequestRequestTypeDef = TypedDict(
    "StopWorkflowRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)

StorageDescriptorTypeDef = TypedDict(
    "StorageDescriptorTypeDef",
    {
        "Columns": List["ColumnTypeDef"],
        "Location": str,
        "AdditionalLocations": List[str],
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

StreamingDataPreviewOptionsTypeDef = TypedDict(
    "StreamingDataPreviewOptionsTypeDef",
    {
        "PollingTime": int,
        "RecordPollingLimit": int,
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
    "TableErrorTypeDef",
    {
        "TableName": str,
        "ErrorDetail": "ErrorDetailTypeDef",
    },
    total=False,
)

TableIdentifierTypeDef = TypedDict(
    "TableIdentifierTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "Name": str,
    },
    total=False,
)

_RequiredTableInputTypeDef = TypedDict(
    "_RequiredTableInputTypeDef",
    {
        "Name": str,
    },
)
_OptionalTableInputTypeDef = TypedDict(
    "_OptionalTableInputTypeDef",
    {
        "Description": str,
        "Owner": str,
        "LastAccessTime": Union[datetime, str],
        "LastAnalyzedTime": Union[datetime, str],
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

_RequiredTableTypeDef = TypedDict(
    "_RequiredTableTypeDef",
    {
        "Name": str,
    },
)
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
        "VersionId": str,
        "FederatedTable": "FederatedTableTypeDef",
    },
    total=False,
)

class TableTypeDef(_RequiredTableTypeDef, _OptionalTableTypeDef):
    pass

TableVersionErrorTypeDef = TypedDict(
    "TableVersionErrorTypeDef",
    {
        "TableName": str,
        "VersionId": str,
        "ErrorDetail": "ErrorDetailTypeDef",
    },
    total=False,
)

TableVersionTypeDef = TypedDict(
    "TableVersionTypeDef",
    {
        "Table": "TableTypeDef",
        "VersionId": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagsToAdd": Dict[str, str],
    },
)

TaskRunFilterCriteriaTypeDef = TypedDict(
    "TaskRunFilterCriteriaTypeDef",
    {
        "TaskRunType": TaskTypeType,
        "Status": TaskStatusTypeType,
        "StartedBefore": Union[datetime, str],
        "StartedAfter": Union[datetime, str],
    },
    total=False,
)

TaskRunPropertiesTypeDef = TypedDict(
    "TaskRunPropertiesTypeDef",
    {
        "TaskType": TaskTypeType,
        "ImportLabelsTaskRunProperties": "ImportLabelsTaskRunPropertiesTypeDef",
        "ExportLabelsTaskRunProperties": "ExportLabelsTaskRunPropertiesTypeDef",
        "LabelingSetGenerationTaskRunProperties": "LabelingSetGenerationTaskRunPropertiesTypeDef",
        "FindMatchesTaskRunProperties": "FindMatchesTaskRunPropertiesTypeDef",
    },
    total=False,
)

TaskRunSortCriteriaTypeDef = TypedDict(
    "TaskRunSortCriteriaTypeDef",
    {
        "Column": TaskRunSortColumnTypeType,
        "SortDirection": SortDirectionTypeType,
    },
)

TaskRunTypeDef = TypedDict(
    "TaskRunTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": TaskStatusTypeType,
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

_RequiredTransformConfigParameterTypeDef = TypedDict(
    "_RequiredTransformConfigParameterTypeDef",
    {
        "Name": str,
        "Type": ParamTypeType,
    },
)
_OptionalTransformConfigParameterTypeDef = TypedDict(
    "_OptionalTransformConfigParameterTypeDef",
    {
        "ValidationRule": str,
        "ValidationMessage": str,
        "Value": List[str],
        "ListType": ParamTypeType,
        "IsOptional": bool,
    },
    total=False,
)

class TransformConfigParameterTypeDef(
    _RequiredTransformConfigParameterTypeDef, _OptionalTransformConfigParameterTypeDef
):
    pass

TransformEncryptionTypeDef = TypedDict(
    "TransformEncryptionTypeDef",
    {
        "MlUserDataEncryption": "MLUserDataEncryptionTypeDef",
        "TaskRunSecurityConfigurationName": str,
    },
    total=False,
)

TransformFilterCriteriaTypeDef = TypedDict(
    "TransformFilterCriteriaTypeDef",
    {
        "Name": str,
        "TransformType": Literal["FIND_MATCHES"],
        "Status": TransformStatusTypeType,
        "GlueVersion": str,
        "CreatedBefore": Union[datetime, str],
        "CreatedAfter": Union[datetime, str],
        "LastModifiedBefore": Union[datetime, str],
        "LastModifiedAfter": Union[datetime, str],
        "Schema": List["SchemaColumnTypeDef"],
    },
    total=False,
)

_RequiredTransformParametersTypeDef = TypedDict(
    "_RequiredTransformParametersTypeDef",
    {
        "TransformType": Literal["FIND_MATCHES"],
    },
)
_OptionalTransformParametersTypeDef = TypedDict(
    "_OptionalTransformParametersTypeDef",
    {
        "FindMatchesParameters": "FindMatchesParametersTypeDef",
    },
    total=False,
)

class TransformParametersTypeDef(
    _RequiredTransformParametersTypeDef, _OptionalTransformParametersTypeDef
):
    pass

TransformSortCriteriaTypeDef = TypedDict(
    "TransformSortCriteriaTypeDef",
    {
        "Column": TransformSortColumnTypeType,
        "SortDirection": SortDirectionTypeType,
    },
)

TriggerNodeDetailsTypeDef = TypedDict(
    "TriggerNodeDetailsTypeDef",
    {
        "Trigger": "TriggerTypeDef",
    },
    total=False,
)

TriggerTypeDef = TypedDict(
    "TriggerTypeDef",
    {
        "Name": str,
        "WorkflowName": str,
        "Id": str,
        "Type": TriggerTypeType,
        "State": TriggerStateType,
        "Description": str,
        "Schedule": str,
        "Actions": List["ActionTypeDef"],
        "Predicate": "PredicateTypeDef",
        "EventBatchingCondition": "EventBatchingConditionTypeDef",
    },
    total=False,
)

TriggerUpdateTypeDef = TypedDict(
    "TriggerUpdateTypeDef",
    {
        "Name": str,
        "Description": str,
        "Schedule": str,
        "Actions": List["ActionTypeDef"],
        "Predicate": "PredicateTypeDef",
        "EventBatchingCondition": "EventBatchingConditionTypeDef",
    },
    total=False,
)

UnfilteredPartitionTypeDef = TypedDict(
    "UnfilteredPartitionTypeDef",
    {
        "Partition": "PartitionTypeDef",
        "AuthorizedColumns": List[str],
        "IsRegisteredWithLakeFormation": bool,
    },
    total=False,
)

UnionTypeDef = TypedDict(
    "UnionTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "UnionType": UnionTypeType,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagsToRemove": List[str],
    },
)

_RequiredUpdateBlueprintRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBlueprintRequestRequestTypeDef",
    {
        "Name": str,
        "BlueprintLocation": str,
    },
)
_OptionalUpdateBlueprintRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBlueprintRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateBlueprintRequestRequestTypeDef(
    _RequiredUpdateBlueprintRequestRequestTypeDef, _OptionalUpdateBlueprintRequestRequestTypeDef
):
    pass

UpdateBlueprintResponseTypeDef = TypedDict(
    "UpdateBlueprintResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClassifierRequestRequestTypeDef = TypedDict(
    "UpdateClassifierRequestRequestTypeDef",
    {
        "GrokClassifier": "UpdateGrokClassifierRequestTypeDef",
        "XMLClassifier": "UpdateXMLClassifierRequestTypeDef",
        "JsonClassifier": "UpdateJsonClassifierRequestTypeDef",
        "CsvClassifier": "UpdateCsvClassifierRequestTypeDef",
    },
    total=False,
)

_RequiredUpdateColumnStatisticsForPartitionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateColumnStatisticsForPartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": List[str],
        "ColumnStatisticsList": List["ColumnStatisticsTypeDef"],
    },
)
_OptionalUpdateColumnStatisticsForPartitionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateColumnStatisticsForPartitionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class UpdateColumnStatisticsForPartitionRequestRequestTypeDef(
    _RequiredUpdateColumnStatisticsForPartitionRequestRequestTypeDef,
    _OptionalUpdateColumnStatisticsForPartitionRequestRequestTypeDef,
):
    pass

UpdateColumnStatisticsForPartitionResponseTypeDef = TypedDict(
    "UpdateColumnStatisticsForPartitionResponseTypeDef",
    {
        "Errors": List["ColumnStatisticsErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateColumnStatisticsForTableRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateColumnStatisticsForTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "ColumnStatisticsList": List["ColumnStatisticsTypeDef"],
    },
)
_OptionalUpdateColumnStatisticsForTableRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateColumnStatisticsForTableRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class UpdateColumnStatisticsForTableRequestRequestTypeDef(
    _RequiredUpdateColumnStatisticsForTableRequestRequestTypeDef,
    _OptionalUpdateColumnStatisticsForTableRequestRequestTypeDef,
):
    pass

UpdateColumnStatisticsForTableResponseTypeDef = TypedDict(
    "UpdateColumnStatisticsForTableResponseTypeDef",
    {
        "Errors": List["ColumnStatisticsErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectionRequestRequestTypeDef",
    {
        "Name": str,
        "ConnectionInput": "ConnectionInputTypeDef",
    },
)
_OptionalUpdateConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class UpdateConnectionRequestRequestTypeDef(
    _RequiredUpdateConnectionRequestRequestTypeDef, _OptionalUpdateConnectionRequestRequestTypeDef
):
    pass

_RequiredUpdateCrawlerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCrawlerRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateCrawlerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCrawlerRequestRequestTypeDef",
    {
        "Role": str,
        "DatabaseName": str,
        "Description": str,
        "Targets": "CrawlerTargetsTypeDef",
        "Schedule": str,
        "Classifiers": List[str],
        "TablePrefix": str,
        "SchemaChangePolicy": "SchemaChangePolicyTypeDef",
        "RecrawlPolicy": "RecrawlPolicyTypeDef",
        "LineageConfiguration": "LineageConfigurationTypeDef",
        "LakeFormationConfiguration": "LakeFormationConfigurationTypeDef",
        "Configuration": str,
        "CrawlerSecurityConfiguration": str,
    },
    total=False,
)

class UpdateCrawlerRequestRequestTypeDef(
    _RequiredUpdateCrawlerRequestRequestTypeDef, _OptionalUpdateCrawlerRequestRequestTypeDef
):
    pass

_RequiredUpdateCrawlerScheduleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCrawlerScheduleRequestRequestTypeDef",
    {
        "CrawlerName": str,
    },
)
_OptionalUpdateCrawlerScheduleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCrawlerScheduleRequestRequestTypeDef",
    {
        "Schedule": str,
    },
    total=False,
)

class UpdateCrawlerScheduleRequestRequestTypeDef(
    _RequiredUpdateCrawlerScheduleRequestRequestTypeDef,
    _OptionalUpdateCrawlerScheduleRequestRequestTypeDef,
):
    pass

_RequiredUpdateCsvClassifierRequestTypeDef = TypedDict(
    "_RequiredUpdateCsvClassifierRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateCsvClassifierRequestTypeDef = TypedDict(
    "_OptionalUpdateCsvClassifierRequestTypeDef",
    {
        "Delimiter": str,
        "QuoteSymbol": str,
        "ContainsHeader": CsvHeaderOptionType,
        "Header": List[str],
        "DisableValueTrimming": bool,
        "AllowSingleColumn": bool,
        "CustomDatatypeConfigured": bool,
        "CustomDatatypes": List[str],
    },
    total=False,
)

class UpdateCsvClassifierRequestTypeDef(
    _RequiredUpdateCsvClassifierRequestTypeDef, _OptionalUpdateCsvClassifierRequestTypeDef
):
    pass

_RequiredUpdateDataQualityRulesetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataQualityRulesetRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateDataQualityRulesetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataQualityRulesetRequestRequestTypeDef",
    {
        "Description": str,
        "Ruleset": str,
    },
    total=False,
)

class UpdateDataQualityRulesetRequestRequestTypeDef(
    _RequiredUpdateDataQualityRulesetRequestRequestTypeDef,
    _OptionalUpdateDataQualityRulesetRequestRequestTypeDef,
):
    pass

UpdateDataQualityRulesetResponseTypeDef = TypedDict(
    "UpdateDataQualityRulesetResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "Ruleset": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDatabaseRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDatabaseRequestRequestTypeDef",
    {
        "Name": str,
        "DatabaseInput": "DatabaseInputTypeDef",
    },
)
_OptionalUpdateDatabaseRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDatabaseRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class UpdateDatabaseRequestRequestTypeDef(
    _RequiredUpdateDatabaseRequestRequestTypeDef, _OptionalUpdateDatabaseRequestRequestTypeDef
):
    pass

_RequiredUpdateDevEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDevEndpointRequestRequestTypeDef",
    {
        "EndpointName": str,
    },
)
_OptionalUpdateDevEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDevEndpointRequestRequestTypeDef",
    {
        "PublicKey": str,
        "AddPublicKeys": List[str],
        "DeletePublicKeys": List[str],
        "CustomLibraries": "DevEndpointCustomLibrariesTypeDef",
        "UpdateEtlLibraries": bool,
        "DeleteArguments": List[str],
        "AddArguments": Dict[str, str],
    },
    total=False,
)

class UpdateDevEndpointRequestRequestTypeDef(
    _RequiredUpdateDevEndpointRequestRequestTypeDef, _OptionalUpdateDevEndpointRequestRequestTypeDef
):
    pass

_RequiredUpdateGrokClassifierRequestTypeDef = TypedDict(
    "_RequiredUpdateGrokClassifierRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateGrokClassifierRequestTypeDef = TypedDict(
    "_OptionalUpdateGrokClassifierRequestTypeDef",
    {
        "Classification": str,
        "GrokPattern": str,
        "CustomPatterns": str,
    },
    total=False,
)

class UpdateGrokClassifierRequestTypeDef(
    _RequiredUpdateGrokClassifierRequestTypeDef, _OptionalUpdateGrokClassifierRequestTypeDef
):
    pass

UpdateJobFromSourceControlRequestRequestTypeDef = TypedDict(
    "UpdateJobFromSourceControlRequestRequestTypeDef",
    {
        "JobName": str,
        "Provider": SourceControlProviderType,
        "RepositoryName": str,
        "RepositoryOwner": str,
        "BranchName": str,
        "Folder": str,
        "CommitId": str,
        "AuthStrategy": SourceControlAuthStrategyType,
        "AuthToken": str,
    },
    total=False,
)

UpdateJobFromSourceControlResponseTypeDef = TypedDict(
    "UpdateJobFromSourceControlResponseTypeDef",
    {
        "JobName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateJobRequestRequestTypeDef = TypedDict(
    "UpdateJobRequestRequestTypeDef",
    {
        "JobName": str,
        "JobUpdate": "JobUpdateTypeDef",
    },
)

UpdateJobResponseTypeDef = TypedDict(
    "UpdateJobResponseTypeDef",
    {
        "JobName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateJsonClassifierRequestTypeDef = TypedDict(
    "_RequiredUpdateJsonClassifierRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateJsonClassifierRequestTypeDef = TypedDict(
    "_OptionalUpdateJsonClassifierRequestTypeDef",
    {
        "JsonPath": str,
    },
    total=False,
)

class UpdateJsonClassifierRequestTypeDef(
    _RequiredUpdateJsonClassifierRequestTypeDef, _OptionalUpdateJsonClassifierRequestTypeDef
):
    pass

_RequiredUpdateMLTransformRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMLTransformRequestRequestTypeDef",
    {
        "TransformId": str,
    },
)
_OptionalUpdateMLTransformRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMLTransformRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Parameters": "TransformParametersTypeDef",
        "Role": str,
        "GlueVersion": str,
        "MaxCapacity": float,
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
    },
    total=False,
)

class UpdateMLTransformRequestRequestTypeDef(
    _RequiredUpdateMLTransformRequestRequestTypeDef, _OptionalUpdateMLTransformRequestRequestTypeDef
):
    pass

UpdateMLTransformResponseTypeDef = TypedDict(
    "UpdateMLTransformResponseTypeDef",
    {
        "TransformId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePartitionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValueList": List[str],
        "PartitionInput": "PartitionInputTypeDef",
    },
)
_OptionalUpdatePartitionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePartitionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class UpdatePartitionRequestRequestTypeDef(
    _RequiredUpdatePartitionRequestRequestTypeDef, _OptionalUpdatePartitionRequestRequestTypeDef
):
    pass

UpdateRegistryInputRequestTypeDef = TypedDict(
    "UpdateRegistryInputRequestTypeDef",
    {
        "RegistryId": "RegistryIdTypeDef",
        "Description": str,
    },
)

UpdateRegistryResponseTypeDef = TypedDict(
    "UpdateRegistryResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSchemaInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSchemaInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
    },
)
_OptionalUpdateSchemaInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSchemaInputRequestTypeDef",
    {
        "SchemaVersionNumber": "SchemaVersionNumberTypeDef",
        "Compatibility": CompatibilityType,
        "Description": str,
    },
    total=False,
)

class UpdateSchemaInputRequestTypeDef(
    _RequiredUpdateSchemaInputRequestTypeDef, _OptionalUpdateSchemaInputRequestTypeDef
):
    pass

UpdateSchemaResponseTypeDef = TypedDict(
    "UpdateSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "RegistryName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSourceControlFromJobRequestRequestTypeDef = TypedDict(
    "UpdateSourceControlFromJobRequestRequestTypeDef",
    {
        "JobName": str,
        "Provider": SourceControlProviderType,
        "RepositoryName": str,
        "RepositoryOwner": str,
        "BranchName": str,
        "Folder": str,
        "CommitId": str,
        "AuthStrategy": SourceControlAuthStrategyType,
        "AuthToken": str,
    },
    total=False,
)

UpdateSourceControlFromJobResponseTypeDef = TypedDict(
    "UpdateSourceControlFromJobResponseTypeDef",
    {
        "JobName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTableRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableInput": "TableInputTypeDef",
    },
)
_OptionalUpdateTableRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTableRequestRequestTypeDef",
    {
        "CatalogId": str,
        "SkipArchive": bool,
        "TransactionId": str,
        "VersionId": str,
    },
    total=False,
)

class UpdateTableRequestRequestTypeDef(
    _RequiredUpdateTableRequestRequestTypeDef, _OptionalUpdateTableRequestRequestTypeDef
):
    pass

UpdateTriggerRequestRequestTypeDef = TypedDict(
    "UpdateTriggerRequestRequestTypeDef",
    {
        "Name": str,
        "TriggerUpdate": "TriggerUpdateTypeDef",
    },
)

UpdateTriggerResponseTypeDef = TypedDict(
    "UpdateTriggerResponseTypeDef",
    {
        "Trigger": "TriggerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserDefinedFunctionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionName": str,
        "FunctionInput": "UserDefinedFunctionInputTypeDef",
    },
)
_OptionalUpdateUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserDefinedFunctionRequestRequestTypeDef",
    {
        "CatalogId": str,
    },
    total=False,
)

class UpdateUserDefinedFunctionRequestRequestTypeDef(
    _RequiredUpdateUserDefinedFunctionRequestRequestTypeDef,
    _OptionalUpdateUserDefinedFunctionRequestRequestTypeDef,
):
    pass

_RequiredUpdateWorkflowRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkflowRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateWorkflowRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkflowRequestRequestTypeDef",
    {
        "Description": str,
        "DefaultRunProperties": Dict[str, str],
        "MaxConcurrentRuns": int,
    },
    total=False,
)

class UpdateWorkflowRequestRequestTypeDef(
    _RequiredUpdateWorkflowRequestRequestTypeDef, _OptionalUpdateWorkflowRequestRequestTypeDef
):
    pass

UpdateWorkflowResponseTypeDef = TypedDict(
    "UpdateWorkflowResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateXMLClassifierRequestTypeDef = TypedDict(
    "_RequiredUpdateXMLClassifierRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateXMLClassifierRequestTypeDef = TypedDict(
    "_OptionalUpdateXMLClassifierRequestTypeDef",
    {
        "Classification": str,
        "RowTag": str,
    },
    total=False,
)

class UpdateXMLClassifierRequestTypeDef(
    _RequiredUpdateXMLClassifierRequestTypeDef, _OptionalUpdateXMLClassifierRequestTypeDef
):
    pass

UpsertRedshiftTargetOptionsTypeDef = TypedDict(
    "UpsertRedshiftTargetOptionsTypeDef",
    {
        "TableLocation": str,
        "ConnectionName": str,
        "UpsertKeys": List[str],
    },
    total=False,
)

UserDefinedFunctionInputTypeDef = TypedDict(
    "UserDefinedFunctionInputTypeDef",
    {
        "FunctionName": str,
        "ClassName": str,
        "OwnerName": str,
        "OwnerType": PrincipalTypeType,
        "ResourceUris": List["ResourceUriTypeDef"],
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
        "OwnerType": PrincipalTypeType,
        "CreateTime": datetime,
        "ResourceUris": List["ResourceUriTypeDef"],
        "CatalogId": str,
    },
    total=False,
)

WorkflowGraphTypeDef = TypedDict(
    "WorkflowGraphTypeDef",
    {
        "Nodes": List["NodeTypeDef"],
        "Edges": List["EdgeTypeDef"],
    },
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
        "ErroredActions": int,
        "WaitingActions": int,
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
        "Status": WorkflowRunStatusType,
        "ErrorMessage": str,
        "Statistics": "WorkflowRunStatisticsTypeDef",
        "Graph": "WorkflowGraphTypeDef",
        "StartingEventBatchCondition": "StartingEventBatchConditionTypeDef",
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
        "BlueprintDetails": "BlueprintDetailsTypeDef",
    },
    total=False,
)

_RequiredXMLClassifierTypeDef = TypedDict(
    "_RequiredXMLClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
    },
)
_OptionalXMLClassifierTypeDef = TypedDict(
    "_OptionalXMLClassifierTypeDef",
    {
        "CreationTime": datetime,
        "LastUpdated": datetime,
        "Version": int,
        "RowTag": str,
    },
    total=False,
)

class XMLClassifierTypeDef(_RequiredXMLClassifierTypeDef, _OptionalXMLClassifierTypeDef):
    pass
