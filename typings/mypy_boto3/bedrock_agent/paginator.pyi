"""
Type annotations for bedrock-agent service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_bedrock_agent import AgentsforBedrockClient
    from mypy_boto3_bedrock_agent.paginator import (
        ListAgentActionGroupsPaginator,
        ListAgentAliasesPaginator,
        ListAgentKnowledgeBasesPaginator,
        ListAgentVersionsPaginator,
        ListAgentsPaginator,
        ListDataSourcesPaginator,
        ListIngestionJobsPaginator,
        ListKnowledgeBasesPaginator,
    )

    client: AgentsforBedrockClient = boto3.client("bedrock-agent")

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

from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    IngestionJobFilterTypeDef,
    IngestionJobSortByTypeDef,
    ListAgentActionGroupsResponseTypeDef,
    ListAgentAliasesResponseTypeDef,
    ListAgentKnowledgeBasesResponseTypeDef,
    ListAgentsResponseTypeDef,
    ListAgentVersionsResponseTypeDef,
    ListDataSourcesResponseTypeDef,
    ListIngestionJobsResponseTypeDef,
    ListKnowledgeBasesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAgentActionGroupsPaginator",
    "ListAgentAliasesPaginator",
    "ListAgentKnowledgeBasesPaginator",
    "ListAgentVersionsPaginator",
    "ListAgentsPaginator",
    "ListDataSourcesPaginator",
    "ListIngestionJobsPaginator",
    "ListKnowledgeBasesPaginator",
)

class ListAgentActionGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentActionGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listagentactiongroupspaginator)
    """

    def paginate(
        self, *, agentId: str, agentVersion: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAgentActionGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentActionGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listagentactiongroupspaginator)
        """

class ListAgentAliasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentAliases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listagentaliasespaginator)
    """

    def paginate(
        self, *, agentId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAgentAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentAliases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listagentaliasespaginator)
        """

class ListAgentKnowledgeBasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentKnowledgeBases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listagentknowledgebasespaginator)
    """

    def paginate(
        self, *, agentId: str, agentVersion: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAgentKnowledgeBasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentKnowledgeBases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listagentknowledgebasespaginator)
        """

class ListAgentVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listagentversionspaginator)
    """

    def paginate(
        self, *, agentId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAgentVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgentVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listagentversionspaginator)
        """

class ListAgentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listagentspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAgentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListAgents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listagentspaginator)
        """

class ListDataSourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListDataSources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listdatasourcespaginator)
    """

    def paginate(
        self, *, knowledgeBaseId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListDataSources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listdatasourcespaginator)
        """

class ListIngestionJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListIngestionJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listingestionjobspaginator)
    """

    def paginate(
        self,
        *,
        dataSourceId: str,
        knowledgeBaseId: str,
        filters: List["IngestionJobFilterTypeDef"] = None,
        sortBy: "IngestionJobSortByTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIngestionJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListIngestionJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listingestionjobspaginator)
        """

class ListKnowledgeBasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListKnowledgeBases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listknowledgebasespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKnowledgeBasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent.html#AgentsforBedrock.Paginator.ListKnowledgeBases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators.html#listknowledgebasespaginator)
        """
