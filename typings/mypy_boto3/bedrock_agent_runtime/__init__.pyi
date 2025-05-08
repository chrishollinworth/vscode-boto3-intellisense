"""
Main interface for bedrock-agent-runtime service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bedrock_agent_runtime import (
        AgentsforBedrockRuntimeClient,
        Client,
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

from .client import AgentsforBedrockRuntimeClient
from .paginator import (
    GetAgentMemoryPaginator,
    ListInvocationsPaginator,
    ListInvocationStepsPaginator,
    ListSessionsPaginator,
    RerankPaginator,
    RetrievePaginator,
)

Client = AgentsforBedrockRuntimeClient

__all__ = (
    "AgentsforBedrockRuntimeClient",
    "Client",
    "GetAgentMemoryPaginator",
    "ListInvocationStepsPaginator",
    "ListInvocationsPaginator",
    "ListSessionsPaginator",
    "RerankPaginator",
    "RetrievePaginator",
)
