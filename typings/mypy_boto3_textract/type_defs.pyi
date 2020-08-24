"""
Main interface for textract service type definitions.

Usage::

    ```python
    from mypy_boto3_textract.type_defs import BlockTypeDef

    data: BlockTypeDef = {...}
    ```
"""
import sys
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
    "BlockTypeDef",
    "BoundingBoxTypeDef",
    "DocumentMetadataTypeDef",
    "GeometryTypeDef",
    "HumanLoopActivationOutputTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "PointTypeDef",
    "RelationshipTypeDef",
    "S3ObjectTypeDef",
    "WarningTypeDef",
    "AnalyzeDocumentResponseTypeDef",
    "DetectDocumentTextResponseTypeDef",
    "DocumentLocationTypeDef",
    "DocumentTypeDef",
    "GetDocumentAnalysisResponseTypeDef",
    "GetDocumentTextDetectionResponseTypeDef",
    "HumanLoopConfigTypeDef",
    "NotificationChannelTypeDef",
    "StartDocumentAnalysisResponseTypeDef",
    "StartDocumentTextDetectionResponseTypeDef",
)

BlockTypeDef = TypedDict(
    "BlockTypeDef",
    {
        "BlockType": Literal[
            "KEY_VALUE_SET", "PAGE", "LINE", "WORD", "TABLE", "CELL", "SELECTION_ELEMENT"
        ],
        "Confidence": float,
        "Text": str,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": "GeometryTypeDef",
        "Id": str,
        "Relationships": List["RelationshipTypeDef"],
        "EntityTypes": List[Literal["KEY", "VALUE"]],
        "SelectionStatus": Literal["SELECTED", "NOT_SELECTED"],
        "Page": int,
    },
    total=False,
)

BoundingBoxTypeDef = TypedDict(
    "BoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
    total=False,
)

DocumentMetadataTypeDef = TypedDict("DocumentMetadataTypeDef", {"Pages": int}, total=False)

GeometryTypeDef = TypedDict(
    "GeometryTypeDef",
    {"BoundingBox": "BoundingBoxTypeDef", "Polygon": List["PointTypeDef"]},
    total=False,
)

HumanLoopActivationOutputTypeDef = TypedDict(
    "HumanLoopActivationOutputTypeDef",
    {
        "HumanLoopArn": str,
        "HumanLoopActivationReasons": List[str],
        "HumanLoopActivationConditionsEvaluationResults": str,
    },
    total=False,
)

HumanLoopDataAttributesTypeDef = TypedDict(
    "HumanLoopDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
    total=False,
)

PointTypeDef = TypedDict("PointTypeDef", {"X": float, "Y": float}, total=False)

RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef", {"Type": Literal["VALUE", "CHILD"], "Ids": List[str]}, total=False
)

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef", {"Bucket": str, "Name": str, "Version": str}, total=False
)

WarningTypeDef = TypedDict("WarningTypeDef", {"ErrorCode": str, "Pages": List[int]}, total=False)

AnalyzeDocumentResponseTypeDef = TypedDict(
    "AnalyzeDocumentResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "Blocks": List["BlockTypeDef"],
        "HumanLoopActivationOutput": "HumanLoopActivationOutputTypeDef",
        "AnalyzeDocumentModelVersion": str,
    },
    total=False,
)

DetectDocumentTextResponseTypeDef = TypedDict(
    "DetectDocumentTextResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "Blocks": List["BlockTypeDef"],
        "DetectDocumentTextModelVersion": str,
    },
    total=False,
)

DocumentLocationTypeDef = TypedDict(
    "DocumentLocationTypeDef", {"S3Object": "S3ObjectTypeDef"}, total=False
)

DocumentTypeDef = TypedDict(
    "DocumentTypeDef", {"Bytes": bytes, "S3Object": "S3ObjectTypeDef"}, total=False
)

GetDocumentAnalysisResponseTypeDef = TypedDict(
    "GetDocumentAnalysisResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED", "PARTIAL_SUCCESS"],
        "NextToken": str,
        "Blocks": List["BlockTypeDef"],
        "Warnings": List["WarningTypeDef"],
        "StatusMessage": str,
        "AnalyzeDocumentModelVersion": str,
    },
    total=False,
)

GetDocumentTextDetectionResponseTypeDef = TypedDict(
    "GetDocumentTextDetectionResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED", "PARTIAL_SUCCESS"],
        "NextToken": str,
        "Blocks": List["BlockTypeDef"],
        "Warnings": List["WarningTypeDef"],
        "StatusMessage": str,
        "DetectDocumentTextModelVersion": str,
    },
    total=False,
)

_RequiredHumanLoopConfigTypeDef = TypedDict(
    "_RequiredHumanLoopConfigTypeDef", {"HumanLoopName": str, "FlowDefinitionArn": str}
)
_OptionalHumanLoopConfigTypeDef = TypedDict(
    "_OptionalHumanLoopConfigTypeDef",
    {"DataAttributes": "HumanLoopDataAttributesTypeDef"},
    total=False,
)


class HumanLoopConfigTypeDef(_RequiredHumanLoopConfigTypeDef, _OptionalHumanLoopConfigTypeDef):
    pass


NotificationChannelTypeDef = TypedDict(
    "NotificationChannelTypeDef", {"SNSTopicArn": str, "RoleArn": str}
)

StartDocumentAnalysisResponseTypeDef = TypedDict(
    "StartDocumentAnalysisResponseTypeDef", {"JobId": str}, total=False
)

StartDocumentTextDetectionResponseTypeDef = TypedDict(
    "StartDocumentTextDetectionResponseTypeDef", {"JobId": str}, total=False
)
