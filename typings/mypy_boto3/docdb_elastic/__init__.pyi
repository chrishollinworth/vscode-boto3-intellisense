"""
Main interface for docdb-elastic service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_docdb_elastic import (
        Client,
        DocDBElasticClient,
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

from .client import DocDBElasticClient
from .paginator import (
    ListClusterSnapshotsPaginator,
    ListClustersPaginator,
    ListPendingMaintenanceActionsPaginator,
)

Client = DocDBElasticClient

__all__ = (
    "Client",
    "DocDBElasticClient",
    "ListClusterSnapshotsPaginator",
    "ListClustersPaginator",
    "ListPendingMaintenanceActionsPaginator",
)
