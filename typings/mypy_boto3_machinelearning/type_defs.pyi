"""
Type annotations for machinelearning service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/type_defs.html)

Usage::

    ```python
    from mypy_boto3_machinelearning.type_defs import AddTagsInputRequestTypeDef

    data: AddTagsInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    BatchPredictionFilterVariableType,
    DataSourceFilterVariableType,
    DetailsAttributesType,
    EntityStatusType,
    EvaluationFilterVariableType,
    MLModelFilterVariableType,
    MLModelTypeType,
    RealtimeEndpointStatusType,
    SortOrderType,
    TaggableResourceTypeType,
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
    "AddTagsInputRequestTypeDef",
    "AddTagsOutputTypeDef",
    "BatchPredictionTypeDef",
    "CreateBatchPredictionInputRequestTypeDef",
    "CreateBatchPredictionOutputTypeDef",
    "CreateDataSourceFromRDSInputRequestTypeDef",
    "CreateDataSourceFromRDSOutputTypeDef",
    "CreateDataSourceFromRedshiftInputRequestTypeDef",
    "CreateDataSourceFromRedshiftOutputTypeDef",
    "CreateDataSourceFromS3InputRequestTypeDef",
    "CreateDataSourceFromS3OutputTypeDef",
    "CreateEvaluationInputRequestTypeDef",
    "CreateEvaluationOutputTypeDef",
    "CreateMLModelInputRequestTypeDef",
    "CreateMLModelOutputTypeDef",
    "CreateRealtimeEndpointInputRequestTypeDef",
    "CreateRealtimeEndpointOutputTypeDef",
    "DataSourceTypeDef",
    "DeleteBatchPredictionInputRequestTypeDef",
    "DeleteBatchPredictionOutputTypeDef",
    "DeleteDataSourceInputRequestTypeDef",
    "DeleteDataSourceOutputTypeDef",
    "DeleteEvaluationInputRequestTypeDef",
    "DeleteEvaluationOutputTypeDef",
    "DeleteMLModelInputRequestTypeDef",
    "DeleteMLModelOutputTypeDef",
    "DeleteRealtimeEndpointInputRequestTypeDef",
    "DeleteRealtimeEndpointOutputTypeDef",
    "DeleteTagsInputRequestTypeDef",
    "DeleteTagsOutputTypeDef",
    "DescribeBatchPredictionsInputRequestTypeDef",
    "DescribeBatchPredictionsOutputTypeDef",
    "DescribeDataSourcesInputRequestTypeDef",
    "DescribeDataSourcesOutputTypeDef",
    "DescribeEvaluationsInputRequestTypeDef",
    "DescribeEvaluationsOutputTypeDef",
    "DescribeMLModelsInputRequestTypeDef",
    "DescribeMLModelsOutputTypeDef",
    "DescribeTagsInputRequestTypeDef",
    "DescribeTagsOutputTypeDef",
    "EvaluationTypeDef",
    "GetBatchPredictionInputRequestTypeDef",
    "GetBatchPredictionOutputTypeDef",
    "GetDataSourceInputRequestTypeDef",
    "GetDataSourceOutputTypeDef",
    "GetEvaluationInputRequestTypeDef",
    "GetEvaluationOutputTypeDef",
    "GetMLModelInputRequestTypeDef",
    "GetMLModelOutputTypeDef",
    "MLModelTypeDef",
    "PaginatorConfigTypeDef",
    "PerformanceMetricsTypeDef",
    "PredictInputRequestTypeDef",
    "PredictOutputTypeDef",
    "PredictionTypeDef",
    "RDSDataSpecTypeDef",
    "RDSDatabaseCredentialsTypeDef",
    "RDSDatabaseTypeDef",
    "RDSMetadataTypeDef",
    "RealtimeEndpointInfoTypeDef",
    "RedshiftDataSpecTypeDef",
    "RedshiftDatabaseCredentialsTypeDef",
    "RedshiftDatabaseTypeDef",
    "RedshiftMetadataTypeDef",
    "ResponseMetadataTypeDef",
    "S3DataSpecTypeDef",
    "TagTypeDef",
    "UpdateBatchPredictionInputRequestTypeDef",
    "UpdateBatchPredictionOutputTypeDef",
    "UpdateDataSourceInputRequestTypeDef",
    "UpdateDataSourceOutputTypeDef",
    "UpdateEvaluationInputRequestTypeDef",
    "UpdateEvaluationOutputTypeDef",
    "UpdateMLModelInputRequestTypeDef",
    "UpdateMLModelOutputTypeDef",
    "WaiterConfigTypeDef",
)

AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
    },
)

AddTagsOutputTypeDef = TypedDict(
    "AddTagsOutputTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPredictionTypeDef = TypedDict(
    "BatchPredictionTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "OutputUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "TotalRecordCount": int,
        "InvalidRecordCount": int,
    },
    total=False,
)

_RequiredCreateBatchPredictionInputRequestTypeDef = TypedDict(
    "_RequiredCreateBatchPredictionInputRequestTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "OutputUri": str,
    },
)
_OptionalCreateBatchPredictionInputRequestTypeDef = TypedDict(
    "_OptionalCreateBatchPredictionInputRequestTypeDef",
    {
        "BatchPredictionName": str,
    },
    total=False,
)

class CreateBatchPredictionInputRequestTypeDef(
    _RequiredCreateBatchPredictionInputRequestTypeDef,
    _OptionalCreateBatchPredictionInputRequestTypeDef,
):
    pass

CreateBatchPredictionOutputTypeDef = TypedDict(
    "CreateBatchPredictionOutputTypeDef",
    {
        "BatchPredictionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSourceFromRDSInputRequestTypeDef = TypedDict(
    "_RequiredCreateDataSourceFromRDSInputRequestTypeDef",
    {
        "DataSourceId": str,
        "RDSData": "RDSDataSpecTypeDef",
        "RoleARN": str,
    },
)
_OptionalCreateDataSourceFromRDSInputRequestTypeDef = TypedDict(
    "_OptionalCreateDataSourceFromRDSInputRequestTypeDef",
    {
        "DataSourceName": str,
        "ComputeStatistics": bool,
    },
    total=False,
)

class CreateDataSourceFromRDSInputRequestTypeDef(
    _RequiredCreateDataSourceFromRDSInputRequestTypeDef,
    _OptionalCreateDataSourceFromRDSInputRequestTypeDef,
):
    pass

CreateDataSourceFromRDSOutputTypeDef = TypedDict(
    "CreateDataSourceFromRDSOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSourceFromRedshiftInputRequestTypeDef = TypedDict(
    "_RequiredCreateDataSourceFromRedshiftInputRequestTypeDef",
    {
        "DataSourceId": str,
        "DataSpec": "RedshiftDataSpecTypeDef",
        "RoleARN": str,
    },
)
_OptionalCreateDataSourceFromRedshiftInputRequestTypeDef = TypedDict(
    "_OptionalCreateDataSourceFromRedshiftInputRequestTypeDef",
    {
        "DataSourceName": str,
        "ComputeStatistics": bool,
    },
    total=False,
)

class CreateDataSourceFromRedshiftInputRequestTypeDef(
    _RequiredCreateDataSourceFromRedshiftInputRequestTypeDef,
    _OptionalCreateDataSourceFromRedshiftInputRequestTypeDef,
):
    pass

CreateDataSourceFromRedshiftOutputTypeDef = TypedDict(
    "CreateDataSourceFromRedshiftOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataSourceFromS3InputRequestTypeDef = TypedDict(
    "_RequiredCreateDataSourceFromS3InputRequestTypeDef",
    {
        "DataSourceId": str,
        "DataSpec": "S3DataSpecTypeDef",
    },
)
_OptionalCreateDataSourceFromS3InputRequestTypeDef = TypedDict(
    "_OptionalCreateDataSourceFromS3InputRequestTypeDef",
    {
        "DataSourceName": str,
        "ComputeStatistics": bool,
    },
    total=False,
)

class CreateDataSourceFromS3InputRequestTypeDef(
    _RequiredCreateDataSourceFromS3InputRequestTypeDef,
    _OptionalCreateDataSourceFromS3InputRequestTypeDef,
):
    pass

CreateDataSourceFromS3OutputTypeDef = TypedDict(
    "CreateDataSourceFromS3OutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEvaluationInputRequestTypeDef = TypedDict(
    "_RequiredCreateEvaluationInputRequestTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
    },
)
_OptionalCreateEvaluationInputRequestTypeDef = TypedDict(
    "_OptionalCreateEvaluationInputRequestTypeDef",
    {
        "EvaluationName": str,
    },
    total=False,
)

class CreateEvaluationInputRequestTypeDef(
    _RequiredCreateEvaluationInputRequestTypeDef, _OptionalCreateEvaluationInputRequestTypeDef
):
    pass

CreateEvaluationOutputTypeDef = TypedDict(
    "CreateEvaluationOutputTypeDef",
    {
        "EvaluationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMLModelInputRequestTypeDef = TypedDict(
    "_RequiredCreateMLModelInputRequestTypeDef",
    {
        "MLModelId": str,
        "MLModelType": MLModelTypeType,
        "TrainingDataSourceId": str,
    },
)
_OptionalCreateMLModelInputRequestTypeDef = TypedDict(
    "_OptionalCreateMLModelInputRequestTypeDef",
    {
        "MLModelName": str,
        "Parameters": Dict[str, str],
        "Recipe": str,
        "RecipeUri": str,
    },
    total=False,
)

class CreateMLModelInputRequestTypeDef(
    _RequiredCreateMLModelInputRequestTypeDef, _OptionalCreateMLModelInputRequestTypeDef
):
    pass

CreateMLModelOutputTypeDef = TypedDict(
    "CreateMLModelOutputTypeDef",
    {
        "MLModelId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRealtimeEndpointInputRequestTypeDef = TypedDict(
    "CreateRealtimeEndpointInputRequestTypeDef",
    {
        "MLModelId": str,
    },
)

CreateRealtimeEndpointOutputTypeDef = TypedDict(
    "CreateRealtimeEndpointOutputTypeDef",
    {
        "MLModelId": str,
        "RealtimeEndpointInfo": "RealtimeEndpointInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "DataSourceId": str,
        "DataLocationS3": str,
        "DataRearrangement": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "DataSizeInBytes": int,
        "NumberOfFiles": int,
        "Name": str,
        "Status": EntityStatusType,
        "Message": str,
        "RedshiftMetadata": "RedshiftMetadataTypeDef",
        "RDSMetadata": "RDSMetadataTypeDef",
        "RoleARN": str,
        "ComputeStatistics": bool,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)

DeleteBatchPredictionInputRequestTypeDef = TypedDict(
    "DeleteBatchPredictionInputRequestTypeDef",
    {
        "BatchPredictionId": str,
    },
)

DeleteBatchPredictionOutputTypeDef = TypedDict(
    "DeleteBatchPredictionOutputTypeDef",
    {
        "BatchPredictionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataSourceInputRequestTypeDef = TypedDict(
    "DeleteDataSourceInputRequestTypeDef",
    {
        "DataSourceId": str,
    },
)

DeleteDataSourceOutputTypeDef = TypedDict(
    "DeleteDataSourceOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEvaluationInputRequestTypeDef = TypedDict(
    "DeleteEvaluationInputRequestTypeDef",
    {
        "EvaluationId": str,
    },
)

DeleteEvaluationOutputTypeDef = TypedDict(
    "DeleteEvaluationOutputTypeDef",
    {
        "EvaluationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMLModelInputRequestTypeDef = TypedDict(
    "DeleteMLModelInputRequestTypeDef",
    {
        "MLModelId": str,
    },
)

DeleteMLModelOutputTypeDef = TypedDict(
    "DeleteMLModelOutputTypeDef",
    {
        "MLModelId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRealtimeEndpointInputRequestTypeDef = TypedDict(
    "DeleteRealtimeEndpointInputRequestTypeDef",
    {
        "MLModelId": str,
    },
)

DeleteRealtimeEndpointOutputTypeDef = TypedDict(
    "DeleteRealtimeEndpointOutputTypeDef",
    {
        "MLModelId": str,
        "RealtimeEndpointInfo": "RealtimeEndpointInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTagsInputRequestTypeDef = TypedDict(
    "DeleteTagsInputRequestTypeDef",
    {
        "TagKeys": List[str],
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
    },
)

DeleteTagsOutputTypeDef = TypedDict(
    "DeleteTagsOutputTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBatchPredictionsInputRequestTypeDef = TypedDict(
    "DescribeBatchPredictionsInputRequestTypeDef",
    {
        "FilterVariable": BatchPredictionFilterVariableType,
        "EQ": str,
        "GT": str,
        "LT": str,
        "GE": str,
        "LE": str,
        "NE": str,
        "Prefix": str,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeBatchPredictionsOutputTypeDef = TypedDict(
    "DescribeBatchPredictionsOutputTypeDef",
    {
        "Results": List["BatchPredictionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSourcesInputRequestTypeDef = TypedDict(
    "DescribeDataSourcesInputRequestTypeDef",
    {
        "FilterVariable": DataSourceFilterVariableType,
        "EQ": str,
        "GT": str,
        "LT": str,
        "GE": str,
        "LE": str,
        "NE": str,
        "Prefix": str,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeDataSourcesOutputTypeDef = TypedDict(
    "DescribeDataSourcesOutputTypeDef",
    {
        "Results": List["DataSourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEvaluationsInputRequestTypeDef = TypedDict(
    "DescribeEvaluationsInputRequestTypeDef",
    {
        "FilterVariable": EvaluationFilterVariableType,
        "EQ": str,
        "GT": str,
        "LT": str,
        "GE": str,
        "LE": str,
        "NE": str,
        "Prefix": str,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeEvaluationsOutputTypeDef = TypedDict(
    "DescribeEvaluationsOutputTypeDef",
    {
        "Results": List["EvaluationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMLModelsInputRequestTypeDef = TypedDict(
    "DescribeMLModelsInputRequestTypeDef",
    {
        "FilterVariable": MLModelFilterVariableType,
        "EQ": str,
        "GT": str,
        "LT": str,
        "GE": str,
        "LE": str,
        "NE": str,
        "Prefix": str,
        "SortOrder": SortOrderType,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

DescribeMLModelsOutputTypeDef = TypedDict(
    "DescribeMLModelsOutputTypeDef",
    {
        "Results": List["MLModelTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsInputRequestTypeDef = TypedDict(
    "DescribeTagsInputRequestTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
    },
)

DescribeTagsOutputTypeDef = TypedDict(
    "DescribeTagsOutputTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EvaluationTypeDef = TypedDict(
    "EvaluationTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "PerformanceMetrics": "PerformanceMetricsTypeDef",
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)

GetBatchPredictionInputRequestTypeDef = TypedDict(
    "GetBatchPredictionInputRequestTypeDef",
    {
        "BatchPredictionId": str,
    },
)

GetBatchPredictionOutputTypeDef = TypedDict(
    "GetBatchPredictionOutputTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "OutputUri": str,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "TotalRecordCount": int,
        "InvalidRecordCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDataSourceInputRequestTypeDef = TypedDict(
    "_RequiredGetDataSourceInputRequestTypeDef",
    {
        "DataSourceId": str,
    },
)
_OptionalGetDataSourceInputRequestTypeDef = TypedDict(
    "_OptionalGetDataSourceInputRequestTypeDef",
    {
        "Verbose": bool,
    },
    total=False,
)

class GetDataSourceInputRequestTypeDef(
    _RequiredGetDataSourceInputRequestTypeDef, _OptionalGetDataSourceInputRequestTypeDef
):
    pass

GetDataSourceOutputTypeDef = TypedDict(
    "GetDataSourceOutputTypeDef",
    {
        "DataSourceId": str,
        "DataLocationS3": str,
        "DataRearrangement": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "DataSizeInBytes": int,
        "NumberOfFiles": int,
        "Name": str,
        "Status": EntityStatusType,
        "LogUri": str,
        "Message": str,
        "RedshiftMetadata": "RedshiftMetadataTypeDef",
        "RDSMetadata": "RDSMetadataTypeDef",
        "RoleARN": str,
        "ComputeStatistics": bool,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "DataSourceSchema": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEvaluationInputRequestTypeDef = TypedDict(
    "GetEvaluationInputRequestTypeDef",
    {
        "EvaluationId": str,
    },
)

GetEvaluationOutputTypeDef = TypedDict(
    "GetEvaluationOutputTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "PerformanceMetrics": "PerformanceMetricsTypeDef",
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMLModelInputRequestTypeDef = TypedDict(
    "_RequiredGetMLModelInputRequestTypeDef",
    {
        "MLModelId": str,
    },
)
_OptionalGetMLModelInputRequestTypeDef = TypedDict(
    "_OptionalGetMLModelInputRequestTypeDef",
    {
        "Verbose": bool,
    },
    total=False,
)

class GetMLModelInputRequestTypeDef(
    _RequiredGetMLModelInputRequestTypeDef, _OptionalGetMLModelInputRequestTypeDef
):
    pass

GetMLModelOutputTypeDef = TypedDict(
    "GetMLModelOutputTypeDef",
    {
        "MLModelId": str,
        "TrainingDataSourceId": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "SizeInBytes": int,
        "EndpointInfo": "RealtimeEndpointInfoTypeDef",
        "TrainingParameters": Dict[str, str],
        "InputDataLocationS3": str,
        "MLModelType": MLModelTypeType,
        "ScoreThreshold": float,
        "ScoreThresholdLastUpdatedAt": datetime,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "Recipe": str,
        "Schema": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MLModelTypeDef = TypedDict(
    "MLModelTypeDef",
    {
        "MLModelId": str,
        "TrainingDataSourceId": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "SizeInBytes": int,
        "EndpointInfo": "RealtimeEndpointInfoTypeDef",
        "TrainingParameters": Dict[str, str],
        "InputDataLocationS3": str,
        "Algorithm": Literal["sgd"],
        "MLModelType": MLModelTypeType,
        "ScoreThreshold": float,
        "ScoreThresholdLastUpdatedAt": datetime,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
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

PerformanceMetricsTypeDef = TypedDict(
    "PerformanceMetricsTypeDef",
    {
        "Properties": Dict[str, str],
    },
    total=False,
)

PredictInputRequestTypeDef = TypedDict(
    "PredictInputRequestTypeDef",
    {
        "MLModelId": str,
        "Record": Dict[str, str],
        "PredictEndpoint": str,
    },
)

PredictOutputTypeDef = TypedDict(
    "PredictOutputTypeDef",
    {
        "Prediction": "PredictionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PredictionTypeDef = TypedDict(
    "PredictionTypeDef",
    {
        "predictedLabel": str,
        "predictedValue": float,
        "predictedScores": Dict[str, float],
        "details": Dict[DetailsAttributesType, str],
    },
    total=False,
)

_RequiredRDSDataSpecTypeDef = TypedDict(
    "_RequiredRDSDataSpecTypeDef",
    {
        "DatabaseInformation": "RDSDatabaseTypeDef",
        "SelectSqlQuery": str,
        "DatabaseCredentials": "RDSDatabaseCredentialsTypeDef",
        "S3StagingLocation": str,
        "ResourceRole": str,
        "ServiceRole": str,
        "SubnetId": str,
        "SecurityGroupIds": List[str],
    },
)
_OptionalRDSDataSpecTypeDef = TypedDict(
    "_OptionalRDSDataSpecTypeDef",
    {
        "DataRearrangement": str,
        "DataSchema": str,
        "DataSchemaUri": str,
    },
    total=False,
)

class RDSDataSpecTypeDef(_RequiredRDSDataSpecTypeDef, _OptionalRDSDataSpecTypeDef):
    pass

RDSDatabaseCredentialsTypeDef = TypedDict(
    "RDSDatabaseCredentialsTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)

RDSDatabaseTypeDef = TypedDict(
    "RDSDatabaseTypeDef",
    {
        "InstanceIdentifier": str,
        "DatabaseName": str,
    },
)

RDSMetadataTypeDef = TypedDict(
    "RDSMetadataTypeDef",
    {
        "Database": "RDSDatabaseTypeDef",
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
        "ResourceRole": str,
        "ServiceRole": str,
        "DataPipelineId": str,
    },
    total=False,
)

RealtimeEndpointInfoTypeDef = TypedDict(
    "RealtimeEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": int,
        "CreatedAt": datetime,
        "EndpointUrl": str,
        "EndpointStatus": RealtimeEndpointStatusType,
    },
    total=False,
)

_RequiredRedshiftDataSpecTypeDef = TypedDict(
    "_RequiredRedshiftDataSpecTypeDef",
    {
        "DatabaseInformation": "RedshiftDatabaseTypeDef",
        "SelectSqlQuery": str,
        "DatabaseCredentials": "RedshiftDatabaseCredentialsTypeDef",
        "S3StagingLocation": str,
    },
)
_OptionalRedshiftDataSpecTypeDef = TypedDict(
    "_OptionalRedshiftDataSpecTypeDef",
    {
        "DataRearrangement": str,
        "DataSchema": str,
        "DataSchemaUri": str,
    },
    total=False,
)

class RedshiftDataSpecTypeDef(_RequiredRedshiftDataSpecTypeDef, _OptionalRedshiftDataSpecTypeDef):
    pass

RedshiftDatabaseCredentialsTypeDef = TypedDict(
    "RedshiftDatabaseCredentialsTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)

RedshiftDatabaseTypeDef = TypedDict(
    "RedshiftDatabaseTypeDef",
    {
        "DatabaseName": str,
        "ClusterIdentifier": str,
    },
)

RedshiftMetadataTypeDef = TypedDict(
    "RedshiftMetadataTypeDef",
    {
        "RedshiftDatabase": "RedshiftDatabaseTypeDef",
        "DatabaseUserName": str,
        "SelectSqlQuery": str,
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

_RequiredS3DataSpecTypeDef = TypedDict(
    "_RequiredS3DataSpecTypeDef",
    {
        "DataLocationS3": str,
    },
)
_OptionalS3DataSpecTypeDef = TypedDict(
    "_OptionalS3DataSpecTypeDef",
    {
        "DataRearrangement": str,
        "DataSchema": str,
        "DataSchemaLocationS3": str,
    },
    total=False,
)

class S3DataSpecTypeDef(_RequiredS3DataSpecTypeDef, _OptionalS3DataSpecTypeDef):
    pass

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

UpdateBatchPredictionInputRequestTypeDef = TypedDict(
    "UpdateBatchPredictionInputRequestTypeDef",
    {
        "BatchPredictionId": str,
        "BatchPredictionName": str,
    },
)

UpdateBatchPredictionOutputTypeDef = TypedDict(
    "UpdateBatchPredictionOutputTypeDef",
    {
        "BatchPredictionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDataSourceInputRequestTypeDef = TypedDict(
    "UpdateDataSourceInputRequestTypeDef",
    {
        "DataSourceId": str,
        "DataSourceName": str,
    },
)

UpdateDataSourceOutputTypeDef = TypedDict(
    "UpdateDataSourceOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEvaluationInputRequestTypeDef = TypedDict(
    "UpdateEvaluationInputRequestTypeDef",
    {
        "EvaluationId": str,
        "EvaluationName": str,
    },
)

UpdateEvaluationOutputTypeDef = TypedDict(
    "UpdateEvaluationOutputTypeDef",
    {
        "EvaluationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMLModelInputRequestTypeDef = TypedDict(
    "_RequiredUpdateMLModelInputRequestTypeDef",
    {
        "MLModelId": str,
    },
)
_OptionalUpdateMLModelInputRequestTypeDef = TypedDict(
    "_OptionalUpdateMLModelInputRequestTypeDef",
    {
        "MLModelName": str,
        "ScoreThreshold": float,
    },
    total=False,
)

class UpdateMLModelInputRequestTypeDef(
    _RequiredUpdateMLModelInputRequestTypeDef, _OptionalUpdateMLModelInputRequestTypeDef
):
    pass

UpdateMLModelOutputTypeDef = TypedDict(
    "UpdateMLModelOutputTypeDef",
    {
        "MLModelId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
