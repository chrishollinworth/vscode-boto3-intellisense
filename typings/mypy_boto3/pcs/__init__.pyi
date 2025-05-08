"""
Main interface for pcs service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_pcs import (
        Client,
        ListClustersPaginator,
        ListComputeNodeGroupsPaginator,
        ListQueuesPaginator,
        ParallelComputingServiceClient,
    )

    session = Session()
    client: ParallelComputingServiceClient = session.client("pcs")

    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_compute_node_groups_paginator: ListComputeNodeGroupsPaginator = client.get_paginator("list_compute_node_groups")
    list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
    ```
"""

from .client import ParallelComputingServiceClient
from .paginator import ListClustersPaginator, ListComputeNodeGroupsPaginator, ListQueuesPaginator

Client = ParallelComputingServiceClient

__all__ = (
    "Client",
    "ListClustersPaginator",
    "ListComputeNodeGroupsPaginator",
    "ListQueuesPaginator",
    "ParallelComputingServiceClient",
)
