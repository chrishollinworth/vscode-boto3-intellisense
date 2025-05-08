"""
Type annotations for mediastore service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mediastore.client import MediaStoreClient
    from mypy_boto3_mediastore.paginator import (
        ListContainersPaginator,
    )

    session = Session()
    client: MediaStoreClient = session.client("mediastore")

    list_containers_paginator: ListContainersPaginator = client.get_paginator("list_containers")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListContainersInputPaginateTypeDef, ListContainersOutputTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListContainersPaginator",)

if TYPE_CHECKING:
    _ListContainersPaginatorBase = Paginator[ListContainersOutputTypeDef]
else:
    _ListContainersPaginatorBase = Paginator  # type: ignore[assignment]

class ListContainersPaginator(_ListContainersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/paginator/ListContainers.html#MediaStore.Paginator.ListContainers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/paginators/#listcontainerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListContainersInputPaginateTypeDef]
    ) -> PageIterator[ListContainersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore/paginator/ListContainers.html#MediaStore.Paginator.ListContainers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore/paginators/#listcontainerspaginator)
        """
