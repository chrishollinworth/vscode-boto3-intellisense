"""
Type annotations for glue service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_glue.client import GlueClient

    session = Session()
    client: GlueClient = session.client("glue")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeEntityPaginator,
    GetClassifiersPaginator,
    GetConnectionsPaginator,
    GetCrawlerMetricsPaginator,
    GetCrawlersPaginator,
    GetDatabasesPaginator,
    GetDevEndpointsPaginator,
    GetJobRunsPaginator,
    GetJobsPaginator,
    GetPartitionIndexesPaginator,
    GetPartitionsPaginator,
    GetResourcePoliciesPaginator,
    GetSecurityConfigurationsPaginator,
    GetTablesPaginator,
    GetTableVersionsPaginator,
    GetTriggersPaginator,
    GetUserDefinedFunctionsPaginator,
    GetWorkflowRunsPaginator,
    ListBlueprintsPaginator,
    ListConnectionTypesPaginator,
    ListEntitiesPaginator,
    ListJobsPaginator,
    ListRegistriesPaginator,
    ListSchemasPaginator,
    ListSchemaVersionsPaginator,
    ListTableOptimizerRunsPaginator,
    ListTriggersPaginator,
    ListUsageProfilesPaginator,
    ListWorkflowsPaginator,
)
from .type_defs import (
    BatchCreatePartitionRequestTypeDef,
    BatchCreatePartitionResponseTypeDef,
    BatchDeleteConnectionRequestTypeDef,
    BatchDeleteConnectionResponseTypeDef,
    BatchDeletePartitionRequestTypeDef,
    BatchDeletePartitionResponseTypeDef,
    BatchDeleteTableRequestTypeDef,
    BatchDeleteTableResponseTypeDef,
    BatchDeleteTableVersionRequestTypeDef,
    BatchDeleteTableVersionResponseTypeDef,
    BatchGetBlueprintsRequestTypeDef,
    BatchGetBlueprintsResponseTypeDef,
    BatchGetCrawlersRequestTypeDef,
    BatchGetCrawlersResponseTypeDef,
    BatchGetCustomEntityTypesRequestTypeDef,
    BatchGetCustomEntityTypesResponseTypeDef,
    BatchGetDataQualityResultRequestTypeDef,
    BatchGetDataQualityResultResponseTypeDef,
    BatchGetDevEndpointsRequestTypeDef,
    BatchGetDevEndpointsResponseTypeDef,
    BatchGetJobsRequestTypeDef,
    BatchGetJobsResponseTypeDef,
    BatchGetPartitionRequestTypeDef,
    BatchGetPartitionResponseTypeDef,
    BatchGetTableOptimizerRequestTypeDef,
    BatchGetTableOptimizerResponseTypeDef,
    BatchGetTriggersRequestTypeDef,
    BatchGetTriggersResponseTypeDef,
    BatchGetWorkflowsRequestTypeDef,
    BatchGetWorkflowsResponseTypeDef,
    BatchPutDataQualityStatisticAnnotationRequestTypeDef,
    BatchPutDataQualityStatisticAnnotationResponseTypeDef,
    BatchStopJobRunRequestTypeDef,
    BatchStopJobRunResponseTypeDef,
    BatchUpdatePartitionRequestTypeDef,
    BatchUpdatePartitionResponseTypeDef,
    CancelDataQualityRuleRecommendationRunRequestTypeDef,
    CancelDataQualityRulesetEvaluationRunRequestTypeDef,
    CancelMLTaskRunRequestTypeDef,
    CancelMLTaskRunResponseTypeDef,
    CancelStatementRequestTypeDef,
    CheckSchemaVersionValidityInputTypeDef,
    CheckSchemaVersionValidityResponseTypeDef,
    CreateBlueprintRequestTypeDef,
    CreateBlueprintResponseTypeDef,
    CreateCatalogRequestTypeDef,
    CreateClassifierRequestTypeDef,
    CreateColumnStatisticsTaskSettingsRequestTypeDef,
    CreateConnectionRequestTypeDef,
    CreateConnectionResponseTypeDef,
    CreateCrawlerRequestTypeDef,
    CreateCustomEntityTypeRequestTypeDef,
    CreateCustomEntityTypeResponseTypeDef,
    CreateDatabaseRequestTypeDef,
    CreateDataQualityRulesetRequestTypeDef,
    CreateDataQualityRulesetResponseTypeDef,
    CreateDevEndpointRequestTypeDef,
    CreateDevEndpointResponseTypeDef,
    CreateIntegrationRequestTypeDef,
    CreateIntegrationResourcePropertyRequestTypeDef,
    CreateIntegrationResourcePropertyResponseTypeDef,
    CreateIntegrationResponseTypeDef,
    CreateIntegrationTablePropertiesRequestTypeDef,
    CreateJobRequestTypeDef,
    CreateJobResponseTypeDef,
    CreateMLTransformRequestTypeDef,
    CreateMLTransformResponseTypeDef,
    CreatePartitionIndexRequestTypeDef,
    CreatePartitionRequestTypeDef,
    CreateRegistryInputTypeDef,
    CreateRegistryResponseTypeDef,
    CreateSchemaInputTypeDef,
    CreateSchemaResponseTypeDef,
    CreateScriptRequestTypeDef,
    CreateScriptResponseTypeDef,
    CreateSecurityConfigurationRequestTypeDef,
    CreateSecurityConfigurationResponseTypeDef,
    CreateSessionRequestTypeDef,
    CreateSessionResponseTypeDef,
    CreateTableOptimizerRequestTypeDef,
    CreateTableRequestTypeDef,
    CreateTriggerRequestTypeDef,
    CreateTriggerResponseTypeDef,
    CreateUsageProfileRequestTypeDef,
    CreateUsageProfileResponseTypeDef,
    CreateUserDefinedFunctionRequestTypeDef,
    CreateWorkflowRequestTypeDef,
    CreateWorkflowResponseTypeDef,
    DeleteBlueprintRequestTypeDef,
    DeleteBlueprintResponseTypeDef,
    DeleteCatalogRequestTypeDef,
    DeleteClassifierRequestTypeDef,
    DeleteColumnStatisticsForPartitionRequestTypeDef,
    DeleteColumnStatisticsForTableRequestTypeDef,
    DeleteColumnStatisticsTaskSettingsRequestTypeDef,
    DeleteConnectionRequestTypeDef,
    DeleteCrawlerRequestTypeDef,
    DeleteCustomEntityTypeRequestTypeDef,
    DeleteCustomEntityTypeResponseTypeDef,
    DeleteDatabaseRequestTypeDef,
    DeleteDataQualityRulesetRequestTypeDef,
    DeleteDevEndpointRequestTypeDef,
    DeleteIntegrationRequestTypeDef,
    DeleteIntegrationResponseTypeDef,
    DeleteIntegrationTablePropertiesRequestTypeDef,
    DeleteJobRequestTypeDef,
    DeleteJobResponseTypeDef,
    DeleteMLTransformRequestTypeDef,
    DeleteMLTransformResponseTypeDef,
    DeletePartitionIndexRequestTypeDef,
    DeletePartitionRequestTypeDef,
    DeleteRegistryInputTypeDef,
    DeleteRegistryResponseTypeDef,
    DeleteResourcePolicyRequestTypeDef,
    DeleteSchemaInputTypeDef,
    DeleteSchemaResponseTypeDef,
    DeleteSchemaVersionsInputTypeDef,
    DeleteSchemaVersionsResponseTypeDef,
    DeleteSecurityConfigurationRequestTypeDef,
    DeleteSessionRequestTypeDef,
    DeleteSessionResponseTypeDef,
    DeleteTableOptimizerRequestTypeDef,
    DeleteTableRequestTypeDef,
    DeleteTableVersionRequestTypeDef,
    DeleteTriggerRequestTypeDef,
    DeleteTriggerResponseTypeDef,
    DeleteUsageProfileRequestTypeDef,
    DeleteUserDefinedFunctionRequestTypeDef,
    DeleteWorkflowRequestTypeDef,
    DeleteWorkflowResponseTypeDef,
    DescribeConnectionTypeRequestTypeDef,
    DescribeConnectionTypeResponseTypeDef,
    DescribeEntityRequestTypeDef,
    DescribeEntityResponseTypeDef,
    DescribeInboundIntegrationsRequestTypeDef,
    DescribeInboundIntegrationsResponseTypeDef,
    DescribeIntegrationsRequestTypeDef,
    DescribeIntegrationsResponseTypeDef,
    GetBlueprintRequestTypeDef,
    GetBlueprintResponseTypeDef,
    GetBlueprintRunRequestTypeDef,
    GetBlueprintRunResponseTypeDef,
    GetBlueprintRunsRequestTypeDef,
    GetBlueprintRunsResponseTypeDef,
    GetCatalogImportStatusRequestTypeDef,
    GetCatalogImportStatusResponseTypeDef,
    GetCatalogRequestTypeDef,
    GetCatalogResponseTypeDef,
    GetCatalogsRequestTypeDef,
    GetCatalogsResponseTypeDef,
    GetClassifierRequestTypeDef,
    GetClassifierResponseTypeDef,
    GetClassifiersRequestTypeDef,
    GetClassifiersResponseTypeDef,
    GetColumnStatisticsForPartitionRequestTypeDef,
    GetColumnStatisticsForPartitionResponseTypeDef,
    GetColumnStatisticsForTableRequestTypeDef,
    GetColumnStatisticsForTableResponseTypeDef,
    GetColumnStatisticsTaskRunRequestTypeDef,
    GetColumnStatisticsTaskRunResponseTypeDef,
    GetColumnStatisticsTaskRunsRequestTypeDef,
    GetColumnStatisticsTaskRunsResponseTypeDef,
    GetColumnStatisticsTaskSettingsRequestTypeDef,
    GetColumnStatisticsTaskSettingsResponseTypeDef,
    GetConnectionRequestTypeDef,
    GetConnectionResponseTypeDef,
    GetConnectionsRequestTypeDef,
    GetConnectionsResponseTypeDef,
    GetCrawlerMetricsRequestTypeDef,
    GetCrawlerMetricsResponseTypeDef,
    GetCrawlerRequestTypeDef,
    GetCrawlerResponseTypeDef,
    GetCrawlersRequestTypeDef,
    GetCrawlersResponseTypeDef,
    GetCustomEntityTypeRequestTypeDef,
    GetCustomEntityTypeResponseTypeDef,
    GetDatabaseRequestTypeDef,
    GetDatabaseResponseTypeDef,
    GetDatabasesRequestTypeDef,
    GetDatabasesResponseTypeDef,
    GetDataCatalogEncryptionSettingsRequestTypeDef,
    GetDataCatalogEncryptionSettingsResponseTypeDef,
    GetDataflowGraphRequestTypeDef,
    GetDataflowGraphResponseTypeDef,
    GetDataQualityModelRequestTypeDef,
    GetDataQualityModelResponseTypeDef,
    GetDataQualityModelResultRequestTypeDef,
    GetDataQualityModelResultResponseTypeDef,
    GetDataQualityResultRequestTypeDef,
    GetDataQualityResultResponseTypeDef,
    GetDataQualityRuleRecommendationRunRequestTypeDef,
    GetDataQualityRuleRecommendationRunResponseTypeDef,
    GetDataQualityRulesetEvaluationRunRequestTypeDef,
    GetDataQualityRulesetEvaluationRunResponseTypeDef,
    GetDataQualityRulesetRequestTypeDef,
    GetDataQualityRulesetResponseTypeDef,
    GetDevEndpointRequestTypeDef,
    GetDevEndpointResponseTypeDef,
    GetDevEndpointsRequestTypeDef,
    GetDevEndpointsResponseTypeDef,
    GetEntityRecordsRequestTypeDef,
    GetEntityRecordsResponseTypeDef,
    GetIntegrationResourcePropertyRequestTypeDef,
    GetIntegrationResourcePropertyResponseTypeDef,
    GetIntegrationTablePropertiesRequestTypeDef,
    GetIntegrationTablePropertiesResponseTypeDef,
    GetJobBookmarkRequestTypeDef,
    GetJobBookmarkResponseTypeDef,
    GetJobRequestTypeDef,
    GetJobResponseTypeDef,
    GetJobRunRequestTypeDef,
    GetJobRunResponseTypeDef,
    GetJobRunsRequestTypeDef,
    GetJobRunsResponseTypeDef,
    GetJobsRequestTypeDef,
    GetJobsResponseTypeDef,
    GetMappingRequestTypeDef,
    GetMappingResponseTypeDef,
    GetMLTaskRunRequestTypeDef,
    GetMLTaskRunResponseTypeDef,
    GetMLTaskRunsRequestTypeDef,
    GetMLTaskRunsResponseTypeDef,
    GetMLTransformRequestTypeDef,
    GetMLTransformResponseTypeDef,
    GetMLTransformsRequestTypeDef,
    GetMLTransformsResponseTypeDef,
    GetPartitionIndexesRequestTypeDef,
    GetPartitionIndexesResponseTypeDef,
    GetPartitionRequestTypeDef,
    GetPartitionResponseTypeDef,
    GetPartitionsRequestTypeDef,
    GetPartitionsResponseTypeDef,
    GetPlanRequestTypeDef,
    GetPlanResponseTypeDef,
    GetRegistryInputTypeDef,
    GetRegistryResponseTypeDef,
    GetResourcePoliciesRequestTypeDef,
    GetResourcePoliciesResponseTypeDef,
    GetResourcePolicyRequestTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetSchemaByDefinitionInputTypeDef,
    GetSchemaByDefinitionResponseTypeDef,
    GetSchemaInputTypeDef,
    GetSchemaResponseTypeDef,
    GetSchemaVersionInputTypeDef,
    GetSchemaVersionResponseTypeDef,
    GetSchemaVersionsDiffInputTypeDef,
    GetSchemaVersionsDiffResponseTypeDef,
    GetSecurityConfigurationRequestTypeDef,
    GetSecurityConfigurationResponseTypeDef,
    GetSecurityConfigurationsRequestTypeDef,
    GetSecurityConfigurationsResponseTypeDef,
    GetSessionRequestTypeDef,
    GetSessionResponseTypeDef,
    GetStatementRequestTypeDef,
    GetStatementResponseTypeDef,
    GetTableOptimizerRequestTypeDef,
    GetTableOptimizerResponseTypeDef,
    GetTableRequestTypeDef,
    GetTableResponseTypeDef,
    GetTablesRequestTypeDef,
    GetTablesResponseTypeDef,
    GetTableVersionRequestTypeDef,
    GetTableVersionResponseTypeDef,
    GetTableVersionsRequestTypeDef,
    GetTableVersionsResponseTypeDef,
    GetTagsRequestTypeDef,
    GetTagsResponseTypeDef,
    GetTriggerRequestTypeDef,
    GetTriggerResponseTypeDef,
    GetTriggersRequestTypeDef,
    GetTriggersResponseTypeDef,
    GetUnfilteredPartitionMetadataRequestTypeDef,
    GetUnfilteredPartitionMetadataResponseTypeDef,
    GetUnfilteredPartitionsMetadataRequestTypeDef,
    GetUnfilteredPartitionsMetadataResponseTypeDef,
    GetUnfilteredTableMetadataRequestTypeDef,
    GetUnfilteredTableMetadataResponseTypeDef,
    GetUsageProfileRequestTypeDef,
    GetUsageProfileResponseTypeDef,
    GetUserDefinedFunctionRequestTypeDef,
    GetUserDefinedFunctionResponseTypeDef,
    GetUserDefinedFunctionsRequestTypeDef,
    GetUserDefinedFunctionsResponseTypeDef,
    GetWorkflowRequestTypeDef,
    GetWorkflowResponseTypeDef,
    GetWorkflowRunPropertiesRequestTypeDef,
    GetWorkflowRunPropertiesResponseTypeDef,
    GetWorkflowRunRequestTypeDef,
    GetWorkflowRunResponseTypeDef,
    GetWorkflowRunsRequestTypeDef,
    GetWorkflowRunsResponseTypeDef,
    ImportCatalogToGlueRequestTypeDef,
    ListBlueprintsRequestTypeDef,
    ListBlueprintsResponseTypeDef,
    ListColumnStatisticsTaskRunsRequestTypeDef,
    ListColumnStatisticsTaskRunsResponseTypeDef,
    ListConnectionTypesRequestTypeDef,
    ListConnectionTypesResponseTypeDef,
    ListCrawlersRequestTypeDef,
    ListCrawlersResponseTypeDef,
    ListCrawlsRequestTypeDef,
    ListCrawlsResponseTypeDef,
    ListCustomEntityTypesRequestTypeDef,
    ListCustomEntityTypesResponseTypeDef,
    ListDataQualityResultsRequestTypeDef,
    ListDataQualityResultsResponseTypeDef,
    ListDataQualityRuleRecommendationRunsRequestTypeDef,
    ListDataQualityRuleRecommendationRunsResponseTypeDef,
    ListDataQualityRulesetEvaluationRunsRequestTypeDef,
    ListDataQualityRulesetEvaluationRunsResponseTypeDef,
    ListDataQualityRulesetsRequestTypeDef,
    ListDataQualityRulesetsResponseTypeDef,
    ListDataQualityStatisticAnnotationsRequestTypeDef,
    ListDataQualityStatisticAnnotationsResponseTypeDef,
    ListDataQualityStatisticsRequestTypeDef,
    ListDataQualityStatisticsResponseTypeDef,
    ListDevEndpointsRequestTypeDef,
    ListDevEndpointsResponseTypeDef,
    ListEntitiesRequestTypeDef,
    ListEntitiesResponseTypeDef,
    ListJobsRequestTypeDef,
    ListJobsResponseTypeDef,
    ListMLTransformsRequestTypeDef,
    ListMLTransformsResponseTypeDef,
    ListRegistriesInputTypeDef,
    ListRegistriesResponseTypeDef,
    ListSchemasInputTypeDef,
    ListSchemasResponseTypeDef,
    ListSchemaVersionsInputTypeDef,
    ListSchemaVersionsResponseTypeDef,
    ListSessionsRequestTypeDef,
    ListSessionsResponseTypeDef,
    ListStatementsRequestTypeDef,
    ListStatementsResponseTypeDef,
    ListTableOptimizerRunsRequestTypeDef,
    ListTableOptimizerRunsResponseTypeDef,
    ListTriggersRequestTypeDef,
    ListTriggersResponseTypeDef,
    ListUsageProfilesRequestTypeDef,
    ListUsageProfilesResponseTypeDef,
    ListWorkflowsRequestTypeDef,
    ListWorkflowsResponseTypeDef,
    ModifyIntegrationRequestTypeDef,
    ModifyIntegrationResponseTypeDef,
    PutDataCatalogEncryptionSettingsRequestTypeDef,
    PutDataQualityProfileAnnotationRequestTypeDef,
    PutResourcePolicyRequestTypeDef,
    PutResourcePolicyResponseTypeDef,
    PutSchemaVersionMetadataInputTypeDef,
    PutSchemaVersionMetadataResponseTypeDef,
    PutWorkflowRunPropertiesRequestTypeDef,
    QuerySchemaVersionMetadataInputTypeDef,
    QuerySchemaVersionMetadataResponseTypeDef,
    RegisterSchemaVersionInputTypeDef,
    RegisterSchemaVersionResponseTypeDef,
    RemoveSchemaVersionMetadataInputTypeDef,
    RemoveSchemaVersionMetadataResponseTypeDef,
    ResetJobBookmarkRequestTypeDef,
    ResetJobBookmarkResponseTypeDef,
    ResumeWorkflowRunRequestTypeDef,
    ResumeWorkflowRunResponseTypeDef,
    RunStatementRequestTypeDef,
    RunStatementResponseTypeDef,
    SearchTablesRequestTypeDef,
    SearchTablesResponseTypeDef,
    StartBlueprintRunRequestTypeDef,
    StartBlueprintRunResponseTypeDef,
    StartColumnStatisticsTaskRunRequestTypeDef,
    StartColumnStatisticsTaskRunResponseTypeDef,
    StartColumnStatisticsTaskRunScheduleRequestTypeDef,
    StartCrawlerRequestTypeDef,
    StartCrawlerScheduleRequestTypeDef,
    StartDataQualityRuleRecommendationRunRequestTypeDef,
    StartDataQualityRuleRecommendationRunResponseTypeDef,
    StartDataQualityRulesetEvaluationRunRequestTypeDef,
    StartDataQualityRulesetEvaluationRunResponseTypeDef,
    StartExportLabelsTaskRunRequestTypeDef,
    StartExportLabelsTaskRunResponseTypeDef,
    StartImportLabelsTaskRunRequestTypeDef,
    StartImportLabelsTaskRunResponseTypeDef,
    StartJobRunRequestTypeDef,
    StartJobRunResponseTypeDef,
    StartMLEvaluationTaskRunRequestTypeDef,
    StartMLEvaluationTaskRunResponseTypeDef,
    StartMLLabelingSetGenerationTaskRunRequestTypeDef,
    StartMLLabelingSetGenerationTaskRunResponseTypeDef,
    StartTriggerRequestTypeDef,
    StartTriggerResponseTypeDef,
    StartWorkflowRunRequestTypeDef,
    StartWorkflowRunResponseTypeDef,
    StopColumnStatisticsTaskRunRequestTypeDef,
    StopColumnStatisticsTaskRunScheduleRequestTypeDef,
    StopCrawlerRequestTypeDef,
    StopCrawlerScheduleRequestTypeDef,
    StopSessionRequestTypeDef,
    StopSessionResponseTypeDef,
    StopTriggerRequestTypeDef,
    StopTriggerResponseTypeDef,
    StopWorkflowRunRequestTypeDef,
    TagResourceRequestTypeDef,
    TestConnectionRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateBlueprintRequestTypeDef,
    UpdateBlueprintResponseTypeDef,
    UpdateCatalogRequestTypeDef,
    UpdateClassifierRequestTypeDef,
    UpdateColumnStatisticsForPartitionRequestTypeDef,
    UpdateColumnStatisticsForPartitionResponseTypeDef,
    UpdateColumnStatisticsForTableRequestTypeDef,
    UpdateColumnStatisticsForTableResponseTypeDef,
    UpdateColumnStatisticsTaskSettingsRequestTypeDef,
    UpdateConnectionRequestTypeDef,
    UpdateCrawlerRequestTypeDef,
    UpdateCrawlerScheduleRequestTypeDef,
    UpdateDatabaseRequestTypeDef,
    UpdateDataQualityRulesetRequestTypeDef,
    UpdateDataQualityRulesetResponseTypeDef,
    UpdateDevEndpointRequestTypeDef,
    UpdateIntegrationResourcePropertyRequestTypeDef,
    UpdateIntegrationResourcePropertyResponseTypeDef,
    UpdateIntegrationTablePropertiesRequestTypeDef,
    UpdateJobFromSourceControlRequestTypeDef,
    UpdateJobFromSourceControlResponseTypeDef,
    UpdateJobRequestTypeDef,
    UpdateJobResponseTypeDef,
    UpdateMLTransformRequestTypeDef,
    UpdateMLTransformResponseTypeDef,
    UpdatePartitionRequestTypeDef,
    UpdateRegistryInputTypeDef,
    UpdateRegistryResponseTypeDef,
    UpdateSchemaInputTypeDef,
    UpdateSchemaResponseTypeDef,
    UpdateSourceControlFromJobRequestTypeDef,
    UpdateSourceControlFromJobResponseTypeDef,
    UpdateTableOptimizerRequestTypeDef,
    UpdateTableRequestTypeDef,
    UpdateTriggerRequestTypeDef,
    UpdateTriggerResponseTypeDef,
    UpdateUsageProfileRequestTypeDef,
    UpdateUsageProfileResponseTypeDef,
    UpdateUserDefinedFunctionRequestTypeDef,
    UpdateWorkflowRequestTypeDef,
    UpdateWorkflowResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("GlueClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    AlreadyExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ColumnStatisticsTaskNotRunningException: Type[BotocoreClientError]
    ColumnStatisticsTaskRunningException: Type[BotocoreClientError]
    ColumnStatisticsTaskStoppingException: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConcurrentRunsExceededException: Type[BotocoreClientError]
    ConditionCheckFailureException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    CrawlerNotRunningException: Type[BotocoreClientError]
    CrawlerRunningException: Type[BotocoreClientError]
    CrawlerStoppingException: Type[BotocoreClientError]
    EntityNotFoundException: Type[BotocoreClientError]
    FederatedResourceAlreadyExistsException: Type[BotocoreClientError]
    FederationSourceException: Type[BotocoreClientError]
    FederationSourceRetryableException: Type[BotocoreClientError]
    GlueEncryptionException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    IllegalBlueprintStateException: Type[BotocoreClientError]
    IllegalSessionStateException: Type[BotocoreClientError]
    IllegalWorkflowStateException: Type[BotocoreClientError]
    IntegrationConflictOperationFault: Type[BotocoreClientError]
    IntegrationNotFoundFault: Type[BotocoreClientError]
    IntegrationQuotaExceededFault: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidIntegrationStateFault: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    KMSKeyNotAccessibleFault: Type[BotocoreClientError]
    MLTransformNotReadyException: Type[BotocoreClientError]
    NoScheduleException: Type[BotocoreClientError]
    OperationNotSupportedException: Type[BotocoreClientError]
    OperationTimeoutException: Type[BotocoreClientError]
    PermissionTypeMismatchException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceNotReadyException: Type[BotocoreClientError]
    ResourceNumberLimitExceededException: Type[BotocoreClientError]
    SchedulerNotRunningException: Type[BotocoreClientError]
    SchedulerRunningException: Type[BotocoreClientError]
    SchedulerTransitioningException: Type[BotocoreClientError]
    TargetResourceNotFound: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]
    VersionMismatchException: Type[BotocoreClientError]

class GlueClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        GlueClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html#Glue.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#generate_presigned_url)
        """

    def batch_create_partition(
        self, **kwargs: Unpack[BatchCreatePartitionRequestTypeDef]
    ) -> BatchCreatePartitionResponseTypeDef:
        """
        Creates one or more partitions in a batch operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_create_partition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_create_partition)
        """

    def batch_delete_connection(
        self, **kwargs: Unpack[BatchDeleteConnectionRequestTypeDef]
    ) -> BatchDeleteConnectionResponseTypeDef:
        """
        Deletes a list of connection definitions from the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_delete_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_delete_connection)
        """

    def batch_delete_partition(
        self, **kwargs: Unpack[BatchDeletePartitionRequestTypeDef]
    ) -> BatchDeletePartitionResponseTypeDef:
        """
        Deletes one or more partitions in a batch operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_delete_partition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_delete_partition)
        """

    def batch_delete_table(
        self, **kwargs: Unpack[BatchDeleteTableRequestTypeDef]
    ) -> BatchDeleteTableResponseTypeDef:
        """
        Deletes multiple tables at once.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_delete_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_delete_table)
        """

    def batch_delete_table_version(
        self, **kwargs: Unpack[BatchDeleteTableVersionRequestTypeDef]
    ) -> BatchDeleteTableVersionResponseTypeDef:
        """
        Deletes a specified batch of versions of a table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_delete_table_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_delete_table_version)
        """

    def batch_get_blueprints(
        self, **kwargs: Unpack[BatchGetBlueprintsRequestTypeDef]
    ) -> BatchGetBlueprintsResponseTypeDef:
        """
        Retrieves information about a list of blueprints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_get_blueprints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_get_blueprints)
        """

    def batch_get_crawlers(
        self, **kwargs: Unpack[BatchGetCrawlersRequestTypeDef]
    ) -> BatchGetCrawlersResponseTypeDef:
        """
        Returns a list of resource metadata for a given list of crawler names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_get_crawlers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_get_crawlers)
        """

    def batch_get_custom_entity_types(
        self, **kwargs: Unpack[BatchGetCustomEntityTypesRequestTypeDef]
    ) -> BatchGetCustomEntityTypesResponseTypeDef:
        """
        Retrieves the details for the custom patterns specified by a list of names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_get_custom_entity_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_get_custom_entity_types)
        """

    def batch_get_data_quality_result(
        self, **kwargs: Unpack[BatchGetDataQualityResultRequestTypeDef]
    ) -> BatchGetDataQualityResultResponseTypeDef:
        """
        Retrieves a list of data quality results for the specified result IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_get_data_quality_result.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_get_data_quality_result)
        """

    def batch_get_dev_endpoints(
        self, **kwargs: Unpack[BatchGetDevEndpointsRequestTypeDef]
    ) -> BatchGetDevEndpointsResponseTypeDef:
        """
        Returns a list of resource metadata for a given list of development endpoint
        names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_get_dev_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_get_dev_endpoints)
        """

    def batch_get_jobs(
        self, **kwargs: Unpack[BatchGetJobsRequestTypeDef]
    ) -> BatchGetJobsResponseTypeDef:
        """
        Returns a list of resource metadata for a given list of job names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_get_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_get_jobs)
        """

    def batch_get_partition(
        self, **kwargs: Unpack[BatchGetPartitionRequestTypeDef]
    ) -> BatchGetPartitionResponseTypeDef:
        """
        Retrieves partitions in a batch request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_get_partition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_get_partition)
        """

    def batch_get_table_optimizer(
        self, **kwargs: Unpack[BatchGetTableOptimizerRequestTypeDef]
    ) -> BatchGetTableOptimizerResponseTypeDef:
        """
        Returns the configuration for the specified table optimizers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_get_table_optimizer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_get_table_optimizer)
        """

    def batch_get_triggers(
        self, **kwargs: Unpack[BatchGetTriggersRequestTypeDef]
    ) -> BatchGetTriggersResponseTypeDef:
        """
        Returns a list of resource metadata for a given list of trigger names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_get_triggers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_get_triggers)
        """

    def batch_get_workflows(
        self, **kwargs: Unpack[BatchGetWorkflowsRequestTypeDef]
    ) -> BatchGetWorkflowsResponseTypeDef:
        """
        Returns a list of resource metadata for a given list of workflow names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_get_workflows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_get_workflows)
        """

    def batch_put_data_quality_statistic_annotation(
        self, **kwargs: Unpack[BatchPutDataQualityStatisticAnnotationRequestTypeDef]
    ) -> BatchPutDataQualityStatisticAnnotationResponseTypeDef:
        """
        Annotate datapoints over time for a specific data quality statistic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_put_data_quality_statistic_annotation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_put_data_quality_statistic_annotation)
        """

    def batch_stop_job_run(
        self, **kwargs: Unpack[BatchStopJobRunRequestTypeDef]
    ) -> BatchStopJobRunResponseTypeDef:
        """
        Stops one or more job runs for a specified job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_stop_job_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_stop_job_run)
        """

    def batch_update_partition(
        self, **kwargs: Unpack[BatchUpdatePartitionRequestTypeDef]
    ) -> BatchUpdatePartitionResponseTypeDef:
        """
        Updates one or more partitions in a batch operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/batch_update_partition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#batch_update_partition)
        """

    def cancel_data_quality_rule_recommendation_run(
        self, **kwargs: Unpack[CancelDataQualityRuleRecommendationRunRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels the specified recommendation run that was being used to generate rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/cancel_data_quality_rule_recommendation_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#cancel_data_quality_rule_recommendation_run)
        """

    def cancel_data_quality_ruleset_evaluation_run(
        self, **kwargs: Unpack[CancelDataQualityRulesetEvaluationRunRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels a run where a ruleset is being evaluated against a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/cancel_data_quality_ruleset_evaluation_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#cancel_data_quality_ruleset_evaluation_run)
        """

    def cancel_ml_task_run(
        self, **kwargs: Unpack[CancelMLTaskRunRequestTypeDef]
    ) -> CancelMLTaskRunResponseTypeDef:
        """
        Cancels (stops) a task run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/cancel_ml_task_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#cancel_ml_task_run)
        """

    def cancel_statement(self, **kwargs: Unpack[CancelStatementRequestTypeDef]) -> Dict[str, Any]:
        """
        Cancels the statement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/cancel_statement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#cancel_statement)
        """

    def check_schema_version_validity(
        self, **kwargs: Unpack[CheckSchemaVersionValidityInputTypeDef]
    ) -> CheckSchemaVersionValidityResponseTypeDef:
        """
        Validates the supplied schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/check_schema_version_validity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#check_schema_version_validity)
        """

    def create_blueprint(
        self, **kwargs: Unpack[CreateBlueprintRequestTypeDef]
    ) -> CreateBlueprintResponseTypeDef:
        """
        Registers a blueprint with Glue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_blueprint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_blueprint)
        """

    def create_catalog(self, **kwargs: Unpack[CreateCatalogRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a new catalog in the Glue Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_catalog.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_catalog)
        """

    def create_classifier(self, **kwargs: Unpack[CreateClassifierRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a classifier in the user's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_classifier.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_classifier)
        """

    def create_column_statistics_task_settings(
        self, **kwargs: Unpack[CreateColumnStatisticsTaskSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates settings for a column statistics task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_column_statistics_task_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_column_statistics_task_settings)
        """

    def create_connection(
        self, **kwargs: Unpack[CreateConnectionRequestTypeDef]
    ) -> CreateConnectionResponseTypeDef:
        """
        Creates a connection definition in the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_connection)
        """

    def create_crawler(self, **kwargs: Unpack[CreateCrawlerRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a new crawler with specified targets, role, configuration, and optional
        schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_crawler.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_crawler)
        """

    def create_custom_entity_type(
        self, **kwargs: Unpack[CreateCustomEntityTypeRequestTypeDef]
    ) -> CreateCustomEntityTypeResponseTypeDef:
        """
        Creates a custom pattern that is used to detect sensitive data across the
        columns and rows of your structured data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_custom_entity_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_custom_entity_type)
        """

    def create_data_quality_ruleset(
        self, **kwargs: Unpack[CreateDataQualityRulesetRequestTypeDef]
    ) -> CreateDataQualityRulesetResponseTypeDef:
        """
        Creates a data quality ruleset with DQDL rules applied to a specified Glue
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_data_quality_ruleset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_data_quality_ruleset)
        """

    def create_database(self, **kwargs: Unpack[CreateDatabaseRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a new database in a Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_database)
        """

    def create_dev_endpoint(
        self, **kwargs: Unpack[CreateDevEndpointRequestTypeDef]
    ) -> CreateDevEndpointResponseTypeDef:
        """
        Creates a new development endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_dev_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_dev_endpoint)
        """

    def create_integration(
        self, **kwargs: Unpack[CreateIntegrationRequestTypeDef]
    ) -> CreateIntegrationResponseTypeDef:
        """
        Creates a Zero-ETL integration in the caller's account between two resources
        with Amazon Resource Names (ARNs): the <code>SourceArn</code> and
        <code>TargetArn</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_integration)
        """

    def create_integration_resource_property(
        self, **kwargs: Unpack[CreateIntegrationResourcePropertyRequestTypeDef]
    ) -> CreateIntegrationResourcePropertyResponseTypeDef:
        """
        This API can be used for setting up the <code>ResourceProperty</code> of the
        Glue connection (for the source) or Glue database ARN (for the target).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_integration_resource_property.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_integration_resource_property)
        """

    def create_integration_table_properties(
        self, **kwargs: Unpack[CreateIntegrationTablePropertiesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This API is used to provide optional override properties for the the tables
        that need to be replicated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_integration_table_properties.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_integration_table_properties)
        """

    def create_job(self, **kwargs: Unpack[CreateJobRequestTypeDef]) -> CreateJobResponseTypeDef:
        """
        Creates a new job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_job)
        """

    def create_ml_transform(
        self, **kwargs: Unpack[CreateMLTransformRequestTypeDef]
    ) -> CreateMLTransformResponseTypeDef:
        """
        Creates an Glue machine learning transform.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_ml_transform.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_ml_transform)
        """

    def create_partition(self, **kwargs: Unpack[CreatePartitionRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a new partition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_partition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_partition)
        """

    def create_partition_index(
        self, **kwargs: Unpack[CreatePartitionIndexRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a specified partition index in an existing table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_partition_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_partition_index)
        """

    def create_registry(
        self, **kwargs: Unpack[CreateRegistryInputTypeDef]
    ) -> CreateRegistryResponseTypeDef:
        """
        Creates a new registry which may be used to hold a collection of schemas.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_registry.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_registry)
        """

    def create_schema(
        self, **kwargs: Unpack[CreateSchemaInputTypeDef]
    ) -> CreateSchemaResponseTypeDef:
        """
        Creates a new schema set and registers the schema definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_schema)
        """

    def create_script(
        self, **kwargs: Unpack[CreateScriptRequestTypeDef]
    ) -> CreateScriptResponseTypeDef:
        """
        Transforms a directed acyclic graph (DAG) into code.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_script.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_script)
        """

    def create_security_configuration(
        self, **kwargs: Unpack[CreateSecurityConfigurationRequestTypeDef]
    ) -> CreateSecurityConfigurationResponseTypeDef:
        """
        Creates a new security configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_security_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_security_configuration)
        """

    def create_session(
        self, **kwargs: Unpack[CreateSessionRequestTypeDef]
    ) -> CreateSessionResponseTypeDef:
        """
        Creates a new session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_session)
        """

    def create_table(self, **kwargs: Unpack[CreateTableRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a new table definition in the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_table)
        """

    def create_table_optimizer(
        self, **kwargs: Unpack[CreateTableOptimizerRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a new table optimizer for a specific function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_table_optimizer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_table_optimizer)
        """

    def create_trigger(
        self, **kwargs: Unpack[CreateTriggerRequestTypeDef]
    ) -> CreateTriggerResponseTypeDef:
        """
        Creates a new trigger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_trigger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_trigger)
        """

    def create_usage_profile(
        self, **kwargs: Unpack[CreateUsageProfileRequestTypeDef]
    ) -> CreateUsageProfileResponseTypeDef:
        """
        Creates an Glue usage profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_usage_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_usage_profile)
        """

    def create_user_defined_function(
        self, **kwargs: Unpack[CreateUserDefinedFunctionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a new function definition in the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_user_defined_function.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_user_defined_function)
        """

    def create_workflow(
        self, **kwargs: Unpack[CreateWorkflowRequestTypeDef]
    ) -> CreateWorkflowResponseTypeDef:
        """
        Creates a new workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/create_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#create_workflow)
        """

    def delete_blueprint(
        self, **kwargs: Unpack[DeleteBlueprintRequestTypeDef]
    ) -> DeleteBlueprintResponseTypeDef:
        """
        Deletes an existing blueprint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_blueprint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_blueprint)
        """

    def delete_catalog(self, **kwargs: Unpack[DeleteCatalogRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified catalog from the Glue Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_catalog.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_catalog)
        """

    def delete_classifier(self, **kwargs: Unpack[DeleteClassifierRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a classifier from the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_classifier.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_classifier)
        """

    def delete_column_statistics_for_partition(
        self, **kwargs: Unpack[DeleteColumnStatisticsForPartitionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete the partition column statistics of a column.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_column_statistics_for_partition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_column_statistics_for_partition)
        """

    def delete_column_statistics_for_table(
        self, **kwargs: Unpack[DeleteColumnStatisticsForTableRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Retrieves table statistics of columns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_column_statistics_for_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_column_statistics_for_table)
        """

    def delete_column_statistics_task_settings(
        self, **kwargs: Unpack[DeleteColumnStatisticsTaskSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes settings for a column statistics task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_column_statistics_task_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_column_statistics_task_settings)
        """

    def delete_connection(self, **kwargs: Unpack[DeleteConnectionRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a connection from the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_connection)
        """

    def delete_crawler(self, **kwargs: Unpack[DeleteCrawlerRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a specified crawler from the Glue Data Catalog, unless the crawler
        state is <code>RUNNING</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_crawler.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_crawler)
        """

    def delete_custom_entity_type(
        self, **kwargs: Unpack[DeleteCustomEntityTypeRequestTypeDef]
    ) -> DeleteCustomEntityTypeResponseTypeDef:
        """
        Deletes a custom pattern by specifying its name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_custom_entity_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_custom_entity_type)
        """

    def delete_data_quality_ruleset(
        self, **kwargs: Unpack[DeleteDataQualityRulesetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a data quality ruleset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_data_quality_ruleset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_data_quality_ruleset)
        """

    def delete_database(self, **kwargs: Unpack[DeleteDatabaseRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a specified database from a Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_database)
        """

    def delete_dev_endpoint(
        self, **kwargs: Unpack[DeleteDevEndpointRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a specified development endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_dev_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_dev_endpoint)
        """

    def delete_integration(
        self, **kwargs: Unpack[DeleteIntegrationRequestTypeDef]
    ) -> DeleteIntegrationResponseTypeDef:
        """
        Deletes the specified Zero-ETL integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_integration)
        """

    def delete_integration_table_properties(
        self, **kwargs: Unpack[DeleteIntegrationTablePropertiesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the table properties that have been created for the tables that need to
        be replicated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_integration_table_properties.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_integration_table_properties)
        """

    def delete_job(self, **kwargs: Unpack[DeleteJobRequestTypeDef]) -> DeleteJobResponseTypeDef:
        """
        Deletes a specified job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_job)
        """

    def delete_ml_transform(
        self, **kwargs: Unpack[DeleteMLTransformRequestTypeDef]
    ) -> DeleteMLTransformResponseTypeDef:
        """
        Deletes an Glue machine learning transform.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_ml_transform.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_ml_transform)
        """

    def delete_partition(self, **kwargs: Unpack[DeletePartitionRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a specified partition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_partition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_partition)
        """

    def delete_partition_index(
        self, **kwargs: Unpack[DeletePartitionIndexRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a specified partition index from an existing table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_partition_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_partition_index)
        """

    def delete_registry(
        self, **kwargs: Unpack[DeleteRegistryInputTypeDef]
    ) -> DeleteRegistryResponseTypeDef:
        """
        Delete the entire registry including schema and all of its versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_registry.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_registry)
        """

    def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a specified policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_resource_policy)
        """

    def delete_schema(
        self, **kwargs: Unpack[DeleteSchemaInputTypeDef]
    ) -> DeleteSchemaResponseTypeDef:
        """
        Deletes the entire schema set, including the schema set and all of its versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_schema)
        """

    def delete_schema_versions(
        self, **kwargs: Unpack[DeleteSchemaVersionsInputTypeDef]
    ) -> DeleteSchemaVersionsResponseTypeDef:
        """
        Remove versions from the specified schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_schema_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_schema_versions)
        """

    def delete_security_configuration(
        self, **kwargs: Unpack[DeleteSecurityConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a specified security configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_security_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_security_configuration)
        """

    def delete_session(
        self, **kwargs: Unpack[DeleteSessionRequestTypeDef]
    ) -> DeleteSessionResponseTypeDef:
        """
        Deletes the session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_session)
        """

    def delete_table(self, **kwargs: Unpack[DeleteTableRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a table definition from the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_table)
        """

    def delete_table_optimizer(
        self, **kwargs: Unpack[DeleteTableOptimizerRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an optimizer and all associated metadata for a table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_table_optimizer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_table_optimizer)
        """

    def delete_table_version(
        self, **kwargs: Unpack[DeleteTableVersionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a specified version of a table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_table_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_table_version)
        """

    def delete_trigger(
        self, **kwargs: Unpack[DeleteTriggerRequestTypeDef]
    ) -> DeleteTriggerResponseTypeDef:
        """
        Deletes a specified trigger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_trigger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_trigger)
        """

    def delete_usage_profile(
        self, **kwargs: Unpack[DeleteUsageProfileRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the Glue specified usage profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_usage_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_usage_profile)
        """

    def delete_user_defined_function(
        self, **kwargs: Unpack[DeleteUserDefinedFunctionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an existing function definition from the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_user_defined_function.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_user_defined_function)
        """

    def delete_workflow(
        self, **kwargs: Unpack[DeleteWorkflowRequestTypeDef]
    ) -> DeleteWorkflowResponseTypeDef:
        """
        Deletes a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/delete_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#delete_workflow)
        """

    def describe_connection_type(
        self, **kwargs: Unpack[DescribeConnectionTypeRequestTypeDef]
    ) -> DescribeConnectionTypeResponseTypeDef:
        """
        The <code>DescribeConnectionType</code> API provides full details of the
        supported options for a given connection type in Glue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/describe_connection_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#describe_connection_type)
        """

    def describe_entity(
        self, **kwargs: Unpack[DescribeEntityRequestTypeDef]
    ) -> DescribeEntityResponseTypeDef:
        """
        Provides details regarding the entity used with the connection type, with a
        description of the data model for each field in the selected entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/describe_entity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#describe_entity)
        """

    def describe_inbound_integrations(
        self, **kwargs: Unpack[DescribeInboundIntegrationsRequestTypeDef]
    ) -> DescribeInboundIntegrationsResponseTypeDef:
        """
        Returns a list of inbound integrations for the specified integration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/describe_inbound_integrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#describe_inbound_integrations)
        """

    def describe_integrations(
        self, **kwargs: Unpack[DescribeIntegrationsRequestTypeDef]
    ) -> DescribeIntegrationsResponseTypeDef:
        """
        The API is used to retrieve a list of integrations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/describe_integrations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#describe_integrations)
        """

    def get_blueprint(
        self, **kwargs: Unpack[GetBlueprintRequestTypeDef]
    ) -> GetBlueprintResponseTypeDef:
        """
        Retrieves the details of a blueprint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_blueprint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_blueprint)
        """

    def get_blueprint_run(
        self, **kwargs: Unpack[GetBlueprintRunRequestTypeDef]
    ) -> GetBlueprintRunResponseTypeDef:
        """
        Retrieves the details of a blueprint run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_blueprint_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_blueprint_run)
        """

    def get_blueprint_runs(
        self, **kwargs: Unpack[GetBlueprintRunsRequestTypeDef]
    ) -> GetBlueprintRunsResponseTypeDef:
        """
        Retrieves the details of blueprint runs for a specified blueprint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_blueprint_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_blueprint_runs)
        """

    def get_catalog(self, **kwargs: Unpack[GetCatalogRequestTypeDef]) -> GetCatalogResponseTypeDef:
        """
        The name of the Catalog to retrieve.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_catalog.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_catalog)
        """

    def get_catalog_import_status(
        self, **kwargs: Unpack[GetCatalogImportStatusRequestTypeDef]
    ) -> GetCatalogImportStatusResponseTypeDef:
        """
        Retrieves the status of a migration operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_catalog_import_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_catalog_import_status)
        """

    def get_catalogs(
        self, **kwargs: Unpack[GetCatalogsRequestTypeDef]
    ) -> GetCatalogsResponseTypeDef:
        """
        Retrieves all catalogs defined in a catalog in the Glue Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_catalogs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_catalogs)
        """

    def get_classifier(
        self, **kwargs: Unpack[GetClassifierRequestTypeDef]
    ) -> GetClassifierResponseTypeDef:
        """
        Retrieve a classifier by name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_classifier.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_classifier)
        """

    def get_classifiers(
        self, **kwargs: Unpack[GetClassifiersRequestTypeDef]
    ) -> GetClassifiersResponseTypeDef:
        """
        Lists all classifier objects in the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_classifiers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_classifiers)
        """

    def get_column_statistics_for_partition(
        self, **kwargs: Unpack[GetColumnStatisticsForPartitionRequestTypeDef]
    ) -> GetColumnStatisticsForPartitionResponseTypeDef:
        """
        Retrieves partition statistics of columns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_column_statistics_for_partition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_column_statistics_for_partition)
        """

    def get_column_statistics_for_table(
        self, **kwargs: Unpack[GetColumnStatisticsForTableRequestTypeDef]
    ) -> GetColumnStatisticsForTableResponseTypeDef:
        """
        Retrieves table statistics of columns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_column_statistics_for_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_column_statistics_for_table)
        """

    def get_column_statistics_task_run(
        self, **kwargs: Unpack[GetColumnStatisticsTaskRunRequestTypeDef]
    ) -> GetColumnStatisticsTaskRunResponseTypeDef:
        """
        Get the associated metadata/information for a task run, given a task run ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_column_statistics_task_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_column_statistics_task_run)
        """

    def get_column_statistics_task_runs(
        self, **kwargs: Unpack[GetColumnStatisticsTaskRunsRequestTypeDef]
    ) -> GetColumnStatisticsTaskRunsResponseTypeDef:
        """
        Retrieves information about all runs associated with the specified table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_column_statistics_task_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_column_statistics_task_runs)
        """

    def get_column_statistics_task_settings(
        self, **kwargs: Unpack[GetColumnStatisticsTaskSettingsRequestTypeDef]
    ) -> GetColumnStatisticsTaskSettingsResponseTypeDef:
        """
        Gets settings for a column statistics task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_column_statistics_task_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_column_statistics_task_settings)
        """

    def get_connection(
        self, **kwargs: Unpack[GetConnectionRequestTypeDef]
    ) -> GetConnectionResponseTypeDef:
        """
        Retrieves a connection definition from the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_connection)
        """

    def get_connections(
        self, **kwargs: Unpack[GetConnectionsRequestTypeDef]
    ) -> GetConnectionsResponseTypeDef:
        """
        Retrieves a list of connection definitions from the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_connections)
        """

    def get_crawler(self, **kwargs: Unpack[GetCrawlerRequestTypeDef]) -> GetCrawlerResponseTypeDef:
        """
        Retrieves metadata for a specified crawler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_crawler.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_crawler)
        """

    def get_crawler_metrics(
        self, **kwargs: Unpack[GetCrawlerMetricsRequestTypeDef]
    ) -> GetCrawlerMetricsResponseTypeDef:
        """
        Retrieves metrics about specified crawlers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_crawler_metrics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_crawler_metrics)
        """

    def get_crawlers(
        self, **kwargs: Unpack[GetCrawlersRequestTypeDef]
    ) -> GetCrawlersResponseTypeDef:
        """
        Retrieves metadata for all crawlers defined in the customer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_crawlers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_crawlers)
        """

    def get_custom_entity_type(
        self, **kwargs: Unpack[GetCustomEntityTypeRequestTypeDef]
    ) -> GetCustomEntityTypeResponseTypeDef:
        """
        Retrieves the details of a custom pattern by specifying its name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_custom_entity_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_custom_entity_type)
        """

    def get_data_catalog_encryption_settings(
        self, **kwargs: Unpack[GetDataCatalogEncryptionSettingsRequestTypeDef]
    ) -> GetDataCatalogEncryptionSettingsResponseTypeDef:
        """
        Retrieves the security configuration for a specified catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_data_catalog_encryption_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_data_catalog_encryption_settings)
        """

    def get_data_quality_model(
        self, **kwargs: Unpack[GetDataQualityModelRequestTypeDef]
    ) -> GetDataQualityModelResponseTypeDef:
        """
        Retrieve the training status of the model along with more information
        (CompletedOn, StartedOn, FailureReason).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_data_quality_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_data_quality_model)
        """

    def get_data_quality_model_result(
        self, **kwargs: Unpack[GetDataQualityModelResultRequestTypeDef]
    ) -> GetDataQualityModelResultResponseTypeDef:
        """
        Retrieve a statistic's predictions for a given Profile ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_data_quality_model_result.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_data_quality_model_result)
        """

    def get_data_quality_result(
        self, **kwargs: Unpack[GetDataQualityResultRequestTypeDef]
    ) -> GetDataQualityResultResponseTypeDef:
        """
        Retrieves the result of a data quality rule evaluation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_data_quality_result.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_data_quality_result)
        """

    def get_data_quality_rule_recommendation_run(
        self, **kwargs: Unpack[GetDataQualityRuleRecommendationRunRequestTypeDef]
    ) -> GetDataQualityRuleRecommendationRunResponseTypeDef:
        """
        Gets the specified recommendation run that was used to generate rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_data_quality_rule_recommendation_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_data_quality_rule_recommendation_run)
        """

    def get_data_quality_ruleset(
        self, **kwargs: Unpack[GetDataQualityRulesetRequestTypeDef]
    ) -> GetDataQualityRulesetResponseTypeDef:
        """
        Returns an existing ruleset by identifier or name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_data_quality_ruleset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_data_quality_ruleset)
        """

    def get_data_quality_ruleset_evaluation_run(
        self, **kwargs: Unpack[GetDataQualityRulesetEvaluationRunRequestTypeDef]
    ) -> GetDataQualityRulesetEvaluationRunResponseTypeDef:
        """
        Retrieves a specific run where a ruleset is evaluated against a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_data_quality_ruleset_evaluation_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_data_quality_ruleset_evaluation_run)
        """

    def get_database(
        self, **kwargs: Unpack[GetDatabaseRequestTypeDef]
    ) -> GetDatabaseResponseTypeDef:
        """
        Retrieves the definition of a specified database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_database)
        """

    def get_databases(
        self, **kwargs: Unpack[GetDatabasesRequestTypeDef]
    ) -> GetDatabasesResponseTypeDef:
        """
        Retrieves all databases defined in a given Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_databases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_databases)
        """

    def get_dataflow_graph(
        self, **kwargs: Unpack[GetDataflowGraphRequestTypeDef]
    ) -> GetDataflowGraphResponseTypeDef:
        """
        Transforms a Python script into a directed acyclic graph (DAG).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_dataflow_graph.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_dataflow_graph)
        """

    def get_dev_endpoint(
        self, **kwargs: Unpack[GetDevEndpointRequestTypeDef]
    ) -> GetDevEndpointResponseTypeDef:
        """
        Retrieves information about a specified development endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_dev_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_dev_endpoint)
        """

    def get_dev_endpoints(
        self, **kwargs: Unpack[GetDevEndpointsRequestTypeDef]
    ) -> GetDevEndpointsResponseTypeDef:
        """
        Retrieves all the development endpoints in this Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_dev_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_dev_endpoints)
        """

    def get_entity_records(
        self, **kwargs: Unpack[GetEntityRecordsRequestTypeDef]
    ) -> GetEntityRecordsResponseTypeDef:
        """
        This API is used to query preview data from a given connection type or from a
        native Amazon S3 based Glue Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_entity_records.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_entity_records)
        """

    def get_integration_resource_property(
        self, **kwargs: Unpack[GetIntegrationResourcePropertyRequestTypeDef]
    ) -> GetIntegrationResourcePropertyResponseTypeDef:
        """
        This API is used for fetching the <code>ResourceProperty</code> of the Glue
        connection (for the source) or Glue database ARN (for the target).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_integration_resource_property.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_integration_resource_property)
        """

    def get_integration_table_properties(
        self, **kwargs: Unpack[GetIntegrationTablePropertiesRequestTypeDef]
    ) -> GetIntegrationTablePropertiesResponseTypeDef:
        """
        This API is used to retrieve optional override properties for the tables that
        need to be replicated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_integration_table_properties.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_integration_table_properties)
        """

    def get_job(self, **kwargs: Unpack[GetJobRequestTypeDef]) -> GetJobResponseTypeDef:
        """
        Retrieves an existing job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_job)
        """

    def get_job_bookmark(
        self, **kwargs: Unpack[GetJobBookmarkRequestTypeDef]
    ) -> GetJobBookmarkResponseTypeDef:
        """
        Returns information on a job bookmark entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_job_bookmark.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_job_bookmark)
        """

    def get_job_run(self, **kwargs: Unpack[GetJobRunRequestTypeDef]) -> GetJobRunResponseTypeDef:
        """
        Retrieves the metadata for a given job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_job_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_job_run)
        """

    def get_job_runs(self, **kwargs: Unpack[GetJobRunsRequestTypeDef]) -> GetJobRunsResponseTypeDef:
        """
        Retrieves metadata for all runs of a given job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_job_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_job_runs)
        """

    def get_jobs(self, **kwargs: Unpack[GetJobsRequestTypeDef]) -> GetJobsResponseTypeDef:
        """
        Retrieves all current job definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_jobs)
        """

    def get_ml_task_run(
        self, **kwargs: Unpack[GetMLTaskRunRequestTypeDef]
    ) -> GetMLTaskRunResponseTypeDef:
        """
        Gets details for a specific task run on a machine learning transform.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_ml_task_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_ml_task_run)
        """

    def get_ml_task_runs(
        self, **kwargs: Unpack[GetMLTaskRunsRequestTypeDef]
    ) -> GetMLTaskRunsResponseTypeDef:
        """
        Gets a list of runs for a machine learning transform.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_ml_task_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_ml_task_runs)
        """

    def get_ml_transform(
        self, **kwargs: Unpack[GetMLTransformRequestTypeDef]
    ) -> GetMLTransformResponseTypeDef:
        """
        Gets an Glue machine learning transform artifact and all its corresponding
        metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_ml_transform.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_ml_transform)
        """

    def get_ml_transforms(
        self, **kwargs: Unpack[GetMLTransformsRequestTypeDef]
    ) -> GetMLTransformsResponseTypeDef:
        """
        Gets a sortable, filterable list of existing Glue machine learning transforms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_ml_transforms.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_ml_transforms)
        """

    def get_mapping(self, **kwargs: Unpack[GetMappingRequestTypeDef]) -> GetMappingResponseTypeDef:
        """
        Creates mappings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_mapping.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_mapping)
        """

    def get_partition(
        self, **kwargs: Unpack[GetPartitionRequestTypeDef]
    ) -> GetPartitionResponseTypeDef:
        """
        Retrieves information about a specified partition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_partition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_partition)
        """

    def get_partition_indexes(
        self, **kwargs: Unpack[GetPartitionIndexesRequestTypeDef]
    ) -> GetPartitionIndexesResponseTypeDef:
        """
        Retrieves the partition indexes associated with a table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_partition_indexes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_partition_indexes)
        """

    def get_partitions(
        self, **kwargs: Unpack[GetPartitionsRequestTypeDef]
    ) -> GetPartitionsResponseTypeDef:
        """
        Retrieves information about the partitions in a table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_partitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_partitions)
        """

    def get_plan(self, **kwargs: Unpack[GetPlanRequestTypeDef]) -> GetPlanResponseTypeDef:
        """
        Gets code to perform a specified mapping.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_plan)
        """

    def get_registry(self, **kwargs: Unpack[GetRegistryInputTypeDef]) -> GetRegistryResponseTypeDef:
        """
        Describes the specified registry in detail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_registry.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_registry)
        """

    def get_resource_policies(
        self, **kwargs: Unpack[GetResourcePoliciesRequestTypeDef]
    ) -> GetResourcePoliciesResponseTypeDef:
        """
        Retrieves the resource policies set on individual resources by Resource Access
        Manager during cross-account permission grants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_resource_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_resource_policies)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyRequestTypeDef]
    ) -> GetResourcePolicyResponseTypeDef:
        """
        Retrieves a specified resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_resource_policy)
        """

    def get_schema(self, **kwargs: Unpack[GetSchemaInputTypeDef]) -> GetSchemaResponseTypeDef:
        """
        Describes the specified schema in detail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_schema)
        """

    def get_schema_by_definition(
        self, **kwargs: Unpack[GetSchemaByDefinitionInputTypeDef]
    ) -> GetSchemaByDefinitionResponseTypeDef:
        """
        Retrieves a schema by the <code>SchemaDefinition</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_schema_by_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_schema_by_definition)
        """

    def get_schema_version(
        self, **kwargs: Unpack[GetSchemaVersionInputTypeDef]
    ) -> GetSchemaVersionResponseTypeDef:
        """
        Get the specified schema by its unique ID assigned when a version of the schema
        is created or registered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_schema_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_schema_version)
        """

    def get_schema_versions_diff(
        self, **kwargs: Unpack[GetSchemaVersionsDiffInputTypeDef]
    ) -> GetSchemaVersionsDiffResponseTypeDef:
        """
        Fetches the schema version difference in the specified difference type between
        two stored schema versions in the Schema Registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_schema_versions_diff.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_schema_versions_diff)
        """

    def get_security_configuration(
        self, **kwargs: Unpack[GetSecurityConfigurationRequestTypeDef]
    ) -> GetSecurityConfigurationResponseTypeDef:
        """
        Retrieves a specified security configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_security_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_security_configuration)
        """

    def get_security_configurations(
        self, **kwargs: Unpack[GetSecurityConfigurationsRequestTypeDef]
    ) -> GetSecurityConfigurationsResponseTypeDef:
        """
        Retrieves a list of all security configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_security_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_security_configurations)
        """

    def get_session(self, **kwargs: Unpack[GetSessionRequestTypeDef]) -> GetSessionResponseTypeDef:
        """
        Retrieves the session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_session)
        """

    def get_statement(
        self, **kwargs: Unpack[GetStatementRequestTypeDef]
    ) -> GetStatementResponseTypeDef:
        """
        Retrieves the statement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_statement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_statement)
        """

    def get_table(self, **kwargs: Unpack[GetTableRequestTypeDef]) -> GetTableResponseTypeDef:
        """
        Retrieves the <code>Table</code> definition in a Data Catalog for a specified
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_table)
        """

    def get_table_optimizer(
        self, **kwargs: Unpack[GetTableOptimizerRequestTypeDef]
    ) -> GetTableOptimizerResponseTypeDef:
        """
        Returns the configuration of all optimizers associated with a specified table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_table_optimizer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_table_optimizer)
        """

    def get_table_version(
        self, **kwargs: Unpack[GetTableVersionRequestTypeDef]
    ) -> GetTableVersionResponseTypeDef:
        """
        Retrieves a specified version of a table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_table_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_table_version)
        """

    def get_table_versions(
        self, **kwargs: Unpack[GetTableVersionsRequestTypeDef]
    ) -> GetTableVersionsResponseTypeDef:
        """
        Retrieves a list of strings that identify available versions of a specified
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_table_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_table_versions)
        """

    def get_tables(self, **kwargs: Unpack[GetTablesRequestTypeDef]) -> GetTablesResponseTypeDef:
        """
        Retrieves the definitions of some or all of the tables in a given
        <code>Database</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_tables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_tables)
        """

    def get_tags(self, **kwargs: Unpack[GetTagsRequestTypeDef]) -> GetTagsResponseTypeDef:
        """
        Retrieves a list of tags associated with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_tags)
        """

    def get_trigger(self, **kwargs: Unpack[GetTriggerRequestTypeDef]) -> GetTriggerResponseTypeDef:
        """
        Retrieves the definition of a trigger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_trigger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_trigger)
        """

    def get_triggers(
        self, **kwargs: Unpack[GetTriggersRequestTypeDef]
    ) -> GetTriggersResponseTypeDef:
        """
        Gets all the triggers associated with a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_triggers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_triggers)
        """

    def get_unfiltered_partition_metadata(
        self, **kwargs: Unpack[GetUnfilteredPartitionMetadataRequestTypeDef]
    ) -> GetUnfilteredPartitionMetadataResponseTypeDef:
        """
        Retrieves partition metadata from the Data Catalog that contains unfiltered
        metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_unfiltered_partition_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_unfiltered_partition_metadata)
        """

    def get_unfiltered_partitions_metadata(
        self, **kwargs: Unpack[GetUnfilteredPartitionsMetadataRequestTypeDef]
    ) -> GetUnfilteredPartitionsMetadataResponseTypeDef:
        """
        Retrieves partition metadata from the Data Catalog that contains unfiltered
        metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_unfiltered_partitions_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_unfiltered_partitions_metadata)
        """

    def get_unfiltered_table_metadata(
        self, **kwargs: Unpack[GetUnfilteredTableMetadataRequestTypeDef]
    ) -> GetUnfilteredTableMetadataResponseTypeDef:
        """
        Allows a third-party analytical engine to retrieve unfiltered table metadata
        from the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_unfiltered_table_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_unfiltered_table_metadata)
        """

    def get_usage_profile(
        self, **kwargs: Unpack[GetUsageProfileRequestTypeDef]
    ) -> GetUsageProfileResponseTypeDef:
        """
        Retrieves information about the specified Glue usage profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_usage_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_usage_profile)
        """

    def get_user_defined_function(
        self, **kwargs: Unpack[GetUserDefinedFunctionRequestTypeDef]
    ) -> GetUserDefinedFunctionResponseTypeDef:
        """
        Retrieves a specified function definition from the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_user_defined_function.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_user_defined_function)
        """

    def get_user_defined_functions(
        self, **kwargs: Unpack[GetUserDefinedFunctionsRequestTypeDef]
    ) -> GetUserDefinedFunctionsResponseTypeDef:
        """
        Retrieves multiple function definitions from the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_user_defined_functions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_user_defined_functions)
        """

    def get_workflow(
        self, **kwargs: Unpack[GetWorkflowRequestTypeDef]
    ) -> GetWorkflowResponseTypeDef:
        """
        Retrieves resource metadata for a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_workflow)
        """

    def get_workflow_run(
        self, **kwargs: Unpack[GetWorkflowRunRequestTypeDef]
    ) -> GetWorkflowRunResponseTypeDef:
        """
        Retrieves the metadata for a given workflow run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_workflow_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_workflow_run)
        """

    def get_workflow_run_properties(
        self, **kwargs: Unpack[GetWorkflowRunPropertiesRequestTypeDef]
    ) -> GetWorkflowRunPropertiesResponseTypeDef:
        """
        Retrieves the workflow run properties which were set during the run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_workflow_run_properties.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_workflow_run_properties)
        """

    def get_workflow_runs(
        self, **kwargs: Unpack[GetWorkflowRunsRequestTypeDef]
    ) -> GetWorkflowRunsResponseTypeDef:
        """
        Retrieves metadata for all runs of a given workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_workflow_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_workflow_runs)
        """

    def import_catalog_to_glue(
        self, **kwargs: Unpack[ImportCatalogToGlueRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Imports an existing Amazon Athena Data Catalog to Glue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/import_catalog_to_glue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#import_catalog_to_glue)
        """

    def list_blueprints(
        self, **kwargs: Unpack[ListBlueprintsRequestTypeDef]
    ) -> ListBlueprintsResponseTypeDef:
        """
        Lists all the blueprint names in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_blueprints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_blueprints)
        """

    def list_column_statistics_task_runs(
        self, **kwargs: Unpack[ListColumnStatisticsTaskRunsRequestTypeDef]
    ) -> ListColumnStatisticsTaskRunsResponseTypeDef:
        """
        List all task runs for a particular account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_column_statistics_task_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_column_statistics_task_runs)
        """

    def list_connection_types(
        self, **kwargs: Unpack[ListConnectionTypesRequestTypeDef]
    ) -> ListConnectionTypesResponseTypeDef:
        """
        The <code>ListConnectionTypes</code> API provides a discovery mechanism to
        learn available connection types in Glue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_connection_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_connection_types)
        """

    def list_crawlers(
        self, **kwargs: Unpack[ListCrawlersRequestTypeDef]
    ) -> ListCrawlersResponseTypeDef:
        """
        Retrieves the names of all crawler resources in this Amazon Web Services
        account, or the resources with the specified tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_crawlers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_crawlers)
        """

    def list_crawls(self, **kwargs: Unpack[ListCrawlsRequestTypeDef]) -> ListCrawlsResponseTypeDef:
        """
        Returns all the crawls of a specified crawler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_crawls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_crawls)
        """

    def list_custom_entity_types(
        self, **kwargs: Unpack[ListCustomEntityTypesRequestTypeDef]
    ) -> ListCustomEntityTypesResponseTypeDef:
        """
        Lists all the custom patterns that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_custom_entity_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_custom_entity_types)
        """

    def list_data_quality_results(
        self, **kwargs: Unpack[ListDataQualityResultsRequestTypeDef]
    ) -> ListDataQualityResultsResponseTypeDef:
        """
        Returns all data quality execution results for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_data_quality_results.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_data_quality_results)
        """

    def list_data_quality_rule_recommendation_runs(
        self, **kwargs: Unpack[ListDataQualityRuleRecommendationRunsRequestTypeDef]
    ) -> ListDataQualityRuleRecommendationRunsResponseTypeDef:
        """
        Lists the recommendation runs meeting the filter criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_data_quality_rule_recommendation_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_data_quality_rule_recommendation_runs)
        """

    def list_data_quality_ruleset_evaluation_runs(
        self, **kwargs: Unpack[ListDataQualityRulesetEvaluationRunsRequestTypeDef]
    ) -> ListDataQualityRulesetEvaluationRunsResponseTypeDef:
        """
        Lists all the runs meeting the filter criteria, where a ruleset is evaluated
        against a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_data_quality_ruleset_evaluation_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_data_quality_ruleset_evaluation_runs)
        """

    def list_data_quality_rulesets(
        self, **kwargs: Unpack[ListDataQualityRulesetsRequestTypeDef]
    ) -> ListDataQualityRulesetsResponseTypeDef:
        """
        Returns a paginated list of rulesets for the specified list of Glue tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_data_quality_rulesets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_data_quality_rulesets)
        """

    def list_data_quality_statistic_annotations(
        self, **kwargs: Unpack[ListDataQualityStatisticAnnotationsRequestTypeDef]
    ) -> ListDataQualityStatisticAnnotationsResponseTypeDef:
        """
        Retrieve annotations for a data quality statistic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_data_quality_statistic_annotations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_data_quality_statistic_annotations)
        """

    def list_data_quality_statistics(
        self, **kwargs: Unpack[ListDataQualityStatisticsRequestTypeDef]
    ) -> ListDataQualityStatisticsResponseTypeDef:
        """
        Retrieves a list of data quality statistics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_data_quality_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_data_quality_statistics)
        """

    def list_dev_endpoints(
        self, **kwargs: Unpack[ListDevEndpointsRequestTypeDef]
    ) -> ListDevEndpointsResponseTypeDef:
        """
        Retrieves the names of all <code>DevEndpoint</code> resources in this Amazon
        Web Services account, or the resources with the specified tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_dev_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_dev_endpoints)
        """

    def list_entities(
        self, **kwargs: Unpack[ListEntitiesRequestTypeDef]
    ) -> ListEntitiesResponseTypeDef:
        """
        Returns the available entities supported by the connection type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_entities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_entities)
        """

    def list_jobs(self, **kwargs: Unpack[ListJobsRequestTypeDef]) -> ListJobsResponseTypeDef:
        """
        Retrieves the names of all job resources in this Amazon Web Services account,
        or the resources with the specified tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_jobs)
        """

    def list_ml_transforms(
        self, **kwargs: Unpack[ListMLTransformsRequestTypeDef]
    ) -> ListMLTransformsResponseTypeDef:
        """
        Retrieves a sortable, filterable list of existing Glue machine learning
        transforms in this Amazon Web Services account, or the resources with the
        specified tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_ml_transforms.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_ml_transforms)
        """

    def list_registries(
        self, **kwargs: Unpack[ListRegistriesInputTypeDef]
    ) -> ListRegistriesResponseTypeDef:
        """
        Returns a list of registries that you have created, with minimal registry
        information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_registries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_registries)
        """

    def list_schema_versions(
        self, **kwargs: Unpack[ListSchemaVersionsInputTypeDef]
    ) -> ListSchemaVersionsResponseTypeDef:
        """
        Returns a list of schema versions that you have created, with minimal
        information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_schema_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_schema_versions)
        """

    def list_schemas(self, **kwargs: Unpack[ListSchemasInputTypeDef]) -> ListSchemasResponseTypeDef:
        """
        Returns a list of schemas with minimal details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_schemas.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_schemas)
        """

    def list_sessions(
        self, **kwargs: Unpack[ListSessionsRequestTypeDef]
    ) -> ListSessionsResponseTypeDef:
        """
        Retrieve a list of sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_sessions)
        """

    def list_statements(
        self, **kwargs: Unpack[ListStatementsRequestTypeDef]
    ) -> ListStatementsResponseTypeDef:
        """
        Lists statements for the session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_statements.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_statements)
        """

    def list_table_optimizer_runs(
        self, **kwargs: Unpack[ListTableOptimizerRunsRequestTypeDef]
    ) -> ListTableOptimizerRunsResponseTypeDef:
        """
        Lists the history of previous optimizer runs for a specific table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_table_optimizer_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_table_optimizer_runs)
        """

    def list_triggers(
        self, **kwargs: Unpack[ListTriggersRequestTypeDef]
    ) -> ListTriggersResponseTypeDef:
        """
        Retrieves the names of all trigger resources in this Amazon Web Services
        account, or the resources with the specified tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_triggers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_triggers)
        """

    def list_usage_profiles(
        self, **kwargs: Unpack[ListUsageProfilesRequestTypeDef]
    ) -> ListUsageProfilesResponseTypeDef:
        """
        List all the Glue usage profiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_usage_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_usage_profiles)
        """

    def list_workflows(
        self, **kwargs: Unpack[ListWorkflowsRequestTypeDef]
    ) -> ListWorkflowsResponseTypeDef:
        """
        Lists names of workflows created in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/list_workflows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#list_workflows)
        """

    def modify_integration(
        self, **kwargs: Unpack[ModifyIntegrationRequestTypeDef]
    ) -> ModifyIntegrationResponseTypeDef:
        """
        Modifies a Zero-ETL integration in the caller's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/modify_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#modify_integration)
        """

    def put_data_catalog_encryption_settings(
        self, **kwargs: Unpack[PutDataCatalogEncryptionSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sets the security configuration for a specified catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/put_data_catalog_encryption_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#put_data_catalog_encryption_settings)
        """

    def put_data_quality_profile_annotation(
        self, **kwargs: Unpack[PutDataQualityProfileAnnotationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Annotate all datapoints for a Profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/put_data_quality_profile_annotation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#put_data_quality_profile_annotation)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestTypeDef]
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Sets the Data Catalog resource policy for access control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/put_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#put_resource_policy)
        """

    def put_schema_version_metadata(
        self, **kwargs: Unpack[PutSchemaVersionMetadataInputTypeDef]
    ) -> PutSchemaVersionMetadataResponseTypeDef:
        """
        Puts the metadata key value pair for a specified schema version ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/put_schema_version_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#put_schema_version_metadata)
        """

    def put_workflow_run_properties(
        self, **kwargs: Unpack[PutWorkflowRunPropertiesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Puts the specified workflow run properties for the given workflow run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/put_workflow_run_properties.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#put_workflow_run_properties)
        """

    def query_schema_version_metadata(
        self, **kwargs: Unpack[QuerySchemaVersionMetadataInputTypeDef]
    ) -> QuerySchemaVersionMetadataResponseTypeDef:
        """
        Queries for the schema version metadata information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/query_schema_version_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#query_schema_version_metadata)
        """

    def register_schema_version(
        self, **kwargs: Unpack[RegisterSchemaVersionInputTypeDef]
    ) -> RegisterSchemaVersionResponseTypeDef:
        """
        Adds a new version to the existing schema.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/register_schema_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#register_schema_version)
        """

    def remove_schema_version_metadata(
        self, **kwargs: Unpack[RemoveSchemaVersionMetadataInputTypeDef]
    ) -> RemoveSchemaVersionMetadataResponseTypeDef:
        """
        Removes a key value pair from the schema version metadata for the specified
        schema version ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/remove_schema_version_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#remove_schema_version_metadata)
        """

    def reset_job_bookmark(
        self, **kwargs: Unpack[ResetJobBookmarkRequestTypeDef]
    ) -> ResetJobBookmarkResponseTypeDef:
        """
        Resets a bookmark entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/reset_job_bookmark.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#reset_job_bookmark)
        """

    def resume_workflow_run(
        self, **kwargs: Unpack[ResumeWorkflowRunRequestTypeDef]
    ) -> ResumeWorkflowRunResponseTypeDef:
        """
        Restarts selected nodes of a previous partially completed workflow run and
        resumes the workflow run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/resume_workflow_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#resume_workflow_run)
        """

    def run_statement(
        self, **kwargs: Unpack[RunStatementRequestTypeDef]
    ) -> RunStatementResponseTypeDef:
        """
        Executes the statement.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/run_statement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#run_statement)
        """

    def search_tables(
        self, **kwargs: Unpack[SearchTablesRequestTypeDef]
    ) -> SearchTablesResponseTypeDef:
        """
        Searches a set of tables based on properties in the table metadata as well as
        on the parent database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/search_tables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#search_tables)
        """

    def start_blueprint_run(
        self, **kwargs: Unpack[StartBlueprintRunRequestTypeDef]
    ) -> StartBlueprintRunResponseTypeDef:
        """
        Starts a new run of the specified blueprint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/start_blueprint_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#start_blueprint_run)
        """

    def start_column_statistics_task_run(
        self, **kwargs: Unpack[StartColumnStatisticsTaskRunRequestTypeDef]
    ) -> StartColumnStatisticsTaskRunResponseTypeDef:
        """
        Starts a column statistics task run, for a specified table and columns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/start_column_statistics_task_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#start_column_statistics_task_run)
        """

    def start_column_statistics_task_run_schedule(
        self, **kwargs: Unpack[StartColumnStatisticsTaskRunScheduleRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Starts a column statistics task run schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/start_column_statistics_task_run_schedule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#start_column_statistics_task_run_schedule)
        """

    def start_crawler(self, **kwargs: Unpack[StartCrawlerRequestTypeDef]) -> Dict[str, Any]:
        """
        Starts a crawl using the specified crawler, regardless of what is scheduled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/start_crawler.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#start_crawler)
        """

    def start_crawler_schedule(
        self, **kwargs: Unpack[StartCrawlerScheduleRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Changes the schedule state of the specified crawler to <code>SCHEDULED</code>,
        unless the crawler is already running or the schedule state is already
        <code>SCHEDULED</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/start_crawler_schedule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#start_crawler_schedule)
        """

    def start_data_quality_rule_recommendation_run(
        self, **kwargs: Unpack[StartDataQualityRuleRecommendationRunRequestTypeDef]
    ) -> StartDataQualityRuleRecommendationRunResponseTypeDef:
        """
        Starts a recommendation run that is used to generate rules when you don't know
        what rules to write.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/start_data_quality_rule_recommendation_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#start_data_quality_rule_recommendation_run)
        """

    def start_data_quality_ruleset_evaluation_run(
        self, **kwargs: Unpack[StartDataQualityRulesetEvaluationRunRequestTypeDef]
    ) -> StartDataQualityRulesetEvaluationRunResponseTypeDef:
        """
        Once you have a ruleset definition (either recommended or your own), you call
        this operation to evaluate the ruleset against a data source (Glue table).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/start_data_quality_ruleset_evaluation_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#start_data_quality_ruleset_evaluation_run)
        """

    def start_export_labels_task_run(
        self, **kwargs: Unpack[StartExportLabelsTaskRunRequestTypeDef]
    ) -> StartExportLabelsTaskRunResponseTypeDef:
        """
        Begins an asynchronous task to export all labeled data for a particular
        transform.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/start_export_labels_task_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#start_export_labels_task_run)
        """

    def start_import_labels_task_run(
        self, **kwargs: Unpack[StartImportLabelsTaskRunRequestTypeDef]
    ) -> StartImportLabelsTaskRunResponseTypeDef:
        """
        Enables you to provide additional labels (examples of truth) to be used to
        teach the machine learning transform and improve its quality.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/start_import_labels_task_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#start_import_labels_task_run)
        """

    def start_job_run(
        self, **kwargs: Unpack[StartJobRunRequestTypeDef]
    ) -> StartJobRunResponseTypeDef:
        """
        Starts a job run using a job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/start_job_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#start_job_run)
        """

    def start_ml_evaluation_task_run(
        self, **kwargs: Unpack[StartMLEvaluationTaskRunRequestTypeDef]
    ) -> StartMLEvaluationTaskRunResponseTypeDef:
        """
        Starts a task to estimate the quality of the transform.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/start_ml_evaluation_task_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#start_ml_evaluation_task_run)
        """

    def start_ml_labeling_set_generation_task_run(
        self, **kwargs: Unpack[StartMLLabelingSetGenerationTaskRunRequestTypeDef]
    ) -> StartMLLabelingSetGenerationTaskRunResponseTypeDef:
        """
        Starts the active learning workflow for your machine learning transform to
        improve the transform's quality by generating label sets and adding labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/start_ml_labeling_set_generation_task_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#start_ml_labeling_set_generation_task_run)
        """

    def start_trigger(
        self, **kwargs: Unpack[StartTriggerRequestTypeDef]
    ) -> StartTriggerResponseTypeDef:
        """
        Starts an existing trigger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/start_trigger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#start_trigger)
        """

    def start_workflow_run(
        self, **kwargs: Unpack[StartWorkflowRunRequestTypeDef]
    ) -> StartWorkflowRunResponseTypeDef:
        """
        Starts a new run of the specified workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/start_workflow_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#start_workflow_run)
        """

    def stop_column_statistics_task_run(
        self, **kwargs: Unpack[StopColumnStatisticsTaskRunRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops a task run for the specified table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/stop_column_statistics_task_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#stop_column_statistics_task_run)
        """

    def stop_column_statistics_task_run_schedule(
        self, **kwargs: Unpack[StopColumnStatisticsTaskRunScheduleRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops a column statistics task run schedule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/stop_column_statistics_task_run_schedule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#stop_column_statistics_task_run_schedule)
        """

    def stop_crawler(self, **kwargs: Unpack[StopCrawlerRequestTypeDef]) -> Dict[str, Any]:
        """
        If the specified crawler is running, stops the crawl.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/stop_crawler.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#stop_crawler)
        """

    def stop_crawler_schedule(
        self, **kwargs: Unpack[StopCrawlerScheduleRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sets the schedule state of the specified crawler to <code>NOT_SCHEDULED</code>,
        but does not stop the crawler if it is already running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/stop_crawler_schedule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#stop_crawler_schedule)
        """

    def stop_session(
        self, **kwargs: Unpack[StopSessionRequestTypeDef]
    ) -> StopSessionResponseTypeDef:
        """
        Stops the session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/stop_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#stop_session)
        """

    def stop_trigger(
        self, **kwargs: Unpack[StopTriggerRequestTypeDef]
    ) -> StopTriggerResponseTypeDef:
        """
        Stops a specified trigger.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/stop_trigger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#stop_trigger)
        """

    def stop_workflow_run(self, **kwargs: Unpack[StopWorkflowRunRequestTypeDef]) -> Dict[str, Any]:
        """
        Stops the execution of the specified workflow run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/stop_workflow_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#stop_workflow_run)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#tag_resource)
        """

    def test_connection(self, **kwargs: Unpack[TestConnectionRequestTypeDef]) -> Dict[str, Any]:
        """
        Tests a connection to a service to validate the service credentials that you
        provide.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/test_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#test_connection)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#untag_resource)
        """

    def update_blueprint(
        self, **kwargs: Unpack[UpdateBlueprintRequestTypeDef]
    ) -> UpdateBlueprintResponseTypeDef:
        """
        Updates a registered blueprint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_blueprint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_blueprint)
        """

    def update_catalog(self, **kwargs: Unpack[UpdateCatalogRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates an existing catalog's properties in the Glue Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_catalog.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_catalog)
        """

    def update_classifier(self, **kwargs: Unpack[UpdateClassifierRequestTypeDef]) -> Dict[str, Any]:
        """
        Modifies an existing classifier (a <code>GrokClassifier</code>, an
        <code>XMLClassifier</code>, a <code>JsonClassifier</code>, or a
        <code>CsvClassifier</code>, depending on which field is present).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_classifier.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_classifier)
        """

    def update_column_statistics_for_partition(
        self, **kwargs: Unpack[UpdateColumnStatisticsForPartitionRequestTypeDef]
    ) -> UpdateColumnStatisticsForPartitionResponseTypeDef:
        """
        Creates or updates partition statistics of columns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_column_statistics_for_partition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_column_statistics_for_partition)
        """

    def update_column_statistics_for_table(
        self, **kwargs: Unpack[UpdateColumnStatisticsForTableRequestTypeDef]
    ) -> UpdateColumnStatisticsForTableResponseTypeDef:
        """
        Creates or updates table statistics of columns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_column_statistics_for_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_column_statistics_for_table)
        """

    def update_column_statistics_task_settings(
        self, **kwargs: Unpack[UpdateColumnStatisticsTaskSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates settings for a column statistics task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_column_statistics_task_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_column_statistics_task_settings)
        """

    def update_connection(self, **kwargs: Unpack[UpdateConnectionRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a connection definition in the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_connection)
        """

    def update_crawler(self, **kwargs: Unpack[UpdateCrawlerRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a crawler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_crawler.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_crawler)
        """

    def update_crawler_schedule(
        self, **kwargs: Unpack[UpdateCrawlerScheduleRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the schedule of a crawler using a <code>cron</code> expression.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_crawler_schedule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_crawler_schedule)
        """

    def update_data_quality_ruleset(
        self, **kwargs: Unpack[UpdateDataQualityRulesetRequestTypeDef]
    ) -> UpdateDataQualityRulesetResponseTypeDef:
        """
        Updates the specified data quality ruleset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_data_quality_ruleset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_data_quality_ruleset)
        """

    def update_database(self, **kwargs: Unpack[UpdateDatabaseRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates an existing database definition in a Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_database)
        """

    def update_dev_endpoint(
        self, **kwargs: Unpack[UpdateDevEndpointRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates a specified development endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_dev_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_dev_endpoint)
        """

    def update_integration_resource_property(
        self, **kwargs: Unpack[UpdateIntegrationResourcePropertyRequestTypeDef]
    ) -> UpdateIntegrationResourcePropertyResponseTypeDef:
        """
        This API can be used for updating the <code>ResourceProperty</code> of the Glue
        connection (for the source) or Glue database ARN (for the target).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_integration_resource_property.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_integration_resource_property)
        """

    def update_integration_table_properties(
        self, **kwargs: Unpack[UpdateIntegrationTablePropertiesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This API is used to provide optional override properties for the tables that
        need to be replicated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_integration_table_properties.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_integration_table_properties)
        """

    def update_job(self, **kwargs: Unpack[UpdateJobRequestTypeDef]) -> UpdateJobResponseTypeDef:
        """
        Updates an existing job definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_job)
        """

    def update_job_from_source_control(
        self, **kwargs: Unpack[UpdateJobFromSourceControlRequestTypeDef]
    ) -> UpdateJobFromSourceControlResponseTypeDef:
        """
        Synchronizes a job from the source control repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_job_from_source_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_job_from_source_control)
        """

    def update_ml_transform(
        self, **kwargs: Unpack[UpdateMLTransformRequestTypeDef]
    ) -> UpdateMLTransformResponseTypeDef:
        """
        Updates an existing machine learning transform.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_ml_transform.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_ml_transform)
        """

    def update_partition(self, **kwargs: Unpack[UpdatePartitionRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a partition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_partition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_partition)
        """

    def update_registry(
        self, **kwargs: Unpack[UpdateRegistryInputTypeDef]
    ) -> UpdateRegistryResponseTypeDef:
        """
        Updates an existing registry which is used to hold a collection of schemas.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_registry.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_registry)
        """

    def update_schema(
        self, **kwargs: Unpack[UpdateSchemaInputTypeDef]
    ) -> UpdateSchemaResponseTypeDef:
        """
        Updates the description, compatibility setting, or version checkpoint for a
        schema set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_schema)
        """

    def update_source_control_from_job(
        self, **kwargs: Unpack[UpdateSourceControlFromJobRequestTypeDef]
    ) -> UpdateSourceControlFromJobResponseTypeDef:
        """
        Synchronizes a job to the source control repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_source_control_from_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_source_control_from_job)
        """

    def update_table(self, **kwargs: Unpack[UpdateTableRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates a metadata table in the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_table)
        """

    def update_table_optimizer(
        self, **kwargs: Unpack[UpdateTableOptimizerRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the configuration for an existing table optimizer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_table_optimizer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_table_optimizer)
        """

    def update_trigger(
        self, **kwargs: Unpack[UpdateTriggerRequestTypeDef]
    ) -> UpdateTriggerResponseTypeDef:
        """
        Updates a trigger definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_trigger.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_trigger)
        """

    def update_usage_profile(
        self, **kwargs: Unpack[UpdateUsageProfileRequestTypeDef]
    ) -> UpdateUsageProfileResponseTypeDef:
        """
        Update an Glue usage profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_usage_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_usage_profile)
        """

    def update_user_defined_function(
        self, **kwargs: Unpack[UpdateUserDefinedFunctionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates an existing function definition in the Data Catalog.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_user_defined_function.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_user_defined_function)
        """

    def update_workflow(
        self, **kwargs: Unpack[UpdateWorkflowRequestTypeDef]
    ) -> UpdateWorkflowResponseTypeDef:
        """
        Updates an existing workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/update_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#update_workflow)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_entity"]
    ) -> DescribeEntityPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_classifiers"]
    ) -> GetClassifiersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_connections"]
    ) -> GetConnectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_crawler_metrics"]
    ) -> GetCrawlerMetricsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_crawlers"]
    ) -> GetCrawlersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_databases"]
    ) -> GetDatabasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_dev_endpoints"]
    ) -> GetDevEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_job_runs"]
    ) -> GetJobRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_jobs"]
    ) -> GetJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_partition_indexes"]
    ) -> GetPartitionIndexesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_partitions"]
    ) -> GetPartitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_resource_policies"]
    ) -> GetResourcePoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_security_configurations"]
    ) -> GetSecurityConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_table_versions"]
    ) -> GetTableVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_tables"]
    ) -> GetTablesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_triggers"]
    ) -> GetTriggersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_user_defined_functions"]
    ) -> GetUserDefinedFunctionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_workflow_runs"]
    ) -> GetWorkflowRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_blueprints"]
    ) -> ListBlueprintsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_connection_types"]
    ) -> ListConnectionTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_entities"]
    ) -> ListEntitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_jobs"]
    ) -> ListJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_registries"]
    ) -> ListRegistriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_schema_versions"]
    ) -> ListSchemaVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_schemas"]
    ) -> ListSchemasPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_table_optimizer_runs"]
    ) -> ListTableOptimizerRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_triggers"]
    ) -> ListTriggersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_usage_profiles"]
    ) -> ListUsageProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workflows"]
    ) -> ListWorkflowsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_glue/client/#get_paginator)
        """
