"""
Type annotations for textract service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/type_defs.html)

Usage::

    ```python
    from mypy_boto3_textract.type_defs import AdapterOverviewTypeDef

    data: AdapterOverviewTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AdapterVersionStatusType,
    AutoUpdateType,
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
    "AdapterOverviewTypeDef",
    "AdapterTypeDef",
    "AdapterVersionDatasetConfigTypeDef",
    "AdapterVersionEvaluationMetricTypeDef",
    "AdapterVersionOverviewTypeDef",
    "AdaptersConfigTypeDef",
    "AnalyzeDocumentRequestRequestTypeDef",
    "AnalyzeDocumentResponseTypeDef",
    "AnalyzeExpenseRequestRequestTypeDef",
    "AnalyzeExpenseResponseTypeDef",
    "AnalyzeIDDetectionsTypeDef",
    "AnalyzeIDRequestRequestTypeDef",
    "AnalyzeIDResponseTypeDef",
    "BlockTypeDef",
    "BoundingBoxTypeDef",
    "CreateAdapterRequestRequestTypeDef",
    "CreateAdapterResponseTypeDef",
    "CreateAdapterVersionRequestRequestTypeDef",
    "CreateAdapterVersionResponseTypeDef",
    "DeleteAdapterRequestRequestTypeDef",
    "DeleteAdapterVersionRequestRequestTypeDef",
    "DetectDocumentTextRequestRequestTypeDef",
    "DetectDocumentTextResponseTypeDef",
    "DetectedSignatureTypeDef",
    "DocumentGroupTypeDef",
    "DocumentLocationTypeDef",
    "DocumentMetadataTypeDef",
    "DocumentTypeDef",
    "EvaluationMetricTypeDef",
    "ExpenseCurrencyTypeDef",
    "ExpenseDetectionTypeDef",
    "ExpenseDocumentTypeDef",
    "ExpenseFieldTypeDef",
    "ExpenseGroupPropertyTypeDef",
    "ExpenseTypeTypeDef",
    "ExtractionTypeDef",
    "GeometryTypeDef",
    "GetAdapterRequestRequestTypeDef",
    "GetAdapterResponseTypeDef",
    "GetAdapterVersionRequestRequestTypeDef",
    "GetAdapterVersionResponseTypeDef",
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
    "ListAdapterVersionsRequestRequestTypeDef",
    "ListAdapterVersionsResponseTypeDef",
    "ListAdaptersRequestRequestTypeDef",
    "ListAdaptersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NormalizedValueTypeDef",
    "NotificationChannelTypeDef",
    "OutputConfigTypeDef",
    "PageClassificationTypeDef",
    "PaginatorConfigTypeDef",
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
    "TagResourceRequestRequestTypeDef",
    "UndetectedSignatureTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAdapterRequestRequestTypeDef",
    "UpdateAdapterResponseTypeDef",
    "WarningTypeDef",
)

AdapterOverviewTypeDef = TypedDict(
    "AdapterOverviewTypeDef",
    {
        "AdapterId": str,
        "AdapterName": str,
        "CreationTime": datetime,
        "FeatureTypes": List[FeatureTypeType],
    },
    total=False,
)

_RequiredAdapterTypeDef = TypedDict(
    "_RequiredAdapterTypeDef",
    {
        "AdapterId": str,
        "Version": str,
    },
)
_OptionalAdapterTypeDef = TypedDict(
    "_OptionalAdapterTypeDef",
    {
        "Pages": List[str],
    },
    total=False,
)

class AdapterTypeDef(_RequiredAdapterTypeDef, _OptionalAdapterTypeDef):
    pass

AdapterVersionDatasetConfigTypeDef = TypedDict(
    "AdapterVersionDatasetConfigTypeDef",
    {
        "ManifestS3Object": "S3ObjectTypeDef",
    },
    total=False,
)

AdapterVersionEvaluationMetricTypeDef = TypedDict(
    "AdapterVersionEvaluationMetricTypeDef",
    {
        "Baseline": "EvaluationMetricTypeDef",
        "AdapterVersion": "EvaluationMetricTypeDef",
        "FeatureType": FeatureTypeType,
    },
    total=False,
)

AdapterVersionOverviewTypeDef = TypedDict(
    "AdapterVersionOverviewTypeDef",
    {
        "AdapterId": str,
        "AdapterVersion": str,
        "CreationTime": datetime,
        "FeatureTypes": List[FeatureTypeType],
        "Status": AdapterVersionStatusType,
        "StatusMessage": str,
    },
    total=False,
)

AdaptersConfigTypeDef = TypedDict(
    "AdaptersConfigTypeDef",
    {
        "Adapters": List["AdapterTypeDef"],
    },
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
        "AdaptersConfig": "AdaptersConfigTypeDef",
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

_RequiredCreateAdapterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAdapterRequestRequestTypeDef",
    {
        "AdapterName": str,
        "FeatureTypes": List[FeatureTypeType],
    },
)
_OptionalCreateAdapterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAdapterRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Description": str,
        "AutoUpdate": AutoUpdateType,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateAdapterRequestRequestTypeDef(
    _RequiredCreateAdapterRequestRequestTypeDef, _OptionalCreateAdapterRequestRequestTypeDef
):
    pass

CreateAdapterResponseTypeDef = TypedDict(
    "CreateAdapterResponseTypeDef",
    {
        "AdapterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAdapterVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAdapterVersionRequestRequestTypeDef",
    {
        "AdapterId": str,
        "DatasetConfig": "AdapterVersionDatasetConfigTypeDef",
        "OutputConfig": "OutputConfigTypeDef",
    },
)
_OptionalCreateAdapterVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAdapterVersionRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "KMSKeyId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateAdapterVersionRequestRequestTypeDef(
    _RequiredCreateAdapterVersionRequestRequestTypeDef,
    _OptionalCreateAdapterVersionRequestRequestTypeDef,
):
    pass

CreateAdapterVersionResponseTypeDef = TypedDict(
    "CreateAdapterVersionResponseTypeDef",
    {
        "AdapterId": str,
        "AdapterVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAdapterRequestRequestTypeDef = TypedDict(
    "DeleteAdapterRequestRequestTypeDef",
    {
        "AdapterId": str,
    },
)

DeleteAdapterVersionRequestRequestTypeDef = TypedDict(
    "DeleteAdapterVersionRequestRequestTypeDef",
    {
        "AdapterId": str,
        "AdapterVersion": str,
    },
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

EvaluationMetricTypeDef = TypedDict(
    "EvaluationMetricTypeDef",
    {
        "F1Score": float,
        "Precision": float,
        "Recall": float,
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

GetAdapterRequestRequestTypeDef = TypedDict(
    "GetAdapterRequestRequestTypeDef",
    {
        "AdapterId": str,
    },
)

GetAdapterResponseTypeDef = TypedDict(
    "GetAdapterResponseTypeDef",
    {
        "AdapterId": str,
        "AdapterName": str,
        "CreationTime": datetime,
        "Description": str,
        "FeatureTypes": List[FeatureTypeType],
        "AutoUpdate": AutoUpdateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAdapterVersionRequestRequestTypeDef = TypedDict(
    "GetAdapterVersionRequestRequestTypeDef",
    {
        "AdapterId": str,
        "AdapterVersion": str,
    },
)

GetAdapterVersionResponseTypeDef = TypedDict(
    "GetAdapterVersionResponseTypeDef",
    {
        "AdapterId": str,
        "AdapterVersion": str,
        "CreationTime": datetime,
        "FeatureTypes": List[FeatureTypeType],
        "Status": AdapterVersionStatusType,
        "StatusMessage": str,
        "DatasetConfig": "AdapterVersionDatasetConfigTypeDef",
        "KMSKeyId": str,
        "OutputConfig": "OutputConfigTypeDef",
        "EvaluationMetrics": List["AdapterVersionEvaluationMetricTypeDef"],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ListAdapterVersionsRequestRequestTypeDef = TypedDict(
    "ListAdapterVersionsRequestRequestTypeDef",
    {
        "AdapterId": str,
        "AfterCreationTime": Union[datetime, str],
        "BeforeCreationTime": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAdapterVersionsResponseTypeDef = TypedDict(
    "ListAdapterVersionsResponseTypeDef",
    {
        "AdapterVersions": List["AdapterVersionOverviewTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAdaptersRequestRequestTypeDef = TypedDict(
    "ListAdaptersRequestRequestTypeDef",
    {
        "AfterCreationTime": Union[datetime, str],
        "BeforeCreationTime": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAdaptersResponseTypeDef = TypedDict(
    "ListAdaptersResponseTypeDef",
    {
        "Adapters": List["AdapterOverviewTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
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
        "AdaptersConfig": "AdaptersConfigTypeDef",
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Dict[str, str],
    },
)

UndetectedSignatureTypeDef = TypedDict(
    "UndetectedSignatureTypeDef",
    {
        "Page": int,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAdapterRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAdapterRequestRequestTypeDef",
    {
        "AdapterId": str,
    },
)
_OptionalUpdateAdapterRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAdapterRequestRequestTypeDef",
    {
        "Description": str,
        "AdapterName": str,
        "AutoUpdate": AutoUpdateType,
    },
    total=False,
)

class UpdateAdapterRequestRequestTypeDef(
    _RequiredUpdateAdapterRequestRequestTypeDef, _OptionalUpdateAdapterRequestRequestTypeDef
):
    pass

UpdateAdapterResponseTypeDef = TypedDict(
    "UpdateAdapterResponseTypeDef",
    {
        "AdapterId": str,
        "AdapterName": str,
        "CreationTime": datetime,
        "Description": str,
        "FeatureTypes": List[FeatureTypeType],
        "AutoUpdate": AutoUpdateType,
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
