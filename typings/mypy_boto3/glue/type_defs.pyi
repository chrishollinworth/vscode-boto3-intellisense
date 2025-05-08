"""
Type annotations for glue service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_glue.type_defs import NotificationPropertyTypeDef

    data: NotificationPropertyTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AdditionalOptionKeysType,
    AggFunctionType,
    AllowFullTableExternalDataAccessEnumType,
    AuthenticationTypeType,
    BackfillErrorCodeType,
    BlueprintRunStateType,
    BlueprintStatusType,
    CatalogEncryptionModeType,
    CloudWatchEncryptionModeType,
    ColumnStatisticsStateType,
    ColumnStatisticsTypeType,
    ComparatorType,
    CompatibilityType,
    CompressionTypeType,
    ComputationTypeType,
    ComputeEnvironmentType,
    ConnectionPropertyKeyType,
    ConnectionStatusType,
    ConnectionTypeType,
    CrawlerHistoryStateType,
    CrawlerLineageSettingsType,
    CrawlerStateType,
    CrawlStateType,
    CsvHeaderOptionType,
    CsvSerdeOptionType,
    DataFormatType,
    DataOperationType,
    DataQualityEncryptionModeType,
    DataQualityModelStatusType,
    DataQualityRuleResultStatusType,
    DeleteBehaviorType,
    DeltaTargetCompressionTypeType,
    DQCompositeRuleEvaluationMethodType,
    DQStopJobOnFailureTimingType,
    DQTransformOutputType,
    EnableHybridValuesType,
    ExecutionClassType,
    ExecutionStatusType,
    ExistConditionType,
    FieldDataTypeType,
    FieldFilterOperatorType,
    FieldNameType,
    FilterLogicalOperatorType,
    FilterOperationType,
    FilterOperatorType,
    FilterValueTypeType,
    GlueRecordTypeType,
    HudiTargetCompressionTypeType,
    InclusionAnnotationValueType,
    IntegrationStatusType,
    JDBCConnectionTypeType,
    JDBCDataTypeType,
    JdbcMetadataEntryType,
    JobBookmarksEncryptionModeType,
    JobModeType,
    JobRunStateType,
    JoinTypeType,
    LanguageType,
    LastCrawlStatusType,
    LogicalType,
    MLUserDataEncryptionModeStringType,
    NodeTypeType,
    OAuth2GrantTypeType,
    ParamTypeType,
    ParquetCompressionTypeType,
    PartitionIndexStatusType,
    PermissionType,
    PermissionTypeType,
    PiiTypeType,
    PrincipalTypeType,
    PropertyTypeType,
    QuoteCharType,
    RecrawlBehaviorType,
    RegistryStatusType,
    ResourceActionType,
    ResourceShareTypeType,
    ResourceStateType,
    ResourceTypeType,
    S3EncryptionModeType,
    ScheduleStateType,
    ScheduleTypeType,
    SchemaStatusType,
    SchemaVersionStatusType,
    SeparatorType,
    SessionStatusType,
    SettingSourceType,
    SortDirectionTypeType,
    SortType,
    SourceControlAuthStrategyType,
    SourceControlProviderType,
    StartingPositionType,
    StatementStateType,
    StatisticEvaluationLevelType,
    TableAttributesType,
    TableOptimizerEventTypeType,
    TableOptimizerTypeType,
    TargetFormatType,
    TaskRunSortColumnTypeType,
    TaskStatusTypeType,
    TaskTypeType,
    TransformSortColumnTypeType,
    TransformStatusTypeType,
    TriggerStateType,
    TriggerTypeType,
    UnionTypeType,
    UnnestSpecType,
    UpdateBehaviorType,
    UpdateCatalogBehaviorType,
    ViewDialectType,
    ViewUpdateActionType,
    WorkerTypeType,
    WorkflowRunStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ActionOutputTypeDef",
    "ActionTypeDef",
    "ActionUnionTypeDef",
    "AggregateOperationOutputTypeDef",
    "AggregateOperationTypeDef",
    "AggregateOperationUnionTypeDef",
    "AggregateOutputTypeDef",
    "AggregateTypeDef",
    "AggregateUnionTypeDef",
    "AllowedValueTypeDef",
    "AmazonRedshiftAdvancedOptionTypeDef",
    "AmazonRedshiftNodeDataOutputTypeDef",
    "AmazonRedshiftNodeDataTypeDef",
    "AmazonRedshiftNodeDataUnionTypeDef",
    "AmazonRedshiftSourceOutputTypeDef",
    "AmazonRedshiftSourceTypeDef",
    "AmazonRedshiftSourceUnionTypeDef",
    "AmazonRedshiftTargetOutputTypeDef",
    "AmazonRedshiftTargetTypeDef",
    "AmazonRedshiftTargetUnionTypeDef",
    "AnnotationErrorTypeDef",
    "ApplyMappingOutputTypeDef",
    "ApplyMappingPaginatorTypeDef",
    "ApplyMappingTypeDef",
    "ApplyMappingUnionTypeDef",
    "AthenaConnectorSourceOutputTypeDef",
    "AthenaConnectorSourceTypeDef",
    "AthenaConnectorSourceUnionTypeDef",
    "AuditContextTypeDef",
    "AuthConfigurationTypeDef",
    "AuthenticationConfigurationInputTypeDef",
    "AuthenticationConfigurationTypeDef",
    "AuthorizationCodePropertiesTypeDef",
    "BackfillErrorTypeDef",
    "BasicAuthenticationCredentialsTypeDef",
    "BasicCatalogTargetOutputTypeDef",
    "BasicCatalogTargetTypeDef",
    "BasicCatalogTargetUnionTypeDef",
    "BatchCreatePartitionRequestTypeDef",
    "BatchCreatePartitionResponseTypeDef",
    "BatchDeleteConnectionRequestTypeDef",
    "BatchDeleteConnectionResponseTypeDef",
    "BatchDeletePartitionRequestTypeDef",
    "BatchDeletePartitionResponseTypeDef",
    "BatchDeleteTableRequestTypeDef",
    "BatchDeleteTableResponseTypeDef",
    "BatchDeleteTableVersionRequestTypeDef",
    "BatchDeleteTableVersionResponseTypeDef",
    "BatchGetBlueprintsRequestTypeDef",
    "BatchGetBlueprintsResponseTypeDef",
    "BatchGetCrawlersRequestTypeDef",
    "BatchGetCrawlersResponseTypeDef",
    "BatchGetCustomEntityTypesRequestTypeDef",
    "BatchGetCustomEntityTypesResponseTypeDef",
    "BatchGetDataQualityResultRequestTypeDef",
    "BatchGetDataQualityResultResponseTypeDef",
    "BatchGetDevEndpointsRequestTypeDef",
    "BatchGetDevEndpointsResponseTypeDef",
    "BatchGetJobsRequestTypeDef",
    "BatchGetJobsResponseTypeDef",
    "BatchGetPartitionRequestTypeDef",
    "BatchGetPartitionResponseTypeDef",
    "BatchGetTableOptimizerEntryTypeDef",
    "BatchGetTableOptimizerErrorTypeDef",
    "BatchGetTableOptimizerRequestTypeDef",
    "BatchGetTableOptimizerResponseTypeDef",
    "BatchGetTriggersRequestTypeDef",
    "BatchGetTriggersResponseTypeDef",
    "BatchGetWorkflowsRequestTypeDef",
    "BatchGetWorkflowsResponseTypeDef",
    "BatchPutDataQualityStatisticAnnotationRequestTypeDef",
    "BatchPutDataQualityStatisticAnnotationResponseTypeDef",
    "BatchStopJobRunErrorTypeDef",
    "BatchStopJobRunRequestTypeDef",
    "BatchStopJobRunResponseTypeDef",
    "BatchStopJobRunSuccessfulSubmissionTypeDef",
    "BatchTableOptimizerTypeDef",
    "BatchUpdatePartitionFailureEntryTypeDef",
    "BatchUpdatePartitionRequestEntryTypeDef",
    "BatchUpdatePartitionRequestTypeDef",
    "BatchUpdatePartitionResponseTypeDef",
    "BinaryColumnStatisticsDataTypeDef",
    "BlobTypeDef",
    "BlueprintDetailsTypeDef",
    "BlueprintRunTypeDef",
    "BlueprintTypeDef",
    "BooleanColumnStatisticsDataTypeDef",
    "CancelDataQualityRuleRecommendationRunRequestTypeDef",
    "CancelDataQualityRulesetEvaluationRunRequestTypeDef",
    "CancelMLTaskRunRequestTypeDef",
    "CancelMLTaskRunResponseTypeDef",
    "CancelStatementRequestTypeDef",
    "CapabilitiesTypeDef",
    "CatalogDeltaSourceOutputTypeDef",
    "CatalogDeltaSourceTypeDef",
    "CatalogDeltaSourceUnionTypeDef",
    "CatalogEntryTypeDef",
    "CatalogHudiSourceOutputTypeDef",
    "CatalogHudiSourceTypeDef",
    "CatalogHudiSourceUnionTypeDef",
    "CatalogImportStatusTypeDef",
    "CatalogInputTypeDef",
    "CatalogKafkaSourceOutputTypeDef",
    "CatalogKafkaSourceTypeDef",
    "CatalogKafkaSourceUnionTypeDef",
    "CatalogKinesisSourceOutputTypeDef",
    "CatalogKinesisSourceTypeDef",
    "CatalogKinesisSourceUnionTypeDef",
    "CatalogPropertiesOutputTypeDef",
    "CatalogPropertiesTypeDef",
    "CatalogSchemaChangePolicyTypeDef",
    "CatalogSourceTypeDef",
    "CatalogTargetOutputTypeDef",
    "CatalogTargetTypeDef",
    "CatalogTypeDef",
    "CheckSchemaVersionValidityInputTypeDef",
    "CheckSchemaVersionValidityResponseTypeDef",
    "ClassifierTypeDef",
    "CloudWatchEncryptionTypeDef",
    "CodeGenConfigurationNodeOutputTypeDef",
    "CodeGenConfigurationNodePaginatorTypeDef",
    "CodeGenConfigurationNodeTypeDef",
    "CodeGenConfigurationNodeUnionTypeDef",
    "CodeGenEdgeTypeDef",
    "CodeGenNodeArgTypeDef",
    "CodeGenNodeOutputTypeDef",
    "CodeGenNodeTypeDef",
    "CodeGenNodeUnionTypeDef",
    "ColumnErrorTypeDef",
    "ColumnImportanceTypeDef",
    "ColumnOutputTypeDef",
    "ColumnRowFilterTypeDef",
    "ColumnStatisticsDataOutputTypeDef",
    "ColumnStatisticsDataTypeDef",
    "ColumnStatisticsDataUnionTypeDef",
    "ColumnStatisticsErrorTypeDef",
    "ColumnStatisticsOutputTypeDef",
    "ColumnStatisticsTaskRunTypeDef",
    "ColumnStatisticsTaskSettingsTypeDef",
    "ColumnStatisticsTypeDef",
    "ColumnStatisticsUnionTypeDef",
    "ColumnTypeDef",
    "ColumnUnionTypeDef",
    "CompactionMetricsTypeDef",
    "ComputeEnvironmentConfigurationTypeDef",
    "ConditionExpressionTypeDef",
    "ConditionTypeDef",
    "ConfigurationObjectOutputTypeDef",
    "ConfigurationObjectTypeDef",
    "ConfusionMatrixTypeDef",
    "ConnectionInputTypeDef",
    "ConnectionPasswordEncryptionTypeDef",
    "ConnectionTypeBriefTypeDef",
    "ConnectionTypeDef",
    "ConnectionsListOutputTypeDef",
    "ConnectionsListTypeDef",
    "ConnectionsListUnionTypeDef",
    "ConnectorDataSourceOutputTypeDef",
    "ConnectorDataSourceTypeDef",
    "ConnectorDataSourceUnionTypeDef",
    "ConnectorDataTargetOutputTypeDef",
    "ConnectorDataTargetTypeDef",
    "ConnectorDataTargetUnionTypeDef",
    "CrawlTypeDef",
    "CrawlerHistoryTypeDef",
    "CrawlerMetricsTypeDef",
    "CrawlerNodeDetailsTypeDef",
    "CrawlerTargetsOutputTypeDef",
    "CrawlerTargetsTypeDef",
    "CrawlerTargetsUnionTypeDef",
    "CrawlerTypeDef",
    "CrawlsFilterTypeDef",
    "CreateBlueprintRequestTypeDef",
    "CreateBlueprintResponseTypeDef",
    "CreateCatalogRequestTypeDef",
    "CreateClassifierRequestTypeDef",
    "CreateColumnStatisticsTaskSettingsRequestTypeDef",
    "CreateConnectionRequestTypeDef",
    "CreateConnectionResponseTypeDef",
    "CreateCrawlerRequestTypeDef",
    "CreateCsvClassifierRequestTypeDef",
    "CreateCustomEntityTypeRequestTypeDef",
    "CreateCustomEntityTypeResponseTypeDef",
    "CreateDataQualityRulesetRequestTypeDef",
    "CreateDataQualityRulesetResponseTypeDef",
    "CreateDatabaseRequestTypeDef",
    "CreateDevEndpointRequestTypeDef",
    "CreateDevEndpointResponseTypeDef",
    "CreateGrokClassifierRequestTypeDef",
    "CreateIntegrationRequestTypeDef",
    "CreateIntegrationResourcePropertyRequestTypeDef",
    "CreateIntegrationResourcePropertyResponseTypeDef",
    "CreateIntegrationResponseTypeDef",
    "CreateIntegrationTablePropertiesRequestTypeDef",
    "CreateJobRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreateJsonClassifierRequestTypeDef",
    "CreateMLTransformRequestTypeDef",
    "CreateMLTransformResponseTypeDef",
    "CreatePartitionIndexRequestTypeDef",
    "CreatePartitionRequestTypeDef",
    "CreateRegistryInputTypeDef",
    "CreateRegistryResponseTypeDef",
    "CreateSchemaInputTypeDef",
    "CreateSchemaResponseTypeDef",
    "CreateScriptRequestTypeDef",
    "CreateScriptResponseTypeDef",
    "CreateSecurityConfigurationRequestTypeDef",
    "CreateSecurityConfigurationResponseTypeDef",
    "CreateSessionRequestTypeDef",
    "CreateSessionResponseTypeDef",
    "CreateTableOptimizerRequestTypeDef",
    "CreateTableRequestTypeDef",
    "CreateTriggerRequestTypeDef",
    "CreateTriggerResponseTypeDef",
    "CreateUsageProfileRequestTypeDef",
    "CreateUsageProfileResponseTypeDef",
    "CreateUserDefinedFunctionRequestTypeDef",
    "CreateWorkflowRequestTypeDef",
    "CreateWorkflowResponseTypeDef",
    "CreateXMLClassifierRequestTypeDef",
    "CsvClassifierTypeDef",
    "CustomCodeOutputTypeDef",
    "CustomCodeTypeDef",
    "CustomCodeUnionTypeDef",
    "CustomEntityTypeTypeDef",
    "DQResultsPublishingOptionsTypeDef",
    "DQStopJobOnFailureOptionsTypeDef",
    "DataCatalogEncryptionSettingsTypeDef",
    "DataLakeAccessPropertiesOutputTypeDef",
    "DataLakeAccessPropertiesTypeDef",
    "DataLakePrincipalTypeDef",
    "DataQualityAnalyzerResultTypeDef",
    "DataQualityEncryptionTypeDef",
    "DataQualityEvaluationRunAdditionalRunOptionsTypeDef",
    "DataQualityMetricValuesTypeDef",
    "DataQualityObservationTypeDef",
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
    "DataSourceOutputTypeDef",
    "DataSourceTypeDef",
    "DataSourceUnionTypeDef",
    "DatabaseIdentifierTypeDef",
    "DatabaseInputTypeDef",
    "DatabaseTypeDef",
    "DatapointInclusionAnnotationTypeDef",
    "DatatypeTypeDef",
    "DateColumnStatisticsDataOutputTypeDef",
    "DateColumnStatisticsDataTypeDef",
    "DateColumnStatisticsDataUnionTypeDef",
    "DecimalColumnStatisticsDataOutputTypeDef",
    "DecimalColumnStatisticsDataTypeDef",
    "DecimalColumnStatisticsDataUnionTypeDef",
    "DecimalNumberOutputTypeDef",
    "DecimalNumberTypeDef",
    "DecimalNumberUnionTypeDef",
    "DeleteBlueprintRequestTypeDef",
    "DeleteBlueprintResponseTypeDef",
    "DeleteCatalogRequestTypeDef",
    "DeleteClassifierRequestTypeDef",
    "DeleteColumnStatisticsForPartitionRequestTypeDef",
    "DeleteColumnStatisticsForTableRequestTypeDef",
    "DeleteColumnStatisticsTaskSettingsRequestTypeDef",
    "DeleteConnectionRequestTypeDef",
    "DeleteCrawlerRequestTypeDef",
    "DeleteCustomEntityTypeRequestTypeDef",
    "DeleteCustomEntityTypeResponseTypeDef",
    "DeleteDataQualityRulesetRequestTypeDef",
    "DeleteDatabaseRequestTypeDef",
    "DeleteDevEndpointRequestTypeDef",
    "DeleteIntegrationRequestTypeDef",
    "DeleteIntegrationResponseTypeDef",
    "DeleteIntegrationTablePropertiesRequestTypeDef",
    "DeleteJobRequestTypeDef",
    "DeleteJobResponseTypeDef",
    "DeleteMLTransformRequestTypeDef",
    "DeleteMLTransformResponseTypeDef",
    "DeletePartitionIndexRequestTypeDef",
    "DeletePartitionRequestTypeDef",
    "DeleteRegistryInputTypeDef",
    "DeleteRegistryResponseTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteSchemaInputTypeDef",
    "DeleteSchemaResponseTypeDef",
    "DeleteSchemaVersionsInputTypeDef",
    "DeleteSchemaVersionsResponseTypeDef",
    "DeleteSecurityConfigurationRequestTypeDef",
    "DeleteSessionRequestTypeDef",
    "DeleteSessionResponseTypeDef",
    "DeleteTableOptimizerRequestTypeDef",
    "DeleteTableRequestTypeDef",
    "DeleteTableVersionRequestTypeDef",
    "DeleteTriggerRequestTypeDef",
    "DeleteTriggerResponseTypeDef",
    "DeleteUsageProfileRequestTypeDef",
    "DeleteUserDefinedFunctionRequestTypeDef",
    "DeleteWorkflowRequestTypeDef",
    "DeleteWorkflowResponseTypeDef",
    "DeltaTargetOutputTypeDef",
    "DeltaTargetTypeDef",
    "DescribeConnectionTypeRequestTypeDef",
    "DescribeConnectionTypeResponseTypeDef",
    "DescribeEntityRequestPaginateTypeDef",
    "DescribeEntityRequestTypeDef",
    "DescribeEntityResponseTypeDef",
    "DescribeInboundIntegrationsRequestTypeDef",
    "DescribeInboundIntegrationsResponseTypeDef",
    "DescribeIntegrationsRequestTypeDef",
    "DescribeIntegrationsResponseTypeDef",
    "DevEndpointCustomLibrariesTypeDef",
    "DevEndpointTypeDef",
    "DirectJDBCSourceTypeDef",
    "DirectKafkaSourceOutputTypeDef",
    "DirectKafkaSourceTypeDef",
    "DirectKafkaSourceUnionTypeDef",
    "DirectKinesisSourceOutputTypeDef",
    "DirectKinesisSourceTypeDef",
    "DirectKinesisSourceUnionTypeDef",
    "DirectSchemaChangePolicyTypeDef",
    "DoubleColumnStatisticsDataTypeDef",
    "DropDuplicatesOutputTypeDef",
    "DropDuplicatesTypeDef",
    "DropDuplicatesUnionTypeDef",
    "DropFieldsOutputTypeDef",
    "DropFieldsTypeDef",
    "DropFieldsUnionTypeDef",
    "DropNullFieldsOutputTypeDef",
    "DropNullFieldsTypeDef",
    "DropNullFieldsUnionTypeDef",
    "DynamicTransformOutputTypeDef",
    "DynamicTransformTypeDef",
    "DynamicTransformUnionTypeDef",
    "DynamoDBCatalogSourceTypeDef",
    "DynamoDBTargetTypeDef",
    "EdgeTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionConfigurationOutputTypeDef",
    "EncryptionConfigurationTypeDef",
    "EncryptionConfigurationUnionTypeDef",
    "EntityTypeDef",
    "ErrorDetailTypeDef",
    "ErrorDetailsTypeDef",
    "EvaluateDataQualityMultiFrameOutputTypeDef",
    "EvaluateDataQualityMultiFrameTypeDef",
    "EvaluateDataQualityMultiFrameUnionTypeDef",
    "EvaluateDataQualityOutputTypeDef",
    "EvaluateDataQualityTypeDef",
    "EvaluateDataQualityUnionTypeDef",
    "EvaluationMetricsTypeDef",
    "EventBatchingConditionTypeDef",
    "ExecutionAttemptTypeDef",
    "ExecutionPropertyTypeDef",
    "ExportLabelsTaskRunPropertiesTypeDef",
    "FederatedCatalogTypeDef",
    "FederatedDatabaseTypeDef",
    "FederatedTableTypeDef",
    "FieldTypeDef",
    "FillMissingValuesOutputTypeDef",
    "FillMissingValuesTypeDef",
    "FillMissingValuesUnionTypeDef",
    "FilterExpressionOutputTypeDef",
    "FilterExpressionTypeDef",
    "FilterExpressionUnionTypeDef",
    "FilterOutputTypeDef",
    "FilterTypeDef",
    "FilterUnionTypeDef",
    "FilterValueOutputTypeDef",
    "FilterValueTypeDef",
    "FilterValueUnionTypeDef",
    "FindMatchesMetricsTypeDef",
    "FindMatchesParametersTypeDef",
    "FindMatchesTaskRunPropertiesTypeDef",
    "GetBlueprintRequestTypeDef",
    "GetBlueprintResponseTypeDef",
    "GetBlueprintRunRequestTypeDef",
    "GetBlueprintRunResponseTypeDef",
    "GetBlueprintRunsRequestTypeDef",
    "GetBlueprintRunsResponseTypeDef",
    "GetCatalogImportStatusRequestTypeDef",
    "GetCatalogImportStatusResponseTypeDef",
    "GetCatalogRequestTypeDef",
    "GetCatalogResponseTypeDef",
    "GetCatalogsRequestTypeDef",
    "GetCatalogsResponseTypeDef",
    "GetClassifierRequestTypeDef",
    "GetClassifierResponseTypeDef",
    "GetClassifiersRequestPaginateTypeDef",
    "GetClassifiersRequestTypeDef",
    "GetClassifiersResponseTypeDef",
    "GetColumnStatisticsForPartitionRequestTypeDef",
    "GetColumnStatisticsForPartitionResponseTypeDef",
    "GetColumnStatisticsForTableRequestTypeDef",
    "GetColumnStatisticsForTableResponseTypeDef",
    "GetColumnStatisticsTaskRunRequestTypeDef",
    "GetColumnStatisticsTaskRunResponseTypeDef",
    "GetColumnStatisticsTaskRunsRequestTypeDef",
    "GetColumnStatisticsTaskRunsResponseTypeDef",
    "GetColumnStatisticsTaskSettingsRequestTypeDef",
    "GetColumnStatisticsTaskSettingsResponseTypeDef",
    "GetConnectionRequestTypeDef",
    "GetConnectionResponseTypeDef",
    "GetConnectionsFilterTypeDef",
    "GetConnectionsRequestPaginateTypeDef",
    "GetConnectionsRequestTypeDef",
    "GetConnectionsResponseTypeDef",
    "GetCrawlerMetricsRequestPaginateTypeDef",
    "GetCrawlerMetricsRequestTypeDef",
    "GetCrawlerMetricsResponseTypeDef",
    "GetCrawlerRequestTypeDef",
    "GetCrawlerResponseTypeDef",
    "GetCrawlersRequestPaginateTypeDef",
    "GetCrawlersRequestTypeDef",
    "GetCrawlersResponseTypeDef",
    "GetCustomEntityTypeRequestTypeDef",
    "GetCustomEntityTypeResponseTypeDef",
    "GetDataCatalogEncryptionSettingsRequestTypeDef",
    "GetDataCatalogEncryptionSettingsResponseTypeDef",
    "GetDataQualityModelRequestTypeDef",
    "GetDataQualityModelResponseTypeDef",
    "GetDataQualityModelResultRequestTypeDef",
    "GetDataQualityModelResultResponseTypeDef",
    "GetDataQualityResultRequestTypeDef",
    "GetDataQualityResultResponseTypeDef",
    "GetDataQualityRuleRecommendationRunRequestTypeDef",
    "GetDataQualityRuleRecommendationRunResponseTypeDef",
    "GetDataQualityRulesetEvaluationRunRequestTypeDef",
    "GetDataQualityRulesetEvaluationRunResponseTypeDef",
    "GetDataQualityRulesetRequestTypeDef",
    "GetDataQualityRulesetResponseTypeDef",
    "GetDatabaseRequestTypeDef",
    "GetDatabaseResponseTypeDef",
    "GetDatabasesRequestPaginateTypeDef",
    "GetDatabasesRequestTypeDef",
    "GetDatabasesResponseTypeDef",
    "GetDataflowGraphRequestTypeDef",
    "GetDataflowGraphResponseTypeDef",
    "GetDevEndpointRequestTypeDef",
    "GetDevEndpointResponseTypeDef",
    "GetDevEndpointsRequestPaginateTypeDef",
    "GetDevEndpointsRequestTypeDef",
    "GetDevEndpointsResponseTypeDef",
    "GetEntityRecordsRequestTypeDef",
    "GetEntityRecordsResponseTypeDef",
    "GetIntegrationResourcePropertyRequestTypeDef",
    "GetIntegrationResourcePropertyResponseTypeDef",
    "GetIntegrationTablePropertiesRequestTypeDef",
    "GetIntegrationTablePropertiesResponseTypeDef",
    "GetJobBookmarkRequestTypeDef",
    "GetJobBookmarkResponseTypeDef",
    "GetJobRequestTypeDef",
    "GetJobResponseTypeDef",
    "GetJobRunRequestTypeDef",
    "GetJobRunResponseTypeDef",
    "GetJobRunsRequestPaginateTypeDef",
    "GetJobRunsRequestTypeDef",
    "GetJobRunsResponseTypeDef",
    "GetJobsRequestPaginateTypeDef",
    "GetJobsRequestTypeDef",
    "GetJobsResponsePaginatorTypeDef",
    "GetJobsResponseTypeDef",
    "GetMLTaskRunRequestTypeDef",
    "GetMLTaskRunResponseTypeDef",
    "GetMLTaskRunsRequestTypeDef",
    "GetMLTaskRunsResponseTypeDef",
    "GetMLTransformRequestTypeDef",
    "GetMLTransformResponseTypeDef",
    "GetMLTransformsRequestTypeDef",
    "GetMLTransformsResponseTypeDef",
    "GetMappingRequestTypeDef",
    "GetMappingResponseTypeDef",
    "GetPartitionIndexesRequestPaginateTypeDef",
    "GetPartitionIndexesRequestTypeDef",
    "GetPartitionIndexesResponseTypeDef",
    "GetPartitionRequestTypeDef",
    "GetPartitionResponseTypeDef",
    "GetPartitionsRequestPaginateTypeDef",
    "GetPartitionsRequestTypeDef",
    "GetPartitionsResponseTypeDef",
    "GetPlanRequestTypeDef",
    "GetPlanResponseTypeDef",
    "GetRegistryInputTypeDef",
    "GetRegistryResponseTypeDef",
    "GetResourcePoliciesRequestPaginateTypeDef",
    "GetResourcePoliciesRequestTypeDef",
    "GetResourcePoliciesResponseTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetSchemaByDefinitionInputTypeDef",
    "GetSchemaByDefinitionResponseTypeDef",
    "GetSchemaInputTypeDef",
    "GetSchemaResponseTypeDef",
    "GetSchemaVersionInputTypeDef",
    "GetSchemaVersionResponseTypeDef",
    "GetSchemaVersionsDiffInputTypeDef",
    "GetSchemaVersionsDiffResponseTypeDef",
    "GetSecurityConfigurationRequestTypeDef",
    "GetSecurityConfigurationResponseTypeDef",
    "GetSecurityConfigurationsRequestPaginateTypeDef",
    "GetSecurityConfigurationsRequestTypeDef",
    "GetSecurityConfigurationsResponseTypeDef",
    "GetSessionRequestTypeDef",
    "GetSessionResponseTypeDef",
    "GetStatementRequestTypeDef",
    "GetStatementResponseTypeDef",
    "GetTableOptimizerRequestTypeDef",
    "GetTableOptimizerResponseTypeDef",
    "GetTableRequestTypeDef",
    "GetTableResponseTypeDef",
    "GetTableVersionRequestTypeDef",
    "GetTableVersionResponseTypeDef",
    "GetTableVersionsRequestPaginateTypeDef",
    "GetTableVersionsRequestTypeDef",
    "GetTableVersionsResponsePaginatorTypeDef",
    "GetTableVersionsResponseTypeDef",
    "GetTablesRequestPaginateTypeDef",
    "GetTablesRequestTypeDef",
    "GetTablesResponsePaginatorTypeDef",
    "GetTablesResponseTypeDef",
    "GetTagsRequestTypeDef",
    "GetTagsResponseTypeDef",
    "GetTriggerRequestTypeDef",
    "GetTriggerResponseTypeDef",
    "GetTriggersRequestPaginateTypeDef",
    "GetTriggersRequestTypeDef",
    "GetTriggersResponseTypeDef",
    "GetUnfilteredPartitionMetadataRequestTypeDef",
    "GetUnfilteredPartitionMetadataResponseTypeDef",
    "GetUnfilteredPartitionsMetadataRequestTypeDef",
    "GetUnfilteredPartitionsMetadataResponseTypeDef",
    "GetUnfilteredTableMetadataRequestTypeDef",
    "GetUnfilteredTableMetadataResponseTypeDef",
    "GetUsageProfileRequestTypeDef",
    "GetUsageProfileResponseTypeDef",
    "GetUserDefinedFunctionRequestTypeDef",
    "GetUserDefinedFunctionResponseTypeDef",
    "GetUserDefinedFunctionsRequestPaginateTypeDef",
    "GetUserDefinedFunctionsRequestTypeDef",
    "GetUserDefinedFunctionsResponseTypeDef",
    "GetWorkflowRequestTypeDef",
    "GetWorkflowResponseTypeDef",
    "GetWorkflowRunPropertiesRequestTypeDef",
    "GetWorkflowRunPropertiesResponseTypeDef",
    "GetWorkflowRunRequestTypeDef",
    "GetWorkflowRunResponseTypeDef",
    "GetWorkflowRunsRequestPaginateTypeDef",
    "GetWorkflowRunsRequestTypeDef",
    "GetWorkflowRunsResponseTypeDef",
    "GluePolicyTypeDef",
    "GlueSchemaOutputTypeDef",
    "GlueSchemaTypeDef",
    "GlueSchemaUnionTypeDef",
    "GlueStudioSchemaColumnTypeDef",
    "GlueTableOutputTypeDef",
    "GlueTableTypeDef",
    "GlueTableUnionTypeDef",
    "GovernedCatalogSourceTypeDef",
    "GovernedCatalogTargetOutputTypeDef",
    "GovernedCatalogTargetTypeDef",
    "GovernedCatalogTargetUnionTypeDef",
    "GrokClassifierTypeDef",
    "HudiTargetOutputTypeDef",
    "HudiTargetTypeDef",
    "IcebergCompactionMetricsTypeDef",
    "IcebergInputTypeDef",
    "IcebergOrphanFileDeletionConfigurationTypeDef",
    "IcebergOrphanFileDeletionMetricsTypeDef",
    "IcebergRetentionConfigurationTypeDef",
    "IcebergRetentionMetricsTypeDef",
    "IcebergTargetOutputTypeDef",
    "IcebergTargetTypeDef",
    "ImportCatalogToGlueRequestTypeDef",
    "ImportLabelsTaskRunPropertiesTypeDef",
    "InboundIntegrationTypeDef",
    "IntegrationErrorTypeDef",
    "IntegrationFilterTypeDef",
    "IntegrationPartitionTypeDef",
    "IntegrationTypeDef",
    "JDBCConnectorOptionsOutputTypeDef",
    "JDBCConnectorOptionsTypeDef",
    "JDBCConnectorOptionsUnionTypeDef",
    "JDBCConnectorSourceOutputTypeDef",
    "JDBCConnectorSourceTypeDef",
    "JDBCConnectorSourceUnionTypeDef",
    "JDBCConnectorTargetOutputTypeDef",
    "JDBCConnectorTargetTypeDef",
    "JDBCConnectorTargetUnionTypeDef",
    "JdbcTargetOutputTypeDef",
    "JdbcTargetTypeDef",
    "JobBookmarkEntryTypeDef",
    "JobBookmarksEncryptionTypeDef",
    "JobCommandTypeDef",
    "JobNodeDetailsTypeDef",
    "JobPaginatorTypeDef",
    "JobRunTypeDef",
    "JobTypeDef",
    "JobUpdateTypeDef",
    "JoinColumnOutputTypeDef",
    "JoinColumnTypeDef",
    "JoinColumnUnionTypeDef",
    "JoinOutputTypeDef",
    "JoinTypeDef",
    "JoinUnionTypeDef",
    "JsonClassifierTypeDef",
    "KafkaStreamingSourceOptionsOutputTypeDef",
    "KafkaStreamingSourceOptionsTypeDef",
    "KafkaStreamingSourceOptionsUnionTypeDef",
    "KeySchemaElementTypeDef",
    "KinesisStreamingSourceOptionsOutputTypeDef",
    "KinesisStreamingSourceOptionsTypeDef",
    "KinesisStreamingSourceOptionsUnionTypeDef",
    "LabelingSetGenerationTaskRunPropertiesTypeDef",
    "LakeFormationConfigurationTypeDef",
    "LastActiveDefinitionTypeDef",
    "LastCrawlInfoTypeDef",
    "LineageConfigurationTypeDef",
    "ListBlueprintsRequestPaginateTypeDef",
    "ListBlueprintsRequestTypeDef",
    "ListBlueprintsResponseTypeDef",
    "ListColumnStatisticsTaskRunsRequestTypeDef",
    "ListColumnStatisticsTaskRunsResponseTypeDef",
    "ListConnectionTypesRequestPaginateTypeDef",
    "ListConnectionTypesRequestTypeDef",
    "ListConnectionTypesResponseTypeDef",
    "ListCrawlersRequestTypeDef",
    "ListCrawlersResponseTypeDef",
    "ListCrawlsRequestTypeDef",
    "ListCrawlsResponseTypeDef",
    "ListCustomEntityTypesRequestTypeDef",
    "ListCustomEntityTypesResponseTypeDef",
    "ListDataQualityResultsRequestTypeDef",
    "ListDataQualityResultsResponseTypeDef",
    "ListDataQualityRuleRecommendationRunsRequestTypeDef",
    "ListDataQualityRuleRecommendationRunsResponseTypeDef",
    "ListDataQualityRulesetEvaluationRunsRequestTypeDef",
    "ListDataQualityRulesetEvaluationRunsResponseTypeDef",
    "ListDataQualityRulesetsRequestTypeDef",
    "ListDataQualityRulesetsResponseTypeDef",
    "ListDataQualityStatisticAnnotationsRequestTypeDef",
    "ListDataQualityStatisticAnnotationsResponseTypeDef",
    "ListDataQualityStatisticsRequestTypeDef",
    "ListDataQualityStatisticsResponseTypeDef",
    "ListDevEndpointsRequestTypeDef",
    "ListDevEndpointsResponseTypeDef",
    "ListEntitiesRequestPaginateTypeDef",
    "ListEntitiesRequestTypeDef",
    "ListEntitiesResponseTypeDef",
    "ListJobsRequestPaginateTypeDef",
    "ListJobsRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListMLTransformsRequestTypeDef",
    "ListMLTransformsResponseTypeDef",
    "ListRegistriesInputPaginateTypeDef",
    "ListRegistriesInputTypeDef",
    "ListRegistriesResponseTypeDef",
    "ListSchemaVersionsInputPaginateTypeDef",
    "ListSchemaVersionsInputTypeDef",
    "ListSchemaVersionsResponseTypeDef",
    "ListSchemasInputPaginateTypeDef",
    "ListSchemasInputTypeDef",
    "ListSchemasResponseTypeDef",
    "ListSessionsRequestTypeDef",
    "ListSessionsResponseTypeDef",
    "ListStatementsRequestTypeDef",
    "ListStatementsResponseTypeDef",
    "ListTableOptimizerRunsRequestPaginateTypeDef",
    "ListTableOptimizerRunsRequestTypeDef",
    "ListTableOptimizerRunsResponseTypeDef",
    "ListTriggersRequestPaginateTypeDef",
    "ListTriggersRequestTypeDef",
    "ListTriggersResponseTypeDef",
    "ListUsageProfilesRequestPaginateTypeDef",
    "ListUsageProfilesRequestTypeDef",
    "ListUsageProfilesResponseTypeDef",
    "ListWorkflowsRequestPaginateTypeDef",
    "ListWorkflowsRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "LocationTypeDef",
    "LongColumnStatisticsDataTypeDef",
    "MLTransformTypeDef",
    "MLUserDataEncryptionTypeDef",
    "MappingEntryTypeDef",
    "MappingOutputTypeDef",
    "MappingPaginatorTypeDef",
    "MappingTypeDef",
    "MappingUnionTypeDef",
    "MergeOutputTypeDef",
    "MergeTypeDef",
    "MergeUnionTypeDef",
    "MetadataInfoTypeDef",
    "MetadataKeyValuePairTypeDef",
    "MetricBasedObservationTypeDef",
    "MicrosoftSQLServerCatalogSourceTypeDef",
    "MicrosoftSQLServerCatalogTargetOutputTypeDef",
    "MicrosoftSQLServerCatalogTargetTypeDef",
    "MicrosoftSQLServerCatalogTargetUnionTypeDef",
    "ModifyIntegrationRequestTypeDef",
    "ModifyIntegrationResponseTypeDef",
    "MongoDBTargetTypeDef",
    "MySQLCatalogSourceTypeDef",
    "MySQLCatalogTargetOutputTypeDef",
    "MySQLCatalogTargetTypeDef",
    "MySQLCatalogTargetUnionTypeDef",
    "NodeTypeDef",
    "NotificationPropertyTypeDef",
    "NullCheckBoxListTypeDef",
    "NullValueFieldTypeDef",
    "OAuth2ClientApplicationTypeDef",
    "OAuth2CredentialsTypeDef",
    "OAuth2PropertiesInputTypeDef",
    "OAuth2PropertiesTypeDef",
    "OpenTableFormatInputTypeDef",
    "OptionTypeDef",
    "OracleSQLCatalogSourceTypeDef",
    "OracleSQLCatalogTargetOutputTypeDef",
    "OracleSQLCatalogTargetTypeDef",
    "OracleSQLCatalogTargetUnionTypeDef",
    "OrderTypeDef",
    "OrphanFileDeletionConfigurationTypeDef",
    "OrphanFileDeletionMetricsTypeDef",
    "OtherMetadataValueListItemTypeDef",
    "PIIDetectionOutputTypeDef",
    "PIIDetectionTypeDef",
    "PIIDetectionUnionTypeDef",
    "PaginatorConfigTypeDef",
    "PartitionErrorTypeDef",
    "PartitionIndexDescriptorTypeDef",
    "PartitionIndexTypeDef",
    "PartitionInputTypeDef",
    "PartitionTypeDef",
    "PartitionValueListOutputTypeDef",
    "PartitionValueListTypeDef",
    "PartitionValueListUnionTypeDef",
    "PhysicalConnectionRequirementsOutputTypeDef",
    "PhysicalConnectionRequirementsTypeDef",
    "PhysicalConnectionRequirementsUnionTypeDef",
    "PostgreSQLCatalogSourceTypeDef",
    "PostgreSQLCatalogTargetOutputTypeDef",
    "PostgreSQLCatalogTargetTypeDef",
    "PostgreSQLCatalogTargetUnionTypeDef",
    "PredecessorTypeDef",
    "PredicateOutputTypeDef",
    "PredicateTypeDef",
    "PredicateUnionTypeDef",
    "PrincipalPermissionsOutputTypeDef",
    "PrincipalPermissionsTypeDef",
    "PrincipalPermissionsUnionTypeDef",
    "ProfileConfigurationOutputTypeDef",
    "ProfileConfigurationTypeDef",
    "ProfileConfigurationUnionTypeDef",
    "PropertyPredicateTypeDef",
    "PropertyTypeDef",
    "PutDataCatalogEncryptionSettingsRequestTypeDef",
    "PutDataQualityProfileAnnotationRequestTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "PutSchemaVersionMetadataInputTypeDef",
    "PutSchemaVersionMetadataResponseTypeDef",
    "PutWorkflowRunPropertiesRequestTypeDef",
    "QuerySchemaVersionMetadataInputTypeDef",
    "QuerySchemaVersionMetadataResponseTypeDef",
    "QuerySessionContextTypeDef",
    "RecipeActionOutputTypeDef",
    "RecipeActionTypeDef",
    "RecipeActionUnionTypeDef",
    "RecipeOutputTypeDef",
    "RecipeReferenceTypeDef",
    "RecipeStepOutputTypeDef",
    "RecipeStepTypeDef",
    "RecipeStepUnionTypeDef",
    "RecipeTypeDef",
    "RecipeUnionTypeDef",
    "RecrawlPolicyTypeDef",
    "RedshiftSourceTypeDef",
    "RedshiftTargetOutputTypeDef",
    "RedshiftTargetTypeDef",
    "RedshiftTargetUnionTypeDef",
    "RegisterSchemaVersionInputTypeDef",
    "RegisterSchemaVersionResponseTypeDef",
    "RegistryIdTypeDef",
    "RegistryListItemTypeDef",
    "RelationalCatalogSourceTypeDef",
    "RemoveSchemaVersionMetadataInputTypeDef",
    "RemoveSchemaVersionMetadataResponseTypeDef",
    "RenameFieldOutputTypeDef",
    "RenameFieldTypeDef",
    "RenameFieldUnionTypeDef",
    "ResetJobBookmarkRequestTypeDef",
    "ResetJobBookmarkResponseTypeDef",
    "ResourceUriTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeWorkflowRunRequestTypeDef",
    "ResumeWorkflowRunResponseTypeDef",
    "RetentionConfigurationTypeDef",
    "RetentionMetricsTypeDef",
    "RunIdentifierTypeDef",
    "RunMetricsTypeDef",
    "RunStatementRequestTypeDef",
    "RunStatementResponseTypeDef",
    "S3CatalogDeltaSourceOutputTypeDef",
    "S3CatalogDeltaSourceTypeDef",
    "S3CatalogDeltaSourceUnionTypeDef",
    "S3CatalogHudiSourceOutputTypeDef",
    "S3CatalogHudiSourceTypeDef",
    "S3CatalogHudiSourceUnionTypeDef",
    "S3CatalogSourceTypeDef",
    "S3CatalogTargetOutputTypeDef",
    "S3CatalogTargetTypeDef",
    "S3CatalogTargetUnionTypeDef",
    "S3CsvSourceOutputTypeDef",
    "S3CsvSourceTypeDef",
    "S3CsvSourceUnionTypeDef",
    "S3DeltaCatalogTargetOutputTypeDef",
    "S3DeltaCatalogTargetTypeDef",
    "S3DeltaCatalogTargetUnionTypeDef",
    "S3DeltaDirectTargetOutputTypeDef",
    "S3DeltaDirectTargetTypeDef",
    "S3DeltaDirectTargetUnionTypeDef",
    "S3DeltaSourceOutputTypeDef",
    "S3DeltaSourceTypeDef",
    "S3DeltaSourceUnionTypeDef",
    "S3DirectSourceAdditionalOptionsTypeDef",
    "S3DirectTargetOutputTypeDef",
    "S3DirectTargetTypeDef",
    "S3DirectTargetUnionTypeDef",
    "S3EncryptionTypeDef",
    "S3GlueParquetTargetOutputTypeDef",
    "S3GlueParquetTargetTypeDef",
    "S3GlueParquetTargetUnionTypeDef",
    "S3HudiCatalogTargetOutputTypeDef",
    "S3HudiCatalogTargetTypeDef",
    "S3HudiCatalogTargetUnionTypeDef",
    "S3HudiDirectTargetOutputTypeDef",
    "S3HudiDirectTargetTypeDef",
    "S3HudiDirectTargetUnionTypeDef",
    "S3HudiSourceOutputTypeDef",
    "S3HudiSourceTypeDef",
    "S3HudiSourceUnionTypeDef",
    "S3JsonSourceOutputTypeDef",
    "S3JsonSourceTypeDef",
    "S3JsonSourceUnionTypeDef",
    "S3ParquetSourceOutputTypeDef",
    "S3ParquetSourceTypeDef",
    "S3ParquetSourceUnionTypeDef",
    "S3SourceAdditionalOptionsTypeDef",
    "S3TargetOutputTypeDef",
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
    "SearchTablesRequestTypeDef",
    "SearchTablesResponseTypeDef",
    "SecurityConfigurationTypeDef",
    "SegmentTypeDef",
    "SelectFieldsOutputTypeDef",
    "SelectFieldsTypeDef",
    "SelectFieldsUnionTypeDef",
    "SelectFromCollectionOutputTypeDef",
    "SelectFromCollectionTypeDef",
    "SelectFromCollectionUnionTypeDef",
    "SerDeInfoOutputTypeDef",
    "SerDeInfoTypeDef",
    "SerDeInfoUnionTypeDef",
    "SessionCommandTypeDef",
    "SessionTypeDef",
    "SkewedInfoOutputTypeDef",
    "SkewedInfoTypeDef",
    "SkewedInfoUnionTypeDef",
    "SnowflakeNodeDataOutputTypeDef",
    "SnowflakeNodeDataTypeDef",
    "SnowflakeNodeDataUnionTypeDef",
    "SnowflakeSourceOutputTypeDef",
    "SnowflakeSourceTypeDef",
    "SnowflakeSourceUnionTypeDef",
    "SnowflakeTargetOutputTypeDef",
    "SnowflakeTargetTypeDef",
    "SnowflakeTargetUnionTypeDef",
    "SortCriterionTypeDef",
    "SourceControlDetailsTypeDef",
    "SourceProcessingPropertiesTypeDef",
    "SourceTableConfigOutputTypeDef",
    "SourceTableConfigTypeDef",
    "SourceTableConfigUnionTypeDef",
    "SparkConnectorSourceOutputTypeDef",
    "SparkConnectorSourceTypeDef",
    "SparkConnectorSourceUnionTypeDef",
    "SparkConnectorTargetOutputTypeDef",
    "SparkConnectorTargetTypeDef",
    "SparkConnectorTargetUnionTypeDef",
    "SparkSQLOutputTypeDef",
    "SparkSQLTypeDef",
    "SparkSQLUnionTypeDef",
    "SpigotOutputTypeDef",
    "SpigotTypeDef",
    "SpigotUnionTypeDef",
    "SplitFieldsOutputTypeDef",
    "SplitFieldsTypeDef",
    "SplitFieldsUnionTypeDef",
    "SqlAliasTypeDef",
    "StartBlueprintRunRequestTypeDef",
    "StartBlueprintRunResponseTypeDef",
    "StartColumnStatisticsTaskRunRequestTypeDef",
    "StartColumnStatisticsTaskRunResponseTypeDef",
    "StartColumnStatisticsTaskRunScheduleRequestTypeDef",
    "StartCrawlerRequestTypeDef",
    "StartCrawlerScheduleRequestTypeDef",
    "StartDataQualityRuleRecommendationRunRequestTypeDef",
    "StartDataQualityRuleRecommendationRunResponseTypeDef",
    "StartDataQualityRulesetEvaluationRunRequestTypeDef",
    "StartDataQualityRulesetEvaluationRunResponseTypeDef",
    "StartExportLabelsTaskRunRequestTypeDef",
    "StartExportLabelsTaskRunResponseTypeDef",
    "StartImportLabelsTaskRunRequestTypeDef",
    "StartImportLabelsTaskRunResponseTypeDef",
    "StartJobRunRequestTypeDef",
    "StartJobRunResponseTypeDef",
    "StartMLEvaluationTaskRunRequestTypeDef",
    "StartMLEvaluationTaskRunResponseTypeDef",
    "StartMLLabelingSetGenerationTaskRunRequestTypeDef",
    "StartMLLabelingSetGenerationTaskRunResponseTypeDef",
    "StartTriggerRequestTypeDef",
    "StartTriggerResponseTypeDef",
    "StartWorkflowRunRequestTypeDef",
    "StartWorkflowRunResponseTypeDef",
    "StartingEventBatchConditionTypeDef",
    "StatementOutputDataTypeDef",
    "StatementOutputTypeDef",
    "StatementTypeDef",
    "StatisticAnnotationTypeDef",
    "StatisticModelResultTypeDef",
    "StatisticSummaryTypeDef",
    "StatusDetailsPaginatorTypeDef",
    "StatusDetailsTypeDef",
    "StopColumnStatisticsTaskRunRequestTypeDef",
    "StopColumnStatisticsTaskRunScheduleRequestTypeDef",
    "StopCrawlerRequestTypeDef",
    "StopCrawlerScheduleRequestTypeDef",
    "StopSessionRequestTypeDef",
    "StopSessionResponseTypeDef",
    "StopTriggerRequestTypeDef",
    "StopTriggerResponseTypeDef",
    "StopWorkflowRunRequestTypeDef",
    "StorageDescriptorOutputTypeDef",
    "StorageDescriptorTypeDef",
    "StorageDescriptorUnionTypeDef",
    "StreamingDataPreviewOptionsTypeDef",
    "StringColumnStatisticsDataTypeDef",
    "SupportedDialectTypeDef",
    "TableErrorTypeDef",
    "TableIdentifierTypeDef",
    "TableInputTypeDef",
    "TableOptimizerConfigurationTypeDef",
    "TableOptimizerRunTypeDef",
    "TableOptimizerTypeDef",
    "TableOptimizerVpcConfigurationTypeDef",
    "TablePaginatorTypeDef",
    "TableStatusPaginatorTypeDef",
    "TableStatusTypeDef",
    "TableTypeDef",
    "TableVersionErrorTypeDef",
    "TableVersionPaginatorTypeDef",
    "TableVersionTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TargetProcessingPropertiesTypeDef",
    "TargetRedshiftCatalogTypeDef",
    "TargetTableConfigOutputTypeDef",
    "TargetTableConfigTypeDef",
    "TargetTableConfigUnionTypeDef",
    "TaskRunFilterCriteriaTypeDef",
    "TaskRunPropertiesTypeDef",
    "TaskRunSortCriteriaTypeDef",
    "TaskRunTypeDef",
    "TestConnectionInputTypeDef",
    "TestConnectionRequestTypeDef",
    "TimestampFilterTypeDef",
    "TimestampTypeDef",
    "TimestampedInclusionAnnotationTypeDef",
    "TransformConfigParameterOutputTypeDef",
    "TransformConfigParameterTypeDef",
    "TransformConfigParameterUnionTypeDef",
    "TransformEncryptionTypeDef",
    "TransformFilterCriteriaTypeDef",
    "TransformParametersTypeDef",
    "TransformSortCriteriaTypeDef",
    "TriggerNodeDetailsTypeDef",
    "TriggerTypeDef",
    "TriggerUpdateTypeDef",
    "UnfilteredPartitionTypeDef",
    "UnionOutputTypeDef",
    "UnionTypeDef",
    "UnionUnionTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateBlueprintRequestTypeDef",
    "UpdateBlueprintResponseTypeDef",
    "UpdateCatalogRequestTypeDef",
    "UpdateClassifierRequestTypeDef",
    "UpdateColumnStatisticsForPartitionRequestTypeDef",
    "UpdateColumnStatisticsForPartitionResponseTypeDef",
    "UpdateColumnStatisticsForTableRequestTypeDef",
    "UpdateColumnStatisticsForTableResponseTypeDef",
    "UpdateColumnStatisticsTaskSettingsRequestTypeDef",
    "UpdateConnectionRequestTypeDef",
    "UpdateCrawlerRequestTypeDef",
    "UpdateCrawlerScheduleRequestTypeDef",
    "UpdateCsvClassifierRequestTypeDef",
    "UpdateDataQualityRulesetRequestTypeDef",
    "UpdateDataQualityRulesetResponseTypeDef",
    "UpdateDatabaseRequestTypeDef",
    "UpdateDevEndpointRequestTypeDef",
    "UpdateGrokClassifierRequestTypeDef",
    "UpdateIntegrationResourcePropertyRequestTypeDef",
    "UpdateIntegrationResourcePropertyResponseTypeDef",
    "UpdateIntegrationTablePropertiesRequestTypeDef",
    "UpdateJobFromSourceControlRequestTypeDef",
    "UpdateJobFromSourceControlResponseTypeDef",
    "UpdateJobRequestTypeDef",
    "UpdateJobResponseTypeDef",
    "UpdateJsonClassifierRequestTypeDef",
    "UpdateMLTransformRequestTypeDef",
    "UpdateMLTransformResponseTypeDef",
    "UpdatePartitionRequestTypeDef",
    "UpdateRegistryInputTypeDef",
    "UpdateRegistryResponseTypeDef",
    "UpdateSchemaInputTypeDef",
    "UpdateSchemaResponseTypeDef",
    "UpdateSourceControlFromJobRequestTypeDef",
    "UpdateSourceControlFromJobResponseTypeDef",
    "UpdateTableOptimizerRequestTypeDef",
    "UpdateTableRequestTypeDef",
    "UpdateTriggerRequestTypeDef",
    "UpdateTriggerResponseTypeDef",
    "UpdateUsageProfileRequestTypeDef",
    "UpdateUsageProfileResponseTypeDef",
    "UpdateUserDefinedFunctionRequestTypeDef",
    "UpdateWorkflowRequestTypeDef",
    "UpdateWorkflowResponseTypeDef",
    "UpdateXMLClassifierRequestTypeDef",
    "UpsertRedshiftTargetOptionsOutputTypeDef",
    "UpsertRedshiftTargetOptionsTypeDef",
    "UpsertRedshiftTargetOptionsUnionTypeDef",
    "UsageProfileDefinitionTypeDef",
    "UserDefinedFunctionInputTypeDef",
    "UserDefinedFunctionTypeDef",
    "ViewDefinitionInputTypeDef",
    "ViewDefinitionTypeDef",
    "ViewRepresentationInputTypeDef",
    "ViewRepresentationTypeDef",
    "ViewValidationTypeDef",
    "WorkflowGraphTypeDef",
    "WorkflowRunStatisticsTypeDef",
    "WorkflowRunTypeDef",
    "WorkflowTypeDef",
    "XMLClassifierTypeDef",
)

class NotificationPropertyTypeDef(TypedDict):
    NotifyDelayAfter: NotRequired[int]

class AggregateOperationOutputTypeDef(TypedDict):
    Column: List[str]
    AggFunc: AggFunctionType

class AggregateOperationTypeDef(TypedDict):
    Column: Sequence[str]
    AggFunc: AggFunctionType

class AllowedValueTypeDef(TypedDict):
    Value: str
    Description: NotRequired[str]

class AmazonRedshiftAdvancedOptionTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class OptionTypeDef(TypedDict):
    Value: NotRequired[str]
    Label: NotRequired[str]
    Description: NotRequired[str]

class AnnotationErrorTypeDef(TypedDict):
    ProfileId: NotRequired[str]
    StatisticId: NotRequired[str]
    FailureReason: NotRequired[str]

class MappingOutputTypeDef(TypedDict):
    ToKey: NotRequired[str]
    FromPath: NotRequired[List[str]]
    FromType: NotRequired[str]
    ToType: NotRequired[str]
    Dropped: NotRequired[bool]
    Children: NotRequired[List[Dict[str, Any]]]

class MappingPaginatorTypeDef(TypedDict):
    ToKey: NotRequired[str]
    FromPath: NotRequired[List[str]]
    FromType: NotRequired[str]
    ToType: NotRequired[str]
    Dropped: NotRequired[bool]
    Children: NotRequired[List[Dict[str, Any]]]

class AuditContextTypeDef(TypedDict):
    AdditionalAuditContext: NotRequired[str]
    RequestedColumns: NotRequired[Sequence[str]]
    AllColumnsRequested: NotRequired[bool]

class BasicAuthenticationCredentialsTypeDef(TypedDict):
    Username: NotRequired[str]
    Password: NotRequired[str]

class AuthorizationCodePropertiesTypeDef(TypedDict):
    AuthorizationCode: NotRequired[str]
    RedirectUri: NotRequired[str]

class PartitionValueListOutputTypeDef(TypedDict):
    Values: List[str]

class BasicCatalogTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str
    PartitionKeys: NotRequired[List[List[str]]]

class BasicCatalogTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str
    PartitionKeys: NotRequired[Sequence[Sequence[str]]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BatchDeleteConnectionRequestTypeDef(TypedDict):
    ConnectionNameList: Sequence[str]
    CatalogId: NotRequired[str]

class ErrorDetailTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class BatchDeleteTableRequestTypeDef(TypedDict):
    DatabaseName: str
    TablesToDelete: Sequence[str]
    CatalogId: NotRequired[str]
    TransactionId: NotRequired[str]

class BatchDeleteTableVersionRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    VersionIds: Sequence[str]
    CatalogId: NotRequired[str]

class BatchGetBlueprintsRequestTypeDef(TypedDict):
    Names: Sequence[str]
    IncludeBlueprint: NotRequired[bool]
    IncludeParameterSpec: NotRequired[bool]

class BatchGetCrawlersRequestTypeDef(TypedDict):
    CrawlerNames: Sequence[str]

class BatchGetCustomEntityTypesRequestTypeDef(TypedDict):
    Names: Sequence[str]

class CustomEntityTypeTypeDef(TypedDict):
    Name: str
    RegexString: str
    ContextWords: NotRequired[List[str]]

class BatchGetDataQualityResultRequestTypeDef(TypedDict):
    ResultIds: Sequence[str]

class BatchGetDevEndpointsRequestTypeDef(TypedDict):
    DevEndpointNames: Sequence[str]

class DevEndpointTypeDef(TypedDict):
    EndpointName: NotRequired[str]
    RoleArn: NotRequired[str]
    SecurityGroupIds: NotRequired[List[str]]
    SubnetId: NotRequired[str]
    YarnEndpointAddress: NotRequired[str]
    PrivateAddress: NotRequired[str]
    ZeppelinRemoteSparkInterpreterPort: NotRequired[int]
    PublicAddress: NotRequired[str]
    Status: NotRequired[str]
    WorkerType: NotRequired[WorkerTypeType]
    GlueVersion: NotRequired[str]
    NumberOfWorkers: NotRequired[int]
    NumberOfNodes: NotRequired[int]
    AvailabilityZone: NotRequired[str]
    VpcId: NotRequired[str]
    ExtraPythonLibsS3Path: NotRequired[str]
    ExtraJarsS3Path: NotRequired[str]
    FailureReason: NotRequired[str]
    LastUpdateStatus: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]
    LastModifiedTimestamp: NotRequired[datetime]
    PublicKey: NotRequired[str]
    PublicKeys: NotRequired[List[str]]
    SecurityConfiguration: NotRequired[str]
    Arguments: NotRequired[Dict[str, str]]

class BatchGetJobsRequestTypeDef(TypedDict):
    JobNames: Sequence[str]

BatchGetTableOptimizerEntryTypeDef = TypedDict(
    "BatchGetTableOptimizerEntryTypeDef",
    {
        "catalogId": NotRequired[str],
        "databaseName": NotRequired[str],
        "tableName": NotRequired[str],
        "type": NotRequired[TableOptimizerTypeType],
    },
)

class BatchGetTriggersRequestTypeDef(TypedDict):
    TriggerNames: Sequence[str]

class BatchGetWorkflowsRequestTypeDef(TypedDict):
    Names: Sequence[str]
    IncludeGraph: NotRequired[bool]

class DatapointInclusionAnnotationTypeDef(TypedDict):
    ProfileId: NotRequired[str]
    StatisticId: NotRequired[str]
    InclusionAnnotation: NotRequired[InclusionAnnotationValueType]

class BatchStopJobRunRequestTypeDef(TypedDict):
    JobName: str
    JobRunIds: Sequence[str]

class BatchStopJobRunSuccessfulSubmissionTypeDef(TypedDict):
    JobName: NotRequired[str]
    JobRunId: NotRequired[str]

class BinaryColumnStatisticsDataTypeDef(TypedDict):
    MaximumLength: int
    AverageLength: float
    NumberOfNulls: int

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class BlueprintDetailsTypeDef(TypedDict):
    BlueprintName: NotRequired[str]
    RunId: NotRequired[str]

class BlueprintRunTypeDef(TypedDict):
    BlueprintName: NotRequired[str]
    RunId: NotRequired[str]
    WorkflowName: NotRequired[str]
    State: NotRequired[BlueprintRunStateType]
    StartedOn: NotRequired[datetime]
    CompletedOn: NotRequired[datetime]
    ErrorMessage: NotRequired[str]
    RollbackErrorMessage: NotRequired[str]
    Parameters: NotRequired[str]
    RoleArn: NotRequired[str]

class LastActiveDefinitionTypeDef(TypedDict):
    Description: NotRequired[str]
    LastModifiedOn: NotRequired[datetime]
    ParameterSpec: NotRequired[str]
    BlueprintLocation: NotRequired[str]
    BlueprintServiceLocation: NotRequired[str]

class BooleanColumnStatisticsDataTypeDef(TypedDict):
    NumberOfTrues: int
    NumberOfFalses: int
    NumberOfNulls: int

class CancelDataQualityRuleRecommendationRunRequestTypeDef(TypedDict):
    RunId: str

class CancelDataQualityRulesetEvaluationRunRequestTypeDef(TypedDict):
    RunId: str

class CancelMLTaskRunRequestTypeDef(TypedDict):
    TransformId: str
    TaskRunId: str

class CancelStatementRequestTypeDef(TypedDict):
    SessionId: str
    Id: int
    RequestOrigin: NotRequired[str]

class CapabilitiesTypeDef(TypedDict):
    SupportedAuthenticationTypes: List[AuthenticationTypeType]
    SupportedDataOperations: List[DataOperationType]
    SupportedComputeEnvironments: List[ComputeEnvironmentType]

class CatalogEntryTypeDef(TypedDict):
    DatabaseName: str
    TableName: str

class CatalogImportStatusTypeDef(TypedDict):
    ImportCompleted: NotRequired[bool]
    ImportTime: NotRequired[datetime]
    ImportedBy: NotRequired[str]

class FederatedCatalogTypeDef(TypedDict):
    Identifier: NotRequired[str]
    ConnectionName: NotRequired[str]

class TargetRedshiftCatalogTypeDef(TypedDict):
    CatalogArn: str

class KafkaStreamingSourceOptionsOutputTypeDef(TypedDict):
    BootstrapServers: NotRequired[str]
    SecurityProtocol: NotRequired[str]
    ConnectionName: NotRequired[str]
    TopicName: NotRequired[str]
    Assign: NotRequired[str]
    SubscribePattern: NotRequired[str]
    Classification: NotRequired[str]
    Delimiter: NotRequired[str]
    StartingOffsets: NotRequired[str]
    EndingOffsets: NotRequired[str]
    PollTimeoutMs: NotRequired[int]
    NumRetries: NotRequired[int]
    RetryIntervalMs: NotRequired[int]
    MaxOffsetsPerTrigger: NotRequired[int]
    MinPartitions: NotRequired[int]
    IncludeHeaders: NotRequired[bool]
    AddRecordTimestamp: NotRequired[str]
    EmitConsumerLagMetrics: NotRequired[str]
    StartingTimestamp: NotRequired[datetime]

class StreamingDataPreviewOptionsTypeDef(TypedDict):
    PollingTime: NotRequired[int]
    RecordPollingLimit: NotRequired[int]

class KinesisStreamingSourceOptionsOutputTypeDef(TypedDict):
    EndpointUrl: NotRequired[str]
    StreamName: NotRequired[str]
    Classification: NotRequired[str]
    Delimiter: NotRequired[str]
    StartingPosition: NotRequired[StartingPositionType]
    MaxFetchTimeInMs: NotRequired[int]
    MaxFetchRecordsPerShard: NotRequired[int]
    MaxRecordPerRead: NotRequired[int]
    AddIdleTimeBetweenReads: NotRequired[bool]
    IdleTimeBetweenReadsInMs: NotRequired[int]
    DescribeShardInterval: NotRequired[int]
    NumRetries: NotRequired[int]
    RetryIntervalMs: NotRequired[int]
    MaxRetryIntervalMs: NotRequired[int]
    AvoidEmptyBatches: NotRequired[bool]
    StreamArn: NotRequired[str]
    RoleArn: NotRequired[str]
    RoleSessionName: NotRequired[str]
    AddRecordTimestamp: NotRequired[str]
    EmitConsumerLagMetrics: NotRequired[str]
    StartingTimestamp: NotRequired[datetime]

class DataLakeAccessPropertiesOutputTypeDef(TypedDict):
    DataLakeAccess: NotRequired[bool]
    DataTransferRole: NotRequired[str]
    KmsKey: NotRequired[str]
    ManagedWorkgroupName: NotRequired[str]
    ManagedWorkgroupStatus: NotRequired[str]
    RedshiftDatabaseName: NotRequired[str]
    StatusMessage: NotRequired[str]
    CatalogType: NotRequired[str]

class DataLakeAccessPropertiesTypeDef(TypedDict):
    DataLakeAccess: NotRequired[bool]
    DataTransferRole: NotRequired[str]
    KmsKey: NotRequired[str]
    CatalogType: NotRequired[str]

class CatalogSchemaChangePolicyTypeDef(TypedDict):
    EnableUpdateCatalog: NotRequired[bool]
    UpdateBehavior: NotRequired[UpdateCatalogBehaviorType]

class CatalogSourceTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str

class CatalogTargetOutputTypeDef(TypedDict):
    DatabaseName: str
    Tables: List[str]
    ConnectionName: NotRequired[str]
    EventQueueArn: NotRequired[str]
    DlqEventQueueArn: NotRequired[str]

class CatalogTargetTypeDef(TypedDict):
    DatabaseName: str
    Tables: Sequence[str]
    ConnectionName: NotRequired[str]
    EventQueueArn: NotRequired[str]
    DlqEventQueueArn: NotRequired[str]

class CheckSchemaVersionValidityInputTypeDef(TypedDict):
    DataFormat: DataFormatType
    SchemaDefinition: str

class CsvClassifierTypeDef(TypedDict):
    Name: str
    CreationTime: NotRequired[datetime]
    LastUpdated: NotRequired[datetime]
    Version: NotRequired[int]
    Delimiter: NotRequired[str]
    QuoteSymbol: NotRequired[str]
    ContainsHeader: NotRequired[CsvHeaderOptionType]
    Header: NotRequired[List[str]]
    DisableValueTrimming: NotRequired[bool]
    AllowSingleColumn: NotRequired[bool]
    CustomDatatypeConfigured: NotRequired[bool]
    CustomDatatypes: NotRequired[List[str]]
    Serde: NotRequired[CsvSerdeOptionType]

class GrokClassifierTypeDef(TypedDict):
    Name: str
    Classification: str
    GrokPattern: str
    CreationTime: NotRequired[datetime]
    LastUpdated: NotRequired[datetime]
    Version: NotRequired[int]
    CustomPatterns: NotRequired[str]

class JsonClassifierTypeDef(TypedDict):
    Name: str
    JsonPath: str
    CreationTime: NotRequired[datetime]
    LastUpdated: NotRequired[datetime]
    Version: NotRequired[int]

class XMLClassifierTypeDef(TypedDict):
    Name: str
    Classification: str
    CreationTime: NotRequired[datetime]
    LastUpdated: NotRequired[datetime]
    Version: NotRequired[int]
    RowTag: NotRequired[str]

class CloudWatchEncryptionTypeDef(TypedDict):
    CloudWatchEncryptionMode: NotRequired[CloudWatchEncryptionModeType]
    KmsKeyArn: NotRequired[str]

class ConnectorDataTargetOutputTypeDef(TypedDict):
    Name: str
    ConnectionType: str
    Data: Dict[str, str]
    Inputs: NotRequired[List[str]]

class DirectJDBCSourceTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str
    ConnectionName: str
    ConnectionType: JDBCConnectionTypeType
    RedshiftTmpDir: NotRequired[str]

class DropDuplicatesOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Columns: NotRequired[List[List[str]]]

class DropFieldsOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]

class DynamoDBCatalogSourceTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str

class FillMissingValuesOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    ImputedPath: str
    FilledPath: NotRequired[str]

class MergeOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Source: str
    PrimaryKeys: List[List[str]]

class MicrosoftSQLServerCatalogSourceTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str

class MicrosoftSQLServerCatalogTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class MySQLCatalogSourceTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str

class MySQLCatalogTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class OracleSQLCatalogSourceTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str

class OracleSQLCatalogTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class PIIDetectionOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    PiiType: PiiTypeType
    EntityTypesToDetect: List[str]
    OutputColumnName: NotRequired[str]
    SampleFraction: NotRequired[float]
    ThresholdFraction: NotRequired[float]
    MaskValue: NotRequired[str]

class PostgreSQLCatalogSourceTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str

class PostgreSQLCatalogTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class RedshiftSourceTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str
    RedshiftTmpDir: NotRequired[str]
    TmpDirIAMRole: NotRequired[str]

class RelationalCatalogSourceTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str

class RenameFieldOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    SourcePath: List[str]
    TargetPath: List[str]

class SelectFieldsOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]

class SelectFromCollectionOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Index: int

class SpigotOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Path: str
    Topk: NotRequired[int]
    Prob: NotRequired[float]

class SplitFieldsOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]

class UnionOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    UnionType: UnionTypeType

class CodeGenEdgeTypeDef(TypedDict):
    Source: str
    Target: str
    TargetParameter: NotRequired[str]

class CodeGenNodeArgTypeDef(TypedDict):
    Name: str
    Value: str
    Param: NotRequired[bool]

class ColumnImportanceTypeDef(TypedDict):
    ColumnName: NotRequired[str]
    Importance: NotRequired[float]

ColumnOutputTypeDef = TypedDict(
    "ColumnOutputTypeDef",
    {
        "Name": str,
        "Type": NotRequired[str],
        "Comment": NotRequired[str],
        "Parameters": NotRequired[Dict[str, str]],
    },
)

class ColumnRowFilterTypeDef(TypedDict):
    ColumnName: NotRequired[str]
    RowFilterExpression: NotRequired[str]

class DateColumnStatisticsDataOutputTypeDef(TypedDict):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: NotRequired[datetime]
    MaximumValue: NotRequired[datetime]

class DoubleColumnStatisticsDataTypeDef(TypedDict):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: NotRequired[float]
    MaximumValue: NotRequired[float]

class LongColumnStatisticsDataTypeDef(TypedDict):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: NotRequired[int]
    MaximumValue: NotRequired[int]

class StringColumnStatisticsDataTypeDef(TypedDict):
    MaximumLength: int
    AverageLength: float
    NumberOfNulls: int
    NumberOfDistinctValues: int

class ColumnStatisticsTaskRunTypeDef(TypedDict):
    CustomerId: NotRequired[str]
    ColumnStatisticsTaskRunId: NotRequired[str]
    DatabaseName: NotRequired[str]
    TableName: NotRequired[str]
    ColumnNameList: NotRequired[List[str]]
    CatalogID: NotRequired[str]
    Role: NotRequired[str]
    SampleSize: NotRequired[float]
    SecurityConfiguration: NotRequired[str]
    NumberOfWorkers: NotRequired[int]
    WorkerType: NotRequired[str]
    ComputationType: NotRequired[ComputationTypeType]
    Status: NotRequired[ColumnStatisticsStateType]
    CreationTime: NotRequired[datetime]
    LastUpdated: NotRequired[datetime]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    ErrorMessage: NotRequired[str]
    DPUSeconds: NotRequired[float]

class ExecutionAttemptTypeDef(TypedDict):
    Status: NotRequired[ExecutionStatusType]
    ColumnStatisticsTaskRunId: NotRequired[str]
    ExecutionTimestamp: NotRequired[datetime]
    ErrorMessage: NotRequired[str]

class ScheduleTypeDef(TypedDict):
    ScheduleExpression: NotRequired[str]
    State: NotRequired[ScheduleStateType]

TimestampTypeDef = Union[datetime, str]
ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "Name": str,
        "Type": NotRequired[str],
        "Comment": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
    },
)

class IcebergCompactionMetricsTypeDef(TypedDict):
    NumberOfBytesCompacted: NotRequired[int]
    NumberOfFilesCompacted: NotRequired[int]
    DpuHours: NotRequired[float]
    NumberOfDpus: NotRequired[int]
    JobDurationInHour: NotRequired[float]

class ConditionExpressionTypeDef(TypedDict):
    Condition: str
    TargetColumn: str
    Value: NotRequired[str]

class ConditionTypeDef(TypedDict):
    LogicalOperator: NotRequired[Literal["EQUALS"]]
    JobName: NotRequired[str]
    State: NotRequired[JobRunStateType]
    CrawlerName: NotRequired[str]
    CrawlState: NotRequired[CrawlStateType]

class ConfigurationObjectOutputTypeDef(TypedDict):
    DefaultValue: NotRequired[str]
    AllowedValues: NotRequired[List[str]]
    MinValue: NotRequired[str]
    MaxValue: NotRequired[str]

class ConfigurationObjectTypeDef(TypedDict):
    DefaultValue: NotRequired[str]
    AllowedValues: NotRequired[Sequence[str]]
    MinValue: NotRequired[str]
    MaxValue: NotRequired[str]

class ConfusionMatrixTypeDef(TypedDict):
    NumTruePositives: NotRequired[int]
    NumFalsePositives: NotRequired[int]
    NumTrueNegatives: NotRequired[int]
    NumFalseNegatives: NotRequired[int]

class ConnectionPasswordEncryptionTypeDef(TypedDict):
    ReturnConnectionPasswordEncrypted: bool
    AwsKmsKeyId: NotRequired[str]

class PhysicalConnectionRequirementsOutputTypeDef(TypedDict):
    SubnetId: NotRequired[str]
    SecurityGroupIdList: NotRequired[List[str]]
    AvailabilityZone: NotRequired[str]

class ConnectionsListOutputTypeDef(TypedDict):
    Connections: NotRequired[List[str]]

class ConnectionsListTypeDef(TypedDict):
    Connections: NotRequired[Sequence[str]]

class ConnectorDataTargetTypeDef(TypedDict):
    Name: str
    ConnectionType: str
    Data: Mapping[str, str]
    Inputs: NotRequired[Sequence[str]]

class CrawlTypeDef(TypedDict):
    State: NotRequired[CrawlStateType]
    StartedOn: NotRequired[datetime]
    CompletedOn: NotRequired[datetime]
    ErrorMessage: NotRequired[str]
    LogGroup: NotRequired[str]
    LogStream: NotRequired[str]

class CrawlerHistoryTypeDef(TypedDict):
    CrawlId: NotRequired[str]
    State: NotRequired[CrawlerHistoryStateType]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    Summary: NotRequired[str]
    ErrorMessage: NotRequired[str]
    LogGroup: NotRequired[str]
    LogStream: NotRequired[str]
    MessagePrefix: NotRequired[str]
    DPUHour: NotRequired[float]

class CrawlerMetricsTypeDef(TypedDict):
    CrawlerName: NotRequired[str]
    TimeLeftSeconds: NotRequired[float]
    StillEstimating: NotRequired[bool]
    LastRuntimeSeconds: NotRequired[float]
    MedianRuntimeSeconds: NotRequired[float]
    TablesCreated: NotRequired[int]
    TablesUpdated: NotRequired[int]
    TablesDeleted: NotRequired[int]

class DeltaTargetOutputTypeDef(TypedDict):
    DeltaTables: NotRequired[List[str]]
    ConnectionName: NotRequired[str]
    WriteManifest: NotRequired[bool]
    CreateNativeDeltaTable: NotRequired[bool]

class DynamoDBTargetTypeDef(TypedDict):
    Path: NotRequired[str]
    scanAll: NotRequired[bool]
    scanRate: NotRequired[float]

class HudiTargetOutputTypeDef(TypedDict):
    Paths: NotRequired[List[str]]
    ConnectionName: NotRequired[str]
    Exclusions: NotRequired[List[str]]
    MaximumTraversalDepth: NotRequired[int]

class IcebergTargetOutputTypeDef(TypedDict):
    Paths: NotRequired[List[str]]
    ConnectionName: NotRequired[str]
    Exclusions: NotRequired[List[str]]
    MaximumTraversalDepth: NotRequired[int]

class JdbcTargetOutputTypeDef(TypedDict):
    ConnectionName: NotRequired[str]
    Path: NotRequired[str]
    Exclusions: NotRequired[List[str]]
    EnableAdditionalMetadata: NotRequired[List[JdbcMetadataEntryType]]

class MongoDBTargetTypeDef(TypedDict):
    ConnectionName: NotRequired[str]
    Path: NotRequired[str]
    ScanAll: NotRequired[bool]

class S3TargetOutputTypeDef(TypedDict):
    Path: NotRequired[str]
    Exclusions: NotRequired[List[str]]
    ConnectionName: NotRequired[str]
    SampleSize: NotRequired[int]
    EventQueueArn: NotRequired[str]
    DlqEventQueueArn: NotRequired[str]

class DeltaTargetTypeDef(TypedDict):
    DeltaTables: NotRequired[Sequence[str]]
    ConnectionName: NotRequired[str]
    WriteManifest: NotRequired[bool]
    CreateNativeDeltaTable: NotRequired[bool]

class HudiTargetTypeDef(TypedDict):
    Paths: NotRequired[Sequence[str]]
    ConnectionName: NotRequired[str]
    Exclusions: NotRequired[Sequence[str]]
    MaximumTraversalDepth: NotRequired[int]

class IcebergTargetTypeDef(TypedDict):
    Paths: NotRequired[Sequence[str]]
    ConnectionName: NotRequired[str]
    Exclusions: NotRequired[Sequence[str]]
    MaximumTraversalDepth: NotRequired[int]

class JdbcTargetTypeDef(TypedDict):
    ConnectionName: NotRequired[str]
    Path: NotRequired[str]
    Exclusions: NotRequired[Sequence[str]]
    EnableAdditionalMetadata: NotRequired[Sequence[JdbcMetadataEntryType]]

class S3TargetTypeDef(TypedDict):
    Path: NotRequired[str]
    Exclusions: NotRequired[Sequence[str]]
    ConnectionName: NotRequired[str]
    SampleSize: NotRequired[int]
    EventQueueArn: NotRequired[str]
    DlqEventQueueArn: NotRequired[str]

class LakeFormationConfigurationTypeDef(TypedDict):
    UseLakeFormationCredentials: NotRequired[bool]
    AccountId: NotRequired[str]

class LastCrawlInfoTypeDef(TypedDict):
    Status: NotRequired[LastCrawlStatusType]
    ErrorMessage: NotRequired[str]
    LogGroup: NotRequired[str]
    LogStream: NotRequired[str]
    MessagePrefix: NotRequired[str]
    StartTime: NotRequired[datetime]

class LineageConfigurationTypeDef(TypedDict):
    CrawlerLineageSettings: NotRequired[CrawlerLineageSettingsType]

class RecrawlPolicyTypeDef(TypedDict):
    RecrawlBehavior: NotRequired[RecrawlBehaviorType]

class SchemaChangePolicyTypeDef(TypedDict):
    UpdateBehavior: NotRequired[UpdateBehaviorType]
    DeleteBehavior: NotRequired[DeleteBehaviorType]

class CrawlsFilterTypeDef(TypedDict):
    FieldName: NotRequired[FieldNameType]
    FilterOperator: NotRequired[FilterOperatorType]
    FieldValue: NotRequired[str]

class CreateBlueprintRequestTypeDef(TypedDict):
    Name: str
    BlueprintLocation: str
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CreateCsvClassifierRequestTypeDef(TypedDict):
    Name: str
    Delimiter: NotRequired[str]
    QuoteSymbol: NotRequired[str]
    ContainsHeader: NotRequired[CsvHeaderOptionType]
    Header: NotRequired[Sequence[str]]
    DisableValueTrimming: NotRequired[bool]
    AllowSingleColumn: NotRequired[bool]
    CustomDatatypeConfigured: NotRequired[bool]
    CustomDatatypes: NotRequired[Sequence[str]]
    Serde: NotRequired[CsvSerdeOptionType]

class CreateGrokClassifierRequestTypeDef(TypedDict):
    Classification: str
    Name: str
    GrokPattern: str
    CustomPatterns: NotRequired[str]

class CreateJsonClassifierRequestTypeDef(TypedDict):
    Name: str
    JsonPath: str

class CreateXMLClassifierRequestTypeDef(TypedDict):
    Classification: str
    Name: str
    RowTag: NotRequired[str]

class CreateColumnStatisticsTaskSettingsRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    Role: str
    Schedule: NotRequired[str]
    ColumnNameList: NotRequired[Sequence[str]]
    SampleSize: NotRequired[float]
    CatalogID: NotRequired[str]
    SecurityConfiguration: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CreateCustomEntityTypeRequestTypeDef(TypedDict):
    Name: str
    RegexString: str
    ContextWords: NotRequired[Sequence[str]]
    Tags: NotRequired[Mapping[str, str]]

class DataQualityTargetTableTypeDef(TypedDict):
    TableName: str
    DatabaseName: str
    CatalogId: NotRequired[str]

class CreateDevEndpointRequestTypeDef(TypedDict):
    EndpointName: str
    RoleArn: str
    SecurityGroupIds: NotRequired[Sequence[str]]
    SubnetId: NotRequired[str]
    PublicKey: NotRequired[str]
    PublicKeys: NotRequired[Sequence[str]]
    NumberOfNodes: NotRequired[int]
    WorkerType: NotRequired[WorkerTypeType]
    GlueVersion: NotRequired[str]
    NumberOfWorkers: NotRequired[int]
    ExtraPythonLibsS3Path: NotRequired[str]
    ExtraJarsS3Path: NotRequired[str]
    SecurityConfiguration: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    Arguments: NotRequired[Mapping[str, str]]

class TagTypeDef(TypedDict):
    key: NotRequired[str]
    value: NotRequired[str]

class SourceProcessingPropertiesTypeDef(TypedDict):
    RoleArn: NotRequired[str]

class TargetProcessingPropertiesTypeDef(TypedDict):
    RoleArn: NotRequired[str]
    KmsArn: NotRequired[str]
    ConnectionName: NotRequired[str]
    EventBusArn: NotRequired[str]

class IntegrationErrorTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class ExecutionPropertyTypeDef(TypedDict):
    MaxConcurrentRuns: NotRequired[int]

class JobCommandTypeDef(TypedDict):
    Name: NotRequired[str]
    ScriptLocation: NotRequired[str]
    PythonVersion: NotRequired[str]
    Runtime: NotRequired[str]

class SourceControlDetailsTypeDef(TypedDict):
    Provider: NotRequired[SourceControlProviderType]
    Repository: NotRequired[str]
    Owner: NotRequired[str]
    Branch: NotRequired[str]
    Folder: NotRequired[str]
    LastCommitId: NotRequired[str]
    AuthStrategy: NotRequired[SourceControlAuthStrategyType]
    AuthToken: NotRequired[str]

class PartitionIndexTypeDef(TypedDict):
    Keys: Sequence[str]
    IndexName: str

class CreateRegistryInputTypeDef(TypedDict):
    RegistryName: str
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class RegistryIdTypeDef(TypedDict):
    RegistryName: NotRequired[str]
    RegistryArn: NotRequired[str]

class SessionCommandTypeDef(TypedDict):
    Name: NotRequired[str]
    PythonVersion: NotRequired[str]

class EventBatchingConditionTypeDef(TypedDict):
    BatchSize: int
    BatchWindow: NotRequired[int]

class CreateWorkflowRequestTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    DefaultRunProperties: NotRequired[Mapping[str, str]]
    Tags: NotRequired[Mapping[str, str]]
    MaxConcurrentRuns: NotRequired[int]

class DQResultsPublishingOptionsTypeDef(TypedDict):
    EvaluationContext: NotRequired[str]
    ResultsS3Prefix: NotRequired[str]
    CloudWatchMetricsEnabled: NotRequired[bool]
    ResultsPublishingEnabled: NotRequired[bool]

class DQStopJobOnFailureOptionsTypeDef(TypedDict):
    StopJobOnFailureTiming: NotRequired[DQStopJobOnFailureTimingType]

class EncryptionAtRestTypeDef(TypedDict):
    CatalogEncryptionMode: CatalogEncryptionModeType
    SseAwsKmsKeyId: NotRequired[str]
    CatalogEncryptionServiceRole: NotRequired[str]

class DataLakePrincipalTypeDef(TypedDict):
    DataLakePrincipalIdentifier: NotRequired[str]

class DataQualityAnalyzerResultTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    EvaluationMessage: NotRequired[str]
    EvaluatedMetrics: NotRequired[Dict[str, float]]

class DataQualityEncryptionTypeDef(TypedDict):
    DataQualityEncryptionMode: NotRequired[DataQualityEncryptionModeType]
    KmsKeyArn: NotRequired[str]

class DataQualityEvaluationRunAdditionalRunOptionsTypeDef(TypedDict):
    CloudWatchMetricsEnabled: NotRequired[bool]
    ResultsS3Prefix: NotRequired[str]
    CompositeRuleEvaluationMethod: NotRequired[DQCompositeRuleEvaluationMethodType]

class DataQualityMetricValuesTypeDef(TypedDict):
    ActualValue: NotRequired[float]
    ExpectedValue: NotRequired[float]
    LowerLimit: NotRequired[float]
    UpperLimit: NotRequired[float]

class DataQualityRuleResultTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    EvaluationMessage: NotRequired[str]
    Result: NotRequired[DataQualityRuleResultStatusType]
    EvaluatedMetrics: NotRequired[Dict[str, float]]
    EvaluatedRule: NotRequired[str]

class GlueTableOutputTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    CatalogId: NotRequired[str]
    ConnectionName: NotRequired[str]
    AdditionalOptions: NotRequired[Dict[str, str]]

class DatabaseIdentifierTypeDef(TypedDict):
    CatalogId: NotRequired[str]
    DatabaseName: NotRequired[str]
    Region: NotRequired[str]

class FederatedDatabaseTypeDef(TypedDict):
    Identifier: NotRequired[str]
    ConnectionName: NotRequired[str]

class DatatypeTypeDef(TypedDict):
    Id: str
    Label: str

class DecimalNumberOutputTypeDef(TypedDict):
    UnscaledValue: bytes
    Scale: int

class DeleteBlueprintRequestTypeDef(TypedDict):
    Name: str

class DeleteCatalogRequestTypeDef(TypedDict):
    CatalogId: str

class DeleteClassifierRequestTypeDef(TypedDict):
    Name: str

class DeleteColumnStatisticsForPartitionRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    ColumnName: str
    CatalogId: NotRequired[str]

class DeleteColumnStatisticsForTableRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    ColumnName: str
    CatalogId: NotRequired[str]

class DeleteColumnStatisticsTaskSettingsRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str

class DeleteConnectionRequestTypeDef(TypedDict):
    ConnectionName: str
    CatalogId: NotRequired[str]

class DeleteCrawlerRequestTypeDef(TypedDict):
    Name: str

class DeleteCustomEntityTypeRequestTypeDef(TypedDict):
    Name: str

class DeleteDataQualityRulesetRequestTypeDef(TypedDict):
    Name: str

class DeleteDatabaseRequestTypeDef(TypedDict):
    Name: str
    CatalogId: NotRequired[str]

class DeleteDevEndpointRequestTypeDef(TypedDict):
    EndpointName: str

class DeleteIntegrationRequestTypeDef(TypedDict):
    IntegrationIdentifier: str

class DeleteIntegrationTablePropertiesRequestTypeDef(TypedDict):
    ResourceArn: str
    TableName: str

class DeleteJobRequestTypeDef(TypedDict):
    JobName: str

class DeleteMLTransformRequestTypeDef(TypedDict):
    TransformId: str

class DeletePartitionIndexRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    IndexName: str
    CatalogId: NotRequired[str]

class DeletePartitionRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    CatalogId: NotRequired[str]

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    PolicyHashCondition: NotRequired[str]
    ResourceArn: NotRequired[str]

class SchemaIdTypeDef(TypedDict):
    SchemaArn: NotRequired[str]
    SchemaName: NotRequired[str]
    RegistryName: NotRequired[str]

class DeleteSecurityConfigurationRequestTypeDef(TypedDict):
    Name: str

class DeleteSessionRequestTypeDef(TypedDict):
    Id: str
    RequestOrigin: NotRequired[str]

DeleteTableOptimizerRequestTypeDef = TypedDict(
    "DeleteTableOptimizerRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Type": TableOptimizerTypeType,
    },
)

class DeleteTableRequestTypeDef(TypedDict):
    DatabaseName: str
    Name: str
    CatalogId: NotRequired[str]
    TransactionId: NotRequired[str]

class DeleteTableVersionRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    VersionId: str
    CatalogId: NotRequired[str]

class DeleteTriggerRequestTypeDef(TypedDict):
    Name: str

class DeleteUsageProfileRequestTypeDef(TypedDict):
    Name: str

class DeleteUserDefinedFunctionRequestTypeDef(TypedDict):
    DatabaseName: str
    FunctionName: str
    CatalogId: NotRequired[str]

class DeleteWorkflowRequestTypeDef(TypedDict):
    Name: str

class DescribeConnectionTypeRequestTypeDef(TypedDict):
    ConnectionType: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeEntityRequestTypeDef(TypedDict):
    ConnectionName: str
    EntityName: str
    CatalogId: NotRequired[str]
    NextToken: NotRequired[str]
    DataStoreApiVersion: NotRequired[str]

class FieldTypeDef(TypedDict):
    FieldName: NotRequired[str]
    Label: NotRequired[str]
    Description: NotRequired[str]
    FieldType: NotRequired[FieldDataTypeType]
    IsPrimaryKey: NotRequired[bool]
    IsNullable: NotRequired[bool]
    IsRetrievable: NotRequired[bool]
    IsFilterable: NotRequired[bool]
    IsPartitionable: NotRequired[bool]
    IsCreateable: NotRequired[bool]
    IsUpdateable: NotRequired[bool]
    IsUpsertable: NotRequired[bool]
    IsDefaultOnCreate: NotRequired[bool]
    SupportedValues: NotRequired[List[str]]
    SupportedFilterOperators: NotRequired[List[FieldFilterOperatorType]]
    ParentField: NotRequired[str]
    NativeDataType: NotRequired[str]
    CustomProperties: NotRequired[Dict[str, str]]

class DescribeInboundIntegrationsRequestTypeDef(TypedDict):
    IntegrationArn: NotRequired[str]
    Marker: NotRequired[str]
    MaxRecords: NotRequired[int]
    TargetArn: NotRequired[str]

class IntegrationFilterTypeDef(TypedDict):
    Name: NotRequired[str]
    Values: NotRequired[Sequence[str]]

class DevEndpointCustomLibrariesTypeDef(TypedDict):
    ExtraPythonLibsS3Path: NotRequired[str]
    ExtraJarsS3Path: NotRequired[str]

class DirectSchemaChangePolicyTypeDef(TypedDict):
    EnableUpdateCatalog: NotRequired[bool]
    UpdateBehavior: NotRequired[UpdateCatalogBehaviorType]
    Table: NotRequired[str]
    Database: NotRequired[str]

class DropDuplicatesTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Columns: NotRequired[Sequence[Sequence[str]]]

class DropFieldsTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Paths: Sequence[Sequence[str]]

class NullCheckBoxListTypeDef(TypedDict):
    IsEmpty: NotRequired[bool]
    IsNullString: NotRequired[bool]
    IsNegOne: NotRequired[bool]

TransformConfigParameterOutputTypeDef = TypedDict(
    "TransformConfigParameterOutputTypeDef",
    {
        "Name": str,
        "Type": ParamTypeType,
        "ValidationRule": NotRequired[str],
        "ValidationMessage": NotRequired[str],
        "Value": NotRequired[List[str]],
        "ListType": NotRequired[ParamTypeType],
        "IsOptional": NotRequired[bool],
    },
)

class EdgeTypeDef(TypedDict):
    SourceId: NotRequired[str]
    DestinationId: NotRequired[str]

class JobBookmarksEncryptionTypeDef(TypedDict):
    JobBookmarksEncryptionMode: NotRequired[JobBookmarksEncryptionModeType]
    KmsKeyArn: NotRequired[str]

class S3EncryptionTypeDef(TypedDict):
    S3EncryptionMode: NotRequired[S3EncryptionModeType]
    KmsKeyArn: NotRequired[str]

class EntityTypeDef(TypedDict):
    EntityName: NotRequired[str]
    Label: NotRequired[str]
    IsParentEntity: NotRequired[bool]
    Description: NotRequired[str]
    Category: NotRequired[str]
    CustomProperties: NotRequired[Dict[str, str]]

class ErrorDetailsTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class ExportLabelsTaskRunPropertiesTypeDef(TypedDict):
    OutputS3Path: NotRequired[str]

class FederatedTableTypeDef(TypedDict):
    Identifier: NotRequired[str]
    DatabaseIdentifier: NotRequired[str]
    ConnectionName: NotRequired[str]

class FillMissingValuesTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    ImputedPath: str
    FilledPath: NotRequired[str]

FilterValueOutputTypeDef = TypedDict(
    "FilterValueOutputTypeDef",
    {
        "Type": FilterValueTypeType,
        "Value": List[str],
    },
)
FilterValueTypeDef = TypedDict(
    "FilterValueTypeDef",
    {
        "Type": FilterValueTypeType,
        "Value": Sequence[str],
    },
)

class FindMatchesParametersTypeDef(TypedDict):
    PrimaryKeyColumnName: NotRequired[str]
    PrecisionRecallTradeoff: NotRequired[float]
    AccuracyCostTradeoff: NotRequired[float]
    EnforceProvidedLabels: NotRequired[bool]

class FindMatchesTaskRunPropertiesTypeDef(TypedDict):
    JobId: NotRequired[str]
    JobName: NotRequired[str]
    JobRunId: NotRequired[str]

class GetBlueprintRequestTypeDef(TypedDict):
    Name: str
    IncludeBlueprint: NotRequired[bool]
    IncludeParameterSpec: NotRequired[bool]

class GetBlueprintRunRequestTypeDef(TypedDict):
    BlueprintName: str
    RunId: str

class GetBlueprintRunsRequestTypeDef(TypedDict):
    BlueprintName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetCatalogImportStatusRequestTypeDef(TypedDict):
    CatalogId: NotRequired[str]

class GetCatalogRequestTypeDef(TypedDict):
    CatalogId: str

class GetCatalogsRequestTypeDef(TypedDict):
    ParentCatalogId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Recursive: NotRequired[bool]
    IncludeRoot: NotRequired[bool]

class GetClassifierRequestTypeDef(TypedDict):
    Name: str

class GetClassifiersRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetColumnStatisticsForPartitionRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    ColumnNames: Sequence[str]
    CatalogId: NotRequired[str]

class GetColumnStatisticsForTableRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    ColumnNames: Sequence[str]
    CatalogId: NotRequired[str]

class GetColumnStatisticsTaskRunRequestTypeDef(TypedDict):
    ColumnStatisticsTaskRunId: str

class GetColumnStatisticsTaskRunsRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetColumnStatisticsTaskSettingsRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str

class GetConnectionRequestTypeDef(TypedDict):
    Name: str
    CatalogId: NotRequired[str]
    HidePassword: NotRequired[bool]
    ApplyOverrideForComputeEnvironment: NotRequired[ComputeEnvironmentType]

class GetConnectionsFilterTypeDef(TypedDict):
    MatchCriteria: NotRequired[Sequence[str]]
    ConnectionType: NotRequired[ConnectionTypeType]
    ConnectionSchemaVersion: NotRequired[int]

class GetCrawlerMetricsRequestTypeDef(TypedDict):
    CrawlerNameList: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetCrawlerRequestTypeDef(TypedDict):
    Name: str

class GetCrawlersRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetCustomEntityTypeRequestTypeDef(TypedDict):
    Name: str

class GetDataCatalogEncryptionSettingsRequestTypeDef(TypedDict):
    CatalogId: NotRequired[str]

class GetDataQualityModelRequestTypeDef(TypedDict):
    ProfileId: str
    StatisticId: NotRequired[str]

class GetDataQualityModelResultRequestTypeDef(TypedDict):
    StatisticId: str
    ProfileId: str

class StatisticModelResultTypeDef(TypedDict):
    LowerBound: NotRequired[float]
    UpperBound: NotRequired[float]
    PredictedValue: NotRequired[float]
    ActualValue: NotRequired[float]
    Date: NotRequired[datetime]
    InclusionAnnotation: NotRequired[InclusionAnnotationValueType]

class GetDataQualityResultRequestTypeDef(TypedDict):
    ResultId: str

class GetDataQualityRuleRecommendationRunRequestTypeDef(TypedDict):
    RunId: str

class GetDataQualityRulesetEvaluationRunRequestTypeDef(TypedDict):
    RunId: str

class GetDataQualityRulesetRequestTypeDef(TypedDict):
    Name: str

class GetDatabaseRequestTypeDef(TypedDict):
    Name: str
    CatalogId: NotRequired[str]

class GetDatabasesRequestTypeDef(TypedDict):
    CatalogId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    ResourceShareType: NotRequired[ResourceShareTypeType]
    AttributesToGet: NotRequired[Sequence[Literal["NAME"]]]

class GetDataflowGraphRequestTypeDef(TypedDict):
    PythonScript: NotRequired[str]

class GetDevEndpointRequestTypeDef(TypedDict):
    EndpointName: str

class GetDevEndpointsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetEntityRecordsRequestTypeDef(TypedDict):
    EntityName: str
    Limit: int
    ConnectionName: NotRequired[str]
    CatalogId: NotRequired[str]
    NextToken: NotRequired[str]
    DataStoreApiVersion: NotRequired[str]
    ConnectionOptions: NotRequired[Mapping[str, str]]
    FilterPredicate: NotRequired[str]
    OrderBy: NotRequired[str]
    SelectedFields: NotRequired[Sequence[str]]

class GetIntegrationResourcePropertyRequestTypeDef(TypedDict):
    ResourceArn: str

class GetIntegrationTablePropertiesRequestTypeDef(TypedDict):
    ResourceArn: str
    TableName: str

class SourceTableConfigOutputTypeDef(TypedDict):
    Fields: NotRequired[List[str]]
    FilterPredicate: NotRequired[str]
    PrimaryKey: NotRequired[List[str]]
    RecordUpdateField: NotRequired[str]

class GetJobBookmarkRequestTypeDef(TypedDict):
    JobName: str
    RunId: NotRequired[str]

class JobBookmarkEntryTypeDef(TypedDict):
    JobName: NotRequired[str]
    Version: NotRequired[int]
    Run: NotRequired[int]
    Attempt: NotRequired[int]
    PreviousRunId: NotRequired[str]
    RunId: NotRequired[str]
    JobBookmark: NotRequired[str]

class GetJobRequestTypeDef(TypedDict):
    JobName: str

class GetJobRunRequestTypeDef(TypedDict):
    JobName: str
    RunId: str
    PredecessorsIncluded: NotRequired[bool]

class GetJobRunsRequestTypeDef(TypedDict):
    JobName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetJobsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetMLTaskRunRequestTypeDef(TypedDict):
    TransformId: str
    TaskRunId: str

class TaskRunSortCriteriaTypeDef(TypedDict):
    Column: TaskRunSortColumnTypeType
    SortDirection: SortDirectionTypeType

class GetMLTransformRequestTypeDef(TypedDict):
    TransformId: str

class SchemaColumnTypeDef(TypedDict):
    Name: NotRequired[str]
    DataType: NotRequired[str]

class TransformSortCriteriaTypeDef(TypedDict):
    Column: TransformSortColumnTypeType
    SortDirection: SortDirectionTypeType

class MappingEntryTypeDef(TypedDict):
    SourceTable: NotRequired[str]
    SourcePath: NotRequired[str]
    SourceType: NotRequired[str]
    TargetTable: NotRequired[str]
    TargetPath: NotRequired[str]
    TargetType: NotRequired[str]

class GetPartitionIndexesRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    CatalogId: NotRequired[str]
    NextToken: NotRequired[str]

class GetPartitionRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    CatalogId: NotRequired[str]

class SegmentTypeDef(TypedDict):
    SegmentNumber: int
    TotalSegments: int

class GetResourcePoliciesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GluePolicyTypeDef(TypedDict):
    PolicyInJson: NotRequired[str]
    PolicyHash: NotRequired[str]
    CreateTime: NotRequired[datetime]
    UpdateTime: NotRequired[datetime]

class GetResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: NotRequired[str]

class SchemaVersionNumberTypeDef(TypedDict):
    LatestVersion: NotRequired[bool]
    VersionNumber: NotRequired[int]

class GetSecurityConfigurationRequestTypeDef(TypedDict):
    Name: str

class GetSecurityConfigurationsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetSessionRequestTypeDef(TypedDict):
    Id: str
    RequestOrigin: NotRequired[str]

class GetStatementRequestTypeDef(TypedDict):
    SessionId: str
    Id: int
    RequestOrigin: NotRequired[str]

GetTableOptimizerRequestTypeDef = TypedDict(
    "GetTableOptimizerRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Type": TableOptimizerTypeType,
    },
)

class GetTableVersionRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    CatalogId: NotRequired[str]
    VersionId: NotRequired[str]

class GetTableVersionsRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    CatalogId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetTagsRequestTypeDef(TypedDict):
    ResourceArn: str

class GetTriggerRequestTypeDef(TypedDict):
    Name: str

class GetTriggersRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    DependentJobName: NotRequired[str]
    MaxResults: NotRequired[int]

class SupportedDialectTypeDef(TypedDict):
    Dialect: NotRequired[ViewDialectType]
    DialectVersion: NotRequired[str]

class GetUsageProfileRequestTypeDef(TypedDict):
    Name: str

class GetUserDefinedFunctionRequestTypeDef(TypedDict):
    DatabaseName: str
    FunctionName: str
    CatalogId: NotRequired[str]

GetUserDefinedFunctionsRequestTypeDef = TypedDict(
    "GetUserDefinedFunctionsRequestTypeDef",
    {
        "Pattern": str,
        "CatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

class GetWorkflowRequestTypeDef(TypedDict):
    Name: str
    IncludeGraph: NotRequired[bool]

class GetWorkflowRunPropertiesRequestTypeDef(TypedDict):
    Name: str
    RunId: str

class GetWorkflowRunRequestTypeDef(TypedDict):
    Name: str
    RunId: str
    IncludeGraph: NotRequired[bool]

class GetWorkflowRunsRequestTypeDef(TypedDict):
    Name: str
    IncludeGraph: NotRequired[bool]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

GlueStudioSchemaColumnTypeDef = TypedDict(
    "GlueStudioSchemaColumnTypeDef",
    {
        "Name": str,
        "Type": NotRequired[str],
    },
)

class GlueTableTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    CatalogId: NotRequired[str]
    ConnectionName: NotRequired[str]
    AdditionalOptions: NotRequired[Mapping[str, str]]

class S3SourceAdditionalOptionsTypeDef(TypedDict):
    BoundedSize: NotRequired[int]
    BoundedFiles: NotRequired[int]

class IcebergInputTypeDef(TypedDict):
    MetadataOperation: Literal["CREATE"]
    Version: NotRequired[str]

class IcebergOrphanFileDeletionConfigurationTypeDef(TypedDict):
    orphanFileRetentionPeriodInDays: NotRequired[int]
    location: NotRequired[str]

class IcebergOrphanFileDeletionMetricsTypeDef(TypedDict):
    NumberOfOrphanFilesDeleted: NotRequired[int]
    DpuHours: NotRequired[float]
    NumberOfDpus: NotRequired[int]
    JobDurationInHour: NotRequired[float]

class IcebergRetentionConfigurationTypeDef(TypedDict):
    snapshotRetentionPeriodInDays: NotRequired[int]
    numberOfSnapshotsToRetain: NotRequired[int]
    cleanExpiredFiles: NotRequired[bool]

class IcebergRetentionMetricsTypeDef(TypedDict):
    NumberOfDataFilesDeleted: NotRequired[int]
    NumberOfManifestFilesDeleted: NotRequired[int]
    NumberOfManifestListsDeleted: NotRequired[int]
    DpuHours: NotRequired[float]
    NumberOfDpus: NotRequired[int]
    JobDurationInHour: NotRequired[float]

class ImportCatalogToGlueRequestTypeDef(TypedDict):
    CatalogId: NotRequired[str]

class ImportLabelsTaskRunPropertiesTypeDef(TypedDict):
    InputS3Path: NotRequired[str]
    Replace: NotRequired[bool]

class IntegrationPartitionTypeDef(TypedDict):
    FieldName: NotRequired[str]
    FunctionSpec: NotRequired[str]

class JDBCConnectorOptionsOutputTypeDef(TypedDict):
    FilterPredicate: NotRequired[str]
    PartitionColumn: NotRequired[str]
    LowerBound: NotRequired[int]
    UpperBound: NotRequired[int]
    NumPartitions: NotRequired[int]
    JobBookmarkKeys: NotRequired[List[str]]
    JobBookmarkKeysSortOrder: NotRequired[str]
    DataTypeMapping: NotRequired[Dict[JDBCDataTypeType, GlueRecordTypeType]]

class JDBCConnectorOptionsTypeDef(TypedDict):
    FilterPredicate: NotRequired[str]
    PartitionColumn: NotRequired[str]
    LowerBound: NotRequired[int]
    UpperBound: NotRequired[int]
    NumPartitions: NotRequired[int]
    JobBookmarkKeys: NotRequired[Sequence[str]]
    JobBookmarkKeysSortOrder: NotRequired[str]
    DataTypeMapping: NotRequired[Mapping[JDBCDataTypeType, GlueRecordTypeType]]

class PredecessorTypeDef(TypedDict):
    JobName: NotRequired[str]
    RunId: NotRequired[str]

class JoinColumnOutputTypeDef(TypedDict):
    From: str
    Keys: List[List[str]]

class JoinColumnTypeDef(TypedDict):
    From: str
    Keys: Sequence[Sequence[str]]

KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef",
    {
        "Name": str,
        "Type": str,
    },
)

class LabelingSetGenerationTaskRunPropertiesTypeDef(TypedDict):
    OutputS3Path: NotRequired[str]

class ListBlueprintsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Tags: NotRequired[Mapping[str, str]]

class ListColumnStatisticsTaskRunsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListConnectionTypesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListCrawlersRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class ListCustomEntityTypesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Tags: NotRequired[Mapping[str, str]]

class ListDevEndpointsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Tags: NotRequired[Mapping[str, str]]

class ListEntitiesRequestTypeDef(TypedDict):
    ConnectionName: NotRequired[str]
    CatalogId: NotRequired[str]
    ParentEntityName: NotRequired[str]
    NextToken: NotRequired[str]
    DataStoreApiVersion: NotRequired[str]

class ListJobsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Tags: NotRequired[Mapping[str, str]]

class ListRegistriesInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class RegistryListItemTypeDef(TypedDict):
    RegistryName: NotRequired[str]
    RegistryArn: NotRequired[str]
    Description: NotRequired[str]
    Status: NotRequired[RegistryStatusType]
    CreatedTime: NotRequired[str]
    UpdatedTime: NotRequired[str]

class SchemaVersionListItemTypeDef(TypedDict):
    SchemaArn: NotRequired[str]
    SchemaVersionId: NotRequired[str]
    VersionNumber: NotRequired[int]
    Status: NotRequired[SchemaVersionStatusType]
    CreatedTime: NotRequired[str]

class SchemaListItemTypeDef(TypedDict):
    RegistryName: NotRequired[str]
    SchemaName: NotRequired[str]
    SchemaArn: NotRequired[str]
    Description: NotRequired[str]
    SchemaStatus: NotRequired[SchemaStatusType]
    CreatedTime: NotRequired[str]
    UpdatedTime: NotRequired[str]

class ListSessionsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Tags: NotRequired[Mapping[str, str]]
    RequestOrigin: NotRequired[str]

class ListStatementsRequestTypeDef(TypedDict):
    SessionId: str
    RequestOrigin: NotRequired[str]
    NextToken: NotRequired[str]

ListTableOptimizerRunsRequestTypeDef = TypedDict(
    "ListTableOptimizerRunsRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Type": TableOptimizerTypeType,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

class ListTriggersRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    DependentJobName: NotRequired[str]
    MaxResults: NotRequired[int]
    Tags: NotRequired[Mapping[str, str]]

class ListUsageProfilesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class UsageProfileDefinitionTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    CreatedOn: NotRequired[datetime]
    LastModifiedOn: NotRequired[datetime]

class ListWorkflowsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class MLUserDataEncryptionTypeDef(TypedDict):
    MlUserDataEncryptionMode: MLUserDataEncryptionModeStringType
    KmsKeyId: NotRequired[str]

class MappingTypeDef(TypedDict):
    ToKey: NotRequired[str]
    FromPath: NotRequired[Sequence[str]]
    FromType: NotRequired[str]
    ToType: NotRequired[str]
    Dropped: NotRequired[bool]
    Children: NotRequired[Sequence[Mapping[str, Any]]]

class MergeTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Source: str
    PrimaryKeys: Sequence[Sequence[str]]

class OtherMetadataValueListItemTypeDef(TypedDict):
    MetadataValue: NotRequired[str]
    CreatedTime: NotRequired[str]

class MetadataKeyValuePairTypeDef(TypedDict):
    MetadataKey: NotRequired[str]
    MetadataValue: NotRequired[str]

class MicrosoftSQLServerCatalogTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str

class ModifyIntegrationRequestTypeDef(TypedDict):
    IntegrationIdentifier: str
    Description: NotRequired[str]
    DataFilter: NotRequired[str]
    IntegrationName: NotRequired[str]

class MySQLCatalogTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str

class OAuth2ClientApplicationTypeDef(TypedDict):
    UserManagedClientApplicationClientId: NotRequired[str]
    AWSManagedClientApplicationReference: NotRequired[str]

class OAuth2CredentialsTypeDef(TypedDict):
    UserManagedClientApplicationClientSecret: NotRequired[str]
    AccessToken: NotRequired[str]
    RefreshToken: NotRequired[str]
    JwtToken: NotRequired[str]

class OracleSQLCatalogTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str

class OrderTypeDef(TypedDict):
    Column: str
    SortOrder: int

class PIIDetectionTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    PiiType: PiiTypeType
    EntityTypesToDetect: Sequence[str]
    OutputColumnName: NotRequired[str]
    SampleFraction: NotRequired[float]
    ThresholdFraction: NotRequired[float]
    MaskValue: NotRequired[str]

class PartitionValueListTypeDef(TypedDict):
    Values: Sequence[str]

class PhysicalConnectionRequirementsTypeDef(TypedDict):
    SubnetId: NotRequired[str]
    SecurityGroupIdList: NotRequired[Sequence[str]]
    AvailabilityZone: NotRequired[str]

class PostgreSQLCatalogTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str

class PropertyPredicateTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]
    Comparator: NotRequired[ComparatorType]

class PutDataQualityProfileAnnotationRequestTypeDef(TypedDict):
    ProfileId: str
    InclusionAnnotation: InclusionAnnotationValueType

class PutResourcePolicyRequestTypeDef(TypedDict):
    PolicyInJson: str
    ResourceArn: NotRequired[str]
    PolicyHashCondition: NotRequired[str]
    PolicyExistsCondition: NotRequired[ExistConditionType]
    EnableHybrid: NotRequired[EnableHybridValuesType]

class PutWorkflowRunPropertiesRequestTypeDef(TypedDict):
    Name: str
    RunId: str
    RunProperties: Mapping[str, str]

class RecipeActionOutputTypeDef(TypedDict):
    Operation: str
    Parameters: NotRequired[Dict[str, str]]

class RecipeActionTypeDef(TypedDict):
    Operation: str
    Parameters: NotRequired[Mapping[str, str]]

class RecipeReferenceTypeDef(TypedDict):
    RecipeArn: str
    RecipeVersion: str

class UpsertRedshiftTargetOptionsOutputTypeDef(TypedDict):
    TableLocation: NotRequired[str]
    ConnectionName: NotRequired[str]
    UpsertKeys: NotRequired[List[str]]

class RenameFieldTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    SourcePath: Sequence[str]
    TargetPath: Sequence[str]

class ResetJobBookmarkRequestTypeDef(TypedDict):
    JobName: str
    RunId: NotRequired[str]

class ResourceUriTypeDef(TypedDict):
    ResourceType: NotRequired[ResourceTypeType]
    Uri: NotRequired[str]

class ResumeWorkflowRunRequestTypeDef(TypedDict):
    Name: str
    RunId: str
    NodeIds: Sequence[str]

class RunIdentifierTypeDef(TypedDict):
    RunId: NotRequired[str]
    JobRunId: NotRequired[str]

class RunMetricsTypeDef(TypedDict):
    NumberOfBytesCompacted: NotRequired[str]
    NumberOfFilesCompacted: NotRequired[str]
    NumberOfDpus: NotRequired[str]
    JobDurationInHour: NotRequired[str]

class RunStatementRequestTypeDef(TypedDict):
    SessionId: str
    Code: str
    RequestOrigin: NotRequired[str]

class S3DirectSourceAdditionalOptionsTypeDef(TypedDict):
    BoundedSize: NotRequired[int]
    BoundedFiles: NotRequired[int]
    EnableSamplePath: NotRequired[bool]
    SamplePath: NotRequired[str]

class SortCriterionTypeDef(TypedDict):
    FieldName: NotRequired[str]
    Sort: NotRequired[SortType]

class SelectFieldsTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Paths: Sequence[Sequence[str]]

class SelectFromCollectionTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Index: int

class SerDeInfoOutputTypeDef(TypedDict):
    Name: NotRequired[str]
    SerializationLibrary: NotRequired[str]
    Parameters: NotRequired[Dict[str, str]]

class SerDeInfoTypeDef(TypedDict):
    Name: NotRequired[str]
    SerializationLibrary: NotRequired[str]
    Parameters: NotRequired[Mapping[str, str]]

class SkewedInfoOutputTypeDef(TypedDict):
    SkewedColumnNames: NotRequired[List[str]]
    SkewedColumnValues: NotRequired[List[str]]
    SkewedColumnValueLocationMaps: NotRequired[Dict[str, str]]

class SkewedInfoTypeDef(TypedDict):
    SkewedColumnNames: NotRequired[Sequence[str]]
    SkewedColumnValues: NotRequired[Sequence[str]]
    SkewedColumnValueLocationMaps: NotRequired[Mapping[str, str]]

class SourceTableConfigTypeDef(TypedDict):
    Fields: NotRequired[Sequence[str]]
    FilterPredicate: NotRequired[str]
    PrimaryKey: NotRequired[Sequence[str]]
    RecordUpdateField: NotRequired[str]

class SqlAliasTypeDef(TypedDict):
    From: str
    Alias: str

class SpigotTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Topk: NotRequired[int]
    Prob: NotRequired[float]

class SplitFieldsTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Paths: Sequence[Sequence[str]]

class StartBlueprintRunRequestTypeDef(TypedDict):
    BlueprintName: str
    RoleArn: str
    Parameters: NotRequired[str]

class StartColumnStatisticsTaskRunRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    Role: str
    ColumnNameList: NotRequired[Sequence[str]]
    SampleSize: NotRequired[float]
    CatalogID: NotRequired[str]
    SecurityConfiguration: NotRequired[str]

class StartColumnStatisticsTaskRunScheduleRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str

class StartCrawlerRequestTypeDef(TypedDict):
    Name: str

class StartCrawlerScheduleRequestTypeDef(TypedDict):
    CrawlerName: str

class StartExportLabelsTaskRunRequestTypeDef(TypedDict):
    TransformId: str
    OutputS3Path: str

class StartImportLabelsTaskRunRequestTypeDef(TypedDict):
    TransformId: str
    InputS3Path: str
    ReplaceAllLabels: NotRequired[bool]

class StartMLEvaluationTaskRunRequestTypeDef(TypedDict):
    TransformId: str

class StartMLLabelingSetGenerationTaskRunRequestTypeDef(TypedDict):
    TransformId: str
    OutputS3Path: str

class StartTriggerRequestTypeDef(TypedDict):
    Name: str

class StartWorkflowRunRequestTypeDef(TypedDict):
    Name: str
    RunProperties: NotRequired[Mapping[str, str]]

class StartingEventBatchConditionTypeDef(TypedDict):
    BatchSize: NotRequired[int]
    BatchWindow: NotRequired[int]

class StatementOutputDataTypeDef(TypedDict):
    TextPlain: NotRequired[str]

class TimestampedInclusionAnnotationTypeDef(TypedDict):
    Value: NotRequired[InclusionAnnotationValueType]
    LastModifiedOn: NotRequired[datetime]

class StopColumnStatisticsTaskRunRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str

class StopColumnStatisticsTaskRunScheduleRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str

class StopCrawlerRequestTypeDef(TypedDict):
    Name: str

class StopCrawlerScheduleRequestTypeDef(TypedDict):
    CrawlerName: str

class StopSessionRequestTypeDef(TypedDict):
    Id: str
    RequestOrigin: NotRequired[str]

class StopTriggerRequestTypeDef(TypedDict):
    Name: str

class StopWorkflowRunRequestTypeDef(TypedDict):
    Name: str
    RunId: str

class TableIdentifierTypeDef(TypedDict):
    CatalogId: NotRequired[str]
    DatabaseName: NotRequired[str]
    Name: NotRequired[str]
    Region: NotRequired[str]

class TableOptimizerVpcConfigurationTypeDef(TypedDict):
    glueConnectionName: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagsToAdd: Mapping[str, str]

TransformConfigParameterTypeDef = TypedDict(
    "TransformConfigParameterTypeDef",
    {
        "Name": str,
        "Type": ParamTypeType,
        "ValidationRule": NotRequired[str],
        "ValidationMessage": NotRequired[str],
        "Value": NotRequired[Sequence[str]],
        "ListType": NotRequired[ParamTypeType],
        "IsOptional": NotRequired[bool],
    },
)

class UnionTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    UnionType: UnionTypeType

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagsToRemove: Sequence[str]

class UpdateBlueprintRequestTypeDef(TypedDict):
    Name: str
    BlueprintLocation: str
    Description: NotRequired[str]

class UpdateCsvClassifierRequestTypeDef(TypedDict):
    Name: str
    Delimiter: NotRequired[str]
    QuoteSymbol: NotRequired[str]
    ContainsHeader: NotRequired[CsvHeaderOptionType]
    Header: NotRequired[Sequence[str]]
    DisableValueTrimming: NotRequired[bool]
    AllowSingleColumn: NotRequired[bool]
    CustomDatatypeConfigured: NotRequired[bool]
    CustomDatatypes: NotRequired[Sequence[str]]
    Serde: NotRequired[CsvSerdeOptionType]

class UpdateGrokClassifierRequestTypeDef(TypedDict):
    Name: str
    Classification: NotRequired[str]
    GrokPattern: NotRequired[str]
    CustomPatterns: NotRequired[str]

class UpdateJsonClassifierRequestTypeDef(TypedDict):
    Name: str
    JsonPath: NotRequired[str]

class UpdateXMLClassifierRequestTypeDef(TypedDict):
    Name: str
    Classification: NotRequired[str]
    RowTag: NotRequired[str]

class UpdateColumnStatisticsTaskSettingsRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    Role: NotRequired[str]
    Schedule: NotRequired[str]
    ColumnNameList: NotRequired[Sequence[str]]
    SampleSize: NotRequired[float]
    CatalogID: NotRequired[str]
    SecurityConfiguration: NotRequired[str]

class UpdateCrawlerScheduleRequestTypeDef(TypedDict):
    CrawlerName: str
    Schedule: NotRequired[str]

class UpdateDataQualityRulesetRequestTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    Ruleset: NotRequired[str]

class UpdateJobFromSourceControlRequestTypeDef(TypedDict):
    JobName: NotRequired[str]
    Provider: NotRequired[SourceControlProviderType]
    RepositoryName: NotRequired[str]
    RepositoryOwner: NotRequired[str]
    BranchName: NotRequired[str]
    Folder: NotRequired[str]
    CommitId: NotRequired[str]
    AuthStrategy: NotRequired[SourceControlAuthStrategyType]
    AuthToken: NotRequired[str]

class UpdateSourceControlFromJobRequestTypeDef(TypedDict):
    JobName: NotRequired[str]
    Provider: NotRequired[SourceControlProviderType]
    RepositoryName: NotRequired[str]
    RepositoryOwner: NotRequired[str]
    BranchName: NotRequired[str]
    Folder: NotRequired[str]
    CommitId: NotRequired[str]
    AuthStrategy: NotRequired[SourceControlAuthStrategyType]
    AuthToken: NotRequired[str]

class UpdateWorkflowRequestTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    DefaultRunProperties: NotRequired[Mapping[str, str]]
    MaxConcurrentRuns: NotRequired[int]

class UpsertRedshiftTargetOptionsTypeDef(TypedDict):
    TableLocation: NotRequired[str]
    ConnectionName: NotRequired[str]
    UpsertKeys: NotRequired[Sequence[str]]

class ViewRepresentationInputTypeDef(TypedDict):
    Dialect: NotRequired[ViewDialectType]
    DialectVersion: NotRequired[str]
    ViewOriginalText: NotRequired[str]
    ValidationConnection: NotRequired[str]
    ViewExpandedText: NotRequired[str]

class ViewRepresentationTypeDef(TypedDict):
    Dialect: NotRequired[ViewDialectType]
    DialectVersion: NotRequired[str]
    ViewOriginalText: NotRequired[str]
    ViewExpandedText: NotRequired[str]
    ValidationConnection: NotRequired[str]
    IsStale: NotRequired[bool]

class WorkflowRunStatisticsTypeDef(TypedDict):
    TotalActions: NotRequired[int]
    TimeoutActions: NotRequired[int]
    FailedActions: NotRequired[int]
    StoppedActions: NotRequired[int]
    SucceededActions: NotRequired[int]
    RunningActions: NotRequired[int]
    ErroredActions: NotRequired[int]
    WaitingActions: NotRequired[int]

class ActionOutputTypeDef(TypedDict):
    JobName: NotRequired[str]
    Arguments: NotRequired[Dict[str, str]]
    Timeout: NotRequired[int]
    SecurityConfiguration: NotRequired[str]
    NotificationProperty: NotRequired[NotificationPropertyTypeDef]
    CrawlerName: NotRequired[str]

class ActionTypeDef(TypedDict):
    JobName: NotRequired[str]
    Arguments: NotRequired[Mapping[str, str]]
    Timeout: NotRequired[int]
    SecurityConfiguration: NotRequired[str]
    NotificationProperty: NotRequired[NotificationPropertyTypeDef]
    CrawlerName: NotRequired[str]

class StartJobRunRequestTypeDef(TypedDict):
    JobName: str
    JobRunQueuingEnabled: NotRequired[bool]
    JobRunId: NotRequired[str]
    Arguments: NotRequired[Mapping[str, str]]
    AllocatedCapacity: NotRequired[int]
    Timeout: NotRequired[int]
    MaxCapacity: NotRequired[float]
    SecurityConfiguration: NotRequired[str]
    NotificationProperty: NotRequired[NotificationPropertyTypeDef]
    WorkerType: NotRequired[WorkerTypeType]
    NumberOfWorkers: NotRequired[int]
    ExecutionClass: NotRequired[ExecutionClassType]

class AggregateOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Groups: List[List[str]]
    Aggs: List[AggregateOperationOutputTypeDef]

AggregateOperationUnionTypeDef = Union[AggregateOperationTypeDef, AggregateOperationOutputTypeDef]
PropertyTypeDef = TypedDict(
    "PropertyTypeDef",
    {
        "Name": str,
        "Description": str,
        "Required": bool,
        "PropertyTypes": List[PropertyTypeType],
        "DefaultValue": NotRequired[str],
        "AllowedValues": NotRequired[List[AllowedValueTypeDef]],
        "DataOperationScopes": NotRequired[List[DataOperationType]],
    },
)

class AmazonRedshiftNodeDataOutputTypeDef(TypedDict):
    AccessType: NotRequired[str]
    SourceType: NotRequired[str]
    Connection: NotRequired[OptionTypeDef]
    Schema: NotRequired[OptionTypeDef]
    Table: NotRequired[OptionTypeDef]
    CatalogDatabase: NotRequired[OptionTypeDef]
    CatalogTable: NotRequired[OptionTypeDef]
    CatalogRedshiftSchema: NotRequired[str]
    CatalogRedshiftTable: NotRequired[str]
    TempDir: NotRequired[str]
    IamRole: NotRequired[OptionTypeDef]
    AdvancedOptions: NotRequired[List[AmazonRedshiftAdvancedOptionTypeDef]]
    SampleQuery: NotRequired[str]
    PreAction: NotRequired[str]
    PostAction: NotRequired[str]
    Action: NotRequired[str]
    TablePrefix: NotRequired[str]
    Upsert: NotRequired[bool]
    MergeAction: NotRequired[str]
    MergeWhenMatched: NotRequired[str]
    MergeWhenNotMatched: NotRequired[str]
    MergeClause: NotRequired[str]
    CrawlerConnection: NotRequired[str]
    TableSchema: NotRequired[List[OptionTypeDef]]
    StagingTable: NotRequired[str]
    SelectedColumns: NotRequired[List[OptionTypeDef]]

class AmazonRedshiftNodeDataTypeDef(TypedDict):
    AccessType: NotRequired[str]
    SourceType: NotRequired[str]
    Connection: NotRequired[OptionTypeDef]
    Schema: NotRequired[OptionTypeDef]
    Table: NotRequired[OptionTypeDef]
    CatalogDatabase: NotRequired[OptionTypeDef]
    CatalogTable: NotRequired[OptionTypeDef]
    CatalogRedshiftSchema: NotRequired[str]
    CatalogRedshiftTable: NotRequired[str]
    TempDir: NotRequired[str]
    IamRole: NotRequired[OptionTypeDef]
    AdvancedOptions: NotRequired[Sequence[AmazonRedshiftAdvancedOptionTypeDef]]
    SampleQuery: NotRequired[str]
    PreAction: NotRequired[str]
    PostAction: NotRequired[str]
    Action: NotRequired[str]
    TablePrefix: NotRequired[str]
    Upsert: NotRequired[bool]
    MergeAction: NotRequired[str]
    MergeWhenMatched: NotRequired[str]
    MergeWhenNotMatched: NotRequired[str]
    MergeClause: NotRequired[str]
    CrawlerConnection: NotRequired[str]
    TableSchema: NotRequired[Sequence[OptionTypeDef]]
    StagingTable: NotRequired[str]
    SelectedColumns: NotRequired[Sequence[OptionTypeDef]]

class SnowflakeNodeDataOutputTypeDef(TypedDict):
    SourceType: NotRequired[str]
    Connection: NotRequired[OptionTypeDef]
    Schema: NotRequired[str]
    Table: NotRequired[str]
    Database: NotRequired[str]
    TempDir: NotRequired[str]
    IamRole: NotRequired[OptionTypeDef]
    AdditionalOptions: NotRequired[Dict[str, str]]
    SampleQuery: NotRequired[str]
    PreAction: NotRequired[str]
    PostAction: NotRequired[str]
    Action: NotRequired[str]
    Upsert: NotRequired[bool]
    MergeAction: NotRequired[str]
    MergeWhenMatched: NotRequired[str]
    MergeWhenNotMatched: NotRequired[str]
    MergeClause: NotRequired[str]
    StagingTable: NotRequired[str]
    SelectedColumns: NotRequired[List[OptionTypeDef]]
    AutoPushdown: NotRequired[bool]
    TableSchema: NotRequired[List[OptionTypeDef]]

class SnowflakeNodeDataTypeDef(TypedDict):
    SourceType: NotRequired[str]
    Connection: NotRequired[OptionTypeDef]
    Schema: NotRequired[str]
    Table: NotRequired[str]
    Database: NotRequired[str]
    TempDir: NotRequired[str]
    IamRole: NotRequired[OptionTypeDef]
    AdditionalOptions: NotRequired[Mapping[str, str]]
    SampleQuery: NotRequired[str]
    PreAction: NotRequired[str]
    PostAction: NotRequired[str]
    Action: NotRequired[str]
    Upsert: NotRequired[bool]
    MergeAction: NotRequired[str]
    MergeWhenMatched: NotRequired[str]
    MergeWhenNotMatched: NotRequired[str]
    MergeClause: NotRequired[str]
    StagingTable: NotRequired[str]
    SelectedColumns: NotRequired[Sequence[OptionTypeDef]]
    AutoPushdown: NotRequired[bool]
    TableSchema: NotRequired[Sequence[OptionTypeDef]]

ApplyMappingOutputTypeDef = TypedDict(
    "ApplyMappingOutputTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Mapping": List[MappingOutputTypeDef],
    },
)
ApplyMappingPaginatorTypeDef = TypedDict(
    "ApplyMappingPaginatorTypeDef",
    {
        "Name": str,
        "Inputs": List[str],
        "Mapping": List[MappingPaginatorTypeDef],
    },
)

class BackfillErrorTypeDef(TypedDict):
    Code: NotRequired[BackfillErrorCodeType]
    Partitions: NotRequired[List[PartitionValueListOutputTypeDef]]

BasicCatalogTargetUnionTypeDef = Union[BasicCatalogTargetTypeDef, BasicCatalogTargetOutputTypeDef]

class BatchPutDataQualityStatisticAnnotationResponseTypeDef(TypedDict):
    FailedInclusionAnnotations: List[AnnotationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CancelMLTaskRunResponseTypeDef(TypedDict):
    TransformId: str
    TaskRunId: str
    Status: TaskStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class CheckSchemaVersionValidityResponseTypeDef(TypedDict):
    Valid: bool
    Error: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBlueprintResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectionResponseTypeDef(TypedDict):
    CreateConnectionStatus: ConnectionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomEntityTypeResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataQualityRulesetResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDevEndpointResponseTypeDef(TypedDict):
    EndpointName: str
    Status: str
    SecurityGroupIds: List[str]
    SubnetId: str
    RoleArn: str
    YarnEndpointAddress: str
    ZeppelinRemoteSparkInterpreterPort: int
    NumberOfNodes: int
    WorkerType: WorkerTypeType
    GlueVersion: str
    NumberOfWorkers: int
    AvailabilityZone: str
    VpcId: str
    ExtraPythonLibsS3Path: str
    ExtraJarsS3Path: str
    FailureReason: str
    SecurityConfiguration: str
    CreatedTimestamp: datetime
    Arguments: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMLTransformResponseTypeDef(TypedDict):
    TransformId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRegistryResponseTypeDef(TypedDict):
    RegistryArn: str
    RegistryName: str
    Description: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSchemaResponseTypeDef(TypedDict):
    RegistryName: str
    RegistryArn: str
    SchemaName: str
    SchemaArn: str
    Description: str
    DataFormat: DataFormatType
    Compatibility: CompatibilityType
    SchemaCheckpoint: int
    LatestSchemaVersion: int
    NextSchemaVersion: int
    SchemaStatus: SchemaStatusType
    Tags: Dict[str, str]
    SchemaVersionId: str
    SchemaVersionStatus: SchemaVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScriptResponseTypeDef(TypedDict):
    PythonScript: str
    ScalaCode: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityConfigurationResponseTypeDef(TypedDict):
    Name: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTriggerResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUsageProfileResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkflowResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBlueprintResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCustomEntityTypeResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteJobResponseTypeDef(TypedDict):
    JobName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMLTransformResponseTypeDef(TypedDict):
    TransformId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRegistryResponseTypeDef(TypedDict):
    RegistryName: str
    RegistryArn: str
    Status: RegistryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSchemaResponseTypeDef(TypedDict):
    SchemaArn: str
    SchemaName: str
    Status: SchemaStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSessionResponseTypeDef(TypedDict):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTriggerResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkflowResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCustomEntityTypeResponseTypeDef(TypedDict):
    Name: str
    RegexString: str
    ContextWords: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataQualityModelResponseTypeDef(TypedDict):
    Status: DataQualityModelStatusType
    StartedOn: datetime
    CompletedOn: datetime
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEntityRecordsResponseTypeDef(TypedDict):
    Records: List[Dict[str, Any]]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetPlanResponseTypeDef(TypedDict):
    PythonScript: str
    ScalaCode: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegistryResponseTypeDef(TypedDict):
    RegistryName: str
    RegistryArn: str
    Description: str
    Status: RegistryStatusType
    CreatedTime: str
    UpdatedTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(TypedDict):
    PolicyInJson: str
    PolicyHash: str
    CreateTime: datetime
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaByDefinitionResponseTypeDef(TypedDict):
    SchemaVersionId: str
    SchemaArn: str
    DataFormat: DataFormatType
    Status: SchemaVersionStatusType
    CreatedTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaResponseTypeDef(TypedDict):
    RegistryName: str
    RegistryArn: str
    SchemaName: str
    SchemaArn: str
    Description: str
    DataFormat: DataFormatType
    Compatibility: CompatibilityType
    SchemaCheckpoint: int
    LatestSchemaVersion: int
    NextSchemaVersion: int
    SchemaStatus: SchemaStatusType
    CreatedTime: str
    UpdatedTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaVersionResponseTypeDef(TypedDict):
    SchemaVersionId: str
    SchemaDefinition: str
    DataFormat: DataFormatType
    SchemaArn: str
    VersionNumber: int
    Status: SchemaVersionStatusType
    CreatedTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaVersionsDiffResponseTypeDef(TypedDict):
    Diff: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTagsResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowRunPropertiesResponseTypeDef(TypedDict):
    RunProperties: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBlueprintsResponseTypeDef(TypedDict):
    Blueprints: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListColumnStatisticsTaskRunsResponseTypeDef(TypedDict):
    ColumnStatisticsTaskRunIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCrawlersResponseTypeDef(TypedDict):
    CrawlerNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDevEndpointsResponseTypeDef(TypedDict):
    DevEndpointNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListJobsResponseTypeDef(TypedDict):
    JobNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListMLTransformsResponseTypeDef(TypedDict):
    TransformIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTriggersResponseTypeDef(TypedDict):
    TriggerNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListWorkflowsResponseTypeDef(TypedDict):
    Workflows: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutResourcePolicyResponseTypeDef(TypedDict):
    PolicyHash: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutSchemaVersionMetadataResponseTypeDef(TypedDict):
    SchemaArn: str
    SchemaName: str
    RegistryName: str
    LatestVersion: bool
    VersionNumber: int
    SchemaVersionId: str
    MetadataKey: str
    MetadataValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterSchemaVersionResponseTypeDef(TypedDict):
    SchemaVersionId: str
    VersionNumber: int
    Status: SchemaVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveSchemaVersionMetadataResponseTypeDef(TypedDict):
    SchemaArn: str
    SchemaName: str
    RegistryName: str
    LatestVersion: bool
    VersionNumber: int
    SchemaVersionId: str
    MetadataKey: str
    MetadataValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResumeWorkflowRunResponseTypeDef(TypedDict):
    RunId: str
    NodeIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RunStatementResponseTypeDef(TypedDict):
    Id: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartBlueprintRunResponseTypeDef(TypedDict):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartColumnStatisticsTaskRunResponseTypeDef(TypedDict):
    ColumnStatisticsTaskRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataQualityRuleRecommendationRunResponseTypeDef(TypedDict):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataQualityRulesetEvaluationRunResponseTypeDef(TypedDict):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartExportLabelsTaskRunResponseTypeDef(TypedDict):
    TaskRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportLabelsTaskRunResponseTypeDef(TypedDict):
    TaskRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartJobRunResponseTypeDef(TypedDict):
    JobRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMLEvaluationTaskRunResponseTypeDef(TypedDict):
    TaskRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMLLabelingSetGenerationTaskRunResponseTypeDef(TypedDict):
    TaskRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartTriggerResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartWorkflowRunResponseTypeDef(TypedDict):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopSessionResponseTypeDef(TypedDict):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopTriggerResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBlueprintResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataQualityRulesetResponseTypeDef(TypedDict):
    Name: str
    Description: str
    Ruleset: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateJobFromSourceControlResponseTypeDef(TypedDict):
    JobName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateJobResponseTypeDef(TypedDict):
    JobName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMLTransformResponseTypeDef(TypedDict):
    TransformId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRegistryResponseTypeDef(TypedDict):
    RegistryName: str
    RegistryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSchemaResponseTypeDef(TypedDict):
    SchemaArn: str
    SchemaName: str
    RegistryName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSourceControlFromJobResponseTypeDef(TypedDict):
    JobName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUsageProfileResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkflowResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteConnectionResponseTypeDef(TypedDict):
    Succeeded: List[str]
    Errors: Dict[str, ErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

BatchGetTableOptimizerErrorTypeDef = TypedDict(
    "BatchGetTableOptimizerErrorTypeDef",
    {
        "error": NotRequired[ErrorDetailTypeDef],
        "catalogId": NotRequired[str],
        "databaseName": NotRequired[str],
        "tableName": NotRequired[str],
        "type": NotRequired[TableOptimizerTypeType],
    },
)

class BatchStopJobRunErrorTypeDef(TypedDict):
    JobName: NotRequired[str]
    JobRunId: NotRequired[str]
    ErrorDetail: NotRequired[ErrorDetailTypeDef]

class BatchUpdatePartitionFailureEntryTypeDef(TypedDict):
    PartitionValueList: NotRequired[List[str]]
    ErrorDetail: NotRequired[ErrorDetailTypeDef]

class ColumnErrorTypeDef(TypedDict):
    ColumnName: NotRequired[str]
    Error: NotRequired[ErrorDetailTypeDef]

class PartitionErrorTypeDef(TypedDict):
    PartitionValues: NotRequired[List[str]]
    ErrorDetail: NotRequired[ErrorDetailTypeDef]

class TableErrorTypeDef(TypedDict):
    TableName: NotRequired[str]
    ErrorDetail: NotRequired[ErrorDetailTypeDef]

class TableVersionErrorTypeDef(TypedDict):
    TableName: NotRequired[str]
    VersionId: NotRequired[str]
    ErrorDetail: NotRequired[ErrorDetailTypeDef]

class ViewValidationTypeDef(TypedDict):
    Dialect: NotRequired[ViewDialectType]
    DialectVersion: NotRequired[str]
    ViewValidationText: NotRequired[str]
    UpdateTime: NotRequired[datetime]
    State: NotRequired[ResourceStateType]
    Error: NotRequired[ErrorDetailTypeDef]

class BatchGetCustomEntityTypesResponseTypeDef(TypedDict):
    CustomEntityTypes: List[CustomEntityTypeTypeDef]
    CustomEntityTypesNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomEntityTypesResponseTypeDef(TypedDict):
    CustomEntityTypes: List[CustomEntityTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchGetDevEndpointsResponseTypeDef(TypedDict):
    DevEndpoints: List[DevEndpointTypeDef]
    DevEndpointsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevEndpointResponseTypeDef(TypedDict):
    DevEndpoint: DevEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevEndpointsResponseTypeDef(TypedDict):
    DevEndpoints: List[DevEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchGetTableOptimizerRequestTypeDef(TypedDict):
    Entries: Sequence[BatchGetTableOptimizerEntryTypeDef]

class BatchPutDataQualityStatisticAnnotationRequestTypeDef(TypedDict):
    InclusionAnnotations: Sequence[DatapointInclusionAnnotationTypeDef]
    ClientToken: NotRequired[str]

class DecimalNumberTypeDef(TypedDict):
    UnscaledValue: BlobTypeDef
    Scale: int

class GetBlueprintRunResponseTypeDef(TypedDict):
    BlueprintRun: BlueprintRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBlueprintRunsResponseTypeDef(TypedDict):
    BlueprintRuns: List[BlueprintRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BlueprintTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    CreatedOn: NotRequired[datetime]
    LastModifiedOn: NotRequired[datetime]
    ParameterSpec: NotRequired[str]
    BlueprintLocation: NotRequired[str]
    BlueprintServiceLocation: NotRequired[str]
    Status: NotRequired[BlueprintStatusType]
    ErrorMessage: NotRequired[str]
    LastActiveDefinition: NotRequired[LastActiveDefinitionTypeDef]

class ConnectionTypeBriefTypeDef(TypedDict):
    ConnectionType: NotRequired[ConnectionTypeType]
    Description: NotRequired[str]
    Capabilities: NotRequired[CapabilitiesTypeDef]

class GetCatalogImportStatusResponseTypeDef(TypedDict):
    ImportStatus: CatalogImportStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CatalogKafkaSourceOutputTypeDef(TypedDict):
    Name: str
    Table: str
    Database: str
    WindowSize: NotRequired[int]
    DetectSchema: NotRequired[bool]
    StreamingOptions: NotRequired[KafkaStreamingSourceOptionsOutputTypeDef]
    DataPreviewOptions: NotRequired[StreamingDataPreviewOptionsTypeDef]

class DirectKafkaSourceOutputTypeDef(TypedDict):
    Name: str
    StreamingOptions: NotRequired[KafkaStreamingSourceOptionsOutputTypeDef]
    WindowSize: NotRequired[int]
    DetectSchema: NotRequired[bool]
    DataPreviewOptions: NotRequired[StreamingDataPreviewOptionsTypeDef]

class CatalogKinesisSourceOutputTypeDef(TypedDict):
    Name: str
    Table: str
    Database: str
    WindowSize: NotRequired[int]
    DetectSchema: NotRequired[bool]
    StreamingOptions: NotRequired[KinesisStreamingSourceOptionsOutputTypeDef]
    DataPreviewOptions: NotRequired[StreamingDataPreviewOptionsTypeDef]

class DirectKinesisSourceOutputTypeDef(TypedDict):
    Name: str
    WindowSize: NotRequired[int]
    DetectSchema: NotRequired[bool]
    StreamingOptions: NotRequired[KinesisStreamingSourceOptionsOutputTypeDef]
    DataPreviewOptions: NotRequired[StreamingDataPreviewOptionsTypeDef]

class CatalogPropertiesOutputTypeDef(TypedDict):
    DataLakeAccessProperties: NotRequired[DataLakeAccessPropertiesOutputTypeDef]
    CustomProperties: NotRequired[Dict[str, str]]

class CatalogPropertiesTypeDef(TypedDict):
    DataLakeAccessProperties: NotRequired[DataLakeAccessPropertiesTypeDef]
    CustomProperties: NotRequired[Mapping[str, str]]

class GovernedCatalogTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: NotRequired[List[List[str]]]
    SchemaChangePolicy: NotRequired[CatalogSchemaChangePolicyTypeDef]

class GovernedCatalogTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    PartitionKeys: NotRequired[Sequence[Sequence[str]]]
    SchemaChangePolicy: NotRequired[CatalogSchemaChangePolicyTypeDef]

class S3CatalogTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: NotRequired[List[List[str]]]
    SchemaChangePolicy: NotRequired[CatalogSchemaChangePolicyTypeDef]

class S3CatalogTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    PartitionKeys: NotRequired[Sequence[Sequence[str]]]
    SchemaChangePolicy: NotRequired[CatalogSchemaChangePolicyTypeDef]

class S3DeltaCatalogTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: NotRequired[List[List[str]]]
    AdditionalOptions: NotRequired[Dict[str, str]]
    SchemaChangePolicy: NotRequired[CatalogSchemaChangePolicyTypeDef]

class S3DeltaCatalogTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    PartitionKeys: NotRequired[Sequence[Sequence[str]]]
    AdditionalOptions: NotRequired[Mapping[str, str]]
    SchemaChangePolicy: NotRequired[CatalogSchemaChangePolicyTypeDef]

class S3HudiCatalogTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    AdditionalOptions: Dict[str, str]
    PartitionKeys: NotRequired[List[List[str]]]
    SchemaChangePolicy: NotRequired[CatalogSchemaChangePolicyTypeDef]

class S3HudiCatalogTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    AdditionalOptions: Mapping[str, str]
    PartitionKeys: NotRequired[Sequence[Sequence[str]]]
    SchemaChangePolicy: NotRequired[CatalogSchemaChangePolicyTypeDef]

class ClassifierTypeDef(TypedDict):
    GrokClassifier: NotRequired[GrokClassifierTypeDef]
    XMLClassifier: NotRequired[XMLClassifierTypeDef]
    JsonClassifier: NotRequired[JsonClassifierTypeDef]
    CsvClassifier: NotRequired[CsvClassifierTypeDef]

class CodeGenNodeOutputTypeDef(TypedDict):
    Id: str
    NodeType: str
    Args: List[CodeGenNodeArgTypeDef]
    LineNumber: NotRequired[int]

class CodeGenNodeTypeDef(TypedDict):
    Id: str
    NodeType: str
    Args: Sequence[CodeGenNodeArgTypeDef]
    LineNumber: NotRequired[int]

class LocationTypeDef(TypedDict):
    Jdbc: NotRequired[Sequence[CodeGenNodeArgTypeDef]]
    S3: NotRequired[Sequence[CodeGenNodeArgTypeDef]]
    DynamoDB: NotRequired[Sequence[CodeGenNodeArgTypeDef]]

class GetColumnStatisticsTaskRunResponseTypeDef(TypedDict):
    ColumnStatisticsTaskRun: ColumnStatisticsTaskRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetColumnStatisticsTaskRunsResponseTypeDef(TypedDict):
    ColumnStatisticsTaskRuns: List[ColumnStatisticsTaskRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ColumnStatisticsTaskSettingsTypeDef(TypedDict):
    DatabaseName: NotRequired[str]
    TableName: NotRequired[str]
    Schedule: NotRequired[ScheduleTypeDef]
    ColumnNameList: NotRequired[List[str]]
    CatalogID: NotRequired[str]
    Role: NotRequired[str]
    SampleSize: NotRequired[float]
    SecurityConfiguration: NotRequired[str]
    ScheduleType: NotRequired[ScheduleTypeType]
    SettingSource: NotRequired[SettingSourceType]
    LastExecutionAttempt: NotRequired[ExecutionAttemptTypeDef]

class DateColumnStatisticsDataTypeDef(TypedDict):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: NotRequired[TimestampTypeDef]
    MaximumValue: NotRequired[TimestampTypeDef]

class GetTableRequestTypeDef(TypedDict):
    DatabaseName: str
    Name: str
    CatalogId: NotRequired[str]
    TransactionId: NotRequired[str]
    QueryAsOfTime: NotRequired[TimestampTypeDef]
    IncludeStatusDetails: NotRequired[bool]

class GetTablesRequestTypeDef(TypedDict):
    DatabaseName: str
    CatalogId: NotRequired[str]
    Expression: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    TransactionId: NotRequired[str]
    QueryAsOfTime: NotRequired[TimestampTypeDef]
    IncludeStatusDetails: NotRequired[bool]
    AttributesToGet: NotRequired[Sequence[TableAttributesType]]

class KafkaStreamingSourceOptionsTypeDef(TypedDict):
    BootstrapServers: NotRequired[str]
    SecurityProtocol: NotRequired[str]
    ConnectionName: NotRequired[str]
    TopicName: NotRequired[str]
    Assign: NotRequired[str]
    SubscribePattern: NotRequired[str]
    Classification: NotRequired[str]
    Delimiter: NotRequired[str]
    StartingOffsets: NotRequired[str]
    EndingOffsets: NotRequired[str]
    PollTimeoutMs: NotRequired[int]
    NumRetries: NotRequired[int]
    RetryIntervalMs: NotRequired[int]
    MaxOffsetsPerTrigger: NotRequired[int]
    MinPartitions: NotRequired[int]
    IncludeHeaders: NotRequired[bool]
    AddRecordTimestamp: NotRequired[str]
    EmitConsumerLagMetrics: NotRequired[str]
    StartingTimestamp: NotRequired[TimestampTypeDef]

class KinesisStreamingSourceOptionsTypeDef(TypedDict):
    EndpointUrl: NotRequired[str]
    StreamName: NotRequired[str]
    Classification: NotRequired[str]
    Delimiter: NotRequired[str]
    StartingPosition: NotRequired[StartingPositionType]
    MaxFetchTimeInMs: NotRequired[int]
    MaxFetchRecordsPerShard: NotRequired[int]
    MaxRecordPerRead: NotRequired[int]
    AddIdleTimeBetweenReads: NotRequired[bool]
    IdleTimeBetweenReadsInMs: NotRequired[int]
    DescribeShardInterval: NotRequired[int]
    NumRetries: NotRequired[int]
    RetryIntervalMs: NotRequired[int]
    MaxRetryIntervalMs: NotRequired[int]
    AvoidEmptyBatches: NotRequired[bool]
    StreamArn: NotRequired[str]
    RoleArn: NotRequired[str]
    RoleSessionName: NotRequired[str]
    AddRecordTimestamp: NotRequired[str]
    EmitConsumerLagMetrics: NotRequired[str]
    StartingTimestamp: NotRequired[TimestampTypeDef]

class QuerySessionContextTypeDef(TypedDict):
    QueryId: NotRequired[str]
    QueryStartTime: NotRequired[TimestampTypeDef]
    ClusterId: NotRequired[str]
    QueryAuthorizationId: NotRequired[str]
    AdditionalContext: NotRequired[Mapping[str, str]]

class TaskRunFilterCriteriaTypeDef(TypedDict):
    TaskRunType: NotRequired[TaskTypeType]
    Status: NotRequired[TaskStatusTypeType]
    StartedBefore: NotRequired[TimestampTypeDef]
    StartedAfter: NotRequired[TimestampTypeDef]

class TimestampFilterTypeDef(TypedDict):
    RecordedBefore: NotRequired[TimestampTypeDef]
    RecordedAfter: NotRequired[TimestampTypeDef]

ColumnUnionTypeDef = Union[ColumnTypeDef, ColumnOutputTypeDef]

class CompactionMetricsTypeDef(TypedDict):
    IcebergMetrics: NotRequired[IcebergCompactionMetricsTypeDef]

class PredicateOutputTypeDef(TypedDict):
    Logical: NotRequired[LogicalType]
    Conditions: NotRequired[List[ConditionTypeDef]]

class PredicateTypeDef(TypedDict):
    Logical: NotRequired[LogicalType]
    Conditions: NotRequired[Sequence[ConditionTypeDef]]

class ProfileConfigurationOutputTypeDef(TypedDict):
    SessionConfiguration: NotRequired[Dict[str, ConfigurationObjectOutputTypeDef]]
    JobConfiguration: NotRequired[Dict[str, ConfigurationObjectOutputTypeDef]]

class ProfileConfigurationTypeDef(TypedDict):
    SessionConfiguration: NotRequired[Mapping[str, ConfigurationObjectTypeDef]]
    JobConfiguration: NotRequired[Mapping[str, ConfigurationObjectTypeDef]]

class FindMatchesMetricsTypeDef(TypedDict):
    AreaUnderPRCurve: NotRequired[float]
    Precision: NotRequired[float]
    Recall: NotRequired[float]
    F1: NotRequired[float]
    ConfusionMatrix: NotRequired[ConfusionMatrixTypeDef]
    ColumnImportances: NotRequired[List[ColumnImportanceTypeDef]]

ConnectionsListUnionTypeDef = Union[ConnectionsListTypeDef, ConnectionsListOutputTypeDef]
ConnectorDataTargetUnionTypeDef = Union[
    ConnectorDataTargetTypeDef, ConnectorDataTargetOutputTypeDef
]

class CrawlerNodeDetailsTypeDef(TypedDict):
    Crawls: NotRequired[List[CrawlTypeDef]]

class ListCrawlsResponseTypeDef(TypedDict):
    Crawls: List[CrawlerHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetCrawlerMetricsResponseTypeDef(TypedDict):
    CrawlerMetricsList: List[CrawlerMetricsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CrawlerTargetsOutputTypeDef(TypedDict):
    S3Targets: NotRequired[List[S3TargetOutputTypeDef]]
    JdbcTargets: NotRequired[List[JdbcTargetOutputTypeDef]]
    MongoDBTargets: NotRequired[List[MongoDBTargetTypeDef]]
    DynamoDBTargets: NotRequired[List[DynamoDBTargetTypeDef]]
    CatalogTargets: NotRequired[List[CatalogTargetOutputTypeDef]]
    DeltaTargets: NotRequired[List[DeltaTargetOutputTypeDef]]
    IcebergTargets: NotRequired[List[IcebergTargetOutputTypeDef]]
    HudiTargets: NotRequired[List[HudiTargetOutputTypeDef]]

class CrawlerTargetsTypeDef(TypedDict):
    S3Targets: NotRequired[Sequence[S3TargetTypeDef]]
    JdbcTargets: NotRequired[Sequence[JdbcTargetTypeDef]]
    MongoDBTargets: NotRequired[Sequence[MongoDBTargetTypeDef]]
    DynamoDBTargets: NotRequired[Sequence[DynamoDBTargetTypeDef]]
    CatalogTargets: NotRequired[Sequence[CatalogTargetTypeDef]]
    DeltaTargets: NotRequired[Sequence[DeltaTargetTypeDef]]
    IcebergTargets: NotRequired[Sequence[IcebergTargetTypeDef]]
    HudiTargets: NotRequired[Sequence[HudiTargetTypeDef]]

class ListCrawlsRequestTypeDef(TypedDict):
    CrawlerName: str
    MaxResults: NotRequired[int]
    Filters: NotRequired[Sequence[CrawlsFilterTypeDef]]
    NextToken: NotRequired[str]

class CreateClassifierRequestTypeDef(TypedDict):
    GrokClassifier: NotRequired[CreateGrokClassifierRequestTypeDef]
    XMLClassifier: NotRequired[CreateXMLClassifierRequestTypeDef]
    JsonClassifier: NotRequired[CreateJsonClassifierRequestTypeDef]
    CsvClassifier: NotRequired[CreateCsvClassifierRequestTypeDef]

class CreateDataQualityRulesetRequestTypeDef(TypedDict):
    Name: str
    Ruleset: str
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    TargetTable: NotRequired[DataQualityTargetTableTypeDef]
    DataQualitySecurityConfiguration: NotRequired[str]
    ClientToken: NotRequired[str]

class DataQualityRulesetFilterCriteriaTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    CreatedBefore: NotRequired[TimestampTypeDef]
    CreatedAfter: NotRequired[TimestampTypeDef]
    LastModifiedBefore: NotRequired[TimestampTypeDef]
    LastModifiedAfter: NotRequired[TimestampTypeDef]
    TargetTable: NotRequired[DataQualityTargetTableTypeDef]

class DataQualityRulesetListDetailsTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    CreatedOn: NotRequired[datetime]
    LastModifiedOn: NotRequired[datetime]
    TargetTable: NotRequired[DataQualityTargetTableTypeDef]
    RecommendationRunId: NotRequired[str]
    RuleCount: NotRequired[int]

class GetDataQualityRulesetResponseTypeDef(TypedDict):
    Name: str
    Description: str
    Ruleset: str
    TargetTable: DataQualityTargetTableTypeDef
    CreatedOn: datetime
    LastModifiedOn: datetime
    RecommendationRunId: str
    DataQualitySecurityConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIntegrationRequestTypeDef(TypedDict):
    IntegrationName: str
    SourceArn: str
    TargetArn: str
    Description: NotRequired[str]
    DataFilter: NotRequired[str]
    KmsKeyId: NotRequired[str]
    AdditionalEncryptionContext: NotRequired[Mapping[str, str]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateIntegrationResourcePropertyRequestTypeDef(TypedDict):
    ResourceArn: str
    SourceProcessingProperties: NotRequired[SourceProcessingPropertiesTypeDef]
    TargetProcessingProperties: NotRequired[TargetProcessingPropertiesTypeDef]

class CreateIntegrationResourcePropertyResponseTypeDef(TypedDict):
    ResourceArn: str
    SourceProcessingProperties: SourceProcessingPropertiesTypeDef
    TargetProcessingProperties: TargetProcessingPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIntegrationResourcePropertyResponseTypeDef(TypedDict):
    ResourceArn: str
    SourceProcessingProperties: SourceProcessingPropertiesTypeDef
    TargetProcessingProperties: TargetProcessingPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIntegrationResourcePropertyRequestTypeDef(TypedDict):
    ResourceArn: str
    SourceProcessingProperties: NotRequired[SourceProcessingPropertiesTypeDef]
    TargetProcessingProperties: NotRequired[TargetProcessingPropertiesTypeDef]

class UpdateIntegrationResourcePropertyResponseTypeDef(TypedDict):
    ResourceArn: str
    SourceProcessingProperties: SourceProcessingPropertiesTypeDef
    TargetProcessingProperties: TargetProcessingPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIntegrationResponseTypeDef(TypedDict):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    Description: str
    IntegrationArn: str
    KmsKeyId: str
    AdditionalEncryptionContext: Dict[str, str]
    Tags: List[TagTypeDef]
    Status: IntegrationStatusType
    CreateTime: datetime
    Errors: List[IntegrationErrorTypeDef]
    DataFilter: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIntegrationResponseTypeDef(TypedDict):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    Description: str
    IntegrationArn: str
    KmsKeyId: str
    AdditionalEncryptionContext: Dict[str, str]
    Tags: List[TagTypeDef]
    Status: IntegrationStatusType
    CreateTime: datetime
    Errors: List[IntegrationErrorTypeDef]
    DataFilter: str
    ResponseMetadata: ResponseMetadataTypeDef

class InboundIntegrationTypeDef(TypedDict):
    SourceArn: str
    TargetArn: str
    IntegrationArn: str
    Status: IntegrationStatusType
    CreateTime: datetime
    Errors: NotRequired[List[IntegrationErrorTypeDef]]

class IntegrationTypeDef(TypedDict):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    IntegrationArn: str
    Status: IntegrationStatusType
    CreateTime: datetime
    Description: NotRequired[str]
    KmsKeyId: NotRequired[str]
    AdditionalEncryptionContext: NotRequired[Dict[str, str]]
    Tags: NotRequired[List[TagTypeDef]]
    Errors: NotRequired[List[IntegrationErrorTypeDef]]
    DataFilter: NotRequired[str]

class ModifyIntegrationResponseTypeDef(TypedDict):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    Description: str
    IntegrationArn: str
    KmsKeyId: str
    AdditionalEncryptionContext: Dict[str, str]
    Tags: List[TagTypeDef]
    Status: IntegrationStatusType
    CreateTime: datetime
    Errors: List[IntegrationErrorTypeDef]
    DataFilter: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePartitionIndexRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    PartitionIndex: PartitionIndexTypeDef
    CatalogId: NotRequired[str]

class CreateSchemaInputTypeDef(TypedDict):
    SchemaName: str
    DataFormat: DataFormatType
    RegistryId: NotRequired[RegistryIdTypeDef]
    Compatibility: NotRequired[CompatibilityType]
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    SchemaDefinition: NotRequired[str]

class DeleteRegistryInputTypeDef(TypedDict):
    RegistryId: RegistryIdTypeDef

class GetRegistryInputTypeDef(TypedDict):
    RegistryId: RegistryIdTypeDef

class ListSchemasInputTypeDef(TypedDict):
    RegistryId: NotRequired[RegistryIdTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class UpdateRegistryInputTypeDef(TypedDict):
    RegistryId: RegistryIdTypeDef
    Description: str

class SessionTypeDef(TypedDict):
    Id: NotRequired[str]
    CreatedOn: NotRequired[datetime]
    Status: NotRequired[SessionStatusType]
    ErrorMessage: NotRequired[str]
    Description: NotRequired[str]
    Role: NotRequired[str]
    Command: NotRequired[SessionCommandTypeDef]
    DefaultArguments: NotRequired[Dict[str, str]]
    Connections: NotRequired[ConnectionsListOutputTypeDef]
    Progress: NotRequired[float]
    MaxCapacity: NotRequired[float]
    SecurityConfiguration: NotRequired[str]
    GlueVersion: NotRequired[str]
    NumberOfWorkers: NotRequired[int]
    WorkerType: NotRequired[WorkerTypeType]
    CompletedOn: NotRequired[datetime]
    ExecutionTime: NotRequired[float]
    DPUSeconds: NotRequired[float]
    IdleTimeout: NotRequired[int]
    ProfileName: NotRequired[str]

class EvaluateDataQualityMultiFrameOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Ruleset: str
    AdditionalDataSources: NotRequired[Dict[str, str]]
    PublishingOptions: NotRequired[DQResultsPublishingOptionsTypeDef]
    AdditionalOptions: NotRequired[Dict[AdditionalOptionKeysType, str]]
    StopJobOnFailureOptions: NotRequired[DQStopJobOnFailureOptionsTypeDef]

class EvaluateDataQualityMultiFrameTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Ruleset: str
    AdditionalDataSources: NotRequired[Mapping[str, str]]
    PublishingOptions: NotRequired[DQResultsPublishingOptionsTypeDef]
    AdditionalOptions: NotRequired[Mapping[AdditionalOptionKeysType, str]]
    StopJobOnFailureOptions: NotRequired[DQStopJobOnFailureOptionsTypeDef]

class EvaluateDataQualityOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Ruleset: str
    Output: NotRequired[DQTransformOutputType]
    PublishingOptions: NotRequired[DQResultsPublishingOptionsTypeDef]
    StopJobOnFailureOptions: NotRequired[DQStopJobOnFailureOptionsTypeDef]

class EvaluateDataQualityTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Ruleset: str
    Output: NotRequired[DQTransformOutputType]
    PublishingOptions: NotRequired[DQResultsPublishingOptionsTypeDef]
    StopJobOnFailureOptions: NotRequired[DQStopJobOnFailureOptionsTypeDef]

class DataCatalogEncryptionSettingsTypeDef(TypedDict):
    EncryptionAtRest: NotRequired[EncryptionAtRestTypeDef]
    ConnectionPasswordEncryption: NotRequired[ConnectionPasswordEncryptionTypeDef]

class PrincipalPermissionsOutputTypeDef(TypedDict):
    Principal: NotRequired[DataLakePrincipalTypeDef]
    Permissions: NotRequired[List[PermissionType]]

class PrincipalPermissionsTypeDef(TypedDict):
    Principal: NotRequired[DataLakePrincipalTypeDef]
    Permissions: NotRequired[Sequence[PermissionType]]

class MetricBasedObservationTypeDef(TypedDict):
    MetricName: NotRequired[str]
    StatisticId: NotRequired[str]
    MetricValues: NotRequired[DataQualityMetricValuesTypeDef]
    NewRules: NotRequired[List[str]]

class DataSourceOutputTypeDef(TypedDict):
    GlueTable: GlueTableOutputTypeDef

class NullValueFieldTypeDef(TypedDict):
    Value: str
    Datatype: DatatypeTypeDef

class DecimalColumnStatisticsDataOutputTypeDef(TypedDict):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: NotRequired[DecimalNumberOutputTypeDef]
    MaximumValue: NotRequired[DecimalNumberOutputTypeDef]

class DeleteSchemaInputTypeDef(TypedDict):
    SchemaId: SchemaIdTypeDef

class DeleteSchemaVersionsInputTypeDef(TypedDict):
    SchemaId: SchemaIdTypeDef
    Versions: str

class GetSchemaByDefinitionInputTypeDef(TypedDict):
    SchemaId: SchemaIdTypeDef
    SchemaDefinition: str

class GetSchemaInputTypeDef(TypedDict):
    SchemaId: SchemaIdTypeDef

class ListSchemaVersionsInputTypeDef(TypedDict):
    SchemaId: SchemaIdTypeDef
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class RegisterSchemaVersionInputTypeDef(TypedDict):
    SchemaId: SchemaIdTypeDef
    SchemaDefinition: str

class SchemaReferenceTypeDef(TypedDict):
    SchemaId: NotRequired[SchemaIdTypeDef]
    SchemaVersionId: NotRequired[str]
    SchemaVersionNumber: NotRequired[int]

class DescribeEntityRequestPaginateTypeDef(TypedDict):
    ConnectionName: str
    EntityName: str
    CatalogId: NotRequired[str]
    DataStoreApiVersion: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetClassifiersRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetCrawlerMetricsRequestPaginateTypeDef(TypedDict):
    CrawlerNameList: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetCrawlersRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetDatabasesRequestPaginateTypeDef(TypedDict):
    CatalogId: NotRequired[str]
    ResourceShareType: NotRequired[ResourceShareTypeType]
    AttributesToGet: NotRequired[Sequence[Literal["NAME"]]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetDevEndpointsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetJobRunsRequestPaginateTypeDef(TypedDict):
    JobName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetJobsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetPartitionIndexesRequestPaginateTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    CatalogId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetResourcePoliciesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetSecurityConfigurationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetTableVersionsRequestPaginateTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    CatalogId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetTablesRequestPaginateTypeDef(TypedDict):
    DatabaseName: str
    CatalogId: NotRequired[str]
    Expression: NotRequired[str]
    TransactionId: NotRequired[str]
    QueryAsOfTime: NotRequired[TimestampTypeDef]
    IncludeStatusDetails: NotRequired[bool]
    AttributesToGet: NotRequired[Sequence[TableAttributesType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetTriggersRequestPaginateTypeDef(TypedDict):
    DependentJobName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

GetUserDefinedFunctionsRequestPaginateTypeDef = TypedDict(
    "GetUserDefinedFunctionsRequestPaginateTypeDef",
    {
        "Pattern": str,
        "CatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class GetWorkflowRunsRequestPaginateTypeDef(TypedDict):
    Name: str
    IncludeGraph: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBlueprintsRequestPaginateTypeDef(TypedDict):
    Tags: NotRequired[Mapping[str, str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListConnectionTypesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEntitiesRequestPaginateTypeDef(TypedDict):
    ConnectionName: NotRequired[str]
    CatalogId: NotRequired[str]
    ParentEntityName: NotRequired[str]
    DataStoreApiVersion: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListJobsRequestPaginateTypeDef(TypedDict):
    Tags: NotRequired[Mapping[str, str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRegistriesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSchemaVersionsInputPaginateTypeDef(TypedDict):
    SchemaId: SchemaIdTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSchemasInputPaginateTypeDef(TypedDict):
    RegistryId: NotRequired[RegistryIdTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListTableOptimizerRunsRequestPaginateTypeDef = TypedDict(
    "ListTableOptimizerRunsRequestPaginateTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Type": TableOptimizerTypeType,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListTriggersRequestPaginateTypeDef(TypedDict):
    DependentJobName: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUsageProfilesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkflowsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEntityResponseTypeDef(TypedDict):
    Fields: List[FieldTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeIntegrationsRequestTypeDef(TypedDict):
    IntegrationIdentifier: NotRequired[str]
    Marker: NotRequired[str]
    MaxRecords: NotRequired[int]
    Filters: NotRequired[Sequence[IntegrationFilterTypeDef]]

class UpdateDevEndpointRequestTypeDef(TypedDict):
    EndpointName: str
    PublicKey: NotRequired[str]
    AddPublicKeys: NotRequired[Sequence[str]]
    DeletePublicKeys: NotRequired[Sequence[str]]
    CustomLibraries: NotRequired[DevEndpointCustomLibrariesTypeDef]
    UpdateEtlLibraries: NotRequired[bool]
    DeleteArguments: NotRequired[Sequence[str]]
    AddArguments: NotRequired[Mapping[str, str]]

class S3DeltaDirectTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Path: str
    Compression: DeltaTargetCompressionTypeType
    Format: TargetFormatType
    PartitionKeys: NotRequired[List[List[str]]]
    AdditionalOptions: NotRequired[Dict[str, str]]
    SchemaChangePolicy: NotRequired[DirectSchemaChangePolicyTypeDef]

class S3DeltaDirectTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Compression: DeltaTargetCompressionTypeType
    Format: TargetFormatType
    PartitionKeys: NotRequired[Sequence[Sequence[str]]]
    AdditionalOptions: NotRequired[Mapping[str, str]]
    SchemaChangePolicy: NotRequired[DirectSchemaChangePolicyTypeDef]

class S3DirectTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Path: str
    Format: TargetFormatType
    PartitionKeys: NotRequired[List[List[str]]]
    Compression: NotRequired[str]
    SchemaChangePolicy: NotRequired[DirectSchemaChangePolicyTypeDef]

class S3DirectTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Format: TargetFormatType
    PartitionKeys: NotRequired[Sequence[Sequence[str]]]
    Compression: NotRequired[str]
    SchemaChangePolicy: NotRequired[DirectSchemaChangePolicyTypeDef]

class S3GlueParquetTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Path: str
    PartitionKeys: NotRequired[List[List[str]]]
    Compression: NotRequired[ParquetCompressionTypeType]
    SchemaChangePolicy: NotRequired[DirectSchemaChangePolicyTypeDef]

class S3GlueParquetTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Path: str
    PartitionKeys: NotRequired[Sequence[Sequence[str]]]
    Compression: NotRequired[ParquetCompressionTypeType]
    SchemaChangePolicy: NotRequired[DirectSchemaChangePolicyTypeDef]

class S3HudiDirectTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Path: str
    Compression: HudiTargetCompressionTypeType
    Format: TargetFormatType
    AdditionalOptions: Dict[str, str]
    PartitionKeys: NotRequired[List[List[str]]]
    SchemaChangePolicy: NotRequired[DirectSchemaChangePolicyTypeDef]

class S3HudiDirectTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Compression: HudiTargetCompressionTypeType
    Format: TargetFormatType
    AdditionalOptions: Mapping[str, str]
    PartitionKeys: NotRequired[Sequence[Sequence[str]]]
    SchemaChangePolicy: NotRequired[DirectSchemaChangePolicyTypeDef]

DropDuplicatesUnionTypeDef = Union[DropDuplicatesTypeDef, DropDuplicatesOutputTypeDef]
DropFieldsUnionTypeDef = Union[DropFieldsTypeDef, DropFieldsOutputTypeDef]

class EncryptionConfigurationOutputTypeDef(TypedDict):
    S3Encryption: NotRequired[List[S3EncryptionTypeDef]]
    CloudWatchEncryption: NotRequired[CloudWatchEncryptionTypeDef]
    JobBookmarksEncryption: NotRequired[JobBookmarksEncryptionTypeDef]
    DataQualityEncryption: NotRequired[DataQualityEncryptionTypeDef]

class EncryptionConfigurationTypeDef(TypedDict):
    S3Encryption: NotRequired[Sequence[S3EncryptionTypeDef]]
    CloudWatchEncryption: NotRequired[CloudWatchEncryptionTypeDef]
    JobBookmarksEncryption: NotRequired[JobBookmarksEncryptionTypeDef]
    DataQualityEncryption: NotRequired[DataQualityEncryptionTypeDef]

class ListEntitiesResponseTypeDef(TypedDict):
    Entities: List[EntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SchemaVersionErrorItemTypeDef(TypedDict):
    VersionNumber: NotRequired[int]
    ErrorDetails: NotRequired[ErrorDetailsTypeDef]

FillMissingValuesUnionTypeDef = Union[FillMissingValuesTypeDef, FillMissingValuesOutputTypeDef]

class FilterExpressionOutputTypeDef(TypedDict):
    Operation: FilterOperationType
    Values: List[FilterValueOutputTypeDef]
    Negated: NotRequired[bool]

FilterValueUnionTypeDef = Union[FilterValueTypeDef, FilterValueOutputTypeDef]

class TransformParametersTypeDef(TypedDict):
    TransformType: Literal["FIND_MATCHES"]
    FindMatchesParameters: NotRequired[FindMatchesParametersTypeDef]

class GetConnectionsRequestPaginateTypeDef(TypedDict):
    CatalogId: NotRequired[str]
    Filter: NotRequired[GetConnectionsFilterTypeDef]
    HidePassword: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetConnectionsRequestTypeDef(TypedDict):
    CatalogId: NotRequired[str]
    Filter: NotRequired[GetConnectionsFilterTypeDef]
    HidePassword: NotRequired[bool]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetDataQualityModelResultResponseTypeDef(TypedDict):
    CompletedOn: datetime
    Model: List[StatisticModelResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobBookmarkResponseTypeDef(TypedDict):
    JobBookmarkEntry: JobBookmarkEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResetJobBookmarkResponseTypeDef(TypedDict):
    JobBookmarkEntry: JobBookmarkEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TransformFilterCriteriaTypeDef(TypedDict):
    Name: NotRequired[str]
    TransformType: NotRequired[Literal["FIND_MATCHES"]]
    Status: NotRequired[TransformStatusTypeType]
    GlueVersion: NotRequired[str]
    CreatedBefore: NotRequired[TimestampTypeDef]
    CreatedAfter: NotRequired[TimestampTypeDef]
    LastModifiedBefore: NotRequired[TimestampTypeDef]
    LastModifiedAfter: NotRequired[TimestampTypeDef]
    Schema: NotRequired[Sequence[SchemaColumnTypeDef]]

GetMappingResponseTypeDef = TypedDict(
    "GetMappingResponseTypeDef",
    {
        "Mapping": List[MappingEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetPartitionsRequestPaginateTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    CatalogId: NotRequired[str]
    Expression: NotRequired[str]
    Segment: NotRequired[SegmentTypeDef]
    ExcludeColumnSchema: NotRequired[bool]
    TransactionId: NotRequired[str]
    QueryAsOfTime: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetPartitionsRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    CatalogId: NotRequired[str]
    Expression: NotRequired[str]
    NextToken: NotRequired[str]
    Segment: NotRequired[SegmentTypeDef]
    MaxResults: NotRequired[int]
    ExcludeColumnSchema: NotRequired[bool]
    TransactionId: NotRequired[str]
    QueryAsOfTime: NotRequired[TimestampTypeDef]

class GetResourcePoliciesResponseTypeDef(TypedDict):
    GetResourcePoliciesResponseList: List[GluePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetSchemaVersionInputTypeDef(TypedDict):
    SchemaId: NotRequired[SchemaIdTypeDef]
    SchemaVersionId: NotRequired[str]
    SchemaVersionNumber: NotRequired[SchemaVersionNumberTypeDef]

class GetSchemaVersionsDiffInputTypeDef(TypedDict):
    SchemaId: SchemaIdTypeDef
    FirstSchemaVersionNumber: SchemaVersionNumberTypeDef
    SecondSchemaVersionNumber: SchemaVersionNumberTypeDef
    SchemaDiffType: Literal["SYNTAX_DIFF"]

class UpdateSchemaInputTypeDef(TypedDict):
    SchemaId: SchemaIdTypeDef
    SchemaVersionNumber: NotRequired[SchemaVersionNumberTypeDef]
    Compatibility: NotRequired[CompatibilityType]
    Description: NotRequired[str]

class GlueSchemaOutputTypeDef(TypedDict):
    Columns: NotRequired[List[GlueStudioSchemaColumnTypeDef]]

class GlueSchemaTypeDef(TypedDict):
    Columns: NotRequired[Sequence[GlueStudioSchemaColumnTypeDef]]

GlueTableUnionTypeDef = Union[GlueTableTypeDef, GlueTableOutputTypeDef]

class GovernedCatalogSourceTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str
    PartitionPredicate: NotRequired[str]
    AdditionalOptions: NotRequired[S3SourceAdditionalOptionsTypeDef]

class S3CatalogSourceTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str
    PartitionPredicate: NotRequired[str]
    AdditionalOptions: NotRequired[S3SourceAdditionalOptionsTypeDef]

class OpenTableFormatInputTypeDef(TypedDict):
    IcebergInput: NotRequired[IcebergInputTypeDef]

class OrphanFileDeletionConfigurationTypeDef(TypedDict):
    icebergConfiguration: NotRequired[IcebergOrphanFileDeletionConfigurationTypeDef]

class OrphanFileDeletionMetricsTypeDef(TypedDict):
    IcebergMetrics: NotRequired[IcebergOrphanFileDeletionMetricsTypeDef]

class RetentionConfigurationTypeDef(TypedDict):
    icebergConfiguration: NotRequired[IcebergRetentionConfigurationTypeDef]

class RetentionMetricsTypeDef(TypedDict):
    IcebergMetrics: NotRequired[IcebergRetentionMetricsTypeDef]

class TargetTableConfigOutputTypeDef(TypedDict):
    UnnestSpec: NotRequired[UnnestSpecType]
    PartitionSpec: NotRequired[List[IntegrationPartitionTypeDef]]
    TargetTableName: NotRequired[str]

class TargetTableConfigTypeDef(TypedDict):
    UnnestSpec: NotRequired[UnnestSpecType]
    PartitionSpec: NotRequired[Sequence[IntegrationPartitionTypeDef]]
    TargetTableName: NotRequired[str]

JDBCConnectorOptionsUnionTypeDef = Union[
    JDBCConnectorOptionsTypeDef, JDBCConnectorOptionsOutputTypeDef
]

class JobRunTypeDef(TypedDict):
    Id: NotRequired[str]
    Attempt: NotRequired[int]
    PreviousRunId: NotRequired[str]
    TriggerName: NotRequired[str]
    JobName: NotRequired[str]
    JobMode: NotRequired[JobModeType]
    JobRunQueuingEnabled: NotRequired[bool]
    StartedOn: NotRequired[datetime]
    LastModifiedOn: NotRequired[datetime]
    CompletedOn: NotRequired[datetime]
    JobRunState: NotRequired[JobRunStateType]
    Arguments: NotRequired[Dict[str, str]]
    ErrorMessage: NotRequired[str]
    PredecessorRuns: NotRequired[List[PredecessorTypeDef]]
    AllocatedCapacity: NotRequired[int]
    ExecutionTime: NotRequired[int]
    Timeout: NotRequired[int]
    MaxCapacity: NotRequired[float]
    WorkerType: NotRequired[WorkerTypeType]
    NumberOfWorkers: NotRequired[int]
    SecurityConfiguration: NotRequired[str]
    LogGroupName: NotRequired[str]
    NotificationProperty: NotRequired[NotificationPropertyTypeDef]
    GlueVersion: NotRequired[str]
    DPUSeconds: NotRequired[float]
    ExecutionClass: NotRequired[ExecutionClassType]
    MaintenanceWindow: NotRequired[str]
    ProfileName: NotRequired[str]
    StateDetail: NotRequired[str]

class JoinOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    JoinType: JoinTypeType
    Columns: List[JoinColumnOutputTypeDef]

JoinColumnUnionTypeDef = Union[JoinColumnTypeDef, JoinColumnOutputTypeDef]

class TaskRunPropertiesTypeDef(TypedDict):
    TaskType: NotRequired[TaskTypeType]
    ImportLabelsTaskRunProperties: NotRequired[ImportLabelsTaskRunPropertiesTypeDef]
    ExportLabelsTaskRunProperties: NotRequired[ExportLabelsTaskRunPropertiesTypeDef]
    LabelingSetGenerationTaskRunProperties: NotRequired[
        LabelingSetGenerationTaskRunPropertiesTypeDef
    ]
    FindMatchesTaskRunProperties: NotRequired[FindMatchesTaskRunPropertiesTypeDef]

class ListRegistriesResponseTypeDef(TypedDict):
    Registries: List[RegistryListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSchemaVersionsResponseTypeDef(TypedDict):
    Schemas: List[SchemaVersionListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSchemasResponseTypeDef(TypedDict):
    Schemas: List[SchemaListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListUsageProfilesResponseTypeDef(TypedDict):
    Profiles: List[UsageProfileDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TransformEncryptionTypeDef(TypedDict):
    MlUserDataEncryption: NotRequired[MLUserDataEncryptionTypeDef]
    TaskRunSecurityConfigurationName: NotRequired[str]

MappingUnionTypeDef = Union[MappingTypeDef, MappingOutputTypeDef]
MergeUnionTypeDef = Union[MergeTypeDef, MergeOutputTypeDef]

class MetadataInfoTypeDef(TypedDict):
    MetadataValue: NotRequired[str]
    CreatedTime: NotRequired[str]
    OtherMetadataValueList: NotRequired[List[OtherMetadataValueListItemTypeDef]]

class PutSchemaVersionMetadataInputTypeDef(TypedDict):
    MetadataKeyValue: MetadataKeyValuePairTypeDef
    SchemaId: NotRequired[SchemaIdTypeDef]
    SchemaVersionNumber: NotRequired[SchemaVersionNumberTypeDef]
    SchemaVersionId: NotRequired[str]

class QuerySchemaVersionMetadataInputTypeDef(TypedDict):
    SchemaId: NotRequired[SchemaIdTypeDef]
    SchemaVersionNumber: NotRequired[SchemaVersionNumberTypeDef]
    SchemaVersionId: NotRequired[str]
    MetadataList: NotRequired[Sequence[MetadataKeyValuePairTypeDef]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class RemoveSchemaVersionMetadataInputTypeDef(TypedDict):
    MetadataKeyValue: MetadataKeyValuePairTypeDef
    SchemaId: NotRequired[SchemaIdTypeDef]
    SchemaVersionNumber: NotRequired[SchemaVersionNumberTypeDef]
    SchemaVersionId: NotRequired[str]

MicrosoftSQLServerCatalogTargetUnionTypeDef = Union[
    MicrosoftSQLServerCatalogTargetTypeDef, MicrosoftSQLServerCatalogTargetOutputTypeDef
]
MySQLCatalogTargetUnionTypeDef = Union[MySQLCatalogTargetTypeDef, MySQLCatalogTargetOutputTypeDef]

class OAuth2PropertiesTypeDef(TypedDict):
    OAuth2GrantType: NotRequired[OAuth2GrantTypeType]
    OAuth2ClientApplication: NotRequired[OAuth2ClientApplicationTypeDef]
    TokenUrl: NotRequired[str]
    TokenUrlParametersMap: NotRequired[Dict[str, str]]

class OAuth2PropertiesInputTypeDef(TypedDict):
    OAuth2GrantType: NotRequired[OAuth2GrantTypeType]
    OAuth2ClientApplication: NotRequired[OAuth2ClientApplicationTypeDef]
    TokenUrl: NotRequired[str]
    TokenUrlParametersMap: NotRequired[Mapping[str, str]]
    AuthorizationCodeProperties: NotRequired[AuthorizationCodePropertiesTypeDef]
    OAuth2Credentials: NotRequired[OAuth2CredentialsTypeDef]

OracleSQLCatalogTargetUnionTypeDef = Union[
    OracleSQLCatalogTargetTypeDef, OracleSQLCatalogTargetOutputTypeDef
]
PIIDetectionUnionTypeDef = Union[PIIDetectionTypeDef, PIIDetectionOutputTypeDef]
PartitionValueListUnionTypeDef = Union[PartitionValueListTypeDef, PartitionValueListOutputTypeDef]
PhysicalConnectionRequirementsUnionTypeDef = Union[
    PhysicalConnectionRequirementsTypeDef, PhysicalConnectionRequirementsOutputTypeDef
]
PostgreSQLCatalogTargetUnionTypeDef = Union[
    PostgreSQLCatalogTargetTypeDef, PostgreSQLCatalogTargetOutputTypeDef
]

class RecipeStepOutputTypeDef(TypedDict):
    Action: RecipeActionOutputTypeDef
    ConditionExpressions: NotRequired[List[ConditionExpressionTypeDef]]

RecipeActionUnionTypeDef = Union[RecipeActionTypeDef, RecipeActionOutputTypeDef]

class RedshiftTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str
    RedshiftTmpDir: NotRequired[str]
    TmpDirIAMRole: NotRequired[str]
    UpsertRedshiftOptions: NotRequired[UpsertRedshiftTargetOptionsOutputTypeDef]

RenameFieldUnionTypeDef = Union[RenameFieldTypeDef, RenameFieldOutputTypeDef]

class UserDefinedFunctionInputTypeDef(TypedDict):
    FunctionName: NotRequired[str]
    ClassName: NotRequired[str]
    OwnerName: NotRequired[str]
    OwnerType: NotRequired[PrincipalTypeType]
    ResourceUris: NotRequired[Sequence[ResourceUriTypeDef]]

class UserDefinedFunctionTypeDef(TypedDict):
    FunctionName: NotRequired[str]
    DatabaseName: NotRequired[str]
    ClassName: NotRequired[str]
    OwnerName: NotRequired[str]
    OwnerType: NotRequired[PrincipalTypeType]
    CreateTime: NotRequired[datetime]
    ResourceUris: NotRequired[List[ResourceUriTypeDef]]
    CatalogId: NotRequired[str]

class SearchTablesRequestTypeDef(TypedDict):
    CatalogId: NotRequired[str]
    NextToken: NotRequired[str]
    Filters: NotRequired[Sequence[PropertyPredicateTypeDef]]
    SearchText: NotRequired[str]
    SortCriteria: NotRequired[Sequence[SortCriterionTypeDef]]
    MaxResults: NotRequired[int]
    ResourceShareType: NotRequired[ResourceShareTypeType]
    IncludeStatusDetails: NotRequired[bool]

SelectFieldsUnionTypeDef = Union[SelectFieldsTypeDef, SelectFieldsOutputTypeDef]
SelectFromCollectionUnionTypeDef = Union[
    SelectFromCollectionTypeDef, SelectFromCollectionOutputTypeDef
]
SerDeInfoUnionTypeDef = Union[SerDeInfoTypeDef, SerDeInfoOutputTypeDef]
SkewedInfoUnionTypeDef = Union[SkewedInfoTypeDef, SkewedInfoOutputTypeDef]
SourceTableConfigUnionTypeDef = Union[SourceTableConfigTypeDef, SourceTableConfigOutputTypeDef]
SpigotUnionTypeDef = Union[SpigotTypeDef, SpigotOutputTypeDef]
SplitFieldsUnionTypeDef = Union[SplitFieldsTypeDef, SplitFieldsOutputTypeDef]

class StatementOutputTypeDef(TypedDict):
    Data: NotRequired[StatementOutputDataTypeDef]
    ExecutionCount: NotRequired[int]
    Status: NotRequired[StatementStateType]
    ErrorName: NotRequired[str]
    ErrorValue: NotRequired[str]
    Traceback: NotRequired[List[str]]

class StatisticAnnotationTypeDef(TypedDict):
    ProfileId: NotRequired[str]
    StatisticId: NotRequired[str]
    StatisticRecordedOn: NotRequired[datetime]
    InclusionAnnotation: NotRequired[TimestampedInclusionAnnotationTypeDef]

class StatisticSummaryTypeDef(TypedDict):
    StatisticId: NotRequired[str]
    ProfileId: NotRequired[str]
    RunIdentifier: NotRequired[RunIdentifierTypeDef]
    StatisticName: NotRequired[str]
    DoubleValue: NotRequired[float]
    EvaluationLevel: NotRequired[StatisticEvaluationLevelType]
    ColumnsReferenced: NotRequired[List[str]]
    ReferencedDatasets: NotRequired[List[str]]
    StatisticProperties: NotRequired[Dict[str, str]]
    RecordedOn: NotRequired[datetime]
    InclusionAnnotation: NotRequired[TimestampedInclusionAnnotationTypeDef]

TransformConfigParameterUnionTypeDef = Union[
    TransformConfigParameterTypeDef, TransformConfigParameterOutputTypeDef
]
UnionUnionTypeDef = Union[UnionTypeDef, UnionOutputTypeDef]

class UpdateClassifierRequestTypeDef(TypedDict):
    GrokClassifier: NotRequired[UpdateGrokClassifierRequestTypeDef]
    XMLClassifier: NotRequired[UpdateXMLClassifierRequestTypeDef]
    JsonClassifier: NotRequired[UpdateJsonClassifierRequestTypeDef]
    CsvClassifier: NotRequired[UpdateCsvClassifierRequestTypeDef]

UpsertRedshiftTargetOptionsUnionTypeDef = Union[
    UpsertRedshiftTargetOptionsTypeDef, UpsertRedshiftTargetOptionsOutputTypeDef
]

class ViewDefinitionInputTypeDef(TypedDict):
    IsProtected: NotRequired[bool]
    Definer: NotRequired[str]
    Representations: NotRequired[Sequence[ViewRepresentationInputTypeDef]]
    SubObjects: NotRequired[Sequence[str]]

class ViewDefinitionTypeDef(TypedDict):
    IsProtected: NotRequired[bool]
    Definer: NotRequired[str]
    SubObjects: NotRequired[List[str]]
    Representations: NotRequired[List[ViewRepresentationTypeDef]]

ActionUnionTypeDef = Union[ActionTypeDef, ActionOutputTypeDef]

class AggregateTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Groups: Sequence[Sequence[str]]
    Aggs: Sequence[AggregateOperationUnionTypeDef]

class AuthConfigurationTypeDef(TypedDict):
    AuthenticationType: PropertyTypeDef
    SecretArn: NotRequired[PropertyTypeDef]
    OAuth2Properties: NotRequired[Dict[str, PropertyTypeDef]]
    BasicAuthenticationProperties: NotRequired[Dict[str, PropertyTypeDef]]
    CustomAuthenticationProperties: NotRequired[Dict[str, PropertyTypeDef]]

class ComputeEnvironmentConfigurationTypeDef(TypedDict):
    Name: str
    Description: str
    ComputeEnvironment: ComputeEnvironmentType
    SupportedAuthenticationTypes: List[AuthenticationTypeType]
    ConnectionOptions: Dict[str, PropertyTypeDef]
    ConnectionPropertyNameOverrides: Dict[str, str]
    ConnectionOptionNameOverrides: Dict[str, str]
    ConnectionPropertiesRequiredOverrides: List[str]
    PhysicalConnectionPropertiesRequired: NotRequired[bool]

class AmazonRedshiftSourceOutputTypeDef(TypedDict):
    Name: NotRequired[str]
    Data: NotRequired[AmazonRedshiftNodeDataOutputTypeDef]

class AmazonRedshiftTargetOutputTypeDef(TypedDict):
    Name: NotRequired[str]
    Data: NotRequired[AmazonRedshiftNodeDataOutputTypeDef]
    Inputs: NotRequired[List[str]]

AmazonRedshiftNodeDataUnionTypeDef = Union[
    AmazonRedshiftNodeDataTypeDef, AmazonRedshiftNodeDataOutputTypeDef
]

class SnowflakeTargetOutputTypeDef(TypedDict):
    Name: str
    Data: SnowflakeNodeDataOutputTypeDef
    Inputs: NotRequired[List[str]]

SnowflakeNodeDataUnionTypeDef = Union[SnowflakeNodeDataTypeDef, SnowflakeNodeDataOutputTypeDef]

class PartitionIndexDescriptorTypeDef(TypedDict):
    IndexName: str
    Keys: List[KeySchemaElementTypeDef]
    IndexStatus: PartitionIndexStatusType
    BackfillErrors: NotRequired[List[BackfillErrorTypeDef]]

class BatchStopJobRunResponseTypeDef(TypedDict):
    SuccessfulSubmissions: List[BatchStopJobRunSuccessfulSubmissionTypeDef]
    Errors: List[BatchStopJobRunErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdatePartitionResponseTypeDef(TypedDict):
    Errors: List[BatchUpdatePartitionFailureEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreatePartitionResponseTypeDef(TypedDict):
    Errors: List[PartitionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeletePartitionResponseTypeDef(TypedDict):
    Errors: List[PartitionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteTableResponseTypeDef(TypedDict):
    Errors: List[TableErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteTableVersionResponseTypeDef(TypedDict):
    Errors: List[TableVersionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StatusDetailsPaginatorTypeDef(TypedDict):
    RequestedChange: NotRequired[Dict[str, Any]]
    ViewValidations: NotRequired[List[ViewValidationTypeDef]]

class StatusDetailsTypeDef(TypedDict):
    RequestedChange: NotRequired[Dict[str, Any]]
    ViewValidations: NotRequired[List[ViewValidationTypeDef]]

DecimalNumberUnionTypeDef = Union[DecimalNumberTypeDef, DecimalNumberOutputTypeDef]

class BatchGetBlueprintsResponseTypeDef(TypedDict):
    Blueprints: List[BlueprintTypeDef]
    MissingBlueprints: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetBlueprintResponseTypeDef(TypedDict):
    Blueprint: BlueprintTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectionTypesResponseTypeDef(TypedDict):
    ConnectionTypes: List[ConnectionTypeBriefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

GovernedCatalogTargetUnionTypeDef = Union[
    GovernedCatalogTargetTypeDef, GovernedCatalogTargetOutputTypeDef
]
S3CatalogTargetUnionTypeDef = Union[S3CatalogTargetTypeDef, S3CatalogTargetOutputTypeDef]
S3DeltaCatalogTargetUnionTypeDef = Union[
    S3DeltaCatalogTargetTypeDef, S3DeltaCatalogTargetOutputTypeDef
]
S3HudiCatalogTargetUnionTypeDef = Union[
    S3HudiCatalogTargetTypeDef, S3HudiCatalogTargetOutputTypeDef
]

class GetClassifierResponseTypeDef(TypedDict):
    Classifier: ClassifierTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetClassifiersResponseTypeDef(TypedDict):
    Classifiers: List[ClassifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetDataflowGraphResponseTypeDef(TypedDict):
    DagNodes: List[CodeGenNodeOutputTypeDef]
    DagEdges: List[CodeGenEdgeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

CodeGenNodeUnionTypeDef = Union[CodeGenNodeTypeDef, CodeGenNodeOutputTypeDef]

class GetMappingRequestTypeDef(TypedDict):
    Source: CatalogEntryTypeDef
    Sinks: NotRequired[Sequence[CatalogEntryTypeDef]]
    Location: NotRequired[LocationTypeDef]

GetPlanRequestTypeDef = TypedDict(
    "GetPlanRequestTypeDef",
    {
        "Mapping": Sequence[MappingEntryTypeDef],
        "Source": CatalogEntryTypeDef,
        "Sinks": NotRequired[Sequence[CatalogEntryTypeDef]],
        "Location": NotRequired[LocationTypeDef],
        "Language": NotRequired[LanguageType],
        "AdditionalPlanOptionsMap": NotRequired[Mapping[str, str]],
    },
)

class GetColumnStatisticsTaskSettingsResponseTypeDef(TypedDict):
    ColumnStatisticsTaskSettings: ColumnStatisticsTaskSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

DateColumnStatisticsDataUnionTypeDef = Union[
    DateColumnStatisticsDataTypeDef, DateColumnStatisticsDataOutputTypeDef
]
KafkaStreamingSourceOptionsUnionTypeDef = Union[
    KafkaStreamingSourceOptionsTypeDef, KafkaStreamingSourceOptionsOutputTypeDef
]
KinesisStreamingSourceOptionsUnionTypeDef = Union[
    KinesisStreamingSourceOptionsTypeDef, KinesisStreamingSourceOptionsOutputTypeDef
]

class GetUnfilteredPartitionMetadataRequestTypeDef(TypedDict):
    CatalogId: str
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    SupportedPermissionTypes: Sequence[PermissionTypeType]
    Region: NotRequired[str]
    AuditContext: NotRequired[AuditContextTypeDef]
    QuerySessionContext: NotRequired[QuerySessionContextTypeDef]

class GetUnfilteredPartitionsMetadataRequestTypeDef(TypedDict):
    CatalogId: str
    DatabaseName: str
    TableName: str
    SupportedPermissionTypes: Sequence[PermissionTypeType]
    Region: NotRequired[str]
    Expression: NotRequired[str]
    AuditContext: NotRequired[AuditContextTypeDef]
    NextToken: NotRequired[str]
    Segment: NotRequired[SegmentTypeDef]
    MaxResults: NotRequired[int]
    QuerySessionContext: NotRequired[QuerySessionContextTypeDef]

class GetUnfilteredTableMetadataRequestTypeDef(TypedDict):
    CatalogId: str
    DatabaseName: str
    Name: str
    SupportedPermissionTypes: Sequence[PermissionTypeType]
    Region: NotRequired[str]
    AuditContext: NotRequired[AuditContextTypeDef]
    ParentResourceArn: NotRequired[str]
    RootResourceArn: NotRequired[str]
    SupportedDialect: NotRequired[SupportedDialectTypeDef]
    Permissions: NotRequired[Sequence[PermissionType]]
    QuerySessionContext: NotRequired[QuerySessionContextTypeDef]

class GetMLTaskRunsRequestTypeDef(TypedDict):
    TransformId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filter: NotRequired[TaskRunFilterCriteriaTypeDef]
    Sort: NotRequired[TaskRunSortCriteriaTypeDef]

class ListDataQualityStatisticAnnotationsRequestTypeDef(TypedDict):
    StatisticId: NotRequired[str]
    ProfileId: NotRequired[str]
    TimestampFilter: NotRequired[TimestampFilterTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListDataQualityStatisticsRequestTypeDef(TypedDict):
    StatisticId: NotRequired[str]
    ProfileId: NotRequired[str]
    TimestampFilter: NotRequired[TimestampFilterTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

TriggerTypeDef = TypedDict(
    "TriggerTypeDef",
    {
        "Name": NotRequired[str],
        "WorkflowName": NotRequired[str],
        "Id": NotRequired[str],
        "Type": NotRequired[TriggerTypeType],
        "State": NotRequired[TriggerStateType],
        "Description": NotRequired[str],
        "Schedule": NotRequired[str],
        "Actions": NotRequired[List[ActionOutputTypeDef]],
        "Predicate": NotRequired[PredicateOutputTypeDef],
        "EventBatchingCondition": NotRequired[EventBatchingConditionTypeDef],
    },
)
PredicateUnionTypeDef = Union[PredicateTypeDef, PredicateOutputTypeDef]

class GetUsageProfileResponseTypeDef(TypedDict):
    Name: str
    Description: str
    Configuration: ProfileConfigurationOutputTypeDef
    CreatedOn: datetime
    LastModifiedOn: datetime
    ResponseMetadata: ResponseMetadataTypeDef

ProfileConfigurationUnionTypeDef = Union[
    ProfileConfigurationTypeDef, ProfileConfigurationOutputTypeDef
]

class EvaluationMetricsTypeDef(TypedDict):
    TransformType: Literal["FIND_MATCHES"]
    FindMatchesMetrics: NotRequired[FindMatchesMetricsTypeDef]

class CreateSessionRequestTypeDef(TypedDict):
    Id: str
    Role: str
    Command: SessionCommandTypeDef
    Description: NotRequired[str]
    Timeout: NotRequired[int]
    IdleTimeout: NotRequired[int]
    DefaultArguments: NotRequired[Mapping[str, str]]
    Connections: NotRequired[ConnectionsListUnionTypeDef]
    MaxCapacity: NotRequired[float]
    NumberOfWorkers: NotRequired[int]
    WorkerType: NotRequired[WorkerTypeType]
    SecurityConfiguration: NotRequired[str]
    GlueVersion: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    RequestOrigin: NotRequired[str]

class CrawlerTypeDef(TypedDict):
    Name: NotRequired[str]
    Role: NotRequired[str]
    Targets: NotRequired[CrawlerTargetsOutputTypeDef]
    DatabaseName: NotRequired[str]
    Description: NotRequired[str]
    Classifiers: NotRequired[List[str]]
    RecrawlPolicy: NotRequired[RecrawlPolicyTypeDef]
    SchemaChangePolicy: NotRequired[SchemaChangePolicyTypeDef]
    LineageConfiguration: NotRequired[LineageConfigurationTypeDef]
    State: NotRequired[CrawlerStateType]
    TablePrefix: NotRequired[str]
    Schedule: NotRequired[ScheduleTypeDef]
    CrawlElapsedTime: NotRequired[int]
    CreationTime: NotRequired[datetime]
    LastUpdated: NotRequired[datetime]
    LastCrawl: NotRequired[LastCrawlInfoTypeDef]
    Version: NotRequired[int]
    Configuration: NotRequired[str]
    CrawlerSecurityConfiguration: NotRequired[str]
    LakeFormationConfiguration: NotRequired[LakeFormationConfigurationTypeDef]

CrawlerTargetsUnionTypeDef = Union[CrawlerTargetsTypeDef, CrawlerTargetsOutputTypeDef]

class ListDataQualityRulesetsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filter: NotRequired[DataQualityRulesetFilterCriteriaTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class ListDataQualityRulesetsResponseTypeDef(TypedDict):
    Rulesets: List[DataQualityRulesetListDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeInboundIntegrationsResponseTypeDef(TypedDict):
    InboundIntegrations: List[InboundIntegrationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIntegrationsResponseTypeDef(TypedDict):
    Integrations: List[IntegrationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSessionResponseTypeDef(TypedDict):
    Session: SessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSessionResponseTypeDef(TypedDict):
    Session: SessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSessionsResponseTypeDef(TypedDict):
    Ids: List[str]
    Sessions: List[SessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

EvaluateDataQualityMultiFrameUnionTypeDef = Union[
    EvaluateDataQualityMultiFrameTypeDef, EvaluateDataQualityMultiFrameOutputTypeDef
]
EvaluateDataQualityUnionTypeDef = Union[
    EvaluateDataQualityTypeDef, EvaluateDataQualityOutputTypeDef
]

class GetDataCatalogEncryptionSettingsResponseTypeDef(TypedDict):
    DataCatalogEncryptionSettings: DataCatalogEncryptionSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDataCatalogEncryptionSettingsRequestTypeDef(TypedDict):
    DataCatalogEncryptionSettings: DataCatalogEncryptionSettingsTypeDef
    CatalogId: NotRequired[str]

class CatalogTypeDef(TypedDict):
    Name: str
    CatalogId: NotRequired[str]
    ResourceArn: NotRequired[str]
    Description: NotRequired[str]
    Parameters: NotRequired[Dict[str, str]]
    CreateTime: NotRequired[datetime]
    UpdateTime: NotRequired[datetime]
    TargetRedshiftCatalog: NotRequired[TargetRedshiftCatalogTypeDef]
    FederatedCatalog: NotRequired[FederatedCatalogTypeDef]
    CatalogProperties: NotRequired[CatalogPropertiesOutputTypeDef]
    CreateTableDefaultPermissions: NotRequired[List[PrincipalPermissionsOutputTypeDef]]
    CreateDatabaseDefaultPermissions: NotRequired[List[PrincipalPermissionsOutputTypeDef]]
    AllowFullTableExternalDataAccess: NotRequired[AllowFullTableExternalDataAccessEnumType]

class DatabaseTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    LocationUri: NotRequired[str]
    Parameters: NotRequired[Dict[str, str]]
    CreateTime: NotRequired[datetime]
    CreateTableDefaultPermissions: NotRequired[List[PrincipalPermissionsOutputTypeDef]]
    TargetDatabase: NotRequired[DatabaseIdentifierTypeDef]
    CatalogId: NotRequired[str]
    FederatedDatabase: NotRequired[FederatedDatabaseTypeDef]

PrincipalPermissionsUnionTypeDef = Union[
    PrincipalPermissionsTypeDef, PrincipalPermissionsOutputTypeDef
]

class DataQualityObservationTypeDef(TypedDict):
    Description: NotRequired[str]
    MetricBasedObservation: NotRequired[MetricBasedObservationTypeDef]

class DataQualityResultDescriptionTypeDef(TypedDict):
    ResultId: NotRequired[str]
    DataSource: NotRequired[DataSourceOutputTypeDef]
    JobName: NotRequired[str]
    JobRunId: NotRequired[str]
    StartedOn: NotRequired[datetime]

class DataQualityRuleRecommendationRunDescriptionTypeDef(TypedDict):
    RunId: NotRequired[str]
    Status: NotRequired[TaskStatusTypeType]
    StartedOn: NotRequired[datetime]
    DataSource: NotRequired[DataSourceOutputTypeDef]

class DataQualityRulesetEvaluationRunDescriptionTypeDef(TypedDict):
    RunId: NotRequired[str]
    Status: NotRequired[TaskStatusTypeType]
    StartedOn: NotRequired[datetime]
    DataSource: NotRequired[DataSourceOutputTypeDef]

class GetDataQualityRuleRecommendationRunResponseTypeDef(TypedDict):
    RunId: str
    DataSource: DataSourceOutputTypeDef
    Role: str
    NumberOfWorkers: int
    Timeout: int
    Status: TaskStatusTypeType
    ErrorString: str
    StartedOn: datetime
    LastModifiedOn: datetime
    CompletedOn: datetime
    ExecutionTime: int
    RecommendedRuleset: str
    CreatedRulesetName: str
    DataQualitySecurityConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataQualityRulesetEvaluationRunResponseTypeDef(TypedDict):
    RunId: str
    DataSource: DataSourceOutputTypeDef
    Role: str
    NumberOfWorkers: int
    Timeout: int
    AdditionalRunOptions: DataQualityEvaluationRunAdditionalRunOptionsTypeDef
    Status: TaskStatusTypeType
    ErrorString: str
    StartedOn: datetime
    LastModifiedOn: datetime
    CompletedOn: datetime
    ExecutionTime: int
    RulesetNames: List[str]
    ResultIds: List[str]
    AdditionalDataSources: Dict[str, DataSourceOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DropNullFieldsOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    NullCheckBoxList: NotRequired[NullCheckBoxListTypeDef]
    NullTextList: NotRequired[List[NullValueFieldTypeDef]]

class DropNullFieldsTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    NullCheckBoxList: NotRequired[NullCheckBoxListTypeDef]
    NullTextList: NotRequired[Sequence[NullValueFieldTypeDef]]

ColumnStatisticsDataOutputTypeDef = TypedDict(
    "ColumnStatisticsDataOutputTypeDef",
    {
        "Type": ColumnStatisticsTypeType,
        "BooleanColumnStatisticsData": NotRequired[BooleanColumnStatisticsDataTypeDef],
        "DateColumnStatisticsData": NotRequired[DateColumnStatisticsDataOutputTypeDef],
        "DecimalColumnStatisticsData": NotRequired[DecimalColumnStatisticsDataOutputTypeDef],
        "DoubleColumnStatisticsData": NotRequired[DoubleColumnStatisticsDataTypeDef],
        "LongColumnStatisticsData": NotRequired[LongColumnStatisticsDataTypeDef],
        "StringColumnStatisticsData": NotRequired[StringColumnStatisticsDataTypeDef],
        "BinaryColumnStatisticsData": NotRequired[BinaryColumnStatisticsDataTypeDef],
    },
)

class StorageDescriptorOutputTypeDef(TypedDict):
    Columns: NotRequired[List[ColumnOutputTypeDef]]
    Location: NotRequired[str]
    AdditionalLocations: NotRequired[List[str]]
    InputFormat: NotRequired[str]
    OutputFormat: NotRequired[str]
    Compressed: NotRequired[bool]
    NumberOfBuckets: NotRequired[int]
    SerdeInfo: NotRequired[SerDeInfoOutputTypeDef]
    BucketColumns: NotRequired[List[str]]
    SortColumns: NotRequired[List[OrderTypeDef]]
    Parameters: NotRequired[Dict[str, str]]
    SkewedInfo: NotRequired[SkewedInfoOutputTypeDef]
    StoredAsSubDirectories: NotRequired[bool]
    SchemaReference: NotRequired[SchemaReferenceTypeDef]

S3DeltaDirectTargetUnionTypeDef = Union[
    S3DeltaDirectTargetTypeDef, S3DeltaDirectTargetOutputTypeDef
]
S3DirectTargetUnionTypeDef = Union[S3DirectTargetTypeDef, S3DirectTargetOutputTypeDef]
S3GlueParquetTargetUnionTypeDef = Union[
    S3GlueParquetTargetTypeDef, S3GlueParquetTargetOutputTypeDef
]
S3HudiDirectTargetUnionTypeDef = Union[S3HudiDirectTargetTypeDef, S3HudiDirectTargetOutputTypeDef]

class SecurityConfigurationTypeDef(TypedDict):
    Name: NotRequired[str]
    CreatedTimeStamp: NotRequired[datetime]
    EncryptionConfiguration: NotRequired[EncryptionConfigurationOutputTypeDef]

EncryptionConfigurationUnionTypeDef = Union[
    EncryptionConfigurationTypeDef, EncryptionConfigurationOutputTypeDef
]

class DeleteSchemaVersionsResponseTypeDef(TypedDict):
    SchemaVersionErrors: List[SchemaVersionErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FilterOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    LogicalOperator: FilterLogicalOperatorType
    Filters: List[FilterExpressionOutputTypeDef]

class FilterExpressionTypeDef(TypedDict):
    Operation: FilterOperationType
    Values: Sequence[FilterValueUnionTypeDef]
    Negated: NotRequired[bool]

class UpdateMLTransformRequestTypeDef(TypedDict):
    TransformId: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    Parameters: NotRequired[TransformParametersTypeDef]
    Role: NotRequired[str]
    GlueVersion: NotRequired[str]
    MaxCapacity: NotRequired[float]
    WorkerType: NotRequired[WorkerTypeType]
    NumberOfWorkers: NotRequired[int]
    Timeout: NotRequired[int]
    MaxRetries: NotRequired[int]

class GetMLTransformsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filter: NotRequired[TransformFilterCriteriaTypeDef]
    Sort: NotRequired[TransformSortCriteriaTypeDef]

class ListMLTransformsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filter: NotRequired[TransformFilterCriteriaTypeDef]
    Sort: NotRequired[TransformSortCriteriaTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class AthenaConnectorSourceOutputTypeDef(TypedDict):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    SchemaName: str
    ConnectionTable: NotRequired[str]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class CatalogDeltaSourceOutputTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: NotRequired[Dict[str, str]]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class CatalogHudiSourceOutputTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: NotRequired[Dict[str, str]]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class ConnectorDataSourceOutputTypeDef(TypedDict):
    Name: str
    ConnectionType: str
    Data: Dict[str, str]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class CustomCodeOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    Code: str
    ClassName: str
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class DynamicTransformOutputTypeDef(TypedDict):
    Name: str
    TransformName: str
    Inputs: List[str]
    FunctionName: str
    Path: str
    Parameters: NotRequired[List[TransformConfigParameterOutputTypeDef]]
    Version: NotRequired[str]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class JDBCConnectorSourceOutputTypeDef(TypedDict):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: NotRequired[JDBCConnectorOptionsOutputTypeDef]
    ConnectionTable: NotRequired[str]
    Query: NotRequired[str]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class JDBCConnectorTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    ConnectionName: str
    ConnectionTable: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: NotRequired[Dict[str, str]]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class S3CatalogDeltaSourceOutputTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: NotRequired[Dict[str, str]]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class S3CatalogHudiSourceOutputTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: NotRequired[Dict[str, str]]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class S3CsvSourceOutputTypeDef(TypedDict):
    Name: str
    Paths: List[str]
    Separator: SeparatorType
    QuoteChar: QuoteCharType
    CompressionType: NotRequired[CompressionTypeType]
    Exclusions: NotRequired[List[str]]
    GroupSize: NotRequired[str]
    GroupFiles: NotRequired[str]
    Recurse: NotRequired[bool]
    MaxBand: NotRequired[int]
    MaxFilesInBand: NotRequired[int]
    AdditionalOptions: NotRequired[S3DirectSourceAdditionalOptionsTypeDef]
    Escaper: NotRequired[str]
    Multiline: NotRequired[bool]
    WithHeader: NotRequired[bool]
    WriteHeader: NotRequired[bool]
    SkipFirst: NotRequired[bool]
    OptimizePerformance: NotRequired[bool]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class S3DeltaSourceOutputTypeDef(TypedDict):
    Name: str
    Paths: List[str]
    AdditionalDeltaOptions: NotRequired[Dict[str, str]]
    AdditionalOptions: NotRequired[S3DirectSourceAdditionalOptionsTypeDef]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class S3HudiSourceOutputTypeDef(TypedDict):
    Name: str
    Paths: List[str]
    AdditionalHudiOptions: NotRequired[Dict[str, str]]
    AdditionalOptions: NotRequired[S3DirectSourceAdditionalOptionsTypeDef]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class S3JsonSourceOutputTypeDef(TypedDict):
    Name: str
    Paths: List[str]
    CompressionType: NotRequired[CompressionTypeType]
    Exclusions: NotRequired[List[str]]
    GroupSize: NotRequired[str]
    GroupFiles: NotRequired[str]
    Recurse: NotRequired[bool]
    MaxBand: NotRequired[int]
    MaxFilesInBand: NotRequired[int]
    AdditionalOptions: NotRequired[S3DirectSourceAdditionalOptionsTypeDef]
    JsonPath: NotRequired[str]
    Multiline: NotRequired[bool]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class S3ParquetSourceOutputTypeDef(TypedDict):
    Name: str
    Paths: List[str]
    CompressionType: NotRequired[ParquetCompressionTypeType]
    Exclusions: NotRequired[List[str]]
    GroupSize: NotRequired[str]
    GroupFiles: NotRequired[str]
    Recurse: NotRequired[bool]
    MaxBand: NotRequired[int]
    MaxFilesInBand: NotRequired[int]
    AdditionalOptions: NotRequired[S3DirectSourceAdditionalOptionsTypeDef]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class SnowflakeSourceOutputTypeDef(TypedDict):
    Name: str
    Data: SnowflakeNodeDataOutputTypeDef
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class SparkConnectorSourceOutputTypeDef(TypedDict):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: NotRequired[Dict[str, str]]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class SparkConnectorTargetOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: NotRequired[Dict[str, str]]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class SparkSQLOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    SqlQuery: str
    SqlAliases: List[SqlAliasTypeDef]
    OutputSchemas: NotRequired[List[GlueSchemaOutputTypeDef]]

class AthenaConnectorSourceTypeDef(TypedDict):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    SchemaName: str
    ConnectionTable: NotRequired[str]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class CatalogDeltaSourceTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: NotRequired[Mapping[str, str]]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class CatalogHudiSourceTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: NotRequired[Mapping[str, str]]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class CustomCodeTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Code: str
    ClassName: str
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

GlueSchemaUnionTypeDef = Union[GlueSchemaTypeDef, GlueSchemaOutputTypeDef]

class JDBCConnectorTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    ConnectionName: str
    ConnectionTable: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: NotRequired[Mapping[str, str]]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class S3CatalogDeltaSourceTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: NotRequired[Mapping[str, str]]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class S3CatalogHudiSourceTypeDef(TypedDict):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: NotRequired[Mapping[str, str]]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class S3CsvSourceTypeDef(TypedDict):
    Name: str
    Paths: Sequence[str]
    Separator: SeparatorType
    QuoteChar: QuoteCharType
    CompressionType: NotRequired[CompressionTypeType]
    Exclusions: NotRequired[Sequence[str]]
    GroupSize: NotRequired[str]
    GroupFiles: NotRequired[str]
    Recurse: NotRequired[bool]
    MaxBand: NotRequired[int]
    MaxFilesInBand: NotRequired[int]
    AdditionalOptions: NotRequired[S3DirectSourceAdditionalOptionsTypeDef]
    Escaper: NotRequired[str]
    Multiline: NotRequired[bool]
    WithHeader: NotRequired[bool]
    WriteHeader: NotRequired[bool]
    SkipFirst: NotRequired[bool]
    OptimizePerformance: NotRequired[bool]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class S3DeltaSourceTypeDef(TypedDict):
    Name: str
    Paths: Sequence[str]
    AdditionalDeltaOptions: NotRequired[Mapping[str, str]]
    AdditionalOptions: NotRequired[S3DirectSourceAdditionalOptionsTypeDef]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class S3HudiSourceTypeDef(TypedDict):
    Name: str
    Paths: Sequence[str]
    AdditionalHudiOptions: NotRequired[Mapping[str, str]]
    AdditionalOptions: NotRequired[S3DirectSourceAdditionalOptionsTypeDef]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class S3JsonSourceTypeDef(TypedDict):
    Name: str
    Paths: Sequence[str]
    CompressionType: NotRequired[CompressionTypeType]
    Exclusions: NotRequired[Sequence[str]]
    GroupSize: NotRequired[str]
    GroupFiles: NotRequired[str]
    Recurse: NotRequired[bool]
    MaxBand: NotRequired[int]
    MaxFilesInBand: NotRequired[int]
    AdditionalOptions: NotRequired[S3DirectSourceAdditionalOptionsTypeDef]
    JsonPath: NotRequired[str]
    Multiline: NotRequired[bool]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class S3ParquetSourceTypeDef(TypedDict):
    Name: str
    Paths: Sequence[str]
    CompressionType: NotRequired[ParquetCompressionTypeType]
    Exclusions: NotRequired[Sequence[str]]
    GroupSize: NotRequired[str]
    GroupFiles: NotRequired[str]
    Recurse: NotRequired[bool]
    MaxBand: NotRequired[int]
    MaxFilesInBand: NotRequired[int]
    AdditionalOptions: NotRequired[S3DirectSourceAdditionalOptionsTypeDef]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class SparkConnectorSourceTypeDef(TypedDict):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: NotRequired[Mapping[str, str]]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class SparkConnectorTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: NotRequired[Mapping[str, str]]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class SparkSQLTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    SqlQuery: str
    SqlAliases: Sequence[SqlAliasTypeDef]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class DataSourceTypeDef(TypedDict):
    GlueTable: GlueTableUnionTypeDef

class TableOptimizerConfigurationTypeDef(TypedDict):
    roleArn: NotRequired[str]
    enabled: NotRequired[bool]
    vpcConfiguration: NotRequired[TableOptimizerVpcConfigurationTypeDef]
    retentionConfiguration: NotRequired[RetentionConfigurationTypeDef]
    orphanFileDeletionConfiguration: NotRequired[OrphanFileDeletionConfigurationTypeDef]

class TableOptimizerRunTypeDef(TypedDict):
    eventType: NotRequired[TableOptimizerEventTypeType]
    startTimestamp: NotRequired[datetime]
    endTimestamp: NotRequired[datetime]
    metrics: NotRequired[RunMetricsTypeDef]
    error: NotRequired[str]
    compactionMetrics: NotRequired[CompactionMetricsTypeDef]
    retentionMetrics: NotRequired[RetentionMetricsTypeDef]
    orphanFileDeletionMetrics: NotRequired[OrphanFileDeletionMetricsTypeDef]

class GetIntegrationTablePropertiesResponseTypeDef(TypedDict):
    ResourceArn: str
    TableName: str
    SourceTableConfig: SourceTableConfigOutputTypeDef
    TargetTableConfig: TargetTableConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

TargetTableConfigUnionTypeDef = Union[TargetTableConfigTypeDef, TargetTableConfigOutputTypeDef]

class JDBCConnectorSourceTypeDef(TypedDict):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: NotRequired[JDBCConnectorOptionsUnionTypeDef]
    ConnectionTable: NotRequired[str]
    Query: NotRequired[str]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class GetJobRunResponseTypeDef(TypedDict):
    JobRun: JobRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobRunsResponseTypeDef(TypedDict):
    JobRuns: List[JobRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class JobNodeDetailsTypeDef(TypedDict):
    JobRuns: NotRequired[List[JobRunTypeDef]]

class JoinTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    JoinType: JoinTypeType
    Columns: Sequence[JoinColumnUnionTypeDef]

class GetMLTaskRunResponseTypeDef(TypedDict):
    TransformId: str
    TaskRunId: str
    Status: TaskStatusTypeType
    LogGroupName: str
    Properties: TaskRunPropertiesTypeDef
    ErrorString: str
    StartedOn: datetime
    LastModifiedOn: datetime
    CompletedOn: datetime
    ExecutionTime: int
    ResponseMetadata: ResponseMetadataTypeDef

class TaskRunTypeDef(TypedDict):
    TransformId: NotRequired[str]
    TaskRunId: NotRequired[str]
    Status: NotRequired[TaskStatusTypeType]
    LogGroupName: NotRequired[str]
    Properties: NotRequired[TaskRunPropertiesTypeDef]
    ErrorString: NotRequired[str]
    StartedOn: NotRequired[datetime]
    LastModifiedOn: NotRequired[datetime]
    CompletedOn: NotRequired[datetime]
    ExecutionTime: NotRequired[int]

class CreateMLTransformRequestTypeDef(TypedDict):
    Name: str
    InputRecordTables: Sequence[GlueTableUnionTypeDef]
    Parameters: TransformParametersTypeDef
    Role: str
    Description: NotRequired[str]
    GlueVersion: NotRequired[str]
    MaxCapacity: NotRequired[float]
    WorkerType: NotRequired[WorkerTypeType]
    NumberOfWorkers: NotRequired[int]
    Timeout: NotRequired[int]
    MaxRetries: NotRequired[int]
    Tags: NotRequired[Mapping[str, str]]
    TransformEncryption: NotRequired[TransformEncryptionTypeDef]

ApplyMappingTypeDef = TypedDict(
    "ApplyMappingTypeDef",
    {
        "Name": str,
        "Inputs": Sequence[str],
        "Mapping": Sequence[MappingUnionTypeDef],
    },
)

class QuerySchemaVersionMetadataResponseTypeDef(TypedDict):
    MetadataInfoMap: Dict[str, MetadataInfoTypeDef]
    SchemaVersionId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AuthenticationConfigurationTypeDef(TypedDict):
    AuthenticationType: NotRequired[AuthenticationTypeType]
    SecretArn: NotRequired[str]
    OAuth2Properties: NotRequired[OAuth2PropertiesTypeDef]

class AuthenticationConfigurationInputTypeDef(TypedDict):
    AuthenticationType: NotRequired[AuthenticationTypeType]
    OAuth2Properties: NotRequired[OAuth2PropertiesInputTypeDef]
    SecretArn: NotRequired[str]
    KmsKeyArn: NotRequired[str]
    BasicAuthenticationCredentials: NotRequired[BasicAuthenticationCredentialsTypeDef]
    CustomAuthenticationCredentials: NotRequired[Mapping[str, str]]

class BatchDeletePartitionRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    PartitionsToDelete: Sequence[PartitionValueListUnionTypeDef]
    CatalogId: NotRequired[str]

class BatchGetPartitionRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    PartitionsToGet: Sequence[PartitionValueListUnionTypeDef]
    CatalogId: NotRequired[str]

class RecipeOutputTypeDef(TypedDict):
    Name: str
    Inputs: List[str]
    RecipeReference: NotRequired[RecipeReferenceTypeDef]
    RecipeSteps: NotRequired[List[RecipeStepOutputTypeDef]]

class RecipeStepTypeDef(TypedDict):
    Action: RecipeActionUnionTypeDef
    ConditionExpressions: NotRequired[Sequence[ConditionExpressionTypeDef]]

class CreateUserDefinedFunctionRequestTypeDef(TypedDict):
    DatabaseName: str
    FunctionInput: UserDefinedFunctionInputTypeDef
    CatalogId: NotRequired[str]

class UpdateUserDefinedFunctionRequestTypeDef(TypedDict):
    DatabaseName: str
    FunctionName: str
    FunctionInput: UserDefinedFunctionInputTypeDef
    CatalogId: NotRequired[str]

class GetUserDefinedFunctionResponseTypeDef(TypedDict):
    UserDefinedFunction: UserDefinedFunctionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserDefinedFunctionsResponseTypeDef(TypedDict):
    UserDefinedFunctions: List[UserDefinedFunctionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StorageDescriptorTypeDef(TypedDict):
    Columns: NotRequired[Sequence[ColumnUnionTypeDef]]
    Location: NotRequired[str]
    AdditionalLocations: NotRequired[Sequence[str]]
    InputFormat: NotRequired[str]
    OutputFormat: NotRequired[str]
    Compressed: NotRequired[bool]
    NumberOfBuckets: NotRequired[int]
    SerdeInfo: NotRequired[SerDeInfoUnionTypeDef]
    BucketColumns: NotRequired[Sequence[str]]
    SortColumns: NotRequired[Sequence[OrderTypeDef]]
    Parameters: NotRequired[Mapping[str, str]]
    SkewedInfo: NotRequired[SkewedInfoUnionTypeDef]
    StoredAsSubDirectories: NotRequired[bool]
    SchemaReference: NotRequired[SchemaReferenceTypeDef]

class StatementTypeDef(TypedDict):
    Id: NotRequired[int]
    Code: NotRequired[str]
    State: NotRequired[StatementStateType]
    Output: NotRequired[StatementOutputTypeDef]
    Progress: NotRequired[float]
    StartedOn: NotRequired[int]
    CompletedOn: NotRequired[int]

class ListDataQualityStatisticAnnotationsResponseTypeDef(TypedDict):
    Annotations: List[StatisticAnnotationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDataQualityStatisticsResponseTypeDef(TypedDict):
    Statistics: List[StatisticSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DynamicTransformTypeDef(TypedDict):
    Name: str
    TransformName: str
    Inputs: Sequence[str]
    FunctionName: str
    Path: str
    Parameters: NotRequired[Sequence[TransformConfigParameterUnionTypeDef]]
    Version: NotRequired[str]
    OutputSchemas: NotRequired[Sequence[GlueSchemaTypeDef]]

class RedshiftTargetTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str
    RedshiftTmpDir: NotRequired[str]
    TmpDirIAMRole: NotRequired[str]
    UpsertRedshiftOptions: NotRequired[UpsertRedshiftTargetOptionsUnionTypeDef]

AggregateUnionTypeDef = Union[AggregateTypeDef, AggregateOutputTypeDef]

class DescribeConnectionTypeResponseTypeDef(TypedDict):
    ConnectionType: str
    Description: str
    Capabilities: CapabilitiesTypeDef
    ConnectionProperties: Dict[str, PropertyTypeDef]
    ConnectionOptions: Dict[str, PropertyTypeDef]
    AuthenticationConfiguration: AuthConfigurationTypeDef
    ComputeEnvironmentConfigurations: Dict[str, ComputeEnvironmentConfigurationTypeDef]
    PhysicalConnectionRequirements: Dict[str, PropertyTypeDef]
    AthenaConnectionProperties: Dict[str, PropertyTypeDef]
    PythonConnectionProperties: Dict[str, PropertyTypeDef]
    SparkConnectionProperties: Dict[str, PropertyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AmazonRedshiftSourceTypeDef(TypedDict):
    Name: NotRequired[str]
    Data: NotRequired[AmazonRedshiftNodeDataUnionTypeDef]

class AmazonRedshiftTargetTypeDef(TypedDict):
    Name: NotRequired[str]
    Data: NotRequired[AmazonRedshiftNodeDataUnionTypeDef]
    Inputs: NotRequired[Sequence[str]]

class SnowflakeTargetTypeDef(TypedDict):
    Name: str
    Data: SnowflakeNodeDataUnionTypeDef
    Inputs: NotRequired[Sequence[str]]

class GetPartitionIndexesResponseTypeDef(TypedDict):
    PartitionIndexDescriptorList: List[PartitionIndexDescriptorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TableStatusPaginatorTypeDef(TypedDict):
    RequestedBy: NotRequired[str]
    UpdatedBy: NotRequired[str]
    RequestTime: NotRequired[datetime]
    UpdateTime: NotRequired[datetime]
    Action: NotRequired[ResourceActionType]
    State: NotRequired[ResourceStateType]
    Error: NotRequired[ErrorDetailTypeDef]
    Details: NotRequired[StatusDetailsPaginatorTypeDef]

class TableStatusTypeDef(TypedDict):
    RequestedBy: NotRequired[str]
    UpdatedBy: NotRequired[str]
    RequestTime: NotRequired[datetime]
    UpdateTime: NotRequired[datetime]
    Action: NotRequired[ResourceActionType]
    State: NotRequired[ResourceStateType]
    Error: NotRequired[ErrorDetailTypeDef]
    Details: NotRequired[StatusDetailsTypeDef]

class DecimalColumnStatisticsDataTypeDef(TypedDict):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: NotRequired[DecimalNumberUnionTypeDef]
    MaximumValue: NotRequired[DecimalNumberUnionTypeDef]

class CreateScriptRequestTypeDef(TypedDict):
    DagNodes: NotRequired[Sequence[CodeGenNodeUnionTypeDef]]
    DagEdges: NotRequired[Sequence[CodeGenEdgeTypeDef]]
    Language: NotRequired[LanguageType]

class CatalogKafkaSourceTypeDef(TypedDict):
    Name: str
    Table: str
    Database: str
    WindowSize: NotRequired[int]
    DetectSchema: NotRequired[bool]
    StreamingOptions: NotRequired[KafkaStreamingSourceOptionsUnionTypeDef]
    DataPreviewOptions: NotRequired[StreamingDataPreviewOptionsTypeDef]

class DirectKafkaSourceTypeDef(TypedDict):
    Name: str
    StreamingOptions: NotRequired[KafkaStreamingSourceOptionsUnionTypeDef]
    WindowSize: NotRequired[int]
    DetectSchema: NotRequired[bool]
    DataPreviewOptions: NotRequired[StreamingDataPreviewOptionsTypeDef]

class CatalogKinesisSourceTypeDef(TypedDict):
    Name: str
    Table: str
    Database: str
    WindowSize: NotRequired[int]
    DetectSchema: NotRequired[bool]
    StreamingOptions: NotRequired[KinesisStreamingSourceOptionsUnionTypeDef]
    DataPreviewOptions: NotRequired[StreamingDataPreviewOptionsTypeDef]

class DirectKinesisSourceTypeDef(TypedDict):
    Name: str
    WindowSize: NotRequired[int]
    DetectSchema: NotRequired[bool]
    StreamingOptions: NotRequired[KinesisStreamingSourceOptionsUnionTypeDef]
    DataPreviewOptions: NotRequired[StreamingDataPreviewOptionsTypeDef]

class BatchGetTriggersResponseTypeDef(TypedDict):
    Triggers: List[TriggerTypeDef]
    TriggersNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTriggerResponseTypeDef(TypedDict):
    Trigger: TriggerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTriggersResponseTypeDef(TypedDict):
    Triggers: List[TriggerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TriggerNodeDetailsTypeDef(TypedDict):
    Trigger: NotRequired[TriggerTypeDef]

class UpdateTriggerResponseTypeDef(TypedDict):
    Trigger: TriggerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CreateTriggerRequestTypeDef = TypedDict(
    "CreateTriggerRequestTypeDef",
    {
        "Name": str,
        "Type": TriggerTypeType,
        "Actions": Sequence[ActionUnionTypeDef],
        "WorkflowName": NotRequired[str],
        "Schedule": NotRequired[str],
        "Predicate": NotRequired[PredicateUnionTypeDef],
        "Description": NotRequired[str],
        "StartOnCreation": NotRequired[bool],
        "Tags": NotRequired[Mapping[str, str]],
        "EventBatchingCondition": NotRequired[EventBatchingConditionTypeDef],
    },
)

class TriggerUpdateTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    Schedule: NotRequired[str]
    Actions: NotRequired[Sequence[ActionUnionTypeDef]]
    Predicate: NotRequired[PredicateUnionTypeDef]
    EventBatchingCondition: NotRequired[EventBatchingConditionTypeDef]

class CreateUsageProfileRequestTypeDef(TypedDict):
    Name: str
    Configuration: ProfileConfigurationUnionTypeDef
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class UpdateUsageProfileRequestTypeDef(TypedDict):
    Name: str
    Configuration: ProfileConfigurationUnionTypeDef
    Description: NotRequired[str]

class GetMLTransformResponseTypeDef(TypedDict):
    TransformId: str
    Name: str
    Description: str
    Status: TransformStatusTypeType
    CreatedOn: datetime
    LastModifiedOn: datetime
    InputRecordTables: List[GlueTableOutputTypeDef]
    Parameters: TransformParametersTypeDef
    EvaluationMetrics: EvaluationMetricsTypeDef
    LabelCount: int
    Schema: List[SchemaColumnTypeDef]
    Role: str
    GlueVersion: str
    MaxCapacity: float
    WorkerType: WorkerTypeType
    NumberOfWorkers: int
    Timeout: int
    MaxRetries: int
    TransformEncryption: TransformEncryptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MLTransformTypeDef(TypedDict):
    TransformId: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    Status: NotRequired[TransformStatusTypeType]
    CreatedOn: NotRequired[datetime]
    LastModifiedOn: NotRequired[datetime]
    InputRecordTables: NotRequired[List[GlueTableOutputTypeDef]]
    Parameters: NotRequired[TransformParametersTypeDef]
    EvaluationMetrics: NotRequired[EvaluationMetricsTypeDef]
    LabelCount: NotRequired[int]
    Schema: NotRequired[List[SchemaColumnTypeDef]]
    Role: NotRequired[str]
    GlueVersion: NotRequired[str]
    MaxCapacity: NotRequired[float]
    WorkerType: NotRequired[WorkerTypeType]
    NumberOfWorkers: NotRequired[int]
    Timeout: NotRequired[int]
    MaxRetries: NotRequired[int]
    TransformEncryption: NotRequired[TransformEncryptionTypeDef]

class BatchGetCrawlersResponseTypeDef(TypedDict):
    Crawlers: List[CrawlerTypeDef]
    CrawlersNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCrawlerResponseTypeDef(TypedDict):
    Crawler: CrawlerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCrawlersResponseTypeDef(TypedDict):
    Crawlers: List[CrawlerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateCrawlerRequestTypeDef(TypedDict):
    Name: str
    Role: str
    Targets: CrawlerTargetsUnionTypeDef
    DatabaseName: NotRequired[str]
    Description: NotRequired[str]
    Schedule: NotRequired[str]
    Classifiers: NotRequired[Sequence[str]]
    TablePrefix: NotRequired[str]
    SchemaChangePolicy: NotRequired[SchemaChangePolicyTypeDef]
    RecrawlPolicy: NotRequired[RecrawlPolicyTypeDef]
    LineageConfiguration: NotRequired[LineageConfigurationTypeDef]
    LakeFormationConfiguration: NotRequired[LakeFormationConfigurationTypeDef]
    Configuration: NotRequired[str]
    CrawlerSecurityConfiguration: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class UpdateCrawlerRequestTypeDef(TypedDict):
    Name: str
    Role: NotRequired[str]
    DatabaseName: NotRequired[str]
    Description: NotRequired[str]
    Targets: NotRequired[CrawlerTargetsUnionTypeDef]
    Schedule: NotRequired[str]
    Classifiers: NotRequired[Sequence[str]]
    TablePrefix: NotRequired[str]
    SchemaChangePolicy: NotRequired[SchemaChangePolicyTypeDef]
    RecrawlPolicy: NotRequired[RecrawlPolicyTypeDef]
    LineageConfiguration: NotRequired[LineageConfigurationTypeDef]
    LakeFormationConfiguration: NotRequired[LakeFormationConfigurationTypeDef]
    Configuration: NotRequired[str]
    CrawlerSecurityConfiguration: NotRequired[str]

class GetCatalogResponseTypeDef(TypedDict):
    Catalog: CatalogTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCatalogsResponseTypeDef(TypedDict):
    CatalogList: List[CatalogTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetDatabaseResponseTypeDef(TypedDict):
    Database: DatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDatabasesResponseTypeDef(TypedDict):
    DatabaseList: List[DatabaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CatalogInputTypeDef(TypedDict):
    Description: NotRequired[str]
    FederatedCatalog: NotRequired[FederatedCatalogTypeDef]
    Parameters: NotRequired[Mapping[str, str]]
    TargetRedshiftCatalog: NotRequired[TargetRedshiftCatalogTypeDef]
    CatalogProperties: NotRequired[CatalogPropertiesTypeDef]
    CreateTableDefaultPermissions: NotRequired[Sequence[PrincipalPermissionsUnionTypeDef]]
    CreateDatabaseDefaultPermissions: NotRequired[Sequence[PrincipalPermissionsUnionTypeDef]]
    AllowFullTableExternalDataAccess: NotRequired[AllowFullTableExternalDataAccessEnumType]

class DatabaseInputTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    LocationUri: NotRequired[str]
    Parameters: NotRequired[Mapping[str, str]]
    CreateTableDefaultPermissions: NotRequired[Sequence[PrincipalPermissionsUnionTypeDef]]
    TargetDatabase: NotRequired[DatabaseIdentifierTypeDef]
    FederatedDatabase: NotRequired[FederatedDatabaseTypeDef]

class DataQualityResultTypeDef(TypedDict):
    ResultId: NotRequired[str]
    ProfileId: NotRequired[str]
    Score: NotRequired[float]
    DataSource: NotRequired[DataSourceOutputTypeDef]
    RulesetName: NotRequired[str]
    EvaluationContext: NotRequired[str]
    StartedOn: NotRequired[datetime]
    CompletedOn: NotRequired[datetime]
    JobName: NotRequired[str]
    JobRunId: NotRequired[str]
    RulesetEvaluationRunId: NotRequired[str]
    RuleResults: NotRequired[List[DataQualityRuleResultTypeDef]]
    AnalyzerResults: NotRequired[List[DataQualityAnalyzerResultTypeDef]]
    Observations: NotRequired[List[DataQualityObservationTypeDef]]

class GetDataQualityResultResponseTypeDef(TypedDict):
    ResultId: str
    ProfileId: str
    Score: float
    DataSource: DataSourceOutputTypeDef
    RulesetName: str
    EvaluationContext: str
    StartedOn: datetime
    CompletedOn: datetime
    JobName: str
    JobRunId: str
    RulesetEvaluationRunId: str
    RuleResults: List[DataQualityRuleResultTypeDef]
    AnalyzerResults: List[DataQualityAnalyzerResultTypeDef]
    Observations: List[DataQualityObservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataQualityResultsResponseTypeDef(TypedDict):
    Results: List[DataQualityResultDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDataQualityRuleRecommendationRunsResponseTypeDef(TypedDict):
    Runs: List[DataQualityRuleRecommendationRunDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDataQualityRulesetEvaluationRunsResponseTypeDef(TypedDict):
    Runs: List[DataQualityRulesetEvaluationRunDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

DropNullFieldsUnionTypeDef = Union[DropNullFieldsTypeDef, DropNullFieldsOutputTypeDef]

class ColumnStatisticsOutputTypeDef(TypedDict):
    ColumnName: str
    ColumnType: str
    AnalyzedTime: datetime
    StatisticsData: ColumnStatisticsDataOutputTypeDef

class PartitionTypeDef(TypedDict):
    Values: NotRequired[List[str]]
    DatabaseName: NotRequired[str]
    TableName: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastAccessTime: NotRequired[datetime]
    StorageDescriptor: NotRequired[StorageDescriptorOutputTypeDef]
    Parameters: NotRequired[Dict[str, str]]
    LastAnalyzedTime: NotRequired[datetime]
    CatalogId: NotRequired[str]

class GetSecurityConfigurationResponseTypeDef(TypedDict):
    SecurityConfiguration: SecurityConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSecurityConfigurationsResponseTypeDef(TypedDict):
    SecurityConfigurations: List[SecurityConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateSecurityConfigurationRequestTypeDef(TypedDict):
    Name: str
    EncryptionConfiguration: EncryptionConfigurationUnionTypeDef

FilterExpressionUnionTypeDef = Union[FilterExpressionTypeDef, FilterExpressionOutputTypeDef]
AthenaConnectorSourceUnionTypeDef = Union[
    AthenaConnectorSourceTypeDef, AthenaConnectorSourceOutputTypeDef
]
CatalogDeltaSourceUnionTypeDef = Union[CatalogDeltaSourceTypeDef, CatalogDeltaSourceOutputTypeDef]
CatalogHudiSourceUnionTypeDef = Union[CatalogHudiSourceTypeDef, CatalogHudiSourceOutputTypeDef]
CustomCodeUnionTypeDef = Union[CustomCodeTypeDef, CustomCodeOutputTypeDef]

class ConnectorDataSourceTypeDef(TypedDict):
    Name: str
    ConnectionType: str
    Data: Mapping[str, str]
    OutputSchemas: NotRequired[Sequence[GlueSchemaUnionTypeDef]]

class SnowflakeSourceTypeDef(TypedDict):
    Name: str
    Data: SnowflakeNodeDataUnionTypeDef
    OutputSchemas: NotRequired[Sequence[GlueSchemaUnionTypeDef]]

JDBCConnectorTargetUnionTypeDef = Union[
    JDBCConnectorTargetTypeDef, JDBCConnectorTargetOutputTypeDef
]
S3CatalogDeltaSourceUnionTypeDef = Union[
    S3CatalogDeltaSourceTypeDef, S3CatalogDeltaSourceOutputTypeDef
]
S3CatalogHudiSourceUnionTypeDef = Union[
    S3CatalogHudiSourceTypeDef, S3CatalogHudiSourceOutputTypeDef
]
S3CsvSourceUnionTypeDef = Union[S3CsvSourceTypeDef, S3CsvSourceOutputTypeDef]
S3DeltaSourceUnionTypeDef = Union[S3DeltaSourceTypeDef, S3DeltaSourceOutputTypeDef]
S3HudiSourceUnionTypeDef = Union[S3HudiSourceTypeDef, S3HudiSourceOutputTypeDef]
S3JsonSourceUnionTypeDef = Union[S3JsonSourceTypeDef, S3JsonSourceOutputTypeDef]
S3ParquetSourceUnionTypeDef = Union[S3ParquetSourceTypeDef, S3ParquetSourceOutputTypeDef]
SparkConnectorSourceUnionTypeDef = Union[
    SparkConnectorSourceTypeDef, SparkConnectorSourceOutputTypeDef
]
SparkConnectorTargetUnionTypeDef = Union[
    SparkConnectorTargetTypeDef, SparkConnectorTargetOutputTypeDef
]
SparkSQLUnionTypeDef = Union[SparkSQLTypeDef, SparkSQLOutputTypeDef]
DataSourceUnionTypeDef = Union[DataSourceTypeDef, DataSourceOutputTypeDef]
CreateTableOptimizerRequestTypeDef = TypedDict(
    "CreateTableOptimizerRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Type": TableOptimizerTypeType,
        "TableOptimizerConfiguration": TableOptimizerConfigurationTypeDef,
    },
)
UpdateTableOptimizerRequestTypeDef = TypedDict(
    "UpdateTableOptimizerRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Type": TableOptimizerTypeType,
        "TableOptimizerConfiguration": TableOptimizerConfigurationTypeDef,
    },
)

class ListTableOptimizerRunsResponseTypeDef(TypedDict):
    CatalogId: str
    DatabaseName: str
    TableName: str
    TableOptimizerRuns: List[TableOptimizerRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

TableOptimizerTypeDef = TypedDict(
    "TableOptimizerTypeDef",
    {
        "type": NotRequired[TableOptimizerTypeType],
        "configuration": NotRequired[TableOptimizerConfigurationTypeDef],
        "lastRun": NotRequired[TableOptimizerRunTypeDef],
    },
)

class CreateIntegrationTablePropertiesRequestTypeDef(TypedDict):
    ResourceArn: str
    TableName: str
    SourceTableConfig: NotRequired[SourceTableConfigUnionTypeDef]
    TargetTableConfig: NotRequired[TargetTableConfigUnionTypeDef]

class UpdateIntegrationTablePropertiesRequestTypeDef(TypedDict):
    ResourceArn: str
    TableName: str
    SourceTableConfig: NotRequired[SourceTableConfigUnionTypeDef]
    TargetTableConfig: NotRequired[TargetTableConfigUnionTypeDef]

JDBCConnectorSourceUnionTypeDef = Union[
    JDBCConnectorSourceTypeDef, JDBCConnectorSourceOutputTypeDef
]
JoinUnionTypeDef = Union[JoinTypeDef, JoinOutputTypeDef]

class GetMLTaskRunsResponseTypeDef(TypedDict):
    TaskRuns: List[TaskRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

ApplyMappingUnionTypeDef = Union[ApplyMappingTypeDef, ApplyMappingOutputTypeDef]

class ConnectionTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    ConnectionType: NotRequired[ConnectionTypeType]
    MatchCriteria: NotRequired[List[str]]
    ConnectionProperties: NotRequired[Dict[ConnectionPropertyKeyType, str]]
    SparkProperties: NotRequired[Dict[str, str]]
    AthenaProperties: NotRequired[Dict[str, str]]
    PythonProperties: NotRequired[Dict[str, str]]
    PhysicalConnectionRequirements: NotRequired[PhysicalConnectionRequirementsOutputTypeDef]
    CreationTime: NotRequired[datetime]
    LastUpdatedTime: NotRequired[datetime]
    LastUpdatedBy: NotRequired[str]
    Status: NotRequired[ConnectionStatusType]
    StatusReason: NotRequired[str]
    LastConnectionValidationTime: NotRequired[datetime]
    AuthenticationConfiguration: NotRequired[AuthenticationConfigurationTypeDef]
    ConnectionSchemaVersion: NotRequired[int]
    CompatibleComputeEnvironments: NotRequired[List[ComputeEnvironmentType]]

class ConnectionInputTypeDef(TypedDict):
    Name: str
    ConnectionType: ConnectionTypeType
    ConnectionProperties: Mapping[ConnectionPropertyKeyType, str]
    Description: NotRequired[str]
    MatchCriteria: NotRequired[Sequence[str]]
    SparkProperties: NotRequired[Mapping[str, str]]
    AthenaProperties: NotRequired[Mapping[str, str]]
    PythonProperties: NotRequired[Mapping[str, str]]
    PhysicalConnectionRequirements: NotRequired[PhysicalConnectionRequirementsUnionTypeDef]
    AuthenticationConfiguration: NotRequired[AuthenticationConfigurationInputTypeDef]
    ValidateCredentials: NotRequired[bool]
    ValidateForComputeEnvironments: NotRequired[Sequence[ComputeEnvironmentType]]

class TestConnectionInputTypeDef(TypedDict):
    ConnectionType: ConnectionTypeType
    ConnectionProperties: Mapping[ConnectionPropertyKeyType, str]
    AuthenticationConfiguration: NotRequired[AuthenticationConfigurationInputTypeDef]

CodeGenConfigurationNodeOutputTypeDef = TypedDict(
    "CodeGenConfigurationNodeOutputTypeDef",
    {
        "AthenaConnectorSource": NotRequired[AthenaConnectorSourceOutputTypeDef],
        "JDBCConnectorSource": NotRequired[JDBCConnectorSourceOutputTypeDef],
        "SparkConnectorSource": NotRequired[SparkConnectorSourceOutputTypeDef],
        "CatalogSource": NotRequired[CatalogSourceTypeDef],
        "RedshiftSource": NotRequired[RedshiftSourceTypeDef],
        "S3CatalogSource": NotRequired[S3CatalogSourceTypeDef],
        "S3CsvSource": NotRequired[S3CsvSourceOutputTypeDef],
        "S3JsonSource": NotRequired[S3JsonSourceOutputTypeDef],
        "S3ParquetSource": NotRequired[S3ParquetSourceOutputTypeDef],
        "RelationalCatalogSource": NotRequired[RelationalCatalogSourceTypeDef],
        "DynamoDBCatalogSource": NotRequired[DynamoDBCatalogSourceTypeDef],
        "JDBCConnectorTarget": NotRequired[JDBCConnectorTargetOutputTypeDef],
        "SparkConnectorTarget": NotRequired[SparkConnectorTargetOutputTypeDef],
        "CatalogTarget": NotRequired[BasicCatalogTargetOutputTypeDef],
        "RedshiftTarget": NotRequired[RedshiftTargetOutputTypeDef],
        "S3CatalogTarget": NotRequired[S3CatalogTargetOutputTypeDef],
        "S3GlueParquetTarget": NotRequired[S3GlueParquetTargetOutputTypeDef],
        "S3DirectTarget": NotRequired[S3DirectTargetOutputTypeDef],
        "ApplyMapping": NotRequired[ApplyMappingOutputTypeDef],
        "SelectFields": NotRequired[SelectFieldsOutputTypeDef],
        "DropFields": NotRequired[DropFieldsOutputTypeDef],
        "RenameField": NotRequired[RenameFieldOutputTypeDef],
        "Spigot": NotRequired[SpigotOutputTypeDef],
        "Join": NotRequired[JoinOutputTypeDef],
        "SplitFields": NotRequired[SplitFieldsOutputTypeDef],
        "SelectFromCollection": NotRequired[SelectFromCollectionOutputTypeDef],
        "FillMissingValues": NotRequired[FillMissingValuesOutputTypeDef],
        "Filter": NotRequired[FilterOutputTypeDef],
        "CustomCode": NotRequired[CustomCodeOutputTypeDef],
        "SparkSQL": NotRequired[SparkSQLOutputTypeDef],
        "DirectKinesisSource": NotRequired[DirectKinesisSourceOutputTypeDef],
        "DirectKafkaSource": NotRequired[DirectKafkaSourceOutputTypeDef],
        "CatalogKinesisSource": NotRequired[CatalogKinesisSourceOutputTypeDef],
        "CatalogKafkaSource": NotRequired[CatalogKafkaSourceOutputTypeDef],
        "DropNullFields": NotRequired[DropNullFieldsOutputTypeDef],
        "Merge": NotRequired[MergeOutputTypeDef],
        "Union": NotRequired[UnionOutputTypeDef],
        "PIIDetection": NotRequired[PIIDetectionOutputTypeDef],
        "Aggregate": NotRequired[AggregateOutputTypeDef],
        "DropDuplicates": NotRequired[DropDuplicatesOutputTypeDef],
        "GovernedCatalogTarget": NotRequired[GovernedCatalogTargetOutputTypeDef],
        "GovernedCatalogSource": NotRequired[GovernedCatalogSourceTypeDef],
        "MicrosoftSQLServerCatalogSource": NotRequired[MicrosoftSQLServerCatalogSourceTypeDef],
        "MySQLCatalogSource": NotRequired[MySQLCatalogSourceTypeDef],
        "OracleSQLCatalogSource": NotRequired[OracleSQLCatalogSourceTypeDef],
        "PostgreSQLCatalogSource": NotRequired[PostgreSQLCatalogSourceTypeDef],
        "MicrosoftSQLServerCatalogTarget": NotRequired[
            MicrosoftSQLServerCatalogTargetOutputTypeDef
        ],
        "MySQLCatalogTarget": NotRequired[MySQLCatalogTargetOutputTypeDef],
        "OracleSQLCatalogTarget": NotRequired[OracleSQLCatalogTargetOutputTypeDef],
        "PostgreSQLCatalogTarget": NotRequired[PostgreSQLCatalogTargetOutputTypeDef],
        "DynamicTransform": NotRequired[DynamicTransformOutputTypeDef],
        "EvaluateDataQuality": NotRequired[EvaluateDataQualityOutputTypeDef],
        "S3CatalogHudiSource": NotRequired[S3CatalogHudiSourceOutputTypeDef],
        "CatalogHudiSource": NotRequired[CatalogHudiSourceOutputTypeDef],
        "S3HudiSource": NotRequired[S3HudiSourceOutputTypeDef],
        "S3HudiCatalogTarget": NotRequired[S3HudiCatalogTargetOutputTypeDef],
        "S3HudiDirectTarget": NotRequired[S3HudiDirectTargetOutputTypeDef],
        "DirectJDBCSource": NotRequired[DirectJDBCSourceTypeDef],
        "S3CatalogDeltaSource": NotRequired[S3CatalogDeltaSourceOutputTypeDef],
        "CatalogDeltaSource": NotRequired[CatalogDeltaSourceOutputTypeDef],
        "S3DeltaSource": NotRequired[S3DeltaSourceOutputTypeDef],
        "S3DeltaCatalogTarget": NotRequired[S3DeltaCatalogTargetOutputTypeDef],
        "S3DeltaDirectTarget": NotRequired[S3DeltaDirectTargetOutputTypeDef],
        "AmazonRedshiftSource": NotRequired[AmazonRedshiftSourceOutputTypeDef],
        "AmazonRedshiftTarget": NotRequired[AmazonRedshiftTargetOutputTypeDef],
        "EvaluateDataQualityMultiFrame": NotRequired[EvaluateDataQualityMultiFrameOutputTypeDef],
        "Recipe": NotRequired[RecipeOutputTypeDef],
        "SnowflakeSource": NotRequired[SnowflakeSourceOutputTypeDef],
        "SnowflakeTarget": NotRequired[SnowflakeTargetOutputTypeDef],
        "ConnectorDataSource": NotRequired[ConnectorDataSourceOutputTypeDef],
        "ConnectorDataTarget": NotRequired[ConnectorDataTargetOutputTypeDef],
    },
)
CodeGenConfigurationNodePaginatorTypeDef = TypedDict(
    "CodeGenConfigurationNodePaginatorTypeDef",
    {
        "AthenaConnectorSource": NotRequired[AthenaConnectorSourceOutputTypeDef],
        "JDBCConnectorSource": NotRequired[JDBCConnectorSourceOutputTypeDef],
        "SparkConnectorSource": NotRequired[SparkConnectorSourceOutputTypeDef],
        "CatalogSource": NotRequired[CatalogSourceTypeDef],
        "RedshiftSource": NotRequired[RedshiftSourceTypeDef],
        "S3CatalogSource": NotRequired[S3CatalogSourceTypeDef],
        "S3CsvSource": NotRequired[S3CsvSourceOutputTypeDef],
        "S3JsonSource": NotRequired[S3JsonSourceOutputTypeDef],
        "S3ParquetSource": NotRequired[S3ParquetSourceOutputTypeDef],
        "RelationalCatalogSource": NotRequired[RelationalCatalogSourceTypeDef],
        "DynamoDBCatalogSource": NotRequired[DynamoDBCatalogSourceTypeDef],
        "JDBCConnectorTarget": NotRequired[JDBCConnectorTargetOutputTypeDef],
        "SparkConnectorTarget": NotRequired[SparkConnectorTargetOutputTypeDef],
        "CatalogTarget": NotRequired[BasicCatalogTargetOutputTypeDef],
        "RedshiftTarget": NotRequired[RedshiftTargetOutputTypeDef],
        "S3CatalogTarget": NotRequired[S3CatalogTargetOutputTypeDef],
        "S3GlueParquetTarget": NotRequired[S3GlueParquetTargetOutputTypeDef],
        "S3DirectTarget": NotRequired[S3DirectTargetOutputTypeDef],
        "ApplyMapping": NotRequired[ApplyMappingPaginatorTypeDef],
        "SelectFields": NotRequired[SelectFieldsOutputTypeDef],
        "DropFields": NotRequired[DropFieldsOutputTypeDef],
        "RenameField": NotRequired[RenameFieldOutputTypeDef],
        "Spigot": NotRequired[SpigotOutputTypeDef],
        "Join": NotRequired[JoinOutputTypeDef],
        "SplitFields": NotRequired[SplitFieldsOutputTypeDef],
        "SelectFromCollection": NotRequired[SelectFromCollectionOutputTypeDef],
        "FillMissingValues": NotRequired[FillMissingValuesOutputTypeDef],
        "Filter": NotRequired[FilterOutputTypeDef],
        "CustomCode": NotRequired[CustomCodeOutputTypeDef],
        "SparkSQL": NotRequired[SparkSQLOutputTypeDef],
        "DirectKinesisSource": NotRequired[DirectKinesisSourceOutputTypeDef],
        "DirectKafkaSource": NotRequired[DirectKafkaSourceOutputTypeDef],
        "CatalogKinesisSource": NotRequired[CatalogKinesisSourceOutputTypeDef],
        "CatalogKafkaSource": NotRequired[CatalogKafkaSourceOutputTypeDef],
        "DropNullFields": NotRequired[DropNullFieldsOutputTypeDef],
        "Merge": NotRequired[MergeOutputTypeDef],
        "Union": NotRequired[UnionOutputTypeDef],
        "PIIDetection": NotRequired[PIIDetectionOutputTypeDef],
        "Aggregate": NotRequired[AggregateOutputTypeDef],
        "DropDuplicates": NotRequired[DropDuplicatesOutputTypeDef],
        "GovernedCatalogTarget": NotRequired[GovernedCatalogTargetOutputTypeDef],
        "GovernedCatalogSource": NotRequired[GovernedCatalogSourceTypeDef],
        "MicrosoftSQLServerCatalogSource": NotRequired[MicrosoftSQLServerCatalogSourceTypeDef],
        "MySQLCatalogSource": NotRequired[MySQLCatalogSourceTypeDef],
        "OracleSQLCatalogSource": NotRequired[OracleSQLCatalogSourceTypeDef],
        "PostgreSQLCatalogSource": NotRequired[PostgreSQLCatalogSourceTypeDef],
        "MicrosoftSQLServerCatalogTarget": NotRequired[
            MicrosoftSQLServerCatalogTargetOutputTypeDef
        ],
        "MySQLCatalogTarget": NotRequired[MySQLCatalogTargetOutputTypeDef],
        "OracleSQLCatalogTarget": NotRequired[OracleSQLCatalogTargetOutputTypeDef],
        "PostgreSQLCatalogTarget": NotRequired[PostgreSQLCatalogTargetOutputTypeDef],
        "DynamicTransform": NotRequired[DynamicTransformOutputTypeDef],
        "EvaluateDataQuality": NotRequired[EvaluateDataQualityOutputTypeDef],
        "S3CatalogHudiSource": NotRequired[S3CatalogHudiSourceOutputTypeDef],
        "CatalogHudiSource": NotRequired[CatalogHudiSourceOutputTypeDef],
        "S3HudiSource": NotRequired[S3HudiSourceOutputTypeDef],
        "S3HudiCatalogTarget": NotRequired[S3HudiCatalogTargetOutputTypeDef],
        "S3HudiDirectTarget": NotRequired[S3HudiDirectTargetOutputTypeDef],
        "DirectJDBCSource": NotRequired[DirectJDBCSourceTypeDef],
        "S3CatalogDeltaSource": NotRequired[S3CatalogDeltaSourceOutputTypeDef],
        "CatalogDeltaSource": NotRequired[CatalogDeltaSourceOutputTypeDef],
        "S3DeltaSource": NotRequired[S3DeltaSourceOutputTypeDef],
        "S3DeltaCatalogTarget": NotRequired[S3DeltaCatalogTargetOutputTypeDef],
        "S3DeltaDirectTarget": NotRequired[S3DeltaDirectTargetOutputTypeDef],
        "AmazonRedshiftSource": NotRequired[AmazonRedshiftSourceOutputTypeDef],
        "AmazonRedshiftTarget": NotRequired[AmazonRedshiftTargetOutputTypeDef],
        "EvaluateDataQualityMultiFrame": NotRequired[EvaluateDataQualityMultiFrameOutputTypeDef],
        "Recipe": NotRequired[RecipeOutputTypeDef],
        "SnowflakeSource": NotRequired[SnowflakeSourceOutputTypeDef],
        "SnowflakeTarget": NotRequired[SnowflakeTargetOutputTypeDef],
        "ConnectorDataSource": NotRequired[ConnectorDataSourceOutputTypeDef],
        "ConnectorDataTarget": NotRequired[ConnectorDataTargetOutputTypeDef],
    },
)
RecipeStepUnionTypeDef = Union[RecipeStepTypeDef, RecipeStepOutputTypeDef]
StorageDescriptorUnionTypeDef = Union[StorageDescriptorTypeDef, StorageDescriptorOutputTypeDef]

class GetStatementResponseTypeDef(TypedDict):
    Statement: StatementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStatementsResponseTypeDef(TypedDict):
    Statements: List[StatementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

DynamicTransformUnionTypeDef = Union[DynamicTransformTypeDef, DynamicTransformOutputTypeDef]
RedshiftTargetUnionTypeDef = Union[RedshiftTargetTypeDef, RedshiftTargetOutputTypeDef]
AmazonRedshiftSourceUnionTypeDef = Union[
    AmazonRedshiftSourceTypeDef, AmazonRedshiftSourceOutputTypeDef
]
AmazonRedshiftTargetUnionTypeDef = Union[
    AmazonRedshiftTargetTypeDef, AmazonRedshiftTargetOutputTypeDef
]
SnowflakeTargetUnionTypeDef = Union[SnowflakeTargetTypeDef, SnowflakeTargetOutputTypeDef]

class TablePaginatorTypeDef(TypedDict):
    Name: str
    DatabaseName: NotRequired[str]
    Description: NotRequired[str]
    Owner: NotRequired[str]
    CreateTime: NotRequired[datetime]
    UpdateTime: NotRequired[datetime]
    LastAccessTime: NotRequired[datetime]
    LastAnalyzedTime: NotRequired[datetime]
    Retention: NotRequired[int]
    StorageDescriptor: NotRequired[StorageDescriptorOutputTypeDef]
    PartitionKeys: NotRequired[List[ColumnOutputTypeDef]]
    ViewOriginalText: NotRequired[str]
    ViewExpandedText: NotRequired[str]
    TableType: NotRequired[str]
    Parameters: NotRequired[Dict[str, str]]
    CreatedBy: NotRequired[str]
    IsRegisteredWithLakeFormation: NotRequired[bool]
    TargetTable: NotRequired[TableIdentifierTypeDef]
    CatalogId: NotRequired[str]
    VersionId: NotRequired[str]
    FederatedTable: NotRequired[FederatedTableTypeDef]
    ViewDefinition: NotRequired[ViewDefinitionTypeDef]
    IsMultiDialectView: NotRequired[bool]
    Status: NotRequired[TableStatusPaginatorTypeDef]

class TableTypeDef(TypedDict):
    Name: str
    DatabaseName: NotRequired[str]
    Description: NotRequired[str]
    Owner: NotRequired[str]
    CreateTime: NotRequired[datetime]
    UpdateTime: NotRequired[datetime]
    LastAccessTime: NotRequired[datetime]
    LastAnalyzedTime: NotRequired[datetime]
    Retention: NotRequired[int]
    StorageDescriptor: NotRequired[StorageDescriptorOutputTypeDef]
    PartitionKeys: NotRequired[List[ColumnOutputTypeDef]]
    ViewOriginalText: NotRequired[str]
    ViewExpandedText: NotRequired[str]
    TableType: NotRequired[str]
    Parameters: NotRequired[Dict[str, str]]
    CreatedBy: NotRequired[str]
    IsRegisteredWithLakeFormation: NotRequired[bool]
    TargetTable: NotRequired[TableIdentifierTypeDef]
    CatalogId: NotRequired[str]
    VersionId: NotRequired[str]
    FederatedTable: NotRequired[FederatedTableTypeDef]
    ViewDefinition: NotRequired[ViewDefinitionTypeDef]
    IsMultiDialectView: NotRequired[bool]
    Status: NotRequired[TableStatusTypeDef]

DecimalColumnStatisticsDataUnionTypeDef = Union[
    DecimalColumnStatisticsDataTypeDef, DecimalColumnStatisticsDataOutputTypeDef
]
CatalogKafkaSourceUnionTypeDef = Union[CatalogKafkaSourceTypeDef, CatalogKafkaSourceOutputTypeDef]
DirectKafkaSourceUnionTypeDef = Union[DirectKafkaSourceTypeDef, DirectKafkaSourceOutputTypeDef]
CatalogKinesisSourceUnionTypeDef = Union[
    CatalogKinesisSourceTypeDef, CatalogKinesisSourceOutputTypeDef
]
DirectKinesisSourceUnionTypeDef = Union[
    DirectKinesisSourceTypeDef, DirectKinesisSourceOutputTypeDef
]
NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "Type": NotRequired[NodeTypeType],
        "Name": NotRequired[str],
        "UniqueId": NotRequired[str],
        "TriggerDetails": NotRequired[TriggerNodeDetailsTypeDef],
        "JobDetails": NotRequired[JobNodeDetailsTypeDef],
        "CrawlerDetails": NotRequired[CrawlerNodeDetailsTypeDef],
    },
)

class UpdateTriggerRequestTypeDef(TypedDict):
    Name: str
    TriggerUpdate: TriggerUpdateTypeDef

class GetMLTransformsResponseTypeDef(TypedDict):
    Transforms: List[MLTransformTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateCatalogRequestTypeDef(TypedDict):
    Name: str
    CatalogInput: CatalogInputTypeDef
    Tags: NotRequired[Mapping[str, str]]

class UpdateCatalogRequestTypeDef(TypedDict):
    CatalogId: str
    CatalogInput: CatalogInputTypeDef

class CreateDatabaseRequestTypeDef(TypedDict):
    DatabaseInput: DatabaseInputTypeDef
    CatalogId: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class UpdateDatabaseRequestTypeDef(TypedDict):
    Name: str
    DatabaseInput: DatabaseInputTypeDef
    CatalogId: NotRequired[str]

class BatchGetDataQualityResultResponseTypeDef(TypedDict):
    Results: List[DataQualityResultTypeDef]
    ResultsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ColumnStatisticsErrorTypeDef(TypedDict):
    ColumnStatistics: NotRequired[ColumnStatisticsOutputTypeDef]
    Error: NotRequired[ErrorDetailTypeDef]

class GetColumnStatisticsForPartitionResponseTypeDef(TypedDict):
    ColumnStatisticsList: List[ColumnStatisticsOutputTypeDef]
    Errors: List[ColumnErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetColumnStatisticsForTableResponseTypeDef(TypedDict):
    ColumnStatisticsList: List[ColumnStatisticsOutputTypeDef]
    Errors: List[ColumnErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetPartitionResponseTypeDef(TypedDict):
    Partitions: List[PartitionTypeDef]
    UnprocessedKeys: List[PartitionValueListOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPartitionResponseTypeDef(TypedDict):
    Partition: PartitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPartitionsResponseTypeDef(TypedDict):
    Partitions: List[PartitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetUnfilteredPartitionMetadataResponseTypeDef(TypedDict):
    Partition: PartitionTypeDef
    AuthorizedColumns: List[str]
    IsRegisteredWithLakeFormation: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UnfilteredPartitionTypeDef(TypedDict):
    Partition: NotRequired[PartitionTypeDef]
    AuthorizedColumns: NotRequired[List[str]]
    IsRegisteredWithLakeFormation: NotRequired[bool]

class FilterTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    LogicalOperator: FilterLogicalOperatorType
    Filters: Sequence[FilterExpressionUnionTypeDef]

ConnectorDataSourceUnionTypeDef = Union[
    ConnectorDataSourceTypeDef, ConnectorDataSourceOutputTypeDef
]
SnowflakeSourceUnionTypeDef = Union[SnowflakeSourceTypeDef, SnowflakeSourceOutputTypeDef]

class DataQualityResultFilterCriteriaTypeDef(TypedDict):
    DataSource: NotRequired[DataSourceUnionTypeDef]
    JobName: NotRequired[str]
    JobRunId: NotRequired[str]
    StartedAfter: NotRequired[TimestampTypeDef]
    StartedBefore: NotRequired[TimestampTypeDef]

class DataQualityRuleRecommendationRunFilterTypeDef(TypedDict):
    DataSource: DataSourceUnionTypeDef
    StartedBefore: NotRequired[TimestampTypeDef]
    StartedAfter: NotRequired[TimestampTypeDef]

class DataQualityRulesetEvaluationRunFilterTypeDef(TypedDict):
    DataSource: DataSourceUnionTypeDef
    StartedBefore: NotRequired[TimestampTypeDef]
    StartedAfter: NotRequired[TimestampTypeDef]

class StartDataQualityRuleRecommendationRunRequestTypeDef(TypedDict):
    DataSource: DataSourceUnionTypeDef
    Role: str
    NumberOfWorkers: NotRequired[int]
    Timeout: NotRequired[int]
    CreatedRulesetName: NotRequired[str]
    DataQualitySecurityConfiguration: NotRequired[str]
    ClientToken: NotRequired[str]

class StartDataQualityRulesetEvaluationRunRequestTypeDef(TypedDict):
    DataSource: DataSourceUnionTypeDef
    Role: str
    RulesetNames: Sequence[str]
    NumberOfWorkers: NotRequired[int]
    Timeout: NotRequired[int]
    ClientToken: NotRequired[str]
    AdditionalRunOptions: NotRequired[DataQualityEvaluationRunAdditionalRunOptionsTypeDef]
    AdditionalDataSources: NotRequired[Mapping[str, DataSourceUnionTypeDef]]

class BatchTableOptimizerTypeDef(TypedDict):
    catalogId: NotRequired[str]
    databaseName: NotRequired[str]
    tableName: NotRequired[str]
    tableOptimizer: NotRequired[TableOptimizerTypeDef]

class GetTableOptimizerResponseTypeDef(TypedDict):
    CatalogId: str
    DatabaseName: str
    TableName: str
    TableOptimizer: TableOptimizerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionResponseTypeDef(TypedDict):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionsResponseTypeDef(TypedDict):
    ConnectionList: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateConnectionRequestTypeDef(TypedDict):
    ConnectionInput: ConnectionInputTypeDef
    CatalogId: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class UpdateConnectionRequestTypeDef(TypedDict):
    Name: str
    ConnectionInput: ConnectionInputTypeDef
    CatalogId: NotRequired[str]

class TestConnectionRequestTypeDef(TypedDict):
    ConnectionName: NotRequired[str]
    CatalogId: NotRequired[str]
    TestConnectionInput: NotRequired[TestConnectionInputTypeDef]

class JobTypeDef(TypedDict):
    Name: NotRequired[str]
    JobMode: NotRequired[JobModeType]
    JobRunQueuingEnabled: NotRequired[bool]
    Description: NotRequired[str]
    LogUri: NotRequired[str]
    Role: NotRequired[str]
    CreatedOn: NotRequired[datetime]
    LastModifiedOn: NotRequired[datetime]
    ExecutionProperty: NotRequired[ExecutionPropertyTypeDef]
    Command: NotRequired[JobCommandTypeDef]
    DefaultArguments: NotRequired[Dict[str, str]]
    NonOverridableArguments: NotRequired[Dict[str, str]]
    Connections: NotRequired[ConnectionsListOutputTypeDef]
    MaxRetries: NotRequired[int]
    AllocatedCapacity: NotRequired[int]
    Timeout: NotRequired[int]
    MaxCapacity: NotRequired[float]
    WorkerType: NotRequired[WorkerTypeType]
    NumberOfWorkers: NotRequired[int]
    SecurityConfiguration: NotRequired[str]
    NotificationProperty: NotRequired[NotificationPropertyTypeDef]
    GlueVersion: NotRequired[str]
    CodeGenConfigurationNodes: NotRequired[Dict[str, CodeGenConfigurationNodeOutputTypeDef]]
    ExecutionClass: NotRequired[ExecutionClassType]
    SourceControlDetails: NotRequired[SourceControlDetailsTypeDef]
    MaintenanceWindow: NotRequired[str]
    ProfileName: NotRequired[str]

class JobPaginatorTypeDef(TypedDict):
    Name: NotRequired[str]
    JobMode: NotRequired[JobModeType]
    JobRunQueuingEnabled: NotRequired[bool]
    Description: NotRequired[str]
    LogUri: NotRequired[str]
    Role: NotRequired[str]
    CreatedOn: NotRequired[datetime]
    LastModifiedOn: NotRequired[datetime]
    ExecutionProperty: NotRequired[ExecutionPropertyTypeDef]
    Command: NotRequired[JobCommandTypeDef]
    DefaultArguments: NotRequired[Dict[str, str]]
    NonOverridableArguments: NotRequired[Dict[str, str]]
    Connections: NotRequired[ConnectionsListOutputTypeDef]
    MaxRetries: NotRequired[int]
    AllocatedCapacity: NotRequired[int]
    Timeout: NotRequired[int]
    MaxCapacity: NotRequired[float]
    WorkerType: NotRequired[WorkerTypeType]
    NumberOfWorkers: NotRequired[int]
    SecurityConfiguration: NotRequired[str]
    NotificationProperty: NotRequired[NotificationPropertyTypeDef]
    GlueVersion: NotRequired[str]
    CodeGenConfigurationNodes: NotRequired[Dict[str, CodeGenConfigurationNodePaginatorTypeDef]]
    ExecutionClass: NotRequired[ExecutionClassType]
    SourceControlDetails: NotRequired[SourceControlDetailsTypeDef]
    MaintenanceWindow: NotRequired[str]
    ProfileName: NotRequired[str]

class RecipeTypeDef(TypedDict):
    Name: str
    Inputs: Sequence[str]
    RecipeReference: NotRequired[RecipeReferenceTypeDef]
    RecipeSteps: NotRequired[Sequence[RecipeStepUnionTypeDef]]

class PartitionInputTypeDef(TypedDict):
    Values: NotRequired[Sequence[str]]
    LastAccessTime: NotRequired[TimestampTypeDef]
    StorageDescriptor: NotRequired[StorageDescriptorUnionTypeDef]
    Parameters: NotRequired[Mapping[str, str]]
    LastAnalyzedTime: NotRequired[TimestampTypeDef]

class TableInputTypeDef(TypedDict):
    Name: str
    Description: NotRequired[str]
    Owner: NotRequired[str]
    LastAccessTime: NotRequired[TimestampTypeDef]
    LastAnalyzedTime: NotRequired[TimestampTypeDef]
    Retention: NotRequired[int]
    StorageDescriptor: NotRequired[StorageDescriptorUnionTypeDef]
    PartitionKeys: NotRequired[Sequence[ColumnUnionTypeDef]]
    ViewOriginalText: NotRequired[str]
    ViewExpandedText: NotRequired[str]
    TableType: NotRequired[str]
    Parameters: NotRequired[Mapping[str, str]]
    TargetTable: NotRequired[TableIdentifierTypeDef]
    ViewDefinition: NotRequired[ViewDefinitionInputTypeDef]

class GetTablesResponsePaginatorTypeDef(TypedDict):
    TableList: List[TablePaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TableVersionPaginatorTypeDef(TypedDict):
    Table: NotRequired[TablePaginatorTypeDef]
    VersionId: NotRequired[str]

class GetTableResponseTypeDef(TypedDict):
    Table: TableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTablesResponseTypeDef(TypedDict):
    TableList: List[TableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetUnfilteredTableMetadataResponseTypeDef(TypedDict):
    Table: TableTypeDef
    AuthorizedColumns: List[str]
    IsRegisteredWithLakeFormation: bool
    CellFilters: List[ColumnRowFilterTypeDef]
    QueryAuthorizationId: str
    IsMultiDialectView: bool
    ResourceArn: str
    IsProtected: bool
    Permissions: List[PermissionType]
    RowFilter: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchTablesResponseTypeDef(TypedDict):
    TableList: List[TableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TableVersionTypeDef(TypedDict):
    Table: NotRequired[TableTypeDef]
    VersionId: NotRequired[str]

ColumnStatisticsDataTypeDef = TypedDict(
    "ColumnStatisticsDataTypeDef",
    {
        "Type": ColumnStatisticsTypeType,
        "BooleanColumnStatisticsData": NotRequired[BooleanColumnStatisticsDataTypeDef],
        "DateColumnStatisticsData": NotRequired[DateColumnStatisticsDataUnionTypeDef],
        "DecimalColumnStatisticsData": NotRequired[DecimalColumnStatisticsDataUnionTypeDef],
        "DoubleColumnStatisticsData": NotRequired[DoubleColumnStatisticsDataTypeDef],
        "LongColumnStatisticsData": NotRequired[LongColumnStatisticsDataTypeDef],
        "StringColumnStatisticsData": NotRequired[StringColumnStatisticsDataTypeDef],
        "BinaryColumnStatisticsData": NotRequired[BinaryColumnStatisticsDataTypeDef],
    },
)

class WorkflowGraphTypeDef(TypedDict):
    Nodes: NotRequired[List[NodeTypeDef]]
    Edges: NotRequired[List[EdgeTypeDef]]

class UpdateColumnStatisticsForPartitionResponseTypeDef(TypedDict):
    Errors: List[ColumnStatisticsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateColumnStatisticsForTableResponseTypeDef(TypedDict):
    Errors: List[ColumnStatisticsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetUnfilteredPartitionsMetadataResponseTypeDef(TypedDict):
    UnfilteredPartitions: List[UnfilteredPartitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

FilterUnionTypeDef = Union[FilterTypeDef, FilterOutputTypeDef]

class ListDataQualityResultsRequestTypeDef(TypedDict):
    Filter: NotRequired[DataQualityResultFilterCriteriaTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDataQualityRuleRecommendationRunsRequestTypeDef(TypedDict):
    Filter: NotRequired[DataQualityRuleRecommendationRunFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDataQualityRulesetEvaluationRunsRequestTypeDef(TypedDict):
    Filter: NotRequired[DataQualityRulesetEvaluationRunFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class BatchGetTableOptimizerResponseTypeDef(TypedDict):
    TableOptimizers: List[BatchTableOptimizerTypeDef]
    Failures: List[BatchGetTableOptimizerErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetJobsResponseTypeDef(TypedDict):
    Jobs: List[JobTypeDef]
    JobsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobResponseTypeDef(TypedDict):
    Job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobsResponseTypeDef(TypedDict):
    Jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetJobsResponsePaginatorTypeDef(TypedDict):
    Jobs: List[JobPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

RecipeUnionTypeDef = Union[RecipeTypeDef, RecipeOutputTypeDef]

class BatchCreatePartitionRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    PartitionInputList: Sequence[PartitionInputTypeDef]
    CatalogId: NotRequired[str]

class BatchUpdatePartitionRequestEntryTypeDef(TypedDict):
    PartitionValueList: Sequence[str]
    PartitionInput: PartitionInputTypeDef

class CreatePartitionRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    PartitionInput: PartitionInputTypeDef
    CatalogId: NotRequired[str]

class UpdatePartitionRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    PartitionValueList: Sequence[str]
    PartitionInput: PartitionInputTypeDef
    CatalogId: NotRequired[str]

class CreateTableRequestTypeDef(TypedDict):
    DatabaseName: str
    TableInput: TableInputTypeDef
    CatalogId: NotRequired[str]
    PartitionIndexes: NotRequired[Sequence[PartitionIndexTypeDef]]
    TransactionId: NotRequired[str]
    OpenTableFormatInput: NotRequired[OpenTableFormatInputTypeDef]

class UpdateTableRequestTypeDef(TypedDict):
    DatabaseName: str
    TableInput: TableInputTypeDef
    CatalogId: NotRequired[str]
    SkipArchive: NotRequired[bool]
    TransactionId: NotRequired[str]
    VersionId: NotRequired[str]
    ViewUpdateAction: NotRequired[ViewUpdateActionType]
    Force: NotRequired[bool]

class GetTableVersionsResponsePaginatorTypeDef(TypedDict):
    TableVersions: List[TableVersionPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetTableVersionResponseTypeDef(TypedDict):
    TableVersion: TableVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTableVersionsResponseTypeDef(TypedDict):
    TableVersions: List[TableVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

ColumnStatisticsDataUnionTypeDef = Union[
    ColumnStatisticsDataTypeDef, ColumnStatisticsDataOutputTypeDef
]

class WorkflowRunTypeDef(TypedDict):
    Name: NotRequired[str]
    WorkflowRunId: NotRequired[str]
    PreviousRunId: NotRequired[str]
    WorkflowRunProperties: NotRequired[Dict[str, str]]
    StartedOn: NotRequired[datetime]
    CompletedOn: NotRequired[datetime]
    Status: NotRequired[WorkflowRunStatusType]
    ErrorMessage: NotRequired[str]
    Statistics: NotRequired[WorkflowRunStatisticsTypeDef]
    Graph: NotRequired[WorkflowGraphTypeDef]
    StartingEventBatchCondition: NotRequired[StartingEventBatchConditionTypeDef]

CodeGenConfigurationNodeTypeDef = TypedDict(
    "CodeGenConfigurationNodeTypeDef",
    {
        "AthenaConnectorSource": NotRequired[AthenaConnectorSourceUnionTypeDef],
        "JDBCConnectorSource": NotRequired[JDBCConnectorSourceUnionTypeDef],
        "SparkConnectorSource": NotRequired[SparkConnectorSourceUnionTypeDef],
        "CatalogSource": NotRequired[CatalogSourceTypeDef],
        "RedshiftSource": NotRequired[RedshiftSourceTypeDef],
        "S3CatalogSource": NotRequired[S3CatalogSourceTypeDef],
        "S3CsvSource": NotRequired[S3CsvSourceUnionTypeDef],
        "S3JsonSource": NotRequired[S3JsonSourceUnionTypeDef],
        "S3ParquetSource": NotRequired[S3ParquetSourceUnionTypeDef],
        "RelationalCatalogSource": NotRequired[RelationalCatalogSourceTypeDef],
        "DynamoDBCatalogSource": NotRequired[DynamoDBCatalogSourceTypeDef],
        "JDBCConnectorTarget": NotRequired[JDBCConnectorTargetUnionTypeDef],
        "SparkConnectorTarget": NotRequired[SparkConnectorTargetUnionTypeDef],
        "CatalogTarget": NotRequired[BasicCatalogTargetUnionTypeDef],
        "RedshiftTarget": NotRequired[RedshiftTargetUnionTypeDef],
        "S3CatalogTarget": NotRequired[S3CatalogTargetUnionTypeDef],
        "S3GlueParquetTarget": NotRequired[S3GlueParquetTargetUnionTypeDef],
        "S3DirectTarget": NotRequired[S3DirectTargetUnionTypeDef],
        "ApplyMapping": NotRequired[ApplyMappingUnionTypeDef],
        "SelectFields": NotRequired[SelectFieldsUnionTypeDef],
        "DropFields": NotRequired[DropFieldsUnionTypeDef],
        "RenameField": NotRequired[RenameFieldUnionTypeDef],
        "Spigot": NotRequired[SpigotUnionTypeDef],
        "Join": NotRequired[JoinUnionTypeDef],
        "SplitFields": NotRequired[SplitFieldsUnionTypeDef],
        "SelectFromCollection": NotRequired[SelectFromCollectionUnionTypeDef],
        "FillMissingValues": NotRequired[FillMissingValuesUnionTypeDef],
        "Filter": NotRequired[FilterUnionTypeDef],
        "CustomCode": NotRequired[CustomCodeUnionTypeDef],
        "SparkSQL": NotRequired[SparkSQLUnionTypeDef],
        "DirectKinesisSource": NotRequired[DirectKinesisSourceUnionTypeDef],
        "DirectKafkaSource": NotRequired[DirectKafkaSourceUnionTypeDef],
        "CatalogKinesisSource": NotRequired[CatalogKinesisSourceUnionTypeDef],
        "CatalogKafkaSource": NotRequired[CatalogKafkaSourceUnionTypeDef],
        "DropNullFields": NotRequired[DropNullFieldsUnionTypeDef],
        "Merge": NotRequired[MergeUnionTypeDef],
        "Union": NotRequired[UnionUnionTypeDef],
        "PIIDetection": NotRequired[PIIDetectionUnionTypeDef],
        "Aggregate": NotRequired[AggregateUnionTypeDef],
        "DropDuplicates": NotRequired[DropDuplicatesUnionTypeDef],
        "GovernedCatalogTarget": NotRequired[GovernedCatalogTargetUnionTypeDef],
        "GovernedCatalogSource": NotRequired[GovernedCatalogSourceTypeDef],
        "MicrosoftSQLServerCatalogSource": NotRequired[MicrosoftSQLServerCatalogSourceTypeDef],
        "MySQLCatalogSource": NotRequired[MySQLCatalogSourceTypeDef],
        "OracleSQLCatalogSource": NotRequired[OracleSQLCatalogSourceTypeDef],
        "PostgreSQLCatalogSource": NotRequired[PostgreSQLCatalogSourceTypeDef],
        "MicrosoftSQLServerCatalogTarget": NotRequired[MicrosoftSQLServerCatalogTargetUnionTypeDef],
        "MySQLCatalogTarget": NotRequired[MySQLCatalogTargetUnionTypeDef],
        "OracleSQLCatalogTarget": NotRequired[OracleSQLCatalogTargetUnionTypeDef],
        "PostgreSQLCatalogTarget": NotRequired[PostgreSQLCatalogTargetUnionTypeDef],
        "DynamicTransform": NotRequired[DynamicTransformUnionTypeDef],
        "EvaluateDataQuality": NotRequired[EvaluateDataQualityUnionTypeDef],
        "S3CatalogHudiSource": NotRequired[S3CatalogHudiSourceUnionTypeDef],
        "CatalogHudiSource": NotRequired[CatalogHudiSourceUnionTypeDef],
        "S3HudiSource": NotRequired[S3HudiSourceUnionTypeDef],
        "S3HudiCatalogTarget": NotRequired[S3HudiCatalogTargetUnionTypeDef],
        "S3HudiDirectTarget": NotRequired[S3HudiDirectTargetUnionTypeDef],
        "DirectJDBCSource": NotRequired[DirectJDBCSourceTypeDef],
        "S3CatalogDeltaSource": NotRequired[S3CatalogDeltaSourceUnionTypeDef],
        "CatalogDeltaSource": NotRequired[CatalogDeltaSourceUnionTypeDef],
        "S3DeltaSource": NotRequired[S3DeltaSourceUnionTypeDef],
        "S3DeltaCatalogTarget": NotRequired[S3DeltaCatalogTargetUnionTypeDef],
        "S3DeltaDirectTarget": NotRequired[S3DeltaDirectTargetUnionTypeDef],
        "AmazonRedshiftSource": NotRequired[AmazonRedshiftSourceUnionTypeDef],
        "AmazonRedshiftTarget": NotRequired[AmazonRedshiftTargetUnionTypeDef],
        "EvaluateDataQualityMultiFrame": NotRequired[EvaluateDataQualityMultiFrameUnionTypeDef],
        "Recipe": NotRequired[RecipeUnionTypeDef],
        "SnowflakeSource": NotRequired[SnowflakeSourceUnionTypeDef],
        "SnowflakeTarget": NotRequired[SnowflakeTargetUnionTypeDef],
        "ConnectorDataSource": NotRequired[ConnectorDataSourceUnionTypeDef],
        "ConnectorDataTarget": NotRequired[ConnectorDataTargetUnionTypeDef],
    },
)

class BatchUpdatePartitionRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    Entries: Sequence[BatchUpdatePartitionRequestEntryTypeDef]
    CatalogId: NotRequired[str]

class ColumnStatisticsTypeDef(TypedDict):
    ColumnName: str
    ColumnType: str
    AnalyzedTime: TimestampTypeDef
    StatisticsData: ColumnStatisticsDataUnionTypeDef

class GetWorkflowRunResponseTypeDef(TypedDict):
    Run: WorkflowRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowRunsResponseTypeDef(TypedDict):
    Runs: List[WorkflowRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class WorkflowTypeDef(TypedDict):
    Name: NotRequired[str]
    Description: NotRequired[str]
    DefaultRunProperties: NotRequired[Dict[str, str]]
    CreatedOn: NotRequired[datetime]
    LastModifiedOn: NotRequired[datetime]
    LastRun: NotRequired[WorkflowRunTypeDef]
    Graph: NotRequired[WorkflowGraphTypeDef]
    MaxConcurrentRuns: NotRequired[int]
    BlueprintDetails: NotRequired[BlueprintDetailsTypeDef]

CodeGenConfigurationNodeUnionTypeDef = Union[
    CodeGenConfigurationNodeTypeDef, CodeGenConfigurationNodeOutputTypeDef
]
ColumnStatisticsUnionTypeDef = Union[ColumnStatisticsTypeDef, ColumnStatisticsOutputTypeDef]

class BatchGetWorkflowsResponseTypeDef(TypedDict):
    Workflows: List[WorkflowTypeDef]
    MissingWorkflows: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowResponseTypeDef(TypedDict):
    Workflow: WorkflowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobRequestTypeDef(TypedDict):
    Name: str
    Role: str
    Command: JobCommandTypeDef
    JobMode: NotRequired[JobModeType]
    JobRunQueuingEnabled: NotRequired[bool]
    Description: NotRequired[str]
    LogUri: NotRequired[str]
    ExecutionProperty: NotRequired[ExecutionPropertyTypeDef]
    DefaultArguments: NotRequired[Mapping[str, str]]
    NonOverridableArguments: NotRequired[Mapping[str, str]]
    Connections: NotRequired[ConnectionsListUnionTypeDef]
    MaxRetries: NotRequired[int]
    AllocatedCapacity: NotRequired[int]
    Timeout: NotRequired[int]
    MaxCapacity: NotRequired[float]
    SecurityConfiguration: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    NotificationProperty: NotRequired[NotificationPropertyTypeDef]
    GlueVersion: NotRequired[str]
    NumberOfWorkers: NotRequired[int]
    WorkerType: NotRequired[WorkerTypeType]
    CodeGenConfigurationNodes: NotRequired[Mapping[str, CodeGenConfigurationNodeUnionTypeDef]]
    ExecutionClass: NotRequired[ExecutionClassType]
    SourceControlDetails: NotRequired[SourceControlDetailsTypeDef]
    MaintenanceWindow: NotRequired[str]

class JobUpdateTypeDef(TypedDict):
    JobMode: NotRequired[JobModeType]
    JobRunQueuingEnabled: NotRequired[bool]
    Description: NotRequired[str]
    LogUri: NotRequired[str]
    Role: NotRequired[str]
    ExecutionProperty: NotRequired[ExecutionPropertyTypeDef]
    Command: NotRequired[JobCommandTypeDef]
    DefaultArguments: NotRequired[Mapping[str, str]]
    NonOverridableArguments: NotRequired[Mapping[str, str]]
    Connections: NotRequired[ConnectionsListUnionTypeDef]
    MaxRetries: NotRequired[int]
    AllocatedCapacity: NotRequired[int]
    Timeout: NotRequired[int]
    MaxCapacity: NotRequired[float]
    WorkerType: NotRequired[WorkerTypeType]
    NumberOfWorkers: NotRequired[int]
    SecurityConfiguration: NotRequired[str]
    NotificationProperty: NotRequired[NotificationPropertyTypeDef]
    GlueVersion: NotRequired[str]
    CodeGenConfigurationNodes: NotRequired[Mapping[str, CodeGenConfigurationNodeUnionTypeDef]]
    ExecutionClass: NotRequired[ExecutionClassType]
    SourceControlDetails: NotRequired[SourceControlDetailsTypeDef]
    MaintenanceWindow: NotRequired[str]

class UpdateColumnStatisticsForPartitionRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    ColumnStatisticsList: Sequence[ColumnStatisticsUnionTypeDef]
    CatalogId: NotRequired[str]

class UpdateColumnStatisticsForTableRequestTypeDef(TypedDict):
    DatabaseName: str
    TableName: str
    ColumnStatisticsList: Sequence[ColumnStatisticsUnionTypeDef]
    CatalogId: NotRequired[str]

class UpdateJobRequestTypeDef(TypedDict):
    JobName: str
    JobUpdate: JobUpdateTypeDef
