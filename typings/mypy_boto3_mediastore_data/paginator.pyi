# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for mediastore-data service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_mediastore_data import MediaStoreDataClient
    from mypy_boto3_mediastore_data.paginator import (
        ListItemsPaginator,
    )

    client: MediaStoreDataClient = boto3.client("mediastore-data")

    list_items_paginator: ListItemsPaginator = client.get_paginator("list_items")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_mediastore_data.type_defs import ListItemsResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListItemsPaginator",)


class ListItemsPaginator(Boto3Paginator):
    """
    [Paginator.ListItems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore-data.html#MediaStoreData.Paginator.ListItems)
    """

    def paginate(
        self, Path: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListItemsResponseTypeDef]:
        """
        [ListItems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore-data.html#MediaStoreData.Paginator.ListItems.paginate)
        """
