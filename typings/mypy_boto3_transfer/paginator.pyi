"""
Type annotations for transfer service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html)

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

from .type_defs import ListServersResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListServersPaginator",)

class ListServersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/transfer.html#Transfer.Paginator.ListServers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listserverspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/transfer.html#Transfer.Paginator.ListServers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listserverspaginator)
        """
