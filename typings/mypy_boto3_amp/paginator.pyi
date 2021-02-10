"""
Main interface for amp service client paginators.

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

from mypy_boto3_amp.type_defs import ListWorkspacesResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListWorkspacesPaginator",)


class ListWorkspacesPaginator(Boto3Paginator):
    """
    [Paginator.ListWorkspaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/amp.html#PrometheusService.Paginator.ListWorkspaces)
    """

    def paginate(
        self, alias: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorkspacesResponseTypeDef]:
        """
        [ListWorkspaces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/amp.html#PrometheusService.Paginator.ListWorkspaces.paginate)
        """
