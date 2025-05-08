"""
Type annotations for mediastore-data service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_mediastore_data.client import MediaStoreDataClient
    from mypy_boto3_mediastore_data.paginator import (
        ListItemsPaginator,
    )

    session = Session()
    client: MediaStoreDataClient = session.client("mediastore-data")

    list_items_paginator: ListItemsPaginator = client.get_paginator("list_items")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListItemsRequestPaginateTypeDef, ListItemsResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListItemsPaginator",)

if TYPE_CHECKING:
    _ListItemsPaginatorBase = Paginator[ListItemsResponseTypeDef]
else:
    _ListItemsPaginatorBase = Paginator  # type: ignore[assignment]

class ListItemsPaginator(_ListItemsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data/paginator/ListItems.html#MediaStoreData.Paginator.ListItems)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/paginators/#listitemspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListItemsRequestPaginateTypeDef]
    ) -> PageIterator[ListItemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mediastore-data/paginator/ListItems.html#MediaStoreData.Paginator.ListItems.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/paginators/#listitemspaginator)
        """
