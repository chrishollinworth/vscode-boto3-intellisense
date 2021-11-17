"""
Main interface for wisdom service.

Usage::

    ```python
    import boto3
    from mypy_boto3_wisdom import (
        Client,
        ConnectWisdomServiceClient,
        ListAssistantAssociationsPaginator,
        ListAssistantsPaginator,
        ListContentsPaginator,
        ListKnowledgeBasesPaginator,
        QueryAssistantPaginator,
        SearchContentPaginator,
        SearchSessionsPaginator,
    )

    session = boto3.Session()

    client: ConnectWisdomServiceClient = boto3.client("wisdom")
    session_client: ConnectWisdomServiceClient = session.client("wisdom")

    list_assistant_associations_paginator: ListAssistantAssociationsPaginator = client.get_paginator("list_assistant_associations")
    list_assistants_paginator: ListAssistantsPaginator = client.get_paginator("list_assistants")
    list_contents_paginator: ListContentsPaginator = client.get_paginator("list_contents")
    list_knowledge_bases_paginator: ListKnowledgeBasesPaginator = client.get_paginator("list_knowledge_bases")
    query_assistant_paginator: QueryAssistantPaginator = client.get_paginator("query_assistant")
    search_content_paginator: SearchContentPaginator = client.get_paginator("search_content")
    search_sessions_paginator: SearchSessionsPaginator = client.get_paginator("search_sessions")
    ```
"""
from .client import ConnectWisdomServiceClient
from .paginator import (
    ListAssistantAssociationsPaginator,
    ListAssistantsPaginator,
    ListContentsPaginator,
    ListKnowledgeBasesPaginator,
    QueryAssistantPaginator,
    SearchContentPaginator,
    SearchSessionsPaginator,
)

Client = ConnectWisdomServiceClient

__all__ = (
    "Client",
    "ConnectWisdomServiceClient",
    "ListAssistantAssociationsPaginator",
    "ListAssistantsPaginator",
    "ListContentsPaginator",
    "ListKnowledgeBasesPaginator",
    "QueryAssistantPaginator",
    "SearchContentPaginator",
    "SearchSessionsPaginator",
)
