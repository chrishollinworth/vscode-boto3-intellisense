"""
Main interface for docdb-elastic service.

Usage::

    ```python
    import boto3
    from mypy_boto3_docdb_elastic import (
        Client,
        DocDBElasticClient,
        ListClusterSnapshotsPaginator,
        ListClustersPaginator,
    )

    session = boto3.Session()

    client: DocDBElasticClient = boto3.client("docdb-elastic")
    session_client: DocDBElasticClient = session.client("docdb-elastic")

    list_cluster_snapshots_paginator: ListClusterSnapshotsPaginator = client.get_paginator("list_cluster_snapshots")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    ```
"""

from .client import DocDBElasticClient
from .paginator import ListClusterSnapshotsPaginator, ListClustersPaginator

Client = DocDBElasticClient

__all__ = ("Client", "DocDBElasticClient", "ListClusterSnapshotsPaginator", "ListClustersPaginator")
