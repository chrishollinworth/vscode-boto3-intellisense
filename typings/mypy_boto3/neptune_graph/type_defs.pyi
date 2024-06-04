"""
Type annotations for neptune-graph service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune_graph/type_defs.html)

Usage::

    ```python
    from mypy_boto3_neptune_graph.type_defs import CancelImportTaskInputRequestTypeDef

    data: CancelImportTaskInputRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from botocore.response import StreamingBody

from .literals import (
    ExplainModeType,
    FormatType,
    GraphStatusType,
    GraphSummaryModeType,
    ImportTaskStatusType,
    PlanCacheTypeType,
    PrivateGraphEndpointStatusType,
    QueryStateInputType,
    QueryStateType,
    SnapshotStatusType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CancelImportTaskInputRequestTypeDef",
    "CancelImportTaskOutputTypeDef",
    "CancelQueryInputRequestTypeDef",
    "CreateGraphInputRequestTypeDef",
    "CreateGraphOutputTypeDef",
    "CreateGraphSnapshotInputRequestTypeDef",
    "CreateGraphSnapshotOutputTypeDef",
    "CreateGraphUsingImportTaskInputRequestTypeDef",
    "CreateGraphUsingImportTaskOutputTypeDef",
    "CreatePrivateGraphEndpointInputRequestTypeDef",
    "CreatePrivateGraphEndpointOutputTypeDef",
    "DeleteGraphInputRequestTypeDef",
    "DeleteGraphOutputTypeDef",
    "DeleteGraphSnapshotInputRequestTypeDef",
    "DeleteGraphSnapshotOutputTypeDef",
    "DeletePrivateGraphEndpointInputRequestTypeDef",
    "DeletePrivateGraphEndpointOutputTypeDef",
    "EdgeStructureTypeDef",
    "ExecuteQueryInputRequestTypeDef",
    "ExecuteQueryOutputTypeDef",
    "GetGraphInputRequestTypeDef",
    "GetGraphOutputTypeDef",
    "GetGraphSnapshotInputRequestTypeDef",
    "GetGraphSnapshotOutputTypeDef",
    "GetGraphSummaryInputRequestTypeDef",
    "GetGraphSummaryOutputTypeDef",
    "GetImportTaskInputRequestTypeDef",
    "GetImportTaskOutputTypeDef",
    "GetPrivateGraphEndpointInputRequestTypeDef",
    "GetPrivateGraphEndpointOutputTypeDef",
    "GetQueryInputRequestTypeDef",
    "GetQueryOutputTypeDef",
    "GraphDataSummaryTypeDef",
    "GraphSnapshotSummaryTypeDef",
    "GraphSummaryTypeDef",
    "ImportOptionsTypeDef",
    "ImportTaskDetailsTypeDef",
    "ImportTaskSummaryTypeDef",
    "ListGraphSnapshotsInputRequestTypeDef",
    "ListGraphSnapshotsOutputTypeDef",
    "ListGraphsInputRequestTypeDef",
    "ListGraphsOutputTypeDef",
    "ListImportTasksInputRequestTypeDef",
    "ListImportTasksOutputTypeDef",
    "ListPrivateGraphEndpointsInputRequestTypeDef",
    "ListPrivateGraphEndpointsOutputTypeDef",
    "ListQueriesInputRequestTypeDef",
    "ListQueriesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "NeptuneImportOptionsTypeDef",
    "NodeStructureTypeDef",
    "PaginatorConfigTypeDef",
    "PrivateGraphEndpointSummaryTypeDef",
    "QuerySummaryTypeDef",
    "ResetGraphInputRequestTypeDef",
    "ResetGraphOutputTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreGraphFromSnapshotInputRequestTypeDef",
    "RestoreGraphFromSnapshotOutputTypeDef",
    "StartImportTaskInputRequestTypeDef",
    "StartImportTaskOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateGraphInputRequestTypeDef",
    "UpdateGraphOutputTypeDef",
    "VectorSearchConfigurationTypeDef",
    "WaiterConfigTypeDef",
)

CancelImportTaskInputRequestTypeDef = TypedDict(
    "CancelImportTaskInputRequestTypeDef",
    {
        "taskIdentifier": str,
    },
)

CancelImportTaskOutputTypeDef = TypedDict(
    "CancelImportTaskOutputTypeDef",
    {
        "graphId": str,
        "taskId": str,
        "source": str,
        "format": FormatType,
        "roleArn": str,
        "status": ImportTaskStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelQueryInputRequestTypeDef = TypedDict(
    "CancelQueryInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "queryId": str,
    },
)

_RequiredCreateGraphInputRequestTypeDef = TypedDict(
    "_RequiredCreateGraphInputRequestTypeDef",
    {
        "graphName": str,
        "provisionedMemory": int,
    },
)
_OptionalCreateGraphInputRequestTypeDef = TypedDict(
    "_OptionalCreateGraphInputRequestTypeDef",
    {
        "tags": Dict[str, str],
        "publicConnectivity": bool,
        "kmsKeyIdentifier": str,
        "vectorSearchConfiguration": "VectorSearchConfigurationTypeDef",
        "replicaCount": int,
        "deletionProtection": bool,
    },
    total=False,
)

class CreateGraphInputRequestTypeDef(
    _RequiredCreateGraphInputRequestTypeDef, _OptionalCreateGraphInputRequestTypeDef
):
    pass

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
        "vectorSearchConfiguration": "VectorSearchConfigurationTypeDef",
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGraphSnapshotInputRequestTypeDef = TypedDict(
    "_RequiredCreateGraphSnapshotInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "snapshotName": str,
    },
)
_OptionalCreateGraphSnapshotInputRequestTypeDef = TypedDict(
    "_OptionalCreateGraphSnapshotInputRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateGraphSnapshotInputRequestTypeDef(
    _RequiredCreateGraphSnapshotInputRequestTypeDef, _OptionalCreateGraphSnapshotInputRequestTypeDef
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGraphUsingImportTaskInputRequestTypeDef = TypedDict(
    "_RequiredCreateGraphUsingImportTaskInputRequestTypeDef",
    {
        "graphName": str,
        "source": str,
        "roleArn": str,
    },
)
_OptionalCreateGraphUsingImportTaskInputRequestTypeDef = TypedDict(
    "_OptionalCreateGraphUsingImportTaskInputRequestTypeDef",
    {
        "tags": Dict[str, str],
        "publicConnectivity": bool,
        "kmsKeyIdentifier": str,
        "vectorSearchConfiguration": "VectorSearchConfigurationTypeDef",
        "replicaCount": int,
        "deletionProtection": bool,
        "importOptions": "ImportOptionsTypeDef",
        "maxProvisionedMemory": int,
        "minProvisionedMemory": int,
        "failOnError": bool,
        "format": FormatType,
    },
    total=False,
)

class CreateGraphUsingImportTaskInputRequestTypeDef(
    _RequiredCreateGraphUsingImportTaskInputRequestTypeDef,
    _OptionalCreateGraphUsingImportTaskInputRequestTypeDef,
):
    pass

CreateGraphUsingImportTaskOutputTypeDef = TypedDict(
    "CreateGraphUsingImportTaskOutputTypeDef",
    {
        "graphId": str,
        "taskId": str,
        "source": str,
        "format": FormatType,
        "roleArn": str,
        "status": ImportTaskStatusType,
        "importOptions": "ImportOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePrivateGraphEndpointInputRequestTypeDef = TypedDict(
    "_RequiredCreatePrivateGraphEndpointInputRequestTypeDef",
    {
        "graphIdentifier": str,
    },
)
_OptionalCreatePrivateGraphEndpointInputRequestTypeDef = TypedDict(
    "_OptionalCreatePrivateGraphEndpointInputRequestTypeDef",
    {
        "vpcId": str,
        "subnetIds": List[str],
        "vpcSecurityGroupIds": List[str],
    },
    total=False,
)

class CreatePrivateGraphEndpointInputRequestTypeDef(
    _RequiredCreatePrivateGraphEndpointInputRequestTypeDef,
    _OptionalCreatePrivateGraphEndpointInputRequestTypeDef,
):
    pass

CreatePrivateGraphEndpointOutputTypeDef = TypedDict(
    "CreatePrivateGraphEndpointOutputTypeDef",
    {
        "vpcId": str,
        "subnetIds": List[str],
        "status": PrivateGraphEndpointStatusType,
        "vpcEndpointId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGraphInputRequestTypeDef = TypedDict(
    "DeleteGraphInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "skipSnapshot": bool,
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
        "vectorSearchConfiguration": "VectorSearchConfigurationTypeDef",
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGraphSnapshotInputRequestTypeDef = TypedDict(
    "DeleteGraphSnapshotInputRequestTypeDef",
    {
        "snapshotIdentifier": str,
    },
)

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePrivateGraphEndpointInputRequestTypeDef = TypedDict(
    "DeletePrivateGraphEndpointInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "vpcId": str,
    },
)

DeletePrivateGraphEndpointOutputTypeDef = TypedDict(
    "DeletePrivateGraphEndpointOutputTypeDef",
    {
        "vpcId": str,
        "subnetIds": List[str],
        "status": PrivateGraphEndpointStatusType,
        "vpcEndpointId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EdgeStructureTypeDef = TypedDict(
    "EdgeStructureTypeDef",
    {
        "count": int,
        "edgeProperties": List[str],
    },
    total=False,
)

_RequiredExecuteQueryInputRequestTypeDef = TypedDict(
    "_RequiredExecuteQueryInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "queryString": str,
        "language": Literal["OPEN_CYPHER"],
    },
)
_OptionalExecuteQueryInputRequestTypeDef = TypedDict(
    "_OptionalExecuteQueryInputRequestTypeDef",
    {
        "parameters": Dict[str, Dict[str, Any]],
        "planCache": PlanCacheTypeType,
        "explainMode": ExplainModeType,
        "queryTimeoutMilliseconds": int,
    },
    total=False,
)

class ExecuteQueryInputRequestTypeDef(
    _RequiredExecuteQueryInputRequestTypeDef, _OptionalExecuteQueryInputRequestTypeDef
):
    pass

ExecuteQueryOutputTypeDef = TypedDict(
    "ExecuteQueryOutputTypeDef",
    {
        "payload": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGraphInputRequestTypeDef = TypedDict(
    "GetGraphInputRequestTypeDef",
    {
        "graphIdentifier": str,
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
        "vectorSearchConfiguration": "VectorSearchConfigurationTypeDef",
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGraphSnapshotInputRequestTypeDef = TypedDict(
    "GetGraphSnapshotInputRequestTypeDef",
    {
        "snapshotIdentifier": str,
    },
)

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetGraphSummaryInputRequestTypeDef = TypedDict(
    "_RequiredGetGraphSummaryInputRequestTypeDef",
    {
        "graphIdentifier": str,
    },
)
_OptionalGetGraphSummaryInputRequestTypeDef = TypedDict(
    "_OptionalGetGraphSummaryInputRequestTypeDef",
    {
        "mode": GraphSummaryModeType,
    },
    total=False,
)

class GetGraphSummaryInputRequestTypeDef(
    _RequiredGetGraphSummaryInputRequestTypeDef, _OptionalGetGraphSummaryInputRequestTypeDef
):
    pass

GetGraphSummaryOutputTypeDef = TypedDict(
    "GetGraphSummaryOutputTypeDef",
    {
        "version": str,
        "lastStatisticsComputationTime": datetime,
        "graphSummary": "GraphDataSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportTaskInputRequestTypeDef = TypedDict(
    "GetImportTaskInputRequestTypeDef",
    {
        "taskIdentifier": str,
    },
)

GetImportTaskOutputTypeDef = TypedDict(
    "GetImportTaskOutputTypeDef",
    {
        "graphId": str,
        "taskId": str,
        "source": str,
        "format": FormatType,
        "roleArn": str,
        "status": ImportTaskStatusType,
        "importOptions": "ImportOptionsTypeDef",
        "importTaskDetails": "ImportTaskDetailsTypeDef",
        "attemptNumber": int,
        "statusReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPrivateGraphEndpointInputRequestTypeDef = TypedDict(
    "GetPrivateGraphEndpointInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "vpcId": str,
    },
)

GetPrivateGraphEndpointOutputTypeDef = TypedDict(
    "GetPrivateGraphEndpointOutputTypeDef",
    {
        "vpcId": str,
        "subnetIds": List[str],
        "status": PrivateGraphEndpointStatusType,
        "vpcEndpointId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryInputRequestTypeDef = TypedDict(
    "GetQueryInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "queryId": str,
    },
)

GetQueryOutputTypeDef = TypedDict(
    "GetQueryOutputTypeDef",
    {
        "id": str,
        "queryString": str,
        "waited": int,
        "elapsed": int,
        "state": QueryStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GraphDataSummaryTypeDef = TypedDict(
    "GraphDataSummaryTypeDef",
    {
        "numNodes": int,
        "numEdges": int,
        "numNodeLabels": int,
        "numEdgeLabels": int,
        "nodeLabels": List[str],
        "edgeLabels": List[str],
        "numNodeProperties": int,
        "numEdgeProperties": int,
        "nodeProperties": List[Dict[str, int]],
        "edgeProperties": List[Dict[str, int]],
        "totalNodePropertyValues": int,
        "totalEdgePropertyValues": int,
        "nodeStructures": List["NodeStructureTypeDef"],
        "edgeStructures": List["EdgeStructureTypeDef"],
    },
    total=False,
)

_RequiredGraphSnapshotSummaryTypeDef = TypedDict(
    "_RequiredGraphSnapshotSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
    },
)
_OptionalGraphSnapshotSummaryTypeDef = TypedDict(
    "_OptionalGraphSnapshotSummaryTypeDef",
    {
        "sourceGraphId": str,
        "snapshotCreateTime": datetime,
        "status": SnapshotStatusType,
        "kmsKeyIdentifier": str,
    },
    total=False,
)

class GraphSnapshotSummaryTypeDef(
    _RequiredGraphSnapshotSummaryTypeDef, _OptionalGraphSnapshotSummaryTypeDef
):
    pass

_RequiredGraphSummaryTypeDef = TypedDict(
    "_RequiredGraphSummaryTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
    },
)
_OptionalGraphSummaryTypeDef = TypedDict(
    "_OptionalGraphSummaryTypeDef",
    {
        "status": GraphStatusType,
        "provisionedMemory": int,
        "publicConnectivity": bool,
        "endpoint": str,
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "deletionProtection": bool,
    },
    total=False,
)

class GraphSummaryTypeDef(_RequiredGraphSummaryTypeDef, _OptionalGraphSummaryTypeDef):
    pass

ImportOptionsTypeDef = TypedDict(
    "ImportOptionsTypeDef",
    {
        "neptune": "NeptuneImportOptionsTypeDef",
    },
    total=False,
)

_RequiredImportTaskDetailsTypeDef = TypedDict(
    "_RequiredImportTaskDetailsTypeDef",
    {
        "status": str,
        "startTime": datetime,
        "timeElapsedSeconds": int,
        "progressPercentage": int,
        "errorCount": int,
        "statementCount": int,
        "dictionaryEntryCount": int,
    },
)
_OptionalImportTaskDetailsTypeDef = TypedDict(
    "_OptionalImportTaskDetailsTypeDef",
    {
        "errorDetails": str,
    },
    total=False,
)

class ImportTaskDetailsTypeDef(
    _RequiredImportTaskDetailsTypeDef, _OptionalImportTaskDetailsTypeDef
):
    pass

_RequiredImportTaskSummaryTypeDef = TypedDict(
    "_RequiredImportTaskSummaryTypeDef",
    {
        "taskId": str,
        "source": str,
        "roleArn": str,
        "status": ImportTaskStatusType,
    },
)
_OptionalImportTaskSummaryTypeDef = TypedDict(
    "_OptionalImportTaskSummaryTypeDef",
    {
        "graphId": str,
        "format": FormatType,
    },
    total=False,
)

class ImportTaskSummaryTypeDef(
    _RequiredImportTaskSummaryTypeDef, _OptionalImportTaskSummaryTypeDef
):
    pass

ListGraphSnapshotsInputRequestTypeDef = TypedDict(
    "ListGraphSnapshotsInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListGraphSnapshotsOutputTypeDef = TypedDict(
    "ListGraphSnapshotsOutputTypeDef",
    {
        "graphSnapshots": List["GraphSnapshotSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGraphsInputRequestTypeDef = TypedDict(
    "ListGraphsInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListGraphsOutputTypeDef = TypedDict(
    "ListGraphsOutputTypeDef",
    {
        "graphs": List["GraphSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImportTasksInputRequestTypeDef = TypedDict(
    "ListImportTasksInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListImportTasksOutputTypeDef = TypedDict(
    "ListImportTasksOutputTypeDef",
    {
        "tasks": List["ImportTaskSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPrivateGraphEndpointsInputRequestTypeDef = TypedDict(
    "_RequiredListPrivateGraphEndpointsInputRequestTypeDef",
    {
        "graphIdentifier": str,
    },
)
_OptionalListPrivateGraphEndpointsInputRequestTypeDef = TypedDict(
    "_OptionalListPrivateGraphEndpointsInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListPrivateGraphEndpointsInputRequestTypeDef(
    _RequiredListPrivateGraphEndpointsInputRequestTypeDef,
    _OptionalListPrivateGraphEndpointsInputRequestTypeDef,
):
    pass

ListPrivateGraphEndpointsOutputTypeDef = TypedDict(
    "ListPrivateGraphEndpointsOutputTypeDef",
    {
        "privateGraphEndpoints": List["PrivateGraphEndpointSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListQueriesInputRequestTypeDef = TypedDict(
    "_RequiredListQueriesInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "maxResults": int,
    },
)
_OptionalListQueriesInputRequestTypeDef = TypedDict(
    "_OptionalListQueriesInputRequestTypeDef",
    {
        "state": QueryStateInputType,
    },
    total=False,
)

class ListQueriesInputRequestTypeDef(
    _RequiredListQueriesInputRequestTypeDef, _OptionalListQueriesInputRequestTypeDef
):
    pass

ListQueriesOutputTypeDef = TypedDict(
    "ListQueriesOutputTypeDef",
    {
        "queries": List["QuerySummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredNeptuneImportOptionsTypeDef = TypedDict(
    "_RequiredNeptuneImportOptionsTypeDef",
    {
        "s3ExportPath": str,
        "s3ExportKmsKeyId": str,
    },
)
_OptionalNeptuneImportOptionsTypeDef = TypedDict(
    "_OptionalNeptuneImportOptionsTypeDef",
    {
        "preserveDefaultVertexLabels": bool,
        "preserveEdgeIds": bool,
    },
    total=False,
)

class NeptuneImportOptionsTypeDef(
    _RequiredNeptuneImportOptionsTypeDef, _OptionalNeptuneImportOptionsTypeDef
):
    pass

NodeStructureTypeDef = TypedDict(
    "NodeStructureTypeDef",
    {
        "count": int,
        "nodeProperties": List[str],
        "distinctOutgoingEdgeLabels": List[str],
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPrivateGraphEndpointSummaryTypeDef = TypedDict(
    "_RequiredPrivateGraphEndpointSummaryTypeDef",
    {
        "vpcId": str,
        "subnetIds": List[str],
        "status": PrivateGraphEndpointStatusType,
    },
)
_OptionalPrivateGraphEndpointSummaryTypeDef = TypedDict(
    "_OptionalPrivateGraphEndpointSummaryTypeDef",
    {
        "vpcEndpointId": str,
    },
    total=False,
)

class PrivateGraphEndpointSummaryTypeDef(
    _RequiredPrivateGraphEndpointSummaryTypeDef, _OptionalPrivateGraphEndpointSummaryTypeDef
):
    pass

QuerySummaryTypeDef = TypedDict(
    "QuerySummaryTypeDef",
    {
        "id": str,
        "queryString": str,
        "waited": int,
        "elapsed": int,
        "state": QueryStateType,
    },
    total=False,
)

ResetGraphInputRequestTypeDef = TypedDict(
    "ResetGraphInputRequestTypeDef",
    {
        "graphIdentifier": str,
        "skipSnapshot": bool,
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
        "vectorSearchConfiguration": "VectorSearchConfigurationTypeDef",
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredRestoreGraphFromSnapshotInputRequestTypeDef = TypedDict(
    "_RequiredRestoreGraphFromSnapshotInputRequestTypeDef",
    {
        "snapshotIdentifier": str,
        "graphName": str,
    },
)
_OptionalRestoreGraphFromSnapshotInputRequestTypeDef = TypedDict(
    "_OptionalRestoreGraphFromSnapshotInputRequestTypeDef",
    {
        "provisionedMemory": int,
        "deletionProtection": bool,
        "tags": Dict[str, str],
        "replicaCount": int,
        "publicConnectivity": bool,
    },
    total=False,
)

class RestoreGraphFromSnapshotInputRequestTypeDef(
    _RequiredRestoreGraphFromSnapshotInputRequestTypeDef,
    _OptionalRestoreGraphFromSnapshotInputRequestTypeDef,
):
    pass

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
        "vectorSearchConfiguration": "VectorSearchConfigurationTypeDef",
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartImportTaskInputRequestTypeDef = TypedDict(
    "_RequiredStartImportTaskInputRequestTypeDef",
    {
        "source": str,
        "graphIdentifier": str,
        "roleArn": str,
    },
)
_OptionalStartImportTaskInputRequestTypeDef = TypedDict(
    "_OptionalStartImportTaskInputRequestTypeDef",
    {
        "importOptions": "ImportOptionsTypeDef",
        "failOnError": bool,
        "format": FormatType,
    },
    total=False,
)

class StartImportTaskInputRequestTypeDef(
    _RequiredStartImportTaskInputRequestTypeDef, _OptionalStartImportTaskInputRequestTypeDef
):
    pass

StartImportTaskOutputTypeDef = TypedDict(
    "StartImportTaskOutputTypeDef",
    {
        "graphId": str,
        "taskId": str,
        "source": str,
        "format": FormatType,
        "roleArn": str,
        "status": ImportTaskStatusType,
        "importOptions": "ImportOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateGraphInputRequestTypeDef = TypedDict(
    "_RequiredUpdateGraphInputRequestTypeDef",
    {
        "graphIdentifier": str,
    },
)
_OptionalUpdateGraphInputRequestTypeDef = TypedDict(
    "_OptionalUpdateGraphInputRequestTypeDef",
    {
        "publicConnectivity": bool,
        "provisionedMemory": int,
        "deletionProtection": bool,
    },
    total=False,
)

class UpdateGraphInputRequestTypeDef(
    _RequiredUpdateGraphInputRequestTypeDef, _OptionalUpdateGraphInputRequestTypeDef
):
    pass

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
        "vectorSearchConfiguration": "VectorSearchConfigurationTypeDef",
        "replicaCount": int,
        "kmsKeyIdentifier": str,
        "sourceSnapshotId": str,
        "deletionProtection": bool,
        "buildNumber": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VectorSearchConfigurationTypeDef = TypedDict(
    "VectorSearchConfigurationTypeDef",
    {
        "dimension": int,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
