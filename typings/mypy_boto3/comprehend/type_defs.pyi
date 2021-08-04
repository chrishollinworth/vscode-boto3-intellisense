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
    DocumentClassifierDataFormatType,
    DocumentClassifierModeType,
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
    SyntaxLanguageCodeType,
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
    "DescribeSentimentDetectionJobRequestRequestTypeDef",
    "DescribeSentimentDetectionJobResponseTypeDef",
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
    "DocumentClassTypeDef",
    "DocumentClassificationJobFilterTypeDef",
    "DocumentClassificationJobPropertiesTypeDef",
    "DocumentClassifierFilterTypeDef",
    "DocumentClassifierInputDataConfigTypeDef",
    "DocumentClassifierOutputDataConfigTypeDef",
    "DocumentClassifierPropertiesTypeDef",
    "DocumentLabelTypeDef",
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
    "EntityTypeDef",
    "EntityTypesEvaluationMetricsTypeDef",
    "EntityTypesListItemTypeDef",
    "EventsDetectionJobFilterTypeDef",
    "EventsDetectionJobPropertiesTypeDef",
    "InputDataConfigTypeDef",
    "KeyPhraseTypeDef",
    "KeyPhrasesDetectionJobFilterTypeDef",
    "KeyPhrasesDetectionJobPropertiesTypeDef",
    "ListDocumentClassificationJobsRequestRequestTypeDef",
    "ListDocumentClassificationJobsResponseTypeDef",
    "ListDocumentClassifiersRequestRequestTypeDef",
    "ListDocumentClassifiersResponseTypeDef",
    "ListDominantLanguageDetectionJobsRequestRequestTypeDef",
    "ListDominantLanguageDetectionJobsResponseTypeDef",
    "ListEndpointsRequestRequestTypeDef",
    "ListEndpointsResponseTypeDef",
    "ListEntitiesDetectionJobsRequestRequestTypeDef",
    "ListEntitiesDetectionJobsResponseTypeDef",
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
    "ListTopicsDetectionJobsRequestRequestTypeDef",
    "ListTopicsDetectionJobsResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PartOfSpeechTagTypeDef",
    "PiiEntitiesDetectionJobFilterTypeDef",
    "PiiEntitiesDetectionJobPropertiesTypeDef",
    "PiiEntityTypeDef",
    "PiiOutputDataConfigTypeDef",
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
    "StopTrainingDocumentClassifierRequestRequestTypeDef",
    "StopTrainingEntityRecognizerRequestRequestTypeDef",
    "SyntaxTokenTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TopicsDetectionJobFilterTypeDef",
    "TopicsDetectionJobPropertiesTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEndpointRequestRequestTypeDef",
    "VpcConfigTypeDef",
)

AugmentedManifestsListItemTypeDef = TypedDict(
    "AugmentedManifestsListItemTypeDef",
    {
        "S3Uri": str,
        "AttributeNames": List[str],
    },
)

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
        "Tags": List["TagTypeDef"],
        "OutputDataConfig": "DocumentClassifierOutputDataConfigTypeDef",
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "Mode": DocumentClassifierModeType,
        "ModelKmsKeyId": str,
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
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "ModelKmsKeyId": str,
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
        "DesiredInferenceUnits": int,
        "CurrentInferenceUnits": int,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "DataAccessRoleArn": str,
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

EntityRecognizerAnnotationsTypeDef = TypedDict(
    "EntityRecognizerAnnotationsTypeDef",
    {
        "S3Uri": str,
    },
)

EntityRecognizerDocumentsTypeDef = TypedDict(
    "EntityRecognizerDocumentsTypeDef",
    {
        "S3Uri": str,
    },
)

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

UpdateEndpointRequestRequestTypeDef = TypedDict(
    "UpdateEndpointRequestRequestTypeDef",
    {
        "EndpointArn": str,
        "DesiredInferenceUnits": int,
    },
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SecurityGroupIds": List[str],
        "Subnets": List[str],
    },
)
