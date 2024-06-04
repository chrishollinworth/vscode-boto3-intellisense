"""
Type annotations for rekognition service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rekognition.type_defs import AgeRangeTypeDef

    data: AgeRangeTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AttributeType,
    BodyPartType,
    CelebrityRecognitionSortByType,
    ContentClassifierType,
    ContentModerationAggregateByType,
    ContentModerationSortByType,
    CustomizationFeatureType,
    DatasetStatusMessageCodeType,
    DatasetStatusType,
    DatasetTypeType,
    DetectLabelsFeatureNameType,
    EmotionNameType,
    FaceAttributesType,
    FaceSearchSortByType,
    GenderTypeType,
    KnownGenderTypeType,
    LabelDetectionAggregateByType,
    LabelDetectionSortByType,
    LandmarkTypeType,
    LivenessSessionStatusType,
    MediaAnalysisJobFailureCodeType,
    MediaAnalysisJobStatusType,
    OrientationCorrectionType,
    PersonTrackingSortByType,
    ProjectAutoUpdateType,
    ProjectStatusType,
    ProjectVersionStatusType,
    ProtectiveEquipmentTypeType,
    QualityFilterType,
    ReasonType,
    SegmentTypeType,
    StreamProcessorParameterToDeleteType,
    StreamProcessorStatusType,
    TechnicalCueTypeType,
    TextTypesType,
    UnsearchedFaceReasonType,
    UnsuccessfulFaceAssociationReasonType,
    UnsuccessfulFaceDeletionReasonType,
    UnsuccessfulFaceDisassociationReasonType,
    UserStatusType,
    VideoColorRangeType,
    VideoJobStatusType,
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
    "AgeRangeTypeDef",
    "AssetTypeDef",
    "AssociateFacesRequestRequestTypeDef",
    "AssociateFacesResponseTypeDef",
    "AssociatedFaceTypeDef",
    "AudioMetadataTypeDef",
    "AuditImageTypeDef",
    "BeardTypeDef",
    "BlackFrameTypeDef",
    "BoundingBoxTypeDef",
    "CelebrityDetailTypeDef",
    "CelebrityRecognitionTypeDef",
    "CelebrityTypeDef",
    "CompareFacesMatchTypeDef",
    "CompareFacesRequestRequestTypeDef",
    "CompareFacesResponseTypeDef",
    "ComparedFaceTypeDef",
    "ComparedSourceImageFaceTypeDef",
    "ConnectedHomeSettingsForUpdateTypeDef",
    "ConnectedHomeSettingsTypeDef",
    "ContentModerationDetectionTypeDef",
    "ContentTypeTypeDef",
    "CopyProjectVersionRequestRequestTypeDef",
    "CopyProjectVersionResponseTypeDef",
    "CoversBodyPartTypeDef",
    "CreateCollectionRequestRequestTypeDef",
    "CreateCollectionResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateFaceLivenessSessionRequestRequestTypeDef",
    "CreateFaceLivenessSessionRequestSettingsTypeDef",
    "CreateFaceLivenessSessionResponseTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateProjectVersionRequestRequestTypeDef",
    "CreateProjectVersionResponseTypeDef",
    "CreateStreamProcessorRequestRequestTypeDef",
    "CreateStreamProcessorResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CustomLabelTypeDef",
    "CustomizationFeatureConfigTypeDef",
    "CustomizationFeatureContentModerationConfigTypeDef",
    "DatasetChangesTypeDef",
    "DatasetDescriptionTypeDef",
    "DatasetLabelDescriptionTypeDef",
    "DatasetLabelStatsTypeDef",
    "DatasetMetadataTypeDef",
    "DatasetSourceTypeDef",
    "DatasetStatsTypeDef",
    "DeleteCollectionRequestRequestTypeDef",
    "DeleteCollectionResponseTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteFacesRequestRequestTypeDef",
    "DeleteFacesResponseTypeDef",
    "DeleteProjectPolicyRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteProjectVersionRequestRequestTypeDef",
    "DeleteProjectVersionResponseTypeDef",
    "DeleteStreamProcessorRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeCollectionRequestRequestTypeDef",
    "DescribeCollectionResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeProjectVersionsRequestRequestTypeDef",
    "DescribeProjectVersionsResponseTypeDef",
    "DescribeProjectsRequestRequestTypeDef",
    "DescribeProjectsResponseTypeDef",
    "DescribeStreamProcessorRequestRequestTypeDef",
    "DescribeStreamProcessorResponseTypeDef",
    "DetectCustomLabelsRequestRequestTypeDef",
    "DetectCustomLabelsResponseTypeDef",
    "DetectFacesRequestRequestTypeDef",
    "DetectFacesResponseTypeDef",
    "DetectLabelsImageBackgroundTypeDef",
    "DetectLabelsImageForegroundTypeDef",
    "DetectLabelsImagePropertiesSettingsTypeDef",
    "DetectLabelsImagePropertiesTypeDef",
    "DetectLabelsImageQualityTypeDef",
    "DetectLabelsRequestRequestTypeDef",
    "DetectLabelsResponseTypeDef",
    "DetectLabelsSettingsTypeDef",
    "DetectModerationLabelsRequestRequestTypeDef",
    "DetectModerationLabelsResponseTypeDef",
    "DetectProtectiveEquipmentRequestRequestTypeDef",
    "DetectProtectiveEquipmentResponseTypeDef",
    "DetectTextFiltersTypeDef",
    "DetectTextRequestRequestTypeDef",
    "DetectTextResponseTypeDef",
    "DetectionFilterTypeDef",
    "DisassociateFacesRequestRequestTypeDef",
    "DisassociateFacesResponseTypeDef",
    "DisassociatedFaceTypeDef",
    "DistributeDatasetEntriesRequestRequestTypeDef",
    "DistributeDatasetTypeDef",
    "DominantColorTypeDef",
    "EmotionTypeDef",
    "EquipmentDetectionTypeDef",
    "EvaluationResultTypeDef",
    "EyeDirectionTypeDef",
    "EyeOpenTypeDef",
    "EyeglassesTypeDef",
    "FaceDetailTypeDef",
    "FaceDetectionTypeDef",
    "FaceMatchTypeDef",
    "FaceOccludedTypeDef",
    "FaceRecordTypeDef",
    "FaceSearchSettingsTypeDef",
    "FaceTypeDef",
    "GenderTypeDef",
    "GeneralLabelsSettingsTypeDef",
    "GeometryTypeDef",
    "GetCelebrityInfoRequestRequestTypeDef",
    "GetCelebrityInfoResponseTypeDef",
    "GetCelebrityRecognitionRequestRequestTypeDef",
    "GetCelebrityRecognitionResponseTypeDef",
    "GetContentModerationRequestMetadataTypeDef",
    "GetContentModerationRequestRequestTypeDef",
    "GetContentModerationResponseTypeDef",
    "GetFaceDetectionRequestRequestTypeDef",
    "GetFaceDetectionResponseTypeDef",
    "GetFaceLivenessSessionResultsRequestRequestTypeDef",
    "GetFaceLivenessSessionResultsResponseTypeDef",
    "GetFaceSearchRequestRequestTypeDef",
    "GetFaceSearchResponseTypeDef",
    "GetLabelDetectionRequestMetadataTypeDef",
    "GetLabelDetectionRequestRequestTypeDef",
    "GetLabelDetectionResponseTypeDef",
    "GetMediaAnalysisJobRequestRequestTypeDef",
    "GetMediaAnalysisJobResponseTypeDef",
    "GetPersonTrackingRequestRequestTypeDef",
    "GetPersonTrackingResponseTypeDef",
    "GetSegmentDetectionRequestRequestTypeDef",
    "GetSegmentDetectionResponseTypeDef",
    "GetTextDetectionRequestRequestTypeDef",
    "GetTextDetectionResponseTypeDef",
    "GroundTruthManifestTypeDef",
    "HumanLoopActivationOutputTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "ImageQualityTypeDef",
    "ImageTypeDef",
    "IndexFacesRequestRequestTypeDef",
    "IndexFacesResponseTypeDef",
    "InstanceTypeDef",
    "KinesisDataStreamTypeDef",
    "KinesisVideoStreamStartSelectorTypeDef",
    "KinesisVideoStreamTypeDef",
    "KnownGenderTypeDef",
    "LabelAliasTypeDef",
    "LabelCategoryTypeDef",
    "LabelDetectionSettingsTypeDef",
    "LabelDetectionTypeDef",
    "LabelTypeDef",
    "LandmarkTypeDef",
    "ListCollectionsRequestRequestTypeDef",
    "ListCollectionsResponseTypeDef",
    "ListDatasetEntriesRequestRequestTypeDef",
    "ListDatasetEntriesResponseTypeDef",
    "ListDatasetLabelsRequestRequestTypeDef",
    "ListDatasetLabelsResponseTypeDef",
    "ListFacesRequestRequestTypeDef",
    "ListFacesResponseTypeDef",
    "ListMediaAnalysisJobsRequestRequestTypeDef",
    "ListMediaAnalysisJobsResponseTypeDef",
    "ListProjectPoliciesRequestRequestTypeDef",
    "ListProjectPoliciesResponseTypeDef",
    "ListStreamProcessorsRequestRequestTypeDef",
    "ListStreamProcessorsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "LivenessOutputConfigTypeDef",
    "MatchedUserTypeDef",
    "MediaAnalysisDetectModerationLabelsConfigTypeDef",
    "MediaAnalysisInputTypeDef",
    "MediaAnalysisJobDescriptionTypeDef",
    "MediaAnalysisJobFailureDetailsTypeDef",
    "MediaAnalysisManifestSummaryTypeDef",
    "MediaAnalysisModelVersionsTypeDef",
    "MediaAnalysisOperationsConfigTypeDef",
    "MediaAnalysisOutputConfigTypeDef",
    "MediaAnalysisResultsTypeDef",
    "ModerationLabelTypeDef",
    "MouthOpenTypeDef",
    "MustacheTypeDef",
    "NotificationChannelTypeDef",
    "OutputConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParentTypeDef",
    "PersonDetailTypeDef",
    "PersonDetectionTypeDef",
    "PersonMatchTypeDef",
    "PointTypeDef",
    "PoseTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectPolicyTypeDef",
    "ProjectVersionDescriptionTypeDef",
    "ProtectiveEquipmentBodyPartTypeDef",
    "ProtectiveEquipmentPersonTypeDef",
    "ProtectiveEquipmentSummarizationAttributesTypeDef",
    "ProtectiveEquipmentSummaryTypeDef",
    "PutProjectPolicyRequestRequestTypeDef",
    "PutProjectPolicyResponseTypeDef",
    "RecognizeCelebritiesRequestRequestTypeDef",
    "RecognizeCelebritiesResponseTypeDef",
    "RegionOfInterestTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationTypeDef",
    "S3ObjectTypeDef",
    "SearchFacesByImageRequestRequestTypeDef",
    "SearchFacesByImageResponseTypeDef",
    "SearchFacesRequestRequestTypeDef",
    "SearchFacesResponseTypeDef",
    "SearchUsersByImageRequestRequestTypeDef",
    "SearchUsersByImageResponseTypeDef",
    "SearchUsersRequestRequestTypeDef",
    "SearchUsersResponseTypeDef",
    "SearchedFaceDetailsTypeDef",
    "SearchedFaceTypeDef",
    "SearchedUserTypeDef",
    "SegmentDetectionTypeDef",
    "SegmentTypeInfoTypeDef",
    "ShotSegmentTypeDef",
    "SmileTypeDef",
    "StartCelebrityRecognitionRequestRequestTypeDef",
    "StartCelebrityRecognitionResponseTypeDef",
    "StartContentModerationRequestRequestTypeDef",
    "StartContentModerationResponseTypeDef",
    "StartFaceDetectionRequestRequestTypeDef",
    "StartFaceDetectionResponseTypeDef",
    "StartFaceSearchRequestRequestTypeDef",
    "StartFaceSearchResponseTypeDef",
    "StartLabelDetectionRequestRequestTypeDef",
    "StartLabelDetectionResponseTypeDef",
    "StartMediaAnalysisJobRequestRequestTypeDef",
    "StartMediaAnalysisJobResponseTypeDef",
    "StartPersonTrackingRequestRequestTypeDef",
    "StartPersonTrackingResponseTypeDef",
    "StartProjectVersionRequestRequestTypeDef",
    "StartProjectVersionResponseTypeDef",
    "StartSegmentDetectionFiltersTypeDef",
    "StartSegmentDetectionRequestRequestTypeDef",
    "StartSegmentDetectionResponseTypeDef",
    "StartShotDetectionFilterTypeDef",
    "StartStreamProcessorRequestRequestTypeDef",
    "StartStreamProcessorResponseTypeDef",
    "StartTechnicalCueDetectionFilterTypeDef",
    "StartTextDetectionFiltersTypeDef",
    "StartTextDetectionRequestRequestTypeDef",
    "StartTextDetectionResponseTypeDef",
    "StopProjectVersionRequestRequestTypeDef",
    "StopProjectVersionResponseTypeDef",
    "StopStreamProcessorRequestRequestTypeDef",
    "StreamProcessingStartSelectorTypeDef",
    "StreamProcessingStopSelectorTypeDef",
    "StreamProcessorDataSharingPreferenceTypeDef",
    "StreamProcessorInputTypeDef",
    "StreamProcessorNotificationChannelTypeDef",
    "StreamProcessorOutputTypeDef",
    "StreamProcessorSettingsForUpdateTypeDef",
    "StreamProcessorSettingsTypeDef",
    "StreamProcessorTypeDef",
    "SummaryTypeDef",
    "SunglassesTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TechnicalCueSegmentTypeDef",
    "TestingDataResultTypeDef",
    "TestingDataTypeDef",
    "TextDetectionResultTypeDef",
    "TextDetectionTypeDef",
    "TrainingDataResultTypeDef",
    "TrainingDataTypeDef",
    "UnindexedFaceTypeDef",
    "UnsearchedFaceTypeDef",
    "UnsuccessfulFaceAssociationTypeDef",
    "UnsuccessfulFaceDeletionTypeDef",
    "UnsuccessfulFaceDisassociationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatasetEntriesRequestRequestTypeDef",
    "UpdateStreamProcessorRequestRequestTypeDef",
    "UserMatchTypeDef",
    "UserTypeDef",
    "ValidationDataTypeDef",
    "VideoMetadataTypeDef",
    "VideoTypeDef",
    "WaiterConfigTypeDef",
)

AgeRangeTypeDef = TypedDict(
    "AgeRangeTypeDef",
    {
        "Low": int,
        "High": int,
    },
    total=False,
)

AssetTypeDef = TypedDict(
    "AssetTypeDef",
    {
        "GroundTruthManifest": "GroundTruthManifestTypeDef",
    },
    total=False,
)

_RequiredAssociateFacesRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
        "UserId": str,
        "FaceIds": List[str],
    },
)
_OptionalAssociateFacesRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateFacesRequestRequestTypeDef",
    {
        "UserMatchThreshold": float,
        "ClientRequestToken": str,
    },
    total=False,
)

class AssociateFacesRequestRequestTypeDef(
    _RequiredAssociateFacesRequestRequestTypeDef, _OptionalAssociateFacesRequestRequestTypeDef
):
    pass

AssociateFacesResponseTypeDef = TypedDict(
    "AssociateFacesResponseTypeDef",
    {
        "AssociatedFaces": List["AssociatedFaceTypeDef"],
        "UnsuccessfulFaceAssociations": List["UnsuccessfulFaceAssociationTypeDef"],
        "UserStatus": UserStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociatedFaceTypeDef = TypedDict(
    "AssociatedFaceTypeDef",
    {
        "FaceId": str,
    },
    total=False,
)

AudioMetadataTypeDef = TypedDict(
    "AudioMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "SampleRate": int,
        "NumberOfChannels": int,
    },
    total=False,
)

AuditImageTypeDef = TypedDict(
    "AuditImageTypeDef",
    {
        "Bytes": bytes,
        "S3Object": "S3ObjectTypeDef",
        "BoundingBox": "BoundingBoxTypeDef",
    },
    total=False,
)

BeardTypeDef = TypedDict(
    "BeardTypeDef",
    {
        "Value": bool,
        "Confidence": float,
    },
    total=False,
)

BlackFrameTypeDef = TypedDict(
    "BlackFrameTypeDef",
    {
        "MaxPixelThreshold": float,
        "MinCoveragePercentage": float,
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

CelebrityDetailTypeDef = TypedDict(
    "CelebrityDetailTypeDef",
    {
        "Urls": List[str],
        "Name": str,
        "Id": str,
        "Confidence": float,
        "BoundingBox": "BoundingBoxTypeDef",
        "Face": "FaceDetailTypeDef",
        "KnownGender": "KnownGenderTypeDef",
    },
    total=False,
)

CelebrityRecognitionTypeDef = TypedDict(
    "CelebrityRecognitionTypeDef",
    {
        "Timestamp": int,
        "Celebrity": "CelebrityDetailTypeDef",
    },
    total=False,
)

CelebrityTypeDef = TypedDict(
    "CelebrityTypeDef",
    {
        "Urls": List[str],
        "Name": str,
        "Id": str,
        "Face": "ComparedFaceTypeDef",
        "MatchConfidence": float,
        "KnownGender": "KnownGenderTypeDef",
    },
    total=False,
)

CompareFacesMatchTypeDef = TypedDict(
    "CompareFacesMatchTypeDef",
    {
        "Similarity": float,
        "Face": "ComparedFaceTypeDef",
    },
    total=False,
)

_RequiredCompareFacesRequestRequestTypeDef = TypedDict(
    "_RequiredCompareFacesRequestRequestTypeDef",
    {
        "SourceImage": "ImageTypeDef",
        "TargetImage": "ImageTypeDef",
    },
)
_OptionalCompareFacesRequestRequestTypeDef = TypedDict(
    "_OptionalCompareFacesRequestRequestTypeDef",
    {
        "SimilarityThreshold": float,
        "QualityFilter": QualityFilterType,
    },
    total=False,
)

class CompareFacesRequestRequestTypeDef(
    _RequiredCompareFacesRequestRequestTypeDef, _OptionalCompareFacesRequestRequestTypeDef
):
    pass

CompareFacesResponseTypeDef = TypedDict(
    "CompareFacesResponseTypeDef",
    {
        "SourceImageFace": "ComparedSourceImageFaceTypeDef",
        "FaceMatches": List["CompareFacesMatchTypeDef"],
        "UnmatchedFaces": List["ComparedFaceTypeDef"],
        "SourceImageOrientationCorrection": OrientationCorrectionType,
        "TargetImageOrientationCorrection": OrientationCorrectionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ComparedFaceTypeDef = TypedDict(
    "ComparedFaceTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
        "Confidence": float,
        "Landmarks": List["LandmarkTypeDef"],
        "Pose": "PoseTypeDef",
        "Quality": "ImageQualityTypeDef",
        "Emotions": List["EmotionTypeDef"],
        "Smile": "SmileTypeDef",
    },
    total=False,
)

ComparedSourceImageFaceTypeDef = TypedDict(
    "ComparedSourceImageFaceTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
        "Confidence": float,
    },
    total=False,
)

ConnectedHomeSettingsForUpdateTypeDef = TypedDict(
    "ConnectedHomeSettingsForUpdateTypeDef",
    {
        "Labels": List[str],
        "MinConfidence": float,
    },
    total=False,
)

_RequiredConnectedHomeSettingsTypeDef = TypedDict(
    "_RequiredConnectedHomeSettingsTypeDef",
    {
        "Labels": List[str],
    },
)
_OptionalConnectedHomeSettingsTypeDef = TypedDict(
    "_OptionalConnectedHomeSettingsTypeDef",
    {
        "MinConfidence": float,
    },
    total=False,
)

class ConnectedHomeSettingsTypeDef(
    _RequiredConnectedHomeSettingsTypeDef, _OptionalConnectedHomeSettingsTypeDef
):
    pass

ContentModerationDetectionTypeDef = TypedDict(
    "ContentModerationDetectionTypeDef",
    {
        "Timestamp": int,
        "ModerationLabel": "ModerationLabelTypeDef",
        "StartTimestampMillis": int,
        "EndTimestampMillis": int,
        "DurationMillis": int,
        "ContentTypes": List["ContentTypeTypeDef"],
    },
    total=False,
)

ContentTypeTypeDef = TypedDict(
    "ContentTypeTypeDef",
    {
        "Confidence": float,
        "Name": str,
    },
    total=False,
)

_RequiredCopyProjectVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCopyProjectVersionRequestRequestTypeDef",
    {
        "SourceProjectArn": str,
        "SourceProjectVersionArn": str,
        "DestinationProjectArn": str,
        "VersionName": str,
        "OutputConfig": "OutputConfigTypeDef",
    },
)
_OptionalCopyProjectVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCopyProjectVersionRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
        "KmsKeyId": str,
    },
    total=False,
)

class CopyProjectVersionRequestRequestTypeDef(
    _RequiredCopyProjectVersionRequestRequestTypeDef,
    _OptionalCopyProjectVersionRequestRequestTypeDef,
):
    pass

CopyProjectVersionResponseTypeDef = TypedDict(
    "CopyProjectVersionResponseTypeDef",
    {
        "ProjectVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CoversBodyPartTypeDef = TypedDict(
    "CoversBodyPartTypeDef",
    {
        "Confidence": float,
        "Value": bool,
    },
    total=False,
)

_RequiredCreateCollectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCollectionRequestRequestTypeDef",
    {
        "CollectionId": str,
    },
)
_OptionalCreateCollectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCollectionRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateCollectionRequestRequestTypeDef(
    _RequiredCreateCollectionRequestRequestTypeDef, _OptionalCreateCollectionRequestRequestTypeDef
):
    pass

CreateCollectionResponseTypeDef = TypedDict(
    "CreateCollectionResponseTypeDef",
    {
        "StatusCode": int,
        "CollectionArn": str,
        "FaceModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestRequestTypeDef",
    {
        "DatasetType": DatasetTypeType,
        "ProjectArn": str,
    },
)
_OptionalCreateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestRequestTypeDef",
    {
        "DatasetSource": "DatasetSourceTypeDef",
    },
    total=False,
)

class CreateDatasetRequestRequestTypeDef(
    _RequiredCreateDatasetRequestRequestTypeDef, _OptionalCreateDatasetRequestRequestTypeDef
):
    pass

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "DatasetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFaceLivenessSessionRequestRequestTypeDef = TypedDict(
    "CreateFaceLivenessSessionRequestRequestTypeDef",
    {
        "KmsKeyId": str,
        "Settings": "CreateFaceLivenessSessionRequestSettingsTypeDef",
        "ClientRequestToken": str,
    },
    total=False,
)

CreateFaceLivenessSessionRequestSettingsTypeDef = TypedDict(
    "CreateFaceLivenessSessionRequestSettingsTypeDef",
    {
        "OutputConfig": "LivenessOutputConfigTypeDef",
        "AuditImagesLimit": int,
    },
    total=False,
)

CreateFaceLivenessSessionResponseTypeDef = TypedDict(
    "CreateFaceLivenessSessionResponseTypeDef",
    {
        "SessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestRequestTypeDef",
    {
        "ProjectName": str,
    },
)
_OptionalCreateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestRequestTypeDef",
    {
        "Feature": CustomizationFeatureType,
        "AutoUpdate": ProjectAutoUpdateType,
    },
    total=False,
)

class CreateProjectRequestRequestTypeDef(
    _RequiredCreateProjectRequestRequestTypeDef, _OptionalCreateProjectRequestRequestTypeDef
):
    pass

CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "ProjectArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProjectVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProjectVersionRequestRequestTypeDef",
    {
        "ProjectArn": str,
        "VersionName": str,
        "OutputConfig": "OutputConfigTypeDef",
    },
)
_OptionalCreateProjectVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProjectVersionRequestRequestTypeDef",
    {
        "TrainingData": "TrainingDataTypeDef",
        "TestingData": "TestingDataTypeDef",
        "Tags": Dict[str, str],
        "KmsKeyId": str,
        "VersionDescription": str,
        "FeatureConfig": "CustomizationFeatureConfigTypeDef",
    },
    total=False,
)

class CreateProjectVersionRequestRequestTypeDef(
    _RequiredCreateProjectVersionRequestRequestTypeDef,
    _OptionalCreateProjectVersionRequestRequestTypeDef,
):
    pass

CreateProjectVersionResponseTypeDef = TypedDict(
    "CreateProjectVersionResponseTypeDef",
    {
        "ProjectVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamProcessorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStreamProcessorRequestRequestTypeDef",
    {
        "Input": "StreamProcessorInputTypeDef",
        "Output": "StreamProcessorOutputTypeDef",
        "Name": str,
        "Settings": "StreamProcessorSettingsTypeDef",
        "RoleArn": str,
    },
)
_OptionalCreateStreamProcessorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStreamProcessorRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
        "NotificationChannel": "StreamProcessorNotificationChannelTypeDef",
        "KmsKeyId": str,
        "RegionsOfInterest": List["RegionOfInterestTypeDef"],
        "DataSharingPreference": "StreamProcessorDataSharingPreferenceTypeDef",
    },
    total=False,
)

class CreateStreamProcessorRequestRequestTypeDef(
    _RequiredCreateStreamProcessorRequestRequestTypeDef,
    _OptionalCreateStreamProcessorRequestRequestTypeDef,
):
    pass

CreateStreamProcessorResponseTypeDef = TypedDict(
    "CreateStreamProcessorResponseTypeDef",
    {
        "StreamProcessorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "CollectionId": str,
        "UserId": str,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass

CustomLabelTypeDef = TypedDict(
    "CustomLabelTypeDef",
    {
        "Name": str,
        "Confidence": float,
        "Geometry": "GeometryTypeDef",
    },
    total=False,
)

CustomizationFeatureConfigTypeDef = TypedDict(
    "CustomizationFeatureConfigTypeDef",
    {
        "ContentModeration": "CustomizationFeatureContentModerationConfigTypeDef",
    },
    total=False,
)

CustomizationFeatureContentModerationConfigTypeDef = TypedDict(
    "CustomizationFeatureContentModerationConfigTypeDef",
    {
        "ConfidenceThreshold": float,
    },
    total=False,
)

DatasetChangesTypeDef = TypedDict(
    "DatasetChangesTypeDef",
    {
        "GroundTruth": Union[bytes, IO[bytes], StreamingBody],
    },
)

DatasetDescriptionTypeDef = TypedDict(
    "DatasetDescriptionTypeDef",
    {
        "CreationTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Status": DatasetStatusType,
        "StatusMessage": str,
        "StatusMessageCode": DatasetStatusMessageCodeType,
        "DatasetStats": "DatasetStatsTypeDef",
    },
    total=False,
)

DatasetLabelDescriptionTypeDef = TypedDict(
    "DatasetLabelDescriptionTypeDef",
    {
        "LabelName": str,
        "LabelStats": "DatasetLabelStatsTypeDef",
    },
    total=False,
)

DatasetLabelStatsTypeDef = TypedDict(
    "DatasetLabelStatsTypeDef",
    {
        "EntryCount": int,
        "BoundingBoxCount": int,
    },
    total=False,
)

DatasetMetadataTypeDef = TypedDict(
    "DatasetMetadataTypeDef",
    {
        "CreationTimestamp": datetime,
        "DatasetType": DatasetTypeType,
        "DatasetArn": str,
        "Status": DatasetStatusType,
        "StatusMessage": str,
        "StatusMessageCode": DatasetStatusMessageCodeType,
    },
    total=False,
)

DatasetSourceTypeDef = TypedDict(
    "DatasetSourceTypeDef",
    {
        "GroundTruthManifest": "GroundTruthManifestTypeDef",
        "DatasetArn": str,
    },
    total=False,
)

DatasetStatsTypeDef = TypedDict(
    "DatasetStatsTypeDef",
    {
        "LabeledEntries": int,
        "TotalEntries": int,
        "TotalLabels": int,
        "ErrorEntries": int,
    },
    total=False,
)

DeleteCollectionRequestRequestTypeDef = TypedDict(
    "DeleteCollectionRequestRequestTypeDef",
    {
        "CollectionId": str,
    },
)

DeleteCollectionResponseTypeDef = TypedDict(
    "DeleteCollectionResponseTypeDef",
    {
        "StatusCode": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "DatasetArn": str,
    },
)

DeleteFacesRequestRequestTypeDef = TypedDict(
    "DeleteFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
        "FaceIds": List[str],
    },
)

DeleteFacesResponseTypeDef = TypedDict(
    "DeleteFacesResponseTypeDef",
    {
        "DeletedFaces": List[str],
        "UnsuccessfulFaceDeletions": List["UnsuccessfulFaceDeletionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteProjectPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteProjectPolicyRequestRequestTypeDef",
    {
        "ProjectArn": str,
        "PolicyName": str,
    },
)
_OptionalDeleteProjectPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteProjectPolicyRequestRequestTypeDef",
    {
        "PolicyRevisionId": str,
    },
    total=False,
)

class DeleteProjectPolicyRequestRequestTypeDef(
    _RequiredDeleteProjectPolicyRequestRequestTypeDef,
    _OptionalDeleteProjectPolicyRequestRequestTypeDef,
):
    pass

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "ProjectArn": str,
    },
)

DeleteProjectResponseTypeDef = TypedDict(
    "DeleteProjectResponseTypeDef",
    {
        "Status": ProjectStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectVersionRequestRequestTypeDef = TypedDict(
    "DeleteProjectVersionRequestRequestTypeDef",
    {
        "ProjectVersionArn": str,
    },
)

DeleteProjectVersionResponseTypeDef = TypedDict(
    "DeleteProjectVersionResponseTypeDef",
    {
        "Status": ProjectVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteStreamProcessorRequestRequestTypeDef = TypedDict(
    "DeleteStreamProcessorRequestRequestTypeDef",
    {
        "Name": str,
    },
)

_RequiredDeleteUserRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteUserRequestRequestTypeDef",
    {
        "CollectionId": str,
        "UserId": str,
    },
)
_OptionalDeleteUserRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteUserRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class DeleteUserRequestRequestTypeDef(
    _RequiredDeleteUserRequestRequestTypeDef, _OptionalDeleteUserRequestRequestTypeDef
):
    pass

DescribeCollectionRequestRequestTypeDef = TypedDict(
    "DescribeCollectionRequestRequestTypeDef",
    {
        "CollectionId": str,
    },
)

DescribeCollectionResponseTypeDef = TypedDict(
    "DescribeCollectionResponseTypeDef",
    {
        "FaceCount": int,
        "FaceModelVersion": str,
        "CollectionARN": str,
        "CreationTimestamp": datetime,
        "UserCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "DatasetArn": str,
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "DatasetDescription": "DatasetDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeProjectVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeProjectVersionsRequestRequestTypeDef",
    {
        "ProjectArn": str,
    },
)
_OptionalDescribeProjectVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeProjectVersionsRequestRequestTypeDef",
    {
        "VersionNames": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeProjectVersionsRequestRequestTypeDef(
    _RequiredDescribeProjectVersionsRequestRequestTypeDef,
    _OptionalDescribeProjectVersionsRequestRequestTypeDef,
):
    pass

DescribeProjectVersionsResponseTypeDef = TypedDict(
    "DescribeProjectVersionsResponseTypeDef",
    {
        "ProjectVersionDescriptions": List["ProjectVersionDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectsRequestRequestTypeDef = TypedDict(
    "DescribeProjectsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "ProjectNames": List[str],
        "Features": List[CustomizationFeatureType],
    },
    total=False,
)

DescribeProjectsResponseTypeDef = TypedDict(
    "DescribeProjectsResponseTypeDef",
    {
        "ProjectDescriptions": List["ProjectDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamProcessorRequestRequestTypeDef = TypedDict(
    "DescribeStreamProcessorRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeStreamProcessorResponseTypeDef = TypedDict(
    "DescribeStreamProcessorResponseTypeDef",
    {
        "Name": str,
        "StreamProcessorArn": str,
        "Status": StreamProcessorStatusType,
        "StatusMessage": str,
        "CreationTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "Input": "StreamProcessorInputTypeDef",
        "Output": "StreamProcessorOutputTypeDef",
        "RoleArn": str,
        "Settings": "StreamProcessorSettingsTypeDef",
        "NotificationChannel": "StreamProcessorNotificationChannelTypeDef",
        "KmsKeyId": str,
        "RegionsOfInterest": List["RegionOfInterestTypeDef"],
        "DataSharingPreference": "StreamProcessorDataSharingPreferenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetectCustomLabelsRequestRequestTypeDef = TypedDict(
    "_RequiredDetectCustomLabelsRequestRequestTypeDef",
    {
        "ProjectVersionArn": str,
        "Image": "ImageTypeDef",
    },
)
_OptionalDetectCustomLabelsRequestRequestTypeDef = TypedDict(
    "_OptionalDetectCustomLabelsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "MinConfidence": float,
    },
    total=False,
)

class DetectCustomLabelsRequestRequestTypeDef(
    _RequiredDetectCustomLabelsRequestRequestTypeDef,
    _OptionalDetectCustomLabelsRequestRequestTypeDef,
):
    pass

DetectCustomLabelsResponseTypeDef = TypedDict(
    "DetectCustomLabelsResponseTypeDef",
    {
        "CustomLabels": List["CustomLabelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetectFacesRequestRequestTypeDef = TypedDict(
    "_RequiredDetectFacesRequestRequestTypeDef",
    {
        "Image": "ImageTypeDef",
    },
)
_OptionalDetectFacesRequestRequestTypeDef = TypedDict(
    "_OptionalDetectFacesRequestRequestTypeDef",
    {
        "Attributes": List[AttributeType],
    },
    total=False,
)

class DetectFacesRequestRequestTypeDef(
    _RequiredDetectFacesRequestRequestTypeDef, _OptionalDetectFacesRequestRequestTypeDef
):
    pass

DetectFacesResponseTypeDef = TypedDict(
    "DetectFacesResponseTypeDef",
    {
        "FaceDetails": List["FaceDetailTypeDef"],
        "OrientationCorrection": OrientationCorrectionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectLabelsImageBackgroundTypeDef = TypedDict(
    "DetectLabelsImageBackgroundTypeDef",
    {
        "Quality": "DetectLabelsImageQualityTypeDef",
        "DominantColors": List["DominantColorTypeDef"],
    },
    total=False,
)

DetectLabelsImageForegroundTypeDef = TypedDict(
    "DetectLabelsImageForegroundTypeDef",
    {
        "Quality": "DetectLabelsImageQualityTypeDef",
        "DominantColors": List["DominantColorTypeDef"],
    },
    total=False,
)

DetectLabelsImagePropertiesSettingsTypeDef = TypedDict(
    "DetectLabelsImagePropertiesSettingsTypeDef",
    {
        "MaxDominantColors": int,
    },
    total=False,
)

DetectLabelsImagePropertiesTypeDef = TypedDict(
    "DetectLabelsImagePropertiesTypeDef",
    {
        "Quality": "DetectLabelsImageQualityTypeDef",
        "DominantColors": List["DominantColorTypeDef"],
        "Foreground": "DetectLabelsImageForegroundTypeDef",
        "Background": "DetectLabelsImageBackgroundTypeDef",
    },
    total=False,
)

DetectLabelsImageQualityTypeDef = TypedDict(
    "DetectLabelsImageQualityTypeDef",
    {
        "Brightness": float,
        "Sharpness": float,
        "Contrast": float,
    },
    total=False,
)

_RequiredDetectLabelsRequestRequestTypeDef = TypedDict(
    "_RequiredDetectLabelsRequestRequestTypeDef",
    {
        "Image": "ImageTypeDef",
    },
)
_OptionalDetectLabelsRequestRequestTypeDef = TypedDict(
    "_OptionalDetectLabelsRequestRequestTypeDef",
    {
        "MaxLabels": int,
        "MinConfidence": float,
        "Features": List[DetectLabelsFeatureNameType],
        "Settings": "DetectLabelsSettingsTypeDef",
    },
    total=False,
)

class DetectLabelsRequestRequestTypeDef(
    _RequiredDetectLabelsRequestRequestTypeDef, _OptionalDetectLabelsRequestRequestTypeDef
):
    pass

DetectLabelsResponseTypeDef = TypedDict(
    "DetectLabelsResponseTypeDef",
    {
        "Labels": List["LabelTypeDef"],
        "OrientationCorrection": OrientationCorrectionType,
        "LabelModelVersion": str,
        "ImageProperties": "DetectLabelsImagePropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectLabelsSettingsTypeDef = TypedDict(
    "DetectLabelsSettingsTypeDef",
    {
        "GeneralLabels": "GeneralLabelsSettingsTypeDef",
        "ImageProperties": "DetectLabelsImagePropertiesSettingsTypeDef",
    },
    total=False,
)

_RequiredDetectModerationLabelsRequestRequestTypeDef = TypedDict(
    "_RequiredDetectModerationLabelsRequestRequestTypeDef",
    {
        "Image": "ImageTypeDef",
    },
)
_OptionalDetectModerationLabelsRequestRequestTypeDef = TypedDict(
    "_OptionalDetectModerationLabelsRequestRequestTypeDef",
    {
        "MinConfidence": float,
        "HumanLoopConfig": "HumanLoopConfigTypeDef",
        "ProjectVersion": str,
    },
    total=False,
)

class DetectModerationLabelsRequestRequestTypeDef(
    _RequiredDetectModerationLabelsRequestRequestTypeDef,
    _OptionalDetectModerationLabelsRequestRequestTypeDef,
):
    pass

DetectModerationLabelsResponseTypeDef = TypedDict(
    "DetectModerationLabelsResponseTypeDef",
    {
        "ModerationLabels": List["ModerationLabelTypeDef"],
        "ModerationModelVersion": str,
        "HumanLoopActivationOutput": "HumanLoopActivationOutputTypeDef",
        "ProjectVersion": str,
        "ContentTypes": List["ContentTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetectProtectiveEquipmentRequestRequestTypeDef = TypedDict(
    "_RequiredDetectProtectiveEquipmentRequestRequestTypeDef",
    {
        "Image": "ImageTypeDef",
    },
)
_OptionalDetectProtectiveEquipmentRequestRequestTypeDef = TypedDict(
    "_OptionalDetectProtectiveEquipmentRequestRequestTypeDef",
    {
        "SummarizationAttributes": "ProtectiveEquipmentSummarizationAttributesTypeDef",
    },
    total=False,
)

class DetectProtectiveEquipmentRequestRequestTypeDef(
    _RequiredDetectProtectiveEquipmentRequestRequestTypeDef,
    _OptionalDetectProtectiveEquipmentRequestRequestTypeDef,
):
    pass

DetectProtectiveEquipmentResponseTypeDef = TypedDict(
    "DetectProtectiveEquipmentResponseTypeDef",
    {
        "ProtectiveEquipmentModelVersion": str,
        "Persons": List["ProtectiveEquipmentPersonTypeDef"],
        "Summary": "ProtectiveEquipmentSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectTextFiltersTypeDef = TypedDict(
    "DetectTextFiltersTypeDef",
    {
        "WordFilter": "DetectionFilterTypeDef",
        "RegionsOfInterest": List["RegionOfInterestTypeDef"],
    },
    total=False,
)

_RequiredDetectTextRequestRequestTypeDef = TypedDict(
    "_RequiredDetectTextRequestRequestTypeDef",
    {
        "Image": "ImageTypeDef",
    },
)
_OptionalDetectTextRequestRequestTypeDef = TypedDict(
    "_OptionalDetectTextRequestRequestTypeDef",
    {
        "Filters": "DetectTextFiltersTypeDef",
    },
    total=False,
)

class DetectTextRequestRequestTypeDef(
    _RequiredDetectTextRequestRequestTypeDef, _OptionalDetectTextRequestRequestTypeDef
):
    pass

DetectTextResponseTypeDef = TypedDict(
    "DetectTextResponseTypeDef",
    {
        "TextDetections": List["TextDetectionTypeDef"],
        "TextModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectionFilterTypeDef = TypedDict(
    "DetectionFilterTypeDef",
    {
        "MinConfidence": float,
        "MinBoundingBoxHeight": float,
        "MinBoundingBoxWidth": float,
    },
    total=False,
)

_RequiredDisassociateFacesRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
        "UserId": str,
        "FaceIds": List[str],
    },
)
_OptionalDisassociateFacesRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateFacesRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
    },
    total=False,
)

class DisassociateFacesRequestRequestTypeDef(
    _RequiredDisassociateFacesRequestRequestTypeDef, _OptionalDisassociateFacesRequestRequestTypeDef
):
    pass

DisassociateFacesResponseTypeDef = TypedDict(
    "DisassociateFacesResponseTypeDef",
    {
        "DisassociatedFaces": List["DisassociatedFaceTypeDef"],
        "UnsuccessfulFaceDisassociations": List["UnsuccessfulFaceDisassociationTypeDef"],
        "UserStatus": UserStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociatedFaceTypeDef = TypedDict(
    "DisassociatedFaceTypeDef",
    {
        "FaceId": str,
    },
    total=False,
)

DistributeDatasetEntriesRequestRequestTypeDef = TypedDict(
    "DistributeDatasetEntriesRequestRequestTypeDef",
    {
        "Datasets": List["DistributeDatasetTypeDef"],
    },
)

DistributeDatasetTypeDef = TypedDict(
    "DistributeDatasetTypeDef",
    {
        "Arn": str,
    },
)

DominantColorTypeDef = TypedDict(
    "DominantColorTypeDef",
    {
        "Red": int,
        "Blue": int,
        "Green": int,
        "HexCode": str,
        "CSSColor": str,
        "SimplifiedColor": str,
        "PixelPercent": float,
    },
    total=False,
)

EmotionTypeDef = TypedDict(
    "EmotionTypeDef",
    {
        "Type": EmotionNameType,
        "Confidence": float,
    },
    total=False,
)

EquipmentDetectionTypeDef = TypedDict(
    "EquipmentDetectionTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
        "Confidence": float,
        "Type": ProtectiveEquipmentTypeType,
        "CoversBodyPart": "CoversBodyPartTypeDef",
    },
    total=False,
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "F1Score": float,
        "Summary": "SummaryTypeDef",
    },
    total=False,
)

EyeDirectionTypeDef = TypedDict(
    "EyeDirectionTypeDef",
    {
        "Yaw": float,
        "Pitch": float,
        "Confidence": float,
    },
    total=False,
)

EyeOpenTypeDef = TypedDict(
    "EyeOpenTypeDef",
    {
        "Value": bool,
        "Confidence": float,
    },
    total=False,
)

EyeglassesTypeDef = TypedDict(
    "EyeglassesTypeDef",
    {
        "Value": bool,
        "Confidence": float,
    },
    total=False,
)

FaceDetailTypeDef = TypedDict(
    "FaceDetailTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
        "AgeRange": "AgeRangeTypeDef",
        "Smile": "SmileTypeDef",
        "Eyeglasses": "EyeglassesTypeDef",
        "Sunglasses": "SunglassesTypeDef",
        "Gender": "GenderTypeDef",
        "Beard": "BeardTypeDef",
        "Mustache": "MustacheTypeDef",
        "EyesOpen": "EyeOpenTypeDef",
        "MouthOpen": "MouthOpenTypeDef",
        "Emotions": List["EmotionTypeDef"],
        "Landmarks": List["LandmarkTypeDef"],
        "Pose": "PoseTypeDef",
        "Quality": "ImageQualityTypeDef",
        "Confidence": float,
        "FaceOccluded": "FaceOccludedTypeDef",
        "EyeDirection": "EyeDirectionTypeDef",
    },
    total=False,
)

FaceDetectionTypeDef = TypedDict(
    "FaceDetectionTypeDef",
    {
        "Timestamp": int,
        "Face": "FaceDetailTypeDef",
    },
    total=False,
)

FaceMatchTypeDef = TypedDict(
    "FaceMatchTypeDef",
    {
        "Similarity": float,
        "Face": "FaceTypeDef",
    },
    total=False,
)

FaceOccludedTypeDef = TypedDict(
    "FaceOccludedTypeDef",
    {
        "Value": bool,
        "Confidence": float,
    },
    total=False,
)

FaceRecordTypeDef = TypedDict(
    "FaceRecordTypeDef",
    {
        "Face": "FaceTypeDef",
        "FaceDetail": "FaceDetailTypeDef",
    },
    total=False,
)

FaceSearchSettingsTypeDef = TypedDict(
    "FaceSearchSettingsTypeDef",
    {
        "CollectionId": str,
        "FaceMatchThreshold": float,
    },
    total=False,
)

FaceTypeDef = TypedDict(
    "FaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": "BoundingBoxTypeDef",
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": float,
        "IndexFacesModelVersion": str,
        "UserId": str,
    },
    total=False,
)

GenderTypeDef = TypedDict(
    "GenderTypeDef",
    {
        "Value": GenderTypeType,
        "Confidence": float,
    },
    total=False,
)

GeneralLabelsSettingsTypeDef = TypedDict(
    "GeneralLabelsSettingsTypeDef",
    {
        "LabelInclusionFilters": List[str],
        "LabelExclusionFilters": List[str],
        "LabelCategoryInclusionFilters": List[str],
        "LabelCategoryExclusionFilters": List[str],
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

GetCelebrityInfoRequestRequestTypeDef = TypedDict(
    "GetCelebrityInfoRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetCelebrityInfoResponseTypeDef = TypedDict(
    "GetCelebrityInfoResponseTypeDef",
    {
        "Urls": List[str],
        "Name": str,
        "KnownGender": "KnownGenderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCelebrityRecognitionRequestRequestTypeDef = TypedDict(
    "_RequiredGetCelebrityRecognitionRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetCelebrityRecognitionRequestRequestTypeDef = TypedDict(
    "_OptionalGetCelebrityRecognitionRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SortBy": CelebrityRecognitionSortByType,
    },
    total=False,
)

class GetCelebrityRecognitionRequestRequestTypeDef(
    _RequiredGetCelebrityRecognitionRequestRequestTypeDef,
    _OptionalGetCelebrityRecognitionRequestRequestTypeDef,
):
    pass

GetCelebrityRecognitionResponseTypeDef = TypedDict(
    "GetCelebrityRecognitionResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Celebrities": List["CelebrityRecognitionTypeDef"],
        "JobId": str,
        "Video": "VideoTypeDef",
        "JobTag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContentModerationRequestMetadataTypeDef = TypedDict(
    "GetContentModerationRequestMetadataTypeDef",
    {
        "SortBy": ContentModerationSortByType,
        "AggregateBy": ContentModerationAggregateByType,
    },
    total=False,
)

_RequiredGetContentModerationRequestRequestTypeDef = TypedDict(
    "_RequiredGetContentModerationRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetContentModerationRequestRequestTypeDef = TypedDict(
    "_OptionalGetContentModerationRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SortBy": ContentModerationSortByType,
        "AggregateBy": ContentModerationAggregateByType,
    },
    total=False,
)

class GetContentModerationRequestRequestTypeDef(
    _RequiredGetContentModerationRequestRequestTypeDef,
    _OptionalGetContentModerationRequestRequestTypeDef,
):
    pass

GetContentModerationResponseTypeDef = TypedDict(
    "GetContentModerationResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "ModerationLabels": List["ContentModerationDetectionTypeDef"],
        "NextToken": str,
        "ModerationModelVersion": str,
        "JobId": str,
        "Video": "VideoTypeDef",
        "JobTag": str,
        "GetRequestMetadata": "GetContentModerationRequestMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFaceDetectionRequestRequestTypeDef = TypedDict(
    "_RequiredGetFaceDetectionRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetFaceDetectionRequestRequestTypeDef = TypedDict(
    "_OptionalGetFaceDetectionRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetFaceDetectionRequestRequestTypeDef(
    _RequiredGetFaceDetectionRequestRequestTypeDef, _OptionalGetFaceDetectionRequestRequestTypeDef
):
    pass

GetFaceDetectionResponseTypeDef = TypedDict(
    "GetFaceDetectionResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Faces": List["FaceDetectionTypeDef"],
        "JobId": str,
        "Video": "VideoTypeDef",
        "JobTag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFaceLivenessSessionResultsRequestRequestTypeDef = TypedDict(
    "GetFaceLivenessSessionResultsRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)

GetFaceLivenessSessionResultsResponseTypeDef = TypedDict(
    "GetFaceLivenessSessionResultsResponseTypeDef",
    {
        "SessionId": str,
        "Status": LivenessSessionStatusType,
        "Confidence": float,
        "ReferenceImage": "AuditImageTypeDef",
        "AuditImages": List["AuditImageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFaceSearchRequestRequestTypeDef = TypedDict(
    "_RequiredGetFaceSearchRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetFaceSearchRequestRequestTypeDef = TypedDict(
    "_OptionalGetFaceSearchRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SortBy": FaceSearchSortByType,
    },
    total=False,
)

class GetFaceSearchRequestRequestTypeDef(
    _RequiredGetFaceSearchRequestRequestTypeDef, _OptionalGetFaceSearchRequestRequestTypeDef
):
    pass

GetFaceSearchResponseTypeDef = TypedDict(
    "GetFaceSearchResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "NextToken": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "Persons": List["PersonMatchTypeDef"],
        "JobId": str,
        "Video": "VideoTypeDef",
        "JobTag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLabelDetectionRequestMetadataTypeDef = TypedDict(
    "GetLabelDetectionRequestMetadataTypeDef",
    {
        "SortBy": LabelDetectionSortByType,
        "AggregateBy": LabelDetectionAggregateByType,
    },
    total=False,
)

_RequiredGetLabelDetectionRequestRequestTypeDef = TypedDict(
    "_RequiredGetLabelDetectionRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetLabelDetectionRequestRequestTypeDef = TypedDict(
    "_OptionalGetLabelDetectionRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SortBy": LabelDetectionSortByType,
        "AggregateBy": LabelDetectionAggregateByType,
    },
    total=False,
)

class GetLabelDetectionRequestRequestTypeDef(
    _RequiredGetLabelDetectionRequestRequestTypeDef, _OptionalGetLabelDetectionRequestRequestTypeDef
):
    pass

GetLabelDetectionResponseTypeDef = TypedDict(
    "GetLabelDetectionResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Labels": List["LabelDetectionTypeDef"],
        "LabelModelVersion": str,
        "JobId": str,
        "Video": "VideoTypeDef",
        "JobTag": str,
        "GetRequestMetadata": "GetLabelDetectionRequestMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMediaAnalysisJobRequestRequestTypeDef = TypedDict(
    "GetMediaAnalysisJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

GetMediaAnalysisJobResponseTypeDef = TypedDict(
    "GetMediaAnalysisJobResponseTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "OperationsConfig": "MediaAnalysisOperationsConfigTypeDef",
        "Status": MediaAnalysisJobStatusType,
        "FailureDetails": "MediaAnalysisJobFailureDetailsTypeDef",
        "CreationTimestamp": datetime,
        "CompletionTimestamp": datetime,
        "Input": "MediaAnalysisInputTypeDef",
        "OutputConfig": "MediaAnalysisOutputConfigTypeDef",
        "KmsKeyId": str,
        "Results": "MediaAnalysisResultsTypeDef",
        "ManifestSummary": "MediaAnalysisManifestSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPersonTrackingRequestRequestTypeDef = TypedDict(
    "_RequiredGetPersonTrackingRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetPersonTrackingRequestRequestTypeDef = TypedDict(
    "_OptionalGetPersonTrackingRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SortBy": PersonTrackingSortByType,
    },
    total=False,
)

class GetPersonTrackingRequestRequestTypeDef(
    _RequiredGetPersonTrackingRequestRequestTypeDef, _OptionalGetPersonTrackingRequestRequestTypeDef
):
    pass

GetPersonTrackingResponseTypeDef = TypedDict(
    "GetPersonTrackingResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Persons": List["PersonDetectionTypeDef"],
        "JobId": str,
        "Video": "VideoTypeDef",
        "JobTag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSegmentDetectionRequestRequestTypeDef = TypedDict(
    "_RequiredGetSegmentDetectionRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetSegmentDetectionRequestRequestTypeDef = TypedDict(
    "_OptionalGetSegmentDetectionRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetSegmentDetectionRequestRequestTypeDef(
    _RequiredGetSegmentDetectionRequestRequestTypeDef,
    _OptionalGetSegmentDetectionRequestRequestTypeDef,
):
    pass

GetSegmentDetectionResponseTypeDef = TypedDict(
    "GetSegmentDetectionResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": List["VideoMetadataTypeDef"],
        "AudioMetadata": List["AudioMetadataTypeDef"],
        "NextToken": str,
        "Segments": List["SegmentDetectionTypeDef"],
        "SelectedSegmentTypes": List["SegmentTypeInfoTypeDef"],
        "JobId": str,
        "Video": "VideoTypeDef",
        "JobTag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTextDetectionRequestRequestTypeDef = TypedDict(
    "_RequiredGetTextDetectionRequestRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetTextDetectionRequestRequestTypeDef = TypedDict(
    "_OptionalGetTextDetectionRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetTextDetectionRequestRequestTypeDef(
    _RequiredGetTextDetectionRequestRequestTypeDef, _OptionalGetTextDetectionRequestRequestTypeDef
):
    pass

GetTextDetectionResponseTypeDef = TypedDict(
    "GetTextDetectionResponseTypeDef",
    {
        "JobStatus": VideoJobStatusType,
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "TextDetections": List["TextDetectionResultTypeDef"],
        "NextToken": str,
        "TextModelVersion": str,
        "JobId": str,
        "Video": "VideoTypeDef",
        "JobTag": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroundTruthManifestTypeDef = TypedDict(
    "GroundTruthManifestTypeDef",
    {
        "S3Object": "S3ObjectTypeDef",
    },
    total=False,
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

ImageQualityTypeDef = TypedDict(
    "ImageQualityTypeDef",
    {
        "Brightness": float,
        "Sharpness": float,
    },
    total=False,
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "Bytes": Union[bytes, IO[bytes], StreamingBody],
        "S3Object": "S3ObjectTypeDef",
    },
    total=False,
)

_RequiredIndexFacesRequestRequestTypeDef = TypedDict(
    "_RequiredIndexFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
        "Image": "ImageTypeDef",
    },
)
_OptionalIndexFacesRequestRequestTypeDef = TypedDict(
    "_OptionalIndexFacesRequestRequestTypeDef",
    {
        "ExternalImageId": str,
        "DetectionAttributes": List[AttributeType],
        "MaxFaces": int,
        "QualityFilter": QualityFilterType,
    },
    total=False,
)

class IndexFacesRequestRequestTypeDef(
    _RequiredIndexFacesRequestRequestTypeDef, _OptionalIndexFacesRequestRequestTypeDef
):
    pass

IndexFacesResponseTypeDef = TypedDict(
    "IndexFacesResponseTypeDef",
    {
        "FaceRecords": List["FaceRecordTypeDef"],
        "OrientationCorrection": OrientationCorrectionType,
        "FaceModelVersion": str,
        "UnindexedFaces": List["UnindexedFaceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
        "Confidence": float,
        "DominantColors": List["DominantColorTypeDef"],
    },
    total=False,
)

KinesisDataStreamTypeDef = TypedDict(
    "KinesisDataStreamTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

KinesisVideoStreamStartSelectorTypeDef = TypedDict(
    "KinesisVideoStreamStartSelectorTypeDef",
    {
        "ProducerTimestamp": int,
        "FragmentNumber": str,
    },
    total=False,
)

KinesisVideoStreamTypeDef = TypedDict(
    "KinesisVideoStreamTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

KnownGenderTypeDef = TypedDict(
    "KnownGenderTypeDef",
    {
        "Type": KnownGenderTypeType,
    },
    total=False,
)

LabelAliasTypeDef = TypedDict(
    "LabelAliasTypeDef",
    {
        "Name": str,
    },
    total=False,
)

LabelCategoryTypeDef = TypedDict(
    "LabelCategoryTypeDef",
    {
        "Name": str,
    },
    total=False,
)

LabelDetectionSettingsTypeDef = TypedDict(
    "LabelDetectionSettingsTypeDef",
    {
        "GeneralLabels": "GeneralLabelsSettingsTypeDef",
    },
    total=False,
)

LabelDetectionTypeDef = TypedDict(
    "LabelDetectionTypeDef",
    {
        "Timestamp": int,
        "Label": "LabelTypeDef",
        "StartTimestampMillis": int,
        "EndTimestampMillis": int,
        "DurationMillis": int,
    },
    total=False,
)

LabelTypeDef = TypedDict(
    "LabelTypeDef",
    {
        "Name": str,
        "Confidence": float,
        "Instances": List["InstanceTypeDef"],
        "Parents": List["ParentTypeDef"],
        "Aliases": List["LabelAliasTypeDef"],
        "Categories": List["LabelCategoryTypeDef"],
    },
    total=False,
)

LandmarkTypeDef = TypedDict(
    "LandmarkTypeDef",
    {
        "Type": LandmarkTypeType,
        "X": float,
        "Y": float,
    },
    total=False,
)

ListCollectionsRequestRequestTypeDef = TypedDict(
    "ListCollectionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListCollectionsResponseTypeDef = TypedDict(
    "ListCollectionsResponseTypeDef",
    {
        "CollectionIds": List[str],
        "NextToken": str,
        "FaceModelVersions": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDatasetEntriesRequestRequestTypeDef = TypedDict(
    "_RequiredListDatasetEntriesRequestRequestTypeDef",
    {
        "DatasetArn": str,
    },
)
_OptionalListDatasetEntriesRequestRequestTypeDef = TypedDict(
    "_OptionalListDatasetEntriesRequestRequestTypeDef",
    {
        "ContainsLabels": List[str],
        "Labeled": bool,
        "SourceRefContains": str,
        "HasErrors": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDatasetEntriesRequestRequestTypeDef(
    _RequiredListDatasetEntriesRequestRequestTypeDef,
    _OptionalListDatasetEntriesRequestRequestTypeDef,
):
    pass

ListDatasetEntriesResponseTypeDef = TypedDict(
    "ListDatasetEntriesResponseTypeDef",
    {
        "DatasetEntries": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDatasetLabelsRequestRequestTypeDef = TypedDict(
    "_RequiredListDatasetLabelsRequestRequestTypeDef",
    {
        "DatasetArn": str,
    },
)
_OptionalListDatasetLabelsRequestRequestTypeDef = TypedDict(
    "_OptionalListDatasetLabelsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDatasetLabelsRequestRequestTypeDef(
    _RequiredListDatasetLabelsRequestRequestTypeDef, _OptionalListDatasetLabelsRequestRequestTypeDef
):
    pass

ListDatasetLabelsResponseTypeDef = TypedDict(
    "ListDatasetLabelsResponseTypeDef",
    {
        "DatasetLabelDescriptions": List["DatasetLabelDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFacesRequestRequestTypeDef = TypedDict(
    "_RequiredListFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
    },
)
_OptionalListFacesRequestRequestTypeDef = TypedDict(
    "_OptionalListFacesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "UserId": str,
        "FaceIds": List[str],
    },
    total=False,
)

class ListFacesRequestRequestTypeDef(
    _RequiredListFacesRequestRequestTypeDef, _OptionalListFacesRequestRequestTypeDef
):
    pass

ListFacesResponseTypeDef = TypedDict(
    "ListFacesResponseTypeDef",
    {
        "Faces": List["FaceTypeDef"],
        "NextToken": str,
        "FaceModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMediaAnalysisJobsRequestRequestTypeDef = TypedDict(
    "ListMediaAnalysisJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMediaAnalysisJobsResponseTypeDef = TypedDict(
    "ListMediaAnalysisJobsResponseTypeDef",
    {
        "NextToken": str,
        "MediaAnalysisJobs": List["MediaAnalysisJobDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProjectPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredListProjectPoliciesRequestRequestTypeDef",
    {
        "ProjectArn": str,
    },
)
_OptionalListProjectPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalListProjectPoliciesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListProjectPoliciesRequestRequestTypeDef(
    _RequiredListProjectPoliciesRequestRequestTypeDef,
    _OptionalListProjectPoliciesRequestRequestTypeDef,
):
    pass

ListProjectPoliciesResponseTypeDef = TypedDict(
    "ListProjectPoliciesResponseTypeDef",
    {
        "ProjectPolicies": List["ProjectPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamProcessorsRequestRequestTypeDef = TypedDict(
    "ListStreamProcessorsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListStreamProcessorsResponseTypeDef = TypedDict(
    "ListStreamProcessorsResponseTypeDef",
    {
        "NextToken": str,
        "StreamProcessors": List["StreamProcessorTypeDef"],
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
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "CollectionId": str,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLivenessOutputConfigTypeDef = TypedDict(
    "_RequiredLivenessOutputConfigTypeDef",
    {
        "S3Bucket": str,
    },
)
_OptionalLivenessOutputConfigTypeDef = TypedDict(
    "_OptionalLivenessOutputConfigTypeDef",
    {
        "S3KeyPrefix": str,
    },
    total=False,
)

class LivenessOutputConfigTypeDef(
    _RequiredLivenessOutputConfigTypeDef, _OptionalLivenessOutputConfigTypeDef
):
    pass

MatchedUserTypeDef = TypedDict(
    "MatchedUserTypeDef",
    {
        "UserId": str,
        "UserStatus": UserStatusType,
    },
    total=False,
)

MediaAnalysisDetectModerationLabelsConfigTypeDef = TypedDict(
    "MediaAnalysisDetectModerationLabelsConfigTypeDef",
    {
        "MinConfidence": float,
        "ProjectVersion": str,
    },
    total=False,
)

MediaAnalysisInputTypeDef = TypedDict(
    "MediaAnalysisInputTypeDef",
    {
        "S3Object": "S3ObjectTypeDef",
    },
)

_RequiredMediaAnalysisJobDescriptionTypeDef = TypedDict(
    "_RequiredMediaAnalysisJobDescriptionTypeDef",
    {
        "JobId": str,
        "OperationsConfig": "MediaAnalysisOperationsConfigTypeDef",
        "Status": MediaAnalysisJobStatusType,
        "CreationTimestamp": datetime,
        "Input": "MediaAnalysisInputTypeDef",
        "OutputConfig": "MediaAnalysisOutputConfigTypeDef",
    },
)
_OptionalMediaAnalysisJobDescriptionTypeDef = TypedDict(
    "_OptionalMediaAnalysisJobDescriptionTypeDef",
    {
        "JobName": str,
        "FailureDetails": "MediaAnalysisJobFailureDetailsTypeDef",
        "CompletionTimestamp": datetime,
        "KmsKeyId": str,
        "Results": "MediaAnalysisResultsTypeDef",
        "ManifestSummary": "MediaAnalysisManifestSummaryTypeDef",
    },
    total=False,
)

class MediaAnalysisJobDescriptionTypeDef(
    _RequiredMediaAnalysisJobDescriptionTypeDef, _OptionalMediaAnalysisJobDescriptionTypeDef
):
    pass

MediaAnalysisJobFailureDetailsTypeDef = TypedDict(
    "MediaAnalysisJobFailureDetailsTypeDef",
    {
        "Code": MediaAnalysisJobFailureCodeType,
        "Message": str,
    },
    total=False,
)

MediaAnalysisManifestSummaryTypeDef = TypedDict(
    "MediaAnalysisManifestSummaryTypeDef",
    {
        "S3Object": "S3ObjectTypeDef",
    },
    total=False,
)

MediaAnalysisModelVersionsTypeDef = TypedDict(
    "MediaAnalysisModelVersionsTypeDef",
    {
        "Moderation": str,
    },
    total=False,
)

MediaAnalysisOperationsConfigTypeDef = TypedDict(
    "MediaAnalysisOperationsConfigTypeDef",
    {
        "DetectModerationLabels": "MediaAnalysisDetectModerationLabelsConfigTypeDef",
    },
    total=False,
)

_RequiredMediaAnalysisOutputConfigTypeDef = TypedDict(
    "_RequiredMediaAnalysisOutputConfigTypeDef",
    {
        "S3Bucket": str,
    },
)
_OptionalMediaAnalysisOutputConfigTypeDef = TypedDict(
    "_OptionalMediaAnalysisOutputConfigTypeDef",
    {
        "S3KeyPrefix": str,
    },
    total=False,
)

class MediaAnalysisOutputConfigTypeDef(
    _RequiredMediaAnalysisOutputConfigTypeDef, _OptionalMediaAnalysisOutputConfigTypeDef
):
    pass

MediaAnalysisResultsTypeDef = TypedDict(
    "MediaAnalysisResultsTypeDef",
    {
        "S3Object": "S3ObjectTypeDef",
        "ModelVersions": "MediaAnalysisModelVersionsTypeDef",
    },
    total=False,
)

ModerationLabelTypeDef = TypedDict(
    "ModerationLabelTypeDef",
    {
        "Confidence": float,
        "Name": str,
        "ParentName": str,
        "TaxonomyLevel": int,
    },
    total=False,
)

MouthOpenTypeDef = TypedDict(
    "MouthOpenTypeDef",
    {
        "Value": bool,
        "Confidence": float,
    },
    total=False,
)

MustacheTypeDef = TypedDict(
    "MustacheTypeDef",
    {
        "Value": bool,
        "Confidence": float,
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

OutputConfigTypeDef = TypedDict(
    "OutputConfigTypeDef",
    {
        "S3Bucket": str,
        "S3KeyPrefix": str,
    },
    total=False,
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

ParentTypeDef = TypedDict(
    "ParentTypeDef",
    {
        "Name": str,
    },
    total=False,
)

PersonDetailTypeDef = TypedDict(
    "PersonDetailTypeDef",
    {
        "Index": int,
        "BoundingBox": "BoundingBoxTypeDef",
        "Face": "FaceDetailTypeDef",
    },
    total=False,
)

PersonDetectionTypeDef = TypedDict(
    "PersonDetectionTypeDef",
    {
        "Timestamp": int,
        "Person": "PersonDetailTypeDef",
    },
    total=False,
)

PersonMatchTypeDef = TypedDict(
    "PersonMatchTypeDef",
    {
        "Timestamp": int,
        "Person": "PersonDetailTypeDef",
        "FaceMatches": List["FaceMatchTypeDef"],
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

PoseTypeDef = TypedDict(
    "PoseTypeDef",
    {
        "Roll": float,
        "Yaw": float,
        "Pitch": float,
    },
    total=False,
)

ProjectDescriptionTypeDef = TypedDict(
    "ProjectDescriptionTypeDef",
    {
        "ProjectArn": str,
        "CreationTimestamp": datetime,
        "Status": ProjectStatusType,
        "Datasets": List["DatasetMetadataTypeDef"],
        "Feature": CustomizationFeatureType,
        "AutoUpdate": ProjectAutoUpdateType,
    },
    total=False,
)

ProjectPolicyTypeDef = TypedDict(
    "ProjectPolicyTypeDef",
    {
        "ProjectArn": str,
        "PolicyName": str,
        "PolicyRevisionId": str,
        "PolicyDocument": str,
        "CreationTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

ProjectVersionDescriptionTypeDef = TypedDict(
    "ProjectVersionDescriptionTypeDef",
    {
        "ProjectVersionArn": str,
        "CreationTimestamp": datetime,
        "MinInferenceUnits": int,
        "Status": ProjectVersionStatusType,
        "StatusMessage": str,
        "BillableTrainingTimeInSeconds": int,
        "TrainingEndTimestamp": datetime,
        "OutputConfig": "OutputConfigTypeDef",
        "TrainingDataResult": "TrainingDataResultTypeDef",
        "TestingDataResult": "TestingDataResultTypeDef",
        "EvaluationResult": "EvaluationResultTypeDef",
        "ManifestSummary": "GroundTruthManifestTypeDef",
        "KmsKeyId": str,
        "MaxInferenceUnits": int,
        "SourceProjectVersionArn": str,
        "VersionDescription": str,
        "Feature": CustomizationFeatureType,
        "BaseModelVersion": str,
        "FeatureConfig": "CustomizationFeatureConfigTypeDef",
    },
    total=False,
)

ProtectiveEquipmentBodyPartTypeDef = TypedDict(
    "ProtectiveEquipmentBodyPartTypeDef",
    {
        "Name": BodyPartType,
        "Confidence": float,
        "EquipmentDetections": List["EquipmentDetectionTypeDef"],
    },
    total=False,
)

ProtectiveEquipmentPersonTypeDef = TypedDict(
    "ProtectiveEquipmentPersonTypeDef",
    {
        "BodyParts": List["ProtectiveEquipmentBodyPartTypeDef"],
        "BoundingBox": "BoundingBoxTypeDef",
        "Confidence": float,
        "Id": int,
    },
    total=False,
)

ProtectiveEquipmentSummarizationAttributesTypeDef = TypedDict(
    "ProtectiveEquipmentSummarizationAttributesTypeDef",
    {
        "MinConfidence": float,
        "RequiredEquipmentTypes": List[ProtectiveEquipmentTypeType],
    },
)

ProtectiveEquipmentSummaryTypeDef = TypedDict(
    "ProtectiveEquipmentSummaryTypeDef",
    {
        "PersonsWithRequiredEquipment": List[int],
        "PersonsWithoutRequiredEquipment": List[int],
        "PersonsIndeterminate": List[int],
    },
    total=False,
)

_RequiredPutProjectPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutProjectPolicyRequestRequestTypeDef",
    {
        "ProjectArn": str,
        "PolicyName": str,
        "PolicyDocument": str,
    },
)
_OptionalPutProjectPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutProjectPolicyRequestRequestTypeDef",
    {
        "PolicyRevisionId": str,
    },
    total=False,
)

class PutProjectPolicyRequestRequestTypeDef(
    _RequiredPutProjectPolicyRequestRequestTypeDef, _OptionalPutProjectPolicyRequestRequestTypeDef
):
    pass

PutProjectPolicyResponseTypeDef = TypedDict(
    "PutProjectPolicyResponseTypeDef",
    {
        "PolicyRevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecognizeCelebritiesRequestRequestTypeDef = TypedDict(
    "RecognizeCelebritiesRequestRequestTypeDef",
    {
        "Image": "ImageTypeDef",
    },
)

RecognizeCelebritiesResponseTypeDef = TypedDict(
    "RecognizeCelebritiesResponseTypeDef",
    {
        "CelebrityFaces": List["CelebrityTypeDef"],
        "UnrecognizedFaces": List["ComparedFaceTypeDef"],
        "OrientationCorrection": OrientationCorrectionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegionOfInterestTypeDef = TypedDict(
    "RegionOfInterestTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
        "Polygon": List["PointTypeDef"],
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

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "Bucket": str,
        "KeyPrefix": str,
    },
    total=False,
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

_RequiredSearchFacesByImageRequestRequestTypeDef = TypedDict(
    "_RequiredSearchFacesByImageRequestRequestTypeDef",
    {
        "CollectionId": str,
        "Image": "ImageTypeDef",
    },
)
_OptionalSearchFacesByImageRequestRequestTypeDef = TypedDict(
    "_OptionalSearchFacesByImageRequestRequestTypeDef",
    {
        "MaxFaces": int,
        "FaceMatchThreshold": float,
        "QualityFilter": QualityFilterType,
    },
    total=False,
)

class SearchFacesByImageRequestRequestTypeDef(
    _RequiredSearchFacesByImageRequestRequestTypeDef,
    _OptionalSearchFacesByImageRequestRequestTypeDef,
):
    pass

SearchFacesByImageResponseTypeDef = TypedDict(
    "SearchFacesByImageResponseTypeDef",
    {
        "SearchedFaceBoundingBox": "BoundingBoxTypeDef",
        "SearchedFaceConfidence": float,
        "FaceMatches": List["FaceMatchTypeDef"],
        "FaceModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchFacesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchFacesRequestRequestTypeDef",
    {
        "CollectionId": str,
        "FaceId": str,
    },
)
_OptionalSearchFacesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchFacesRequestRequestTypeDef",
    {
        "MaxFaces": int,
        "FaceMatchThreshold": float,
    },
    total=False,
)

class SearchFacesRequestRequestTypeDef(
    _RequiredSearchFacesRequestRequestTypeDef, _OptionalSearchFacesRequestRequestTypeDef
):
    pass

SearchFacesResponseTypeDef = TypedDict(
    "SearchFacesResponseTypeDef",
    {
        "SearchedFaceId": str,
        "FaceMatches": List["FaceMatchTypeDef"],
        "FaceModelVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchUsersByImageRequestRequestTypeDef = TypedDict(
    "_RequiredSearchUsersByImageRequestRequestTypeDef",
    {
        "CollectionId": str,
        "Image": "ImageTypeDef",
    },
)
_OptionalSearchUsersByImageRequestRequestTypeDef = TypedDict(
    "_OptionalSearchUsersByImageRequestRequestTypeDef",
    {
        "UserMatchThreshold": float,
        "MaxUsers": int,
        "QualityFilter": QualityFilterType,
    },
    total=False,
)

class SearchUsersByImageRequestRequestTypeDef(
    _RequiredSearchUsersByImageRequestRequestTypeDef,
    _OptionalSearchUsersByImageRequestRequestTypeDef,
):
    pass

SearchUsersByImageResponseTypeDef = TypedDict(
    "SearchUsersByImageResponseTypeDef",
    {
        "UserMatches": List["UserMatchTypeDef"],
        "FaceModelVersion": str,
        "SearchedFace": "SearchedFaceDetailsTypeDef",
        "UnsearchedFaces": List["UnsearchedFaceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchUsersRequestRequestTypeDef = TypedDict(
    "_RequiredSearchUsersRequestRequestTypeDef",
    {
        "CollectionId": str,
    },
)
_OptionalSearchUsersRequestRequestTypeDef = TypedDict(
    "_OptionalSearchUsersRequestRequestTypeDef",
    {
        "UserId": str,
        "FaceId": str,
        "UserMatchThreshold": float,
        "MaxUsers": int,
    },
    total=False,
)

class SearchUsersRequestRequestTypeDef(
    _RequiredSearchUsersRequestRequestTypeDef, _OptionalSearchUsersRequestRequestTypeDef
):
    pass

SearchUsersResponseTypeDef = TypedDict(
    "SearchUsersResponseTypeDef",
    {
        "UserMatches": List["UserMatchTypeDef"],
        "FaceModelVersion": str,
        "SearchedFace": "SearchedFaceTypeDef",
        "SearchedUser": "SearchedUserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchedFaceDetailsTypeDef = TypedDict(
    "SearchedFaceDetailsTypeDef",
    {
        "FaceDetail": "FaceDetailTypeDef",
    },
    total=False,
)

SearchedFaceTypeDef = TypedDict(
    "SearchedFaceTypeDef",
    {
        "FaceId": str,
    },
    total=False,
)

SearchedUserTypeDef = TypedDict(
    "SearchedUserTypeDef",
    {
        "UserId": str,
    },
    total=False,
)

SegmentDetectionTypeDef = TypedDict(
    "SegmentDetectionTypeDef",
    {
        "Type": SegmentTypeType,
        "StartTimestampMillis": int,
        "EndTimestampMillis": int,
        "DurationMillis": int,
        "StartTimecodeSMPTE": str,
        "EndTimecodeSMPTE": str,
        "DurationSMPTE": str,
        "TechnicalCueSegment": "TechnicalCueSegmentTypeDef",
        "ShotSegment": "ShotSegmentTypeDef",
        "StartFrameNumber": int,
        "EndFrameNumber": int,
        "DurationFrames": int,
    },
    total=False,
)

SegmentTypeInfoTypeDef = TypedDict(
    "SegmentTypeInfoTypeDef",
    {
        "Type": SegmentTypeType,
        "ModelVersion": str,
    },
    total=False,
)

ShotSegmentTypeDef = TypedDict(
    "ShotSegmentTypeDef",
    {
        "Index": int,
        "Confidence": float,
    },
    total=False,
)

SmileTypeDef = TypedDict(
    "SmileTypeDef",
    {
        "Value": bool,
        "Confidence": float,
    },
    total=False,
)

_RequiredStartCelebrityRecognitionRequestRequestTypeDef = TypedDict(
    "_RequiredStartCelebrityRecognitionRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
    },
)
_OptionalStartCelebrityRecognitionRequestRequestTypeDef = TypedDict(
    "_OptionalStartCelebrityRecognitionRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "JobTag": str,
    },
    total=False,
)

class StartCelebrityRecognitionRequestRequestTypeDef(
    _RequiredStartCelebrityRecognitionRequestRequestTypeDef,
    _OptionalStartCelebrityRecognitionRequestRequestTypeDef,
):
    pass

StartCelebrityRecognitionResponseTypeDef = TypedDict(
    "StartCelebrityRecognitionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartContentModerationRequestRequestTypeDef = TypedDict(
    "_RequiredStartContentModerationRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
    },
)
_OptionalStartContentModerationRequestRequestTypeDef = TypedDict(
    "_OptionalStartContentModerationRequestRequestTypeDef",
    {
        "MinConfidence": float,
        "ClientRequestToken": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "JobTag": str,
    },
    total=False,
)

class StartContentModerationRequestRequestTypeDef(
    _RequiredStartContentModerationRequestRequestTypeDef,
    _OptionalStartContentModerationRequestRequestTypeDef,
):
    pass

StartContentModerationResponseTypeDef = TypedDict(
    "StartContentModerationResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartFaceDetectionRequestRequestTypeDef = TypedDict(
    "_RequiredStartFaceDetectionRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
    },
)
_OptionalStartFaceDetectionRequestRequestTypeDef = TypedDict(
    "_OptionalStartFaceDetectionRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "FaceAttributes": FaceAttributesType,
        "JobTag": str,
    },
    total=False,
)

class StartFaceDetectionRequestRequestTypeDef(
    _RequiredStartFaceDetectionRequestRequestTypeDef,
    _OptionalStartFaceDetectionRequestRequestTypeDef,
):
    pass

StartFaceDetectionResponseTypeDef = TypedDict(
    "StartFaceDetectionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartFaceSearchRequestRequestTypeDef = TypedDict(
    "_RequiredStartFaceSearchRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
        "CollectionId": str,
    },
)
_OptionalStartFaceSearchRequestRequestTypeDef = TypedDict(
    "_OptionalStartFaceSearchRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "FaceMatchThreshold": float,
        "NotificationChannel": "NotificationChannelTypeDef",
        "JobTag": str,
    },
    total=False,
)

class StartFaceSearchRequestRequestTypeDef(
    _RequiredStartFaceSearchRequestRequestTypeDef, _OptionalStartFaceSearchRequestRequestTypeDef
):
    pass

StartFaceSearchResponseTypeDef = TypedDict(
    "StartFaceSearchResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartLabelDetectionRequestRequestTypeDef = TypedDict(
    "_RequiredStartLabelDetectionRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
    },
)
_OptionalStartLabelDetectionRequestRequestTypeDef = TypedDict(
    "_OptionalStartLabelDetectionRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "MinConfidence": float,
        "NotificationChannel": "NotificationChannelTypeDef",
        "JobTag": str,
        "Features": List[Literal["GENERAL_LABELS"]],
        "Settings": "LabelDetectionSettingsTypeDef",
    },
    total=False,
)

class StartLabelDetectionRequestRequestTypeDef(
    _RequiredStartLabelDetectionRequestRequestTypeDef,
    _OptionalStartLabelDetectionRequestRequestTypeDef,
):
    pass

StartLabelDetectionResponseTypeDef = TypedDict(
    "StartLabelDetectionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartMediaAnalysisJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartMediaAnalysisJobRequestRequestTypeDef",
    {
        "OperationsConfig": "MediaAnalysisOperationsConfigTypeDef",
        "Input": "MediaAnalysisInputTypeDef",
        "OutputConfig": "MediaAnalysisOutputConfigTypeDef",
    },
)
_OptionalStartMediaAnalysisJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartMediaAnalysisJobRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "JobName": str,
        "KmsKeyId": str,
    },
    total=False,
)

class StartMediaAnalysisJobRequestRequestTypeDef(
    _RequiredStartMediaAnalysisJobRequestRequestTypeDef,
    _OptionalStartMediaAnalysisJobRequestRequestTypeDef,
):
    pass

StartMediaAnalysisJobResponseTypeDef = TypedDict(
    "StartMediaAnalysisJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartPersonTrackingRequestRequestTypeDef = TypedDict(
    "_RequiredStartPersonTrackingRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
    },
)
_OptionalStartPersonTrackingRequestRequestTypeDef = TypedDict(
    "_OptionalStartPersonTrackingRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "JobTag": str,
    },
    total=False,
)

class StartPersonTrackingRequestRequestTypeDef(
    _RequiredStartPersonTrackingRequestRequestTypeDef,
    _OptionalStartPersonTrackingRequestRequestTypeDef,
):
    pass

StartPersonTrackingResponseTypeDef = TypedDict(
    "StartPersonTrackingResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartProjectVersionRequestRequestTypeDef = TypedDict(
    "_RequiredStartProjectVersionRequestRequestTypeDef",
    {
        "ProjectVersionArn": str,
        "MinInferenceUnits": int,
    },
)
_OptionalStartProjectVersionRequestRequestTypeDef = TypedDict(
    "_OptionalStartProjectVersionRequestRequestTypeDef",
    {
        "MaxInferenceUnits": int,
    },
    total=False,
)

class StartProjectVersionRequestRequestTypeDef(
    _RequiredStartProjectVersionRequestRequestTypeDef,
    _OptionalStartProjectVersionRequestRequestTypeDef,
):
    pass

StartProjectVersionResponseTypeDef = TypedDict(
    "StartProjectVersionResponseTypeDef",
    {
        "Status": ProjectVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartSegmentDetectionFiltersTypeDef = TypedDict(
    "StartSegmentDetectionFiltersTypeDef",
    {
        "TechnicalCueFilter": "StartTechnicalCueDetectionFilterTypeDef",
        "ShotFilter": "StartShotDetectionFilterTypeDef",
    },
    total=False,
)

_RequiredStartSegmentDetectionRequestRequestTypeDef = TypedDict(
    "_RequiredStartSegmentDetectionRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
        "SegmentTypes": List[SegmentTypeType],
    },
)
_OptionalStartSegmentDetectionRequestRequestTypeDef = TypedDict(
    "_OptionalStartSegmentDetectionRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "JobTag": str,
        "Filters": "StartSegmentDetectionFiltersTypeDef",
    },
    total=False,
)

class StartSegmentDetectionRequestRequestTypeDef(
    _RequiredStartSegmentDetectionRequestRequestTypeDef,
    _OptionalStartSegmentDetectionRequestRequestTypeDef,
):
    pass

StartSegmentDetectionResponseTypeDef = TypedDict(
    "StartSegmentDetectionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartShotDetectionFilterTypeDef = TypedDict(
    "StartShotDetectionFilterTypeDef",
    {
        "MinSegmentConfidence": float,
    },
    total=False,
)

_RequiredStartStreamProcessorRequestRequestTypeDef = TypedDict(
    "_RequiredStartStreamProcessorRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalStartStreamProcessorRequestRequestTypeDef = TypedDict(
    "_OptionalStartStreamProcessorRequestRequestTypeDef",
    {
        "StartSelector": "StreamProcessingStartSelectorTypeDef",
        "StopSelector": "StreamProcessingStopSelectorTypeDef",
    },
    total=False,
)

class StartStreamProcessorRequestRequestTypeDef(
    _RequiredStartStreamProcessorRequestRequestTypeDef,
    _OptionalStartStreamProcessorRequestRequestTypeDef,
):
    pass

StartStreamProcessorResponseTypeDef = TypedDict(
    "StartStreamProcessorResponseTypeDef",
    {
        "SessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartTechnicalCueDetectionFilterTypeDef = TypedDict(
    "StartTechnicalCueDetectionFilterTypeDef",
    {
        "MinSegmentConfidence": float,
        "BlackFrame": "BlackFrameTypeDef",
    },
    total=False,
)

StartTextDetectionFiltersTypeDef = TypedDict(
    "StartTextDetectionFiltersTypeDef",
    {
        "WordFilter": "DetectionFilterTypeDef",
        "RegionsOfInterest": List["RegionOfInterestTypeDef"],
    },
    total=False,
)

_RequiredStartTextDetectionRequestRequestTypeDef = TypedDict(
    "_RequiredStartTextDetectionRequestRequestTypeDef",
    {
        "Video": "VideoTypeDef",
    },
)
_OptionalStartTextDetectionRequestRequestTypeDef = TypedDict(
    "_OptionalStartTextDetectionRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NotificationChannel": "NotificationChannelTypeDef",
        "JobTag": str,
        "Filters": "StartTextDetectionFiltersTypeDef",
    },
    total=False,
)

class StartTextDetectionRequestRequestTypeDef(
    _RequiredStartTextDetectionRequestRequestTypeDef,
    _OptionalStartTextDetectionRequestRequestTypeDef,
):
    pass

StartTextDetectionResponseTypeDef = TypedDict(
    "StartTextDetectionResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopProjectVersionRequestRequestTypeDef = TypedDict(
    "StopProjectVersionRequestRequestTypeDef",
    {
        "ProjectVersionArn": str,
    },
)

StopProjectVersionResponseTypeDef = TypedDict(
    "StopProjectVersionResponseTypeDef",
    {
        "Status": ProjectVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopStreamProcessorRequestRequestTypeDef = TypedDict(
    "StopStreamProcessorRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StreamProcessingStartSelectorTypeDef = TypedDict(
    "StreamProcessingStartSelectorTypeDef",
    {
        "KVSStreamStartSelector": "KinesisVideoStreamStartSelectorTypeDef",
    },
    total=False,
)

StreamProcessingStopSelectorTypeDef = TypedDict(
    "StreamProcessingStopSelectorTypeDef",
    {
        "MaxDurationInSeconds": int,
    },
    total=False,
)

StreamProcessorDataSharingPreferenceTypeDef = TypedDict(
    "StreamProcessorDataSharingPreferenceTypeDef",
    {
        "OptIn": bool,
    },
)

StreamProcessorInputTypeDef = TypedDict(
    "StreamProcessorInputTypeDef",
    {
        "KinesisVideoStream": "KinesisVideoStreamTypeDef",
    },
    total=False,
)

StreamProcessorNotificationChannelTypeDef = TypedDict(
    "StreamProcessorNotificationChannelTypeDef",
    {
        "SNSTopicArn": str,
    },
)

StreamProcessorOutputTypeDef = TypedDict(
    "StreamProcessorOutputTypeDef",
    {
        "KinesisDataStream": "KinesisDataStreamTypeDef",
        "S3Destination": "S3DestinationTypeDef",
    },
    total=False,
)

StreamProcessorSettingsForUpdateTypeDef = TypedDict(
    "StreamProcessorSettingsForUpdateTypeDef",
    {
        "ConnectedHomeForUpdate": "ConnectedHomeSettingsForUpdateTypeDef",
    },
    total=False,
)

StreamProcessorSettingsTypeDef = TypedDict(
    "StreamProcessorSettingsTypeDef",
    {
        "FaceSearch": "FaceSearchSettingsTypeDef",
        "ConnectedHome": "ConnectedHomeSettingsTypeDef",
    },
    total=False,
)

StreamProcessorTypeDef = TypedDict(
    "StreamProcessorTypeDef",
    {
        "Name": str,
        "Status": StreamProcessorStatusType,
    },
    total=False,
)

SummaryTypeDef = TypedDict(
    "SummaryTypeDef",
    {
        "S3Object": "S3ObjectTypeDef",
    },
    total=False,
)

SunglassesTypeDef = TypedDict(
    "SunglassesTypeDef",
    {
        "Value": bool,
        "Confidence": float,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TechnicalCueSegmentTypeDef = TypedDict(
    "TechnicalCueSegmentTypeDef",
    {
        "Type": TechnicalCueTypeType,
        "Confidence": float,
    },
    total=False,
)

TestingDataResultTypeDef = TypedDict(
    "TestingDataResultTypeDef",
    {
        "Input": "TestingDataTypeDef",
        "Output": "TestingDataTypeDef",
        "Validation": "ValidationDataTypeDef",
    },
    total=False,
)

TestingDataTypeDef = TypedDict(
    "TestingDataTypeDef",
    {
        "Assets": List["AssetTypeDef"],
        "AutoCreate": bool,
    },
    total=False,
)

TextDetectionResultTypeDef = TypedDict(
    "TextDetectionResultTypeDef",
    {
        "Timestamp": int,
        "TextDetection": "TextDetectionTypeDef",
    },
    total=False,
)

TextDetectionTypeDef = TypedDict(
    "TextDetectionTypeDef",
    {
        "DetectedText": str,
        "Type": TextTypesType,
        "Id": int,
        "ParentId": int,
        "Confidence": float,
        "Geometry": "GeometryTypeDef",
    },
    total=False,
)

TrainingDataResultTypeDef = TypedDict(
    "TrainingDataResultTypeDef",
    {
        "Input": "TrainingDataTypeDef",
        "Output": "TrainingDataTypeDef",
        "Validation": "ValidationDataTypeDef",
    },
    total=False,
)

TrainingDataTypeDef = TypedDict(
    "TrainingDataTypeDef",
    {
        "Assets": List["AssetTypeDef"],
    },
    total=False,
)

UnindexedFaceTypeDef = TypedDict(
    "UnindexedFaceTypeDef",
    {
        "Reasons": List[ReasonType],
        "FaceDetail": "FaceDetailTypeDef",
    },
    total=False,
)

UnsearchedFaceTypeDef = TypedDict(
    "UnsearchedFaceTypeDef",
    {
        "FaceDetails": "FaceDetailTypeDef",
        "Reasons": List[UnsearchedFaceReasonType],
    },
    total=False,
)

UnsuccessfulFaceAssociationTypeDef = TypedDict(
    "UnsuccessfulFaceAssociationTypeDef",
    {
        "FaceId": str,
        "UserId": str,
        "Confidence": float,
        "Reasons": List[UnsuccessfulFaceAssociationReasonType],
    },
    total=False,
)

UnsuccessfulFaceDeletionTypeDef = TypedDict(
    "UnsuccessfulFaceDeletionTypeDef",
    {
        "FaceId": str,
        "UserId": str,
        "Reasons": List[UnsuccessfulFaceDeletionReasonType],
    },
    total=False,
)

UnsuccessfulFaceDisassociationTypeDef = TypedDict(
    "UnsuccessfulFaceDisassociationTypeDef",
    {
        "FaceId": str,
        "UserId": str,
        "Reasons": List[UnsuccessfulFaceDisassociationReasonType],
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

UpdateDatasetEntriesRequestRequestTypeDef = TypedDict(
    "UpdateDatasetEntriesRequestRequestTypeDef",
    {
        "DatasetArn": str,
        "Changes": "DatasetChangesTypeDef",
    },
)

_RequiredUpdateStreamProcessorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateStreamProcessorRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateStreamProcessorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateStreamProcessorRequestRequestTypeDef",
    {
        "SettingsForUpdate": "StreamProcessorSettingsForUpdateTypeDef",
        "RegionsOfInterestForUpdate": List["RegionOfInterestTypeDef"],
        "DataSharingPreferenceForUpdate": "StreamProcessorDataSharingPreferenceTypeDef",
        "ParametersToDelete": List[StreamProcessorParameterToDeleteType],
    },
    total=False,
)

class UpdateStreamProcessorRequestRequestTypeDef(
    _RequiredUpdateStreamProcessorRequestRequestTypeDef,
    _OptionalUpdateStreamProcessorRequestRequestTypeDef,
):
    pass

UserMatchTypeDef = TypedDict(
    "UserMatchTypeDef",
    {
        "Similarity": float,
        "User": "MatchedUserTypeDef",
    },
    total=False,
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "UserId": str,
        "UserStatus": UserStatusType,
    },
    total=False,
)

ValidationDataTypeDef = TypedDict(
    "ValidationDataTypeDef",
    {
        "Assets": List["AssetTypeDef"],
    },
    total=False,
)

VideoMetadataTypeDef = TypedDict(
    "VideoMetadataTypeDef",
    {
        "Codec": str,
        "DurationMillis": int,
        "Format": str,
        "FrameRate": float,
        "FrameHeight": int,
        "FrameWidth": int,
        "ColorRange": VideoColorRangeType,
    },
    total=False,
)

VideoTypeDef = TypedDict(
    "VideoTypeDef",
    {
        "S3Object": "S3ObjectTypeDef",
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
