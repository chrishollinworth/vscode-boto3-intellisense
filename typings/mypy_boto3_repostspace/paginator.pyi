"""
Type annotations for repostspace service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_repostspace.client import RePostPrivateClient
    from mypy_boto3_repostspace.paginator import (
        ListSpacesPaginator,
    )

    session = Session()
    client: RePostPrivateClient = session.client("repostspace")

    list_spaces_paginator: ListSpacesPaginator = client.get_paginator("list_spaces")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListSpacesInputPaginateTypeDef, ListSpacesOutputTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListSpacesPaginator",)

if TYPE_CHECKING:
    _ListSpacesPaginatorBase = Paginator[ListSpacesOutputTypeDef]
else:
    _ListSpacesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSpacesPaginator(_ListSpacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/paginator/ListSpaces.html#RePostPrivate.Paginator.ListSpaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/paginators/#listspacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSpacesInputPaginateTypeDef]
    ) -> PageIterator[ListSpacesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/repostspace/paginator/ListSpaces.html#RePostPrivate.Paginator.ListSpaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_repostspace/paginators/#listspacespaginator)
        """
