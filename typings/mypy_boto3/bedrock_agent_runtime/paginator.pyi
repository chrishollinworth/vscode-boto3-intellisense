"""
Type annotations for bedrock-agent-runtime service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_bedrock_agent_runtime import AgentsforBedrockRuntimeClient
    from mypy_boto3_bedrock_agent_runtime.paginator import (
        RetrievePaginator,
    )

    client: AgentsforBedrockRuntimeClient = boto3.client("bedrock-agent-runtime")

    retrieve_paginator: RetrievePaginator = client.get_paginator("retrieve")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    KnowledgeBaseQueryTypeDef,
    KnowledgeBaseRetrievalConfigurationTypeDef,
    PaginatorConfigTypeDef,
    RetrieveResponseTypeDef,
)

__all__ = ("RetrievePaginator",)

class RetrievePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Paginator.Retrieve)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators.html#retrievepaginator)
    """

    def paginate(
        self,
        *,
        knowledgeBaseId: str,
        retrievalQuery: "KnowledgeBaseQueryTypeDef",
        retrievalConfiguration: "KnowledgeBaseRetrievalConfigurationTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[RetrieveResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/bedrock-agent-runtime.html#AgentsforBedrockRuntime.Paginator.Retrieve.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agent_runtime/paginators.html#retrievepaginator)
        """
