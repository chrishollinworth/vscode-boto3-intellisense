"""
Type annotations for neptune-graph service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_neptune_graph import NeptuneGraphClient

    client: NeptuneGraphClient = boto3.client("neptune-graph")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ExplainModeType,
    FormatType,
    GraphSummaryModeType,
    PlanCacheTypeType,
    QueryStateInputType,
)
from .paginator import (
    ListGraphSnapshotsPaginator,
    ListGraphsPaginator,
    ListImportTasksPaginator,
    ListPrivateGraphEndpointsPaginator,
)
from .type_defs import (
    CancelImportTaskOutputTypeDef,
    CreateGraphOutputTypeDef,
    CreateGraphSnapshotOutputTypeDef,
    CreateGraphUsingImportTaskOutputTypeDef,
    CreatePrivateGraphEndpointOutputTypeDef,
    DeleteGraphOutputTypeDef,
    DeleteGraphSnapshotOutputTypeDef,
    DeletePrivateGraphEndpointOutputTypeDef,
    ExecuteQueryOutputTypeDef,
    GetGraphOutputTypeDef,
    GetGraphSnapshotOutputTypeDef,
    GetGraphSummaryOutputTypeDef,
    GetImportTaskOutputTypeDef,
    GetPrivateGraphEndpointOutputTypeDef,
    GetQueryOutputTypeDef,
    ImportOptionsTypeDef,
    ListGraphSnapshotsOutputTypeDef,
    ListGraphsOutputTypeDef,
    ListImportTasksOutputTypeDef,
    ListPrivateGraphEndpointsOutputTypeDef,
    ListQueriesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ResetGraphOutputTypeDef,
    RestoreGraphFromSnapshotOutputTypeDef,
    StartImportTaskOutputTypeDef,
    UpdateGraphOutputTypeDef,
    VectorSearchConfigurationTypeDef,
)
from .waiter import (
    GraphAvailableWaiter,
    GraphDeletedWaiter,
    GraphSnapshotAvailableWaiter,
    GraphSnapshotDeletedWaiter,
    ImportTaskCancelledWaiter,
    ImportTaskSuccessfulWaiter,
    PrivateGraphEndpointAvailableWaiter,
    PrivateGraphEndpointDeletedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("NeptuneGraphClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnprocessableException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class NeptuneGraphClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NeptuneGraphClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#can_paginate)
        """

    def cancel_import_task(self, *, taskIdentifier: str) -> CancelImportTaskOutputTypeDef:
        """
        Deletes the specified import task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.cancel_import_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#cancel_import_task)
        """

    def cancel_query(self, *, graphIdentifier: str, queryId: str) -> None:
        """
        Cancels a specified query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.cancel_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#cancel_query)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#close)
        """

    def create_graph(
        self,
        *,
        graphName: str,
        provisionedMemory: int,
        tags: Dict[str, str] = None,
        publicConnectivity: bool = None,
        kmsKeyIdentifier: str = None,
        vectorSearchConfiguration: "VectorSearchConfigurationTypeDef" = None,
        replicaCount: int = None,
        deletionProtection: bool = None
    ) -> CreateGraphOutputTypeDef:
        """
        Creates a new Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.create_graph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#create_graph)
        """

    def create_graph_snapshot(
        self, *, graphIdentifier: str, snapshotName: str, tags: Dict[str, str] = None
    ) -> CreateGraphSnapshotOutputTypeDef:
        """
        Creates a snapshot of the specific graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.create_graph_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#create_graph_snapshot)
        """

    def create_graph_using_import_task(
        self,
        *,
        graphName: str,
        source: str,
        roleArn: str,
        tags: Dict[str, str] = None,
        publicConnectivity: bool = None,
        kmsKeyIdentifier: str = None,
        vectorSearchConfiguration: "VectorSearchConfigurationTypeDef" = None,
        replicaCount: int = None,
        deletionProtection: bool = None,
        importOptions: "ImportOptionsTypeDef" = None,
        maxProvisionedMemory: int = None,
        minProvisionedMemory: int = None,
        failOnError: bool = None,
        format: FormatType = None
    ) -> CreateGraphUsingImportTaskOutputTypeDef:
        """
        Creates a new Neptune Analytics graph and imports data into it, either from
        Amazon Simple Storage Service (S3) or from a Neptune database or a Neptune
        database snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.create_graph_using_import_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#create_graph_using_import_task)
        """

    def create_private_graph_endpoint(
        self,
        *,
        graphIdentifier: str,
        vpcId: str = None,
        subnetIds: List[str] = None,
        vpcSecurityGroupIds: List[str] = None
    ) -> CreatePrivateGraphEndpointOutputTypeDef:
        """
        Create a private graph endpoint to allow private access from to the graph from
        within a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.create_private_graph_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#create_private_graph_endpoint)
        """

    def delete_graph(self, *, graphIdentifier: str, skipSnapshot: bool) -> DeleteGraphOutputTypeDef:
        """
        Deletes the specified graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.delete_graph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#delete_graph)
        """

    def delete_graph_snapshot(self, *, snapshotIdentifier: str) -> DeleteGraphSnapshotOutputTypeDef:
        """
        Deletes the specifed graph snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.delete_graph_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#delete_graph_snapshot)
        """

    def delete_private_graph_endpoint(
        self, *, graphIdentifier: str, vpcId: str
    ) -> DeletePrivateGraphEndpointOutputTypeDef:
        """
        Deletes a private graph endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.delete_private_graph_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#delete_private_graph_endpoint)
        """

    def execute_query(
        self,
        *,
        graphIdentifier: str,
        queryString: str,
        language: Literal["OPEN_CYPHER"],
        parameters: Dict[str, Dict[str, Any]] = None,
        planCache: PlanCacheTypeType = None,
        explainMode: ExplainModeType = None,
        queryTimeoutMilliseconds: int = None
    ) -> ExecuteQueryOutputTypeDef:
        """
        Execute an openCypher query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.execute_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#execute_query)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#generate_presigned_url)
        """

    def get_graph(self, *, graphIdentifier: str) -> GetGraphOutputTypeDef:
        """
        Gets information about a specified graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.get_graph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#get_graph)
        """

    def get_graph_snapshot(self, *, snapshotIdentifier: str) -> GetGraphSnapshotOutputTypeDef:
        """
        Retrieves a specified graph snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.get_graph_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#get_graph_snapshot)
        """

    def get_graph_summary(
        self, *, graphIdentifier: str, mode: GraphSummaryModeType = None
    ) -> GetGraphSummaryOutputTypeDef:
        """
        Gets a graph summary for a property graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.get_graph_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#get_graph_summary)
        """

    def get_import_task(self, *, taskIdentifier: str) -> GetImportTaskOutputTypeDef:
        """
        Retrieves a specified import task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.get_import_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#get_import_task)
        """

    def get_private_graph_endpoint(
        self, *, graphIdentifier: str, vpcId: str
    ) -> GetPrivateGraphEndpointOutputTypeDef:
        """
        Retrieves information about a specified private endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.get_private_graph_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#get_private_graph_endpoint)
        """

    def get_query(self, *, graphIdentifier: str, queryId: str) -> GetQueryOutputTypeDef:
        """
        Retrieves the status of a specified query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.get_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#get_query)
        """

    def list_graph_snapshots(
        self, *, graphIdentifier: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListGraphSnapshotsOutputTypeDef:
        """
        Lists available snapshots of a specified Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.list_graph_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#list_graph_snapshots)
        """

    def list_graphs(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListGraphsOutputTypeDef:
        """
        Lists available Neptune Analytics graphs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.list_graphs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#list_graphs)
        """

    def list_import_tasks(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListImportTasksOutputTypeDef:
        """
        Lists import tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.list_import_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#list_import_tasks)
        """

    def list_private_graph_endpoints(
        self, *, graphIdentifier: str, nextToken: str = None, maxResults: int = None
    ) -> ListPrivateGraphEndpointsOutputTypeDef:
        """
        Lists private endpoints for a specified Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.list_private_graph_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#list_private_graph_endpoints)
        """

    def list_queries(
        self, *, graphIdentifier: str, maxResults: int, state: QueryStateInputType = None
    ) -> ListQueriesOutputTypeDef:
        """
        Lists active openCypher queries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.list_queries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#list_queries)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Lists tags associated with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#list_tags_for_resource)
        """

    def reset_graph(self, *, graphIdentifier: str, skipSnapshot: bool) -> ResetGraphOutputTypeDef:
        """
        Empties the data from a specified Neptune Analytics graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.reset_graph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#reset_graph)
        """

    def restore_graph_from_snapshot(
        self,
        *,
        snapshotIdentifier: str,
        graphName: str,
        provisionedMemory: int = None,
        deletionProtection: bool = None,
        tags: Dict[str, str] = None,
        replicaCount: int = None,
        publicConnectivity: bool = None
    ) -> RestoreGraphFromSnapshotOutputTypeDef:
        """
        Restores a graph from a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.restore_graph_from_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#restore_graph_from_snapshot)
        """

    def start_import_task(
        self,
        *,
        source: str,
        graphIdentifier: str,
        roleArn: str,
        importOptions: "ImportOptionsTypeDef" = None,
        failOnError: bool = None,
        format: FormatType = None
    ) -> StartImportTaskOutputTypeDef:
        """
        Import data into existing Neptune Analytics graph from Amazon Simple Storage
        Service (S3).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.start_import_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#start_import_task)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#untag_resource)
        """

    def update_graph(
        self,
        *,
        graphIdentifier: str,
        publicConnectivity: bool = None,
        provisionedMemory: int = None,
        deletionProtection: bool = None
    ) -> UpdateGraphOutputTypeDef:
        """
        Updates the configuration of a specified Neptune Analytics graph See also: `AWS
        API Documentation <https://docs.aws.amazon.com/goto/WebAPI/neptune-
        graph-2023-11-29/UpdateGraph>`_ **Request Syntax** response =
        client.update_graph( graphIdentifier='string', publicConnectivity...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Client.update_graph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/client.html#update_graph)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_graph_snapshots"]
    ) -> ListGraphSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Paginator.ListGraphSnapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators.html#listgraphsnapshotspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_graphs"]) -> ListGraphsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Paginator.ListGraphs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators.html#listgraphspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_import_tasks"]
    ) -> ListImportTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Paginator.ListImportTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators.html#listimporttaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_private_graph_endpoints"]
    ) -> ListPrivateGraphEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Paginator.ListPrivateGraphEndpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/paginators.html#listprivategraphendpointspaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["graph_available"]) -> GraphAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#graphavailablewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["graph_deleted"]) -> GraphDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#graphdeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["graph_snapshot_available"]
    ) -> GraphSnapshotAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphSnapshotAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#graphsnapshotavailablewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["graph_snapshot_deleted"]
    ) -> GraphSnapshotDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Waiter.GraphSnapshotDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#graphsnapshotdeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["import_task_cancelled"]
    ) -> ImportTaskCancelledWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Waiter.ImportTaskCancelled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#importtaskcancelledwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["import_task_successful"]
    ) -> ImportTaskSuccessfulWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Waiter.ImportTaskSuccessful)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#importtasksuccessfulwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["private_graph_endpoint_available"]
    ) -> PrivateGraphEndpointAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Waiter.PrivateGraphEndpointAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#privategraphendpointavailablewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["private_graph_endpoint_deleted"]
    ) -> PrivateGraphEndpointDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/neptune-graph.html#NeptuneGraph.Waiter.PrivateGraphEndpointDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/waiters.html#privategraphendpointdeletedwaiter)
        """
