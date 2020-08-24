"""
Main interface for rekognition service type definitions.

Usage::

    ```python
    from mypy_boto3_rekognition.type_defs import AgeRangeTypeDef

    data: AgeRangeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

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
    "BoundingBoxTypeDef",
    "CelebrityDetailTypeDef",
    "CelebrityRecognitionTypeDef",
    "CelebrityTypeDef",
    "CompareFacesMatchTypeDef",
    "ComparedFaceTypeDef",
    "ComparedSourceImageFaceTypeDef",
    "ContentModerationDetectionTypeDef",
    "CustomLabelTypeDef",
    "DetectionFilterTypeDef",
    "EmotionTypeDef",
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
    "GeometryTypeDef",
    "GroundTruthManifestTypeDef",
    "HumanLoopActivationOutputTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "ImageQualityTypeDef",
    "InstanceTypeDef",
    "KinesisDataStreamTypeDef",
    "KinesisVideoStreamTypeDef",
    "LabelDetectionTypeDef",
    "LabelTypeDef",
    "LandmarkTypeDef",
    "ModerationLabelTypeDef",
    "MouthOpenTypeDef",
    "MustacheTypeDef",
    "OutputConfigTypeDef",
    "ParentTypeDef",
    "PersonDetailTypeDef",
    "PersonDetectionTypeDef",
    "PersonMatchTypeDef",
    "PointTypeDef",
    "PoseTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectVersionDescriptionTypeDef",
    "RegionOfInterestTypeDef",
    "S3ObjectTypeDef",
    "SegmentDetectionTypeDef",
    "SegmentTypeInfoTypeDef",
    "ShotSegmentTypeDef",
    "SmileTypeDef",
    "StartShotDetectionFilterTypeDef",
    "StartTechnicalCueDetectionFilterTypeDef",
    "StreamProcessorInputTypeDef",
    "StreamProcessorOutputTypeDef",
    "StreamProcessorSettingsTypeDef",
    "StreamProcessorTypeDef",
    "SummaryTypeDef",
    "SunglassesTypeDef",
    "TechnicalCueSegmentTypeDef",
    "TestingDataResultTypeDef",
    "TestingDataTypeDef",
    "TextDetectionResultTypeDef",
    "TextDetectionTypeDef",
    "TrainingDataResultTypeDef",
    "TrainingDataTypeDef",
    "UnindexedFaceTypeDef",
    "VideoMetadataTypeDef",
    "CompareFacesResponseTypeDef",
    "CreateCollectionResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateProjectVersionResponseTypeDef",
    "CreateStreamProcessorResponseTypeDef",
    "DeleteCollectionResponseTypeDef",
    "DeleteFacesResponseTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteProjectVersionResponseTypeDef",
    "DescribeCollectionResponseTypeDef",
    "DescribeProjectVersionsResponseTypeDef",
    "DescribeProjectsResponseTypeDef",
    "DescribeStreamProcessorResponseTypeDef",
    "DetectCustomLabelsResponseTypeDef",
    "DetectFacesResponseTypeDef",
    "DetectLabelsResponseTypeDef",
    "DetectModerationLabelsResponseTypeDef",
    "DetectTextFiltersTypeDef",
    "DetectTextResponseTypeDef",
    "GetCelebrityInfoResponseTypeDef",
    "GetCelebrityRecognitionResponseTypeDef",
    "GetContentModerationResponseTypeDef",
    "GetFaceDetectionResponseTypeDef",
    "GetFaceSearchResponseTypeDef",
    "GetLabelDetectionResponseTypeDef",
    "GetPersonTrackingResponseTypeDef",
    "GetSegmentDetectionResponseTypeDef",
    "GetTextDetectionResponseTypeDef",
    "HumanLoopConfigTypeDef",
    "ImageTypeDef",
    "IndexFacesResponseTypeDef",
    "ListCollectionsResponseTypeDef",
    "ListFacesResponseTypeDef",
    "ListStreamProcessorsResponseTypeDef",
    "NotificationChannelTypeDef",
    "PaginatorConfigTypeDef",
    "RecognizeCelebritiesResponseTypeDef",
    "SearchFacesByImageResponseTypeDef",
    "SearchFacesResponseTypeDef",
    "StartCelebrityRecognitionResponseTypeDef",
    "StartContentModerationResponseTypeDef",
    "StartFaceDetectionResponseTypeDef",
    "StartFaceSearchResponseTypeDef",
    "StartLabelDetectionResponseTypeDef",
    "StartPersonTrackingResponseTypeDef",
    "StartProjectVersionResponseTypeDef",
    "StartSegmentDetectionFiltersTypeDef",
    "StartSegmentDetectionResponseTypeDef",
    "StartTextDetectionFiltersTypeDef",
    "StartTextDetectionResponseTypeDef",
    "StopProjectVersionResponseTypeDef",
    "VideoTypeDef",
    "WaiterConfigTypeDef",
)

AgeRangeTypeDef = TypedDict("AgeRangeTypeDef", {"Low": int, "High": int}, total=False)

AssetTypeDef = TypedDict(
    "AssetTypeDef", {"GroundTruthManifest": "GroundTruthManifestTypeDef"}, total=False
)

AudioMetadataTypeDef = TypedDict(
    "AudioMetadataTypeDef",
    {"Codec": str, "DurationMillis": int, "SampleRate": int, "NumberOfChannels": int},
    total=False,
)

BeardTypeDef = TypedDict("BeardTypeDef", {"Value": bool, "Confidence": float}, total=False)

BoundingBoxTypeDef = TypedDict(
    "BoundingBoxTypeDef",
    {"Width": float, "Height": float, "Left": float, "Top": float},
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
    },
    total=False,
)

CelebrityRecognitionTypeDef = TypedDict(
    "CelebrityRecognitionTypeDef",
    {"Timestamp": int, "Celebrity": "CelebrityDetailTypeDef"},
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
    },
    total=False,
)

CompareFacesMatchTypeDef = TypedDict(
    "CompareFacesMatchTypeDef", {"Similarity": float, "Face": "ComparedFaceTypeDef"}, total=False
)

ComparedFaceTypeDef = TypedDict(
    "ComparedFaceTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
        "Confidence": float,
        "Landmarks": List["LandmarkTypeDef"],
        "Pose": "PoseTypeDef",
        "Quality": "ImageQualityTypeDef",
    },
    total=False,
)

ComparedSourceImageFaceTypeDef = TypedDict(
    "ComparedSourceImageFaceTypeDef",
    {"BoundingBox": "BoundingBoxTypeDef", "Confidence": float},
    total=False,
)

ContentModerationDetectionTypeDef = TypedDict(
    "ContentModerationDetectionTypeDef",
    {"Timestamp": int, "ModerationLabel": "ModerationLabelTypeDef"},
    total=False,
)

CustomLabelTypeDef = TypedDict(
    "CustomLabelTypeDef",
    {"Name": str, "Confidence": float, "Geometry": "GeometryTypeDef"},
    total=False,
)

DetectionFilterTypeDef = TypedDict(
    "DetectionFilterTypeDef",
    {"MinConfidence": float, "MinBoundingBoxHeight": float, "MinBoundingBoxWidth": float},
    total=False,
)

EmotionTypeDef = TypedDict(
    "EmotionTypeDef",
    {
        "Type": Literal[
            "HAPPY", "SAD", "ANGRY", "CONFUSED", "DISGUSTED", "SURPRISED", "CALM", "UNKNOWN", "FEAR"
        ],
        "Confidence": float,
    },
    total=False,
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef", {"F1Score": float, "Summary": "SummaryTypeDef"}, total=False
)

EyeOpenTypeDef = TypedDict("EyeOpenTypeDef", {"Value": bool, "Confidence": float}, total=False)

EyeglassesTypeDef = TypedDict(
    "EyeglassesTypeDef", {"Value": bool, "Confidence": float}, total=False
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
    "FaceDetectionTypeDef", {"Timestamp": int, "Face": "FaceDetailTypeDef"}, total=False
)

FaceMatchTypeDef = TypedDict(
    "FaceMatchTypeDef", {"Similarity": float, "Face": "FaceTypeDef"}, total=False
)

FaceRecordTypeDef = TypedDict(
    "FaceRecordTypeDef", {"Face": "FaceTypeDef", "FaceDetail": "FaceDetailTypeDef"}, total=False
)

FaceSearchSettingsTypeDef = TypedDict(
    "FaceSearchSettingsTypeDef", {"CollectionId": str, "FaceMatchThreshold": float}, total=False
)

FaceTypeDef = TypedDict(
    "FaceTypeDef",
    {
        "FaceId": str,
        "BoundingBox": "BoundingBoxTypeDef",
        "ImageId": str,
        "ExternalImageId": str,
        "Confidence": float,
    },
    total=False,
)

GenderTypeDef = TypedDict(
    "GenderTypeDef", {"Value": Literal["Male", "Female"], "Confidence": float}, total=False
)

GeometryTypeDef = TypedDict(
    "GeometryTypeDef",
    {"BoundingBox": "BoundingBoxTypeDef", "Polygon": List["PointTypeDef"]},
    total=False,
)

GroundTruthManifestTypeDef = TypedDict(
    "GroundTruthManifestTypeDef", {"S3Object": "S3ObjectTypeDef"}, total=False
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

HumanLoopDataAttributesTypeDef = TypedDict(
    "HumanLoopDataAttributesTypeDef",
    {
        "ContentClassifiers": List[
            Literal["FreeOfPersonallyIdentifiableInformation", "FreeOfAdultContent"]
        ]
    },
    total=False,
)

ImageQualityTypeDef = TypedDict(
    "ImageQualityTypeDef", {"Brightness": float, "Sharpness": float}, total=False
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef", {"BoundingBox": "BoundingBoxTypeDef", "Confidence": float}, total=False
)

KinesisDataStreamTypeDef = TypedDict("KinesisDataStreamTypeDef", {"Arn": str}, total=False)

KinesisVideoStreamTypeDef = TypedDict("KinesisVideoStreamTypeDef", {"Arn": str}, total=False)

LabelDetectionTypeDef = TypedDict(
    "LabelDetectionTypeDef", {"Timestamp": int, "Label": "LabelTypeDef"}, total=False
)

LabelTypeDef = TypedDict(
    "LabelTypeDef",
    {
        "Name": str,
        "Confidence": float,
        "Instances": List["InstanceTypeDef"],
        "Parents": List["ParentTypeDef"],
    },
    total=False,
)

LandmarkTypeDef = TypedDict(
    "LandmarkTypeDef",
    {
        "Type": Literal[
            "eyeLeft",
            "eyeRight",
            "nose",
            "mouthLeft",
            "mouthRight",
            "leftEyeBrowLeft",
            "leftEyeBrowRight",
            "leftEyeBrowUp",
            "rightEyeBrowLeft",
            "rightEyeBrowRight",
            "rightEyeBrowUp",
            "leftEyeLeft",
            "leftEyeRight",
            "leftEyeUp",
            "leftEyeDown",
            "rightEyeLeft",
            "rightEyeRight",
            "rightEyeUp",
            "rightEyeDown",
            "noseLeft",
            "noseRight",
            "mouthUp",
            "mouthDown",
            "leftPupil",
            "rightPupil",
            "upperJawlineLeft",
            "midJawlineLeft",
            "chinBottom",
            "midJawlineRight",
            "upperJawlineRight",
        ],
        "X": float,
        "Y": float,
    },
    total=False,
)

ModerationLabelTypeDef = TypedDict(
    "ModerationLabelTypeDef", {"Confidence": float, "Name": str, "ParentName": str}, total=False
)

MouthOpenTypeDef = TypedDict("MouthOpenTypeDef", {"Value": bool, "Confidence": float}, total=False)

MustacheTypeDef = TypedDict("MustacheTypeDef", {"Value": bool, "Confidence": float}, total=False)

OutputConfigTypeDef = TypedDict(
    "OutputConfigTypeDef", {"S3Bucket": str, "S3KeyPrefix": str}, total=False
)

ParentTypeDef = TypedDict("ParentTypeDef", {"Name": str}, total=False)

PersonDetailTypeDef = TypedDict(
    "PersonDetailTypeDef",
    {"Index": int, "BoundingBox": "BoundingBoxTypeDef", "Face": "FaceDetailTypeDef"},
    total=False,
)

PersonDetectionTypeDef = TypedDict(
    "PersonDetectionTypeDef", {"Timestamp": int, "Person": "PersonDetailTypeDef"}, total=False
)

PersonMatchTypeDef = TypedDict(
    "PersonMatchTypeDef",
    {"Timestamp": int, "Person": "PersonDetailTypeDef", "FaceMatches": List["FaceMatchTypeDef"]},
    total=False,
)

PointTypeDef = TypedDict("PointTypeDef", {"X": float, "Y": float}, total=False)

PoseTypeDef = TypedDict("PoseTypeDef", {"Roll": float, "Yaw": float, "Pitch": float}, total=False)

ProjectDescriptionTypeDef = TypedDict(
    "ProjectDescriptionTypeDef",
    {
        "ProjectArn": str,
        "CreationTimestamp": datetime,
        "Status": Literal["CREATING", "CREATED", "DELETING"],
    },
    total=False,
)

ProjectVersionDescriptionTypeDef = TypedDict(
    "ProjectVersionDescriptionTypeDef",
    {
        "ProjectVersionArn": str,
        "CreationTimestamp": datetime,
        "MinInferenceUnits": int,
        "Status": Literal[
            "TRAINING_IN_PROGRESS",
            "TRAINING_COMPLETED",
            "TRAINING_FAILED",
            "STARTING",
            "RUNNING",
            "FAILED",
            "STOPPING",
            "STOPPED",
            "DELETING",
        ],
        "StatusMessage": str,
        "BillableTrainingTimeInSeconds": int,
        "TrainingEndTimestamp": datetime,
        "OutputConfig": "OutputConfigTypeDef",
        "TrainingDataResult": "TrainingDataResultTypeDef",
        "TestingDataResult": "TestingDataResultTypeDef",
        "EvaluationResult": "EvaluationResultTypeDef",
    },
    total=False,
)

RegionOfInterestTypeDef = TypedDict(
    "RegionOfInterestTypeDef", {"BoundingBox": "BoundingBoxTypeDef"}, total=False
)

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef", {"Bucket": str, "Name": str, "Version": str}, total=False
)

SegmentDetectionTypeDef = TypedDict(
    "SegmentDetectionTypeDef",
    {
        "Type": Literal["TECHNICAL_CUE", "SHOT"],
        "StartTimestampMillis": int,
        "EndTimestampMillis": int,
        "DurationMillis": int,
        "StartTimecodeSMPTE": str,
        "EndTimecodeSMPTE": str,
        "DurationSMPTE": str,
        "TechnicalCueSegment": "TechnicalCueSegmentTypeDef",
        "ShotSegment": "ShotSegmentTypeDef",
    },
    total=False,
)

SegmentTypeInfoTypeDef = TypedDict(
    "SegmentTypeInfoTypeDef",
    {"Type": Literal["TECHNICAL_CUE", "SHOT"], "ModelVersion": str},
    total=False,
)

ShotSegmentTypeDef = TypedDict(
    "ShotSegmentTypeDef", {"Index": int, "Confidence": float}, total=False
)

SmileTypeDef = TypedDict("SmileTypeDef", {"Value": bool, "Confidence": float}, total=False)

StartShotDetectionFilterTypeDef = TypedDict(
    "StartShotDetectionFilterTypeDef", {"MinSegmentConfidence": float}, total=False
)

StartTechnicalCueDetectionFilterTypeDef = TypedDict(
    "StartTechnicalCueDetectionFilterTypeDef", {"MinSegmentConfidence": float}, total=False
)

StreamProcessorInputTypeDef = TypedDict(
    "StreamProcessorInputTypeDef", {"KinesisVideoStream": "KinesisVideoStreamTypeDef"}, total=False
)

StreamProcessorOutputTypeDef = TypedDict(
    "StreamProcessorOutputTypeDef", {"KinesisDataStream": "KinesisDataStreamTypeDef"}, total=False
)

StreamProcessorSettingsTypeDef = TypedDict(
    "StreamProcessorSettingsTypeDef", {"FaceSearch": "FaceSearchSettingsTypeDef"}, total=False
)

StreamProcessorTypeDef = TypedDict(
    "StreamProcessorTypeDef",
    {"Name": str, "Status": Literal["STOPPED", "STARTING", "RUNNING", "FAILED", "STOPPING"]},
    total=False,
)

SummaryTypeDef = TypedDict("SummaryTypeDef", {"S3Object": "S3ObjectTypeDef"}, total=False)

SunglassesTypeDef = TypedDict(
    "SunglassesTypeDef", {"Value": bool, "Confidence": float}, total=False
)

TechnicalCueSegmentTypeDef = TypedDict(
    "TechnicalCueSegmentTypeDef",
    {"Type": Literal["ColorBars", "EndCredits", "BlackFrames"], "Confidence": float},
    total=False,
)

TestingDataResultTypeDef = TypedDict(
    "TestingDataResultTypeDef",
    {"Input": "TestingDataTypeDef", "Output": "TestingDataTypeDef"},
    total=False,
)

TestingDataTypeDef = TypedDict(
    "TestingDataTypeDef", {"Assets": List["AssetTypeDef"], "AutoCreate": bool}, total=False
)

TextDetectionResultTypeDef = TypedDict(
    "TextDetectionResultTypeDef",
    {"Timestamp": int, "TextDetection": "TextDetectionTypeDef"},
    total=False,
)

TextDetectionTypeDef = TypedDict(
    "TextDetectionTypeDef",
    {
        "DetectedText": str,
        "Type": Literal["LINE", "WORD"],
        "Id": int,
        "ParentId": int,
        "Confidence": float,
        "Geometry": "GeometryTypeDef",
    },
    total=False,
)

TrainingDataResultTypeDef = TypedDict(
    "TrainingDataResultTypeDef",
    {"Input": "TrainingDataTypeDef", "Output": "TrainingDataTypeDef"},
    total=False,
)

TrainingDataTypeDef = TypedDict(
    "TrainingDataTypeDef", {"Assets": List["AssetTypeDef"]}, total=False
)

UnindexedFaceTypeDef = TypedDict(
    "UnindexedFaceTypeDef",
    {
        "Reasons": List[
            Literal[
                "EXCEEDS_MAX_FACES",
                "EXTREME_POSE",
                "LOW_BRIGHTNESS",
                "LOW_SHARPNESS",
                "LOW_CONFIDENCE",
                "SMALL_BOUNDING_BOX",
                "LOW_FACE_QUALITY",
            ]
        ],
        "FaceDetail": "FaceDetailTypeDef",
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
    },
    total=False,
)

CompareFacesResponseTypeDef = TypedDict(
    "CompareFacesResponseTypeDef",
    {
        "SourceImageFace": "ComparedSourceImageFaceTypeDef",
        "FaceMatches": List["CompareFacesMatchTypeDef"],
        "UnmatchedFaces": List["ComparedFaceTypeDef"],
        "SourceImageOrientationCorrection": Literal[
            "ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"
        ],
        "TargetImageOrientationCorrection": Literal[
            "ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"
        ],
    },
    total=False,
)

CreateCollectionResponseTypeDef = TypedDict(
    "CreateCollectionResponseTypeDef",
    {"StatusCode": int, "CollectionArn": str, "FaceModelVersion": str},
    total=False,
)

CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef", {"ProjectArn": str}, total=False
)

CreateProjectVersionResponseTypeDef = TypedDict(
    "CreateProjectVersionResponseTypeDef", {"ProjectVersionArn": str}, total=False
)

CreateStreamProcessorResponseTypeDef = TypedDict(
    "CreateStreamProcessorResponseTypeDef", {"StreamProcessorArn": str}, total=False
)

DeleteCollectionResponseTypeDef = TypedDict(
    "DeleteCollectionResponseTypeDef", {"StatusCode": int}, total=False
)

DeleteFacesResponseTypeDef = TypedDict(
    "DeleteFacesResponseTypeDef", {"DeletedFaces": List[str]}, total=False
)

DeleteProjectResponseTypeDef = TypedDict(
    "DeleteProjectResponseTypeDef",
    {"Status": Literal["CREATING", "CREATED", "DELETING"]},
    total=False,
)

DeleteProjectVersionResponseTypeDef = TypedDict(
    "DeleteProjectVersionResponseTypeDef",
    {
        "Status": Literal[
            "TRAINING_IN_PROGRESS",
            "TRAINING_COMPLETED",
            "TRAINING_FAILED",
            "STARTING",
            "RUNNING",
            "FAILED",
            "STOPPING",
            "STOPPED",
            "DELETING",
        ]
    },
    total=False,
)

DescribeCollectionResponseTypeDef = TypedDict(
    "DescribeCollectionResponseTypeDef",
    {
        "FaceCount": int,
        "FaceModelVersion": str,
        "CollectionARN": str,
        "CreationTimestamp": datetime,
    },
    total=False,
)

DescribeProjectVersionsResponseTypeDef = TypedDict(
    "DescribeProjectVersionsResponseTypeDef",
    {"ProjectVersionDescriptions": List["ProjectVersionDescriptionTypeDef"], "NextToken": str},
    total=False,
)

DescribeProjectsResponseTypeDef = TypedDict(
    "DescribeProjectsResponseTypeDef",
    {"ProjectDescriptions": List["ProjectDescriptionTypeDef"], "NextToken": str},
    total=False,
)

DescribeStreamProcessorResponseTypeDef = TypedDict(
    "DescribeStreamProcessorResponseTypeDef",
    {
        "Name": str,
        "StreamProcessorArn": str,
        "Status": Literal["STOPPED", "STARTING", "RUNNING", "FAILED", "STOPPING"],
        "StatusMessage": str,
        "CreationTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "Input": "StreamProcessorInputTypeDef",
        "Output": "StreamProcessorOutputTypeDef",
        "RoleArn": str,
        "Settings": "StreamProcessorSettingsTypeDef",
    },
    total=False,
)

DetectCustomLabelsResponseTypeDef = TypedDict(
    "DetectCustomLabelsResponseTypeDef", {"CustomLabels": List["CustomLabelTypeDef"]}, total=False
)

DetectFacesResponseTypeDef = TypedDict(
    "DetectFacesResponseTypeDef",
    {
        "FaceDetails": List["FaceDetailTypeDef"],
        "OrientationCorrection": Literal["ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"],
    },
    total=False,
)

DetectLabelsResponseTypeDef = TypedDict(
    "DetectLabelsResponseTypeDef",
    {
        "Labels": List["LabelTypeDef"],
        "OrientationCorrection": Literal["ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"],
        "LabelModelVersion": str,
    },
    total=False,
)

DetectModerationLabelsResponseTypeDef = TypedDict(
    "DetectModerationLabelsResponseTypeDef",
    {
        "ModerationLabels": List["ModerationLabelTypeDef"],
        "ModerationModelVersion": str,
        "HumanLoopActivationOutput": "HumanLoopActivationOutputTypeDef",
    },
    total=False,
)

DetectTextFiltersTypeDef = TypedDict(
    "DetectTextFiltersTypeDef",
    {"WordFilter": "DetectionFilterTypeDef", "RegionsOfInterest": List["RegionOfInterestTypeDef"]},
    total=False,
)

DetectTextResponseTypeDef = TypedDict(
    "DetectTextResponseTypeDef",
    {"TextDetections": List["TextDetectionTypeDef"], "TextModelVersion": str},
    total=False,
)

GetCelebrityInfoResponseTypeDef = TypedDict(
    "GetCelebrityInfoResponseTypeDef", {"Urls": List[str], "Name": str}, total=False
)

GetCelebrityRecognitionResponseTypeDef = TypedDict(
    "GetCelebrityRecognitionResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Celebrities": List["CelebrityRecognitionTypeDef"],
    },
    total=False,
)

GetContentModerationResponseTypeDef = TypedDict(
    "GetContentModerationResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "ModerationLabels": List["ContentModerationDetectionTypeDef"],
        "NextToken": str,
        "ModerationModelVersion": str,
    },
    total=False,
)

GetFaceDetectionResponseTypeDef = TypedDict(
    "GetFaceDetectionResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Faces": List["FaceDetectionTypeDef"],
    },
    total=False,
)

GetFaceSearchResponseTypeDef = TypedDict(
    "GetFaceSearchResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "NextToken": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "Persons": List["PersonMatchTypeDef"],
    },
    total=False,
)

GetLabelDetectionResponseTypeDef = TypedDict(
    "GetLabelDetectionResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Labels": List["LabelDetectionTypeDef"],
        "LabelModelVersion": str,
    },
    total=False,
)

GetPersonTrackingResponseTypeDef = TypedDict(
    "GetPersonTrackingResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "NextToken": str,
        "Persons": List["PersonDetectionTypeDef"],
    },
    total=False,
)

GetSegmentDetectionResponseTypeDef = TypedDict(
    "GetSegmentDetectionResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": List["VideoMetadataTypeDef"],
        "AudioMetadata": List["AudioMetadataTypeDef"],
        "NextToken": str,
        "Segments": List["SegmentDetectionTypeDef"],
        "SelectedSegmentTypes": List["SegmentTypeInfoTypeDef"],
    },
    total=False,
)

GetTextDetectionResponseTypeDef = TypedDict(
    "GetTextDetectionResponseTypeDef",
    {
        "JobStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "StatusMessage": str,
        "VideoMetadata": "VideoMetadataTypeDef",
        "TextDetections": List["TextDetectionResultTypeDef"],
        "NextToken": str,
        "TextModelVersion": str,
    },
    total=False,
)

_RequiredHumanLoopConfigTypeDef = TypedDict(
    "_RequiredHumanLoopConfigTypeDef", {"HumanLoopName": str, "FlowDefinitionArn": str}
)
_OptionalHumanLoopConfigTypeDef = TypedDict(
    "_OptionalHumanLoopConfigTypeDef",
    {"DataAttributes": "HumanLoopDataAttributesTypeDef"},
    total=False,
)


class HumanLoopConfigTypeDef(_RequiredHumanLoopConfigTypeDef, _OptionalHumanLoopConfigTypeDef):
    pass


ImageTypeDef = TypedDict(
    "ImageTypeDef", {"Bytes": bytes, "S3Object": "S3ObjectTypeDef"}, total=False
)

IndexFacesResponseTypeDef = TypedDict(
    "IndexFacesResponseTypeDef",
    {
        "FaceRecords": List["FaceRecordTypeDef"],
        "OrientationCorrection": Literal["ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"],
        "FaceModelVersion": str,
        "UnindexedFaces": List["UnindexedFaceTypeDef"],
    },
    total=False,
)

ListCollectionsResponseTypeDef = TypedDict(
    "ListCollectionsResponseTypeDef",
    {"CollectionIds": List[str], "NextToken": str, "FaceModelVersions": List[str]},
    total=False,
)

ListFacesResponseTypeDef = TypedDict(
    "ListFacesResponseTypeDef",
    {"Faces": List["FaceTypeDef"], "NextToken": str, "FaceModelVersion": str},
    total=False,
)

ListStreamProcessorsResponseTypeDef = TypedDict(
    "ListStreamProcessorsResponseTypeDef",
    {"NextToken": str, "StreamProcessors": List["StreamProcessorTypeDef"]},
    total=False,
)

NotificationChannelTypeDef = TypedDict(
    "NotificationChannelTypeDef", {"SNSTopicArn": str, "RoleArn": str}
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RecognizeCelebritiesResponseTypeDef = TypedDict(
    "RecognizeCelebritiesResponseTypeDef",
    {
        "CelebrityFaces": List["CelebrityTypeDef"],
        "UnrecognizedFaces": List["ComparedFaceTypeDef"],
        "OrientationCorrection": Literal["ROTATE_0", "ROTATE_90", "ROTATE_180", "ROTATE_270"],
    },
    total=False,
)

SearchFacesByImageResponseTypeDef = TypedDict(
    "SearchFacesByImageResponseTypeDef",
    {
        "SearchedFaceBoundingBox": "BoundingBoxTypeDef",
        "SearchedFaceConfidence": float,
        "FaceMatches": List["FaceMatchTypeDef"],
        "FaceModelVersion": str,
    },
    total=False,
)

SearchFacesResponseTypeDef = TypedDict(
    "SearchFacesResponseTypeDef",
    {"SearchedFaceId": str, "FaceMatches": List["FaceMatchTypeDef"], "FaceModelVersion": str},
    total=False,
)

StartCelebrityRecognitionResponseTypeDef = TypedDict(
    "StartCelebrityRecognitionResponseTypeDef", {"JobId": str}, total=False
)

StartContentModerationResponseTypeDef = TypedDict(
    "StartContentModerationResponseTypeDef", {"JobId": str}, total=False
)

StartFaceDetectionResponseTypeDef = TypedDict(
    "StartFaceDetectionResponseTypeDef", {"JobId": str}, total=False
)

StartFaceSearchResponseTypeDef = TypedDict(
    "StartFaceSearchResponseTypeDef", {"JobId": str}, total=False
)

StartLabelDetectionResponseTypeDef = TypedDict(
    "StartLabelDetectionResponseTypeDef", {"JobId": str}, total=False
)

StartPersonTrackingResponseTypeDef = TypedDict(
    "StartPersonTrackingResponseTypeDef", {"JobId": str}, total=False
)

StartProjectVersionResponseTypeDef = TypedDict(
    "StartProjectVersionResponseTypeDef",
    {
        "Status": Literal[
            "TRAINING_IN_PROGRESS",
            "TRAINING_COMPLETED",
            "TRAINING_FAILED",
            "STARTING",
            "RUNNING",
            "FAILED",
            "STOPPING",
            "STOPPED",
            "DELETING",
        ]
    },
    total=False,
)

StartSegmentDetectionFiltersTypeDef = TypedDict(
    "StartSegmentDetectionFiltersTypeDef",
    {
        "TechnicalCueFilter": "StartTechnicalCueDetectionFilterTypeDef",
        "ShotFilter": "StartShotDetectionFilterTypeDef",
    },
    total=False,
)

StartSegmentDetectionResponseTypeDef = TypedDict(
    "StartSegmentDetectionResponseTypeDef", {"JobId": str}, total=False
)

StartTextDetectionFiltersTypeDef = TypedDict(
    "StartTextDetectionFiltersTypeDef",
    {"WordFilter": "DetectionFilterTypeDef", "RegionsOfInterest": List["RegionOfInterestTypeDef"]},
    total=False,
)

StartTextDetectionResponseTypeDef = TypedDict(
    "StartTextDetectionResponseTypeDef", {"JobId": str}, total=False
)

StopProjectVersionResponseTypeDef = TypedDict(
    "StopProjectVersionResponseTypeDef",
    {
        "Status": Literal[
            "TRAINING_IN_PROGRESS",
            "TRAINING_COMPLETED",
            "TRAINING_FAILED",
            "STARTING",
            "RUNNING",
            "FAILED",
            "STOPPING",
            "STOPPED",
            "DELETING",
        ]
    },
    total=False,
)

VideoTypeDef = TypedDict("VideoTypeDef", {"S3Object": "S3ObjectTypeDef"}, total=False)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
