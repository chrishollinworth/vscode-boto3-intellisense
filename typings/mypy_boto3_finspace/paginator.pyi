"""
Type annotations for finspace service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_finspace import finspaceClient
    from mypy_boto3_finspace.paginator import (
        ListKxEnvironmentsPaginator,
    )

    client: finspaceClient = boto3.client("finspace")

    list_kx_environments_paginator: ListKxEnvironmentsPaginator = client.get_paginator("list_kx_environments")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import ListKxEnvironmentsResponseTypeDef, PaginatorConfigTypeDef

__all__ = ("ListKxEnvironmentsPaginator",)

class ListKxEnvironmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/finspace.html#finspace.Paginator.ListKxEnvironments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/paginators.html#listkxenvironmentspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKxEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/finspace.html#finspace.Paginator.ListKxEnvironments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/paginators.html#listkxenvironmentspaginator)
        """
