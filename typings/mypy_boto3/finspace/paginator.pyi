"""
Type annotations for finspace service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_finspace.client import FinspaceClient
    from mypy_boto3_finspace.paginator import (
        ListKxEnvironmentsPaginator,
    )

    session = Session()
    client: FinspaceClient = session.client("finspace")

    list_kx_environments_paginator: ListKxEnvironmentsPaginator = client.get_paginator("list_kx_environments")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListKxEnvironmentsRequestPaginateTypeDef, ListKxEnvironmentsResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListKxEnvironmentsPaginator",)

if TYPE_CHECKING:
    _ListKxEnvironmentsPaginatorBase = Paginator[ListKxEnvironmentsResponseTypeDef]
else:
    _ListKxEnvironmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListKxEnvironmentsPaginator(_ListKxEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/paginator/ListKxEnvironments.html#Finspace.Paginator.ListKxEnvironments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/paginators/#listkxenvironmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListKxEnvironmentsRequestPaginateTypeDef]
    ) -> PageIterator[ListKxEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/finspace/paginator/ListKxEnvironments.html#Finspace.Paginator.ListKxEnvironments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_finspace/paginators/#listkxenvironmentspaginator)
        """
