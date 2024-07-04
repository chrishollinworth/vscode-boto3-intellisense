"""
Type annotations for docdb-elastic service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_docdb_elastic import DocDBElasticClient
    from mypy_boto3_docdb_elastic.paginator import (
        ListClusterSnapshotsPaginator,
        ListClustersPaginator,
    )

    client: DocDBElasticClient = boto3.client("docdb-elastic")

    list_cluster_snapshots_paginator: ListClusterSnapshotsPaginator = client.get_paginator("list_cluster_snapshots")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListClusterSnapshotsOutputTypeDef,
    ListClustersOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListClusterSnapshotsPaginator", "ListClustersPaginator")

class ListClusterSnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Paginator.ListClusterSnapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators.html#listclustersnapshotspaginator)
    """

    def paginate(
        self,
        *,
        clusterArn: str = None,
        snapshotType: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClusterSnapshotsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Paginator.ListClusterSnapshots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators.html#listclustersnapshotspaginator)
        """

class ListClustersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Paginator.ListClusters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators.html#listclusterspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClustersOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Paginator.ListClusters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators.html#listclusterspaginator)
        """
