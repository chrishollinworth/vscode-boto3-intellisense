"""
Type annotations for wisdom service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_wisdom import ConnectWisdomServiceClient
    from mypy_boto3_wisdom.paginator import (
        ListAssistantAssociationsPaginator,
        ListAssistantsPaginator,
        ListContentsPaginator,
        ListImportJobsPaginator,
        ListKnowledgeBasesPaginator,
        ListQuickResponsesPaginator,
        QueryAssistantPaginator,
        SearchContentPaginator,
        SearchQuickResponsesPaginator,
        SearchSessionsPaginator,
    )

    client: ConnectWisdomServiceClient = boto3.client("wisdom")

    list_assistant_associations_paginator: ListAssistantAssociationsPaginator = client.get_paginator("list_assistant_associations")
    list_assistants_paginator: ListAssistantsPaginator = client.get_paginator("list_assistants")
    list_contents_paginator: ListContentsPaginator = client.get_paginator("list_contents")
    list_import_jobs_paginator: ListImportJobsPaginator = client.get_paginator("list_import_jobs")
    list_knowledge_bases_paginator: ListKnowledgeBasesPaginator = client.get_paginator("list_knowledge_bases")
    list_quick_responses_paginator: ListQuickResponsesPaginator = client.get_paginator("list_quick_responses")
    query_assistant_paginator: QueryAssistantPaginator = client.get_paginator("query_assistant")
    search_content_paginator: SearchContentPaginator = client.get_paginator("search_content")
    search_quick_responses_paginator: SearchQuickResponsesPaginator = client.get_paginator("search_quick_responses")
    search_sessions_paginator: SearchSessionsPaginator = client.get_paginator("search_sessions")
    ```
"""
from typing import Dict, Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListAssistantAssociationsResponseTypeDef,
    ListAssistantsResponseTypeDef,
    ListContentsResponseTypeDef,
    ListImportJobsResponseTypeDef,
    ListKnowledgeBasesResponseTypeDef,
    ListQuickResponsesResponseTypeDef,
    PaginatorConfigTypeDef,
    QueryAssistantResponseTypeDef,
    QuickResponseSearchExpressionTypeDef,
    SearchContentResponseTypeDef,
    SearchExpressionTypeDef,
    SearchQuickResponsesResponseTypeDef,
    SearchSessionsResponseTypeDef,
)

__all__ = (
    "ListAssistantAssociationsPaginator",
    "ListAssistantsPaginator",
    "ListContentsPaginator",
    "ListImportJobsPaginator",
    "ListKnowledgeBasesPaginator",
    "ListQuickResponsesPaginator",
    "QueryAssistantPaginator",
    "SearchContentPaginator",
    "SearchQuickResponsesPaginator",
    "SearchSessionsPaginator",
)

class ListAssistantAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.ListAssistantAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#listassistantassociationspaginator)
    """

    def paginate(
        self, *, assistantId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssistantAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.ListAssistantAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#listassistantassociationspaginator)
        """

class ListAssistantsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.ListAssistants)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#listassistantspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssistantsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.ListAssistants.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#listassistantspaginator)
        """

class ListContentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.ListContents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#listcontentspaginator)
    """

    def paginate(
        self, *, knowledgeBaseId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListContentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.ListContents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#listcontentspaginator)
        """

class ListImportJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.ListImportJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#listimportjobspaginator)
    """

    def paginate(
        self, *, knowledgeBaseId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.ListImportJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#listimportjobspaginator)
        """

class ListKnowledgeBasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.ListKnowledgeBases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#listknowledgebasespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKnowledgeBasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.ListKnowledgeBases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#listknowledgebasespaginator)
        """

class ListQuickResponsesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.ListQuickResponses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#listquickresponsespaginator)
    """

    def paginate(
        self, *, knowledgeBaseId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListQuickResponsesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.ListQuickResponses.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#listquickresponsespaginator)
        """

class QueryAssistantPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.QueryAssistant)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#queryassistantpaginator)
    """

    def paginate(
        self, *, assistantId: str, queryText: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[QueryAssistantResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.QueryAssistant.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#queryassistantpaginator)
        """

class SearchContentPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.SearchContent)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#searchcontentpaginator)
    """

    def paginate(
        self,
        *,
        knowledgeBaseId: str,
        searchExpression: "SearchExpressionTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchContentResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.SearchContent.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#searchcontentpaginator)
        """

class SearchQuickResponsesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.SearchQuickResponses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#searchquickresponsespaginator)
    """

    def paginate(
        self,
        *,
        knowledgeBaseId: str,
        searchExpression: "QuickResponseSearchExpressionTypeDef",
        attributes: Dict[str, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchQuickResponsesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.SearchQuickResponses.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#searchquickresponsespaginator)
        """

class SearchSessionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.SearchSessions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#searchsessionspaginator)
    """

    def paginate(
        self,
        *,
        assistantId: str,
        searchExpression: "SearchExpressionTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/wisdom.html#ConnectWisdomService.Paginator.SearchSessions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators.html#searchsessionspaginator)
        """
