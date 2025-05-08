"""
Type annotations for dsql service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_dsql.client import AuroraDSQLClient
    from mypy_boto3_dsql.paginator import (
        ListClustersPaginator,
    )

    session = Session()
    client: AuroraDSQLClient = session.client("dsql")

    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListClustersInputPaginateTypeDef, ListClustersOutputTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListClustersPaginator",)

if TYPE_CHECKING:
    _ListClustersPaginatorBase = Paginator[ListClustersOutputTypeDef]
else:
    _ListClustersPaginatorBase = Paginator  # type: ignore[assignment]

class ListClustersPaginator(_ListClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/paginator/ListClusters.html#AuroraDSQL.Paginator.ListClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/paginators/#listclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClustersInputPaginateTypeDef]
    ) -> PageIterator[ListClustersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/paginator/ListClusters.html#AuroraDSQL.Paginator.ListClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/paginators/#listclusterspaginator)
        """
