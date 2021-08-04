"""
Type annotations for lookoutvision service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lookoutvision.type_defs import CreateDatasetRequestRequestTypeDef

    data: CreateDatasetRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import DatasetStatusType, ModelHostingStatusType, ModelStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateModelRequestRequestTypeDef",
    "CreateModelResponseTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "DatasetDescriptionTypeDef",
    "DatasetGroundTruthManifestTypeDef",
    "DatasetImageStatsTypeDef",
    "DatasetMetadataTypeDef",
    "DatasetSourceTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteModelRequestRequestTypeDef",
    "DeleteModelResponseTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteProjectResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeModelRequestRequestTypeDef",
    "DescribeModelResponseTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "DescribeProjectResponseTypeDef",
    "DetectAnomaliesRequestRequestTypeDef",
    "DetectAnomaliesResponseTypeDef",
    "DetectAnomalyResultTypeDef",
    "ImageSourceTypeDef",
    "InputS3ObjectTypeDef",
    "ListDatasetEntriesRequestRequestTypeDef",
    "ListDatasetEntriesResponseTypeDef",
    "ListModelsRequestRequestTypeDef",
    "ListModelsResponseTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModelDescriptionTypeDef",
    "ModelMetadataTypeDef",
    "ModelPerformanceTypeDef",
    "OutputConfigTypeDef",
    "OutputS3ObjectTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectMetadataTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "StartModelRequestRequestTypeDef",
    "StartModelResponseTypeDef",
    "StopModelRequestRequestTypeDef",
    "StopModelResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatasetEntriesRequestRequestTypeDef",
    "UpdateDatasetEntriesResponseTypeDef",
)

_RequiredCreateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
    },
)
_OptionalCreateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestRequestTypeDef",
    {
        "DatasetSource": "DatasetSourceTypeDef",
        "ClientToken": str,
    },
    total=False,
)

class CreateDatasetRequestRequestTypeDef(
    _RequiredCreateDatasetRequestRequestTypeDef, _OptionalCreateDatasetRequestRequestTypeDef
):
    pass

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "DatasetMetadata": "DatasetMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelRequestRequestTypeDef",
    {
        "ProjectName": str,
        "OutputConfig": "OutputConfigTypeDef",
    },
)
_OptionalCreateModelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelRequestRequestTypeDef",
    {
        "Description": str,
        "ClientToken": str,
        "KmsKeyId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateModelRequestRequestTypeDef(
    _RequiredCreateModelRequestRequestTypeDef, _OptionalCreateModelRequestRequestTypeDef
):
    pass

CreateModelResponseTypeDef = TypedDict(
    "CreateModelResponseTypeDef",
    {
        "ModelMetadata": "ModelMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestRequestTypeDef",
    {
        "ProjectName": str,
    },
)
_OptionalCreateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class CreateProjectRequestRequestTypeDef(
    _RequiredCreateProjectRequestRequestTypeDef, _OptionalCreateProjectRequestRequestTypeDef
):
    pass

CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "ProjectMetadata": "ProjectMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatasetDescriptionTypeDef = TypedDict(
    "DatasetDescriptionTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
        "CreationTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Status": DatasetStatusType,
        "StatusMessage": str,
        "ImageStats": "DatasetImageStatsTypeDef",
    },
    total=False,
)

DatasetGroundTruthManifestTypeDef = TypedDict(
    "DatasetGroundTruthManifestTypeDef",
    {
        "S3Object": "InputS3ObjectTypeDef",
    },
    total=False,
)

DatasetImageStatsTypeDef = TypedDict(
    "DatasetImageStatsTypeDef",
    {
        "Total": int,
        "Labeled": int,
        "Normal": int,
        "Anomaly": int,
    },
    total=False,
)

DatasetMetadataTypeDef = TypedDict(
    "DatasetMetadataTypeDef",
    {
        "DatasetType": str,
        "CreationTimestamp": datetime,
        "Status": DatasetStatusType,
        "StatusMessage": str,
    },
    total=False,
)

DatasetSourceTypeDef = TypedDict(
    "DatasetSourceTypeDef",
    {
        "GroundTruthManifest": "DatasetGroundTruthManifestTypeDef",
    },
    total=False,
)

_RequiredDeleteDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDatasetRequestRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
    },
)
_OptionalDeleteDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDatasetRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class DeleteDatasetRequestRequestTypeDef(
    _RequiredDeleteDatasetRequestRequestTypeDef, _OptionalDeleteDatasetRequestRequestTypeDef
):
    pass

_RequiredDeleteModelRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteModelRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
    },
)
_OptionalDeleteModelRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteModelRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class DeleteModelRequestRequestTypeDef(
    _RequiredDeleteModelRequestRequestTypeDef, _OptionalDeleteModelRequestRequestTypeDef
):
    pass

DeleteModelResponseTypeDef = TypedDict(
    "DeleteModelResponseTypeDef",
    {
        "ModelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteProjectRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteProjectRequestRequestTypeDef",
    {
        "ProjectName": str,
    },
)
_OptionalDeleteProjectRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteProjectRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class DeleteProjectRequestRequestTypeDef(
    _RequiredDeleteProjectRequestRequestTypeDef, _OptionalDeleteProjectRequestRequestTypeDef
):
    pass

DeleteProjectResponseTypeDef = TypedDict(
    "DeleteProjectResponseTypeDef",
    {
        "ProjectArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "DatasetDescription": "DatasetDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelRequestRequestTypeDef = TypedDict(
    "DescribeModelRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
    },
)

DescribeModelResponseTypeDef = TypedDict(
    "DescribeModelResponseTypeDef",
    {
        "ModelDescription": "ModelDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "ProjectName": str,
    },
)

DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {
        "ProjectDescription": "ProjectDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectAnomaliesRequestRequestTypeDef = TypedDict(
    "DetectAnomaliesRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "ContentType": str,
    },
)

DetectAnomaliesResponseTypeDef = TypedDict(
    "DetectAnomaliesResponseTypeDef",
    {
        "DetectAnomalyResult": "DetectAnomalyResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectAnomalyResultTypeDef = TypedDict(
    "DetectAnomalyResultTypeDef",
    {
        "Source": "ImageSourceTypeDef",
        "IsAnomalous": bool,
        "Confidence": float,
    },
    total=False,
)

ImageSourceTypeDef = TypedDict(
    "ImageSourceTypeDef",
    {
        "Type": str,
    },
    total=False,
)

_RequiredInputS3ObjectTypeDef = TypedDict(
    "_RequiredInputS3ObjectTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)
_OptionalInputS3ObjectTypeDef = TypedDict(
    "_OptionalInputS3ObjectTypeDef",
    {
        "VersionId": str,
    },
    total=False,
)

class InputS3ObjectTypeDef(_RequiredInputS3ObjectTypeDef, _OptionalInputS3ObjectTypeDef):
    pass

_RequiredListDatasetEntriesRequestRequestTypeDef = TypedDict(
    "_RequiredListDatasetEntriesRequestRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
    },
)
_OptionalListDatasetEntriesRequestRequestTypeDef = TypedDict(
    "_OptionalListDatasetEntriesRequestRequestTypeDef",
    {
        "Labeled": bool,
        "AnomalyClass": str,
        "BeforeCreationDate": Union[datetime, str],
        "AfterCreationDate": Union[datetime, str],
        "NextToken": str,
        "MaxResults": int,
        "SourceRefContains": str,
    },
    total=False,
)

class ListDatasetEntriesRequestRequestTypeDef(
    _RequiredListDatasetEntriesRequestRequestTypeDef,
    _OptionalListDatasetEntriesRequestRequestTypeDef,
):
    pass

ListDatasetEntriesResponseTypeDef = TypedDict(
    "ListDatasetEntriesResponseTypeDef",
    {
        "DatasetEntries": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListModelsRequestRequestTypeDef = TypedDict(
    "_RequiredListModelsRequestRequestTypeDef",
    {
        "ProjectName": str,
    },
)
_OptionalListModelsRequestRequestTypeDef = TypedDict(
    "_OptionalListModelsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListModelsRequestRequestTypeDef(
    _RequiredListModelsRequestRequestTypeDef, _OptionalListModelsRequestRequestTypeDef
):
    pass

ListModelsResponseTypeDef = TypedDict(
    "ListModelsResponseTypeDef",
    {
        "Models": List["ModelMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "Projects": List["ProjectMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModelDescriptionTypeDef = TypedDict(
    "ModelDescriptionTypeDef",
    {
        "ModelVersion": str,
        "ModelArn": str,
        "CreationTimestamp": datetime,
        "Description": str,
        "Status": ModelStatusType,
        "StatusMessage": str,
        "Performance": "ModelPerformanceTypeDef",
        "OutputConfig": "OutputConfigTypeDef",
        "EvaluationManifest": "OutputS3ObjectTypeDef",
        "EvaluationResult": "OutputS3ObjectTypeDef",
        "EvaluationEndTimestamp": datetime,
        "KmsKeyId": str,
    },
    total=False,
)

ModelMetadataTypeDef = TypedDict(
    "ModelMetadataTypeDef",
    {
        "CreationTimestamp": datetime,
        "ModelVersion": str,
        "ModelArn": str,
        "Description": str,
        "Status": ModelStatusType,
        "StatusMessage": str,
        "Performance": "ModelPerformanceTypeDef",
    },
    total=False,
)

ModelPerformanceTypeDef = TypedDict(
    "ModelPerformanceTypeDef",
    {
        "F1Score": float,
        "Recall": float,
        "Precision": float,
    },
    total=False,
)

OutputConfigTypeDef = TypedDict(
    "OutputConfigTypeDef",
    {
        "S3Location": "S3LocationTypeDef",
    },
)

OutputS3ObjectTypeDef = TypedDict(
    "OutputS3ObjectTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
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

ProjectDescriptionTypeDef = TypedDict(
    "ProjectDescriptionTypeDef",
    {
        "ProjectArn": str,
        "ProjectName": str,
        "CreationTimestamp": datetime,
        "Datasets": List["DatasetMetadataTypeDef"],
    },
    total=False,
)

ProjectMetadataTypeDef = TypedDict(
    "ProjectMetadataTypeDef",
    {
        "ProjectArn": str,
        "ProjectName": str,
        "CreationTimestamp": datetime,
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

_RequiredS3LocationTypeDef = TypedDict(
    "_RequiredS3LocationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalS3LocationTypeDef = TypedDict(
    "_OptionalS3LocationTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)

class S3LocationTypeDef(_RequiredS3LocationTypeDef, _OptionalS3LocationTypeDef):
    pass

_RequiredStartModelRequestRequestTypeDef = TypedDict(
    "_RequiredStartModelRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
        "MinInferenceUnits": int,
    },
)
_OptionalStartModelRequestRequestTypeDef = TypedDict(
    "_OptionalStartModelRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class StartModelRequestRequestTypeDef(
    _RequiredStartModelRequestRequestTypeDef, _OptionalStartModelRequestRequestTypeDef
):
    pass

StartModelResponseTypeDef = TypedDict(
    "StartModelResponseTypeDef",
    {
        "Status": ModelHostingStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopModelRequestRequestTypeDef = TypedDict(
    "_RequiredStopModelRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
    },
)
_OptionalStopModelRequestRequestTypeDef = TypedDict(
    "_OptionalStopModelRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class StopModelRequestRequestTypeDef(
    _RequiredStopModelRequestRequestTypeDef, _OptionalStopModelRequestRequestTypeDef
):
    pass

StopModelResponseTypeDef = TypedDict(
    "StopModelResponseTypeDef",
    {
        "Status": ModelHostingStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateDatasetEntriesRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDatasetEntriesRequestRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
        "Changes": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalUpdateDatasetEntriesRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDatasetEntriesRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class UpdateDatasetEntriesRequestRequestTypeDef(
    _RequiredUpdateDatasetEntriesRequestRequestTypeDef,
    _OptionalUpdateDatasetEntriesRequestRequestTypeDef,
):
    pass

UpdateDatasetEntriesResponseTypeDef = TypedDict(
    "UpdateDatasetEntriesResponseTypeDef",
    {
        "Status": DatasetStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
