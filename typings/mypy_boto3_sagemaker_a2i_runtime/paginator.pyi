"""
Type annotations for sagemaker-a2i-runtime service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_sagemaker_a2i_runtime.client import AugmentedAIRuntimeClient
    from mypy_boto3_sagemaker_a2i_runtime.paginator import (
        ListHumanLoopsPaginator,
    )

    session = Session()
    client: AugmentedAIRuntimeClient = session.client("sagemaker-a2i-runtime")

    list_human_loops_paginator: ListHumanLoopsPaginator = client.get_paginator("list_human_loops")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListHumanLoopsRequestPaginateTypeDef, ListHumanLoopsResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListHumanLoopsPaginator",)

if TYPE_CHECKING:
    _ListHumanLoopsPaginatorBase = Paginator[ListHumanLoopsResponseTypeDef]
else:
    _ListHumanLoopsPaginatorBase = Paginator  # type: ignore[assignment]

class ListHumanLoopsPaginator(_ListHumanLoopsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime/paginator/ListHumanLoops.html#AugmentedAIRuntime.Paginator.ListHumanLoops)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/paginators/#listhumanloopspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListHumanLoopsRequestPaginateTypeDef]
    ) -> PageIterator[ListHumanLoopsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime/paginator/ListHumanLoops.html#AugmentedAIRuntime.Paginator.ListHumanLoops.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/paginators/#listhumanloopspaginator)
        """
