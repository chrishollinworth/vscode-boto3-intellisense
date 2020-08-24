"""
Main interface for machinelearning service type definitions.

Usage::

    ```python
    from mypy_boto3_machinelearning.type_defs import BatchPredictionTypeDef

    data: BatchPredictionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchPredictionTypeDef",
    "DataSourceTypeDef",
    "EvaluationTypeDef",
    "MLModelTypeDef",
    "PerformanceMetricsTypeDef",
    "PredictionTypeDef",
    "RDSDatabaseCredentialsTypeDef",
    "RDSDatabaseTypeDef",
    "RDSMetadataTypeDef",
    "RealtimeEndpointInfoTypeDef",
    "RedshiftDatabaseCredentialsTypeDef",
    "RedshiftDatabaseTypeDef",
    "RedshiftMetadataTypeDef",
    "TagTypeDef",
    "AddTagsOutputTypeDef",
    "CreateBatchPredictionOutputTypeDef",
    "CreateDataSourceFromRDSOutputTypeDef",
    "CreateDataSourceFromRedshiftOutputTypeDef",
    "CreateDataSourceFromS3OutputTypeDef",
    "CreateEvaluationOutputTypeDef",
    "CreateMLModelOutputTypeDef",
    "CreateRealtimeEndpointOutputTypeDef",
    "DeleteBatchPredictionOutputTypeDef",
    "DeleteDataSourceOutputTypeDef",
    "DeleteEvaluationOutputTypeDef",
    "DeleteMLModelOutputTypeDef",
    "DeleteRealtimeEndpointOutputTypeDef",
    "DeleteTagsOutputTypeDef",
    "DescribeBatchPredictionsOutputTypeDef",
    "DescribeDataSourcesOutputTypeDef",
    "DescribeEvaluationsOutputTypeDef",
    "DescribeMLModelsOutputTypeDef",
    "DescribeTagsOutputTypeDef",
    "GetBatchPredictionOutputTypeDef",
    "GetDataSourceOutputTypeDef",
    "GetEvaluationOutputTypeDef",
    "GetMLModelOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PredictOutputTypeDef",
    "RDSDataSpecTypeDef",
    "RedshiftDataSpecTypeDef",
    "S3DataSpecTypeDef",
    "UpdateBatchPredictionOutputTypeDef",
    "UpdateDataSourceOutputTypeDef",
    "UpdateEvaluationOutputTypeDef",
    "UpdateMLModelOutputTypeDef",
    "WaiterConfigTypeDef",
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
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
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
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
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
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "PerformanceMetrics": "PerformanceMetricsTypeDef",
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
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
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "SizeInBytes": int,
        "EndpointInfo": "RealtimeEndpointInfoTypeDef",
        "TrainingParameters": Dict[str, str],
        "InputDataLocationS3": str,
        "Algorithm": Literal["sgd"],
        "MLModelType": Literal["REGRESSION", "BINARY", "MULTICLASS"],
        "ScoreThreshold": float,
        "ScoreThresholdLastUpdatedAt": datetime,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)

PerformanceMetricsTypeDef = TypedDict(
    "PerformanceMetricsTypeDef", {"Properties": Dict[str, str]}, total=False
)

PredictionTypeDef = TypedDict(
    "PredictionTypeDef",
    {
        "predictedLabel": str,
        "predictedValue": float,
        "predictedScores": Dict[str, float],
        "details": Dict[Literal["PredictiveModelType", "Algorithm"], str],
    },
    total=False,
)

RDSDatabaseCredentialsTypeDef = TypedDict(
    "RDSDatabaseCredentialsTypeDef", {"Username": str, "Password": str}
)

RDSDatabaseTypeDef = TypedDict(
    "RDSDatabaseTypeDef", {"InstanceIdentifier": str, "DatabaseName": str}
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
        "EndpointStatus": Literal["NONE", "READY", "UPDATING", "FAILED"],
    },
    total=False,
)

RedshiftDatabaseCredentialsTypeDef = TypedDict(
    "RedshiftDatabaseCredentialsTypeDef", {"Username": str, "Password": str}
)

RedshiftDatabaseTypeDef = TypedDict(
    "RedshiftDatabaseTypeDef", {"DatabaseName": str, "ClusterIdentifier": str}
)

RedshiftMetadataTypeDef = TypedDict(
    "RedshiftMetadataTypeDef",
    {"RedshiftDatabase": "RedshiftDatabaseTypeDef", "DatabaseUserName": str, "SelectSqlQuery": str},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

AddTagsOutputTypeDef = TypedDict(
    "AddTagsOutputTypeDef",
    {
        "ResourceId": str,
        "ResourceType": Literal["BatchPrediction", "DataSource", "Evaluation", "MLModel"],
    },
    total=False,
)

CreateBatchPredictionOutputTypeDef = TypedDict(
    "CreateBatchPredictionOutputTypeDef", {"BatchPredictionId": str}, total=False
)

CreateDataSourceFromRDSOutputTypeDef = TypedDict(
    "CreateDataSourceFromRDSOutputTypeDef", {"DataSourceId": str}, total=False
)

CreateDataSourceFromRedshiftOutputTypeDef = TypedDict(
    "CreateDataSourceFromRedshiftOutputTypeDef", {"DataSourceId": str}, total=False
)

CreateDataSourceFromS3OutputTypeDef = TypedDict(
    "CreateDataSourceFromS3OutputTypeDef", {"DataSourceId": str}, total=False
)

CreateEvaluationOutputTypeDef = TypedDict(
    "CreateEvaluationOutputTypeDef", {"EvaluationId": str}, total=False
)

CreateMLModelOutputTypeDef = TypedDict(
    "CreateMLModelOutputTypeDef", {"MLModelId": str}, total=False
)

CreateRealtimeEndpointOutputTypeDef = TypedDict(
    "CreateRealtimeEndpointOutputTypeDef",
    {"MLModelId": str, "RealtimeEndpointInfo": "RealtimeEndpointInfoTypeDef"},
    total=False,
)

DeleteBatchPredictionOutputTypeDef = TypedDict(
    "DeleteBatchPredictionOutputTypeDef", {"BatchPredictionId": str}, total=False
)

DeleteDataSourceOutputTypeDef = TypedDict(
    "DeleteDataSourceOutputTypeDef", {"DataSourceId": str}, total=False
)

DeleteEvaluationOutputTypeDef = TypedDict(
    "DeleteEvaluationOutputTypeDef", {"EvaluationId": str}, total=False
)

DeleteMLModelOutputTypeDef = TypedDict(
    "DeleteMLModelOutputTypeDef", {"MLModelId": str}, total=False
)

DeleteRealtimeEndpointOutputTypeDef = TypedDict(
    "DeleteRealtimeEndpointOutputTypeDef",
    {"MLModelId": str, "RealtimeEndpointInfo": "RealtimeEndpointInfoTypeDef"},
    total=False,
)

DeleteTagsOutputTypeDef = TypedDict(
    "DeleteTagsOutputTypeDef",
    {
        "ResourceId": str,
        "ResourceType": Literal["BatchPrediction", "DataSource", "Evaluation", "MLModel"],
    },
    total=False,
)

DescribeBatchPredictionsOutputTypeDef = TypedDict(
    "DescribeBatchPredictionsOutputTypeDef",
    {"Results": List["BatchPredictionTypeDef"], "NextToken": str},
    total=False,
)

DescribeDataSourcesOutputTypeDef = TypedDict(
    "DescribeDataSourcesOutputTypeDef",
    {"Results": List["DataSourceTypeDef"], "NextToken": str},
    total=False,
)

DescribeEvaluationsOutputTypeDef = TypedDict(
    "DescribeEvaluationsOutputTypeDef",
    {"Results": List["EvaluationTypeDef"], "NextToken": str},
    total=False,
)

DescribeMLModelsOutputTypeDef = TypedDict(
    "DescribeMLModelsOutputTypeDef",
    {"Results": List["MLModelTypeDef"], "NextToken": str},
    total=False,
)

DescribeTagsOutputTypeDef = TypedDict(
    "DescribeTagsOutputTypeDef",
    {
        "ResourceId": str,
        "ResourceType": Literal["BatchPrediction", "DataSource", "Evaluation", "MLModel"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
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
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "OutputUri": str,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "TotalRecordCount": int,
        "InvalidRecordCount": int,
    },
    total=False,
)

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
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
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
    },
    total=False,
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
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "PerformanceMetrics": "PerformanceMetricsTypeDef",
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
    },
    total=False,
)

GetMLModelOutputTypeDef = TypedDict(
    "GetMLModelOutputTypeDef",
    {
        "MLModelId": str,
        "TrainingDataSourceId": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": Literal["PENDING", "INPROGRESS", "FAILED", "COMPLETED", "DELETED"],
        "SizeInBytes": int,
        "EndpointInfo": "RealtimeEndpointInfoTypeDef",
        "TrainingParameters": Dict[str, str],
        "InputDataLocationS3": str,
        "MLModelType": Literal["REGRESSION", "BINARY", "MULTICLASS"],
        "ScoreThreshold": float,
        "ScoreThresholdLastUpdatedAt": datetime,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "Recipe": str,
        "Schema": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PredictOutputTypeDef = TypedDict(
    "PredictOutputTypeDef", {"Prediction": "PredictionTypeDef"}, total=False
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
    {"DataRearrangement": str, "DataSchema": str, "DataSchemaUri": str},
    total=False,
)


class RDSDataSpecTypeDef(_RequiredRDSDataSpecTypeDef, _OptionalRDSDataSpecTypeDef):
    pass


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
    {"DataRearrangement": str, "DataSchema": str, "DataSchemaUri": str},
    total=False,
)


class RedshiftDataSpecTypeDef(_RequiredRedshiftDataSpecTypeDef, _OptionalRedshiftDataSpecTypeDef):
    pass


_RequiredS3DataSpecTypeDef = TypedDict("_RequiredS3DataSpecTypeDef", {"DataLocationS3": str})
_OptionalS3DataSpecTypeDef = TypedDict(
    "_OptionalS3DataSpecTypeDef",
    {"DataRearrangement": str, "DataSchema": str, "DataSchemaLocationS3": str},
    total=False,
)


class S3DataSpecTypeDef(_RequiredS3DataSpecTypeDef, _OptionalS3DataSpecTypeDef):
    pass


UpdateBatchPredictionOutputTypeDef = TypedDict(
    "UpdateBatchPredictionOutputTypeDef", {"BatchPredictionId": str}, total=False
)

UpdateDataSourceOutputTypeDef = TypedDict(
    "UpdateDataSourceOutputTypeDef", {"DataSourceId": str}, total=False
)

UpdateEvaluationOutputTypeDef = TypedDict(
    "UpdateEvaluationOutputTypeDef", {"EvaluationId": str}, total=False
)

UpdateMLModelOutputTypeDef = TypedDict(
    "UpdateMLModelOutputTypeDef", {"MLModelId": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
