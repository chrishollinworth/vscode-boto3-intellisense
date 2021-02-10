"""
Main interface for lookoutvision service type definitions.

Usage::

    ```python
    from mypy_boto3_lookoutvision.type_defs import DatasetDescriptionTypeDef

    data: DatasetDescriptionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DatasetDescriptionTypeDef",
    "DatasetGroundTruthManifestTypeDef",
    "DatasetImageStatsTypeDef",
    "DatasetMetadataTypeDef",
    "DetectAnomalyResultTypeDef",
    "ImageSourceTypeDef",
    "InputS3ObjectTypeDef",
    "ModelDescriptionTypeDef",
    "ModelMetadataTypeDef",
    "ModelPerformanceTypeDef",
    "OutputConfigTypeDef",
    "OutputS3ObjectTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectMetadataTypeDef",
    "S3LocationTypeDef",
    "TagTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateModelResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "DatasetSourceTypeDef",
    "DeleteModelResponseTypeDef",
    "DeleteProjectResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeModelResponseTypeDef",
    "DescribeProjectResponseTypeDef",
    "DetectAnomaliesResponseTypeDef",
    "ListDatasetEntriesResponseTypeDef",
    "ListModelsResponseTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "StartModelResponseTypeDef",
    "StopModelResponseTypeDef",
    "UpdateDatasetEntriesResponseTypeDef",
)

DatasetDescriptionTypeDef = TypedDict(
    "DatasetDescriptionTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
        "CreationTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Status": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_COMPLETE",
            "CREATE_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_FAILED_ROLLBACK_IN_PROGRESS",
            "UPDATE_FAILED_ROLLBACK_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_COMPLETE",
            "DELETE_FAILED",
        ],
        "StatusMessage": str,
        "ImageStats": "DatasetImageStatsTypeDef",
    },
    total=False,
)

DatasetGroundTruthManifestTypeDef = TypedDict(
    "DatasetGroundTruthManifestTypeDef", {"S3Object": "InputS3ObjectTypeDef"}, total=False
)

DatasetImageStatsTypeDef = TypedDict(
    "DatasetImageStatsTypeDef",
    {"Total": int, "Labeled": int, "Normal": int, "Anomaly": int},
    total=False,
)

DatasetMetadataTypeDef = TypedDict(
    "DatasetMetadataTypeDef",
    {
        "DatasetType": str,
        "CreationTimestamp": datetime,
        "Status": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_COMPLETE",
            "CREATE_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_FAILED_ROLLBACK_IN_PROGRESS",
            "UPDATE_FAILED_ROLLBACK_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_COMPLETE",
            "DELETE_FAILED",
        ],
        "StatusMessage": str,
    },
    total=False,
)

DetectAnomalyResultTypeDef = TypedDict(
    "DetectAnomalyResultTypeDef",
    {"Source": "ImageSourceTypeDef", "IsAnomalous": bool, "Confidence": float},
    total=False,
)

ImageSourceTypeDef = TypedDict("ImageSourceTypeDef", {"Type": str}, total=False)

_RequiredInputS3ObjectTypeDef = TypedDict(
    "_RequiredInputS3ObjectTypeDef", {"Bucket": str, "Key": str}
)
_OptionalInputS3ObjectTypeDef = TypedDict(
    "_OptionalInputS3ObjectTypeDef", {"VersionId": str}, total=False
)


class InputS3ObjectTypeDef(_RequiredInputS3ObjectTypeDef, _OptionalInputS3ObjectTypeDef):
    pass


ModelDescriptionTypeDef = TypedDict(
    "ModelDescriptionTypeDef",
    {
        "ModelVersion": str,
        "ModelArn": str,
        "CreationTimestamp": datetime,
        "Description": str,
        "Status": Literal[
            "TRAINING",
            "TRAINED",
            "TRAINING_FAILED",
            "STARTING_HOSTING",
            "HOSTED",
            "HOSTING_FAILED",
            "STOPPING_HOSTING",
            "SYSTEM_UPDATING",
            "DELETING",
        ],
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
        "Status": Literal[
            "TRAINING",
            "TRAINED",
            "TRAINING_FAILED",
            "STARTING_HOSTING",
            "HOSTED",
            "HOSTING_FAILED",
            "STOPPING_HOSTING",
            "SYSTEM_UPDATING",
            "DELETING",
        ],
        "StatusMessage": str,
        "Performance": "ModelPerformanceTypeDef",
    },
    total=False,
)

ModelPerformanceTypeDef = TypedDict(
    "ModelPerformanceTypeDef", {"F1Score": float, "Recall": float, "Precision": float}, total=False
)

OutputConfigTypeDef = TypedDict("OutputConfigTypeDef", {"S3Location": "S3LocationTypeDef"})

OutputS3ObjectTypeDef = TypedDict("OutputS3ObjectTypeDef", {"Bucket": str, "Key": str})

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
    {"ProjectArn": str, "ProjectName": str, "CreationTimestamp": datetime},
    total=False,
)

_RequiredS3LocationTypeDef = TypedDict("_RequiredS3LocationTypeDef", {"Bucket": str})
_OptionalS3LocationTypeDef = TypedDict("_OptionalS3LocationTypeDef", {"Prefix": str}, total=False)


class S3LocationTypeDef(_RequiredS3LocationTypeDef, _OptionalS3LocationTypeDef):
    pass


TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef", {"DatasetMetadata": "DatasetMetadataTypeDef"}, total=False
)

CreateModelResponseTypeDef = TypedDict(
    "CreateModelResponseTypeDef", {"ModelMetadata": "ModelMetadataTypeDef"}, total=False
)

CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef", {"ProjectMetadata": "ProjectMetadataTypeDef"}, total=False
)

DatasetSourceTypeDef = TypedDict(
    "DatasetSourceTypeDef",
    {"GroundTruthManifest": "DatasetGroundTruthManifestTypeDef"},
    total=False,
)

DeleteModelResponseTypeDef = TypedDict("DeleteModelResponseTypeDef", {"ModelArn": str}, total=False)

DeleteProjectResponseTypeDef = TypedDict(
    "DeleteProjectResponseTypeDef", {"ProjectArn": str}, total=False
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {"DatasetDescription": "DatasetDescriptionTypeDef"},
    total=False,
)

DescribeModelResponseTypeDef = TypedDict(
    "DescribeModelResponseTypeDef", {"ModelDescription": "ModelDescriptionTypeDef"}, total=False
)

DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {"ProjectDescription": "ProjectDescriptionTypeDef"},
    total=False,
)

DetectAnomaliesResponseTypeDef = TypedDict(
    "DetectAnomaliesResponseTypeDef",
    {"DetectAnomalyResult": "DetectAnomalyResultTypeDef"},
    total=False,
)

ListDatasetEntriesResponseTypeDef = TypedDict(
    "ListDatasetEntriesResponseTypeDef",
    {"DatasetEntries": List[str], "NextToken": str},
    total=False,
)

ListModelsResponseTypeDef = TypedDict(
    "ListModelsResponseTypeDef",
    {"Models": List["ModelMetadataTypeDef"], "NextToken": str},
    total=False,
)

ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {"Projects": List["ProjectMetadataTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartModelResponseTypeDef = TypedDict(
    "StartModelResponseTypeDef",
    {"Status": Literal["RUNNING", "STARTING", "STOPPED", "FAILED"]},
    total=False,
)

StopModelResponseTypeDef = TypedDict(
    "StopModelResponseTypeDef",
    {"Status": Literal["RUNNING", "STARTING", "STOPPED", "FAILED"]},
    total=False,
)

UpdateDatasetEntriesResponseTypeDef = TypedDict(
    "UpdateDatasetEntriesResponseTypeDef",
    {
        "Status": Literal[
            "CREATE_IN_PROGRESS",
            "CREATE_COMPLETE",
            "CREATE_FAILED",
            "UPDATE_IN_PROGRESS",
            "UPDATE_COMPLETE",
            "UPDATE_FAILED_ROLLBACK_IN_PROGRESS",
            "UPDATE_FAILED_ROLLBACK_COMPLETE",
            "DELETE_IN_PROGRESS",
            "DELETE_COMPLETE",
            "DELETE_FAILED",
        ]
    },
    total=False,
)
