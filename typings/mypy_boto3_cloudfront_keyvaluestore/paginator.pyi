"""
Type annotations for cloudfront-keyvaluestore service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cloudfront_keyvaluestore.client import CloudFrontKeyValueStoreClient
    from mypy_boto3_cloudfront_keyvaluestore.paginator import (
        ListKeysPaginator,
    )

    session = Session()
    client: CloudFrontKeyValueStoreClient = session.client("cloudfront-keyvaluestore")

    list_keys_paginator: ListKeysPaginator = client.get_paginator("list_keys")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListKeysRequestPaginateTypeDef, ListKeysResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListKeysPaginator",)

if TYPE_CHECKING:
    _ListKeysPaginatorBase = Paginator[ListKeysResponseTypeDef]
else:
    _ListKeysPaginatorBase = Paginator  # type: ignore[assignment]

class ListKeysPaginator(_ListKeysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront-keyvaluestore/paginator/ListKeys.html#CloudFrontKeyValueStore.Paginator.ListKeys)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/paginators/#listkeyspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListKeysRequestPaginateTypeDef]
    ) -> PageIterator[ListKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront-keyvaluestore/paginator/ListKeys.html#CloudFrontKeyValueStore.Paginator.ListKeys.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/paginators/#listkeyspaginator)
        """
