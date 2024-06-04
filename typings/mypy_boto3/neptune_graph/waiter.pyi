"""
Type annotations for neptune-graph service client waiters.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_neptune_graph import NeptuneGraphClient
    from mypy_boto3_neptune_graph.waiter import (
        GraphAvailableWaiter,
        GraphDeletedWaiter,
        GraphSnapshotAvailableWaiter,
        GraphSnapshotDeletedWaiter,
        ImportTaskCancelledWaiter,
        ImportTaskSuccessfulWaiter,
        PrivateGraphEndpointAvailableWaiter,
        PrivateGraphEndpointDeletedWaiter,
    )

    client: NeptuneGraphClient = boto3.client("neptune-graph")

    graph_available_waiter: GraphAvailableWaiter = client.get_waiter("graph_available")
    graph_deleted_waiter: GraphDeletedWaiter = client.get_waiter("graph_deleted")
    graph_snapshot_available_waiter: GraphSnapshotAvailableWaiter = client.get_waiter("graph_snapshot_available")
    graph_snapshot_deleted_waiter: GraphSnapshotDeletedWaiter = client.get_waiter("graph_snapshot_deleted")
    import_task_cancelled_waiter: ImportTaskCancelledWaiter = client.get_waiter("import_task_cancelled")
    import_task_successful_waiter: ImportTaskSuccessfulWaiter = client.get_waiter("import_task_successful")
    private_graph_endpoint_available_waiter: PrivateGraphEndpointAvailableWaiter = client.get_waiter("private_graph_endpoint_available")
    private_graph_endpoint_deleted_waiter: PrivateGraphEndpointDeletedWaiter = client.get_waiter("private_graph_endpoint_deleted")
    ```
"""

from botocore.waiter import Waiter as Boto3Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = (
    "GraphAvailableWaiter",
    "GraphDeletedWaiter",
    "GraphSnapshotAvailableWaiter",
    "GraphSnapshotDeletedWaiter",
    "ImportTaskCancelledWaiter",
    "ImportTaskSuccessfulWaiter",
    "PrivateGraphEndpointAvailableWaiter",
    "PrivateGraphEndpointDeletedWaiter",
)

class GraphAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphAvailable)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#graphavailablewaiter)
    """

    def wait(self, *, graphIdentifier: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphAvailable.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#graphavailablewaiter)
        """

class GraphDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#graphdeletedwaiter)
    """

    def wait(self, *, graphIdentifier: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#graphdeletedwaiter)
        """

class GraphSnapshotAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphSnapshotAvailable)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#graphsnapshotavailablewaiter)
    """

    def wait(self, *, snapshotIdentifier: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphSnapshotAvailable.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#graphsnapshotavailablewaiter)
        """

class GraphSnapshotDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphSnapshotDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#graphsnapshotdeletedwaiter)
    """

    def wait(self, *, snapshotIdentifier: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphSnapshotDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#graphsnapshotdeletedwaiter)
        """

class ImportTaskCancelledWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.ImportTaskCancelled)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#importtaskcancelledwaiter)
    """

    def wait(self, *, taskIdentifier: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.ImportTaskCancelled.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#importtaskcancelledwaiter)
        """

class ImportTaskSuccessfulWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.ImportTaskSuccessful)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#importtasksuccessfulwaiter)
    """

    def wait(self, *, taskIdentifier: str, WaiterConfig: WaiterConfigTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.ImportTaskSuccessful.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#importtasksuccessfulwaiter)
        """

class PrivateGraphEndpointAvailableWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.PrivateGraphEndpointAvailable)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#privategraphendpointavailablewaiter)
    """

    def wait(
        self, *, graphIdentifier: str, vpcId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.PrivateGraphEndpointAvailable.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#privategraphendpointavailablewaiter)
        """

class PrivateGraphEndpointDeletedWaiter(Boto3Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.PrivateGraphEndpointDeleted)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#privategraphendpointdeletedwaiter)
    """

    def wait(
        self, *, graphIdentifier: str, vpcId: str, WaiterConfig: WaiterConfigTypeDef = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/neptune-graph.html#NeptuneGraph.Waiter.PrivateGraphEndpointDeleted.wait)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#privategraphendpointdeletedwaiter)
        """
