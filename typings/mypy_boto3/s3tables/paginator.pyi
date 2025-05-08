"""
Type annotations for s3tables service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3tables/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_s3tables.client import S3TablesClient
    from mypy_boto3_s3tables.paginator import (
        ListNamespacesPaginator,
        ListTableBucketsPaginator,
        ListTablesPaginator,
    )

    session = Session()
    client: S3TablesClient = session.client("s3tables")

    list_namespaces_paginator: ListNamespacesPaginator = client.get_paginator("list_namespaces")
    list_table_buckets_paginator: ListTableBucketsPaginator = client.get_paginator("list_table_buckets")
    list_tables_paginator: ListTablesPaginator = client.get_paginator("list_tables")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListNamespacesRequestPaginateTypeDef,
    ListNamespacesResponseTypeDef,
    ListTableBucketsRequestPaginateTypeDef,
    ListTableBucketsResponseTypeDef,
    ListTablesRequestPaginateTypeDef,
    ListTablesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListNamespacesPaginator", "ListTableBucketsPaginator", "ListTablesPaginator")

if TYPE_CHECKING:
    _ListNamespacesPaginatorBase = Paginator[ListNamespacesResponseTypeDef]
else:
    _ListNamespacesPaginatorBase = Paginator  # type: ignore[assignment]

class ListNamespacesPaginator(_ListNamespacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3tables/paginator/ListNamespaces.html#S3Tables.Paginator.ListNamespaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3tables/paginators/#listnamespacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNamespacesRequestPaginateTypeDef]
    ) -> PageIterator[ListNamespacesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3tables/paginator/ListNamespaces.html#S3Tables.Paginator.ListNamespaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3tables/paginators/#listnamespacespaginator)
        """

if TYPE_CHECKING:
    _ListTableBucketsPaginatorBase = Paginator[ListTableBucketsResponseTypeDef]
else:
    _ListTableBucketsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTableBucketsPaginator(_ListTableBucketsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3tables/paginator/ListTableBuckets.html#S3Tables.Paginator.ListTableBuckets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3tables/paginators/#listtablebucketspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTableBucketsRequestPaginateTypeDef]
    ) -> PageIterator[ListTableBucketsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3tables/paginator/ListTableBuckets.html#S3Tables.Paginator.ListTableBuckets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3tables/paginators/#listtablebucketspaginator)
        """

if TYPE_CHECKING:
    _ListTablesPaginatorBase = Paginator[ListTablesResponseTypeDef]
else:
    _ListTablesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTablesPaginator(_ListTablesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3tables/paginator/ListTables.html#S3Tables.Paginator.ListTables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3tables/paginators/#listtablespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTablesRequestPaginateTypeDef]
    ) -> PageIterator[ListTablesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3tables/paginator/ListTables.html#S3Tables.Paginator.ListTables.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_s3tables/paginators/#listtablespaginator)
        """
