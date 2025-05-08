"""
Type annotations for bedrock-agent service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_bedrock_agent.client import AgentsforBedrockClient
    from mypy_boto3_bedrock_agent.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAgentActionGroupsRequestPaginateTypeDef,
    ListAgentActionGroupsResponseTypeDef,
    ListAgentAliasesRequestPaginateTypeDef,
    ListAgentAliasesResponseTypeDef,
    ListAgentCollaboratorsRequestPaginateTypeDef,
    ListAgentCollaboratorsResponseTypeDef,
    ListAgentKnowledgeBasesRequestPaginateTypeDef,
    ListAgentKnowledgeBasesResponseTypeDef,
    ListAgentsRequestPaginateTypeDef,
    ListAgentsResponseTypeDef,
    ListAgentVersionsRequestPaginateTypeDef,
    ListAgentVersionsResponseTypeDef,
    ListDataSourcesRequestPaginateTypeDef,
    ListDataSourcesResponseTypeDef,
    ListFlowAliasesRequestPaginateTypeDef,
    ListFlowAliasesResponseTypeDef,
    ListFlowsRequestPaginateTypeDef,
    ListFlowsResponseTypeDef,
    ListFlowVersionsRequestPaginateTypeDef,
    ListFlowVersionsResponseTypeDef,
    ListIngestionJobsRequestPaginateTypeDef,
    ListIngestionJobsResponseTypeDef,
    ListKnowledgeBaseDocumentsRequestPaginateTypeDef,
    ListKnowledgeBaseDocumentsResponseTypeDef,
    ListKnowledgeBasesRequestPaginateTypeDef,
    ListKnowledgeBasesResponseTypeDef,
    ListPromptsRequestPaginateTypeDef,
    ListPromptsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
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

if TYPE_CHECKING:
    _ListAgentActionGroupsPaginatorBase = Paginator[ListAgentActionGroupsResponseTypeDef]
else:
    _ListAgentActionGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAgentActionGroupsPaginator(_ListAgentActionGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListAgentActionGroups.html#AgentsforBedrock.Paginator.ListAgentActionGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentactiongroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAgentActionGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListAgentActionGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListAgentActionGroups.html#AgentsforBedrock.Paginator.ListAgentActionGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentactiongroupspaginator)
        """

if TYPE_CHECKING:
    _ListAgentAliasesPaginatorBase = Paginator[ListAgentAliasesResponseTypeDef]
else:
    _ListAgentAliasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAgentAliasesPaginator(_ListAgentAliasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListAgentAliases.html#AgentsforBedrock.Paginator.ListAgentAliases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentaliasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAgentAliasesRequestPaginateTypeDef]
    ) -> PageIterator[ListAgentAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListAgentAliases.html#AgentsforBedrock.Paginator.ListAgentAliases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentaliasespaginator)
        """

if TYPE_CHECKING:
    _ListAgentCollaboratorsPaginatorBase = Paginator[ListAgentCollaboratorsResponseTypeDef]
else:
    _ListAgentCollaboratorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAgentCollaboratorsPaginator(_ListAgentCollaboratorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListAgentCollaborators.html#AgentsforBedrock.Paginator.ListAgentCollaborators)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentcollaboratorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAgentCollaboratorsRequestPaginateTypeDef]
    ) -> PageIterator[ListAgentCollaboratorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListAgentCollaborators.html#AgentsforBedrock.Paginator.ListAgentCollaborators.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentcollaboratorspaginator)
        """

if TYPE_CHECKING:
    _ListAgentKnowledgeBasesPaginatorBase = Paginator[ListAgentKnowledgeBasesResponseTypeDef]
else:
    _ListAgentKnowledgeBasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAgentKnowledgeBasesPaginator(_ListAgentKnowledgeBasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListAgentKnowledgeBases.html#AgentsforBedrock.Paginator.ListAgentKnowledgeBases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentknowledgebasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAgentKnowledgeBasesRequestPaginateTypeDef]
    ) -> PageIterator[ListAgentKnowledgeBasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListAgentKnowledgeBases.html#AgentsforBedrock.Paginator.ListAgentKnowledgeBases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentknowledgebasespaginator)
        """

if TYPE_CHECKING:
    _ListAgentVersionsPaginatorBase = Paginator[ListAgentVersionsResponseTypeDef]
else:
    _ListAgentVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAgentVersionsPaginator(_ListAgentVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListAgentVersions.html#AgentsforBedrock.Paginator.ListAgentVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAgentVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListAgentVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListAgentVersions.html#AgentsforBedrock.Paginator.ListAgentVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentversionspaginator)
        """

if TYPE_CHECKING:
    _ListAgentsPaginatorBase = Paginator[ListAgentsResponseTypeDef]
else:
    _ListAgentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAgentsPaginator(_ListAgentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListAgents.html#AgentsforBedrock.Paginator.ListAgents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAgentsRequestPaginateTypeDef]
    ) -> PageIterator[ListAgentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListAgents.html#AgentsforBedrock.Paginator.ListAgents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listagentspaginator)
        """

if TYPE_CHECKING:
    _ListDataSourcesPaginatorBase = Paginator[ListDataSourcesResponseTypeDef]
else:
    _ListDataSourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataSourcesPaginator(_ListDataSourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListDataSources.html#AgentsforBedrock.Paginator.ListDataSources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listdatasourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataSourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListDataSourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListDataSources.html#AgentsforBedrock.Paginator.ListDataSources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listdatasourcespaginator)
        """

if TYPE_CHECKING:
    _ListFlowAliasesPaginatorBase = Paginator[ListFlowAliasesResponseTypeDef]
else:
    _ListFlowAliasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListFlowAliasesPaginator(_ListFlowAliasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListFlowAliases.html#AgentsforBedrock.Paginator.ListFlowAliases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listflowaliasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFlowAliasesRequestPaginateTypeDef]
    ) -> PageIterator[ListFlowAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListFlowAliases.html#AgentsforBedrock.Paginator.ListFlowAliases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listflowaliasespaginator)
        """

if TYPE_CHECKING:
    _ListFlowVersionsPaginatorBase = Paginator[ListFlowVersionsResponseTypeDef]
else:
    _ListFlowVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFlowVersionsPaginator(_ListFlowVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListFlowVersions.html#AgentsforBedrock.Paginator.ListFlowVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listflowversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFlowVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListFlowVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListFlowVersions.html#AgentsforBedrock.Paginator.ListFlowVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listflowversionspaginator)
        """

if TYPE_CHECKING:
    _ListFlowsPaginatorBase = Paginator[ListFlowsResponseTypeDef]
else:
    _ListFlowsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFlowsPaginator(_ListFlowsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListFlows.html#AgentsforBedrock.Paginator.ListFlows)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listflowspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFlowsRequestPaginateTypeDef]
    ) -> PageIterator[ListFlowsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListFlows.html#AgentsforBedrock.Paginator.ListFlows.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listflowspaginator)
        """

if TYPE_CHECKING:
    _ListIngestionJobsPaginatorBase = Paginator[ListIngestionJobsResponseTypeDef]
else:
    _ListIngestionJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListIngestionJobsPaginator(_ListIngestionJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListIngestionJobs.html#AgentsforBedrock.Paginator.ListIngestionJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listingestionjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIngestionJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListIngestionJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListIngestionJobs.html#AgentsforBedrock.Paginator.ListIngestionJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listingestionjobspaginator)
        """

if TYPE_CHECKING:
    _ListKnowledgeBaseDocumentsPaginatorBase = Paginator[ListKnowledgeBaseDocumentsResponseTypeDef]
else:
    _ListKnowledgeBaseDocumentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListKnowledgeBaseDocumentsPaginator(_ListKnowledgeBaseDocumentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListKnowledgeBaseDocuments.html#AgentsforBedrock.Paginator.ListKnowledgeBaseDocuments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listknowledgebasedocumentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListKnowledgeBaseDocumentsRequestPaginateTypeDef]
    ) -> PageIterator[ListKnowledgeBaseDocumentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListKnowledgeBaseDocuments.html#AgentsforBedrock.Paginator.ListKnowledgeBaseDocuments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listknowledgebasedocumentspaginator)
        """

if TYPE_CHECKING:
    _ListKnowledgeBasesPaginatorBase = Paginator[ListKnowledgeBasesResponseTypeDef]
else:
    _ListKnowledgeBasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListKnowledgeBasesPaginator(_ListKnowledgeBasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListKnowledgeBases.html#AgentsforBedrock.Paginator.ListKnowledgeBases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listknowledgebasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListKnowledgeBasesRequestPaginateTypeDef]
    ) -> PageIterator[ListKnowledgeBasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListKnowledgeBases.html#AgentsforBedrock.Paginator.ListKnowledgeBases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listknowledgebasespaginator)
        """

if TYPE_CHECKING:
    _ListPromptsPaginatorBase = Paginator[ListPromptsResponseTypeDef]
else:
    _ListPromptsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPromptsPaginator(_ListPromptsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListPrompts.html#AgentsforBedrock.Paginator.ListPrompts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listpromptspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPromptsRequestPaginateTypeDef]
    ) -> PageIterator[ListPromptsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent/paginator/ListPrompts.html#AgentsforBedrock.Paginator.ListPrompts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent/paginators/#listpromptspaginator)
        """
