"""
Type annotations for repostspace service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_repostspace import rePostPrivateClient
    from mypy_boto3_repostspace.paginator import (
        ListSpacesPaginator,
    )

    client: rePostPrivateClient = boto3.client("repostspace")

    list_spaces_paginator: ListSpacesPaginator = client.get_paginator("list_spaces")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListSpacesOutputTypeDef, PaginatorConfigTypeDef

__all__ = ("ListSpacesPaginator",)

class ListSpacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Paginator.ListSpaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/paginators.html#listspacespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSpacesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/repostspace.html#rePostPrivate.Paginator.ListSpaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/paginators.html#listspacespaginator)
        """
