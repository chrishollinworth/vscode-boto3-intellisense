"""
Type annotations for neptune-graph service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/literals.html)

Usage::

    ```python
    from mypy_boto3_neptune_graph.literals import ExplainModeType

    data: ExplainModeType = "DETAILS"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ExplainModeType",
    "FormatType",
    "GraphAvailableWaiterName",
    "GraphDeletedWaiterName",
    "GraphSnapshotAvailableWaiterName",
    "GraphSnapshotDeletedWaiterName",
    "GraphStatusType",
    "GraphSummaryModeType",
    "ImportTaskCancelledWaiterName",
    "ImportTaskStatusType",
    "ImportTaskSuccessfulWaiterName",
    "ListGraphSnapshotsPaginatorName",
    "ListGraphsPaginatorName",
    "ListImportTasksPaginatorName",
    "ListPrivateGraphEndpointsPaginatorName",
    "PlanCacheTypeType",
    "PrivateGraphEndpointAvailableWaiterName",
    "PrivateGraphEndpointDeletedWaiterName",
    "PrivateGraphEndpointStatusType",
    "QueryLanguageType",
    "QueryStateInputType",
    "QueryStateType",
    "SnapshotStatusType",
)

ExplainModeType = Literal["DETAILS", "STATIC"]
FormatType = Literal["CSV", "OPEN_CYPHER"]
GraphAvailableWaiterName = Literal["graph_available"]
GraphDeletedWaiterName = Literal["graph_deleted"]
GraphSnapshotAvailableWaiterName = Literal["graph_snapshot_available"]
GraphSnapshotDeletedWaiterName = Literal["graph_snapshot_deleted"]
GraphStatusType = Literal[
    "AVAILABLE",
    "CREATING",
    "DELETING",
    "FAILED",
    "IMPORTING",
    "RESETTING",
    "SNAPSHOTTING",
    "UPDATING",
]
GraphSummaryModeType = Literal["BASIC", "DETAILED"]
ImportTaskCancelledWaiterName = Literal["import_task_cancelled"]
ImportTaskStatusType = Literal[
    "ANALYZING_DATA",
    "CANCELLED",
    "CANCELLING",
    "EXPORTING",
    "FAILED",
    "IMPORTING",
    "INITIALIZING",
    "REPROVISIONING",
    "ROLLING_BACK",
    "SUCCEEDED",
]
ImportTaskSuccessfulWaiterName = Literal["import_task_successful"]
ListGraphSnapshotsPaginatorName = Literal["list_graph_snapshots"]
ListGraphsPaginatorName = Literal["list_graphs"]
ListImportTasksPaginatorName = Literal["list_import_tasks"]
ListPrivateGraphEndpointsPaginatorName = Literal["list_private_graph_endpoints"]
PlanCacheTypeType = Literal["AUTO", "DISABLED", "ENABLED"]
PrivateGraphEndpointAvailableWaiterName = Literal["private_graph_endpoint_available"]
PrivateGraphEndpointDeletedWaiterName = Literal["private_graph_endpoint_deleted"]
PrivateGraphEndpointStatusType = Literal["AVAILABLE", "CREATING", "DELETING", "FAILED"]
QueryLanguageType = Literal["OPEN_CYPHER"]
QueryStateInputType = Literal["ALL", "CANCELLING", "RUNNING", "WAITING"]
QueryStateType = Literal["CANCELLING", "RUNNING", "WAITING"]
SnapshotStatusType = Literal["AVAILABLE", "CREATING", "DELETING", "FAILED"]
