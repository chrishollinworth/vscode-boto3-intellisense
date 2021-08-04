"""
Type annotations for rekognition service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/literals.html)

Usage::

    ```python
    from mypy_boto3_rekognition.literals import AttributeType

    data: AttributeType = "ALL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AttributeType",
    "BodyPartType",
    "CelebrityRecognitionSortByType",
    "ContentClassifierType",
    "ContentModerationSortByType",
    "DescribeProjectVersionsPaginatorName",
    "DescribeProjectsPaginatorName",
    "EmotionNameType",
    "FaceAttributesType",
    "FaceSearchSortByType",
    "GenderTypeType",
    "LabelDetectionSortByType",
    "LandmarkTypeType",
    "ListCollectionsPaginatorName",
    "ListFacesPaginatorName",
    "ListStreamProcessorsPaginatorName",
    "OrientationCorrectionType",
    "PersonTrackingSortByType",
    "ProjectStatusType",
    "ProjectVersionRunningWaiterName",
    "ProjectVersionStatusType",
    "ProjectVersionTrainingCompletedWaiterName",
    "ProtectiveEquipmentTypeType",
    "QualityFilterType",
    "ReasonType",
    "SegmentTypeType",
    "StreamProcessorStatusType",
    "TechnicalCueTypeType",
    "TextTypesType",
    "VideoJobStatusType",
)

AttributeType = Literal["ALL", "DEFAULT"]
BodyPartType = Literal["FACE", "HEAD", "LEFT_HAND", "RIGHT_HAND"]
CelebrityRecognitionSortByType = Literal["ID", "TIMESTAMP"]
ContentClassifierType = Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
ContentModerationSortByType = Literal["NAME", "TIMESTAMP"]
DescribeProjectVersionsPaginatorName = Literal["describe_project_versions"]
DescribeProjectsPaginatorName = Literal["describe_projects"]
EmotionNameType = Literal[
    "ANGRY", "CALM", "CONFUSED", "DISGUSTED", "FEAR", "HAPPY", "SAD", "SURPRISED", "UNKNOWN"
]
FaceAttributesType = Literal["ALL", "DEFAULT"]
FaceSearchSortByType = Literal["INDEX", "TIMESTAMP"]
GenderTypeType = Literal["Female", "Male"]
LabelDetectionSortByType = Literal["NAME", "TIMESTAMP"]
LandmarkTypeType = Literal[
    "chinBottom",
    "eyeLeft",
    "eyeRight",
    "leftEyeBrowLeft",
    "leftEyeBrowRight",
    "leftEyeBrowUp",
    "leftEyeDown",
    "leftEyeLeft",
    "leftEyeRight",
    "leftEyeUp",
    "leftPupil",
    "midJawlineLeft",
    "midJawlineRight",
    "mouthDown",
    "mouthLeft",
    "mouthRight",
    "mouthUp",
    "nose",
    "noseLeft",
    "noseRight",
    "rightEyeBrowLeft",
    "rightEyeBrowRight",
    "rightEyeBrowUp",
    "rightEyeDown",
    "rightEyeLeft",
    "rightEyeRight",
    "rightEyeUp",
    "rightPupil",
    "upperJawlineLeft",
    "upperJawlineRight",
]
ListCollectionsPaginatorName = Literal["list_collections"]
ListFacesPaginatorName = Literal["list_faces"]
ListStreamProcessorsPaginatorName = Literal["list_stream_processors"]
OrientationCorrectionType = Literal["ROTATE_0", "ROTATE_180", "ROTATE_270", "ROTATE_90"]
PersonTrackingSortByType = Literal["INDEX", "TIMESTAMP"]
ProjectStatusType = Literal["CREATED", "CREATING", "DELETING"]
ProjectVersionRunningWaiterName = Literal["project_version_running"]
ProjectVersionStatusType = Literal[
    "DELETING",
    "FAILED",
    "RUNNING",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "TRAINING_COMPLETED",
    "TRAINING_FAILED",
    "TRAINING_IN_PROGRESS",
]
ProjectVersionTrainingCompletedWaiterName = Literal["project_version_training_completed"]
ProtectiveEquipmentTypeType = Literal["FACE_COVER", "HAND_COVER", "HEAD_COVER"]
QualityFilterType = Literal["AUTO", "HIGH", "LOW", "MEDIUM", "NONE"]
ReasonType = Literal[
    "EXCEEDS_MAX_FACES",
    "EXTREME_POSE",
    "LOW_BRIGHTNESS",
    "LOW_CONFIDENCE",
    "LOW_FACE_QUALITY",
    "LOW_SHARPNESS",
    "SMALL_BOUNDING_BOX",
]
SegmentTypeType = Literal["SHOT", "TECHNICAL_CUE"]
StreamProcessorStatusType = Literal["FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING"]
TechnicalCueTypeType = Literal["BlackFrames", "ColorBars", "EndCredits"]
TextTypesType = Literal["LINE", "WORD"]
VideoJobStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
