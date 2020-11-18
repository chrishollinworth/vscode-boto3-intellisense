# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for comprehend service client

Usage::

    ```python
    import boto3
    from mypy_boto3_comprehend import ComprehendClient

    client: ComprehendClient = boto3.client("comprehend")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_comprehend.paginator import (
    ListDocumentClassificationJobsPaginator,
    ListDocumentClassifiersPaginator,
    ListDominantLanguageDetectionJobsPaginator,
    ListEntitiesDetectionJobsPaginator,
    ListEntityRecognizersPaginator,
    ListKeyPhrasesDetectionJobsPaginator,
    ListSentimentDetectionJobsPaginator,
    ListTopicsDetectionJobsPaginator,
)
from mypy_boto3_comprehend.type_defs import (
    BatchDetectDominantLanguageResponseTypeDef,
    BatchDetectEntitiesResponseTypeDef,
    BatchDetectKeyPhrasesResponseTypeDef,
    BatchDetectSentimentResponseTypeDef,
    BatchDetectSyntaxResponseTypeDef,
    ClassifyDocumentResponseTypeDef,
    CreateDocumentClassifierResponseTypeDef,
    CreateEndpointResponseTypeDef,
    CreateEntityRecognizerResponseTypeDef,
    DescribeDocumentClassificationJobResponseTypeDef,
    DescribeDocumentClassifierResponseTypeDef,
    DescribeDominantLanguageDetectionJobResponseTypeDef,
    DescribeEndpointResponseTypeDef,
    DescribeEntitiesDetectionJobResponseTypeDef,
    DescribeEntityRecognizerResponseTypeDef,
    DescribeKeyPhrasesDetectionJobResponseTypeDef,
    DescribePiiEntitiesDetectionJobResponseTypeDef,
    DescribeSentimentDetectionJobResponseTypeDef,
    DescribeTopicsDetectionJobResponseTypeDef,
    DetectDominantLanguageResponseTypeDef,
    DetectEntitiesResponseTypeDef,
    DetectKeyPhrasesResponseTypeDef,
    DetectPiiEntitiesResponseTypeDef,
    DetectSentimentResponseTypeDef,
    DetectSyntaxResponseTypeDef,
    DocumentClassificationJobFilterTypeDef,
    DocumentClassifierFilterTypeDef,
    DocumentClassifierInputDataConfigTypeDef,
    DocumentClassifierOutputDataConfigTypeDef,
    DominantLanguageDetectionJobFilterTypeDef,
    EndpointFilterTypeDef,
    EntitiesDetectionJobFilterTypeDef,
    EntityRecognizerFilterTypeDef,
    EntityRecognizerInputDataConfigTypeDef,
    InputDataConfigTypeDef,
    KeyPhrasesDetectionJobFilterTypeDef,
    ListDocumentClassificationJobsResponseTypeDef,
    ListDocumentClassifiersResponseTypeDef,
    ListDominantLanguageDetectionJobsResponseTypeDef,
    ListEndpointsResponseTypeDef,
    ListEntitiesDetectionJobsResponseTypeDef,
    ListEntityRecognizersResponseTypeDef,
    ListKeyPhrasesDetectionJobsResponseTypeDef,
    ListPiiEntitiesDetectionJobsResponseTypeDef,
    ListSentimentDetectionJobsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTopicsDetectionJobsResponseTypeDef,
    OutputDataConfigTypeDef,
    PiiEntitiesDetectionJobFilterTypeDef,
    RedactionConfigTypeDef,
    SentimentDetectionJobFilterTypeDef,
    StartDocumentClassificationJobResponseTypeDef,
    StartDominantLanguageDetectionJobResponseTypeDef,
    StartEntitiesDetectionJobResponseTypeDef,
    StartKeyPhrasesDetectionJobResponseTypeDef,
    StartPiiEntitiesDetectionJobResponseTypeDef,
    StartSentimentDetectionJobResponseTypeDef,
    StartTopicsDetectionJobResponseTypeDef,
    StopDominantLanguageDetectionJobResponseTypeDef,
    StopEntitiesDetectionJobResponseTypeDef,
    StopKeyPhrasesDetectionJobResponseTypeDef,
    StopPiiEntitiesDetectionJobResponseTypeDef,
    StopSentimentDetectionJobResponseTypeDef,
    TagTypeDef,
    TopicsDetectionJobFilterTypeDef,
    VpcConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ComprehendClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BatchSizeLimitExceededException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidFilterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    JobNotFoundException: Type[BotocoreClientError]
    KmsKeyValidationException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    TextSizeLimitExceededException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    TooManyTagKeysException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnsupportedLanguageException: Type[BotocoreClientError]


class ComprehendClient:
    """
    [Comprehend.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_detect_dominant_language(
        self, TextList: List[str]
    ) -> BatchDetectDominantLanguageResponseTypeDef:
        """
        [Client.batch_detect_dominant_language documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.batch_detect_dominant_language)
        """

    def batch_detect_entities(
        self,
        TextList: List[str],
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> BatchDetectEntitiesResponseTypeDef:
        """
        [Client.batch_detect_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.batch_detect_entities)
        """

    def batch_detect_key_phrases(
        self,
        TextList: List[str],
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> BatchDetectKeyPhrasesResponseTypeDef:
        """
        [Client.batch_detect_key_phrases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.batch_detect_key_phrases)
        """

    def batch_detect_sentiment(
        self,
        TextList: List[str],
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> BatchDetectSentimentResponseTypeDef:
        """
        [Client.batch_detect_sentiment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.batch_detect_sentiment)
        """

    def batch_detect_syntax(
        self, TextList: List[str], LanguageCode: Literal["en", "es", "fr", "de", "it", "pt"]
    ) -> BatchDetectSyntaxResponseTypeDef:
        """
        [Client.batch_detect_syntax documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.batch_detect_syntax)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.can_paginate)
        """

    def classify_document(self, Text: str, EndpointArn: str) -> ClassifyDocumentResponseTypeDef:
        """
        [Client.classify_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.classify_document)
        """

    def create_document_classifier(
        self,
        DocumentClassifierName: str,
        DataAccessRoleArn: str,
        InputDataConfig: "DocumentClassifierInputDataConfigTypeDef",
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        Tags: List["TagTypeDef"] = None,
        OutputDataConfig: "DocumentClassifierOutputDataConfigTypeDef" = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        Mode: Literal["MULTI_CLASS", "MULTI_LABEL"] = None,
    ) -> CreateDocumentClassifierResponseTypeDef:
        """
        [Client.create_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.create_document_classifier)
        """

    def create_endpoint(
        self,
        EndpointName: str,
        ModelArn: str,
        DesiredInferenceUnits: int,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateEndpointResponseTypeDef:
        """
        [Client.create_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.create_endpoint)
        """

    def create_entity_recognizer(
        self,
        RecognizerName: str,
        DataAccessRoleArn: str,
        InputDataConfig: "EntityRecognizerInputDataConfigTypeDef",
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
    ) -> CreateEntityRecognizerResponseTypeDef:
        """
        [Client.create_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.create_entity_recognizer)
        """

    def delete_document_classifier(self, DocumentClassifierArn: str) -> Dict[str, Any]:
        """
        [Client.delete_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.delete_document_classifier)
        """

    def delete_endpoint(self, EndpointArn: str) -> Dict[str, Any]:
        """
        [Client.delete_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.delete_endpoint)
        """

    def delete_entity_recognizer(self, EntityRecognizerArn: str) -> Dict[str, Any]:
        """
        [Client.delete_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.delete_entity_recognizer)
        """

    def describe_document_classification_job(
        self, JobId: str
    ) -> DescribeDocumentClassificationJobResponseTypeDef:
        """
        [Client.describe_document_classification_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.describe_document_classification_job)
        """

    def describe_document_classifier(
        self, DocumentClassifierArn: str
    ) -> DescribeDocumentClassifierResponseTypeDef:
        """
        [Client.describe_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.describe_document_classifier)
        """

    def describe_dominant_language_detection_job(
        self, JobId: str
    ) -> DescribeDominantLanguageDetectionJobResponseTypeDef:
        """
        [Client.describe_dominant_language_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.describe_dominant_language_detection_job)
        """

    def describe_endpoint(self, EndpointArn: str) -> DescribeEndpointResponseTypeDef:
        """
        [Client.describe_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.describe_endpoint)
        """

    def describe_entities_detection_job(
        self, JobId: str
    ) -> DescribeEntitiesDetectionJobResponseTypeDef:
        """
        [Client.describe_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.describe_entities_detection_job)
        """

    def describe_entity_recognizer(
        self, EntityRecognizerArn: str
    ) -> DescribeEntityRecognizerResponseTypeDef:
        """
        [Client.describe_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.describe_entity_recognizer)
        """

    def describe_key_phrases_detection_job(
        self, JobId: str
    ) -> DescribeKeyPhrasesDetectionJobResponseTypeDef:
        """
        [Client.describe_key_phrases_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.describe_key_phrases_detection_job)
        """

    def describe_pii_entities_detection_job(
        self, JobId: str
    ) -> DescribePiiEntitiesDetectionJobResponseTypeDef:
        """
        [Client.describe_pii_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.describe_pii_entities_detection_job)
        """

    def describe_sentiment_detection_job(
        self, JobId: str
    ) -> DescribeSentimentDetectionJobResponseTypeDef:
        """
        [Client.describe_sentiment_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.describe_sentiment_detection_job)
        """

    def describe_topics_detection_job(
        self, JobId: str
    ) -> DescribeTopicsDetectionJobResponseTypeDef:
        """
        [Client.describe_topics_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.describe_topics_detection_job)
        """

    def detect_dominant_language(self, Text: str) -> DetectDominantLanguageResponseTypeDef:
        """
        [Client.detect_dominant_language documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.detect_dominant_language)
        """

    def detect_entities(
        self,
        Text: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ] = None,
        EndpointArn: str = None,
    ) -> DetectEntitiesResponseTypeDef:
        """
        [Client.detect_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.detect_entities)
        """

    def detect_key_phrases(
        self,
        Text: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> DetectKeyPhrasesResponseTypeDef:
        """
        [Client.detect_key_phrases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.detect_key_phrases)
        """

    def detect_pii_entities(
        self,
        Text: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> DetectPiiEntitiesResponseTypeDef:
        """
        [Client.detect_pii_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.detect_pii_entities)
        """

    def detect_sentiment(
        self,
        Text: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
    ) -> DetectSentimentResponseTypeDef:
        """
        [Client.detect_sentiment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.detect_sentiment)
        """

    def detect_syntax(
        self, Text: str, LanguageCode: Literal["en", "es", "fr", "de", "it", "pt"]
    ) -> DetectSyntaxResponseTypeDef:
        """
        [Client.detect_syntax documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.detect_syntax)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.generate_presigned_url)
        """

    def list_document_classification_jobs(
        self,
        Filter: DocumentClassificationJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListDocumentClassificationJobsResponseTypeDef:
        """
        [Client.list_document_classification_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.list_document_classification_jobs)
        """

    def list_document_classifiers(
        self,
        Filter: DocumentClassifierFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListDocumentClassifiersResponseTypeDef:
        """
        [Client.list_document_classifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.list_document_classifiers)
        """

    def list_dominant_language_detection_jobs(
        self,
        Filter: DominantLanguageDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListDominantLanguageDetectionJobsResponseTypeDef:
        """
        [Client.list_dominant_language_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.list_dominant_language_detection_jobs)
        """

    def list_endpoints(
        self, Filter: EndpointFilterTypeDef = None, NextToken: str = None, MaxResults: int = None
    ) -> ListEndpointsResponseTypeDef:
        """
        [Client.list_endpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.list_endpoints)
        """

    def list_entities_detection_jobs(
        self,
        Filter: EntitiesDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListEntitiesDetectionJobsResponseTypeDef:
        """
        [Client.list_entities_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.list_entities_detection_jobs)
        """

    def list_entity_recognizers(
        self,
        Filter: EntityRecognizerFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListEntityRecognizersResponseTypeDef:
        """
        [Client.list_entity_recognizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.list_entity_recognizers)
        """

    def list_key_phrases_detection_jobs(
        self,
        Filter: KeyPhrasesDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListKeyPhrasesDetectionJobsResponseTypeDef:
        """
        [Client.list_key_phrases_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.list_key_phrases_detection_jobs)
        """

    def list_pii_entities_detection_jobs(
        self,
        Filter: PiiEntitiesDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListPiiEntitiesDetectionJobsResponseTypeDef:
        """
        [Client.list_pii_entities_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.list_pii_entities_detection_jobs)
        """

    def list_sentiment_detection_jobs(
        self,
        Filter: SentimentDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListSentimentDetectionJobsResponseTypeDef:
        """
        [Client.list_sentiment_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.list_sentiment_detection_jobs)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.list_tags_for_resource)
        """

    def list_topics_detection_jobs(
        self,
        Filter: TopicsDetectionJobFilterTypeDef = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListTopicsDetectionJobsResponseTypeDef:
        """
        [Client.list_topics_detection_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.list_topics_detection_jobs)
        """

    def start_document_classification_job(
        self,
        DocumentClassifierArn: str,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
    ) -> StartDocumentClassificationJobResponseTypeDef:
        """
        [Client.start_document_classification_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.start_document_classification_job)
        """

    def start_dominant_language_detection_job(
        self,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
    ) -> StartDominantLanguageDetectionJobResponseTypeDef:
        """
        [Client.start_dominant_language_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.start_dominant_language_detection_job)
        """

    def start_entities_detection_job(
        self,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        JobName: str = None,
        EntityRecognizerArn: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
    ) -> StartEntitiesDetectionJobResponseTypeDef:
        """
        [Client.start_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.start_entities_detection_job)
        """

    def start_key_phrases_detection_job(
        self,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
    ) -> StartKeyPhrasesDetectionJobResponseTypeDef:
        """
        [Client.start_key_phrases_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.start_key_phrases_detection_job)
        """

    def start_pii_entities_detection_job(
        self,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        Mode: Literal["ONLY_REDACTION", "ONLY_OFFSETS"],
        DataAccessRoleArn: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        RedactionConfig: "RedactionConfigTypeDef" = None,
        JobName: str = None,
        ClientRequestToken: str = None,
    ) -> StartPiiEntitiesDetectionJobResponseTypeDef:
        """
        [Client.start_pii_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.start_pii_entities_detection_job)
        """

    def start_sentiment_detection_job(
        self,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: Literal[
            "en", "es", "fr", "de", "it", "pt", "ar", "hi", "ja", "ko", "zh", "zh-TW"
        ],
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
    ) -> StartSentimentDetectionJobResponseTypeDef:
        """
        [Client.start_sentiment_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.start_sentiment_detection_job)
        """

    def start_topics_detection_job(
        self,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        JobName: str = None,
        NumberOfTopics: int = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
    ) -> StartTopicsDetectionJobResponseTypeDef:
        """
        [Client.start_topics_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.start_topics_detection_job)
        """

    def stop_dominant_language_detection_job(
        self, JobId: str
    ) -> StopDominantLanguageDetectionJobResponseTypeDef:
        """
        [Client.stop_dominant_language_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.stop_dominant_language_detection_job)
        """

    def stop_entities_detection_job(self, JobId: str) -> StopEntitiesDetectionJobResponseTypeDef:
        """
        [Client.stop_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.stop_entities_detection_job)
        """

    def stop_key_phrases_detection_job(
        self, JobId: str
    ) -> StopKeyPhrasesDetectionJobResponseTypeDef:
        """
        [Client.stop_key_phrases_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.stop_key_phrases_detection_job)
        """

    def stop_pii_entities_detection_job(
        self, JobId: str
    ) -> StopPiiEntitiesDetectionJobResponseTypeDef:
        """
        [Client.stop_pii_entities_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.stop_pii_entities_detection_job)
        """

    def stop_sentiment_detection_job(self, JobId: str) -> StopSentimentDetectionJobResponseTypeDef:
        """
        [Client.stop_sentiment_detection_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.stop_sentiment_detection_job)
        """

    def stop_training_document_classifier(self, DocumentClassifierArn: str) -> Dict[str, Any]:
        """
        [Client.stop_training_document_classifier documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.stop_training_document_classifier)
        """

    def stop_training_entity_recognizer(self, EntityRecognizerArn: str) -> Dict[str, Any]:
        """
        [Client.stop_training_entity_recognizer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.stop_training_entity_recognizer)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.untag_resource)
        """

    def update_endpoint(self, EndpointArn: str, DesiredInferenceUnits: int) -> Dict[str, Any]:
        """
        [Client.update_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Client.update_endpoint)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_document_classification_jobs"]
    ) -> ListDocumentClassificationJobsPaginator:
        """
        [Paginator.ListDocumentClassificationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassificationJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_document_classifiers"]
    ) -> ListDocumentClassifiersPaginator:
        """
        [Paginator.ListDocumentClassifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassifiers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dominant_language_detection_jobs"]
    ) -> ListDominantLanguageDetectionJobsPaginator:
        """
        [Paginator.ListDominantLanguageDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListDominantLanguageDetectionJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_entities_detection_jobs"]
    ) -> ListEntitiesDetectionJobsPaginator:
        """
        [Paginator.ListEntitiesDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListEntitiesDetectionJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_entity_recognizers"]
    ) -> ListEntityRecognizersPaginator:
        """
        [Paginator.ListEntityRecognizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListEntityRecognizers)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_key_phrases_detection_jobs"]
    ) -> ListKeyPhrasesDetectionJobsPaginator:
        """
        [Paginator.ListKeyPhrasesDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListKeyPhrasesDetectionJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_sentiment_detection_jobs"]
    ) -> ListSentimentDetectionJobsPaginator:
        """
        [Paginator.ListSentimentDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListSentimentDetectionJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_topics_detection_jobs"]
    ) -> ListTopicsDetectionJobsPaginator:
        """
        [Paginator.ListTopicsDetectionJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/comprehend.html#Comprehend.Paginator.ListTopicsDetectionJobs)
        """
