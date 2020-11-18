# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for rekognition service client

Usage::

    ```python
    import boto3
    from mypy_boto3_rekognition import RekognitionClient

    client: RekognitionClient = boto3.client("rekognition")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_rekognition.paginator import (
    DescribeProjectsPaginator,
    DescribeProjectVersionsPaginator,
    ListCollectionsPaginator,
    ListFacesPaginator,
    ListStreamProcessorsPaginator,
)
from mypy_boto3_rekognition.type_defs import (
    CompareFacesResponseTypeDef,
    CreateCollectionResponseTypeDef,
    CreateProjectResponseTypeDef,
    CreateProjectVersionResponseTypeDef,
    CreateStreamProcessorResponseTypeDef,
    DeleteCollectionResponseTypeDef,
    DeleteFacesResponseTypeDef,
    DeleteProjectResponseTypeDef,
    DeleteProjectVersionResponseTypeDef,
    DescribeCollectionResponseTypeDef,
    DescribeProjectsResponseTypeDef,
    DescribeProjectVersionsResponseTypeDef,
    DescribeStreamProcessorResponseTypeDef,
    DetectCustomLabelsResponseTypeDef,
    DetectFacesResponseTypeDef,
    DetectLabelsResponseTypeDef,
    DetectModerationLabelsResponseTypeDef,
    DetectProtectiveEquipmentResponseTypeDef,
    DetectTextFiltersTypeDef,
    DetectTextResponseTypeDef,
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
    ListFacesResponseTypeDef,
    ListStreamProcessorsResponseTypeDef,
    NotificationChannelTypeDef,
    OutputConfigTypeDef,
    ProtectiveEquipmentSummarizationAttributesTypeDef,
    RecognizeCelebritiesResponseTypeDef,
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
    StartTextDetectionFiltersTypeDef,
    StartTextDetectionResponseTypeDef,
    StopProjectVersionResponseTypeDef,
    StreamProcessorInputTypeDef,
    StreamProcessorOutputTypeDef,
    StreamProcessorSettingsTypeDef,
    TestingDataTypeDef,
    TrainingDataTypeDef,
    VideoTypeDef,
)
from mypy_boto3_rekognition.waiter import (
    ProjectVersionRunningWaiter,
    ProjectVersionTrainingCompletedWaiter,
)

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
    InvalidS3ObjectException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ProvisionedThroughputExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceNotReadyException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    VideoTooLargeException: Type[BotocoreClientError]


class RekognitionClient:
    """
    [Rekognition.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.can_paginate)
        """

    def compare_faces(
        self,
        SourceImage: ImageTypeDef,
        TargetImage: ImageTypeDef,
        SimilarityThreshold: float = None,
        QualityFilter: Literal["NONE", "AUTO", "LOW", "MEDIUM", "HIGH"] = None,
    ) -> CompareFacesResponseTypeDef:
        """
        [Client.compare_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.compare_faces)
        """

    def create_collection(self, CollectionId: str) -> CreateCollectionResponseTypeDef:
        """
        [Client.create_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.create_collection)
        """

    def create_project(self, ProjectName: str) -> CreateProjectResponseTypeDef:
        """
        [Client.create_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.create_project)
        """

    def create_project_version(
        self,
        ProjectArn: str,
        VersionName: str,
        OutputConfig: "OutputConfigTypeDef",
        TrainingData: "TrainingDataTypeDef",
        TestingData: "TestingDataTypeDef",
    ) -> CreateProjectVersionResponseTypeDef:
        """
        [Client.create_project_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.create_project_version)
        """

    def create_stream_processor(
        self,
        Input: "StreamProcessorInputTypeDef",
        Output: "StreamProcessorOutputTypeDef",
        Name: str,
        Settings: "StreamProcessorSettingsTypeDef",
        RoleArn: str,
    ) -> CreateStreamProcessorResponseTypeDef:
        """
        [Client.create_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.create_stream_processor)
        """

    def delete_collection(self, CollectionId: str) -> DeleteCollectionResponseTypeDef:
        """
        [Client.delete_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.delete_collection)
        """

    def delete_faces(self, CollectionId: str, FaceIds: List[str]) -> DeleteFacesResponseTypeDef:
        """
        [Client.delete_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.delete_faces)
        """

    def delete_project(self, ProjectArn: str) -> DeleteProjectResponseTypeDef:
        """
        [Client.delete_project documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.delete_project)
        """

    def delete_project_version(self, ProjectVersionArn: str) -> DeleteProjectVersionResponseTypeDef:
        """
        [Client.delete_project_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.delete_project_version)
        """

    def delete_stream_processor(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.delete_stream_processor)
        """

    def describe_collection(self, CollectionId: str) -> DescribeCollectionResponseTypeDef:
        """
        [Client.describe_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.describe_collection)
        """

    def describe_project_versions(
        self,
        ProjectArn: str,
        VersionNames: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeProjectVersionsResponseTypeDef:
        """
        [Client.describe_project_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.describe_project_versions)
        """

    def describe_projects(
        self, NextToken: str = None, MaxResults: int = None
    ) -> DescribeProjectsResponseTypeDef:
        """
        [Client.describe_projects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.describe_projects)
        """

    def describe_stream_processor(self, Name: str) -> DescribeStreamProcessorResponseTypeDef:
        """
        [Client.describe_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.describe_stream_processor)
        """

    def detect_custom_labels(
        self,
        ProjectVersionArn: str,
        Image: ImageTypeDef,
        MaxResults: int = None,
        MinConfidence: float = None,
    ) -> DetectCustomLabelsResponseTypeDef:
        """
        [Client.detect_custom_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.detect_custom_labels)
        """

    def detect_faces(
        self, Image: ImageTypeDef, Attributes: List[Literal["DEFAULT", "ALL"]] = None
    ) -> DetectFacesResponseTypeDef:
        """
        [Client.detect_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.detect_faces)
        """

    def detect_labels(
        self, Image: ImageTypeDef, MaxLabels: int = None, MinConfidence: float = None
    ) -> DetectLabelsResponseTypeDef:
        """
        [Client.detect_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.detect_labels)
        """

    def detect_moderation_labels(
        self,
        Image: ImageTypeDef,
        MinConfidence: float = None,
        HumanLoopConfig: HumanLoopConfigTypeDef = None,
    ) -> DetectModerationLabelsResponseTypeDef:
        """
        [Client.detect_moderation_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.detect_moderation_labels)
        """

    def detect_protective_equipment(
        self,
        Image: ImageTypeDef,
        SummarizationAttributes: ProtectiveEquipmentSummarizationAttributesTypeDef = None,
    ) -> DetectProtectiveEquipmentResponseTypeDef:
        """
        [Client.detect_protective_equipment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.detect_protective_equipment)
        """

    def detect_text(
        self, Image: ImageTypeDef, Filters: DetectTextFiltersTypeDef = None
    ) -> DetectTextResponseTypeDef:
        """
        [Client.detect_text documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.detect_text)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.generate_presigned_url)
        """

    def get_celebrity_info(self, Id: str) -> GetCelebrityInfoResponseTypeDef:
        """
        [Client.get_celebrity_info documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.get_celebrity_info)
        """

    def get_celebrity_recognition(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["ID", "TIMESTAMP"] = None,
    ) -> GetCelebrityRecognitionResponseTypeDef:
        """
        [Client.get_celebrity_recognition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.get_celebrity_recognition)
        """

    def get_content_moderation(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["NAME", "TIMESTAMP"] = None,
    ) -> GetContentModerationResponseTypeDef:
        """
        [Client.get_content_moderation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.get_content_moderation)
        """

    def get_face_detection(
        self, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetFaceDetectionResponseTypeDef:
        """
        [Client.get_face_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.get_face_detection)
        """

    def get_face_search(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["INDEX", "TIMESTAMP"] = None,
    ) -> GetFaceSearchResponseTypeDef:
        """
        [Client.get_face_search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.get_face_search)
        """

    def get_label_detection(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["NAME", "TIMESTAMP"] = None,
    ) -> GetLabelDetectionResponseTypeDef:
        """
        [Client.get_label_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.get_label_detection)
        """

    def get_person_tracking(
        self,
        JobId: str,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: Literal["INDEX", "TIMESTAMP"] = None,
    ) -> GetPersonTrackingResponseTypeDef:
        """
        [Client.get_person_tracking documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.get_person_tracking)
        """

    def get_segment_detection(
        self, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetSegmentDetectionResponseTypeDef:
        """
        [Client.get_segment_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.get_segment_detection)
        """

    def get_text_detection(
        self, JobId: str, MaxResults: int = None, NextToken: str = None
    ) -> GetTextDetectionResponseTypeDef:
        """
        [Client.get_text_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.get_text_detection)
        """

    def index_faces(
        self,
        CollectionId: str,
        Image: ImageTypeDef,
        ExternalImageId: str = None,
        DetectionAttributes: List[Literal["DEFAULT", "ALL"]] = None,
        MaxFaces: int = None,
        QualityFilter: Literal["NONE", "AUTO", "LOW", "MEDIUM", "HIGH"] = None,
    ) -> IndexFacesResponseTypeDef:
        """
        [Client.index_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.index_faces)
        """

    def list_collections(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListCollectionsResponseTypeDef:
        """
        [Client.list_collections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.list_collections)
        """

    def list_faces(
        self, CollectionId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFacesResponseTypeDef:
        """
        [Client.list_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.list_faces)
        """

    def list_stream_processors(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListStreamProcessorsResponseTypeDef:
        """
        [Client.list_stream_processors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.list_stream_processors)
        """

    def recognize_celebrities(self, Image: ImageTypeDef) -> RecognizeCelebritiesResponseTypeDef:
        """
        [Client.recognize_celebrities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.recognize_celebrities)
        """

    def search_faces(
        self, CollectionId: str, FaceId: str, MaxFaces: int = None, FaceMatchThreshold: float = None
    ) -> SearchFacesResponseTypeDef:
        """
        [Client.search_faces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.search_faces)
        """

    def search_faces_by_image(
        self,
        CollectionId: str,
        Image: ImageTypeDef,
        MaxFaces: int = None,
        FaceMatchThreshold: float = None,
        QualityFilter: Literal["NONE", "AUTO", "LOW", "MEDIUM", "HIGH"] = None,
    ) -> SearchFacesByImageResponseTypeDef:
        """
        [Client.search_faces_by_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.search_faces_by_image)
        """

    def start_celebrity_recognition(
        self,
        Video: VideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> StartCelebrityRecognitionResponseTypeDef:
        """
        [Client.start_celebrity_recognition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.start_celebrity_recognition)
        """

    def start_content_moderation(
        self,
        Video: VideoTypeDef,
        MinConfidence: float = None,
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> StartContentModerationResponseTypeDef:
        """
        [Client.start_content_moderation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.start_content_moderation)
        """

    def start_face_detection(
        self,
        Video: VideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        FaceAttributes: Literal["DEFAULT", "ALL"] = None,
        JobTag: str = None,
    ) -> StartFaceDetectionResponseTypeDef:
        """
        [Client.start_face_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.start_face_detection)
        """

    def start_face_search(
        self,
        Video: VideoTypeDef,
        CollectionId: str,
        ClientRequestToken: str = None,
        FaceMatchThreshold: float = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> StartFaceSearchResponseTypeDef:
        """
        [Client.start_face_search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.start_face_search)
        """

    def start_label_detection(
        self,
        Video: VideoTypeDef,
        ClientRequestToken: str = None,
        MinConfidence: float = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> StartLabelDetectionResponseTypeDef:
        """
        [Client.start_label_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.start_label_detection)
        """

    def start_person_tracking(
        self,
        Video: VideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None,
    ) -> StartPersonTrackingResponseTypeDef:
        """
        [Client.start_person_tracking documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.start_person_tracking)
        """

    def start_project_version(
        self, ProjectVersionArn: str, MinInferenceUnits: int
    ) -> StartProjectVersionResponseTypeDef:
        """
        [Client.start_project_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.start_project_version)
        """

    def start_segment_detection(
        self,
        Video: VideoTypeDef,
        SegmentTypes: List[Literal["TECHNICAL_CUE", "SHOT"]],
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None,
        Filters: StartSegmentDetectionFiltersTypeDef = None,
    ) -> StartSegmentDetectionResponseTypeDef:
        """
        [Client.start_segment_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.start_segment_detection)
        """

    def start_stream_processor(self, Name: str) -> Dict[str, Any]:
        """
        [Client.start_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.start_stream_processor)
        """

    def start_text_detection(
        self,
        Video: VideoTypeDef,
        ClientRequestToken: str = None,
        NotificationChannel: NotificationChannelTypeDef = None,
        JobTag: str = None,
        Filters: StartTextDetectionFiltersTypeDef = None,
    ) -> StartTextDetectionResponseTypeDef:
        """
        [Client.start_text_detection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.start_text_detection)
        """

    def stop_project_version(self, ProjectVersionArn: str) -> StopProjectVersionResponseTypeDef:
        """
        [Client.stop_project_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.stop_project_version)
        """

    def stop_stream_processor(self, Name: str) -> Dict[str, Any]:
        """
        [Client.stop_stream_processor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Client.stop_stream_processor)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_project_versions"]
    ) -> DescribeProjectVersionsPaginator:
        """
        [Paginator.DescribeProjectVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjectVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_projects"]
    ) -> DescribeProjectsPaginator:
        """
        [Paginator.DescribeProjects documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Paginator.DescribeProjects)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_collections"]
    ) -> ListCollectionsPaginator:
        """
        [Paginator.ListCollections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Paginator.ListCollections)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_faces"]) -> ListFacesPaginator:
        """
        [Paginator.ListFaces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Paginator.ListFaces)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_stream_processors"]
    ) -> ListStreamProcessorsPaginator:
        """
        [Paginator.ListStreamProcessors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Paginator.ListStreamProcessors)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["project_version_running"]
    ) -> ProjectVersionRunningWaiter:
        """
        [Waiter.ProjectVersionRunning documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionRunning)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["project_version_training_completed"]
    ) -> ProjectVersionTrainingCompletedWaiter:
        """
        [Waiter.ProjectVersionTrainingCompleted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/rekognition.html#Rekognition.Waiter.ProjectVersionTrainingCompleted)
        """
