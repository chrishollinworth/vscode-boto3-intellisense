"""
Type annotations for bedrock-agent service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/type_defs.html)

Usage::

    ```python
    from mypy_boto3_bedrock_agent.type_defs import APISchemaTypeDef

    data: APISchemaTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ActionGroupStateType,
    AgentAliasStatusType,
    AgentStatusType,
    ChunkingStrategyType,
    CreationModeType,
    DataDeletionPolicyType,
    DataSourceStatusType,
    IngestionJobSortByAttributeType,
    IngestionJobStatusType,
    KnowledgeBaseStateType,
    KnowledgeBaseStatusType,
    KnowledgeBaseStorageTypeType,
    PromptStateType,
    PromptTypeType,
    SortOrderType,
    TypeType,
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
    "APISchemaTypeDef",
    "ActionGroupExecutorTypeDef",
    "ActionGroupSummaryTypeDef",
    "AgentActionGroupTypeDef",
    "AgentAliasHistoryEventTypeDef",
    "AgentAliasRoutingConfigurationListItemTypeDef",
    "AgentAliasSummaryTypeDef",
    "AgentAliasTypeDef",
    "AgentKnowledgeBaseSummaryTypeDef",
    "AgentKnowledgeBaseTypeDef",
    "AgentSummaryTypeDef",
    "AgentTypeDef",
    "AgentVersionSummaryTypeDef",
    "AgentVersionTypeDef",
    "AssociateAgentKnowledgeBaseRequestRequestTypeDef",
    "AssociateAgentKnowledgeBaseResponseTypeDef",
    "BedrockEmbeddingModelConfigurationTypeDef",
    "ChunkingConfigurationTypeDef",
    "CreateAgentActionGroupRequestRequestTypeDef",
    "CreateAgentActionGroupResponseTypeDef",
    "CreateAgentAliasRequestRequestTypeDef",
    "CreateAgentAliasResponseTypeDef",
    "CreateAgentRequestRequestTypeDef",
    "CreateAgentResponseTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateKnowledgeBaseRequestRequestTypeDef",
    "CreateKnowledgeBaseResponseTypeDef",
    "DataSourceConfigurationTypeDef",
    "DataSourceSummaryTypeDef",
    "DataSourceTypeDef",
    "DeleteAgentActionGroupRequestRequestTypeDef",
    "DeleteAgentAliasRequestRequestTypeDef",
    "DeleteAgentAliasResponseTypeDef",
    "DeleteAgentRequestRequestTypeDef",
    "DeleteAgentResponseTypeDef",
    "DeleteAgentVersionRequestRequestTypeDef",
    "DeleteAgentVersionResponseTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteDataSourceResponseTypeDef",
    "DeleteKnowledgeBaseRequestRequestTypeDef",
    "DeleteKnowledgeBaseResponseTypeDef",
    "DisassociateAgentKnowledgeBaseRequestRequestTypeDef",
    "EmbeddingModelConfigurationTypeDef",
    "FixedSizeChunkingConfigurationTypeDef",
    "FunctionSchemaTypeDef",
    "FunctionTypeDef",
    "GetAgentActionGroupRequestRequestTypeDef",
    "GetAgentActionGroupResponseTypeDef",
    "GetAgentAliasRequestRequestTypeDef",
    "GetAgentAliasResponseTypeDef",
    "GetAgentKnowledgeBaseRequestRequestTypeDef",
    "GetAgentKnowledgeBaseResponseTypeDef",
    "GetAgentRequestRequestTypeDef",
    "GetAgentResponseTypeDef",
    "GetAgentVersionRequestRequestTypeDef",
    "GetAgentVersionResponseTypeDef",
    "GetDataSourceRequestRequestTypeDef",
    "GetDataSourceResponseTypeDef",
    "GetIngestionJobRequestRequestTypeDef",
    "GetIngestionJobResponseTypeDef",
    "GetKnowledgeBaseRequestRequestTypeDef",
    "GetKnowledgeBaseResponseTypeDef",
    "GuardrailConfigurationTypeDef",
    "InferenceConfigurationTypeDef",
    "IngestionJobFilterTypeDef",
    "IngestionJobSortByTypeDef",
    "IngestionJobStatisticsTypeDef",
    "IngestionJobSummaryTypeDef",
    "IngestionJobTypeDef",
    "KnowledgeBaseConfigurationTypeDef",
    "KnowledgeBaseSummaryTypeDef",
    "KnowledgeBaseTypeDef",
    "ListAgentActionGroupsRequestRequestTypeDef",
    "ListAgentActionGroupsResponseTypeDef",
    "ListAgentAliasesRequestRequestTypeDef",
    "ListAgentAliasesResponseTypeDef",
    "ListAgentKnowledgeBasesRequestRequestTypeDef",
    "ListAgentKnowledgeBasesResponseTypeDef",
    "ListAgentVersionsRequestRequestTypeDef",
    "ListAgentVersionsResponseTypeDef",
    "ListAgentsRequestRequestTypeDef",
    "ListAgentsResponseTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListIngestionJobsRequestRequestTypeDef",
    "ListIngestionJobsResponseTypeDef",
    "ListKnowledgeBasesRequestRequestTypeDef",
    "ListKnowledgeBasesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MongoDbAtlasConfigurationTypeDef",
    "MongoDbAtlasFieldMappingTypeDef",
    "OpenSearchServerlessConfigurationTypeDef",
    "OpenSearchServerlessFieldMappingTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterDetailTypeDef",
    "PineconeConfigurationTypeDef",
    "PineconeFieldMappingTypeDef",
    "PrepareAgentRequestRequestTypeDef",
    "PrepareAgentResponseTypeDef",
    "PromptConfigurationTypeDef",
    "PromptOverrideConfigurationTypeDef",
    "RdsConfigurationTypeDef",
    "RdsFieldMappingTypeDef",
    "RedisEnterpriseCloudConfigurationTypeDef",
    "RedisEnterpriseCloudFieldMappingTypeDef",
    "ResponseMetadataTypeDef",
    "S3DataSourceConfigurationTypeDef",
    "S3IdentifierTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "StartIngestionJobRequestRequestTypeDef",
    "StartIngestionJobResponseTypeDef",
    "StorageConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAgentActionGroupRequestRequestTypeDef",
    "UpdateAgentActionGroupResponseTypeDef",
    "UpdateAgentAliasRequestRequestTypeDef",
    "UpdateAgentAliasResponseTypeDef",
    "UpdateAgentKnowledgeBaseRequestRequestTypeDef",
    "UpdateAgentKnowledgeBaseResponseTypeDef",
    "UpdateAgentRequestRequestTypeDef",
    "UpdateAgentResponseTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "UpdateDataSourceResponseTypeDef",
    "UpdateKnowledgeBaseRequestRequestTypeDef",
    "UpdateKnowledgeBaseResponseTypeDef",
    "VectorIngestionConfigurationTypeDef",
    "VectorKnowledgeBaseConfigurationTypeDef",
)

APISchemaTypeDef = TypedDict(
    "APISchemaTypeDef",
    {
        "payload": str,
        "s3": "S3IdentifierTypeDef",
    },
    total=False,
)

ActionGroupExecutorTypeDef = TypedDict(
    "ActionGroupExecutorTypeDef",
    {
        "customControl": Literal["RETURN_CONTROL"],
        "lambda": str,
    },
    total=False,
)

_RequiredActionGroupSummaryTypeDef = TypedDict(
    "_RequiredActionGroupSummaryTypeDef",
    {
        "actionGroupId": str,
        "actionGroupName": str,
        "actionGroupState": ActionGroupStateType,
        "updatedAt": datetime,
    },
)
_OptionalActionGroupSummaryTypeDef = TypedDict(
    "_OptionalActionGroupSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class ActionGroupSummaryTypeDef(
    _RequiredActionGroupSummaryTypeDef, _OptionalActionGroupSummaryTypeDef
):
    pass

_RequiredAgentActionGroupTypeDef = TypedDict(
    "_RequiredAgentActionGroupTypeDef",
    {
        "actionGroupId": str,
        "actionGroupName": str,
        "actionGroupState": ActionGroupStateType,
        "agentId": str,
        "agentVersion": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalAgentActionGroupTypeDef = TypedDict(
    "_OptionalAgentActionGroupTypeDef",
    {
        "actionGroupExecutor": "ActionGroupExecutorTypeDef",
        "apiSchema": "APISchemaTypeDef",
        "clientToken": str,
        "description": str,
        "functionSchema": "FunctionSchemaTypeDef",
        "parentActionSignature": Literal["AMAZON.UserInput"],
    },
    total=False,
)

class AgentActionGroupTypeDef(_RequiredAgentActionGroupTypeDef, _OptionalAgentActionGroupTypeDef):
    pass

AgentAliasHistoryEventTypeDef = TypedDict(
    "AgentAliasHistoryEventTypeDef",
    {
        "endDate": datetime,
        "routingConfiguration": List["AgentAliasRoutingConfigurationListItemTypeDef"],
        "startDate": datetime,
    },
    total=False,
)

AgentAliasRoutingConfigurationListItemTypeDef = TypedDict(
    "AgentAliasRoutingConfigurationListItemTypeDef",
    {
        "agentVersion": str,
        "provisionedThroughput": str,
    },
    total=False,
)

_RequiredAgentAliasSummaryTypeDef = TypedDict(
    "_RequiredAgentAliasSummaryTypeDef",
    {
        "agentAliasId": str,
        "agentAliasName": str,
        "agentAliasStatus": AgentAliasStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalAgentAliasSummaryTypeDef = TypedDict(
    "_OptionalAgentAliasSummaryTypeDef",
    {
        "description": str,
        "routingConfiguration": List["AgentAliasRoutingConfigurationListItemTypeDef"],
    },
    total=False,
)

class AgentAliasSummaryTypeDef(
    _RequiredAgentAliasSummaryTypeDef, _OptionalAgentAliasSummaryTypeDef
):
    pass

_RequiredAgentAliasTypeDef = TypedDict(
    "_RequiredAgentAliasTypeDef",
    {
        "agentAliasArn": str,
        "agentAliasId": str,
        "agentAliasName": str,
        "agentAliasStatus": AgentAliasStatusType,
        "agentId": str,
        "createdAt": datetime,
        "routingConfiguration": List["AgentAliasRoutingConfigurationListItemTypeDef"],
        "updatedAt": datetime,
    },
)
_OptionalAgentAliasTypeDef = TypedDict(
    "_OptionalAgentAliasTypeDef",
    {
        "agentAliasHistoryEvents": List["AgentAliasHistoryEventTypeDef"],
        "clientToken": str,
        "description": str,
        "failureReasons": List[str],
    },
    total=False,
)

class AgentAliasTypeDef(_RequiredAgentAliasTypeDef, _OptionalAgentAliasTypeDef):
    pass

_RequiredAgentKnowledgeBaseSummaryTypeDef = TypedDict(
    "_RequiredAgentKnowledgeBaseSummaryTypeDef",
    {
        "knowledgeBaseId": str,
        "knowledgeBaseState": KnowledgeBaseStateType,
        "updatedAt": datetime,
    },
)
_OptionalAgentKnowledgeBaseSummaryTypeDef = TypedDict(
    "_OptionalAgentKnowledgeBaseSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class AgentKnowledgeBaseSummaryTypeDef(
    _RequiredAgentKnowledgeBaseSummaryTypeDef, _OptionalAgentKnowledgeBaseSummaryTypeDef
):
    pass

AgentKnowledgeBaseTypeDef = TypedDict(
    "AgentKnowledgeBaseTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "createdAt": datetime,
        "description": str,
        "knowledgeBaseId": str,
        "knowledgeBaseState": KnowledgeBaseStateType,
        "updatedAt": datetime,
    },
)

_RequiredAgentSummaryTypeDef = TypedDict(
    "_RequiredAgentSummaryTypeDef",
    {
        "agentId": str,
        "agentName": str,
        "agentStatus": AgentStatusType,
        "updatedAt": datetime,
    },
)
_OptionalAgentSummaryTypeDef = TypedDict(
    "_OptionalAgentSummaryTypeDef",
    {
        "description": str,
        "guardrailConfiguration": "GuardrailConfigurationTypeDef",
        "latestAgentVersion": str,
    },
    total=False,
)

class AgentSummaryTypeDef(_RequiredAgentSummaryTypeDef, _OptionalAgentSummaryTypeDef):
    pass

_RequiredAgentTypeDef = TypedDict(
    "_RequiredAgentTypeDef",
    {
        "agentArn": str,
        "agentId": str,
        "agentName": str,
        "agentResourceRoleArn": str,
        "agentStatus": AgentStatusType,
        "agentVersion": str,
        "createdAt": datetime,
        "idleSessionTTLInSeconds": int,
        "updatedAt": datetime,
    },
)
_OptionalAgentTypeDef = TypedDict(
    "_OptionalAgentTypeDef",
    {
        "clientToken": str,
        "customerEncryptionKeyArn": str,
        "description": str,
        "failureReasons": List[str],
        "foundationModel": str,
        "guardrailConfiguration": "GuardrailConfigurationTypeDef",
        "instruction": str,
        "preparedAt": datetime,
        "promptOverrideConfiguration": "PromptOverrideConfigurationTypeDef",
        "recommendedActions": List[str],
    },
    total=False,
)

class AgentTypeDef(_RequiredAgentTypeDef, _OptionalAgentTypeDef):
    pass

_RequiredAgentVersionSummaryTypeDef = TypedDict(
    "_RequiredAgentVersionSummaryTypeDef",
    {
        "agentName": str,
        "agentStatus": AgentStatusType,
        "agentVersion": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalAgentVersionSummaryTypeDef = TypedDict(
    "_OptionalAgentVersionSummaryTypeDef",
    {
        "description": str,
        "guardrailConfiguration": "GuardrailConfigurationTypeDef",
    },
    total=False,
)

class AgentVersionSummaryTypeDef(
    _RequiredAgentVersionSummaryTypeDef, _OptionalAgentVersionSummaryTypeDef
):
    pass

_RequiredAgentVersionTypeDef = TypedDict(
    "_RequiredAgentVersionTypeDef",
    {
        "agentArn": str,
        "agentId": str,
        "agentName": str,
        "agentResourceRoleArn": str,
        "agentStatus": AgentStatusType,
        "createdAt": datetime,
        "idleSessionTTLInSeconds": int,
        "updatedAt": datetime,
        "version": str,
    },
)
_OptionalAgentVersionTypeDef = TypedDict(
    "_OptionalAgentVersionTypeDef",
    {
        "customerEncryptionKeyArn": str,
        "description": str,
        "failureReasons": List[str],
        "foundationModel": str,
        "guardrailConfiguration": "GuardrailConfigurationTypeDef",
        "instruction": str,
        "promptOverrideConfiguration": "PromptOverrideConfigurationTypeDef",
        "recommendedActions": List[str],
    },
    total=False,
)

class AgentVersionTypeDef(_RequiredAgentVersionTypeDef, _OptionalAgentVersionTypeDef):
    pass

_RequiredAssociateAgentKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateAgentKnowledgeBaseRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "description": str,
        "knowledgeBaseId": str,
    },
)
_OptionalAssociateAgentKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateAgentKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseState": KnowledgeBaseStateType,
    },
    total=False,
)

class AssociateAgentKnowledgeBaseRequestRequestTypeDef(
    _RequiredAssociateAgentKnowledgeBaseRequestRequestTypeDef,
    _OptionalAssociateAgentKnowledgeBaseRequestRequestTypeDef,
):
    pass

AssociateAgentKnowledgeBaseResponseTypeDef = TypedDict(
    "AssociateAgentKnowledgeBaseResponseTypeDef",
    {
        "agentKnowledgeBase": "AgentKnowledgeBaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BedrockEmbeddingModelConfigurationTypeDef = TypedDict(
    "BedrockEmbeddingModelConfigurationTypeDef",
    {
        "dimensions": int,
    },
    total=False,
)

_RequiredChunkingConfigurationTypeDef = TypedDict(
    "_RequiredChunkingConfigurationTypeDef",
    {
        "chunkingStrategy": ChunkingStrategyType,
    },
)
_OptionalChunkingConfigurationTypeDef = TypedDict(
    "_OptionalChunkingConfigurationTypeDef",
    {
        "fixedSizeChunkingConfiguration": "FixedSizeChunkingConfigurationTypeDef",
    },
    total=False,
)

class ChunkingConfigurationTypeDef(
    _RequiredChunkingConfigurationTypeDef, _OptionalChunkingConfigurationTypeDef
):
    pass

_RequiredCreateAgentActionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAgentActionGroupRequestRequestTypeDef",
    {
        "actionGroupName": str,
        "agentId": str,
        "agentVersion": str,
    },
)
_OptionalCreateAgentActionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAgentActionGroupRequestRequestTypeDef",
    {
        "actionGroupExecutor": "ActionGroupExecutorTypeDef",
        "actionGroupState": ActionGroupStateType,
        "apiSchema": "APISchemaTypeDef",
        "clientToken": str,
        "description": str,
        "functionSchema": "FunctionSchemaTypeDef",
        "parentActionGroupSignature": Literal["AMAZON.UserInput"],
    },
    total=False,
)

class CreateAgentActionGroupRequestRequestTypeDef(
    _RequiredCreateAgentActionGroupRequestRequestTypeDef,
    _OptionalCreateAgentActionGroupRequestRequestTypeDef,
):
    pass

CreateAgentActionGroupResponseTypeDef = TypedDict(
    "CreateAgentActionGroupResponseTypeDef",
    {
        "agentActionGroup": "AgentActionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAgentAliasRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAgentAliasRequestRequestTypeDef",
    {
        "agentAliasName": str,
        "agentId": str,
    },
)
_OptionalCreateAgentAliasRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAgentAliasRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "routingConfiguration": List["AgentAliasRoutingConfigurationListItemTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateAgentAliasRequestRequestTypeDef(
    _RequiredCreateAgentAliasRequestRequestTypeDef, _OptionalCreateAgentAliasRequestRequestTypeDef
):
    pass

CreateAgentAliasResponseTypeDef = TypedDict(
    "CreateAgentAliasResponseTypeDef",
    {
        "agentAlias": "AgentAliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAgentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAgentRequestRequestTypeDef",
    {
        "agentName": str,
    },
)
_OptionalCreateAgentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAgentRequestRequestTypeDef",
    {
        "agentResourceRoleArn": str,
        "clientToken": str,
        "customerEncryptionKeyArn": str,
        "description": str,
        "foundationModel": str,
        "guardrailConfiguration": "GuardrailConfigurationTypeDef",
        "idleSessionTTLInSeconds": int,
        "instruction": str,
        "promptOverrideConfiguration": "PromptOverrideConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateAgentRequestRequestTypeDef(
    _RequiredCreateAgentRequestRequestTypeDef, _OptionalCreateAgentRequestRequestTypeDef
):
    pass

CreateAgentResponseTypeDef = TypedDict(
    "CreateAgentResponseTypeDef",
    {
        "agent": "AgentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataSourceRequestRequestTypeDef",
    {
        "dataSourceConfiguration": "DataSourceConfigurationTypeDef",
        "knowledgeBaseId": str,
        "name": str,
    },
)
_OptionalCreateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataSourceRequestRequestTypeDef",
    {
        "clientToken": str,
        "dataDeletionPolicy": DataDeletionPolicyType,
        "description": str,
        "serverSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "vectorIngestionConfiguration": "VectorIngestionConfigurationTypeDef",
    },
    total=False,
)

class CreateDataSourceRequestRequestTypeDef(
    _RequiredCreateDataSourceRequestRequestTypeDef, _OptionalCreateDataSourceRequestRequestTypeDef
):
    pass

CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "dataSource": "DataSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseConfiguration": "KnowledgeBaseConfigurationTypeDef",
        "name": str,
        "roleArn": str,
        "storageConfiguration": "StorageConfigurationTypeDef",
    },
)
_OptionalCreateKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateKnowledgeBaseRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateKnowledgeBaseRequestRequestTypeDef(
    _RequiredCreateKnowledgeBaseRequestRequestTypeDef,
    _OptionalCreateKnowledgeBaseRequestRequestTypeDef,
):
    pass

CreateKnowledgeBaseResponseTypeDef = TypedDict(
    "CreateKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBase": "KnowledgeBaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDataSourceConfigurationTypeDef = TypedDict(
    "_RequiredDataSourceConfigurationTypeDef",
    {
        "type": Literal["S3"],
    },
)
_OptionalDataSourceConfigurationTypeDef = TypedDict(
    "_OptionalDataSourceConfigurationTypeDef",
    {
        "s3Configuration": "S3DataSourceConfigurationTypeDef",
    },
    total=False,
)

class DataSourceConfigurationTypeDef(
    _RequiredDataSourceConfigurationTypeDef, _OptionalDataSourceConfigurationTypeDef
):
    pass

_RequiredDataSourceSummaryTypeDef = TypedDict(
    "_RequiredDataSourceSummaryTypeDef",
    {
        "dataSourceId": str,
        "knowledgeBaseId": str,
        "name": str,
        "status": DataSourceStatusType,
        "updatedAt": datetime,
    },
)
_OptionalDataSourceSummaryTypeDef = TypedDict(
    "_OptionalDataSourceSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class DataSourceSummaryTypeDef(
    _RequiredDataSourceSummaryTypeDef, _OptionalDataSourceSummaryTypeDef
):
    pass

_RequiredDataSourceTypeDef = TypedDict(
    "_RequiredDataSourceTypeDef",
    {
        "createdAt": datetime,
        "dataSourceConfiguration": "DataSourceConfigurationTypeDef",
        "dataSourceId": str,
        "knowledgeBaseId": str,
        "name": str,
        "status": DataSourceStatusType,
        "updatedAt": datetime,
    },
)
_OptionalDataSourceTypeDef = TypedDict(
    "_OptionalDataSourceTypeDef",
    {
        "dataDeletionPolicy": DataDeletionPolicyType,
        "description": str,
        "failureReasons": List[str],
        "serverSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "vectorIngestionConfiguration": "VectorIngestionConfigurationTypeDef",
    },
    total=False,
)

class DataSourceTypeDef(_RequiredDataSourceTypeDef, _OptionalDataSourceTypeDef):
    pass

_RequiredDeleteAgentActionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAgentActionGroupRequestRequestTypeDef",
    {
        "actionGroupId": str,
        "agentId": str,
        "agentVersion": str,
    },
)
_OptionalDeleteAgentActionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAgentActionGroupRequestRequestTypeDef",
    {
        "skipResourceInUseCheck": bool,
    },
    total=False,
)

class DeleteAgentActionGroupRequestRequestTypeDef(
    _RequiredDeleteAgentActionGroupRequestRequestTypeDef,
    _OptionalDeleteAgentActionGroupRequestRequestTypeDef,
):
    pass

DeleteAgentAliasRequestRequestTypeDef = TypedDict(
    "DeleteAgentAliasRequestRequestTypeDef",
    {
        "agentAliasId": str,
        "agentId": str,
    },
)

DeleteAgentAliasResponseTypeDef = TypedDict(
    "DeleteAgentAliasResponseTypeDef",
    {
        "agentAliasId": str,
        "agentAliasStatus": AgentAliasStatusType,
        "agentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAgentRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAgentRequestRequestTypeDef",
    {
        "agentId": str,
    },
)
_OptionalDeleteAgentRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAgentRequestRequestTypeDef",
    {
        "skipResourceInUseCheck": bool,
    },
    total=False,
)

class DeleteAgentRequestRequestTypeDef(
    _RequiredDeleteAgentRequestRequestTypeDef, _OptionalDeleteAgentRequestRequestTypeDef
):
    pass

DeleteAgentResponseTypeDef = TypedDict(
    "DeleteAgentResponseTypeDef",
    {
        "agentId": str,
        "agentStatus": AgentStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAgentVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAgentVersionRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
    },
)
_OptionalDeleteAgentVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAgentVersionRequestRequestTypeDef",
    {
        "skipResourceInUseCheck": bool,
    },
    total=False,
)

class DeleteAgentVersionRequestRequestTypeDef(
    _RequiredDeleteAgentVersionRequestRequestTypeDef,
    _OptionalDeleteAgentVersionRequestRequestTypeDef,
):
    pass

DeleteAgentVersionResponseTypeDef = TypedDict(
    "DeleteAgentVersionResponseTypeDef",
    {
        "agentId": str,
        "agentStatus": AgentStatusType,
        "agentVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "dataSourceId": str,
        "knowledgeBaseId": str,
    },
)

DeleteDataSourceResponseTypeDef = TypedDict(
    "DeleteDataSourceResponseTypeDef",
    {
        "dataSourceId": str,
        "knowledgeBaseId": str,
        "status": DataSourceStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "DeleteKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)

DeleteKnowledgeBaseResponseTypeDef = TypedDict(
    "DeleteKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBaseId": str,
        "status": KnowledgeBaseStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateAgentKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "DisassociateAgentKnowledgeBaseRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "knowledgeBaseId": str,
    },
)

EmbeddingModelConfigurationTypeDef = TypedDict(
    "EmbeddingModelConfigurationTypeDef",
    {
        "bedrockEmbeddingModelConfiguration": "BedrockEmbeddingModelConfigurationTypeDef",
    },
    total=False,
)

FixedSizeChunkingConfigurationTypeDef = TypedDict(
    "FixedSizeChunkingConfigurationTypeDef",
    {
        "maxTokens": int,
        "overlapPercentage": int,
    },
)

FunctionSchemaTypeDef = TypedDict(
    "FunctionSchemaTypeDef",
    {
        "functions": List["FunctionTypeDef"],
    },
    total=False,
)

_RequiredFunctionTypeDef = TypedDict(
    "_RequiredFunctionTypeDef",
    {
        "name": str,
    },
)
_OptionalFunctionTypeDef = TypedDict(
    "_OptionalFunctionTypeDef",
    {
        "description": str,
        "parameters": Dict[str, "ParameterDetailTypeDef"],
    },
    total=False,
)

class FunctionTypeDef(_RequiredFunctionTypeDef, _OptionalFunctionTypeDef):
    pass

GetAgentActionGroupRequestRequestTypeDef = TypedDict(
    "GetAgentActionGroupRequestRequestTypeDef",
    {
        "actionGroupId": str,
        "agentId": str,
        "agentVersion": str,
    },
)

GetAgentActionGroupResponseTypeDef = TypedDict(
    "GetAgentActionGroupResponseTypeDef",
    {
        "agentActionGroup": "AgentActionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAgentAliasRequestRequestTypeDef = TypedDict(
    "GetAgentAliasRequestRequestTypeDef",
    {
        "agentAliasId": str,
        "agentId": str,
    },
)

GetAgentAliasResponseTypeDef = TypedDict(
    "GetAgentAliasResponseTypeDef",
    {
        "agentAlias": "AgentAliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAgentKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "GetAgentKnowledgeBaseRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "knowledgeBaseId": str,
    },
)

GetAgentKnowledgeBaseResponseTypeDef = TypedDict(
    "GetAgentKnowledgeBaseResponseTypeDef",
    {
        "agentKnowledgeBase": "AgentKnowledgeBaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAgentRequestRequestTypeDef = TypedDict(
    "GetAgentRequestRequestTypeDef",
    {
        "agentId": str,
    },
)

GetAgentResponseTypeDef = TypedDict(
    "GetAgentResponseTypeDef",
    {
        "agent": "AgentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAgentVersionRequestRequestTypeDef = TypedDict(
    "GetAgentVersionRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
    },
)

GetAgentVersionResponseTypeDef = TypedDict(
    "GetAgentVersionResponseTypeDef",
    {
        "agentVersion": "AgentVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataSourceRequestRequestTypeDef = TypedDict(
    "GetDataSourceRequestRequestTypeDef",
    {
        "dataSourceId": str,
        "knowledgeBaseId": str,
    },
)

GetDataSourceResponseTypeDef = TypedDict(
    "GetDataSourceResponseTypeDef",
    {
        "dataSource": "DataSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIngestionJobRequestRequestTypeDef = TypedDict(
    "GetIngestionJobRequestRequestTypeDef",
    {
        "dataSourceId": str,
        "ingestionJobId": str,
        "knowledgeBaseId": str,
    },
)

GetIngestionJobResponseTypeDef = TypedDict(
    "GetIngestionJobResponseTypeDef",
    {
        "ingestionJob": "IngestionJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "GetKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)

GetKnowledgeBaseResponseTypeDef = TypedDict(
    "GetKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBase": "KnowledgeBaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GuardrailConfigurationTypeDef = TypedDict(
    "GuardrailConfigurationTypeDef",
    {
        "guardrailIdentifier": str,
        "guardrailVersion": str,
    },
    total=False,
)

InferenceConfigurationTypeDef = TypedDict(
    "InferenceConfigurationTypeDef",
    {
        "maximumLength": int,
        "stopSequences": List[str],
        "temperature": float,
        "topK": int,
        "topP": float,
    },
    total=False,
)

IngestionJobFilterTypeDef = TypedDict(
    "IngestionJobFilterTypeDef",
    {
        "attribute": Literal["STATUS"],
        "operator": Literal["EQ"],
        "values": List[str],
    },
)

IngestionJobSortByTypeDef = TypedDict(
    "IngestionJobSortByTypeDef",
    {
        "attribute": IngestionJobSortByAttributeType,
        "order": SortOrderType,
    },
)

IngestionJobStatisticsTypeDef = TypedDict(
    "IngestionJobStatisticsTypeDef",
    {
        "numberOfDocumentsDeleted": int,
        "numberOfDocumentsFailed": int,
        "numberOfDocumentsScanned": int,
        "numberOfMetadataDocumentsModified": int,
        "numberOfMetadataDocumentsScanned": int,
        "numberOfModifiedDocumentsIndexed": int,
        "numberOfNewDocumentsIndexed": int,
    },
    total=False,
)

_RequiredIngestionJobSummaryTypeDef = TypedDict(
    "_RequiredIngestionJobSummaryTypeDef",
    {
        "dataSourceId": str,
        "ingestionJobId": str,
        "knowledgeBaseId": str,
        "startedAt": datetime,
        "status": IngestionJobStatusType,
        "updatedAt": datetime,
    },
)
_OptionalIngestionJobSummaryTypeDef = TypedDict(
    "_OptionalIngestionJobSummaryTypeDef",
    {
        "description": str,
        "statistics": "IngestionJobStatisticsTypeDef",
    },
    total=False,
)

class IngestionJobSummaryTypeDef(
    _RequiredIngestionJobSummaryTypeDef, _OptionalIngestionJobSummaryTypeDef
):
    pass

_RequiredIngestionJobTypeDef = TypedDict(
    "_RequiredIngestionJobTypeDef",
    {
        "dataSourceId": str,
        "ingestionJobId": str,
        "knowledgeBaseId": str,
        "startedAt": datetime,
        "status": IngestionJobStatusType,
        "updatedAt": datetime,
    },
)
_OptionalIngestionJobTypeDef = TypedDict(
    "_OptionalIngestionJobTypeDef",
    {
        "description": str,
        "failureReasons": List[str],
        "statistics": "IngestionJobStatisticsTypeDef",
    },
    total=False,
)

class IngestionJobTypeDef(_RequiredIngestionJobTypeDef, _OptionalIngestionJobTypeDef):
    pass

_RequiredKnowledgeBaseConfigurationTypeDef = TypedDict(
    "_RequiredKnowledgeBaseConfigurationTypeDef",
    {
        "type": Literal["VECTOR"],
    },
)
_OptionalKnowledgeBaseConfigurationTypeDef = TypedDict(
    "_OptionalKnowledgeBaseConfigurationTypeDef",
    {
        "vectorKnowledgeBaseConfiguration": "VectorKnowledgeBaseConfigurationTypeDef",
    },
    total=False,
)

class KnowledgeBaseConfigurationTypeDef(
    _RequiredKnowledgeBaseConfigurationTypeDef, _OptionalKnowledgeBaseConfigurationTypeDef
):
    pass

_RequiredKnowledgeBaseSummaryTypeDef = TypedDict(
    "_RequiredKnowledgeBaseSummaryTypeDef",
    {
        "knowledgeBaseId": str,
        "name": str,
        "status": KnowledgeBaseStatusType,
        "updatedAt": datetime,
    },
)
_OptionalKnowledgeBaseSummaryTypeDef = TypedDict(
    "_OptionalKnowledgeBaseSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class KnowledgeBaseSummaryTypeDef(
    _RequiredKnowledgeBaseSummaryTypeDef, _OptionalKnowledgeBaseSummaryTypeDef
):
    pass

_RequiredKnowledgeBaseTypeDef = TypedDict(
    "_RequiredKnowledgeBaseTypeDef",
    {
        "createdAt": datetime,
        "knowledgeBaseArn": str,
        "knowledgeBaseConfiguration": "KnowledgeBaseConfigurationTypeDef",
        "knowledgeBaseId": str,
        "name": str,
        "roleArn": str,
        "status": KnowledgeBaseStatusType,
        "storageConfiguration": "StorageConfigurationTypeDef",
        "updatedAt": datetime,
    },
)
_OptionalKnowledgeBaseTypeDef = TypedDict(
    "_OptionalKnowledgeBaseTypeDef",
    {
        "description": str,
        "failureReasons": List[str],
    },
    total=False,
)

class KnowledgeBaseTypeDef(_RequiredKnowledgeBaseTypeDef, _OptionalKnowledgeBaseTypeDef):
    pass

_RequiredListAgentActionGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListAgentActionGroupsRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
    },
)
_OptionalListAgentActionGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListAgentActionGroupsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAgentActionGroupsRequestRequestTypeDef(
    _RequiredListAgentActionGroupsRequestRequestTypeDef,
    _OptionalListAgentActionGroupsRequestRequestTypeDef,
):
    pass

ListAgentActionGroupsResponseTypeDef = TypedDict(
    "ListAgentActionGroupsResponseTypeDef",
    {
        "actionGroupSummaries": List["ActionGroupSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAgentAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredListAgentAliasesRequestRequestTypeDef",
    {
        "agentId": str,
    },
)
_OptionalListAgentAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalListAgentAliasesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAgentAliasesRequestRequestTypeDef(
    _RequiredListAgentAliasesRequestRequestTypeDef, _OptionalListAgentAliasesRequestRequestTypeDef
):
    pass

ListAgentAliasesResponseTypeDef = TypedDict(
    "ListAgentAliasesResponseTypeDef",
    {
        "agentAliasSummaries": List["AgentAliasSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAgentKnowledgeBasesRequestRequestTypeDef = TypedDict(
    "_RequiredListAgentKnowledgeBasesRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
    },
)
_OptionalListAgentKnowledgeBasesRequestRequestTypeDef = TypedDict(
    "_OptionalListAgentKnowledgeBasesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAgentKnowledgeBasesRequestRequestTypeDef(
    _RequiredListAgentKnowledgeBasesRequestRequestTypeDef,
    _OptionalListAgentKnowledgeBasesRequestRequestTypeDef,
):
    pass

ListAgentKnowledgeBasesResponseTypeDef = TypedDict(
    "ListAgentKnowledgeBasesResponseTypeDef",
    {
        "agentKnowledgeBaseSummaries": List["AgentKnowledgeBaseSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAgentVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListAgentVersionsRequestRequestTypeDef",
    {
        "agentId": str,
    },
)
_OptionalListAgentVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListAgentVersionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAgentVersionsRequestRequestTypeDef(
    _RequiredListAgentVersionsRequestRequestTypeDef, _OptionalListAgentVersionsRequestRequestTypeDef
):
    pass

ListAgentVersionsResponseTypeDef = TypedDict(
    "ListAgentVersionsResponseTypeDef",
    {
        "agentVersionSummaries": List["AgentVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAgentsRequestRequestTypeDef = TypedDict(
    "ListAgentsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListAgentsResponseTypeDef = TypedDict(
    "ListAgentsResponseTypeDef",
    {
        "agentSummaries": List["AgentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDataSourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListDataSourcesRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)
_OptionalListDataSourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListDataSourcesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListDataSourcesRequestRequestTypeDef(
    _RequiredListDataSourcesRequestRequestTypeDef, _OptionalListDataSourcesRequestRequestTypeDef
):
    pass

ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "dataSourceSummaries": List["DataSourceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIngestionJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListIngestionJobsRequestRequestTypeDef",
    {
        "dataSourceId": str,
        "knowledgeBaseId": str,
    },
)
_OptionalListIngestionJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListIngestionJobsRequestRequestTypeDef",
    {
        "filters": List["IngestionJobFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "sortBy": "IngestionJobSortByTypeDef",
    },
    total=False,
)

class ListIngestionJobsRequestRequestTypeDef(
    _RequiredListIngestionJobsRequestRequestTypeDef, _OptionalListIngestionJobsRequestRequestTypeDef
):
    pass

ListIngestionJobsResponseTypeDef = TypedDict(
    "ListIngestionJobsResponseTypeDef",
    {
        "ingestionJobSummaries": List["IngestionJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKnowledgeBasesRequestRequestTypeDef = TypedDict(
    "ListKnowledgeBasesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListKnowledgeBasesResponseTypeDef = TypedDict(
    "ListKnowledgeBasesResponseTypeDef",
    {
        "knowledgeBaseSummaries": List["KnowledgeBaseSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMongoDbAtlasConfigurationTypeDef = TypedDict(
    "_RequiredMongoDbAtlasConfigurationTypeDef",
    {
        "collectionName": str,
        "credentialsSecretArn": str,
        "databaseName": str,
        "endpoint": str,
        "fieldMapping": "MongoDbAtlasFieldMappingTypeDef",
        "vectorIndexName": str,
    },
)
_OptionalMongoDbAtlasConfigurationTypeDef = TypedDict(
    "_OptionalMongoDbAtlasConfigurationTypeDef",
    {
        "endpointServiceName": str,
    },
    total=False,
)

class MongoDbAtlasConfigurationTypeDef(
    _RequiredMongoDbAtlasConfigurationTypeDef, _OptionalMongoDbAtlasConfigurationTypeDef
):
    pass

MongoDbAtlasFieldMappingTypeDef = TypedDict(
    "MongoDbAtlasFieldMappingTypeDef",
    {
        "metadataField": str,
        "textField": str,
        "vectorField": str,
    },
)

OpenSearchServerlessConfigurationTypeDef = TypedDict(
    "OpenSearchServerlessConfigurationTypeDef",
    {
        "collectionArn": str,
        "fieldMapping": "OpenSearchServerlessFieldMappingTypeDef",
        "vectorIndexName": str,
    },
)

OpenSearchServerlessFieldMappingTypeDef = TypedDict(
    "OpenSearchServerlessFieldMappingTypeDef",
    {
        "metadataField": str,
        "textField": str,
        "vectorField": str,
    },
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

_RequiredParameterDetailTypeDef = TypedDict(
    "_RequiredParameterDetailTypeDef",
    {
        "type": TypeType,
    },
)
_OptionalParameterDetailTypeDef = TypedDict(
    "_OptionalParameterDetailTypeDef",
    {
        "description": str,
        "required": bool,
    },
    total=False,
)

class ParameterDetailTypeDef(_RequiredParameterDetailTypeDef, _OptionalParameterDetailTypeDef):
    pass

_RequiredPineconeConfigurationTypeDef = TypedDict(
    "_RequiredPineconeConfigurationTypeDef",
    {
        "connectionString": str,
        "credentialsSecretArn": str,
        "fieldMapping": "PineconeFieldMappingTypeDef",
    },
)
_OptionalPineconeConfigurationTypeDef = TypedDict(
    "_OptionalPineconeConfigurationTypeDef",
    {
        "namespace": str,
    },
    total=False,
)

class PineconeConfigurationTypeDef(
    _RequiredPineconeConfigurationTypeDef, _OptionalPineconeConfigurationTypeDef
):
    pass

PineconeFieldMappingTypeDef = TypedDict(
    "PineconeFieldMappingTypeDef",
    {
        "metadataField": str,
        "textField": str,
    },
)

PrepareAgentRequestRequestTypeDef = TypedDict(
    "PrepareAgentRequestRequestTypeDef",
    {
        "agentId": str,
    },
)

PrepareAgentResponseTypeDef = TypedDict(
    "PrepareAgentResponseTypeDef",
    {
        "agentId": str,
        "agentStatus": AgentStatusType,
        "agentVersion": str,
        "preparedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PromptConfigurationTypeDef = TypedDict(
    "PromptConfigurationTypeDef",
    {
        "basePromptTemplate": str,
        "inferenceConfiguration": "InferenceConfigurationTypeDef",
        "parserMode": CreationModeType,
        "promptCreationMode": CreationModeType,
        "promptState": PromptStateType,
        "promptType": PromptTypeType,
    },
    total=False,
)

_RequiredPromptOverrideConfigurationTypeDef = TypedDict(
    "_RequiredPromptOverrideConfigurationTypeDef",
    {
        "promptConfigurations": List["PromptConfigurationTypeDef"],
    },
)
_OptionalPromptOverrideConfigurationTypeDef = TypedDict(
    "_OptionalPromptOverrideConfigurationTypeDef",
    {
        "overrideLambda": str,
    },
    total=False,
)

class PromptOverrideConfigurationTypeDef(
    _RequiredPromptOverrideConfigurationTypeDef, _OptionalPromptOverrideConfigurationTypeDef
):
    pass

RdsConfigurationTypeDef = TypedDict(
    "RdsConfigurationTypeDef",
    {
        "credentialsSecretArn": str,
        "databaseName": str,
        "fieldMapping": "RdsFieldMappingTypeDef",
        "resourceArn": str,
        "tableName": str,
    },
)

RdsFieldMappingTypeDef = TypedDict(
    "RdsFieldMappingTypeDef",
    {
        "metadataField": str,
        "primaryKeyField": str,
        "textField": str,
        "vectorField": str,
    },
)

RedisEnterpriseCloudConfigurationTypeDef = TypedDict(
    "RedisEnterpriseCloudConfigurationTypeDef",
    {
        "credentialsSecretArn": str,
        "endpoint": str,
        "fieldMapping": "RedisEnterpriseCloudFieldMappingTypeDef",
        "vectorIndexName": str,
    },
)

RedisEnterpriseCloudFieldMappingTypeDef = TypedDict(
    "RedisEnterpriseCloudFieldMappingTypeDef",
    {
        "metadataField": str,
        "textField": str,
        "vectorField": str,
    },
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

_RequiredS3DataSourceConfigurationTypeDef = TypedDict(
    "_RequiredS3DataSourceConfigurationTypeDef",
    {
        "bucketArn": str,
    },
)
_OptionalS3DataSourceConfigurationTypeDef = TypedDict(
    "_OptionalS3DataSourceConfigurationTypeDef",
    {
        "bucketOwnerAccountId": str,
        "inclusionPrefixes": List[str],
    },
    total=False,
)

class S3DataSourceConfigurationTypeDef(
    _RequiredS3DataSourceConfigurationTypeDef, _OptionalS3DataSourceConfigurationTypeDef
):
    pass

S3IdentifierTypeDef = TypedDict(
    "S3IdentifierTypeDef",
    {
        "s3BucketName": str,
        "s3ObjectKey": str,
    },
    total=False,
)

ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "kmsKeyArn": str,
    },
    total=False,
)

_RequiredStartIngestionJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartIngestionJobRequestRequestTypeDef",
    {
        "dataSourceId": str,
        "knowledgeBaseId": str,
    },
)
_OptionalStartIngestionJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartIngestionJobRequestRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
    },
    total=False,
)

class StartIngestionJobRequestRequestTypeDef(
    _RequiredStartIngestionJobRequestRequestTypeDef, _OptionalStartIngestionJobRequestRequestTypeDef
):
    pass

StartIngestionJobResponseTypeDef = TypedDict(
    "StartIngestionJobResponseTypeDef",
    {
        "ingestionJob": "IngestionJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStorageConfigurationTypeDef = TypedDict(
    "_RequiredStorageConfigurationTypeDef",
    {
        "type": KnowledgeBaseStorageTypeType,
    },
)
_OptionalStorageConfigurationTypeDef = TypedDict(
    "_OptionalStorageConfigurationTypeDef",
    {
        "mongoDbAtlasConfiguration": "MongoDbAtlasConfigurationTypeDef",
        "opensearchServerlessConfiguration": "OpenSearchServerlessConfigurationTypeDef",
        "pineconeConfiguration": "PineconeConfigurationTypeDef",
        "rdsConfiguration": "RdsConfigurationTypeDef",
        "redisEnterpriseCloudConfiguration": "RedisEnterpriseCloudConfigurationTypeDef",
    },
    total=False,
)

class StorageConfigurationTypeDef(
    _RequiredStorageConfigurationTypeDef, _OptionalStorageConfigurationTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAgentActionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAgentActionGroupRequestRequestTypeDef",
    {
        "actionGroupId": str,
        "actionGroupName": str,
        "agentId": str,
        "agentVersion": str,
    },
)
_OptionalUpdateAgentActionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAgentActionGroupRequestRequestTypeDef",
    {
        "actionGroupExecutor": "ActionGroupExecutorTypeDef",
        "actionGroupState": ActionGroupStateType,
        "apiSchema": "APISchemaTypeDef",
        "description": str,
        "functionSchema": "FunctionSchemaTypeDef",
        "parentActionGroupSignature": Literal["AMAZON.UserInput"],
    },
    total=False,
)

class UpdateAgentActionGroupRequestRequestTypeDef(
    _RequiredUpdateAgentActionGroupRequestRequestTypeDef,
    _OptionalUpdateAgentActionGroupRequestRequestTypeDef,
):
    pass

UpdateAgentActionGroupResponseTypeDef = TypedDict(
    "UpdateAgentActionGroupResponseTypeDef",
    {
        "agentActionGroup": "AgentActionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAgentAliasRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAgentAliasRequestRequestTypeDef",
    {
        "agentAliasId": str,
        "agentAliasName": str,
        "agentId": str,
    },
)
_OptionalUpdateAgentAliasRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAgentAliasRequestRequestTypeDef",
    {
        "description": str,
        "routingConfiguration": List["AgentAliasRoutingConfigurationListItemTypeDef"],
    },
    total=False,
)

class UpdateAgentAliasRequestRequestTypeDef(
    _RequiredUpdateAgentAliasRequestRequestTypeDef, _OptionalUpdateAgentAliasRequestRequestTypeDef
):
    pass

UpdateAgentAliasResponseTypeDef = TypedDict(
    "UpdateAgentAliasResponseTypeDef",
    {
        "agentAlias": "AgentAliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAgentKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAgentKnowledgeBaseRequestRequestTypeDef",
    {
        "agentId": str,
        "agentVersion": str,
        "knowledgeBaseId": str,
    },
)
_OptionalUpdateAgentKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAgentKnowledgeBaseRequestRequestTypeDef",
    {
        "description": str,
        "knowledgeBaseState": KnowledgeBaseStateType,
    },
    total=False,
)

class UpdateAgentKnowledgeBaseRequestRequestTypeDef(
    _RequiredUpdateAgentKnowledgeBaseRequestRequestTypeDef,
    _OptionalUpdateAgentKnowledgeBaseRequestRequestTypeDef,
):
    pass

UpdateAgentKnowledgeBaseResponseTypeDef = TypedDict(
    "UpdateAgentKnowledgeBaseResponseTypeDef",
    {
        "agentKnowledgeBase": "AgentKnowledgeBaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAgentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAgentRequestRequestTypeDef",
    {
        "agentId": str,
        "agentName": str,
        "agentResourceRoleArn": str,
        "foundationModel": str,
    },
)
_OptionalUpdateAgentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAgentRequestRequestTypeDef",
    {
        "customerEncryptionKeyArn": str,
        "description": str,
        "guardrailConfiguration": "GuardrailConfigurationTypeDef",
        "idleSessionTTLInSeconds": int,
        "instruction": str,
        "promptOverrideConfiguration": "PromptOverrideConfigurationTypeDef",
    },
    total=False,
)

class UpdateAgentRequestRequestTypeDef(
    _RequiredUpdateAgentRequestRequestTypeDef, _OptionalUpdateAgentRequestRequestTypeDef
):
    pass

UpdateAgentResponseTypeDef = TypedDict(
    "UpdateAgentResponseTypeDef",
    {
        "agent": "AgentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataSourceRequestRequestTypeDef",
    {
        "dataSourceConfiguration": "DataSourceConfigurationTypeDef",
        "dataSourceId": str,
        "knowledgeBaseId": str,
        "name": str,
    },
)
_OptionalUpdateDataSourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataSourceRequestRequestTypeDef",
    {
        "dataDeletionPolicy": DataDeletionPolicyType,
        "description": str,
        "serverSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "vectorIngestionConfiguration": "VectorIngestionConfigurationTypeDef",
    },
    total=False,
)

class UpdateDataSourceRequestRequestTypeDef(
    _RequiredUpdateDataSourceRequestRequestTypeDef, _OptionalUpdateDataSourceRequestRequestTypeDef
):
    pass

UpdateDataSourceResponseTypeDef = TypedDict(
    "UpdateDataSourceResponseTypeDef",
    {
        "dataSource": "DataSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseConfiguration": "KnowledgeBaseConfigurationTypeDef",
        "knowledgeBaseId": str,
        "name": str,
        "roleArn": str,
        "storageConfiguration": "StorageConfigurationTypeDef",
    },
)
_OptionalUpdateKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateKnowledgeBaseRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateKnowledgeBaseRequestRequestTypeDef(
    _RequiredUpdateKnowledgeBaseRequestRequestTypeDef,
    _OptionalUpdateKnowledgeBaseRequestRequestTypeDef,
):
    pass

UpdateKnowledgeBaseResponseTypeDef = TypedDict(
    "UpdateKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBase": "KnowledgeBaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VectorIngestionConfigurationTypeDef = TypedDict(
    "VectorIngestionConfigurationTypeDef",
    {
        "chunkingConfiguration": "ChunkingConfigurationTypeDef",
    },
    total=False,
)

_RequiredVectorKnowledgeBaseConfigurationTypeDef = TypedDict(
    "_RequiredVectorKnowledgeBaseConfigurationTypeDef",
    {
        "embeddingModelArn": str,
    },
)
_OptionalVectorKnowledgeBaseConfigurationTypeDef = TypedDict(
    "_OptionalVectorKnowledgeBaseConfigurationTypeDef",
    {
        "embeddingModelConfiguration": "EmbeddingModelConfigurationTypeDef",
    },
    total=False,
)

class VectorKnowledgeBaseConfigurationTypeDef(
    _RequiredVectorKnowledgeBaseConfigurationTypeDef,
    _OptionalVectorKnowledgeBaseConfigurationTypeDef,
):
    pass
