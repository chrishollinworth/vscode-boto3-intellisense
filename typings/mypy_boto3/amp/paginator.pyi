"""
Type annotations for amp service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_amp import PrometheusServiceClient
    from mypy_boto3_amp.paginator import (
        ListWorkspacesPaginator,
    )

    client: PrometheusServiceClient = boto3.client("amp")

    list_workspaces_paginator: ListWorkspacesPaginator = client.get_paginator("list_workspaces")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListWorkspacesResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListWorkspacesPaginator",)

class ListWorkspacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amp.html#PrometheusService.Paginator.ListWorkspaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/paginators.html#listworkspacespaginator)
    """

    def paginate(
        self, *, alias: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkspacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/amp.html#PrometheusService.Paginator.ListWorkspaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/paginators.html#listworkspacespaginator)
        """
