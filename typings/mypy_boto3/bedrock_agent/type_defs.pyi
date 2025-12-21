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
    AliasInvocationStateType,
    ChunkingStrategyType,
    ConcurrencyTypeType,
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
    FlowNodeInputCategoryType,
    FlowNodeIODataTypeType,
    FlowNodeTypeType,
    FlowStatusType,
    FlowValidationSeverityType,
    FlowValidationTypeType,
    IncludeExcludeType,
    IncompatibleLoopNodeTypeType,
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
    PerformanceConfigLatencyType,
    PromptStateType,
    PromptTemplateTypeType,
    PromptTypeType,
    RedshiftProvisionedAuthTypeType,
    RedshiftQueryEngineStorageTypeType,
    RedshiftQueryEngineTypeType,
    RedshiftServerlessAuthTypeType,
    RelayConversationHistoryType,
    RequireConfirmationType,
    RerankingMetadataSelectionModeType,
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
    "AudioConfigurationTypeDef",
    "AudioSegmentationConfigurationTypeDef",
    "BedrockDataAutomationConfigurationTypeDef",
    "BedrockEmbeddingModelConfigurationOutputTypeDef",
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
    "EmbeddingModelConfigurationOutputTypeDef",
    "EmbeddingModelConfigurationTypeDef",
    "EnrichmentStrategyConfigurationTypeDef",
    "FieldForRerankingTypeDef",
    "FixedSizeChunkingConfigurationTypeDef",
    "FlowAliasConcurrencyConfigurationTypeDef",
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
    "InvalidLoopBoundaryFlowValidationDetailsTypeDef",
    "KendraKnowledgeBaseConfigurationTypeDef",
    "KnowledgeBaseConfigurationOutputTypeDef",
    "KnowledgeBaseConfigurationTypeDef",
    "KnowledgeBaseConfigurationUnionTypeDef",
    "KnowledgeBaseDocumentDetailTypeDef",
    "KnowledgeBaseDocumentTypeDef",
    "KnowledgeBaseFlowNodeConfigurationOutputTypeDef",
    "KnowledgeBaseFlowNodeConfigurationTypeDef",
    "KnowledgeBaseOrchestrationConfigurationOutputTypeDef",
    "KnowledgeBaseOrchestrationConfigurationTypeDef",
    "KnowledgeBasePromptTemplateTypeDef",
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
    "LoopControllerFlowNodeConfigurationTypeDef",
    "LoopFlowNodeConfigurationOutputTypeDef",
    "LoopFlowNodeConfigurationTypeDef",
    "LoopIncompatibleNodeTypeFlowValidationDetailsTypeDef",
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
    "MetadataConfigurationForRerankingOutputTypeDef",
    "MetadataConfigurationForRerankingTypeDef",
    "MismatchedNodeInputTypeFlowValidationDetailsTypeDef",
    "MismatchedNodeOutputTypeFlowValidationDetailsTypeDef",
    "MissingConnectionConfigurationFlowValidationDetailsTypeDef",
    "MissingDefaultConditionFlowValidationDetailsTypeDef",
    "MissingLoopControllerNodeFlowValidationDetailsTypeDef",
    "MissingLoopInputNodeFlowValidationDetailsTypeDef",
    "MissingNodeConfigurationFlowValidationDetailsTypeDef",
    "MissingNodeInputFlowValidationDetailsTypeDef",
    "MissingNodeOutputFlowValidationDetailsTypeDef",
    "MongoDbAtlasConfigurationTypeDef",
    "MongoDbAtlasFieldMappingTypeDef",
    "MultipleLoopControllerNodesFlowValidationDetailsTypeDef",
    "MultipleLoopInputNodesFlowValidationDetailsTypeDef",
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
    "PerformanceConfigurationTypeDef",
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
    "RerankingMetadataSelectiveModeConfigurationOutputTypeDef",
    "RerankingMetadataSelectiveModeConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "RetrievalFlowNodeConfigurationTypeDef",
    "RetrievalFlowNodeS3ConfigurationTypeDef",
    "RetrievalFlowNodeServiceConfigurationTypeDef",
    "S3ContentTypeDef",
    "S3DataSourceConfigurationOutputTypeDef",
    "S3DataSourceConfigurationTypeDef",
    "S3IdentifierTypeDef",
    "S3LocationTypeDef",
    "S3VectorsConfigurationTypeDef",
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
    "VectorSearchBedrockRerankingConfigurationOutputTypeDef",
    "VectorSearchBedrockRerankingConfigurationTypeDef",
    "VectorSearchBedrockRerankingModelConfigurationOutputTypeDef",
    "VectorSearchBedrockRerankingModelConfigurationTypeDef",
    "VectorSearchRerankingConfigurationOutputTypeDef",
    "VectorSearchRerankingConfigurationTypeDef",
    "VideoConfigurationTypeDef",
    "VideoSegmentationConfigurationTypeDef",
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
        "lambda": NotRequired[str],
        "customControl": NotRequired[Literal["RETURN_CONTROL"]],
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
    knowledgeBaseId: str
    description: str
    createdAt: datetime
    updatedAt: datetime
    knowledgeBaseState: KnowledgeBaseStateType

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
    knowledgeBaseId: str
    description: str
    knowledgeBaseState: NotRequired[KnowledgeBaseStateType]

class AudioSegmentationConfigurationTypeDef(TypedDict):
    fixedLengthDuration: int

class BedrockDataAutomationConfigurationTypeDef(TypedDict):
    parsingModality: NotRequired[Literal["MULTIMODAL"]]

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
    maxTokens: int
    bufferSize: int
    breakpointPercentileThreshold: int

class FlowConditionTypeDef(TypedDict):
    name: str
    expression: NotRequired[str]

class ConfluenceSourceConfigurationTypeDef(TypedDict):
    hostUrl: str
    hostType: Literal["SAAS"]
    authType: ConfluenceAuthTypeType
    credentialsSecretArn: str

class ServerSideEncryptionConfigurationTypeDef(TypedDict):
    kmsKeyArn: NotRequired[str]

FlowAliasConcurrencyConfigurationTypeDef = TypedDict(
    "FlowAliasConcurrencyConfigurationTypeDef",
    {
        "type": ConcurrencyTypeType,
        "maxConcurrency": NotRequired[int],
    },
)

class FlowAliasRoutingConfigurationListItemTypeDef(TypedDict):
    flowVersion: NotRequired[str]

class CreateFlowVersionRequestTypeDef(TypedDict):
    flowIdentifier: str
    description: NotRequired[str]
    clientToken: NotRequired[str]

class CreatePromptVersionRequestTypeDef(TypedDict):
    promptIdentifier: str
    description: NotRequired[str]
    clientToken: NotRequired[str]
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
    inclusionPrefixes: NotRequired[List[str]]
    bucketOwnerAccountId: NotRequired[str]

class S3DataSourceConfigurationTypeDef(TypedDict):
    bucketArn: str
    inclusionPrefixes: NotRequired[Sequence[str]]
    bucketOwnerAccountId: NotRequired[str]

class DataSourceSummaryTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str
    name: str
    status: DataSourceStatusType
    updatedAt: datetime
    description: NotRequired[str]

class DeleteAgentActionGroupRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    actionGroupId: str
    skipResourceInUseCheck: NotRequired[bool]

class DeleteAgentAliasRequestTypeDef(TypedDict):
    agentId: str
    agentAliasId: str

class DeleteAgentRequestTypeDef(TypedDict):
    agentId: str
    skipResourceInUseCheck: NotRequired[bool]

class DeleteAgentVersionRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    skipResourceInUseCheck: NotRequired[bool]

class DeleteDataSourceRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str

class DeleteFlowAliasRequestTypeDef(TypedDict):
    flowIdentifier: str
    aliasIdentifier: str

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
    node: str
    expression: str

class DuplicateConnectionsFlowValidationDetailsTypeDef(TypedDict):
    source: str
    target: str

class FieldForRerankingTypeDef(TypedDict):
    fieldName: str

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

class LoopFlowNodeConfigurationOutputTypeDef(TypedDict):
    definition: Dict[str, Any]

class LoopFlowNodeConfigurationTypeDef(TypedDict):
    definition: Mapping[str, Any]

FlowNodeInputTypeDef = TypedDict(
    "FlowNodeInputTypeDef",
    {
        "name": str,
        "type": FlowNodeIODataTypeType,
        "expression": str,
        "category": NotRequired[FlowNodeInputCategoryType],
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
        "name": str,
        "id": str,
        "arn": str,
        "status": FlowStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "version": str,
        "description": NotRequired[str],
    },
)

class IncompatibleConnectionDataTypeFlowValidationDetailsTypeDef(TypedDict):
    connection: str

class InvalidLoopBoundaryFlowValidationDetailsTypeDef(TypedDict):
    connection: str
    source: str
    target: str

class LoopIncompatibleNodeTypeFlowValidationDetailsTypeDef(TypedDict):
    node: str
    incompatibleNodeType: IncompatibleLoopNodeTypeType
    incompatibleNodeName: str

class MalformedConditionExpressionFlowValidationDetailsTypeDef(TypedDict):
    node: str
    condition: str
    cause: str

MalformedNodeInputExpressionFlowValidationDetailsTypeDef = TypedDict(
    "MalformedNodeInputExpressionFlowValidationDetailsTypeDef",
    {
        "node": str,
        "input": str,
        "cause": str,
    },
)
MismatchedNodeInputTypeFlowValidationDetailsTypeDef = TypedDict(
    "MismatchedNodeInputTypeFlowValidationDetailsTypeDef",
    {
        "node": str,
        "input": str,
        "expectedType": FlowNodeIODataTypeType,
    },
)

class MismatchedNodeOutputTypeFlowValidationDetailsTypeDef(TypedDict):
    node: str
    output: str
    expectedType: FlowNodeIODataTypeType

class MissingConnectionConfigurationFlowValidationDetailsTypeDef(TypedDict):
    connection: str

class MissingDefaultConditionFlowValidationDetailsTypeDef(TypedDict):
    node: str

class MissingLoopControllerNodeFlowValidationDetailsTypeDef(TypedDict):
    loopNode: str

class MissingLoopInputNodeFlowValidationDetailsTypeDef(TypedDict):
    loopNode: str

class MissingNodeConfigurationFlowValidationDetailsTypeDef(TypedDict):
    node: str

MissingNodeInputFlowValidationDetailsTypeDef = TypedDict(
    "MissingNodeInputFlowValidationDetailsTypeDef",
    {
        "node": str,
        "input": str,
    },
)

class MissingNodeOutputFlowValidationDetailsTypeDef(TypedDict):
    node: str
    output: str

class MultipleLoopControllerNodesFlowValidationDetailsTypeDef(TypedDict):
    loopNode: str

class MultipleLoopInputNodesFlowValidationDetailsTypeDef(TypedDict):
    loopNode: str

MultipleNodeInputConnectionsFlowValidationDetailsTypeDef = TypedDict(
    "MultipleNodeInputConnectionsFlowValidationDetailsTypeDef",
    {
        "node": str,
        "input": str,
    },
)
UnfulfilledNodeInputFlowValidationDetailsTypeDef = TypedDict(
    "UnfulfilledNodeInputFlowValidationDetailsTypeDef",
    {
        "node": str,
        "input": str,
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
        "node": str,
        "input": str,
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
        "id": str,
        "arn": str,
        "status": FlowStatusType,
        "createdAt": datetime,
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
    agentId: str
    agentVersion: str
    actionGroupId: str

class GetAgentAliasRequestTypeDef(TypedDict):
    agentId: str
    agentAliasId: str

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
    knowledgeBaseId: str
    dataSourceId: str

class GetFlowAliasRequestTypeDef(TypedDict):
    flowIdentifier: str
    aliasIdentifier: str

class GetFlowRequestTypeDef(TypedDict):
    flowIdentifier: str

class GetFlowVersionRequestTypeDef(TypedDict):
    flowIdentifier: str
    flowVersion: str

class GetIngestionJobRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str
    ingestionJobId: str

class GetKnowledgeBaseRequestTypeDef(TypedDict):
    knowledgeBaseId: str

class GetPromptRequestTypeDef(TypedDict):
    promptIdentifier: str
    promptVersion: NotRequired[str]

class HierarchicalChunkingLevelConfigurationTypeDef(TypedDict):
    maxTokens: int

class InferenceConfigurationOutputTypeDef(TypedDict):
    temperature: NotRequired[float]
    topP: NotRequired[float]
    topK: NotRequired[int]
    maximumLength: NotRequired[int]
    stopSequences: NotRequired[List[str]]

class InferenceConfigurationTypeDef(TypedDict):
    temperature: NotRequired[float]
    topP: NotRequired[float]
    topK: NotRequired[int]
    maximumLength: NotRequired[int]
    stopSequences: NotRequired[Sequence[str]]

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
    numberOfDocumentsScanned: NotRequired[int]
    numberOfMetadataDocumentsScanned: NotRequired[int]
    numberOfNewDocumentsIndexed: NotRequired[int]
    numberOfModifiedDocumentsIndexed: NotRequired[int]
    numberOfMetadataDocumentsModified: NotRequired[int]
    numberOfDocumentsDeleted: NotRequired[int]
    numberOfDocumentsFailed: NotRequired[int]

class TextContentDocTypeDef(TypedDict):
    data: str

class KendraKnowledgeBaseConfigurationTypeDef(TypedDict):
    kendraIndexArn: str

class KnowledgeBasePromptTemplateTypeDef(TypedDict):
    textPromptTemplate: NotRequired[str]

class PerformanceConfigurationTypeDef(TypedDict):
    latency: NotRequired[PerformanceConfigLatencyType]

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
    knowledgeBaseId: str
    dataSourceId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListKnowledgeBasesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListPromptsRequestTypeDef(TypedDict):
    promptIdentifier: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

PromptSummaryTypeDef = TypedDict(
    "PromptSummaryTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "version": str,
        "createdAt": datetime,
        "updatedAt": datetime,
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
        "numberValue": NotRequired[float],
        "booleanValue": NotRequired[bool],
        "stringValue": NotRequired[str],
        "stringListValue": NotRequired[Sequence[str]],
    },
)

class MongoDbAtlasFieldMappingTypeDef(TypedDict):
    vectorField: str
    textField: str
    metadataField: str

class NeptuneAnalyticsFieldMappingTypeDef(TypedDict):
    textField: str
    metadataField: str

class OpenSearchManagedClusterFieldMappingTypeDef(TypedDict):
    vectorField: str
    textField: str
    metadataField: str

class OpenSearchServerlessFieldMappingTypeDef(TypedDict):
    vectorField: str
    textField: str
    metadataField: str

class PatternObjectFilterOutputTypeDef(TypedDict):
    objectType: str
    inclusionFilters: NotRequired[List[str]]
    exclusionFilters: NotRequired[List[str]]

class PatternObjectFilterTypeDef(TypedDict):
    objectType: str
    inclusionFilters: NotRequired[Sequence[str]]
    exclusionFilters: NotRequired[Sequence[str]]

class PineconeFieldMappingTypeDef(TypedDict):
    textField: str
    metadataField: str

class PrepareAgentRequestTypeDef(TypedDict):
    agentId: str

class PrepareFlowRequestTypeDef(TypedDict):
    flowIdentifier: str

class PromptAgentResourceTypeDef(TypedDict):
    agentIdentifier: str

class PromptFlowNodeResourceConfigurationTypeDef(TypedDict):
    promptArn: str

class PromptModelInferenceConfigurationOutputTypeDef(TypedDict):
    temperature: NotRequired[float]
    topP: NotRequired[float]
    maxTokens: NotRequired[int]
    stopSequences: NotRequired[List[str]]

class PromptMetadataEntryTypeDef(TypedDict):
    key: str
    value: str

class PromptModelInferenceConfigurationTypeDef(TypedDict):
    temperature: NotRequired[float]
    topP: NotRequired[float]
    maxTokens: NotRequired[int]
    stopSequences: NotRequired[Sequence[str]]

class QueryGenerationColumnTypeDef(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str]
    inclusion: NotRequired[IncludeExcludeType]

class RdsFieldMappingTypeDef(TypedDict):
    primaryKeyField: str
    vectorField: str
    textField: str
    metadataField: str
    customMetadataField: NotRequired[str]

class RedisEnterpriseCloudFieldMappingTypeDef(TypedDict):
    vectorField: str
    textField: str
    metadataField: str

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

class S3VectorsConfigurationTypeDef(TypedDict):
    vectorBucketArn: NotRequired[str]
    indexArn: NotRequired[str]
    indexName: NotRequired[str]

class SalesforceSourceConfigurationTypeDef(TypedDict):
    hostUrl: str
    authType: Literal["OAUTH2_CLIENT_CREDENTIALS"]
    credentialsSecretArn: str

class SeedUrlTypeDef(TypedDict):
    url: NotRequired[str]

class SharePointSourceConfigurationOutputTypeDef(TypedDict):
    domain: str
    siteUrls: List[str]
    hostType: Literal["ONLINE"]
    authType: SharePointAuthTypeType
    credentialsSecretArn: str
    tenantId: NotRequired[str]

class SharePointSourceConfigurationTypeDef(TypedDict):
    domain: str
    siteUrls: Sequence[str]
    hostType: Literal["ONLINE"]
    authType: SharePointAuthTypeType
    credentialsSecretArn: str
    tenantId: NotRequired[str]

class SpecificToolChoiceTypeDef(TypedDict):
    name: str

class StartIngestionJobRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str
    clientToken: NotRequired[str]
    description: NotRequired[str]

class StopIngestionJobRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str
    ingestionJobId: str

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

class VectorSearchBedrockRerankingModelConfigurationOutputTypeDef(TypedDict):
    modelArn: str
    additionalModelRequestFields: NotRequired[Dict[str, Dict[str, Any]]]

class VectorSearchBedrockRerankingModelConfigurationTypeDef(TypedDict):
    modelArn: str
    additionalModelRequestFields: NotRequired[Mapping[str, Mapping[str, Any]]]

class VideoSegmentationConfigurationTypeDef(TypedDict):
    fixedLengthDuration: int

class WebCrawlerLimitsTypeDef(TypedDict):
    rateLimit: NotRequired[int]
    maxPages: NotRequired[int]

class APISchemaTypeDef(TypedDict):
    s3: NotRequired[S3IdentifierTypeDef]
    payload: NotRequired[str]

class AgentAliasHistoryEventTypeDef(TypedDict):
    routingConfiguration: NotRequired[List[AgentAliasRoutingConfigurationListItemTypeDef]]
    endDate: NotRequired[datetime]
    startDate: NotRequired[datetime]

class AgentAliasSummaryTypeDef(TypedDict):
    agentAliasId: str
    agentAliasName: str
    agentAliasStatus: AgentAliasStatusType
    createdAt: datetime
    updatedAt: datetime
    description: NotRequired[str]
    routingConfiguration: NotRequired[List[AgentAliasRoutingConfigurationListItemTypeDef]]
    aliasInvocationState: NotRequired[AliasInvocationStateType]

class CreateAgentAliasRequestTypeDef(TypedDict):
    agentId: str
    agentAliasName: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    routingConfiguration: NotRequired[Sequence[AgentAliasRoutingConfigurationListItemTypeDef]]
    tags: NotRequired[Mapping[str, str]]

class UpdateAgentAliasRequestTypeDef(TypedDict):
    agentId: str
    agentAliasId: str
    agentAliasName: str
    description: NotRequired[str]
    routingConfiguration: NotRequired[Sequence[AgentAliasRoutingConfigurationListItemTypeDef]]
    aliasInvocationState: NotRequired[AliasInvocationStateType]

class AgentCollaboratorSummaryTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    collaboratorId: str
    agentDescriptor: AgentDescriptorTypeDef
    collaborationInstruction: str
    relayConversationHistory: RelayConversationHistoryType
    collaboratorName: str
    createdAt: datetime
    lastUpdatedAt: datetime

class AgentCollaboratorTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    agentDescriptor: AgentDescriptorTypeDef
    collaboratorId: str
    collaborationInstruction: str
    collaboratorName: str
    createdAt: datetime
    lastUpdatedAt: datetime
    relayConversationHistory: NotRequired[RelayConversationHistoryType]
    clientToken: NotRequired[str]

class AssociateAgentCollaboratorRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    agentDescriptor: AgentDescriptorTypeDef
    collaboratorName: str
    collaborationInstruction: str
    relayConversationHistory: NotRequired[RelayConversationHistoryType]
    clientToken: NotRequired[str]

class UpdateAgentCollaboratorRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    collaboratorId: str
    agentDescriptor: AgentDescriptorTypeDef
    collaboratorName: str
    collaborationInstruction: str
    relayConversationHistory: NotRequired[RelayConversationHistoryType]

class AgentSummaryTypeDef(TypedDict):
    agentId: str
    agentName: str
    agentStatus: AgentStatusType
    updatedAt: datetime
    description: NotRequired[str]
    latestAgentVersion: NotRequired[str]
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]

class AgentVersionSummaryTypeDef(TypedDict):
    agentName: str
    agentStatus: AgentStatusType
    agentVersion: str
    createdAt: datetime
    updatedAt: datetime
    description: NotRequired[str]
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]

class AssociateAgentKnowledgeBaseResponseTypeDef(TypedDict):
    agentKnowledgeBase: AgentKnowledgeBaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAgentAliasResponseTypeDef(TypedDict):
    agentId: str
    agentAliasId: str
    agentAliasStatus: AgentAliasStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAgentResponseTypeDef(TypedDict):
    agentId: str
    agentStatus: AgentStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAgentVersionResponseTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    agentStatus: AgentStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataSourceResponseTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str
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

class AudioConfigurationTypeDef(TypedDict):
    segmentationConfiguration: AudioSegmentationConfigurationTypeDef

class BedrockFoundationModelConfigurationTypeDef(TypedDict):
    modelArn: str
    parsingPrompt: NotRequired[ParsingPromptTypeDef]
    parsingModality: NotRequired[Literal["MULTIMODAL"]]

class BedrockFoundationModelContextEnrichmentConfigurationTypeDef(TypedDict):
    enrichmentStrategyConfiguration: EnrichmentStrategyConfigurationTypeDef
    modelArn: str

class ByteContentDocTypeDef(TypedDict):
    mimeType: str
    data: BlobTypeDef

class ContentBlockTypeDef(TypedDict):
    text: NotRequired[str]
    cachePoint: NotRequired[CachePointBlockTypeDef]

class SystemContentBlockTypeDef(TypedDict):
    text: NotRequired[str]
    cachePoint: NotRequired[CachePointBlockTypeDef]

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

class LoopControllerFlowNodeConfigurationTypeDef(TypedDict):
    continueCondition: FlowConditionTypeDef
    maxIterations: NotRequired[int]

class CreateFlowAliasRequestTypeDef(TypedDict):
    name: str
    routingConfiguration: Sequence[FlowAliasRoutingConfigurationListItemTypeDef]
    flowIdentifier: str
    description: NotRequired[str]
    concurrencyConfiguration: NotRequired[FlowAliasConcurrencyConfigurationTypeDef]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

CreateFlowAliasResponseTypeDef = TypedDict(
    "CreateFlowAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "routingConfiguration": List[FlowAliasRoutingConfigurationListItemTypeDef],
        "concurrencyConfiguration": FlowAliasConcurrencyConfigurationTypeDef,
        "flowId": str,
        "id": str,
        "arn": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
FlowAliasSummaryTypeDef = TypedDict(
    "FlowAliasSummaryTypeDef",
    {
        "name": str,
        "routingConfiguration": List[FlowAliasRoutingConfigurationListItemTypeDef],
        "flowId": str,
        "id": str,
        "arn": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "description": NotRequired[str],
        "concurrencyConfiguration": NotRequired[FlowAliasConcurrencyConfigurationTypeDef],
    },
)
GetFlowAliasResponseTypeDef = TypedDict(
    "GetFlowAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "routingConfiguration": List[FlowAliasRoutingConfigurationListItemTypeDef],
        "concurrencyConfiguration": FlowAliasConcurrencyConfigurationTypeDef,
        "flowId": str,
        "id": str,
        "arn": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UpdateFlowAliasRequestTypeDef(TypedDict):
    name: str
    routingConfiguration: Sequence[FlowAliasRoutingConfigurationListItemTypeDef]
    flowIdentifier: str
    aliasIdentifier: str
    description: NotRequired[str]
    concurrencyConfiguration: NotRequired[FlowAliasConcurrencyConfigurationTypeDef]

UpdateFlowAliasResponseTypeDef = TypedDict(
    "UpdateFlowAliasResponseTypeDef",
    {
        "name": str,
        "description": str,
        "routingConfiguration": List[FlowAliasRoutingConfigurationListItemTypeDef],
        "concurrencyConfiguration": FlowAliasConcurrencyConfigurationTypeDef,
        "flowId": str,
        "id": str,
        "arn": str,
        "createdAt": datetime,
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
    s3: NotRequired[S3LocationTypeDef]
    custom: NotRequired[CustomDocumentIdentifierTypeDef]

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

class RerankingMetadataSelectiveModeConfigurationOutputTypeDef(TypedDict):
    fieldsToInclude: NotRequired[List[FieldForRerankingTypeDef]]
    fieldsToExclude: NotRequired[List[FieldForRerankingTypeDef]]

class RerankingMetadataSelectiveModeConfigurationTypeDef(TypedDict):
    fieldsToInclude: NotRequired[Sequence[FieldForRerankingTypeDef]]
    fieldsToExclude: NotRequired[Sequence[FieldForRerankingTypeDef]]

class FlowConnectionConfigurationTypeDef(TypedDict):
    data: NotRequired[FlowDataConnectionConfigurationTypeDef]
    conditional: NotRequired[FlowConditionalConnectionConfigurationTypeDef]

class ListFlowsResponseTypeDef(TypedDict):
    flowSummaries: List[FlowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class FlowValidationDetailsTypeDef(TypedDict):
    cyclicConnection: NotRequired[CyclicConnectionFlowValidationDetailsTypeDef]
    duplicateConnections: NotRequired[DuplicateConnectionsFlowValidationDetailsTypeDef]
    duplicateConditionExpression: NotRequired[
        DuplicateConditionExpressionFlowValidationDetailsTypeDef
    ]
    unreachableNode: NotRequired[UnreachableNodeFlowValidationDetailsTypeDef]
    unknownConnectionSource: NotRequired[UnknownConnectionSourceFlowValidationDetailsTypeDef]
    unknownConnectionSourceOutput: NotRequired[
        UnknownConnectionSourceOutputFlowValidationDetailsTypeDef
    ]
    unknownConnectionTarget: NotRequired[UnknownConnectionTargetFlowValidationDetailsTypeDef]
    unknownConnectionTargetInput: NotRequired[
        UnknownConnectionTargetInputFlowValidationDetailsTypeDef
    ]
    unknownConnectionCondition: NotRequired[UnknownConnectionConditionFlowValidationDetailsTypeDef]
    malformedConditionExpression: NotRequired[
        MalformedConditionExpressionFlowValidationDetailsTypeDef
    ]
    malformedNodeInputExpression: NotRequired[
        MalformedNodeInputExpressionFlowValidationDetailsTypeDef
    ]
    mismatchedNodeInputType: NotRequired[MismatchedNodeInputTypeFlowValidationDetailsTypeDef]
    mismatchedNodeOutputType: NotRequired[MismatchedNodeOutputTypeFlowValidationDetailsTypeDef]
    incompatibleConnectionDataType: NotRequired[
        IncompatibleConnectionDataTypeFlowValidationDetailsTypeDef
    ]
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
    unsatisfiedConnectionConditions: NotRequired[
        UnsatisfiedConnectionConditionsFlowValidationDetailsTypeDef
    ]
    unspecified: NotRequired[Dict[str, Any]]
    unknownNodeInput: NotRequired[UnknownNodeInputFlowValidationDetailsTypeDef]
    unknownNodeOutput: NotRequired[UnknownNodeOutputFlowValidationDetailsTypeDef]
    missingLoopInputNode: NotRequired[MissingLoopInputNodeFlowValidationDetailsTypeDef]
    missingLoopControllerNode: NotRequired[MissingLoopControllerNodeFlowValidationDetailsTypeDef]
    multipleLoopInputNodes: NotRequired[MultipleLoopInputNodesFlowValidationDetailsTypeDef]
    multipleLoopControllerNodes: NotRequired[
        MultipleLoopControllerNodesFlowValidationDetailsTypeDef
    ]
    loopIncompatibleNodeType: NotRequired[LoopIncompatibleNodeTypeFlowValidationDetailsTypeDef]
    invalidLoopBoundary: NotRequired[InvalidLoopBoundaryFlowValidationDetailsTypeDef]

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
    promptType: NotRequired[PromptTypeType]
    promptCreationMode: NotRequired[CreationModeType]
    promptState: NotRequired[PromptStateType]
    basePromptTemplate: NotRequired[str]
    inferenceConfiguration: NotRequired[InferenceConfigurationOutputTypeDef]
    parserMode: NotRequired[CreationModeType]
    foundationModel: NotRequired[str]
    additionalModelRequestFields: NotRequired[Dict[str, Any]]

class PromptConfigurationTypeDef(TypedDict):
    promptType: NotRequired[PromptTypeType]
    promptCreationMode: NotRequired[CreationModeType]
    promptState: NotRequired[PromptStateType]
    basePromptTemplate: NotRequired[str]
    inferenceConfiguration: NotRequired[InferenceConfigurationTypeDef]
    parserMode: NotRequired[CreationModeType]
    foundationModel: NotRequired[str]
    additionalModelRequestFields: NotRequired[Mapping[str, Any]]

class ListIngestionJobsRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str
    filters: NotRequired[Sequence[IngestionJobFilterTypeDef]]
    sortBy: NotRequired[IngestionJobSortByTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class IngestionJobSummaryTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str
    ingestionJobId: str
    status: IngestionJobStatusType
    startedAt: datetime
    updatedAt: datetime
    description: NotRequired[str]
    statistics: NotRequired[IngestionJobStatisticsTypeDef]

class IngestionJobTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str
    ingestionJobId: str
    status: IngestionJobStatusType
    startedAt: datetime
    updatedAt: datetime
    description: NotRequired[str]
    statistics: NotRequired[IngestionJobStatisticsTypeDef]
    failureReasons: NotRequired[List[str]]

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
    knowledgeBaseId: str
    dataSourceId: str
    filters: NotRequired[Sequence[IngestionJobFilterTypeDef]]
    sortBy: NotRequired[IngestionJobSortByTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListKnowledgeBaseDocumentsRequestPaginateTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str
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
    storageDays: NotRequired[int]
    sessionSummaryConfiguration: NotRequired[SessionSummaryConfigurationTypeDef]

class MemoryConfigurationTypeDef(TypedDict):
    enabledMemoryTypes: Sequence[Literal["SESSION_SUMMARY"]]
    storageDays: NotRequired[int]
    sessionSummaryConfiguration: NotRequired[SessionSummaryConfigurationTypeDef]

class MetadataAttributeTypeDef(TypedDict):
    key: str
    value: MetadataAttributeValueTypeDef

class MongoDbAtlasConfigurationTypeDef(TypedDict):
    endpoint: str
    databaseName: str
    collectionName: str
    vectorIndexName: str
    credentialsSecretArn: str
    fieldMapping: MongoDbAtlasFieldMappingTypeDef
    endpointServiceName: NotRequired[str]
    textIndexName: NotRequired[str]

class NeptuneAnalyticsConfigurationTypeDef(TypedDict):
    graphArn: str
    fieldMapping: NeptuneAnalyticsFieldMappingTypeDef

class OpenSearchManagedClusterConfigurationTypeDef(TypedDict):
    domainEndpoint: str
    domainArn: str
    vectorIndexName: str
    fieldMapping: OpenSearchManagedClusterFieldMappingTypeDef

class OpenSearchServerlessConfigurationTypeDef(TypedDict):
    collectionArn: str
    vectorIndexName: str
    fieldMapping: OpenSearchServerlessFieldMappingTypeDef

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
    description: NotRequired[str]
    inclusion: NotRequired[IncludeExcludeType]
    columns: NotRequired[List[QueryGenerationColumnTypeDef]]

class QueryGenerationTableTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    inclusion: NotRequired[IncludeExcludeType]
    columns: NotRequired[Sequence[QueryGenerationColumnTypeDef]]

class RdsConfigurationTypeDef(TypedDict):
    resourceArn: str
    credentialsSecretArn: str
    databaseName: str
    tableName: str
    fieldMapping: RdsFieldMappingTypeDef

class RedisEnterpriseCloudConfigurationTypeDef(TypedDict):
    endpoint: str
    vectorIndexName: str
    credentialsSecretArn: str
    fieldMapping: RedisEnterpriseCloudFieldMappingTypeDef

class RedshiftProvisionedConfigurationTypeDef(TypedDict):
    clusterIdentifier: str
    authConfiguration: RedshiftProvisionedAuthConfigurationTypeDef

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
    workgroupArn: str
    authConfiguration: RedshiftServerlessAuthConfigurationTypeDef

class RetrievalFlowNodeServiceConfigurationTypeDef(TypedDict):
    s3: NotRequired[RetrievalFlowNodeS3ConfigurationTypeDef]

class UrlConfigurationOutputTypeDef(TypedDict):
    seedUrls: NotRequired[List[SeedUrlTypeDef]]

class UrlConfigurationTypeDef(TypedDict):
    seedUrls: NotRequired[Sequence[SeedUrlTypeDef]]

ToolChoiceOutputTypeDef = TypedDict(
    "ToolChoiceOutputTypeDef",
    {
        "auto": NotRequired[Dict[str, Any]],
        "any": NotRequired[Dict[str, Any]],
        "tool": NotRequired[SpecificToolChoiceTypeDef],
    },
)
ToolChoiceTypeDef = TypedDict(
    "ToolChoiceTypeDef",
    {
        "auto": NotRequired[Mapping[str, Any]],
        "any": NotRequired[Mapping[str, Any]],
        "tool": NotRequired[SpecificToolChoiceTypeDef],
    },
)

class StorageFlowNodeServiceConfigurationTypeDef(TypedDict):
    s3: NotRequired[StorageFlowNodeS3ConfigurationTypeDef]

class ToolSpecificationOutputTypeDef(TypedDict):
    name: str
    inputSchema: ToolInputSchemaOutputTypeDef
    description: NotRequired[str]

ToolInputSchemaUnionTypeDef = Union[ToolInputSchemaTypeDef, ToolInputSchemaOutputTypeDef]

class TransformationFunctionTypeDef(TypedDict):
    transformationLambdaConfiguration: TransformationLambdaConfigurationTypeDef

class VideoConfigurationTypeDef(TypedDict):
    segmentationConfiguration: VideoSegmentationConfigurationTypeDef

class WebCrawlerConfigurationOutputTypeDef(TypedDict):
    crawlerLimits: NotRequired[WebCrawlerLimitsTypeDef]
    inclusionFilters: NotRequired[List[str]]
    exclusionFilters: NotRequired[List[str]]
    scope: NotRequired[WebScopeTypeType]
    userAgent: NotRequired[str]
    userAgentHeader: NotRequired[str]

class WebCrawlerConfigurationTypeDef(TypedDict):
    crawlerLimits: NotRequired[WebCrawlerLimitsTypeDef]
    inclusionFilters: NotRequired[Sequence[str]]
    exclusionFilters: NotRequired[Sequence[str]]
    scope: NotRequired[WebScopeTypeType]
    userAgent: NotRequired[str]
    userAgentHeader: NotRequired[str]

class AgentAliasTypeDef(TypedDict):
    agentId: str
    agentAliasId: str
    agentAliasName: str
    agentAliasArn: str
    routingConfiguration: List[AgentAliasRoutingConfigurationListItemTypeDef]
    createdAt: datetime
    updatedAt: datetime
    agentAliasStatus: AgentAliasStatusType
    clientToken: NotRequired[str]
    description: NotRequired[str]
    agentAliasHistoryEvents: NotRequired[List[AgentAliasHistoryEventTypeDef]]
    failureReasons: NotRequired[List[str]]
    aliasInvocationState: NotRequired[AliasInvocationStateType]

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
    bedrockFoundationModelConfiguration: NotRequired[BedrockFoundationModelConfigurationTypeDef]
    bedrockDataAutomationConfiguration: NotRequired[BedrockDataAutomationConfigurationTypeDef]

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
    role: ConversationRoleType
    content: List[ContentBlockTypeDef]

class MessageTypeDef(TypedDict):
    role: ConversationRoleType
    content: Sequence[ContentBlockTypeDef]

TextPromptTemplateConfigurationUnionTypeDef = Union[
    TextPromptTemplateConfigurationTypeDef, TextPromptTemplateConfigurationOutputTypeDef
]

class ListFlowAliasesResponseTypeDef(TypedDict):
    flowAliasSummaries: List[FlowAliasSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DeleteKnowledgeBaseDocumentsRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str
    documentIdentifiers: Sequence[DocumentIdentifierTypeDef]
    clientToken: NotRequired[str]

class GetKnowledgeBaseDocumentsRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str
    documentIdentifiers: Sequence[DocumentIdentifierTypeDef]

class KnowledgeBaseDocumentDetailTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str
    status: DocumentStatusType
    identifier: DocumentIdentifierTypeDef
    statusReason: NotRequired[str]
    updatedAt: NotRequired[datetime]

class SupplementalDataStorageConfigurationOutputTypeDef(TypedDict):
    storageLocations: List[SupplementalDataStorageLocationTypeDef]

class SupplementalDataStorageConfigurationTypeDef(TypedDict):
    storageLocations: Sequence[SupplementalDataStorageLocationTypeDef]

class MetadataConfigurationForRerankingOutputTypeDef(TypedDict):
    selectionMode: RerankingMetadataSelectionModeType
    selectiveModeConfiguration: NotRequired[
        RerankingMetadataSelectiveModeConfigurationOutputTypeDef
    ]

class MetadataConfigurationForRerankingTypeDef(TypedDict):
    selectionMode: RerankingMetadataSelectionModeType
    selectiveModeConfiguration: NotRequired[RerankingMetadataSelectiveModeConfigurationTypeDef]

FlowConnectionTypeDef = TypedDict(
    "FlowConnectionTypeDef",
    {
        "type": FlowConnectionTypeType,
        "name": str,
        "source": str,
        "target": str,
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

class KnowledgeBaseOrchestrationConfigurationOutputTypeDef(TypedDict):
    promptTemplate: NotRequired[KnowledgeBasePromptTemplateTypeDef]
    inferenceConfig: NotRequired[PromptInferenceConfigurationOutputTypeDef]
    additionalModelRequestFields: NotRequired[Dict[str, Dict[str, Any]]]
    performanceConfig: NotRequired[PerformanceConfigurationTypeDef]

class PromptInferenceConfigurationTypeDef(TypedDict):
    text: NotRequired[PromptModelInferenceConfigurationUnionTypeDef]

class QueryGenerationContextOutputTypeDef(TypedDict):
    tables: NotRequired[List[QueryGenerationTableOutputTypeDef]]
    curatedQueries: NotRequired[List[CuratedQueryTypeDef]]

class QueryGenerationContextTypeDef(TypedDict):
    tables: NotRequired[Sequence[QueryGenerationTableTypeDef]]
    curatedQueries: NotRequired[Sequence[CuratedQueryTypeDef]]

StorageConfigurationTypeDef = TypedDict(
    "StorageConfigurationTypeDef",
    {
        "type": KnowledgeBaseStorageTypeType,
        "opensearchServerlessConfiguration": NotRequired[OpenSearchServerlessConfigurationTypeDef],
        "opensearchManagedClusterConfiguration": NotRequired[
            OpenSearchManagedClusterConfigurationTypeDef
        ],
        "pineconeConfiguration": NotRequired[PineconeConfigurationTypeDef],
        "redisEnterpriseCloudConfiguration": NotRequired[RedisEnterpriseCloudConfigurationTypeDef],
        "rdsConfiguration": NotRequired[RdsConfigurationTypeDef],
        "mongoDbAtlasConfiguration": NotRequired[MongoDbAtlasConfigurationTypeDef],
        "neptuneAnalyticsConfiguration": NotRequired[NeptuneAnalyticsConfigurationTypeDef],
        "s3VectorsConfiguration": NotRequired[S3VectorsConfigurationTypeDef],
    },
)
RedshiftQueryEngineConfigurationTypeDef = TypedDict(
    "RedshiftQueryEngineConfigurationTypeDef",
    {
        "type": RedshiftQueryEngineTypeType,
        "serverlessConfiguration": NotRequired[RedshiftServerlessConfigurationTypeDef],
        "provisionedConfiguration": NotRequired[RedshiftProvisionedConfigurationTypeDef],
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
    toolSpec: NotRequired[ToolSpecificationOutputTypeDef]
    cachePoint: NotRequired[CachePointBlockTypeDef]

class ToolSpecificationTypeDef(TypedDict):
    name: str
    inputSchema: ToolInputSchemaUnionTypeDef
    description: NotRequired[str]

class TransformationTypeDef(TypedDict):
    transformationFunction: TransformationFunctionTypeDef
    stepToApply: Literal["POST_CHUNKING"]

class BedrockEmbeddingModelConfigurationOutputTypeDef(TypedDict):
    dimensions: NotRequired[int]
    embeddingDataType: NotRequired[EmbeddingDataTypeType]
    audio: NotRequired[List[AudioConfigurationTypeDef]]
    video: NotRequired[List[VideoConfigurationTypeDef]]

class BedrockEmbeddingModelConfigurationTypeDef(TypedDict):
    dimensions: NotRequired[int]
    embeddingDataType: NotRequired[EmbeddingDataTypeType]
    audio: NotRequired[Sequence[AudioConfigurationTypeDef]]
    video: NotRequired[Sequence[VideoConfigurationTypeDef]]

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
    s3Location: NotRequired[CustomS3LocationTypeDef]
    inlineContent: NotRequired[InlineContentTypeDef]

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

class VectorSearchBedrockRerankingConfigurationOutputTypeDef(TypedDict):
    modelConfiguration: VectorSearchBedrockRerankingModelConfigurationOutputTypeDef
    numberOfRerankedResults: NotRequired[int]
    metadataConfiguration: NotRequired[MetadataConfigurationForRerankingOutputTypeDef]

class VectorSearchBedrockRerankingConfigurationTypeDef(TypedDict):
    modelConfiguration: VectorSearchBedrockRerankingModelConfigurationTypeDef
    numberOfRerankedResults: NotRequired[int]
    metadataConfiguration: NotRequired[MetadataConfigurationForRerankingTypeDef]

class ValidateFlowDefinitionResponseTypeDef(TypedDict):
    validations: List[FlowValidationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AgentActionGroupTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    actionGroupId: str
    actionGroupName: str
    createdAt: datetime
    updatedAt: datetime
    actionGroupState: ActionGroupStateType
    clientToken: NotRequired[str]
    description: NotRequired[str]
    parentActionSignature: NotRequired[ActionGroupSignatureType]
    parentActionGroupSignatureParams: NotRequired[Dict[str, str]]
    actionGroupExecutor: NotRequired[ActionGroupExecutorTypeDef]
    apiSchema: NotRequired[APISchemaTypeDef]
    functionSchema: NotRequired[FunctionSchemaOutputTypeDef]

FunctionSchemaUnionTypeDef = Union[FunctionSchemaTypeDef, FunctionSchemaOutputTypeDef]

class AgentTypeDef(TypedDict):
    agentId: str
    agentName: str
    agentArn: str
    agentVersion: str
    agentStatus: AgentStatusType
    idleSessionTTLInSeconds: int
    agentResourceRoleArn: str
    createdAt: datetime
    updatedAt: datetime
    clientToken: NotRequired[str]
    instruction: NotRequired[str]
    foundationModel: NotRequired[str]
    description: NotRequired[str]
    orchestrationType: NotRequired[OrchestrationTypeType]
    customOrchestration: NotRequired[CustomOrchestrationTypeDef]
    customerEncryptionKeyArn: NotRequired[str]
    preparedAt: NotRequired[datetime]
    failureReasons: NotRequired[List[str]]
    recommendedActions: NotRequired[List[str]]
    promptOverrideConfiguration: NotRequired[PromptOverrideConfigurationOutputTypeDef]
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]
    memoryConfiguration: NotRequired[MemoryConfigurationOutputTypeDef]
    agentCollaboration: NotRequired[AgentCollaborationType]

class AgentVersionTypeDef(TypedDict):
    agentId: str
    agentName: str
    agentArn: str
    version: str
    agentStatus: AgentStatusType
    idleSessionTTLInSeconds: int
    agentResourceRoleArn: str
    createdAt: datetime
    updatedAt: datetime
    instruction: NotRequired[str]
    foundationModel: NotRequired[str]
    description: NotRequired[str]
    customerEncryptionKeyArn: NotRequired[str]
    failureReasons: NotRequired[List[str]]
    recommendedActions: NotRequired[List[str]]
    promptOverrideConfiguration: NotRequired[PromptOverrideConfigurationOutputTypeDef]
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]
    memoryConfiguration: NotRequired[MemoryConfigurationOutputTypeDef]
    agentCollaboration: NotRequired[AgentCollaborationType]

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

class KnowledgeBaseOrchestrationConfigurationTypeDef(TypedDict):
    promptTemplate: NotRequired[KnowledgeBasePromptTemplateTypeDef]
    inferenceConfig: NotRequired[PromptInferenceConfigurationTypeDef]
    additionalModelRequestFields: NotRequired[Mapping[str, Mapping[str, Any]]]
    performanceConfig: NotRequired[PerformanceConfigurationTypeDef]

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

class EmbeddingModelConfigurationOutputTypeDef(TypedDict):
    bedrockEmbeddingModelConfiguration: NotRequired[BedrockEmbeddingModelConfigurationOutputTypeDef]

class EmbeddingModelConfigurationTypeDef(TypedDict):
    bedrockEmbeddingModelConfiguration: NotRequired[BedrockEmbeddingModelConfigurationTypeDef]

class DocumentContentTypeDef(TypedDict):
    dataSourceType: ContentDataSourceTypeType
    custom: NotRequired[CustomContentTypeDef]
    s3: NotRequired[S3ContentTypeDef]

VectorSearchRerankingConfigurationOutputTypeDef = TypedDict(
    "VectorSearchRerankingConfigurationOutputTypeDef",
    {
        "type": Literal["BEDROCK_RERANKING_MODEL"],
        "bedrockRerankingConfiguration": NotRequired[
            VectorSearchBedrockRerankingConfigurationOutputTypeDef
        ],
    },
)
VectorSearchRerankingConfigurationTypeDef = TypedDict(
    "VectorSearchRerankingConfigurationTypeDef",
    {
        "type": Literal["BEDROCK_RERANKING_MODEL"],
        "bedrockRerankingConfiguration": NotRequired[
            VectorSearchBedrockRerankingConfigurationTypeDef
        ],
    },
)

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
    agentId: str
    agentVersion: str
    actionGroupName: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    parentActionGroupSignature: NotRequired[ActionGroupSignatureType]
    parentActionGroupSignatureParams: NotRequired[Mapping[str, str]]
    actionGroupExecutor: NotRequired[ActionGroupExecutorTypeDef]
    apiSchema: NotRequired[APISchemaTypeDef]
    actionGroupState: NotRequired[ActionGroupStateType]
    functionSchema: NotRequired[FunctionSchemaUnionTypeDef]

class UpdateAgentActionGroupRequestTypeDef(TypedDict):
    agentId: str
    agentVersion: str
    actionGroupId: str
    actionGroupName: str
    description: NotRequired[str]
    parentActionGroupSignature: NotRequired[ActionGroupSignatureType]
    parentActionGroupSignatureParams: NotRequired[Mapping[str, str]]
    actionGroupExecutor: NotRequired[ActionGroupExecutorTypeDef]
    actionGroupState: NotRequired[ActionGroupStateType]
    apiSchema: NotRequired[APISchemaTypeDef]
    functionSchema: NotRequired[FunctionSchemaUnionTypeDef]

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
    clientToken: NotRequired[str]
    instruction: NotRequired[str]
    foundationModel: NotRequired[str]
    description: NotRequired[str]
    orchestrationType: NotRequired[OrchestrationTypeType]
    customOrchestration: NotRequired[CustomOrchestrationTypeDef]
    idleSessionTTLInSeconds: NotRequired[int]
    agentResourceRoleArn: NotRequired[str]
    customerEncryptionKeyArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    promptOverrideConfiguration: NotRequired[PromptOverrideConfigurationUnionTypeDef]
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]
    memoryConfiguration: NotRequired[MemoryConfigurationUnionTypeDef]
    agentCollaboration: NotRequired[AgentCollaborationType]

class UpdateAgentRequestTypeDef(TypedDict):
    agentId: str
    agentName: str
    foundationModel: str
    agentResourceRoleArn: str
    instruction: NotRequired[str]
    description: NotRequired[str]
    orchestrationType: NotRequired[OrchestrationTypeType]
    customOrchestration: NotRequired[CustomOrchestrationTypeDef]
    idleSessionTTLInSeconds: NotRequired[int]
    customerEncryptionKeyArn: NotRequired[str]
    promptOverrideConfiguration: NotRequired[PromptOverrideConfigurationUnionTypeDef]
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]
    memoryConfiguration: NotRequired[MemoryConfigurationUnionTypeDef]
    agentCollaboration: NotRequired[AgentCollaborationType]

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
    storageConfigurations: List[RedshiftQueryEngineStorageConfigurationOutputTypeDef]
    queryEngineConfiguration: RedshiftQueryEngineConfigurationTypeDef
    queryGenerationConfiguration: NotRequired[QueryGenerationConfigurationOutputTypeDef]

class RedshiftConfigurationTypeDef(TypedDict):
    storageConfigurations: Sequence[RedshiftQueryEngineStorageConfigurationTypeDef]
    queryEngineConfiguration: RedshiftQueryEngineConfigurationTypeDef
    queryGenerationConfiguration: NotRequired[QueryGenerationConfigurationTypeDef]

class ChatPromptTemplateConfigurationOutputTypeDef(TypedDict):
    messages: List[MessageOutputTypeDef]
    system: NotRequired[List[SystemContentBlockTypeDef]]
    inputVariables: NotRequired[List[PromptInputVariableTypeDef]]
    toolConfiguration: NotRequired[ToolConfigurationOutputTypeDef]

class ToolTypeDef(TypedDict):
    toolSpec: NotRequired[ToolSpecificationUnionTypeDef]
    cachePoint: NotRequired[CachePointBlockTypeDef]

class VectorIngestionConfigurationOutputTypeDef(TypedDict):
    chunkingConfiguration: NotRequired[ChunkingConfigurationOutputTypeDef]
    customTransformationConfiguration: NotRequired[CustomTransformationConfigurationOutputTypeDef]
    parsingConfiguration: NotRequired[ParsingConfigurationTypeDef]
    contextEnrichmentConfiguration: NotRequired[ContextEnrichmentConfigurationTypeDef]

class VectorIngestionConfigurationTypeDef(TypedDict):
    chunkingConfiguration: NotRequired[ChunkingConfigurationTypeDef]
    customTransformationConfiguration: NotRequired[CustomTransformationConfigurationTypeDef]
    parsingConfiguration: NotRequired[ParsingConfigurationTypeDef]
    contextEnrichmentConfiguration: NotRequired[ContextEnrichmentConfigurationTypeDef]

class VectorKnowledgeBaseConfigurationOutputTypeDef(TypedDict):
    embeddingModelArn: str
    embeddingModelConfiguration: NotRequired[EmbeddingModelConfigurationOutputTypeDef]
    supplementalDataStorageConfiguration: NotRequired[
        SupplementalDataStorageConfigurationOutputTypeDef
    ]

class VectorKnowledgeBaseConfigurationTypeDef(TypedDict):
    embeddingModelArn: str
    embeddingModelConfiguration: NotRequired[EmbeddingModelConfigurationTypeDef]
    supplementalDataStorageConfiguration: NotRequired[SupplementalDataStorageConfigurationTypeDef]

class KnowledgeBaseDocumentTypeDef(TypedDict):
    content: DocumentContentTypeDef
    metadata: NotRequired[DocumentMetadataTypeDef]

class KnowledgeBaseFlowNodeConfigurationOutputTypeDef(TypedDict):
    knowledgeBaseId: str
    modelId: NotRequired[str]
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]
    numberOfResults: NotRequired[int]
    promptTemplate: NotRequired[KnowledgeBasePromptTemplateTypeDef]
    inferenceConfiguration: NotRequired[PromptInferenceConfigurationOutputTypeDef]
    rerankingConfiguration: NotRequired[VectorSearchRerankingConfigurationOutputTypeDef]
    orchestrationConfiguration: NotRequired[KnowledgeBaseOrchestrationConfigurationOutputTypeDef]

class KnowledgeBaseFlowNodeConfigurationTypeDef(TypedDict):
    knowledgeBaseId: str
    modelId: NotRequired[str]
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]
    numberOfResults: NotRequired[int]
    promptTemplate: NotRequired[KnowledgeBasePromptTemplateTypeDef]
    inferenceConfiguration: NotRequired[PromptInferenceConfigurationTypeDef]
    rerankingConfiguration: NotRequired[VectorSearchRerankingConfigurationTypeDef]
    orchestrationConfiguration: NotRequired[KnowledgeBaseOrchestrationConfigurationTypeDef]

DataSourceConfigurationOutputTypeDef = TypedDict(
    "DataSourceConfigurationOutputTypeDef",
    {
        "type": DataSourceTypeType,
        "s3Configuration": NotRequired[S3DataSourceConfigurationOutputTypeDef],
        "webConfiguration": NotRequired[WebDataSourceConfigurationOutputTypeDef],
        "confluenceConfiguration": NotRequired[ConfluenceDataSourceConfigurationOutputTypeDef],
        "salesforceConfiguration": NotRequired[SalesforceDataSourceConfigurationOutputTypeDef],
        "sharePointConfiguration": NotRequired[SharePointDataSourceConfigurationOutputTypeDef],
    },
)
DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef",
    {
        "type": DataSourceTypeType,
        "s3Configuration": NotRequired[S3DataSourceConfigurationTypeDef],
        "webConfiguration": NotRequired[WebDataSourceConfigurationTypeDef],
        "confluenceConfiguration": NotRequired[ConfluenceDataSourceConfigurationTypeDef],
        "salesforceConfiguration": NotRequired[SalesforceDataSourceConfigurationTypeDef],
        "sharePointConfiguration": NotRequired[SharePointDataSourceConfigurationTypeDef],
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
    text: NotRequired[TextPromptTemplateConfigurationOutputTypeDef]
    chat: NotRequired[ChatPromptTemplateConfigurationOutputTypeDef]

ToolUnionTypeDef = Union[ToolTypeDef, ToolOutputTypeDef]
VectorIngestionConfigurationUnionTypeDef = Union[
    VectorIngestionConfigurationTypeDef, VectorIngestionConfigurationOutputTypeDef
]

class IngestKnowledgeBaseDocumentsRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str
    documents: Sequence[KnowledgeBaseDocumentTypeDef]
    clientToken: NotRequired[str]

class DataSourceTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str
    name: str
    status: DataSourceStatusType
    dataSourceConfiguration: DataSourceConfigurationOutputTypeDef
    createdAt: datetime
    updatedAt: datetime
    description: NotRequired[str]
    serverSideEncryptionConfiguration: NotRequired[ServerSideEncryptionConfigurationTypeDef]
    vectorIngestionConfiguration: NotRequired[VectorIngestionConfigurationOutputTypeDef]
    dataDeletionPolicy: NotRequired[DataDeletionPolicyType]
    failureReasons: NotRequired[List[str]]

DataSourceConfigurationUnionTypeDef = Union[
    DataSourceConfigurationTypeDef, DataSourceConfigurationOutputTypeDef
]
KnowledgeBaseConfigurationOutputTypeDef = TypedDict(
    "KnowledgeBaseConfigurationOutputTypeDef",
    {
        "type": KnowledgeBaseTypeType,
        "vectorKnowledgeBaseConfiguration": NotRequired[
            VectorKnowledgeBaseConfigurationOutputTypeDef
        ],
        "kendraKnowledgeBaseConfiguration": NotRequired[KendraKnowledgeBaseConfigurationTypeDef],
        "sqlKnowledgeBaseConfiguration": NotRequired[SqlKnowledgeBaseConfigurationOutputTypeDef],
    },
)
KnowledgeBaseConfigurationTypeDef = TypedDict(
    "KnowledgeBaseConfigurationTypeDef",
    {
        "type": KnowledgeBaseTypeType,
        "vectorKnowledgeBaseConfiguration": NotRequired[VectorKnowledgeBaseConfigurationTypeDef],
        "kendraKnowledgeBaseConfiguration": NotRequired[KendraKnowledgeBaseConfigurationTypeDef],
        "sqlKnowledgeBaseConfiguration": NotRequired[SqlKnowledgeBaseConfigurationTypeDef],
    },
)

class PromptFlowNodeInlineConfigurationOutputTypeDef(TypedDict):
    templateType: PromptTemplateTypeType
    templateConfiguration: PromptTemplateConfigurationOutputTypeDef
    modelId: str
    inferenceConfiguration: NotRequired[PromptInferenceConfigurationOutputTypeDef]
    additionalModelRequestFields: NotRequired[Dict[str, Any]]

class PromptVariantOutputTypeDef(TypedDict):
    name: str
    templateType: PromptTemplateTypeType
    templateConfiguration: PromptTemplateConfigurationOutputTypeDef
    modelId: NotRequired[str]
    inferenceConfiguration: NotRequired[PromptInferenceConfigurationOutputTypeDef]
    metadata: NotRequired[List[PromptMetadataEntryTypeDef]]
    additionalModelRequestFields: NotRequired[Dict[str, Any]]
    genAiResource: NotRequired[PromptGenAiResourceTypeDef]

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
    knowledgeBaseId: str
    name: str
    dataSourceConfiguration: DataSourceConfigurationUnionTypeDef
    clientToken: NotRequired[str]
    description: NotRequired[str]
    dataDeletionPolicy: NotRequired[DataDeletionPolicyType]
    serverSideEncryptionConfiguration: NotRequired[ServerSideEncryptionConfigurationTypeDef]
    vectorIngestionConfiguration: NotRequired[VectorIngestionConfigurationUnionTypeDef]

class UpdateDataSourceRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    dataSourceId: str
    name: str
    dataSourceConfiguration: DataSourceConfigurationUnionTypeDef
    description: NotRequired[str]
    dataDeletionPolicy: NotRequired[DataDeletionPolicyType]
    serverSideEncryptionConfiguration: NotRequired[ServerSideEncryptionConfigurationTypeDef]
    vectorIngestionConfiguration: NotRequired[VectorIngestionConfigurationUnionTypeDef]

class KnowledgeBaseTypeDef(TypedDict):
    knowledgeBaseId: str
    name: str
    knowledgeBaseArn: str
    roleArn: str
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationOutputTypeDef
    status: KnowledgeBaseStatusType
    createdAt: datetime
    updatedAt: datetime
    description: NotRequired[str]
    storageConfiguration: NotRequired[StorageConfigurationTypeDef]
    failureReasons: NotRequired[List[str]]

KnowledgeBaseConfigurationUnionTypeDef = Union[
    KnowledgeBaseConfigurationTypeDef, KnowledgeBaseConfigurationOutputTypeDef
]

class PromptFlowNodeSourceConfigurationOutputTypeDef(TypedDict):
    resource: NotRequired[PromptFlowNodeResourceConfigurationTypeDef]
    inline: NotRequired[PromptFlowNodeInlineConfigurationOutputTypeDef]

CreatePromptResponseTypeDef = TypedDict(
    "CreatePromptResponseTypeDef",
    {
        "name": str,
        "description": str,
        "customerEncryptionKeyArn": str,
        "defaultVariant": str,
        "variants": List[PromptVariantOutputTypeDef],
        "id": str,
        "arn": str,
        "version": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePromptVersionResponseTypeDef = TypedDict(
    "CreatePromptVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "customerEncryptionKeyArn": str,
        "defaultVariant": str,
        "variants": List[PromptVariantOutputTypeDef],
        "id": str,
        "arn": str,
        "version": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPromptResponseTypeDef = TypedDict(
    "GetPromptResponseTypeDef",
    {
        "name": str,
        "description": str,
        "customerEncryptionKeyArn": str,
        "defaultVariant": str,
        "variants": List[PromptVariantOutputTypeDef],
        "id": str,
        "arn": str,
        "version": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdatePromptResponseTypeDef = TypedDict(
    "UpdatePromptResponseTypeDef",
    {
        "name": str,
        "description": str,
        "customerEncryptionKeyArn": str,
        "defaultVariant": str,
        "variants": List[PromptVariantOutputTypeDef],
        "id": str,
        "arn": str,
        "version": str,
        "createdAt": datetime,
        "updatedAt": datetime,
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
    name: str
    roleArn: str
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationUnionTypeDef
    clientToken: NotRequired[str]
    description: NotRequired[str]
    storageConfiguration: NotRequired[StorageConfigurationTypeDef]
    tags: NotRequired[Mapping[str, str]]

class UpdateKnowledgeBaseRequestTypeDef(TypedDict):
    knowledgeBaseId: str
    name: str
    roleArn: str
    knowledgeBaseConfiguration: KnowledgeBaseConfigurationUnionTypeDef
    description: NotRequired[str]
    storageConfiguration: NotRequired[StorageConfigurationTypeDef]

class PromptFlowNodeConfigurationOutputTypeDef(TypedDict):
    sourceConfiguration: PromptFlowNodeSourceConfigurationOutputTypeDef
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]

class ChatPromptTemplateConfigurationTypeDef(TypedDict):
    messages: Sequence[MessageUnionTypeDef]
    system: NotRequired[Sequence[SystemContentBlockTypeDef]]
    inputVariables: NotRequired[Sequence[PromptInputVariableTypeDef]]
    toolConfiguration: NotRequired[ToolConfigurationUnionTypeDef]

FlowNodeConfigurationOutputTypeDef = TypedDict(
    "FlowNodeConfigurationOutputTypeDef",
    {
        "input": NotRequired[Dict[str, Any]],
        "output": NotRequired[Dict[str, Any]],
        "knowledgeBase": NotRequired[KnowledgeBaseFlowNodeConfigurationOutputTypeDef],
        "condition": NotRequired[ConditionFlowNodeConfigurationOutputTypeDef],
        "lex": NotRequired[LexFlowNodeConfigurationTypeDef],
        "prompt": NotRequired[PromptFlowNodeConfigurationOutputTypeDef],
        "lambdaFunction": NotRequired[LambdaFunctionFlowNodeConfigurationTypeDef],
        "storage": NotRequired[StorageFlowNodeConfigurationTypeDef],
        "agent": NotRequired[AgentFlowNodeConfigurationTypeDef],
        "retrieval": NotRequired[RetrievalFlowNodeConfigurationTypeDef],
        "iterator": NotRequired[Dict[str, Any]],
        "collector": NotRequired[Dict[str, Any]],
        "inlineCode": NotRequired[InlineCodeFlowNodeConfigurationTypeDef],
        "loop": NotRequired[LoopFlowNodeConfigurationOutputTypeDef],
        "loopInput": NotRequired[Dict[str, Any]],
        "loopController": NotRequired[LoopControllerFlowNodeConfigurationTypeDef],
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
    text: NotRequired[TextPromptTemplateConfigurationUnionTypeDef]
    chat: NotRequired[ChatPromptTemplateConfigurationUnionTypeDef]

class FlowDefinitionOutputTypeDef(TypedDict):
    nodes: NotRequired[List[FlowNodeExtraTypeDef]]
    connections: NotRequired[List[FlowConnectionTypeDef]]

class PromptFlowNodeInlineConfigurationTypeDef(TypedDict):
    templateType: PromptTemplateTypeType
    templateConfiguration: PromptTemplateConfigurationTypeDef
    modelId: str
    inferenceConfiguration: NotRequired[PromptInferenceConfigurationTypeDef]
    additionalModelRequestFields: NotRequired[Mapping[str, Any]]

PromptTemplateConfigurationUnionTypeDef = Union[
    PromptTemplateConfigurationTypeDef, PromptTemplateConfigurationOutputTypeDef
]
CreateFlowResponseTypeDef = TypedDict(
    "CreateFlowResponseTypeDef",
    {
        "name": str,
        "description": str,
        "executionRoleArn": str,
        "customerEncryptionKeyArn": str,
        "id": str,
        "arn": str,
        "status": FlowStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "version": str,
        "definition": FlowDefinitionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateFlowVersionResponseTypeDef = TypedDict(
    "CreateFlowVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "executionRoleArn": str,
        "customerEncryptionKeyArn": str,
        "id": str,
        "arn": str,
        "status": FlowStatusType,
        "createdAt": datetime,
        "version": str,
        "definition": FlowDefinitionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFlowResponseTypeDef = TypedDict(
    "GetFlowResponseTypeDef",
    {
        "name": str,
        "description": str,
        "executionRoleArn": str,
        "customerEncryptionKeyArn": str,
        "id": str,
        "arn": str,
        "status": FlowStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "version": str,
        "definition": FlowDefinitionOutputTypeDef,
        "validations": List[FlowValidationTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFlowVersionResponseTypeDef = TypedDict(
    "GetFlowVersionResponseTypeDef",
    {
        "name": str,
        "description": str,
        "executionRoleArn": str,
        "customerEncryptionKeyArn": str,
        "id": str,
        "arn": str,
        "status": FlowStatusType,
        "createdAt": datetime,
        "version": str,
        "definition": FlowDefinitionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateFlowResponseTypeDef = TypedDict(
    "UpdateFlowResponseTypeDef",
    {
        "name": str,
        "description": str,
        "executionRoleArn": str,
        "customerEncryptionKeyArn": str,
        "id": str,
        "arn": str,
        "status": FlowStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "version": str,
        "definition": FlowDefinitionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class PromptFlowNodeSourceConfigurationTypeDef(TypedDict):
    resource: NotRequired[PromptFlowNodeResourceConfigurationTypeDef]
    inline: NotRequired[PromptFlowNodeInlineConfigurationTypeDef]

class PromptVariantTypeDef(TypedDict):
    name: str
    templateType: PromptTemplateTypeType
    templateConfiguration: PromptTemplateConfigurationUnionTypeDef
    modelId: NotRequired[str]
    inferenceConfiguration: NotRequired[PromptInferenceConfigurationUnionTypeDef]
    metadata: NotRequired[Sequence[PromptMetadataEntryTypeDef]]
    additionalModelRequestFields: NotRequired[Mapping[str, Any]]
    genAiResource: NotRequired[PromptGenAiResourceTypeDef]

class PromptFlowNodeConfigurationTypeDef(TypedDict):
    sourceConfiguration: PromptFlowNodeSourceConfigurationTypeDef
    guardrailConfiguration: NotRequired[GuardrailConfigurationTypeDef]

PromptVariantUnionTypeDef = Union[PromptVariantTypeDef, PromptVariantOutputTypeDef]
FlowNodeConfigurationTypeDef = TypedDict(
    "FlowNodeConfigurationTypeDef",
    {
        "input": NotRequired[Mapping[str, Any]],
        "output": NotRequired[Mapping[str, Any]],
        "knowledgeBase": NotRequired[KnowledgeBaseFlowNodeConfigurationTypeDef],
        "condition": NotRequired[ConditionFlowNodeConfigurationTypeDef],
        "lex": NotRequired[LexFlowNodeConfigurationTypeDef],
        "prompt": NotRequired[PromptFlowNodeConfigurationTypeDef],
        "lambdaFunction": NotRequired[LambdaFunctionFlowNodeConfigurationTypeDef],
        "storage": NotRequired[StorageFlowNodeConfigurationTypeDef],
        "agent": NotRequired[AgentFlowNodeConfigurationTypeDef],
        "retrieval": NotRequired[RetrievalFlowNodeConfigurationTypeDef],
        "iterator": NotRequired[Mapping[str, Any]],
        "collector": NotRequired[Mapping[str, Any]],
        "inlineCode": NotRequired[InlineCodeFlowNodeConfigurationTypeDef],
        "loop": NotRequired[LoopFlowNodeConfigurationTypeDef],
        "loopInput": NotRequired[Mapping[str, Any]],
        "loopController": NotRequired[LoopControllerFlowNodeConfigurationTypeDef],
    },
)

class CreatePromptRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    customerEncryptionKeyArn: NotRequired[str]
    defaultVariant: NotRequired[str]
    variants: NotRequired[Sequence[PromptVariantUnionTypeDef]]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdatePromptRequestTypeDef(TypedDict):
    name: str
    promptIdentifier: str
    description: NotRequired[str]
    customerEncryptionKeyArn: NotRequired[str]
    defaultVariant: NotRequired[str]
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
    nodes: NotRequired[Sequence[FlowNodeTypeDef]]
    connections: NotRequired[Sequence[FlowConnectionTypeDef]]

FlowDefinitionUnionTypeDef = Union[FlowDefinitionTypeDef, FlowDefinitionOutputTypeDef]

class CreateFlowRequestTypeDef(TypedDict):
    name: str
    executionRoleArn: str
    description: NotRequired[str]
    customerEncryptionKeyArn: NotRequired[str]
    definition: NotRequired[FlowDefinitionUnionTypeDef]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateFlowRequestTypeDef(TypedDict):
    name: str
    executionRoleArn: str
    flowIdentifier: str
    description: NotRequired[str]
    customerEncryptionKeyArn: NotRequired[str]
    definition: NotRequired[FlowDefinitionUnionTypeDef]

class ValidateFlowDefinitionRequestTypeDef(TypedDict):
    definition: FlowDefinitionUnionTypeDef
