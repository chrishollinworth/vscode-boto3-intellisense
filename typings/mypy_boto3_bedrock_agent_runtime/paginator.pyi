"""
Type annotations for bedrock-agent-runtime service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_bedrock_agent_runtime.client import AgentsforBedrockRuntimeClient
    from mypy_boto3_bedrock_agent_runtime.paginator import (
        GetAgentMemoryPaginator,
        ListInvocationStepsPaginator,
        ListInvocationsPaginator,
        ListSessionsPaginator,
        RerankPaginator,
        RetrievePaginator,
    )

    session = Session()
    client: AgentsforBedrockRuntimeClient = session.client("bedrock-agent-runtime")

    get_agent_memory_paginator: GetAgentMemoryPaginator = client.get_paginator("get_agent_memory")
    list_invocation_steps_paginator: ListInvocationStepsPaginator = client.get_paginator("list_invocation_steps")
    list_invocations_paginator: ListInvocationsPaginator = client.get_paginator("list_invocations")
    list_sessions_paginator: ListSessionsPaginator = client.get_paginator("list_sessions")
    rerank_paginator: RerankPaginator = client.get_paginator("rerank")
    retrieve_paginator: RetrievePaginator = client.get_paginator("retrieve")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetAgentMemoryRequestPaginateTypeDef,
    GetAgentMemoryResponseTypeDef,
    ListInvocationsRequestPaginateTypeDef,
    ListInvocationsResponseTypeDef,
    ListInvocationStepsRequestPaginateTypeDef,
    ListInvocationStepsResponseTypeDef,
    ListSessionsRequestPaginateTypeDef,
    ListSessionsResponseTypeDef,
    RerankRequestPaginateTypeDef,
    RerankResponseTypeDef,
    RetrieveRequestPaginateTypeDef,
    RetrieveResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetAgentMemoryPaginator",
    "ListInvocationStepsPaginator",
    "ListInvocationsPaginator",
    "ListSessionsPaginator",
    "RerankPaginator",
    "RetrievePaginator",
)

if TYPE_CHECKING:
    _GetAgentMemoryPaginatorBase = Paginator[GetAgentMemoryResponseTypeDef]
else:
    _GetAgentMemoryPaginatorBase = Paginator  # type: ignore[assignment]

class GetAgentMemoryPaginator(_GetAgentMemoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/paginator/GetAgentMemory.html#AgentsforBedrockRuntime.Paginator.GetAgentMemory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#getagentmemorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAgentMemoryRequestPaginateTypeDef]
    ) -> PageIterator[GetAgentMemoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/paginator/GetAgentMemory.html#AgentsforBedrockRuntime.Paginator.GetAgentMemory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#getagentmemorypaginator)
        """

if TYPE_CHECKING:
    _ListInvocationStepsPaginatorBase = Paginator[ListInvocationStepsResponseTypeDef]
else:
    _ListInvocationStepsPaginatorBase = Paginator  # type: ignore[assignment]

class ListInvocationStepsPaginator(_ListInvocationStepsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/paginator/ListInvocationSteps.html#AgentsforBedrockRuntime.Paginator.ListInvocationSteps)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#listinvocationstepspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInvocationStepsRequestPaginateTypeDef]
    ) -> PageIterator[ListInvocationStepsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/paginator/ListInvocationSteps.html#AgentsforBedrockRuntime.Paginator.ListInvocationSteps.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#listinvocationstepspaginator)
        """

if TYPE_CHECKING:
    _ListInvocationsPaginatorBase = Paginator[ListInvocationsResponseTypeDef]
else:
    _ListInvocationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListInvocationsPaginator(_ListInvocationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/paginator/ListInvocations.html#AgentsforBedrockRuntime.Paginator.ListInvocations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#listinvocationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListInvocationsRequestPaginateTypeDef]
    ) -> PageIterator[ListInvocationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/paginator/ListInvocations.html#AgentsforBedrockRuntime.Paginator.ListInvocations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#listinvocationspaginator)
        """

if TYPE_CHECKING:
    _ListSessionsPaginatorBase = Paginator[ListSessionsResponseTypeDef]
else:
    _ListSessionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSessionsPaginator(_ListSessionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/paginator/ListSessions.html#AgentsforBedrockRuntime.Paginator.ListSessions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#listsessionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSessionsRequestPaginateTypeDef]
    ) -> PageIterator[ListSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/paginator/ListSessions.html#AgentsforBedrockRuntime.Paginator.ListSessions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#listsessionspaginator)
        """

if TYPE_CHECKING:
    _RerankPaginatorBase = Paginator[RerankResponseTypeDef]
else:
    _RerankPaginatorBase = Paginator  # type: ignore[assignment]

class RerankPaginator(_RerankPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/paginator/Rerank.html#AgentsforBedrockRuntime.Paginator.Rerank)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#rerankpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[RerankRequestPaginateTypeDef]
    ) -> PageIterator[RerankResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/paginator/Rerank.html#AgentsforBedrockRuntime.Paginator.Rerank.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#rerankpaginator)
        """

if TYPE_CHECKING:
    _RetrievePaginatorBase = Paginator[RetrieveResponseTypeDef]
else:
    _RetrievePaginatorBase = Paginator  # type: ignore[assignment]

class RetrievePaginator(_RetrievePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/paginator/Retrieve.html#AgentsforBedrockRuntime.Paginator.Retrieve)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#retrievepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[RetrieveRequestPaginateTypeDef]
    ) -> PageIterator[RetrieveResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent-runtime/paginator/Retrieve.html#AgentsforBedrockRuntime.Paginator.Retrieve.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators/#retrievepaginator)
        """
