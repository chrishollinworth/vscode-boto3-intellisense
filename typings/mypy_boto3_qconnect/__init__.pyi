"""
Main interface for qconnect service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qconnect/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_qconnect import (
        Client,
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
        QConnectClient,
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

from .client import QConnectClient
from .paginator import (
    ListAIAgentsPaginator,
    ListAIAgentVersionsPaginator,
    ListAIGuardrailsPaginator,
    ListAIGuardrailVersionsPaginator,
    ListAIPromptsPaginator,
    ListAIPromptVersionsPaginator,
    ListAssistantAssociationsPaginator,
    ListAssistantsPaginator,
    ListContentAssociationsPaginator,
    ListContentsPaginator,
    ListImportJobsPaginator,
    ListKnowledgeBasesPaginator,
    ListMessagesPaginator,
    ListMessageTemplatesPaginator,
    ListMessageTemplateVersionsPaginator,
    ListQuickResponsesPaginator,
    QueryAssistantPaginator,
    SearchContentPaginator,
    SearchMessageTemplatesPaginator,
    SearchQuickResponsesPaginator,
    SearchSessionsPaginator,
)

Client = QConnectClient

__all__ = (
    "Client",
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
    "QConnectClient",
    "QueryAssistantPaginator",
    "SearchContentPaginator",
    "SearchMessageTemplatesPaginator",
    "SearchQuickResponsesPaginator",
    "SearchSessionsPaginator",
)
