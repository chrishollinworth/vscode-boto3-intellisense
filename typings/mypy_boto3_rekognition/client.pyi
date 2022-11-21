"""
Type annotations for rekognition service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_rekognition import RekognitionClient

    client: RekognitionClient = boto3.client("rekognition")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AttributeType,
    CelebrityRecognitionSortByType,
    ContentModerationSortByType,
    DatasetTypeType,
    DetectLabelsFeatureNameType,
    FaceAttributesType,
    FaceSearchSortByType,
    LabelDetectionSortByType,
    PersonTrackingSortByType,
    QualityFilterType,
    SegmentTypeType,
    StreamProcessorParameterToDeleteType,
)
from .paginator import (
    DescribeProjectsPaginator,
    DescribeProjectVersionsPaginator,
    ListCollectionsPaginator,
    ListDatasetEntriesPaginator,
    ListDatasetLabelsPaginator,
    ListFacesPaginator,
    ListProjectPoliciesPaginator,
    ListStreamProcessorsPaginator,
)
from .type_defs import (
    CompareFacesResponseTypeDef,
    CopyProjectVersionResponseTypeDef,
    CreateCollectionResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateProjectResponseTypeDef,
    CreateProjectVersionResponseTypeDef,
    CreateStreamProcessorResponseTypeDef,
    DatasetChangesTypeDef,
    DatasetSourceTypeDef,
    DeleteCollectionResponseTypeDef,
    DeleteFacesResponseTypeDef,
    DeleteProjectResponseTypeDef,
    DeleteProjectVersionResponseTypeDef,
    DescribeCollectionResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeProjectsResponseTypeDef,
    DescribeProjectVersionsResponseTypeDef,
    DescribeStreamProcessorResponseTypeDef,
    DetectCustomLabelsResponseTypeDef,
    DetectFacesResponseTypeDef,
    DetectLabelsResponseTypeDef,
    DetectLabelsSettingsTypeDef,
    DetectModerationLabelsResponseTypeDef,
    DetectProtectiveEquipmentResponseTypeDef,
    DetectTextFiltersTypeDef,
    DetectTextResponseTypeDef,
    DistributeDatasetTypeDef,
    GetCelebrityInfoResponseTypeDef,
    GetCelebrityRecognitionResponseTypeDef,
    GetContentModerationResponseTypeDef,
    GetFaceDetectionResponseTypeDef,
    GetFaceSearchResponseTypeDef,
    GetLabelDetectionResponseTypeDef,
    GetPersonTrackingResponseTypeDef,
    GetSegmentDetectionResponseTypeDef,
    GetTextDetectionResponseTypeDef,
    HumanLoopConfigTypeDef,
    ImageTypeDef,
    IndexFacesResponseTypeDef,
    ListCollectionsResponseTypeDef,
    ListDatasetEntriesResponseTypeDef,
    ListDatasetLabelsResponseTypeDef,
    ListFacesResponseTypeDef,
    ListProjectPoliciesResponseTypeDef,
    ListStreamProcessorsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    NotificationChannelTypeDef,
    OutputConfigTypeDef,
    ProtectiveEquipmentSummarizationAttributesTypeDef,
    PutProjectPolicyResponseTypeDef,
    RecognizeCelebritiesResponseTypeDef,
    RegionOfInterestTypeDef,
    SearchFacesByImageResponseTypeDef,
    SearchFacesResponseTypeDef,
    StartCelebrityRecognitionResponseTypeDef,
    StartContentModerationResponseTypeDef,
    StartFaceDetectionResponseTypeDef,
    StartFaceSearchResponseTypeDef,
    StartLabelDetectionResponseTypeDef,
    StartPersonTrackingResponseTypeDef,
    StartProjectVersionResponseTypeDef,
    StartSegmentDetectionFiltersTypeDef,
    StartSegmentDetectionResponseTypeDef,
    StartStreamProcessorResponseTypeDef,
    StartTextDetectionFiltersTypeDef,
    StartTextDetectionResponseTypeDef,
    StopProjectVersionResponseTypeDef,
    StreamProcessingStartSelectorTypeDef,
    StreamProcessingStopSelectorTypeDef,
    StreamProcessorDataSharingPreferenceTypeDef,
    StreamProcessorInputTypeDef,
    StreamProcessorNotificationChannelTypeDef,
    StreamProcessorOutputTypeDef,
    StreamProcessorSettingsForUpdateTypeDef,
    StreamProcessorSettingsTypeDef,
    TestingDataTypeDef,
    TrainingDataTypeDef,
    VideoTypeDef,
)
from .waiter import ProjectVersionRunningWaiter, ProjectVersionTrainingCompletedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("RekognitionClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    HumanLoopQuotaExceededException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    ImageTooLargeException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidImageFormatException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidPolicyRevisionIdException: Type[BotocoreClientError]
    InvalidS3ObjectException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    ProvisionedThroughputExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceNotReadyException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    VideoTooLargeException: Type[BotocoreClientError]

class RekognitionClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RekognitionClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#close)
        """
    def compare_faces(
        self,
        *,
        SourceImage: "ImageTypeDef",
        TargetImage: "ImageTypeDef",
        SimilarityThreshold: float = None,
        QualityFilter: QualityFilterType = None
    ) -> CompareFacesResponseTypeDef:
        """
        Compares a face in the *source* input image with each of the 100 largest faces
        detected in the *target* input image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.compare_faces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#compare_faces)
        """
    def copy_project_version(
        self,
        *,
        SourceProjectArn: str,
        SourceProjectVersionArn: str,
        DestinationProjectArn: str,
        VersionName: str,
        OutputConfig: "OutputConfigTypeDef",
        Tags: Dict[str, str] = None,
        KmsKeyId: str = None
    ) -> CopyProjectVersionResponseTypeDef:
        """
        Copies a version of an Amazon Rekognition Custom Labels model from a source
        project to a destination project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.copy_project_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#copy_project_version)
        """
    def create_collection(
        self, *, CollectionId: str, Tags: Dict[str, str] = None
    ) -> CreateCollectionResponseTypeDef:
        """
        Creates a collection in an AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.create_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#create_collection)
        """
    def create_dataset(
        self,
        *,
        DatasetType: DatasetTypeType,
        ProjectArn: str,
        DatasetSource: "DatasetSourceTypeDef" = None
    ) -> CreateDatasetResponseTypeDef:
        """
        Creates a new Amazon Rekognition Custom Labels dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.create_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#create_dataset)
        """
    def create_project(self, *, ProjectName: str) -> CreateProjectResponseTypeDef:
        """
        Creates a new Amazon Rekognition Custom Labels project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#create_project)
        """
    def create_project_version(
        self,
        *,
        ProjectArn: str,
        VersionName: str,
        OutputConfig: "OutputConfigTypeDef",
        TrainingData: "TrainingDataTypeDef" = None,
        TestingData: "TestingDataTypeDef" = None,
        Tags: Dict[str, str] = None,
        KmsKeyId: str = None
    ) -> CreateProjectVersionResponseTypeDef:
        """
        Creates a new version of a model and begins training.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.create_project_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#create_project_version)
        """
    def create_stream_processor(
        self,
        *,
        Input: "StreamProcessorInputTypeDef",
        Output: "StreamProcessorOutputTypeDef",
        Name: str,
        Settings: "StreamProcessorSettingsTypeDef",
        RoleArn: str,
        Tags: Dict[str, str] = None,
        NotificationChannel: "StreamProcessorNotificationChannelTypeDef" = None,
        KmsKeyId: str = None,
        RegionsOfInterest: List["RegionOfInterestTypeDef"] = None,
        DataSharingPreference: "StreamProcessorDataSharingPreferenceTypeDef" = None
    ) -> CreateStreamProcessorResponseTypeDef:
        """
        Creates an Amazon Rekognition stream processor that you can use to detect and
        recognize faces or to detect labels in a streaming video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.create_stream_processor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#create_stream_processor)
        """
    def delete_collection(self, *, CollectionId: str) -> DeleteCollectionResponseTypeDef:
        """
        Deletes the specified collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.delete_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#delete_collection)
        """
    def delete_dataset(self, *, DatasetArn: str) -> Dict[str, Any]:
        """
        Deletes an existing Amazon Rekognition Custom Labels dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.delete_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#delete_dataset)
        """
    def delete_faces(self, *, CollectionId: str, FaceIds: List[str]) -> DeleteFacesResponseTypeDef:
        """
        Deletes faces from a collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.delete_faces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#delete_faces)
        """
    def delete_project(self, *, ProjectArn: str) -> DeleteProjectResponseTypeDef:
        """
        Deletes an Amazon Rekognition Custom Labels project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.delete_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#delete_project)
        """
    def delete_project_policy(
        self, *, ProjectArn: str, PolicyName: str, PolicyRevisionId: str = None
    ) -> Dict[str, Any]:
        """
        Deletes an existing project policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.delete_project_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#delete_project_policy)
        """
    def delete_project_version(
        self, *, ProjectVersionArn: str
    ) -> DeleteProjectVersionResponseTypeDef:
        """
        Deletes an Amazon Rekognition Custom Labels model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.delete_project_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#delete_project_version)
        """
    def delete_stream_processor(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes the stream processor identified by `Name`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.delete_stream_processor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#delete_stream_processor)
        """
    def describe_collection(self, *, CollectionId: str) -> DescribeCollectionResponseTypeDef:
        """
        Describes the specified collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.describe_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#describe_collection)
        """
    def describe_dataset(self, *, DatasetArn: str) -> DescribeDatasetResponseTypeDef:
        """
        Describes an Amazon Rekognition Custom Labels dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.describe_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#describe_dataset)
        """
    def describe_project_versions(
        self,
        *,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeProjectVersionsResponseTypeDef:
        """
        Lists and describes the versions of a model in an Amazon Rekognition Custom
        Labels project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.describe_project_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#describe_project_versions)
        """
    def describe_projects(
        self, *, NextToken: str = None, MaxResults: int = None, ProjectNames: List[str] = None
    ) -> DescribeProjectsResponseTypeDef:
        """
        Gets information about your Amazon Rekognition Custom Labels projects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.describe_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#describe_projects)
        """
    def describe_stream_processor(self, *, Name: str) -> DescribeStreamProcessorResponseTypeDef:
        """
        Provides information about a stream processor created by  CreateStreamProcessor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.describe_stream_processor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#describe_stream_processor)
        """
    def detect_custom_labels(
        self,
        *,
        ProjectVersionArn: str,
        Image: "ImageTypeDef",
        MaxResults: int = None,
        MinConfidence: float = None
    ) -> DetectCustomLabelsResponseTypeDef:
        """
        Detects custom labels in a supplied image by using an Amazon Rekognition Custom
        Labels model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.detect_custom_labels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#detect_custom_labels)
        """
    def detect_faces(
        self, *, Image: "ImageTypeDef", Attributes: List[AttributeType] = None
    ) -> DetectFacesResponseTypeDef:
        """
        Detects faces within an image that is provided as input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.detect_faces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#detect_faces)
        """
    def detect_labels(
        self,
        *,
        Image: "ImageTypeDef",
        MaxLabels: int = None,
        MinConfidence: float = None,
        Features: List[DetectLabelsFeatureNameType] = None,
        Settings: "DetectLabelsSettingsTypeDef" = None
    ) -> DetectLabelsResponseTypeDef:
        """
        Detects instances of real-world entities within an image (JPEG or PNG) provided
        as input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.detect_labels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#detect_labels)
        """
    def detect_moderation_labels(
        self,
        *,
        Image: "ImageTypeDef",
        MinConfidence: float = None,
        HumanLoopConfig: "HumanLoopConfigTypeDef" = None
    ) -> DetectModerationLabelsResponseTypeDef:
        """
        Detects unsafe content in a specified JPEG or PNG format image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.detect_moderation_labels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#detect_moderation_labels)
        """
    def detect_protective_equipment(
        self,
        *,
        Image: "ImageTypeDef",
        SummarizationAttributes: "ProtectiveEquipmentSummarizationAttributesTypeDef" = None
    ) -> DetectProtectiveEquipmentResponseTypeDef:
        """
        Detects Personal Protective Equipment (PPE) worn by people detected in an image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.detect_protective_equipment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#detect_protective_equipment)
        """
    def detect_text(
        self, *, Image: "ImageTypeDef", Filters: "DetectTextFiltersTypeDef" = None
    ) -> DetectTextResponseTypeDef:
        """
        Detects text in the input image and converts it into machine-readable text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.detect_text)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#detect_text)
        """
    def distribute_dataset_entries(
        self, *, Datasets: List["DistributeDatasetTypeDef"]
    ) -> Dict[str, Any]:
        """
        Distributes the entries (images) in a training dataset across the training
        dataset and the test dataset for a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.distribute_dataset_entries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#distribute_dataset_entries)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#generate_presigned_url)
        """
    def get_celebrity_info(self, *, Id: str) -> GetCelebrityInfoResponseTypeDef:
        """
        Gets the name and additional information about a celebrity based on their Amazon
        Rekognition ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.get_celebrity_info)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_celebrity_info)
        """
    def get_celebrity_recognition(
        self,
        *,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: CelebrityRecognitionSortByType = None
    ) -> GetCelebrityRecognitionResponseTypeDef:
        """
        Gets the celebrity recognition results for a Amazon Rekognition Video analysis
        started by  StartCelebrityRecognition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.get_celebrity_recognition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_celebrity_recognition)
        """
    def get_content_moderation(
        self,
        *,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: ContentModerationSortByType = None
    ) -> GetContentModerationResponseTypeDef:
        """
        Gets the inappropriate, unwanted, or offensive content analysis results for a
        Amazon Rekognition Video analysis started by  StartContentModeration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.get_content_moderation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_content_moderation)
        """
    def get_face_detection(
        self, *, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetFaceDetectionResponseTypeDef:
        """
        Gets face detection results for a Amazon Rekognition Video analysis started by
        StartFaceDetection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.get_face_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_face_detection)
        """
    def get_face_search(
        self,
        *,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: FaceSearchSortByType = None
    ) -> GetFaceSearchResponseTypeDef:
        """
        Gets the face search results for Amazon Rekognition Video face search started by
        StartFaceSearch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.get_face_search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_face_search)
        """
    def get_label_detection(
        self,
        *,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: LabelDetectionSortByType = None
    ) -> GetLabelDetectionResponseTypeDef:
        """
        Gets the label detection results of a Amazon Rekognition Video analysis started
        by  StartLabelDetection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.get_label_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_label_detection)
        """
    def get_person_tracking(
        self,
        *,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: PersonTrackingSortByType = None
    ) -> GetPersonTrackingResponseTypeDef:
        """
        Gets the path tracking results of a Amazon Rekognition Video analysis started by
        StartPersonTracking.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.get_person_tracking)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_person_tracking)
        """
    def get_segment_detection(
        self, *, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetSegmentDetectionResponseTypeDef:
        """
        Gets the segment detection results of a Amazon Rekognition Video analysis
        started by  StartSegmentDetection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.get_segment_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_segment_detection)
        """
    def get_text_detection(
        self, *, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetTextDetectionResponseTypeDef:
        """
        Gets the text detection results of a Amazon Rekognition Video analysis started
        by  StartTextDetection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.get_text_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#get_text_detection)
        """
    def index_faces(
        self,
        *,
        CollectionId: str,
        Image: "ImageTypeDef",
        ExternalImageId: str = None,
        DetectionAttributes: List[AttributeType] = None,
        MaxFaces: int = None,
        QualityFilter: QualityFilterType = None
    ) -> IndexFacesResponseTypeDef:
        """
        Detects faces in the input image and adds them to the specified collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.index_faces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#index_faces)
        """
    def list_collections(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListCollectionsResponseTypeDef:
        """
        Returns list of collection IDs in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.list_collections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#list_collections)
        """
    def list_dataset_entries(
        self,
        *,
        DatasetArn: str,
        ContainsLabels: List[str] = None,
        Labeled: bool = None,
        SourceRefContains: str = None,
        HasErrors: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListDatasetEntriesResponseTypeDef:
        """
        Lists the entries (images) within a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.list_dataset_entries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#list_dataset_entries)
        """
    def list_dataset_labels(
        self, *, DatasetArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDatasetLabelsResponseTypeDef:
        """
        Lists the labels in a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.list_dataset_labels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#list_dataset_labels)
        """
    def list_faces(
        self, *, CollectionId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFacesResponseTypeDef:
        """
        Returns metadata for faces in the specified collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.list_faces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#list_faces)
        """
    def list_project_policies(
        self, *, ProjectArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListProjectPoliciesResponseTypeDef:
        """
        Gets a list of the project policies attached to a project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.list_project_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#list_project_policies)
        """
    def list_stream_processors(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListStreamProcessorsResponseTypeDef:
        """
        Gets a list of stream processors that you have created with
        CreateStreamProcessor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.list_stream_processors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#list_stream_processors)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags in an Amazon Rekognition collection, stream processor, or
        Custom Labels model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#list_tags_for_resource)
        """
    def put_project_policy(
        self, *, ProjectArn: str, PolicyName: str, PolicyDocument: str, PolicyRevisionId: str = None
    ) -> PutProjectPolicyResponseTypeDef:
        """
        Attaches a project policy to a Amazon Rekognition Custom Labels project in a
        trusting AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.put_project_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#put_project_policy)
        """
    def recognize_celebrities(
        self, *, Image: "ImageTypeDef"
    ) -> RecognizeCelebritiesResponseTypeDef:
        """
        Returns an array of celebrities recognized in the input image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.recognize_celebrities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#recognize_celebrities)
        """
    def search_faces(
        self,
        *,
        CollectionId: str,
        FaceId: str,
        MaxFaces: int = None,
        FaceMatchThreshold: float = None
    ) -> SearchFacesResponseTypeDef:
        """
        For a given input face ID, searches for matching faces in the collection the
        face belongs to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.search_faces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#search_faces)
        """
    def search_faces_by_image(
        self,
        *,
        CollectionId: str,
        Image: "ImageTypeDef",
        MaxFaces: int = None,
        FaceMatchThreshold: float = None,
        QualityFilter: QualityFilterType = None
    ) -> SearchFacesByImageResponseTypeDef:
        """
        For a given input image, first detects the largest face in the image, and then
        searches the specified collection for matching faces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.search_faces_by_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#search_faces_by_image)
        """
    def start_celebrity_recognition(
        self,
        *,
        Video: "VideoTypeDef",
        ClientRequestToken: str = None,
        NotificationChannel: "NotificationChannelTypeDef" = None,
        JobTag: str = None
    ) -> StartCelebrityRecognitionResponseTypeDef:
        """
        Starts asynchronous recognition of celebrities in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.start_celebrity_recognition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_celebrity_recognition)
        """
    def start_content_moderation(
        self,
        *,
        Video: "VideoTypeDef",
        MinConfidence: float = None,
        ClientRequestToken: str = None,
        NotificationChannel: "NotificationChannelTypeDef" = None,
        JobTag: str = None
    ) -> StartContentModerationResponseTypeDef:
        """
        Starts asynchronous detection of inappropriate, unwanted, or offensive content
        in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.start_content_moderation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_content_moderation)
        """
    def start_face_detection(
        self,
        *,
        Video: "VideoTypeDef",
        ClientRequestToken: str = None,
        NotificationChannel: "NotificationChannelTypeDef" = None,
        FaceAttributes: FaceAttributesType = None,
        JobTag: str = None
    ) -> StartFaceDetectionResponseTypeDef:
        """
        Starts asynchronous detection of faces in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.start_face_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_face_detection)
        """
    def start_face_search(
        self,
        *,
        Video: "VideoTypeDef",
        CollectionId: str,
        ClientRequestToken: str = None,
        FaceMatchThreshold: float = None,
        NotificationChannel: "NotificationChannelTypeDef" = None,
        JobTag: str = None
    ) -> StartFaceSearchResponseTypeDef:
        """
        Starts the asynchronous search for faces in a collection that match the faces of
        persons detected in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.start_face_search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_face_search)
        """
    def start_label_detection(
        self,
        *,
        Video: "VideoTypeDef",
        ClientRequestToken: str = None,
        MinConfidence: float = None,
        NotificationChannel: "NotificationChannelTypeDef" = None,
        JobTag: str = None
    ) -> StartLabelDetectionResponseTypeDef:
        """
        Starts asynchronous detection of labels in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.start_label_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_label_detection)
        """
    def start_person_tracking(
        self,
        *,
        Video: "VideoTypeDef",
        ClientRequestToken: str = None,
        NotificationChannel: "NotificationChannelTypeDef" = None,
        JobTag: str = None
    ) -> StartPersonTrackingResponseTypeDef:
        """
        Starts the asynchronous tracking of a person's path in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.start_person_tracking)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_person_tracking)
        """
    def start_project_version(
        self, *, ProjectVersionArn: str, MinInferenceUnits: int, MaxInferenceUnits: int = None
    ) -> StartProjectVersionResponseTypeDef:
        """
        Starts the running of the version of a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.start_project_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_project_version)
        """
    def start_segment_detection(
        self,
        *,
        Video: "VideoTypeDef",
        SegmentTypes: List[SegmentTypeType],
        ClientRequestToken: str = None,
        NotificationChannel: "NotificationChannelTypeDef" = None,
        JobTag: str = None,
        Filters: "StartSegmentDetectionFiltersTypeDef" = None
    ) -> StartSegmentDetectionResponseTypeDef:
        """
        Starts asynchronous detection of segment detection in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.start_segment_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_segment_detection)
        """
    def start_stream_processor(
        self,
        *,
        Name: str,
        StartSelector: "StreamProcessingStartSelectorTypeDef" = None,
        StopSelector: "StreamProcessingStopSelectorTypeDef" = None
    ) -> StartStreamProcessorResponseTypeDef:
        """
        Starts processing a stream processor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.start_stream_processor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_stream_processor)
        """
    def start_text_detection(
        self,
        *,
        Video: "VideoTypeDef",
        ClientRequestToken: str = None,
        NotificationChannel: "NotificationChannelTypeDef" = None,
        JobTag: str = None,
        Filters: "StartTextDetectionFiltersTypeDef" = None
    ) -> StartTextDetectionResponseTypeDef:
        """
        Starts asynchronous detection of text in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.start_text_detection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#start_text_detection)
        """
    def stop_project_version(self, *, ProjectVersionArn: str) -> StopProjectVersionResponseTypeDef:
        """
        Stops a running model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.stop_project_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#stop_project_version)
        """
    def stop_stream_processor(self, *, Name: str) -> Dict[str, Any]:
        """
        Stops a running stream processor that was created by  CreateStreamProcessor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.stop_stream_processor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#stop_stream_processor)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds one or more key-value tags to an Amazon Rekognition collection, stream
        processor, or Custom Labels model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from an Amazon Rekognition collection, stream
        processor, or Custom Labels model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#untag_resource)
        """
    def update_dataset_entries(
        self, *, DatasetArn: str, Changes: "DatasetChangesTypeDef"
    ) -> Dict[str, Any]:
        """
        Adds or updates one or more entries (images) in a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.update_dataset_entries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#update_dataset_entries)
        """
    def update_stream_processor(
        self,
        *,
        Name: str,
        SettingsForUpdate: "StreamProcessorSettingsForUpdateTypeDef" = None,
        RegionsOfInterestForUpdate: List["RegionOfInterestTypeDef"] = None,
        DataSharingPreferenceForUpdate: "StreamProcessorDataSharingPreferenceTypeDef" = None,
        ParametersToDelete: List[StreamProcessorParameterToDeleteType] = None
    ) -> Dict[str, Any]:
        """
        Allows you to update a stream processor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Client.update_stream_processor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client.html#update_stream_processor)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_project_versions"]
    ) -> DescribeProjectVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjectVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#describeprojectversionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_projects"]
    ) -> DescribeProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#describeprojectspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_collections"]
    ) -> ListCollectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Paginator.ListCollections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listcollectionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_entries"]
    ) -> ListDatasetEntriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Paginator.ListDatasetEntries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listdatasetentriespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_labels"]
    ) -> ListDatasetLabelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Paginator.ListDatasetLabels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listdatasetlabelspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_faces"]) -> ListFacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Paginator.ListFaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listfacespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_project_policies"]
    ) -> ListProjectPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Paginator.ListProjectPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#listprojectpoliciespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_stream_processors"]
    ) -> ListStreamProcessorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Paginator.ListStreamProcessors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/paginators.html#liststreamprocessorspaginator)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["project_version_running"]
    ) -> ProjectVersionRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionRunning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/waiters.html#projectversionrunningwaiter)
        """
    @overload
    def get_waiter(
        self, waiter_name: Literal["project_version_training_completed"]
    ) -> ProjectVersionTrainingCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionTrainingCompleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/waiters.html#projectversiontrainingcompletedwaiter)
        """
