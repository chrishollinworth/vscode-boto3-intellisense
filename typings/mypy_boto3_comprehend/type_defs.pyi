"""
Type annotations for comprehend service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_comprehend/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_comprehend.type_defs import AugmentedManifestsListItemOutputTypeDef

    data: AugmentedManifestsListItemOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AugmentedManifestsDocumentTypeFormatType,
    BlockTypeType,
    DatasetDataFormatType,
    DatasetStatusType,
    DatasetTypeType,
    DocumentClassifierDataFormatType,
    DocumentClassifierDocumentTypeFormatType,
    DocumentClassifierModeType,
    DocumentReadActionType,
    DocumentReadFeatureTypesType,
    DocumentReadModeType,
    DocumentTypeType,
    EndpointStatusType,
    EntityRecognizerDataFormatType,
    EntityTypeType,
    FlywheelIterationStatusType,
    FlywheelStatusType,
    InputFormatType,
    JobStatusType,
    LanguageCodeType,
    ModelStatusType,
    ModelTypeType,
    PageBasedErrorCodeType,
    PageBasedWarningCodeType,
    PartOfSpeechTagTypeType,
    PiiEntitiesDetectionMaskModeType,
    PiiEntitiesDetectionModeType,
    PiiEntityTypeType,
    SentimentTypeType,
    SplitType,
    SyntaxLanguageCodeType,
    TargetedSentimentEntityTypeType,
    ToxicContentTypeType,
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
    "AugmentedManifestsListItemOutputTypeDef",
    "AugmentedManifestsListItemTypeDef",
    "BatchDetectDominantLanguageItemResultTypeDef",
    "BatchDetectDominantLanguageRequestTypeDef",
    "BatchDetectDominantLanguageResponseTypeDef",
    "BatchDetectEntitiesItemResultTypeDef",
    "BatchDetectEntitiesRequestTypeDef",
    "BatchDetectEntitiesResponseTypeDef",
    "BatchDetectKeyPhrasesItemResultTypeDef",
    "BatchDetectKeyPhrasesRequestTypeDef",
    "BatchDetectKeyPhrasesResponseTypeDef",
    "BatchDetectSentimentItemResultTypeDef",
    "BatchDetectSentimentRequestTypeDef",
    "BatchDetectSentimentResponseTypeDef",
    "BatchDetectSyntaxItemResultTypeDef",
    "BatchDetectSyntaxRequestTypeDef",
    "BatchDetectSyntaxResponseTypeDef",
    "BatchDetectTargetedSentimentItemResultTypeDef",
    "BatchDetectTargetedSentimentRequestTypeDef",
    "BatchDetectTargetedSentimentResponseTypeDef",
    "BatchItemErrorTypeDef",
    "BlobTypeDef",
    "BlockReferenceTypeDef",
    "BlockTypeDef",
    "BoundingBoxTypeDef",
    "ChildBlockTypeDef",
    "ClassifierEvaluationMetricsTypeDef",
    "ClassifierMetadataTypeDef",
    "ClassifyDocumentRequestTypeDef",
    "ClassifyDocumentResponseTypeDef",
    "ContainsPiiEntitiesRequestTypeDef",
    "ContainsPiiEntitiesResponseTypeDef",
    "CreateDatasetRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateDocumentClassifierRequestTypeDef",
    "CreateDocumentClassifierResponseTypeDef",
    "CreateEndpointRequestTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreateEntityRecognizerRequestTypeDef",
    "CreateEntityRecognizerResponseTypeDef",
    "CreateFlywheelRequestTypeDef",
    "CreateFlywheelResponseTypeDef",
    "DataSecurityConfigOutputTypeDef",
    "DataSecurityConfigTypeDef",
    "DataSecurityConfigUnionTypeDef",
    "DatasetAugmentedManifestsListItemTypeDef",
    "DatasetDocumentClassifierInputDataConfigTypeDef",
    "DatasetEntityRecognizerAnnotationsTypeDef",
    "DatasetEntityRecognizerDocumentsTypeDef",
    "DatasetEntityRecognizerEntityListTypeDef",
    "DatasetEntityRecognizerInputDataConfigTypeDef",
    "DatasetFilterTypeDef",
    "DatasetInputDataConfigTypeDef",
    "DatasetPropertiesTypeDef",
    "DeleteDocumentClassifierRequestTypeDef",
    "DeleteEndpointRequestTypeDef",
    "DeleteEntityRecognizerRequestTypeDef",
    "DeleteFlywheelRequestTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DescribeDatasetRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeDocumentClassificationJobRequestTypeDef",
    "DescribeDocumentClassificationJobResponseTypeDef",
    "DescribeDocumentClassifierRequestTypeDef",
    "DescribeDocumentClassifierResponseTypeDef",
    "DescribeDominantLanguageDetectionJobRequestTypeDef",
    "DescribeDominantLanguageDetectionJobResponseTypeDef",
    "DescribeEndpointRequestTypeDef",
    "DescribeEndpointResponseTypeDef",
    "DescribeEntitiesDetectionJobRequestTypeDef",
    "DescribeEntitiesDetectionJobResponseTypeDef",
    "DescribeEntityRecognizerRequestTypeDef",
    "DescribeEntityRecognizerResponseTypeDef",
    "DescribeEventsDetectionJobRequestTypeDef",
    "DescribeEventsDetectionJobResponseTypeDef",
    "DescribeFlywheelIterationRequestTypeDef",
    "DescribeFlywheelIterationResponseTypeDef",
    "DescribeFlywheelRequestTypeDef",
    "DescribeFlywheelResponseTypeDef",
    "DescribeKeyPhrasesDetectionJobRequestTypeDef",
    "DescribeKeyPhrasesDetectionJobResponseTypeDef",
    "DescribePiiEntitiesDetectionJobRequestTypeDef",
    "DescribePiiEntitiesDetectionJobResponseTypeDef",
    "DescribeResourcePolicyRequestTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DescribeSentimentDetectionJobRequestTypeDef",
    "DescribeSentimentDetectionJobResponseTypeDef",
    "DescribeTargetedSentimentDetectionJobRequestTypeDef",
    "DescribeTargetedSentimentDetectionJobResponseTypeDef",
    "DescribeTopicsDetectionJobRequestTypeDef",
    "DescribeTopicsDetectionJobResponseTypeDef",
    "DetectDominantLanguageRequestTypeDef",
    "DetectDominantLanguageResponseTypeDef",
    "DetectEntitiesRequestTypeDef",
    "DetectEntitiesResponseTypeDef",
    "DetectKeyPhrasesRequestTypeDef",
    "DetectKeyPhrasesResponseTypeDef",
    "DetectPiiEntitiesRequestTypeDef",
    "DetectPiiEntitiesResponseTypeDef",
    "DetectSentimentRequestTypeDef",
    "DetectSentimentResponseTypeDef",
    "DetectSyntaxRequestTypeDef",
    "DetectSyntaxResponseTypeDef",
    "DetectTargetedSentimentRequestTypeDef",
    "DetectTargetedSentimentResponseTypeDef",
    "DetectToxicContentRequestTypeDef",
    "DetectToxicContentResponseTypeDef",
    "DocumentClassTypeDef",
    "DocumentClassificationConfigOutputTypeDef",
    "DocumentClassificationConfigTypeDef",
    "DocumentClassificationJobFilterTypeDef",
    "DocumentClassificationJobPropertiesTypeDef",
    "DocumentClassifierDocumentsTypeDef",
    "DocumentClassifierFilterTypeDef",
    "DocumentClassifierInputDataConfigOutputTypeDef",
    "DocumentClassifierInputDataConfigTypeDef",
    "DocumentClassifierInputDataConfigUnionTypeDef",
    "DocumentClassifierOutputDataConfigTypeDef",
    "DocumentClassifierPropertiesTypeDef",
    "DocumentClassifierSummaryTypeDef",
    "DocumentLabelTypeDef",
    "DocumentMetadataTypeDef",
    "DocumentReaderConfigOutputTypeDef",
    "DocumentReaderConfigTypeDef",
    "DocumentReaderConfigUnionTypeDef",
    "DocumentTypeListItemTypeDef",
    "DominantLanguageDetectionJobFilterTypeDef",
    "DominantLanguageDetectionJobPropertiesTypeDef",
    "DominantLanguageTypeDef",
    "EndpointFilterTypeDef",
    "EndpointPropertiesTypeDef",
    "EntitiesDetectionJobFilterTypeDef",
    "EntitiesDetectionJobPropertiesTypeDef",
    "EntityLabelTypeDef",
    "EntityRecognitionConfigOutputTypeDef",
    "EntityRecognitionConfigTypeDef",
    "EntityRecognizerAnnotationsTypeDef",
    "EntityRecognizerDocumentsTypeDef",
    "EntityRecognizerEntityListTypeDef",
    "EntityRecognizerEvaluationMetricsTypeDef",
    "EntityRecognizerFilterTypeDef",
    "EntityRecognizerInputDataConfigOutputTypeDef",
    "EntityRecognizerInputDataConfigTypeDef",
    "EntityRecognizerInputDataConfigUnionTypeDef",
    "EntityRecognizerMetadataEntityTypesListItemTypeDef",
    "EntityRecognizerMetadataTypeDef",
    "EntityRecognizerOutputDataConfigTypeDef",
    "EntityRecognizerPropertiesTypeDef",
    "EntityRecognizerSummaryTypeDef",
    "EntityTypeDef",
    "EntityTypesEvaluationMetricsTypeDef",
    "EntityTypesListItemTypeDef",
    "ErrorsListItemTypeDef",
    "EventsDetectionJobFilterTypeDef",
    "EventsDetectionJobPropertiesTypeDef",
    "ExtractedCharactersListItemTypeDef",
    "FlywheelFilterTypeDef",
    "FlywheelIterationFilterTypeDef",
    "FlywheelIterationPropertiesTypeDef",
    "FlywheelModelEvaluationMetricsTypeDef",
    "FlywheelPropertiesTypeDef",
    "FlywheelSummaryTypeDef",
    "GeometryTypeDef",
    "ImportModelRequestTypeDef",
    "ImportModelResponseTypeDef",
    "InputDataConfigOutputTypeDef",
    "InputDataConfigTypeDef",
    "InputDataConfigUnionTypeDef",
    "KeyPhraseTypeDef",
    "KeyPhrasesDetectionJobFilterTypeDef",
    "KeyPhrasesDetectionJobPropertiesTypeDef",
    "ListDatasetsRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListDocumentClassificationJobsRequestPaginateTypeDef",
    "ListDocumentClassificationJobsRequestTypeDef",
    "ListDocumentClassificationJobsResponseTypeDef",
    "ListDocumentClassifierSummariesRequestTypeDef",
    "ListDocumentClassifierSummariesResponseTypeDef",
    "ListDocumentClassifiersRequestPaginateTypeDef",
    "ListDocumentClassifiersRequestTypeDef",
    "ListDocumentClassifiersResponseTypeDef",
    "ListDominantLanguageDetectionJobsRequestPaginateTypeDef",
    "ListDominantLanguageDetectionJobsRequestTypeDef",
    "ListDominantLanguageDetectionJobsResponseTypeDef",
    "ListEndpointsRequestPaginateTypeDef",
    "ListEndpointsRequestTypeDef",
    "ListEndpointsResponseTypeDef",
    "ListEntitiesDetectionJobsRequestPaginateTypeDef",
    "ListEntitiesDetectionJobsRequestTypeDef",
    "ListEntitiesDetectionJobsResponseTypeDef",
    "ListEntityRecognizerSummariesRequestTypeDef",
    "ListEntityRecognizerSummariesResponseTypeDef",
    "ListEntityRecognizersRequestPaginateTypeDef",
    "ListEntityRecognizersRequestTypeDef",
    "ListEntityRecognizersResponseTypeDef",
    "ListEventsDetectionJobsRequestTypeDef",
    "ListEventsDetectionJobsResponseTypeDef",
    "ListFlywheelIterationHistoryRequestTypeDef",
    "ListFlywheelIterationHistoryResponseTypeDef",
    "ListFlywheelsRequestTypeDef",
    "ListFlywheelsResponseTypeDef",
    "ListKeyPhrasesDetectionJobsRequestPaginateTypeDef",
    "ListKeyPhrasesDetectionJobsRequestTypeDef",
    "ListKeyPhrasesDetectionJobsResponseTypeDef",
    "ListPiiEntitiesDetectionJobsRequestPaginateTypeDef",
    "ListPiiEntitiesDetectionJobsRequestTypeDef",
    "ListPiiEntitiesDetectionJobsResponseTypeDef",
    "ListSentimentDetectionJobsRequestPaginateTypeDef",
    "ListSentimentDetectionJobsRequestTypeDef",
    "ListSentimentDetectionJobsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetedSentimentDetectionJobsRequestTypeDef",
    "ListTargetedSentimentDetectionJobsResponseTypeDef",
    "ListTopicsDetectionJobsRequestPaginateTypeDef",
    "ListTopicsDetectionJobsRequestTypeDef",
    "ListTopicsDetectionJobsResponseTypeDef",
    "MentionSentimentTypeDef",
    "OutputDataConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PartOfSpeechTagTypeDef",
    "PiiEntitiesDetectionJobFilterTypeDef",
    "PiiEntitiesDetectionJobPropertiesTypeDef",
    "PiiEntityTypeDef",
    "PiiOutputDataConfigTypeDef",
    "PointTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "RedactionConfigOutputTypeDef",
    "RedactionConfigTypeDef",
    "RedactionConfigUnionTypeDef",
    "RelationshipsListItemTypeDef",
    "ResponseMetadataTypeDef",
    "SentimentDetectionJobFilterTypeDef",
    "SentimentDetectionJobPropertiesTypeDef",
    "SentimentScoreTypeDef",
    "StartDocumentClassificationJobRequestTypeDef",
    "StartDocumentClassificationJobResponseTypeDef",
    "StartDominantLanguageDetectionJobRequestTypeDef",
    "StartDominantLanguageDetectionJobResponseTypeDef",
    "StartEntitiesDetectionJobRequestTypeDef",
    "StartEntitiesDetectionJobResponseTypeDef",
    "StartEventsDetectionJobRequestTypeDef",
    "StartEventsDetectionJobResponseTypeDef",
    "StartFlywheelIterationRequestTypeDef",
    "StartFlywheelIterationResponseTypeDef",
    "StartKeyPhrasesDetectionJobRequestTypeDef",
    "StartKeyPhrasesDetectionJobResponseTypeDef",
    "StartPiiEntitiesDetectionJobRequestTypeDef",
    "StartPiiEntitiesDetectionJobResponseTypeDef",
    "StartSentimentDetectionJobRequestTypeDef",
    "StartSentimentDetectionJobResponseTypeDef",
    "StartTargetedSentimentDetectionJobRequestTypeDef",
    "StartTargetedSentimentDetectionJobResponseTypeDef",
    "StartTopicsDetectionJobRequestTypeDef",
    "StartTopicsDetectionJobResponseTypeDef",
    "StopDominantLanguageDetectionJobRequestTypeDef",
    "StopDominantLanguageDetectionJobResponseTypeDef",
    "StopEntitiesDetectionJobRequestTypeDef",
    "StopEntitiesDetectionJobResponseTypeDef",
    "StopEventsDetectionJobRequestTypeDef",
    "StopEventsDetectionJobResponseTypeDef",
    "StopKeyPhrasesDetectionJobRequestTypeDef",
    "StopKeyPhrasesDetectionJobResponseTypeDef",
    "StopPiiEntitiesDetectionJobRequestTypeDef",
    "StopPiiEntitiesDetectionJobResponseTypeDef",
    "StopSentimentDetectionJobRequestTypeDef",
    "StopSentimentDetectionJobResponseTypeDef",
    "StopTargetedSentimentDetectionJobRequestTypeDef",
    "StopTargetedSentimentDetectionJobResponseTypeDef",
    "StopTrainingDocumentClassifierRequestTypeDef",
    "StopTrainingEntityRecognizerRequestTypeDef",
    "SyntaxTokenTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TargetedSentimentDetectionJobFilterTypeDef",
    "TargetedSentimentDetectionJobPropertiesTypeDef",
    "TargetedSentimentEntityTypeDef",
    "TargetedSentimentMentionTypeDef",
    "TaskConfigOutputTypeDef",
    "TaskConfigTypeDef",
    "TaskConfigUnionTypeDef",
    "TextSegmentTypeDef",
    "TimestampTypeDef",
    "TopicsDetectionJobFilterTypeDef",
    "TopicsDetectionJobPropertiesTypeDef",
    "ToxicContentTypeDef",
    "ToxicLabelsTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDataSecurityConfigTypeDef",
    "UpdateEndpointRequestTypeDef",
    "UpdateEndpointResponseTypeDef",
    "UpdateFlywheelRequestTypeDef",
    "UpdateFlywheelResponseTypeDef",
    "VpcConfigOutputTypeDef",
    "VpcConfigTypeDef",
    "VpcConfigUnionTypeDef",
    "WarningsListItemTypeDef",
)

class AugmentedManifestsListItemOutputTypeDef(TypedDict):
    S3Uri: str
    AttributeNames: List[str]
    Split: NotRequired[SplitType]
    AnnotationDataS3Uri: NotRequired[str]
    SourceDocumentsS3Uri: NotRequired[str]
    DocumentType: NotRequired[AugmentedManifestsDocumentTypeFormatType]

class AugmentedManifestsListItemTypeDef(TypedDict):
    S3Uri: str
    AttributeNames: Sequence[str]
    Split: NotRequired[SplitType]
    AnnotationDataS3Uri: NotRequired[str]
    SourceDocumentsS3Uri: NotRequired[str]
    DocumentType: NotRequired[AugmentedManifestsDocumentTypeFormatType]

class DominantLanguageTypeDef(TypedDict):
    LanguageCode: NotRequired[str]
    Score: NotRequired[float]

class BatchDetectDominantLanguageRequestTypeDef(TypedDict):
    TextList: Sequence[str]

class BatchItemErrorTypeDef(TypedDict):
    Index: NotRequired[int]
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BatchDetectEntitiesRequestTypeDef(TypedDict):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType

KeyPhraseTypeDef = TypedDict(
    "KeyPhraseTypeDef",
    {
        "Score": NotRequired[float],
        "Text": NotRequired[str],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
    },
)

class BatchDetectKeyPhrasesRequestTypeDef(TypedDict):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType

class SentimentScoreTypeDef(TypedDict):
    Positive: NotRequired[float]
    Negative: NotRequired[float]
    Neutral: NotRequired[float]
    Mixed: NotRequired[float]

class BatchDetectSentimentRequestTypeDef(TypedDict):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType

class BatchDetectSyntaxRequestTypeDef(TypedDict):
    TextList: Sequence[str]
    LanguageCode: SyntaxLanguageCodeType

class BatchDetectTargetedSentimentRequestTypeDef(TypedDict):
    TextList: Sequence[str]
    LanguageCode: LanguageCodeType

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class ChildBlockTypeDef(TypedDict):
    ChildBlockId: NotRequired[str]
    BeginOffset: NotRequired[int]
    EndOffset: NotRequired[int]

RelationshipsListItemTypeDef = TypedDict(
    "RelationshipsListItemTypeDef",
    {
        "Ids": NotRequired[List[str]],
        "Type": NotRequired[Literal["CHILD"]],
    },
)

class BoundingBoxTypeDef(TypedDict):
    Height: NotRequired[float]
    Left: NotRequired[float]
    Top: NotRequired[float]
    Width: NotRequired[float]

class ClassifierEvaluationMetricsTypeDef(TypedDict):
    Accuracy: NotRequired[float]
    Precision: NotRequired[float]
    Recall: NotRequired[float]
    F1Score: NotRequired[float]
    MicroPrecision: NotRequired[float]
    MicroRecall: NotRequired[float]
    MicroF1Score: NotRequired[float]
    HammingLoss: NotRequired[float]

class DocumentClassTypeDef(TypedDict):
    Name: NotRequired[str]
    Score: NotRequired[float]
    Page: NotRequired[int]

class DocumentLabelTypeDef(TypedDict):
    Name: NotRequired[str]
    Score: NotRequired[float]
    Page: NotRequired[int]

DocumentTypeListItemTypeDef = TypedDict(
    "DocumentTypeListItemTypeDef",
    {
        "Page": NotRequired[int],
        "Type": NotRequired[DocumentTypeType],
    },
)

class ErrorsListItemTypeDef(TypedDict):
    Page: NotRequired[int]
    ErrorCode: NotRequired[PageBasedErrorCodeType]
    ErrorMessage: NotRequired[str]

class WarningsListItemTypeDef(TypedDict):
    Page: NotRequired[int]
    WarnCode: NotRequired[PageBasedWarningCodeType]
    WarnMessage: NotRequired[str]

ContainsPiiEntitiesRequestTypeDef = TypedDict(
    "ContainsPiiEntitiesRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)

class EntityLabelTypeDef(TypedDict):
    Name: NotRequired[PiiEntityTypeType]
    Score: NotRequired[float]

class TagTypeDef(TypedDict):
    Key: str
    Value: NotRequired[str]

class DocumentClassifierOutputDataConfigTypeDef(TypedDict):
    S3Uri: NotRequired[str]
    KmsKeyId: NotRequired[str]
    FlywheelStatsS3Prefix: NotRequired[str]

class VpcConfigOutputTypeDef(TypedDict):
    SecurityGroupIds: List[str]
    Subnets: List[str]

class VpcConfigTypeDef(TypedDict):
    SecurityGroupIds: Sequence[str]
    Subnets: Sequence[str]

class DatasetAugmentedManifestsListItemTypeDef(TypedDict):
    AttributeNames: Sequence[str]
    S3Uri: str
    AnnotationDataS3Uri: NotRequired[str]
    SourceDocumentsS3Uri: NotRequired[str]
    DocumentType: NotRequired[AugmentedManifestsDocumentTypeFormatType]

class DatasetDocumentClassifierInputDataConfigTypeDef(TypedDict):
    S3Uri: str
    LabelDelimiter: NotRequired[str]

class DatasetEntityRecognizerAnnotationsTypeDef(TypedDict):
    S3Uri: str

class DatasetEntityRecognizerDocumentsTypeDef(TypedDict):
    S3Uri: str
    InputFormat: NotRequired[InputFormatType]

class DatasetEntityRecognizerEntityListTypeDef(TypedDict):
    S3Uri: str

TimestampTypeDef = Union[datetime, str]

class DatasetPropertiesTypeDef(TypedDict):
    DatasetArn: NotRequired[str]
    DatasetName: NotRequired[str]
    DatasetType: NotRequired[DatasetTypeType]
    DatasetS3Uri: NotRequired[str]
    Description: NotRequired[str]
    Status: NotRequired[DatasetStatusType]
    Message: NotRequired[str]
    NumberOfDocuments: NotRequired[int]
    CreationTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]

class DeleteDocumentClassifierRequestTypeDef(TypedDict):
    DocumentClassifierArn: str

class DeleteEndpointRequestTypeDef(TypedDict):
    EndpointArn: str

class DeleteEntityRecognizerRequestTypeDef(TypedDict):
    EntityRecognizerArn: str

class DeleteFlywheelRequestTypeDef(TypedDict):
    FlywheelArn: str

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: str
    PolicyRevisionId: NotRequired[str]

class DescribeDatasetRequestTypeDef(TypedDict):
    DatasetArn: str

class DescribeDocumentClassificationJobRequestTypeDef(TypedDict):
    JobId: str

class DescribeDocumentClassifierRequestTypeDef(TypedDict):
    DocumentClassifierArn: str

class DescribeDominantLanguageDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class DescribeEndpointRequestTypeDef(TypedDict):
    EndpointArn: str

class EndpointPropertiesTypeDef(TypedDict):
    EndpointArn: NotRequired[str]
    Status: NotRequired[EndpointStatusType]
    Message: NotRequired[str]
    ModelArn: NotRequired[str]
    DesiredModelArn: NotRequired[str]
    DesiredInferenceUnits: NotRequired[int]
    CurrentInferenceUnits: NotRequired[int]
    CreationTime: NotRequired[datetime]
    LastModifiedTime: NotRequired[datetime]
    DataAccessRoleArn: NotRequired[str]
    DesiredDataAccessRoleArn: NotRequired[str]
    FlywheelArn: NotRequired[str]

class DescribeEntitiesDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class DescribeEntityRecognizerRequestTypeDef(TypedDict):
    EntityRecognizerArn: str

class DescribeEventsDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class DescribeFlywheelIterationRequestTypeDef(TypedDict):
    FlywheelArn: str
    FlywheelIterationId: str

class DescribeFlywheelRequestTypeDef(TypedDict):
    FlywheelArn: str

class DescribeKeyPhrasesDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class DescribePiiEntitiesDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class DescribeResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: str

class DescribeSentimentDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class DescribeTargetedSentimentDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class DescribeTopicsDetectionJobRequestTypeDef(TypedDict):
    JobId: str

DetectDominantLanguageRequestTypeDef = TypedDict(
    "DetectDominantLanguageRequestTypeDef",
    {
        "Text": str,
    },
)
DetectKeyPhrasesRequestTypeDef = TypedDict(
    "DetectKeyPhrasesRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)
DetectPiiEntitiesRequestTypeDef = TypedDict(
    "DetectPiiEntitiesRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)
PiiEntityTypeDef = TypedDict(
    "PiiEntityTypeDef",
    {
        "Score": NotRequired[float],
        "Type": NotRequired[PiiEntityTypeType],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
    },
)
DetectSentimentRequestTypeDef = TypedDict(
    "DetectSentimentRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)
DetectSyntaxRequestTypeDef = TypedDict(
    "DetectSyntaxRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": SyntaxLanguageCodeType,
    },
)
DetectTargetedSentimentRequestTypeDef = TypedDict(
    "DetectTargetedSentimentRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)
TextSegmentTypeDef = TypedDict(
    "TextSegmentTypeDef",
    {
        "Text": str,
    },
)

class DocumentClassificationConfigOutputTypeDef(TypedDict):
    Mode: DocumentClassifierModeType
    Labels: NotRequired[List[str]]

class DocumentClassificationConfigTypeDef(TypedDict):
    Mode: DocumentClassifierModeType
    Labels: NotRequired[Sequence[str]]

class OutputDataConfigTypeDef(TypedDict):
    S3Uri: str
    KmsKeyId: NotRequired[str]

class DocumentClassifierDocumentsTypeDef(TypedDict):
    S3Uri: str
    TestS3Uri: NotRequired[str]

class DocumentReaderConfigOutputTypeDef(TypedDict):
    DocumentReadAction: DocumentReadActionType
    DocumentReadMode: NotRequired[DocumentReadModeType]
    FeatureTypes: NotRequired[List[DocumentReadFeatureTypesType]]

class DocumentReaderConfigTypeDef(TypedDict):
    DocumentReadAction: DocumentReadActionType
    DocumentReadMode: NotRequired[DocumentReadModeType]
    FeatureTypes: NotRequired[Sequence[DocumentReadFeatureTypesType]]

class DocumentClassifierSummaryTypeDef(TypedDict):
    DocumentClassifierName: NotRequired[str]
    NumberOfVersions: NotRequired[int]
    LatestVersionCreatedAt: NotRequired[datetime]
    LatestVersionName: NotRequired[str]
    LatestVersionStatus: NotRequired[ModelStatusType]

class ExtractedCharactersListItemTypeDef(TypedDict):
    Page: NotRequired[int]
    Count: NotRequired[int]

EntityTypesListItemTypeDef = TypedDict(
    "EntityTypesListItemTypeDef",
    {
        "Type": str,
    },
)

class EntityRecognizerAnnotationsTypeDef(TypedDict):
    S3Uri: str
    TestS3Uri: NotRequired[str]

class EntityRecognizerDocumentsTypeDef(TypedDict):
    S3Uri: str
    TestS3Uri: NotRequired[str]
    InputFormat: NotRequired[InputFormatType]

class EntityRecognizerEntityListTypeDef(TypedDict):
    S3Uri: str

class EntityRecognizerEvaluationMetricsTypeDef(TypedDict):
    Precision: NotRequired[float]
    Recall: NotRequired[float]
    F1Score: NotRequired[float]

class EntityTypesEvaluationMetricsTypeDef(TypedDict):
    Precision: NotRequired[float]
    Recall: NotRequired[float]
    F1Score: NotRequired[float]

class EntityRecognizerOutputDataConfigTypeDef(TypedDict):
    FlywheelStatsS3Prefix: NotRequired[str]

class EntityRecognizerSummaryTypeDef(TypedDict):
    RecognizerName: NotRequired[str]
    NumberOfVersions: NotRequired[int]
    LatestVersionCreatedAt: NotRequired[datetime]
    LatestVersionName: NotRequired[str]
    LatestVersionStatus: NotRequired[ModelStatusType]

class FlywheelModelEvaluationMetricsTypeDef(TypedDict):
    AverageF1Score: NotRequired[float]
    AveragePrecision: NotRequired[float]
    AverageRecall: NotRequired[float]
    AverageAccuracy: NotRequired[float]

class FlywheelSummaryTypeDef(TypedDict):
    FlywheelArn: NotRequired[str]
    ActiveModelArn: NotRequired[str]
    DataLakeS3Uri: NotRequired[str]
    Status: NotRequired[FlywheelStatusType]
    ModelType: NotRequired[ModelTypeType]
    Message: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastModifiedTime: NotRequired[datetime]
    LatestFlywheelIteration: NotRequired[str]

class PointTypeDef(TypedDict):
    X: NotRequired[float]
    Y: NotRequired[float]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListDocumentClassifierSummariesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListEntityRecognizerSummariesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class PartOfSpeechTagTypeDef(TypedDict):
    Tag: NotRequired[PartOfSpeechTagTypeType]
    Score: NotRequired[float]

class PiiOutputDataConfigTypeDef(TypedDict):
    S3Uri: str
    KmsKeyId: NotRequired[str]

class RedactionConfigOutputTypeDef(TypedDict):
    PiiEntityTypes: NotRequired[List[PiiEntityTypeType]]
    MaskMode: NotRequired[PiiEntitiesDetectionMaskModeType]
    MaskCharacter: NotRequired[str]

class PutResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: str
    ResourcePolicy: str
    PolicyRevisionId: NotRequired[str]

class RedactionConfigTypeDef(TypedDict):
    PiiEntityTypes: NotRequired[Sequence[PiiEntityTypeType]]
    MaskMode: NotRequired[PiiEntitiesDetectionMaskModeType]
    MaskCharacter: NotRequired[str]

class StartFlywheelIterationRequestTypeDef(TypedDict):
    FlywheelArn: str
    ClientRequestToken: NotRequired[str]

class StopDominantLanguageDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class StopEntitiesDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class StopEventsDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class StopKeyPhrasesDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class StopPiiEntitiesDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class StopSentimentDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class StopTargetedSentimentDetectionJobRequestTypeDef(TypedDict):
    JobId: str

class StopTrainingDocumentClassifierRequestTypeDef(TypedDict):
    DocumentClassifierArn: str

class StopTrainingEntityRecognizerRequestTypeDef(TypedDict):
    EntityRecognizerArn: str

class ToxicContentTypeDef(TypedDict):
    Name: NotRequired[ToxicContentTypeType]
    Score: NotRequired[float]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateEndpointRequestTypeDef(TypedDict):
    EndpointArn: str
    DesiredModelArn: NotRequired[str]
    DesiredInferenceUnits: NotRequired[int]
    DesiredDataAccessRoleArn: NotRequired[str]
    FlywheelArn: NotRequired[str]

class BatchDetectDominantLanguageItemResultTypeDef(TypedDict):
    Index: NotRequired[int]
    Languages: NotRequired[List[DominantLanguageTypeDef]]

class CreateDatasetResponseTypeDef(TypedDict):
    DatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDocumentClassifierResponseTypeDef(TypedDict):
    DocumentClassifierArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointResponseTypeDef(TypedDict):
    EndpointArn: str
    ModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEntityRecognizerResponseTypeDef(TypedDict):
    EntityRecognizerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlywheelResponseTypeDef(TypedDict):
    FlywheelArn: str
    ActiveModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourcePolicyResponseTypeDef(TypedDict):
    ResourcePolicy: str
    CreationTime: datetime
    LastModifiedTime: datetime
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DetectDominantLanguageResponseTypeDef(TypedDict):
    Languages: List[DominantLanguageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportModelResponseTypeDef(TypedDict):
    ModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(TypedDict):
    PolicyRevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDocumentClassificationJobResponseTypeDef(TypedDict):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    DocumentClassifierArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDominantLanguageDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartEntitiesDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    EntityRecognizerArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartEventsDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartFlywheelIterationResponseTypeDef(TypedDict):
    FlywheelArn: str
    FlywheelIterationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartKeyPhrasesDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartPiiEntitiesDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartSentimentDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartTargetedSentimentDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartTopicsDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    JobArn: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopDominantLanguageDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopEntitiesDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopEventsDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopKeyPhrasesDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopPiiEntitiesDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopSentimentDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopTargetedSentimentDetectionJobResponseTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEndpointResponseTypeDef(TypedDict):
    DesiredModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectKeyPhrasesItemResultTypeDef(TypedDict):
    Index: NotRequired[int]
    KeyPhrases: NotRequired[List[KeyPhraseTypeDef]]

class DetectKeyPhrasesResponseTypeDef(TypedDict):
    KeyPhrases: List[KeyPhraseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectSentimentItemResultTypeDef(TypedDict):
    Index: NotRequired[int]
    Sentiment: NotRequired[SentimentTypeType]
    SentimentScore: NotRequired[SentimentScoreTypeDef]

class DetectSentimentResponseTypeDef(TypedDict):
    Sentiment: SentimentTypeType
    SentimentScore: SentimentScoreTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MentionSentimentTypeDef(TypedDict):
    Sentiment: NotRequired[SentimentTypeType]
    SentimentScore: NotRequired[SentimentScoreTypeDef]

class BlockReferenceTypeDef(TypedDict):
    BlockId: NotRequired[str]
    BeginOffset: NotRequired[int]
    EndOffset: NotRequired[int]
    ChildBlocks: NotRequired[List[ChildBlockTypeDef]]

class ClassifierMetadataTypeDef(TypedDict):
    NumberOfLabels: NotRequired[int]
    NumberOfTrainedDocuments: NotRequired[int]
    NumberOfTestDocuments: NotRequired[int]
    EvaluationMetrics: NotRequired[ClassifierEvaluationMetricsTypeDef]

class ContainsPiiEntitiesResponseTypeDef(TypedDict):
    Labels: List[EntityLabelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointRequestTypeDef(TypedDict):
    EndpointName: str
    DesiredInferenceUnits: int
    ModelArn: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    DataAccessRoleArn: NotRequired[str]
    FlywheelArn: NotRequired[str]

class ImportModelRequestTypeDef(TypedDict):
    SourceModelArn: str
    ModelName: NotRequired[str]
    VersionName: NotRequired[str]
    ModelKmsKeyId: NotRequired[str]
    DataAccessRoleArn: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class DataSecurityConfigOutputTypeDef(TypedDict):
    ModelKmsKeyId: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    DataLakeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigOutputTypeDef]

class DataSecurityConfigTypeDef(TypedDict):
    ModelKmsKeyId: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    DataLakeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigTypeDef]

VpcConfigUnionTypeDef = Union[VpcConfigTypeDef, VpcConfigOutputTypeDef]

class DatasetEntityRecognizerInputDataConfigTypeDef(TypedDict):
    Documents: DatasetEntityRecognizerDocumentsTypeDef
    Annotations: NotRequired[DatasetEntityRecognizerAnnotationsTypeDef]
    EntityList: NotRequired[DatasetEntityRecognizerEntityListTypeDef]

class DatasetFilterTypeDef(TypedDict):
    Status: NotRequired[DatasetStatusType]
    DatasetType: NotRequired[DatasetTypeType]
    CreationTimeAfter: NotRequired[TimestampTypeDef]
    CreationTimeBefore: NotRequired[TimestampTypeDef]

class DocumentClassificationJobFilterTypeDef(TypedDict):
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    SubmitTimeBefore: NotRequired[TimestampTypeDef]
    SubmitTimeAfter: NotRequired[TimestampTypeDef]

class DocumentClassifierFilterTypeDef(TypedDict):
    Status: NotRequired[ModelStatusType]
    DocumentClassifierName: NotRequired[str]
    SubmitTimeBefore: NotRequired[TimestampTypeDef]
    SubmitTimeAfter: NotRequired[TimestampTypeDef]

class DominantLanguageDetectionJobFilterTypeDef(TypedDict):
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    SubmitTimeBefore: NotRequired[TimestampTypeDef]
    SubmitTimeAfter: NotRequired[TimestampTypeDef]

class EndpointFilterTypeDef(TypedDict):
    ModelArn: NotRequired[str]
    Status: NotRequired[EndpointStatusType]
    CreationTimeBefore: NotRequired[TimestampTypeDef]
    CreationTimeAfter: NotRequired[TimestampTypeDef]

class EntitiesDetectionJobFilterTypeDef(TypedDict):
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    SubmitTimeBefore: NotRequired[TimestampTypeDef]
    SubmitTimeAfter: NotRequired[TimestampTypeDef]

class EntityRecognizerFilterTypeDef(TypedDict):
    Status: NotRequired[ModelStatusType]
    RecognizerName: NotRequired[str]
    SubmitTimeBefore: NotRequired[TimestampTypeDef]
    SubmitTimeAfter: NotRequired[TimestampTypeDef]

class EventsDetectionJobFilterTypeDef(TypedDict):
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    SubmitTimeBefore: NotRequired[TimestampTypeDef]
    SubmitTimeAfter: NotRequired[TimestampTypeDef]

class FlywheelFilterTypeDef(TypedDict):
    Status: NotRequired[FlywheelStatusType]
    CreationTimeAfter: NotRequired[TimestampTypeDef]
    CreationTimeBefore: NotRequired[TimestampTypeDef]

class FlywheelIterationFilterTypeDef(TypedDict):
    CreationTimeAfter: NotRequired[TimestampTypeDef]
    CreationTimeBefore: NotRequired[TimestampTypeDef]

class KeyPhrasesDetectionJobFilterTypeDef(TypedDict):
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    SubmitTimeBefore: NotRequired[TimestampTypeDef]
    SubmitTimeAfter: NotRequired[TimestampTypeDef]

class PiiEntitiesDetectionJobFilterTypeDef(TypedDict):
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    SubmitTimeBefore: NotRequired[TimestampTypeDef]
    SubmitTimeAfter: NotRequired[TimestampTypeDef]

class SentimentDetectionJobFilterTypeDef(TypedDict):
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    SubmitTimeBefore: NotRequired[TimestampTypeDef]
    SubmitTimeAfter: NotRequired[TimestampTypeDef]

class TargetedSentimentDetectionJobFilterTypeDef(TypedDict):
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    SubmitTimeBefore: NotRequired[TimestampTypeDef]
    SubmitTimeAfter: NotRequired[TimestampTypeDef]

class TopicsDetectionJobFilterTypeDef(TypedDict):
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    SubmitTimeBefore: NotRequired[TimestampTypeDef]
    SubmitTimeAfter: NotRequired[TimestampTypeDef]

class DescribeDatasetResponseTypeDef(TypedDict):
    DatasetProperties: DatasetPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetsResponseTypeDef(TypedDict):
    DatasetPropertiesList: List[DatasetPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeEndpointResponseTypeDef(TypedDict):
    EndpointProperties: EndpointPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEndpointsResponseTypeDef(TypedDict):
    EndpointPropertiesList: List[EndpointPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DetectPiiEntitiesResponseTypeDef(TypedDict):
    Entities: List[PiiEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DetectToxicContentRequestTypeDef(TypedDict):
    TextSegments: Sequence[TextSegmentTypeDef]
    LanguageCode: LanguageCodeType

class DocumentClassifierInputDataConfigOutputTypeDef(TypedDict):
    DataFormat: NotRequired[DocumentClassifierDataFormatType]
    S3Uri: NotRequired[str]
    TestS3Uri: NotRequired[str]
    LabelDelimiter: NotRequired[str]
    AugmentedManifests: NotRequired[List[AugmentedManifestsListItemOutputTypeDef]]
    DocumentType: NotRequired[DocumentClassifierDocumentTypeFormatType]
    Documents: NotRequired[DocumentClassifierDocumentsTypeDef]
    DocumentReaderConfig: NotRequired[DocumentReaderConfigOutputTypeDef]

class InputDataConfigOutputTypeDef(TypedDict):
    S3Uri: str
    InputFormat: NotRequired[InputFormatType]
    DocumentReaderConfig: NotRequired[DocumentReaderConfigOutputTypeDef]

class DocumentClassifierInputDataConfigTypeDef(TypedDict):
    DataFormat: NotRequired[DocumentClassifierDataFormatType]
    S3Uri: NotRequired[str]
    TestS3Uri: NotRequired[str]
    LabelDelimiter: NotRequired[str]
    AugmentedManifests: NotRequired[Sequence[AugmentedManifestsListItemTypeDef]]
    DocumentType: NotRequired[DocumentClassifierDocumentTypeFormatType]
    Documents: NotRequired[DocumentClassifierDocumentsTypeDef]
    DocumentReaderConfig: NotRequired[DocumentReaderConfigTypeDef]

DocumentReaderConfigUnionTypeDef = Union[
    DocumentReaderConfigTypeDef, DocumentReaderConfigOutputTypeDef
]

class InputDataConfigTypeDef(TypedDict):
    S3Uri: str
    InputFormat: NotRequired[InputFormatType]
    DocumentReaderConfig: NotRequired[DocumentReaderConfigTypeDef]

class ListDocumentClassifierSummariesResponseTypeDef(TypedDict):
    DocumentClassifierSummariesList: List[DocumentClassifierSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DocumentMetadataTypeDef(TypedDict):
    Pages: NotRequired[int]
    ExtractedCharacters: NotRequired[List[ExtractedCharactersListItemTypeDef]]

class EntityRecognitionConfigOutputTypeDef(TypedDict):
    EntityTypes: List[EntityTypesListItemTypeDef]

class EntityRecognitionConfigTypeDef(TypedDict):
    EntityTypes: Sequence[EntityTypesListItemTypeDef]

class EntityRecognizerInputDataConfigOutputTypeDef(TypedDict):
    EntityTypes: List[EntityTypesListItemTypeDef]
    DataFormat: NotRequired[EntityRecognizerDataFormatType]
    Documents: NotRequired[EntityRecognizerDocumentsTypeDef]
    Annotations: NotRequired[EntityRecognizerAnnotationsTypeDef]
    EntityList: NotRequired[EntityRecognizerEntityListTypeDef]
    AugmentedManifests: NotRequired[List[AugmentedManifestsListItemOutputTypeDef]]

class EntityRecognizerInputDataConfigTypeDef(TypedDict):
    EntityTypes: Sequence[EntityTypesListItemTypeDef]
    DataFormat: NotRequired[EntityRecognizerDataFormatType]
    Documents: NotRequired[EntityRecognizerDocumentsTypeDef]
    Annotations: NotRequired[EntityRecognizerAnnotationsTypeDef]
    EntityList: NotRequired[EntityRecognizerEntityListTypeDef]
    AugmentedManifests: NotRequired[Sequence[AugmentedManifestsListItemTypeDef]]

EntityRecognizerMetadataEntityTypesListItemTypeDef = TypedDict(
    "EntityRecognizerMetadataEntityTypesListItemTypeDef",
    {
        "Type": NotRequired[str],
        "EvaluationMetrics": NotRequired[EntityTypesEvaluationMetricsTypeDef],
        "NumberOfTrainMentions": NotRequired[int],
    },
)

class ListEntityRecognizerSummariesResponseTypeDef(TypedDict):
    EntityRecognizerSummariesList: List[EntityRecognizerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class FlywheelIterationPropertiesTypeDef(TypedDict):
    FlywheelArn: NotRequired[str]
    FlywheelIterationId: NotRequired[str]
    CreationTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    Status: NotRequired[FlywheelIterationStatusType]
    Message: NotRequired[str]
    EvaluatedModelArn: NotRequired[str]
    EvaluatedModelMetrics: NotRequired[FlywheelModelEvaluationMetricsTypeDef]
    TrainedModelArn: NotRequired[str]
    TrainedModelMetrics: NotRequired[FlywheelModelEvaluationMetricsTypeDef]
    EvaluationManifestS3Prefix: NotRequired[str]

class ListFlywheelsResponseTypeDef(TypedDict):
    FlywheelSummaryList: List[FlywheelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GeometryTypeDef(TypedDict):
    BoundingBox: NotRequired[BoundingBoxTypeDef]
    Polygon: NotRequired[List[PointTypeDef]]

SyntaxTokenTypeDef = TypedDict(
    "SyntaxTokenTypeDef",
    {
        "TokenId": NotRequired[int],
        "Text": NotRequired[str],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "PartOfSpeech": NotRequired[PartOfSpeechTagTypeDef],
    },
)
RedactionConfigUnionTypeDef = Union[RedactionConfigTypeDef, RedactionConfigOutputTypeDef]

class ToxicLabelsTypeDef(TypedDict):
    Labels: NotRequired[List[ToxicContentTypeDef]]
    Toxicity: NotRequired[float]

class BatchDetectDominantLanguageResponseTypeDef(TypedDict):
    ResultList: List[BatchDetectDominantLanguageItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectKeyPhrasesResponseTypeDef(TypedDict):
    ResultList: List[BatchDetectKeyPhrasesItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectSentimentResponseTypeDef(TypedDict):
    ResultList: List[BatchDetectSentimentItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

TargetedSentimentMentionTypeDef = TypedDict(
    "TargetedSentimentMentionTypeDef",
    {
        "Score": NotRequired[float],
        "GroupScore": NotRequired[float],
        "Text": NotRequired[str],
        "Type": NotRequired[TargetedSentimentEntityTypeType],
        "MentionSentiment": NotRequired[MentionSentimentTypeDef],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
    },
)
EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Score": NotRequired[float],
        "Type": NotRequired[EntityTypeType],
        "Text": NotRequired[str],
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "BlockReferences": NotRequired[List[BlockReferenceTypeDef]],
    },
)
DataSecurityConfigUnionTypeDef = Union[DataSecurityConfigTypeDef, DataSecurityConfigOutputTypeDef]

class UpdateDataSecurityConfigTypeDef(TypedDict):
    ModelKmsKeyId: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigUnionTypeDef]

class DatasetInputDataConfigTypeDef(TypedDict):
    AugmentedManifests: NotRequired[Sequence[DatasetAugmentedManifestsListItemTypeDef]]
    DataFormat: NotRequired[DatasetDataFormatType]
    DocumentClassifierInputDataConfig: NotRequired[DatasetDocumentClassifierInputDataConfigTypeDef]
    EntityRecognizerInputDataConfig: NotRequired[DatasetEntityRecognizerInputDataConfigTypeDef]

class ListDatasetsRequestTypeDef(TypedDict):
    FlywheelArn: NotRequired[str]
    Filter: NotRequired[DatasetFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDocumentClassificationJobsRequestPaginateTypeDef(TypedDict):
    Filter: NotRequired[DocumentClassificationJobFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDocumentClassificationJobsRequestTypeDef(TypedDict):
    Filter: NotRequired[DocumentClassificationJobFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDocumentClassifiersRequestPaginateTypeDef(TypedDict):
    Filter: NotRequired[DocumentClassifierFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDocumentClassifiersRequestTypeDef(TypedDict):
    Filter: NotRequired[DocumentClassifierFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDominantLanguageDetectionJobsRequestPaginateTypeDef(TypedDict):
    Filter: NotRequired[DominantLanguageDetectionJobFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDominantLanguageDetectionJobsRequestTypeDef(TypedDict):
    Filter: NotRequired[DominantLanguageDetectionJobFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListEndpointsRequestPaginateTypeDef(TypedDict):
    Filter: NotRequired[EndpointFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEndpointsRequestTypeDef(TypedDict):
    Filter: NotRequired[EndpointFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListEntitiesDetectionJobsRequestPaginateTypeDef(TypedDict):
    Filter: NotRequired[EntitiesDetectionJobFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEntitiesDetectionJobsRequestTypeDef(TypedDict):
    Filter: NotRequired[EntitiesDetectionJobFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListEntityRecognizersRequestPaginateTypeDef(TypedDict):
    Filter: NotRequired[EntityRecognizerFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEntityRecognizersRequestTypeDef(TypedDict):
    Filter: NotRequired[EntityRecognizerFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListEventsDetectionJobsRequestTypeDef(TypedDict):
    Filter: NotRequired[EventsDetectionJobFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListFlywheelsRequestTypeDef(TypedDict):
    Filter: NotRequired[FlywheelFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListFlywheelIterationHistoryRequestTypeDef(TypedDict):
    FlywheelArn: str
    Filter: NotRequired[FlywheelIterationFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListKeyPhrasesDetectionJobsRequestPaginateTypeDef(TypedDict):
    Filter: NotRequired[KeyPhrasesDetectionJobFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListKeyPhrasesDetectionJobsRequestTypeDef(TypedDict):
    Filter: NotRequired[KeyPhrasesDetectionJobFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListPiiEntitiesDetectionJobsRequestPaginateTypeDef(TypedDict):
    Filter: NotRequired[PiiEntitiesDetectionJobFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPiiEntitiesDetectionJobsRequestTypeDef(TypedDict):
    Filter: NotRequired[PiiEntitiesDetectionJobFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListSentimentDetectionJobsRequestPaginateTypeDef(TypedDict):
    Filter: NotRequired[SentimentDetectionJobFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSentimentDetectionJobsRequestTypeDef(TypedDict):
    Filter: NotRequired[SentimentDetectionJobFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTargetedSentimentDetectionJobsRequestTypeDef(TypedDict):
    Filter: NotRequired[TargetedSentimentDetectionJobFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTopicsDetectionJobsRequestPaginateTypeDef(TypedDict):
    Filter: NotRequired[TopicsDetectionJobFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTopicsDetectionJobsRequestTypeDef(TypedDict):
    Filter: NotRequired[TopicsDetectionJobFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DocumentClassifierPropertiesTypeDef(TypedDict):
    DocumentClassifierArn: NotRequired[str]
    LanguageCode: NotRequired[LanguageCodeType]
    Status: NotRequired[ModelStatusType]
    Message: NotRequired[str]
    SubmitTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    TrainingStartTime: NotRequired[datetime]
    TrainingEndTime: NotRequired[datetime]
    InputDataConfig: NotRequired[DocumentClassifierInputDataConfigOutputTypeDef]
    OutputDataConfig: NotRequired[DocumentClassifierOutputDataConfigTypeDef]
    ClassifierMetadata: NotRequired[ClassifierMetadataTypeDef]
    DataAccessRoleArn: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigOutputTypeDef]
    Mode: NotRequired[DocumentClassifierModeType]
    ModelKmsKeyId: NotRequired[str]
    VersionName: NotRequired[str]
    SourceModelArn: NotRequired[str]
    FlywheelArn: NotRequired[str]

class DocumentClassificationJobPropertiesTypeDef(TypedDict):
    JobId: NotRequired[str]
    JobArn: NotRequired[str]
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    Message: NotRequired[str]
    SubmitTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    DocumentClassifierArn: NotRequired[str]
    InputDataConfig: NotRequired[InputDataConfigOutputTypeDef]
    OutputDataConfig: NotRequired[OutputDataConfigTypeDef]
    DataAccessRoleArn: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigOutputTypeDef]
    FlywheelArn: NotRequired[str]

class DominantLanguageDetectionJobPropertiesTypeDef(TypedDict):
    JobId: NotRequired[str]
    JobArn: NotRequired[str]
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    Message: NotRequired[str]
    SubmitTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    InputDataConfig: NotRequired[InputDataConfigOutputTypeDef]
    OutputDataConfig: NotRequired[OutputDataConfigTypeDef]
    DataAccessRoleArn: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigOutputTypeDef]

class EntitiesDetectionJobPropertiesTypeDef(TypedDict):
    JobId: NotRequired[str]
    JobArn: NotRequired[str]
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    Message: NotRequired[str]
    SubmitTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    EntityRecognizerArn: NotRequired[str]
    InputDataConfig: NotRequired[InputDataConfigOutputTypeDef]
    OutputDataConfig: NotRequired[OutputDataConfigTypeDef]
    LanguageCode: NotRequired[LanguageCodeType]
    DataAccessRoleArn: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigOutputTypeDef]
    FlywheelArn: NotRequired[str]

class EventsDetectionJobPropertiesTypeDef(TypedDict):
    JobId: NotRequired[str]
    JobArn: NotRequired[str]
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    Message: NotRequired[str]
    SubmitTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    InputDataConfig: NotRequired[InputDataConfigOutputTypeDef]
    OutputDataConfig: NotRequired[OutputDataConfigTypeDef]
    LanguageCode: NotRequired[LanguageCodeType]
    DataAccessRoleArn: NotRequired[str]
    TargetEventTypes: NotRequired[List[str]]

class KeyPhrasesDetectionJobPropertiesTypeDef(TypedDict):
    JobId: NotRequired[str]
    JobArn: NotRequired[str]
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    Message: NotRequired[str]
    SubmitTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    InputDataConfig: NotRequired[InputDataConfigOutputTypeDef]
    OutputDataConfig: NotRequired[OutputDataConfigTypeDef]
    LanguageCode: NotRequired[LanguageCodeType]
    DataAccessRoleArn: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigOutputTypeDef]

class PiiEntitiesDetectionJobPropertiesTypeDef(TypedDict):
    JobId: NotRequired[str]
    JobArn: NotRequired[str]
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    Message: NotRequired[str]
    SubmitTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    InputDataConfig: NotRequired[InputDataConfigOutputTypeDef]
    OutputDataConfig: NotRequired[PiiOutputDataConfigTypeDef]
    RedactionConfig: NotRequired[RedactionConfigOutputTypeDef]
    LanguageCode: NotRequired[LanguageCodeType]
    DataAccessRoleArn: NotRequired[str]
    Mode: NotRequired[PiiEntitiesDetectionModeType]

class SentimentDetectionJobPropertiesTypeDef(TypedDict):
    JobId: NotRequired[str]
    JobArn: NotRequired[str]
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    Message: NotRequired[str]
    SubmitTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    InputDataConfig: NotRequired[InputDataConfigOutputTypeDef]
    OutputDataConfig: NotRequired[OutputDataConfigTypeDef]
    LanguageCode: NotRequired[LanguageCodeType]
    DataAccessRoleArn: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigOutputTypeDef]

class TargetedSentimentDetectionJobPropertiesTypeDef(TypedDict):
    JobId: NotRequired[str]
    JobArn: NotRequired[str]
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    Message: NotRequired[str]
    SubmitTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    InputDataConfig: NotRequired[InputDataConfigOutputTypeDef]
    OutputDataConfig: NotRequired[OutputDataConfigTypeDef]
    LanguageCode: NotRequired[LanguageCodeType]
    DataAccessRoleArn: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigOutputTypeDef]

class TopicsDetectionJobPropertiesTypeDef(TypedDict):
    JobId: NotRequired[str]
    JobArn: NotRequired[str]
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    Message: NotRequired[str]
    SubmitTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    InputDataConfig: NotRequired[InputDataConfigOutputTypeDef]
    OutputDataConfig: NotRequired[OutputDataConfigTypeDef]
    NumberOfTopics: NotRequired[int]
    DataAccessRoleArn: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigOutputTypeDef]

DocumentClassifierInputDataConfigUnionTypeDef = Union[
    DocumentClassifierInputDataConfigTypeDef, DocumentClassifierInputDataConfigOutputTypeDef
]
ClassifyDocumentRequestTypeDef = TypedDict(
    "ClassifyDocumentRequestTypeDef",
    {
        "EndpointArn": str,
        "Text": NotRequired[str],
        "Bytes": NotRequired[BlobTypeDef],
        "DocumentReaderConfig": NotRequired[DocumentReaderConfigUnionTypeDef],
    },
)
DetectEntitiesRequestTypeDef = TypedDict(
    "DetectEntitiesRequestTypeDef",
    {
        "Text": NotRequired[str],
        "LanguageCode": NotRequired[LanguageCodeType],
        "EndpointArn": NotRequired[str],
        "Bytes": NotRequired[BlobTypeDef],
        "DocumentReaderConfig": NotRequired[DocumentReaderConfigUnionTypeDef],
    },
)
InputDataConfigUnionTypeDef = Union[InputDataConfigTypeDef, InputDataConfigOutputTypeDef]

class ClassifyDocumentResponseTypeDef(TypedDict):
    Classes: List[DocumentClassTypeDef]
    Labels: List[DocumentLabelTypeDef]
    DocumentMetadata: DocumentMetadataTypeDef
    DocumentType: List[DocumentTypeListItemTypeDef]
    Errors: List[ErrorsListItemTypeDef]
    Warnings: List[WarningsListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TaskConfigOutputTypeDef(TypedDict):
    LanguageCode: LanguageCodeType
    DocumentClassificationConfig: NotRequired[DocumentClassificationConfigOutputTypeDef]
    EntityRecognitionConfig: NotRequired[EntityRecognitionConfigOutputTypeDef]

class TaskConfigTypeDef(TypedDict):
    LanguageCode: LanguageCodeType
    DocumentClassificationConfig: NotRequired[DocumentClassificationConfigTypeDef]
    EntityRecognitionConfig: NotRequired[EntityRecognitionConfigTypeDef]

EntityRecognizerInputDataConfigUnionTypeDef = Union[
    EntityRecognizerInputDataConfigTypeDef, EntityRecognizerInputDataConfigOutputTypeDef
]

class EntityRecognizerMetadataTypeDef(TypedDict):
    NumberOfTrainedDocuments: NotRequired[int]
    NumberOfTestDocuments: NotRequired[int]
    EvaluationMetrics: NotRequired[EntityRecognizerEvaluationMetricsTypeDef]
    EntityTypes: NotRequired[List[EntityRecognizerMetadataEntityTypesListItemTypeDef]]

class DescribeFlywheelIterationResponseTypeDef(TypedDict):
    FlywheelIterationProperties: FlywheelIterationPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFlywheelIterationHistoryResponseTypeDef(TypedDict):
    FlywheelIterationPropertiesList: List[FlywheelIterationPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

BlockTypeDef = TypedDict(
    "BlockTypeDef",
    {
        "Id": NotRequired[str],
        "BlockType": NotRequired[BlockTypeType],
        "Text": NotRequired[str],
        "Page": NotRequired[int],
        "Geometry": NotRequired[GeometryTypeDef],
        "Relationships": NotRequired[List[RelationshipsListItemTypeDef]],
    },
)

class BatchDetectSyntaxItemResultTypeDef(TypedDict):
    Index: NotRequired[int]
    SyntaxTokens: NotRequired[List[SyntaxTokenTypeDef]]

class DetectSyntaxResponseTypeDef(TypedDict):
    SyntaxTokens: List[SyntaxTokenTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DetectToxicContentResponseTypeDef(TypedDict):
    ResultList: List[ToxicLabelsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TargetedSentimentEntityTypeDef(TypedDict):
    DescriptiveMentionIndex: NotRequired[List[int]]
    Mentions: NotRequired[List[TargetedSentimentMentionTypeDef]]

class BatchDetectEntitiesItemResultTypeDef(TypedDict):
    Index: NotRequired[int]
    Entities: NotRequired[List[EntityTypeDef]]

class UpdateFlywheelRequestTypeDef(TypedDict):
    FlywheelArn: str
    ActiveModelArn: NotRequired[str]
    DataAccessRoleArn: NotRequired[str]
    DataSecurityConfig: NotRequired[UpdateDataSecurityConfigTypeDef]

class CreateDatasetRequestTypeDef(TypedDict):
    FlywheelArn: str
    DatasetName: str
    InputDataConfig: DatasetInputDataConfigTypeDef
    DatasetType: NotRequired[DatasetTypeType]
    Description: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class DescribeDocumentClassifierResponseTypeDef(TypedDict):
    DocumentClassifierProperties: DocumentClassifierPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDocumentClassifiersResponseTypeDef(TypedDict):
    DocumentClassifierPropertiesList: List[DocumentClassifierPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeDocumentClassificationJobResponseTypeDef(TypedDict):
    DocumentClassificationJobProperties: DocumentClassificationJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDocumentClassificationJobsResponseTypeDef(TypedDict):
    DocumentClassificationJobPropertiesList: List[DocumentClassificationJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeDominantLanguageDetectionJobResponseTypeDef(TypedDict):
    DominantLanguageDetectionJobProperties: DominantLanguageDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDominantLanguageDetectionJobsResponseTypeDef(TypedDict):
    DominantLanguageDetectionJobPropertiesList: List[DominantLanguageDetectionJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeEntitiesDetectionJobResponseTypeDef(TypedDict):
    EntitiesDetectionJobProperties: EntitiesDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntitiesDetectionJobsResponseTypeDef(TypedDict):
    EntitiesDetectionJobPropertiesList: List[EntitiesDetectionJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeEventsDetectionJobResponseTypeDef(TypedDict):
    EventsDetectionJobProperties: EventsDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventsDetectionJobsResponseTypeDef(TypedDict):
    EventsDetectionJobPropertiesList: List[EventsDetectionJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeKeyPhrasesDetectionJobResponseTypeDef(TypedDict):
    KeyPhrasesDetectionJobProperties: KeyPhrasesDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyPhrasesDetectionJobsResponseTypeDef(TypedDict):
    KeyPhrasesDetectionJobPropertiesList: List[KeyPhrasesDetectionJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribePiiEntitiesDetectionJobResponseTypeDef(TypedDict):
    PiiEntitiesDetectionJobProperties: PiiEntitiesDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPiiEntitiesDetectionJobsResponseTypeDef(TypedDict):
    PiiEntitiesDetectionJobPropertiesList: List[PiiEntitiesDetectionJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeSentimentDetectionJobResponseTypeDef(TypedDict):
    SentimentDetectionJobProperties: SentimentDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSentimentDetectionJobsResponseTypeDef(TypedDict):
    SentimentDetectionJobPropertiesList: List[SentimentDetectionJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeTargetedSentimentDetectionJobResponseTypeDef(TypedDict):
    TargetedSentimentDetectionJobProperties: TargetedSentimentDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetedSentimentDetectionJobsResponseTypeDef(TypedDict):
    TargetedSentimentDetectionJobPropertiesList: List[
        TargetedSentimentDetectionJobPropertiesTypeDef
    ]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeTopicsDetectionJobResponseTypeDef(TypedDict):
    TopicsDetectionJobProperties: TopicsDetectionJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTopicsDetectionJobsResponseTypeDef(TypedDict):
    TopicsDetectionJobPropertiesList: List[TopicsDetectionJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateDocumentClassifierRequestTypeDef(TypedDict):
    DocumentClassifierName: str
    DataAccessRoleArn: str
    InputDataConfig: DocumentClassifierInputDataConfigUnionTypeDef
    LanguageCode: LanguageCodeType
    VersionName: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    OutputDataConfig: NotRequired[DocumentClassifierOutputDataConfigTypeDef]
    ClientRequestToken: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigUnionTypeDef]
    Mode: NotRequired[DocumentClassifierModeType]
    ModelKmsKeyId: NotRequired[str]
    ModelPolicy: NotRequired[str]

class StartDocumentClassificationJobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    JobName: NotRequired[str]
    DocumentClassifierArn: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    FlywheelArn: NotRequired[str]

class StartDominantLanguageDetectionJobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    JobName: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class StartEntitiesDetectionJobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: NotRequired[str]
    EntityRecognizerArn: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    FlywheelArn: NotRequired[str]

class StartEventsDetectionJobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    TargetEventTypes: Sequence[str]
    JobName: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class StartKeyPhrasesDetectionJobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class StartPiiEntitiesDetectionJobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    Mode: PiiEntitiesDetectionModeType
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    RedactionConfig: NotRequired[RedactionConfigUnionTypeDef]
    JobName: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class StartSentimentDetectionJobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class StartTargetedSentimentDetectionJobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    LanguageCode: LanguageCodeType
    JobName: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class StartTopicsDetectionJobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigUnionTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    JobName: NotRequired[str]
    NumberOfTopics: NotRequired[int]
    ClientRequestToken: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class FlywheelPropertiesTypeDef(TypedDict):
    FlywheelArn: NotRequired[str]
    ActiveModelArn: NotRequired[str]
    DataAccessRoleArn: NotRequired[str]
    TaskConfig: NotRequired[TaskConfigOutputTypeDef]
    DataLakeS3Uri: NotRequired[str]
    DataSecurityConfig: NotRequired[DataSecurityConfigOutputTypeDef]
    Status: NotRequired[FlywheelStatusType]
    ModelType: NotRequired[ModelTypeType]
    Message: NotRequired[str]
    CreationTime: NotRequired[datetime]
    LastModifiedTime: NotRequired[datetime]
    LatestFlywheelIteration: NotRequired[str]

TaskConfigUnionTypeDef = Union[TaskConfigTypeDef, TaskConfigOutputTypeDef]

class CreateEntityRecognizerRequestTypeDef(TypedDict):
    RecognizerName: str
    DataAccessRoleArn: str
    InputDataConfig: EntityRecognizerInputDataConfigUnionTypeDef
    LanguageCode: LanguageCodeType
    VersionName: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientRequestToken: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigUnionTypeDef]
    ModelKmsKeyId: NotRequired[str]
    ModelPolicy: NotRequired[str]

class EntityRecognizerPropertiesTypeDef(TypedDict):
    EntityRecognizerArn: NotRequired[str]
    LanguageCode: NotRequired[LanguageCodeType]
    Status: NotRequired[ModelStatusType]
    Message: NotRequired[str]
    SubmitTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    TrainingStartTime: NotRequired[datetime]
    TrainingEndTime: NotRequired[datetime]
    InputDataConfig: NotRequired[EntityRecognizerInputDataConfigOutputTypeDef]
    RecognizerMetadata: NotRequired[EntityRecognizerMetadataTypeDef]
    DataAccessRoleArn: NotRequired[str]
    VolumeKmsKeyId: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigOutputTypeDef]
    ModelKmsKeyId: NotRequired[str]
    VersionName: NotRequired[str]
    SourceModelArn: NotRequired[str]
    FlywheelArn: NotRequired[str]
    OutputDataConfig: NotRequired[EntityRecognizerOutputDataConfigTypeDef]

class DetectEntitiesResponseTypeDef(TypedDict):
    Entities: List[EntityTypeDef]
    DocumentMetadata: DocumentMetadataTypeDef
    DocumentType: List[DocumentTypeListItemTypeDef]
    Blocks: List[BlockTypeDef]
    Errors: List[ErrorsListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectSyntaxResponseTypeDef(TypedDict):
    ResultList: List[BatchDetectSyntaxItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectTargetedSentimentItemResultTypeDef(TypedDict):
    Index: NotRequired[int]
    Entities: NotRequired[List[TargetedSentimentEntityTypeDef]]

class DetectTargetedSentimentResponseTypeDef(TypedDict):
    Entities: List[TargetedSentimentEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDetectEntitiesResponseTypeDef(TypedDict):
    ResultList: List[BatchDetectEntitiesItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFlywheelResponseTypeDef(TypedDict):
    FlywheelProperties: FlywheelPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFlywheelResponseTypeDef(TypedDict):
    FlywheelProperties: FlywheelPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlywheelRequestTypeDef(TypedDict):
    FlywheelName: str
    DataAccessRoleArn: str
    DataLakeS3Uri: str
    ActiveModelArn: NotRequired[str]
    TaskConfig: NotRequired[TaskConfigUnionTypeDef]
    ModelType: NotRequired[ModelTypeType]
    DataSecurityConfig: NotRequired[DataSecurityConfigUnionTypeDef]
    ClientRequestToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class DescribeEntityRecognizerResponseTypeDef(TypedDict):
    EntityRecognizerProperties: EntityRecognizerPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntityRecognizersResponseTypeDef(TypedDict):
    EntityRecognizerPropertiesList: List[EntityRecognizerPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchDetectTargetedSentimentResponseTypeDef(TypedDict):
    ResultList: List[BatchDetectTargetedSentimentItemResultTypeDef]
    ErrorList: List[BatchItemErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
