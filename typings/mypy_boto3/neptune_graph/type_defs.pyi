"""
Type annotations for neptune-graph service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_neptune_graph.type_defs import CancelExportTaskInputTypeDef

    data: CancelExportTaskInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from botocore.response import StreamingBody

from .literals import (
    ExplainModeType,
    ExportFormatType,
    ExportTaskStatusType,
    FormatType,
    GraphStatusType,
    GraphSummaryModeType,
    ImportTaskStatusType,
    MultiValueHandlingTypeType,
    PlanCacheTypeType,
    PrivateGraphEndpointStatusType,
    QueryStateInputType,
    QueryStateType,
    SnapshotStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "CancelExportTaskInputTypeDef",
    "CancelExportTaskOutputTypeDef",
    "CancelImportTaskInputTypeDef",
    "CancelImportTaskOutputTypeDef",
    "CancelQueryInputTypeDef",
    "CreateGraphInputTypeDef",
    "CreateGraphOutputTypeDef",
    "CreateGraphSnapshotInputTypeDef",
    "CreateGraphSnapshotOutputTypeDef",
    "CreateGraphUsingImportTaskInputTypeDef",
    "CreateGraphUsingImportTaskOutputTypeDef",
    "CreatePrivateGraphEndpointInputTypeDef",
    "CreatePrivateGraphEndpointOutputTypeDef",
    "DeleteGraphInputTypeDef",
    "DeleteGraphOutputTypeDef",
    "DeleteGraphSnapshotInputTypeDef",
    "DeleteGraphSnapshotOutputTypeDef",
    "DeletePrivateGraphEndpointInputTypeDef",
    "DeletePrivateGraphEndpointOutputTypeDef",
    "EdgeStructureTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExecuteQueryInputTypeDef",
    "ExecuteQueryOutputTypeDef",
    "ExportFilterElementOutputTypeDef",
    "ExportFilterElementTypeDef",
    "ExportFilterOutputTypeDef",
    "ExportFilterPropertyAttributesTypeDef",
    "ExportFilterTypeDef",
    "ExportFilterUnionTypeDef",
    "ExportTaskDetailsTypeDef",
    "ExportTaskSummaryTypeDef",
    "GetExportTaskInputTypeDef",
    "GetExportTaskInputWaitExtraTypeDef",
    "GetExportTaskInputWaitTypeDef",
    "GetExportTaskOutputTypeDef",
    "GetGraphInputTypeDef",
    "GetGraphInputWaitExtraTypeDef",
    "GetGraphInputWaitTypeDef",
    "GetGraphOutputTypeDef",
    "GetGraphSnapshotInputTypeDef",
    "GetGraphSnapshotInputWaitExtraTypeDef",
    "GetGraphSnapshotInputWaitTypeDef",
    "GetGraphSnapshotOutputTypeDef",
    "GetGraphSummaryInputTypeDef",
    "GetGraphSummaryOutputTypeDef",
    "GetImportTaskInputTypeDef",
    "GetImportTaskInputWaitExtraTypeDef",
    "GetImportTaskInputWaitTypeDef",
    "GetImportTaskOutputTypeDef",
    "GetPrivateGraphEndpointInputTypeDef",
    "GetPrivateGraphEndpointInputWaitExtraTypeDef",
    "GetPrivateGraphEndpointInputWaitTypeDef",
    "GetPrivateGraphEndpointOutputTypeDef",
    "GetQueryInputTypeDef",
    "GetQueryOutputTypeDef",
    "GraphDataSummaryTypeDef",
    "GraphSnapshotSummaryTypeDef",
    "GraphSummaryTypeDef",
    "ImportOptionsTypeDef",
    "ImportTaskDetailsTypeDef",
    "ImportTaskSummaryTypeDef",
    "ListExportTasksInputPaginateTypeDef",
    "ListExportTasksInputTypeDef",
    "ListExportTasksOutputTypeDef",
    "ListGraphSnapshotsInputPaginateTypeDef",
    "ListGraphSnapshotsInputTypeDef",
    "ListGraphSnapshotsOutputTypeDef",
    "ListGraphsInputPaginateTypeDef",
    "ListGraphsInputTypeDef",
    "ListGraphsOutputTypeDef",
    "ListImportTasksInputPaginateTypeDef",
    "ListImportTasksInputTypeDef",
    "ListImportTasksOutputTypeDef",
    "ListPrivateGraphEndpointsInputPaginateTypeDef",
    "ListPrivateGraphEndpointsInputTypeDef",
    "ListPrivateGraphEndpointsOutputTypeDef",
    "ListQueriesInputTypeDef",
    "ListQueriesOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "NeptuneImportOptionsTypeDef",
    "NodeStructureTypeDef",
    "PaginatorConfigTypeDef",
    "PrivateGraphEndpointSummaryTypeDef",
    "QuerySummaryTypeDef",
    "ResetGraphInputTypeDef",
    "ResetGraphOutputTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreGraphFromSnapshotInputTypeDef",
    "RestoreGraphFromSnapshotOutputTypeDef",
    "StartExportTaskInputTypeDef",
    "StartExportTaskOutputTypeDef",
    "StartImportTaskInputTypeDef",
    "StartImportTaskOutputTypeDef",
    "TagResourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateGraphInputTypeDef",
    "UpdateGraphOutputTypeDef",
    "VectorSearchConfigurationTypeDef",
    "WaiterConfigTypeDef",
)

class CancelExportTaskInputTypeDef(TypedDict):
    taskIdentifier: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CancelImportTaskInputTypeDef(TypedDict):
    taskIdentifier: str

class CancelQueryInputTypeDef(TypedDict):
    graphIdentifier: str
    queryId: str

class VectorSearchConfigurationTypeDef(TypedDict):
    dimension: int

class CreateGraphSnapshotInputTypeDef(TypedDict):
    graphIdentifier: str
    snapshotName: str
    tags: NotRequired[Mapping[str, str]]

class CreatePrivateGraphEndpointInputTypeDef(TypedDict):
    graphIdentifier: str
    vpcId: NotRequired[str]
    subnetIds: NotRequired[Sequence[str]]
    vpcSecurityGroupIds: NotRequired[Sequence[str]]

class DeleteGraphInputTypeDef(TypedDict):
    graphIdentifier: str
    skipSnapshot: bool

class DeleteGraphSnapshotInputTypeDef(TypedDict):
    snapshotIdentifier: str

class DeletePrivateGraphEndpointInputTypeDef(TypedDict):
    graphIdentifier: str
    vpcId: str

class EdgeStructureTypeDef(TypedDict):
    count: NotRequired[int]
    edgeProperties: NotRequired[List[str]]

class ExecuteQueryInputTypeDef(TypedDict):
    graphIdentifier: str
    queryString: str
    language: Literal["OPEN_CYPHER"]
    parameters: NotRequired[Mapping[str, Mapping[str, Any]]]
    planCache: NotRequired[PlanCacheTypeType]
    explainMode: NotRequired[ExplainModeType]
    queryTimeoutMilliseconds: NotRequired[int]

class ExportFilterPropertyAttributesTypeDef(TypedDict):
    outputType: NotRequired[str]
    sourcePropertyName: NotRequired[str]
    multiValueHandling: NotRequired[MultiValueHandlingTypeType]

class ExportTaskDetailsTypeDef(TypedDict):
    startTime: datetime
    timeElapsedSeconds: int
    progressPercentage: int
    numVerticesWritten: NotRequired[int]
    numEdgesWritten: NotRequired[int]

ExportTaskSummaryTypeDef = TypedDict(
    "ExportTaskSummaryTypeDef",
    {
        "graphId": str,
        "roleArn": str,
        "taskId": str,
        "status": ExportTaskStatusType,
        "format": ExportFormatType,
        "destination": str,
        "kmsKeyIdentifier": str,
        "parquetType": NotRequired[Literal["COLUMNAR"]],
        "statusReason": NotRequired[str],
    },
)

class GetExportTaskInputTypeDef(TypedDict):
    taskIdentifier: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class GetGraphInputTypeDef(TypedDict):
    graphIdentifier: str

class GetGraphSnapshotInputTypeDef(TypedDict):
    snapshotIdentifier: str

class GetGraphSummaryInputTypeDef(TypedDict):
    graphIdentifier: str
    mode: NotRequired[GraphSummaryModeType]

class GetImportTaskInputTypeDef(TypedDict):
    taskIdentifier: str

class ImportTaskDetailsTypeDef(TypedDict):
    status: str
    startTime: datetime
    timeElapsedSeconds: int
    progressPercentage: int
    errorCount: int
    statementCount: int
    dictionaryEntryCount: int
    errorDetails: NotRequired[str]

class GetPrivateGraphEndpointInputTypeDef(TypedDict):
    graphIdentifier: str
    vpcId: str

class GetQueryInputTypeDef(TypedDict):
    graphIdentifier: str
    queryId: str

class NodeStructureTypeDef(TypedDict):
    count: NotRequired[int]
    nodeProperties: NotRequired[List[str]]
    distinctOutgoingEdgeLabels: NotRequired[List[str]]

GraphSnapshotSummaryTypeDef = TypedDict(
    "GraphSnapshotSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "sourceGraphId": NotRequired[str],
        "snapshotCreateTime": NotRequired[datetime],
        "status": NotRequired[SnapshotStatusType],
        "kmsKeyIdentifier": NotRequired[str],
    },
)
GraphSummaryTypeDef = TypedDict(
    "GraphSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": NotRequired[GraphStatusType],
        "provisionedMemory": NotRequired[int],
        "publicConnectivity": NotRequired[bool],
        "endpoint": NotRequired[str],
        "replicaCount": NotRequired[int],
        "kmsKeyIdentifier": NotRequired[str],
        "deletionProtection": NotRequired[bool],
    },
)

class NeptuneImportOptionsTypeDef(TypedDict):
    s3ExportPath: str
    s3ExportKmsKeyId: str
    preserveDefaultVertexLabels: NotRequired[bool]
    preserveEdgeIds: NotRequired[bool]

ImportTaskSummaryTypeDef = TypedDict(
    "ImportTaskSummaryTypeDef",
    {
        "taskId": str,
        "source": str,
        "roleArn": str,
        "status": ImportTaskStatusType,
        "graphId": NotRequired[str],
        "format": NotRequired[FormatType],
        "parquetType": NotRequired[Literal["COLUMNAR"]],
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListExportTasksInputTypeDef(TypedDict):
    graphIdentifier: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListGraphSnapshotsInputTypeDef(TypedDict):
    graphIdentifier: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListGraphsInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListImportTasksInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListPrivateGraphEndpointsInputTypeDef(TypedDict):
    graphIdentifier: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class PrivateGraphEndpointSummaryTypeDef(TypedDict):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: NotRequired[str]

class ListQueriesInputTypeDef(TypedDict):
    graphIdentifier: str
    maxResults: int
    state: NotRequired[QueryStateInputType]

QuerySummaryTypeDef = TypedDict(
    "QuerySummaryTypeDef",
    {
        "id": NotRequired[str],
        "queryString": NotRequired[str],
        "waited": NotRequired[int],
        "elapsed": NotRequired[int],
        "state": NotRequired[QueryStateType],
    },
)

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str

class ResetGraphInputTypeDef(TypedDict):
    graphIdentifier: str
    skipSnapshot: bool

class RestoreGraphFromSnapshotInputTypeDef(TypedDict):
    snapshotIdentifier: str
    graphName: str
    provisionedMemory: NotRequired[int]
    deletionProtection: NotRequired[bool]
    tags: NotRequired[Mapping[str, str]]
    replicaCount: NotRequired[int]
    publicConnectivity: NotRequired[bool]

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateGraphInputTypeDef(TypedDict):
    graphIdentifier: str
    publicConnectivity: NotRequired[bool]
    provisionedMemory: NotRequired[int]
    deletionProtection: NotRequired[bool]

CancelExportTaskOutputTypeDef = TypedDict(
    "CancelExportTaskOutputTypeDef",
    {
        "graphId": str,
        "roleArn": str,
        "taskId": str,
        "status": ExportTaskStatusType,
        "format": ExportFormatType,
        "destination": str,
        "kmsKeyIdentifier": str,
        "parquetType": Literal["COLUMNAR"],
        "statusReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CancelImportTaskOutputTypeDef = TypedDict(
    "CancelImportTaskOutputTypeDef",
    {
        "graphId": str,
        "taskId": str,
        "source": str,
        "format": FormatType,
        "parquetType": Literal["COLUMNAR"],
        "roleArn": str,
        "status": ImportTaskStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGraphSnapshotOutputTypeDef = TypedDict(
    "CreateGraphSnapshotOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "sourceGraphId": str,
        "snapshotCreateTime": datetime,
        "status": SnapshotStatusType,
        "kmsKeyIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreatePrivateGraphEndpointOutputTypeDef(TypedDict):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef

DeleteGraphSnapshotOutputTypeDef = TypedDict(
    "DeleteGraphSnapshotOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "sourceGraphId": str,
        "snapshotCreateTime": datetime,
        "status": SnapshotStatusType,
        "kmsKeyIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DeletePrivateGraphEndpointOutputTypeDef(TypedDict):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteQueryOutputTypeDef(TypedDict):
    payload: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

GetGraphSnapshotOutputTypeDef = TypedDict(
    "GetGraphSnapshotOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "sourceGraphId": str,
        "snapshotCreateTime": datetime,
        "status": SnapshotStatusType,
        "kmsKeyIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetPrivateGraphEndpointOutputTypeDef(TypedDict):
    vpcId: str
    subnetIds: List[str]
    status: PrivateGraphEndpointStatusType
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef

GetQueryOutputTypeDef = TypedDict(
    "GetQueryOutputTypeDef",
    {
        "id": str,
        "queryString": str,
        "waited": int,
        "elapsed": int,
        "state": QueryStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGraphInputTypeDef(TypedDict):
    graphName: str
    provisionedMemory: int
    tags: NotRequired[Mapping[str, str]]
    publicConnectivity: NotRequired[bool]
    kmsKeyIdentifier: NotRequired[str]
    vectorSearchConfiguration: NotRequired[VectorSearchConfigurationTypeDef]
    replicaCount: NotRequired[int]
    deletionProtection: NotRequired[bool]

CreateGraphOutputTypeDef = TypedDict(
    "CreateGraphOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": GraphStatusType,
        "statusReason": str,
        "createTime": datetime,
        "provisionedMemory": int,
        "endpoint": str,
        "publicConnectivity": bool,
        "vectorSearchConfiguration": VectorSearchConfigurationTypeDef,
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteGraphOutputTypeDef = TypedDict(
    "DeleteGraphOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": GraphStatusType,
        "statusReason": str,
        "createTime": datetime,
        "provisionedMemory": int,
        "endpoint": str,
        "publicConnectivity": bool,
        "vectorSearchConfiguration": VectorSearchConfigurationTypeDef,
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGraphOutputTypeDef = TypedDict(
    "GetGraphOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": GraphStatusType,
        "statusReason": str,
        "createTime": datetime,
        "provisionedMemory": int,
        "endpoint": str,
        "publicConnectivity": bool,
        "vectorSearchConfiguration": VectorSearchConfigurationTypeDef,
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetGraphOutputTypeDef = TypedDict(
    "ResetGraphOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": GraphStatusType,
        "statusReason": str,
        "createTime": datetime,
        "provisionedMemory": int,
        "endpoint": str,
        "publicConnectivity": bool,
        "vectorSearchConfiguration": VectorSearchConfigurationTypeDef,
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestoreGraphFromSnapshotOutputTypeDef = TypedDict(
    "RestoreGraphFromSnapshotOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": GraphStatusType,
        "statusReason": str,
        "createTime": datetime,
        "provisionedMemory": int,
        "endpoint": str,
        "publicConnectivity": bool,
        "vectorSearchConfiguration": VectorSearchConfigurationTypeDef,
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGraphOutputTypeDef = TypedDict(
    "UpdateGraphOutputTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "status": GraphStatusType,
        "statusReason": str,
        "createTime": datetime,
        "provisionedMemory": int,
        "endpoint": str,
        "publicConnectivity": bool,
        "vectorSearchConfiguration": VectorSearchConfigurationTypeDef,
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ExportFilterElementOutputTypeDef(TypedDict):
    properties: NotRequired[Dict[str, ExportFilterPropertyAttributesTypeDef]]

class ExportFilterElementTypeDef(TypedDict):
    properties: NotRequired[Mapping[str, ExportFilterPropertyAttributesTypeDef]]

class ListExportTasksOutputTypeDef(TypedDict):
    tasks: List[ExportTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetExportTaskInputWaitExtraTypeDef(TypedDict):
    taskIdentifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetExportTaskInputWaitTypeDef(TypedDict):
    taskIdentifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetGraphInputWaitExtraTypeDef(TypedDict):
    graphIdentifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetGraphInputWaitTypeDef(TypedDict):
    graphIdentifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetGraphSnapshotInputWaitExtraTypeDef(TypedDict):
    snapshotIdentifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetGraphSnapshotInputWaitTypeDef(TypedDict):
    snapshotIdentifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetImportTaskInputWaitExtraTypeDef(TypedDict):
    taskIdentifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetImportTaskInputWaitTypeDef(TypedDict):
    taskIdentifier: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetPrivateGraphEndpointInputWaitExtraTypeDef(TypedDict):
    graphIdentifier: str
    vpcId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetPrivateGraphEndpointInputWaitTypeDef(TypedDict):
    graphIdentifier: str
    vpcId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GraphDataSummaryTypeDef(TypedDict):
    numNodes: NotRequired[int]
    numEdges: NotRequired[int]
    numNodeLabels: NotRequired[int]
    numEdgeLabels: NotRequired[int]
    nodeLabels: NotRequired[List[str]]
    edgeLabels: NotRequired[List[str]]
    numNodeProperties: NotRequired[int]
    numEdgeProperties: NotRequired[int]
    nodeProperties: NotRequired[List[Dict[str, int]]]
    edgeProperties: NotRequired[List[Dict[str, int]]]
    totalNodePropertyValues: NotRequired[int]
    totalEdgePropertyValues: NotRequired[int]
    nodeStructures: NotRequired[List[NodeStructureTypeDef]]
    edgeStructures: NotRequired[List[EdgeStructureTypeDef]]

class ListGraphSnapshotsOutputTypeDef(TypedDict):
    graphSnapshots: List[GraphSnapshotSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListGraphsOutputTypeDef(TypedDict):
    graphs: List[GraphSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ImportOptionsTypeDef(TypedDict):
    neptune: NotRequired[NeptuneImportOptionsTypeDef]

class ListImportTasksOutputTypeDef(TypedDict):
    tasks: List[ImportTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListExportTasksInputPaginateTypeDef(TypedDict):
    graphIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGraphSnapshotsInputPaginateTypeDef(TypedDict):
    graphIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGraphsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListImportTasksInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPrivateGraphEndpointsInputPaginateTypeDef(TypedDict):
    graphIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPrivateGraphEndpointsOutputTypeDef(TypedDict):
    privateGraphEndpoints: List[PrivateGraphEndpointSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListQueriesOutputTypeDef(TypedDict):
    queries: List[QuerySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ExportFilterOutputTypeDef(TypedDict):
    vertexFilter: NotRequired[Dict[str, ExportFilterElementOutputTypeDef]]
    edgeFilter: NotRequired[Dict[str, ExportFilterElementOutputTypeDef]]

class ExportFilterTypeDef(TypedDict):
    vertexFilter: NotRequired[Mapping[str, ExportFilterElementTypeDef]]
    edgeFilter: NotRequired[Mapping[str, ExportFilterElementTypeDef]]

class GetGraphSummaryOutputTypeDef(TypedDict):
    version: str
    lastStatisticsComputationTime: datetime
    graphSummary: GraphDataSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CreateGraphUsingImportTaskInputTypeDef = TypedDict(
    "CreateGraphUsingImportTaskInputTypeDef",
    {
        "graphName": str,
        "source": str,
        "roleArn": str,
        "tags": NotRequired[Mapping[str, str]],
        "publicConnectivity": NotRequired[bool],
        "kmsKeyIdentifier": NotRequired[str],
        "vectorSearchConfiguration": NotRequired[VectorSearchConfigurationTypeDef],
        "replicaCount": NotRequired[int],
        "deletionProtection": NotRequired[bool],
        "importOptions": NotRequired[ImportOptionsTypeDef],
        "maxProvisionedMemory": NotRequired[int],
        "minProvisionedMemory": NotRequired[int],
        "failOnError": NotRequired[bool],
        "format": NotRequired[FormatType],
        "parquetType": NotRequired[Literal["COLUMNAR"]],
        "blankNodeHandling": NotRequired[Literal["convertToIri"]],
    },
)
CreateGraphUsingImportTaskOutputTypeDef = TypedDict(
    "CreateGraphUsingImportTaskOutputTypeDef",
    {
        "graphId": str,
        "taskId": str,
        "source": str,
        "format": FormatType,
        "parquetType": Literal["COLUMNAR"],
        "roleArn": str,
        "status": ImportTaskStatusType,
        "importOptions": ImportOptionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetImportTaskOutputTypeDef = TypedDict(
    "GetImportTaskOutputTypeDef",
    {
        "graphId": str,
        "taskId": str,
        "source": str,
        "format": FormatType,
        "parquetType": Literal["COLUMNAR"],
        "roleArn": str,
        "status": ImportTaskStatusType,
        "importOptions": ImportOptionsTypeDef,
        "importTaskDetails": ImportTaskDetailsTypeDef,
        "attemptNumber": int,
        "statusReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartImportTaskInputTypeDef = TypedDict(
    "StartImportTaskInputTypeDef",
    {
        "source": str,
        "graphIdentifier": str,
        "roleArn": str,
        "importOptions": NotRequired[ImportOptionsTypeDef],
        "failOnError": NotRequired[bool],
        "format": NotRequired[FormatType],
        "parquetType": NotRequired[Literal["COLUMNAR"]],
        "blankNodeHandling": NotRequired[Literal["convertToIri"]],
    },
)
StartImportTaskOutputTypeDef = TypedDict(
    "StartImportTaskOutputTypeDef",
    {
        "graphId": str,
        "taskId": str,
        "source": str,
        "format": FormatType,
        "parquetType": Literal["COLUMNAR"],
        "roleArn": str,
        "status": ImportTaskStatusType,
        "importOptions": ImportOptionsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetExportTaskOutputTypeDef = TypedDict(
    "GetExportTaskOutputTypeDef",
    {
        "graphId": str,
        "roleArn": str,
        "taskId": str,
        "status": ExportTaskStatusType,
        "format": ExportFormatType,
        "destination": str,
        "kmsKeyIdentifier": str,
        "parquetType": Literal["COLUMNAR"],
        "statusReason": str,
        "exportTaskDetails": ExportTaskDetailsTypeDef,
        "exportFilter": ExportFilterOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartExportTaskOutputTypeDef = TypedDict(
    "StartExportTaskOutputTypeDef",
    {
        "graphId": str,
        "roleArn": str,
        "taskId": str,
        "status": ExportTaskStatusType,
        "format": ExportFormatType,
        "destination": str,
        "kmsKeyIdentifier": str,
        "parquetType": Literal["COLUMNAR"],
        "statusReason": str,
        "exportFilter": ExportFilterOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportFilterUnionTypeDef = Union[ExportFilterTypeDef, ExportFilterOutputTypeDef]
StartExportTaskInputTypeDef = TypedDict(
    "StartExportTaskInputTypeDef",
    {
        "graphIdentifier": str,
        "roleArn": str,
        "format": ExportFormatType,
        "destination": str,
        "kmsKeyIdentifier": str,
        "parquetType": NotRequired[Literal["COLUMNAR"]],
        "exportFilter": NotRequired[ExportFilterUnionTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
