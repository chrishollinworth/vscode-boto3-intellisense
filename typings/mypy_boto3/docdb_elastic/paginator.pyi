"""
Type annotations for docdb-elastic service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_docdb_elastic.client import DocDBElasticClient
    from mypy_boto3_docdb_elastic.paginator import (
        ListClusterSnapshotsPaginator,
        ListClustersPaginator,
        ListPendingMaintenanceActionsPaginator,
    )

    session = Session()
    client: DocDBElasticClient = session.client("docdb-elastic")

    list_cluster_snapshots_paginator: ListClusterSnapshotsPaginator = client.get_paginator("list_cluster_snapshots")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_pending_maintenance_actions_paginator: ListPendingMaintenanceActionsPaginator = client.get_paginator("list_pending_maintenance_actions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListClustersInputPaginateTypeDef,
    ListClusterSnapshotsInputPaginateTypeDef,
    ListClusterSnapshotsOutputTypeDef,
    ListClustersOutputTypeDef,
    ListPendingMaintenanceActionsInputPaginateTypeDef,
    ListPendingMaintenanceActionsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListClusterSnapshotsPaginator",
    "ListClustersPaginator",
    "ListPendingMaintenanceActionsPaginator",
)

if TYPE_CHECKING:
    _ListClusterSnapshotsPaginatorBase = Paginator[ListClusterSnapshotsOutputTypeDef]
else:
    _ListClusterSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class ListClusterSnapshotsPaginator(_ListClusterSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic/paginator/ListClusterSnapshots.html#DocDBElastic.Paginator.ListClusterSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators/#listclustersnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClusterSnapshotsInputPaginateTypeDef]
    ) -> PageIterator[ListClusterSnapshotsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic/paginator/ListClusterSnapshots.html#DocDBElastic.Paginator.ListClusterSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators/#listclustersnapshotspaginator)
        """

if TYPE_CHECKING:
    _ListClustersPaginatorBase = Paginator[ListClustersOutputTypeDef]
else:
    _ListClustersPaginatorBase = Paginator  # type: ignore[assignment]

class ListClustersPaginator(_ListClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic/paginator/ListClusters.html#DocDBElastic.Paginator.ListClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators/#listclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClustersInputPaginateTypeDef]
    ) -> PageIterator[ListClustersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic/paginator/ListClusters.html#DocDBElastic.Paginator.ListClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators/#listclusterspaginator)
        """

if TYPE_CHECKING:
    _ListPendingMaintenanceActionsPaginatorBase = Paginator[
        ListPendingMaintenanceActionsOutputTypeDef
    ]
else:
    _ListPendingMaintenanceActionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPendingMaintenanceActionsPaginator(_ListPendingMaintenanceActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic/paginator/ListPendingMaintenanceActions.html#DocDBElastic.Paginator.ListPendingMaintenanceActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators/#listpendingmaintenanceactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPendingMaintenanceActionsInputPaginateTypeDef]
    ) -> PageIterator[ListPendingMaintenanceActionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/docdb-elastic/paginator/ListPendingMaintenanceActions.html#DocDBElastic.Paginator.ListPendingMaintenanceActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators/#listpendingmaintenanceactionspaginator)
        """
