"""
Type annotations for pcs service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_pcs.client import ParallelComputingServiceClient
    from mypy_boto3_pcs.paginator import (
        ListClustersPaginator,
        ListComputeNodeGroupsPaginator,
        ListQueuesPaginator,
    )

    session = Session()
    client: ParallelComputingServiceClient = session.client("pcs")

    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_compute_node_groups_paginator: ListComputeNodeGroupsPaginator = client.get_paginator("list_compute_node_groups")
    list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListClustersRequestPaginateTypeDef,
    ListClustersResponseTypeDef,
    ListComputeNodeGroupsRequestPaginateTypeDef,
    ListComputeNodeGroupsResponseTypeDef,
    ListQueuesRequestPaginateTypeDef,
    ListQueuesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListClustersPaginator", "ListComputeNodeGroupsPaginator", "ListQueuesPaginator")

if TYPE_CHECKING:
    _ListClustersPaginatorBase = Paginator[ListClustersResponseTypeDef]
else:
    _ListClustersPaginatorBase = Paginator  # type: ignore[assignment]

class ListClustersPaginator(_ListClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/paginator/ListClusters.html#ParallelComputingService.Paginator.ListClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/paginators/#listclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClustersRequestPaginateTypeDef]
    ) -> PageIterator[ListClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/paginator/ListClusters.html#ParallelComputingService.Paginator.ListClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/paginators/#listclusterspaginator)
        """

if TYPE_CHECKING:
    _ListComputeNodeGroupsPaginatorBase = Paginator[ListComputeNodeGroupsResponseTypeDef]
else:
    _ListComputeNodeGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListComputeNodeGroupsPaginator(_ListComputeNodeGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/paginator/ListComputeNodeGroups.html#ParallelComputingService.Paginator.ListComputeNodeGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/paginators/#listcomputenodegroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListComputeNodeGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListComputeNodeGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/paginator/ListComputeNodeGroups.html#ParallelComputingService.Paginator.ListComputeNodeGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/paginators/#listcomputenodegroupspaginator)
        """

if TYPE_CHECKING:
    _ListQueuesPaginatorBase = Paginator[ListQueuesResponseTypeDef]
else:
    _ListQueuesPaginatorBase = Paginator  # type: ignore[assignment]

class ListQueuesPaginator(_ListQueuesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/paginator/ListQueues.html#ParallelComputingService.Paginator.ListQueues)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/paginators/#listqueuespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListQueuesRequestPaginateTypeDef]
    ) -> PageIterator[ListQueuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/paginator/ListQueues.html#ParallelComputingService.Paginator.ListQueues.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/paginators/#listqueuespaginator)
        """
