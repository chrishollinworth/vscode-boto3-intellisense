"""
Type annotations for neptune-graph service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_neptune_graph import NeptuneGraphClient
    from mypy_boto3_neptune_graph.paginator import (
        ListGraphSnapshotsPaginator,
        ListGraphsPaginator,
        ListImportTasksPaginator,
        ListPrivateGraphEndpointsPaginator,
    )

    client: NeptuneGraphClient = boto3.client("neptune-graph")

    list_graph_snapshots_paginator: ListGraphSnapshotsPaginator = client.get_paginator("list_graph_snapshots")
    list_graphs_paginator: ListGraphsPaginator = client.get_paginator("list_graphs")
    list_import_tasks_paginator: ListImportTasksPaginator = client.get_paginator("list_import_tasks")
    list_private_graph_endpoints_paginator: ListPrivateGraphEndpointsPaginator = client.get_paginator("list_private_graph_endpoints")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListGraphSnapshotsOutputTypeDef,
    ListGraphsOutputTypeDef,
    ListImportTasksOutputTypeDef,
    ListPrivateGraphEndpointsOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListGraphSnapshotsPaginator",
    "ListGraphsPaginator",
    "ListImportTasksPaginator",
    "ListPrivateGraphEndpointsPaginator",
)

class ListGraphSnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Paginator.ListGraphSnapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators.html#listgraphsnapshotspaginator)
    """

    def paginate(
        self, *, graphIdentifier: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGraphSnapshotsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Paginator.ListGraphSnapshots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators.html#listgraphsnapshotspaginator)
        """

class ListGraphsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Paginator.ListGraphs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators.html#listgraphspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGraphsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Paginator.ListGraphs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators.html#listgraphspaginator)
        """

class ListImportTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Paginator.ListImportTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators.html#listimporttaskspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListImportTasksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Paginator.ListImportTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators.html#listimporttaskspaginator)
        """

class ListPrivateGraphEndpointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Paginator.ListPrivateGraphEndpoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators.html#listprivategraphendpointspaginator)
    """

    def paginate(
        self, *, graphIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPrivateGraphEndpointsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Paginator.ListPrivateGraphEndpoints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators.html#listprivategraphendpointspaginator)
        """
