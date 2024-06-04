"""
Main interface for bedrock-agent service.

Usage::

    ```python
    import boto3
    from mypy_boto3_bedrock_agent import (
        AgentsforBedrockClient,
        Client,
        ListAgentActionGroupsPaginator,
        ListAgentAliasesPaginator,
        ListAgentKnowledgeBasesPaginator,
        ListAgentVersionsPaginator,
        ListAgentsPaginator,
        ListDataSourcesPaginator,
        ListIngestionJobsPaginator,
        ListKnowledgeBasesPaginator,
    )

    session = boto3.Session()

    client: AgentsforBedrockClient = boto3.client("bedrock-agent")
    session_client: AgentsforBedrockClient = session.client("bedrock-agent")

    list_agent_action_groups_paginator: ListAgentActionGroupsPaginator = client.get_paginator("list_agent_action_groups")
    list_agent_aliases_paginator: ListAgentAliasesPaginator = client.get_paginator("list_agent_aliases")
    list_agent_knowledge_bases_paginator: ListAgentKnowledgeBasesPaginator = client.get_paginator("list_agent_knowledge_bases")
    list_agent_versions_paginator: ListAgentVersionsPaginator = client.get_paginator("list_agent_versions")
    list_agents_paginator: ListAgentsPaginator = client.get_paginator("list_agents")
    list_data_sources_paginator: ListDataSourcesPaginator = client.get_paginator("list_data_sources")
    list_ingestion_jobs_paginator: ListIngestionJobsPaginator = client.get_paginator("list_ingestion_jobs")
    list_knowledge_bases_paginator: ListKnowledgeBasesPaginator = client.get_paginator("list_knowledge_bases")
    ```
"""

from .client import AgentsforBedrockClient
from .paginator import (
    ListAgentActionGroupsPaginator,
    ListAgentAliasesPaginator,
    ListAgentKnowledgeBasesPaginator,
    ListAgentsPaginator,
    ListAgentVersionsPaginator,
    ListDataSourcesPaginator,
    ListIngestionJobsPaginator,
    ListKnowledgeBasesPaginator,
)

Client = AgentsforBedrockClient

__all__ = (
    "AgentsforBedrockClient",
    "Client",
    "ListAgentActionGroupsPaginator",
    "ListAgentAliasesPaginator",
    "ListAgentKnowledgeBasesPaginator",
    "ListAgentVersionsPaginator",
    "ListAgentsPaginator",
    "ListDataSourcesPaginator",
    "ListIngestionJobsPaginator",
    "ListKnowledgeBasesPaginator",
)
