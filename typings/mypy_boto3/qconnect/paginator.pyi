"""
Type annotations for qconnect service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_qconnect.client import QConnectClient
    from mypy_boto3_qconnect.paginator import (
        ListAIAgentVersionsPaginator,
        ListAIAgentsPaginator,
        ListAIGuardrailVersionsPaginator,
        ListAIGuardrailsPaginator,
        ListAIPromptVersionsPaginator,
        ListAIPromptsPaginator,
        ListAssistantAssociationsPaginator,
        ListAssistantsPaginator,
        ListContentAssociationsPaginator,
        ListContentsPaginator,
        ListImportJobsPaginator,
        ListKnowledgeBasesPaginator,
        ListMessageTemplateVersionsPaginator,
        ListMessageTemplatesPaginator,
        ListMessagesPaginator,
        ListQuickResponsesPaginator,
        QueryAssistantPaginator,
        SearchContentPaginator,
        SearchMessageTemplatesPaginator,
        SearchQuickResponsesPaginator,
        SearchSessionsPaginator,
    )

    session = Session()
    client: QConnectClient = session.client("qconnect")

    list_ai_agent_versions_paginator: ListAIAgentVersionsPaginator = client.get_paginator("list_ai_agent_versions")
    list_ai_agents_paginator: ListAIAgentsPaginator = client.get_paginator("list_ai_agents")
    list_ai_guardrail_versions_paginator: ListAIGuardrailVersionsPaginator = client.get_paginator("list_ai_guardrail_versions")
    list_ai_guardrails_paginator: ListAIGuardrailsPaginator = client.get_paginator("list_ai_guardrails")
    list_ai_prompt_versions_paginator: ListAIPromptVersionsPaginator = client.get_paginator("list_ai_prompt_versions")
    list_ai_prompts_paginator: ListAIPromptsPaginator = client.get_paginator("list_ai_prompts")
    list_assistant_associations_paginator: ListAssistantAssociationsPaginator = client.get_paginator("list_assistant_associations")
    list_assistants_paginator: ListAssistantsPaginator = client.get_paginator("list_assistants")
    list_content_associations_paginator: ListContentAssociationsPaginator = client.get_paginator("list_content_associations")
    list_contents_paginator: ListContentsPaginator = client.get_paginator("list_contents")
    list_import_jobs_paginator: ListImportJobsPaginator = client.get_paginator("list_import_jobs")
    list_knowledge_bases_paginator: ListKnowledgeBasesPaginator = client.get_paginator("list_knowledge_bases")
    list_message_template_versions_paginator: ListMessageTemplateVersionsPaginator = client.get_paginator("list_message_template_versions")
    list_message_templates_paginator: ListMessageTemplatesPaginator = client.get_paginator("list_message_templates")
    list_messages_paginator: ListMessagesPaginator = client.get_paginator("list_messages")
    list_quick_responses_paginator: ListQuickResponsesPaginator = client.get_paginator("list_quick_responses")
    query_assistant_paginator: QueryAssistantPaginator = client.get_paginator("query_assistant")
    search_content_paginator: SearchContentPaginator = client.get_paginator("search_content")
    search_message_templates_paginator: SearchMessageTemplatesPaginator = client.get_paginator("search_message_templates")
    search_quick_responses_paginator: SearchQuickResponsesPaginator = client.get_paginator("search_quick_responses")
    search_sessions_paginator: SearchSessionsPaginator = client.get_paginator("search_sessions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAIAgentsRequestPaginateTypeDef,
    ListAIAgentsResponseTypeDef,
    ListAIAgentVersionsRequestPaginateTypeDef,
    ListAIAgentVersionsResponseTypeDef,
    ListAIGuardrailsRequestPaginateTypeDef,
    ListAIGuardrailsResponseTypeDef,
    ListAIGuardrailVersionsRequestPaginateTypeDef,
    ListAIGuardrailVersionsResponseTypeDef,
    ListAIPromptsRequestPaginateTypeDef,
    ListAIPromptsResponseTypeDef,
    ListAIPromptVersionsRequestPaginateTypeDef,
    ListAIPromptVersionsResponseTypeDef,
    ListAssistantAssociationsRequestPaginateTypeDef,
    ListAssistantAssociationsResponseTypeDef,
    ListAssistantsRequestPaginateTypeDef,
    ListAssistantsResponseTypeDef,
    ListContentAssociationsRequestPaginateTypeDef,
    ListContentAssociationsResponseTypeDef,
    ListContentsRequestPaginateTypeDef,
    ListContentsResponseTypeDef,
    ListImportJobsRequestPaginateTypeDef,
    ListImportJobsResponseTypeDef,
    ListKnowledgeBasesRequestPaginateTypeDef,
    ListKnowledgeBasesResponseTypeDef,
    ListMessagesRequestPaginateTypeDef,
    ListMessagesResponseTypeDef,
    ListMessageTemplatesRequestPaginateTypeDef,
    ListMessageTemplatesResponseTypeDef,
    ListMessageTemplateVersionsRequestPaginateTypeDef,
    ListMessageTemplateVersionsResponseTypeDef,
    ListQuickResponsesRequestPaginateTypeDef,
    ListQuickResponsesResponseTypeDef,
    QueryAssistantRequestPaginateTypeDef,
    QueryAssistantResponsePaginatorTypeDef,
    SearchContentRequestPaginateTypeDef,
    SearchContentResponseTypeDef,
    SearchMessageTemplatesRequestPaginateTypeDef,
    SearchMessageTemplatesResponseTypeDef,
    SearchQuickResponsesRequestPaginateTypeDef,
    SearchQuickResponsesResponseTypeDef,
    SearchSessionsRequestPaginateTypeDef,
    SearchSessionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAIAgentVersionsPaginator",
    "ListAIAgentsPaginator",
    "ListAIGuardrailVersionsPaginator",
    "ListAIGuardrailsPaginator",
    "ListAIPromptVersionsPaginator",
    "ListAIPromptsPaginator",
    "ListAssistantAssociationsPaginator",
    "ListAssistantsPaginator",
    "ListContentAssociationsPaginator",
    "ListContentsPaginator",
    "ListImportJobsPaginator",
    "ListKnowledgeBasesPaginator",
    "ListMessageTemplateVersionsPaginator",
    "ListMessageTemplatesPaginator",
    "ListMessagesPaginator",
    "ListQuickResponsesPaginator",
    "QueryAssistantPaginator",
    "SearchContentPaginator",
    "SearchMessageTemplatesPaginator",
    "SearchQuickResponsesPaginator",
    "SearchSessionsPaginator",
)

if TYPE_CHECKING:
    _ListAIAgentVersionsPaginatorBase = Paginator[ListAIAgentVersionsResponseTypeDef]
else:
    _ListAIAgentVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAIAgentVersionsPaginator(_ListAIAgentVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAIAgentVersions.html#QConnect.Paginator.ListAIAgentVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaiagentversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAIAgentVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListAIAgentVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAIAgentVersions.html#QConnect.Paginator.ListAIAgentVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaiagentversionspaginator)
        """

if TYPE_CHECKING:
    _ListAIAgentsPaginatorBase = Paginator[ListAIAgentsResponseTypeDef]
else:
    _ListAIAgentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAIAgentsPaginator(_ListAIAgentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAIAgents.html#QConnect.Paginator.ListAIAgents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaiagentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAIAgentsRequestPaginateTypeDef]
    ) -> PageIterator[ListAIAgentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAIAgents.html#QConnect.Paginator.ListAIAgents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaiagentspaginator)
        """

if TYPE_CHECKING:
    _ListAIGuardrailVersionsPaginatorBase = Paginator[ListAIGuardrailVersionsResponseTypeDef]
else:
    _ListAIGuardrailVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAIGuardrailVersionsPaginator(_ListAIGuardrailVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAIGuardrailVersions.html#QConnect.Paginator.ListAIGuardrailVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaiguardrailversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAIGuardrailVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListAIGuardrailVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAIGuardrailVersions.html#QConnect.Paginator.ListAIGuardrailVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaiguardrailversionspaginator)
        """

if TYPE_CHECKING:
    _ListAIGuardrailsPaginatorBase = Paginator[ListAIGuardrailsResponseTypeDef]
else:
    _ListAIGuardrailsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAIGuardrailsPaginator(_ListAIGuardrailsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAIGuardrails.html#QConnect.Paginator.ListAIGuardrails)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaiguardrailspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAIGuardrailsRequestPaginateTypeDef]
    ) -> PageIterator[ListAIGuardrailsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAIGuardrails.html#QConnect.Paginator.ListAIGuardrails.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaiguardrailspaginator)
        """

if TYPE_CHECKING:
    _ListAIPromptVersionsPaginatorBase = Paginator[ListAIPromptVersionsResponseTypeDef]
else:
    _ListAIPromptVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAIPromptVersionsPaginator(_ListAIPromptVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAIPromptVersions.html#QConnect.Paginator.ListAIPromptVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaipromptversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAIPromptVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListAIPromptVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAIPromptVersions.html#QConnect.Paginator.ListAIPromptVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaipromptversionspaginator)
        """

if TYPE_CHECKING:
    _ListAIPromptsPaginatorBase = Paginator[ListAIPromptsResponseTypeDef]
else:
    _ListAIPromptsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAIPromptsPaginator(_ListAIPromptsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAIPrompts.html#QConnect.Paginator.ListAIPrompts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaipromptspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAIPromptsRequestPaginateTypeDef]
    ) -> PageIterator[ListAIPromptsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAIPrompts.html#QConnect.Paginator.ListAIPrompts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listaipromptspaginator)
        """

if TYPE_CHECKING:
    _ListAssistantAssociationsPaginatorBase = Paginator[ListAssistantAssociationsResponseTypeDef]
else:
    _ListAssistantAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssistantAssociationsPaginator(_ListAssistantAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAssistantAssociations.html#QConnect.Paginator.ListAssistantAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listassistantassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssistantAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssistantAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAssistantAssociations.html#QConnect.Paginator.ListAssistantAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listassistantassociationspaginator)
        """

if TYPE_CHECKING:
    _ListAssistantsPaginatorBase = Paginator[ListAssistantsResponseTypeDef]
else:
    _ListAssistantsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssistantsPaginator(_ListAssistantsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAssistants.html#QConnect.Paginator.ListAssistants)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listassistantspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssistantsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssistantsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListAssistants.html#QConnect.Paginator.ListAssistants.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listassistantspaginator)
        """

if TYPE_CHECKING:
    _ListContentAssociationsPaginatorBase = Paginator[ListContentAssociationsResponseTypeDef]
else:
    _ListContentAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListContentAssociationsPaginator(_ListContentAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListContentAssociations.html#QConnect.Paginator.ListContentAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listcontentassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListContentAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListContentAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListContentAssociations.html#QConnect.Paginator.ListContentAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listcontentassociationspaginator)
        """

if TYPE_CHECKING:
    _ListContentsPaginatorBase = Paginator[ListContentsResponseTypeDef]
else:
    _ListContentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListContentsPaginator(_ListContentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListContents.html#QConnect.Paginator.ListContents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listcontentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListContentsRequestPaginateTypeDef]
    ) -> PageIterator[ListContentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListContents.html#QConnect.Paginator.ListContents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listcontentspaginator)
        """

if TYPE_CHECKING:
    _ListImportJobsPaginatorBase = Paginator[ListImportJobsResponseTypeDef]
else:
    _ListImportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListImportJobsPaginator(_ListImportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListImportJobs.html#QConnect.Paginator.ListImportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listimportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListImportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListImportJobs.html#QConnect.Paginator.ListImportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listimportjobspaginator)
        """

if TYPE_CHECKING:
    _ListKnowledgeBasesPaginatorBase = Paginator[ListKnowledgeBasesResponseTypeDef]
else:
    _ListKnowledgeBasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListKnowledgeBasesPaginator(_ListKnowledgeBasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListKnowledgeBases.html#QConnect.Paginator.ListKnowledgeBases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listknowledgebasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListKnowledgeBasesRequestPaginateTypeDef]
    ) -> PageIterator[ListKnowledgeBasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListKnowledgeBases.html#QConnect.Paginator.ListKnowledgeBases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listknowledgebasespaginator)
        """

if TYPE_CHECKING:
    _ListMessageTemplateVersionsPaginatorBase = Paginator[
        ListMessageTemplateVersionsResponseTypeDef
    ]
else:
    _ListMessageTemplateVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMessageTemplateVersionsPaginator(_ListMessageTemplateVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListMessageTemplateVersions.html#QConnect.Paginator.ListMessageTemplateVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listmessagetemplateversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMessageTemplateVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListMessageTemplateVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListMessageTemplateVersions.html#QConnect.Paginator.ListMessageTemplateVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listmessagetemplateversionspaginator)
        """

if TYPE_CHECKING:
    _ListMessageTemplatesPaginatorBase = Paginator[ListMessageTemplatesResponseTypeDef]
else:
    _ListMessageTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListMessageTemplatesPaginator(_ListMessageTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListMessageTemplates.html#QConnect.Paginator.ListMessageTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listmessagetemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMessageTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[ListMessageTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListMessageTemplates.html#QConnect.Paginator.ListMessageTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listmessagetemplatespaginator)
        """

if TYPE_CHECKING:
    _ListMessagesPaginatorBase = Paginator[ListMessagesResponseTypeDef]
else:
    _ListMessagesPaginatorBase = Paginator  # type: ignore[assignment]

class ListMessagesPaginator(_ListMessagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListMessages.html#QConnect.Paginator.ListMessages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listmessagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMessagesRequestPaginateTypeDef]
    ) -> PageIterator[ListMessagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListMessages.html#QConnect.Paginator.ListMessages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listmessagespaginator)
        """

if TYPE_CHECKING:
    _ListQuickResponsesPaginatorBase = Paginator[ListQuickResponsesResponseTypeDef]
else:
    _ListQuickResponsesPaginatorBase = Paginator  # type: ignore[assignment]

class ListQuickResponsesPaginator(_ListQuickResponsesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListQuickResponses.html#QConnect.Paginator.ListQuickResponses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listquickresponsespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQuickResponsesRequestPaginateTypeDef]
    ) -> PageIterator[ListQuickResponsesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/ListQuickResponses.html#QConnect.Paginator.ListQuickResponses.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#listquickresponsespaginator)
        """

if TYPE_CHECKING:
    _QueryAssistantPaginatorBase = Paginator[QueryAssistantResponsePaginatorTypeDef]
else:
    _QueryAssistantPaginatorBase = Paginator  # type: ignore[assignment]

class QueryAssistantPaginator(_QueryAssistantPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/QueryAssistant.html#QConnect.Paginator.QueryAssistant)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#queryassistantpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[QueryAssistantRequestPaginateTypeDef]
    ) -> PageIterator[QueryAssistantResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/QueryAssistant.html#QConnect.Paginator.QueryAssistant.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#queryassistantpaginator)
        """

if TYPE_CHECKING:
    _SearchContentPaginatorBase = Paginator[SearchContentResponseTypeDef]
else:
    _SearchContentPaginatorBase = Paginator  # type: ignore[assignment]

class SearchContentPaginator(_SearchContentPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/SearchContent.html#QConnect.Paginator.SearchContent)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#searchcontentpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchContentRequestPaginateTypeDef]
    ) -> PageIterator[SearchContentResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/SearchContent.html#QConnect.Paginator.SearchContent.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#searchcontentpaginator)
        """

if TYPE_CHECKING:
    _SearchMessageTemplatesPaginatorBase = Paginator[SearchMessageTemplatesResponseTypeDef]
else:
    _SearchMessageTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchMessageTemplatesPaginator(_SearchMessageTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/SearchMessageTemplates.html#QConnect.Paginator.SearchMessageTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#searchmessagetemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchMessageTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[SearchMessageTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/SearchMessageTemplates.html#QConnect.Paginator.SearchMessageTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#searchmessagetemplatespaginator)
        """

if TYPE_CHECKING:
    _SearchQuickResponsesPaginatorBase = Paginator[SearchQuickResponsesResponseTypeDef]
else:
    _SearchQuickResponsesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchQuickResponsesPaginator(_SearchQuickResponsesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/SearchQuickResponses.html#QConnect.Paginator.SearchQuickResponses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#searchquickresponsespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchQuickResponsesRequestPaginateTypeDef]
    ) -> PageIterator[SearchQuickResponsesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/SearchQuickResponses.html#QConnect.Paginator.SearchQuickResponses.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#searchquickresponsespaginator)
        """

if TYPE_CHECKING:
    _SearchSessionsPaginatorBase = Paginator[SearchSessionsResponseTypeDef]
else:
    _SearchSessionsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchSessionsPaginator(_SearchSessionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/SearchSessions.html#QConnect.Paginator.SearchSessions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#searchsessionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchSessionsRequestPaginateTypeDef]
    ) -> PageIterator[SearchSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qconnect/paginator/SearchSessions.html#QConnect.Paginator.SearchSessions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/paginators/#searchsessionspaginator)
        """
