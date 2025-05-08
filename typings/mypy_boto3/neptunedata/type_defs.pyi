"""
Type annotations for neptunedata service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_neptunedata.type_defs import CancelGremlinQueryInputTypeDef

    data: CancelGremlinQueryInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any

from botocore.response import StreamingBody

from .literals import (
    ActionType,
    FormatType,
    GraphSummaryTypeType,
    IteratorTypeType,
    ModeType,
    OpenCypherExplainModeType,
    ParallelismType,
    S3BucketRegionType,
    StatisticsAutoGenerationModeType,
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
    "CancelGremlinQueryInputTypeDef",
    "CancelGremlinQueryOutputTypeDef",
    "CancelLoaderJobInputTypeDef",
    "CancelLoaderJobOutputTypeDef",
    "CancelMLDataProcessingJobInputTypeDef",
    "CancelMLDataProcessingJobOutputTypeDef",
    "CancelMLModelTrainingJobInputTypeDef",
    "CancelMLModelTrainingJobOutputTypeDef",
    "CancelMLModelTransformJobInputTypeDef",
    "CancelMLModelTransformJobOutputTypeDef",
    "CancelOpenCypherQueryInputTypeDef",
    "CancelOpenCypherQueryOutputTypeDef",
    "CreateMLEndpointInputTypeDef",
    "CreateMLEndpointOutputTypeDef",
    "CustomModelTrainingParametersTypeDef",
    "CustomModelTransformParametersTypeDef",
    "DeleteMLEndpointInputTypeDef",
    "DeleteMLEndpointOutputTypeDef",
    "DeletePropertygraphStatisticsOutputTypeDef",
    "DeleteSparqlStatisticsOutputTypeDef",
    "DeleteStatisticsValueMapTypeDef",
    "EdgeStructureTypeDef",
    "ExecuteFastResetInputTypeDef",
    "ExecuteFastResetOutputTypeDef",
    "ExecuteGremlinExplainQueryInputTypeDef",
    "ExecuteGremlinExplainQueryOutputTypeDef",
    "ExecuteGremlinProfileQueryInputTypeDef",
    "ExecuteGremlinProfileQueryOutputTypeDef",
    "ExecuteGremlinQueryInputTypeDef",
    "ExecuteGremlinQueryOutputTypeDef",
    "ExecuteOpenCypherExplainQueryInputTypeDef",
    "ExecuteOpenCypherExplainQueryOutputTypeDef",
    "ExecuteOpenCypherQueryInputTypeDef",
    "ExecuteOpenCypherQueryOutputTypeDef",
    "FastResetTokenTypeDef",
    "GetEngineStatusOutputTypeDef",
    "GetGremlinQueryStatusInputTypeDef",
    "GetGremlinQueryStatusOutputTypeDef",
    "GetLoaderJobStatusInputTypeDef",
    "GetLoaderJobStatusOutputTypeDef",
    "GetMLDataProcessingJobInputTypeDef",
    "GetMLDataProcessingJobOutputTypeDef",
    "GetMLEndpointInputTypeDef",
    "GetMLEndpointOutputTypeDef",
    "GetMLModelTrainingJobInputTypeDef",
    "GetMLModelTrainingJobOutputTypeDef",
    "GetMLModelTransformJobInputTypeDef",
    "GetMLModelTransformJobOutputTypeDef",
    "GetOpenCypherQueryStatusInputTypeDef",
    "GetOpenCypherQueryStatusOutputTypeDef",
    "GetPropertygraphStatisticsOutputTypeDef",
    "GetPropertygraphStreamInputTypeDef",
    "GetPropertygraphStreamOutputTypeDef",
    "GetPropertygraphSummaryInputTypeDef",
    "GetPropertygraphSummaryOutputTypeDef",
    "GetRDFGraphSummaryInputTypeDef",
    "GetRDFGraphSummaryOutputTypeDef",
    "GetSparqlStatisticsOutputTypeDef",
    "GetSparqlStreamInputTypeDef",
    "GetSparqlStreamOutputTypeDef",
    "GremlinQueryStatusAttributesTypeDef",
    "GremlinQueryStatusTypeDef",
    "ListGremlinQueriesInputTypeDef",
    "ListGremlinQueriesOutputTypeDef",
    "ListLoaderJobsInputTypeDef",
    "ListLoaderJobsOutputTypeDef",
    "ListMLDataProcessingJobsInputTypeDef",
    "ListMLDataProcessingJobsOutputTypeDef",
    "ListMLEndpointsInputTypeDef",
    "ListMLEndpointsOutputTypeDef",
    "ListMLModelTrainingJobsInputTypeDef",
    "ListMLModelTrainingJobsOutputTypeDef",
    "ListMLModelTransformJobsInputTypeDef",
    "ListMLModelTransformJobsOutputTypeDef",
    "ListOpenCypherQueriesInputTypeDef",
    "ListOpenCypherQueriesOutputTypeDef",
    "LoaderIdResultTypeDef",
    "ManagePropertygraphStatisticsInputTypeDef",
    "ManagePropertygraphStatisticsOutputTypeDef",
    "ManageSparqlStatisticsInputTypeDef",
    "ManageSparqlStatisticsOutputTypeDef",
    "MlConfigDefinitionTypeDef",
    "MlResourceDefinitionTypeDef",
    "NodeStructureTypeDef",
    "PropertygraphDataTypeDef",
    "PropertygraphRecordTypeDef",
    "PropertygraphSummaryTypeDef",
    "PropertygraphSummaryValueMapTypeDef",
    "QueryEvalStatsTypeDef",
    "QueryLanguageVersionTypeDef",
    "RDFGraphSummaryTypeDef",
    "RDFGraphSummaryValueMapTypeDef",
    "RefreshStatisticsIdMapTypeDef",
    "ResponseMetadataTypeDef",
    "SparqlDataTypeDef",
    "SparqlRecordTypeDef",
    "StartLoaderJobInputTypeDef",
    "StartLoaderJobOutputTypeDef",
    "StartMLDataProcessingJobInputTypeDef",
    "StartMLDataProcessingJobOutputTypeDef",
    "StartMLModelTrainingJobInputTypeDef",
    "StartMLModelTrainingJobOutputTypeDef",
    "StartMLModelTransformJobInputTypeDef",
    "StartMLModelTransformJobOutputTypeDef",
    "StatisticsSummaryTypeDef",
    "StatisticsTypeDef",
    "SubjectStructureTypeDef",
)

class CancelGremlinQueryInputTypeDef(TypedDict):
    queryId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CancelLoaderJobInputTypeDef(TypedDict):
    loadId: str

CancelMLDataProcessingJobInputTypeDef = TypedDict(
    "CancelMLDataProcessingJobInputTypeDef",
    {
        "id": str,
        "neptuneIamRoleArn": NotRequired[str],
        "clean": NotRequired[bool],
    },
)
CancelMLModelTrainingJobInputTypeDef = TypedDict(
    "CancelMLModelTrainingJobInputTypeDef",
    {
        "id": str,
        "neptuneIamRoleArn": NotRequired[str],
        "clean": NotRequired[bool],
    },
)
CancelMLModelTransformJobInputTypeDef = TypedDict(
    "CancelMLModelTransformJobInputTypeDef",
    {
        "id": str,
        "neptuneIamRoleArn": NotRequired[str],
        "clean": NotRequired[bool],
    },
)

class CancelOpenCypherQueryInputTypeDef(TypedDict):
    queryId: str
    silent: NotRequired[bool]

CreateMLEndpointInputTypeDef = TypedDict(
    "CreateMLEndpointInputTypeDef",
    {
        "id": NotRequired[str],
        "mlModelTrainingJobId": NotRequired[str],
        "mlModelTransformJobId": NotRequired[str],
        "update": NotRequired[bool],
        "neptuneIamRoleArn": NotRequired[str],
        "modelName": NotRequired[str],
        "instanceType": NotRequired[str],
        "instanceCount": NotRequired[int],
        "volumeEncryptionKMSKey": NotRequired[str],
    },
)

class CustomModelTrainingParametersTypeDef(TypedDict):
    sourceS3DirectoryPath: str
    trainingEntryPointScript: NotRequired[str]
    transformEntryPointScript: NotRequired[str]

class CustomModelTransformParametersTypeDef(TypedDict):
    sourceS3DirectoryPath: str
    transformEntryPointScript: NotRequired[str]

DeleteMLEndpointInputTypeDef = TypedDict(
    "DeleteMLEndpointInputTypeDef",
    {
        "id": str,
        "neptuneIamRoleArn": NotRequired[str],
        "clean": NotRequired[bool],
    },
)

class DeleteStatisticsValueMapTypeDef(TypedDict):
    active: NotRequired[bool]
    statisticsId: NotRequired[str]

class EdgeStructureTypeDef(TypedDict):
    count: NotRequired[int]
    edgeProperties: NotRequired[List[str]]

class ExecuteFastResetInputTypeDef(TypedDict):
    action: ActionType
    token: NotRequired[str]

class FastResetTokenTypeDef(TypedDict):
    token: NotRequired[str]

class ExecuteGremlinExplainQueryInputTypeDef(TypedDict):
    gremlinQuery: str

class ExecuteGremlinProfileQueryInputTypeDef(TypedDict):
    gremlinQuery: str
    results: NotRequired[bool]
    chop: NotRequired[int]
    serializer: NotRequired[str]
    indexOps: NotRequired[bool]

class ExecuteGremlinQueryInputTypeDef(TypedDict):
    gremlinQuery: str
    serializer: NotRequired[str]

class GremlinQueryStatusAttributesTypeDef(TypedDict):
    message: NotRequired[str]
    code: NotRequired[int]
    attributes: NotRequired[Dict[str, Any]]

class ExecuteOpenCypherExplainQueryInputTypeDef(TypedDict):
    openCypherQuery: str
    explainMode: OpenCypherExplainModeType
    parameters: NotRequired[str]

class ExecuteOpenCypherQueryInputTypeDef(TypedDict):
    openCypherQuery: str
    parameters: NotRequired[str]

class QueryLanguageVersionTypeDef(TypedDict):
    version: str

class GetGremlinQueryStatusInputTypeDef(TypedDict):
    queryId: str

class QueryEvalStatsTypeDef(TypedDict):
    waited: NotRequired[int]
    elapsed: NotRequired[int]
    cancelled: NotRequired[bool]
    subqueries: NotRequired[Dict[str, Any]]

class GetLoaderJobStatusInputTypeDef(TypedDict):
    loadId: str
    details: NotRequired[bool]
    errors: NotRequired[bool]
    page: NotRequired[int]
    errorsPerPage: NotRequired[int]

GetMLDataProcessingJobInputTypeDef = TypedDict(
    "GetMLDataProcessingJobInputTypeDef",
    {
        "id": str,
        "neptuneIamRoleArn": NotRequired[str],
    },
)

class MlResourceDefinitionTypeDef(TypedDict):
    name: NotRequired[str]
    arn: NotRequired[str]
    status: NotRequired[str]
    outputLocation: NotRequired[str]
    failureReason: NotRequired[str]
    cloudwatchLogUrl: NotRequired[str]

GetMLEndpointInputTypeDef = TypedDict(
    "GetMLEndpointInputTypeDef",
    {
        "id": str,
        "neptuneIamRoleArn": NotRequired[str],
    },
)

class MlConfigDefinitionTypeDef(TypedDict):
    name: NotRequired[str]
    arn: NotRequired[str]

GetMLModelTrainingJobInputTypeDef = TypedDict(
    "GetMLModelTrainingJobInputTypeDef",
    {
        "id": str,
        "neptuneIamRoleArn": NotRequired[str],
    },
)
GetMLModelTransformJobInputTypeDef = TypedDict(
    "GetMLModelTransformJobInputTypeDef",
    {
        "id": str,
        "neptuneIamRoleArn": NotRequired[str],
    },
)

class GetOpenCypherQueryStatusInputTypeDef(TypedDict):
    queryId: str

class GetPropertygraphStreamInputTypeDef(TypedDict):
    limit: NotRequired[int]
    iteratorType: NotRequired[IteratorTypeType]
    commitNum: NotRequired[int]
    opNum: NotRequired[int]
    encoding: NotRequired[Literal["gzip"]]

class GetPropertygraphSummaryInputTypeDef(TypedDict):
    mode: NotRequired[GraphSummaryTypeType]

class GetRDFGraphSummaryInputTypeDef(TypedDict):
    mode: NotRequired[GraphSummaryTypeType]

class GetSparqlStreamInputTypeDef(TypedDict):
    limit: NotRequired[int]
    iteratorType: NotRequired[IteratorTypeType]
    commitNum: NotRequired[int]
    opNum: NotRequired[int]
    encoding: NotRequired[Literal["gzip"]]

class ListGremlinQueriesInputTypeDef(TypedDict):
    includeWaiting: NotRequired[bool]

class ListLoaderJobsInputTypeDef(TypedDict):
    limit: NotRequired[int]
    includeQueuedLoads: NotRequired[bool]

class LoaderIdResultTypeDef(TypedDict):
    loadIds: NotRequired[List[str]]

class ListMLDataProcessingJobsInputTypeDef(TypedDict):
    maxItems: NotRequired[int]
    neptuneIamRoleArn: NotRequired[str]

class ListMLEndpointsInputTypeDef(TypedDict):
    maxItems: NotRequired[int]
    neptuneIamRoleArn: NotRequired[str]

class ListMLModelTrainingJobsInputTypeDef(TypedDict):
    maxItems: NotRequired[int]
    neptuneIamRoleArn: NotRequired[str]

class ListMLModelTransformJobsInputTypeDef(TypedDict):
    maxItems: NotRequired[int]
    neptuneIamRoleArn: NotRequired[str]

class ListOpenCypherQueriesInputTypeDef(TypedDict):
    includeWaiting: NotRequired[bool]

class ManagePropertygraphStatisticsInputTypeDef(TypedDict):
    mode: NotRequired[StatisticsAutoGenerationModeType]

class RefreshStatisticsIdMapTypeDef(TypedDict):
    statisticsId: NotRequired[str]

class ManageSparqlStatisticsInputTypeDef(TypedDict):
    mode: NotRequired[StatisticsAutoGenerationModeType]

class NodeStructureTypeDef(TypedDict):
    count: NotRequired[int]
    nodeProperties: NotRequired[List[str]]
    distinctOutgoingEdgeLabels: NotRequired[List[str]]

PropertygraphDataTypeDef = TypedDict(
    "PropertygraphDataTypeDef",
    {
        "id": str,
        "type": str,
        "key": str,
        "value": Dict[str, Any],
        "from": NotRequired[str],
        "to": NotRequired[str],
    },
)

class SubjectStructureTypeDef(TypedDict):
    count: NotRequired[int]
    predicates: NotRequired[List[str]]

class SparqlDataTypeDef(TypedDict):
    stmt: str

StartLoaderJobInputTypeDef = TypedDict(
    "StartLoaderJobInputTypeDef",
    {
        "source": str,
        "format": FormatType,
        "s3BucketRegion": S3BucketRegionType,
        "iamRoleArn": str,
        "mode": NotRequired[ModeType],
        "failOnError": NotRequired[bool],
        "parallelism": NotRequired[ParallelismType],
        "parserConfiguration": NotRequired[Mapping[str, str]],
        "updateSingleCardinalityProperties": NotRequired[bool],
        "queueRequest": NotRequired[bool],
        "dependencies": NotRequired[Sequence[str]],
        "userProvidedEdgeIds": NotRequired[bool],
    },
)
StartMLDataProcessingJobInputTypeDef = TypedDict(
    "StartMLDataProcessingJobInputTypeDef",
    {
        "inputDataS3Location": str,
        "processedDataS3Location": str,
        "id": NotRequired[str],
        "previousDataProcessingJobId": NotRequired[str],
        "sagemakerIamRoleArn": NotRequired[str],
        "neptuneIamRoleArn": NotRequired[str],
        "processingInstanceType": NotRequired[str],
        "processingInstanceVolumeSizeInGB": NotRequired[int],
        "processingTimeOutInSeconds": NotRequired[int],
        "modelType": NotRequired[str],
        "configFileName": NotRequired[str],
        "subnets": NotRequired[Sequence[str]],
        "securityGroupIds": NotRequired[Sequence[str]],
        "volumeEncryptionKMSKey": NotRequired[str],
        "s3OutputEncryptionKMSKey": NotRequired[str],
    },
)

class StatisticsSummaryTypeDef(TypedDict):
    signatureCount: NotRequired[int]
    instanceCount: NotRequired[int]
    predicateCount: NotRequired[int]

class CancelGremlinQueryOutputTypeDef(TypedDict):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelLoaderJobOutputTypeDef(TypedDict):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelMLDataProcessingJobOutputTypeDef(TypedDict):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelMLModelTrainingJobOutputTypeDef(TypedDict):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelMLModelTransformJobOutputTypeDef(TypedDict):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelOpenCypherQueryOutputTypeDef(TypedDict):
    status: str
    payload: bool
    ResponseMetadata: ResponseMetadataTypeDef

CreateMLEndpointOutputTypeDef = TypedDict(
    "CreateMLEndpointOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "creationTimeInMillis": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DeleteMLEndpointOutputTypeDef(TypedDict):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteGremlinExplainQueryOutputTypeDef(TypedDict):
    output: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteGremlinProfileQueryOutputTypeDef(TypedDict):
    output: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteOpenCypherExplainQueryOutputTypeDef(TypedDict):
    results: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteOpenCypherQueryOutputTypeDef(TypedDict):
    results: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoaderJobStatusOutputTypeDef(TypedDict):
    status: str
    payload: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMLDataProcessingJobsOutputTypeDef(TypedDict):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMLEndpointsOutputTypeDef(TypedDict):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMLModelTrainingJobsOutputTypeDef(TypedDict):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMLModelTransformJobsOutputTypeDef(TypedDict):
    ids: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartLoaderJobOutputTypeDef(TypedDict):
    status: str
    payload: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

StartMLDataProcessingJobOutputTypeDef = TypedDict(
    "StartMLDataProcessingJobOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "creationTimeInMillis": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMLModelTrainingJobOutputTypeDef = TypedDict(
    "StartMLModelTrainingJobOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "creationTimeInMillis": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMLModelTransformJobOutputTypeDef = TypedDict(
    "StartMLModelTransformJobOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "creationTimeInMillis": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartMLModelTrainingJobInputTypeDef = TypedDict(
    "StartMLModelTrainingJobInputTypeDef",
    {
        "dataProcessingJobId": str,
        "trainModelS3Location": str,
        "id": NotRequired[str],
        "previousModelTrainingJobId": NotRequired[str],
        "sagemakerIamRoleArn": NotRequired[str],
        "neptuneIamRoleArn": NotRequired[str],
        "baseProcessingInstanceType": NotRequired[str],
        "trainingInstanceType": NotRequired[str],
        "trainingInstanceVolumeSizeInGB": NotRequired[int],
        "trainingTimeOutInSeconds": NotRequired[int],
        "maxHPONumberOfTrainingJobs": NotRequired[int],
        "maxHPOParallelTrainingJobs": NotRequired[int],
        "subnets": NotRequired[Sequence[str]],
        "securityGroupIds": NotRequired[Sequence[str]],
        "volumeEncryptionKMSKey": NotRequired[str],
        "s3OutputEncryptionKMSKey": NotRequired[str],
        "enableManagedSpotTraining": NotRequired[bool],
        "customModelTrainingParameters": NotRequired[CustomModelTrainingParametersTypeDef],
    },
)
StartMLModelTransformJobInputTypeDef = TypedDict(
    "StartMLModelTransformJobInputTypeDef",
    {
        "modelTransformOutputS3Location": str,
        "id": NotRequired[str],
        "dataProcessingJobId": NotRequired[str],
        "mlModelTrainingJobId": NotRequired[str],
        "trainingJobName": NotRequired[str],
        "sagemakerIamRoleArn": NotRequired[str],
        "neptuneIamRoleArn": NotRequired[str],
        "customModelTransformParameters": NotRequired[CustomModelTransformParametersTypeDef],
        "baseProcessingInstanceType": NotRequired[str],
        "baseProcessingInstanceVolumeSizeInGB": NotRequired[int],
        "subnets": NotRequired[Sequence[str]],
        "securityGroupIds": NotRequired[Sequence[str]],
        "volumeEncryptionKMSKey": NotRequired[str],
        "s3OutputEncryptionKMSKey": NotRequired[str],
    },
)

class DeletePropertygraphStatisticsOutputTypeDef(TypedDict):
    statusCode: int
    status: str
    payload: DeleteStatisticsValueMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSparqlStatisticsOutputTypeDef(TypedDict):
    statusCode: int
    status: str
    payload: DeleteStatisticsValueMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteFastResetOutputTypeDef(TypedDict):
    status: str
    payload: FastResetTokenTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteGremlinQueryOutputTypeDef(TypedDict):
    requestId: str
    status: GremlinQueryStatusAttributesTypeDef
    result: Dict[str, Any]
    meta: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

class GetEngineStatusOutputTypeDef(TypedDict):
    status: str
    startTime: str
    dbEngineVersion: str
    role: str
    dfeQueryEngine: str
    gremlin: QueryLanguageVersionTypeDef
    sparql: QueryLanguageVersionTypeDef
    opencypher: QueryLanguageVersionTypeDef
    labMode: Dict[str, str]
    rollingBackTrxCount: int
    rollingBackTrxEarliestStartTime: str
    features: Dict[str, Dict[str, Any]]
    settings: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetGremlinQueryStatusOutputTypeDef(TypedDict):
    queryId: str
    queryString: str
    queryEvalStats: QueryEvalStatsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOpenCypherQueryStatusOutputTypeDef(TypedDict):
    queryId: str
    queryString: str
    queryEvalStats: QueryEvalStatsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GremlinQueryStatusTypeDef(TypedDict):
    queryId: NotRequired[str]
    queryString: NotRequired[str]
    queryEvalStats: NotRequired[QueryEvalStatsTypeDef]

GetMLDataProcessingJobOutputTypeDef = TypedDict(
    "GetMLDataProcessingJobOutputTypeDef",
    {
        "status": str,
        "id": str,
        "processingJob": MlResourceDefinitionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMLEndpointOutputTypeDef = TypedDict(
    "GetMLEndpointOutputTypeDef",
    {
        "status": str,
        "id": str,
        "endpoint": MlResourceDefinitionTypeDef,
        "endpointConfig": MlConfigDefinitionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMLModelTrainingJobOutputTypeDef = TypedDict(
    "GetMLModelTrainingJobOutputTypeDef",
    {
        "status": str,
        "id": str,
        "processingJob": MlResourceDefinitionTypeDef,
        "hpoJob": MlResourceDefinitionTypeDef,
        "modelTransformJob": MlResourceDefinitionTypeDef,
        "mlModels": List[MlConfigDefinitionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMLModelTransformJobOutputTypeDef = TypedDict(
    "GetMLModelTransformJobOutputTypeDef",
    {
        "status": str,
        "id": str,
        "baseProcessingJob": MlResourceDefinitionTypeDef,
        "remoteModelTransformJob": MlResourceDefinitionTypeDef,
        "models": List[MlConfigDefinitionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListLoaderJobsOutputTypeDef(TypedDict):
    status: str
    payload: LoaderIdResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ManagePropertygraphStatisticsOutputTypeDef(TypedDict):
    status: str
    payload: RefreshStatisticsIdMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ManageSparqlStatisticsOutputTypeDef(TypedDict):
    status: str
    payload: RefreshStatisticsIdMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PropertygraphSummaryTypeDef(TypedDict):
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

class PropertygraphRecordTypeDef(TypedDict):
    commitTimestampInMillis: int
    eventId: Dict[str, str]
    data: PropertygraphDataTypeDef
    op: str
    isLastOp: NotRequired[bool]

class RDFGraphSummaryTypeDef(TypedDict):
    numDistinctSubjects: NotRequired[int]
    numDistinctPredicates: NotRequired[int]
    numQuads: NotRequired[int]
    numClasses: NotRequired[int]
    classes: NotRequired[List[str]]
    predicates: NotRequired[List[Dict[str, int]]]
    subjectStructures: NotRequired[List[SubjectStructureTypeDef]]

class SparqlRecordTypeDef(TypedDict):
    commitTimestampInMillis: int
    eventId: Dict[str, str]
    data: SparqlDataTypeDef
    op: str
    isLastOp: NotRequired[bool]

class StatisticsTypeDef(TypedDict):
    autoCompute: NotRequired[bool]
    active: NotRequired[bool]
    statisticsId: NotRequired[str]
    date: NotRequired[datetime]
    note: NotRequired[str]
    signatureInfo: NotRequired[StatisticsSummaryTypeDef]

class ListGremlinQueriesOutputTypeDef(TypedDict):
    acceptedQueryCount: int
    runningQueryCount: int
    queries: List[GremlinQueryStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListOpenCypherQueriesOutputTypeDef(TypedDict):
    acceptedQueryCount: int
    runningQueryCount: int
    queries: List[GremlinQueryStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PropertygraphSummaryValueMapTypeDef(TypedDict):
    version: NotRequired[str]
    lastStatisticsComputationTime: NotRequired[datetime]
    graphSummary: NotRequired[PropertygraphSummaryTypeDef]

GetPropertygraphStreamOutputTypeDef = TypedDict(
    "GetPropertygraphStreamOutputTypeDef",
    {
        "lastEventId": Dict[str, str],
        "lastTrxTimestampInMillis": int,
        "format": str,
        "records": List[PropertygraphRecordTypeDef],
        "totalRecords": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class RDFGraphSummaryValueMapTypeDef(TypedDict):
    version: NotRequired[str]
    lastStatisticsComputationTime: NotRequired[datetime]
    graphSummary: NotRequired[RDFGraphSummaryTypeDef]

GetSparqlStreamOutputTypeDef = TypedDict(
    "GetSparqlStreamOutputTypeDef",
    {
        "lastEventId": Dict[str, str],
        "lastTrxTimestampInMillis": int,
        "format": str,
        "records": List[SparqlRecordTypeDef],
        "totalRecords": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetPropertygraphStatisticsOutputTypeDef(TypedDict):
    status: str
    payload: StatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSparqlStatisticsOutputTypeDef(TypedDict):
    status: str
    payload: StatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPropertygraphSummaryOutputTypeDef(TypedDict):
    statusCode: int
    payload: PropertygraphSummaryValueMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRDFGraphSummaryOutputTypeDef(TypedDict):
    statusCode: int
    payload: RDFGraphSummaryValueMapTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
