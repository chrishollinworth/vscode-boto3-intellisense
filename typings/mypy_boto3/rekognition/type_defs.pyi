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
    ContentModerationSortByType,
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
    OrientationCorrectionType,
    PersonTrackingSortByType,
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
    "AudioMetadataTypeDef",
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
    "CopyProjectVersionRequestRequestTypeDef",
    "CopyProjectVersionResponseTypeDef",
    "CoversBodyPartTypeDef",
    "CreateCollectionRequestRequestTypeDef",
    "CreateCollectionResponseTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateProjectVersionRequestRequestTypeDef",
    "CreateProjectVersionResponseTypeDef",
    "CreateStreamProcessorRequestRequestTypeDef",
    "CreateStreamProcessorResponseTypeDef",
    "CustomLabelTypeDef",
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
    "DistributeDatasetEntriesRequestRequestTypeDef",
    "DistributeDatasetTypeDef",
    "DominantColorTypeDef",
    "EmotionTypeDef",
    "EquipmentDetectionTypeDef",
    "EvaluationResultTypeDef",
    "EyeOpenTypeDef",
    "EyeglassesTypeDef",
    "FaceDetailTypeDef",
    "FaceDetectionTypeDef",
    "FaceMatchTypeDef",
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
    "GetContentModerationRequestRequestTypeDef",
    "GetContentModerationResponseTypeDef",
    "GetFaceDetectionRequestRequestTypeDef",
    "GetFaceDetectionResponseTypeDef",
    "GetFaceSearchRequestRequestTypeDef",
    "GetFaceSearchResponseTypeDef",
    "GetLabelDetectionRequestRequestTypeDef",
    "GetLabelDetectionResponseTypeDef",
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
    "ListProjectPoliciesRequestRequestTypeDef",
    "ListProjectPoliciesResponseTypeDef",
    "ListStreamProcessorsRequestRequestTypeDef",
    "ListStreamProcessorsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
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
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatasetEntriesRequestRequestTypeDef",
    "UpdateStreamProcessorRequestRequestTypeDef",
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

CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "ProjectName": str,
    },
)

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

CustomLabelTypeDef = TypedDict(
    "CustomLabelTypeDef",
    {
        "Name": str,
        "Confidence": float,
        "Geometry": "GeometryTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ModerationLabelTypeDef = TypedDict(
    "ModerationLabelTypeDef",
    {
        "Confidence": float,
        "Name": str,
        "ParentName": str,
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
