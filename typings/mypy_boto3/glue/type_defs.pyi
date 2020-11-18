from mypy_boto3_glue.type_defs import (
    ActionTypeDef,
    BatchStopJobRunErrorTypeDef,
    BatchStopJobRunSuccessfulSubmissionTypeDef,
    BatchUpdatePartitionFailureEntryTypeDef,
    BinaryColumnStatisticsDataTypeDef,
    BooleanColumnStatisticsDataTypeDef,
    CatalogImportStatusTypeDef,
    CatalogTargetTypeDef,
    ClassifierTypeDef,
    CloudWatchEncryptionTypeDef,
    CodeGenEdgeTypeDef,
    CodeGenNodeArgTypeDef,
    CodeGenNodeTypeDef,
    ColumnErrorTypeDef,
    ColumnStatisticsDataTypeDef,
    ColumnStatisticsErrorTypeDef,
    ColumnStatisticsTypeDef,
    ColumnTypeDef,
    ConditionTypeDef,
    ConfusionMatrixTypeDef,
    ConnectionPasswordEncryptionTypeDef,
    ConnectionTypeDef,
    ConnectionsListTypeDef,
    CrawlTypeDef,
    CrawlerMetricsTypeDef,
    CrawlerNodeDetailsTypeDef,
    CrawlerTargetsTypeDef,
    CrawlerTypeDef,
    CsvClassifierTypeDef,
    DataCatalogEncryptionSettingsTypeDef,
    DataLakePrincipalTypeDef,
    DatabaseIdentifierTypeDef,
    DatabaseTypeDef,
    DateColumnStatisticsDataTypeDef,
    DecimalColumnStatisticsDataTypeDef,
    DecimalNumberTypeDef,
    DevEndpointTypeDef,
    DoubleColumnStatisticsDataTypeDef,
    DynamoDBTargetTypeDef,
    EdgeTypeDef,
    EncryptionAtRestTypeDef,
    EncryptionConfigurationTypeDef,
    ErrorDetailTypeDef,
    EvaluationMetricsTypeDef,
    ExecutionPropertyTypeDef,
    ExportLabelsTaskRunPropertiesTypeDef,
    FindMatchesMetricsTypeDef,
    FindMatchesParametersTypeDef,
    FindMatchesTaskRunPropertiesTypeDef,
    GluePolicyTypeDef,
    GlueTableTypeDef,
    GrokClassifierTypeDef,
    ImportLabelsTaskRunPropertiesTypeDef,
    JdbcTargetTypeDef,
    JobBookmarkEntryTypeDef,
    JobBookmarksEncryptionTypeDef,
    JobCommandTypeDef,
    JobNodeDetailsTypeDef,
    JobRunTypeDef,
    JobTypeDef,
    JsonClassifierTypeDef,
    KeySchemaElementTypeDef,
    LabelingSetGenerationTaskRunPropertiesTypeDef,
    LastCrawlInfoTypeDef,
    LongColumnStatisticsDataTypeDef,
    MLTransformTypeDef,
    MLUserDataEncryptionTypeDef,
    MappingEntryTypeDef,
    MongoDBTargetTypeDef,
    NodeTypeDef,
    NotificationPropertyTypeDef,
    OrderTypeDef,
    PartitionErrorTypeDef,
    PartitionIndexDescriptorTypeDef,
    PartitionInputTypeDef,
    PartitionTypeDef,
    PartitionValueListTypeDef,
    PhysicalConnectionRequirementsTypeDef,
    PredecessorTypeDef,
    PredicateTypeDef,
    PrincipalPermissionsTypeDef,
    RecrawlPolicyTypeDef,
    ResourceUriTypeDef,
    S3EncryptionTypeDef,
    S3TargetTypeDef,
    ScheduleTypeDef,
    SchemaChangePolicyTypeDef,
    SchemaColumnTypeDef,
    SecurityConfigurationTypeDef,
    SerDeInfoTypeDef,
    SkewedInfoTypeDef,
    StorageDescriptorTypeDef,
    StringColumnStatisticsDataTypeDef,
    TableErrorTypeDef,
    TableIdentifierTypeDef,
    TableTypeDef,
    TableVersionErrorTypeDef,
    TableVersionTypeDef,
    TaskRunPropertiesTypeDef,
    TaskRunTypeDef,
    TransformEncryptionTypeDef,
    TransformParametersTypeDef,
    TriggerNodeDetailsTypeDef,
    TriggerTypeDef,
    UserDefinedFunctionTypeDef,
    WorkflowGraphTypeDef,
    WorkflowRunStatisticsTypeDef,
    WorkflowRunTypeDef,
    WorkflowTypeDef,
    XMLClassifierTypeDef,
    BatchCreatePartitionResponseTypeDef,
    BatchDeleteConnectionResponseTypeDef,
    BatchDeletePartitionResponseTypeDef,
    BatchDeleteTableResponseTypeDef,
    BatchDeleteTableVersionResponseTypeDef,
    BatchGetCrawlersResponseTypeDef,
    BatchGetDevEndpointsResponseTypeDef,
    BatchGetJobsResponseTypeDef,
    BatchGetPartitionResponseTypeDef,
    BatchGetTriggersResponseTypeDef,
    BatchGetWorkflowsResponseTypeDef,
    BatchStopJobRunResponseTypeDef,
    BatchUpdatePartitionRequestEntryTypeDef,
    BatchUpdatePartitionResponseTypeDef,
    CancelMLTaskRunResponseTypeDef,
    CatalogEntryTypeDef,
    ConnectionInputTypeDef,
    CreateCsvClassifierRequestTypeDef,
    CreateDevEndpointResponseTypeDef,
    CreateGrokClassifierRequestTypeDef,
    CreateJobResponseTypeDef,
    CreateJsonClassifierRequestTypeDef,
    CreateMLTransformResponseTypeDef,
    CreateScriptResponseTypeDef,
    CreateSecurityConfigurationResponseTypeDef,
    CreateTriggerResponseTypeDef,
    CreateWorkflowResponseTypeDef,
    CreateXMLClassifierRequestTypeDef,
    DatabaseInputTypeDef,
    DeleteJobResponseTypeDef,
    DeleteMLTransformResponseTypeDef,
    DeleteTriggerResponseTypeDef,
    DeleteWorkflowResponseTypeDef,
    DevEndpointCustomLibrariesTypeDef,
    GetCatalogImportStatusResponseTypeDef,
    GetClassifierResponseTypeDef,
    GetClassifiersResponseTypeDef,
    GetColumnStatisticsForPartitionResponseTypeDef,
    GetColumnStatisticsForTableResponseTypeDef,
    GetConnectionResponseTypeDef,
    GetConnectionsFilterTypeDef,
    GetConnectionsResponseTypeDef,
    GetCrawlerMetricsResponseTypeDef,
    GetCrawlerResponseTypeDef,
    GetCrawlersResponseTypeDef,
    GetDataCatalogEncryptionSettingsResponseTypeDef,
    GetDatabaseResponseTypeDef,
    GetDatabasesResponseTypeDef,
    GetDataflowGraphResponseTypeDef,
    GetDevEndpointResponseTypeDef,
    GetDevEndpointsResponseTypeDef,
    GetJobBookmarkResponseTypeDef,
    GetJobResponseTypeDef,
    GetJobRunResponseTypeDef,
    GetJobRunsResponseTypeDef,
    GetJobsResponseTypeDef,
    GetMLTaskRunResponseTypeDef,
    GetMLTaskRunsResponseTypeDef,
    GetMLTransformResponseTypeDef,
    GetMLTransformsResponseTypeDef,
    GetMappingResponseTypeDef,
    GetPartitionIndexesResponseTypeDef,
    GetPartitionResponseTypeDef,
    GetPartitionsResponseTypeDef,
    GetPlanResponseTypeDef,
    GetResourcePoliciesResponseTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetSecurityConfigurationResponseTypeDef,
    GetSecurityConfigurationsResponseTypeDef,
    GetTableResponseTypeDef,
    GetTableVersionResponseTypeDef,
    GetTableVersionsResponseTypeDef,
    GetTablesResponseTypeDef,
    GetTagsResponseTypeDef,
    GetTriggerResponseTypeDef,
    GetTriggersResponseTypeDef,
    GetUserDefinedFunctionResponseTypeDef,
    GetUserDefinedFunctionsResponseTypeDef,
    GetWorkflowResponseTypeDef,
    GetWorkflowRunPropertiesResponseTypeDef,
    GetWorkflowRunResponseTypeDef,
    GetWorkflowRunsResponseTypeDef,
    JobUpdateTypeDef,
    ListCrawlersResponseTypeDef,
    ListDevEndpointsResponseTypeDef,
    ListJobsResponseTypeDef,
    ListMLTransformsResponseTypeDef,
    ListTriggersResponseTypeDef,
    ListWorkflowsResponseTypeDef,
    LocationTypeDef,
    PaginatorConfigTypeDef,
    PartitionIndexTypeDef,
    PropertyPredicateTypeDef,
    PutResourcePolicyResponseTypeDef,
    ResetJobBookmarkResponseTypeDef,
    ResumeWorkflowRunResponseTypeDef,
    SearchTablesResponseTypeDef,
    SegmentTypeDef,
    SortCriterionTypeDef,
    StartExportLabelsTaskRunResponseTypeDef,
    StartImportLabelsTaskRunResponseTypeDef,
    StartJobRunResponseTypeDef,
    StartMLEvaluationTaskRunResponseTypeDef,
    StartMLLabelingSetGenerationTaskRunResponseTypeDef,
    StartTriggerResponseTypeDef,
    StartWorkflowRunResponseTypeDef,
    StopTriggerResponseTypeDef,
    TableInputTypeDef,
    TaskRunFilterCriteriaTypeDef,
    TaskRunSortCriteriaTypeDef,
    TransformFilterCriteriaTypeDef,
    TransformSortCriteriaTypeDef,
    TriggerUpdateTypeDef,
    UpdateColumnStatisticsForPartitionResponseTypeDef,
    UpdateColumnStatisticsForTableResponseTypeDef,
    UpdateCsvClassifierRequestTypeDef,
    UpdateGrokClassifierRequestTypeDef,
    UpdateJobResponseTypeDef,
    UpdateJsonClassifierRequestTypeDef,
    UpdateMLTransformResponseTypeDef,
    UpdateTriggerResponseTypeDef,
    UpdateWorkflowResponseTypeDef,
    UpdateXMLClassifierRequestTypeDef,
    UserDefinedFunctionInputTypeDef,
)

__all__ = (
    "ActionTypeDef",
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
    "LongColumnStatisticsDataTypeDef",
    "MLTransformTypeDef",
    "MLUserDataEncryptionTypeDef",
    "MappingEntryTypeDef",
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
    "ResourceUriTypeDef",
    "S3EncryptionTypeDef",
    "S3TargetTypeDef",
    "ScheduleTypeDef",
    "SchemaChangePolicyTypeDef",
    "SchemaColumnTypeDef",
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
    "ConnectionInputTypeDef",
    "CreateCsvClassifierRequestTypeDef",
    "CreateDevEndpointResponseTypeDef",
    "CreateGrokClassifierRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreateJsonClassifierRequestTypeDef",
    "CreateMLTransformResponseTypeDef",
    "CreateScriptResponseTypeDef",
    "CreateSecurityConfigurationResponseTypeDef",
    "CreateTriggerResponseTypeDef",
    "CreateWorkflowResponseTypeDef",
    "CreateXMLClassifierRequestTypeDef",
    "DatabaseInputTypeDef",
    "DeleteJobResponseTypeDef",
    "DeleteMLTransformResponseTypeDef",
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
    "GetResourcePoliciesResponseTypeDef",
    "GetResourcePolicyResponseTypeDef",
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
    "ListTriggersResponseTypeDef",
    "ListWorkflowsResponseTypeDef",
    "LocationTypeDef",
    "PaginatorConfigTypeDef",
    "PartitionIndexTypeDef",
    "PropertyPredicateTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "ResetJobBookmarkResponseTypeDef",
    "ResumeWorkflowRunResponseTypeDef",
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
    "UpdateTriggerResponseTypeDef",
    "UpdateWorkflowResponseTypeDef",
    "UpdateXMLClassifierRequestTypeDef",
    "UserDefinedFunctionInputTypeDef",
)
