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
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AnalyzeDocumentRequestRequestTypeDef",
    "AnalyzeDocumentResponseTypeDef",
    "AnalyzeExpenseRequestRequestTypeDef",
    "AnalyzeExpenseResponseTypeDef",
    "AnalyzeIDDetectionsTypeDef",
    "AnalyzeIDRequestRequestTypeDef",
    "AnalyzeIDResponseTypeDef",
    "BlockTypeDef",
    "BoundingBoxTypeDef",
    "DetectDocumentTextRequestRequestTypeDef",
    "DetectDocumentTextResponseTypeDef",
    "DetectedSignatureTypeDef",
    "DocumentGroupTypeDef",
    "DocumentLocationTypeDef",
    "DocumentMetadataTypeDef",
    "DocumentTypeDef",
    "ExpenseCurrencyTypeDef",
    "ExpenseDetectionTypeDef",
    "ExpenseDocumentTypeDef",
    "ExpenseFieldTypeDef",
    "ExpenseGroupPropertyTypeDef",
    "ExpenseTypeTypeDef",
    "ExtractionTypeDef",
    "GeometryTypeDef",
    "GetDocumentAnalysisRequestRequestTypeDef",
    "GetDocumentAnalysisResponseTypeDef",
    "GetDocumentTextDetectionRequestRequestTypeDef",
    "GetDocumentTextDetectionResponseTypeDef",
    "GetExpenseAnalysisRequestRequestTypeDef",
    "GetExpenseAnalysisResponseTypeDef",
    "GetLendingAnalysisRequestRequestTypeDef",
    "GetLendingAnalysisResponseTypeDef",
    "GetLendingAnalysisSummaryRequestRequestTypeDef",
    "GetLendingAnalysisSummaryResponseTypeDef",
    "HumanLoopActivationOutputTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "IdentityDocumentFieldTypeDef",
    "IdentityDocumentTypeDef",
    "LendingDetectionTypeDef",
    "LendingDocumentTypeDef",
    "LendingFieldTypeDef",
    "LendingResultTypeDef",
    "LendingSummaryTypeDef",
    "LineItemFieldsTypeDef",
    "LineItemGroupTypeDef",
    "NormalizedValueTypeDef",
    "NotificationChannelTypeDef",
    "OutputConfigTypeDef",
    "PageClassificationTypeDef",
    "PointTypeDef",
    "PredictionTypeDef",
    "QueriesConfigTypeDef",
    "QueryTypeDef",
    "RelationshipTypeDef",
    "ResponseMetadataTypeDef",
    "S3ObjectTypeDef",
    "SignatureDetectionTypeDef",
    "SplitDocumentTypeDef",
    "StartDocumentAnalysisRequestRequestTypeDef",
    "StartDocumentAnalysisResponseTypeDef",
    "StartDocumentTextDetectionRequestRequestTypeDef",
    "StartDocumentTextDetectionResponseTypeDef",
    "StartExpenseAnalysisRequestRequestTypeDef",
    "StartExpenseAnalysisResponseTypeDef",
    "StartLendingAnalysisRequestRequestTypeDef",
    "StartLendingAnalysisResponseTypeDef",
    "UndetectedSignatureTypeDef",
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
        "QueriesConfig": "QueriesConfigTypeDef",
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

_RequiredAnalyzeIDDetectionsTypeDef = TypedDict(
    "_RequiredAnalyzeIDDetectionsTypeDef",
    {
        "Text": str,
    },
)
_OptionalAnalyzeIDDetectionsTypeDef = TypedDict(
    "_OptionalAnalyzeIDDetectionsTypeDef",
    {
        "NormalizedValue": "NormalizedValueTypeDef",
        "Confidence": float,
    },
    total=False,
)

class AnalyzeIDDetectionsTypeDef(
    _RequiredAnalyzeIDDetectionsTypeDef, _OptionalAnalyzeIDDetectionsTypeDef
):
    pass

AnalyzeIDRequestRequestTypeDef = TypedDict(
    "AnalyzeIDRequestRequestTypeDef",
    {
        "DocumentPages": List["DocumentTypeDef"],
    },
)

AnalyzeIDResponseTypeDef = TypedDict(
    "AnalyzeIDResponseTypeDef",
    {
        "IdentityDocuments": List["IdentityDocumentTypeDef"],
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "AnalyzeIDModelVersion": str,
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
        "Query": "QueryTypeDef",
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

DetectedSignatureTypeDef = TypedDict(
    "DetectedSignatureTypeDef",
    {
        "Page": int,
    },
    total=False,
)

DocumentGroupTypeDef = TypedDict(
    "DocumentGroupTypeDef",
    {
        "Type": str,
        "SplitDocuments": List["SplitDocumentTypeDef"],
        "DetectedSignatures": List["DetectedSignatureTypeDef"],
        "UndetectedSignatures": List["UndetectedSignatureTypeDef"],
    },
    total=False,
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

ExpenseCurrencyTypeDef = TypedDict(
    "ExpenseCurrencyTypeDef",
    {
        "Code": str,
        "Confidence": float,
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
        "Blocks": List["BlockTypeDef"],
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
        "Currency": "ExpenseCurrencyTypeDef",
        "GroupProperties": List["ExpenseGroupPropertyTypeDef"],
    },
    total=False,
)

ExpenseGroupPropertyTypeDef = TypedDict(
    "ExpenseGroupPropertyTypeDef",
    {
        "Types": List[str],
        "Id": str,
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

ExtractionTypeDef = TypedDict(
    "ExtractionTypeDef",
    {
        "LendingDocument": "LendingDocumentTypeDef",
        "ExpenseDocument": "ExpenseDocumentTypeDef",
        "IdentityDocument": "IdentityDocumentTypeDef",
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

_RequiredGetExpenseAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredGetExpenseAnalysisRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetExpenseAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalGetExpenseAnalysisRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetExpenseAnalysisRequestRequestTypeDef(
    _RequiredGetExpenseAnalysisRequestRequestTypeDef,
    _OptionalGetExpenseAnalysisRequestRequestTypeDef,
):
    pass

GetExpenseAnalysisResponseTypeDef = TypedDict(
    "GetExpenseAnalysisResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "JobStatus": JobStatusType,
        "NextToken": str,
        "ExpenseDocuments": List["ExpenseDocumentTypeDef"],
        "Warnings": List["WarningTypeDef"],
        "StatusMessage": str,
        "AnalyzeExpenseModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLendingAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredGetLendingAnalysisRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetLendingAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalGetLendingAnalysisRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetLendingAnalysisRequestRequestTypeDef(
    _RequiredGetLendingAnalysisRequestRequestTypeDef,
    _OptionalGetLendingAnalysisRequestRequestTypeDef,
):
    pass

GetLendingAnalysisResponseTypeDef = TypedDict(
    "GetLendingAnalysisResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "JobStatus": JobStatusType,
        "NextToken": str,
        "Results": List["LendingResultTypeDef"],
        "Warnings": List["WarningTypeDef"],
        "StatusMessage": str,
        "AnalyzeLendingModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLendingAnalysisSummaryRequestRequestTypeDef = TypedDict(
    "GetLendingAnalysisSummaryRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

GetLendingAnalysisSummaryResponseTypeDef = TypedDict(
    "GetLendingAnalysisSummaryResponseTypeDef",
    {
        "DocumentMetadata": "DocumentMetadataTypeDef",
        "JobStatus": JobStatusType,
        "Summary": "LendingSummaryTypeDef",
        "Warnings": List["WarningTypeDef"],
        "StatusMessage": str,
        "AnalyzeLendingModelVersion": str,
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

IdentityDocumentFieldTypeDef = TypedDict(
    "IdentityDocumentFieldTypeDef",
    {
        "Type": "AnalyzeIDDetectionsTypeDef",
        "ValueDetection": "AnalyzeIDDetectionsTypeDef",
    },
    total=False,
)

IdentityDocumentTypeDef = TypedDict(
    "IdentityDocumentTypeDef",
    {
        "DocumentIndex": int,
        "IdentityDocumentFields": List["IdentityDocumentFieldTypeDef"],
        "Blocks": List["BlockTypeDef"],
    },
    total=False,
)

LendingDetectionTypeDef = TypedDict(
    "LendingDetectionTypeDef",
    {
        "Text": str,
        "SelectionStatus": SelectionStatusType,
        "Geometry": "GeometryTypeDef",
        "Confidence": float,
    },
    total=False,
)

LendingDocumentTypeDef = TypedDict(
    "LendingDocumentTypeDef",
    {
        "LendingFields": List["LendingFieldTypeDef"],
        "SignatureDetections": List["SignatureDetectionTypeDef"],
    },
    total=False,
)

LendingFieldTypeDef = TypedDict(
    "LendingFieldTypeDef",
    {
        "Type": str,
        "KeyDetection": "LendingDetectionTypeDef",
        "ValueDetections": List["LendingDetectionTypeDef"],
    },
    total=False,
)

LendingResultTypeDef = TypedDict(
    "LendingResultTypeDef",
    {
        "Page": int,
        "PageClassification": "PageClassificationTypeDef",
        "Extractions": List["ExtractionTypeDef"],
    },
    total=False,
)

LendingSummaryTypeDef = TypedDict(
    "LendingSummaryTypeDef",
    {
        "DocumentGroups": List["DocumentGroupTypeDef"],
        "UndetectedDocumentTypes": List[str],
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

NormalizedValueTypeDef = TypedDict(
    "NormalizedValueTypeDef",
    {
        "Value": str,
        "ValueType": Literal["DATE"],
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

PageClassificationTypeDef = TypedDict(
    "PageClassificationTypeDef",
    {
        "PageType": List["PredictionTypeDef"],
        "PageNumber": List["PredictionTypeDef"],
    },
)

PointTypeDef = TypedDict(
    "PointTypeDef",
    {
        "X": float,
        "Y": float,
    },
    total=False,
)

PredictionTypeDef = TypedDict(
    "PredictionTypeDef",
    {
        "Value": str,
        "Confidence": float,
    },
    total=False,
)

QueriesConfigTypeDef = TypedDict(
    "QueriesConfigTypeDef",
    {
        "Queries": List["QueryTypeDef"],
    },
)

_RequiredQueryTypeDef = TypedDict(
    "_RequiredQueryTypeDef",
    {
        "Text": str,
    },
)
_OptionalQueryTypeDef = TypedDict(
    "_OptionalQueryTypeDef",
    {
        "Alias": str,
        "Pages": List[str],
    },
    total=False,
)

class QueryTypeDef(_RequiredQueryTypeDef, _OptionalQueryTypeDef):
    pass

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

SignatureDetectionTypeDef = TypedDict(
    "SignatureDetectionTypeDef",
    {
        "Confidence": float,
        "Geometry": "GeometryTypeDef",
    },
    total=False,
)

SplitDocumentTypeDef = TypedDict(
    "SplitDocumentTypeDef",
    {
        "Index": int,
        "Pages": List[int],
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
        "QueriesConfig": "QueriesConfigTypeDef",
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

_RequiredStartExpenseAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredStartExpenseAnalysisRequestRequestTypeDef",
    {
        "DocumentLocation": "DocumentLocationTypeDef",
    },
)
_OptionalStartExpenseAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalStartExpenseAnalysisRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "JobTag": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "OutputConfig": "OutputConfigTypeDef",
        "KMSKeyId": str,
    },
    total=False,
)

class StartExpenseAnalysisRequestRequestTypeDef(
    _RequiredStartExpenseAnalysisRequestRequestTypeDef,
    _OptionalStartExpenseAnalysisRequestRequestTypeDef,
):
    pass

StartExpenseAnalysisResponseTypeDef = TypedDict(
    "StartExpenseAnalysisResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartLendingAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredStartLendingAnalysisRequestRequestTypeDef",
    {
        "DocumentLocation": "DocumentLocationTypeDef",
    },
)
_OptionalStartLendingAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalStartLendingAnalysisRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "JobTag": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "OutputConfig": "OutputConfigTypeDef",
        "KMSKeyId": str,
    },
    total=False,
)

class StartLendingAnalysisRequestRequestTypeDef(
    _RequiredStartLendingAnalysisRequestRequestTypeDef,
    _OptionalStartLendingAnalysisRequestRequestTypeDef,
):
    pass

StartLendingAnalysisResponseTypeDef = TypedDict(
    "StartLendingAnalysisResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UndetectedSignatureTypeDef = TypedDict(
    "UndetectedSignatureTypeDef",
    {
        "Page": int,
    },
    total=False,
)

WarningTypeDef = TypedDict(
    "WarningTypeDef",
    {
        "ErrorCode": str,
        "Pages": List[int],
    },
    total=False,
)
