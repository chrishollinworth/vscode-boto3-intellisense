# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for transfer service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_transfer import TransferClient
    from mypy_boto3_transfer.paginator import (
        ListServersPaginator,
    )

    client: TransferClient = boto3.client("transfer")

    list_servers_paginator: ListServersPaginator = client.get_paginator("list_servers")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_transfer.type_defs import ListServersResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListServersPaginator",)


class ListServersPaginator(Boto3Paginator):
    """
    [Paginator.ListServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transfer.html#Transfer.Paginator.ListServers)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServersResponseTypeDef]:
        """
        [ListServers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/transfer.html#Transfer.Paginator.ListServers.paginate)
        """
