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
    BackfillErrorCodeType,
    CatalogEncryptionModeType,
    CloudWatchEncryptionModeType,
    ColumnStatisticsTypeType,
    ComparatorType,
    CompatibilityType,
    ConnectionPropertyKeyType,
    ConnectionTypeType,
    CrawlerLineageSettingsType,
    CrawlerStateType,
    CrawlStateType,
    CsvHeaderOptionType,
    DataFormatType,
    DeleteBehaviorType,
    EnableHybridValuesType,
    ExistConditionType,
    JobBookmarksEncryptionModeType,
    JobRunStateType,
    LanguageType,
    LastCrawlStatusType,
    LogicalType,
    MLUserDataEncryptionModeStringType,
    NodeTypeType,
    PartitionIndexStatusType,
    PermissionType,
    PrincipalTypeType,
    RecrawlBehaviorType,
    RegistryStatusType,
    ResourceShareTypeType,
    ResourceTypeType,
    S3EncryptionModeType,
    ScheduleStateType,
    SchemaStatusType,
    SchemaVersionStatusType,
    SortDirectionTypeType,
    SortType,
    TaskRunSortColumnTypeType,
    TaskStatusTypeType,
    TaskTypeType,
    TransformSortColumnTypeType,
    TransformStatusTypeType,
    TriggerStateType,
    TriggerTypeType,
    UpdateBehaviorType,
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
    "BackfillErrorTypeDef",
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
    "BatchGetCrawlersRequestRequestTypeDef",
    "BatchGetCrawlersResponseTypeDef",
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
    "BooleanColumnStatisticsDataTypeDef",
    "CancelMLTaskRunRequestRequestTypeDef",
    "CancelMLTaskRunResponseTypeDef",
    "CatalogEntryTypeDef",
    "CatalogImportStatusTypeDef",
    "CatalogTargetTypeDef",
    "CheckSchemaVersionValidityInputRequestTypeDef",
    "CheckSchemaVersionValidityResponseTypeDef",
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
    "ConnectionInputTypeDef",
    "ConnectionPasswordEncryptionTypeDef",
    "ConnectionTypeDef",
    "ConnectionsListTypeDef",
    "CrawlTypeDef",
    "CrawlerMetricsTypeDef",
    "CrawlerNodeDetailsTypeDef",
    "CrawlerTargetsTypeDef",
    "CrawlerTypeDef",
    "CreateClassifierRequestRequestTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "CreateCrawlerRequestRequestTypeDef",
    "CreateCsvClassifierRequestTypeDef",
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
    "CreateTableRequestRequestTypeDef",
    "CreateTriggerRequestRequestTypeDef",
    "CreateTriggerResponseTypeDef",
    "CreateUserDefinedFunctionRequestRequestTypeDef",
    "CreateWorkflowRequestRequestTypeDef",
    "CreateWorkflowResponseTypeDef",
    "CreateXMLClassifierRequestTypeDef",
    "CsvClassifierTypeDef",
    "DataCatalogEncryptionSettingsTypeDef",
    "DataLakePrincipalTypeDef",
    "DatabaseIdentifierTypeDef",
    "DatabaseInputTypeDef",
    "DatabaseTypeDef",
    "DateColumnStatisticsDataTypeDef",
    "DecimalColumnStatisticsDataTypeDef",
    "DecimalNumberTypeDef",
    "DeleteClassifierRequestRequestTypeDef",
    "DeleteColumnStatisticsForPartitionRequestRequestTypeDef",
    "DeleteColumnStatisticsForTableRequestRequestTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteCrawlerRequestRequestTypeDef",
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
    "DeleteTableRequestRequestTypeDef",
    "DeleteTableVersionRequestRequestTypeDef",
    "DeleteTriggerRequestRequestTypeDef",
    "DeleteTriggerResponseTypeDef",
    "DeleteUserDefinedFunctionRequestRequestTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "DeleteWorkflowResponseTypeDef",
    "DevEndpointCustomLibrariesTypeDef",
    "DevEndpointTypeDef",
    "DoubleColumnStatisticsDataTypeDef",
    "DynamoDBTargetTypeDef",
    "EdgeTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionConfigurationTypeDef",
    "ErrorDetailTypeDef",
    "ErrorDetailsTypeDef",
    "EvaluationMetricsTypeDef",
    "EventBatchingConditionTypeDef",
    "ExecutionPropertyTypeDef",
    "ExportLabelsTaskRunPropertiesTypeDef",
    "FindMatchesMetricsTypeDef",
    "FindMatchesParametersTypeDef",
    "FindMatchesTaskRunPropertiesTypeDef",
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
    "GetDataCatalogEncryptionSettingsRequestRequestTypeDef",
    "GetDataCatalogEncryptionSettingsResponseTypeDef",
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
    "GlueTableTypeDef",
    "GrokClassifierTypeDef",
    "ImportCatalogToGlueRequestRequestTypeDef",
    "ImportLabelsTaskRunPropertiesTypeDef",
    "JdbcTargetTypeDef",
    "JobBookmarkEntryTypeDef",
    "JobBookmarksEncryptionTypeDef",
    "JobCommandTypeDef",
    "JobNodeDetailsTypeDef",
    "JobRunTypeDef",
    "JobTypeDef",
    "JobUpdateTypeDef",
    "JsonClassifierTypeDef",
    "KeySchemaElementTypeDef",
    "LabelingSetGenerationTaskRunPropertiesTypeDef",
    "LastCrawlInfoTypeDef",
    "LineageConfigurationTypeDef",
    "ListCrawlersRequestRequestTypeDef",
    "ListCrawlersResponseTypeDef",
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
    "ListTriggersRequestRequestTypeDef",
    "ListTriggersResponseTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "LocationTypeDef",
    "LongColumnStatisticsDataTypeDef",
    "MLTransformTypeDef",
    "MLUserDataEncryptionTypeDef",
    "MappingEntryTypeDef",
    "MetadataInfoTypeDef",
    "MetadataKeyValuePairTypeDef",
    "MongoDBTargetTypeDef",
    "NodeTypeDef",
    "NotificationPropertyTypeDef",
    "OrderTypeDef",
    "OtherMetadataValueListItemTypeDef",
    "PaginatorConfigTypeDef",
    "PartitionErrorTypeDef",
    "PartitionIndexDescriptorTypeDef",
    "PartitionIndexTypeDef",
    "PartitionInputTypeDef",
    "PartitionTypeDef",
    "PartitionValueListTypeDef",
    "PhysicalConnectionRequirementsTypeDef",
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
    "RegisterSchemaVersionInputRequestTypeDef",
    "RegisterSchemaVersionResponseTypeDef",
    "RegistryIdTypeDef",
    "RegistryListItemTypeDef",
    "RemoveSchemaVersionMetadataInputRequestTypeDef",
    "RemoveSchemaVersionMetadataResponseTypeDef",
    "ResetJobBookmarkRequestRequestTypeDef",
    "ResetJobBookmarkResponseTypeDef",
    "ResourceUriTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeWorkflowRunRequestRequestTypeDef",
    "ResumeWorkflowRunResponseTypeDef",
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
    "SchemaVersionNumberTypeDef",
    "SearchTablesRequestRequestTypeDef",
    "SearchTablesResponseTypeDef",
    "SecurityConfigurationTypeDef",
    "SegmentTypeDef",
    "SerDeInfoTypeDef",
    "SkewedInfoTypeDef",
    "SortCriterionTypeDef",
    "StartCrawlerRequestRequestTypeDef",
    "StartCrawlerScheduleRequestRequestTypeDef",
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
    "StopCrawlerRequestRequestTypeDef",
    "StopCrawlerScheduleRequestRequestTypeDef",
    "StopTriggerRequestRequestTypeDef",
    "StopTriggerResponseTypeDef",
    "StopWorkflowRunRequestRequestTypeDef",
    "StorageDescriptorTypeDef",
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
    "TransformEncryptionTypeDef",
    "TransformFilterCriteriaTypeDef",
    "TransformParametersTypeDef",
    "TransformSortCriteriaTypeDef",
    "TriggerNodeDetailsTypeDef",
    "TriggerTypeDef",
    "TriggerUpdateTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateClassifierRequestRequestTypeDef",
    "UpdateColumnStatisticsForPartitionRequestRequestTypeDef",
    "UpdateColumnStatisticsForPartitionResponseTypeDef",
    "UpdateColumnStatisticsForTableRequestRequestTypeDef",
    "UpdateColumnStatisticsForTableResponseTypeDef",
    "UpdateConnectionRequestRequestTypeDef",
    "UpdateCrawlerRequestRequestTypeDef",
    "UpdateCrawlerScheduleRequestRequestTypeDef",
    "UpdateCsvClassifierRequestTypeDef",
    "UpdateDatabaseRequestRequestTypeDef",
    "UpdateDevEndpointRequestRequestTypeDef",
    "UpdateGrokClassifierRequestTypeDef",
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
    "UpdateTableRequestRequestTypeDef",
    "UpdateTriggerRequestRequestTypeDef",
    "UpdateTriggerResponseTypeDef",
    "UpdateUserDefinedFunctionRequestRequestTypeDef",
    "UpdateWorkflowRequestRequestTypeDef",
    "UpdateWorkflowResponseTypeDef",
    "UpdateXMLClassifierRequestTypeDef",
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

BackfillErrorTypeDef = TypedDict(
    "BackfillErrorTypeDef",
    {
        "Code": BackfillErrorCodeType,
        "Partitions": List["PartitionValueListTypeDef"],
    },
    total=False,
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

BooleanColumnStatisticsDataTypeDef = TypedDict(
    "BooleanColumnStatisticsDataTypeDef",
    {
        "NumberOfTrues": int,
        "NumberOfFalses": int,
        "NumberOfNulls": int,
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

CatalogEntryTypeDef = TypedDict(
    "CatalogEntryTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)

CatalogImportStatusTypeDef = TypedDict(
    "CatalogImportStatusTypeDef",
    {
        "ImportCompleted": bool,
        "ImportTime": datetime,
        "ImportedBy": str,
    },
    total=False,
)

CatalogTargetTypeDef = TypedDict(
    "CatalogTargetTypeDef",
    {
        "DatabaseName": str,
        "Tables": List[str],
    },
)

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
    },
    total=False,
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
    },
    total=False,
)

class CreateCsvClassifierRequestTypeDef(
    _RequiredCreateCsvClassifierRequestTypeDef, _OptionalCreateCsvClassifierRequestTypeDef
):
    pass

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
    "DataLakePrincipalTypeDef",
    {
        "DataLakePrincipalIdentifier": str,
    },
    total=False,
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
    },
    total=False,
)

class DatabaseTypeDef(_RequiredDatabaseTypeDef, _OptionalDatabaseTypeDef):
    pass

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
    },
    total=False,
)

class GlueTableTypeDef(_RequiredGlueTableTypeDef, _OptionalGlueTableTypeDef):
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

JdbcTargetTypeDef = TypedDict(
    "JdbcTargetTypeDef",
    {
        "ConnectionName": str,
        "Path": str,
        "Exclusions": List[str],
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
    },
    total=False,
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

KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef",
    {
        "Name": str,
        "Type": str,
    },
)

LabelingSetGenerationTaskRunPropertiesTypeDef = TypedDict(
    "LabelingSetGenerationTaskRunPropertiesTypeDef",
    {
        "OutputS3Path": str,
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

MongoDBTargetTypeDef = TypedDict(
    "MongoDBTargetTypeDef",
    {
        "ConnectionName": str,
        "Path": str,
        "ScanAll": bool,
    },
    total=False,
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

S3EncryptionTypeDef = TypedDict(
    "S3EncryptionTypeDef",
    {
        "S3EncryptionMode": S3EncryptionModeType,
        "KmsKeyArn": str,
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

SerDeInfoTypeDef = TypedDict(
    "SerDeInfoTypeDef",
    {
        "Name": str,
        "SerializationLibrary": str,
        "Parameters": Dict[str, str],
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

StartWorkflowRunRequestRequestTypeDef = TypedDict(
    "StartWorkflowRunRequestRequestTypeDef",
    {
        "Name": str,
    },
)

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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagsToRemove": List[str],
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
    },
    total=False,
)

class UpdateCsvClassifierRequestTypeDef(
    _RequiredUpdateCsvClassifierRequestTypeDef, _OptionalUpdateCsvClassifierRequestTypeDef
):
    pass

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
