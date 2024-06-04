"""
Type annotations for bedrock-agent service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/literals.html)

Usage::

    ```python
    from mypy_boto3_bedrock_agent.literals import ActionGroupSignatureType

    data: ActionGroupSignatureType = "AMAZON.UserInput"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionGroupSignatureType",
    "ActionGroupStateType",
    "AgentAliasStatusType",
    "AgentStatusType",
    "ChunkingStrategyType",
    "CreationModeType",
    "CustomControlMethodType",
    "DataDeletionPolicyType",
    "DataSourceStatusType",
    "DataSourceTypeType",
    "IngestionJobFilterAttributeType",
    "IngestionJobFilterOperatorType",
    "IngestionJobSortByAttributeType",
    "IngestionJobStatusType",
    "KnowledgeBaseStateType",
    "KnowledgeBaseStatusType",
    "KnowledgeBaseStorageTypeType",
    "KnowledgeBaseTypeType",
    "ListAgentActionGroupsPaginatorName",
    "ListAgentAliasesPaginatorName",
    "ListAgentKnowledgeBasesPaginatorName",
    "ListAgentVersionsPaginatorName",
    "ListAgentsPaginatorName",
    "ListDataSourcesPaginatorName",
    "ListIngestionJobsPaginatorName",
    "ListKnowledgeBasesPaginatorName",
    "PromptStateType",
    "PromptTypeType",
    "SortOrderType",
    "TypeType",
)

ActionGroupSignatureType = Literal["AMAZON.UserInput"]
ActionGroupStateType = Literal["DISABLED", "ENABLED"]
AgentAliasStatusType = Literal["CREATING", "DELETING", "FAILED", "PREPARED", "UPDATING"]
AgentStatusType = Literal[
    "CREATING",
    "DELETING",
    "FAILED",
    "NOT_PREPARED",
    "PREPARED",
    "PREPARING",
    "UPDATING",
    "VERSIONING",
]
ChunkingStrategyType = Literal["FIXED_SIZE", "NONE"]
CreationModeType = Literal["DEFAULT", "OVERRIDDEN"]
CustomControlMethodType = Literal["RETURN_CONTROL"]
DataDeletionPolicyType = Literal["DELETE", "RETAIN"]
DataSourceStatusType = Literal["AVAILABLE", "DELETE_UNSUCCESSFUL", "DELETING"]
DataSourceTypeType = Literal["S3"]
IngestionJobFilterAttributeType = Literal["STATUS"]
IngestionJobFilterOperatorType = Literal["EQ"]
IngestionJobSortByAttributeType = Literal["STARTED_AT", "STATUS"]
IngestionJobStatusType = Literal["COMPLETE", "FAILED", "IN_PROGRESS", "STARTING"]
KnowledgeBaseStateType = Literal["DISABLED", "ENABLED"]
KnowledgeBaseStatusType = Literal[
    "ACTIVE", "CREATING", "DELETE_UNSUCCESSFUL", "DELETING", "FAILED", "UPDATING"
]
KnowledgeBaseStorageTypeType = Literal[
    "MONGO_DB_ATLAS", "OPENSEARCH_SERVERLESS", "PINECONE", "RDS", "REDIS_ENTERPRISE_CLOUD"
]
KnowledgeBaseTypeType = Literal["VECTOR"]
ListAgentActionGroupsPaginatorName = Literal["list_agent_action_groups"]
ListAgentAliasesPaginatorName = Literal["list_agent_aliases"]
ListAgentKnowledgeBasesPaginatorName = Literal["list_agent_knowledge_bases"]
ListAgentVersionsPaginatorName = Literal["list_agent_versions"]
ListAgentsPaginatorName = Literal["list_agents"]
ListDataSourcesPaginatorName = Literal["list_data_sources"]
ListIngestionJobsPaginatorName = Literal["list_ingestion_jobs"]
ListKnowledgeBasesPaginatorName = Literal["list_knowledge_bases"]
PromptStateType = Literal["DISABLED", "ENABLED"]
PromptTypeType = Literal[
    "KNOWLEDGE_BASE_RESPONSE_GENERATION", "ORCHESTRATION", "POST_PROCESSING", "PRE_PROCESSING"
]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
TypeType = Literal["array", "boolean", "integer", "number", "string"]
