"""
Type annotations for wisdom service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_wisdom.client import ConnectWisdomServiceClient
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

    session = Session()
    client: ConnectWisdomServiceClient = session.client("wisdom")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAssistantAssociationsRequestPaginateTypeDef,
    ListAssistantAssociationsResponseTypeDef,
    ListAssistantsRequestPaginateTypeDef,
    ListAssistantsResponseTypeDef,
    ListContentsRequestPaginateTypeDef,
    ListContentsResponseTypeDef,
    ListImportJobsRequestPaginateTypeDef,
    ListImportJobsResponseTypeDef,
    ListKnowledgeBasesRequestPaginateTypeDef,
    ListKnowledgeBasesResponseTypeDef,
    ListQuickResponsesRequestPaginateTypeDef,
    ListQuickResponsesResponseTypeDef,
    QueryAssistantRequestPaginateTypeDef,
    QueryAssistantResponseTypeDef,
    SearchContentRequestPaginateTypeDef,
    SearchContentResponseTypeDef,
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

if TYPE_CHECKING:
    _ListAssistantAssociationsPaginatorBase = Paginator[ListAssistantAssociationsResponseTypeDef]
else:
    _ListAssistantAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssistantAssociationsPaginator(_ListAssistantAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/ListAssistantAssociations.html#ConnectWisdomService.Paginator.ListAssistantAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#listassistantassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssistantAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssistantAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/ListAssistantAssociations.html#ConnectWisdomService.Paginator.ListAssistantAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#listassistantassociationspaginator)
        """

if TYPE_CHECKING:
    _ListAssistantsPaginatorBase = Paginator[ListAssistantsResponseTypeDef]
else:
    _ListAssistantsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssistantsPaginator(_ListAssistantsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/ListAssistants.html#ConnectWisdomService.Paginator.ListAssistants)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#listassistantspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssistantsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssistantsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/ListAssistants.html#ConnectWisdomService.Paginator.ListAssistants.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#listassistantspaginator)
        """

if TYPE_CHECKING:
    _ListContentsPaginatorBase = Paginator[ListContentsResponseTypeDef]
else:
    _ListContentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListContentsPaginator(_ListContentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/ListContents.html#ConnectWisdomService.Paginator.ListContents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#listcontentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListContentsRequestPaginateTypeDef]
    ) -> PageIterator[ListContentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/ListContents.html#ConnectWisdomService.Paginator.ListContents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#listcontentspaginator)
        """

if TYPE_CHECKING:
    _ListImportJobsPaginatorBase = Paginator[ListImportJobsResponseTypeDef]
else:
    _ListImportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListImportJobsPaginator(_ListImportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/ListImportJobs.html#ConnectWisdomService.Paginator.ListImportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#listimportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListImportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/ListImportJobs.html#ConnectWisdomService.Paginator.ListImportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#listimportjobspaginator)
        """

if TYPE_CHECKING:
    _ListKnowledgeBasesPaginatorBase = Paginator[ListKnowledgeBasesResponseTypeDef]
else:
    _ListKnowledgeBasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListKnowledgeBasesPaginator(_ListKnowledgeBasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/ListKnowledgeBases.html#ConnectWisdomService.Paginator.ListKnowledgeBases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#listknowledgebasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListKnowledgeBasesRequestPaginateTypeDef]
    ) -> PageIterator[ListKnowledgeBasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/ListKnowledgeBases.html#ConnectWisdomService.Paginator.ListKnowledgeBases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#listknowledgebasespaginator)
        """

if TYPE_CHECKING:
    _ListQuickResponsesPaginatorBase = Paginator[ListQuickResponsesResponseTypeDef]
else:
    _ListQuickResponsesPaginatorBase = Paginator  # type: ignore[assignment]

class ListQuickResponsesPaginator(_ListQuickResponsesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/ListQuickResponses.html#ConnectWisdomService.Paginator.ListQuickResponses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#listquickresponsespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQuickResponsesRequestPaginateTypeDef]
    ) -> PageIterator[ListQuickResponsesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/ListQuickResponses.html#ConnectWisdomService.Paginator.ListQuickResponses.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#listquickresponsespaginator)
        """

if TYPE_CHECKING:
    _QueryAssistantPaginatorBase = Paginator[QueryAssistantResponseTypeDef]
else:
    _QueryAssistantPaginatorBase = Paginator  # type: ignore[assignment]

class QueryAssistantPaginator(_QueryAssistantPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/QueryAssistant.html#ConnectWisdomService.Paginator.QueryAssistant)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#queryassistantpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[QueryAssistantRequestPaginateTypeDef]
    ) -> PageIterator[QueryAssistantResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/QueryAssistant.html#ConnectWisdomService.Paginator.QueryAssistant.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#queryassistantpaginator)
        """

if TYPE_CHECKING:
    _SearchContentPaginatorBase = Paginator[SearchContentResponseTypeDef]
else:
    _SearchContentPaginatorBase = Paginator  # type: ignore[assignment]

class SearchContentPaginator(_SearchContentPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/SearchContent.html#ConnectWisdomService.Paginator.SearchContent)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#searchcontentpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchContentRequestPaginateTypeDef]
    ) -> PageIterator[SearchContentResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/SearchContent.html#ConnectWisdomService.Paginator.SearchContent.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#searchcontentpaginator)
        """

if TYPE_CHECKING:
    _SearchQuickResponsesPaginatorBase = Paginator[SearchQuickResponsesResponseTypeDef]
else:
    _SearchQuickResponsesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchQuickResponsesPaginator(_SearchQuickResponsesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/SearchQuickResponses.html#ConnectWisdomService.Paginator.SearchQuickResponses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#searchquickresponsespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchQuickResponsesRequestPaginateTypeDef]
    ) -> PageIterator[SearchQuickResponsesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/SearchQuickResponses.html#ConnectWisdomService.Paginator.SearchQuickResponses.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#searchquickresponsespaginator)
        """

if TYPE_CHECKING:
    _SearchSessionsPaginatorBase = Paginator[SearchSessionsResponseTypeDef]
else:
    _SearchSessionsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchSessionsPaginator(_SearchSessionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/SearchSessions.html#ConnectWisdomService.Paginator.SearchSessions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#searchsessionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchSessionsRequestPaginateTypeDef]
    ) -> PageIterator[SearchSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wisdom/paginator/SearchSessions.html#ConnectWisdomService.Paginator.SearchSessions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wisdom/paginators/#searchsessionspaginator)
        """
