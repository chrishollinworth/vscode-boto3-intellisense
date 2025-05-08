"""
Type annotations for bedrock-agent service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_bedrock_agent.type_defs import S3IdentifierTypeDef

    data: S3IdentifierTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    ActionGroupSignatureType,
    ActionGroupStateType,
    AgentAliasStatusType,
    AgentCollaborationType,
    AgentStatusType,
    ChunkingStrategyType,
    ConfluenceAuthTypeType,
    ContentDataSourceTypeType,
    ConversationRoleType,
    CreationModeType,
    CustomSourceTypeType,
    DataDeletionPolicyType,
    DataSourceStatusType,
    DataSourceTypeType,
    DocumentStatusType,
    EmbeddingDataTypeType,
    FlowConnectionTypeType,
    FlowNodeIODataTypeType,
    FlowNodeTypeType,
    FlowStatusType,
    FlowValidationSeverityType,
    FlowValidationTypeType,
    IncludeExcludeType,
    IngestionJobSortByAttributeType,
    IngestionJobStatusType,
    InlineContentTypeType,
    KnowledgeBaseStateType,
    KnowledgeBaseStatusType,
    KnowledgeBaseStorageTypeType,
    KnowledgeBaseTypeType,
    MetadataSourceTypeType,
    MetadataValueTypeType,
    OrchestrationTypeType,
    ParsingStrategyType,
    PromptStateType,
    PromptTemplateTypeType,
    PromptTypeType,
    RedshiftProvisionedAuthTypeType,
    RedshiftQueryEngineStorageTypeType,
    RedshiftQueryEngineTypeType,
    RedshiftServerlessAuthTypeType,
    RelayConversationHistoryType,
    RequireConfirmationType,
    SharePointAuthTypeType,
    SortOrderType,
    TypeType,
    WebScopeTypeType,
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
    "APISchemaTypeDef",
    "ActionGroupExecutorTypeDef",
    "ActionGroupSummaryTypeDef",
    "AgentActionGroupTypeDef",
    "AgentAliasHistoryEventTypeDef",
    "AgentAliasRoutingConfigurationListItemTypeDef",
    "AgentAliasSummaryTypeDef",
    "AgentAliasTypeDef",
    "AgentCollaboratorSummaryTypeDef",
    "AgentCollaboratorTypeDef",
    "AgentDescriptorTypeDef",
    "AgentFlowNodeConfigurationTypeDef",
    "AgentKnowledgeBaseSummaryTypeDef",
    "AgentKnowledgeBaseTypeDef",
    "AgentSummaryTypeDef",
    "AgentTypeDef",
    "AgentVersionSummaryTypeDef",
    "AgentVersionTypeDef",
    "AssociateAgentCollaboratorRequestTypeDef",
    "AssociateAgentCollaboratorResponseTypeDef",
    "AssociateAgentKnowledgeBaseRequestTypeDef",
    "AssociateAgentKnowledgeBaseResponseTypeDef",
    "BedrockDataAutomationConfigurationTypeDef",
    "BedrockEmbeddingModelConfigurationTypeDef",
    "BedrockFoundationModelConfigurationTypeDef",
    "BedrockFoundationModelContextEnrichmentConfigurationTypeDef",
    "BlobTypeDef",
    "ByteContentDocTypeDef",
    "CachePointBlockTypeDef",
    "ChatPromptTemplateConfigurationOutputTypeDef",
    "ChatPromptTemplateConfigurationTypeDef",
    "ChatPromptTemplateConfigurationUnionTypeDef",
    "ChunkingConfigurationOutputTypeDef",
    "ChunkingConfigurationTypeDef",
    "ConditionFlowNodeConfigurationOutputTypeDef",
    "ConditionFlowNodeConfigurationTypeDef",
    "ConfluenceCrawlerConfigurationOutputTypeDef",
    "ConfluenceCrawlerConfigurationTypeDef",
    "ConfluenceDataSourceConfigurationOutputTypeDef",
    "ConfluenceDataSourceConfigurationTypeDef",
    "ConfluenceSourceConfigurationTypeDef",
    "ContentBlockTypeDef",
    "ContextEnrichmentConfigurationTypeDef",
    "CrawlFilterConfigurationOutputTypeDef",
    "CrawlFilterConfigurationTypeDef",
    "CreateAgentActionGroupRequestTypeDef",
    "CreateAgentActionGroupResponseTypeDef",
    "CreateAgentAliasRequestTypeDef",
    "CreateAgentAliasResponseTypeDef",
    "CreateAgentRequestTypeDef",
    "CreateAgentResponseTypeDef",
    "CreateDataSourceRequestTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateFlowAliasRequestTypeDef",
    "CreateFlowAliasResponseTypeDef",
    "CreateFlowRequestTypeDef",
    "CreateFlowResponseTypeDef",
    "CreateFlowVersionRequestTypeDef",
    "CreateFlowVersionResponseTypeDef",
    "CreateKnowledgeBaseRequestTypeDef",
    "CreateKnowledgeBaseResponseTypeDef",
    "CreatePromptRequestTypeDef",
    "CreatePromptResponseTypeDef",
    "CreatePromptVersionRequestTypeDef",
    "CreatePromptVersionResponseTypeDef",
    "CuratedQueryTypeDef",
    "CustomContentTypeDef",
    "CustomDocumentIdentifierTypeDef",
    "CustomOrchestrationTypeDef",
    "CustomS3LocationTypeDef",
    "CustomTransformationConfigurationOutputTypeDef",
    "CustomTransformationConfigurationTypeDef",
    "CyclicConnectionFlowValidationDetailsTypeDef",
    "DataSourceConfigurationOutputTypeDef",
    "DataSourceConfigurationTypeDef",
    "DataSourceConfigurationUnionTypeDef",
    "DataSourceSummaryTypeDef",
    "DataSourceTypeDef",
    "DeleteAgentActionGroupRequestTypeDef",
    "DeleteAgentAliasRequestTypeDef",
    "DeleteAgentAliasResponseTypeDef",
    "DeleteAgentRequestTypeDef",
    "DeleteAgentResponseTypeDef",
    "DeleteAgentVersionRequestTypeDef",
    "DeleteAgentVersionResponseTypeDef",
    "DeleteDataSourceRequestTypeDef",
    "DeleteDataSourceResponseTypeDef",
    "DeleteFlowAliasRequestTypeDef",
    "DeleteFlowAliasResponseTypeDef",
    "DeleteFlowRequestTypeDef",
    "DeleteFlowResponseTypeDef",
    "DeleteFlowVersionRequestTypeDef",
    "DeleteFlowVersionResponseTypeDef",
    "DeleteKnowledgeBaseDocumentsRequestTypeDef",
    "DeleteKnowledgeBaseDocumentsResponseTypeDef",
    "DeleteKnowledgeBaseRequestTypeDef",
    "DeleteKnowledgeBaseResponseTypeDef",
    "DeletePromptRequestTypeDef",
    "DeletePromptResponseTypeDef",
    "DisassociateAgentCollaboratorRequestTypeDef",
    "DisassociateAgentKnowledgeBaseRequestTypeDef",
    "DocumentContentTypeDef",
    "DocumentIdentifierTypeDef",
    "DocumentMetadataTypeDef",
    "DuplicateConditionExpressionFlowValidationDetailsTypeDef",
    "DuplicateConnectionsFlowValidationDetailsTypeDef",
    "EmbeddingModelConfigurationTypeDef",
    "EnrichmentStrategyConfigurationTypeDef",
    "FixedSizeChunkingConfigurationTypeDef",
    "FlowAliasRoutingConfigurationListItemTypeDef",
    "FlowAliasSummaryTypeDef",
    "FlowConditionTypeDef",
    "FlowConditionalConnectionConfigurationTypeDef",
    "FlowConnectionConfigurationTypeDef",
    "FlowConnectionTypeDef",
    "FlowDataConnectionConfigurationTypeDef",
    "FlowDefinitionOutputTypeDef",
    "FlowDefinitionTypeDef",
    "FlowDefinitionUnionTypeDef",
    "FlowNodeConfigurationOutputTypeDef",
    "FlowNodeConfigurationTypeDef",
    "FlowNodeExtraTypeDef",
    "FlowNodeInputTypeDef",
    "FlowNodeOutputTypeDef",
    "FlowNodeTypeDef",
    "FlowSummaryTypeDef",
    "FlowValidationDetailsTypeDef",
    "FlowValidationTypeDef",
    "FlowVersionSummaryTypeDef",
    "FunctionOutputTypeDef",
    "FunctionSchemaOutputTypeDef",
    "FunctionSchemaTypeDef",
    "FunctionSchemaUnionTypeDef",
    "FunctionTypeDef",
    "GetAgentActionGroupRequestTypeDef",
    "GetAgentActionGroupResponseTypeDef",
    "GetAgentAliasRequestTypeDef",
    "GetAgentAliasResponseTypeDef",
    "GetAgentCollaboratorRequestTypeDef",
    "GetAgentCollaboratorResponseTypeDef",
    "GetAgentKnowledgeBaseRequestTypeDef",
    "GetAgentKnowledgeBaseResponseTypeDef",
    "GetAgentRequestTypeDef",
    "GetAgentResponseTypeDef",
    "GetAgentVersionRequestTypeDef",
    "GetAgentVersionResponseTypeDef",
    "GetDataSourceRequestTypeDef",
    "GetDataSourceResponseTypeDef",
    "GetFlowAliasRequestTypeDef",
    "GetFlowAliasResponseTypeDef",
    "GetFlowRequestTypeDef",
    "GetFlowResponseTypeDef",
    "GetFlowVersionRequestTypeDef",
    "GetFlowVersionResponseTypeDef",
    "GetIngestionJobRequestTypeDef",
    "GetIngestionJobResponseTypeDef",
    "GetKnowledgeBaseDocumentsRequestTypeDef",
    "GetKnowledgeBaseDocumentsResponseTypeDef",
    "GetKnowledgeBaseRequestTypeDef",
    "GetKnowledgeBaseResponseTypeDef",
    "GetPromptRequestTypeDef",
    "GetPromptResponseTypeDef",
    "GuardrailConfigurationTypeDef",
    "HierarchicalChunkingConfigurationOutputTypeDef",
    "HierarchicalChunkingConfigurationTypeDef",
    "HierarchicalChunkingLevelConfigurationTypeDef",
    "IncompatibleConnectionDataTypeFlowValidationDetailsTypeDef",
    "InferenceConfigurationOutputTypeDef",
    "InferenceConfigurationTypeDef",
    "IngestKnowledgeBaseDocumentsRequestTypeDef",
    "IngestKnowledgeBaseDocumentsResponseTypeDef",
    "IngestionJobFilterTypeDef",
    "IngestionJobSortByTypeDef",
    "IngestionJobStatisticsTypeDef",
    "IngestionJobSummaryTypeDef",
    "IngestionJobTypeDef",
    "InlineCodeFlowNodeConfigurationTypeDef",
    "InlineContentTypeDef",
    "IntermediateStorageTypeDef",
    "KendraKnowledgeBaseConfigurationTypeDef",
    "KnowledgeBaseConfigurationOutputTypeDef",
    "KnowledgeBaseConfigurationTypeDef",
    "KnowledgeBaseConfigurationUnionTypeDef",
    "KnowledgeBaseDocumentDetailTypeDef",
    "KnowledgeBaseDocumentTypeDef",
    "KnowledgeBaseFlowNodeConfigurationTypeDef",
    "KnowledgeBaseSummaryTypeDef",
    "KnowledgeBaseTypeDef",
    "LambdaFunctionFlowNodeConfigurationTypeDef",
    "LexFlowNodeConfigurationTypeDef",
    "ListAgentActionGroupsRequestPaginateTypeDef",
    "ListAgentActionGroupsRequestTypeDef",
    "ListAgentActionGroupsResponseTypeDef",
    "ListAgentAliasesRequestPaginateTypeDef",
    "ListAgentAliasesRequestTypeDef",
    "ListAgentAliasesResponseTypeDef",
    "ListAgentCollaboratorsRequestPaginateTypeDef",
    "ListAgentCollaboratorsRequestTypeDef",
    "ListAgentCollaboratorsResponseTypeDef",
    "ListAgentKnowledgeBasesRequestPaginateTypeDef",
    "ListAgentKnowledgeBasesRequestTypeDef",
    "ListAgentKnowledgeBasesResponseTypeDef",
    "ListAgentVersionsRequestPaginateTypeDef",
    "ListAgentVersionsRequestTypeDef",
    "ListAgentVersionsResponseTypeDef",
    "ListAgentsRequestPaginateTypeDef",
    "ListAgentsRequestTypeDef",
    "ListAgentsResponseTypeDef",
    "ListDataSourcesRequestPaginateTypeDef",
    "ListDataSourcesRequestTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListFlowAliasesRequestPaginateTypeDef",
    "ListFlowAliasesRequestTypeDef",
    "ListFlowAliasesResponseTypeDef",
    "ListFlowVersionsRequestPaginateTypeDef",
    "ListFlowVersionsRequestTypeDef",
    "ListFlowVersionsResponseTypeDef",
    "ListFlowsRequestPaginateTypeDef",
    "ListFlowsRequestTypeDef",
    "ListFlowsResponseTypeDef",
    "ListIngestionJobsRequestPaginateTypeDef",
    "ListIngestionJobsRequestTypeDef",
    "ListIngestionJobsResponseTypeDef",
    "ListKnowledgeBaseDocumentsRequestPaginateTypeDef",
    "ListKnowledgeBaseDocumentsRequestTypeDef",
    "ListKnowledgeBaseDocumentsResponseTypeDef",
    "ListKnowledgeBasesRequestPaginateTypeDef",
    "ListKnowledgeBasesRequestTypeDef",
    "ListKnowledgeBasesResponseTypeDef",
    "ListPromptsRequestPaginateTypeDef",
    "ListPromptsRequestTypeDef",
    "ListPromptsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MalformedConditionExpressionFlowValidationDetailsTypeDef",
    "MalformedNodeInputExpressionFlowValidationDetailsTypeDef",
    "MemoryConfigurationOutputTypeDef",
    "MemoryConfigurationTypeDef",
    "MemoryConfigurationUnionTypeDef",
    "MessageOutputTypeDef",
    "MessageTypeDef",
    "MessageUnionTypeDef",
    "MetadataAttributeTypeDef",
    "MetadataAttributeValueTypeDef",
    "MismatchedNodeInputTypeFlowValidationDetailsTypeDef",
    "MismatchedNodeOutputTypeFlowValidationDetailsTypeDef",
    "MissingConnectionConfigurationFlowValidationDetailsTypeDef",
    "MissingDefaultConditionFlowValidationDetailsTypeDef",
    "MissingNodeConfigurationFlowValidationDetailsTypeDef",
    "MissingNodeInputFlowValidationDetailsTypeDef",
    "MissingNodeOutputFlowValidationDetailsTypeDef",
    "MongoDbAtlasConfigurationTypeDef",
    "MongoDbAtlasFieldMappingTypeDef",
    "MultipleNodeInputConnectionsFlowValidationDetailsTypeDef",
    "NeptuneAnalyticsConfigurationTypeDef",
    "NeptuneAnalyticsFieldMappingTypeDef",
    "OpenSearchManagedClusterConfigurationTypeDef",
    "OpenSearchManagedClusterFieldMappingTypeDef",
    "OpenSearchServerlessConfigurationTypeDef",
    "OpenSearchServerlessFieldMappingTypeDef",
    "OrchestrationExecutorTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterDetailTypeDef",
    "ParsingConfigurationTypeDef",
    "ParsingPromptTypeDef",
    "PatternObjectFilterConfigurationOutputTypeDef",
    "PatternObjectFilterConfigurationTypeDef",
    "PatternObjectFilterOutputTypeDef",
    "PatternObjectFilterTypeDef",
    "PineconeConfigurationTypeDef",
    "PineconeFieldMappingTypeDef",
    "PrepareAgentRequestTypeDef",
    "PrepareAgentResponseTypeDef",
    "PrepareFlowRequestTypeDef",
    "PrepareFlowResponseTypeDef",
    "PromptAgentResourceTypeDef",
    "PromptConfigurationOutputTypeDef",
    "PromptConfigurationTypeDef",
    "PromptFlowNodeConfigurationOutputTypeDef",
    "PromptFlowNodeConfigurationTypeDef",
    "PromptFlowNodeInlineConfigurationOutputTypeDef",
    "PromptFlowNodeInlineConfigurationTypeDef",
    "PromptFlowNodeResourceConfigurationTypeDef",
    "PromptFlowNodeSourceConfigurationOutputTypeDef",
    "PromptFlowNodeSourceConfigurationTypeDef",
    "PromptGenAiResourceTypeDef",
    "PromptInferenceConfigurationOutputTypeDef",
    "PromptInferenceConfigurationTypeDef",
    "PromptInferenceConfigurationUnionTypeDef",
    "PromptInputVariableTypeDef",
    "PromptMetadataEntryTypeDef",
    "PromptModelInferenceConfigurationOutputTypeDef",
    "PromptModelInferenceConfigurationTypeDef",
    "PromptModelInferenceConfigurationUnionTypeDef",
    "PromptOverrideConfigurationOutputTypeDef",
    "PromptOverrideConfigurationTypeDef",
    "PromptOverrideConfigurationUnionTypeDef",
    "PromptSummaryTypeDef",
    "PromptTemplateConfigurationOutputTypeDef",
    "PromptTemplateConfigurationTypeDef",
    "PromptTemplateConfigurationUnionTypeDef",
    "PromptVariantOutputTypeDef",
    "PromptVariantTypeDef",
    "PromptVariantUnionTypeDef",
    "QueryGenerationColumnTypeDef",
    "QueryGenerationConfigurationOutputTypeDef",
    "QueryGenerationConfigurationTypeDef",
    "QueryGenerationContextOutputTypeDef",
    "QueryGenerationContextTypeDef",
    "QueryGenerationTableOutputTypeDef",
    "QueryGenerationTableTypeDef",
    "RdsConfigurationTypeDef",
    "RdsFieldMappingTypeDef",
    "RedisEnterpriseCloudConfigurationTypeDef",
    "RedisEnterpriseCloudFieldMappingTypeDef",
    "RedshiftConfigurationOutputTypeDef",
    "RedshiftConfigurationTypeDef",
    "RedshiftProvisionedAuthConfigurationTypeDef",
    "RedshiftProvisionedConfigurationTypeDef",
    "RedshiftQueryEngineAwsDataCatalogStorageConfigurationOutputTypeDef",
    "RedshiftQueryEngineAwsDataCatalogStorageConfigurationTypeDef",
    "RedshiftQueryEngineConfigurationTypeDef",
    "RedshiftQueryEngineRedshiftStorageConfigurationTypeDef",
    "RedshiftQueryEngineStorageConfigurationOutputTypeDef",
    "RedshiftQueryEngineStorageConfigurationTypeDef",
    "RedshiftServerlessAuthConfigurationTypeDef",
    "RedshiftServerlessConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "RetrievalFlowNodeConfigurationTypeDef",
    "RetrievalFlowNodeS3ConfigurationTypeDef",
    "RetrievalFlowNodeServiceConfigurationTypeDef",
    "S3ContentTypeDef",
    "S3DataSourceConfigurationOutputTypeDef",
    "S3DataSourceConfigurationTypeDef",
    "S3IdentifierTypeDef",
    "S3LocationTypeDef",
    "SalesforceCrawlerConfigurationOutputTypeDef",
    "SalesforceCrawlerConfigurationTypeDef",
    "SalesforceDataSourceConfigurationOutputTypeDef",
    "SalesforceDataSourceConfigurationTypeDef",
    "SalesforceSourceConfigurationTypeDef",
    "SeedUrlTypeDef",
    "SemanticChunkingConfigurationTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "SessionSummaryConfigurationTypeDef",
    "SharePointCrawlerConfigurationOutputTypeDef",
    "SharePointCrawlerConfigurationTypeDef",
    "SharePointDataSourceConfigurationOutputTypeDef",
    "SharePointDataSourceConfigurationTypeDef",
    "SharePointSourceConfigurationOutputTypeDef",
    "SharePointSourceConfigurationTypeDef",
    "SpecificToolChoiceTypeDef",
    "SqlKnowledgeBaseConfigurationOutputTypeDef",
    "SqlKnowledgeBaseConfigurationTypeDef",
    "StartIngestionJobRequestTypeDef",
    "StartIngestionJobResponseTypeDef",
    "StopIngestionJobRequestTypeDef",
    "StopIngestionJobResponseTypeDef",
    "StorageConfigurationTypeDef",
    "StorageFlowNodeConfigurationTypeDef",
    "StorageFlowNodeS3ConfigurationTypeDef",
    "StorageFlowNodeServiceConfigurationTypeDef",
    "SupplementalDataStorageConfigurationOutputTypeDef",
    "SupplementalDataStorageConfigurationTypeDef",
    "SupplementalDataStorageLocationTypeDef",
    "SystemContentBlockTypeDef",
    "TagResourceRequestTypeDef",
    "TextContentDocTypeDef",
    "TextPromptTemplateConfigurationOutputTypeDef",
    "TextPromptTemplateConfigurationTypeDef",
    "TextPromptTemplateConfigurationUnionTypeDef",
    "ToolChoiceOutputTypeDef",
    "ToolChoiceTypeDef",
    "ToolChoiceUnionTypeDef",
    "ToolConfigurationOutputTypeDef",
    "ToolConfigurationTypeDef",
    "ToolConfigurationUnionTypeDef",
    "ToolInputSchemaOutputTypeDef",
    "ToolInputSchemaTypeDef",
    "ToolInputSchemaUnionTypeDef",
    "ToolOutputTypeDef",
    "ToolSpecificationOutputTypeDef",
    "ToolSpecificationTypeDef",
    "ToolSpecificationUnionTypeDef",
    "ToolTypeDef",
    "ToolUnionTypeDef",
    "TransformationFunctionTypeDef",
    "TransformationLambdaConfigurationTypeDef",
    "TransformationTypeDef",
    "UnfulfilledNodeInputFlowValidationDetailsTypeDef",
    "UnknownConnectionConditionFlowValidationDetailsTypeDef",
    "UnknownConnectionSourceFlowValidationDetailsTypeDef",
    "UnknownConnectionSourceOutputFlowValidationDetailsTypeDef",
    "UnknownConnectionTargetFlowValidationDetailsTypeDef",
    "UnknownConnectionTargetInputFlowValidationDetailsTypeDef",
    "UnknownNodeInputFlowValidationDetailsTypeDef",
    "UnknownNodeOutputFlowValidationDetailsTypeDef",
    "UnreachableNodeFlowValidationDetailsTypeDef",
    "UnsatisfiedConnectionConditionsFlowValidationDetailsTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAgentActionGroupRequestTypeDef",
    "UpdateAgentActionGroupResponseTypeDef",
    "UpdateAgentAliasRequestTypeDef",
    "UpdateAgentAliasResponseTypeDef",
    "UpdateAgentCollaboratorRequestTypeDef",
    "UpdateAgentCollaboratorResponseTypeDef",
    "UpdateAgentKnowledgeBaseRequestTypeDef",
    "UpdateAgentKnowledgeBaseResponseTypeDef",
    "UpdateAgentRequestTypeDef",
    "UpdateAgentResponseTypeDef",
    "UpdateDataSourceRequestTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "UpdateFlowAliasRequestTypeDef",
    "UpdateFlowAliasResponseTypeDef",
    "UpdateFlowRequestTypeDef",
    "UpdateFlowResponseTypeDef",
    "UpdateKnowledgeBaseRequestTypeDef",
    "UpdateKnowledgeBaseResponseTypeDef",
    "UpdatePromptRequestTypeDef",
    "UpdatePromptResponseTypeDef",
    "UrlConfigurationOutputTypeDef",
    "UrlConfigurationTypeDef",
    "ValidateFlowDefinitionRequestTypeDef",
    "ValidateFlowDefinitionResponseTypeDef",
    "VectorIngestionConfigurationOutputTypeDef",
    "VectorIngestionConfigurationTypeDef",
    "VectorIngestionConfigurationUnionTypeDef",
    "VectorKnowledgeBaseConfigurationOutputTypeDef",
    "VectorKnowledgeBaseConfigurationTypeDef",
    "WebCrawlerConfigurationOutputTypeDef",
    "WebCrawlerConfigurationTypeDef",
    "WebCrawlerLimitsTypeDef",
    "WebDataSourceConfigurationOutputTypeDef",
    "WebDataSourceConfigurationTypeDef",
    "WebSourceConfigurationOutputTypeDef",
    "WebSourceConfigurationTypeDef",
)

class S3IdentifierTypeDef(TypedDict):
    s3BucketName: NotRequired[str]
    s3ObjectKey: NotRequired[str]

ActionGroupExecutorTypeDef = TypedDict(
    "ActionGroupExecutorTypeDef",
    {
        "customControl": NotRequired[Literal["RETURN_CONTROL"]],
        "lambda": NotRequired[str],
    },
)

class ActionGroupSummaryTypeDef(TypedDict):
    actionGroupId: str
    actionGroupName: str
    actionGroupState: ActionGroupStateType
    updatedAt: datetime
    description: NotRequired[str]

class AgentAliasRoutingConfigurationListItemTypeDef(TypedDict):
    agentVersion: NotRequired[str]
    provisionedThroughput: NotRequired[str]

class AgentDescriptorTypeDef(TypedDict):
    aliasArn: NotRequired[str]

class AgentFlowNodeConfigurationTypeDef(TypedDict):
    agentAliasArn: str

class AgentKnowledgeBaseSummaryTypeDef(TypedDict):
    knowledgeBaseId: str
    knowledgeBaseState: KnowledgeBaseStateType
    updatedAt: datetime
    description: NotRequired[str]

class AgentKnowledgeBaseTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    createdAt: datetime
    description: str
    knowledgeBaseId: str
    knowledgeBaseState: KnowledgeBaseStateType
    updatedAt: datetime

class GuardrailConfigurationTypeDef(TypedDict):
    guardrailIdentifier: NotRequired[str]
    guardrailVersion: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AssociateAgentKnowledgeBaseRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    description: str
    knowledgeBaseId: str
    knowledgeBaseState: NotRequired[KnowledgeBaseStateType]

class BedrockDataAutomationConfigurationTypeDef(TypedDict):
    parsingModality: NotRequired[Literal["MULTIMODAL"]]

class BedrockEmbeddingModelConfigurationTypeDef(TypedDict):
    dimensions: NotRequired[int]
    embeddingDataType: NotRequired[EmbeddingDataTypeType]

class ParsingPromptTypeDef(TypedDict):
    parsingPromptText: str

class EnrichmentStrategyConfigurationTypeDef(TypedDict):
    method: Literal["CHUNK_ENTITY_EXTRACTION"]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CachePointBlockTypeDef = TypedDict(
    "CachePointBlockTypeDef",
    {
        "type": Literal["default"],
    },
)

class PromptInputVariableTypeDef(TypedDict):
    name: NotRequired[str]

class FixedSizeChunkingConfigurationTypeDef(TypedDict):
    maxTokens: int
    overlapPercentage: int

class SemanticChunkingConfigurationTypeDef(TypedDict):
    breakpointPercentileThreshold: int
    bufferSize: int
    maxTokens: int

class FlowConditionTypeDef(TypedDict):
    name: str
    expression: NotRequired[str]

class ConfluenceSourceConfigurationTypeDef(TypedDict):
    authType: ConfluenceAuthTypeType
    credentialsSecretArn: str
    hostType: Literal["SAAS"]
    hostUrl: str

class ServerSideEncryptionConfigurationTypeDef(TypedDict):
    kmsKeyArn: NotRequired[str]

class FlowAliasRoutingConfigurationListItemTypeDef(TypedDict):
    flowVersion: NotRequired[str]

class CreateFlowVersionRequestTypeDef(TypedDict):
    flowIdentifier: str
    clientToken: NotRequired[str]
    description: NotRequired[str]

class CreatePromptVersionRequestTypeDef(TypedDict):
    promptIdentifier: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CuratedQueryTypeDef(TypedDict):
    naturalLanguage: str
    sql: str

CustomDocumentIdentifierTypeDef = TypedDict(
    "CustomDocumentIdentifierTypeDef",
    {
        "id": str,
    },
)

class CustomS3LocationTypeDef(TypedDict):
    uri: str
    bucketOwnerAccountId: NotRequired[str]

OrchestrationExecutorTypeDef = TypedDict(
    "OrchestrationExecutorTypeDef",
    {
        "lambda": NotRequired[str],
    },
)

class CyclicConnectionFlowValidationDetailsTypeDef(TypedDict):
    connection: str

class S3DataSourceConfigurationOutputTypeDef(TypedDict):
    bucketArn: str
    bucketOwnerAccountId: NotRequired[str]
    inclusionPrefixes: NotRequired[List[str]]

class S3DataSourceConfigurationTypeDef(TypedDict):
    bucketArn: str
    bucketOwnerAccountId: NotRequired[str]
    inclusionPrefixes: NotRequired[Sequence[str]]

class DataSourceSummaryTypeDef(TypedDict):
    dataSourceId: str
    knowledgeBaseId: str
    name: str
    status: DataSourceStatusType
    updatedAt: datetime
    description: NotRequired[str]

class DeleteAgentActionGroupRequestTypeDef(TypedDict):
    actionGroupId: str
    agentId: str
    agentVersion: str
    skipResourceInUseCheck: NotRequired[bool]

class DeleteAgentAliasRequestTypeDef(TypedDict):
    agentAliasId: str
    agentId: str

class DeleteAgentRequestTypeDef(TypedDict):
    agentId: str
    skipResourceInUseCheck: NotRequired[bool]

class DeleteAgentVersionRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    skipResourceInUseCheck: NotRequired[bool]

class DeleteDataSourceRequestTypeDef(TypedDict):
    dataSourceId: str
    knowledgeBaseId: str

class DeleteFlowAliasRequestTypeDef(TypedDict):
    aliasIdentifier: str
    flowIdentifier: str

class DeleteFlowRequestTypeDef(TypedDict):
    flowIdentifier: str
    skipResourceInUseCheck: NotRequired[bool]

class DeleteFlowVersionRequestTypeDef(TypedDict):
    flowIdentifier: str
    flowVersion: str
    skipResourceInUseCheck: NotRequired[bool]

class DeleteKnowledgeBaseRequestTypeDef(TypedDict):
    knowledgeBaseId: str

class DeletePromptRequestTypeDef(TypedDict):
    promptIdentifier: str
    promptVersion: NotRequired[str]

class DisassociateAgentCollaboratorRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    collaboratorId: str

class DisassociateAgentKnowledgeBaseRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str

class S3LocationTypeDef(TypedDict):
    uri: str

class DuplicateConditionExpressionFlowValidationDetailsTypeDef(TypedDict):
    expression: str
    node: str

class DuplicateConnectionsFlowValidationDetailsTypeDef(TypedDict):
    source: str
    target: str

class FlowConditionalConnectionConfigurationTypeDef(TypedDict):
    condition: str

class FlowDataConnectionConfigurationTypeDef(TypedDict):
    sourceOutput: str
    targetInput: str

class InlineCodeFlowNodeConfigurationTypeDef(TypedDict):
    code: str
    language: Literal["Python_3"]

class LambdaFunctionFlowNodeConfigurationTypeDef(TypedDict):
    lambdaArn: str

class LexFlowNodeConfigurationTypeDef(TypedDict):
    botAliasArn: str
    localeId: str

FlowNodeInputTypeDef = TypedDict(
    "FlowNodeInputTypeDef",
    {
        "expression": str,
        "name": str,
        "type": FlowNodeIODataTypeType,
    },
)
FlowNodeOutputTypeDef = TypedDict(
    "FlowNodeOutputTypeDef",
    {
        "name": str,
        "type": FlowNodeIODataTypeType,
    },
)
FlowSummaryTypeDef = TypedDict(
    "FlowSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "id": str,
        "name": str,
        "status": FlowStatusType,
        "updatedAt": datetime,
        "version": str,
        "description": NotRequired[str],
    },
)

class IncompatibleConnectionDataTypeFlowValidationDetailsTypeDef(TypedDict):
    connection: str

class MalformedConditionExpressionFlowValidationDetailsTypeDef(TypedDict):
    cause: str
    condition: str
    node: str

MalformedNodeInputExpressionFlowValidationDetailsTypeDef = TypedDict(
    "MalformedNodeInputExpressionFlowValidationDetailsTypeDef",
    {
        "cause": str,
        "input": str,
        "node": str,
    },
)
MismatchedNodeInputTypeFlowValidationDetailsTypeDef = TypedDict(
    "MismatchedNodeInputTypeFlowValidationDetailsTypeDef",
    {
        "expectedType": FlowNodeIODataTypeType,
        "input": str,
        "node": str,
    },
)

class MismatchedNodeOutputTypeFlowValidationDetailsTypeDef(TypedDict):
    expectedType: FlowNodeIODataTypeType
    node: str
    output: str

class MissingConnectionConfigurationFlowValidationDetailsTypeDef(TypedDict):
    connection: str

class MissingDefaultConditionFlowValidationDetailsTypeDef(TypedDict):
    node: str

class MissingNodeConfigurationFlowValidationDetailsTypeDef(TypedDict):
    node: str

MissingNodeInputFlowValidationDetailsTypeDef = TypedDict(
    "MissingNodeInputFlowValidationDetailsTypeDef",
    {
        "input": str,
        "node": str,
    },
)

class MissingNodeOutputFlowValidationDetailsTypeDef(TypedDict):
    node: str
    output: str

MultipleNodeInputConnectionsFlowValidationDetailsTypeDef = TypedDict(
    "MultipleNodeInputConnectionsFlowValidationDetailsTypeDef",
    {
        "input": str,
        "node": str,
    },
)
UnfulfilledNodeInputFlowValidationDetailsTypeDef = TypedDict(
    "UnfulfilledNodeInputFlowValidationDetailsTypeDef",
    {
        "input": str,
        "node": str,
    },
)

class UnknownConnectionConditionFlowValidationDetailsTypeDef(TypedDict):
    connection: str

class UnknownConnectionSourceFlowValidationDetailsTypeDef(TypedDict):
    connection: str

class UnknownConnectionSourceOutputFlowValidationDetailsTypeDef(TypedDict):
    connection: str

class UnknownConnectionTargetFlowValidationDetailsTypeDef(TypedDict):
    connection: str

class UnknownConnectionTargetInputFlowValidationDetailsTypeDef(TypedDict):
    connection: str

UnknownNodeInputFlowValidationDetailsTypeDef = TypedDict(
    "UnknownNodeInputFlowValidationDetailsTypeDef",
    {
        "input": str,
        "node": str,
    },
)

class UnknownNodeOutputFlowValidationDetailsTypeDef(TypedDict):
    node: str
    output: str

class UnreachableNodeFlowValidationDetailsTypeDef(TypedDict):
    node: str

class UnsatisfiedConnectionConditionsFlowValidationDetailsTypeDef(TypedDict):
    connection: str

FlowVersionSummaryTypeDef = TypedDict(
    "FlowVersionSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "id": str,
        "status": FlowStatusType,
        "version": str,
    },
)
ParameterDetailTypeDef = TypedDict(
    "ParameterDetailTypeDef",
    {
        "type": TypeType,
        "description": NotRequired[str],
        "required": NotRequired[bool],
    },
)

class GetAgentActionGroupRequestTypeDef(TypedDict):
    actionGroupId: str
    agentId: str
    agentVersion: str

class GetAgentAliasRequestTypeDef(TypedDict):
    agentAliasId: str
    agentId: str

class GetAgentCollaboratorRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    collaboratorId: str

class GetAgentKnowledgeBaseRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str

class GetAgentRequestTypeDef(TypedDict):
    agentId: str

class GetAgentVersionRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str

class GetDataSourceRequestTypeDef(TypedDict):
    dataSourceId: str
    knowledgeBaseId: str

class GetFlowAliasRequestTypeDef(TypedDict):
    aliasIdentifier: str
    flowIdentifier: str

class GetFlowRequestTypeDef(TypedDict):
    flowIdentifier: str

class GetFlowVersionRequestTypeDef(TypedDict):
    flowIdentifier: str
    flowVersion: str

class GetIngestionJobRequestTypeDef(TypedDict):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str

class GetKnowledgeBaseRequestTypeDef(TypedDict):
    knowledgeBaseId: str

class GetPromptRequestTypeDef(TypedDict):
    promptIdentifier: str
    promptVersion: NotRequired[str]

class HierarchicalChunkingLevelConfigurationTypeDef(TypedDict):
    maxTokens: int

class InferenceConfigurationOutputTypeDef(TypedDict):
    maximumLength: NotRequired[int]
    stopSequences: NotRequired[List[str]]
    temperature: NotRequired[float]
    topK: NotRequired[int]
    topP: NotRequired[float]

class InferenceConfigurationTypeDef(TypedDict):
    maximumLength: NotRequired[int]
    stopSequences: NotRequired[Sequence[str]]
    temperature: NotRequired[float]
    topK: NotRequired[int]
    topP: NotRequired[float]

IngestionJobFilterTypeDef = TypedDict(
    "IngestionJobFilterTypeDef",
    {
        "attribute": Literal["STATUS"],
        "operator": Literal["EQ"],
        "values": Sequence[str],
    },
)

class IngestionJobSortByTypeDef(TypedDict):
    attribute: IngestionJobSortByAttributeType
    order: SortOrderType

class IngestionJobStatisticsTypeDef(TypedDict):
    numberOfDocumentsDeleted: NotRequired[int]
    numberOfDocumentsFailed: NotRequired[int]
    numberOfDocumentsScanned: NotRequired[int]
    numberOfMetadataDocumentsModified: NotRequired[int]
    numberOfMetadataDocumentsScanned: NotRequired[int]
    numberOfModifiedDocumentsIndexed: NotRequired[int]
    numberOfNewDocumentsIndexed: NotRequired[int]

class TextContentDocTypeDef(TypedDict):
    data: str

class KendraKnowledgeBaseConfigurationTypeDef(TypedDict):
    kendraIndexArn: str

class KnowledgeBaseSummaryTypeDef(TypedDict):
    knowledgeBaseId: str
    name: str
    status: KnowledgeBaseStatusType
    updatedAt: datetime
    description: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAgentActionGroupsRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAgentAliasesRequestTypeDef(TypedDict):
    agentId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAgentCollaboratorsRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAgentKnowledgeBasesRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAgentVersionsRequestTypeDef(TypedDict):
    agentId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAgentsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListDataSourcesRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListFlowAliasesRequestTypeDef(TypedDict):
    flowIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListFlowVersionsRequestTypeDef(TypedDict):
    flowIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListFlowsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListKnowledgeBaseDocumentsRequestTypeDef(TypedDict):
    dataSourceId: str
    knowledgeBaseId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListKnowledgeBasesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListPromptsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    promptIdentifier: NotRequired[str]

PromptSummaryTypeDef = TypedDict(
    "PromptSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "id": str,
        "name": str,
        "updatedAt": datetime,
        "version": str,
        "description": NotRequired[str],
    },
)

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class SessionSummaryConfigurationTypeDef(TypedDict):
    maxRecentSessions: NotRequired[int]

MetadataAttributeValueTypeDef = TypedDict(
    "MetadataAttributeValueTypeDef",
    {
        "type": MetadataValueTypeType,
        "booleanValue": NotRequired[bool],
        "numberValue": NotRequired[float],
        "stringListValue": NotRequired[Sequence[str]],
        "stringValue": NotRequired[str],
    },
)

class MongoDbAtlasFieldMappingTypeDef(TypedDict):
    metadataField: str
    textField: str
    vectorField: str

class NeptuneAnalyticsFieldMappingTypeDef(TypedDict):
    metadataField: str
    textField: str

class OpenSearchManagedClusterFieldMappingTypeDef(TypedDict):
    metadataField: str
    textField: str
    vectorField: str

class OpenSearchServerlessFieldMappingTypeDef(TypedDict):
    metadataField: str
    textField: str
    vectorField: str

class PatternObjectFilterOutputTypeDef(TypedDict):
    objectType: str
    exclusionFilters: NotRequired[List[str]]
    inclusionFilters: NotRequired[List[str]]

class PatternObjectFilterTypeDef(TypedDict):
    objectType: str
    exclusionFilters: NotRequired[Sequence[str]]
    inclusionFilters: NotRequired[Sequence[str]]

class PineconeFieldMappingTypeDef(TypedDict):
    metadataField: str
    textField: str

class PrepareAgentRequestTypeDef(TypedDict):
    agentId: str

class PrepareFlowRequestTypeDef(TypedDict):
    flowIdentifier: str

class PromptAgentResourceTypeDef(TypedDict):
    agentIdentifier: str

class PromptFlowNodeResourceConfigurationTypeDef(TypedDict):
    promptArn: str

class PromptModelInferenceConfigurationOutputTypeDef(TypedDict):
    maxTokens: NotRequired[int]
    stopSequences: NotRequired[List[str]]
    temperature: NotRequired[float]
    topP: NotRequired[float]

class PromptMetadataEntryTypeDef(TypedDict):
    key: str
    value: str

class PromptModelInferenceConfigurationTypeDef(TypedDict):
    maxTokens: NotRequired[int]
    stopSequences: NotRequired[Sequence[str]]
    temperature: NotRequired[float]
    topP: NotRequired[float]

class QueryGenerationColumnTypeDef(TypedDict):
    description: NotRequired[str]
    inclusion: NotRequired[IncludeExcludeType]
    name: NotRequired[str]

class RdsFieldMappingTypeDef(TypedDict):
    metadataField: str
    primaryKeyField: str
    textField: str
    vectorField: str
    customMetadataField: NotRequired[str]

class RedisEnterpriseCloudFieldMappingTypeDef(TypedDict):
    metadataField: str
    textField: str
    vectorField: str

RedshiftProvisionedAuthConfigurationTypeDef = TypedDict(
    "RedshiftProvisionedAuthConfigurationTypeDef",
    {
        "type": RedshiftProvisionedAuthTypeType,
        "databaseUser": NotRequired[str],
        "usernamePasswordSecretArn": NotRequired[str],
    },
)

class RedshiftQueryEngineAwsDataCatalogStorageConfigurationOutputTypeDef(TypedDict):
    tableNames: List[str]

class RedshiftQueryEngineAwsDataCatalogStorageConfigurationTypeDef(TypedDict):
    tableNames: Sequence[str]

class RedshiftQueryEngineRedshiftStorageConfigurationTypeDef(TypedDict):
    databaseName: str

RedshiftServerlessAuthConfigurationTypeDef = TypedDict(
    "RedshiftServerlessAuthConfigurationTypeDef",
    {
        "type": RedshiftServerlessAuthTypeType,
        "usernamePasswordSecretArn": NotRequired[str],
    },
)

class RetrievalFlowNodeS3ConfigurationTypeDef(TypedDict):
    bucketName: str

class SalesforceSourceConfigurationTypeDef(TypedDict):
    authType: Literal["OAUTH2_CLIENT_CREDENTIALS"]
    credentialsSecretArn: str
    hostUrl: str

class SeedUrlTypeDef(TypedDict):
    url: NotRequired[str]

class SharePointSourceConfigurationOutputTypeDef(TypedDict):
    authType: SharePointAuthTypeType
    credentialsSecretArn: str
    domain: str
    hostType: Literal["ONLINE"]
    siteUrls: List[str]
    tenantId: NotRequired[str]

class SharePointSourceConfigurationTypeDef(TypedDict):
    authType: SharePointAuthTypeType
    credentialsSecretArn: str
    domain: str
    hostType: Literal["ONLINE"]
    siteUrls: Sequence[str]
    tenantId: NotRequired[str]

class SpecificToolChoiceTypeDef(TypedDict):
    name: str

class StartIngestionJobRequestTypeDef(TypedDict):
    dataSourceId: str
    knowledgeBaseId: str
    clientToken: NotRequired[str]
    description: NotRequired[str]

class StopIngestionJobRequestTypeDef(TypedDict):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str

class StorageFlowNodeS3ConfigurationTypeDef(TypedDict):
    bucketName: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class ToolInputSchemaOutputTypeDef(TypedDict):
    json: NotRequired[Dict[str, Any]]

class ToolInputSchemaTypeDef(TypedDict):
    json: NotRequired[Mapping[str, Any]]

class TransformationLambdaConfigurationTypeDef(TypedDict):
    lambdaArn: str

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAgentKnowledgeBaseRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    knowledgeBaseId: str
    description: NotRequired[str]
    knowledgeBaseState: NotRequired[KnowledgeBaseStateType]

class WebCrawlerLimitsTypeDef(TypedDict):
    maxPages: NotRequired[int]
    rateLimit: NotRequired[int]

class APISchemaTypeDef(TypedDict):
    payload: NotRequired[str]
    s3: NotRequired[S3IdentifierTypeDef]

class AgentAliasHistoryEventTypeDef(TypedDict):
    endDate: NotRequired[datetime]
    routingConfiguration: NotRequired[List[AgentAliasRoutingConfigurationListItemTypeDef]]
    startDate: NotRequired[datetime]

class AgentAliasSummaryTypeDef(TypedDict):
    agentAliasId: str
    agentAliasName: str
    agentAliasStatus: AgentAliasStatusType
    createdAt: datetime
    updatedAt: datetime
    description: NotRequired[str]
    routingConfiguration: NotRequired[List[AgentAliasRoutingConfigurationListItemTypeDef]]

class CreateAgentAliasRequestTypeDef(TypedDict):
    agentAliasName: str
    agentId: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    routingConfiguration: NotRequired[Sequence[AgentAliasRoutingConfigurationListItemTypeDef]]
    tags: NotRequired[Mapping[str, str]]

class UpdateAgentAliasRequestTypeDef(TypedDict):
    agentAliasId: str
    agentAliasName: str
    agentId: str
    description: NotRequired[str]
    routingConfiguration: NotRequired[Sequence[AgentAliasRoutingConfigurationListItemTypeDef]]

class AgentCollaboratorSummaryTypeDef(TypedDict):
    agentDescriptor: AgentDescriptorTypeDef
    agentId: str
    agentVersion: str
    collaborationInstruction: str
    collaboratorId: str
    collaboratorName: str
    createdAt: datetime
    lastUpdatedAt: datetime
    relayConversationHistory: RelayConversationHistoryType

class AgentCollaboratorTypeDef(TypedDict):
    agentDescriptor: AgentDescriptorTypeDef
    agentId: str
    agentVersion: str
    collaborationInstruction: str
    collaboratorId: str
    collaboratorName: str
    createdAt: datetime
    lastUpdatedAt: datetime
    clientToken: NotRequired[str]
    relayConversationHistory: NotRequired[RelayConversationHistoryType]

class AssociateAgentCollaboratorRequestTypeDef(TypedDict):
    agentDescriptor: AgentDescriptorTypeDef
    agentId: str
    agentVersion: str
    collaborationInstruction: str
    collaboratorName: str
    clientToken: NotRequired[str]
    relayConversationHistory: NotRequired[RelayConversationHistoryType]

class UpdateAgentCollaboratorRequestTypeDef(TypedDict):
    agentDescriptor: AgentDescriptorTypeDef
    agentId: str
    agentVersion: str
    collaborationInstruction: str
    collaboratorId: str
    collaboratorName: str
    relayConversationHistory: NotRequired[RelayConversationHistoryType]

class AgentSummaryTypeDef(TypedDict):
    agentId: str
    agentName: str
    agentStatus: AgentStatusType
    updatedAt: datetime
    description: NotRequired[str]
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]
    latestAgentVersion: NotRequired[str]

class AgentVersionSummaryTypeDef(TypedDict):
    agentName: str
    agentStatus: AgentStatusType
    agentVersion: str
    createdAt: datetime
    updatedAt: datetime
    description: NotRequired[str]
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]

class KnowledgeBaseFlowNodeConfigurationTypeDef(TypedDict):
    knowledgeBaseId: str
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]
    modelId: NotRequired[str]

class AssociateAgentKnowledgeBaseResponseTypeDef(TypedDict):
    agentKnowledgeBase: AgentKnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAgentAliasResponseTypeDef(TypedDict):
    agentAliasId: str
    agentAliasStatus: AgentAliasStatusType
    agentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAgentResponseTypeDef(TypedDict):
    agentId: str
    agentStatus: AgentStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAgentVersionResponseTypeDef(TypedDict):
    agentId: str
    agentStatus: AgentStatusType
    agentVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataSourceResponseTypeDef(TypedDict):
    dataSourceId: str
    knowledgeBaseId: str
    status: DataSourceStatusType
    ResponseMetadata: ResponseMetadataTypeDef

DeleteFlowAliasResponseTypeDef = TypedDict(
    "DeleteFlowAliasResponseTypeDef",
    {
        "flowId": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFlowResponseTypeDef = TypedDict(
    "DeleteFlowResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteFlowVersionResponseTypeDef = TypedDict(
    "DeleteFlowVersionResponseTypeDef",
    {
        "id": str,
        "version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DeleteKnowledgeBaseResponseTypeDef(TypedDict):
    knowledgeBaseId: str
    status: KnowledgeBaseStatusType
    ResponseMetadata: ResponseMetadataTypeDef

DeletePromptResponseTypeDef = TypedDict(
    "DeletePromptResponseTypeDef",
    {
        "id": str,
        "version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetAgentKnowledgeBaseResponseTypeDef(TypedDict):
    agentKnowledgeBase: AgentKnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAgentActionGroupsResponseTypeDef(TypedDict):
    actionGroupSummaries: List[ActionGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAgentKnowledgeBasesResponseTypeDef(TypedDict):
    agentKnowledgeBaseSummaries: List[AgentKnowledgeBaseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PrepareAgentResponseTypeDef(TypedDict):
    agentId: str
    agentStatus: AgentStatusType
    agentVersion: str
    preparedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

PrepareFlowResponseTypeDef = TypedDict(
    "PrepareFlowResponseTypeDef",
    {
        "id": str,
        "status": FlowStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UpdateAgentKnowledgeBaseResponseTypeDef(TypedDict):
    agentKnowledgeBase: AgentKnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmbeddingModelConfigurationTypeDef(TypedDict):
    bedrockEmbeddingModelConfiguration: NotRequired[BedrockEmbeddingModelConfigurationTypeDef]

class BedrockFoundationModelConfigurationTypeDef(TypedDict):
    modelArn: str
    parsingModality: NotRequired[Literal["MULTIMODAL"]]
    parsingPrompt: NotRequired[ParsingPromptTypeDef]

class BedrockFoundationModelContextEnrichmentConfigurationTypeDef(TypedDict):
    enrichmentStrategyConfiguration: EnrichmentStrategyConfigurationTypeDef
    modelArn: str

class ByteContentDocTypeDef(TypedDict):
    data: BlobTypeDef
    mimeType: str

class ContentBlockTypeDef(TypedDict):
    cachePoint: NotRequired[CachePointBlockTypeDef]
    text: NotRequired[str]

class SystemContentBlockTypeDef(TypedDict):
    cachePoint: NotRequired[CachePointBlockTypeDef]
    text: NotRequired[str]

class TextPromptTemplateConfigurationOutputTypeDef(TypedDict):
    text: str
    cachePoint: NotRequired[CachePointBlockTypeDef]
    inputVariables: NotRequired[List[PromptInputVariableTypeDef]]

class TextPromptTemplateConfigurationTypeDef(TypedDict):
    text: str
    cachePoint: NotRequired[CachePointBlockTypeDef]
    inputVariables: NotRequired[Sequence[PromptInputVariableTypeDef]]

class ConditionFlowNodeConfigurationOutputTypeDef(TypedDict):
    conditions: List[FlowConditionTypeDef]

class ConditionFlowNodeConfigurationTypeDef(TypedDict):
    conditions: Sequence[FlowConditionTypeDef]

class CreateFlowAliasRequestTypeDef(TypedDict):
    flowIdentifier: str
    name: str
    routingConfiguration: Sequence[FlowAliasRoutingConfigurationListItemTypeDef]
    clientToken: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

CreateFlowAliasResponseTypeDef = TypedDict(
    "CreateFlowAliasResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "description": str,
        "flowId": str,
        "id": str,
        "name": str,
        "routingConfiguration": List[FlowAliasRoutingConfigurationListItemTypeDef],
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FlowAliasSummaryTypeDef = TypedDict(
    "FlowAliasSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "flowId": str,
        "id": str,
        "name": str,
        "routingConfiguration": List[FlowAliasRoutingConfigurationListItemTypeDef],
        "updatedAt": datetime,
        "description": NotRequired[str],
    },
)
GetFlowAliasResponseTypeDef = TypedDict(
    "GetFlowAliasResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "description": str,
        "flowId": str,
        "id": str,
        "name": str,
        "routingConfiguration": List[FlowAliasRoutingConfigurationListItemTypeDef],
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UpdateFlowAliasRequestTypeDef(TypedDict):
    aliasIdentifier: str
    flowIdentifier: str
    name: str
    routingConfiguration: Sequence[FlowAliasRoutingConfigurationListItemTypeDef]
    description: NotRequired[str]

UpdateFlowAliasResponseTypeDef = TypedDict(
    "UpdateFlowAliasResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "description": str,
        "flowId": str,
        "id": str,
        "name": str,
        "routingConfiguration": List[FlowAliasRoutingConfigurationListItemTypeDef],
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CustomOrchestrationTypeDef(TypedDict):
    executor: NotRequired[OrchestrationExecutorTypeDef]

class ListDataSourcesResponseTypeDef(TypedDict):
    dataSourceSummaries: List[DataSourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DocumentIdentifierTypeDef(TypedDict):
    dataSourceType: ContentDataSourceTypeType
    custom: NotRequired[CustomDocumentIdentifierTypeDef]
    s3: NotRequired[S3LocationTypeDef]

class IntermediateStorageTypeDef(TypedDict):
    s3Location: S3LocationTypeDef

class S3ContentTypeDef(TypedDict):
    s3Location: S3LocationTypeDef

SupplementalDataStorageLocationTypeDef = TypedDict(
    "SupplementalDataStorageLocationTypeDef",
    {
        "type": Literal["S3"],
        "s3Location": NotRequired[S3LocationTypeDef],
    },
)

class FlowConnectionConfigurationTypeDef(TypedDict):
    conditional: NotRequired[FlowConditionalConnectionConfigurationTypeDef]
    data: NotRequired[FlowDataConnectionConfigurationTypeDef]

class ListFlowsResponseTypeDef(TypedDict):
    flowSummaries: List[FlowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class FlowValidationDetailsTypeDef(TypedDict):
    cyclicConnection: NotRequired[CyclicConnectionFlowValidationDetailsTypeDef]
    duplicateConditionExpression: NotRequired[
        DuplicateConditionExpressionFlowValidationDetailsTypeDef
    ]
    duplicateConnections: NotRequired[DuplicateConnectionsFlowValidationDetailsTypeDef]
    incompatibleConnectionDataType: NotRequired[
        IncompatibleConnectionDataTypeFlowValidationDetailsTypeDef
    ]
    malformedConditionExpression: NotRequired[
        MalformedConditionExpressionFlowValidationDetailsTypeDef
    ]
    malformedNodeInputExpression: NotRequired[
        MalformedNodeInputExpressionFlowValidationDetailsTypeDef
    ]
    mismatchedNodeInputType: NotRequired[MismatchedNodeInputTypeFlowValidationDetailsTypeDef]
    mismatchedNodeOutputType: NotRequired[MismatchedNodeOutputTypeFlowValidationDetailsTypeDef]
    missingConnectionConfiguration: NotRequired[
        MissingConnectionConfigurationFlowValidationDetailsTypeDef
    ]
    missingDefaultCondition: NotRequired[MissingDefaultConditionFlowValidationDetailsTypeDef]
    missingEndingNodes: NotRequired[Dict[str, Any]]
    missingNodeConfiguration: NotRequired[MissingNodeConfigurationFlowValidationDetailsTypeDef]
    missingNodeInput: NotRequired[MissingNodeInputFlowValidationDetailsTypeDef]
    missingNodeOutput: NotRequired[MissingNodeOutputFlowValidationDetailsTypeDef]
    missingStartingNodes: NotRequired[Dict[str, Any]]
    multipleNodeInputConnections: NotRequired[
        MultipleNodeInputConnectionsFlowValidationDetailsTypeDef
    ]
    unfulfilledNodeInput: NotRequired[UnfulfilledNodeInputFlowValidationDetailsTypeDef]
    unknownConnectionCondition: NotRequired[UnknownConnectionConditionFlowValidationDetailsTypeDef]
    unknownConnectionSource: NotRequired[UnknownConnectionSourceFlowValidationDetailsTypeDef]
    unknownConnectionSourceOutput: NotRequired[
        UnknownConnectionSourceOutputFlowValidationDetailsTypeDef
    ]
    unknownConnectionTarget: NotRequired[UnknownConnectionTargetFlowValidationDetailsTypeDef]
    unknownConnectionTargetInput: NotRequired[
        UnknownConnectionTargetInputFlowValidationDetailsTypeDef
    ]
    unknownNodeInput: NotRequired[UnknownNodeInputFlowValidationDetailsTypeDef]
    unknownNodeOutput: NotRequired[UnknownNodeOutputFlowValidationDetailsTypeDef]
    unreachableNode: NotRequired[UnreachableNodeFlowValidationDetailsTypeDef]
    unsatisfiedConnectionConditions: NotRequired[
        UnsatisfiedConnectionConditionsFlowValidationDetailsTypeDef
    ]
    unspecified: NotRequired[Dict[str, Any]]

class ListFlowVersionsResponseTypeDef(TypedDict):
    flowVersionSummaries: List[FlowVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class FunctionOutputTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    parameters: NotRequired[Dict[str, ParameterDetailTypeDef]]
    requireConfirmation: NotRequired[RequireConfirmationType]

class FunctionTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    parameters: NotRequired[Mapping[str, ParameterDetailTypeDef]]
    requireConfirmation: NotRequired[RequireConfirmationType]

class HierarchicalChunkingConfigurationOutputTypeDef(TypedDict):
    levelConfigurations: List[HierarchicalChunkingLevelConfigurationTypeDef]
    overlapTokens: int

class HierarchicalChunkingConfigurationTypeDef(TypedDict):
    levelConfigurations: Sequence[HierarchicalChunkingLevelConfigurationTypeDef]
    overlapTokens: int

class PromptConfigurationOutputTypeDef(TypedDict):
    additionalModelRequestFields: NotRequired[Dict[str, Any]]
    basePromptTemplate: NotRequired[str]
    foundationModel: NotRequired[str]
    inferenceConfiguration: NotRequired[InferenceConfigurationOutputTypeDef]
    parserMode: NotRequired[CreationModeType]
    promptCreationMode: NotRequired[CreationModeType]
    promptState: NotRequired[PromptStateType]
    promptType: NotRequired[PromptTypeType]

class PromptConfigurationTypeDef(TypedDict):
    additionalModelRequestFields: NotRequired[Mapping[str, Any]]
    basePromptTemplate: NotRequired[str]
    foundationModel: NotRequired[str]
    inferenceConfiguration: NotRequired[InferenceConfigurationTypeDef]
    parserMode: NotRequired[CreationModeType]
    promptCreationMode: NotRequired[CreationModeType]
    promptState: NotRequired[PromptStateType]
    promptType: NotRequired[PromptTypeType]

class ListIngestionJobsRequestTypeDef(TypedDict):
    dataSourceId: str
    knowledgeBaseId: str
    filters: NotRequired[Sequence[IngestionJobFilterTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortBy: NotRequired[IngestionJobSortByTypeDef]

class IngestionJobSummaryTypeDef(TypedDict):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str
    startedAt: datetime
    status: IngestionJobStatusType
    updatedAt: datetime
    description: NotRequired[str]
    statistics: NotRequired[IngestionJobStatisticsTypeDef]

class IngestionJobTypeDef(TypedDict):
    dataSourceId: str
    ingestionJobId: str
    knowledgeBaseId: str
    startedAt: datetime
    status: IngestionJobStatusType
    updatedAt: datetime
    description: NotRequired[str]
    failureReasons: NotRequired[List[str]]
    statistics: NotRequired[IngestionJobStatisticsTypeDef]

class ListKnowledgeBasesResponseTypeDef(TypedDict):
    knowledgeBaseSummaries: List[KnowledgeBaseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAgentActionGroupsRequestPaginateTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAgentAliasesRequestPaginateTypeDef(TypedDict):
    agentId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAgentCollaboratorsRequestPaginateTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAgentKnowledgeBasesRequestPaginateTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAgentVersionsRequestPaginateTypeDef(TypedDict):
    agentId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAgentsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataSourcesRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFlowAliasesRequestPaginateTypeDef(TypedDict):
    flowIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFlowVersionsRequestPaginateTypeDef(TypedDict):
    flowIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFlowsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIngestionJobsRequestPaginateTypeDef(TypedDict):
    dataSourceId: str
    knowledgeBaseId: str
    filters: NotRequired[Sequence[IngestionJobFilterTypeDef]]
    sortBy: NotRequired[IngestionJobSortByTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListKnowledgeBaseDocumentsRequestPaginateTypeDef(TypedDict):
    dataSourceId: str
    knowledgeBaseId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListKnowledgeBasesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPromptsRequestPaginateTypeDef(TypedDict):
    promptIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPromptsResponseTypeDef(TypedDict):
    promptSummaries: List[PromptSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class MemoryConfigurationOutputTypeDef(TypedDict):
    enabledMemoryTypes: List[Literal["SESSION_SUMMARY"]]
    sessionSummaryConfiguration: NotRequired[SessionSummaryConfigurationTypeDef]
    storageDays: NotRequired[int]

class MemoryConfigurationTypeDef(TypedDict):
    enabledMemoryTypes: Sequence[Literal["SESSION_SUMMARY"]]
    sessionSummaryConfiguration: NotRequired[SessionSummaryConfigurationTypeDef]
    storageDays: NotRequired[int]

class MetadataAttributeTypeDef(TypedDict):
    key: str
    value: MetadataAttributeValueTypeDef

class MongoDbAtlasConfigurationTypeDef(TypedDict):
    collectionName: str
    credentialsSecretArn: str
    databaseName: str
    endpoint: str
    fieldMapping: MongoDbAtlasFieldMappingTypeDef
    vectorIndexName: str
    endpointServiceName: NotRequired[str]
    textIndexName: NotRequired[str]

class NeptuneAnalyticsConfigurationTypeDef(TypedDict):
    fieldMapping: NeptuneAnalyticsFieldMappingTypeDef
    graphArn: str

class OpenSearchManagedClusterConfigurationTypeDef(TypedDict):
    domainArn: str
    domainEndpoint: str
    fieldMapping: OpenSearchManagedClusterFieldMappingTypeDef
    vectorIndexName: str

class OpenSearchServerlessConfigurationTypeDef(TypedDict):
    collectionArn: str
    fieldMapping: OpenSearchServerlessFieldMappingTypeDef
    vectorIndexName: str

class PatternObjectFilterConfigurationOutputTypeDef(TypedDict):
    filters: List[PatternObjectFilterOutputTypeDef]

class PatternObjectFilterConfigurationTypeDef(TypedDict):
    filters: Sequence[PatternObjectFilterTypeDef]

class PineconeConfigurationTypeDef(TypedDict):
    connectionString: str
    credentialsSecretArn: str
    fieldMapping: PineconeFieldMappingTypeDef
    namespace: NotRequired[str]

class PromptGenAiResourceTypeDef(TypedDict):
    agent: NotRequired[PromptAgentResourceTypeDef]

class PromptInferenceConfigurationOutputTypeDef(TypedDict):
    text: NotRequired[PromptModelInferenceConfigurationOutputTypeDef]

PromptModelInferenceConfigurationUnionTypeDef = Union[
    PromptModelInferenceConfigurationTypeDef, PromptModelInferenceConfigurationOutputTypeDef
]

class QueryGenerationTableOutputTypeDef(TypedDict):
    name: str
    columns: NotRequired[List[QueryGenerationColumnTypeDef]]
    description: NotRequired[str]
    inclusion: NotRequired[IncludeExcludeType]

class QueryGenerationTableTypeDef(TypedDict):
    name: str
    columns: NotRequired[Sequence[QueryGenerationColumnTypeDef]]
    description: NotRequired[str]
    inclusion: NotRequired[IncludeExcludeType]

class RdsConfigurationTypeDef(TypedDict):
    credentialsSecretArn: str
    databaseName: str
    fieldMapping: RdsFieldMappingTypeDef
    resourceArn: str
    tableName: str

class RedisEnterpriseCloudConfigurationTypeDef(TypedDict):
    credentialsSecretArn: str
    endpoint: str
    fieldMapping: RedisEnterpriseCloudFieldMappingTypeDef
    vectorIndexName: str

class RedshiftProvisionedConfigurationTypeDef(TypedDict):
    authConfiguration: RedshiftProvisionedAuthConfigurationTypeDef
    clusterIdentifier: str

RedshiftQueryEngineStorageConfigurationOutputTypeDef = TypedDict(
    "RedshiftQueryEngineStorageConfigurationOutputTypeDef",
    {
        "type": RedshiftQueryEngineStorageTypeType,
        "awsDataCatalogConfiguration": NotRequired[
            RedshiftQueryEngineAwsDataCatalogStorageConfigurationOutputTypeDef
        ],
        "redshiftConfiguration": NotRequired[
            RedshiftQueryEngineRedshiftStorageConfigurationTypeDef
        ],
    },
)
RedshiftQueryEngineStorageConfigurationTypeDef = TypedDict(
    "RedshiftQueryEngineStorageConfigurationTypeDef",
    {
        "type": RedshiftQueryEngineStorageTypeType,
        "awsDataCatalogConfiguration": NotRequired[
            RedshiftQueryEngineAwsDataCatalogStorageConfigurationTypeDef
        ],
        "redshiftConfiguration": NotRequired[
            RedshiftQueryEngineRedshiftStorageConfigurationTypeDef
        ],
    },
)

class RedshiftServerlessConfigurationTypeDef(TypedDict):
    authConfiguration: RedshiftServerlessAuthConfigurationTypeDef
    workgroupArn: str

class RetrievalFlowNodeServiceConfigurationTypeDef(TypedDict):
    s3: NotRequired[RetrievalFlowNodeS3ConfigurationTypeDef]

class UrlConfigurationOutputTypeDef(TypedDict):
    seedUrls: NotRequired[List[SeedUrlTypeDef]]

class UrlConfigurationTypeDef(TypedDict):
    seedUrls: NotRequired[Sequence[SeedUrlTypeDef]]

ToolChoiceOutputTypeDef = TypedDict(
    "ToolChoiceOutputTypeDef",
    {
        "any": NotRequired[Dict[str, Any]],
        "auto": NotRequired[Dict[str, Any]],
        "tool": NotRequired[SpecificToolChoiceTypeDef],
    },
)
ToolChoiceTypeDef = TypedDict(
    "ToolChoiceTypeDef",
    {
        "any": NotRequired[Mapping[str, Any]],
        "auto": NotRequired[Mapping[str, Any]],
        "tool": NotRequired[SpecificToolChoiceTypeDef],
    },
)

class StorageFlowNodeServiceConfigurationTypeDef(TypedDict):
    s3: NotRequired[StorageFlowNodeS3ConfigurationTypeDef]

class ToolSpecificationOutputTypeDef(TypedDict):
    inputSchema: ToolInputSchemaOutputTypeDef
    name: str
    description: NotRequired[str]

ToolInputSchemaUnionTypeDef = Union[ToolInputSchemaTypeDef, ToolInputSchemaOutputTypeDef]

class TransformationFunctionTypeDef(TypedDict):
    transformationLambdaConfiguration: TransformationLambdaConfigurationTypeDef

class WebCrawlerConfigurationOutputTypeDef(TypedDict):
    crawlerLimits: NotRequired[WebCrawlerLimitsTypeDef]
    exclusionFilters: NotRequired[List[str]]
    inclusionFilters: NotRequired[List[str]]
    scope: NotRequired[WebScopeTypeType]
    userAgent: NotRequired[str]
    userAgentHeader: NotRequired[str]

class WebCrawlerConfigurationTypeDef(TypedDict):
    crawlerLimits: NotRequired[WebCrawlerLimitsTypeDef]
    exclusionFilters: NotRequired[Sequence[str]]
    inclusionFilters: NotRequired[Sequence[str]]
    scope: NotRequired[WebScopeTypeType]
    userAgent: NotRequired[str]
    userAgentHeader: NotRequired[str]

class AgentAliasTypeDef(TypedDict):
    agentAliasArn: str
    agentAliasId: str
    agentAliasName: str
    agentAliasStatus: AgentAliasStatusType
    agentId: str
    createdAt: datetime
    routingConfiguration: List[AgentAliasRoutingConfigurationListItemTypeDef]
    updatedAt: datetime
    agentAliasHistoryEvents: NotRequired[List[AgentAliasHistoryEventTypeDef]]
    clientToken: NotRequired[str]
    description: NotRequired[str]
    failureReasons: NotRequired[List[str]]

class ListAgentAliasesResponseTypeDef(TypedDict):
    agentAliasSummaries: List[AgentAliasSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAgentCollaboratorsResponseTypeDef(TypedDict):
    agentCollaboratorSummaries: List[AgentCollaboratorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AssociateAgentCollaboratorResponseTypeDef(TypedDict):
    agentCollaborator: AgentCollaboratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentCollaboratorResponseTypeDef(TypedDict):
    agentCollaborator: AgentCollaboratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgentCollaboratorResponseTypeDef(TypedDict):
    agentCollaborator: AgentCollaboratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAgentsResponseTypeDef(TypedDict):
    agentSummaries: List[AgentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAgentVersionsResponseTypeDef(TypedDict):
    agentVersionSummaries: List[AgentVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ParsingConfigurationTypeDef(TypedDict):
    parsingStrategy: ParsingStrategyType
    bedrockDataAutomationConfiguration: NotRequired[BedrockDataAutomationConfigurationTypeDef]
    bedrockFoundationModelConfiguration: NotRequired[BedrockFoundationModelConfigurationTypeDef]

ContextEnrichmentConfigurationTypeDef = TypedDict(
    "ContextEnrichmentConfigurationTypeDef",
    {
        "type": Literal["BEDROCK_FOUNDATION_MODEL"],
        "bedrockFoundationModelConfiguration": NotRequired[
            BedrockFoundationModelContextEnrichmentConfigurationTypeDef
        ],
    },
)
InlineContentTypeDef = TypedDict(
    "InlineContentTypeDef",
    {
        "type": InlineContentTypeType,
        "byteContent": NotRequired[ByteContentDocTypeDef],
        "textContent": NotRequired[TextContentDocTypeDef],
    },
)

class MessageOutputTypeDef(TypedDict):
    content: List[ContentBlockTypeDef]
    role: ConversationRoleType

class MessageTypeDef(TypedDict):
    content: Sequence[ContentBlockTypeDef]
    role: ConversationRoleType

TextPromptTemplateConfigurationUnionTypeDef = Union[
    TextPromptTemplateConfigurationTypeDef, TextPromptTemplateConfigurationOutputTypeDef
]

class ListFlowAliasesResponseTypeDef(TypedDict):
    flowAliasSummaries: List[FlowAliasSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DeleteKnowledgeBaseDocumentsRequestTypeDef(TypedDict):
    dataSourceId: str
    documentIdentifiers: Sequence[DocumentIdentifierTypeDef]
    knowledgeBaseId: str
    clientToken: NotRequired[str]

class GetKnowledgeBaseDocumentsRequestTypeDef(TypedDict):
    dataSourceId: str
    documentIdentifiers: Sequence[DocumentIdentifierTypeDef]
    knowledgeBaseId: str

class KnowledgeBaseDocumentDetailTypeDef(TypedDict):
    dataSourceId: str
    identifier: DocumentIdentifierTypeDef
    knowledgeBaseId: str
    status: DocumentStatusType
    statusReason: NotRequired[str]
    updatedAt: NotRequired[datetime]

class SupplementalDataStorageConfigurationOutputTypeDef(TypedDict):
    storageLocations: List[SupplementalDataStorageLocationTypeDef]

class SupplementalDataStorageConfigurationTypeDef(TypedDict):
    storageLocations: Sequence[SupplementalDataStorageLocationTypeDef]

FlowConnectionTypeDef = TypedDict(
    "FlowConnectionTypeDef",
    {
        "name": str,
        "source": str,
        "target": str,
        "type": FlowConnectionTypeType,
        "configuration": NotRequired[FlowConnectionConfigurationTypeDef],
    },
)
FlowValidationTypeDef = TypedDict(
    "FlowValidationTypeDef",
    {
        "message": str,
        "severity": FlowValidationSeverityType,
        "details": NotRequired[FlowValidationDetailsTypeDef],
        "type": NotRequired[FlowValidationTypeType],
    },
)

class FunctionSchemaOutputTypeDef(TypedDict):
    functions: NotRequired[List[FunctionOutputTypeDef]]

class FunctionSchemaTypeDef(TypedDict):
    functions: NotRequired[Sequence[FunctionTypeDef]]

class ChunkingConfigurationOutputTypeDef(TypedDict):
    chunkingStrategy: ChunkingStrategyType
    fixedSizeChunkingConfiguration: NotRequired[FixedSizeChunkingConfigurationTypeDef]
    hierarchicalChunkingConfiguration: NotRequired[HierarchicalChunkingConfigurationOutputTypeDef]
    semanticChunkingConfiguration: NotRequired[SemanticChunkingConfigurationTypeDef]

class ChunkingConfigurationTypeDef(TypedDict):
    chunkingStrategy: ChunkingStrategyType
    fixedSizeChunkingConfiguration: NotRequired[FixedSizeChunkingConfigurationTypeDef]
    hierarchicalChunkingConfiguration: NotRequired[HierarchicalChunkingConfigurationTypeDef]
    semanticChunkingConfiguration: NotRequired[SemanticChunkingConfigurationTypeDef]

class PromptOverrideConfigurationOutputTypeDef(TypedDict):
    promptConfigurations: List[PromptConfigurationOutputTypeDef]
    overrideLambda: NotRequired[str]

class PromptOverrideConfigurationTypeDef(TypedDict):
    promptConfigurations: Sequence[PromptConfigurationTypeDef]
    overrideLambda: NotRequired[str]

class ListIngestionJobsResponseTypeDef(TypedDict):
    ingestionJobSummaries: List[IngestionJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetIngestionJobResponseTypeDef(TypedDict):
    ingestionJob: IngestionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartIngestionJobResponseTypeDef(TypedDict):
    ingestionJob: IngestionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopIngestionJobResponseTypeDef(TypedDict):
    ingestionJob: IngestionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

MemoryConfigurationUnionTypeDef = Union[
    MemoryConfigurationTypeDef, MemoryConfigurationOutputTypeDef
]
DocumentMetadataTypeDef = TypedDict(
    "DocumentMetadataTypeDef",
    {
        "type": MetadataSourceTypeType,
        "inlineAttributes": NotRequired[Sequence[MetadataAttributeTypeDef]],
        "s3Location": NotRequired[CustomS3LocationTypeDef],
    },
)
CrawlFilterConfigurationOutputTypeDef = TypedDict(
    "CrawlFilterConfigurationOutputTypeDef",
    {
        "type": Literal["PATTERN"],
        "patternObjectFilter": NotRequired[PatternObjectFilterConfigurationOutputTypeDef],
    },
)
CrawlFilterConfigurationTypeDef = TypedDict(
    "CrawlFilterConfigurationTypeDef",
    {
        "type": Literal["PATTERN"],
        "patternObjectFilter": NotRequired[PatternObjectFilterConfigurationTypeDef],
    },
)

class PromptInferenceConfigurationTypeDef(TypedDict):
    text: NotRequired[PromptModelInferenceConfigurationUnionTypeDef]

class QueryGenerationContextOutputTypeDef(TypedDict):
    curatedQueries: NotRequired[List[CuratedQueryTypeDef]]
    tables: NotRequired[List[QueryGenerationTableOutputTypeDef]]

class QueryGenerationContextTypeDef(TypedDict):
    curatedQueries: NotRequired[Sequence[CuratedQueryTypeDef]]
    tables: NotRequired[Sequence[QueryGenerationTableTypeDef]]

StorageConfigurationTypeDef = TypedDict(
    "StorageConfigurationTypeDef",
    {
        "type": KnowledgeBaseStorageTypeType,
        "mongoDbAtlasConfiguration": NotRequired[MongoDbAtlasConfigurationTypeDef],
        "neptuneAnalyticsConfiguration": NotRequired[NeptuneAnalyticsConfigurationTypeDef],
        "opensearchManagedClusterConfiguration": NotRequired[
            OpenSearchManagedClusterConfigurationTypeDef
        ],
        "opensearchServerlessConfiguration": NotRequired[OpenSearchServerlessConfigurationTypeDef],
        "pineconeConfiguration": NotRequired[PineconeConfigurationTypeDef],
        "rdsConfiguration": NotRequired[RdsConfigurationTypeDef],
        "redisEnterpriseCloudConfiguration": NotRequired[RedisEnterpriseCloudConfigurationTypeDef],
    },
)
RedshiftQueryEngineConfigurationTypeDef = TypedDict(
    "RedshiftQueryEngineConfigurationTypeDef",
    {
        "type": RedshiftQueryEngineTypeType,
        "provisionedConfiguration": NotRequired[RedshiftProvisionedConfigurationTypeDef],
        "serverlessConfiguration": NotRequired[RedshiftServerlessConfigurationTypeDef],
    },
)

class RetrievalFlowNodeConfigurationTypeDef(TypedDict):
    serviceConfiguration: RetrievalFlowNodeServiceConfigurationTypeDef

class WebSourceConfigurationOutputTypeDef(TypedDict):
    urlConfiguration: UrlConfigurationOutputTypeDef

class WebSourceConfigurationTypeDef(TypedDict):
    urlConfiguration: UrlConfigurationTypeDef

ToolChoiceUnionTypeDef = Union[ToolChoiceTypeDef, ToolChoiceOutputTypeDef]

class StorageFlowNodeConfigurationTypeDef(TypedDict):
    serviceConfiguration: StorageFlowNodeServiceConfigurationTypeDef

class ToolOutputTypeDef(TypedDict):
    cachePoint: NotRequired[CachePointBlockTypeDef]
    toolSpec: NotRequired[ToolSpecificationOutputTypeDef]

class ToolSpecificationTypeDef(TypedDict):
    inputSchema: ToolInputSchemaUnionTypeDef
    name: str
    description: NotRequired[str]

class TransformationTypeDef(TypedDict):
    stepToApply: Literal["POST_CHUNKING"]
    transformationFunction: TransformationFunctionTypeDef

class CreateAgentAliasResponseTypeDef(TypedDict):
    agentAlias: AgentAliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentAliasResponseTypeDef(TypedDict):
    agentAlias: AgentAliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgentAliasResponseTypeDef(TypedDict):
    agentAlias: AgentAliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CustomContentTypeDef(TypedDict):
    customDocumentIdentifier: CustomDocumentIdentifierTypeDef
    sourceType: CustomSourceTypeType
    inlineContent: NotRequired[InlineContentTypeDef]
    s3Location: NotRequired[CustomS3LocationTypeDef]

MessageUnionTypeDef = Union[MessageTypeDef, MessageOutputTypeDef]

class DeleteKnowledgeBaseDocumentsResponseTypeDef(TypedDict):
    documentDetails: List[KnowledgeBaseDocumentDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetKnowledgeBaseDocumentsResponseTypeDef(TypedDict):
    documentDetails: List[KnowledgeBaseDocumentDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IngestKnowledgeBaseDocumentsResponseTypeDef(TypedDict):
    documentDetails: List[KnowledgeBaseDocumentDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListKnowledgeBaseDocumentsResponseTypeDef(TypedDict):
    documentDetails: List[KnowledgeBaseDocumentDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class VectorKnowledgeBaseConfigurationOutputTypeDef(TypedDict):
    embeddingModelArn: str
    embeddingModelConfiguration: NotRequired[EmbeddingModelConfigurationTypeDef]
    supplementalDataStorageConfiguration: NotRequired[
        SupplementalDataStorageConfigurationOutputTypeDef
    ]

class VectorKnowledgeBaseConfigurationTypeDef(TypedDict):
    embeddingModelArn: str
    embeddingModelConfiguration: NotRequired[EmbeddingModelConfigurationTypeDef]
    supplementalDataStorageConfiguration: NotRequired[SupplementalDataStorageConfigurationTypeDef]

class ValidateFlowDefinitionResponseTypeDef(TypedDict):
    validations: List[FlowValidationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AgentActionGroupTypeDef(TypedDict):
    actionGroupId: str
    actionGroupName: str
    actionGroupState: ActionGroupStateType
    agentId: str
    agentVersion: str
    createdAt: datetime
    updatedAt: datetime
    actionGroupExecutor: NotRequired[ActionGroupExecutorTypeDef]
    apiSchema: NotRequired[APISchemaTypeDef]
    clientToken: NotRequired[str]
    description: NotRequired[str]
    functionSchema: NotRequired[FunctionSchemaOutputTypeDef]
    parentActionGroupSignatureParams: NotRequired[Dict[str, str]]
    parentActionSignature: NotRequired[ActionGroupSignatureType]

FunctionSchemaUnionTypeDef = Union[FunctionSchemaTypeDef, FunctionSchemaOutputTypeDef]

class AgentTypeDef(TypedDict):
    agentArn: str
    agentId: str
    agentName: str
    agentResourceRoleArn: str
    agentStatus: AgentStatusType
    agentVersion: str
    createdAt: datetime
    idleSessionTTLInSeconds: int
    updatedAt: datetime
    agentCollaboration: NotRequired[AgentCollaborationType]
    clientToken: NotRequired[str]
    customOrchestration: NotRequired[CustomOrchestrationTypeDef]
    customerEncryptionKeyArn: NotRequired[str]
    description: NotRequired[str]
    failureReasons: NotRequired[List[str]]
    foundationModel: NotRequired[str]
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]
    instruction: NotRequired[str]
    memoryConfiguration: NotRequired[MemoryConfigurationOutputTypeDef]
    orchestrationType: NotRequired[OrchestrationTypeType]
    preparedAt: NotRequired[datetime]
    promptOverrideConfiguration: NotRequired[PromptOverrideConfigurationOutputTypeDef]
    recommendedActions: NotRequired[List[str]]

class AgentVersionTypeDef(TypedDict):
    agentArn: str
    agentId: str
    agentName: str
    agentResourceRoleArn: str
    agentStatus: AgentStatusType
    createdAt: datetime
    idleSessionTTLInSeconds: int
    updatedAt: datetime
    version: str
    agentCollaboration: NotRequired[AgentCollaborationType]
    customerEncryptionKeyArn: NotRequired[str]
    description: NotRequired[str]
    failureReasons: NotRequired[List[str]]
    foundationModel: NotRequired[str]
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]
    instruction: NotRequired[str]
    memoryConfiguration: NotRequired[MemoryConfigurationOutputTypeDef]
    promptOverrideConfiguration: NotRequired[PromptOverrideConfigurationOutputTypeDef]
    recommendedActions: NotRequired[List[str]]

PromptOverrideConfigurationUnionTypeDef = Union[
    PromptOverrideConfigurationTypeDef, PromptOverrideConfigurationOutputTypeDef
]

class ConfluenceCrawlerConfigurationOutputTypeDef(TypedDict):
    filterConfiguration: NotRequired[CrawlFilterConfigurationOutputTypeDef]

class SalesforceCrawlerConfigurationOutputTypeDef(TypedDict):
    filterConfiguration: NotRequired[CrawlFilterConfigurationOutputTypeDef]

class SharePointCrawlerConfigurationOutputTypeDef(TypedDict):
    filterConfiguration: NotRequired[CrawlFilterConfigurationOutputTypeDef]

class ConfluenceCrawlerConfigurationTypeDef(TypedDict):
    filterConfiguration: NotRequired[CrawlFilterConfigurationTypeDef]

class SalesforceCrawlerConfigurationTypeDef(TypedDict):
    filterConfiguration: NotRequired[CrawlFilterConfigurationTypeDef]

class SharePointCrawlerConfigurationTypeDef(TypedDict):
    filterConfiguration: NotRequired[CrawlFilterConfigurationTypeDef]

PromptInferenceConfigurationUnionTypeDef = Union[
    PromptInferenceConfigurationTypeDef, PromptInferenceConfigurationOutputTypeDef
]

class QueryGenerationConfigurationOutputTypeDef(TypedDict):
    executionTimeoutSeconds: NotRequired[int]
    generationContext: NotRequired[QueryGenerationContextOutputTypeDef]

class QueryGenerationConfigurationTypeDef(TypedDict):
    executionTimeoutSeconds: NotRequired[int]
    generationContext: NotRequired[QueryGenerationContextTypeDef]

class WebDataSourceConfigurationOutputTypeDef(TypedDict):
    sourceConfiguration: WebSourceConfigurationOutputTypeDef
    crawlerConfiguration: NotRequired[WebCrawlerConfigurationOutputTypeDef]

class WebDataSourceConfigurationTypeDef(TypedDict):
    sourceConfiguration: WebSourceConfigurationTypeDef
    crawlerConfiguration: NotRequired[WebCrawlerConfigurationTypeDef]

class ToolConfigurationOutputTypeDef(TypedDict):
    tools: List[ToolOutputTypeDef]
    toolChoice: NotRequired[ToolChoiceOutputTypeDef]

ToolSpecificationUnionTypeDef = Union[ToolSpecificationTypeDef, ToolSpecificationOutputTypeDef]

class CustomTransformationConfigurationOutputTypeDef(TypedDict):
    intermediateStorage: IntermediateStorageTypeDef
    transformations: List[TransformationTypeDef]

class CustomTransformationConfigurationTypeDef(TypedDict):
    intermediateStorage: IntermediateStorageTypeDef
    transformations: Sequence[TransformationTypeDef]

class DocumentContentTypeDef(TypedDict):
    dataSourceType: ContentDataSourceTypeType
    custom: NotRequired[CustomContentTypeDef]
    s3: NotRequired[S3ContentTypeDef]

class CreateAgentActionGroupResponseTypeDef(TypedDict):
    agentActionGroup: AgentActionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentActionGroupResponseTypeDef(TypedDict):
    agentActionGroup: AgentActionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgentActionGroupResponseTypeDef(TypedDict):
    agentActionGroup: AgentActionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAgentActionGroupRequestTypeDef(TypedDict):
    actionGroupName: str
    agentId: str
    agentVersion: str
    actionGroupExecutor: NotRequired[ActionGroupExecutorTypeDef]
    actionGroupState: NotRequired[ActionGroupStateType]
    apiSchema: NotRequired[APISchemaTypeDef]
    clientToken: NotRequired[str]
    description: NotRequired[str]
    functionSchema: NotRequired[FunctionSchemaUnionTypeDef]
    parentActionGroupSignature: NotRequired[ActionGroupSignatureType]
    parentActionGroupSignatureParams: NotRequired[Mapping[str, str]]

class UpdateAgentActionGroupRequestTypeDef(TypedDict):
    actionGroupId: str
    actionGroupName: str
    agentId: str
    agentVersion: str
    actionGroupExecutor: NotRequired[ActionGroupExecutorTypeDef]
    actionGroupState: NotRequired[ActionGroupStateType]
    apiSchema: NotRequired[APISchemaTypeDef]
    description: NotRequired[str]
    functionSchema: NotRequired[FunctionSchemaUnionTypeDef]
    parentActionGroupSignature: NotRequired[ActionGroupSignatureType]
    parentActionGroupSignatureParams: NotRequired[Mapping[str, str]]

class CreateAgentResponseTypeDef(TypedDict):
    agent: AgentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentResponseTypeDef(TypedDict):
    agent: AgentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgentResponseTypeDef(TypedDict):
    agent: AgentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentVersionResponseTypeDef(TypedDict):
    agentVersion: AgentVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAgentRequestTypeDef(TypedDict):
    agentName: str
    agentCollaboration: NotRequired[AgentCollaborationType]
    agentResourceRoleArn: NotRequired[str]
    clientToken: NotRequired[str]
    customOrchestration: NotRequired[CustomOrchestrationTypeDef]
    customerEncryptionKeyArn: NotRequired[str]
    description: NotRequired[str]
    foundationModel: NotRequired[str]
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]
    idleSessionTTLInSeconds: NotRequired[int]
    instruction: NotRequired[str]
    memoryConfiguration: NotRequired[MemoryConfigurationUnionTypeDef]
    orchestrationType: NotRequired[OrchestrationTypeType]
    promptOverrideConfiguration: NotRequired[PromptOverrideConfigurationUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]

class UpdateAgentRequestTypeDef(TypedDict):
    agentId: str
    agentName: str
    agentResourceRoleArn: str
    foundationModel: str
    agentCollaboration: NotRequired[AgentCollaborationType]
    customOrchestration: NotRequired[CustomOrchestrationTypeDef]
    customerEncryptionKeyArn: NotRequired[str]
    description: NotRequired[str]
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]
    idleSessionTTLInSeconds: NotRequired[int]
    instruction: NotRequired[str]
    memoryConfiguration: NotRequired[MemoryConfigurationUnionTypeDef]
    orchestrationType: NotRequired[OrchestrationTypeType]
    promptOverrideConfiguration: NotRequired[PromptOverrideConfigurationUnionTypeDef]

class ConfluenceDataSourceConfigurationOutputTypeDef(TypedDict):
    sourceConfiguration: ConfluenceSourceConfigurationTypeDef
    crawlerConfiguration: NotRequired[ConfluenceCrawlerConfigurationOutputTypeDef]

class SalesforceDataSourceConfigurationOutputTypeDef(TypedDict):
    sourceConfiguration: SalesforceSourceConfigurationTypeDef
    crawlerConfiguration: NotRequired[SalesforceCrawlerConfigurationOutputTypeDef]

class SharePointDataSourceConfigurationOutputTypeDef(TypedDict):
    sourceConfiguration: SharePointSourceConfigurationOutputTypeDef
    crawlerConfiguration: NotRequired[SharePointCrawlerConfigurationOutputTypeDef]

class ConfluenceDataSourceConfigurationTypeDef(TypedDict):
    sourceConfiguration: ConfluenceSourceConfigurationTypeDef
    crawlerConfiguration: NotRequired[ConfluenceCrawlerConfigurationTypeDef]

class SalesforceDataSourceConfigurationTypeDef(TypedDict):
    sourceConfiguration: SalesforceSourceConfigurationTypeDef
    crawlerConfiguration: NotRequired[SalesforceCrawlerConfigurationTypeDef]

class SharePointDataSourceConfigurationTypeDef(TypedDict):
    sourceConfiguration: SharePointSourceConfigurationTypeDef
    crawlerConfiguration: NotRequired[SharePointCrawlerConfigurationTypeDef]

class RedshiftConfigurationOutputTypeDef(TypedDict):
    queryEngineConfiguration: RedshiftQueryEngineConfigurationTypeDef
    storageConfigurations: List[RedshiftQueryEngineStorageConfigurationOutputTypeDef]
    queryGenerationConfiguration: NotRequired[QueryGenerationConfigurationOutputTypeDef]

class RedshiftConfigurationTypeDef(TypedDict):
    queryEngineConfiguration: RedshiftQueryEngineConfigurationTypeDef
    storageConfigurations: Sequence[RedshiftQueryEngineStorageConfigurationTypeDef]
    queryGenerationConfiguration: NotRequired[QueryGenerationConfigurationTypeDef]

class ChatPromptTemplateConfigurationOutputTypeDef(TypedDict):
    messages: List[MessageOutputTypeDef]
    inputVariables: NotRequired[List[PromptInputVariableTypeDef]]
    system: NotRequired[List[SystemContentBlockTypeDef]]
    toolConfiguration: NotRequired[ToolConfigurationOutputTypeDef]

class ToolTypeDef(TypedDict):
    cachePoint: NotRequired[CachePointBlockTypeDef]
    toolSpec: NotRequired[ToolSpecificationUnionTypeDef]

class VectorIngestionConfigurationOutputTypeDef(TypedDict):
    chunkingConfiguration: NotRequired[ChunkingConfigurationOutputTypeDef]
    contextEnrichmentConfiguration: NotRequired[ContextEnrichmentConfigurationTypeDef]
    customTransformationConfiguration: NotRequired[CustomTransformationConfigurationOutputTypeDef]
    parsingConfiguration: NotRequired[ParsingConfigurationTypeDef]

class VectorIngestionConfigurationTypeDef(TypedDict):
    chunkingConfiguration: NotRequired[ChunkingConfigurationTypeDef]
    contextEnrichmentConfiguration: NotRequired[ContextEnrichmentConfigurationTypeDef]
    customTransformationConfiguration: NotRequired[CustomTransformationConfigurationTypeDef]
    parsingConfiguration: NotRequired[ParsingConfigurationTypeDef]

class KnowledgeBaseDocumentTypeDef(TypedDict):
    content: DocumentContentTypeDef
    metadata: NotRequired[DocumentMetadataTypeDef]

DataSourceConfigurationOutputTypeDef = TypedDict(
    "DataSourceConfigurationOutputTypeDef",
    {
        "type": DataSourceTypeType,
        "confluenceConfiguration": NotRequired[ConfluenceDataSourceConfigurationOutputTypeDef],
        "s3Configuration": NotRequired[S3DataSourceConfigurationOutputTypeDef],
        "salesforceConfiguration": NotRequired[SalesforceDataSourceConfigurationOutputTypeDef],
        "sharePointConfiguration": NotRequired[SharePointDataSourceConfigurationOutputTypeDef],
        "webConfiguration": NotRequired[WebDataSourceConfigurationOutputTypeDef],
    },
)
DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef",
    {
        "type": DataSourceTypeType,
        "confluenceConfiguration": NotRequired[ConfluenceDataSourceConfigurationTypeDef],
        "s3Configuration": NotRequired[S3DataSourceConfigurationTypeDef],
        "salesforceConfiguration": NotRequired[SalesforceDataSourceConfigurationTypeDef],
        "sharePointConfiguration": NotRequired[SharePointDataSourceConfigurationTypeDef],
        "webConfiguration": NotRequired[WebDataSourceConfigurationTypeDef],
    },
)
SqlKnowledgeBaseConfigurationOutputTypeDef = TypedDict(
    "SqlKnowledgeBaseConfigurationOutputTypeDef",
    {
        "type": Literal["REDSHIFT"],
        "redshiftConfiguration": NotRequired[RedshiftConfigurationOutputTypeDef],
    },
)
SqlKnowledgeBaseConfigurationTypeDef = TypedDict(
    "SqlKnowledgeBaseConfigurationTypeDef",
    {
        "type": Literal["REDSHIFT"],
        "redshiftConfiguration": NotRequired[RedshiftConfigurationTypeDef],
    },
)

class PromptTemplateConfigurationOutputTypeDef(TypedDict):
    chat: NotRequired[ChatPromptTemplateConfigurationOutputTypeDef]
    text: NotRequired[TextPromptTemplateConfigurationOutputTypeDef]

ToolUnionTypeDef = Union[ToolTypeDef, ToolOutputTypeDef]
VectorIngestionConfigurationUnionTypeDef = Union[
    VectorIngestionConfigurationTypeDef, VectorIngestionConfigurationOutputTypeDef
]

class IngestKnowledgeBaseDocumentsRequestTypeDef(TypedDict):
    dataSourceId: str
    documents: Sequence[KnowledgeBaseDocumentTypeDef]
    knowledgeBaseId: str
    clientToken: NotRequired[str]

class DataSourceTypeDef(TypedDict):
    createdAt: datetime
    dataSourceConfiguration: DataSourceConfigurationOutputTypeDef
    dataSourceId: str
    knowledgeBaseId: str
    name: str
    status: DataSourceStatusType
    updatedAt: datetime
    dataDeletionPolicy: NotRequired[DataDeletionPolicyType]
    description: NotRequired[str]
    failureReasons: NotRequired[List[str]]
    serverSideEncryptionConfiguration: NotRequired[ServerSideEncryptionConfigurationTypeDef]
    vectorIngestionConfiguration: NotRequired[VectorIngestionConfigurationOutputTypeDef]

DataSourceConfigurationUnionTypeDef = Union[
    DataSourceConfigurationTypeDef, DataSourceConfigurationOutputTypeDef
]
KnowledgeBaseConfigurationOutputTypeDef = TypedDict(
    "KnowledgeBaseConfigurationOutputTypeDef",
    {
        "type": KnowledgeBaseTypeType,
        "kendraKnowledgeBaseConfiguration": NotRequired[KendraKnowledgeBaseConfigurationTypeDef],
        "sqlKnowledgeBaseConfiguration": NotRequired[SqlKnowledgeBaseConfigurationOutputTypeDef],
        "vectorKnowledgeBaseConfiguration": NotRequired[
            VectorKnowledgeBaseConfigurationOutputTypeDef
        ],
    },
)
KnowledgeBaseConfigurationTypeDef = TypedDict(
    "KnowledgeBaseConfigurationTypeDef",
    {
        "type": KnowledgeBaseTypeType,
        "kendraKnowledgeBaseConfiguration": NotRequired[KendraKnowledgeBaseConfigurationTypeDef],
        "sqlKnowledgeBaseConfiguration": NotRequired[SqlKnowledgeBaseConfigurationTypeDef],
        "vectorKnowledgeBaseConfiguration": NotRequired[VectorKnowledgeBaseConfigurationTypeDef],
    },
)

class PromptFlowNodeInlineConfigurationOutputTypeDef(TypedDict):
    modelId: str
    templateConfiguration: PromptTemplateConfigurationOutputTypeDef
    templateType: PromptTemplateTypeType
    additionalModelRequestFields: NotRequired[Dict[str, Any]]
    inferenceConfiguration: NotRequired[PromptInferenceConfigurationOutputTypeDef]

class PromptVariantOutputTypeDef(TypedDict):
    name: str
    templateConfiguration: PromptTemplateConfigurationOutputTypeDef
    templateType: PromptTemplateTypeType
    additionalModelRequestFields: NotRequired[Dict[str, Any]]
    genAiResource: NotRequired[PromptGenAiResourceTypeDef]
    inferenceConfiguration: NotRequired[PromptInferenceConfigurationOutputTypeDef]
    metadata: NotRequired[List[PromptMetadataEntryTypeDef]]
    modelId: NotRequired[str]

class ToolConfigurationTypeDef(TypedDict):
    tools: Sequence[ToolUnionTypeDef]
    toolChoice: NotRequired[ToolChoiceUnionTypeDef]

class CreateDataSourceResponseTypeDef(TypedDict):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataSourceResponseTypeDef(TypedDict):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourceResponseTypeDef(TypedDict):
    dataSource: DataSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceRequestTypeDef(TypedDict):
    dataSourceConfiguration: DataSourceConfigurationUnionTypeDef
    knowledgeBaseId: str
    name: str
    clientToken: NotRequired[str]
    dataDeletionPolicy: NotRequired[DataDeletionPolicyType]
    description: NotRequired[str]
    serverSideEncryptionConfiguration: NotRequired[ServerSideEncryptionConfigurationTypeDef]
    vectorIngestionConfiguration: NotRequired[VectorIngestionConfigurationUnionTypeDef]

class UpdateDataSourceRequestTypeDef(TypedDict):
    dataSourceConfiguration: DataSourceConfigurationUnionTypeDef
    dataSourceId: str
    knowledgeBaseId: str
    name: str
    dataDeletionPolicy: NotRequired[DataDeletionPolicyType]
    description: NotRequired[str]
    serverSideEncryptionConfiguration: NotRequired[ServerSideEncryptionConfigurationTypeDef]
    vectorIngestionConfiguration: NotRequired[VectorIngestionConfigurationUnionTypeDef]

class KnowledgeBaseTypeDef(TypedDict):
    createdAt: datetime
    knowledgeBaseArn: str
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationOutputTypeDef
    knowledgeBaseId: str
    name: str
    roleArn: str
    status: KnowledgeBaseStatusType
    updatedAt: datetime
    description: NotRequired[str]
    failureReasons: NotRequired[List[str]]
    storageConfiguration: NotRequired[StorageConfigurationTypeDef]

KnowledgeBaseConfigurationUnionTypeDef = Union[
    KnowledgeBaseConfigurationTypeDef, KnowledgeBaseConfigurationOutputTypeDef
]

class PromptFlowNodeSourceConfigurationOutputTypeDef(TypedDict):
    inline: NotRequired[PromptFlowNodeInlineConfigurationOutputTypeDef]
    resource: NotRequired[PromptFlowNodeResourceConfigurationTypeDef]

CreatePromptResponseTypeDef = TypedDict(
    "CreatePromptResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "customerEncryptionKeyArn": str,
        "defaultVariant": str,
        "description": str,
        "id": str,
        "name": str,
        "updatedAt": datetime,
        "variants": List[PromptVariantOutputTypeDef],
        "version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePromptVersionResponseTypeDef = TypedDict(
    "CreatePromptVersionResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "customerEncryptionKeyArn": str,
        "defaultVariant": str,
        "description": str,
        "id": str,
        "name": str,
        "updatedAt": datetime,
        "variants": List[PromptVariantOutputTypeDef],
        "version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPromptResponseTypeDef = TypedDict(
    "GetPromptResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "customerEncryptionKeyArn": str,
        "defaultVariant": str,
        "description": str,
        "id": str,
        "name": str,
        "updatedAt": datetime,
        "variants": List[PromptVariantOutputTypeDef],
        "version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePromptResponseTypeDef = TypedDict(
    "UpdatePromptResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "customerEncryptionKeyArn": str,
        "defaultVariant": str,
        "description": str,
        "id": str,
        "name": str,
        "updatedAt": datetime,
        "variants": List[PromptVariantOutputTypeDef],
        "version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ToolConfigurationUnionTypeDef = Union[ToolConfigurationTypeDef, ToolConfigurationOutputTypeDef]

class CreateKnowledgeBaseResponseTypeDef(TypedDict):
    knowledgeBase: KnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetKnowledgeBaseResponseTypeDef(TypedDict):
    knowledgeBase: KnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKnowledgeBaseResponseTypeDef(TypedDict):
    knowledgeBase: KnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKnowledgeBaseRequestTypeDef(TypedDict):
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationUnionTypeDef
    name: str
    roleArn: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    storageConfiguration: NotRequired[StorageConfigurationTypeDef]
    tags: NotRequired[Mapping[str, str]]

class UpdateKnowledgeBaseRequestTypeDef(TypedDict):
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationUnionTypeDef
    knowledgeBaseId: str
    name: str
    roleArn: str
    description: NotRequired[str]
    storageConfiguration: NotRequired[StorageConfigurationTypeDef]

class PromptFlowNodeConfigurationOutputTypeDef(TypedDict):
    sourceConfiguration: PromptFlowNodeSourceConfigurationOutputTypeDef
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]

class ChatPromptTemplateConfigurationTypeDef(TypedDict):
    messages: Sequence[MessageUnionTypeDef]
    inputVariables: NotRequired[Sequence[PromptInputVariableTypeDef]]
    system: NotRequired[Sequence[SystemContentBlockTypeDef]]
    toolConfiguration: NotRequired[ToolConfigurationUnionTypeDef]

FlowNodeConfigurationOutputTypeDef = TypedDict(
    "FlowNodeConfigurationOutputTypeDef",
    {
        "agent": NotRequired[AgentFlowNodeConfigurationTypeDef],
        "collector": NotRequired[Dict[str, Any]],
        "condition": NotRequired[ConditionFlowNodeConfigurationOutputTypeDef],
        "inlineCode": NotRequired[InlineCodeFlowNodeConfigurationTypeDef],
        "input": NotRequired[Dict[str, Any]],
        "iterator": NotRequired[Dict[str, Any]],
        "knowledgeBase": NotRequired[KnowledgeBaseFlowNodeConfigurationTypeDef],
        "lambdaFunction": NotRequired[LambdaFunctionFlowNodeConfigurationTypeDef],
        "lex": NotRequired[LexFlowNodeConfigurationTypeDef],
        "output": NotRequired[Dict[str, Any]],
        "prompt": NotRequired[PromptFlowNodeConfigurationOutputTypeDef],
        "retrieval": NotRequired[RetrievalFlowNodeConfigurationTypeDef],
        "storage": NotRequired[StorageFlowNodeConfigurationTypeDef],
    },
)
ChatPromptTemplateConfigurationUnionTypeDef = Union[
    ChatPromptTemplateConfigurationTypeDef, ChatPromptTemplateConfigurationOutputTypeDef
]
FlowNodeExtraTypeDef = TypedDict(
    "FlowNodeExtraTypeDef",
    {
        "name": str,
        "type": FlowNodeTypeType,
        "configuration": NotRequired[FlowNodeConfigurationOutputTypeDef],
        "inputs": NotRequired[List[FlowNodeInputTypeDef]],
        "outputs": NotRequired[List[FlowNodeOutputTypeDef]],
    },
)

class PromptTemplateConfigurationTypeDef(TypedDict):
    chat: NotRequired[ChatPromptTemplateConfigurationUnionTypeDef]
    text: NotRequired[TextPromptTemplateConfigurationUnionTypeDef]

class FlowDefinitionOutputTypeDef(TypedDict):
    connections: NotRequired[List[FlowConnectionTypeDef]]
    nodes: NotRequired[List[FlowNodeExtraTypeDef]]

class PromptFlowNodeInlineConfigurationTypeDef(TypedDict):
    modelId: str
    templateConfiguration: PromptTemplateConfigurationTypeDef
    templateType: PromptTemplateTypeType
    additionalModelRequestFields: NotRequired[Mapping[str, Any]]
    inferenceConfiguration: NotRequired[PromptInferenceConfigurationTypeDef]

PromptTemplateConfigurationUnionTypeDef = Union[
    PromptTemplateConfigurationTypeDef, PromptTemplateConfigurationOutputTypeDef
]
CreateFlowResponseTypeDef = TypedDict(
    "CreateFlowResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "customerEncryptionKeyArn": str,
        "definition": FlowDefinitionOutputTypeDef,
        "description": str,
        "executionRoleArn": str,
        "id": str,
        "name": str,
        "status": FlowStatusType,
        "updatedAt": datetime,
        "version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFlowVersionResponseTypeDef = TypedDict(
    "CreateFlowVersionResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "customerEncryptionKeyArn": str,
        "definition": FlowDefinitionOutputTypeDef,
        "description": str,
        "executionRoleArn": str,
        "id": str,
        "name": str,
        "status": FlowStatusType,
        "version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFlowResponseTypeDef = TypedDict(
    "GetFlowResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "customerEncryptionKeyArn": str,
        "definition": FlowDefinitionOutputTypeDef,
        "description": str,
        "executionRoleArn": str,
        "id": str,
        "name": str,
        "status": FlowStatusType,
        "updatedAt": datetime,
        "validations": List[FlowValidationTypeDef],
        "version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFlowVersionResponseTypeDef = TypedDict(
    "GetFlowVersionResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "customerEncryptionKeyArn": str,
        "definition": FlowDefinitionOutputTypeDef,
        "description": str,
        "executionRoleArn": str,
        "id": str,
        "name": str,
        "status": FlowStatusType,
        "version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFlowResponseTypeDef = TypedDict(
    "UpdateFlowResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "customerEncryptionKeyArn": str,
        "definition": FlowDefinitionOutputTypeDef,
        "description": str,
        "executionRoleArn": str,
        "id": str,
        "name": str,
        "status": FlowStatusType,
        "updatedAt": datetime,
        "version": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class PromptFlowNodeSourceConfigurationTypeDef(TypedDict):
    inline: NotRequired[PromptFlowNodeInlineConfigurationTypeDef]
    resource: NotRequired[PromptFlowNodeResourceConfigurationTypeDef]

class PromptVariantTypeDef(TypedDict):
    name: str
    templateConfiguration: PromptTemplateConfigurationUnionTypeDef
    templateType: PromptTemplateTypeType
    additionalModelRequestFields: NotRequired[Mapping[str, Any]]
    genAiResource: NotRequired[PromptGenAiResourceTypeDef]
    inferenceConfiguration: NotRequired[PromptInferenceConfigurationUnionTypeDef]
    metadata: NotRequired[Sequence[PromptMetadataEntryTypeDef]]
    modelId: NotRequired[str]

class PromptFlowNodeConfigurationTypeDef(TypedDict):
    sourceConfiguration: PromptFlowNodeSourceConfigurationTypeDef
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]

PromptVariantUnionTypeDef = Union[PromptVariantTypeDef, PromptVariantOutputTypeDef]
FlowNodeConfigurationTypeDef = TypedDict(
    "FlowNodeConfigurationTypeDef",
    {
        "agent": NotRequired[AgentFlowNodeConfigurationTypeDef],
        "collector": NotRequired[Mapping[str, Any]],
        "condition": NotRequired[ConditionFlowNodeConfigurationTypeDef],
        "inlineCode": NotRequired[InlineCodeFlowNodeConfigurationTypeDef],
        "input": NotRequired[Mapping[str, Any]],
        "iterator": NotRequired[Mapping[str, Any]],
        "knowledgeBase": NotRequired[KnowledgeBaseFlowNodeConfigurationTypeDef],
        "lambdaFunction": NotRequired[LambdaFunctionFlowNodeConfigurationTypeDef],
        "lex": NotRequired[LexFlowNodeConfigurationTypeDef],
        "output": NotRequired[Mapping[str, Any]],
        "prompt": NotRequired[PromptFlowNodeConfigurationTypeDef],
        "retrieval": NotRequired[RetrievalFlowNodeConfigurationTypeDef],
        "storage": NotRequired[StorageFlowNodeConfigurationTypeDef],
    },
)

class CreatePromptRequestTypeDef(TypedDict):
    name: str
    clientToken: NotRequired[str]
    customerEncryptionKeyArn: NotRequired[str]
    defaultVariant: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    variants: NotRequired[Sequence[PromptVariantUnionTypeDef]]

class UpdatePromptRequestTypeDef(TypedDict):
    name: str
    promptIdentifier: str
    customerEncryptionKeyArn: NotRequired[str]
    defaultVariant: NotRequired[str]
    description: NotRequired[str]
    variants: NotRequired[Sequence[PromptVariantUnionTypeDef]]

FlowNodeTypeDef = TypedDict(
    "FlowNodeTypeDef",
    {
        "name": str,
        "type": FlowNodeTypeType,
        "configuration": NotRequired[FlowNodeConfigurationTypeDef],
        "inputs": NotRequired[Sequence[FlowNodeInputTypeDef]],
        "outputs": NotRequired[Sequence[FlowNodeOutputTypeDef]],
    },
)

class FlowDefinitionTypeDef(TypedDict):
    connections: NotRequired[Sequence[FlowConnectionTypeDef]]
    nodes: NotRequired[Sequence[FlowNodeTypeDef]]

FlowDefinitionUnionTypeDef = Union[FlowDefinitionTypeDef, FlowDefinitionOutputTypeDef]

class CreateFlowRequestTypeDef(TypedDict):
    executionRoleArn: str
    name: str
    clientToken: NotRequired[str]
    customerEncryptionKeyArn: NotRequired[str]
    definition: NotRequired[FlowDefinitionUnionTypeDef]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateFlowRequestTypeDef(TypedDict):
    executionRoleArn: str
    flowIdentifier: str
    name: str
    customerEncryptionKeyArn: NotRequired[str]
    definition: NotRequired[FlowDefinitionUnionTypeDef]
    description: NotRequired[str]

class ValidateFlowDefinitionRequestTypeDef(TypedDict):
    definition: FlowDefinitionUnionTypeDef
