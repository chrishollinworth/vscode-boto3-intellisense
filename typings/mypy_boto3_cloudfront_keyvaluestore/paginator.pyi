"""
Type annotations for cloudfront-keyvaluestore service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudfront_keyvaluestore import CloudFrontKeyValueStoreClient
    from mypy_boto3_cloudfront_keyvaluestore.paginator import (
        ListKeysPaginator,
    )

    client: CloudFrontKeyValueStoreClient = boto3.client("cloudfront-keyvaluestore")

    list_keys_paginator: ListKeysPaginator = client.get_paginator("list_keys")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListKeysResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListKeysPaginator",)

class ListKeysPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudfront-keyvaluestore.html#CloudFrontKeyValueStore.Paginator.ListKeys)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/paginators.html#listkeyspaginator)
    """

    def paginate(
        self, *, KvsARN: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/cloudfront-keyvaluestore.html#CloudFrontKeyValueStore.Paginator.ListKeys.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront_keyvaluestore/paginators.html#listkeyspaginator)
        """
