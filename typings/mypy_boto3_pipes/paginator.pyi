"""
Type annotations for pipes service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_pipes import EventBridgePipesClient
    from mypy_boto3_pipes.paginator import (
        ListPipesPaginator,
    )

    client: EventBridgePipesClient = boto3.client("pipes")

    list_pipes_paginator: ListPipesPaginator = client.get_paginator("list_pipes")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import PipeStateType, RequestedPipeStateType
from .type_defs import ListPipesResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListPipesPaginator",)

class ListPipesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Paginator.ListPipes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/paginators.html#listpipespaginator)
    """

    def paginate(
        self,
        *,
        CurrentState: PipeStateType = None,
        DesiredState: RequestedPipeStateType = None,
        NamePrefix: str = None,
        SourcePrefix: str = None,
        TargetPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPipesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/pipes.html#EventBridgePipes.Paginator.ListPipes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/paginators.html#listpipespaginator)
        """
