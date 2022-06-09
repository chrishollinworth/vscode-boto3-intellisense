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
    "DatasetStatusMessageCodeType",
    "DatasetStatusType",
    "DatasetTypeType",
    "DescribeProjectVersionsPaginatorName",
    "DescribeProjectsPaginatorName",
    "EmotionNameType",
    "FaceAttributesType",
    "FaceSearchSortByType",
    "GenderTypeType",
    "KnownGenderTypeType",
    "LabelDetectionSortByType",
    "LandmarkTypeType",
    "ListCollectionsPaginatorName",
    "ListDatasetEntriesPaginatorName",
    "ListDatasetLabelsPaginatorName",
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
    "StreamProcessorParameterToDeleteType",
    "StreamProcessorStatusType",
    "TechnicalCueTypeType",
    "TextTypesType",
    "VideoColorRangeType",
    "VideoJobStatusType",
)

AttributeType = Literal["ALL", "DEFAULT"]
BodyPartType = Literal["FACE", "HEAD", "LEFT_HAND", "RIGHT_HAND"]
CelebrityRecognitionSortByType = Literal["ID", "TIMESTAMP"]
ContentClassifierType = Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
ContentModerationSortByType = Literal["NAME", "TIMESTAMP"]
DatasetStatusMessageCodeType = Literal["CLIENT_ERROR", "SERVICE_ERROR", "SUCCESS"]
DatasetStatusType = Literal[
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
DatasetTypeType = Literal["TEST", "TRAIN"]
DescribeProjectVersionsPaginatorName = Literal["describe_project_versions"]
DescribeProjectsPaginatorName = Literal["describe_projects"]
EmotionNameType = Literal[
    "ANGRY", "CALM", "CONFUSED", "DISGUSTED", "FEAR", "HAPPY", "SAD", "SURPRISED", "UNKNOWN"
]
FaceAttributesType = Literal["ALL", "DEFAULT"]
FaceSearchSortByType = Literal["INDEX", "TIMESTAMP"]
GenderTypeType = Literal["Female", "Male"]
KnownGenderTypeType = Literal["Female", "Male", "Nonbinary", "Unlisted"]
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
ListDatasetEntriesPaginatorName = Literal["list_dataset_entries"]
ListDatasetLabelsPaginatorName = Literal["list_dataset_labels"]
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
StreamProcessorParameterToDeleteType = Literal["ConnectedHomeMinConfidence", "RegionsOfInterest"]
StreamProcessorStatusType = Literal[
    "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "UPDATING"
]
TechnicalCueTypeType = Literal[
    "BlackFrames", "ColorBars", "Content", "EndCredits", "OpeningCredits", "Slate", "StudioLogo"
]
TextTypesType = Literal["LINE", "WORD"]
VideoColorRangeType = Literal["FULL", "LIMITED"]
VideoJobStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
