"""
Type annotations for comprehend service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/type_defs.html)

Usage::

    ```python
    from mypy_boto3_comprehend.type_defs import AugmentedManifestsListItemTypeDef

    data: AugmentedManifestsListItemTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AugmentedManifestsDocumentTypeFormatType,
    DocumentClassifierDataFormatType,
    DocumentClassifierModeType,
    DocumentReadActionType,
    DocumentReadFeatureTypesType,
    DocumentReadModeType,
    EndpointStatusType,
    EntityRecognizerDataFormatType,
    EntityTypeType,
    InputFormatType,
    JobStatusType,
    LanguageCodeType,
    ModelStatusType,
    PartOfSpeechTagTypeType,
    PiiEntitiesDetectionMaskModeType,
    PiiEntitiesDetectionModeType,
    PiiEntityTypeType,
    SentimentTypeType,
    SplitType,
    SyntaxLanguageCodeType,
    TargetedSentimentEntityTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AugmentedManifestsListItemTypeDef",
    "BatchDetectDominantLanguageItemResultTypeDef",
    "BatchDetectDominantLanguageRequestRequestTypeDef",
    "BatchDetectDominantLanguageResponseTypeDef",
    "BatchDetectEntitiesItemResultTypeDef",
    "BatchDetectEntitiesRequestRequestTypeDef",
    "BatchDetectEntitiesResponseTypeDef",
    "BatchDetectKeyPhrasesItemResultTypeDef",
    "BatchDetectKeyPhrasesRequestRequestTypeDef",
    "BatchDetectKeyPhrasesResponseTypeDef",
    "BatchDetectSentimentItemResultTypeDef",
    "BatchDetectSentimentRequestRequestTypeDef",
    "BatchDetectSentimentResponseTypeDef",
    "BatchDetectSyntaxItemResultTypeDef",
    "BatchDetectSyntaxRequestRequestTypeDef",
    "BatchDetectSyntaxResponseTypeDef",
    "BatchDetectTargetedSentimentItemResultTypeDef",
    "BatchDetectTargetedSentimentRequestRequestTypeDef",
    "BatchDetectTargetedSentimentResponseTypeDef",
    "BatchItemErrorTypeDef",
    "ClassifierEvaluationMetricsTypeDef",
    "ClassifierMetadataTypeDef",
    "ClassifyDocumentRequestRequestTypeDef",
    "ClassifyDocumentResponseTypeDef",
    "ContainsPiiEntitiesRequestRequestTypeDef",
    "ContainsPiiEntitiesResponseTypeDef",
    "CreateDocumentClassifierRequestRequestTypeDef",
    "CreateDocumentClassifierResponseTypeDef",
    "CreateEndpointRequestRequestTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreateEntityRecognizerRequestRequestTypeDef",
    "CreateEntityRecognizerResponseTypeDef",
    "DeleteDocumentClassifierRequestRequestTypeDef",
    "DeleteEndpointRequestRequestTypeDef",
    "DeleteEntityRecognizerRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DescribeDocumentClassificationJobRequestRequestTypeDef",
    "DescribeDocumentClassificationJobResponseTypeDef",
    "DescribeDocumentClassifierRequestRequestTypeDef",
    "DescribeDocumentClassifierResponseTypeDef",
    "DescribeDominantLanguageDetectionJobRequestRequestTypeDef",
    "DescribeDominantLanguageDetectionJobResponseTypeDef",
    "DescribeEndpointRequestRequestTypeDef",
    "DescribeEndpointResponseTypeDef",
    "DescribeEntitiesDetectionJobRequestRequestTypeDef",
    "DescribeEntitiesDetectionJobResponseTypeDef",
    "DescribeEntityRecognizerRequestRequestTypeDef",
    "DescribeEntityRecognizerResponseTypeDef",
    "DescribeEventsDetectionJobRequestRequestTypeDef",
    "DescribeEventsDetectionJobResponseTypeDef",
    "DescribeKeyPhrasesDetectionJobRequestRequestTypeDef",
    "DescribeKeyPhrasesDetectionJobResponseTypeDef",
    "DescribePiiEntitiesDetectionJobRequestRequestTypeDef",
    "DescribePiiEntitiesDetectionJobResponseTypeDef",
    "DescribeResourcePolicyRequestRequestTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DescribeSentimentDetectionJobRequestRequestTypeDef",
    "DescribeSentimentDetectionJobResponseTypeDef",
    "DescribeTargetedSentimentDetectionJobRequestRequestTypeDef",
    "DescribeTargetedSentimentDetectionJobResponseTypeDef",
    "DescribeTopicsDetectionJobRequestRequestTypeDef",
    "DescribeTopicsDetectionJobResponseTypeDef",
    "DetectDominantLanguageRequestRequestTypeDef",
    "DetectDominantLanguageResponseTypeDef",
    "DetectEntitiesRequestRequestTypeDef",
    "DetectEntitiesResponseTypeDef",
    "DetectKeyPhrasesRequestRequestTypeDef",
    "DetectKeyPhrasesResponseTypeDef",
    "DetectPiiEntitiesRequestRequestTypeDef",
    "DetectPiiEntitiesResponseTypeDef",
    "DetectSentimentRequestRequestTypeDef",
    "DetectSentimentResponseTypeDef",
    "DetectSyntaxRequestRequestTypeDef",
    "DetectSyntaxResponseTypeDef",
    "DetectTargetedSentimentRequestRequestTypeDef",
    "DetectTargetedSentimentResponseTypeDef",
    "DocumentClassTypeDef",
    "DocumentClassificationJobFilterTypeDef",
    "DocumentClassificationJobPropertiesTypeDef",
    "DocumentClassifierFilterTypeDef",
    "DocumentClassifierInputDataConfigTypeDef",
    "DocumentClassifierOutputDataConfigTypeDef",
    "DocumentClassifierPropertiesTypeDef",
    "DocumentClassifierSummaryTypeDef",
    "DocumentLabelTypeDef",
    "DocumentReaderConfigTypeDef",
    "DominantLanguageDetectionJobFilterTypeDef",
    "DominantLanguageDetectionJobPropertiesTypeDef",
    "DominantLanguageTypeDef",
    "EndpointFilterTypeDef",
    "EndpointPropertiesTypeDef",
    "EntitiesDetectionJobFilterTypeDef",
    "EntitiesDetectionJobPropertiesTypeDef",
    "EntityLabelTypeDef",
    "EntityRecognizerAnnotationsTypeDef",
    "EntityRecognizerDocumentsTypeDef",
    "EntityRecognizerEntityListTypeDef",
    "EntityRecognizerEvaluationMetricsTypeDef",
    "EntityRecognizerFilterTypeDef",
    "EntityRecognizerInputDataConfigTypeDef",
    "EntityRecognizerMetadataEntityTypesListItemTypeDef",
    "EntityRecognizerMetadataTypeDef",
    "EntityRecognizerPropertiesTypeDef",
    "EntityRecognizerSummaryTypeDef",
    "EntityTypeDef",
    "EntityTypesEvaluationMetricsTypeDef",
    "EntityTypesListItemTypeDef",
    "EventsDetectionJobFilterTypeDef",
    "EventsDetectionJobPropertiesTypeDef",
    "ImportModelRequestRequestTypeDef",
    "ImportModelResponseTypeDef",
    "InputDataConfigTypeDef",
    "KeyPhraseTypeDef",
    "KeyPhrasesDetectionJobFilterTypeDef",
    "KeyPhrasesDetectionJobPropertiesTypeDef",
    "ListDocumentClassificationJobsRequestRequestTypeDef",
    "ListDocumentClassificationJobsResponseTypeDef",
    "ListDocumentClassifierSummariesRequestRequestTypeDef",
    "ListDocumentClassifierSummariesResponseTypeDef",
    "ListDocumentClassifiersRequestRequestTypeDef",
    "ListDocumentClassifiersResponseTypeDef",
    "ListDominantLanguageDetectionJobsRequestRequestTypeDef",
    "ListDominantLanguageDetectionJobsResponseTypeDef",
    "ListEndpointsRequestRequestTypeDef",
    "ListEndpointsResponseTypeDef",
    "ListEntitiesDetectionJobsRequestRequestTypeDef",
    "ListEntitiesDetectionJobsResponseTypeDef",
    "ListEntityRecognizerSummariesRequestRequestTypeDef",
    "ListEntityRecognizerSummariesResponseTypeDef",
    "ListEntityRecognizersRequestRequestTypeDef",
    "ListEntityRecognizersResponseTypeDef",
    "ListEventsDetectionJobsRequestRequestTypeDef",
    "ListEventsDetectionJobsResponseTypeDef",
    "ListKeyPhrasesDetectionJobsRequestRequestTypeDef",
    "ListKeyPhrasesDetectionJobsResponseTypeDef",
    "ListPiiEntitiesDetectionJobsRequestRequestTypeDef",
    "ListPiiEntitiesDetectionJobsResponseTypeDef",
    "ListSentimentDetectionJobsRequestRequestTypeDef",
    "ListSentimentDetectionJobsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetedSentimentDetectionJobsRequestRequestTypeDef",
    "ListTargetedSentimentDetectionJobsResponseTypeDef",
    "ListTopicsDetectionJobsRequestRequestTypeDef",
    "ListTopicsDetectionJobsResponseTypeDef",
    "MentionSentimentTypeDef",
    "OutputDataConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PartOfSpeechTagTypeDef",
    "PiiEntitiesDetectionJobFilterTypeDef",
    "PiiEntitiesDetectionJobPropertiesTypeDef",
    "PiiEntityTypeDef",
    "PiiOutputDataConfigTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "RedactionConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SentimentDetectionJobFilterTypeDef",
    "SentimentDetectionJobPropertiesTypeDef",
    "SentimentScoreTypeDef",
    "StartDocumentClassificationJobRequestRequestTypeDef",
    "StartDocumentClassificationJobResponseTypeDef",
    "StartDominantLanguageDetectionJobRequestRequestTypeDef",
    "StartDominantLanguageDetectionJobResponseTypeDef",
    "StartEntitiesDetectionJobRequestRequestTypeDef",
    "StartEntitiesDetectionJobResponseTypeDef",
    "StartEventsDetectionJobRequestRequestTypeDef",
    "StartEventsDetectionJobResponseTypeDef",
    "StartKeyPhrasesDetectionJobRequestRequestTypeDef",
    "StartKeyPhrasesDetectionJobResponseTypeDef",
    "StartPiiEntitiesDetectionJobRequestRequestTypeDef",
    "StartPiiEntitiesDetectionJobResponseTypeDef",
    "StartSentimentDetectionJobRequestRequestTypeDef",
    "StartSentimentDetectionJobResponseTypeDef",
    "StartTargetedSentimentDetectionJobRequestRequestTypeDef",
    "StartTargetedSentimentDetectionJobResponseTypeDef",
    "StartTopicsDetectionJobRequestRequestTypeDef",
    "StartTopicsDetectionJobResponseTypeDef",
    "StopDominantLanguageDetectionJobRequestRequestTypeDef",
    "StopDominantLanguageDetectionJobResponseTypeDef",
    "StopEntitiesDetectionJobRequestRequestTypeDef",
    "StopEntitiesDetectionJobResponseTypeDef",
    "StopEventsDetectionJobRequestRequestTypeDef",
    "StopEventsDetectionJobResponseTypeDef",
    "StopKeyPhrasesDetectionJobRequestRequestTypeDef",
    "StopKeyPhrasesDetectionJobResponseTypeDef",
    "StopPiiEntitiesDetectionJobRequestRequestTypeDef",
    "StopPiiEntitiesDetectionJobResponseTypeDef",
    "StopSentimentDetectionJobRequestRequestTypeDef",
    "StopSentimentDetectionJobResponseTypeDef",
    "StopTargetedSentimentDetectionJobRequestRequestTypeDef",
    "StopTargetedSentimentDetectionJobResponseTypeDef",
    "StopTrainingDocumentClassifierRequestRequestTypeDef",
    "StopTrainingEntityRecognizerRequestRequestTypeDef",
    "SyntaxTokenTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TargetedSentimentDetectionJobFilterTypeDef",
    "TargetedSentimentDetectionJobPropertiesTypeDef",
    "TargetedSentimentEntityTypeDef",
    "TargetedSentimentMentionTypeDef",
    "TopicsDetectionJobFilterTypeDef",
    "TopicsDetectionJobPropertiesTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEndpointRequestRequestTypeDef",
    "VpcConfigTypeDef",
)

_RequiredAugmentedManifestsListItemTypeDef = TypedDict(
    "_RequiredAugmentedManifestsListItemTypeDef",
    {
        "S3Uri": str,
        "AttributeNames": List[str],
    },
)
_OptionalAugmentedManifestsListItemTypeDef = TypedDict(
    "_OptionalAugmentedManifestsListItemTypeDef",
    {
        "Split": SplitType,
        "AnnotationDataS3Uri": str,
        "SourceDocumentsS3Uri": str,
        "DocumentType": AugmentedManifestsDocumentTypeFormatType,
    },
    total=False,
)

class AugmentedManifestsListItemTypeDef(
    _RequiredAugmentedManifestsListItemTypeDef, _OptionalAugmentedManifestsListItemTypeDef
):
    pass

BatchDetectDominantLanguageItemResultTypeDef = TypedDict(
    "BatchDetectDominantLanguageItemResultTypeDef",
    {
        "Index": int,
        "Languages": List["DominantLanguageTypeDef"],
    },
    total=False,
)

BatchDetectDominantLanguageRequestRequestTypeDef = TypedDict(
    "BatchDetectDominantLanguageRequestRequestTypeDef",
    {
        "TextList": List[str],
    },
)

BatchDetectDominantLanguageResponseTypeDef = TypedDict(
    "BatchDetectDominantLanguageResponseTypeDef",
    {
        "ResultList": List["BatchDetectDominantLanguageItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDetectEntitiesItemResultTypeDef = TypedDict(
    "BatchDetectEntitiesItemResultTypeDef",
    {
        "Index": int,
        "Entities": List["EntityTypeDef"],
    },
    total=False,
)

BatchDetectEntitiesRequestRequestTypeDef = TypedDict(
    "BatchDetectEntitiesRequestRequestTypeDef",
    {
        "TextList": List[str],
        "LanguageCode": LanguageCodeType,
    },
)

BatchDetectEntitiesResponseTypeDef = TypedDict(
    "BatchDetectEntitiesResponseTypeDef",
    {
        "ResultList": List["BatchDetectEntitiesItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDetectKeyPhrasesItemResultTypeDef = TypedDict(
    "BatchDetectKeyPhrasesItemResultTypeDef",
    {
        "Index": int,
        "KeyPhrases": List["KeyPhraseTypeDef"],
    },
    total=False,
)

BatchDetectKeyPhrasesRequestRequestTypeDef = TypedDict(
    "BatchDetectKeyPhrasesRequestRequestTypeDef",
    {
        "TextList": List[str],
        "LanguageCode": LanguageCodeType,
    },
)

BatchDetectKeyPhrasesResponseTypeDef = TypedDict(
    "BatchDetectKeyPhrasesResponseTypeDef",
    {
        "ResultList": List["BatchDetectKeyPhrasesItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDetectSentimentItemResultTypeDef = TypedDict(
    "BatchDetectSentimentItemResultTypeDef",
    {
        "Index": int,
        "Sentiment": SentimentTypeType,
        "SentimentScore": "SentimentScoreTypeDef",
    },
    total=False,
)

BatchDetectSentimentRequestRequestTypeDef = TypedDict(
    "BatchDetectSentimentRequestRequestTypeDef",
    {
        "TextList": List[str],
        "LanguageCode": LanguageCodeType,
    },
)

BatchDetectSentimentResponseTypeDef = TypedDict(
    "BatchDetectSentimentResponseTypeDef",
    {
        "ResultList": List["BatchDetectSentimentItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDetectSyntaxItemResultTypeDef = TypedDict(
    "BatchDetectSyntaxItemResultTypeDef",
    {
        "Index": int,
        "SyntaxTokens": List["SyntaxTokenTypeDef"],
    },
    total=False,
)

BatchDetectSyntaxRequestRequestTypeDef = TypedDict(
    "BatchDetectSyntaxRequestRequestTypeDef",
    {
        "TextList": List[str],
        "LanguageCode": SyntaxLanguageCodeType,
    },
)

BatchDetectSyntaxResponseTypeDef = TypedDict(
    "BatchDetectSyntaxResponseTypeDef",
    {
        "ResultList": List["BatchDetectSyntaxItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDetectTargetedSentimentItemResultTypeDef = TypedDict(
    "BatchDetectTargetedSentimentItemResultTypeDef",
    {
        "Index": int,
        "Entities": List["TargetedSentimentEntityTypeDef"],
    },
    total=False,
)

BatchDetectTargetedSentimentRequestRequestTypeDef = TypedDict(
    "BatchDetectTargetedSentimentRequestRequestTypeDef",
    {
        "TextList": List[str],
        "LanguageCode": LanguageCodeType,
    },
)

BatchDetectTargetedSentimentResponseTypeDef = TypedDict(
    "BatchDetectTargetedSentimentResponseTypeDef",
    {
        "ResultList": List["BatchDetectTargetedSentimentItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchItemErrorTypeDef = TypedDict(
    "BatchItemErrorTypeDef",
    {
        "Index": int,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

ClassifierEvaluationMetricsTypeDef = TypedDict(
    "ClassifierEvaluationMetricsTypeDef",
    {
        "Accuracy": float,
        "Precision": float,
        "Recall": float,
        "F1Score": float,
        "MicroPrecision": float,
        "MicroRecall": float,
        "MicroF1Score": float,
        "HammingLoss": float,
    },
    total=False,
)

ClassifierMetadataTypeDef = TypedDict(
    "ClassifierMetadataTypeDef",
    {
        "NumberOfLabels": int,
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": "ClassifierEvaluationMetricsTypeDef",
    },
    total=False,
)

ClassifyDocumentRequestRequestTypeDef = TypedDict(
    "ClassifyDocumentRequestRequestTypeDef",
    {
        "Text": str,
        "EndpointArn": str,
    },
)

ClassifyDocumentResponseTypeDef = TypedDict(
    "ClassifyDocumentResponseTypeDef",
    {
        "Classes": List["DocumentClassTypeDef"],
        "Labels": List["DocumentLabelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ContainsPiiEntitiesRequestRequestTypeDef = TypedDict(
    "ContainsPiiEntitiesRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)

ContainsPiiEntitiesResponseTypeDef = TypedDict(
    "ContainsPiiEntitiesResponseTypeDef",
    {
        "Labels": List["EntityLabelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDocumentClassifierRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDocumentClassifierRequestRequestTypeDef",
    {
        "DocumentClassifierName": str,
        "DataAccessRoleArn": str,
        "InputDataConfig": "DocumentClassifierInputDataConfigTypeDef",
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalCreateDocumentClassifierRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDocumentClassifierRequestRequestTypeDef",
    {
        "VersionName": str,
        "Tags": List["TagTypeDef"],
        "OutputDataConfig": "DocumentClassifierOutputDataConfigTypeDef",
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "Mode": DocumentClassifierModeType,
        "ModelKmsKeyId": str,
        "ModelPolicy": str,
    },
    total=False,
)

class CreateDocumentClassifierRequestRequestTypeDef(
    _RequiredCreateDocumentClassifierRequestRequestTypeDef,
    _OptionalCreateDocumentClassifierRequestRequestTypeDef,
):
    pass

CreateDocumentClassifierResponseTypeDef = TypedDict(
    "CreateDocumentClassifierResponseTypeDef",
    {
        "DocumentClassifierArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEndpointRequestRequestTypeDef",
    {
        "EndpointName": str,
        "ModelArn": str,
        "DesiredInferenceUnits": int,
    },
)
_OptionalCreateEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEndpointRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
        "DataAccessRoleArn": str,
    },
    total=False,
)

class CreateEndpointRequestRequestTypeDef(
    _RequiredCreateEndpointRequestRequestTypeDef, _OptionalCreateEndpointRequestRequestTypeDef
):
    pass

CreateEndpointResponseTypeDef = TypedDict(
    "CreateEndpointResponseTypeDef",
    {
        "EndpointArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEntityRecognizerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEntityRecognizerRequestRequestTypeDef",
    {
        "RecognizerName": str,
        "DataAccessRoleArn": str,
        "InputDataConfig": "EntityRecognizerInputDataConfigTypeDef",
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalCreateEntityRecognizerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEntityRecognizerRequestRequestTypeDef",
    {
        "VersionName": str,
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "ModelKmsKeyId": str,
        "ModelPolicy": str,
    },
    total=False,
)

class CreateEntityRecognizerRequestRequestTypeDef(
    _RequiredCreateEntityRecognizerRequestRequestTypeDef,
    _OptionalCreateEntityRecognizerRequestRequestTypeDef,
):
    pass

CreateEntityRecognizerResponseTypeDef = TypedDict(
    "CreateEntityRecognizerResponseTypeDef",
    {
        "EntityRecognizerArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDocumentClassifierRequestRequestTypeDef = TypedDict(
    "DeleteDocumentClassifierRequestRequestTypeDef",
    {
        "DocumentClassifierArn": str,
    },
)

DeleteEndpointRequestRequestTypeDef = TypedDict(
    "DeleteEndpointRequestRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

DeleteEntityRecognizerRequestRequestTypeDef = TypedDict(
    "DeleteEntityRecognizerRequestRequestTypeDef",
    {
        "EntityRecognizerArn": str,
    },
)

_RequiredDeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalDeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteResourcePolicyRequestRequestTypeDef",
    {
        "PolicyRevisionId": str,
    },
    total=False,
)

class DeleteResourcePolicyRequestRequestTypeDef(
    _RequiredDeleteResourcePolicyRequestRequestTypeDef,
    _OptionalDeleteResourcePolicyRequestRequestTypeDef,
):
    pass

DescribeDocumentClassificationJobRequestRequestTypeDef = TypedDict(
    "DescribeDocumentClassificationJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeDocumentClassificationJobResponseTypeDef = TypedDict(
    "DescribeDocumentClassificationJobResponseTypeDef",
    {
        "DocumentClassificationJobProperties": "DocumentClassificationJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDocumentClassifierRequestRequestTypeDef = TypedDict(
    "DescribeDocumentClassifierRequestRequestTypeDef",
    {
        "DocumentClassifierArn": str,
    },
)

DescribeDocumentClassifierResponseTypeDef = TypedDict(
    "DescribeDocumentClassifierResponseTypeDef",
    {
        "DocumentClassifierProperties": "DocumentClassifierPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDominantLanguageDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeDominantLanguageDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "DescribeDominantLanguageDetectionJobResponseTypeDef",
    {
        "DominantLanguageDetectionJobProperties": "DominantLanguageDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointRequestRequestTypeDef = TypedDict(
    "DescribeEndpointRequestRequestTypeDef",
    {
        "EndpointArn": str,
    },
)

DescribeEndpointResponseTypeDef = TypedDict(
    "DescribeEndpointResponseTypeDef",
    {
        "EndpointProperties": "EndpointPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeEntitiesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeEntitiesDetectionJobResponseTypeDef = TypedDict(
    "DescribeEntitiesDetectionJobResponseTypeDef",
    {
        "EntitiesDetectionJobProperties": "EntitiesDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEntityRecognizerRequestRequestTypeDef = TypedDict(
    "DescribeEntityRecognizerRequestRequestTypeDef",
    {
        "EntityRecognizerArn": str,
    },
)

DescribeEntityRecognizerResponseTypeDef = TypedDict(
    "DescribeEntityRecognizerResponseTypeDef",
    {
        "EntityRecognizerProperties": "EntityRecognizerPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventsDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeEventsDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeEventsDetectionJobResponseTypeDef = TypedDict(
    "DescribeEventsDetectionJobResponseTypeDef",
    {
        "EventsDetectionJobProperties": "EventsDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeKeyPhrasesDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeKeyPhrasesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "DescribeKeyPhrasesDetectionJobResponseTypeDef",
    {
        "KeyPhrasesDetectionJobProperties": "KeyPhrasesDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePiiEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribePiiEntitiesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribePiiEntitiesDetectionJobResponseTypeDef = TypedDict(
    "DescribePiiEntitiesDetectionJobResponseTypeDef",
    {
        "PiiEntitiesDetectionJobProperties": "PiiEntitiesDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourcePolicyRequestRequestTypeDef = TypedDict(
    "DescribeResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeResourcePolicyResponseTypeDef = TypedDict(
    "DescribeResourcePolicyResponseTypeDef",
    {
        "ResourcePolicy": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "PolicyRevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeSentimentDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeSentimentDetectionJobResponseTypeDef = TypedDict(
    "DescribeSentimentDetectionJobResponseTypeDef",
    {
        "SentimentDetectionJobProperties": "SentimentDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTargetedSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeTargetedSentimentDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeTargetedSentimentDetectionJobResponseTypeDef = TypedDict(
    "DescribeTargetedSentimentDetectionJobResponseTypeDef",
    {
        "TargetedSentimentDetectionJobProperties": "TargetedSentimentDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTopicsDetectionJobRequestRequestTypeDef = TypedDict(
    "DescribeTopicsDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeTopicsDetectionJobResponseTypeDef = TypedDict(
    "DescribeTopicsDetectionJobResponseTypeDef",
    {
        "TopicsDetectionJobProperties": "TopicsDetectionJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectDominantLanguageRequestRequestTypeDef = TypedDict(
    "DetectDominantLanguageRequestRequestTypeDef",
    {
        "Text": str,
    },
)

DetectDominantLanguageResponseTypeDef = TypedDict(
    "DetectDominantLanguageResponseTypeDef",
    {
        "Languages": List["DominantLanguageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetectEntitiesRequestRequestTypeDef = TypedDict(
    "_RequiredDetectEntitiesRequestRequestTypeDef",
    {
        "Text": str,
    },
)
_OptionalDetectEntitiesRequestRequestTypeDef = TypedDict(
    "_OptionalDetectEntitiesRequestRequestTypeDef",
    {
        "LanguageCode": LanguageCodeType,
        "EndpointArn": str,
    },
    total=False,
)

class DetectEntitiesRequestRequestTypeDef(
    _RequiredDetectEntitiesRequestRequestTypeDef, _OptionalDetectEntitiesRequestRequestTypeDef
):
    pass

DetectEntitiesResponseTypeDef = TypedDict(
    "DetectEntitiesResponseTypeDef",
    {
        "Entities": List["EntityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectKeyPhrasesRequestRequestTypeDef = TypedDict(
    "DetectKeyPhrasesRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)

DetectKeyPhrasesResponseTypeDef = TypedDict(
    "DetectKeyPhrasesResponseTypeDef",
    {
        "KeyPhrases": List["KeyPhraseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectPiiEntitiesRequestRequestTypeDef = TypedDict(
    "DetectPiiEntitiesRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)

DetectPiiEntitiesResponseTypeDef = TypedDict(
    "DetectPiiEntitiesResponseTypeDef",
    {
        "Entities": List["PiiEntityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectSentimentRequestRequestTypeDef = TypedDict(
    "DetectSentimentRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)

DetectSentimentResponseTypeDef = TypedDict(
    "DetectSentimentResponseTypeDef",
    {
        "Sentiment": SentimentTypeType,
        "SentimentScore": "SentimentScoreTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectSyntaxRequestRequestTypeDef = TypedDict(
    "DetectSyntaxRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": SyntaxLanguageCodeType,
    },
)

DetectSyntaxResponseTypeDef = TypedDict(
    "DetectSyntaxResponseTypeDef",
    {
        "SyntaxTokens": List["SyntaxTokenTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectTargetedSentimentRequestRequestTypeDef = TypedDict(
    "DetectTargetedSentimentRequestRequestTypeDef",
    {
        "Text": str,
        "LanguageCode": LanguageCodeType,
    },
)

DetectTargetedSentimentResponseTypeDef = TypedDict(
    "DetectTargetedSentimentResponseTypeDef",
    {
        "Entities": List["TargetedSentimentEntityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentClassTypeDef = TypedDict(
    "DocumentClassTypeDef",
    {
        "Name": str,
        "Score": float,
    },
    total=False,
)

DocumentClassificationJobFilterTypeDef = TypedDict(
    "DocumentClassificationJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

DocumentClassificationJobPropertiesTypeDef = TypedDict(
    "DocumentClassificationJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "DocumentClassifierArn": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

DocumentClassifierFilterTypeDef = TypedDict(
    "DocumentClassifierFilterTypeDef",
    {
        "Status": ModelStatusType,
        "DocumentClassifierName": str,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

DocumentClassifierInputDataConfigTypeDef = TypedDict(
    "DocumentClassifierInputDataConfigTypeDef",
    {
        "DataFormat": DocumentClassifierDataFormatType,
        "S3Uri": str,
        "TestS3Uri": str,
        "LabelDelimiter": str,
        "AugmentedManifests": List["AugmentedManifestsListItemTypeDef"],
    },
    total=False,
)

DocumentClassifierOutputDataConfigTypeDef = TypedDict(
    "DocumentClassifierOutputDataConfigTypeDef",
    {
        "S3Uri": str,
        "KmsKeyId": str,
    },
    total=False,
)

DocumentClassifierPropertiesTypeDef = TypedDict(
    "DocumentClassifierPropertiesTypeDef",
    {
        "DocumentClassifierArn": str,
        "LanguageCode": LanguageCodeType,
        "Status": ModelStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": "DocumentClassifierInputDataConfigTypeDef",
        "OutputDataConfig": "DocumentClassifierOutputDataConfigTypeDef",
        "ClassifierMetadata": "ClassifierMetadataTypeDef",
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "Mode": DocumentClassifierModeType,
        "ModelKmsKeyId": str,
        "VersionName": str,
        "SourceModelArn": str,
    },
    total=False,
)

DocumentClassifierSummaryTypeDef = TypedDict(
    "DocumentClassifierSummaryTypeDef",
    {
        "DocumentClassifierName": str,
        "NumberOfVersions": int,
        "LatestVersionCreatedAt": datetime,
        "LatestVersionName": str,
        "LatestVersionStatus": ModelStatusType,
    },
    total=False,
)

DocumentLabelTypeDef = TypedDict(
    "DocumentLabelTypeDef",
    {
        "Name": str,
        "Score": float,
    },
    total=False,
)

_RequiredDocumentReaderConfigTypeDef = TypedDict(
    "_RequiredDocumentReaderConfigTypeDef",
    {
        "DocumentReadAction": DocumentReadActionType,
    },
)
_OptionalDocumentReaderConfigTypeDef = TypedDict(
    "_OptionalDocumentReaderConfigTypeDef",
    {
        "DocumentReadMode": DocumentReadModeType,
        "FeatureTypes": List[DocumentReadFeatureTypesType],
    },
    total=False,
)

class DocumentReaderConfigTypeDef(
    _RequiredDocumentReaderConfigTypeDef, _OptionalDocumentReaderConfigTypeDef
):
    pass

DominantLanguageDetectionJobFilterTypeDef = TypedDict(
    "DominantLanguageDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

DominantLanguageDetectionJobPropertiesTypeDef = TypedDict(
    "DominantLanguageDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

DominantLanguageTypeDef = TypedDict(
    "DominantLanguageTypeDef",
    {
        "LanguageCode": str,
        "Score": float,
    },
    total=False,
)

EndpointFilterTypeDef = TypedDict(
    "EndpointFilterTypeDef",
    {
        "ModelArn": str,
        "Status": EndpointStatusType,
        "CreationTimeBefore": Union[datetime, str],
        "CreationTimeAfter": Union[datetime, str],
    },
    total=False,
)

EndpointPropertiesTypeDef = TypedDict(
    "EndpointPropertiesTypeDef",
    {
        "EndpointArn": str,
        "Status": EndpointStatusType,
        "Message": str,
        "ModelArn": str,
        "DesiredModelArn": str,
        "DesiredInferenceUnits": int,
        "CurrentInferenceUnits": int,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "DataAccessRoleArn": str,
        "DesiredDataAccessRoleArn": str,
    },
    total=False,
)

EntitiesDetectionJobFilterTypeDef = TypedDict(
    "EntitiesDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

EntitiesDetectionJobPropertiesTypeDef = TypedDict(
    "EntitiesDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "EntityRecognizerArn": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "LanguageCode": LanguageCodeType,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

EntityLabelTypeDef = TypedDict(
    "EntityLabelTypeDef",
    {
        "Name": PiiEntityTypeType,
        "Score": float,
    },
    total=False,
)

_RequiredEntityRecognizerAnnotationsTypeDef = TypedDict(
    "_RequiredEntityRecognizerAnnotationsTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalEntityRecognizerAnnotationsTypeDef = TypedDict(
    "_OptionalEntityRecognizerAnnotationsTypeDef",
    {
        "TestS3Uri": str,
    },
    total=False,
)

class EntityRecognizerAnnotationsTypeDef(
    _RequiredEntityRecognizerAnnotationsTypeDef, _OptionalEntityRecognizerAnnotationsTypeDef
):
    pass

_RequiredEntityRecognizerDocumentsTypeDef = TypedDict(
    "_RequiredEntityRecognizerDocumentsTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalEntityRecognizerDocumentsTypeDef = TypedDict(
    "_OptionalEntityRecognizerDocumentsTypeDef",
    {
        "TestS3Uri": str,
        "InputFormat": InputFormatType,
    },
    total=False,
)

class EntityRecognizerDocumentsTypeDef(
    _RequiredEntityRecognizerDocumentsTypeDef, _OptionalEntityRecognizerDocumentsTypeDef
):
    pass

EntityRecognizerEntityListTypeDef = TypedDict(
    "EntityRecognizerEntityListTypeDef",
    {
        "S3Uri": str,
    },
)

EntityRecognizerEvaluationMetricsTypeDef = TypedDict(
    "EntityRecognizerEvaluationMetricsTypeDef",
    {
        "Precision": float,
        "Recall": float,
        "F1Score": float,
    },
    total=False,
)

EntityRecognizerFilterTypeDef = TypedDict(
    "EntityRecognizerFilterTypeDef",
    {
        "Status": ModelStatusType,
        "RecognizerName": str,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

_RequiredEntityRecognizerInputDataConfigTypeDef = TypedDict(
    "_RequiredEntityRecognizerInputDataConfigTypeDef",
    {
        "EntityTypes": List["EntityTypesListItemTypeDef"],
    },
)
_OptionalEntityRecognizerInputDataConfigTypeDef = TypedDict(
    "_OptionalEntityRecognizerInputDataConfigTypeDef",
    {
        "DataFormat": EntityRecognizerDataFormatType,
        "Documents": "EntityRecognizerDocumentsTypeDef",
        "Annotations": "EntityRecognizerAnnotationsTypeDef",
        "EntityList": "EntityRecognizerEntityListTypeDef",
        "AugmentedManifests": List["AugmentedManifestsListItemTypeDef"],
    },
    total=False,
)

class EntityRecognizerInputDataConfigTypeDef(
    _RequiredEntityRecognizerInputDataConfigTypeDef, _OptionalEntityRecognizerInputDataConfigTypeDef
):
    pass

EntityRecognizerMetadataEntityTypesListItemTypeDef = TypedDict(
    "EntityRecognizerMetadataEntityTypesListItemTypeDef",
    {
        "Type": str,
        "EvaluationMetrics": "EntityTypesEvaluationMetricsTypeDef",
        "NumberOfTrainMentions": int,
    },
    total=False,
)

EntityRecognizerMetadataTypeDef = TypedDict(
    "EntityRecognizerMetadataTypeDef",
    {
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": "EntityRecognizerEvaluationMetricsTypeDef",
        "EntityTypes": List["EntityRecognizerMetadataEntityTypesListItemTypeDef"],
    },
    total=False,
)

EntityRecognizerPropertiesTypeDef = TypedDict(
    "EntityRecognizerPropertiesTypeDef",
    {
        "EntityRecognizerArn": str,
        "LanguageCode": LanguageCodeType,
        "Status": ModelStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": "EntityRecognizerInputDataConfigTypeDef",
        "RecognizerMetadata": "EntityRecognizerMetadataTypeDef",
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "ModelKmsKeyId": str,
        "VersionName": str,
        "SourceModelArn": str,
    },
    total=False,
)

EntityRecognizerSummaryTypeDef = TypedDict(
    "EntityRecognizerSummaryTypeDef",
    {
        "RecognizerName": str,
        "NumberOfVersions": int,
        "LatestVersionCreatedAt": datetime,
        "LatestVersionName": str,
        "LatestVersionStatus": ModelStatusType,
    },
    total=False,
)

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Score": float,
        "Type": EntityTypeType,
        "Text": str,
        "BeginOffset": int,
        "EndOffset": int,
    },
    total=False,
)

EntityTypesEvaluationMetricsTypeDef = TypedDict(
    "EntityTypesEvaluationMetricsTypeDef",
    {
        "Precision": float,
        "Recall": float,
        "F1Score": float,
    },
    total=False,
)

EntityTypesListItemTypeDef = TypedDict(
    "EntityTypesListItemTypeDef",
    {
        "Type": str,
    },
)

EventsDetectionJobFilterTypeDef = TypedDict(
    "EventsDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

EventsDetectionJobPropertiesTypeDef = TypedDict(
    "EventsDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "LanguageCode": LanguageCodeType,
        "DataAccessRoleArn": str,
        "TargetEventTypes": List[str],
    },
    total=False,
)

_RequiredImportModelRequestRequestTypeDef = TypedDict(
    "_RequiredImportModelRequestRequestTypeDef",
    {
        "SourceModelArn": str,
    },
)
_OptionalImportModelRequestRequestTypeDef = TypedDict(
    "_OptionalImportModelRequestRequestTypeDef",
    {
        "ModelName": str,
        "VersionName": str,
        "ModelKmsKeyId": str,
        "DataAccessRoleArn": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class ImportModelRequestRequestTypeDef(
    _RequiredImportModelRequestRequestTypeDef, _OptionalImportModelRequestRequestTypeDef
):
    pass

ImportModelResponseTypeDef = TypedDict(
    "ImportModelResponseTypeDef",
    {
        "ModelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInputDataConfigTypeDef = TypedDict(
    "_RequiredInputDataConfigTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalInputDataConfigTypeDef = TypedDict(
    "_OptionalInputDataConfigTypeDef",
    {
        "InputFormat": InputFormatType,
        "DocumentReaderConfig": "DocumentReaderConfigTypeDef",
    },
    total=False,
)

class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, _OptionalInputDataConfigTypeDef):
    pass

KeyPhraseTypeDef = TypedDict(
    "KeyPhraseTypeDef",
    {
        "Score": float,
        "Text": str,
        "BeginOffset": int,
        "EndOffset": int,
    },
    total=False,
)

KeyPhrasesDetectionJobFilterTypeDef = TypedDict(
    "KeyPhrasesDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

KeyPhrasesDetectionJobPropertiesTypeDef = TypedDict(
    "KeyPhrasesDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "LanguageCode": LanguageCodeType,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

ListDocumentClassificationJobsRequestRequestTypeDef = TypedDict(
    "ListDocumentClassificationJobsRequestRequestTypeDef",
    {
        "Filter": "DocumentClassificationJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDocumentClassificationJobsResponseTypeDef = TypedDict(
    "ListDocumentClassificationJobsResponseTypeDef",
    {
        "DocumentClassificationJobPropertiesList": List[
            "DocumentClassificationJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDocumentClassifierSummariesRequestRequestTypeDef = TypedDict(
    "ListDocumentClassifierSummariesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDocumentClassifierSummariesResponseTypeDef = TypedDict(
    "ListDocumentClassifierSummariesResponseTypeDef",
    {
        "DocumentClassifierSummariesList": List["DocumentClassifierSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDocumentClassifiersRequestRequestTypeDef = TypedDict(
    "ListDocumentClassifiersRequestRequestTypeDef",
    {
        "Filter": "DocumentClassifierFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDocumentClassifiersResponseTypeDef = TypedDict(
    "ListDocumentClassifiersResponseTypeDef",
    {
        "DocumentClassifierPropertiesList": List["DocumentClassifierPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDominantLanguageDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsRequestRequestTypeDef",
    {
        "Filter": "DominantLanguageDetectionJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDominantLanguageDetectionJobsResponseTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsResponseTypeDef",
    {
        "DominantLanguageDetectionJobPropertiesList": List[
            "DominantLanguageDetectionJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEndpointsRequestRequestTypeDef = TypedDict(
    "ListEndpointsRequestRequestTypeDef",
    {
        "Filter": "EndpointFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEndpointsResponseTypeDef = TypedDict(
    "ListEndpointsResponseTypeDef",
    {
        "EndpointPropertiesList": List["EndpointPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEntitiesDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListEntitiesDetectionJobsRequestRequestTypeDef",
    {
        "Filter": "EntitiesDetectionJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEntitiesDetectionJobsResponseTypeDef = TypedDict(
    "ListEntitiesDetectionJobsResponseTypeDef",
    {
        "EntitiesDetectionJobPropertiesList": List["EntitiesDetectionJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEntityRecognizerSummariesRequestRequestTypeDef = TypedDict(
    "ListEntityRecognizerSummariesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEntityRecognizerSummariesResponseTypeDef = TypedDict(
    "ListEntityRecognizerSummariesResponseTypeDef",
    {
        "EntityRecognizerSummariesList": List["EntityRecognizerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEntityRecognizersRequestRequestTypeDef = TypedDict(
    "ListEntityRecognizersRequestRequestTypeDef",
    {
        "Filter": "EntityRecognizerFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEntityRecognizersResponseTypeDef = TypedDict(
    "ListEntityRecognizersResponseTypeDef",
    {
        "EntityRecognizerPropertiesList": List["EntityRecognizerPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventsDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListEventsDetectionJobsRequestRequestTypeDef",
    {
        "Filter": "EventsDetectionJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListEventsDetectionJobsResponseTypeDef = TypedDict(
    "ListEventsDetectionJobsResponseTypeDef",
    {
        "EventsDetectionJobPropertiesList": List["EventsDetectionJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKeyPhrasesDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsRequestRequestTypeDef",
    {
        "Filter": "KeyPhrasesDetectionJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListKeyPhrasesDetectionJobsResponseTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsResponseTypeDef",
    {
        "KeyPhrasesDetectionJobPropertiesList": List["KeyPhrasesDetectionJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPiiEntitiesDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListPiiEntitiesDetectionJobsRequestRequestTypeDef",
    {
        "Filter": "PiiEntitiesDetectionJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListPiiEntitiesDetectionJobsResponseTypeDef = TypedDict(
    "ListPiiEntitiesDetectionJobsResponseTypeDef",
    {
        "PiiEntitiesDetectionJobPropertiesList": List["PiiEntitiesDetectionJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSentimentDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListSentimentDetectionJobsRequestRequestTypeDef",
    {
        "Filter": "SentimentDetectionJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListSentimentDetectionJobsResponseTypeDef = TypedDict(
    "ListSentimentDetectionJobsResponseTypeDef",
    {
        "SentimentDetectionJobPropertiesList": List["SentimentDetectionJobPropertiesTypeDef"],
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
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTargetedSentimentDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListTargetedSentimentDetectionJobsRequestRequestTypeDef",
    {
        "Filter": "TargetedSentimentDetectionJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTargetedSentimentDetectionJobsResponseTypeDef = TypedDict(
    "ListTargetedSentimentDetectionJobsResponseTypeDef",
    {
        "TargetedSentimentDetectionJobPropertiesList": List[
            "TargetedSentimentDetectionJobPropertiesTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTopicsDetectionJobsRequestRequestTypeDef = TypedDict(
    "ListTopicsDetectionJobsRequestRequestTypeDef",
    {
        "Filter": "TopicsDetectionJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTopicsDetectionJobsResponseTypeDef = TypedDict(
    "ListTopicsDetectionJobsResponseTypeDef",
    {
        "TopicsDetectionJobPropertiesList": List["TopicsDetectionJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MentionSentimentTypeDef = TypedDict(
    "MentionSentimentTypeDef",
    {
        "Sentiment": SentimentTypeType,
        "SentimentScore": "SentimentScoreTypeDef",
    },
    total=False,
)

_RequiredOutputDataConfigTypeDef = TypedDict(
    "_RequiredOutputDataConfigTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalOutputDataConfigTypeDef = TypedDict(
    "_OptionalOutputDataConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, _OptionalOutputDataConfigTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PartOfSpeechTagTypeDef = TypedDict(
    "PartOfSpeechTagTypeDef",
    {
        "Tag": PartOfSpeechTagTypeType,
        "Score": float,
    },
    total=False,
)

PiiEntitiesDetectionJobFilterTypeDef = TypedDict(
    "PiiEntitiesDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

PiiEntitiesDetectionJobPropertiesTypeDef = TypedDict(
    "PiiEntitiesDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "PiiOutputDataConfigTypeDef",
        "RedactionConfig": "RedactionConfigTypeDef",
        "LanguageCode": LanguageCodeType,
        "DataAccessRoleArn": str,
        "Mode": PiiEntitiesDetectionModeType,
    },
    total=False,
)

PiiEntityTypeDef = TypedDict(
    "PiiEntityTypeDef",
    {
        "Score": float,
        "Type": PiiEntityTypeType,
        "BeginOffset": int,
        "EndOffset": int,
    },
    total=False,
)

_RequiredPiiOutputDataConfigTypeDef = TypedDict(
    "_RequiredPiiOutputDataConfigTypeDef",
    {
        "S3Uri": str,
    },
)
_OptionalPiiOutputDataConfigTypeDef = TypedDict(
    "_OptionalPiiOutputDataConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class PiiOutputDataConfigTypeDef(
    _RequiredPiiOutputDataConfigTypeDef, _OptionalPiiOutputDataConfigTypeDef
):
    pass

_RequiredPutResourcePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "ResourcePolicy": str,
    },
)
_OptionalPutResourcePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutResourcePolicyRequestRequestTypeDef",
    {
        "PolicyRevisionId": str,
    },
    total=False,
)

class PutResourcePolicyRequestRequestTypeDef(
    _RequiredPutResourcePolicyRequestRequestTypeDef, _OptionalPutResourcePolicyRequestRequestTypeDef
):
    pass

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "PolicyRevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RedactionConfigTypeDef = TypedDict(
    "RedactionConfigTypeDef",
    {
        "PiiEntityTypes": List[PiiEntityTypeType],
        "MaskMode": PiiEntitiesDetectionMaskModeType,
        "MaskCharacter": str,
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

SentimentDetectionJobFilterTypeDef = TypedDict(
    "SentimentDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

SentimentDetectionJobPropertiesTypeDef = TypedDict(
    "SentimentDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "LanguageCode": LanguageCodeType,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

SentimentScoreTypeDef = TypedDict(
    "SentimentScoreTypeDef",
    {
        "Positive": float,
        "Negative": float,
        "Neutral": float,
        "Mixed": float,
    },
    total=False,
)

_RequiredStartDocumentClassificationJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartDocumentClassificationJobRequestRequestTypeDef",
    {
        "DocumentClassifierArn": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
    },
)
_OptionalStartDocumentClassificationJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartDocumentClassificationJobRequestRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class StartDocumentClassificationJobRequestRequestTypeDef(
    _RequiredStartDocumentClassificationJobRequestRequestTypeDef,
    _OptionalStartDocumentClassificationJobRequestRequestTypeDef,
):
    pass

StartDocumentClassificationJobResponseTypeDef = TypedDict(
    "StartDocumentClassificationJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartDominantLanguageDetectionJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartDominantLanguageDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
    },
)
_OptionalStartDominantLanguageDetectionJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartDominantLanguageDetectionJobRequestRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class StartDominantLanguageDetectionJobRequestRequestTypeDef(
    _RequiredStartDominantLanguageDetectionJobRequestRequestTypeDef,
    _OptionalStartDominantLanguageDetectionJobRequestRequestTypeDef,
):
    pass

StartDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "StartDominantLanguageDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartEntitiesDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalStartEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartEntitiesDetectionJobRequestRequestTypeDef",
    {
        "JobName": str,
        "EntityRecognizerArn": str,
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class StartEntitiesDetectionJobRequestRequestTypeDef(
    _RequiredStartEntitiesDetectionJobRequestRequestTypeDef,
    _OptionalStartEntitiesDetectionJobRequestRequestTypeDef,
):
    pass

StartEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StartEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartEventsDetectionJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartEventsDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
        "TargetEventTypes": List[str],
    },
)
_OptionalStartEventsDetectionJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartEventsDetectionJobRequestRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class StartEventsDetectionJobRequestRequestTypeDef(
    _RequiredStartEventsDetectionJobRequestRequestTypeDef,
    _OptionalStartEventsDetectionJobRequestRequestTypeDef,
):
    pass

StartEventsDetectionJobResponseTypeDef = TypedDict(
    "StartEventsDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartKeyPhrasesDetectionJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartKeyPhrasesDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalStartKeyPhrasesDetectionJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartKeyPhrasesDetectionJobRequestRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class StartKeyPhrasesDetectionJobRequestRequestTypeDef(
    _RequiredStartKeyPhrasesDetectionJobRequestRequestTypeDef,
    _OptionalStartKeyPhrasesDetectionJobRequestRequestTypeDef,
):
    pass

StartKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "StartKeyPhrasesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartPiiEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartPiiEntitiesDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "Mode": PiiEntitiesDetectionModeType,
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalStartPiiEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartPiiEntitiesDetectionJobRequestRequestTypeDef",
    {
        "RedactionConfig": "RedactionConfigTypeDef",
        "JobName": str,
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class StartPiiEntitiesDetectionJobRequestRequestTypeDef(
    _RequiredStartPiiEntitiesDetectionJobRequestRequestTypeDef,
    _OptionalStartPiiEntitiesDetectionJobRequestRequestTypeDef,
):
    pass

StartPiiEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StartPiiEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartSentimentDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalStartSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartSentimentDetectionJobRequestRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class StartSentimentDetectionJobRequestRequestTypeDef(
    _RequiredStartSentimentDetectionJobRequestRequestTypeDef,
    _OptionalStartSentimentDetectionJobRequestRequestTypeDef,
):
    pass

StartSentimentDetectionJobResponseTypeDef = TypedDict(
    "StartSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartTargetedSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartTargetedSentimentDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalStartTargetedSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartTargetedSentimentDetectionJobRequestRequestTypeDef",
    {
        "JobName": str,
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class StartTargetedSentimentDetectionJobRequestRequestTypeDef(
    _RequiredStartTargetedSentimentDetectionJobRequestRequestTypeDef,
    _OptionalStartTargetedSentimentDetectionJobRequestRequestTypeDef,
):
    pass

StartTargetedSentimentDetectionJobResponseTypeDef = TypedDict(
    "StartTargetedSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartTopicsDetectionJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartTopicsDetectionJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
    },
)
_OptionalStartTopicsDetectionJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartTopicsDetectionJobRequestRequestTypeDef",
    {
        "JobName": str,
        "NumberOfTopics": int,
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class StartTopicsDetectionJobRequestRequestTypeDef(
    _RequiredStartTopicsDetectionJobRequestRequestTypeDef,
    _OptionalStartTopicsDetectionJobRequestRequestTypeDef,
):
    pass

StartTopicsDetectionJobResponseTypeDef = TypedDict(
    "StartTopicsDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDominantLanguageDetectionJobRequestRequestTypeDef = TypedDict(
    "StopDominantLanguageDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "StopDominantLanguageDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "StopEntitiesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StopEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopEventsDetectionJobRequestRequestTypeDef = TypedDict(
    "StopEventsDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopEventsDetectionJobResponseTypeDef = TypedDict(
    "StopEventsDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopKeyPhrasesDetectionJobRequestRequestTypeDef = TypedDict(
    "StopKeyPhrasesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "StopKeyPhrasesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopPiiEntitiesDetectionJobRequestRequestTypeDef = TypedDict(
    "StopPiiEntitiesDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopPiiEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StopPiiEntitiesDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "StopSentimentDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopSentimentDetectionJobResponseTypeDef = TypedDict(
    "StopSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopTargetedSentimentDetectionJobRequestRequestTypeDef = TypedDict(
    "StopTargetedSentimentDetectionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopTargetedSentimentDetectionJobResponseTypeDef = TypedDict(
    "StopTargetedSentimentDetectionJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopTrainingDocumentClassifierRequestRequestTypeDef = TypedDict(
    "StopTrainingDocumentClassifierRequestRequestTypeDef",
    {
        "DocumentClassifierArn": str,
    },
)

StopTrainingEntityRecognizerRequestRequestTypeDef = TypedDict(
    "StopTrainingEntityRecognizerRequestRequestTypeDef",
    {
        "EntityRecognizerArn": str,
    },
)

SyntaxTokenTypeDef = TypedDict(
    "SyntaxTokenTypeDef",
    {
        "TokenId": int,
        "Text": str,
        "BeginOffset": int,
        "EndOffset": int,
        "PartOfSpeech": "PartOfSpeechTagTypeDef",
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

TargetedSentimentDetectionJobFilterTypeDef = TypedDict(
    "TargetedSentimentDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

TargetedSentimentDetectionJobPropertiesTypeDef = TypedDict(
    "TargetedSentimentDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "LanguageCode": LanguageCodeType,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

TargetedSentimentEntityTypeDef = TypedDict(
    "TargetedSentimentEntityTypeDef",
    {
        "DescriptiveMentionIndex": List[int],
        "Mentions": List["TargetedSentimentMentionTypeDef"],
    },
    total=False,
)

TargetedSentimentMentionTypeDef = TypedDict(
    "TargetedSentimentMentionTypeDef",
    {
        "Score": float,
        "GroupScore": float,
        "Text": str,
        "Type": TargetedSentimentEntityTypeType,
        "MentionSentiment": "MentionSentimentTypeDef",
        "BeginOffset": int,
        "EndOffset": int,
    },
    total=False,
)

TopicsDetectionJobFilterTypeDef = TypedDict(
    "TopicsDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmitTimeBefore": Union[datetime, str],
        "SubmitTimeAfter": Union[datetime, str],
    },
    total=False,
)

TopicsDetectionJobPropertiesTypeDef = TypedDict(
    "TopicsDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobArn": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "NumberOfTopics": int,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEndpointRequestRequestTypeDef",
    {
        "EndpointArn": str,
    },
)
_OptionalUpdateEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEndpointRequestRequestTypeDef",
    {
        "DesiredModelArn": str,
        "DesiredInferenceUnits": int,
        "DesiredDataAccessRoleArn": str,
    },
    total=False,
)

class UpdateEndpointRequestRequestTypeDef(
    _RequiredUpdateEndpointRequestRequestTypeDef, _OptionalUpdateEndpointRequestRequestTypeDef
):
    pass

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SecurityGroupIds": List[str],
        "Subnets": List[str],
    },
)
