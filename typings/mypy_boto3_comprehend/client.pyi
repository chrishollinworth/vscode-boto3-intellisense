"""
Type annotations for comprehend service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_comprehend import ComprehendClient

    client: ComprehendClient = boto3.client("comprehend")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    DatasetTypeType,
    DocumentClassifierModeType,
    LanguageCodeType,
    ModelTypeType,
    PiiEntitiesDetectionModeType,
    SyntaxLanguageCodeType,
)
from .paginator import (
    ListDocumentClassificationJobsPaginator,
    ListDocumentClassifiersPaginator,
    ListDominantLanguageDetectionJobsPaginator,
    ListEndpointsPaginator,
    ListEntitiesDetectionJobsPaginator,
    ListEntityRecognizersPaginator,
    ListKeyPhrasesDetectionJobsPaginator,
    ListPiiEntitiesDetectionJobsPaginator,
    ListSentimentDetectionJobsPaginator,
    ListTopicsDetectionJobsPaginator,
)
from .type_defs import (
    BatchDetectDominantLanguageResponseTypeDef,
    BatchDetectEntitiesResponseTypeDef,
    BatchDetectKeyPhrasesResponseTypeDef,
    BatchDetectSentimentResponseTypeDef,
    BatchDetectSyntaxResponseTypeDef,
    BatchDetectTargetedSentimentResponseTypeDef,
    ClassifyDocumentResponseTypeDef,
    ContainsPiiEntitiesResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateDocumentClassifierResponseTypeDef,
    CreateEndpointResponseTypeDef,
    CreateEntityRecognizerResponseTypeDef,
    CreateFlywheelResponseTypeDef,
    DataSecurityConfigTypeDef,
    DatasetFilterTypeDef,
    DatasetInputDataConfigTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeDocumentClassificationJobResponseTypeDef,
    DescribeDocumentClassifierResponseTypeDef,
    DescribeDominantLanguageDetectionJobResponseTypeDef,
    DescribeEndpointResponseTypeDef,
    DescribeEntitiesDetectionJobResponseTypeDef,
    DescribeEntityRecognizerResponseTypeDef,
    DescribeEventsDetectionJobResponseTypeDef,
    DescribeFlywheelIterationResponseTypeDef,
    DescribeFlywheelResponseTypeDef,
    DescribeKeyPhrasesDetectionJobResponseTypeDef,
    DescribePiiEntitiesDetectionJobResponseTypeDef,
    DescribeResourcePolicyResponseTypeDef,
    DescribeSentimentDetectionJobResponseTypeDef,
    DescribeTargetedSentimentDetectionJobResponseTypeDef,
    DescribeTopicsDetectionJobResponseTypeDef,
    DetectDominantLanguageResponseTypeDef,
    DetectEntitiesResponseTypeDef,
    DetectKeyPhrasesResponseTypeDef,
    DetectPiiEntitiesResponseTypeDef,
    DetectSentimentResponseTypeDef,
    DetectSyntaxResponseTypeDef,
    DetectTargetedSentimentResponseTypeDef,
    DocumentClassificationJobFilterTypeDef,
    DocumentClassifierFilterTypeDef,
    DocumentClassifierInputDataConfigTypeDef,
    DocumentClassifierOutputDataConfigTypeDef,
    DocumentReaderConfigTypeDef,
    DominantLanguageDetectionJobFilterTypeDef,
    EndpointFilterTypeDef,
    EntitiesDetectionJobFilterTypeDef,
    EntityRecognizerFilterTypeDef,
    EntityRecognizerInputDataConfigTypeDef,
    EventsDetectionJobFilterTypeDef,
    FlywheelFilterTypeDef,
    FlywheelIterationFilterTypeDef,
    ImportModelResponseTypeDef,
    InputDataConfigTypeDef,
    KeyPhrasesDetectionJobFilterTypeDef,
    ListDatasetsResponseTypeDef,
    ListDocumentClassificationJobsResponseTypeDef,
    ListDocumentClassifiersResponseTypeDef,
    ListDocumentClassifierSummariesResponseTypeDef,
    ListDominantLanguageDetectionJobsResponseTypeDef,
    ListEndpointsResponseTypeDef,
    ListEntitiesDetectionJobsResponseTypeDef,
    ListEntityRecognizersResponseTypeDef,
    ListEntityRecognizerSummariesResponseTypeDef,
    ListEventsDetectionJobsResponseTypeDef,
    ListFlywheelIterationHistoryResponseTypeDef,
    ListFlywheelsResponseTypeDef,
    ListKeyPhrasesDetectionJobsResponseTypeDef,
    ListPiiEntitiesDetectionJobsResponseTypeDef,
    ListSentimentDetectionJobsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTargetedSentimentDetectionJobsResponseTypeDef,
    ListTopicsDetectionJobsResponseTypeDef,
    OutputDataConfigTypeDef,
    PiiEntitiesDetectionJobFilterTypeDef,
    PutResourcePolicyResponseTypeDef,
    RedactionConfigTypeDef,
    SentimentDetectionJobFilterTypeDef,
    StartDocumentClassificationJobResponseTypeDef,
    StartDominantLanguageDetectionJobResponseTypeDef,
    StartEntitiesDetectionJobResponseTypeDef,
    StartEventsDetectionJobResponseTypeDef,
    StartFlywheelIterationResponseTypeDef,
    StartKeyPhrasesDetectionJobResponseTypeDef,
    StartPiiEntitiesDetectionJobResponseTypeDef,
    StartSentimentDetectionJobResponseTypeDef,
    StartTargetedSentimentDetectionJobResponseTypeDef,
    StartTopicsDetectionJobResponseTypeDef,
    StopDominantLanguageDetectionJobResponseTypeDef,
    StopEntitiesDetectionJobResponseTypeDef,
    StopEventsDetectionJobResponseTypeDef,
    StopKeyPhrasesDetectionJobResponseTypeDef,
    StopPiiEntitiesDetectionJobResponseTypeDef,
    StopSentimentDetectionJobResponseTypeDef,
    StopTargetedSentimentDetectionJobResponseTypeDef,
    TagTypeDef,
    TargetedSentimentDetectionJobFilterTypeDef,
    TaskConfigTypeDef,
    TopicsDetectionJobFilterTypeDef,
    UpdateDataSecurityConfigTypeDef,
    UpdateEndpointResponseTypeDef,
    UpdateFlywheelResponseTypeDef,
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

class ComprehendClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ComprehendClient exceptions.
        """
    def batch_detect_dominant_language(
        self, *, TextList: List[str]
    ) -> BatchDetectDominantLanguageResponseTypeDef:
        """
        Determines the dominant language of the input text for a batch of documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.batch_detect_dominant_language)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#batch_detect_dominant_language)
        """
    def batch_detect_entities(
        self, *, TextList: List[str], LanguageCode: LanguageCodeType
    ) -> BatchDetectEntitiesResponseTypeDef:
        """
        Inspects the text of a batch of documents for named entities and returns
        information about them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.batch_detect_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#batch_detect_entities)
        """
    def batch_detect_key_phrases(
        self, *, TextList: List[str], LanguageCode: LanguageCodeType
    ) -> BatchDetectKeyPhrasesResponseTypeDef:
        """
        Detects the key noun phrases found in a batch of documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.batch_detect_key_phrases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#batch_detect_key_phrases)
        """
    def batch_detect_sentiment(
        self, *, TextList: List[str], LanguageCode: LanguageCodeType
    ) -> BatchDetectSentimentResponseTypeDef:
        """
        Inspects a batch of documents and returns an inference of the prevailing
        sentiment, `POSITIVE`, `NEUTRAL`, `MIXED`, or `NEGATIVE`, in each one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.batch_detect_sentiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#batch_detect_sentiment)
        """
    def batch_detect_syntax(
        self, *, TextList: List[str], LanguageCode: SyntaxLanguageCodeType
    ) -> BatchDetectSyntaxResponseTypeDef:
        """
        Inspects the text of a batch of documents for the syntax and part of speech of
        the words in the document and returns information about them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.batch_detect_syntax)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#batch_detect_syntax)
        """
    def batch_detect_targeted_sentiment(
        self, *, TextList: List[str], LanguageCode: LanguageCodeType
    ) -> BatchDetectTargetedSentimentResponseTypeDef:
        """
        Inspects a batch of documents and returns a sentiment analysis for each entity
        identified in the documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.batch_detect_targeted_sentiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#batch_detect_targeted_sentiment)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#can_paginate)
        """
    def classify_document(
        self,
        *,
        EndpointArn: str,
        Text: str = None,
        Bytes: Union[bytes, IO[bytes], StreamingBody] = None,
        DocumentReaderConfig: "DocumentReaderConfigTypeDef" = None
    ) -> ClassifyDocumentResponseTypeDef:
        """
        Creates a new document classification request to analyze a single document in
        real-time, using a previously created and trained custom model and an endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.classify_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#classify_document)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#close)
        """
    def contains_pii_entities(
        self, *, Text: str, LanguageCode: LanguageCodeType
    ) -> ContainsPiiEntitiesResponseTypeDef:
        """
        Analyzes input text for the presence of personally identifiable information
        (PII) and returns the labels of identified PII entity types such as name,
        address, bank account number, or phone number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.contains_pii_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#contains_pii_entities)
        """
    def create_dataset(
        self,
        *,
        FlywheelArn: str,
        DatasetName: str,
        InputDataConfig: "DatasetInputDataConfigTypeDef",
        DatasetType: DatasetTypeType = None,
        Description: str = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDatasetResponseTypeDef:
        """
        Creates a dataset to upload training or test data for a model associated with a
        flywheel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.create_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#create_dataset)
        """
    def create_document_classifier(
        self,
        *,
        DocumentClassifierName: str,
        DataAccessRoleArn: str,
        InputDataConfig: "DocumentClassifierInputDataConfigTypeDef",
        LanguageCode: LanguageCodeType,
        VersionName: str = None,
        Tags: List["TagTypeDef"] = None,
        OutputDataConfig: "DocumentClassifierOutputDataConfigTypeDef" = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        Mode: DocumentClassifierModeType = None,
        ModelKmsKeyId: str = None,
        ModelPolicy: str = None
    ) -> CreateDocumentClassifierResponseTypeDef:
        """
        Creates a new document classifier that you can use to categorize documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.create_document_classifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#create_document_classifier)
        """
    def create_endpoint(
        self,
        *,
        EndpointName: str,
        DesiredInferenceUnits: int,
        ModelArn: str = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None,
        DataAccessRoleArn: str = None,
        FlywheelArn: str = None
    ) -> CreateEndpointResponseTypeDef:
        """
        Creates a model-specific endpoint for synchronous inference for a previously
        trained custom model For information about endpoints, see `Managing endpoints
        <https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.create_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#create_endpoint)
        """
    def create_entity_recognizer(
        self,
        *,
        RecognizerName: str,
        DataAccessRoleArn: str,
        InputDataConfig: "EntityRecognizerInputDataConfigTypeDef",
        LanguageCode: LanguageCodeType,
        VersionName: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        ModelKmsKeyId: str = None,
        ModelPolicy: str = None
    ) -> CreateEntityRecognizerResponseTypeDef:
        """
        Creates an entity recognizer using submitted files.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.create_entity_recognizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#create_entity_recognizer)
        """
    def create_flywheel(
        self,
        *,
        FlywheelName: str,
        DataAccessRoleArn: str,
        DataLakeS3Uri: str,
        ActiveModelArn: str = None,
        TaskConfig: "TaskConfigTypeDef" = None,
        ModelType: ModelTypeType = None,
        DataSecurityConfig: "DataSecurityConfigTypeDef" = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateFlywheelResponseTypeDef:
        """
        A flywheel is an Amazon Web Services resource that orchestrates the ongoing
        training of a model for custom classification or custom entity recognition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.create_flywheel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#create_flywheel)
        """
    def delete_document_classifier(self, *, DocumentClassifierArn: str) -> Dict[str, Any]:
        """
        Deletes a previously created document classifier Only those classifiers that are
        in terminated states (IN_ERROR, TRAINED) will be deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.delete_document_classifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#delete_document_classifier)
        """
    def delete_endpoint(self, *, EndpointArn: str) -> Dict[str, Any]:
        """
        Deletes a model-specific endpoint for a previously-trained custom model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.delete_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#delete_endpoint)
        """
    def delete_entity_recognizer(self, *, EntityRecognizerArn: str) -> Dict[str, Any]:
        """
        Deletes an entity recognizer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.delete_entity_recognizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#delete_entity_recognizer)
        """
    def delete_flywheel(self, *, FlywheelArn: str) -> Dict[str, Any]:
        """
        Deletes a flywheel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.delete_flywheel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#delete_flywheel)
        """
    def delete_resource_policy(
        self, *, ResourceArn: str, PolicyRevisionId: str = None
    ) -> Dict[str, Any]:
        """
        Deletes a resource-based policy that is attached to a custom model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#delete_resource_policy)
        """
    def describe_dataset(self, *, DatasetArn: str) -> DescribeDatasetResponseTypeDef:
        """
        Returns information about the dataset that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_dataset)
        """
    def describe_document_classification_job(
        self, *, JobId: str
    ) -> DescribeDocumentClassificationJobResponseTypeDef:
        """
        Gets the properties associated with a document classification job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_document_classification_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_document_classification_job)
        """
    def describe_document_classifier(
        self, *, DocumentClassifierArn: str
    ) -> DescribeDocumentClassifierResponseTypeDef:
        """
        Gets the properties associated with a document classifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_document_classifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_document_classifier)
        """
    def describe_dominant_language_detection_job(
        self, *, JobId: str
    ) -> DescribeDominantLanguageDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a dominant language detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_dominant_language_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_dominant_language_detection_job)
        """
    def describe_endpoint(self, *, EndpointArn: str) -> DescribeEndpointResponseTypeDef:
        """
        Gets the properties associated with a specific endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_endpoint)
        """
    def describe_entities_detection_job(
        self, *, JobId: str
    ) -> DescribeEntitiesDetectionJobResponseTypeDef:
        """
        Gets the properties associated with an entities detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_entities_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_entities_detection_job)
        """
    def describe_entity_recognizer(
        self, *, EntityRecognizerArn: str
    ) -> DescribeEntityRecognizerResponseTypeDef:
        """
        Provides details about an entity recognizer including status, S3 buckets
        containing training data, recognizer metadata, metrics, and so on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_entity_recognizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_entity_recognizer)
        """
    def describe_events_detection_job(
        self, *, JobId: str
    ) -> DescribeEventsDetectionJobResponseTypeDef:
        """
        Gets the status and details of an events detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_events_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_events_detection_job)
        """
    def describe_flywheel(self, *, FlywheelArn: str) -> DescribeFlywheelResponseTypeDef:
        """
        Provides configuration information about the flywheel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_flywheel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_flywheel)
        """
    def describe_flywheel_iteration(
        self, *, FlywheelArn: str, FlywheelIterationId: str
    ) -> DescribeFlywheelIterationResponseTypeDef:
        """
        Retrieve the configuration properties of a flywheel iteration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_flywheel_iteration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_flywheel_iteration)
        """
    def describe_key_phrases_detection_job(
        self, *, JobId: str
    ) -> DescribeKeyPhrasesDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a key phrases detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_key_phrases_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_key_phrases_detection_job)
        """
    def describe_pii_entities_detection_job(
        self, *, JobId: str
    ) -> DescribePiiEntitiesDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a PII entities detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_pii_entities_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_pii_entities_detection_job)
        """
    def describe_resource_policy(
        self, *, ResourceArn: str
    ) -> DescribeResourcePolicyResponseTypeDef:
        """
        Gets the details of a resource-based policy that is attached to a custom model,
        including the JSON body of the policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_resource_policy)
        """
    def describe_sentiment_detection_job(
        self, *, JobId: str
    ) -> DescribeSentimentDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a sentiment detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_sentiment_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_sentiment_detection_job)
        """
    def describe_targeted_sentiment_detection_job(
        self, *, JobId: str
    ) -> DescribeTargetedSentimentDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a targeted sentiment detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_targeted_sentiment_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_targeted_sentiment_detection_job)
        """
    def describe_topics_detection_job(
        self, *, JobId: str
    ) -> DescribeTopicsDetectionJobResponseTypeDef:
        """
        Gets the properties associated with a topic detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.describe_topics_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#describe_topics_detection_job)
        """
    def detect_dominant_language(self, *, Text: str) -> DetectDominantLanguageResponseTypeDef:
        """
        Determines the dominant language of the input text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.detect_dominant_language)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#detect_dominant_language)
        """
    def detect_entities(
        self,
        *,
        Text: str = None,
        LanguageCode: LanguageCodeType = None,
        EndpointArn: str = None,
        Bytes: Union[bytes, IO[bytes], StreamingBody] = None,
        DocumentReaderConfig: "DocumentReaderConfigTypeDef" = None
    ) -> DetectEntitiesResponseTypeDef:
        """
        Detects named entities in input text when you use the pre-trained model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.detect_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#detect_entities)
        """
    def detect_key_phrases(
        self, *, Text: str, LanguageCode: LanguageCodeType
    ) -> DetectKeyPhrasesResponseTypeDef:
        """
        Detects the key noun phrases found in the text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.detect_key_phrases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#detect_key_phrases)
        """
    def detect_pii_entities(
        self, *, Text: str, LanguageCode: LanguageCodeType
    ) -> DetectPiiEntitiesResponseTypeDef:
        """
        Inspects the input text for entities that contain personally identifiable
        information (PII) and returns information about them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.detect_pii_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#detect_pii_entities)
        """
    def detect_sentiment(
        self, *, Text: str, LanguageCode: LanguageCodeType
    ) -> DetectSentimentResponseTypeDef:
        """
        Inspects text and returns an inference of the prevailing sentiment ( `POSITIVE`,
        `NEUTRAL`, `MIXED`, or `NEGATIVE`).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.detect_sentiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#detect_sentiment)
        """
    def detect_syntax(
        self, *, Text: str, LanguageCode: SyntaxLanguageCodeType
    ) -> DetectSyntaxResponseTypeDef:
        """
        Inspects text for syntax and the part of speech of words in the document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.detect_syntax)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#detect_syntax)
        """
    def detect_targeted_sentiment(
        self, *, Text: str, LanguageCode: LanguageCodeType
    ) -> DetectTargetedSentimentResponseTypeDef:
        """
        Inspects the input text and returns a sentiment analysis for each entity
        identified in the text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.detect_targeted_sentiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#detect_targeted_sentiment)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#generate_presigned_url)
        """
    def import_model(
        self,
        *,
        SourceModelArn: str,
        ModelName: str = None,
        VersionName: str = None,
        ModelKmsKeyId: str = None,
        DataAccessRoleArn: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> ImportModelResponseTypeDef:
        """
        Creates a new custom model that replicates a source custom model that you
        import.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.import_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#import_model)
        """
    def list_datasets(
        self,
        *,
        FlywheelArn: str = None,
        Filter: "DatasetFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        List the datasets that you have configured in this Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_datasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_datasets)
        """
    def list_document_classification_jobs(
        self,
        *,
        Filter: "DocumentClassificationJobFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListDocumentClassificationJobsResponseTypeDef:
        """
        Gets a list of the documentation classification jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_document_classification_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_document_classification_jobs)
        """
    def list_document_classifier_summaries(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListDocumentClassifierSummariesResponseTypeDef:
        """
        Gets a list of summaries of the document classifiers that you have created See
        also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/comprehend
        -2017-11-27/ListDocumentClassifierSummaries>`_ **Request Syntax** response =
        client.list_document_classifier_summaries( N...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_document_classifier_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_document_classifier_summaries)
        """
    def list_document_classifiers(
        self,
        *,
        Filter: "DocumentClassifierFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListDocumentClassifiersResponseTypeDef:
        """
        Gets a list of the document classifiers that you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_document_classifiers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_document_classifiers)
        """
    def list_dominant_language_detection_jobs(
        self,
        *,
        Filter: "DominantLanguageDetectionJobFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListDominantLanguageDetectionJobsResponseTypeDef:
        """
        Gets a list of the dominant language detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_dominant_language_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_dominant_language_detection_jobs)
        """
    def list_endpoints(
        self,
        *,
        Filter: "EndpointFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListEndpointsResponseTypeDef:
        """
        Gets a list of all existing endpoints that you've created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_endpoints)
        """
    def list_entities_detection_jobs(
        self,
        *,
        Filter: "EntitiesDetectionJobFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListEntitiesDetectionJobsResponseTypeDef:
        """
        Gets a list of the entity detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_entities_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_entities_detection_jobs)
        """
    def list_entity_recognizer_summaries(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListEntityRecognizerSummariesResponseTypeDef:
        """
        Gets a list of summaries for the entity recognizers that you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_entity_recognizer_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_entity_recognizer_summaries)
        """
    def list_entity_recognizers(
        self,
        *,
        Filter: "EntityRecognizerFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListEntityRecognizersResponseTypeDef:
        """
        Gets a list of the properties of all entity recognizers that you created,
        including recognizers currently in training.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_entity_recognizers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_entity_recognizers)
        """
    def list_events_detection_jobs(
        self,
        *,
        Filter: "EventsDetectionJobFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListEventsDetectionJobsResponseTypeDef:
        """
        Gets a list of the events detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_events_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_events_detection_jobs)
        """
    def list_flywheel_iteration_history(
        self,
        *,
        FlywheelArn: str,
        Filter: "FlywheelIterationFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListFlywheelIterationHistoryResponseTypeDef:
        """
        Information about the history of a flywheel iteration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_flywheel_iteration_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_flywheel_iteration_history)
        """
    def list_flywheels(
        self,
        *,
        Filter: "FlywheelFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListFlywheelsResponseTypeDef:
        """
        Gets a list of the flywheels that you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_flywheels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_flywheels)
        """
    def list_key_phrases_detection_jobs(
        self,
        *,
        Filter: "KeyPhrasesDetectionJobFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListKeyPhrasesDetectionJobsResponseTypeDef:
        """
        Get a list of key phrase detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_key_phrases_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_key_phrases_detection_jobs)
        """
    def list_pii_entities_detection_jobs(
        self,
        *,
        Filter: "PiiEntitiesDetectionJobFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListPiiEntitiesDetectionJobsResponseTypeDef:
        """
        Gets a list of the PII entity detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_pii_entities_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_pii_entities_detection_jobs)
        """
    def list_sentiment_detection_jobs(
        self,
        *,
        Filter: "SentimentDetectionJobFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListSentimentDetectionJobsResponseTypeDef:
        """
        Gets a list of sentiment detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_sentiment_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_sentiment_detection_jobs)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with a given Amazon Comprehend resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_tags_for_resource)
        """
    def list_targeted_sentiment_detection_jobs(
        self,
        *,
        Filter: "TargetedSentimentDetectionJobFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListTargetedSentimentDetectionJobsResponseTypeDef:
        """
        Gets a list of targeted sentiment detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_targeted_sentiment_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_targeted_sentiment_detection_jobs)
        """
    def list_topics_detection_jobs(
        self,
        *,
        Filter: "TopicsDetectionJobFilterTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListTopicsDetectionJobsResponseTypeDef:
        """
        Gets a list of the topic detection jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.list_topics_detection_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#list_topics_detection_jobs)
        """
    def put_resource_policy(
        self, *, ResourceArn: str, ResourcePolicy: str, PolicyRevisionId: str = None
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Attaches a resource-based policy to a custom model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#put_resource_policy)
        """
    def start_document_classification_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        JobName: str = None,
        DocumentClassifierArn: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        FlywheelArn: str = None
    ) -> StartDocumentClassificationJobResponseTypeDef:
        """
        Starts an asynchronous document classification job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.start_document_classification_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_document_classification_job)
        """
    def start_dominant_language_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> StartDominantLanguageDetectionJobResponseTypeDef:
        """
        Starts an asynchronous dominant language detection job for a collection of
        documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.start_dominant_language_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_dominant_language_detection_job)
        """
    def start_entities_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: LanguageCodeType,
        JobName: str = None,
        EntityRecognizerArn: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        FlywheelArn: str = None
    ) -> StartEntitiesDetectionJobResponseTypeDef:
        """
        Starts an asynchronous entity detection job for a collection of documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.start_entities_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_entities_detection_job)
        """
    def start_events_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: LanguageCodeType,
        TargetEventTypes: List[str],
        JobName: str = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> StartEventsDetectionJobResponseTypeDef:
        """
        Starts an asynchronous event detection job for a collection of documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.start_events_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_events_detection_job)
        """
    def start_flywheel_iteration(
        self, *, FlywheelArn: str, ClientRequestToken: str = None
    ) -> StartFlywheelIterationResponseTypeDef:
        """
        Start the flywheel iteration.This operation uses any new datasets to train a new
        model version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.start_flywheel_iteration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_flywheel_iteration)
        """
    def start_key_phrases_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: LanguageCodeType,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> StartKeyPhrasesDetectionJobResponseTypeDef:
        """
        Starts an asynchronous key phrase detection job for a collection of documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.start_key_phrases_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_key_phrases_detection_job)
        """
    def start_pii_entities_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        Mode: PiiEntitiesDetectionModeType,
        DataAccessRoleArn: str,
        LanguageCode: LanguageCodeType,
        RedactionConfig: "RedactionConfigTypeDef" = None,
        JobName: str = None,
        ClientRequestToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> StartPiiEntitiesDetectionJobResponseTypeDef:
        """
        Starts an asynchronous PII entity detection job for a collection of documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.start_pii_entities_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_pii_entities_detection_job)
        """
    def start_sentiment_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: LanguageCodeType,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> StartSentimentDetectionJobResponseTypeDef:
        """
        Starts an asynchronous sentiment detection job for a collection of documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.start_sentiment_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_sentiment_detection_job)
        """
    def start_targeted_sentiment_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        LanguageCode: LanguageCodeType,
        JobName: str = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> StartTargetedSentimentDetectionJobResponseTypeDef:
        """
        Starts an asynchronous targeted sentiment detection job for a collection of
        documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.start_targeted_sentiment_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_targeted_sentiment_detection_job)
        """
    def start_topics_detection_job(
        self,
        *,
        InputDataConfig: "InputDataConfigTypeDef",
        OutputDataConfig: "OutputDataConfigTypeDef",
        DataAccessRoleArn: str,
        JobName: str = None,
        NumberOfTopics: int = None,
        ClientRequestToken: str = None,
        VolumeKmsKeyId: str = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> StartTopicsDetectionJobResponseTypeDef:
        """
        Starts an asynchronous topic detection job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.start_topics_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#start_topics_detection_job)
        """
    def stop_dominant_language_detection_job(
        self, *, JobId: str
    ) -> StopDominantLanguageDetectionJobResponseTypeDef:
        """
        Stops a dominant language detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.stop_dominant_language_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_dominant_language_detection_job)
        """
    def stop_entities_detection_job(self, *, JobId: str) -> StopEntitiesDetectionJobResponseTypeDef:
        """
        Stops an entities detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.stop_entities_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_entities_detection_job)
        """
    def stop_events_detection_job(self, *, JobId: str) -> StopEventsDetectionJobResponseTypeDef:
        """
        Stops an events detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.stop_events_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_events_detection_job)
        """
    def stop_key_phrases_detection_job(
        self, *, JobId: str
    ) -> StopKeyPhrasesDetectionJobResponseTypeDef:
        """
        Stops a key phrases detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.stop_key_phrases_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_key_phrases_detection_job)
        """
    def stop_pii_entities_detection_job(
        self, *, JobId: str
    ) -> StopPiiEntitiesDetectionJobResponseTypeDef:
        """
        Stops a PII entities detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.stop_pii_entities_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_pii_entities_detection_job)
        """
    def stop_sentiment_detection_job(
        self, *, JobId: str
    ) -> StopSentimentDetectionJobResponseTypeDef:
        """
        Stops a sentiment detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.stop_sentiment_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_sentiment_detection_job)
        """
    def stop_targeted_sentiment_detection_job(
        self, *, JobId: str
    ) -> StopTargetedSentimentDetectionJobResponseTypeDef:
        """
        Stops a targeted sentiment detection job in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.stop_targeted_sentiment_detection_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_targeted_sentiment_detection_job)
        """
    def stop_training_document_classifier(self, *, DocumentClassifierArn: str) -> Dict[str, Any]:
        """
        Stops a document classifier training job while in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.stop_training_document_classifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_training_document_classifier)
        """
    def stop_training_entity_recognizer(self, *, EntityRecognizerArn: str) -> Dict[str, Any]:
        """
        Stops an entity recognizer training job while in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.stop_training_entity_recognizer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#stop_training_entity_recognizer)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Associates a specific tag with an Amazon Comprehend resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a specific tag associated with an Amazon Comprehend resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#untag_resource)
        """
    def update_endpoint(
        self,
        *,
        EndpointArn: str,
        DesiredModelArn: str = None,
        DesiredInferenceUnits: int = None,
        DesiredDataAccessRoleArn: str = None,
        FlywheelArn: str = None
    ) -> UpdateEndpointResponseTypeDef:
        """
        Updates information about the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.update_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#update_endpoint)
        """
    def update_flywheel(
        self,
        *,
        FlywheelArn: str,
        ActiveModelArn: str = None,
        DataAccessRoleArn: str = None,
        DataSecurityConfig: "UpdateDataSecurityConfigTypeDef" = None
    ) -> UpdateFlywheelResponseTypeDef:
        """
        Update the configuration information for an existing flywheel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Client.update_flywheel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/client.html#update_flywheel)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_document_classification_jobs"]
    ) -> ListDocumentClassificationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassificationJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listdocumentclassificationjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_document_classifiers"]
    ) -> ListDocumentClassifiersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Paginator.ListDocumentClassifiers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listdocumentclassifierspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dominant_language_detection_jobs"]
    ) -> ListDominantLanguageDetectionJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Paginator.ListDominantLanguageDetectionJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listdominantlanguagedetectionjobspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_endpoints"]) -> ListEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Paginator.ListEndpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listendpointspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_entities_detection_jobs"]
    ) -> ListEntitiesDetectionJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Paginator.ListEntitiesDetectionJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listentitiesdetectionjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_entity_recognizers"]
    ) -> ListEntityRecognizersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Paginator.ListEntityRecognizers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listentityrecognizerspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_key_phrases_detection_jobs"]
    ) -> ListKeyPhrasesDetectionJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Paginator.ListKeyPhrasesDetectionJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listkeyphrasesdetectionjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_pii_entities_detection_jobs"]
    ) -> ListPiiEntitiesDetectionJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Paginator.ListPiiEntitiesDetectionJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listpiientitiesdetectionjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_sentiment_detection_jobs"]
    ) -> ListSentimentDetectionJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Paginator.ListSentimentDetectionJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listsentimentdetectionjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_topics_detection_jobs"]
    ) -> ListTopicsDetectionJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/comprehend.html#Comprehend.Paginator.ListTopicsDetectionJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/paginators.html#listtopicsdetectionjobspaginator)
        """
