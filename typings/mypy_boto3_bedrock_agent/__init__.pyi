"""
Main interface for bedrock-agent service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bedrock_agent import (
        AgentsforBedrockClient,
        Client,
        ListAgentActionGroupsPaginator,
        ListAgentAliasesPaginator,
        ListAgentCollaboratorsPaginator,
        ListAgentKnowledgeBasesPaginator,
        ListAgentVersionsPaginator,
        ListAgentsPaginator,
        ListDataSourcesPaginator,
        ListFlowAliasesPaginator,
        ListFlowVersionsPaginator,
        ListFlowsPaginator,
        ListIngestionJobsPaginator,
        ListKnowledgeBaseDocumentsPaginator,
        ListKnowledgeBasesPaginator,
        ListPromptsPaginator,
    )

    session = Session()
    client: AgentsforBedrockClient = session.client("bedrock-agent")

    list_agent_action_groups_paginator: ListAgentActionGroupsPaginator = client.get_paginator("list_agent_action_groups")
    list_agent_aliases_paginator: ListAgentAliasesPaginator = client.get_paginator("list_agent_aliases")
    list_agent_collaborators_paginator: ListAgentCollaboratorsPaginator = client.get_paginator("list_agent_collaborators")
    list_agent_knowledge_bases_paginator: ListAgentKnowledgeBasesPaginator = client.get_paginator("list_agent_knowledge_bases")
    list_agent_versions_paginator: ListAgentVersionsPaginator = client.get_paginator("list_agent_versions")
    list_agents_paginator: ListAgentsPaginator = client.get_paginator("list_agents")
    list_data_sources_paginator: ListDataSourcesPaginator = client.get_paginator("list_data_sources")
    list_flow_aliases_paginator: ListFlowAliasesPaginator = client.get_paginator("list_flow_aliases")
    list_flow_versions_paginator: ListFlowVersionsPaginator = client.get_paginator("list_flow_versions")
    list_flows_paginator: ListFlowsPaginator = client.get_paginator("list_flows")
    list_ingestion_jobs_paginator: ListIngestionJobsPaginator = client.get_paginator("list_ingestion_jobs")
    list_knowledge_base_documents_paginator: ListKnowledgeBaseDocumentsPaginator = client.get_paginator("list_knowledge_base_documents")
    list_knowledge_bases_paginator: ListKnowledgeBasesPaginator = client.get_paginator("list_knowledge_bases")
    list_prompts_paginator: ListPromptsPaginator = client.get_paginator("list_prompts")
    ```
"""

from .client import AgentsforBedrockClient
from .paginator import (
    ListAgentActionGroupsPaginator,
    ListAgentAliasesPaginator,
    ListAgentCollaboratorsPaginator,
    ListAgentKnowledgeBasesPaginator,
    ListAgentsPaginator,
    ListAgentVersionsPaginator,
    ListDataSourcesPaginator,
    ListFlowAliasesPaginator,
    ListFlowsPaginator,
    ListFlowVersionsPaginator,
    ListIngestionJobsPaginator,
    ListKnowledgeBaseDocumentsPaginator,
    ListKnowledgeBasesPaginator,
    ListPromptsPaginator,
)

Client = AgentsforBedrockClient

__all__ = (
    "AgentsforBedrockClient",
    "Client",
    "ListAgentActionGroupsPaginator",
    "ListAgentAliasesPaginator",
    "ListAgentCollaboratorsPaginator",
    "ListAgentKnowledgeBasesPaginator",
    "ListAgentVersionsPaginator",
    "ListAgentsPaginator",
    "ListDataSourcesPaginator",
    "ListFlowAliasesPaginator",
    "ListFlowVersionsPaginator",
    "ListFlowsPaginator",
    "ListIngestionJobsPaginator",
    "ListKnowledgeBaseDocumentsPaginator",
    "ListKnowledgeBasesPaginator",
    "ListPromptsPaginator",
)
