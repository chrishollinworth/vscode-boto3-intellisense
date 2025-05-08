"""
Type annotations for lookoutvision service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_lookoutvision.type_defs import PixelAnomalyTypeDef

    data: PixelAnomalyTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    DatasetStatusType,
    ModelHostingStatusType,
    ModelPackagingJobStatusType,
    ModelStatusType,
    TargetPlatformArchType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AnomalyTypeDef",
    "BlobTypeDef",
    "CreateDatasetRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateModelRequestTypeDef",
    "CreateModelResponseTypeDef",
    "CreateProjectRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "DatasetDescriptionTypeDef",
    "DatasetGroundTruthManifestTypeDef",
    "DatasetImageStatsTypeDef",
    "DatasetMetadataTypeDef",
    "DatasetSourceTypeDef",
    "DeleteDatasetRequestTypeDef",
    "DeleteModelRequestTypeDef",
    "DeleteModelResponseTypeDef",
    "DeleteProjectRequestTypeDef",
    "DeleteProjectResponseTypeDef",
    "DescribeDatasetRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeModelPackagingJobRequestTypeDef",
    "DescribeModelPackagingJobResponseTypeDef",
    "DescribeModelRequestTypeDef",
    "DescribeModelResponseTypeDef",
    "DescribeProjectRequestTypeDef",
    "DescribeProjectResponseTypeDef",
    "DetectAnomaliesRequestTypeDef",
    "DetectAnomaliesResponseTypeDef",
    "DetectAnomalyResultTypeDef",
    "GreengrassConfigurationOutputTypeDef",
    "GreengrassConfigurationTypeDef",
    "GreengrassOutputDetailsTypeDef",
    "ImageSourceTypeDef",
    "InputS3ObjectTypeDef",
    "ListDatasetEntriesRequestPaginateTypeDef",
    "ListDatasetEntriesRequestTypeDef",
    "ListDatasetEntriesResponseTypeDef",
    "ListModelPackagingJobsRequestPaginateTypeDef",
    "ListModelPackagingJobsRequestTypeDef",
    "ListModelPackagingJobsResponseTypeDef",
    "ListModelsRequestPaginateTypeDef",
    "ListModelsRequestTypeDef",
    "ListModelsResponseTypeDef",
    "ListProjectsRequestPaginateTypeDef",
    "ListProjectsRequestTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModelDescriptionTypeDef",
    "ModelMetadataTypeDef",
    "ModelPackagingConfigurationOutputTypeDef",
    "ModelPackagingConfigurationTypeDef",
    "ModelPackagingConfigurationUnionTypeDef",
    "ModelPackagingDescriptionTypeDef",
    "ModelPackagingJobMetadataTypeDef",
    "ModelPackagingOutputDetailsTypeDef",
    "ModelPerformanceTypeDef",
    "OutputConfigTypeDef",
    "OutputS3ObjectTypeDef",
    "PaginatorConfigTypeDef",
    "PixelAnomalyTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectMetadataTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "StartModelPackagingJobRequestTypeDef",
    "StartModelPackagingJobResponseTypeDef",
    "StartModelRequestTypeDef",
    "StartModelResponseTypeDef",
    "StopModelRequestTypeDef",
    "StopModelResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TargetPlatformTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDatasetEntriesRequestTypeDef",
    "UpdateDatasetEntriesResponseTypeDef",
)

class PixelAnomalyTypeDef(TypedDict):
    TotalPercentageArea: NotRequired[float]
    Color: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class DatasetMetadataTypeDef(TypedDict):
    DatasetType: NotRequired[str]
    CreationTimestamp: NotRequired[datetime]
    Status: NotRequired[DatasetStatusType]
    StatusMessage: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class CreateProjectRequestTypeDef(TypedDict):
    ProjectName: str
    ClientToken: NotRequired[str]

class ProjectMetadataTypeDef(TypedDict):
    ProjectArn: NotRequired[str]
    ProjectName: NotRequired[str]
    CreationTimestamp: NotRequired[datetime]

class DatasetImageStatsTypeDef(TypedDict):
    Total: NotRequired[int]
    Labeled: NotRequired[int]
    Normal: NotRequired[int]
    Anomaly: NotRequired[int]

class InputS3ObjectTypeDef(TypedDict):
    Bucket: str
    Key: str
    VersionId: NotRequired[str]

class DeleteDatasetRequestTypeDef(TypedDict):
    ProjectName: str
    DatasetType: str
    ClientToken: NotRequired[str]

class DeleteModelRequestTypeDef(TypedDict):
    ProjectName: str
    ModelVersion: str
    ClientToken: NotRequired[str]

class DeleteProjectRequestTypeDef(TypedDict):
    ProjectName: str
    ClientToken: NotRequired[str]

class DescribeDatasetRequestTypeDef(TypedDict):
    ProjectName: str
    DatasetType: str

class DescribeModelPackagingJobRequestTypeDef(TypedDict):
    ProjectName: str
    JobName: str

class DescribeModelRequestTypeDef(TypedDict):
    ProjectName: str
    ModelVersion: str

class DescribeProjectRequestTypeDef(TypedDict):
    ProjectName: str

ImageSourceTypeDef = TypedDict(
    "ImageSourceTypeDef",
    {
        "Type": NotRequired[str],
    },
)

class S3LocationTypeDef(TypedDict):
    Bucket: str
    Prefix: NotRequired[str]

class TargetPlatformTypeDef(TypedDict):
    Os: Literal["LINUX"]
    Arch: TargetPlatformArchType
    Accelerator: NotRequired[Literal["NVIDIA"]]

class GreengrassOutputDetailsTypeDef(TypedDict):
    ComponentVersionArn: NotRequired[str]
    ComponentName: NotRequired[str]
    ComponentVersion: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class ListModelPackagingJobsRequestTypeDef(TypedDict):
    ProjectName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ModelPackagingJobMetadataTypeDef(TypedDict):
    JobName: NotRequired[str]
    ProjectName: NotRequired[str]
    ModelVersion: NotRequired[str]
    ModelPackagingJobDescription: NotRequired[str]
    ModelPackagingMethod: NotRequired[str]
    Status: NotRequired[ModelPackagingJobStatusType]
    StatusMessage: NotRequired[str]
    CreationTimestamp: NotRequired[datetime]
    LastUpdatedTimestamp: NotRequired[datetime]

class ListModelsRequestTypeDef(TypedDict):
    ProjectName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListProjectsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class ModelPerformanceTypeDef(TypedDict):
    F1Score: NotRequired[float]
    Recall: NotRequired[float]
    Precision: NotRequired[float]

class OutputS3ObjectTypeDef(TypedDict):
    Bucket: str
    Key: str

class StartModelRequestTypeDef(TypedDict):
    ProjectName: str
    ModelVersion: str
    MinInferenceUnits: int
    ClientToken: NotRequired[str]
    MaxInferenceUnits: NotRequired[int]

class StopModelRequestTypeDef(TypedDict):
    ProjectName: str
    ModelVersion: str
    ClientToken: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class AnomalyTypeDef(TypedDict):
    Name: NotRequired[str]
    PixelAnomaly: NotRequired[PixelAnomalyTypeDef]

class DetectAnomaliesRequestTypeDef(TypedDict):
    ProjectName: str
    ModelVersion: str
    Body: BlobTypeDef
    ContentType: str

class UpdateDatasetEntriesRequestTypeDef(TypedDict):
    ProjectName: str
    DatasetType: str
    Changes: BlobTypeDef
    ClientToken: NotRequired[str]

class ProjectDescriptionTypeDef(TypedDict):
    ProjectArn: NotRequired[str]
    ProjectName: NotRequired[str]
    CreationTimestamp: NotRequired[datetime]
    Datasets: NotRequired[List[DatasetMetadataTypeDef]]

class CreateDatasetResponseTypeDef(TypedDict):
    DatasetMetadata: DatasetMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteModelResponseTypeDef(TypedDict):
    ModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProjectResponseTypeDef(TypedDict):
    ProjectArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetEntriesResponseTypeDef(TypedDict):
    DatasetEntries: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StartModelPackagingJobResponseTypeDef(TypedDict):
    JobName: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartModelResponseTypeDef(TypedDict):
    Status: ModelHostingStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopModelResponseTypeDef(TypedDict):
    Status: ModelHostingStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDatasetEntriesResponseTypeDef(TypedDict):
    Status: DatasetStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateProjectResponseTypeDef(TypedDict):
    ProjectMetadata: ProjectMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectsResponseTypeDef(TypedDict):
    Projects: List[ProjectMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DatasetDescriptionTypeDef(TypedDict):
    ProjectName: NotRequired[str]
    DatasetType: NotRequired[str]
    CreationTimestamp: NotRequired[datetime]
    LastUpdatedTimestamp: NotRequired[datetime]
    Status: NotRequired[DatasetStatusType]
    StatusMessage: NotRequired[str]
    ImageStats: NotRequired[DatasetImageStatsTypeDef]

class DatasetGroundTruthManifestTypeDef(TypedDict):
    S3Object: NotRequired[InputS3ObjectTypeDef]

class OutputConfigTypeDef(TypedDict):
    S3Location: S3LocationTypeDef

class GreengrassConfigurationOutputTypeDef(TypedDict):
    S3OutputLocation: S3LocationTypeDef
    ComponentName: str
    CompilerOptions: NotRequired[str]
    TargetDevice: NotRequired[Literal["jetson_xavier"]]
    TargetPlatform: NotRequired[TargetPlatformTypeDef]
    ComponentVersion: NotRequired[str]
    ComponentDescription: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

class GreengrassConfigurationTypeDef(TypedDict):
    S3OutputLocation: S3LocationTypeDef
    ComponentName: str
    CompilerOptions: NotRequired[str]
    TargetDevice: NotRequired[Literal["jetson_xavier"]]
    TargetPlatform: NotRequired[TargetPlatformTypeDef]
    ComponentVersion: NotRequired[str]
    ComponentDescription: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ModelPackagingOutputDetailsTypeDef(TypedDict):
    Greengrass: NotRequired[GreengrassOutputDetailsTypeDef]

class ListModelPackagingJobsRequestPaginateTypeDef(TypedDict):
    ProjectName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListModelsRequestPaginateTypeDef(TypedDict):
    ProjectName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProjectsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDatasetEntriesRequestPaginateTypeDef(TypedDict):
    ProjectName: str
    DatasetType: str
    Labeled: NotRequired[bool]
    AnomalyClass: NotRequired[str]
    BeforeCreationDate: NotRequired[TimestampTypeDef]
    AfterCreationDate: NotRequired[TimestampTypeDef]
    SourceRefContains: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDatasetEntriesRequestTypeDef(TypedDict):
    ProjectName: str
    DatasetType: str
    Labeled: NotRequired[bool]
    AnomalyClass: NotRequired[str]
    BeforeCreationDate: NotRequired[TimestampTypeDef]
    AfterCreationDate: NotRequired[TimestampTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    SourceRefContains: NotRequired[str]

class ListModelPackagingJobsResponseTypeDef(TypedDict):
    ModelPackagingJobs: List[ModelPackagingJobMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ModelMetadataTypeDef(TypedDict):
    CreationTimestamp: NotRequired[datetime]
    ModelVersion: NotRequired[str]
    ModelArn: NotRequired[str]
    Description: NotRequired[str]
    Status: NotRequired[ModelStatusType]
    StatusMessage: NotRequired[str]
    Performance: NotRequired[ModelPerformanceTypeDef]

class DetectAnomalyResultTypeDef(TypedDict):
    Source: NotRequired[ImageSourceTypeDef]
    IsAnomalous: NotRequired[bool]
    Confidence: NotRequired[float]
    Anomalies: NotRequired[List[AnomalyTypeDef]]
    AnomalyMask: NotRequired[bytes]

class DescribeProjectResponseTypeDef(TypedDict):
    ProjectDescription: ProjectDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDatasetResponseTypeDef(TypedDict):
    DatasetDescription: DatasetDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DatasetSourceTypeDef(TypedDict):
    GroundTruthManifest: NotRequired[DatasetGroundTruthManifestTypeDef]

class CreateModelRequestTypeDef(TypedDict):
    ProjectName: str
    OutputConfig: OutputConfigTypeDef
    Description: NotRequired[str]
    ClientToken: NotRequired[str]
    KmsKeyId: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ModelDescriptionTypeDef(TypedDict):
    ModelVersion: NotRequired[str]
    ModelArn: NotRequired[str]
    CreationTimestamp: NotRequired[datetime]
    Description: NotRequired[str]
    Status: NotRequired[ModelStatusType]
    StatusMessage: NotRequired[str]
    Performance: NotRequired[ModelPerformanceTypeDef]
    OutputConfig: NotRequired[OutputConfigTypeDef]
    EvaluationManifest: NotRequired[OutputS3ObjectTypeDef]
    EvaluationResult: NotRequired[OutputS3ObjectTypeDef]
    EvaluationEndTimestamp: NotRequired[datetime]
    KmsKeyId: NotRequired[str]
    MinInferenceUnits: NotRequired[int]
    MaxInferenceUnits: NotRequired[int]

class ModelPackagingConfigurationOutputTypeDef(TypedDict):
    Greengrass: GreengrassConfigurationOutputTypeDef

class ModelPackagingConfigurationTypeDef(TypedDict):
    Greengrass: GreengrassConfigurationTypeDef

class CreateModelResponseTypeDef(TypedDict):
    ModelMetadata: ModelMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListModelsResponseTypeDef(TypedDict):
    Models: List[ModelMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DetectAnomaliesResponseTypeDef(TypedDict):
    DetectAnomalyResult: DetectAnomalyResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetRequestTypeDef(TypedDict):
    ProjectName: str
    DatasetType: str
    DatasetSource: NotRequired[DatasetSourceTypeDef]
    ClientToken: NotRequired[str]

class DescribeModelResponseTypeDef(TypedDict):
    ModelDescription: ModelDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModelPackagingDescriptionTypeDef(TypedDict):
    JobName: NotRequired[str]
    ProjectName: NotRequired[str]
    ModelVersion: NotRequired[str]
    ModelPackagingConfiguration: NotRequired[ModelPackagingConfigurationOutputTypeDef]
    ModelPackagingJobDescription: NotRequired[str]
    ModelPackagingMethod: NotRequired[str]
    ModelPackagingOutputDetails: NotRequired[ModelPackagingOutputDetailsTypeDef]
    Status: NotRequired[ModelPackagingJobStatusType]
    StatusMessage: NotRequired[str]
    CreationTimestamp: NotRequired[datetime]
    LastUpdatedTimestamp: NotRequired[datetime]

ModelPackagingConfigurationUnionTypeDef = Union[
    ModelPackagingConfigurationTypeDef, ModelPackagingConfigurationOutputTypeDef
]

class DescribeModelPackagingJobResponseTypeDef(TypedDict):
    ModelPackagingDescription: ModelPackagingDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartModelPackagingJobRequestTypeDef(TypedDict):
    ProjectName: str
    ModelVersion: str
    Configuration: ModelPackagingConfigurationUnionTypeDef
    JobName: NotRequired[str]
    Description: NotRequired[str]
    ClientToken: NotRequired[str]
