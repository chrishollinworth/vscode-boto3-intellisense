"""
Type annotations for ivs-realtime service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_ivs_realtime import ivsrealtimeClient
    from mypy_boto3_ivs_realtime.paginator import (
        ListPublicKeysPaginator,
    )

    client: ivsrealtimeClient = boto3.client("ivs-realtime")

    list_public_keys_paginator: ListPublicKeysPaginator = client.get_paginator("list_public_keys")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListPublicKeysResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListPublicKeysPaginator",)

class ListPublicKeysPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Paginator.ListPublicKeys)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/paginators.html#listpublickeyspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPublicKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ivs-realtime.html#ivsrealtime.Paginator.ListPublicKeys.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs_realtime/paginators.html#listpublickeyspaginator)
        """
