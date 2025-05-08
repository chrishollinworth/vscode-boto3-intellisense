"""
Type annotations for neptune-graph service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_neptune_graph.client import NeptuneGraphClient
    from mypy_boto3_neptune_graph.paginator import (
        ListExportTasksPaginator,
        ListGraphSnapshotsPaginator,
        ListGraphsPaginator,
        ListImportTasksPaginator,
        ListPrivateGraphEndpointsPaginator,
    )

    session = Session()
    client: NeptuneGraphClient = session.client("neptune-graph")

    list_export_tasks_paginator: ListExportTasksPaginator = client.get_paginator("list_export_tasks")
    list_graph_snapshots_paginator: ListGraphSnapshotsPaginator = client.get_paginator("list_graph_snapshots")
    list_graphs_paginator: ListGraphsPaginator = client.get_paginator("list_graphs")
    list_import_tasks_paginator: ListImportTasksPaginator = client.get_paginator("list_import_tasks")
    list_private_graph_endpoints_paginator: ListPrivateGraphEndpointsPaginator = client.get_paginator("list_private_graph_endpoints")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListExportTasksInputPaginateTypeDef,
    ListExportTasksOutputTypeDef,
    ListGraphsInputPaginateTypeDef,
    ListGraphSnapshotsInputPaginateTypeDef,
    ListGraphSnapshotsOutputTypeDef,
    ListGraphsOutputTypeDef,
    ListImportTasksInputPaginateTypeDef,
    ListImportTasksOutputTypeDef,
    ListPrivateGraphEndpointsInputPaginateTypeDef,
    ListPrivateGraphEndpointsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListExportTasksPaginator",
    "ListGraphSnapshotsPaginator",
    "ListGraphsPaginator",
    "ListImportTasksPaginator",
    "ListPrivateGraphEndpointsPaginator",
)

if TYPE_CHECKING:
    _ListExportTasksPaginatorBase = Paginator[ListExportTasksOutputTypeDef]
else:
    _ListExportTasksPaginatorBase = Paginator  # type: ignore[assignment]

class ListExportTasksPaginator(_ListExportTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/paginator/ListExportTasks.html#NeptuneGraph.Paginator.ListExportTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators/#listexporttaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExportTasksInputPaginateTypeDef]
    ) -> PageIterator[ListExportTasksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/paginator/ListExportTasks.html#NeptuneGraph.Paginator.ListExportTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators/#listexporttaskspaginator)
        """

if TYPE_CHECKING:
    _ListGraphSnapshotsPaginatorBase = Paginator[ListGraphSnapshotsOutputTypeDef]
else:
    _ListGraphSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGraphSnapshotsPaginator(_ListGraphSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/paginator/ListGraphSnapshots.html#NeptuneGraph.Paginator.ListGraphSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators/#listgraphsnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGraphSnapshotsInputPaginateTypeDef]
    ) -> PageIterator[ListGraphSnapshotsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/paginator/ListGraphSnapshots.html#NeptuneGraph.Paginator.ListGraphSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators/#listgraphsnapshotspaginator)
        """

if TYPE_CHECKING:
    _ListGraphsPaginatorBase = Paginator[ListGraphsOutputTypeDef]
else:
    _ListGraphsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGraphsPaginator(_ListGraphsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/paginator/ListGraphs.html#NeptuneGraph.Paginator.ListGraphs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators/#listgraphspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGraphsInputPaginateTypeDef]
    ) -> PageIterator[ListGraphsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/paginator/ListGraphs.html#NeptuneGraph.Paginator.ListGraphs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators/#listgraphspaginator)
        """

if TYPE_CHECKING:
    _ListImportTasksPaginatorBase = Paginator[ListImportTasksOutputTypeDef]
else:
    _ListImportTasksPaginatorBase = Paginator  # type: ignore[assignment]

class ListImportTasksPaginator(_ListImportTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/paginator/ListImportTasks.html#NeptuneGraph.Paginator.ListImportTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators/#listimporttaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListImportTasksInputPaginateTypeDef]
    ) -> PageIterator[ListImportTasksOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/paginator/ListImportTasks.html#NeptuneGraph.Paginator.ListImportTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators/#listimporttaskspaginator)
        """

if TYPE_CHECKING:
    _ListPrivateGraphEndpointsPaginatorBase = Paginator[ListPrivateGraphEndpointsOutputTypeDef]
else:
    _ListPrivateGraphEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPrivateGraphEndpointsPaginator(_ListPrivateGraphEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/paginator/ListPrivateGraphEndpoints.html#NeptuneGraph.Paginator.ListPrivateGraphEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators/#listprivategraphendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPrivateGraphEndpointsInputPaginateTypeDef]
    ) -> PageIterator[ListPrivateGraphEndpointsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptune-graph/paginator/ListPrivateGraphEndpoints.html#NeptuneGraph.Paginator.ListPrivateGraphEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators/#listprivategraphendpointspaginator)
        """
