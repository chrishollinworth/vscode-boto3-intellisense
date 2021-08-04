"""
Type annotations for textract service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/type_defs.html)

Usage::

    ```python
    from mypy_boto3_textract.type_defs import AnalyzeDocumentRequestRequestTypeDef

    data: AnalyzeDocumentRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    BlockTypeType,
    ContentClassifierType,
    EntityTypeType,
    FeatureTypeType,
    JobStatusType,
    RelationshipTypeType,
    SelectionStatusType,
    TextTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AnalyzeDocumentRequestRequestTypeDef",
    "AnalyzeDocumentResponseTypeDef",
    "AnalyzeExpenseRequestRequestTypeDef",
    "AnalyzeExpenseResponseTypeDef",
    "BlockTypeDef",
    "BoundingBoxTypeDef",
    "DetectDocumentTextRequestRequestTypeDef",
    "DetectDocumentTextResponseTypeDef",
    "DocumentLocationTypeDef",
    "DocumentMetadataTypeDef",
    "DocumentTypeDef",
    "ExpenseDetectionTypeDef",
    "ExpenseDocumentTypeDef",
    "ExpenseFieldTypeDef",
    "ExpenseTypeTypeDef",
    "GeometryTypeDef",
    "GetDocumentAnalysisRequestRequestTypeDef",
    "GetDocumentAnalysisResponseTypeDef",
    "GetDocumentTextDetectionRequestRequestTypeDef",
    "GetDocumentTextDetectionResponseTypeDef",
    "HumanLoopActivationOutputTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "LineItemFieldsTypeDef",
    "LineItemGroupTypeDef",
    "NotificationChannelTypeDef",
    "OutputConfigTypeDef",
    "PointTypeDef",
    "RelationshipTypeDef",
    "ResponseMetadataTypeDef",
    "S3ObjectTypeDef",
    "StartDocumentAnalysisRequestRequestTypeDef",
    "StartDocumentAnalysisResponseTypeDef",
    "StartDocumentTextDetectionRequestRequestTypeDef",
    "StartDocumentTextDetectionResponseTypeDef",
    "WarningTypeDef",
)

_RequiredAnalyzeDocumentRequestRequestTypeDef = TypedDict(
    "_RequiredAnalyzeDocumentRequestRequestTypeDef",
    {
        "Document": "DocumentTypeDef",
        "FeatureTypes": List[FeatureTypeType],
    },
)
_OptionalAnalyzeDocumentRequestRequestTypeDef = TypedDict(
    "_OptionalAnalyzeDocumentRequestRequestTypeDef",
    {
        "HumanLoopConfig": "HumanLoopConfigTypeDef",
    },
    total=False,
)

class AnalyzeDocumentRequestRequestTypeDef(
    _RequiredAnalyzeDocumentRequestRequestTypeDef, _OptionalAnalyzeDocumentRequestRequestTypeDef
):
    pass

AnalyzeDocumentResponseTypeDef = TypedDict(
    "AnalyzeDocumentResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "Blocks": List["BlockTypeDef"],
        "HumanLoopActivationOutput": "HumanLoopActivationOutputTypeDef",
        "AnalyzeDocumentModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AnalyzeExpenseRequestRequestTypeDef = TypedDict(
    "AnalyzeExpenseRequestRequestTypeDef",
    {
        "Document": "DocumentTypeDef",
    },
)

AnalyzeExpenseResponseTypeDef = TypedDict(
    "AnalyzeExpenseResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "ExpenseDocuments": List["ExpenseDocumentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlockTypeDef = TypedDict(
    "BlockTypeDef",
    {
        "BlockType": BlockTypeType,
        "Confidence": float,
        "Text": str,
        "TextType": TextTypeType,
        "RowIndex": int,
        "ColumnIndex": int,
        "RowSpan": int,
        "ColumnSpan": int,
        "Geometry": "GeometryTypeDef",
        "Id": str,
        "Relationships": List["RelationshipTypeDef"],
        "EntityTypes": List[EntityTypeType],
        "SelectionStatus": SelectionStatusType,
        "Page": int,
    },
    total=False,
)

BoundingBoxTypeDef = TypedDict(
    "BoundingBoxTypeDef",
    {
        "Width": float,
        "Height": float,
        "Left": float,
        "Top": float,
    },
    total=False,
)

DetectDocumentTextRequestRequestTypeDef = TypedDict(
    "DetectDocumentTextRequestRequestTypeDef",
    {
        "Document": "DocumentTypeDef",
    },
)

DetectDocumentTextResponseTypeDef = TypedDict(
    "DetectDocumentTextResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "Blocks": List["BlockTypeDef"],
        "DetectDocumentTextModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentLocationTypeDef = TypedDict(
    "DocumentLocationTypeDef",
    {
        "S3Object": "S3ObjectTypeDef",
    },
    total=False,
)

DocumentMetadataTypeDef = TypedDict(
    "DocumentMetadataTypeDef",
    {
        "Pages": int,
    },
    total=False,
)

DocumentTypeDef = TypedDict(
    "DocumentTypeDef",
    {
        "Bytes": Union[bytes, IO[bytes], StreamingBody],
        "S3Object": "S3ObjectTypeDef",
    },
    total=False,
)

ExpenseDetectionTypeDef = TypedDict(
    "ExpenseDetectionTypeDef",
    {
        "Text": str,
        "Geometry": "GeometryTypeDef",
        "Confidence": float,
    },
    total=False,
)

ExpenseDocumentTypeDef = TypedDict(
    "ExpenseDocumentTypeDef",
    {
        "ExpenseIndex": int,
        "SummaryFields": List["ExpenseFieldTypeDef"],
        "LineItemGroups": List["LineItemGroupTypeDef"],
    },
    total=False,
)

ExpenseFieldTypeDef = TypedDict(
    "ExpenseFieldTypeDef",
    {
        "Type": "ExpenseTypeTypeDef",
        "LabelDetection": "ExpenseDetectionTypeDef",
        "ValueDetection": "ExpenseDetectionTypeDef",
        "PageNumber": int,
    },
    total=False,
)

ExpenseTypeTypeDef = TypedDict(
    "ExpenseTypeTypeDef",
    {
        "Text": str,
        "Confidence": float,
    },
    total=False,
)

GeometryTypeDef = TypedDict(
    "GeometryTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
        "Polygon": List["PointTypeDef"],
    },
    total=False,
)

_RequiredGetDocumentAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredGetDocumentAnalysisRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetDocumentAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalGetDocumentAnalysisRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetDocumentAnalysisRequestRequestTypeDef(
    _RequiredGetDocumentAnalysisRequestRequestTypeDef,
    _OptionalGetDocumentAnalysisRequestRequestTypeDef,
):
    pass

GetDocumentAnalysisResponseTypeDef = TypedDict(
    "GetDocumentAnalysisResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "JobStatus": JobStatusType,
        "NextToken": str,
        "Blocks": List["BlockTypeDef"],
        "Warnings": List["WarningTypeDef"],
        "StatusMessage": str,
        "AnalyzeDocumentModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDocumentTextDetectionRequestRequestTypeDef = TypedDict(
    "_RequiredGetDocumentTextDetectionRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetDocumentTextDetectionRequestRequestTypeDef = TypedDict(
    "_OptionalGetDocumentTextDetectionRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetDocumentTextDetectionRequestRequestTypeDef(
    _RequiredGetDocumentTextDetectionRequestRequestTypeDef,
    _OptionalGetDocumentTextDetectionRequestRequestTypeDef,
):
    pass

GetDocumentTextDetectionResponseTypeDef = TypedDict(
    "GetDocumentTextDetectionResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "JobStatus": JobStatusType,
        "NextToken": str,
        "Blocks": List["BlockTypeDef"],
        "Warnings": List["WarningTypeDef"],
        "StatusMessage": str,
        "DetectDocumentTextModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredHumanLoopConfigTypeDef = TypedDict(
    "_RequiredHumanLoopConfigTypeDef",
    {
        "HumanLoopName": str,
        "FlowDefinitionArn": str,
    },
)
_OptionalHumanLoopConfigTypeDef = TypedDict(
    "_OptionalHumanLoopConfigTypeDef",
    {
        "DataAttributes": "HumanLoopDataAttributesTypeDef",
    },
    total=False,
)

class HumanLoopConfigTypeDef(_RequiredHumanLoopConfigTypeDef, _OptionalHumanLoopConfigTypeDef):
    pass

HumanLoopDataAttributesTypeDef = TypedDict(
    "HumanLoopDataAttributesTypeDef",
    {
        "ContentClassifiers": List[ContentClassifierType],
    },
    total=False,
)

LineItemFieldsTypeDef = TypedDict(
    "LineItemFieldsTypeDef",
    {
        "LineItemExpenseFields": List["ExpenseFieldTypeDef"],
    },
    total=False,
)

LineItemGroupTypeDef = TypedDict(
    "LineItemGroupTypeDef",
    {
        "LineItemGroupIndex": int,
        "LineItems": List["LineItemFieldsTypeDef"],
    },
    total=False,
)

NotificationChannelTypeDef = TypedDict(
    "NotificationChannelTypeDef",
    {
        "SNSTopicArn": str,
        "RoleArn": str,
    },
)

_RequiredOutputConfigTypeDef = TypedDict(
    "_RequiredOutputConfigTypeDef",
    {
        "S3Bucket": str,
    },
)
_OptionalOutputConfigTypeDef = TypedDict(
    "_OptionalOutputConfigTypeDef",
    {
        "S3Prefix": str,
    },
    total=False,
)

class OutputConfigTypeDef(_RequiredOutputConfigTypeDef, _OptionalOutputConfigTypeDef):
    pass

PointTypeDef = TypedDict(
    "PointTypeDef",
    {
        "X": float,
        "Y": float,
    },
    total=False,
)

RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "Type": RelationshipTypeType,
        "Ids": List[str],
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

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "Bucket": str,
        "Name": str,
        "Version": str,
    },
    total=False,
)

_RequiredStartDocumentAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredStartDocumentAnalysisRequestRequestTypeDef",
    {
        "DocumentLocation": "DocumentLocationTypeDef",
        "FeatureTypes": List[FeatureTypeType],
    },
)
_OptionalStartDocumentAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalStartDocumentAnalysisRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "JobTag": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "OutputConfig": "OutputConfigTypeDef",
        "KMSKeyId": str,
    },
    total=False,
)

class StartDocumentAnalysisRequestRequestTypeDef(
    _RequiredStartDocumentAnalysisRequestRequestTypeDef,
    _OptionalStartDocumentAnalysisRequestRequestTypeDef,
):
    pass

StartDocumentAnalysisResponseTypeDef = TypedDict(
    "StartDocumentAnalysisResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartDocumentTextDetectionRequestRequestTypeDef = TypedDict(
    "_RequiredStartDocumentTextDetectionRequestRequestTypeDef",
    {
        "DocumentLocation": "DocumentLocationTypeDef",
    },
)
_OptionalStartDocumentTextDetectionRequestRequestTypeDef = TypedDict(
    "_OptionalStartDocumentTextDetectionRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "JobTag": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "OutputConfig": "OutputConfigTypeDef",
        "KMSKeyId": str,
    },
    total=False,
)

class StartDocumentTextDetectionRequestRequestTypeDef(
    _RequiredStartDocumentTextDetectionRequestRequestTypeDef,
    _OptionalStartDocumentTextDetectionRequestRequestTypeDef,
):
    pass

StartDocumentTextDetectionResponseTypeDef = TypedDict(
    "StartDocumentTextDetectionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WarningTypeDef = TypedDict(
    "WarningTypeDef",
    {
        "ErrorCode": str,
        "Pages": List[int],
    },
    total=False,
)
