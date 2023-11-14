"""
Type annotations for neptunedata service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/type_defs.html)

Usage::

    ```python
    from mypy_boto3_neptunedata.type_defs import CancelGremlinQueryInputRequestTypeDef

    data: CancelGremlinQueryInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CancelGremlinQueryInputRequestTypeDef",
    "CancelGremlinQueryOutputTypeDef",
    "CancelLoaderJobInputRequestTypeDef",
    "CancelLoaderJobOutputTypeDef",
    "CancelMLDataProcessingJobInputRequestTypeDef",
    "CancelMLDataProcessingJobOutputTypeDef",
    "CancelMLModelTrainingJobInputRequestTypeDef",
    "CancelMLModelTrainingJobOutputTypeDef",
    "CancelMLModelTransformJobInputRequestTypeDef",
    "CancelMLModelTransformJobOutputTypeDef",
    "CancelOpenCypherQueryInputRequestTypeDef",
    "CancelOpenCypherQueryOutputTypeDef",
    "CreateMLEndpointInputRequestTypeDef",
    "CreateMLEndpointOutputTypeDef",
    "CustomModelTrainingParametersTypeDef",
    "CustomModelTransformParametersTypeDef",
    "DeleteMLEndpointInputRequestTypeDef",
    "DeleteMLEndpointOutputTypeDef",
    "DeletePropertygraphStatisticsOutputTypeDef",
    "DeleteSparqlStatisticsOutputTypeDef",
    "DeleteStatisticsValueMapTypeDef",
    "EdgeStructureTypeDef",
    "ExecuteFastResetInputRequestTypeDef",
    "ExecuteFastResetOutputTypeDef",
    "ExecuteGremlinExplainQueryInputRequestTypeDef",
    "ExecuteGremlinExplainQueryOutputTypeDef",
    "ExecuteGremlinProfileQueryInputRequestTypeDef",
    "ExecuteGremlinProfileQueryOutputTypeDef",
    "ExecuteGremlinQueryInputRequestTypeDef",
    "ExecuteGremlinQueryOutputTypeDef",
    "ExecuteOpenCypherExplainQueryInputRequestTypeDef",
    "ExecuteOpenCypherExplainQueryOutputTypeDef",
    "ExecuteOpenCypherQueryInputRequestTypeDef",
    "ExecuteOpenCypherQueryOutputTypeDef",
    "FastResetTokenTypeDef",
    "GetEngineStatusOutputTypeDef",
    "GetGremlinQueryStatusInputRequestTypeDef",
    "GetGremlinQueryStatusOutputTypeDef",
    "GetLoaderJobStatusInputRequestTypeDef",
    "GetLoaderJobStatusOutputTypeDef",
    "GetMLDataProcessingJobInputRequestTypeDef",
    "GetMLDataProcessingJobOutputTypeDef",
    "GetMLEndpointInputRequestTypeDef",
    "GetMLEndpointOutputTypeDef",
    "GetMLModelTrainingJobInputRequestTypeDef",
    "GetMLModelTrainingJobOutputTypeDef",
    "GetMLModelTransformJobInputRequestTypeDef",
    "GetMLModelTransformJobOutputTypeDef",
    "GetOpenCypherQueryStatusInputRequestTypeDef",
    "GetOpenCypherQueryStatusOutputTypeDef",
    "GetPropertygraphStatisticsOutputTypeDef",
    "GetPropertygraphStreamInputRequestTypeDef",
    "GetPropertygraphStreamOutputTypeDef",
    "GetPropertygraphSummaryInputRequestTypeDef",
    "GetPropertygraphSummaryOutputTypeDef",
    "GetRDFGraphSummaryInputRequestTypeDef",
    "GetRDFGraphSummaryOutputTypeDef",
    "GetSparqlStatisticsOutputTypeDef",
    "GetSparqlStreamInputRequestTypeDef",
    "GetSparqlStreamOutputTypeDef",
    "GremlinQueryStatusAttributesTypeDef",
    "GremlinQueryStatusTypeDef",
    "ListGremlinQueriesInputRequestTypeDef",
    "ListGremlinQueriesOutputTypeDef",
    "ListLoaderJobsInputRequestTypeDef",
    "ListLoaderJobsOutputTypeDef",
    "ListMLDataProcessingJobsInputRequestTypeDef",
    "ListMLDataProcessingJobsOutputTypeDef",
    "ListMLEndpointsInputRequestTypeDef",
    "ListMLEndpointsOutputTypeDef",
    "ListMLModelTrainingJobsInputRequestTypeDef",
    "ListMLModelTrainingJobsOutputTypeDef",
    "ListMLModelTransformJobsInputRequestTypeDef",
    "ListMLModelTransformJobsOutputTypeDef",
    "ListOpenCypherQueriesInputRequestTypeDef",
    "ListOpenCypherQueriesOutputTypeDef",
    "LoaderIdResultTypeDef",
    "ManagePropertygraphStatisticsInputRequestTypeDef",
    "ManagePropertygraphStatisticsOutputTypeDef",
    "ManageSparqlStatisticsInputRequestTypeDef",
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
    "StartLoaderJobInputRequestTypeDef",
    "StartLoaderJobOutputTypeDef",
    "StartMLDataProcessingJobInputRequestTypeDef",
    "StartMLDataProcessingJobOutputTypeDef",
    "StartMLModelTrainingJobInputRequestTypeDef",
    "StartMLModelTrainingJobOutputTypeDef",
    "StartMLModelTransformJobInputRequestTypeDef",
    "StartMLModelTransformJobOutputTypeDef",
    "StatisticsSummaryTypeDef",
    "StatisticsTypeDef",
    "SubjectStructureTypeDef",
)

CancelGremlinQueryInputRequestTypeDef = TypedDict(
    "CancelGremlinQueryInputRequestTypeDef",
    {
        "queryId": str,
    },
)

CancelGremlinQueryOutputTypeDef = TypedDict(
    "CancelGremlinQueryOutputTypeDef",
    {
        "status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelLoaderJobInputRequestTypeDef = TypedDict(
    "CancelLoaderJobInputRequestTypeDef",
    {
        "loadId": str,
    },
)

CancelLoaderJobOutputTypeDef = TypedDict(
    "CancelLoaderJobOutputTypeDef",
    {
        "status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCancelMLDataProcessingJobInputRequestTypeDef = TypedDict(
    "_RequiredCancelMLDataProcessingJobInputRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalCancelMLDataProcessingJobInputRequestTypeDef = TypedDict(
    "_OptionalCancelMLDataProcessingJobInputRequestTypeDef",
    {
        "neptuneIamRoleArn": str,
        "clean": bool,
    },
    total=False,
)

class CancelMLDataProcessingJobInputRequestTypeDef(
    _RequiredCancelMLDataProcessingJobInputRequestTypeDef,
    _OptionalCancelMLDataProcessingJobInputRequestTypeDef,
):
    pass

CancelMLDataProcessingJobOutputTypeDef = TypedDict(
    "CancelMLDataProcessingJobOutputTypeDef",
    {
        "status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCancelMLModelTrainingJobInputRequestTypeDef = TypedDict(
    "_RequiredCancelMLModelTrainingJobInputRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalCancelMLModelTrainingJobInputRequestTypeDef = TypedDict(
    "_OptionalCancelMLModelTrainingJobInputRequestTypeDef",
    {
        "neptuneIamRoleArn": str,
        "clean": bool,
    },
    total=False,
)

class CancelMLModelTrainingJobInputRequestTypeDef(
    _RequiredCancelMLModelTrainingJobInputRequestTypeDef,
    _OptionalCancelMLModelTrainingJobInputRequestTypeDef,
):
    pass

CancelMLModelTrainingJobOutputTypeDef = TypedDict(
    "CancelMLModelTrainingJobOutputTypeDef",
    {
        "status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCancelMLModelTransformJobInputRequestTypeDef = TypedDict(
    "_RequiredCancelMLModelTransformJobInputRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalCancelMLModelTransformJobInputRequestTypeDef = TypedDict(
    "_OptionalCancelMLModelTransformJobInputRequestTypeDef",
    {
        "neptuneIamRoleArn": str,
        "clean": bool,
    },
    total=False,
)

class CancelMLModelTransformJobInputRequestTypeDef(
    _RequiredCancelMLModelTransformJobInputRequestTypeDef,
    _OptionalCancelMLModelTransformJobInputRequestTypeDef,
):
    pass

CancelMLModelTransformJobOutputTypeDef = TypedDict(
    "CancelMLModelTransformJobOutputTypeDef",
    {
        "status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCancelOpenCypherQueryInputRequestTypeDef = TypedDict(
    "_RequiredCancelOpenCypherQueryInputRequestTypeDef",
    {
        "queryId": str,
    },
)
_OptionalCancelOpenCypherQueryInputRequestTypeDef = TypedDict(
    "_OptionalCancelOpenCypherQueryInputRequestTypeDef",
    {
        "silent": bool,
    },
    total=False,
)

class CancelOpenCypherQueryInputRequestTypeDef(
    _RequiredCancelOpenCypherQueryInputRequestTypeDef,
    _OptionalCancelOpenCypherQueryInputRequestTypeDef,
):
    pass

CancelOpenCypherQueryOutputTypeDef = TypedDict(
    "CancelOpenCypherQueryOutputTypeDef",
    {
        "status": str,
        "payload": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMLEndpointInputRequestTypeDef = TypedDict(
    "CreateMLEndpointInputRequestTypeDef",
    {
        "id": str,
        "mlModelTrainingJobId": str,
        "mlModelTransformJobId": str,
        "update": bool,
        "neptuneIamRoleArn": str,
        "modelName": str,
        "instanceType": str,
        "instanceCount": int,
        "volumeEncryptionKMSKey": str,
    },
    total=False,
)

CreateMLEndpointOutputTypeDef = TypedDict(
    "CreateMLEndpointOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "creationTimeInMillis": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomModelTrainingParametersTypeDef = TypedDict(
    "_RequiredCustomModelTrainingParametersTypeDef",
    {
        "sourceS3DirectoryPath": str,
    },
)
_OptionalCustomModelTrainingParametersTypeDef = TypedDict(
    "_OptionalCustomModelTrainingParametersTypeDef",
    {
        "trainingEntryPointScript": str,
        "transformEntryPointScript": str,
    },
    total=False,
)

class CustomModelTrainingParametersTypeDef(
    _RequiredCustomModelTrainingParametersTypeDef, _OptionalCustomModelTrainingParametersTypeDef
):
    pass

_RequiredCustomModelTransformParametersTypeDef = TypedDict(
    "_RequiredCustomModelTransformParametersTypeDef",
    {
        "sourceS3DirectoryPath": str,
    },
)
_OptionalCustomModelTransformParametersTypeDef = TypedDict(
    "_OptionalCustomModelTransformParametersTypeDef",
    {
        "transformEntryPointScript": str,
    },
    total=False,
)

class CustomModelTransformParametersTypeDef(
    _RequiredCustomModelTransformParametersTypeDef, _OptionalCustomModelTransformParametersTypeDef
):
    pass

_RequiredDeleteMLEndpointInputRequestTypeDef = TypedDict(
    "_RequiredDeleteMLEndpointInputRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalDeleteMLEndpointInputRequestTypeDef = TypedDict(
    "_OptionalDeleteMLEndpointInputRequestTypeDef",
    {
        "neptuneIamRoleArn": str,
        "clean": bool,
    },
    total=False,
)

class DeleteMLEndpointInputRequestTypeDef(
    _RequiredDeleteMLEndpointInputRequestTypeDef, _OptionalDeleteMLEndpointInputRequestTypeDef
):
    pass

DeleteMLEndpointOutputTypeDef = TypedDict(
    "DeleteMLEndpointOutputTypeDef",
    {
        "status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePropertygraphStatisticsOutputTypeDef = TypedDict(
    "DeletePropertygraphStatisticsOutputTypeDef",
    {
        "statusCode": int,
        "status": str,
        "payload": "DeleteStatisticsValueMapTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSparqlStatisticsOutputTypeDef = TypedDict(
    "DeleteSparqlStatisticsOutputTypeDef",
    {
        "statusCode": int,
        "status": str,
        "payload": "DeleteStatisticsValueMapTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteStatisticsValueMapTypeDef = TypedDict(
    "DeleteStatisticsValueMapTypeDef",
    {
        "active": bool,
        "statisticsId": str,
    },
    total=False,
)

EdgeStructureTypeDef = TypedDict(
    "EdgeStructureTypeDef",
    {
        "count": int,
        "edgeProperties": List[str],
    },
    total=False,
)

_RequiredExecuteFastResetInputRequestTypeDef = TypedDict(
    "_RequiredExecuteFastResetInputRequestTypeDef",
    {
        "action": ActionType,
    },
)
_OptionalExecuteFastResetInputRequestTypeDef = TypedDict(
    "_OptionalExecuteFastResetInputRequestTypeDef",
    {
        "token": str,
    },
    total=False,
)

class ExecuteFastResetInputRequestTypeDef(
    _RequiredExecuteFastResetInputRequestTypeDef, _OptionalExecuteFastResetInputRequestTypeDef
):
    pass

ExecuteFastResetOutputTypeDef = TypedDict(
    "ExecuteFastResetOutputTypeDef",
    {
        "status": str,
        "payload": "FastResetTokenTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecuteGremlinExplainQueryInputRequestTypeDef = TypedDict(
    "ExecuteGremlinExplainQueryInputRequestTypeDef",
    {
        "gremlinQuery": str,
    },
)

ExecuteGremlinExplainQueryOutputTypeDef = TypedDict(
    "ExecuteGremlinExplainQueryOutputTypeDef",
    {
        "output": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteGremlinProfileQueryInputRequestTypeDef = TypedDict(
    "_RequiredExecuteGremlinProfileQueryInputRequestTypeDef",
    {
        "gremlinQuery": str,
    },
)
_OptionalExecuteGremlinProfileQueryInputRequestTypeDef = TypedDict(
    "_OptionalExecuteGremlinProfileQueryInputRequestTypeDef",
    {
        "results": bool,
        "chop": int,
        "serializer": str,
        "indexOps": bool,
    },
    total=False,
)

class ExecuteGremlinProfileQueryInputRequestTypeDef(
    _RequiredExecuteGremlinProfileQueryInputRequestTypeDef,
    _OptionalExecuteGremlinProfileQueryInputRequestTypeDef,
):
    pass

ExecuteGremlinProfileQueryOutputTypeDef = TypedDict(
    "ExecuteGremlinProfileQueryOutputTypeDef",
    {
        "output": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteGremlinQueryInputRequestTypeDef = TypedDict(
    "_RequiredExecuteGremlinQueryInputRequestTypeDef",
    {
        "gremlinQuery": str,
    },
)
_OptionalExecuteGremlinQueryInputRequestTypeDef = TypedDict(
    "_OptionalExecuteGremlinQueryInputRequestTypeDef",
    {
        "serializer": str,
    },
    total=False,
)

class ExecuteGremlinQueryInputRequestTypeDef(
    _RequiredExecuteGremlinQueryInputRequestTypeDef, _OptionalExecuteGremlinQueryInputRequestTypeDef
):
    pass

ExecuteGremlinQueryOutputTypeDef = TypedDict(
    "ExecuteGremlinQueryOutputTypeDef",
    {
        "requestId": str,
        "status": "GremlinQueryStatusAttributesTypeDef",
        "result": Dict[str, Any],
        "meta": Dict[str, Any],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteOpenCypherExplainQueryInputRequestTypeDef = TypedDict(
    "_RequiredExecuteOpenCypherExplainQueryInputRequestTypeDef",
    {
        "openCypherQuery": str,
        "explainMode": OpenCypherExplainModeType,
    },
)
_OptionalExecuteOpenCypherExplainQueryInputRequestTypeDef = TypedDict(
    "_OptionalExecuteOpenCypherExplainQueryInputRequestTypeDef",
    {
        "parameters": str,
    },
    total=False,
)

class ExecuteOpenCypherExplainQueryInputRequestTypeDef(
    _RequiredExecuteOpenCypherExplainQueryInputRequestTypeDef,
    _OptionalExecuteOpenCypherExplainQueryInputRequestTypeDef,
):
    pass

ExecuteOpenCypherExplainQueryOutputTypeDef = TypedDict(
    "ExecuteOpenCypherExplainQueryOutputTypeDef",
    {
        "results": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExecuteOpenCypherQueryInputRequestTypeDef = TypedDict(
    "_RequiredExecuteOpenCypherQueryInputRequestTypeDef",
    {
        "openCypherQuery": str,
    },
)
_OptionalExecuteOpenCypherQueryInputRequestTypeDef = TypedDict(
    "_OptionalExecuteOpenCypherQueryInputRequestTypeDef",
    {
        "parameters": str,
    },
    total=False,
)

class ExecuteOpenCypherQueryInputRequestTypeDef(
    _RequiredExecuteOpenCypherQueryInputRequestTypeDef,
    _OptionalExecuteOpenCypherQueryInputRequestTypeDef,
):
    pass

ExecuteOpenCypherQueryOutputTypeDef = TypedDict(
    "ExecuteOpenCypherQueryOutputTypeDef",
    {
        "results": Dict[str, Any],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FastResetTokenTypeDef = TypedDict(
    "FastResetTokenTypeDef",
    {
        "token": str,
    },
    total=False,
)

GetEngineStatusOutputTypeDef = TypedDict(
    "GetEngineStatusOutputTypeDef",
    {
        "status": str,
        "startTime": str,
        "dbEngineVersion": str,
        "role": str,
        "dfeQueryEngine": str,
        "gremlin": "QueryLanguageVersionTypeDef",
        "sparql": "QueryLanguageVersionTypeDef",
        "opencypher": "QueryLanguageVersionTypeDef",
        "labMode": Dict[str, str],
        "rollingBackTrxCount": int,
        "rollingBackTrxEarliestStartTime": str,
        "features": Dict[str, Dict[str, Any]],
        "settings": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGremlinQueryStatusInputRequestTypeDef = TypedDict(
    "GetGremlinQueryStatusInputRequestTypeDef",
    {
        "queryId": str,
    },
)

GetGremlinQueryStatusOutputTypeDef = TypedDict(
    "GetGremlinQueryStatusOutputTypeDef",
    {
        "queryId": str,
        "queryString": str,
        "queryEvalStats": "QueryEvalStatsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLoaderJobStatusInputRequestTypeDef = TypedDict(
    "_RequiredGetLoaderJobStatusInputRequestTypeDef",
    {
        "loadId": str,
    },
)
_OptionalGetLoaderJobStatusInputRequestTypeDef = TypedDict(
    "_OptionalGetLoaderJobStatusInputRequestTypeDef",
    {
        "details": bool,
        "errors": bool,
        "page": int,
        "errorsPerPage": int,
    },
    total=False,
)

class GetLoaderJobStatusInputRequestTypeDef(
    _RequiredGetLoaderJobStatusInputRequestTypeDef, _OptionalGetLoaderJobStatusInputRequestTypeDef
):
    pass

GetLoaderJobStatusOutputTypeDef = TypedDict(
    "GetLoaderJobStatusOutputTypeDef",
    {
        "status": str,
        "payload": Dict[str, Any],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMLDataProcessingJobInputRequestTypeDef = TypedDict(
    "_RequiredGetMLDataProcessingJobInputRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalGetMLDataProcessingJobInputRequestTypeDef = TypedDict(
    "_OptionalGetMLDataProcessingJobInputRequestTypeDef",
    {
        "neptuneIamRoleArn": str,
    },
    total=False,
)

class GetMLDataProcessingJobInputRequestTypeDef(
    _RequiredGetMLDataProcessingJobInputRequestTypeDef,
    _OptionalGetMLDataProcessingJobInputRequestTypeDef,
):
    pass

GetMLDataProcessingJobOutputTypeDef = TypedDict(
    "GetMLDataProcessingJobOutputTypeDef",
    {
        "status": str,
        "id": str,
        "processingJob": "MlResourceDefinitionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMLEndpointInputRequestTypeDef = TypedDict(
    "_RequiredGetMLEndpointInputRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalGetMLEndpointInputRequestTypeDef = TypedDict(
    "_OptionalGetMLEndpointInputRequestTypeDef",
    {
        "neptuneIamRoleArn": str,
    },
    total=False,
)

class GetMLEndpointInputRequestTypeDef(
    _RequiredGetMLEndpointInputRequestTypeDef, _OptionalGetMLEndpointInputRequestTypeDef
):
    pass

GetMLEndpointOutputTypeDef = TypedDict(
    "GetMLEndpointOutputTypeDef",
    {
        "status": str,
        "id": str,
        "endpoint": "MlResourceDefinitionTypeDef",
        "endpointConfig": "MlConfigDefinitionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMLModelTrainingJobInputRequestTypeDef = TypedDict(
    "_RequiredGetMLModelTrainingJobInputRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalGetMLModelTrainingJobInputRequestTypeDef = TypedDict(
    "_OptionalGetMLModelTrainingJobInputRequestTypeDef",
    {
        "neptuneIamRoleArn": str,
    },
    total=False,
)

class GetMLModelTrainingJobInputRequestTypeDef(
    _RequiredGetMLModelTrainingJobInputRequestTypeDef,
    _OptionalGetMLModelTrainingJobInputRequestTypeDef,
):
    pass

GetMLModelTrainingJobOutputTypeDef = TypedDict(
    "GetMLModelTrainingJobOutputTypeDef",
    {
        "status": str,
        "id": str,
        "processingJob": "MlResourceDefinitionTypeDef",
        "hpoJob": "MlResourceDefinitionTypeDef",
        "modelTransformJob": "MlResourceDefinitionTypeDef",
        "mlModels": List["MlConfigDefinitionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMLModelTransformJobInputRequestTypeDef = TypedDict(
    "_RequiredGetMLModelTransformJobInputRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalGetMLModelTransformJobInputRequestTypeDef = TypedDict(
    "_OptionalGetMLModelTransformJobInputRequestTypeDef",
    {
        "neptuneIamRoleArn": str,
    },
    total=False,
)

class GetMLModelTransformJobInputRequestTypeDef(
    _RequiredGetMLModelTransformJobInputRequestTypeDef,
    _OptionalGetMLModelTransformJobInputRequestTypeDef,
):
    pass

GetMLModelTransformJobOutputTypeDef = TypedDict(
    "GetMLModelTransformJobOutputTypeDef",
    {
        "status": str,
        "id": str,
        "baseProcessingJob": "MlResourceDefinitionTypeDef",
        "remoteModelTransformJob": "MlResourceDefinitionTypeDef",
        "models": List["MlConfigDefinitionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOpenCypherQueryStatusInputRequestTypeDef = TypedDict(
    "GetOpenCypherQueryStatusInputRequestTypeDef",
    {
        "queryId": str,
    },
)

GetOpenCypherQueryStatusOutputTypeDef = TypedDict(
    "GetOpenCypherQueryStatusOutputTypeDef",
    {
        "queryId": str,
        "queryString": str,
        "queryEvalStats": "QueryEvalStatsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPropertygraphStatisticsOutputTypeDef = TypedDict(
    "GetPropertygraphStatisticsOutputTypeDef",
    {
        "status": str,
        "payload": "StatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPropertygraphStreamInputRequestTypeDef = TypedDict(
    "GetPropertygraphStreamInputRequestTypeDef",
    {
        "limit": int,
        "iteratorType": IteratorTypeType,
        "commitNum": int,
        "opNum": int,
        "encoding": Literal["gzip"],
    },
    total=False,
)

GetPropertygraphStreamOutputTypeDef = TypedDict(
    "GetPropertygraphStreamOutputTypeDef",
    {
        "lastEventId": Dict[str, str],
        "lastTrxTimestampInMillis": int,
        "format": str,
        "records": List["PropertygraphRecordTypeDef"],
        "totalRecords": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPropertygraphSummaryInputRequestTypeDef = TypedDict(
    "GetPropertygraphSummaryInputRequestTypeDef",
    {
        "mode": GraphSummaryTypeType,
    },
    total=False,
)

GetPropertygraphSummaryOutputTypeDef = TypedDict(
    "GetPropertygraphSummaryOutputTypeDef",
    {
        "statusCode": int,
        "payload": "PropertygraphSummaryValueMapTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRDFGraphSummaryInputRequestTypeDef = TypedDict(
    "GetRDFGraphSummaryInputRequestTypeDef",
    {
        "mode": GraphSummaryTypeType,
    },
    total=False,
)

GetRDFGraphSummaryOutputTypeDef = TypedDict(
    "GetRDFGraphSummaryOutputTypeDef",
    {
        "statusCode": int,
        "payload": "RDFGraphSummaryValueMapTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSparqlStatisticsOutputTypeDef = TypedDict(
    "GetSparqlStatisticsOutputTypeDef",
    {
        "status": str,
        "payload": "StatisticsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSparqlStreamInputRequestTypeDef = TypedDict(
    "GetSparqlStreamInputRequestTypeDef",
    {
        "limit": int,
        "iteratorType": IteratorTypeType,
        "commitNum": int,
        "opNum": int,
        "encoding": Literal["gzip"],
    },
    total=False,
)

GetSparqlStreamOutputTypeDef = TypedDict(
    "GetSparqlStreamOutputTypeDef",
    {
        "lastEventId": Dict[str, str],
        "lastTrxTimestampInMillis": int,
        "format": str,
        "records": List["SparqlRecordTypeDef"],
        "totalRecords": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GremlinQueryStatusAttributesTypeDef = TypedDict(
    "GremlinQueryStatusAttributesTypeDef",
    {
        "message": str,
        "code": int,
        "attributes": Dict[str, Any],
    },
    total=False,
)

GremlinQueryStatusTypeDef = TypedDict(
    "GremlinQueryStatusTypeDef",
    {
        "queryId": str,
        "queryString": str,
        "queryEvalStats": "QueryEvalStatsTypeDef",
    },
    total=False,
)

ListGremlinQueriesInputRequestTypeDef = TypedDict(
    "ListGremlinQueriesInputRequestTypeDef",
    {
        "includeWaiting": bool,
    },
    total=False,
)

ListGremlinQueriesOutputTypeDef = TypedDict(
    "ListGremlinQueriesOutputTypeDef",
    {
        "acceptedQueryCount": int,
        "runningQueryCount": int,
        "queries": List["GremlinQueryStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLoaderJobsInputRequestTypeDef = TypedDict(
    "ListLoaderJobsInputRequestTypeDef",
    {
        "limit": int,
        "includeQueuedLoads": bool,
    },
    total=False,
)

ListLoaderJobsOutputTypeDef = TypedDict(
    "ListLoaderJobsOutputTypeDef",
    {
        "status": str,
        "payload": "LoaderIdResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMLDataProcessingJobsInputRequestTypeDef = TypedDict(
    "ListMLDataProcessingJobsInputRequestTypeDef",
    {
        "maxItems": int,
        "neptuneIamRoleArn": str,
    },
    total=False,
)

ListMLDataProcessingJobsOutputTypeDef = TypedDict(
    "ListMLDataProcessingJobsOutputTypeDef",
    {
        "ids": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMLEndpointsInputRequestTypeDef = TypedDict(
    "ListMLEndpointsInputRequestTypeDef",
    {
        "maxItems": int,
        "neptuneIamRoleArn": str,
    },
    total=False,
)

ListMLEndpointsOutputTypeDef = TypedDict(
    "ListMLEndpointsOutputTypeDef",
    {
        "ids": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMLModelTrainingJobsInputRequestTypeDef = TypedDict(
    "ListMLModelTrainingJobsInputRequestTypeDef",
    {
        "maxItems": int,
        "neptuneIamRoleArn": str,
    },
    total=False,
)

ListMLModelTrainingJobsOutputTypeDef = TypedDict(
    "ListMLModelTrainingJobsOutputTypeDef",
    {
        "ids": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMLModelTransformJobsInputRequestTypeDef = TypedDict(
    "ListMLModelTransformJobsInputRequestTypeDef",
    {
        "maxItems": int,
        "neptuneIamRoleArn": str,
    },
    total=False,
)

ListMLModelTransformJobsOutputTypeDef = TypedDict(
    "ListMLModelTransformJobsOutputTypeDef",
    {
        "ids": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOpenCypherQueriesInputRequestTypeDef = TypedDict(
    "ListOpenCypherQueriesInputRequestTypeDef",
    {
        "includeWaiting": bool,
    },
    total=False,
)

ListOpenCypherQueriesOutputTypeDef = TypedDict(
    "ListOpenCypherQueriesOutputTypeDef",
    {
        "acceptedQueryCount": int,
        "runningQueryCount": int,
        "queries": List["GremlinQueryStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoaderIdResultTypeDef = TypedDict(
    "LoaderIdResultTypeDef",
    {
        "loadIds": List[str],
    },
    total=False,
)

ManagePropertygraphStatisticsInputRequestTypeDef = TypedDict(
    "ManagePropertygraphStatisticsInputRequestTypeDef",
    {
        "mode": StatisticsAutoGenerationModeType,
    },
    total=False,
)

ManagePropertygraphStatisticsOutputTypeDef = TypedDict(
    "ManagePropertygraphStatisticsOutputTypeDef",
    {
        "status": str,
        "payload": "RefreshStatisticsIdMapTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManageSparqlStatisticsInputRequestTypeDef = TypedDict(
    "ManageSparqlStatisticsInputRequestTypeDef",
    {
        "mode": StatisticsAutoGenerationModeType,
    },
    total=False,
)

ManageSparqlStatisticsOutputTypeDef = TypedDict(
    "ManageSparqlStatisticsOutputTypeDef",
    {
        "status": str,
        "payload": "RefreshStatisticsIdMapTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MlConfigDefinitionTypeDef = TypedDict(
    "MlConfigDefinitionTypeDef",
    {
        "name": str,
        "arn": str,
    },
    total=False,
)

MlResourceDefinitionTypeDef = TypedDict(
    "MlResourceDefinitionTypeDef",
    {
        "name": str,
        "arn": str,
        "status": str,
        "outputLocation": str,
        "failureReason": str,
        "cloudwatchLogUrl": str,
    },
    total=False,
)

NodeStructureTypeDef = TypedDict(
    "NodeStructureTypeDef",
    {
        "count": int,
        "nodeProperties": List[str],
        "distinctOutgoingEdgeLabels": List[str],
    },
    total=False,
)

_RequiredPropertygraphDataTypeDef = TypedDict(
    "_RequiredPropertygraphDataTypeDef",
    {
        "id": str,
        "type": str,
        "key": str,
        "value": Dict[str, Any],
    },
)
_OptionalPropertygraphDataTypeDef = TypedDict(
    "_OptionalPropertygraphDataTypeDef",
    {
        "from": str,
        "to": str,
    },
    total=False,
)

class PropertygraphDataTypeDef(
    _RequiredPropertygraphDataTypeDef, _OptionalPropertygraphDataTypeDef
):
    pass

_RequiredPropertygraphRecordTypeDef = TypedDict(
    "_RequiredPropertygraphRecordTypeDef",
    {
        "commitTimestampInMillis": int,
        "eventId": Dict[str, str],
        "data": "PropertygraphDataTypeDef",
        "op": str,
    },
)
_OptionalPropertygraphRecordTypeDef = TypedDict(
    "_OptionalPropertygraphRecordTypeDef",
    {
        "isLastOp": bool,
    },
    total=False,
)

class PropertygraphRecordTypeDef(
    _RequiredPropertygraphRecordTypeDef, _OptionalPropertygraphRecordTypeDef
):
    pass

PropertygraphSummaryTypeDef = TypedDict(
    "PropertygraphSummaryTypeDef",
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

PropertygraphSummaryValueMapTypeDef = TypedDict(
    "PropertygraphSummaryValueMapTypeDef",
    {
        "version": str,
        "lastStatisticsComputationTime": datetime,
        "graphSummary": "PropertygraphSummaryTypeDef",
    },
    total=False,
)

QueryEvalStatsTypeDef = TypedDict(
    "QueryEvalStatsTypeDef",
    {
        "waited": int,
        "elapsed": int,
        "cancelled": bool,
        "subqueries": Dict[str, Any],
    },
    total=False,
)

QueryLanguageVersionTypeDef = TypedDict(
    "QueryLanguageVersionTypeDef",
    {
        "version": str,
    },
)

RDFGraphSummaryTypeDef = TypedDict(
    "RDFGraphSummaryTypeDef",
    {
        "numDistinctSubjects": int,
        "numDistinctPredicates": int,
        "numQuads": int,
        "numClasses": int,
        "classes": List[str],
        "predicates": List[Dict[str, int]],
        "subjectStructures": List["SubjectStructureTypeDef"],
    },
    total=False,
)

RDFGraphSummaryValueMapTypeDef = TypedDict(
    "RDFGraphSummaryValueMapTypeDef",
    {
        "version": str,
        "lastStatisticsComputationTime": datetime,
        "graphSummary": "RDFGraphSummaryTypeDef",
    },
    total=False,
)

RefreshStatisticsIdMapTypeDef = TypedDict(
    "RefreshStatisticsIdMapTypeDef",
    {
        "statisticsId": str,
    },
    total=False,
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

SparqlDataTypeDef = TypedDict(
    "SparqlDataTypeDef",
    {
        "stmt": str,
    },
)

_RequiredSparqlRecordTypeDef = TypedDict(
    "_RequiredSparqlRecordTypeDef",
    {
        "commitTimestampInMillis": int,
        "eventId": Dict[str, str],
        "data": "SparqlDataTypeDef",
        "op": str,
    },
)
_OptionalSparqlRecordTypeDef = TypedDict(
    "_OptionalSparqlRecordTypeDef",
    {
        "isLastOp": bool,
    },
    total=False,
)

class SparqlRecordTypeDef(_RequiredSparqlRecordTypeDef, _OptionalSparqlRecordTypeDef):
    pass

_RequiredStartLoaderJobInputRequestTypeDef = TypedDict(
    "_RequiredStartLoaderJobInputRequestTypeDef",
    {
        "source": str,
        "format": FormatType,
        "s3BucketRegion": S3BucketRegionType,
        "iamRoleArn": str,
    },
)
_OptionalStartLoaderJobInputRequestTypeDef = TypedDict(
    "_OptionalStartLoaderJobInputRequestTypeDef",
    {
        "mode": ModeType,
        "failOnError": bool,
        "parallelism": ParallelismType,
        "parserConfiguration": Dict[str, str],
        "updateSingleCardinalityProperties": bool,
        "queueRequest": bool,
        "dependencies": List[str],
        "userProvidedEdgeIds": bool,
    },
    total=False,
)

class StartLoaderJobInputRequestTypeDef(
    _RequiredStartLoaderJobInputRequestTypeDef, _OptionalStartLoaderJobInputRequestTypeDef
):
    pass

StartLoaderJobOutputTypeDef = TypedDict(
    "StartLoaderJobOutputTypeDef",
    {
        "status": str,
        "payload": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartMLDataProcessingJobInputRequestTypeDef = TypedDict(
    "_RequiredStartMLDataProcessingJobInputRequestTypeDef",
    {
        "inputDataS3Location": str,
        "processedDataS3Location": str,
    },
)
_OptionalStartMLDataProcessingJobInputRequestTypeDef = TypedDict(
    "_OptionalStartMLDataProcessingJobInputRequestTypeDef",
    {
        "id": str,
        "previousDataProcessingJobId": str,
        "sagemakerIamRoleArn": str,
        "neptuneIamRoleArn": str,
        "processingInstanceType": str,
        "processingInstanceVolumeSizeInGB": int,
        "processingTimeOutInSeconds": int,
        "modelType": str,
        "configFileName": str,
        "subnets": List[str],
        "securityGroupIds": List[str],
        "volumeEncryptionKMSKey": str,
        "s3OutputEncryptionKMSKey": str,
    },
    total=False,
)

class StartMLDataProcessingJobInputRequestTypeDef(
    _RequiredStartMLDataProcessingJobInputRequestTypeDef,
    _OptionalStartMLDataProcessingJobInputRequestTypeDef,
):
    pass

StartMLDataProcessingJobOutputTypeDef = TypedDict(
    "StartMLDataProcessingJobOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "creationTimeInMillis": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartMLModelTrainingJobInputRequestTypeDef = TypedDict(
    "_RequiredStartMLModelTrainingJobInputRequestTypeDef",
    {
        "dataProcessingJobId": str,
        "trainModelS3Location": str,
    },
)
_OptionalStartMLModelTrainingJobInputRequestTypeDef = TypedDict(
    "_OptionalStartMLModelTrainingJobInputRequestTypeDef",
    {
        "id": str,
        "previousModelTrainingJobId": str,
        "sagemakerIamRoleArn": str,
        "neptuneIamRoleArn": str,
        "baseProcessingInstanceType": str,
        "trainingInstanceType": str,
        "trainingInstanceVolumeSizeInGB": int,
        "trainingTimeOutInSeconds": int,
        "maxHPONumberOfTrainingJobs": int,
        "maxHPOParallelTrainingJobs": int,
        "subnets": List[str],
        "securityGroupIds": List[str],
        "volumeEncryptionKMSKey": str,
        "s3OutputEncryptionKMSKey": str,
        "enableManagedSpotTraining": bool,
        "customModelTrainingParameters": "CustomModelTrainingParametersTypeDef",
    },
    total=False,
)

class StartMLModelTrainingJobInputRequestTypeDef(
    _RequiredStartMLModelTrainingJobInputRequestTypeDef,
    _OptionalStartMLModelTrainingJobInputRequestTypeDef,
):
    pass

StartMLModelTrainingJobOutputTypeDef = TypedDict(
    "StartMLModelTrainingJobOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "creationTimeInMillis": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartMLModelTransformJobInputRequestTypeDef = TypedDict(
    "_RequiredStartMLModelTransformJobInputRequestTypeDef",
    {
        "modelTransformOutputS3Location": str,
    },
)
_OptionalStartMLModelTransformJobInputRequestTypeDef = TypedDict(
    "_OptionalStartMLModelTransformJobInputRequestTypeDef",
    {
        "id": str,
        "dataProcessingJobId": str,
        "mlModelTrainingJobId": str,
        "trainingJobName": str,
        "sagemakerIamRoleArn": str,
        "neptuneIamRoleArn": str,
        "customModelTransformParameters": "CustomModelTransformParametersTypeDef",
        "baseProcessingInstanceType": str,
        "baseProcessingInstanceVolumeSizeInGB": int,
        "subnets": List[str],
        "securityGroupIds": List[str],
        "volumeEncryptionKMSKey": str,
        "s3OutputEncryptionKMSKey": str,
    },
    total=False,
)

class StartMLModelTransformJobInputRequestTypeDef(
    _RequiredStartMLModelTransformJobInputRequestTypeDef,
    _OptionalStartMLModelTransformJobInputRequestTypeDef,
):
    pass

StartMLModelTransformJobOutputTypeDef = TypedDict(
    "StartMLModelTransformJobOutputTypeDef",
    {
        "id": str,
        "arn": str,
        "creationTimeInMillis": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StatisticsSummaryTypeDef = TypedDict(
    "StatisticsSummaryTypeDef",
    {
        "signatureCount": int,
        "instanceCount": int,
        "predicateCount": int,
    },
    total=False,
)

StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {
        "autoCompute": bool,
        "active": bool,
        "statisticsId": str,
        "date": datetime,
        "note": str,
        "signatureInfo": "StatisticsSummaryTypeDef",
    },
    total=False,
)

SubjectStructureTypeDef = TypedDict(
    "SubjectStructureTypeDef",
    {
        "count": int,
        "predicates": List[str],
    },
    total=False,
)
