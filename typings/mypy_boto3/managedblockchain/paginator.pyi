"""
Type annotations for managedblockchain service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_managedblockchain import ManagedBlockchainClient
    from mypy_boto3_managedblockchain.paginator import (
        ListAccessorsPaginator,
    )

    client: ManagedBlockchainClient = boto3.client("managedblockchain")

    list_accessors_paginator: ListAccessorsPaginator = client.get_paginator("list_accessors")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListAccessorsOutputTypeDef, PaginatorConfigTypeDef

__all__ = ("ListAccessorsPaginator",)

class ListAccessorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/managedblockchain.html#ManagedBlockchain.Paginator.ListAccessors)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/paginators.html#listaccessorspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccessorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/managedblockchain.html#ManagedBlockchain.Paginator.ListAccessors.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/paginators.html#listaccessorspaginator)
        """
