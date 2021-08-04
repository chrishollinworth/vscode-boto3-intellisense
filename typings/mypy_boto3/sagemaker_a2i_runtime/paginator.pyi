"""
Type annotations for sagemaker-a2i-runtime service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_sagemaker_a2i_runtime import AugmentedAIRuntimeClient
    from mypy_boto3_sagemaker_a2i_runtime.paginator import (
        ListHumanLoopsPaginator,
    )

    client: AugmentedAIRuntimeClient = boto3.client("sagemaker-a2i-runtime")

    list_human_loops_paginator: ListHumanLoopsPaginator = client.get_paginator("list_human_loops")
    ```
"""
from datetime import datetime
from typing import Iterator, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import SortOrderType
from .type_defs import ListHumanLoopsResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListHumanLoopsPaginator",)

class ListHumanLoopsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Paginator.ListHumanLoops)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/paginators.html#listhumanloopspaginator)
    """

    def paginate(
        self,
        *,
        FlowDefinitionArn: str,
        CreationTimeAfter: Union[datetime, str] = None,
        CreationTimeBefore: Union[datetime, str] = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListHumanLoopsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Paginator.ListHumanLoops.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/paginators.html#listhumanloopspaginator)
        """
