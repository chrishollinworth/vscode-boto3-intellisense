"""
Type annotations for machinelearning service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_machinelearning.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

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
    "AddTagsInputTypeDef",
    "AddTagsOutputTypeDef",
    "BatchPredictionTypeDef",
    "CreateBatchPredictionInputTypeDef",
    "CreateBatchPredictionOutputTypeDef",
    "CreateDataSourceFromRDSInputTypeDef",
    "CreateDataSourceFromRDSOutputTypeDef",
    "CreateDataSourceFromRedshiftInputTypeDef",
    "CreateDataSourceFromRedshiftOutputTypeDef",
    "CreateDataSourceFromS3InputTypeDef",
    "CreateDataSourceFromS3OutputTypeDef",
    "CreateEvaluationInputTypeDef",
    "CreateEvaluationOutputTypeDef",
    "CreateMLModelInputTypeDef",
    "CreateMLModelOutputTypeDef",
    "CreateRealtimeEndpointInputTypeDef",
    "CreateRealtimeEndpointOutputTypeDef",
    "DataSourceTypeDef",
    "DeleteBatchPredictionInputTypeDef",
    "DeleteBatchPredictionOutputTypeDef",
    "DeleteDataSourceInputTypeDef",
    "DeleteDataSourceOutputTypeDef",
    "DeleteEvaluationInputTypeDef",
    "DeleteEvaluationOutputTypeDef",
    "DeleteMLModelInputTypeDef",
    "DeleteMLModelOutputTypeDef",
    "DeleteRealtimeEndpointInputTypeDef",
    "DeleteRealtimeEndpointOutputTypeDef",
    "DeleteTagsInputTypeDef",
    "DeleteTagsOutputTypeDef",
    "DescribeBatchPredictionsInputPaginateTypeDef",
    "DescribeBatchPredictionsInputTypeDef",
    "DescribeBatchPredictionsInputWaitTypeDef",
    "DescribeBatchPredictionsOutputTypeDef",
    "DescribeDataSourcesInputPaginateTypeDef",
    "DescribeDataSourcesInputTypeDef",
    "DescribeDataSourcesInputWaitTypeDef",
    "DescribeDataSourcesOutputTypeDef",
    "DescribeEvaluationsInputPaginateTypeDef",
    "DescribeEvaluationsInputTypeDef",
    "DescribeEvaluationsInputWaitTypeDef",
    "DescribeEvaluationsOutputTypeDef",
    "DescribeMLModelsInputPaginateTypeDef",
    "DescribeMLModelsInputTypeDef",
    "DescribeMLModelsInputWaitTypeDef",
    "DescribeMLModelsOutputTypeDef",
    "DescribeTagsInputTypeDef",
    "DescribeTagsOutputTypeDef",
    "EvaluationTypeDef",
    "GetBatchPredictionInputTypeDef",
    "GetBatchPredictionOutputTypeDef",
    "GetDataSourceInputTypeDef",
    "GetDataSourceOutputTypeDef",
    "GetEvaluationInputTypeDef",
    "GetEvaluationOutputTypeDef",
    "GetMLModelInputTypeDef",
    "GetMLModelOutputTypeDef",
    "MLModelTypeDef",
    "PaginatorConfigTypeDef",
    "PerformanceMetricsTypeDef",
    "PredictInputTypeDef",
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
    "UpdateBatchPredictionInputTypeDef",
    "UpdateBatchPredictionOutputTypeDef",
    "UpdateDataSourceInputTypeDef",
    "UpdateDataSourceOutputTypeDef",
    "UpdateEvaluationInputTypeDef",
    "UpdateEvaluationOutputTypeDef",
    "UpdateMLModelInputTypeDef",
    "UpdateMLModelOutputTypeDef",
    "WaiterConfigTypeDef",
)

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BatchPredictionTypeDef(TypedDict):
    BatchPredictionId: NotRequired[str]
    MLModelId: NotRequired[str]
    BatchPredictionDataSourceId: NotRequired[str]
    InputDataLocationS3: NotRequired[str]
    CreatedByIamUser: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    Name: NotRequired[str]
    Status: NotRequired[EntityStatusType]
    OutputUri: NotRequired[str]
    Message: NotRequired[str]
    ComputeTime: NotRequired[int]
    FinishedAt: NotRequired[datetime]
    StartedAt: NotRequired[datetime]
    TotalRecordCount: NotRequired[int]
    InvalidRecordCount: NotRequired[int]

class CreateBatchPredictionInputTypeDef(TypedDict):
    BatchPredictionId: str
    MLModelId: str
    BatchPredictionDataSourceId: str
    OutputUri: str
    BatchPredictionName: NotRequired[str]

class S3DataSpecTypeDef(TypedDict):
    DataLocationS3: str
    DataRearrangement: NotRequired[str]
    DataSchema: NotRequired[str]
    DataSchemaLocationS3: NotRequired[str]

class CreateEvaluationInputTypeDef(TypedDict):
    EvaluationId: str
    MLModelId: str
    EvaluationDataSourceId: str
    EvaluationName: NotRequired[str]

class CreateMLModelInputTypeDef(TypedDict):
    MLModelId: str
    MLModelType: MLModelTypeType
    TrainingDataSourceId: str
    MLModelName: NotRequired[str]
    Parameters: NotRequired[Mapping[str, str]]
    Recipe: NotRequired[str]
    RecipeUri: NotRequired[str]

class CreateRealtimeEndpointInputTypeDef(TypedDict):
    MLModelId: str

class RealtimeEndpointInfoTypeDef(TypedDict):
    PeakRequestsPerSecond: NotRequired[int]
    CreatedAt: NotRequired[datetime]
    EndpointUrl: NotRequired[str]
    EndpointStatus: NotRequired[RealtimeEndpointStatusType]

class DeleteBatchPredictionInputTypeDef(TypedDict):
    BatchPredictionId: str

class DeleteDataSourceInputTypeDef(TypedDict):
    DataSourceId: str

class DeleteEvaluationInputTypeDef(TypedDict):
    EvaluationId: str

class DeleteMLModelInputTypeDef(TypedDict):
    MLModelId: str

class DeleteRealtimeEndpointInputTypeDef(TypedDict):
    MLModelId: str

class DeleteTagsInputTypeDef(TypedDict):
    TagKeys: Sequence[str]
    ResourceId: str
    ResourceType: TaggableResourceTypeType

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeBatchPredictionsInputTypeDef(TypedDict):
    FilterVariable: NotRequired[BatchPredictionFilterVariableType]
    EQ: NotRequired[str]
    GT: NotRequired[str]
    LT: NotRequired[str]
    GE: NotRequired[str]
    LE: NotRequired[str]
    NE: NotRequired[str]
    Prefix: NotRequired[str]
    SortOrder: NotRequired[SortOrderType]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeDataSourcesInputTypeDef(TypedDict):
    FilterVariable: NotRequired[DataSourceFilterVariableType]
    EQ: NotRequired[str]
    GT: NotRequired[str]
    LT: NotRequired[str]
    GE: NotRequired[str]
    LE: NotRequired[str]
    NE: NotRequired[str]
    Prefix: NotRequired[str]
    SortOrder: NotRequired[SortOrderType]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class DescribeEvaluationsInputTypeDef(TypedDict):
    FilterVariable: NotRequired[EvaluationFilterVariableType]
    EQ: NotRequired[str]
    GT: NotRequired[str]
    LT: NotRequired[str]
    GE: NotRequired[str]
    LE: NotRequired[str]
    NE: NotRequired[str]
    Prefix: NotRequired[str]
    SortOrder: NotRequired[SortOrderType]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class DescribeMLModelsInputTypeDef(TypedDict):
    FilterVariable: NotRequired[MLModelFilterVariableType]
    EQ: NotRequired[str]
    GT: NotRequired[str]
    LT: NotRequired[str]
    GE: NotRequired[str]
    LE: NotRequired[str]
    NE: NotRequired[str]
    Prefix: NotRequired[str]
    SortOrder: NotRequired[SortOrderType]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]

class DescribeTagsInputTypeDef(TypedDict):
    ResourceId: str
    ResourceType: TaggableResourceTypeType

class PerformanceMetricsTypeDef(TypedDict):
    Properties: NotRequired[Dict[str, str]]

class GetBatchPredictionInputTypeDef(TypedDict):
    BatchPredictionId: str

class GetDataSourceInputTypeDef(TypedDict):
    DataSourceId: str
    Verbose: NotRequired[bool]

class GetEvaluationInputTypeDef(TypedDict):
    EvaluationId: str

class GetMLModelInputTypeDef(TypedDict):
    MLModelId: str
    Verbose: NotRequired[bool]

class PredictInputTypeDef(TypedDict):
    MLModelId: str
    Record: Mapping[str, str]
    PredictEndpoint: str

class PredictionTypeDef(TypedDict):
    predictedLabel: NotRequired[str]
    predictedValue: NotRequired[float]
    predictedScores: NotRequired[Dict[str, float]]
    details: NotRequired[Dict[DetailsAttributesType, str]]

class RDSDatabaseCredentialsTypeDef(TypedDict):
    Username: str
    Password: str

class RDSDatabaseTypeDef(TypedDict):
    InstanceIdentifier: str
    DatabaseName: str

class RedshiftDatabaseCredentialsTypeDef(TypedDict):
    Username: str
    Password: str

class RedshiftDatabaseTypeDef(TypedDict):
    DatabaseName: str
    ClusterIdentifier: str

class UpdateBatchPredictionInputTypeDef(TypedDict):
    BatchPredictionId: str
    BatchPredictionName: str

class UpdateDataSourceInputTypeDef(TypedDict):
    DataSourceId: str
    DataSourceName: str

class UpdateEvaluationInputTypeDef(TypedDict):
    EvaluationId: str
    EvaluationName: str

class UpdateMLModelInputTypeDef(TypedDict):
    MLModelId: str
    MLModelName: NotRequired[str]
    ScoreThreshold: NotRequired[float]

class AddTagsInputTypeDef(TypedDict):
    Tags: Sequence[TagTypeDef]
    ResourceId: str
    ResourceType: TaggableResourceTypeType

class AddTagsOutputTypeDef(TypedDict):
    ResourceId: str
    ResourceType: TaggableResourceTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBatchPredictionOutputTypeDef(TypedDict):
    BatchPredictionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceFromRDSOutputTypeDef(TypedDict):
    DataSourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceFromRedshiftOutputTypeDef(TypedDict):
    DataSourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceFromS3OutputTypeDef(TypedDict):
    DataSourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEvaluationOutputTypeDef(TypedDict):
    EvaluationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMLModelOutputTypeDef(TypedDict):
    MLModelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBatchPredictionOutputTypeDef(TypedDict):
    BatchPredictionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataSourceOutputTypeDef(TypedDict):
    DataSourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEvaluationOutputTypeDef(TypedDict):
    EvaluationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMLModelOutputTypeDef(TypedDict):
    MLModelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTagsOutputTypeDef(TypedDict):
    ResourceId: str
    ResourceType: TaggableResourceTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTagsOutputTypeDef(TypedDict):
    ResourceId: str
    ResourceType: TaggableResourceTypeType
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetBatchPredictionOutputTypeDef(TypedDict):
    BatchPredictionId: str
    MLModelId: str
    BatchPredictionDataSourceId: str
    InputDataLocationS3: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Name: str
    Status: EntityStatusType
    OutputUri: str
    LogUri: str
    Message: str
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime
    TotalRecordCount: int
    InvalidRecordCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBatchPredictionOutputTypeDef(TypedDict):
    BatchPredictionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataSourceOutputTypeDef(TypedDict):
    DataSourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEvaluationOutputTypeDef(TypedDict):
    EvaluationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMLModelOutputTypeDef(TypedDict):
    MLModelId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBatchPredictionsOutputTypeDef(TypedDict):
    Results: List[BatchPredictionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateDataSourceFromS3InputTypeDef(TypedDict):
    DataSourceId: str
    DataSpec: S3DataSpecTypeDef
    DataSourceName: NotRequired[str]
    ComputeStatistics: NotRequired[bool]

class CreateRealtimeEndpointOutputTypeDef(TypedDict):
    MLModelId: str
    RealtimeEndpointInfo: RealtimeEndpointInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRealtimeEndpointOutputTypeDef(TypedDict):
    MLModelId: str
    RealtimeEndpointInfo: RealtimeEndpointInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMLModelOutputTypeDef(TypedDict):
    MLModelId: str
    TrainingDataSourceId: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Name: str
    Status: EntityStatusType
    SizeInBytes: int
    EndpointInfo: RealtimeEndpointInfoTypeDef
    TrainingParameters: Dict[str, str]
    InputDataLocationS3: str
    MLModelType: MLModelTypeType
    ScoreThreshold: float
    ScoreThresholdLastUpdatedAt: datetime
    LogUri: str
    Message: str
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime
    Recipe: str
    Schema: str
    ResponseMetadata: ResponseMetadataTypeDef

class MLModelTypeDef(TypedDict):
    MLModelId: NotRequired[str]
    TrainingDataSourceId: NotRequired[str]
    CreatedByIamUser: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    Name: NotRequired[str]
    Status: NotRequired[EntityStatusType]
    SizeInBytes: NotRequired[int]
    EndpointInfo: NotRequired[RealtimeEndpointInfoTypeDef]
    TrainingParameters: NotRequired[Dict[str, str]]
    InputDataLocationS3: NotRequired[str]
    Algorithm: NotRequired[Literal["sgd"]]
    MLModelType: NotRequired[MLModelTypeType]
    ScoreThreshold: NotRequired[float]
    ScoreThresholdLastUpdatedAt: NotRequired[datetime]
    Message: NotRequired[str]
    ComputeTime: NotRequired[int]
    FinishedAt: NotRequired[datetime]
    StartedAt: NotRequired[datetime]

class DescribeBatchPredictionsInputPaginateTypeDef(TypedDict):
    FilterVariable: NotRequired[BatchPredictionFilterVariableType]
    EQ: NotRequired[str]
    GT: NotRequired[str]
    LT: NotRequired[str]
    GE: NotRequired[str]
    LE: NotRequired[str]
    NE: NotRequired[str]
    Prefix: NotRequired[str]
    SortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDataSourcesInputPaginateTypeDef(TypedDict):
    FilterVariable: NotRequired[DataSourceFilterVariableType]
    EQ: NotRequired[str]
    GT: NotRequired[str]
    LT: NotRequired[str]
    GE: NotRequired[str]
    LE: NotRequired[str]
    NE: NotRequired[str]
    Prefix: NotRequired[str]
    SortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEvaluationsInputPaginateTypeDef(TypedDict):
    FilterVariable: NotRequired[EvaluationFilterVariableType]
    EQ: NotRequired[str]
    GT: NotRequired[str]
    LT: NotRequired[str]
    GE: NotRequired[str]
    LE: NotRequired[str]
    NE: NotRequired[str]
    Prefix: NotRequired[str]
    SortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeMLModelsInputPaginateTypeDef(TypedDict):
    FilterVariable: NotRequired[MLModelFilterVariableType]
    EQ: NotRequired[str]
    GT: NotRequired[str]
    LT: NotRequired[str]
    GE: NotRequired[str]
    LE: NotRequired[str]
    NE: NotRequired[str]
    Prefix: NotRequired[str]
    SortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeBatchPredictionsInputWaitTypeDef(TypedDict):
    FilterVariable: NotRequired[BatchPredictionFilterVariableType]
    EQ: NotRequired[str]
    GT: NotRequired[str]
    LT: NotRequired[str]
    GE: NotRequired[str]
    LE: NotRequired[str]
    NE: NotRequired[str]
    Prefix: NotRequired[str]
    SortOrder: NotRequired[SortOrderType]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeDataSourcesInputWaitTypeDef(TypedDict):
    FilterVariable: NotRequired[DataSourceFilterVariableType]
    EQ: NotRequired[str]
    GT: NotRequired[str]
    LT: NotRequired[str]
    GE: NotRequired[str]
    LE: NotRequired[str]
    NE: NotRequired[str]
    Prefix: NotRequired[str]
    SortOrder: NotRequired[SortOrderType]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeEvaluationsInputWaitTypeDef(TypedDict):
    FilterVariable: NotRequired[EvaluationFilterVariableType]
    EQ: NotRequired[str]
    GT: NotRequired[str]
    LT: NotRequired[str]
    GE: NotRequired[str]
    LE: NotRequired[str]
    NE: NotRequired[str]
    Prefix: NotRequired[str]
    SortOrder: NotRequired[SortOrderType]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeMLModelsInputWaitTypeDef(TypedDict):
    FilterVariable: NotRequired[MLModelFilterVariableType]
    EQ: NotRequired[str]
    GT: NotRequired[str]
    LT: NotRequired[str]
    GE: NotRequired[str]
    LE: NotRequired[str]
    NE: NotRequired[str]
    Prefix: NotRequired[str]
    SortOrder: NotRequired[SortOrderType]
    NextToken: NotRequired[str]
    Limit: NotRequired[int]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class EvaluationTypeDef(TypedDict):
    EvaluationId: NotRequired[str]
    MLModelId: NotRequired[str]
    EvaluationDataSourceId: NotRequired[str]
    InputDataLocationS3: NotRequired[str]
    CreatedByIamUser: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    Name: NotRequired[str]
    Status: NotRequired[EntityStatusType]
    PerformanceMetrics: NotRequired[PerformanceMetricsTypeDef]
    Message: NotRequired[str]
    ComputeTime: NotRequired[int]
    FinishedAt: NotRequired[datetime]
    StartedAt: NotRequired[datetime]

class GetEvaluationOutputTypeDef(TypedDict):
    EvaluationId: str
    MLModelId: str
    EvaluationDataSourceId: str
    InputDataLocationS3: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Name: str
    Status: EntityStatusType
    PerformanceMetrics: PerformanceMetricsTypeDef
    LogUri: str
    Message: str
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PredictOutputTypeDef(TypedDict):
    Prediction: PredictionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RDSDataSpecTypeDef(TypedDict):
    DatabaseInformation: RDSDatabaseTypeDef
    SelectSqlQuery: str
    DatabaseCredentials: RDSDatabaseCredentialsTypeDef
    S3StagingLocation: str
    ResourceRole: str
    ServiceRole: str
    SubnetId: str
    SecurityGroupIds: Sequence[str]
    DataRearrangement: NotRequired[str]
    DataSchema: NotRequired[str]
    DataSchemaUri: NotRequired[str]

class RDSMetadataTypeDef(TypedDict):
    Database: NotRequired[RDSDatabaseTypeDef]
    DatabaseUserName: NotRequired[str]
    SelectSqlQuery: NotRequired[str]
    ResourceRole: NotRequired[str]
    ServiceRole: NotRequired[str]
    DataPipelineId: NotRequired[str]

class RedshiftDataSpecTypeDef(TypedDict):
    DatabaseInformation: RedshiftDatabaseTypeDef
    SelectSqlQuery: str
    DatabaseCredentials: RedshiftDatabaseCredentialsTypeDef
    S3StagingLocation: str
    DataRearrangement: NotRequired[str]
    DataSchema: NotRequired[str]
    DataSchemaUri: NotRequired[str]

class RedshiftMetadataTypeDef(TypedDict):
    RedshiftDatabase: NotRequired[RedshiftDatabaseTypeDef]
    DatabaseUserName: NotRequired[str]
    SelectSqlQuery: NotRequired[str]

class DescribeMLModelsOutputTypeDef(TypedDict):
    Results: List[MLModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeEvaluationsOutputTypeDef(TypedDict):
    Results: List[EvaluationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateDataSourceFromRDSInputTypeDef(TypedDict):
    DataSourceId: str
    RDSData: RDSDataSpecTypeDef
    RoleARN: str
    DataSourceName: NotRequired[str]
    ComputeStatistics: NotRequired[bool]

class CreateDataSourceFromRedshiftInputTypeDef(TypedDict):
    DataSourceId: str
    DataSpec: RedshiftDataSpecTypeDef
    RoleARN: str
    DataSourceName: NotRequired[str]
    ComputeStatistics: NotRequired[bool]

class DataSourceTypeDef(TypedDict):
    DataSourceId: NotRequired[str]
    DataLocationS3: NotRequired[str]
    DataRearrangement: NotRequired[str]
    CreatedByIamUser: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    DataSizeInBytes: NotRequired[int]
    NumberOfFiles: NotRequired[int]
    Name: NotRequired[str]
    Status: NotRequired[EntityStatusType]
    Message: NotRequired[str]
    RedshiftMetadata: NotRequired[RedshiftMetadataTypeDef]
    RDSMetadata: NotRequired[RDSMetadataTypeDef]
    RoleARN: NotRequired[str]
    ComputeStatistics: NotRequired[bool]
    ComputeTime: NotRequired[int]
    FinishedAt: NotRequired[datetime]
    StartedAt: NotRequired[datetime]

class GetDataSourceOutputTypeDef(TypedDict):
    DataSourceId: str
    DataLocationS3: str
    DataRearrangement: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    DataSizeInBytes: int
    NumberOfFiles: int
    Name: str
    Status: EntityStatusType
    LogUri: str
    Message: str
    RedshiftMetadata: RedshiftMetadataTypeDef
    RDSMetadata: RDSMetadataTypeDef
    RoleARN: str
    ComputeStatistics: bool
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime
    DataSourceSchema: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataSourcesOutputTypeDef(TypedDict):
    Results: List[DataSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
