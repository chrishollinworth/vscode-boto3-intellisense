"""
Type annotations for rekognition service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_rekognition.client import RekognitionClient

    session = Session()
    client: RekognitionClient = session.client("rekognition")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeProjectsPaginator,
    DescribeProjectVersionsPaginator,
    ListCollectionsPaginator,
    ListDatasetEntriesPaginator,
    ListDatasetLabelsPaginator,
    ListFacesPaginator,
    ListProjectPoliciesPaginator,
    ListStreamProcessorsPaginator,
    ListUsersPaginator,
)
from .type_defs import (
    AssociateFacesRequestTypeDef,
    AssociateFacesResponseTypeDef,
    CompareFacesRequestTypeDef,
    CompareFacesResponseTypeDef,
    CopyProjectVersionRequestTypeDef,
    CopyProjectVersionResponseTypeDef,
    CreateCollectionRequestTypeDef,
    CreateCollectionResponseTypeDef,
    CreateDatasetRequestTypeDef,
    CreateDatasetResponseTypeDef,
    CreateFaceLivenessSessionRequestTypeDef,
    CreateFaceLivenessSessionResponseTypeDef,
    CreateProjectRequestTypeDef,
    CreateProjectResponseTypeDef,
    CreateProjectVersionRequestTypeDef,
    CreateProjectVersionResponseTypeDef,
    CreateStreamProcessorRequestTypeDef,
    CreateStreamProcessorResponseTypeDef,
    CreateUserRequestTypeDef,
    DeleteCollectionRequestTypeDef,
    DeleteCollectionResponseTypeDef,
    DeleteDatasetRequestTypeDef,
    DeleteFacesRequestTypeDef,
    DeleteFacesResponseTypeDef,
    DeleteProjectPolicyRequestTypeDef,
    DeleteProjectRequestTypeDef,
    DeleteProjectResponseTypeDef,
    DeleteProjectVersionRequestTypeDef,
    DeleteProjectVersionResponseTypeDef,
    DeleteStreamProcessorRequestTypeDef,
    DeleteUserRequestTypeDef,
    DescribeCollectionRequestTypeDef,
    DescribeCollectionResponseTypeDef,
    DescribeDatasetRequestTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeProjectsRequestTypeDef,
    DescribeProjectsResponseTypeDef,
    DescribeProjectVersionsRequestTypeDef,
    DescribeProjectVersionsResponseTypeDef,
    DescribeStreamProcessorRequestTypeDef,
    DescribeStreamProcessorResponseTypeDef,
    DetectCustomLabelsRequestTypeDef,
    DetectCustomLabelsResponseTypeDef,
    DetectFacesRequestTypeDef,
    DetectFacesResponseTypeDef,
    DetectLabelsRequestTypeDef,
    DetectLabelsResponseTypeDef,
    DetectModerationLabelsRequestTypeDef,
    DetectModerationLabelsResponseTypeDef,
    DetectProtectiveEquipmentRequestTypeDef,
    DetectProtectiveEquipmentResponseTypeDef,
    DetectTextRequestTypeDef,
    DetectTextResponseTypeDef,
    DisassociateFacesRequestTypeDef,
    DisassociateFacesResponseTypeDef,
    DistributeDatasetEntriesRequestTypeDef,
    GetCelebrityInfoRequestTypeDef,
    GetCelebrityInfoResponseTypeDef,
    GetCelebrityRecognitionRequestTypeDef,
    GetCelebrityRecognitionResponseTypeDef,
    GetContentModerationRequestTypeDef,
    GetContentModerationResponseTypeDef,
    GetFaceDetectionRequestTypeDef,
    GetFaceDetectionResponseTypeDef,
    GetFaceLivenessSessionResultsRequestTypeDef,
    GetFaceLivenessSessionResultsResponseTypeDef,
    GetFaceSearchRequestTypeDef,
    GetFaceSearchResponseTypeDef,
    GetLabelDetectionRequestTypeDef,
    GetLabelDetectionResponseTypeDef,
    GetMediaAnalysisJobRequestTypeDef,
    GetMediaAnalysisJobResponseTypeDef,
    GetPersonTrackingRequestTypeDef,
    GetPersonTrackingResponseTypeDef,
    GetSegmentDetectionRequestTypeDef,
    GetSegmentDetectionResponseTypeDef,
    GetTextDetectionRequestTypeDef,
    GetTextDetectionResponseTypeDef,
    IndexFacesRequestTypeDef,
    IndexFacesResponseTypeDef,
    ListCollectionsRequestTypeDef,
    ListCollectionsResponseTypeDef,
    ListDatasetEntriesRequestTypeDef,
    ListDatasetEntriesResponseTypeDef,
    ListDatasetLabelsRequestTypeDef,
    ListDatasetLabelsResponseTypeDef,
    ListFacesRequestTypeDef,
    ListFacesResponseTypeDef,
    ListMediaAnalysisJobsRequestTypeDef,
    ListMediaAnalysisJobsResponseTypeDef,
    ListProjectPoliciesRequestTypeDef,
    ListProjectPoliciesResponseTypeDef,
    ListStreamProcessorsRequestTypeDef,
    ListStreamProcessorsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsersRequestTypeDef,
    ListUsersResponseTypeDef,
    PutProjectPolicyRequestTypeDef,
    PutProjectPolicyResponseTypeDef,
    RecognizeCelebritiesRequestTypeDef,
    RecognizeCelebritiesResponseTypeDef,
    SearchFacesByImageRequestTypeDef,
    SearchFacesByImageResponseTypeDef,
    SearchFacesRequestTypeDef,
    SearchFacesResponseTypeDef,
    SearchUsersByImageRequestTypeDef,
    SearchUsersByImageResponseTypeDef,
    SearchUsersRequestTypeDef,
    SearchUsersResponseTypeDef,
    StartCelebrityRecognitionRequestTypeDef,
    StartCelebrityRecognitionResponseTypeDef,
    StartContentModerationRequestTypeDef,
    StartContentModerationResponseTypeDef,
    StartFaceDetectionRequestTypeDef,
    StartFaceDetectionResponseTypeDef,
    StartFaceSearchRequestTypeDef,
    StartFaceSearchResponseTypeDef,
    StartLabelDetectionRequestTypeDef,
    StartLabelDetectionResponseTypeDef,
    StartMediaAnalysisJobRequestTypeDef,
    StartMediaAnalysisJobResponseTypeDef,
    StartPersonTrackingRequestTypeDef,
    StartPersonTrackingResponseTypeDef,
    StartProjectVersionRequestTypeDef,
    StartProjectVersionResponseTypeDef,
    StartSegmentDetectionRequestTypeDef,
    StartSegmentDetectionResponseTypeDef,
    StartStreamProcessorRequestTypeDef,
    StartStreamProcessorResponseTypeDef,
    StartTextDetectionRequestTypeDef,
    StartTextDetectionResponseTypeDef,
    StopProjectVersionRequestTypeDef,
    StopProjectVersionResponseTypeDef,
    StopStreamProcessorRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateDatasetEntriesRequestTypeDef,
    UpdateStreamProcessorRequestTypeDef,
)
from .waiter import ProjectVersionRunningWaiter, ProjectVersionTrainingCompletedWaiter

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("RekognitionClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    HumanLoopQuotaExceededException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    ImageTooLargeException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidImageFormatException: Type[BotocoreClientError]
    InvalidManifestException: Type[BotocoreClientError]
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
    SessionNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    VideoTooLargeException: Type[BotocoreClientError]

class RekognitionClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RekognitionClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#generate_presigned_url)
        """

    def associate_faces(
        self, **kwargs: Unpack[AssociateFacesRequestTypeDef]
    ) -> AssociateFacesResponseTypeDef:
        """
        Associates one or more faces with an existing UserID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/associate_faces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#associate_faces)
        """

    def compare_faces(
        self, **kwargs: Unpack[CompareFacesRequestTypeDef]
    ) -> CompareFacesResponseTypeDef:
        """
        Compares a face in the <i>source</i> input image with each of the 100 largest
        faces detected in the <i>target</i> input image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/compare_faces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#compare_faces)
        """

    def copy_project_version(
        self, **kwargs: Unpack[CopyProjectVersionRequestTypeDef]
    ) -> CopyProjectVersionResponseTypeDef:
        """
        This operation applies only to Amazon Rekognition Custom Labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/copy_project_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#copy_project_version)
        """

    def create_collection(
        self, **kwargs: Unpack[CreateCollectionRequestTypeDef]
    ) -> CreateCollectionResponseTypeDef:
        """
        Creates a collection in an AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/create_collection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#create_collection)
        """

    def create_dataset(
        self, **kwargs: Unpack[CreateDatasetRequestTypeDef]
    ) -> CreateDatasetResponseTypeDef:
        """
        This operation applies only to Amazon Rekognition Custom Labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/create_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#create_dataset)
        """

    def create_face_liveness_session(
        self, **kwargs: Unpack[CreateFaceLivenessSessionRequestTypeDef]
    ) -> CreateFaceLivenessSessionResponseTypeDef:
        """
        This API operation initiates a Face Liveness session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/create_face_liveness_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#create_face_liveness_session)
        """

    def create_project(
        self, **kwargs: Unpack[CreateProjectRequestTypeDef]
    ) -> CreateProjectResponseTypeDef:
        """
        Creates a new Amazon Rekognition project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/create_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#create_project)
        """

    def create_project_version(
        self, **kwargs: Unpack[CreateProjectVersionRequestTypeDef]
    ) -> CreateProjectVersionResponseTypeDef:
        """
        Creates a new version of Amazon Rekognition project (like a Custom Labels model
        or a custom adapter) and begins training.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/create_project_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#create_project_version)
        """

    def create_stream_processor(
        self, **kwargs: Unpack[CreateStreamProcessorRequestTypeDef]
    ) -> CreateStreamProcessorResponseTypeDef:
        """
        Creates an Amazon Rekognition stream processor that you can use to detect and
        recognize faces or to detect labels in a streaming video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/create_stream_processor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#create_stream_processor)
        """

    def create_user(self, **kwargs: Unpack[CreateUserRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a new User within a collection specified by <code>CollectionId</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/create_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#create_user)
        """

    def delete_collection(
        self, **kwargs: Unpack[DeleteCollectionRequestTypeDef]
    ) -> DeleteCollectionResponseTypeDef:
        """
        Deletes the specified collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/delete_collection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#delete_collection)
        """

    def delete_dataset(self, **kwargs: Unpack[DeleteDatasetRequestTypeDef]) -> Dict[str, Any]:
        """
        This operation applies only to Amazon Rekognition Custom Labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/delete_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#delete_dataset)
        """

    def delete_faces(
        self, **kwargs: Unpack[DeleteFacesRequestTypeDef]
    ) -> DeleteFacesResponseTypeDef:
        """
        Deletes faces from a collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/delete_faces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#delete_faces)
        """

    def delete_project(
        self, **kwargs: Unpack[DeleteProjectRequestTypeDef]
    ) -> DeleteProjectResponseTypeDef:
        """
        Deletes a Amazon Rekognition project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/delete_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#delete_project)
        """

    def delete_project_policy(
        self, **kwargs: Unpack[DeleteProjectPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This operation applies only to Amazon Rekognition Custom Labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/delete_project_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#delete_project_policy)
        """

    def delete_project_version(
        self, **kwargs: Unpack[DeleteProjectVersionRequestTypeDef]
    ) -> DeleteProjectVersionResponseTypeDef:
        """
        Deletes a Rekognition project model or project version, like a Amazon
        Rekognition Custom Labels model or a custom adapter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/delete_project_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#delete_project_version)
        """

    def delete_stream_processor(
        self, **kwargs: Unpack[DeleteStreamProcessorRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the stream processor identified by <code>Name</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/delete_stream_processor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#delete_stream_processor)
        """

    def delete_user(self, **kwargs: Unpack[DeleteUserRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified UserID within the collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/delete_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#delete_user)
        """

    def describe_collection(
        self, **kwargs: Unpack[DescribeCollectionRequestTypeDef]
    ) -> DescribeCollectionResponseTypeDef:
        """
        Describes the specified collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/describe_collection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#describe_collection)
        """

    def describe_dataset(
        self, **kwargs: Unpack[DescribeDatasetRequestTypeDef]
    ) -> DescribeDatasetResponseTypeDef:
        """
        This operation applies only to Amazon Rekognition Custom Labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/describe_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#describe_dataset)
        """

    def describe_project_versions(
        self, **kwargs: Unpack[DescribeProjectVersionsRequestTypeDef]
    ) -> DescribeProjectVersionsResponseTypeDef:
        """
        Lists and describes the versions of an Amazon Rekognition project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/describe_project_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#describe_project_versions)
        """

    def describe_projects(
        self, **kwargs: Unpack[DescribeProjectsRequestTypeDef]
    ) -> DescribeProjectsResponseTypeDef:
        """
        Gets information about your Rekognition projects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/describe_projects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#describe_projects)
        """

    def describe_stream_processor(
        self, **kwargs: Unpack[DescribeStreamProcessorRequestTypeDef]
    ) -> DescribeStreamProcessorResponseTypeDef:
        """
        Provides information about a stream processor created by
        <a>CreateStreamProcessor</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/describe_stream_processor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#describe_stream_processor)
        """

    def detect_custom_labels(
        self, **kwargs: Unpack[DetectCustomLabelsRequestTypeDef]
    ) -> DetectCustomLabelsResponseTypeDef:
        """
        This operation applies only to Amazon Rekognition Custom Labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/detect_custom_labels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#detect_custom_labels)
        """

    def detect_faces(
        self, **kwargs: Unpack[DetectFacesRequestTypeDef]
    ) -> DetectFacesResponseTypeDef:
        """
        Detects faces within an image that is provided as input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/detect_faces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#detect_faces)
        """

    def detect_labels(
        self, **kwargs: Unpack[DetectLabelsRequestTypeDef]
    ) -> DetectLabelsResponseTypeDef:
        """
        Detects instances of real-world entities within an image (JPEG or PNG) provided
        as input.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/detect_labels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#detect_labels)
        """

    def detect_moderation_labels(
        self, **kwargs: Unpack[DetectModerationLabelsRequestTypeDef]
    ) -> DetectModerationLabelsResponseTypeDef:
        """
        Detects unsafe content in a specified JPEG or PNG format image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/detect_moderation_labels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#detect_moderation_labels)
        """

    def detect_protective_equipment(
        self, **kwargs: Unpack[DetectProtectiveEquipmentRequestTypeDef]
    ) -> DetectProtectiveEquipmentResponseTypeDef:
        """
        Detects Personal Protective Equipment (PPE) worn by people detected in an image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/detect_protective_equipment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#detect_protective_equipment)
        """

    def detect_text(self, **kwargs: Unpack[DetectTextRequestTypeDef]) -> DetectTextResponseTypeDef:
        """
        Detects text in the input image and converts it into machine-readable text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/detect_text.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#detect_text)
        """

    def disassociate_faces(
        self, **kwargs: Unpack[DisassociateFacesRequestTypeDef]
    ) -> DisassociateFacesResponseTypeDef:
        """
        Removes the association between a <code>Face</code> supplied in an array of
        <code>FaceIds</code> and the User.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/disassociate_faces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#disassociate_faces)
        """

    def distribute_dataset_entries(
        self, **kwargs: Unpack[DistributeDatasetEntriesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This operation applies only to Amazon Rekognition Custom Labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/distribute_dataset_entries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#distribute_dataset_entries)
        """

    def get_celebrity_info(
        self, **kwargs: Unpack[GetCelebrityInfoRequestTypeDef]
    ) -> GetCelebrityInfoResponseTypeDef:
        """
        Gets the name and additional information about a celebrity based on their
        Amazon Rekognition ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_celebrity_info.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_celebrity_info)
        """

    def get_celebrity_recognition(
        self, **kwargs: Unpack[GetCelebrityRecognitionRequestTypeDef]
    ) -> GetCelebrityRecognitionResponseTypeDef:
        """
        Gets the celebrity recognition results for a Amazon Rekognition Video analysis
        started by <a>StartCelebrityRecognition</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_celebrity_recognition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_celebrity_recognition)
        """

    def get_content_moderation(
        self, **kwargs: Unpack[GetContentModerationRequestTypeDef]
    ) -> GetContentModerationResponseTypeDef:
        """
        Gets the inappropriate, unwanted, or offensive content analysis results for a
        Amazon Rekognition Video analysis started by <a>StartContentModeration</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_content_moderation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_content_moderation)
        """

    def get_face_detection(
        self, **kwargs: Unpack[GetFaceDetectionRequestTypeDef]
    ) -> GetFaceDetectionResponseTypeDef:
        """
        Gets face detection results for a Amazon Rekognition Video analysis started by
        <a>StartFaceDetection</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_face_detection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_face_detection)
        """

    def get_face_liveness_session_results(
        self, **kwargs: Unpack[GetFaceLivenessSessionResultsRequestTypeDef]
    ) -> GetFaceLivenessSessionResultsResponseTypeDef:
        """
        Retrieves the results of a specific Face Liveness session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_face_liveness_session_results.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_face_liveness_session_results)
        """

    def get_face_search(
        self, **kwargs: Unpack[GetFaceSearchRequestTypeDef]
    ) -> GetFaceSearchResponseTypeDef:
        """
        Gets the face search results for Amazon Rekognition Video face search started
        by <a>StartFaceSearch</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_face_search.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_face_search)
        """

    def get_label_detection(
        self, **kwargs: Unpack[GetLabelDetectionRequestTypeDef]
    ) -> GetLabelDetectionResponseTypeDef:
        """
        Gets the label detection results of a Amazon Rekognition Video analysis started
        by <a>StartLabelDetection</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_label_detection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_label_detection)
        """

    def get_media_analysis_job(
        self, **kwargs: Unpack[GetMediaAnalysisJobRequestTypeDef]
    ) -> GetMediaAnalysisJobResponseTypeDef:
        """
        Retrieves the results for a given media analysis job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_media_analysis_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_media_analysis_job)
        """

    def get_person_tracking(
        self, **kwargs: Unpack[GetPersonTrackingRequestTypeDef]
    ) -> GetPersonTrackingResponseTypeDef:
        """
        Gets the path tracking results of a Amazon Rekognition Video analysis started
        by <a>StartPersonTracking</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_person_tracking.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_person_tracking)
        """

    def get_segment_detection(
        self, **kwargs: Unpack[GetSegmentDetectionRequestTypeDef]
    ) -> GetSegmentDetectionResponseTypeDef:
        """
        Gets the segment detection results of a Amazon Rekognition Video analysis
        started by <a>StartSegmentDetection</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_segment_detection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_segment_detection)
        """

    def get_text_detection(
        self, **kwargs: Unpack[GetTextDetectionRequestTypeDef]
    ) -> GetTextDetectionResponseTypeDef:
        """
        Gets the text detection results of a Amazon Rekognition Video analysis started
        by <a>StartTextDetection</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_text_detection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_text_detection)
        """

    def index_faces(self, **kwargs: Unpack[IndexFacesRequestTypeDef]) -> IndexFacesResponseTypeDef:
        """
        Detects faces in the input image and adds them to the specified collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/index_faces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#index_faces)
        """

    def list_collections(
        self, **kwargs: Unpack[ListCollectionsRequestTypeDef]
    ) -> ListCollectionsResponseTypeDef:
        """
        Returns list of collection IDs in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/list_collections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#list_collections)
        """

    def list_dataset_entries(
        self, **kwargs: Unpack[ListDatasetEntriesRequestTypeDef]
    ) -> ListDatasetEntriesResponseTypeDef:
        """
        This operation applies only to Amazon Rekognition Custom Labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/list_dataset_entries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#list_dataset_entries)
        """

    def list_dataset_labels(
        self, **kwargs: Unpack[ListDatasetLabelsRequestTypeDef]
    ) -> ListDatasetLabelsResponseTypeDef:
        """
        This operation applies only to Amazon Rekognition Custom Labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/list_dataset_labels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#list_dataset_labels)
        """

    def list_faces(self, **kwargs: Unpack[ListFacesRequestTypeDef]) -> ListFacesResponseTypeDef:
        """
        Returns metadata for faces in the specified collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/list_faces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#list_faces)
        """

    def list_media_analysis_jobs(
        self, **kwargs: Unpack[ListMediaAnalysisJobsRequestTypeDef]
    ) -> ListMediaAnalysisJobsResponseTypeDef:
        """
        Returns a list of media analysis jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/list_media_analysis_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#list_media_analysis_jobs)
        """

    def list_project_policies(
        self, **kwargs: Unpack[ListProjectPoliciesRequestTypeDef]
    ) -> ListProjectPoliciesResponseTypeDef:
        """
        This operation applies only to Amazon Rekognition Custom Labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/list_project_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#list_project_policies)
        """

    def list_stream_processors(
        self, **kwargs: Unpack[ListStreamProcessorsRequestTypeDef]
    ) -> ListStreamProcessorsResponseTypeDef:
        """
        Gets a list of stream processors that you have created with
        <a>CreateStreamProcessor</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/list_stream_processors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#list_stream_processors)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags in an Amazon Rekognition collection, stream processor,
        or Custom Labels model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#list_tags_for_resource)
        """

    def list_users(self, **kwargs: Unpack[ListUsersRequestTypeDef]) -> ListUsersResponseTypeDef:
        """
        Returns metadata of the User such as <code>UserID</code> in the specified
        collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/list_users.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#list_users)
        """

    def put_project_policy(
        self, **kwargs: Unpack[PutProjectPolicyRequestTypeDef]
    ) -> PutProjectPolicyResponseTypeDef:
        """
        This operation applies only to Amazon Rekognition Custom Labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/put_project_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#put_project_policy)
        """

    def recognize_celebrities(
        self, **kwargs: Unpack[RecognizeCelebritiesRequestTypeDef]
    ) -> RecognizeCelebritiesResponseTypeDef:
        """
        Returns an array of celebrities recognized in the input image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/recognize_celebrities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#recognize_celebrities)
        """

    def search_faces(
        self, **kwargs: Unpack[SearchFacesRequestTypeDef]
    ) -> SearchFacesResponseTypeDef:
        """
        For a given input face ID, searches for matching faces in the collection the
        face belongs to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/search_faces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#search_faces)
        """

    def search_faces_by_image(
        self, **kwargs: Unpack[SearchFacesByImageRequestTypeDef]
    ) -> SearchFacesByImageResponseTypeDef:
        """
        For a given input image, first detects the largest face in the image, and then
        searches the specified collection for matching faces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/search_faces_by_image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#search_faces_by_image)
        """

    def search_users(
        self, **kwargs: Unpack[SearchUsersRequestTypeDef]
    ) -> SearchUsersResponseTypeDef:
        """
        Searches for UserIDs within a collection based on a <code>FaceId</code> or
        <code>UserId</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/search_users.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#search_users)
        """

    def search_users_by_image(
        self, **kwargs: Unpack[SearchUsersByImageRequestTypeDef]
    ) -> SearchUsersByImageResponseTypeDef:
        """
        Searches for UserIDs using a supplied image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/search_users_by_image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#search_users_by_image)
        """

    def start_celebrity_recognition(
        self, **kwargs: Unpack[StartCelebrityRecognitionRequestTypeDef]
    ) -> StartCelebrityRecognitionResponseTypeDef:
        """
        Starts asynchronous recognition of celebrities in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/start_celebrity_recognition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#start_celebrity_recognition)
        """

    def start_content_moderation(
        self, **kwargs: Unpack[StartContentModerationRequestTypeDef]
    ) -> StartContentModerationResponseTypeDef:
        """
        Starts asynchronous detection of inappropriate, unwanted, or offensive content
        in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/start_content_moderation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#start_content_moderation)
        """

    def start_face_detection(
        self, **kwargs: Unpack[StartFaceDetectionRequestTypeDef]
    ) -> StartFaceDetectionResponseTypeDef:
        """
        Starts asynchronous detection of faces in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/start_face_detection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#start_face_detection)
        """

    def start_face_search(
        self, **kwargs: Unpack[StartFaceSearchRequestTypeDef]
    ) -> StartFaceSearchResponseTypeDef:
        """
        Starts the asynchronous search for faces in a collection that match the faces
        of persons detected in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/start_face_search.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#start_face_search)
        """

    def start_label_detection(
        self, **kwargs: Unpack[StartLabelDetectionRequestTypeDef]
    ) -> StartLabelDetectionResponseTypeDef:
        """
        Starts asynchronous detection of labels in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/start_label_detection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#start_label_detection)
        """

    def start_media_analysis_job(
        self, **kwargs: Unpack[StartMediaAnalysisJobRequestTypeDef]
    ) -> StartMediaAnalysisJobResponseTypeDef:
        """
        Initiates a new media analysis job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/start_media_analysis_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#start_media_analysis_job)
        """

    def start_person_tracking(
        self, **kwargs: Unpack[StartPersonTrackingRequestTypeDef]
    ) -> StartPersonTrackingResponseTypeDef:
        """
        Starts the asynchronous tracking of a person's path in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/start_person_tracking.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#start_person_tracking)
        """

    def start_project_version(
        self, **kwargs: Unpack[StartProjectVersionRequestTypeDef]
    ) -> StartProjectVersionResponseTypeDef:
        """
        This operation applies only to Amazon Rekognition Custom Labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/start_project_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#start_project_version)
        """

    def start_segment_detection(
        self, **kwargs: Unpack[StartSegmentDetectionRequestTypeDef]
    ) -> StartSegmentDetectionResponseTypeDef:
        """
        Starts asynchronous detection of segment detection in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/start_segment_detection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#start_segment_detection)
        """

    def start_stream_processor(
        self, **kwargs: Unpack[StartStreamProcessorRequestTypeDef]
    ) -> StartStreamProcessorResponseTypeDef:
        """
        Starts processing a stream processor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/start_stream_processor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#start_stream_processor)
        """

    def start_text_detection(
        self, **kwargs: Unpack[StartTextDetectionRequestTypeDef]
    ) -> StartTextDetectionResponseTypeDef:
        """
        Starts asynchronous detection of text in a stored video.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/start_text_detection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#start_text_detection)
        """

    def stop_project_version(
        self, **kwargs: Unpack[StopProjectVersionRequestTypeDef]
    ) -> StopProjectVersionResponseTypeDef:
        """
        This operation applies only to Amazon Rekognition Custom Labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/stop_project_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#stop_project_version)
        """

    def stop_stream_processor(
        self, **kwargs: Unpack[StopStreamProcessorRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops a running stream processor that was created by
        <a>CreateStreamProcessor</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/stop_stream_processor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#stop_stream_processor)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more key-value tags to an Amazon Rekognition collection, stream
        processor, or Custom Labels model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from an Amazon Rekognition collection, stream
        processor, or Custom Labels model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#untag_resource)
        """

    def update_dataset_entries(
        self, **kwargs: Unpack[UpdateDatasetEntriesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        This operation applies only to Amazon Rekognition Custom Labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/update_dataset_entries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#update_dataset_entries)
        """

    def update_stream_processor(
        self, **kwargs: Unpack[UpdateStreamProcessorRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Allows you to update a stream processor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/update_stream_processor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#update_stream_processor)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_project_versions"]
    ) -> DescribeProjectVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_projects"]
    ) -> DescribeProjectsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_collections"]
    ) -> ListCollectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dataset_entries"]
    ) -> ListDatasetEntriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dataset_labels"]
    ) -> ListDatasetLabelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_faces"]
    ) -> ListFacesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_project_policies"]
    ) -> ListProjectPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_stream_processors"]
    ) -> ListStreamProcessorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_users"]
    ) -> ListUsersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["project_version_running"]
    ) -> ProjectVersionRunningWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["project_version_training_completed"]
    ) -> ProjectVersionTrainingCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rekognition/client/#get_waiter)
        """
