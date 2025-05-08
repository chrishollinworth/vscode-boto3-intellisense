"""
Type annotations for managedblockchain service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_managedblockchain.client import ManagedBlockchainClient
    from mypy_boto3_managedblockchain.paginator import (
        ListAccessorsPaginator,
    )

    session = Session()
    client: ManagedBlockchainClient = session.client("managedblockchain")

    list_accessors_paginator: ListAccessorsPaginator = client.get_paginator("list_accessors")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListAccessorsInputPaginateTypeDef, ListAccessorsOutputTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListAccessorsPaginator",)

if TYPE_CHECKING:
    _ListAccessorsPaginatorBase = Paginator[ListAccessorsOutputTypeDef]
else:
    _ListAccessorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccessorsPaginator(_ListAccessorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain/paginator/ListAccessors.html#ManagedBlockchain.Paginator.ListAccessors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/paginators/#listaccessorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccessorsInputPaginateTypeDef]
    ) -> PageIterator[ListAccessorsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain/paginator/ListAccessors.html#ManagedBlockchain.Paginator.ListAccessors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/paginators/#listaccessorspaginator)
        """
